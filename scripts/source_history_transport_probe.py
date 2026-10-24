#!/usr/bin/env python3
"""Exact receipt for preregistered BBP circle-transport measurements.

All nine p/J rows are retained. Small equal-weight measures are independently
calibrated by enumerating every matching permutation. No floats, fitted rate,
or asymptotic source-preservation assertion enters the certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations_with_replacement, product
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from observational_succ.pi_source_collision import prime_window  # noqa: E402
from observational_succ.source_history_stationarity import (  # noqa: E402
    PositiveHistoryMixture, apply_history_filter,
)
from observational_succ.source_history_transport import (  # noqa: E402
    AtomicProbability, PREREGISTERED_HISTORY_DEPTHS, PREREGISTERED_PRIMES,
    bbp_history_transport_rows, brute_force_equal_weight_w1, circle_w1,
    circle_w1_certificate, empirical_law, history_preservation_certificate,
    multiplication_pushforward, validate_circle_w1_certificate,
)


def _json(value):
    if isinstance(value, Q):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    if isinstance(value, dict):
        return {str(key): _json(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json(item) for item in value]
    return value


def _decimal_bracket(value, places=8):
    """Outward decimal enclosure using integer arithmetic, never rounding."""
    scale = 10**places
    quotient, remainder = divmod(value.numerator*scale, value.denominator)
    def format_scaled(integer):
        whole, digits = divmod(integer, scale)
        return f'{whole}.{digits:0{places}d}'
    return {'lower': format_scaled(quotient),
            'upper': format_scaled(quotient+bool(remainder)),
            'method': 'exact integer floor/ceiling'}


def build_receipt():
    comparisons = assignments = 0
    for modulus, sizes in ((3, (1, 2, 3)), (5, (2,))):
        points = tuple(Q(j, modulus) for j in range(modulus))
        for size in sizes:
            supports = tuple(combinations_with_replacement(points, size))
            for first, second in product(supports, repeat=2):
                oracle = brute_force_equal_weight_w1(first, second)
                mu, nu = empirical_law(first), empirical_law(second)
                cert = circle_w1_certificate(mu, nu)
                assert oracle['cost'] == cert.cost
                assert validate_circle_w1_certificate(mu, nu, cert)
                comparisons += 1
                assignments += oracle['assignments_enumerated']
    assert comparisons == 370 and assignments == 1131

    holdouts = (
        ((0, Q(1, 7), Q(3, 5), Q(9, 10)),
         (Q(1, 6), Q(2, 7), Q(8, 9), Q(11, 12))),
        ((0, 0, Q(1, 2), Q(1, 2), Q(7, 8)),
         (Q(1, 10), Q(1, 5), Q(1, 5), Q(4, 5), Q(9, 10))),
        ((Q(-1, 10), 0, Q(1, 11), Q(2, 3), Q(4, 5), Q(8, 7)),
         (Q(1, 13), Q(1, 7), Q(3, 8), Q(5, 11), Q(9, 10), Q(13, 10))),
        ((0, 0, 0, Q(1, 3), Q(1, 3), Q(4, 5)),
         (Q(9, 10), Q(9, 10), Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 2))),
    )
    holdout_rows = []
    for first, second in holdouts:
        oracle = brute_force_equal_weight_w1(first, second)
        mu, nu = empirical_law(first), empirical_law(second)
        cert = circle_w1_certificate(mu, nu)
        assert oracle['cost'] == cert.cost
        assert validate_circle_w1_certificate(mu, nu, cert)
        comparisons += 1
        assignments += oracle['assignments_enumerated']
        holdout_rows.append(oracle)
    assert comparisons == 374 and assignments == 2715

    # All new source measurements occur only after the fixed small calibration.
    rows = bbp_history_transport_rows()
    assert tuple((row['prime'], row['history_depth']) for row in rows) == tuple(
        product(PREREGISTERED_PRIMES, PREREGISTERED_HISTORY_DEPTHS))
    for row in rows:
        if row['history_depth'] == 2:
            assert row['epsilon']*2 == row['beta']
        assert row['beta'] <= row['exact_bound'] <= row['universal_bound']
        assert row['averaged_one_step_defect'] == row['exact_boundary_term']
        row['decimal_enclosures'] = {
            name: _decimal_bracket(row[name])
            for name in ('beta', 'epsilon', 'exact_boundary_term',
                         'exact_bound', 'universal_bound',
                         'true_orbit_beta_error_upper',
                         'true_orbit_epsilon_error_upper')}

    # Direct literal four-pole authentication, separately from the imported
    # source constructor; hash the actual measured states, not supplied digits.
    last = 4*((max(PREREGISTERED_PRIMES)-1)//8)
    state, independent = Q(), [Q()]
    for n in range(1, last+1):
        state = (16*state+Q(4, 8*n-7)-Q(2, 8*n-4)
                 -Q(1, 8*n-3)-Q(1, 8*n-2)) % 1
        independent.append(state)
    source_windows = []
    for p in PREREGISTERED_PRIMES:
        window = prime_window(p)
        assert tuple(independent[window.start+1:4*window.start+1]) == window.states
        assert all(x.denominator % 2 for x in window.states)
        encoded = '\n'.join(f'{x.numerator}/{x.denominator}'
                            for x in window.states).encode('ascii')
        source_windows.append({
            'prime': p, 'length': window.length,
            'first_state_index': window.start+1,
            'last_state_index': 4*window.start,
            'canonical_state_sequence_sha256': sha256(encoded).hexdigest(),
            'positive_bbp_tail_upper': window.tail_bound,
            'literal_four_pole_authentication': True,
            'all_reduced_denominators_odd': True})

    constant_rows = []
    for point, depth in product((Q(), Q(1, 2)), PREREGISTERED_HISTORY_DEPTHS):
        cert = history_preservation_certificate(empirical_law((point,)), depth)
        assert cert['beta'] == cert['epsilon'] == 0
        constant_rows.append({'point': point, **cert, 'haar': False})

    base16_fixed = history_preservation_certificate(empirical_law((Q(1, 5),)), 4)
    assert base16_fixed['beta'] == Q(2, 5)
    assert base16_fixed['epsilon'] == Q(1, 4)

    weights = (Q(), Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8))
    signed_coefficients = (Q(), Q(1), Q(1), Q(-1))
    output = apply_history_filter(weights, 3, signed_coefficients)
    assert output == weights
    mu = AtomicProbability(tuple((Q(j, 5), mass) for j, mass in enumerate(weights)))
    assert multiplication_pushforward(mu, 16) == mu
    signed_beta = circle_w1(multiplication_pushforward(mu), mu)
    assert signed_beta == Q(1, 10)
    try:
        PositiveHistoryMixture(signed_coefficients)
    except ValueError:
        signed_rejected = True
    else:
        raise AssertionError('signed history coefficients accepted as a positive average')

    wrap_circle = circle_w1(empirical_law((0,)), empirical_law((Q(9, 10),)))
    assert wrap_circle == Q(1, 10) and wrap_circle != Q(9, 10)
    source_files = (
        'observational_succ/source_history_transport.py',
        'tests/test_source_history_transport.py',
        'scripts/source_history_transport_probe.py',
        'observational_succ/pi_source_collision.py',
        'observational_succ/source_history_stationarity.py',
        'research/2026-10-24/PI_PATH_SELECTION_HOLE_CONTRACT.md',
    )
    hashes = {name: sha256((REPOSITORY_ROOT/name).read_bytes()).hexdigest()
              for name in source_files}
    return {
        'status': 'VERIFIED_FINITE',
        'scope': 'optimal circle W1 and conditional history-preservation bridge',
        'pi_normality': 'OPEN',
        'authentic_history_preservation_asymptotic': 'OPEN',
        'fitted_decay_rate': None,
        'floating_point_used': False,
        'circle_cost_definition': 'min_c integral_0^1 |F_mu-F_nu-c| dx',
        'exact_dual_witness': 'periodic piecewise-linear 1-Lipschitz potential',
        'bridge': 'beta <= 4 epsilon + W1(U^J mu,mu)/J <= 4 epsilon + 1/(2J)',
        'j2_identity': 'epsilon = beta/2',
        'assignment_calibration': {
            'comparisons': comparisons,
            'matching_permutations_actually_enumerated': assignments,
            'grid_comparisons': 370, 'grid_matching_permutations': 1131,
            'unequal_spacing_or_repeated_mass_holdouts': holdout_rows},
        'line_surrogate_control': {
            'first_point': Q(), 'second_point': Q(9, 10),
            'optimal_circle_cost': wrap_circle, 'sorted_line_cost': Q(9, 10),
            'sorted_line_cost_rejected_as_circle_cost': True},
        'preregistered_source_windows': source_windows,
        'preregistered_history_depths': PREREGISTERED_HISTORY_DEPTHS,
        'all_nine_rows': rows,
        'constant_controls': constant_rows,
        'base16_fixed_point_tripling_obstruction': base16_fixed,
        'signed_q5_control': {
            'weights': weights, 'signed_filter': signed_coefficients,
            'filter_output': output, 'signed_filter_preserves_measure': True,
            'tripling_circle_w1': signed_beta,
            'positive_history_class_rejects_signed_filter': signed_rejected,
            'positive_j4_certificate': history_preservation_certificate(mu, 4)},
        'source_sha256': hashes,
    }


if __name__ == '__main__':
    print(json.dumps(_json(build_receipt()), indent=2, sort_keys=True))
