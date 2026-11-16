"""Independent exact countermodels for the Main XXVI source repairs.

These finite regressions guard source/target distinctions. The infinite
coboundary result additionally uses the written hypothesis g(N)/16**N -> 0;
no finite test establishes that limit or pi normality.
"""

from fractions import Fraction
import unittest


def original_forcing(n):
    """Independent literal four-pole formula; no research helper imported."""
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def states_and_prefixes(g, count):
    original = [Fraction(0)]
    changed = [Fraction(0)]
    prefixes = [(Fraction(0), Fraction(0))]
    for n in range(1, count+1):
        r = original_forcing(n)
        changed_r = r + g(n) - 16*g(n-1)
        original.append(16*original[-1] + r)
        changed.append(16*changed[-1] + changed_r)
        a, b = prefixes[-1]
        prefixes.append((a + r/16**n, b + changed_r/16**n))
    return original, changed, prefixes


def arithmetic_residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def original_tail_interval(n, depth=32):
    """Exact interval from positive decreasing r and the geometric tail."""
    low = sum((original_forcing(n+j)/16**j
               for j in range(1, depth+1)), Fraction(0))
    high = low + original_forcing(n+depth+1)/(15*16**depth)
    return low, high


class MainXXVISourceTransport(unittest.TestCase):
    def test_noninteger_gauge_has_exact_finite_prefix_and_tail_remainders(self):
        # Rational, nonconstant, noninteger and polynomially bounded; g(0)=0.
        g = lambda n: Fraction(n**3 - 3*n, 7)
        original, changed, prefixes = states_and_prefixes(g, 32)
        for n in range(33):
            self.assertEqual(changed[n]-original[n], g(n))
            a, b = prefixes[n]
            self.assertEqual(b-a, g(n)/16**n)
            for depth in (1, 3, 8):
                finite_tail_change = sum(
                    ((g(n+j)-16*g(n+j-1))/16**j
                     for j in range(1, depth+1)), Fraction(0))
                self.assertEqual(finite_tail_change,
                                 -g(n) + g(n+depth)/16**depth)
                self.assertEqual(changed[n]-original[n]+finite_tail_change,
                                 g(n+depth)/16**depth)
        # Noninteger gauges preserve completed lifts, not necessarily the
        # uncompleted real circle. The true tail correction is indispensable.
        self.assertNotEqual(changed[1] % 1, original[1] % 1)

    def test_arbitrary_finite_rational_gauge_telescopes_without_smoothness(self):
        values = [Fraction(0)] + [Fraction((-1)**n*(n*n+3), 2*n+1)
                                  for n in range(1, 41)]
        g = values.__getitem__
        original, changed, prefixes = states_and_prefixes(g, 40)
        for n in range(41):
            self.assertEqual(changed[n]-original[n], g(n))
            self.assertEqual(prefixes[n][1]-prefixes[n][0], g(n)/16**n)
        # This finite table has no asserted asymptotic continuation.

    def test_polynomial_integer_gauge_preserves_circle_changes_winding(self):
        g = lambda n: 2*n*n
        original, changed, prefixes = states_and_prefixes(g, 64)
        for n in range(65):
            self.assertEqual(changed[n]-original[n], g(n))
            self.assertEqual(changed[n] % 1, original[n] % 1)
            self.assertEqual(changed[n].denominator, original[n].denominator)
            self.assertEqual(changed[n].numerator//changed[n].denominator
                             - original[n].numerator//original[n].denominator,
                             g(n))
            self.assertEqual(prefixes[n][1]-prefixes[n][0],
                             Fraction(g(n), 16**n))
        # The nonzero finite remainder must not be mislabeled a changed
        # completed constant; its limit is paid by the polynomial hypothesis.
        self.assertNotEqual(prefixes[2][0], prefixes[2][1])

    def test_integer_gauge_changes_actual_source_holonomy(self):
        g = lambda n: 2*n*n
        original, changed, _ = states_and_prefixes(g, 42)
        for n in range(2, 24):
            jet = arithmetic_residue((original[n+16]-original[n])/16, 16)
            mutated_jet = arithmetic_residue((changed[n+16]-changed[n])/16, 16)
            self.assertEqual((mutated_jet-jet) % 16, 4*n % 16)
            next_jet = arithmetic_residue((original[n+18]-original[n+2])/16, 16)
            next_mutated = arithmetic_residue((changed[n+18]-changed[n+2])/16, 16)
            self.assertEqual((next_jet-jet) % 16, 8)
            self.assertEqual((next_mutated-mutated_jet) % 16, 0)

    def test_wrong_sign_coboundary_is_rejected(self):
        g = lambda n: 2*n*n
        correct = bad = Fraction(0)
        for n in range(1, 4):
            r = original_forcing(n)
            correct = 16*correct + r + g(n) - 16*g(n-1)
            bad = 16*bad + r + g(n) + 16*g(n-1)
        self.assertNotEqual(correct, bad)

    def test_integer_winding_cannot_be_dropped_before_arithmetic_readout(self):
        u = original_forcing(1)
        self.assertEqual(u, Fraction(47, 15))
        reduced = u % 1
        self.assertEqual(arithmetic_residue(u, 16), 1)
        self.assertEqual(arithmetic_residue(reduced, 16), 14)
        self.assertEqual((16*reduced).numerator//(16*reduced).denominator, 2)

    def test_positive_lag_source_norm_and_zero_lag_boundary(self):
        for n in (0, 1, 4, 13):
            for lag in (1, 2, 5):
                # PS12: T_(2n)-2T_(2n+lag)+T_(2n+2lag).
                a0, b0 = original_tail_interval(2*n)
                a1, b1 = original_tail_interval(2*n+lag)
                a2, b2 = original_tail_interval(2*n+2*lag)
                self.assertGreater(a0-2*b1+a2, 0)
                self.assertGreater(b0-2*a1+b2, a0-2*b1+a2)
            for t in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
                source_mark = t**(8*n)
                self.assertEqual((source_mark-source_mark)**2, 0)
                for lag in (1, 2, 5):
                    self.assertGreater((source_mark-t**(8*(n+lag)))**2, 0)


if __name__ == '__main__':
    unittest.main()
