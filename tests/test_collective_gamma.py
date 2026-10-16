"""Exact, hostile controls for collective Gamma clocks; no float oracle."""
from decimal import localcontext, ROUND_DOWN, ROUND_UP
from fractions import Fraction as F
from itertools import product
import unittest
from unittest.mock import patch

from observational_succ.collective_gamma import (
    GammaCertificateError, Interval, Rectangle, Strip, alias_bound,
    certify_gamma, cooperative_gamma, decode_lanes, is_joint_period,
    joint_period_pi, pi_interval, rational_gcd, sin_cos, uniform_error,
)


def overlap(a, b):
    return max(a.lower, b.lower) <= min(a.upper, b.upper)


def exact_exp_oracle(x):
    """Independent rational positive Taylor sum plus geometric remainder."""
    if x < 0:
        lo, hi = exact_exp_oracle(-x)
        return 1/hi, 1/lo
    term = total = F(1)
    for n in range(1, 300):
        term *= x/n
        total += term
    first = term*x/300
    return total, total+first/(1-x/301)


class RationalClockTests(unittest.TestCase):
    def test_joint_period_gcd_not_minimum_or_lcm_mesh(self):
        meshes = (F(1, 2), F(1, 3))
        self.assertEqual(rational_gcd(meshes), F(1, 6))
        self.assertEqual(joint_period_pi(meshes), 24)
        self.assertFalse(is_joint_period(meshes, 8))
        self.assertFalse(is_joint_period(meshes, 12))
        for k in range(-8, 9):
            self.assertTrue(is_joint_period(meshes, 24*k))
        self.assertEqual(joint_period_pi((F(2, 3), F(4, 9))), 18)

    def test_period_enumeration_independent_integer_congruences(self):
        for a, b in product(range(1, 7), repeat=2):
            hs = (F(a, 12), F(b, 12))
            period = joint_period_pi(hs)
            for k in range(1, 49):
                c = F(k, 2)
                direct = all((c*h/4).denominator == 1 for h in hs)
                self.assertEqual(direct, (c/period).denominator == 1)

    def test_duplicate_source_does_not_extend_period(self):
        self.assertEqual(joint_period_pi((F(1, 2),)*4), 8)
        self.assertEqual(joint_period_pi((F(1, 2), F(1, 3), F(1, 2))), 24)

    def test_invalid_meshes(self):
        for hs in ((), (0,), (-1,), (True,), (0.25,), ("1/4",)):
            with self.assertRaises(GammaCertificateError):
                rational_gcd(hs)


