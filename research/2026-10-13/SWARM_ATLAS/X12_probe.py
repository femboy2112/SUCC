#!/usr/bin/env python3
"""Bounded, independent exact probe for action-stable feasible complexes.

Only standard-library code. Limits are 25 wall seconds, 20 CPU seconds and
256 MiB address space. No source-table inference or empirical claim occurs.
"""
from collections import deque
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
from random import Random
import resource
import signal
import subprocess

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
signal.alarm(25)
ROOT = Path(__file__).resolve().parents[3]
ATLAS = ROOT / "research/2026-10-13/SWARM_ATLAS"
CONSULTED = Path("/home/leah/succ_lab/many-worlds-atlas/research/2026-10-13")
PARENT = "dc23cf405fa432b717ca84018ab86d78ef08edde"


def subsets(n):
    return tuple(frozenset(i for i in range(n) if mask >> i & 1)
                 for mask in range(1, 1 << n))


def enabled(action, face):
    return all(action[x] is not None for x in face)


def image(action, face):
    assert enabled(action, face)
    return frozenset(action[x] for x in face)


def scalar_base(n, q, target, epsilon, actions, guard=True):
    answer = set()
    centers = tuple(Q(k, 2) for k in range(5))
    for face in subsets(n):
        geometric = any(all(abs(Q(target[x]) - center) <= epsilon for x in face)
                        for center in centers)
        pair_radius = (max(target[x] for x in face) - min(target[x] for x in face)) / Q(2)
        assert geometric == (pair_radius <= epsilon)
        homogeneous = all(len({action[x] is not None for x in face}) == 1 for action in actions)
        if geometric and len({q[x] for x in face}) == 1 and (homogeneous or not guard):
            answer.add(face)
    return answer


def repair(base, actions):
    current = set(base)
    rounds = 0
    while True:
        next_family = {face for face in current
                       if all(not enabled(a, face) or image(a, face) in current for a in actions)}
        if next_family == current:
            return current, rounds
        assert next_family < current
        current = next_family
        rounds += 1
        assert rounds <= len(base)


def path_oracle(start, base, actions):
    """Independent face-graph reachability, returning a shortest bad word."""
    queue = deque([(start, ())])
    seen = {start}
    while queue:
        face, word = queue.popleft()
        if face not in base:
            return False, word
        for j, action in enumerate(actions):
            if enabled(action, face):
                child = image(action, face)
                if child not in seen:
                    seen.add(child)
                    queue.append((child, word + (j,)))
    return True, None


def audit(n, q, target, epsilon, actions):
    base = scalar_base(n, q, target, epsilon, actions)
    kernel, rounds = repair(base, actions)
    assert rounds <= len(base) - n
    longest = 0
    for face in subsets(n):
        good, witness = path_oracle(face, base, actions)
        assert good == (face in kernel)
        if witness is not None:
            longest = max(longest, len(witness))
            assert len(witness) <= len(base) - n
        if face in kernel:
            assert all(sub in kernel for sub in subsets(n) if sub <= face)
    return len(subsets(n)), rounds, longest


def facets(family):
    return tuple(sorted((face for face in family if not any(face < other for other in family)),
                        key=lambda face: tuple(sorted(face))))


def printable(family):
    return [sorted(face) for face in sorted(family, key=lambda face: (len(face), tuple(sorted(face))))]


