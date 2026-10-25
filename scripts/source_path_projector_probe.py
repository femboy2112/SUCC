#!/usr/bin/env python3
"""Deterministic exact receipt for finite source-path interference.

Candidate-path enumeration, factored character evaluation, and Cartesian
dual-variable enumeration are counted separately. No selected asymptotic
arithmetic estimate is claimed by this finite laboratory.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from observational_succ.source_path_projector import (  # noqa: E402
    bbp_circle_carrier, bbp_prefix_inclusion, cartesian_interference,
    character_sum, circle_inclusion_transport, cyclic_path,
    cyclotomic_polynomial, dual_observable_transport, enumerate_projector,
    observable_transform, projector_weight, quotient_path_transport,
    rational_residue,
)


def _json(value):
    if isinstance(value, Q):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if isinstance(value, dict):
        return {str(key): _json(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json(item) for item in value]
    return value


def _scalar(q, value):
    return (Q(value),)+(Q(),)*(len(cyclotomic_polynomial(q))-2)


def _literal_forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def build_receipt():
    rows = []
    candidate_total = 0
    for q in (3, 5, 7, 9):
        for horizon in range(1, 5):
            source = tuple(j*j+1 for j in range(1, horizon+1))
            row = enumerate_projector(q, 16, source, initial=1)
            assert row["direct_accepted_paths"] == 1
            assert row["interference_total_mass"] == 1
            assert row["factorization_mismatches"] == 0
            candidate_total += row["candidate_paths_enumerated"]
            rows.append(row)
    assert candidate_total == 90_280

    cartesian_terms = 0
    cartesian_paths = 0
    for q, source in ((3, (1, 2)), (5, (3,))):
        for path in product(range(q), repeat=len(source)+1):
            value = projector_weight(q, 2, source, path, initial=1)
            full = cartesian_interference(q, 2, source, path, initial=1)
            assert full["normalized_coefficients"] == _scalar(q, value)
            cartesian_terms += full["cartesian_dual_terms_enumerated"]
            cartesian_paths += 1
    assert cartesian_paths == 52 and cartesian_terms == 1354

    holdout = enumerate_projector(11, 5, (3, 7, 2), initial=4)
    assert holdout["factorization_mismatches"] == 0
    assert holdout["direct_accepted_paths"] == 1

    observable_checks = 0
    for q in (3, 5, 7, 9, 11):
        for horizon in range(1, 5):
            source = tuple(2*j+1 for j in range(horizon))
            frequencies = tuple((-1)**j*(j+2) for j in range(horizon+1))
            data = dual_observable_transport(q, 16, source, frequencies)
            for initial in range(q):
                path = cyclic_path(q, 16, source, initial)
                direct = sum(x*h for x, h in zip(path, frequencies)) % q
                dual = (data["source_offset"]+
                        initial*data["initial_frequency"]) % q
                assert direct == dual
                observable_checks += 1

    prefix_checks = 0
    for q in (3, 5, 7, 9):
        for horizon in range(1, 4):
            source = tuple(j*j+1 for j in range(1, horizon+1))
            for prefix in product(range(q), repeat=horizon):
                expected = projector_weight(q, 16, source[:-1], prefix, initial=1)
                actual = sum((projector_weight(q, 16, source, prefix+(last,), initial=1)
                              for last in range(q)), Q())
                assert actual == expected
                prefix_checks += 1

    free = enumerate_projector(5, 16, (1, 3, 2), initial=None)
    assert free["direct_accepted_paths"] == 5
    assert free["interference_total_mass"] == 5
    changed_phase = enumerate_projector(9, 16, (1, 2), phase_multiplier=3)
    assert changed_phase["interference_total_mass"] == 27
    assert changed_phase["factorization_mismatches"] == 26

    actual = cyclic_path(7, 16, (1, 3, 2), initial=0)
    assert projector_weight(7, 16, (1, 3, 2), actual, initial=1) == 0
    assert projector_weight(7, 16, (-1, 3, 2), actual, initial=0) == 0
    normalization_case = cartesian_interference(3, 5, (2, 1),
                                                 cyclic_path(3, 5, (2, 1)))
    raw_total = normalization_case["reduced_unnormalized_coefficients"][0]
    assert raw_total == 27 and raw_total/9 == 3

    uniform = (Q(1, 7),)*7
    selected = (Q(1),)+(Q(),)*6
    mean = observable_transform(7, 16, (1, 3, 2), (0, 0, 0, 1), uniform)
    chosen = observable_transform(7, 16, (1, 3, 2), (0, 0, 0, 1), selected)
    assert mean == _scalar(7, 0)
    assert chosen == character_sum(7, (actual[-1],)) and chosen != mean

    source_rows = []
    source_states_checked = 0
    for horizon in (1, 2, 3, 4, 6, 8, 12):
        carrier = bbp_circle_carrier(horizon)
        state = Q()
        independent = [state]
        for n in range(1, horizon+1):
            state = (16*state+_literal_forcing(n)) % 1
            independent.append(state)
        assert tuple(independent) == carrier["phases"]
        assert carrier["projector_weight"] == 1
        source_states_checked += horizon+1
        source_rows.append({"horizon": horizon, "modulus": carrier["modulus"],
                            "final_phase": carrier["phases"][-1],
                            "literal_carries": carrier["literal_carries"],
                            "final_cumulative_carry": carrier["cumulative_carries"][-1],
                            "projector_weight": carrier["projector_weight"],
                            "expanded_fourier_sum": False})

    inclusions = tuple(bbp_prefix_inclusion(short, long)
                       for short, long in ((1, 2), (2, 5), (3, 8), (8, 12)))
    quotient = quotient_path_transport(55, 11, 5, (7, 2, 11), initial=4)
    circle = circle_inclusion_transport(3, 15, 16, (1, 2), initial=1)
    assert circle["fine_path"][0] == 5
    assert circle["fine_path"][0] % 3 != circle["coarse_path"][0]

    pole_rejections = 0
    for modulus in (3, 5):
        try:
            rational_residue(Q(47, 15), modulus)
        except ValueError:
            pole_rejections += 1
        else:
            raise AssertionError("BBP pole-domain mutation accepted")

    constant = cyclic_path(7, 16, (0,)*8, initial=0)
    periodic = cyclic_path(7, 16, (0,)*8, initial=1)
    assert constant == (0,)*9 and periodic[:7] == (1, 2, 4, 1, 2, 4, 1)

    source_files = (
        "observational_succ/source_path_projector.py",
        "tests/test_source_path_projector.py",
        "scripts/source_path_projector_probe.py",
        "observational_succ/bbp_source_memory.py",
    )
    hashes = {name: sha256((REPOSITORY_ROOT/name).read_bytes()).hexdigest()
              for name in source_files}

    return {
        "status": "VERIFIED_FINITE",
        "scope": "finite source selection and declared carrier transport",
        "pi_normality": "OPEN",
        "selected_real_carry_estimate": "OPEN",
        "floating_point_used": False,
        "preregistered_factorized_path_checks": {
            "candidate_paths_enumerated": candidate_total,
            "cartesian_path_by_dual_enumeration": False, "rows": rows},
        "separate_cartesian_dual_oracle": {
            "candidate_paths_checked": cartesian_paths,
            "dual_tuples_actually_enumerated": cartesian_terms},
        "holdout_q11_base5": holdout,
        "dual_observable_initial_state_checks": observable_checks,
        "prefix_marginal_checks": prefix_checks,
        "mutations": {
            "omitted_initial_selector": free,
            "nonunit_dual_phase": changed_phase,
            "wrong_initial_rejected": True, "wrong_forcing_rejected": True,
            "wrong_normalization_mass": raw_total/9,
            "rational_pole_domains_rejected": pole_rejections},
        "selector_gap": {"uniform_endpoint_character": mean,
                         "selected_endpoint_character": chosen},
        "authentic_bbp_circle_carriers": {
            "rational_states_independently_checked": source_states_checked,
            "rows": source_rows, "prefix_inclusions": inclusions},
        "distinct_carrier_transports": {
            "profinite_quotient": quotient, "circle_inclusion": circle,
            "modular_reduction_as_circle_inclusion_rejected": True,
            "circle_projector_alone_authenticates_integer_lift": False},
        "accepted_nonnormal_controls": {"constant": constant, "periodic": periodic},
        "source_sha256": hashes,
    }


if __name__ == "__main__":
    print(json.dumps(_json(build_receipt()), indent=2, sort_keys=True))
