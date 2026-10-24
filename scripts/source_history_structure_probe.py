#!/usr/bin/env python3
"""POST_DISCOVERY exact controls for raw amplitudes and fast history depth.

These bounded, source-blind controls do not establish any BBP statistical
premise. Raw (path,dual) tuples and terminal-pair marginals are enumerated
literally. Infinite extension and varying-carrier conclusions remain paper
statements; no infinite conclusion is inferred from these finite samples.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from observational_succ.source_history_transport import (  # noqa: E402
    AtomicProbability, circle_w1, circle_w1_certificate, empirical_law,
    history_average, multiplication_pushforward,
    validate_circle_w1_certificate,
)
from observational_succ.source_path_projector import character_sum  # noqa: E402


def _json(value):
    if isinstance(value, Q):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    if isinstance(value, dict):
        return {str(key): _json(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json(item) for item in value]
    return value


def _prime_root_sum(q, exponents, weight):
    """Independent Phi_q=1+z+...+z^(q-1) reduction for q=3 or5."""
    assert q in (3, 5)
    histogram = [0]*q
    for exponent in exponents:
        histogram[exponent % q] += 1
    result = tuple(weight*(histogram[j]-histogram[-1]) for j in range(q-1))
    assert result == character_sum(q, tuple(exponents), (weight,)*len(exponents))
    return result


def _raw_exponent(q, path, dual, increments, base=16, initial=1):
    assert len(path) == len(dual) == len(increments)+1
    exponent = dual[0]*(path[0]-initial)
    for j, increment in enumerate(increments, start=1):
        exponent += dual[j]*(path[j]-base*path[j-1]-increment)
    return exponent % q


def _raw_projector_row(q, horizon):
    source = tuple(j*j+1 for j in range(1, horizon+1))
    atom_modulus = Q(1, q**(horizon+1))
    exponents = []
    projected_paths = []
    selected = [1]
    for increment in source:
        selected.append((16*selected[-1]+increment) % q)
    selected = tuple(selected)
    atom_count = 0
    for path in product(range(q), repeat=horizon+1):
        path_exponents = []
        for dual in product(range(q), repeat=horizon+1):
            exponent = _raw_exponent(q, path, dual, source)
            path_exponents.append(exponent)
            exponents.append(exponent)
            atom_count += 1
        projected = _prime_root_sum(q, path_exponents, atom_modulus)
        expected = (Q(path == selected),)+(Q(),)*(q-2)
        assert projected == expected
        projected_paths.append({'path': path, 'dual_sum_coefficients': projected})
    total_mass = _prime_root_sum(q, exponents, atom_modulus)
    assert total_mass == (Q(1),)+(Q(),)*(q-2)
    assert atom_count == q**(2*(horizon+1))
    # Each character has complex modulus1. This is count times the common
    # ATOM modulus, not the l1 norm of reduced cyclotomic coefficients.
    variation = atom_count*atom_modulus
    assert variation == q**(horizon+1)

    marginal_rows = []
    marginal_terms = 0
    if horizon:
        for prefix_path in product(range(q), repeat=horizon):
            for prefix_dual in product(range(q), repeat=horizon):
                terminal_exponents = []
                for terminal_state, terminal_dual in product(range(q), repeat=2):
                    terminal_exponents.append(_raw_exponent(
                        q, prefix_path+(terminal_state,), prefix_dual+(terminal_dual,), source))
                    marginal_terms += 1
                actual = _prime_root_sum(q, terminal_exponents, atom_modulus)
                prefix_exponent = _raw_exponent(q, prefix_path, prefix_dual, source[:-1])
                expected = _prime_root_sum(q, (prefix_exponent,), Q(1, q**horizon))
                assert actual == expected
                marginal_rows.append({
                    'prefix_path': prefix_path, 'prefix_dual': prefix_dual,
                    'literal_terminal_pair_sum': actual,
                    'preceding_raw_atom': expected})
        assert len(marginal_rows) == q**(2*horizon)
        assert marginal_terms == q**(2*(horizon+1))
    return {
        'modulus': q, 'horizon': horizon, 'base': 16, 'initial': 1,
        'source_prefix': source, 'source_blind_control': True,
        'joint_path_dual_atoms_actually_enumerated': atom_count,
        'joint_phase_histogram': dict(sorted(Counter(exponents).items())),
        'individual_complex_atom_modulus': atom_modulus,
        'cyclotomic_total_mass_coefficients': total_mass,
        'total_variation_count_times_atom_modulus': variation,
        'selected_path': selected, 'all_dual_projected_path_weights': projected_paths,
        'literal_terminal_marginal_comparisons': len(marginal_rows),
        'terminal_pairs_actually_summed': marginal_terms,
        'terminal_marginal_rows': marginal_rows,
    }


def _fast_history_row(k):
    q, depth = 3**k, k*k
    points = tuple(Q(j, q) for j in range(q))
    mu = empirical_law(points)
    assert multiplication_pushforward(mu, 16) == mu
    once = multiplication_pushforward(mu, 3)
    coarse = empirical_law(tuple(Q(j, q//3) for j in range(q//3)))
    assert once == coarse
    beta_certificate = circle_w1_certificate(once, mu)
    assert validate_circle_w1_certificate(once, mu, beta_certificate)
    beta = beta_certificate.cost

    # A nearest-coarse-grid coupling attains the independent point-to-support
    # lower bound. Each coarse atom receives exactly three fine atoms.
    recipient_counts = Counter()
    coupling_cost = lower_bound = Q()
    coarse_points = tuple(point for point, _ in coarse.atoms)
    for residue, point in enumerate(points):
        recipient = 3*((residue+1)//3) % q
        recipient_counts[recipient] += 1
        distance = abs(point-Q(recipient, q))
        coupling_cost += min(distance, 1-distance)/q
        lower_bound += min(min(abs(point-target), 1-abs(point-target))
                           for target in coarse_points)/q
    assert set(recipient_counts.values()) == {3}
    assert beta == coupling_cost == lower_bound == Q(2, 3**(k+1))

    averaged = history_average(mu, depth, 3)
    decomposition_atoms = []
    for j in range(k):
        remaining_grid = 3**(k-j)
        expected_history = empirical_law(tuple(Q(r, remaining_grid)
                                               for r in range(remaining_grid)))
        assert multiplication_pushforward(mu, 3**j) == expected_history
        decomposition_atoms.extend((point, mass/depth)
                                   for point, mass in expected_history.atoms)
    collapsed_weight = Q(depth-k, depth)
    decomposition_atoms.append((Q(), collapsed_weight))
    assert AtomicProbability(tuple(decomposition_atoms)) == averaged
    delta0 = empirical_law((0,))
    for j in range(k, depth):
        assert multiplication_pushforward(mu, 3**j) == delta0
    epsilon_certificate = circle_w1_certificate(averaged, mu)
    assert validate_circle_w1_certificate(averaged, mu, epsilon_certificate)
    epsilon = epsilon_certificate.cost
    delta_distance = circle_w1(averaged, delta0)
    assert delta_distance <= Q(1, 2*k)
    paper_limit_error_budget = Q(1, 2*k)+Q(1, 4*q)
    assert abs(epsilon-Q(1, 4)) <= paper_limit_error_budget
    return {
        'K': k, 'grid_size': q, 'history_depth': depth,
        'exact_T16_invariance': True,
        'beta': beta, 'nearest_grid_coupling_cost': coupling_cost,
        'point_to_support_lower_bound': lower_bound,
        'epsilon': epsilon,
        'collapsed_history_count': depth-k,
        'delta0_component_weight': collapsed_weight,
        'actual_total_atom_mass_at_zero': dict(averaged.atoms)[Q()],
        'history_decomposition_exact': True,
        'average_to_delta0_distance': delta_distance,
        'absolute_difference_epsilon_to_one_quarter': abs(epsilon-Q(1, 4)),
        'paper_limit_error_budget_checked_at_this_K': paper_limit_error_budget,
        'source_blind_control': True, 'authentic_BBP_window': False,
    }


def build_receipt():
    raw_rows = tuple(_raw_projector_row(q, horizon)
                    for q, horizons in ((3, range(3)), (5, range(2)))
                    for horizon in horizons)
    atom_count = sum(row['joint_path_dual_atoms_actually_enumerated'] for row in raw_rows)
    marginal_count = sum(row['literal_terminal_marginal_comparisons'] for row in raw_rows)
    marginal_terms = sum(row['terminal_pairs_actually_summed'] for row in raw_rows)
    assert (atom_count, marginal_count, marginal_terms) == (1469, 115, 1435)
    history_rows = tuple(_fast_history_row(k) for k in range(1, 5))
    source_files = (
        'scripts/source_history_structure_probe.py',
        'observational_succ/source_history_transport.py',
        'observational_succ/source_path_projector.py',
    )
    return {
        'status': 'POST_DISCOVERY_VERIFIED_FINITE',
        'registration': 'POST_DISCOVERY, not the preregistered nine BBP windows',
        'scope': 'two bounded source-blind structural controls',
        'floating_point_used': False, 'pi_normality': 'OPEN',
        'raw_amplitude_controls': {
            'actual_joint_atoms': atom_count,
            'literal_terminal_marginal_comparisons': marginal_count,
            'terminal_pairs_actually_summed': marginal_terms,
            'rows': raw_rows,
            'infinite_extension_claim_status': 'PAPER_ONLY',
            'varying_BBP_carrier_claim': {
                'status': 'PAPER_ONLY; no varying-carrier Cartesian enumeration',
                'variation_formula': 'D_N^(N+1)',
                'necessary_bound': 'every pushforward marginal has variation at most that of its finite complex parent measure',
                'fixed_q_consistency_not_reused_for_varying_D': True}},
        'fast_history_controls': {
            'rows': history_rows,
            'asymptotic_claim_status': 'PAPER_PROOF_ONLY; not inferred from four finite samples',
            'paper_error_bound': '|epsilon_K-1/4| <= 1/(2K)+1/(4*3^K)',
            'quantifier_guard': 'a prescribed fast history schedule need not preserve a nearly tripling-invariant source law'},
        'source_sha256': {name: sha256((REPOSITORY_ROOT/name).read_bytes()).hexdigest()
                          for name in source_files},
    }


if __name__ == '__main__':
    print(json.dumps(_json(build_receipt()), indent=2, sort_keys=True))
