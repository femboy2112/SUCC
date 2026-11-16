#!/usr/bin/env python3
"""Deterministic exact receipts for the coupled finite SU(2) construction."""
from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.ym_coupled_wilson import (
    LinkGraph, build_wilson_certificate, factorwise_density, haar_integral,
    link_quaternion, sphere_monomial_moment, wilson_expectation, word_trace,
)
from observational_succ.ym_reflection_bridge import haar_moment_recurrence
from observational_succ.ym_reflection_order import (
    even_taylor_character_coefficients, factorwise_expectation_error,
    global_square_witness, su2_character,
)
from observational_succ.ym_trace_observer import (
    conjugate_tuple, same_gauge_orbit, stereographic_unit, trace_bank,
)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def main():
    degrees = (*range(21), 24, 30, 38)
    moments = {}
    for degree in degrees:
        value = sphere_monomial_moment((degree, 0, 0, 0))
        assert value == haar_moment_recurrence(degree)
        moments[degree] = value

    coefficient_checks = 0
    from math import factorial
    for beta in (Q(0), Q(1, 3), Q(1), Q(5, 2)):
        for degree in (0, 2, 4, 6, 10):
            coefficients = even_taylor_character_coefficients(beta, degree)
            assert min(coefficients) >= 0
            reconstructed = [Q(0)] * (degree + 1)
            for j, coefficient in enumerate(coefficients):
                for k, monomial in enumerate(su2_character(j)):
                    reconstructed[k] += coefficient * monomial
            assert reconstructed == [beta**j / factorial(j) for j in range(degree + 1)]
            coefficient_checks += 1

    graph = LinkGraph(1, ((0, 0), (0, 0)))
    x, y = link_quaternion(2, 0)[0], link_quaternion(2, 1)[0]
    z, t = word_trace(2, (1, 2)), word_trace(2, (1, -2))
    density = factorwise_density(graph, ((1, 2), (1, -2)), (Q(1, 2), Q(1, 3)), (2, 2))
    pair = wilson_expectation(graph, ((1, 2),), (Q(1, 2),), (2,), x*y)
    assert pair == Q(1, 33)
    assert haar_integral(x*y*z) == Q(1, 16)
    assert haar_integral(z*t) == Q(-1, 8)
    cert = build_wilson_certificate(graph, ((1, 2),), (Q(1, 8),), z, Q(1, 100))
    assert cert.error_bound <= cert.tolerance
    assert cert.error_bound == factorwise_expectation_error(
        cert.betas, cert.degrees, z.coefficient_bound)

    sources = tuple(stereographic_unit(t) for t in ((1, 2, 3), (2, -1, 1), (0, 3, -2)))
    original_bank = trace_bank(sources)
    for triple in ((1, 1, 2), (-2, 1, 0)):
        transformed = conjugate_tuple(sources, stereographic_unit(triple))
        assert trace_bank(transformed) == original_bank
        assert same_gauge_orbit(sources, transformed)
    witness = global_square_witness()
    assert witness['reflected_square'] == -1

    report = {
        'scope': 'Exact finite SU(2) calculations; no continuum or mass-gap certificate',
        'status': 'passed',
        'sphere_moments': moments,
        'character_reconstruction_cases': coefficient_checks,
        'coupled_source': {
            'haar_xyz': haar_integral(x*y*z), 'haar_zt': haar_integral(z*t),
            'two_factor_partition': haar_integral(density),
            'individual_product_expectation': pair,
            'individual_expectations': [wilson_expectation(graph, ((1, 2),),
                (Q(1, 2),), (2,), obs) for obs in (x, y)],
        },
        'certificate': {
            'betas': cert.betas, 'degrees': cert.degrees,
            'partition': cert.partition, 'expectation': cert.expectation,
            'density_terms': cert.density_terms, 'tolerance': cert.tolerance,
            'error_bound': cert.error_bound,
        },
        'fresh_trace_conjugations': 2,
        'global_square_rp_counterexample': witness,
    }
    print(json.dumps(encode(report), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
