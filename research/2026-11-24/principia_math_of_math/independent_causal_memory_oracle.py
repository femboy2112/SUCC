"""Independent brute-force finite semantics oracle for Principia causal memory.

It enumerates ALL action words of length <= #reachable_marked_states-1 for
small held-out source carriers. This is intentionally NOT the native Moore
partition-refinement algorithm or the pair-saturation verifier.
"""
from itertools import product
from random import Random
from observational_succ.principia_causal_memory import (
    carrier, future_quotient, verify_future_quotient,
    reachable_atoms, initial_memory, step_memory,
    verify_memory, find_target_policy, verify_target_policy,
)

rng = Random(20261124)
count = 0
for trial in range(84):
    nw = 2 + rng.randrange(2)
    ns = 2 + rng.randrange(2)
    worlds = tuple(f'w{j}' for j in range(nw))
    states = tuple(f'q{k}' for k in range(ns))
    actions = ('a', 'b')
    origins = tuple(rng.choice(states) for _ in worlds)
    outputs = tuple(str(rng.randrange(2)) for _ in states)
    targets = tuple(str(rng.randrange(2)) for _ in worlds)
    transitions = tuple(tuple(rng.choice(states) for _ in states) for _ in actions)
    c = carrier(f'independent-model-{trial}', worlds, states, actions,
                origins, outputs, targets, transitions)
    q = future_quotient(c)
    verify_future_quotient(c, q)
    atoms = reachable_atoms(c)
    si = {s:i for i,s in enumerate(states)}
    wi = {w:i for i,w in enumerate(worlds)}
    ai = {a:i for i,a in enumerate(actions)}
    # This is a brute-force semantic signature, not partition refinement.
    words = [word for n in range(len(atoms)) for word in product(actions,repeat=n)]
    signature = []
    for world,state in atoms:
        report = [targets[wi[world]]]
        for word in words:
            current = state
            for a in word:
                current = transitions[ai[a]][si[current]]
            report.append(outputs[si[current]])
        signature.append(tuple(report))
    for i in range(len(atoms)):
        for j in range(i+1,len(atoms)):
            assert (signature[i] == signature[j]) == (q.colors[i] == q.colors[j]), (trial,i,j)
    # Separately check the actual-memory update against a naive world replay.
    actual_world = rng.randrange(nw)
    start = outputs[si[origins[actual_world]]]
    m = initial_memory(c,start)
    current = origins[actual_world]
    history = ()
    for _ in range(4):
        act = rng.choice(actions)
        current = transitions[ai[act]][si[current]]
        seen = outputs[si[current]]
        history += ((act,seen),)
        m = step_memory(c,m,act,seen)
        direct=[]
        for w,q0 in zip(worlds,origins):
            s=q0
            if outputs[si[s]]!=start:
                continue
            for a,y in history:
                s=transitions[ai[a]][si[s]]
                if outputs[si[s]]!=y:
                    break
            else:
                direct.append((w,s))
        assert m.coupling == tuple(direct),(trial,m.coupling,direct)
        assert verify_memory(c,m) == tuple(direct)
    # Independently enforce any synthesized policy's source truth contract.
    m = initial_memory(c,start)
    tree = find_target_policy(c,m,depth=3)
    if tree is not None:
        assert verify_target_policy(c,m,tree,max_depth=3)<=3
    count += 1

print('CAUSAL_MEMORY_INDEPENDENT_BRUTE_FORCE_PASS',count,'fresh carriers, all <=N-1 words')