class DirectedArithmeticTests(unittest.TestCase):
    def test_arithmetic_contains_exact_endpoints(self):
        for a, b in product((F(-11, 7), F(-1, 3), F(0), F(2, 7), F(19, 5)), repeat=2):
            x, y = Interval.of(a, 20), Interval.of(b, 20)
            self.assertTrue((x+y).contains(a+b))
            self.assertTrue((x-y).contains(a-b))
            self.assertTrue((x*y).contains(a*b))
            if b:
                self.assertTrue((x/y).contains(a/b))
        x, y = Interval.hull(-3, 2), Interval.hull(-7, -1)
        for a, b in product((F(-3), F(2)), (F(-7), F(-1))):
            self.assertTrue((x*y).contains(a*b))
            self.assertTrue((x/y).contains(a/b))

    def test_exp_against_independent_rational_series(self):
        for x in (F(-7), F(-1, 3), F(0), F(1, 7), F(1), F(9, 2), F(17)):
            result = Interval.of(x).exp()
            lo, hi = exact_exp_oracle(x)
            self.assertLessEqual(result.lower, lo)
            self.assertGreaterEqual(result.upper, hi)
        small = Interval.of(-1000).exp()
        self.assertEqual(small.lower, 0)
        self.assertEqual(small.upper, F(1, 10**40))

    def test_pi_and_trig_known_values_and_reduction(self):
        p = pi_interval()
        self.assertGreater(p.lower, 3)
        self.assertLess(p.upper, F(22, 7))
        for x, sine, cosine in ((Interval.of(0), 0, 1), (p/2, 1, 0), (p, 0, -1), (1000*p, 0, 1)):
            s, c = sin_cos(x)
            self.assertTrue(s.contains(sine))
            self.assertTrue(c.contains(cosine))
            self.assertLess(s.width+c.width, F(1, 10**25))
        s, c = sin_cos(Interval.hull(-100, 100))
        self.assertEqual((s.lower, s.upper, c.lower, c.upper), (-1, 1, -1, 1))

    def test_trig_pythagorean_and_parity_holdouts(self):
        for x in (F(-71, 19), F(2, 3), F(1001, 7), F(19, 113)):
            s, c = sin_cos(Interval.of(x))
            sn, cn = sin_cos(Interval.of(-x))
            self.assertTrue((s*s+c*c).contains(1))
            self.assertTrue(overlap(-s, sn))
            self.assertTrue(overlap(c, cn))

    def test_ambient_decimal_context_cannot_change_certificate(self):
        results = []
        for precision, rounding in ((6, ROUND_DOWN), (90, ROUND_UP)):
            with localcontext() as ctx:
                ctx.prec, ctx.rounding = precision, rounding
                # Force both contexts through the actual transcendental path.
                from observational_succ.collective_gamma import _exp_endpoint
                _exp_endpoint.cache_clear()
                pi_interval.cache_clear()
                sin_cos.cache_clear()
                results.append(certify_gamma(1, F(1, 3), F(1, 2), -80, 8).as_dict())
        self.assertEqual(*results)

    def test_arithmetic_gates(self):
        for x in (True, 0.5, "0.5"):
            with self.assertRaises(GammaCertificateError):
                Interval.of(x)
        with self.assertRaises(GammaCertificateError):
            Interval.of(1)/Interval.hull(-1, 1)
        with self.assertRaises(GammaCertificateError):
            Interval.of(1, 20)+Interval.of(1, 40)
        with self.assertRaises(GammaCertificateError):
            Interval.of(10001).exp()


