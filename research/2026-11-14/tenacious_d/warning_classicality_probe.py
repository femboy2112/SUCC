"""Exact finite controls for the warning and classicality chapter (stdlib only)."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
import json


def winning(initial, deadline, terminal, operations):
    """A bounded guarantee on joined (original source, current state) pairs.

    operations[t] yields (name, positive duration, transition). Transition
    returns None if illegal or a nonempty tuple of (report, next_state).
    terminal(t,s,x) supplies commands that are safe and complete by deadline.
    """
    if not initial or deadline < 0:
        raise ValueError("Need a nonempty prior and a nonnegative finite deadline")

    @lru_cache(None)
    def solve(t, pairs):
        safe = set.intersection(*(set(terminal(t, s, x)) for s, x in pairs))
        if safe:
            return ('act', sorted(safe, key=repr)[0])
        for name, duration, transition in operations.get(t, ()):
            if type(duration) is not int or duration < 1:
                raise ValueError("Preterminal durations must be positive integers")
            if t + duration > deadline:
                continue
            nexts = defaultdict(set)
            for s, x in pairs:
                successors = transition(s, x)
                if successors is None:
                    break
                if not successors:
                    raise ValueError("Legal transition lacks a successor")
                for observation, new in successors:
                    nexts[observation].add((s, new))
            else:
                continuations = {o: solve(t + duration, frozenset(b))
                                 for o, b in nexts.items()}
                if all(result is not None for result in continuations.values()):
                    return (name, continuations)
        return None

    return solve(0, frozenset(initial))


def run_deadline():
    initial = [(s, 'ready') for s in (0, 1)]
    def safe(latency):
        return lambda t, s, x: {s} if x == 'ready' and t + latency <= 2 else set()
    def probe(_, s, destructive=False):
        return ((s, 'spent' if destructive else 'ready'),)
    read = {0: [('read', 1, lambda s, x: probe(x, s))]}
    winning_policy = winning(initial, 2, safe(1), read)
    assert winning_policy == ('read', {0: ('act', 0), 1: ('act', 1)})
    assert winning(initial, 2, safe(2), read) is None
    assert winning(initial, 2, safe(1), {0: [('read', 1, lambda s,x: probe(x,s,True))]}) is None
    assert winning(initial, 0, lambda t,s,x: {'neutralize'}, {}) == ('act','neutralize')
    triple = [{0,1},{1,2},{2,0}]
    assert all(a & b for a,b in combinations(triple,2)) and not set.intersection(*triple)
    assert winning([(s,0) for s in range(3)],0,lambda t,s,x:triple[s],{}) is None
    # Exhaust all 8^3 action-set tables on three worlds. Independent selector enumeration.
    cases = 0
    for masks in product(range(8),repeat=3):
        accepted = winning([(s,0) for s in range(3)],0,
                           lambda t,s,x:{k for k in range(3) if masks[s] & (1 << k)}, {})
        direct = any(all(mask & (1 << k) for mask in masks) for k in range(3))
        assert (accepted is not None) == direct
        cases += 1
    # Four conflicting original actions. Two nondestructive bits suffice, one never does.
    pairs=[(s,s) for s in range(4)]
    reads=[('bit'+str(j),1,lambda s,x,j=j:(((x>>j)&1,x),)) for j in (0,1)]
    terminal=lambda t,s,x:{s}
    assert winning(pairs,2,terminal,{0:reads,1:reads}) is not None
    assert winning(pairs,1,terminal,{0:reads}) is None
    destructive=[('bit'+str(j),1,lambda s,x,j=j:(((x>>j)&1,0),)) for j in (0,1)]
    assert winning(pairs,2,terminal,{0:destructive,1:reads}) is None
    aligned=[(0,0),(1,1)]
    cartesian=list(product((0,1),repeat=2))
    assert winning(aligned,0,lambda t,s,x:{'wait'} if s==x else set(),{})
    assert winning(cartesian,0,lambda t,s,x:{'wait'} if s==x else set(),{}) is None
    # Feedback routed via the controller. Graph-time ordering is visible in these traces.
    def feedback(bit, activate):
        h,s,a,y=bit,0,0,0
        trace=[y]
        for _ in range(3):
            h,s,a,y=0,h,s if activate else 0,a
            trace.append(y)
        return trace
    assert feedback(0,True)==feedback(1,False)==[0,0,0,0]
    assert feedback(1,True)==[0,0,0,1]
    # Passive shift: C=e2^T, F=e3^T. Repeat with wrong actuator or late pulse.
    linear_cases=0
    for h in {Q(i,j) for i in range(-9,10) for j in range(1,5)}:
        for actuator,arrival,observer in product((1,2),(2,3),(1,2)):
            z=[h,Q(0),Q(0)]
            y_seen=[z[observer]]
            z=[Q(0),z[0],z[1]]
            y_seen.append(z[observer])
            command=-y_seen[-1]
            z=[Q(0),z[0],z[1]]
            if arrival==2:
                z[actuator]+=command
            expected=0 if actuator==2 and arrival==2 and observer==1 else h
            assert z[-1]==expected
            linear_cases+=1
    return {"joined_safe_sets_exhausted":cases,"positive_latency_policy":winning_policy,
            "linear_shift_cases":linear_cases,"control_modes_passed":10}


SIGNS = tuple(product((-1,1),repeat=2))


def initial_hidden(x,z,affine):
    return tuple((1+u*x+v*z if affine else (1+u*x)*(1+v*z))/4 for u,v in SIGNS)


def classical_step(p,action,outcome):
    q = [Q(0)]*4
    for i,(u,v) in enumerate(SIGNS):
        if action=='X': q[SIGNS.index((u,-v))]+=p[i]
        elif action=='H': q[SIGNS.index((v,u))]+=p[i]
        elif v==outcome:
            for refreshed in (-1,1): q[SIGNS.index((refreshed,v))]+=p[i]/2
    return tuple(q)


def quantum_step(rho,action,outcome):
    # rho=(a,b,d) abbreviates real symmetric unnormalized [[a,b],[b,d]].
    a,b,d=rho
    if action=='X': return (d,b,a)
    if action=='H': return ((a+d+2*b)/2,(a-d)/2,(a+d-2*b)/2)
    return (a,Q(0),Q(0)) if outcome==1 else (Q(0),Q(0),d)


def run_quantum():
    counters=defaultdict(int)
    values=[Q(j,4) for j in range(-4,5)]
    preparations={(x,z) for x,z in product(values,repeat=2) if x*x+z*z<=1}
    preparations.update({(Q(3,5),Q(4,5)),(-Q(3,5),Q(4,5))})
    for x,z in sorted(preparations):
        for affine in (False,True):
            if affine and abs(x)+abs(z)>1: continue
            p=initial_hidden(x,z,affine)
            assert min(p)>=0 and sum(p)==1
            rho=((1+z)/2,x/2,(1-z)/2)
            branches=[(p,rho)]
            for _ in range(4):
                nxt=[]
                for p,rho in branches:
                    for action,outcome in [('X',None),('H',None),('Z',-1),('Z',1)]:
                        pp=classical_step(p,action,outcome)
                        rr=quantum_step(rho,action,outcome)
                        a,b,d=rr
                        assert (sum(pp),sum(u*v0 for (u,v),v0 in zip(SIGNS,pp)),
                                sum(v*v0 for (u,v),v0 in zip(SIGNS,pp)))==(a+d,2*b,a-d)
                        counters['affine_branch_comparisons' if affine else 'nonlinear_branch_comparisons']+=1
                        nxt.append((pp,rr))
                branches=nxt
    def twice_area(a,b,c):
        return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
    assert max(twice_area(*t) for t in combinations(SIGNS,3))==4
    x,z=Q(3,5),Q(4,5)
    assert x*x+z*z==1 and initial_hidden(x,z,True)[0]==Q(-1,10)
    assert min(initial_hidden(x,z,False))>=0
    # Rational bracketing controls for the noisy joint-effect form
    # G=(I+r(uX+vZ))/4, positive iff (1-2r^2)/16 >=0.
    assert (1-2*Q(7,10)**2)/16==Q(1,800)
    assert (1-2*Q(5,7)**2)/16==-Q(1,784)
    return {**counters,"distinct_rational_real_preparations":len(preparations),
            "affine_forced_negative_mass":"-1/10","noisy_effect_positive_determinant":"1/800",
            "noisy_effect_negative_determinant":"-1/784"}


if __name__=='__main__':
    print(json.dumps({"status":"EXACT_DECLARED_MODEL_CONTROLS", "deadline":run_deadline(),
                      "quantum":run_quantum()}, sort_keys=True))
