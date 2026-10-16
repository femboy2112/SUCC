#!/usr/bin/env python3
"""Deterministic exact witnesses; stdout is JSON, no optional dependencies."""
from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.collective_modular import (
    BoundedCylinder, affine_character, affine_norm_squared, collective_sectors,
    compatible_crt_image, conditional_expectation, conductor_projector,
    conductor_six_basis, fucc_pullback, linear_pool_projector,
    minimum_target_portfolio, missing_joint_projector, target_pair_cover,
)
from observational_succ.consensus_lambda import Candidate, World
from observational_succ.finite_fourier_carrier import CyclotomicElement as C
from observational_succ.pascal_rotated_transport import matmul, matrix_apply
from observational_succ.source_lambda import Passport


def build_receipt():
    # Independent finite path-count oracle for ALL matrix coefficients:
    # successive uniform translations visit every gcd fiber equally often.
    cases = 0
    for n in range(1, 25):
        ds = [d for d in range(1, n+1) if n % d == 0]
        for m, q in product(ds, repeat=2):
            counts = [0]*n
            for a, b in product(range(n//m), range(n//q)):
                counts[(a*m+b*q) % n] += 1
            scale = (n//m)*(n//q)
            if any(Q(c, scale) != (Q(gcd(m, q), n) if t % gcd(m, q) == 0 else 0)
                   for t, c in enumerate(counts)):
                raise AssertionError("translation path-count oracle failed")
            # Translation invariance: first row determines the full product.
            em, en = conditional_expectation(n, m), conditional_expectation(n, q)
            row = tuple(sum(em[0][k]*en[k][y] for k in range(n)) for y in range(n))
            if row != tuple(Q(c, scale) for c in counts):
                raise AssertionError("expectation disagrees with path-count oracle")
            cases += 1

    u, v = conductor_six_basis()
    p6 = conductor_projector(6, 6)
    for w in (u, v):
        if matrix_apply(p6, w) != w:
            raise AssertionError("conductor-six basis not fixed")
        for m in (2, 3):
            if any(sum(w[x] for x in range(r, 6, m)) for r in range(m)):
                raise AssertionError("conductor-six basis visible in local marginals")
    if missing_joint_projector(6, (2, 3)) != p6:
        raise AssertionError("missing sector mismatch")
    # All P6 coefficients against the independently defined character kernel.
    for x, y in product(range(6), repeat=2):
        kernel = (C.root(6, x-y)+C.root(6, 5*(x-y))).scale(Q(1, 6))
        if kernel != C.scalar(6, p6[x][y]):
            raise AssertionError("primitive character kernel mismatch")
    phase, transported = affine_character(6, 1, 2, 1)
    for x in range(6):
        if C.root(6, 2*x+1) != phase*transported.character_root(x):
            raise AssertionError("affine phase not transported")

    p = Passport("declared-collective-modular-fixture", 0)
    world = World(p, tuple(Candidate(str(x), x, str(x)) for x in range(6)))
    minimum = minimum_target_portfolio(world, (2, 3))
    augmented = minimum_target_portfolio(world, (2, 3, 6))
    if len(minimum.selected) != 2 or len(augmented.selected) != 1:
        raise AssertionError("incorrect minimum read cover")
    hidden = World(p, (Candidate("a", 7, "left"), Candidate("b", 7, "right")))

    # Concrete failure of Haar gcd identity after replacing Haar by correlation.
    weights = (Q(2), Q(1), Q(1), Q(1), Q(1), Q(1))
    def weighted(m):
        return tuple(tuple(weights[y]/sum(weights[z] for z in range(6) if z % m == x % m)
                           if x % m == y % m else Q(0) for y in range(6)) for x in range(6))
    product00 = matmul(weighted(2), weighted(3))[0][0]
    global00 = weighted(1)[0][0]
    if product00 == global00:
        raise AssertionError("nonuniform negative control did not separate")
    fucc = fucc_pullback(6, 2)
    e1 = conditional_expectation(6, 1)
    left00, right00 = matmul(e1, fucc)[0][0], matmul(fucc, e1)[0][0]
    if left00 == right00:
        raise AssertionError("nonunit negative control did not separate")

    owned = ("observational_succ/collective_modular.py", "tests/test_collective_modular.py",
             "scripts/collective_modular_probe.py", "research/2026-10-16/COLLECTIVE_MODULAR_ALGEBRA.md")
    dependencies = (
        "observational_succ/source_lambda.py", "observational_succ/consensus_lambda.py",
        "observational_succ/classical_haar_clock.py", "observational_succ/dynamic_fourier_tower.py",
        "observational_succ/pontryagin_source_duality.py", "observational_succ/finite_fourier_carrier.py",
        "observational_succ/all_places_zeta.py", "observational_succ/prime_form_heat.py",
        "observational_succ/pascal_rotated_transport.py", "observational_succ/structural_coupling.py",
        "observational_succ/classical_unit_origin.py", "observational_succ/diagonal_adele_zeta.py",
        "observational_succ/edge_carrier_reconstruction.py", "provenance/IMPORT_MANIFEST.json",
    )
    return {
        "status": "EXACT_FINITE_CHECKS_PASSED",
        "schema": "collective-modular-v1",
        "scope": "uniform cyclic model, exact rational/cyclotomic arithmetic, no physical authentication",
        "independence": "distinct algorithms; same author and shared repository arithmetic",
        "path_count_oracle": {"ambient_range": [1, 24], "ordered_divisor_pair_cases": cases},
        "pair_2_3": {
            "E2": conditional_expectation(6, 2), "E3": conditional_expectation(6, 3),
            "P6": p6, "linear_projector": linear_pool_projector(6, (2, 3)),
            "basis": [u, v], "normalized_gram": [[Q(2), Q(0)], [Q(0), Q(2, 3)]],
            "linear_dimension": 4, "joint_dimension": 6, "missing_dimension": 2,
            "product_of_local_functions": BoundedCylinder((1, -1)).multiply(BoundedCylinder((2, -1, -1))).values,
            "character_product_labels_mod6": [3, 4, 1], "independent_prime_place_6": False,
        },
        "noncoprime_4_6": {"compatible_image": compatible_crt_image((4, 6)),
                           "compatible_size": 12, "cartesian_size": 24,
                           "rejected_tuple": [0, 1], "linear_dimension": 8, "missing_dimension": 4},
        "multi_menu": [dict(asdict(s), linear_dimension=s.linear_dimension,
                            missing_dimension=s.missing_dimension) for s in
                       (collective_sectors(30, (2, 3, 5)), collective_sectors(30, (6, 10, 15)))],
        "target_cover": {"pairs": target_pair_cover(world, (2, 3)),
                         "minimum_2_3": asdict(minimum), "minimum_2_3_6": asdict(augmented),
                         "hidden_collision": asdict(minimum_target_portfolio(hidden, (2, 3, 5)))},
        "affine_nonunit": {"n": 6, "a": 2, "b": 1, "phase_polynomial": phase.polynomial,
                           "input_conductor": 6, "output_conductor": transported.rational_frequency.denominator,
                           "norm_squared": affine_norm_squared(6, 2),
                           "E1U_entry00": left00, "UE1_entry00": right00},
        "nonuniform_counterexample": {"unnormalized_weights": weights,
                                      "E2E3_entry00": product00, "E1_entry00": global00},
        "finite_portfolio_global_alias": {"moduli": [2, 3], "integers": [0, lcm(2, 3)]},
        "proof_status": "paper proofs in dossier; finite runs do not certify universal claims",
        "analytic_boundary": "cylinders dense in C uniformly and Lp for finite p, not in all Linfinity",
        "sha256": {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
                   for path in owned+dependencies},
    }


if __name__ == "__main__":
    print(json.dumps(build_receipt(), sort_keys=True, indent=2,
                     default=lambda x: str(x) if isinstance(x, Q) else asdict(x)))