class CertifiedGammaTests(unittest.TestCase):
    def test_known_normative_real_place_values(self):
        p = pi_interval()
        targets = {1: Interval.of(1), 2: Interval.of(1)/p,
                   3: Interval.of(1)/(2*p), 4: Interval.of(1)/(p*p)}
        strip = Strip(1, 4, 4)
        for sigma, target in targets.items():
            result = certify_gamma(sigma, 0, F(1, 4), -200, 16, strip=strip)
            self.assertLessEqual(result.enclosure.real.lower, target.lower)
            self.assertGreaterEqual(result.enclosure.real.upper, target.upper)
            self.assertTrue(result.enclosure.imag.contains(0))
            self.assertLess(result.coordinate_radius, F(1, 10**8))

    def test_complex_recurrence_and_conjugation_fresh_points(self):
        for sigma, t in ((F(3, 2), F(5, 3)), (F(7, 3), F(-11, 7))):
            z = certify_gamma(sigma, t, F(1, 4), -200, 20).enclosure
            shifted = certify_gamma(sigma+2, t, F(1, 4), -200, 20).enclosure
            divisor = 2*pi_interval()
            self.assertTrue(overlap((sigma*z.real-t*z.imag)/divisor, shifted.real))
            self.assertTrue(overlap((t*z.real+sigma*z.imag)/divisor, shifted.imag))
            conjugate = certify_gamma(sigma, -t, F(1, 4), -200, 20).enclosure
            self.assertTrue(overlap(z.real, conjugate.real))
            self.assertTrue(overlap(-z.imag, conjugate.imag))

    def test_uniform_budget_responds_to_height_mesh_and_cutoff(self):
        narrow, wide = Strip(1, 4, 4), Strip(1, 4, 40)
        a = uniform_error(F(1, 2), narrow, -80, 8)
        b = uniform_error(F(1, 4), narrow, -160, 16)
        self.assertLess(b.alias*100000, a.alias)
        self.assertGreater(alias_bound(F(1, 2), wide), a.alias)
        self.assertLess(uniform_error(F(1, 4), narrow, -200, 20).left_tail, b.left_tail)
        self.assertEqual(narrow.contour_constant, 3)

    def test_cooperative_decoder_no_extra_s_and_fine_grid_identity(self):
        args = (F(3, 2), F(5, 3), F(3, 4), 3, -210, 18)
        result, lanes = cooperative_gamma(*args)
        direct = certify_gamma(args[0], args[1], F(1, 4), -210, 18)
        decoded = decode_lanes(v for _, v in lanes)
        self.assertEqual(decoded, result.finite_sum)
        self.assertTrue(overlap(decoded.real, direct.finite_sum.real))
        self.assertTrue(overlap(decoded.imag, direct.finite_sum.imag))
        reordered, _ = cooperative_gamma(*args, lanes=(2, 0, 1))
        self.assertEqual(result.as_dict(), reordered.as_dict())
        for omitted_or_repeated in ((0, 1), (0, 1, 1), (False, 1, 2)):
            with self.assertRaises(GammaCertificateError):
                cooperative_gamma(*args, lanes=omitted_or_repeated)

    def test_density_and_missing_history_mutants_fail_exact_one(self):
        certificate = certify_gamma(1, 0, F(1, 4), -200, 16)
        # Dropping h multiplies the source by 4. The authentic target is 1.
        raw = certificate.finite_sum.real*4
        self.assertGreater(raw.lower, 3)
        one_sided = certify_gamma(1, 0, F(1, 4), 0, 16)
        self.assertLess(one_sided.finite_sum.real.upper, F(1, 4))
        self.assertGreater(one_sided.error.left_tail, F(1, 2))
        self.assertTrue(one_sided.enclosure.real.contains(1))

    def test_source_rate_and_half_slope_mutations_are_detected(self):
        # Deliberate implementation mutants. They cannot inherit the theorem.
        from observational_succ.collective_gamma import _sample
        with patch("observational_succ.collective_gamma.pi_interval", lambda digits=40: Interval.of(1, digits)):
            mutated = _sample(1, 0, F(0), 40)
        authentic = _sample(1, 0, F(0), 40)
        self.assertGreater(mutated.real.lower, authentic.real.upper*8)
        # Dropping the half slope at s=1 gives the authentic s=2 source.
        doubled = certify_gamma(2, 0, F(1, 4), -200, 16)
        self.assertLess(doubled.enclosure.real.upper, F(1, 2))

    def test_failure_to_cancel_alias_is_observed_with_rational_enclosures(self):
        # Near the first coarse alias 8*pi. No float or pi-as-rational claim.
        t = F(2513274, 100000)
        strip = Strip(1, 1, 26)
        coarse = certify_gamma(1, t, F(1, 2), -160, 12, strip=strip)
        cooperative, lanes = cooperative_gamma(1, t, F(1, 2), 2, -320, 24, strip=strip)
        self.assertGreater(coarse.finite_sum.real.lower, F(99, 100))
        self.assertLess(cooperative.enclosure.real.upper, F(1, 1000))
        self.assertLess(cooperative.enclosure.imag.upper, F(1, 1000))
        self.assertGreater(cooperative.enclosure.real.lower, -F(1, 1000))
        self.assertGreater(cooperative.enclosure.imag.lower, -F(1, 1000))
        self.assertGreater(coarse.error.alias, 1)
        # Repeating lane zero cannot stand in for the missing shifted source.
        forged = decode_lanes((lanes[0][1], lanes[0][1]))
        self.assertGreater(forged.real.lower, F(99, 100))

    def test_domain_and_resource_gates(self):
        for args in ((0, 1, 1), (2, 1, 1), (1, 2, -1), (1, 65, 0)):
            with self.assertRaises(GammaCertificateError):
                Strip(*args)
        for args in ((0, 0, F(1, 4), -10, 4), (1, 0, 0, -10, 4),
                     (1, 0, F(1, 4), 1, 4), (1, 0, 1, -10, 21),
                     (1, 0, F(1, 4), -20000, 4)):
            with self.assertRaises(GammaCertificateError):
                certify_gamma(*args)
        with self.assertRaises(GammaCertificateError):
            certify_gamma(1, 5, F(1, 4), -100, 12, strip=Strip(1, 4, 4))
        with self.assertRaises(GammaCertificateError):
            uniform_error(F(1, 10), Strip(1, 64, 1), -10, 0)


if __name__ == "__main__":
    unittest.main()
