#!/usr/bin/env python3
"""Deterministic exact finite certificates; never an infinite normality test."""
import argparse
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import cyclotomic_selected_source as c
from observational_succ.bbp_source_memory import forcing
from observational_succ.pi_source_genesis import window_pi_interval, machin_pi_interval


def collapsed_forcing(n):
    """Independently combined common-denominator numerator and odd poles."""
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def box_json(box):
    return {k: str(v) for k, v in asdict(box.outward(52)).items()}


def upper_json(q):
    scale = 2**52
    return str(Q(-((-q*scale)//1), scale))


def run():
    import json
    primes = []
    one = c.ComplexBox(Q(1), Q(1), Q(), Q())
    for p in (17, 41, 73, 97, 113):
        actual = c.prime_window(p)
        m, L = actual.m, actual.period
        for n in range(1, 4*m+1):
            assert collapsed_forcing(n) == forcing(n)
            if n >= m+1:
                independent = sum((16**(n-j)*collapsed_forcing(j)
                                   for j in range(1, n+1)), Q()) % 1
                assert independent == actual.states[n-m-1]
                assert (independent-actual.local[n-m-1]).denominator % p != 0
        spectrum = c.spectral_interference_certificate(actual)
        assert all(z.modulus_squared_upper() <= spectrum['clock']['twist_upper_squared']
                   for z in spectrum['clock']['twisted'])
        assert spectrum['actual'].modulus_squared_upper() < spectrum['interference_upper']**2
        # Incomplete local prefixes, with an exact harmonic-number completion
        # constant (the paper further bounds it by log L).
        prefix = c.ComplexBox(Q(), Q(), Q(), Q())
        harmonic = sum((Q(1, j) for j in range(1, L//2+1)), Q())
        completion = c.sqrt_upper(spectrum['clock']['twist_upper_squared'])*L*harmonic
        prefix_rows = []
        for T in range(1, L+1):
            prefix += c.character_mean([actual.local[T-1]])
            bound = T*spectrum['clock']['zero_mode_upper']+completion
            assert prefix.modulus_squared_upper() <= bound**2
            prefix_rows.append({'length': T, 'signed_sum': box_json(prefix),
                                'completion_upper': upper_json(bound)})
        control = c.dyadic_initial_control(4*m+2)
        changed = c.prime_window(p, control['initial'])
        assert actual.local == changed.local
        low, high = window_pi_interval(control['depth']+8)
        assert max(abs(control['initial']+low/16), abs(control['initial']+high/16)) < Q(1, 2*16**control['depth'])
        full_changed = c.character_mean(changed.states)
        budget = c.coherent_window_error(p, control['depth'], initial_error=control['error_upper'])
        assert (full_changed-one).modulus_squared_upper() < budget**2
        assert full_changed.real_low > Q(99, 100)
        changed_I = c.interference_interval(changed)
        # Same exact local zero mode bounds the block-anchor contribution.
        I_budget = budget+spectrum['clock']['zero_mode_upper']
        assert (changed_I-one).modulus_squared_upper() < I_budget**2
        states_after = c.forced_states(control['depth']+1, control['initial'])
        original_after = c.forced_states(control['depth']+1)
        assert states_after[-2:] == original_after[-2:]
        prime_receipt = {
            'p': p, 'm': m, 'period': L, 'blocks': 3*m//L,
            'good_prime_order_condition': L**3 > p,
            'authentic_initial': '0',
            'authentic_full_window': box_json(c.character_mean(actual.states)),
            'authentic_I': box_json(spectrum['actual']),
            'nonzero_lag_epsilon_upper': str(spectrum['clock']['epsilon']),
            'zero_mode_upper': str(spectrum['clock']['zero_mode_upper']),
            'all_twists_squared_upper': str(spectrum['clock']['twist_upper_squared']),
            'authentic_wiener_upper': upper_json(spectrum['wiener_upper']),
            'authentic_spectral_interference_upper': upper_json(spectrum['interference_upper']),
            'actual_twist_boxes': [box_json(z) for z in spectrum['clock']['twisted']],
            'incomplete_local_prefixes': prefix_rows,
            'changed_initial': str(control['initial']), 'dyadic_depth': control['depth'],
            'least_coalescence_depth': c.coalescence_depth(control['initial']),
            'certified_initial_error_upper': str(control['error_upper']),
            'machin_selector_terms': control['machin_terms'],
            'independent_bbp_selector_depth': control['depth']+8,
            'independent_bbp_selector_verified': True,
            'changed_full_window': box_json(full_changed), 'changed_I': box_json(changed_I),
            'changed_coherence_error_upper': upper_json(budget),
            'changed_I_distance_from_one_upper': upper_json(I_budget),
            'coalescence_checked': True,
            'source_contract': 'exact BBP forcing; changed initial is a finite-window control, not pi',
            'full_source_states': [str(v) for v in actual.states],
            'full_source_complements': [str(v) for v in actual.complement],
        }
        primes.append(prime_receipt)

    profiles = []
    for b, h, mod in ((16, 1, 27), (16, 1, 2**9*27), (6, -9, 2**5*3**4*5),
                       (16, 9, 27), (16, 1, 17*41), (16, 1, 1)):
        profile = c.clock_profile(b, h, mod)
        seen, value, j = {}, h % mod, 0
        while value not in seen:
            seen[value] = j
            j += 1
            value = b*value % mod
        assert profile['transient'] == seen[value]
        assert profile['first_repeat_index'] == j
        profiles.append({'base': b, 'h': h, 'modulus': mod, **profile})
    tomography = []
    for N in (1, 3, 10, 100, 1000):
        mod = c.ternary_tomography_clock(1, N)
        assert len({pow(16, j, mod) for j in range(N)}) == N
        assert 3*N <= mod < 9*N
        tomography.append({'horizon': N, 'sample_clock': mod, 'order': c.order(16, mod)})
    alias = c.fourth_alias_polynomial(16, 1, 3, 27)
    assert alias == {0: 15, -270: 2, 270: 2}

    groups, diagonal = {}, 0
    for a in range(18):
        for b in range(18-a):
            d = 17-a-b
            weight = factorial(17)//(factorial(a)*factorial(b)*factorial(d))
            diagonal += weight**2
            groups.setdefault(a+16*b+256*d, []).append(((a, b, d), weight))
    collisions = [items for items in groups.values() if len(items) > 1]
    assert len(collisions) == 1
    assert {v for v, weight in collisions[0]} == {(16, 0, 1), (0, 17, 0)}
    cross_coefficient = 2*collisions[0][0][1]*collisions[0][1][1]
    assert diagonal == 399769750195965 and cross_coefficient == 34

    carry = []
    for K in range(6):
        for d in (1, 3):
            for n in (0, 1, 5, 20):
                F = (-1)**(K+1)*c.corrected_carry_defect(n, d, K)
                upper = c.corrected_carry_upper(n, d, K)
                assert 0 < F < upper
                # Strict complete-monotonicity checks of the new carry measure.
                differences = []
                for r in range(5):
                    difference = sum(((-1)**j*comb(r, j)*(-1)**(K+1)
                                      *c.corrected_carry_defect(n+j, d, K)
                                      for j in range(r+1)), Q())
                    assert difference > 0
                    differences.append(str(difference))
                carry.append({'order': K, 'lag': d, 'n': n, 'signed_defect': str(F),
                              'strict_upper': str(upper), 'signed_differences': differences})

    # Independent symbolic fibre oracle has no dependency on the new module.
    from cyclotomic_fiber_moment_oracle import run as fiber_run
    fiber = fiber_run()
    variation = []
    for p in (17, 41, 73, 97, 113, 193):
        w = c.prime_window(p)
        L, B = w.period, 3*w.m//w.period
        circle_mean = sum((min((w.complement[t+1]-w.complement[t]) % 1,
                               (w.complement[t]-w.complement[t+1]) % 1)
                           for t in range(3*w.m-1) if (t+1) % L), Q())/B
        lower, upper = 4*circle_mean, Q(44, 7)*circle_mean
        variation.append({'p': p, 'period': L,
                          'exact_mean_circle_variation': str(circle_mean),
                          'chord_variation_lower': str(lower),
                          'chord_variation_upper': str(upper),
                          'outward_integer_lower': lower//1,
                          'outward_integer_upper': -((-upper)//1)})

    # A finite set of typed raw p-adic readouts costs extra dyadic precision.
    M, precision_cost = 17**2*41, 0
    while 16**precision_cost < M:
        precision_cost += 1
    depth = 8+precision_cost+2
    pl, pu = machin_pi_interval(2*depth+20)
    c0 = (-pu*Q(16**depth, 16*M)+Q(1, 2))//1
    c1 = (-pl*Q(16**depth, 16*M)+Q(1, 2))//1
    assert c0 == c1
    delta = Q(M*c0, 16**depth)
    initial_error = max(abs(delta+pl/16), abs(delta+pu/16))
    assert initial_error <= Q(M, 2*16**depth)
    for n in range(depth+2):
        assert (16**n*delta).numerator % M == 0
    changed = c.prime_window(17, delta)
    full = c.character_mean(changed.states)
    budget = c.coherent_window_error(17, depth-precision_cost, initial_error=initial_error)
    assert (full-one).modulus_squared_upper() < budget**2
    crt_control = {'odd_modulus': M, 'prime_powers': {'17': 2, '41': 1},
                   'extra_hexadecimal_precision': precision_cost, 'depth': depth,
                   'initial': str(delta), 'initial_error_upper': str(initial_error),
                   'normalized_window': box_json(full), 'coherence_upper': str(budget),
                   'scope': 'listed p-adic congruences; literal integer carry histories not preserved'}

    # Independently fill the endpoint-gap mutation omitted by the live sibling
    # test file. Both source shears remain present in this comparison.
    p, q, first = 17, 15, 19
    def reduce_unit(x, modulus):
        return x.numerator*pow(x.denominator, -1, modulus) % modulus
    source2 = reduce_unit(collapsed_forcing(2), p*p)
    shear2 = reduce_unit(Q(20, 9)-Q(4, 12)-Q(1, 13), p)
    correct = (16*(1+8*p*q)*first+source2+p*q*shear2) % (p*p)
    mutant = (16*(1+3*p*q)*first+source2+p*q*shear2) % (p*p)
    assert (correct, mutant) == (175, 124)
    assert reduce_unit(Q(47, 15), 289) == 138
    assert reduce_unit(Q(62, 15), 289) == 139
    witt_audit = {'sibling_head': '0683f8f166b9106ab8405a2d6538415b5ac84ba3',
                  'p': p, 'first_filtered_state': first, 'correct_second_state': correct,
                  'wrong_endpoint_gap_second_state': mutant,
                  'same_circle_distinct_unwrapped_mod_p2': [138, 139],
                  'same_circle_phase': '2/15', 'initial_shift': '1/16'}
    paths = ['observational_succ/cyclotomic_selected_source.py',
             'observational_succ/bbp_source_memory.py', 'observational_succ/pi_source_genesis.py',
             'observational_succ/circle_origin_gauge.py', 'tests/test_cyclotomic_selected_source.py',
             'scripts/cyclotomic_selected_oracle.py', 'scripts/cyclotomic_fiber_moment_oracle.py']
    return {'schema': 'cyclotomic-selected-exact-v1',
            'status': 'EXACT_FINITE_CERTIFICATES_NOT_AN_ASYMPTOTIC_PROOF',
            'pi_normality_proved': False, 'authentic_interference_vanishing_proved': False,
            'source_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'prime_windows': primes, 'clock_profiles': profiles,
            'linear_tomography': tomography,
            'fourth_alias_polynomial': {str(k): v for k, v in sorted(alias.items())},
            'first_phase_sensitive_moment': {'base': 16, 'horizon': 3, 'moment': 34,
                'diagonal_numerator': diagonal, 'cosine_coefficient': cross_coefficient,
                'denominator': str(3**34), 'unique_collision': collisions[0]},
            'positive_carry_defect_certificates': carry, 'independent_fiber_moments': fiber,
            'authentic_complement_variation': variation,
            'finite_crt_initial_control': crt_control,
            'live_sibling_witt_audit': witt_audit,
            'inverse_observer': {'base': 16, 'depth': 6, 'cutoff': 257,
                                 'first_source_visible_time': c.inverse_observer_delay(16, 6, 257)}}


def main():
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
