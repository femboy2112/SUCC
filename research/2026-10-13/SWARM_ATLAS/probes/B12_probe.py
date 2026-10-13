#!/usr/bin/env python3
"""Tiny exact B12 controls. Infinite claims are proved in B12.md, not run here."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from observational_succ.absorbing_frames import HornRule, least_horn_closure
from observational_succ.ideal_frames import IdealJetFrame, PolynomialSource


def powerset(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield tuple(x for i, x in enumerate(items) if mask & (1 << i))


def directed(family):
    return bool(family) and all(
        any(a | b <= c for c in family) for a in family for b in family
    )


def union(family):
    return frozenset().union(*family)


def pullback(record, translation):
    values = dict(record)
    return frozenset(
        (j, values[q]) for j, q in enumerate(translation) if q in values
    )


def source_domain_control():
    sources = ((0, 0), (1, 1))
    records = tuple(
        frozenset((q, value) for q, value in enumerate(partial) if value != -1)
        for partial in itertools.product((-1, 0, 1), repeat=2)
    )

    def versions(record):
        return tuple(s for s in sources if all(s[q] == v for q, v in record))

    realizable = tuple(r for r in records if versions(r))
    assert len(realizable) == 7
    directed_families = tuple(f for f in powerset(realizable) if directed(f))
    translation = (1, 1, 0)
    after = (2, 0)
    composition = tuple(translation[j] for j in after)
    scott_checks = 0
    for family in directed_families:
        joined = union(family)
        assert joined in realizable
        # Separate constraint-intersection oracle rather than choosing the last stage.
        common = set(sources)
        for member in family:
            common.intersection_update(versions(member))
        assert common == set(versions(joined)) and common
        assert pullback(joined, translation) == union(
            pullback(r, translation) for r in family
        )
        for finite_record in realizable:
            if finite_record <= joined:
                assert any(finite_record <= r for r in family)
                scott_checks += 1
    for record in realizable:
        assert pullback(pullback(record, translation), after) == pullback(
            record, composition
        )
    for source in sources:
        full = frozenset(enumerate(source))
        assert dict(pullback(full, translation)) == {
            j: source[q] for j, q in enumerate(translation)
        }
    assert not versions(frozenset(((0, 0), (1, 1))))
    return {
        "sources": [list(s) for s in sources],
        "all_partial_records": len(records),
        "realizable_records": len(realizable),
        "nonempty_directed_families": len(directed_families),
        "finite_record_scott_accessibility_checks": scott_checks,
        "version_intersection_and_union_agree": True,
        "pullback_directed_unions_and_composition": True,
        "conflicting_cross_source_union_rejected": True,
    }


def horn_control():
    tokens = ("a", "b", "c")
    rules = (HornRule(("a",), "b"), HornRule(("b",), "c"))
    seeds = tuple(frozenset(s) for s in powerset(tokens))
    successors = {"a": ("b",), "b": ("c",), "c": ()}

    # Independent graph-reachability oracle for this unary-rule control.
    def oracle(seed):
        reached = set(seed)
        todo = list(seed)
        while todo:
            node = todo.pop()
            for child in successors[node]:
                if child not in reached:
                    reached.add(child)
                    todo.append(child)
        return frozenset(reached)

    closures = {
        seed: frozenset(least_horn_closure(tuple(sorted(seed)), rules).atoms)
        for seed in seeds
    }
    assert all(closures[seed] == oracle(seed) for seed in seeds)
    families = tuple(f for f in powerset(seeds) if directed(f))
    for family in families:
        assert closures[union(family)] == union(closures[s] for s in family)
    assert closures[frozenset(("a",))] == frozenset(tokens)
    assert closures[frozenset()] == frozenset()
    return {
        "seeds": len(seeds),
        "directed_families": len(families),
        "independent_reachability_oracle_agrees": True,
        "directed_union_preservation": True,
        "no_seed_no_derived_fact": True,
    }


def source_swap_control():
    zero, linear = PolynomialSource((0,)), PolynomialSource((0, 1))
    initial = IdealJetFrame.initial(zero)
    swapped = initial.succ(linear)
    assert initial.compatible(zero) and initial.compatible(linear)
    assert tuple(swapped.observed_jet) == (0, 1)
    assert swapped.compatible(linear) and not swapped.compatible(zero)
    # Direct coefficient oracle for derivatives zero and one, independent of jet().
    assert (zero.coefficients[0], 0) == (0, 0)
    assert (linear.coefficients[0], linear.coefficients[1]) == (0, 1)
    return {
        "initial_actual_source": "zero polynomial",
        "initial_jet": [str(v) for v in initial.observed_jet],
        "replacement_jet": [str(v) for v in swapped.observed_jet],
        "compatible_substitution_accepted": True,
        "replacement_has_realizer": True,
        "initial_actual_source_realizes_replacement": False,
        "scope": "compatibility-only lab; no physical source identity certificate",
    }


def negative_witness_controls():
    nonclosed = []
    for horizon in range(6):
        source = lambda n, h=horizon: int(n < h)
        assert all(source(n) == 1 for n in range(horizon))
        assert source(horizon) == 0
        nonclosed.append({"horizon": horizon, "next_mismatch": horizon})
    finite_indices = (0, 2, 5)
    support_source = lambda n: int(n in finite_indices)
    assert all(support_source(n) == 1 for n in finite_indices)
    assert support_source(6) == 0
    ones = lambda n: 1
    assert all(ones(n) == 1 for n in range(6))

    infinite_alphabet = []
    for budget in range(6):
        def c(n, m=budget):
            return m if n == 0 else int(1 <= n <= m)
        assert c(0) == budget
        assert all(c(n) == 1 for n in range(1, budget + 1))
        assert c(budget + 1) == 0
        infinite_alphabet.append({
            "hidden_budget": budget,
            "matched_partial_horizon": budget,
            "next_mismatch": budget + 1,
        })
    return {
        "eventually_zero_prefix_witnesses": nonclosed,
        "arbitrary_finite_support_witness": list(finite_indices),
        "outside_support_mismatch": 6,
        "infinite_alphabet_closed_image_witnesses": infinite_alphabet,
        "positive_constant_one_source": {
            "declared_formula": "c(n)=1 for every natural n",
            "sample_values": [ones(n) for n in range(6)],
        },
        "infinite_profile_execution": False,
        "universal_nonrealization_basis": "B12.md sections 5 and 6 proofs",
    }


def main():
    files = (
        "observational_succ/ideal_frames.py",
        "observational_succ/constructive_frontier.py",
        "observational_succ/absorbing_frames.py",
    )
    receipt = {
        "claim_id": "SWM-B12",
        "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "scope": "bounded exact finite controls; no universal computation or kernel proof",
        "source_sha256": {
            path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            for path in files
        },
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "finite_source_domain": source_domain_control(),
        "finite_premise_closure": horn_control(),
        "original_source_substitution": source_swap_control(),
        "negative_witnesses": negative_witness_controls(),
        "checks_passed": True,
        "mandatory_full_repository_validation_run": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
