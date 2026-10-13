"""Tiny exact A06 crucible; pair reachability is independent of refinement.

Run from this worktree: python research/2026-10-13/SWARM_ATLAS/A06_probe.py
Only finite integer tables, at most three states, and standard-library modules.
The stdout JSON is the receipt; no production or archival file is modified.
"""
from __future__ import annotations

from collections import deque
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path
import json
import subprocess
import sys
import types


ROOT = Path(__file__).resolve().parents[3]
PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def load_local(name, relative):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# Bypass package __init__: load only the two inspected targets and their tiny
# source-error dependency. This is an isolated import, not a runtime edit.
package = types.ModuleType("a06_local")
package.__path__ = [str(ROOT / "observational_succ")]
sys.modules[package.__name__] = package
load_local("a06_local.causal_nerode_succ", "observational_succ/causal_nerode_succ.py")
CR = load_local("a06_local.categorical_repair_synthesis",
                "observational_succ/categorical_repair_synthesis.py")
NP = load_local("a06_local.nerode_probe_growth",
                "observational_succ/nerode_probe_growth.py")


def equivalences(n):
    """Enumerate each partition once by restricted-growth labels."""
    def visit(labels):
        if len(labels) == n:
            yield frozenset((i, j) for i in range(n) for j in range(n)
                            if labels[i] == labels[j])
            return
        for label in range(max(labels) + 2):
            yield from visit(labels + (label,))
    return tuple(visit((0,)))


def kernel(outputs):
    return frozenset((i, j) for i in range(len(outputs))
                     for j in range(len(outputs)) if outputs[i] == outputs[j])


def stable(relation, actions):
    return all((action[i], action[j]) in relation
               for i, j in relation for action in actions)


def repair(relation, actions):
    """Reach every finite word in the product-state graph, without refinement."""
    answer = set()
    for pair in relation:
        queue, seen, safe = deque([pair]), {pair}, True
        while queue:
            i, j = queue.popleft()
            if (i, j) not in relation:
                safe = False
                break
            for action in actions:
                nxt = action[i], action[j]
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        if safe:
            answer.add(pair)
    return frozenset(answer)


def pullback(relation, mapping):
    return frozenset((i, j) for i in range(len(mapping))
                     for j in range(len(mapping))
                     if (mapping[i], mapping[j]) in relation)


def relation_from_blocks(blocks):
    return frozenset((i, j) for block in blocks for i in block for j in block)


def lawful(source, target, mapping):
    qs, us = source
    qt, ut = target
    return (all(qs[i] == qt[mapping[i]] for i in range(len(qs)))
            and all(mapping[us[i]] == ut[mapping[i]]
                    for i in range(len(qs))))


counts = dict(moore_sources=0, seed_relations=0, adjunction_biconditionals=0,
              mealy_sources=0, native_quotient_comparisons=0,
              native_universal_factor_checks=0,
              lawful_source_maps=0, pullback_naturality_checks=0,
              machine_reflector_hom_bijections=0)
small_sources = []
for n in range(1, 4):
    parts = equivalences(n)
    for outputs in product(range(2), repeat=n):
        Q = kernel(outputs)
        seeds = tuple(E for E in parts if E <= Q)
        for action in product(range(n), repeat=n):
            actions = (action,)
            congruences = tuple(C for C in seeds if stable(C, actions))
            counts["moore_sources"] += 1
            for E in seeds:
                R = repair(E, actions)
                assert R in congruences and R <= E
                assert repair(R, actions) == R
                for C in congruences:
                    assert (C <= E) == (C <= R)
                    counts["adjunction_biconditionals"] += 1
                for F in seeds:
                    if E <= F:
                        assert R <= repair(F, actions)
                counts["seed_relations"] += 1
            # Inclusion has a LEFT adjoint exactly when its ambient top is stable.
            every_seed_has_upper_congruence = all(
                any(E <= C for C in congruences) for E in seeds)
            assert every_seed_has_upper_congruence == stable(Q, actions)
            if stable(Q, actions):
                for E in seeds:
                    closure = frozenset.intersection(
                        *(C for C in congruences if E <= C))
                    assert closure in congruences and E <= closure
                    for C in congruences:
                        assert (closure <= C) == (E <= C)
            expected = repair(Q, actions)
            mealy = CR.FiniteMealy(("a",), (outputs,), (action,))
            actual = CR.minimal_behavioral_quotient(mealy)
            assert relation_from_blocks(actual.blocks) == expected
            for E in seeds:
                labels = tuple(min(j for j in range(n) if (i, j) in E)
                               for i in range(n))
                factor = CR.universal_observer_factor(mealy, labels)
                assert factor["commutes"] == stable(E, actions)
                if factor["commutes"]:
                    h = dict(factor["universal_factor"])
                    assert all(h[labels[i]] == actual.block_of(i)
                               for i in range(n))
                counts["native_universal_factor_checks"] += 1
            states = tuple(map(str, range(n)))
            source = NP.ObserverDynamics("A06", 0, "binary", states,
                tuple(states[i] for i in action), tuple(map(str, outputs)), "a")
            nr = NP.nerode_fixpoint(source)
            nr_blocks = tuple(tuple(map(int, b)) for b in nr.stable_classes)
            assert relation_from_blocks(nr_blocks) == expected
            counts["native_quotient_comparisons"] += 2
            if n <= 2:
                small_sources.append((outputs, action))

