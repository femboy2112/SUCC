"""Independent exact replay via path enumeration and unnormalized policy values.

No call to the source module's Bayes-update or Bellman routines; the module is
only used as the executable object against which these independently derived
raw-path computations are compared. Rational arithmetic throughout.
"""
import itertools
import random
from fractions import Fraction as Q
from observational_succ.recursive_observer import (
    JointInstrument, initial_pairs, run_trace, optimal_bayes_policy,
    contraction_bound, update_current, tv, predictive_partition,
    predictive_span, SourceCostMeter,
)


def direct_trace(prior, instruments, events):
    n=len(prior)
    raw={}
    for original in range(n):
        for path in itertools.product(range(n),repeat=len(events)):
            xs=(original,)+path
            mass=Q(prior[original])
            for t,(action,outcome) in enumerate(events):
                mass*=instruments[action].joint[xs[t]][xs[t+1]][outcome]
            raw[(original,xs[-1])]=raw.get((original,xs[-1]),Q(0))+mass
    z=sum(raw.values(),Q(0))
    if not z:
        return Q(0),None
    return z,tuple(tuple(raw.get((origin,current),Q(0))/z for current in range(n))
                   for origin in range(n))


def raw_action(raw, instrument, outcome):
    n=instrument.n
    out={}
    for (origin,current),mass in raw.items():
        for nxt in range(n):
            key=(origin,nxt)
            out[key]=out.get(key,Q(0))+mass*instrument.joint[current][nxt][outcome]
    return {k:v for k,v in out.items() if v}


def raw_loss(raw, target):
    total=sum(raw.values(),Q(0))
    if total==0:return Q(0)
    labels={}
    for (origin,_),v in raw.items():
        labels[target[origin]]=labels.get(target[origin],Q(0))+v
    return total-max(labels.values())


def raw_policy_bruteforce(raw, instruments, target, remaining, meters=None):
    """Independent unnormalized worst-weight recursive tree enumeration."""
    best=raw_loss(raw,target)
    if not remaining:return best
    scale=sum(raw.values(),Q(0))
    if meters is None: meters=(None,)*len(instruments)
    for idx,ins in enumerate(instruments):
        cost=ins.cost*scale
        if meters[idx] is not None:
            meter=meters[idx]
            for (original,current),mass in raw.items():
                for nxt in range(ins.n):
                    for out in range(ins.output_count):
                        cost+=mass*ins.joint[current][nxt][out]*meter.table[current][nxt][out]
        for outcome in range(ins.output_count):
            branch=raw_action(raw,ins,outcome)
            cost+=raw_policy_bruteforce(branch,instruments,target,remaining-1,meters)
        best=min(best,cost)
    return best


def random_instrument(rng):
    rows=[]
    for _ in range(2):
        amounts=[rng.randint(0,4) for _ in range(4)]
        if not any(amounts):amounts[0]=1
        z=sum(amounts)
        rows.append(((Q(amounts[0],z),Q(amounts[1],z)),
                     (Q(amounts[2],z),Q(amounts[3],z))))
    return JointInstrument(tuple(rows),Q(rng.randint(1,6),20),tag='seeded-oracle')


