#!/usr/bin/env python3
"""Predeclared F41--F48 exact finite probes; simulator is isolated from learner."""
from __future__ import annotations
import json
from itertools import product
from pathlib import Path
from random import Random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.swarm_discovery import (TableSource, discover_quotient,
    action_algebra, invariant_under_label_change, target_factors, compose, element_order)
from observational_succ.swarm_lawful_history import (LawfulSource, Instrument,
    Event, replay_fiber, quotient_source, legal_histories, synchronized_original_support)
from observational_succ.swarm_resource_geometry import (debt_stages,
    finite_completion_possible, anchored_graph_matrix, graph_evidence_update, clock_gluing)


def simulator(prime, seed, coupling=1, swap=False):
    """ONLY this producer knows coordinates; learner takes resulting tables."""
    raw = list(product(range(prime), repeat=3))
    Random(seed).shuffle(raw)
    index = {v: i for i, v in enumerate(raw)}
    actions = (
        ("a", tuple(index[((x+1) % prime, y, (z+coupling*y) % prime)] for x, y, z in raw)),
        ("b", tuple(index[(x, (y+1) % prime, z)] for x, y, z in raw)))
    if swap:
        actions += (("swap", tuple(index[(z, y, x)] for x, y, z in raw)),)
    return TableSource(f"opaque-{prime}-{seed}-{coupling}-{swap}", actions,
                       (tuple(z for _, _, z in raw),)), tuple(raw)


def dihedral_simulator(size, seed):
    raw = list(range(size))
    Random(seed).shuffle(raw)
    index = {v: i for i, v in enumerate(raw)}
    return TableSource(f"opaque-dihedral-{size}-{seed}",
        (("a", tuple(index[(x+1) % size] for x in raw)),
         ("b", tuple(index[-x % size] for x in raw))),
        (tuple(int(x == 0) for x in raw),))


def fresh_word_checks(source, q, seed=137137):
    rng, qa, checks = Random(seed), dict(q.actions), 0
    # Separate direct simulator replay versus quotient interpreter.
    for length in (17, 31, 79):
        for _ in range(20):
            start = rng.randrange(source.count)
            word = tuple(rng.choice(source.actions)[0] for _ in range(length))
            raw, coarse = start, q.labels[start]
            for name in word:
                raw = next(table for action, table in source.actions if action == name)[raw]
                coarse = qa[name][coarse]
            assert source.readouts[0][raw] == q.readouts[0][coarse]
            assert q.labels[raw] == coarse
            checks += 1
    return checks


def discovery_receipt():
    cases = []
    for p, seed in ((2, 20261013), (5, 987654)):
        source, raw = simulator(p, seed)
        q = discover_quotient(source)
        profile = action_algebra(q)
        assert q.count == p*p and profile["size"] == p**3
        assert profile["central_commutator"] and profile["commutator_order"] == p
        product_order = element_order(compose(dict(q.actions)["a"], dict(q.actions)["b"]))
        assert product_order == (4 if p == 2 else p)
        x_target = tuple(v[0] for v in raw)
        identifiable, witness = target_factors(q.labels, x_target)
        assert not identifiable and witness is not None
        enlarged, _ = simulator(p, seed, swap=True)
        expanded = discover_quotient(enlarged)
        assert expanded.count == p**3
        null, _ = simulator(p, seed, coupling=0)
        nq = discover_quotient(null)
        null_profile = action_algebra(nq)
        assert nq.count == p and null_profile["size"] == 1
        permutation = list(range(source.count))
        Random(seed+1).shuffle(permutation)
        relabeled = invariant_under_label_change(source, tuple(permutation))
        rq = discover_quotient(relabeled)
        assert action_algebra(rq) == profile
        assert all((q.labels[i] == q.labels[j]) == (rq.labels[permutation[i]] == rq.labels[permutation[j]])
                   for i in range(source.count) for j in range(source.count))
        cases.append({"prime_for_audit_only": p, "source_states": source.count,
            "minimal_states": q.count, "action_profile": profile,
            "generator_product_order": product_order,
            "fresh_word_checks": fresh_word_checks(source, q),
            "zero_coupling_states": nq.count, "zero_coupling_profile": null_profile,
            "original_x_dark_witness": list(witness), "new_swap_states": expanded.count,
            "relabeling_conjugacy_checked": True,
            "coordinates_given_to_learner": False, "complete_table_supplied": True})
    out = dihedral_simulator(5, 424242)
    oq = discover_quotient(out)
    profile = action_algebra(oq)
    assert oq.count == 5 and profile["size"] == 10 and profile["center_size"] == 1
    assert not profile["central_commutator"] and profile["commutator_order"] == 5
    return {"family_holdouts": cases, "out_of_family": {
        "source_states": out.count, "minimal_states": oq.count, "action_profile": profile,
        "fresh_word_checks": fresh_word_checks(out, oq)}}


