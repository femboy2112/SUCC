"""BLACK SUN A-track tests: verified Carleman identity, window spectrum, controls.

Validates the independently re-derived windowed completed Weil representation
against the original Weil distribution at high precision, the elementary Kbar
closed form, the mandatory contact tail, the first-window spectrum with its
controls (fake-6 blindness, wrong-contact sensitivity), and the Omega 2*pi band.
"""
import unittest

import numpy as np

from observational_succ.black_sun_window import (
    BlackSunWindowError,
    C_G,
    carleman_vs_weil_check,
    contact_tail,
    kbar_elementary,
    kbar_series,
    lowest_eigenvalues,
    prime_atoms_window,
    von_mangoldt_exact,
    window_form_matrix,
    weil_original,
    autocorr_exact_callable,
    carleman_exact_layers,
)


def _mp():
    import mpmath as mp
    return mp


class TestKbarClosedForm(unittest.TestCase):
    """BS-1: Kbar(z) = (1/2)ln((1+e^{-z/2})/(1-e^{-z/2})) + arctan(e^{-z/2})."""

    def test_matches_defining_series(self):
        mp = _mp()
        for z in ("0.05", "0.2", "0.5", "1.0", "3.0", "10.0"):
            zs = mp.mpf(z)
            self.assertAlmostEqual(
                float(kbar_elementary(zs)), float(kbar_series(zs, dps=30)),
                places=24, msg=f"Kbar closed form vs series at z={z}")

    def test_large_z_asymptotic(self):
        mp = _mp()
        # leading term 2 e^{-z/2}
        z = mp.mpf("20")
        lead = 2*mp.e**(-z/2)
        self.assertLess(abs(kbar_elementary(z)-lead), float(2*mp.e**(-3*z/2)))