def main():
    rng=random.Random(20261114)
    transcript_cases=0
    policy_cases=0
    for trial in range(70):
        p=Q(rng.randint(0,8),8)
        prior=(p,1-p)
        instruments=(random_instrument(rng),random_instrument(rng))
        for depth in range(4):
            for actions in itertools.product(range(2),repeat=depth):
                for outcomes in itertools.product(range(2),repeat=depth):
                    events=tuple(zip(actions,outcomes))
                    expected=direct_trace(prior,instruments,events)
                    got=run_trace(initial_pairs(prior),instruments,events)
                    assert got==expected, (trial,events,got,expected)
                    transcript_cases+=1
        expected=raw_policy_bruteforce({(i,i):p for i,p in enumerate(prior) if p},
                                      instruments,(0,1),2)
        actual=optimal_bayes_policy(initial_pairs(prior),instruments,(0,1),2).value
        assert actual==expected,(trial,actual,expected)
        policy_cases+=1
    # A second, metered budget oracle: account for realized path costs by
    # independent raw-path expectation, without calling production meter.
    metered_cases=0
    for trial in range(70):
        p=Q(rng.randint(0,8),8);prior=(p,1-p)
        instruments=(random_instrument(rng),random_instrument(rng))
        meters=[]
        for inst in instruments:
            tbl=tuple(tuple(tuple(Q(rng.randint(0,8),20)
                                  for _ in range(inst.output_count))
                            for _ in range(inst.n)) for _ in range(inst.n))
            meters.append(SourceCostMeter(tbl,'licensed-energy-unit'))
        raw={(i,i):p for i,p in enumerate(prior) if p}
        expected=raw_policy_bruteforce(raw,instruments,(0,1),2,tuple(meters))
        got=optimal_bayes_policy(initial_pairs(prior),instruments,(0,1),2,tuple(meters)).value
        assert got==expected,(trial,got,expected)
        metered_cases+=1

    # Independent predictive-observability oracle. Enumerate source paths
    # explicitly rather than applying source-module Heisenberg closure.
    def word_probability(model,source,actions,outputs):
        n=model[0].n
        total=Q(0)
        for path in itertools.product(range(n),repeat=len(actions)):
            xs=(source,)+path
            w=Q(1)
            for t,(a,o) in enumerate(zip(actions,outputs)):
                w*=model[a].joint[xs[t]][xs[t+1]][o]
            total+=w
        return total

    def random_instrument_three():
        rows=[]
        for _ in range(3):
            weights=[rng.randint(0,5) for _ in range(6)]
            if sum(weights)==0:weights[0]=1
            z=sum(weights)
            rows.append(tuple((Q(weights[2*j],z),Q(weights[2*j+1],z))
                              for j in range(3)))
        return JointInstrument(tuple(rows),Q(1,3),'independently seeded')

    predictive_cases=0
    for trial in range(100):
        instruments=(random_instrument_three(),random_instrument_three())
        groups=predictive_partition(instruments)
        _,depths,stabilized=predictive_span(instruments)
        assert stabilized<=2 and max(depths)<=2
        for x in range(3):
            for y in range(x+1,3):
                equality=True
                for length in range(3):
                    for actions in itertools.product(range(2),repeat=length):
                        for outputs in itertools.product(range(2),repeat=length):
                            if word_probability(instruments,x,actions,outputs)!=word_probability(instruments,y,actions,outputs):
                                equality=False
                closure_equality=any(x in g and y in g for g in groups)
                assert equality==closure_equality,(trial,x,y,equality,groups)
                predictive_cases+=1

    # Validate the declared uniform contraction bound in a complete finite
    # rational grid without importing a bound-proof implementation.
    from observational_succ.recursive_observer import instrument_from_post_likelihood
    law=instrument_from_post_likelihood(((Q(3,5),Q(2,5)),(Q(2,5),Q(3,5))),
         ((Q(2,3),Q(1,3)),(Q(1,3),Q(2,3))))
    bound=contraction_bound(law)
    assert bound==Q(4,5)
    filter_cases=0
    for i in range(21):
        for j in range(21):
            p=(Q(i,20),Q(20-i,20));q=(Q(j,20),Q(20-j,20))
            for y in (0,1):
                z0,b0=update_current(p,law,y)
                z1,b1=update_current(q,law,y)
                assert z0>0 and z1>0
                assert tv(b0,b1)<=bound*tv(p,q)
                filter_cases+=1
    print('INDEPENDENT_ORACLE_PASS',{'traces':transcript_cases,'policies':policy_cases,
                                      'filter_pairs':filter_cases, 'metered_policies':metered_cases,
                                      'predictive_pairs':predictive_cases, 'contraction_bound':str(bound)})

if __name__=='__main__':
    main()