def destructive_source():
    # Original pair (a,b) is prepared once. Reading either bit erases the other.
    return LawfulSource("single-destructive-pair", (0, 1, 2, 3), (
        Instrument("a", (0, 0, 2, 2), (0, 0, 1, 1), (True,)*4),
        Instrument("b", (0, 1, 0, 1), (0, 1, 0, 1), (True,)*4)))


def history_receipt():
    erase = LawfulSource("erase-original", (0, 1), (
        Instrument("erase", (0, 0), ("done", "done"), (True, True)),
        Instrument("read", (0, 1), (0, 1), (True, True))))
    prefix = replay_fiber(erase, (Event("erase", "done"),))
    assert prefix.configurations == ((0, 0), (1, 0))
    pair = destructive_source()
    a, b = replay_fiber(pair, (Event("a", 1),)), replay_fiber(pair, (Event("b", 1),))
    sequential = replay_fiber(pair, (Event("a", 1), Event("b", 1)))
    assert a.originals & b.originals == {3} and not sequential.originals
    # A hidden copy coordinate safely quotients from current carrier, preserving
    # each separately prepared original's support and future availability.
    duplicated = LawfulSource("duplicate-current", (0, 1, 2, 3), (
        Instrument("flip", (1, 0, 3, 2), (0, 1, 0, 1), (True,)*4),
        Instrument("erase", (0, 0, 2, 2), (0, 0, 0, 0), (True,)*4)))
    labels = (0, 1, 0, 1)
    q = quotient_source(duplicated, labels)
    histories = legal_histories(duplicated, 5)
    assert all(synchronized_original_support(duplicated, q, labels, f.history) for f in histories)
    return {"erase_original_current_pairs": [list(x) for x in prefix.configurations],
        "counterfactual_branch_overlap_originals": sorted(a.originals & b.originals),
        "sequential_both_one_originals": sorted(sequential.originals),
        "quotient_history_checks": len(histories), "single_preparation_reset_assumed": False}


def resource_receipt():
    from fractions import Fraction as F
    boundary = debt_stages(2, 1, 1, F(1, 2), 12)
    assert boundary == tuple(F(2, 2**n) for n in range(13))
    assert not finite_completion_possible(2, 1, 1, F(1, 2))
    assert finite_completion_possible(F(3, 2), 1, 1, F(1, 2))
    below = debt_stages(F(3, 2), 1, 1, F(1, 2), 3)
    assert below[2] == 0
    matrix = anchored_graph_matrix(3, ((0, 1, 1), (0, 2, 1)), (1, 1, 1))
    center = graph_evidence_update(matrix, (0, 0, 0), 0, 1, 1)
    leaf = graph_evidence_update(matrix, (0, 0, 0), 1, 1, 1)
    locked = clock_gluing(3, 3, ((0, 1, 1), (1, 2, 1), (2, 0, 1)))
    obstructed = clock_gluing(3, 3, ((0, 1, 1), (1, 2, 1), (2, 0, 2)))
    assert locked["phases"] == (0, 1, 2)
    assert obstructed["phases"] is None and obstructed["residual"] != 0
    return {"boundary_debt": [str(x) for x in boundary], "below_threshold_debt": [str(x) for x in below],
        "central_feature_update": [str(x) for x in center], "leaf_feature_update": [str(x) for x in leaf],
        "clock_positive": locked, "clock_mutation": obstructed,
        "empirical_psychology_or_music_claim": False}


def main():
    result = {"schema": "succ-swm-f-receipt-v1", "parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "sibling": "b2774ca485db4b5b4f7ce92e535220352fb3af2f",
        "precommit": "3ac5769", "discovery": discovery_receipt(),
        "history": history_receipt(), "resources": resource_receipt(),
        "kernel_proof_executed": False, "academic_novelty_verified": False,
        "scope": "exact finite models plus written general derivations"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