# A genuinely branching alphabet: ALL 256 two-state/two-action binary Mealy
# tables. State reports here are pairs of immediate action outputs.
for rows in product(tuple(product(range(2), repeat=2)), repeat=4):
    outputs, transitions = rows[:2], rows[2:]
    Q = kernel(tuple(zip(*outputs)))
    expected = repair(Q, transitions)
    actual = CR.minimal_behavioral_quotient(
        CR.FiniteMealy(("left", "right"), outputs, transitions))
    assert relation_from_blocks(actual.blocks) == expected
    counts["mealy_sources"] += 1
    counts["native_quotient_comparisons"] += 1

# ALL lawful one-action maps among binary sources of cardinality <= 2.
for source in small_sources:
    qs, us = source
    for target in small_sources:
        qt, ut = target
        B = repair(kernel(qs), (us,))
        for mapping in product(range(len(qt)), repeat=len(qs)):
            if not lawful(source, target, mapping):
                continue
            counts["lawful_source_maps"] += 1
            for E in equivalences(len(qt)):
                if E <= kernel(qt):
                    assert repair(pullback(E, mapping), (us,)) == pullback(
                        repair(E, (ut,)), mapping)
                    counts["pullback_naturality_checks"] += 1
            # Every map to a simple target factors uniquely through S/B.
            if repair(kernel(qt), (ut,)) == kernel(tuple(range(len(qt)))):
                blocks = tuple(sorted({tuple(j for j in range(len(qs))
                    if (i, j) in B) for i in range(len(qs))}))
                block_of = {i: b for b, block in enumerate(blocks) for i in block}
                factors = tuple(h for h in product(range(len(qt)), repeat=len(blocks))
                    if all(h[block_of[i]] == mapping[i] for i in range(len(qs))))
                assert len(factors) == 1
                h = factors[0]
                assert all(qt[h[b]] == qs[block[0]]
                    and h[block_of[us[block[0]]]] == ut[h[b]]
                    for b, block in enumerate(blocks))
                counts["machine_reflector_hom_bijections"] += 1

# Smallest observation-preserving cross-source failure: cardinalities (2,3).
source = ((0, 0), (0, 1))
target = ((0, 0, 1), (0, 2, 2))
mapping = (0, 1)
Q = kernel(target[0])
left = repair(pullback(Q, mapping), (source[1],))
right = pullback(repair(Q, (target[1],)), mapping)
assert not lawful(source, target, mapping)
assert (0, 1) in left and (0, 1) not in right
assert all(target[0][mapping[i]] == source[0][i] for i in range(2))
assert mapping[source[1][1]] == 1 and target[1][mapping[1]] == 2
assert all(not (Q <= C) for C in equivalences(3)
           if C <= Q and stable(C, (target[1],)))
assert repair(Q, ((0, 1, 2),)) == Q
assert repair(Q, (target[1],)) == kernel((0, 1, 2))
# Calibration: the coarser report alone is rejected as an action-stable repair.
assert not stable(Q, (target[1],))
# Restore commutation on the target; a non-surjective map now passes.
lawful_target = (target[0], (0, 1, 2))
assert lawful(source, lawful_target, mapping)
assert repair(pullback(Q, mapping), (source[1],)) == pullback(
    repair(Q, (lawful_target[1],)), mapping)

paths = ["observational_succ/categorical_repair_synthesis.py",
         "observational_succ/nerode_probe_growth.py",
         "observational_succ/causal_nerode_succ.py",
         "provenance/IMPORT_MANIFEST.json",
         str(Path(__file__).relative_to(ROOT))]
receipt = {
    "schema": "SWM-A06-exact-v1", "parent_sha": PARENT,
    "git_head_at_run": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
    "python": sys.version.split()[0], "status": "TESTED MODEL",
    "command": "python research/2026-10-13/SWARM_ATLAS/A06_probe.py",
    "successful_completion_exit_code": 0,
    "arithmetic": "finite integer equality; no floating point",
    "counts": counts, "all_assertions_passed": True,
    "cross_source_counterexample": {
        "source": {"reports": source[0], "update": source[1]},
        "target": {"reports": target[0], "update": target[1]},
        "observation_preserving_map": mapping,
        "offending_state": 1, "f_after_source_action": 1,
        "target_action_after_f": 2, "witness_pair": [0, 1],
        "left_repairs_pullback": sorted(left),
        "right_pullbacks_repair": sorted(right),
        "quotient_descent": "REFUTED for observation-preserving maps alone",
    },
    "same_carrier_incompatible_minima": {
        "reports": target[0], "identity_updates_repair": sorted(Q),
        "split_updates_repair": sorted(repair(Q, (target[1],))),
    },
    "mutations_rejected": ["drop future-word closure", "drop action commutation"],
    "positive_control": "non-surjective lawful map restores pullback equality",
    "sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
    "boundary": "finite source contracts; paper proofs supply universal claims; no CI or physical attestation",
}
print(json.dumps(receipt, indent=2, sort_keys=True))
