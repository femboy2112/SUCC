"""Exact rational and scoped finite theta/Gamma/Li hostile checks.

The universal mathematical assertions are PROOFS, not implied by these
finite numerical calibrations. RH and pi normality remain open.
"""
import unittest
from fractions import Fraction
import mpmath as mp

from observational_succ.theta_dual_triangle_probe import (
    laguerre_pascal, inverse_pascal, pascal_extrude, signed_li,
    theta_k, I_theta, xi_theta, xi_original, theta_triangle_a,
    gamma_first_vertex, fake_atom, phi_theta, dual_theta_halves,
    finite_source_log_current, xi_derivative_current,
)


class ExactTriangle(unittest.TestCase):
    def test_source_coefficients_exact(self):
        for n in range(1, 17):
            row = laguerre_pascal(n)
            self.assertEqual(row[0], n)
            self.assertGreater(row[-1], 0)
            self.assertEqual(len(row), n)

    def test_pascal_inverse_all_orders(self):
        for n in range(1, 15):
            c = tuple(Fraction(j+2, 3*j+7) for j in range(n))
            self.assertEqual(inverse_pascal(pascal_extrude(c)), c)
            b = [pascal_extrude(c)[j]/(j+1) for j in range(n)]
            for _ in range(n):
                self.assertTrue(all(v > 0 for v in b))
                b = [b[j+1]-b[j] for j in range(len(b)-1)]

    def test_signed_log_not_positive_from_positive_coefficients(self):
        a = tuple(Fraction(16*n, 3) for n in range(1, 7))
        lam = signed_li(a)
        self.assertGreater(lam[0], 0)
        self.assertEqual(lam[1], Fraction(-64, 9))

    def test_inputs_fail_closed(self):
        for v in (-1, 0, 1.2, True):
            with self.assertRaises(ValueError):
                laguerre_pascal(v)
        with self.assertRaises(ValueError):
            signed_li(())
        with self.assertRaises(ValueError):
            inverse_pascal([1, 2])


class AuthenticTheta(unittest.TestCase):
    def test_full_gamma_zeta_completion(self):
        with mp.workdps(50):
            for s in (mp.mpf(".5"), mp.mpf("2"),
                      mp.mpc(".7", "2"), mp.mpc(".5", "4")):
                self.assertLess(abs(xi_theta(s)-xi_original(s)), mp.mpf("1e-45"))

    def test_first_li_and_gamma(self):
        with mp.workdps(48):
            a1 = theta_triangle_a(1)
            self.assertLess(abs(a1-gamma_first_vertex()), mp.mpf("1e-42"))
            self.assertGreater(a1, 0)

    def test_completed_li_2_and_4(self):
        with mp.workdps(48):
            a = tuple(theta_triangle_a(n) for n in range(1, 5))
            lam = signed_li(a)
            g = mp.euler
            expected2 = 1+g-g*g+mp.pi**2/8-2*mp.stieltjes(1)-mp.log(4*mp.pi)
            self.assertLess(abs(lam[1]-expected2), mp.mpf("1e-42"))
            self.assertTrue(all(x > 0 for x in lam))

    def test_completed_phi_positive_and_source_gamma(self):
        with mp.workdps(48):
            for t in (mp.mpf(0), mp.mpf(".1"), mp.mpf(".5"), mp.mpf(1)):
                self.assertGreater(theta_k(t), 0)
                self.assertGreater(phi_theta(t), 0)

    def test_canonical_theta_HB_orientation_reverses(self):
        with mp.workdps(48):
            for y, sign in ((mp.mpf(".25"), 1), (mp.mpf(1), -1)):
                e, es = dual_theta_halves(mp.j*y)
                delta = abs(e)**2-abs(es)**2
                self.assertEqual((delta > 0)-(delta < 0), sign)

    def test_original_log_clock_one_point_checks(self):
        with mp.workdps(45):
            for x, y in ((0, ".25"), (5, ".25"), (17, ".25")):
                self.assertGreater(xi_derivative_current(mp.mpc(x, y)), 0)


class HostileControls(unittest.TestCase):
    def test_positive_atom_offcritical_zeros(self):
        with mp.workdps(48):
            self.assertEqual(fake_atom(0), 1)
            self.assertEqual(fake_atom(1), 1)
            self.assertLess(fake_atom(mp.mpf(".5")), 0)
            self.assertLess(4*mp.e*(1-mp.e), 0)

    def test_two_time_kernel_matches_independent_phase(self):
        with mp.workdps(55):
            atoms = ((mp.mpf(0), mp.mpf(2)),
                     (mp.mpf(".2"), mp.mpf(".5")),
                     (mp.mpf("1.3"), mp.mpf("1.5")))
            for u in (mp.mpc(0, ".25"), mp.mpc(3, ".4"),
                      mp.mpc(17, ".25")):
                a, b = finite_source_log_current(atoms, u)
                self.assertLess(abs(a-b), mp.mpf("1e-48"))

    def test_changed_composite_six_is_not_source_invariant(self):
        with mp.workdps(115):
            s = mp.mpf(2)
            a = 36*mp.pi
            delta = s*(s-1)/2*(
                mp.gammainc(s/2, a, mp.inf)/a**(s/2)+
                mp.gammainc((1-s)/2, a, mp.inf)/a**((1-s)/2))
            self.assertGreater(abs(delta), mp.mpf("1e-70"))
            self.assertLess(abs(delta), mp.mpf("1e-40"))

    def test_wrong_gamma_does_not_match(self):
        with mp.workdps(48):
            s = mp.mpf(2)
            bad = s*(s-1)*mp.pi**(-s/2)*mp.gamma((s+1)/2)*mp.zeta(s)/2
            self.assertGreater(abs(bad-xi_original(s)), mp.mpf("1e-5"))


if __name__ == "__main__":
    unittest.main()