def main():
    comparisons = models = largest_round = longest_word = 0
    for n in (1, 2, 3):
        reports = tuple(product(range(2), repeat=n)) if n <= 2 else ((0, 0, 0), (0, 0, 1))
        for action in product((None,) + tuple(range(n)), repeat=n):
            for target in product(range(3), repeat=n):
                for q in reports:
                    for epsilon in (Q(0), Q(1, 2), Q(1)):
                        count, rounds, longest = audit(n, q, target, epsilon, (action,))
                        models += 1; comparisons += count
                        largest_round = max(largest_round, rounds)
                        longest_word = max(longest_word, longest)
    rng = Random(12004629)
    for _ in range(64):
        actions = tuple(tuple(rng.choice((None, 0, 1, 2, 3)) for _ in range(4)) for _ in range(2))
        q = tuple(rng.randrange(2) for _ in range(4))
        target = tuple(rng.randrange(3) for _ in range(4))
        count, rounds, longest = audit(4, q, target, Q(1, 2), actions)
        models += 1; comparisons += count
        largest_round = max(largest_round, rounds); longest_word = max(longest_word, longest)

    # Exact source-map naturality on every lawful two-to-three-state map.
    lawful = 0
    for f in product(range(3), repeat=2):
        for sa in product((None, 0, 1), repeat=2):
            for ta in product((None, 0, 1, 2), repeat=3):
                if any((sa[x] is None) != (ta[f[x]] is None) for x in range(2)):
                    continue
                if any(sa[x] is not None and f[sa[x]] != ta[f[x]] for x in range(2)):
                    continue
                source_base = scalar_base(2, (0, 0), tuple(f), Q(1, 2), (sa,))
                target_base = scalar_base(3, (0, 0, 0), (0, 1, 2), Q(1, 2), (ta,))
                source_kernel, _ = repair(source_base, (sa,))
                target_kernel, _ = repair(target_base, (ta,))
                pullback = {face for face in subsets(2) if frozenset(f[x] for x in face) in target_kernel}
                assert source_kernel == pullback
                lawful += 1

    identity = (0, 1, 2)
    base = scalar_base(3, (0, 0, 0), (0, 1, 2), Q(1, 2), (identity,))
    old, _ = repair(base, (identity,))
    changing = (0, 2, 2)
    updated, _ = repair(base, (changing,))
    assert frozenset((0, 1)) in old and frozenset((0, 1)) not in updated
    assert path_oracle(frozenset((0, 1)), base, (changing,)) == (False, (0,))
    delta = (2, 1, 2)
    assert changing[0] == 0 and changing[delta[0]] == 2
    assert frozenset((0, 1)) not in updated

    # A stationary source-dependent action keeps original tags, yet completing
    # its exact image to either maximal facet invents an endpoint or original.
    original = ("s0", "s0", "s1")
    action = (1, 1, 2)
    family, _ = repair(base, (action,))
    maximal = facets(family)
    exact = image(action, frozenset((0, 1)))
    containers = [face for face in maximal if exact <= face]
    assert containers == [frozenset((0, 1)), frozenset((1, 2))]
    assert exact == frozenset((1,))
    for face in family:
        assert {original[x] for x in image(action, face)} == {original[x] for x in face}
    assert {original[x] for x in containers[1]} == {"s0", "s1"}
    assert all(face - exact for face in containers)

    # Current-carrier recovery is not original-target recovery after erasure.
    erase = (0, 2, 2)
    erased_original = (0, 1, 1)
    current_carrier = (0, 1, 0)
    preparation = frozenset((0, 1))
    after_erase = image(erase, preparation)
    assert {erased_original[x] for x in preparation} == {erased_original[x] for x in after_erase}
    assert {current_carrier[x] for x in after_erase} == {0}
    assert {erased_original[x] for x in after_erase} == {0, 1}

    # Without homogeneous enabling, universally safe-action closure is not
    # hereditary: a smaller face gains an action that the larger one lacks.
    partial = (0, 3, None, 3)
    unguarded = scalar_base(4, (0,) * 4, (0, 0, 0, 2), Q(0), (partial,), False)
    fake, _ = repair(unguarded, (partial,))
    assert frozenset((0, 1, 2)) in fake and frozenset((0, 1)) not in fake
    guarded = scalar_base(4, (0,) * 4, (0, 0, 0, 2), Q(0), (partial,))
    honest, _ = repair(guarded, (partial,))
    assert frozenset((0, 1, 2)) not in honest

    # General target geometry needs actual feasible subsets, not pair graphs.
    points = ((Q(0), Q(0)), (Q(2), Q(0)), (Q(1), Q(2)))
    centers = points + ((Q(1), Q(0)), (Q(1, 2), Q(1)), (Q(3, 2), Q(1)), (Q(1), Q(3, 4)))
    eps2 = Q(36, 25)
    triangle = {face for face in subsets(3) if any(all(sum((points[x][j]-c[j])**2 for j in range(2)) <= eps2
                                                       for x in face) for c in centers)}
    assert all(face in triangle for face in subsets(3) if len(face) <= 2)
    assert frozenset(range(3)) not in triangle
    bary = (Q(1), Q(3, 4)); weights = (Q(5, 16), Q(5, 16), Q(6, 16))
    variance = sum(w * sum((points[i][j]-bary[j])**2 for j in range(2)) for i, w in enumerate(weights))
    assert variance == Q(25, 16) and variance > eps2
    triangle_kernel, _ = repair(triangle, (identity,))
    assert triangle_kernel == triangle

    source_files = ("SWARM_ATLAS/F46_MATHEMATICAL_PHENOMENOLOGY.md",
        "SWARM_ATLAS/D29_ATTRACTORS_CONLEY_SELF_UPDATE.md", "SWARM_ATLAS/A06.md",
        "SWARM_ATLAS/F42.md", "SWARM_ATLAS/F45_PROOF_COST_SCHEDULING.md",
        "SWARM_ATLAS/C21.md", "F48/F48_LAWFUL_HISTORY_FIBRATION.md",
        "SWARM_ATLAS/reviews/E40_F46_F47_PRINCIPAL_REVIEW.md",
        "SWARM_ATLAS/reviews/C21_PRINCIPAL_REVIEW.md", "SWARM_ATLAS/reviews/F48_KERNEL_REVIEW.md",
        "SWARM_ATLAS/reviews/F45_PRINCIPAL_REVIEW.md", "SWARM_ATLAS/PROTOCOL.md")
    hashes = {name: hashlib.sha256((CONSULTED / name).read_bytes()).hexdigest() for name in source_files}
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, text=True,
                          capture_output=True).stdout.strip()
    result = {"schema": "SWM-X12-exact-v1", "parent": PARENT, "execution_head": head,
        "limits": {"wall_seconds": 25, "cpu_seconds": 20, "address_space_mib": 256},
        "command": "PYTHONDONTWRITEBYTECODE=1 python research/2026-10-13/SWARM_ATLAS/X12_probe.py",
        "command_exit": 0, "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "consulted_sha256": hashes,
        "workspace_authority_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in ("AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
                "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
                "observational_succ/field_relative_closure.py", "observational_succ/adaptive_proof_policy.py")},
        "exhaustive_and_seeded": {"models": models, "face_oracle_comparisons": comparisons,
            "largest_removal_round": largest_round, "longest_bad_word": longest_word,
            "lawful_source_map_cases": lawful, "seed": 12004629},
        "noncanonical_partition": {"facets": printable(facets(old)), "full_triple_invalid": True},
        "source_change_control": {"old_facets": printable(facets(old)),
            "updated_facets": printable(facets(updated)), "invalid_face": [0, 1], "bad_word": [0]},
        "carrier_deflection": {"before_orbit": [0, 0], "after_deflection_orbit": [2, 2],
            "unchanged_model_still_rejects_face": [0, 1]},
        "facet_history_control": {"exact_image": sorted(exact), "maximal_containers": printable(containers),
            "exact_original_support": ["s0"], "second_container_original_support": ["s0", "s1"],
            "both_containers_introduce_unreachable_endpoint": True},
        "original_target_erasure_control": {"original_support_before_and_after": [0, 1],
            "current_carrier_after": [0], "current_bound_does_not_certify_original_target": True},
        "missing_enabledness_guard": {"surviving_large_face": [0, 1, 2], "rejected_subface": [0, 1],
            "unguarded_family_not_hereditary": True},
        "hypergraph_control": {"all_pairs_feasible": True, "triple_infeasible": True,
            "variance_lower_bound_squared": str(variance), "tolerance_squared": str(eps2)},
        "proof_status": "PROVED LOCAL paper proof; probe is bounded exact regression evidence",
        "physical_psychological_or_kernel_validation": False}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
