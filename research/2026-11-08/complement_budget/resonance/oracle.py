"""Finite rational source and outward phase checks for CR1--CR3.

The source epochs are reused prior cases; no fresh statistical holdout is
claimed. The new candidate menu is fixed in this script, without fitting.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

from resonance import (ROOT, HERE, SCALE, ZERO, Interval, Box, phase, mean,
                       modulus, nonlinear_floor, error_record, unit_model,
                       order16, source_xi, forcing)
from source import common_history, principal_pair, direct_modular_residue, matched_seed


def run():
    counts = Counter()
    primes = (4201, 4217, 4337)
    data = common_history((max(primes) - 1) // 2, 0)
    den = data['denominator']
    rows = []
    for p in primes:
        L, m, xi = (p - 1) // 4, order16(p), source_xi(p)
        n0, q = L + 1, L // m
        indices = range(n0, 2 * L + 1)
        residues = [data['residues'][n] for n in indices]
        local = [principal_pair(r, den, p) for r in residues]
        assert all(d == p for _, d in local)
        xs = [x for x, _ in local]
        for j, x in enumerate(xs):
            assert x == xi * pow(16, j, p) % p
            counts['exact_source_clock_values'] += 1
        for j in range(L - 1):
            # Direct rational congruence of the complement lift. No complex
            # numerical implementation is involved in this assertion.
            current = Q(residues[j], den) - Q(xs[j], p)
            following = Q(residues[j + 1], den) - Q(xs[j + 1], p)
            assert (following - 16 * current - forcing(n0 + j + 1)).denominator == 1
            counts['exact_complement_cocycles'] += 1
        for n in (n0, 2 * L):
            assert direct_modular_residue(n, den) == data['residues'][n]
            counts['independent_source_power_sums'] += 1
        for h in (1, 3):
            b = [phase(h * (r * p - x * den), den * p) for r, x in zip(residues, xs)]
            for d in (2, 3, 5):
                P = [3, -h] + [0] * (d - 2) + [1]
                floor = nonlinear_floor(p, h, P)
                assert floor['floor'].lo > 0
                for anchor in (Q(0), Q(1, 7)):
                    v = unit_model(p, h, P, anchor.numerator, anchor.denominator)
                    rec = error_record(b, v)
                    assert rec['rho'].lo > floor['floor'].hi
                    assert rec['lift_bound_strictly_certified']
                    counts['outward_nonlinear_floor_checks'] += 1
                    rows.append({'p': p, 'm': m, 'replicas': q, 'h': h,
                                 'polynomial_low_coefficients': P, 'anchor': str(anchor),
                                 'rho': rec['rho'].as_list(),
                                 'full_l2_squared': rec['full_l2_squared'].as_list(),
                                 'universal_floor': floor['floor'].as_list(),
                                 'delta': floor['delta'].as_list(),
                                 'forcing_error': floor['forcing_error'].as_list()})
    # Genuine rational same-forcing control with unchanged principal parts.
    p = primes[0]
    L, m = (p - 1) // 4, order16(p)
    n0 = L + 1
    seed, _, _ = matched_seed(data, n0, 32, Q(1, 2**20), (3, 5, 7, 11, p))
    assert seed.denominator % p
    shadow = []
    shadow_den = den * seed.denominator
    shift = seed.numerator * pow(16, n0, seed.denominator) % seed.denominator
    for n in range(n0, 2 * L + 1):
        value = data['residues'][n] * seed.denominator + shift * den
        assert principal_pair(value, shadow_den, p) == principal_pair(data['residues'][n], den, p)
        shadow.append(value)
        shift = 16 * shift % seed.denominator
        counts['matched_seed_principal_parts'] += 1
    controls = []
    for h in (1, 3):
        xs = [principal_pair(data['residues'][n], den, p)[0] for n in range(n0, 2 * L + 1)]
        b = [phase(h * (z * p - x * shadow_den), shadow_den * p) for z, x in zip(shadow, xs)]
        v = unit_model(p, h, [0, -h])
        rec = error_record(b, v)
        # A successful source-forcing argument must retain this inverse slope.
        assert rec['rho'].hi < SCALE // 100000
        counts['accurate_affine_coherent_controls'] += 1
        controls.append({'h': h, 'rho': rec['rho'].as_list(), 'inverse_slope': -h})
    dependency_paths = [Path(__file__), HERE/'resonance.py', HERE/'THEOREMS.md',
                        ROOT/'observational_succ/duck_bbp.py',
                        ROOT/'research/2026-11-08/covariance_forge/source.py',
                        ROOT/'research/2026-11-08/covariance_forge/intervals.py',
                        ROOT/'research/2026-11-08/signal_frontier/prime_resonance/pr_resonance.py',
                        ROOT/'research/2026-11-08/signal_frontier/prime_resonance/THEOREMS.md']
    return {'scale': SCALE, 'counts': dict(counts), 'rows': rows, 'controls': controls,
            'source': {'last': data['last'], 'unwrapped_sha256': data['unwrapped_sha256'],
                       'carry_sha256': data['carry_sha256']},
            'matched_seed': {'numerator_hex': hex(seed.numerator), 'denominator_hex': hex(seed.denominator),
                             'fixed_seed_across_epochs': False, 'literal_zero': False},
            'dependencies': {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest() for path in dependency_paths},
            'scope': 'Reused source cases, new fixed models; exact rational identities and outward finite phase bounds. No asymptotic certificate.',
            'pi_normality': 'OPEN', 'RH': 'OPEN'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result['counts'], sort_keys=True))
