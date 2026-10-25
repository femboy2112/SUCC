"""Exact formal, interval and hostile-source tests for the Euler/Li bridge."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial

import mpmath as mp

from observational_succ.observer_reflection import RationalInterval as I
from observational_succ.euler_gamma_li_bridge import (
    GammaLiError, stieltjes_log_coefficients, stieltjes_log_intervals,
    li_from_stieltjes, li_intervals_from_stieltjes,
    stieltjes_successor_intervals, integer_zeta_interval, certified_li_prefix,
    first_new_stieltjes_sensitivity, symmetric_anchor_polynomial,
    finite_jet_countermodel_contract,
)


def mul(a, b, degree):
    return [sum((a[j]*b[k-j] for j in range(k+1)
                 if j < len(a) and k-j < len(b)), Q(0))
            for k in range(degree+1)]


def log_by_powers(unit, degree):
    """Independent oracle: finite log(1+u)=u-u²/2+..., no log recurrence."""
    u = [Q(0)]+list(unit[1:])
    power = [Q(1)]+[Q(0)]*degree
    ans = [Q(0)]*(degree+1)
    for j in range(1, degree+1):
        power = mul(power, u, degree)
        for k in range(degree+1):
            ans[k] += Q((-1)**(j+1), j)*power[k]
    return tuple(ans[1:])


def evaluate(coefficients, z):
    return sum((a*z**j for j, a in enumerate(coefficients)), Q(0))


def mpq(q):
    return mp.mpf(q.numerator)/q.denominator


class EulerGammaLiExact(unittest.TestCase):
    def test_log_recurrence_matches_independent_polynomial_log(self):
        for d in range(1, 13):
            g = tuple(Q((-1)**j*(j+2), j+3) for j in range(d))
            unit = (Q(1),)+tuple(Q((-1)**j, factorial(j))*x for j, x in enumerate(g))
            self.assertEqual(stieltjes_log_coefficients(g), log_by_powers(unit, d))

    def test_first_two_completed_coefficients_by_closed_formula(self):
        g0, g1, ell, z2 = Q(3, 5), Q(-1, 15), Q(5, 2), Q(13, 8)
        actual = li_from_stieltjes((g0, g1), log_four_pi=ell, integer_zeta={2: z2})
        self.assertEqual(actual[0], 1+g0/2-ell/2)
        self.assertEqual(actual[1], 1+g0-g0*g0-2*g1-ell+3*z2/4)

    def test_new_stieltjes_jet_has_exact_triangular_sensitivity(self):
        for m in range(12):
            g = tuple(Q(j+1, j+3) for j in range(m+1))
            mutant = g[:-1]+(g[-1]+Q(2, 7),)
            zs = {k: Q(k+3, k) for k in range(2, m+2)}
            a = li_from_stieltjes(g, log_four_pi=Q(9, 4), integer_zeta=zs, arch_euler_gamma=Q(3, 5))
            b = li_from_stieltjes(mutant, log_four_pi=Q(9, 4), integer_zeta=zs, arch_euler_gamma=Q(3, 5))
            self.assertEqual(a[:-1], b[:-1])
            self.assertEqual(b[-1]-a[-1], first_new_stieltjes_sensitivity(m)*Q(2, 7))

    def test_interval_transport_contains_independent_corner_models(self):
        boxes = (I(Q(1, 2), Q(3, 5)), I(Q(-1, 10), Q(-1, 20)), I(Q(-1, 20), Q(1, 30)))
        ell = I(Q(5, 2), Q(51, 20))
        zs = {2: I(Q(8, 5), Q(5, 3)), 3: I(Q(6, 5), Q(5, 4))}
        output = li_intervals_from_stieltjes(boxes, log_four_pi=ell, integer_zeta=zs)
        logs = stieltjes_log_intervals(boxes)
        for choices in product((0, 1), repeat=6):
            gs = tuple((box.lower, box.upper)[choices[j]] for j, box in enumerate(boxes))
            exell = (ell.lower, ell.upper)[choices[3]]
            exzs = {k: (zs[k].lower, zs[k].upper)[choices[k+2]] for k in (2, 3)}
            actual = li_from_stieltjes(gs, log_four_pi=exell, integer_zeta=exzs)
            for box, x in zip(output, actual):
                self.assertLessEqual(box.lower, x); self.assertLessEqual(x, box.upper)
            for box, x in zip(logs, stieltjes_log_coefficients(gs)):
                self.assertLessEqual(box.lower, x); self.assertLessEqual(x, box.upper)

    def test_exact_intervals_recover_exact_models(self):
        g = (Q(2, 3), Q(-1, 7), Q(1, 31))
        zs = {2: Q(5, 3), 3: Q(6, 5)}
        a = li_from_stieltjes(g, log_four_pi=Q(5, 2), integer_zeta=zs)
        b = li_intervals_from_stieltjes(tuple(I.exact(x) for x in g),
                log_four_pi=I.exact(Q(5, 2)), integer_zeta={k: I.exact(v) for k, v in zs.items()})
        self.assertEqual(tuple((v.lower, v.upper) for v in b), tuple((x, x) for x in a))

    def test_completion_channels_are_required_and_detect_wrong_gamma(self):
        g = (Q(3, 5), Q(-1, 15))
        with self.assertRaises(GammaLiError):
            li_from_stieltjes(g, log_four_pi=Q(5, 2), integer_zeta={})
        good = li_from_stieltjes(g, log_four_pi=Q(5, 2), integer_zeta={2: Q(13, 8)})
        bad = li_from_stieltjes(g, log_four_pi=0, integer_zeta={2: 0})
        self.assertNotEqual(good, bad)
        # A fixed completion and a coupled gamma mutation are distinct.
        self.assertEqual(first_new_stieltjes_sensitivity(0), 1)
        self.assertEqual(first_new_stieltjes_sensitivity(0, coupled_arch_gamma=True), Q(1, 2))

    def test_symmetric_polynomial_has_declared_anchor_and_vanishing_jet(self):
        for m in range(2, 11):
            for q in (Q(1, 4), Q(2, 5), Q(3, 4), Q(7, 8)):
                p = symmetric_anchor_polynomial(m, q)
                self.assertTrue(all(x == 0 for x in p[:m]))
                self.assertEqual(evaluate(p, q-1), 1)
                self.assertEqual(evaluate(p, -q), 1)
                for s in (Q(-2), Q(-1, 5), Q(1, 7), Q(1, 2), Q(5, 2)):
                    self.assertEqual(evaluate(p, s-1), evaluate(p, -s))

    def test_countermodel_preserves_finite_li_jet_exactly(self):
        for m in range(2, 9):
            # The argument applies to any nonzero normalized analytic xi jet.
            degree = m+2
            unit = (Q(1),)+tuple(Q(1, j+3) for j in range(1, degree+1))
            p = symmetric_anchor_polynomial(m)
            mutant = tuple(unit[j]-Q(7, 11)*(p[j] if j < len(p) else 0)
                           for j in range(degree+1))
            a, b = log_by_powers(unit, degree), log_by_powers(mutant, degree)
            self.assertEqual(a[:m-1], b[:m-1])
            self.assertNotEqual(a[m-1], b[m-1])
            for n in range(1, m):
                self.assertEqual(sum(comb(n-1, k-1)*a[k-1] for k in range(1, n+1)),
                                 sum(comb(n-1, k-1)*b[k-1] for k in range(1, n+1)))
            contract = finite_jet_countermodel_contract(m)
            self.assertTrue(contract["changes_arithmetic_source"])
            self.assertFalse(contract["original_zeta_counterexample"])
            self.assertFalse(contract["RH_proved"])

    def test_rejects_malformed_source_and_unlicensed_monotonic_tail(self):
        for bad in ((), [Q(1)], (0.5,), (True,)):
            with self.assertRaises(GammaLiError):
                stieltjes_log_coefficients(bad)
        for n, d in ((1, 2), (8, 3), (26, 4), (True, 1), (10001, 1)):
            with self.assertRaises(GammaLiError):
                stieltjes_successor_intervals(n, d)
        for q in (Q(1, 2), Q(0), Q(1), 0.75):
            with self.assertRaises(GammaLiError):
                symmetric_anchor_polynomial(4, q)
        for e in (1, 0, True, 2.0):
            with self.assertRaises(GammaLiError):
                integer_zeta_interval(e, 16)


class EulerGammaLiAnalyticCalibration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = certified_li_prefix(3, 512)

    def test_source_intervals_enclose_stieltjes_numerical_holdouts(self):
        with mp.workdps(65):
            for m, interval in enumerate(self.receipt["stieltjes"]):
                value = mp.stieltjes(m)
                self.assertLess(mpq(interval.lower), value)
                self.assertLess(value, mpq(interval.upper))
            for k, interval in self.receipt["integer_zeta"].items():
                self.assertLess(mpq(interval.lower), mp.zeta(k))
                self.assertLess(mp.zeta(k), mpq(interval.upper))

    def test_first_three_true_li_coefficients_are_rationally_positive(self):
        # Positivity follows from the rational lower endpoints, not mpmath.
        self.assertEqual(self.receipt["strictly_positive_through"], 3)
        self.assertTrue(all(x.lower > 0 for x in self.receipt["li"]))
        self.assertFalse(self.receipt["RH_proved"])
        with mp.workdps(65):
            g, g1, g2 = (mp.stieltjes(k) for k in range(3))
            ell = mp.log(4*mp.pi)
            known = (1+g/2-ell/2,
                1+g-g*g+mp.pi**2/8-2*g1-ell,
                1+mp.mpf(3)/2*g-3*g*g+g**3+3*g*g1-6*g1
                +mp.mpf(3)/2*g2+3*mp.pi**2/8-mp.mpf(7)/8*mp.zeta(3)-mp.mpf(3)/2*ell)
            for interval, value in zip(self.receipt["li"], known):
                self.assertLess(mpq(interval.lower), value)
                self.assertLess(value, mpq(interval.upper))

    def test_real_countermodel_anchor_is_not_an_existing_zeta_zero(self):
        with mp.workdps(60):
            q = mp.mpf(3)/4
            xi_q = q*(q-1)*mp.pi**(-q/2)*mp.gamma(q/2)*mp.zeta(q)/2
            self.assertGreater(xi_q, 0)
            self.assertLess(mp.zeta(q), 0)
            for m in (2, 5, 11):
                p = symmetric_anchor_polynomial(m)
                factor = evaluate(p, Q(-1, 4))
                self.assertEqual(xi_q-xi_q*mpq(factor), 0)
            # This manufactured zero belongs only to the changed-source xi.

    def test_degree_eight_against_direct_completed_xi_taylor(self):
        # Independent numerical calibration, NOT an interval certificate.
        with mp.workdps(80):
            def logarithm(t):
                if t == 0:
                    return mp.mpf(0)
                s = 1/(1-t)
                return mp.log(s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))
            coefficient = mp.taylor(logarithm, 0, 8)
            g = tuple(Q(mp.nstr(mp.stieltjes(j), 75)) for j in range(8))
            result = li_from_stieltjes(g,
                log_four_pi=Q(mp.nstr(mp.log(4*mp.pi), 75)),
                integer_zeta={k: Q(mp.nstr(mp.zeta(k), 75)) for k in range(2, 9)})
            for n, value in enumerate(result, 1):
                self.assertLess(abs(mpq(value)-n*coefficient[n]), mp.mpf("1e-65"))


if __name__ == "__main__":
    unittest.main()
