"""Finite tests with an unshared direct rational oracle; no universal proof claim."""
import unittest
from fractions import Fraction as F

import transport as t

HOLDOUT = (131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
FAMILIES = ((4, -2, -1, -1), (5, -2, -1, -1), (4, 0, -1, 0),
            (5, 7, 2, -3), (F(1, 2), F(-2, 3), F(7, 5), F(-11, 4)))


def independent_prefix(n, weights=(4, -2, -1, -1), seed=F()):
    """Authentic oracle uses the combined rational source, not channel summation."""
    u = F(seed)
    for j in range(1, n + 1):
        if weights == (4, -2, -1, -1):
            forcing = F(120*j*j - 89*j + 16,
                        (2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
        else:
            forcing = sum((F(c) / (8*j-d) for c, d in zip(weights, (7, 4, 3, 2))), F())
        u = 16 * u + forcing
    return u


class ArithmeticTransportTests(unittest.TestCase):
    def test_native_parent_and_required_cancellation(self):
        for p in (13, 17, 29, 37, 41, 53, 73):
            for k in range(1, 5):
                if p <= 8*k-2:
                    continue
                n = ((4*k-1)*p+1)//4
                self.assertEqual(t.rational_mod(p*independent_prefix(n), p),
                                 t.rational_mod(independent_prefix(k), p))
        remote = independent_prefix(274)
        self.assertNotEqual(remote.denominator % 73, 0)
        self.assertEqual(t.rational_mod(independent_prefix(4), 73), 0)

    def test_all_classes_fresh_prime_holdout(self):
        self.assertEqual({p % 8 for p in HOLDOUT}, {1, 3, 5, 7})
        for p in HOLDOUT:
            for k in (1, 2, 4):
                n = t.clock(p, 1, k)
                for weights in FAMILIES:
                    with self.subTest(p=p, k=k, coefficients=weights):
                        exact = t.rational_mod(p*independent_prefix(n, weights), p)
                        self.assertEqual(exact, t.layer_residue(p, 1, k, coefficients=weights))
                        self.assertEqual(exact, t.rational_mod(t.shadow_prefix(p, 1, k, weights), p))

    def test_even_prime_power_return_and_odd_reflection(self):
        cases = ((7, 2, 1), (11, 2, 1), (13, 2, 1), (17, 2, 1),
                 (19, 2, 2), (23, 2, 2), (7, 4, 1), (11, 3, 1), (7, 3, 1))
        for p, a, k in cases:
            # p7 at reflected k1 is outside p>7; assert exclusion explicitly.
            if a % 2 and p == 7:
                with self.assertRaises(ValueError):
                    t.clock(p, a, k)
                continue
            exact = t.rational_mod(p**a*independent_prefix(t.clock(p, a, k)), p)
            self.assertEqual(exact, t.rational_mod(t.shadow_prefix(p, a, k), p))
            if a % 2 == 0:
                self.assertEqual(exact, t.rational_mod(independent_prefix(k), p))

    def test_full_precision_lift_and_mutations(self):
        cases = ((13, 1, 1), (17, 1, 2), (19, 1, 2), (23, 1, 2),
                 (29, 1, 3), (7, 2, 1), (11, 2, 1), (11, 3, 1), (7, 4, 1))
        omitted_layer_fails = omitted_derivative_fails = False
        for p, a, k in cases:
            n = t.clock(p, a, k)
            for weights in FAMILIES:
                u = independent_prefix(n, weights)
                exact = t.rational_mod(p**a*u, p*p)
                self.assertEqual(exact, t.first_lift(p, a, k, weights))
                for r in (1, 2, 3, 4):
                    self.assertEqual(t.rational_mod(p**a*u, p**r),
                                     t.layer_residue(p, a, k, r, weights))
                v = t.rational_mod(t.shadow_prefix(p, a, k, weights), p*p)
                remainder = t.next_layer(p, a, k, weights)
                omitted_derivative_fails |= (v + p*remainder) % (p*p) != exact
                omitted_layer_fails |= (t.first_lift(p, a, k, weights)-p*remainder) % (p*p) != exact
        self.assertTrue(omitted_layer_fails)
        self.assertTrue(omitted_derivative_fails)
        self.assertEqual(t.rational_mod(13*independent_prefix(10)-independent_prefix(1), 169), 65)

    def test_first_birth_every_odd_prime_and_depth(self):
        for p, maximum in ((3, 6), (5, 4), (7, 4), (11, 3), (13, 2), (17, 2), (19, 2)):
            for a in range(1, maximum+1):
                n, residue = t.power_birth(p, a)
                u = independent_prefix(n)
                self.assertEqual(t.valuation(u, p), -a)
                self.assertEqual(t.rational_mod(p**a*u, p), t.rational_mod(residue, p))
                if n > 1:
                    self.assertGreater(t.valuation(independent_prefix(n-1), p), -a)

    def test_all_four_packets_and_reflected_cancellation(self):
        for p in HOLDOUT + (11, 13, 17, 19, 23, 31, 41, 47):
            times, expected = t.packet(p)
            for n, value in zip(times, expected):
                self.assertEqual(t.rational_mod(p*independent_prefix(n), p), value)
        for n in range(10, 17):
            self.assertNotEqual(independent_prefix(n).denominator % 19, 0)
        self.assertEqual(independent_prefix(9).denominator % 19, 0)
        self.assertEqual(independent_prefix(17).denominator % 19, 0)

    def test_reflected_support_obstruction_and_short_window(self):
        self.assertEqual(set(3*s % 8 for s in t.OFFSETS), set(t.REFLECTED))
        self.assertEqual(set(7*s % 8 for s in t.OFFSETS), set(t.REFLECTED))
        self.assertNotEqual(set(t.REFLECTED), set(t.OFFSETS))
        times, _ = t.packet(11)
        self.assertEqual(times[1]-times[0], 2)
        self.assertEqual(pow(16, 5, 11), 1)
        self.assertTrue(all(pow(16, d, 11) != 1 for d in range(1, 5)))

    def test_seed_blindness_and_precision_boundary(self):
        for p, a, k in ((13, 1, 1), (19, 1, 2), (11, 2, 1)):
            n = t.clock(p, a, k)
            u = independent_prefix(n)
            for seed in (F(1, 16), F(1, 256), F(1, 3), F(17, 15), F(1, 7)):
                shifted = independent_prefix(n, seed=seed)
                self.assertEqual(t.rational_mod(p**a*shifted, p**a),
                                 t.rational_mod(p**a*u, p**a))
                self.assertEqual(t.rational_mod(p**a*(shifted-u), p**(a+1)),
                                 t.rational_mod(p**a*16**n*seed, p**(a+1)))
            self.assertNotEqual(t.rational_mod(p**a*independent_prefix(n, seed=F(1, 3)), p**(a+1)),
                                t.rational_mod(p**a*u, p**(a+1)))

    def test_ratio_mutants_and_fixed_support_jet_rigidity(self):
        for p in (13, 29, 37, 149, 157, 173, 181, 197):
            for weights, expected_equal in ((FAMILIES[1], False), (FAMILIES[2], True)):
                n = t.clock(p, 1, 1)
                actual = t.rational_mod(p*independent_prefix(n, weights), p)
                native = t.rational_mod(independent_prefix(1, weights), p)
                self.assertEqual(actual == native, expected_equal)
        # Exact one-dimensional solution after J, Q(0), and Q'(0); Q'' closes it.
        for C in map(F, (-3, -2, -1, 0, 1, 2)):
            A, B, D = -4*C, (19*C+15)/2, (-15-13*C)/2
            self.assertEqual(A+B+C+D, 0)
            self.assertEqual(-3*B-4*C-5*D, 15)
            self.assertEqual(9*B+16*C+25*D, -61*C-120)
            self.assertEqual(9*B+16*C+25*D == -59, C == -1)

    def test_exceptional_source_passports(self):
        factors = ((2, -1), (4, -1), (8, -7), (8, -3))
        constants = (6, 20, 1920, -32)
        for (a, b), expected in zip(factors, constants):
            x = F(-b, a)
            self.assertEqual(a*a*(120*x*x-89*x+16), expected)
        for n in range(1, 201):
            forcing = t.source(n)
            selected = independent_prefix(n)
            self.assertEqual(forcing.denominator % 2, 1)
            self.assertEqual(selected.denominator % 2, 1)
            self.assertEqual(t.rational_mod(selected, 16), t.rational_mod(forcing, 16))
            self.assertEqual(t.rational_mod(selected, 2), n % 2)
        self.assertGreaterEqual(t.valuation(t.source(8), 3), 0)
        self.assertGreaterEqual(t.valuation(t.source(24), 5), 0)

    def test_positive_gamma_matched_arithmetic_mutant(self):
        c = (F(2), F(11, 4), F(-1, 2), F(-17, 4))
        A,B,C,D = c
        self.assertEqual(t.shadow(149, 1, c)[1], c)
        self.assertEqual(sum(c), 0)
        self.assertEqual(-3*B-4*C-5*D, 15)
        self.assertEqual(9*B+16*C+25*D, -F(179, 2))
        # Degree five equality at seven exact points certifies the polynomial.
        for j in range(7):
            x = F(j, 6)
            self.assertEqual(A+B*x**3+C*x**4+D*x**5,
                (1-x)*(17*x**4+19*x**3+8*x*x+8*x+8)/4)
        for p in (149, 157, 173):
            n = t.clock(p, 1, 1)
            self.assertEqual(t.rational_mod(p*independent_prefix(n,c), p),
                             t.rational_mod(independent_prefix(1,c), p))

    def test_domain_guards(self):
        for args in ((2, 1, 1), (9, 1, 1), (7, 1, 1), (13, 1, 2), (13, 0, 1)):
            with self.assertRaises(ValueError):
                t.clock(*args)
        with self.assertRaises(ValueError):
            t.shadow(13, 1, (F(1, 13), 0, 0, 0))
        with self.assertRaises(ValueError):
            t.rational_mod(F(1, 13), 13)

    def test_published_null_relation_and_signed_reflected_tail(self):
        Z = (-8, 8, 4, 8, 2, 2, -1, 0)
        # Both sides are polynomials of degree <=10; 13 exact points suffice.
        for j in range(13):
            x = F(j, 12)
            polynomial = sum((c*x**i for i, c in enumerate(Z)), F())
            self.assertEqual(polynomial*(x*x-2)*(x*x-2*x+2),
                             16*(x*x-4*x+2)*(1-x**8/16))
        for n in range(1, 129):
            reflected = t.source(n, (8, 4, 4, -1), t.REFLECTED)
            self.assertEqual(reflected-2*t.source(n), t.source(n, Z, tuple(range(1, 9))))
            w = t.prefix(n, (8, 4, 4, -1), t.REFLECTED)
            correction = w-2*independent_prefix(n)
            self.assertLess(correction, 0)
            self.assertGreater(correction, -F(1, 8*n+1))

    def test_zero_seed_coherent_null_has_all_odd_conductor_depths(self):
        Z = (-8, 8, 4, 8, 2, 2, -1, 0)
        for p, maximum in ((3, 6), (5, 4), (7, 4), (11, 3), (13, 2), (17, 2)):
            for a in range(1, maximum+1):
                Q = p**a
                if Q < 7:
                    continue
                n = (Q+7)//8
                e = t.prefix(n, Z, tuple(range(1, 9)))
                self.assertEqual(t.valuation(e, p), -a)
                self.assertEqual(t.rational_mod(Q*e, p), Z[Q%8-1] % p)
                self.assertLess(e, 0)
                self.assertGreater(e, -F(1, 8*n+1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
