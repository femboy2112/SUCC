"""Independent raw-path source oracle for finite J coupling and adapted policy.

Does not import source_authentication.py; builds physical-model branches from a
separate, declared read-old/flip/reset table using exact Fraction arithmetic.
The source program/OS RNG is an empirical object, not independently verified
by this mathematical oracle.
"""
from fractions import Fraction as Q
from itertools import product
from observational_succ.recursive_observer import initial_pairs, run_trace
# NOTE: no source instruments imported from implementation being audited.


def weight(acc, state, action, next_state, observation):
    if action=='sense':
        if next_state!=state:return Q(0)
        return acc if observation==state else Q(1)-acc
    if action=='reset':
        if next_state!=0:return Q(0)
        return acc if observation==state else Q(1)-acc
    if action=='flip':
        return Q(1) if next_state==1-state and observation==0 else Q(0)
    raise ValueError('unlicensed action')


def all_source_paths(acc, events):
    """Directly enumerate ALL original/current paths, not recursive Bayes."""
    candidates=[(u,u,Q(1,2)) for u in (0,1)]
    for action,observation in events:
        next_paths=[]
        for u,x,p in candidates:
            for xp in (0,1):
                z=weight(acc,x,action,xp,observation)
                if z:next_paths.append((u,xp,p*z))
        candidates=next_paths
    total=sum((p for _,_,p in candidates),Q(0))
    if total==0:return Q(0),None
    result=[[Q(0)]*2 for _ in range(2)]
    for u,x,p in candidates:result[u][x]+=p/total
    return total,tuple(tuple(row) for row in result)


def oracle_results(max_depth=4):
    from observational_succ.source_authentication import source_instruments
    actionset=('sense','flip','reset')
    checked=0
    for acc in (Q(3,4),Q(1,2)):
        instruments=source_instruments(acc)
        for depth in range(max_depth+1):
            for actions in product(actionset,repeat=depth):
                alphabets=[(0,) if a=='flip' else (0,1) for a in actions]
                for outputs in product(*alphabets):
                    events=tuple(zip(actions,outputs))
                    raw=all_source_paths(acc,events)
                    adapted=run_trace(initial_pairs((Q(1,2),Q(1,2))),
                                      instruments,tuple((actionset.index(a),o) for a,o in events))
                    if raw!=adapted:
                        raise AssertionError((acc,events,raw,adapted))
                    checked+=1
    return checked


def null_martingale_independent(max_depth=6):
    """Predeclared model P vs null Q; observer policy uses P posterior only."""
    from observational_succ.source_authentication import choose_registered_action
    checked=0
    prob=Q(0)
    e_sum=Q(0)
    def rec(history,alt_paths,null_paths,depth):
        nonlocal checked,prob,e_sum
        if depth==max_depth:
            prob+=null_paths
            e_sum+=alt_paths
            checked+=1
            return
        # Policy only sees action/output transcript; reconstruct P posterior
        # *independently* by direct raw-path enumeration.
        _,joint=all_source_paths(Q(3,4),history)
        current=(sum(joint[u][0] for u in range(2)),sum(joint[u][1] for u in range(2)))
        action=choose_registered_action(depth,current)
        for outcome in ((0,) if action=='flip' else (0,1)):
            expanded=history+((action,outcome),)
            p,_=all_source_paths(Q(3,4),expanded)
            q,_=all_source_paths(Q(1,2),expanded)
            if q:
                rec(expanded,p,q,depth+1)
    rec((),Q(1),Q(1),0)
    assert prob==Q(1) and e_sum==Q(1)
    return checked

if __name__=='__main__':
    n=oracle_results(4)
    m=null_martingale_independent(6)
    print(f'Independent path enumeration: {n} model/outcome/action cases PASS')
    print(f'Independent adaptive null-martingale endpoints: {m} PASS')
