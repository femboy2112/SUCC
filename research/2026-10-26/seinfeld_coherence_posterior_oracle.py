#!/usr/bin/env python3
"""Independent rational checks for the publication-time #314/#315 bridge.

Only the standard library is used. Exact urn path products and two-step
predictive probabilities check the Fourier formulas independently of the
Dirichlet-moment proof. Analytic logarithms and all-index statements are proved
in the accompanying dossier, not inferred from these finite computations.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
from math import comb, factorial, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT = HERE / 'seinfeld_coherence_posterior_receipt.json'
DOCUMENT = HERE / 'SEINFELD_COHERENCE_POSTERIOR_BRIDGE.md'


def phase(exponent):
    """Coordinates in Q[zeta_16], using zeta_16**8 = -1."""
    exponent %= 16
    out = [0] * 8
    out[exponent % 8] = 1 if exponent < 8 else -1
    return tuple(out)


def selected_statistics(words, r):
    """Enumerate literal prefixes, then both future urn draws exactly.

    The prefix denominator is common, (16)_r. Integer weights retain all
    path multiplicities. The returned Fourier second moment is the cross
    moment of two distinct future draws, rather than an assumed latent formula.
    """
    evidence_numerator = 0
    first = [0] * 16
    pairs = [[0] * 16 for _ in range(16)]
    word_count = 0
    for word in words:
        if len(word) != r:
            raise ValueError('prefix length mismatch')
        counts = [1] * 16
        weight = 1
        for color in word:
            weight *= counts[color]
            counts[color] += 1
        evidence_numerator += weight
        word_count += 1
        for i in range(16):
            first[i] += weight * counts[i]
            for j in range(16):
                pairs[i][j] += weight * counts[i] * (counts[j] + (i == j))
    total = r + 16
    evidence = Q(evidence_numerator, prod(range(16, total)))
    if sum(first) != evidence_numerator * total:
        raise ArithmeticError('first predictive law is not normalized')
    if sum(map(sum, pairs)) != evidence_numerator * total * (total + 1):
        raise ArithmeticError('second predictive law is not normalized')
    rows = []
    for h in range(1, 16):
        mean = tuple(sum(Q(first[j], evidence_numerator * total) * phase(h*j)[k]
                         for j in range(16)) for k in range(8))
        cross = tuple(sum(Q(pairs[i][j], evidence_numerator * total * (total+1))
                          * phase(h*(i-j))[k]
                          for i in range(16) for j in range(16)) for k in range(8))
        empirical_two = tuple(sum(
            Q(pairs[i][j], 4 * evidence_numerator * total * (total+1))
            * (2*(k == 0) + phase(h*(i-j))[k] + phase(h*(j-i))[k])
            for i in range(16) for j in range(16)) for k in range(8))
        if empirical_two != tuple(Q(k == 0, 2) + cross[k]/2 for k in range(8)):
            raise ArithmeticError('future empirical moment identity failed')
        rows.append({'h': h, 'mean': mean, 'future_pair_cross_moment': cross,
                     'two_future_empirical_second_moment': empirical_two})
    return {'r': r, 'literal_prefixes': word_count, 'evidence': evidence, 'modes': rows}


def build_receipt():
    avoidance = []
    for r in range(4):
        row = selected_statistics(itertools.product(range(1, 16), repeat=r), r)
        m = 15 + r
        expected_mean = Q(-r, 15*(r+16))
        expected_second = Q(m*m-m+30, 15*(m+1)*(m+2))
        if row['evidence'] != Q(15, m):
            raise ArithmeticError('avoidance probability failed')
        for mode in row['modes']:
            if mode['mean'] != (expected_mean,) + (Q(),)*7:
                raise ArithmeticError('avoidance Fourier mean failed')
            if mode['future_pair_cross_moment'] != (expected_second,) + (Q(),)*7:
                raise ArithmeticError('avoidance Fourier second moment failed')
        avoidance.append(row)

    literal = []
    for r in (0, 1, 2, 3, 7, 16, 31, 64, 128):
        row = selected_statistics([(1,)*r], r)
        if row['evidence'] != Q(1, comb(r+15, 15)):
            raise ArithmeticError('literal-word probability failed')
        expected_second = Q(r*r+r+16, (r+16)*(r+17))
        for mode in row['modes']:
            expected_mean = tuple(Q(r, r+16)*c for c in phase(mode['h']))
            if mode['mean'] != expected_mean:
                raise ArithmeticError('literal-word Fourier mean failed')
            if mode['future_pair_cross_moment'] != (expected_second,) + (Q(),)*7:
                raise ArithmeticError('literal-word Fourier second moment failed')
        literal.append(row)

    beta_rows = []
    for r in (0, 1, 2, 3, 7, 16):
        m = r + 15
        moments = []
        for k in range(7):
            # Direct integration of t^k m(1-t)^(m-1) by its finite polynomial.
            integral = sum((Q(m*(-1)**j*comb(m-1, j), j+k+1)
                            for j in range(m)), Q())
            expected = Q(factorial(k)*factorial(m), factorial(m+k))
            if integral != expected:
                raise ArithmeticError('posterior density integral failed')
            moments.append(integral)
        # The full word has a different retained Q likelihood, but the
        # T-dependent likelihood is the same factor (1-T)^r.
        other_color_moment = Q(1, comb(r+14, 14))
        if Q(15, m)*other_color_moment != Q(1, comb(r+15, 15)):
            raise ArithmeticError('same-marginal likelihood factorization failed')
        beta_rows.append({'r': r, 'm': m, 'theta_moments': moments,
                          'other_color_likelihood_factor': other_color_moment})

    bounds = []
    for r in (0, 1, 2, 3, 16, 64, 256, 1024):
        m = r + 15
        v = Q(m*m-m+30, 15*(m+1)*(m+2))
        difference = Q(2*(m-15)*(m-16), 255*(m+1)*(m+2))
        if v-Q(1,17) != difference or difference < 0:
            raise ArithmeticError('uniform positive-energy control failed')
        bounds.append({'m': m, 'avoidance_second_moment': v,
                       'excess_over_one_seventeenth': difference,
                       'log_defect_strict_upper_bound': Q(1,2*m)})

    paths = (Path(__file__).resolve(), DOCUMENT)
    return {
        'status': 'EXACT_FINITE_REPLAY_WITH_SEPARATE_PAPER_PROOFS',
        'prior': 'symmetric Dirichlet(1,...,1) on 16 colors / equivalent Polya law',
        'inspected_sibling': {'pr': 314, 'head': '935c2db4c36ff56d90acd82eae30bcce15b6a053'},
        'parent_interpretation': {'pr': 315, 'commit': '2993a4e203211fae3ac1e6697bab22f9a506870e'},
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'counts': {'avoidance_literal_prefixes': sum(x['literal_prefixes'] for x in avoidance),
                   'literal_constant_prefixes': len(literal),
                   'nontrivial_mode_checks': 15*(len(avoidance)+len(literal)),
                   'independent_density_integrals': 7*len(beta_rows),
                   'positive_energy_controls': len(bounds)},
        'avoidance': avoidance, 'literal_words': literal, 'shared_marginal': beta_rows,
        'bounds': bounds,
        'scope': {'sibling_code_merged': False, 'new_native_modules_or_tests': False,
                  'bbp_path_sampling_identified': False, 'selected_fourier_cancellation_proved': False,
                  'finite_replay_proves_analytic_logarithm_identity': False},
    }


def canonical(data):
    return json.dumps(data, sort_keys=True, indent=2,
                      default=lambda x: str(x) if isinstance(x, Q) else x) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--verify', action='store_true')
    parser.add_argument('--path', type=Path, default=DEFAULT)
    args = parser.parse_args()
    expected = canonical(build_receipt())
    if args.write:
        args.path.write_text(expected)
        print('Wrote exact coherence/posterior receipt:', args.path)
    elif not args.path.exists() or args.path.read_text() != expected:
        raise SystemExit('Receipt mismatch: recomputed conditional law or source hashes differ')
    else:
        print('Verified exact coherence/posterior receipt:', args.path)


if __name__ == '__main__':
    main()
