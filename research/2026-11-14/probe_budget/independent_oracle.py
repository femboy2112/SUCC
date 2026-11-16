"""Independent enumerative oracle for tiny source-probe contracts.

Does not import the new module while evaluating brute policies: uses a
separate budget-decreasing decision-tree implementation. Imports the module
only to compare the resulting verdicts, not as an inference oracle.
"""
from __future__ import annotations
import itertools
import json
import random
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from observational_succ.probe_budget import (Carrier, Probe, minimum_fixed_budget,
                                               minimum_adaptive_budget,
                                               verify_adaptive_solution,
                                               minimum_section_budget)
Q=Fraction


def brute_fixed(c,target):
    ids=[i for i,p in enumerate(c.probes) if p.available and p.is_passive]
    best=None
    for length in range(len(ids)+1):
        for comb in itertools.combinations(ids,length):
            good=True
            for a in range(c.nx):
                for b in range(a+1,c.nx):
                    if c.q[a]!=c.q[b] or target[a]==target[b]:continue
                    if not any(c.probes[i].outputs[a]!=c.probes[i].outputs[b] for i in comb):
                        good=False
            if good:
                cost=sum((Q(c.probes[i].cost) for i in comb),Q(0))
                if best is None or cost<best:best=cost
    return best


def brute_budget_possible(c,target,budget):
    """Direct independent adversarial game with an explicit remaining budget."""
    choices=[p for p in c.probes if p.available]
    @lru_cache(maxsize=None)
    def solves(pairs,remaining):
        if len({target[orig] for orig,cur in pairs})==1:return True
        for p in choices:
            if p.cost>remaining:continue
            outcomes={}
            for original,current in pairs:
                next_current=current if p.updates is None else p.updates[current]
                outcomes.setdefault(p.outputs[current],set()).add((original,next_current))
            if all(solves(tuple(sorted(out)),remaining-Q(p.cost)) for out in outcomes.values()):
                return True
        return False
    return all(solves(tuple((x,x) for x in range(c.nx) if c.q[x]==y),Q(budget))
               for y in range(c.ny))


def random_models(count=320):
    rng=random.Random(20261114)
    fixed_checked=adaptive_checked=negative_traps=0
    adaptive_improvements=0
    for case in range(count):
        n=rng.choice((2,3,4))
        q=tuple(rng.randrange(2) for _ in range(n))
        if set(q)!={0,1}:q=(0,)*n
        t=tuple(rng.randrange(n) for _ in range(n))
        ps=[]
        for i in range(rng.randrange(1,4)):
            outputs=tuple(rng.randrange(2) for _ in range(n))
            is_destructive=rng.randrange(5)==0
            next_states=tuple(rng.randrange(n) for _ in range(n)) if is_destructive else None
            ps.append(Probe(f'r{i}',outputs,Q(rng.randrange(1,4)),next_states,
                            available=bool(rng.randrange(5))))
        c=Carrier(q,(t,),tuple(ps))
        target=tuple(rng.randrange(2) for _ in range(n))
        f=minimum_fixed_budget(c,target)
        b=brute_fixed(c,target)
        assert (None if f is None else f.cost)==b,(case,'fixed',f,b)
        fixed_checked+=1
        a=minimum_adaptive_budget(c,target,max_beliefs=10000)
        assert verify_adaptive_solution(c,a),(case,'certificate')
        v=a.worst_cost
        if v is None:
            negative_traps+=1
            # A negative trap cert also predicts failure for every smaller budget.
            for k in range(0,7):
                assert not brute_budget_possible(c,target,Q(k)),(case,'false impossibility',k)
        elif v<=6:
            expected=next((Q(k) for k in range(7)
                           if brute_budget_possible(c,target,Q(k))),None)
            assert v==expected,(case,'adaptive',v,expected)
            adaptive_checked+=1
        if f is not None and v is not None and v<f.cost:
            adaptive_improvements+=1
    return {'models':count,'fixed_crosschecks':fixed_checked,
            'adaptive_cost_crosschecks_with_budget_le_6':adaptive_checked,
            'certified_impossible_models':negative_traps,
            'strict_adaptive_better_than_fixed':adaptive_improvements}


def main():
    report=random_models()
    # High-value source-compatible example: stochastic and deterministic
    # source reconstruction have distinct exact lawful budgets 2 and 5.
    c=Carrier((0,0,1,1,1,1),((2,3,4,5,5,4),),
              (Probe('middle',(0,0,1,1,0,0),Q(2)),
               Probe('within',(0,1,0,1,0,1),Q(3))))
    sto=minimum_section_budget(c,'stochastic')
    det=minimum_section_budget(c,'point')
    assert (sto.cost,det.cost)==(Q(2),Q(5))
    report['six_state_costs']={'stochastic':'2','deterministic':'5'}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':main()
