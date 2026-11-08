"""Independent exact checks for chronological prime-history theorems.

This module deliberately does not import the earlier source or clock engines.
All proof receipts are integers or Fractions; no floating point or pi input.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import isqrt
from pathlib import Path
import argparse
import json

PRIMES = (17, 41, 73, 89, 97, 137, 193, 233, 281)
POLES = ((4, 7), (-2, 4), (-1, 3), (-1, 2))


def integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError('integer in stated range required')
    return value


def split_prime(p):
    integer(p, 3)
    if p % 8 != 1 or any(p % k == 0 for k in range(2, isqrt(p)+1)):
        raise ValueError('prime congruent to 1 modulo 8 required')
    return p


def forcing(n, poles=POLES):
    integer(n, 1)
    return sum((Q(c, 8*n-o) for c, o in poles), Q(0))


def source_history(last, seed=Q(0), poles=POLES):
    integer(last)
    if type(seed) is not Q:
        raise ValueError('exact rational seed required')
    out = [seed]
    for n in range(1, last+1):
        out.append(16*out[-1]+forcing(n, poles))
    return out


def principal(x, p):
    """Reduced-rational p-part by exact coprime denominator inversion."""
    split_prime(p)
    if type(x) is not Q:
        raise ValueError('rational carrier required')
    unit, power = x.denominator, 1
    while unit % p == 0:
        unit //= p
        power *= p
    return Q((x.numerator * pow(unit, -1, power)) % power, power)


def order(p):
    split_prime(p)
    r, m = 16 % p, 1
    while r != 1:
        r = (16*r) % p
        m += 1
    return m


def effective_frequency(coefficients, lags):
    if len(coefficients) != len(lags):
        raise ValueError('one lag per coefficient required')
    if any(type(c) is not int for c in coefficients):
        raise ValueError('integer coefficients required')
    if any(type(t) is not int or t < 0 for t in lags):
        raise ValueError('nonnegative integer lags required')
    return sum(c*16**t for c, t in zip(coefficients, lags))


def classify(coefficients, lags, p):
    split_prime(p)
    H = effective_frequency(coefficients, lags)
    return 'integer_resonance' if H == 0 else (
        'modular_alias' if H % p == 0 else 'nonresonance')


def word_by_orbit(numerator, p, digits):
    split_prime(p)
    integer(numerator)
    integer(digits, 1)
    if numerator >= p:
        raise ValueError('canonical numerator required')
    word = 0
    for _ in range(digits):
        digit, numerator = divmod(16*numerator, p)
        word = 16*word+digit
    return word


def total_variation(counts, sample_count, cells):
    integer(sample_count, 1)
    integer(cells, 1)
    if any(type(k) is not int or not 0 <= k < cells or
           type(v) is not int or v <= 0 for k, v in counts.items()):
        raise ValueError('positive integer counts on declared cells required')
    if sum(counts.values()) != sample_count:
        raise ValueError('sample count mismatch')
    return (sum((abs(Q(v, sample_count)-Q(1, cells))
                 for v in counts.values()), Q(0))
            +Q(cells-len(counts), cells))/2


def carry_data(states):
    floors = [x.numerator // x.denominator for x in states]
    return floors, [floors[n]-16*floors[n-1] for n in range(1, len(states))]


def carry_radius(states):
    return min((Q(1)-(x-x.numerator//x.denominator))/16**n
               for n, x in enumerate(states))


def run_checks():
    counts = Counter()
    rows = []
    for p in PRIMES:
        L, np = (p-1)//4, (p+7)//8
        n0, m = L+1, order(p)
        states = source_history(2*L+3)
        xi = 4*pow(16, n0-np, p) % p
        orbit = [xi*pow(16, r, p) % p for r in range(m)]
        assert len(set(orbit)) == m and L % m == 0
        for n in range(np, 2*L+1):
            expected = Q(4*pow(16, n-np, p) % p, p)
            assert principal(states[n], p) == expected
            counts['literal_source_clock_checks'] += 1
        # A true next-pole birth changes the clock, rather than extending it.
        extended = Q(4*pow(16, 2*L+1-np, p) % p, p)
        actual = principal(states[2*L+1], p)
        assert actual != extended
        counts['next_birth_rejections'] += 1
        # Same forcing, changed rational source. Identification control only.
        q = 3 if p != 3 else 5
        seed = Q(1, q)
        wrong = source_history(2*L, seed)
        assert wrong[0] != states[0]
        for n in range(2*L+1):
            assert principal(wrong[n], p) == principal(states[n], p)
            counts['wrong_seed_local_history_matches'] += 1
        mutated = source_history(np, poles=((3, 7),)+POLES[1:])
        assert principal(mutated[np], p) != principal(states[np], p)
        counts['pole_mutation_rejections'] += 1
        source_cycle = [principal(states[n0+r], p) for r in range(m)]
        for h in list(product(range(-2, 3), repeat=3))+[(-16, 1, 0), (p, 0, 0)]:
            H = effective_frequency(h, (0, 1, 2))
            actual_phases = []
            expected_phases = []
            for r in range(m):
                # Cyclic source reads stay wholly inside its clean interval.
                phase = sum((h[t]*source_cycle[(r+t) % m]
                             for t in range(3)), Q(0))
                residue = (phase*p).numerator % p
                expected = xi*H*pow(16, r, p) % p
                assert residue == expected
                actual_phases.append(residue)
                expected_phases.append(expected)
                counts['lag_phase_checks'] += 1
            assert Counter(actual_phases) == Counter(expected_phases)
            if H % p == 0:
                assert set(actual_phases) == {0}
            counts['moment_multiset_checks'] += 1
        assert classify((-16, 1), (0, 1), p) == 'integer_resonance'
        assert classify((p, 0), (0, 1), p) == 'modular_alias'
        assert classify((1, 0), (0, 1), p) == 'nonresonance'
        counts['resonance_controls'] += 3
        words = []
        for d in range(1, 5):
            M = 16**d
            by_dynamics = Counter()
            for v in orbit:
                w = word_by_orbit(v, p, d)
                assert w == M*v//p
                by_dynamics[w] += 1
                # Every word boundary remains at least 1/(p*M) away.
                lo = w
                for k in (lo, lo+1):
                    assert abs(Q(v, p)-Q(k, M)) >= Q(1, p*M)
                    counts['precision_margin_checks'] += 1
                counts['word_extraction_checks'] += 1
            tv = total_variation(by_dynamics, m, M)
            assert tv >= max(Q(0), Q(1)-Q(m, M))
            if M >= p:
                assert tv == 1-Q(m, M)
            # Interior source transcripts use actual successive p-parts.
            for n in range(n0, 2*L-d+2):
                transcript = 0
                for j in range(d):
                    x = principal(states[n+j], p)
                    transcript = 16*transcript+(16*x.numerator)//x.denominator
                initial = principal(states[n], p)
                assert transcript == (M*initial.numerator)//initial.denominator
                counts['actual_transcript_checks'] += 1
            words.append({'digits': d, 'cells': M, 'support': len(by_dynamics),
                          'tv': str(tv), 'support_lower': str(max(Q(0), 1-Q(m, M))),
                          'counts': {str(k): v for k, v in sorted(by_dynamics.items())}})
            counts['word_tv_checks'] += 1
        # Independent exact Fourier completion in Z[X]/(X^p-1).
        low, high = p//5, 2*p//5
        interval = list(range(low, high))
        coefficients = [0]*p
        for h in range(p):
            for k in interval:
                for v in orbit:
                    coefficients[h*(v-k) % p] += 1
                    counts['finite_fourier_terms'] += 1
        intersection = sum(low <= v < high for v in orbit)
        baseline = len(interval)*m-intersection
        assert coefficients[0] == baseline+p*intersection
        assert all(c == baseline for c in coefficients[1:])
        counts['fourier_completion_identities'] += 1
        digest = sha256('\n'.join(str(x) for x in states).encode()).hexdigest()
        rows.append({'p': p, 'm': m, 'L': L, 'good_order': m**3 > p,
                     'xi': xi, 'source_sha256': digest,
                     'next_birth_actual': str(actual), 'next_birth_extension': str(extended),
                     'words': words})
    # Sharp carry endpoint, fixed nonzero seed, and missing-C0 control.
    zero = source_history(16)
    radii = []
    for J in range(1, 13):
        prefix = zero[:J+1]
        radius = carry_radius(prefix)
        assert 0 < radius <= Q(1, 16**J)
        inside = source_history(J, radius/2)
        endpoint = source_history(J, radius)
        floors, carries = carry_data(prefix)
        fi, ci = carry_data(inside)
        fe, ce = carry_data(endpoint)
        assert fi == floors and ci == carries
        assert fe != floors and ce != carries
        for k in (-3, -1, 1, 5):
            integer_states = source_history(J, Q(k))
            fk, ck = carry_data(integer_states)
            assert ck == carries and fk[0] == k
            shifted = source_history(J, Q(k)+radius/2)
            assert carry_data(shifted)[1] == carries
            counts['integer_seed_carry_controls'] += 2
        radii.append({'J': J, 'sigma': str(radius), 'upper': str(Q(1, 16**J))})
        counts['carry_endpoint_checks'] += 1
    fixed = Q(1, 16**7)
    fixed_states = source_history(16, fixed)
    first_mismatch = next(n for n in range(17)
                          if carry_data(fixed_states)[0][n] != carry_data(zero)[0][n])
    assert 1 <= first_mismatch <= 7
    counts['fixed_seed_rigidity_control'] += 1
    return {'status': 'exact_finite_checks_only', 'source': 'original four poles; U0=0',
            'floating_point': False, 'counts': dict(sorted(counts.items())),
            'total_counted_instances': sum(counts.values()), 'prime_cases': rows,
            'carry_radii': radii, 'fixed_seed': str(fixed),
            'fixed_seed_first_floor_mismatch': first_mismatch,
            'BK_exponent': 'not numerically supplied; paper input only',
            'pi_normality': 'OPEN', 'RH': 'OPEN'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = run_checks()
    text = json.dumps(receipt, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(json.dumps({'output': str(args.output), 'counts': receipt['counts'],
                          'total_counted_instances': receipt['total_counted_instances']}, sort_keys=True))
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
