#!/usr/bin/env python3
"""Bounded exact controls for the pi-carrier detector interface.

No SUCC production modules are imported. This is an independent finite
arithmetic audit, not a finite proof of matrix Chernoff, GB-12, or normality.
The binomial census is a direct oracle for declared two-row distributions.
The Gamma checks compare repeated rational division with binomial expansion.

Replay from the repository root:
  python research/2026-11-15/pi_carrier_collision/independent_audit.py \
    --output research/2026-11-15/pi_carrier_collision/receipts/translator_independent.json
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import combinations, permutations, product
import json
from math import comb
from pathlib import Path
import platform
import subprocess
import time


ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
QUARTER_PHASES = (ONE, (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, s):
    return a[0] * s, a[1] * s


def conjugate(a):
    return a[0], -a[1]


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def inverse(a):
    return scale(conjugate(a), 1 / norm2(a))


def power(a, n):
    value = ONE
    for _ in range(n):
        value = multiply(value, a)
    return value


class Audit:
    def __init__(self):
        self.counts = Counter()

    def check(self, condition, category):
        if not condition:
            raise AssertionError(category)
        self.counts[category] += 1


def log_budget(ratio):
    """Independent oracle: repeated doubling, not bit lengths."""
    level = 0
    upper = Q(1)
    while upper < ratio:
        upper *= 2
        level += 1
    return level


def ceiling(value):
    quotient, remainder = divmod(value.numerator, value.denominator)
    return quotient + bool(remainder)


def budget(dimension, eta, epsilon, delta):
    level = log_budget(2 * dimension / delta)
    rows = ceiling(3 * dimension * level / ((1 - eta) * epsilon ** 2))
    low = (1 - eta) * (1 - epsilon)
    high = (1 + eta) * (1 + epsilon)
    return dict(dimension=dimension, eta=eta, epsilon=epsilon, delta=delta,
                level=level, rows=rows, failure_bound=Q(2 * dimension, 2 ** level),
                lower=low, upper=high, gram_condition=high / low,
                vector_noise_gain_squared=dimension ** 2 / low,
                mean_noise_gain_squared=dimension / low)


def binomial_census(p, epsilon, delta):
    """Eigenvalues after whitening are k/(s p), (s-k)/(s(1-p))."""
    c = budget(2, abs(2 * p - 1), epsilon, delta)
    count = c['rows']
    failure = Q(0)
    total = Q(0)
    bad_counts = []
    for plus in range(count + 1):
        mass = comb(count, plus) * p ** plus * (1 - p) ** (count - plus)
        total += mass
        eigenvalues = (Q(plus, count) / p, Q(count - plus, count) / (1 - p))
        if any(abs(value - 1) > epsilon for value in eigenvalues):
            failure += mass
            bad_counts.append(plus)
    return dict(**c, probability_plus=p, exact_failure=failure,
                total_mass=total, failing_counts=bad_counts)


def gamma_binomial(alpha, rate, omega):
    """Closed numerator: rate^alpha * (rate-i omega)^alpha / norm^alpha."""
    numerator = ZERO
    for j in range(alpha + 1):
        coefficient = comb(alpha, j) * rate ** (alpha - j) * omega ** j
        numerator = add(numerator, scale(QUARTER_PHASES[(-j) % 4], coefficient))
    return scale(numerator, rate ** alpha / (rate ** 2 + omega ** 2) ** alpha)


def nb_character(scale_parameter, phase):
    denominator = add(ONE, scale(add(ONE, scale(phase, -1)), scale_parameter))
    return power(inverse(denominator), 2)


def determinant(matrix):
    n = len(matrix)
    result = ZERO
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n))
        value = ONE
        for i, j in enumerate(order):
            value = multiply(value, matrix[i][j])
        result = add(result, scale(value, (-1) ** inversions))
    return result


def original_forcing(n):
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def make_receipt():
    started = time.perf_counter()
    audit = Audit()
    rows = []
    for b, eta, epsilon, delta in product(
            (1, 2, 3, 7, 16, 31, 127, 4096),
            (Q(0), Q(1, 9), Q(1, 4), Q(2, 3), Q(7, 8)),
            (Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10)),
            (Q(1, 2), Q(1, 3), Q(1, 17), Q(3, 100), Q(1, 1000))):
        c = budget(b, eta, epsilon, delta)
        exponent = c['rows'] * epsilon ** 2 * (1 - eta) / (3 * b)
        audit.check(exponent >= c['level'], 'rational_exponent_paid')
        audit.check(c['failure_bound'] <= delta, 'requested_failure_paid')
        audit.check(2 ** c['level'] >= 2 * b / delta, 'binary_upper')
        audit.check(c['level'] == 0 or 2 ** (c['level'] - 1) < 2 * b / delta,
                    'binary_minimal')
        audit.check(c['vector_noise_gain_squared'] == b * c['mean_noise_gain_squared'],
                    'readout_normalization')
        rows.append(c['rows'])
    benchmark = budget(16, Q(1, 4), Q(1, 2), Q(1, 64))
    audit.check(benchmark['rows'] == 2816 and benchmark['level'] == 11,
                'recommended_benchmark')
    censuses = []
    for p in (Q(1, 2), Q(2, 3), Q(3, 4), Q(1, 4), Q(7, 8)):
        c = binomial_census(p, Q(3, 4), Q(1, 3))
        audit.check(c['total_mass'] == 1, 'binomial_total_mass')
        audit.check(0 < c['exact_failure'] <= c['failure_bound'], 'exact_census_bound')
        censuses.append(c)
    # One shared sign copied any number of times has Gram determinant zero.
    for sign in (-1, 1):
        audit.check(1 - sign ** 2 == 0, 'copied_row_rank_failure')
    # Exact Sylvester phase matrices demonstrate the dimension cost of B^-1 echoes.
    normalization_controls = []
    for b in (2, 4, 8, 16):
        matrix = [[Q((-1) ** ((i & j).bit_count())) for j in range(b)] for i in range(b)]
        audit.check(all(sum(matrix[k][i] * matrix[k][j] for k in range(b))
                        == (b if i == j else 0) for i in range(b) for j in range(b)),
                    'hadamard_gram')
        # Source/error vector all ones, normalized echo vector (1,0,...,0).
        echo = [sum(row) / b for row in matrix]
        rms_squared = sum(value ** 2 for value in echo) / b
        audit.check(rms_squared == Q(1, b), 'normalized_echo_rms')
        audit.check(1 / rms_squared == b and Q(b) / rms_squared == b ** 2,
                    'dimension_gain_is_necessary')
        normalization_controls.append(dict(dimension=b, echo=echo, rms_squared=rms_squared))
    gamma_examples = []
    for alpha, rate, omega in product(range(11), (Q(1, 2), Q(1), Q(3)),
                                      (Q(0), Q(1), Q(-1), Q(1, 2), Q(3, 2), Q(-5, 3))):
        repeated = power(scale(inverse((rate, omega)), rate), alpha)
        closed = gamma_binomial(alpha, rate, omega)
        audit.check(repeated == closed, 'gamma_two_exact_methods')
        audit.check(norm2(closed) == (rate ** 2 / (rate ** 2 + omega ** 2)) ** alpha,
                    'gamma_attenuation')
        for beta in (0, 1, 4):
            audit.check(gamma_binomial(alpha + beta, rate, omega)
                        == multiply(closed, gamma_binomial(beta, rate, omega)),
                        'gamma_semigroup')
    donor = gamma_binomial(2, Q(1), Q(1))
    audit.check(donor == (Q(0), Q(-1, 2)), 'donor_rotation_fixture')
    audit.check(donor[0] == 0 and norm2(donor) == Q(1, 4), 'single_quadrature_false_null')
    for z, rotation in product(QUARTER_PHASES + ((Q(3, 5), Q(4, 5)),), QUARTER_PHASES):
        y = multiply(z, conjugate(rotation))
        audit.check(multiply(rotation, y) == z, 'recorded_clock_compensation')
        report_mean = multiply(z, donor)
        audit.check(multiply(report_mean, inverse(donor)) == z, 'known_multiplier_inverse')
    gamma_examples.append(dict(alpha=2, rate=Q(1), omega=Q(1), multiplier=donor,
                               fixed_source_variance=1 / norm2(donor) - 1))
    nb_examples = []
    for lam, phase, cutoff in product((Q(1, 4), Q(1), Q(3, 2), Q(2), Q(17), Q(64)),
                                     QUARTER_PHASES, range(13)):
        p, q = 1 / (1 + lam), lam / (1 + lam)
        partial = ZERO
        total = Q(0)
        for k in range(cutoff + 1):
            weight = (k + 1) * p ** 2 * q ** k
            total += weight
            partial = add(partial, scale(power(phase, k), weight))
        tail = q ** (cutoff + 1) * (1 + (cutoff + 1) * p)
        audit.check(total + tail == 1, 'negative_binomial_tail_exact')
        error = add(nb_character(lam, phase), scale(partial, -1))
        audit.check(norm2(error) <= tail ** 2, 'character_tail_enclosure')
        if cutoff == 4 and phase == (Q(0), Q(1)):
            nb_examples.append(dict(scale=lam, cutoff=cutoff, character=nb_character(lam, phase),
                                    partial=partial, tail_mass=tail))
    gram_controls = []
    for b, spacing, quarter_steps, lam in ((2, Q(1, 2), 2, Q(1)),
                                          (3, Q(1, 4), 1, Q(2)),
                                          (3, Q(1, 4), 1, Q(4)),
                                          (3, Q(1, 4), 1, Q(16))):
        eta = 1 / (4 * lam * (1 + lam) * spacing ** 2)
        gram = [[nb_character(lam, QUARTER_PHASES[(quarter_steps * (j - i)) % 4])
                 for j in range(b)] for i in range(b)]
        audit.check(all(gram[i][j] == conjugate(gram[j][i]) for i in range(b) for j in range(b)),
                    'population_hermitian')
        minimum_minors = []
        for direction in (-1, 1):
            # Lower: G-(1-eta)I; upper: (1+eta)I-G.
            matrix = [[add(scale(gram[i][j], -direction),
                           (Q(direction) + eta, Q(0)) if i == j else ZERO)
                       for j in range(b)] for i in range(b)]
            minors = []
            for size in range(1, b + 1):
                for indices in combinations(range(b), size):
                    minor = determinant([[matrix[i][j] for j in indices] for i in indices])
                    audit.check(minor[1] == 0 and minor[0] >= 0, 'gershgorin_bound_psd_control')
                    minors.append(minor[0])
            minimum_minors.append(min(minors))
        gram_controls.append(dict(dimension=b, spacing=spacing, scale=lam, eta=eta,
                                  gram=gram, smallest_principal_minors=minimum_minors))
    # Literal forcing and exact two-tap argument, before exponentiation.
    states = [Q(0)]
    for n in range(1, 34):
        states.append(16 * states[-1] + original_forcing(n))
    for n, h, k in product(range(1, 33), (-3, 1, 7), (0, 1, 2, 17, 257)):
        left = (h - 16 * k) * states[n] + k * states[n + 1]
        right = h * states[n] + k * original_forcing(n + 1)
        audit.check(left == right, 'literal_source_echo')
        if k:
            mutated = Q(4, 8 * (n + 1) - 7)
            audit.check(k * (original_forcing(n + 1) - mutated) != 0,
                        'deleted_channels_detected_in_argument')
    gb_controls = []
    for m in (4096, 4097, 8192, 65536, 1048576):
        level = log_budget(Q(m))
        block_dose = 196 * m
        trials = block_dose * level
        # (1-1/n)^n < 1/2 follows from (1+1/(n-1))^n > 1+n/(n-1)>2.
        audit.check(1 + Q(block_dose, block_dose - 1) > 2,
                    'gb_elementary_dose_margin')
        audit.check(Q(1, 2 ** level) <= Q(1, m), 'gb_binary_failure_paid')
        for h in (1, 2, 31):
            audit.check(1 <= h <= Q(m * m, 64), 'gb_declared_frequency_band')
            # pi < 22/7: a fully rational upper bound on counterseed hit probability.
            counter_hit = min(Q(1), trials * Q(22, 7) ** 2 * h ** 2 / (4096 * (m + 1) ** 4))
            gb_controls.append(dict(m=m, h=h, binary_log=level, trials=trials,
                                    source_no_hit_upper=Q(1, 2 ** level),
                                    counterseed_any_hit_upper=counter_hit,
                                    onset_status='conditional_on_inherited_m_ge_m2'))
    root = Path(__file__).resolve().parents[3]
    input_hashes = {}
    for relative in ('observational_succ/random_probe_frames.py',
                     'tests/test_random_probe_frames.py',
                     'research/2026-10-27/GLOBAL_BRANCH_COERCIVITY.md'):
        input_hashes[relative] = hashlib.sha256((root / relative).read_bytes()).hexdigest()
    return dict(
        status='PASS', authority='exact finite controls; no universal arithmetic promotion',
        production_imports=[],
        inherited_inputs_not_reproved=['Tropp matrix Chernoff', 'GB-12 selected block theorem',
                                      'original BBP tail inequality', 'pi < 22/7'],
        repository_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
        python_version=platform.python_version(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        read_only_input_sha256=input_hashes,
        total_exact_checks=sum(audit.counts.values()), checks=dict(audit.counts),
        budget_grid=dict(cases=len(rows), minimum_rows=min(rows), maximum_rows=max(rows)),
        benchmark=benchmark, exact_binomial_censuses=censuses,
        copied_row_control=dict(dimension=2, actual_failure_probability=Q(1),
                                gram_eigenvalues=[0, 2]),
        normalization_controls=normalization_controls,
        gamma_controls=gamma_examples, negative_binomial_controls=nb_examples,
        population_gram_controls=gram_controls, gb_dose_controls=gb_controls,
        elapsed_seconds_diagnostic=time.perf_counter() - started,
        numerical_diagnostics_used=False,
    )


def encode(value):
    if isinstance(value, Q):
        return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = make_receipt()
    rendered = json.dumps(result, default=encode, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
        print(json.dumps(dict(status=result['status'], exact_checks=result['total_exact_checks'],
                              receipt=str(args.output),
                              receipt_sha256=hashlib.sha256(rendered.encode()).hexdigest())))
    else:
        print(rendered, end='')


if __name__ == '__main__':
    main()