class TestContactTailTrap(unittest.TestCase):
    """The [2a, inf) contact tail is mandatory: +2 h(0) atanh(e^{-2a})."""

    def test_tail_value(self):
        mp = _mp()
        t = contact_tail(1, mp.mpf("0.5"), dps=30)
        # 2 atanh(e^{-1})
        expect = 2*mp.atanh(mp.e**(-1))
        self.assertAlmostEqual(float(t), float(expect), places=28)

    def test_identity_flat_indicator(self):
        """Centerpiece: W(1_W autocorr) == Carleman(1_W) at a=1/2, 25 digits.

        v = 1 on [-1/2, 1/2]: h = triangle (2a-|t|)+, E_G = 2 sum
        (1-e^{-alpha_j})/alpha_j^2 (exact with polygamma tail).
        """
        mp = _mp()
        mp.mp.dps = 40
        a = mp.mpf("0.5")
        M = 16
        nodes = [mp.mpf(x) for x in
                 [float(-a + i/M) for i in range(M+1)]]
        vals = [mp.mpf(1)]*(M+1)
        h = autocorr_exact_callable(nodes, vals)
        W = weil_original(h, a, dps=40)
        # Carleman: E_G exact series + polygamma tail
        L = 2*a
        S1 = mp.fsum((1-mp.e**(-(mp.mpf(2*j)+mp.mpf("0.5"))*L)) /
                     (mp.mpf(2*j)+mp.mpf("0.5"))**2 for j in range(2000))
        # exact tail: sum_{j>=2000} 1/alpha_j^2 = (1/4) psi1(2000.25)
        # (alpha_j = 2(j+1/4); e^{-alpha_j L} negligible)
        tail = mp.mpf("0.25")*mp.polygamma(1, mp.mpf("2000.25"))
        EG = 2*(S1 + tail)
        CG = mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
        C = mp.quad(lambda x: mp.cosh(x/2), [-a, a])   # int of 1*cosh
        S = mp.mpf("0")                                # 1*sinh odd integral
        pole = 2*C**2-2*S**2
        # prime-2: overlap of 1_W with its log2 shift
        ov = mp.quad(lambda x: mp.mpf(1), [-a, a-mp.log(2)])
        prim = -2*(mp.log(2)/mp.sqrt(2))*ov
        Q = EG-CG*(2*a)+pole+prim
        self.assertAlmostEqual(float(W), float(Q), places=24,
                               msg="Carleman identity on flat indicator")

    def test_identity_random_piecewise_linear(self):
        """W == Carleman on random piecewise-linear v (tolerance set by the
        exact-layer-sum truncation J; documented)."""
        mp = _mp()
        rng = np.random.default_rng(20261014)
        for trial, a in ((0, 0.5), (1, 0.36)):
            M = 10
            vs = rng.standard_normal(M+1)*0.5
            W, Q, resid = carleman_vs_weil_check(list(vs), a, dps=30)
            self.assertLess(float(resid), 1e-5,
                            f"trial {trial}: |W-Q| = {float(resid)}")

    def test_truncation_without_tail_breaks_identity(self):
        """The trap: dropping the contact tail changes W by ~0.77 at a=1/2
        for the flat test (quantified regression lock)."""
        mp = _mp()
        mp.mp.dps = 30
        a = mp.mpf("0.5")
        M = 16
        nodes = [mp.mpf(x) for x in [float(-a+i/M) for i in range(M+1)]]
        vals = [mp.mpf(1)]*(M+1)
        h = autocorr_exact_callable(nodes, vals)
        W_full = weil_original(h, a, dps=30)
        # recompute W without the tail: integrate contact only to 2a
        mp.mp.dps = 30
        h0 = h(0)
        I1 = mp.quad(lambda x: h(x)*(mp.e**(x/2)+mp.e**(-x/2)),
                     [-2*a, 0, 2*a])
        I2 = mp.mpf('0')
        for (ell, lam) in [(mp.log(2), mp.log(2))]:
            I2 -= (lam/mp.sqrt(mp.e**ell))*(h(ell)+h(-ell))
        I3 = -(mp.euler+mp.log(4*mp.pi))*h0
        I4 = -mp.quad(lambda x: (mp.e**(-x/2)*(h(x)+h(-x)-2*mp.e**(-x/2)*h0)
                                /(1-mp.e**(-2*x))) if x != 0 else h0/2,
                      [0, 2*a])
        W_trunc = I1+I2+I3+I4
        self.assertGreater(float(abs(W_full-W_trunc)), 0.5,
                           "contact tail must change W substantially")
        self.assertAlmostEqual(float(abs(W_full-W_trunc)), 0.7719, places=2)


