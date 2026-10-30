"""Integer LCM oracle for emitted adjacent-denominator witnesses.

Imports neither transfer_probe nor the parent PR implementation and does not
use Fraction. This is an implementation bearing, not independent provenance.
"""
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path


def adjacent_difference(n):
    # One common integer denominator for the literal four signed source rays.
    terms = [(15 * c * 16 ** (n - j), 8 * (j - 1) + d)
             for d, c in ((1, 4), (4, -2), (5, -1), (6, -1))
             for j in range(1, n + 1)]
    terms.extend((c, 8 * n + d)
                 for d, c in ((1, 4), (4, -2), (5, -1), (6, -1)))
    common = lcm(*(denominator for _, denominator in terms))
    numerator = sum(coefficient * (common // denominator)
                    for coefficient, denominator in terms)
    divisor = gcd(numerator, common)
    return numerator // divisor, common // divisor


def prefix_lcm(n):
    terms = [(c * 16 ** (n - j), 8 * (j - 1) + d)
             for d, c in ((1, 4), (4, -2), (5, -1), (6, -1))
             for j in range(1, n + 1)]
    common = lcm(*(den for _, den in terms))
    numerator = sum(a * (common // den) for a, den in terms)
    return Fraction(numerator, common)


def main():
    here = Path(__file__).resolve().parent
    data = json.loads((here / 'exact_receipt.json').read_text())
    results = []
    for row in data['grid_witnesses']:
        numerator, denominator = adjacent_difference(row['n'])
        assert numerator == int(row['difference_numerator'])
        assert denominator == int(row['difference_denominator'])
        product = int(row['product'])
        assert denominator % product == 0
        assert gcd(numerator, product) == 1
        assert all(denominator % (p * p) != 0 for p in row['plus'] + row['minus'])
        results.append(dict(n=row['n'], integer_lcm_match=True,
                            exact_prime_product_divides=True,
                            prime_count=len(row['plus']) + len(row['minus'])))
    periods = []
    for c in (3, 5):
        for j in range(1, 6):
            q, x, period = c ** j, 16 % (c ** j), 1
            while x != 1:
                x = x * 16 % q
                period += 1
            assert period == c ** (j - 1)
            periods.append(dict(c=c, stage=j, period=period))
    approximate = []
    approx_data = json.loads((here / 'approximate_grid_receipt.json').read_text())
    for row in approx_data['rows']:
        n = row['n']
        states = [prefix_lcm(j) for j in range(n, n + row['length'])]
        best = None
        for q in range(1, row['q_limit'] + 1):
            vals = [(q * x) % 1 for x in states]
            # Different algorithm: rotate each point to zero and minimize the range.
            arc = min(max((x - start) % 1 for x in vals) for start in vals)
            radius = arc / (2 * q)
            if best is None or radius < best[0]:
                best = radius, q
        assert best[0] == Fraction(row['minimum_radius'])
        assert best[1] == row['minimum_radius_q']
        assert best[0] > 2 * Fraction(row['declared_radius'])
        approximate.append(dict(n=n, exact_all_translation_minimum_match=True,
                                original_pi_grid_radius_excluded=True))
    print(json.dumps(dict(status='PASS', integer_lcm_witnesses=results,
                          independent_multiplicative_periods=periods,
                          independent_approximate_grid_checks=approximate), indent=2))


if __name__ == '__main__':
    main()
