#!/usr/bin/env python3
"""Reproduce the exact finite SUCC/graph/Haar/Wilson bridge receipt."""

import json
from fractions import Fraction as Q
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.quantum_records import measure_z
from observational_succ.ym_graph_semantics import (
    Edge, LayeredGraph, Matrix, channel_action, compile_source_lambda,
    pure_density, truncated_successor,
)
from observational_succ.ym_haar_bridge import (
    WeightedSplit, haar_analyze, haar_synthesize, z2_wilson_weights,
)
from observational_succ.ym_reflection_bridge import haar_polynomial, polynomial_product
from observational_succ.ym_succ_character import (
    build_wilson_certificate, chebyshev_character, graph_return_moment,
    wilson_graph_vector,
)


def polynomial_compose(outer, inner):
    """Exact Horner composition, used only by this reproduction probe."""
    result = (Q(0),)
    for coefficient in reversed(outer):
        product = list(polynomial_product(result, inner))
        product[0] += coefficient
        while len(product) > 1 and product[-1] == 0:
            product.pop()
        result = tuple(product)
    return result


def multiplier_probe():
    """Check the existing V_p in central Haar coordinates, including composites."""
    identity_checks = norm_checks = 0
    for p in range(1, 8):
        first_kind = list(chebyshev_character(p))
        if p >= 2:
            for k, coefficient in enumerate(chebyshev_character(p - 2)):
                first_kind[k] -= coefficient
        first_kind = tuple(coefficient / 2 for coefficient in first_kind)
        weight = chebyshev_character(p - 1)
        for n in range(1, 9):
            pulled = polynomial_compose(chebyshev_character(n - 1), first_kind)
            transported = polynomial_product(weight, pulled)
            assert transported == chebyshev_character(p * n - 1)
            identity_checks += 1
            assert haar_polynomial(polynomial_product(transported, transported)) == 1
            norm_checks += 1
    # Omitting U_(p-1) already changes the norm of the polynomial f(x)=x.
    bare_square = polynomial_product((-1, 0, 2), (-1, 0, 2))
    assert haar_polynomial(bare_square) == Q(1, 2)
    assert haar_polynomial((0, 0, 1)) == Q(1, 4)
    return {
        "formula": "W V_p W* f(x) = U_(p-1)(x) f(T_p(x))",
        "multipliers": list(range(1, 8)),
        "positive_integer_basis_indices": list(range(1, 9)),
        "exact_character_identities": identity_checks,
        "exact_norm_checks": norm_checks,
        "bare_T2_pullback_of_x_norm_squared": Q(1, 2),
        "original_x_norm_squared": Q(1, 4),
        "universal_L2_isometry": "proved in SUCC_CHARACTER_PROOF.md, not inferred from finite checks",
    }


def run():
    cert = build_wilson_certificate(Q(3, 2), (0, 1), Q(1, 10**12))
    s = truncated_successor(cert.cutoff + 1).matrix()
    j = (s + s.dagger()).scaled(Q(1, 2))
    density = pure_density(cert.unnormalized_vector)
    expectation = (j @ density).trace().real
    assert expectation == cert.expectation
    assert cert.error_bound <= cert.tolerance
    assert density.trace().real == 1

    packet = haar_analyze((1, -2, 3, 5), (Q(2, 7), Q(5, 7), Q(1, 3), Q(2, 3)))
    assert haar_synthesize(packet) == (1, -2, 3, 5)
    fair, biased = WeightedSplit(*z2_wilson_weights(0)), WeightedSplit(*z2_wilson_weights(Q(3, 5)))
    cancellation = LayeredGraph((1, 2, 1), (
        Edge(0, 0, 0, 1), Edge(0, 0, 1, 1),
        Edge(1, 0, 0, 1), Edge(1, 1, 0, -1),
    ))
    assert cancellation.path_sum(0, 0).real == 0

    small_ray = wilson_graph_vector(1, 1, 1)
    small_j = Matrix(((0, Q(1, 2)), (Q(1, 2), 0)))
    small_density = pure_density(small_ray)
    dephased = channel_action(tuple(Matrix(k) for _, k in measure_z().outcomes), small_density)
    before, after = (small_j @ small_density).trace().real, (small_j @ dephased).trace().real
    assert (before, after) == (Q(4, 17), 0)

    return {
        "source": "normalized single SU(2) Wilson plaquette; trace x=Tr(U)/2",
        "successor_carrier": "old e_(n+1) indexed as n>=0; open vacuum boundary",
        "haar_graph_moments_0_through_12": [graph_return_moment(k) for k in range(13)],
        "cutoff_3_first_defect_at_power_8": graph_return_moment(8)-graph_return_moment(8, 3),
        "multiplicative_succ_character_bridge": multiplier_probe(),
        "constructive_wilson_certificate": {
            "beta": cert.beta, "observable_coefficients": cert.polynomial,
            "tolerance": cert.tolerance, "taylor_degree": cert.taylor_degree,
            "cutoff": cert.cutoff, "graph_vertices": cert.cutoff + 1,
            "norm_squared": cert.norm_squared, "expectation": expectation,
            "error_bound": cert.error_bound, "density_trace": 1,
            "matrix_path_and_source_values_agree": True,
        },
        "weighted_haar": {"coefficients": packet.coefficients,
                          "metric": packet.coefficient_weights,
                          "energy": packet.energy, "inverse_exact": True},
        "state_and_observable_binding": {
            "same_adapted_state": fair.analyze(1, 1) == biased.analyze(1, 1),
            "uniform_observable_expectation": fair.multiplication_matrix(1, -1)[0][0],
            "biased_wilson_observable_expectation": biased.multiplication_matrix(1, -1)[0][0],
        },
        "actual_source_lambda": {
            "successor_mod_6_unitary": compile_source_lambda(6, "succ").matrix().is_unitary(),
            "multiply_2_mod_5_unitary": compile_source_lambda(5, "prime_mul", 2).matrix().is_unitary(),
            "multiply_2_mod_6_unitary": compile_source_lambda(6, "prime_mul", 2).matrix().is_unitary(),
        },
        "coherent_cancellation_amplitude": cancellation.path_sum(0, 0).real,
        "discarding_measurement_record_changes_wilson_expectation": {"before": before, "after": after},
        "full_4d_yang_mills_reproduced": False,
        "physical_mass_gap_proved": False,
        "arithmetic_source_identified_with_wilson_source": False,
        "quantum_speedup_claimed": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), default=str, indent=2, sort_keys=True))
