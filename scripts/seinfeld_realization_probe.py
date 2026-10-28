#!/usr/bin/env python3
"""Replay exact retained-null, inverse-revelation and field-feedback receipts.

All sample values are rational or evaluated cyclotomic coordinates. Universal
claims have separate paper proofs. Verification regenerates the complete
canonical receipt, including the implementation/source hashes and scope flags.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import hashlib
import itertools
import json
from math import comb
from pathlib import Path

from observational_succ.beck_chevalley_source import finite_map
from observational_succ.lambda_source_duality import Cyclo16, original_history
from observational_succ.seinfeld_disintegration import (
    DYADIC_MODES, DyadicFourier, authentic_branch_law, branch_channels,
    branch_law, disintegrate_law, labelled_character_pairing,
)
from observational_succ.path_likelihood import (
    adaptive_coboundary_control, authentic_inverse_window,
    inverse_phase_certificate, path_likelihood_certificate,
    smooth_selector_obstruction,
)
from observational_succ.path_field_feedback import (
    TwoArmField, authenticated_bbp_factor_character, branch_path_probability,
    factor_character_modulus_lower_bound, static_beta_path_probability,
)
from observational_succ.succ_internal_matrix_walk import PhasePoly
from observational_succ.exponential_gamma_bridge import (
    bbp_euler_tail_bridge, euler_remainder_interval, finite_beta_moment,
    finite_beta_survival, golden_gamma_offset_interval,
)
from observational_succ.euler_mascheroni_succ import harmonic_prefix

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'research/2026-10-26/seinfeld_realization_validation/exact_receipt.json'
BASE = '79344c62c39c96755b742700b3d4d22fa60d86da'


def source_hashes():
    paths = (
        'observational_succ/seinfeld_succ.py',
        'observational_succ/beck_chevalley_source.py',
        'observational_succ/shadow_source_inference.py',
        'observational_succ/bidirectional_source_histories.py',
        'observational_succ/growing_dtn_history.py',
        'observational_succ/succ_internal_matrix_walk.py',
        'observational_succ/lambda_source_duality.py',
        'observational_succ/selected_branch_operator.py',
        'observational_succ/selected_branch_transport.py',
        'observational_succ/seinfeld_disintegration.py',
        'observational_succ/path_likelihood.py',
        'observational_succ/path_field_feedback.py',
        'observational_succ/exponential_gamma_bridge.py',
        'observational_succ/euler_mascheroni_succ.py',
        'tests/test_seinfeld_disintegration.py',
        'tests/test_path_likelihood.py',
        'tests/test_path_field_feedback.py',
        'scripts/seinfeld_realization_probe.py',
        'research/2026-10-26/seinfeld_revelation_oracle.py',
    )
    return {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}


def rejected(action):
    try:
        action()
    except ValueError:
        return True
    raise ArithmeticError('a deliberately unauthenticated input was accepted')


def posterior_bridge_receipt():
    """Connect the native beta/Gamma family to retained finite path inference.

    The model is a static uniform latent bias and conditionally iid letters.
    Density/predictive checks below use independent exact polynomial integrals.
    The paper proves the logarithmic hazard transform; no numerical exponential
    or gamma value is smuggled into this rational finite receipt.
    """
    rows, moment_checks, polynomial_checks = [], 0, 0
    for m in (1, 2, 3, 7, 16, 31, 97, 257):
        prefix = 'R'*(m-1)
        evidence = branch_path_probability(prefix, 'reinforced')
        next_evidence = branch_path_probability(prefix+'R', 'reinforced')
        predictive_r = next_evidence/evidence
        if evidence != Q(1, m) or predictive_r != Q(m, m+1):
            raise ArithmeticError('native path law did not yield the stated posterior evidence')
        for k in range(9):
            left = finite_beta_moment(m+1, k)
            right = (Q(m+1, m)**k/predictive_r *
                     (finite_beta_moment(m, k)-finite_beta_moment(m, k+1)/m))
            if left != right:
                raise ArithmeticError('posterior reweight/rescale successor failed')
            moment_checks += 1
        if m <= 31:
            for k in range(7):
                direct = sum((Q((-1)**j*comb(m-1, j)*m**(k+1), k+j+1)
                              for j in range(m)), Q())
                if direct != finite_beta_moment(m, k):
                    raise ArithmeticError('independent posterior density integral failed')
                polynomial_checks += 1
        changed_prior_evidence = branch_path_probability(prefix, 'reinforced', alpha=2, beta=1)
        if changed_prior_evidence != Q(2, m*(m+1)):
            raise ArithmeticError('changed-prior discriminator failed')
        row = {
            'm': m, 'number_observed_R': m-1, 'predictive_prefix_probability': evidence,
            'known_fair_prefix_probability': Q(1, 2**(m-1)),
            'next_R_probability': predictive_r,
            'scaled_posterior_mean': finite_beta_moment(m, 1),
            'scaled_posterior_second_moment': finite_beta_moment(m, 2),
            'scaled_posterior_survival_at_1': finite_beta_survival(m, 1),
            'log_mean_expression': {'log_m_coefficient': 1, 'rational_part': -harmonic_prefix(m)},
            'latent_KL_expression': {'log_m_coefficient': 1, 'rational_part': -Q(m-1, m)},
            'full_event_KL_minus_latent_KL': Q(m-1, m),
            'log_linearization_gap_interval': euler_remainder_interval(m),
            'changed_prior_alpha_2_prefix_probability': changed_prior_evidence,
            'changed_prior_alpha_2_scaled_mean': Q(2*m, m+2),
        }
        if m >= 2:
            row['shared_coin_prefix_probability'] = Q(1, 2)
            row['shared_coin_scaled_mean'] = Q(m, 3)
            row['selected_prefix_or_posterior_laws_differ'] = m > 2
            if (row['shared_coin_prefix_probability'] != evidence) != (m > 2):
                raise ArithmeticError('conditional-iid hostile control failed')
        rows.append(row)
    hazard = []
    for m in (1, 2, 3, 7, 17):
        for q in (0, 1, m, 2*m):
            degree = m+q-1
            direct = sum((Q(m*(-1)**j*comb(degree, j), j+1)
                          for j in range(degree+1)), Q())
            if direct != Q(m, m+q):
                raise ArithmeticError('posterior hazard/predictive reciprocal identity failed')
            future_ratio = branch_path_probability('R'*(m+q-1), 'reinforced') / \
                branch_path_probability('R'*(m-1), 'reinforced')
            if future_ratio != direct:
                raise ArithmeticError('future-prefix conditioning did not match hazard Laplace sample')
            hazard.append({'m': m, 'integer_future_count': q, 'hazard_laplace_argument': Q(q, m),
                           'posterior_expectation_of_one_minus_theta_power_q': direct})
    inherited_bridge = [bbp_euler_tail_bridge(m, 12) for m in (1, 7, 31, 97, 257)]
    # Keep the SAME Z=-4 log(1-theta) coordinate when changing the model.
    # Exact integration of C*theta**(a-1)*(1-theta)**(b-1+q), with q=4.
    mutants = []
    for name, a, b, normalizer, expected in (
            ('uniform_prior_conditional_iid', 1, 4, 4, Q(1, 2)),
            ('shared_coin_dependence', 1, 2, 2, Q(1, 3)),
            ('beta_2_1_prior_conditional_iid', 2, 4, 20, Q(5, 18))):
        degree = b+3
        direct = sum((Q(normalizer*(-1)**j*comb(degree, j), a+j)
                      for j in range(degree+1)), Q())
        if direct != expected:
            raise ArithmeticError('fixed-coordinate posterior mutant integral failed')
        mutants.append({'model': name, 'm': 4, 's': Q(1),
                        'same_coordinate_hazard_laplace': direct})
    return {
        'model': 'static Uniform(0,1) bias; conditionally iid letters; R probability 1-theta',
        'posterior_family': 'Theta | R^(m-1) is Beta(1,m); X_m=m*Theta',
        'exact_log_coordinate': 'Z_m=-m*log(1-Theta) is Exp(1) under each finite posterior',
        'log_coordinate_gap': 'E(log Z_m-log X_m)=H_m-log(m)-gamma',
        'rows': rows, 'moment_successor_equalities': moment_checks,
        'independent_density_integrals': polynomial_checks,
        'independent_hazard_predictive_checks': hazard,
        'fixed_hazard_coordinate_mutants': mutants,
        'inherited_authentic_tail_bridges': inherited_bridge,
        'inherited_oily_offset_interval': golden_gamma_offset_interval(),
        'scaled_limit_c_2_positive_laplace_fixed_point': Q(1, 2),
        'same_latent_theta_sample_path_convergence_asserted': False,
        'infinite_all_R_event_positive_probability': False,
        'bbp_stochastic_path_law_authenticated': False,
        'new_selected_cancellation_bound': False,
    }


def certificate():
    projection = finite_map(('a0', 'a1', 'a2', 'b0', 'b1'),
                            ('A', 'B', 'empty'), lambda x: x[0].upper())
    weights = (Q(1, 4), Q(1, 8), Q(1, 8), Q(1, 6), Q(1, 3))
    split = disintegrate_law(projection, weights, source_id='receipt:unequal-fibres')
    if split.reconstruct() != weights:
        raise ArithmeticError('retained null residual did not reconstruct the law')
    null_example = {
        'weights': weights, 'marginal': split.marginal,
        'uniform_lift': split.uniform_lift(), 'null_residual': split.residual,
        'null_dimension_over_Q': split.null_dimension,
        'noncoarse_indicator_pairing': split.observable((1, 0, 0, 0, 0)),
    }

    codecs = []
    for selected in range(16):
        row = tuple(Q(int(j == selected)) for j in range(16))
        packet = DyadicFourier.from_weights(row)
        if packet.reconstruct() != row or packet.stratum_energies() != (8, 4, 2, 1):
            raise ArithmeticError('Dirac Fourier codec/control failed')
        codecs.append({'selected': selected, 'coordinates': packet.coordinates,
                       'stratum_energies': packet.stratum_energies()})
    omissions = []
    for omitted in DYADIC_MODES:
        half = 8//omitted
        direction = tuple(Q(1 if j % (2*half) == 0 else
                            -1 if j % (2*half) == half else 0) for j in range(16))
        plus, minus = (tuple(Q(1, 16)+sign*x/32 for x in direction)
                       for sign in (1, -1))
        p, q = (DyadicFourier.from_weights(row) for row in (plus, minus))
        changed = tuple(h for h in DYADIC_MODES if p.character(h) != q.character(h))
        if changed != (omitted,) or min(plus+minus) <= 0:
            raise ArithmeticError('omitted-stratum positive alias failed')
        omissions.append({'omitted_mode': omitted, 'plus': plus, 'minus': minus,
                          'changed_modes': changed})

    states = original_history(89)
    law = authentic_branch_law(states[:3])
    labels = law.projection.codomain
    swapped = (labels[1].digit, labels[0].digit)
    alternative = branch_law(labels, tuple(tuple(Q(1, 2) if j == digit else Q()
                              for j in range(16)) for digit in swapped),
                             source_id='declared:changed-source-selector')
    if any(labelled_character_pairing(law, h, (1, 1)) !=
           labelled_character_pairing(alternative, h, (1, 1)) for h in range(16)):
        raise ArithmeticError('swapped coupling did not preserve the branch marginal')
    ghosts = tuple((digit+w.remainder)/16 for digit, w in zip(swapped, labels))
    if any(x.denominator % 2 for x in ghosts):
        raise ArithmeticError('swapped selector unexpectedly preserved odd support')
    tail_difference = (labels[1].remainder-labels[0].remainder)/16
    nonzero_character_difference = (
        (labels[1].digit-labels[0].digit) % 16 != 0 and tail_difference % 1 != 0)
    if not nonzero_character_difference:
        raise ArithmeticError('symbolic full-character coupling control failed')
    source_coupling = {
        'index_convention': 'current positive time n; forcing is r(n+1)',
        'authentic_rows': [{'index': w.source_index, 'digit': w.digit,
                           'tail': w.remainder, 'current': w.current,
                           'forcing': w.forcing} for w in labels],
        'changed_predecessors': ghosts,
        'same_source_marginal': law.marginal == alternative.marginal,
        'same_all_branch_modes': True,
        'signed_branch_pairing': labelled_character_pairing(law, 1, (1, -1)).coefficients,
        'changed_signed_pairing': labelled_character_pairing(
            alternative, 1, (1, -1)).coefficients,
        'full_character_difference_factorization_nonzero': nonzero_character_difference,
        'tail_phase_difference': tail_difference,
        'changed_history_authenticated': False,
    }

    words = tuple(itertools.product((0, 1), repeat=2))
    innovation = path_likelihood_certificate(
        dict.fromkeys(words, Q(1, 4)), {(0, 0): Q(1)},
        dict(zip(words, map(Q, (0, 2, -1, -1)))))
    if tuple(row.signed_pairing for row in innovation.innovations) != (1, -1):
        raise ArithmeticError('signed-covariance cancellation control failed')

    resolution = []
    for frequency in (0, 1, 2, 4, 8, 16, 24, 128, 256, -8):
        c = inverse_phase_certificate(2, 8, frequency, 173, Q(7, 15))
        resolution.append({k: c[k] for k in (
            'frequency', 'first_observable_level', 'selected_phase',
            'selected_chi_square', 'initial_phase_amplitude')})
    source_windows = []
    for start, steps in ((0, 1), (1, 3), (7, 5), (31, 9), (64, 17)):
        for frequency in (1, 2, 8, 16, -17, 257):
            hex_cert = authentic_inverse_window(states, start, steps, frequency)
            bit_cert = authentic_inverse_window(states, start, steps, frequency, binary=True)
            if hex_cert['selected_phase'] != bit_cert['selected_phase']:
                raise ArithmeticError('binary/hex selected characters disagree')
            source_windows.append({
                'start': start, 'steps': steps, 'frequency': frequency,
                'tail': hex_cert['tail'], 'selected_index': hex_cert['selected_index'],
                'selected_phase': hex_cert['selected_phase'],
                'macro_revelation': hex_cert['first_observable_level'],
                'binary_revelation': bit_cert['first_observable_level'],
                'source_authenticated': True,
            })
    huge = inverse_phase_certificate(16, 128, 1, 16**127+123, Q(2, 15))
    smooth = [smooth_selector_obstruction(m, h, Q(3, 2))
              for m, h in ((17, 1), (101, -3), (1009, 8))]

    field_cases = []
    for model in ('fixed', 'reinforced', 'harmonic'):
        field_cases.append({'model': model, 'LL': branch_path_probability('LL', model),
                            'LR': branch_path_probability('LR', model),
                            'LLR': branch_path_probability('LLR', model),
                            'LRL': branch_path_probability('LRL', model)})
    beta_cases = 0
    for depth in range(8):
        for letters in itertools.product('LR', repeat=depth):
            word = ''.join(letters)
            for alpha, beta in ((Q(1), Q(1)), (Q(2, 3), Q(7, 5))):
                if branch_path_probability(word, 'reinforced', alpha=alpha, beta=beta) != \
                        static_beta_path_probability(word, alpha, beta):
                    raise ArithmeticError('reinforcement/static-Beta path law mismatch')
                beta_cases += 1

    factors = []
    for index in (1, 2, 7, 16, 32, 64, 89):
        for h in (1, 8, 17):
            target = states[index-1]
            c = authenticated_bbp_factor_character(states, index, (Q(2, 5), Q(3, 5)),
                                                   (target, target), h)
            if c.factor.character_square != PhasePoly.one():
                raise ArithmeticError('authenticated deterministic character changed')
            factors.append({'index': index, 'h': h, 'conditional_modulus_squared': Q(1)})
    leaked = [{'leakage': epsilon, 'modulus_lower': factor_character_modulus_lower_bound(
                    (1-epsilon, epsilon), (Q(), Q(1, 2)), Q())}
              for epsilon in (Q(), Q(1, 7), Q(1, 3), Q(1, 2), Q(3, 4))]
    altered = tuple(u+Q(16**n, 7) for n, u in enumerate(states, 1))
    source_rejections = {
        'changed_seed_disintegration': rejected(lambda: authentic_branch_law(altered)),
        'changed_seed_revelation': rejected(lambda: authentic_inverse_window(altered, 7, 3, 1)),
        'changed_seed_factor': rejected(lambda: authenticated_bbp_factor_character(
            altered, 7, (1,), (altered[6],), 1)),
        'changed_projected_successor': rejected(lambda: authenticated_bbp_factor_character(
            states, 7, (Q(1, 2), Q(1, 2)), (states[6], states[6]+Q(1, 16)), 1)),
    }
    return {
        'schema': 'succ.seinfeld-realization.exact.v1', 'parent_pr': 313, 'parent_sha': BASE,
        'source_hashes': source_hashes(), 'null_residual_example': null_example,
        'fourier_codec': {'rational_dimensions': [8, 4, 2, 1],
                          'dirac_rows': codecs, 'positive_omission_controls': omissions},
        'authentic_coupling_control': source_coupling,
        'signed_likelihood_innovations': innovation,
        'binary_revelation_table': resolution, 'authentic_inverse_windows': source_windows,
        'compact_large_fiber': {'fiber_size': huge['fiber_size'],
                               'certificate_rows': len(huge['levels']),
                               'first_observable_level': huge['first_observable_level']},
        'all_odd_carrier_continuous_obstruction': smooth,
        'field_comparison': field_cases,
        'field_after_L': {'next_left': TwoArmField(3, 1, 0).next_left,
                          'currents': TwoArmField(3, 1, 0).currents},
        'posterior_golden_gamma_bridge': posterior_bridge_receipt(),
        'reinforcement_static_beta_equalities': beta_cases,
        'authenticated_deterministic_factors': factors, 'leakage_bounds': leaked,
        'factor_index_convention': 'literal forcing n; transition U_(n-1) to U_n',
        'source_mutations_rejected': source_rejections,
        'adaptive_phase_controls': [adaptive_coboundary_control(n, p)
                                    for n, p in ((1, Q(3, 4)), (8, Q(3, 4)),
                                                 (19, Q(1, 2)), (19, Q(1, 3)))],
        'authority': {'finite_receipt': 'EXACT FINITE', 'universal_claims': 'SEPARATE PAPER PROOFS',
                      'new_lean_formalization': False, 'external_peer_review': False},
        'averaging_alone_invertible': False,
        'feedback_law_identified_from_observation_alone': False,
        'arithmetic_stochastic_feedback_authenticated': False,
        'oily_offset_proved_cancellation_invariant': False,
        'selected_weyl_saving_proved': False, 'pi_normality_proved': False,
    }


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(f'no exact receipt encoding for {type(value).__name__}')


def render():
    return json.dumps(certificate(), indent=2, sort_keys=True, default=encode)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--write', action='store_true')
    action.add_argument('--verify', action='store_true')
    parser.add_argument('--path', type=Path, default=DEFAULT)
    args = parser.parse_args()
    expected = render()
    if args.write:
        args.path.parent.mkdir(parents=True, exist_ok=True)
        args.path.write_text(expected)
        print(json.dumps({'status': 'written', 'path': str(args.path)}))
    else:
        if args.path.read_text() != expected:
            raise SystemExit('REJECTED: receipt differs from exact regeneration/source hashes/scope')
        print(json.dumps({'status': 'verified', 'schema': 'succ.seinfeld-realization.exact.v1',
                          'selected_weyl_saving_proved': False}))


if __name__ == '__main__':
    main()
