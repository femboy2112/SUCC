"""Independent finite minimax navigation and Hamming decoding source oracle.

Algorithmically distinct from native reachable-belief attractor: brute-force
all AND/OR action-depth combinations with memoized source replay, plus direct
per-original execution of the claimed policy. No RH/physical claim.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations
from random import Random
from math import inf
from observational_succ.principia_causal_memory import carrier, initial_memory
from observational_succ.principia_reorientation import (
    ReorientationTask, solve, verify_policy, ring_with_beacon,
    ring_with_unknown_heading, reorient_from_anywhere,
)
from observational_succ.principia_reorientation_code import (
    make_local_code, hamming, decode_with_bounded_errors,
)

rng=Random(20261124)
count=0
for case in range(100):
    n=2+rng.randrange(3)
    states=tuple(f'q{i}' for i in range(n))
    actions=('a','b')
    outputs=tuple(str(rng.randrange(2)) for _ in states)
    transitions=tuple(tuple(rng.choice(states) for _ in states) for _ in actions)
    positions=tuple(f'label{rng.randrange(n)}' for _ in states)
    base=carrier(f'fresh-navigation-{case}',states,states,actions,states,outputs,
                 states,transitions)
    task=ReorientationTask(base,positions,'initial' if case%2 else 'current')
    possible_values={w:q for w,q in zip(base.worlds,base.origins)}

    def actual_label(w,q):
        s=possible_values[w] if task.mode=='initial' else q
        return positions[states.index(s)]

    @lru_cache(maxsize=None)
    def brute(belief,depth):
        if len({actual_label(w,q) for w,q in belief})==1:
            return True
        if not depth:return False
        for index,a in enumerate(actions):
            groups={}
            for w,q in belief:
                nxt=transitions[index][states.index(q)]
                groups.setdefault(outputs[states.index(nxt)],[]).append((w,nxt))
            if all(brute(tuple(group),depth-1) for group in groups.values()):
                return True
        return False

    for observed in sorted(set(outputs)):
        memory=initial_memory(base,observed)
        cert=solve(task,memory)
        # Finitely many belief configurations exist. The native certificate
        # discloses how many appeared on the root's reachable graph.
        maximum=cert.reachable_beliefs
        earliest=next((d for d in range(maximum+1)
                       if brute(memory.coupling,d)),None)
        assert cert.rank==earliest,(case,observed,earliest,cert.rank)
        if cert.rank is not None:
            assert verify_policy(task,memory,cert)==cert.rank
            # Independently run every true original world through the policy.
            for world,state in memory.coupling:
                current=state
                node=cert.policy
                t=0
                while node.action is not None:
                    nxt=transitions[actions.index(node.action)][states.index(current)]
                    y=outputs[states.index(nxt)]
                    current=nxt
                    node=dict(node.branches)[y]
                    t+=1
                assert node.answer==actual_label(world,current)
                assert t<=cert.rank
        count+=1
print('INDEPENDENT_REORIENTATION_MINIMAX_PASS',count,'observed-source cases')

# Separate code-theoretic oracle: brute expected beacon traces without using
# Principia make_local_code's transition simulator.
checks=0
for n in (4,5,6,7,9):
    t=ring_with_beacon(n)
    for laps in (1,2,3,4):
        word=('forward',)*(n*laps)
        code=make_local_code(t,word)
        direct=[]
        for initial in range(n):
            outputs=('beacon' if initial==0 else 'dark',)+tuple(
                'beacon' if (initial+j)%n==0 else 'dark' for j in range(1,n*laps+1))
            direct.append((f'x{initial}',f'x{(initial+n*laps)%n}',outputs))
        assert tuple(direct)==code.signatures
        actual=min(hamming(a[2],b[2]) for a,b in combinations(direct,2))
        assert actual==code.min_target_distance
        assert actual>=2*laps
        checks+=1
print('INDEPENDENT_BEACON_ERROR_DISTANCE_PASS',checks,'all-source code models')

# A worst-case one-error exact decoder test, including the first observation.
for n in (4,5,6):
    task=ring_with_beacon(n)
    code=make_local_code(task,('forward',)*(2*n))
    for _,target,report in code.signatures:
        for k in range(len(report)):
            changed=list(report)
            changed[k]='dark' if report[k]=='beacon' else 'beacon'
            assert decode_with_bounded_errors(task,code,changed,1)==target
print('INDEPENDENT_ONE_ERROR_DECODER_PASS')