class TestWindowSpectrum(unittest.TestCase):
    """First-window spectrum and the A/prime decomposition (TESTED MODEL)."""

    def test_prime_atoms_window(self):
        atoms = prime_atoms_window(0.30)
        self.assertEqual(atoms, [])  # log2 > 2a: no atoms below log2/2
        atoms = prime_atoms_window(0.5)
        self.assertEqual(len(atoms), 1)
        self.assertAlmostEqual(atoms[0][0], np.log(2), places=12)
        self.assertAlmostEqual(atoms[0][1], np.log(2)/np.sqrt(2), places=12)
        atoms = prime_atoms_window(0.6)
        self.assertEqual(len(atoms), 2)  # n=2,3
        atoms = prime_atoms_window(0.75)
        self.assertEqual(len(atoms), 3)  # n=2,3,4 (4=2^2)
        self.assertAlmostEqual(sum(1 for _ in prime_atoms_window(0.5493)), 1)

    def test_lambda_min_positive_at_small_window(self):
        vals, _, _, _ = lowest_eigenvalues(0.36, M=1200, k=2)
        self.assertGreater(vals[0], 5e-4, "lambda_min(0.36) should be ~+8.5e-4")
        self.assertLess(vals[0], 1.3e-3)

    def test_lambda_min_near_zero_at_larger_windows(self):
        for a in (0.48, 0.5493):
            vals, _, _, _ = lowest_eigenvalues(a, M=1200, k=2)
            self.assertLess(abs(vals[0]), 3e-4,
                            f"lambda_min({a}) should be within 3e-4 of 0")
            self.assertLess(abs(vals[1]), 3e-3,
                            f"second eigenvalue near zero at a={a}")

    def test_archimedean_part_negative_prime_rescues(self):
        """A-form (no prime) has lambda_0 ~ -0.28 at a=0.5; adding the
        prime-2 atom lands the full Q near zero: the exact compensation."""
        valsQ, _, _, _ = lowest_eigenvalues(0.5, M=1200, k=1, include_prime=True)
        valsA, _, _, _ = lowest_eigenvalues(0.5, M=1200, k=1, include_prime=False)
        self.assertLess(valsA[0], -0.2, "A-form should be strongly negative")
        self.assertGreater(valsA[0], -0.4)
        self.assertLess(abs(valsQ[0]), 3e-4,
                        "full windowed form lands near zero")

    def test_fake6_blind_on_first_window(self):
        """Source mutation control: a fake primitive composite impulse at
        log 6 is INVISIBLE to the first-prime window (2a < log 6): the
        first-window spectrum cannot authenticate against it (IH-01-style
        finite-observer blindness, here as a theorem-grade exact statement)."""
        vals0, _, _, _ = lowest_eigenvalues(0.5, M=800, k=2, fake6_impulse=0.0)
        vals1, _, _, _ = lowest_eigenvalues(0.5, M=800, k=2, fake6_impulse=100.0)
        for x, y in zip(vals0, vals1):
            self.assertAlmostEqual(x, y, 9,
                                msg="fake-6 must be invisible on first window")
        # but visible once the window covers log 6: a >= log(6)/2
        va, _, _, _ = lowest_eigenvalues(0.9, M=800, k=1, fake6_impulse=0.0)
        vb, _, _, _ = lowest_eigenvalues(0.9, M=800, k=1, fake6_impulse=100.0)
        self.assertGreater(abs(vb[0]-va[0]), 0.01,
                           "fake-6 must be visible when window covers log 6")

    def test_wrong_contact_sensitivity(self):
        """Wrong-normalization control: the classical missing-2log2 trap
        (contact_error = -2 log 2) flips the first-window spectrum decisively;
        the razor-thin margin is exactly of this scale."""
        from math import log
        vals_ok, _, _, _ = lowest_eigenvalues(0.36, M=800, k=1)
        vals_bad, _, _, _ = lowest_eigenvalues(0.36, M=800, k=1,
                                               contact_error=+2*log(2.0))
        vals_easy, _, _, _ = lowest_eigenvalues(0.36, M=800, k=1,
                                               contact_error=-2*log(2.0))
        self.assertGreater(vals_ok[0], 0)
        # over-claiming the contact by +2log2 falsely certifies negativity;
        # dropping it by -2log2 falsely inflates positivity by the same
        # scale: the razor-thin margin is exactly of order 2log2.
        self.assertLess(vals_bad[0], -1.0)
        self.assertGreater(vals_easy[0], 1.3)

    def test_omega_band_structure(self):
        """Omega(u) = Re psi(1/4+iu/2) - log pi: Omega(0) = -C_G, negative
        band up to 2pi, positive beyond, ~ log(u/2pi)."""
        mp = _mp()
        mp.mp.dps = 30

        def Omega(u):
            return mp.re(mp.digamma(mp.mpf("0.25")+1j*mp.mpf(u)/2))-mp.log(mp.pi)
        self.assertAlmostEqual(float(Omega(0)), float(-C_G(30)), places=18)
        self.assertLess(float(Omega(2*mp.pi)), 0)
        self.assertGreater(float(Omega(2*mp.pi)), -0.01)
        self.assertGreater(float(Omega(7)), 0.09)
        self.assertGreater(float(Omega(50)), float(mp.log(50/(2*mp.pi)))-0.05)
        self.assertLess(float(Omega(50)), float(mp.log(50/(2*mp.pi)))+0.05)


class TestDomainErrors(unittest.TestCase):

    def test_bad_window(self):
        with self.assertRaises(BlackSunWindowError):
            window_form_matrix(0.0, 100)
        with self.assertRaises(BlackSunWindowError):
            window_form_matrix(0.5, 8)


if __name__ == "__main__":
    unittest.main()