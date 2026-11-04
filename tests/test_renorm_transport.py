"""RENORM transport tests: exact source, calibration, and the RENORM-1 bound.

No pi digits, no normality claim. Exponential sums are a calibrated instrument.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import mpmath as mp

MOD = Path(__file__).resolve().parents[1] / "research" / "2026-11-03" / "renorm_transport" / "renorm_transport.py"
spec = importlib.util.spec_from_file_location("renorm_transport", MOD)
rt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rt)


class RenormTransport(unittest.TestCase):
    def setUp(self):
        mp.mp.dps = 40

    def test_immutable_source_first_terms(self):
        from fractions import Fraction as F
        self.assertEqual(rt.source_force(1), F(4, 1) - F(2, 4) - F(1, 5) - F(1, 6))
        # U_0 = 0 anchoring: first phase is {r(1)} since 16*0 + r(1)
        self.assertEqual(rt.source_epoch(2)[0] % 1, (16 * rt.source_force(1) + rt.source_force(2)) % 1)

    def test_calibration_c0_is_one(self):
        ph = rt.source_epoch(40)
        self.assertLess(abs(rt.coeff(ph, 0) - 1), mp.mpf(10) ** (-30))

    def test_two_blind_sources_agree(self):
        # zero-seed source vs independent odd-conductor modular source: identical phases
        for A in (40, 64):
            ph, phm = rt.source_epoch(A), rt.modular_epoch(A)
            self.assertEqual(list(ph), list(phm))
            for h in (1, 3, 7, 50):
                self.assertLess(abs(rt.coeff(ph, h) - rt.coeff(phm, h)), mp.mpf(10) ** (-30))

    def test_renorm1_bound_holds_on_heldout(self):
        # RENORM-1: |c_A(h) - c_A(16h)| <= 2/A + 15 pi |h| / (4 A (8A-15))
        for A in (40, 64, 128):
            ph = rt.source_epoch(A)
            for h in (1, 3, 8, 50, 100):
                res = float(rt.renorm_residual(ph, h))
                self.assertLessEqual(res, rt.eps_bound_rigorous(A, h),
                                     msg=f"RENORM-1 violated at A={A}, h={h}")

    def test_bound_is_nonvacuous(self):
        # the bound is tight, not a free pass: residual is a real fraction of it
        ph = rt.source_epoch(64)
        res = float(rt.renorm_residual(ph, 50))
        self.assertGreater(res, 0.3 * rt.eps_bound_rigorous(64, 50))

    def test_barrier_transports_not_shrinks(self):
        # RENORM-2: |c_A(h)| and |c_A(16h)| are the same order (mass moved up, not killed)
        ph = rt.source_epoch(256)
        lo = float(abs(rt.coeff(ph, 1)))
        hi = float(abs(rt.coeff(ph, 16)))
        self.assertGreater(hi, 0.5 * lo)  # not driven to zero by one transport step

    def test_bound_is_general_not_a_source_discriminator(self):
        # Honest boundary: a scaled-forcing mutant r'(n)=s*r(n) ALSO satisfies RT-2.
        # RT-1/RT-2 are general (any small-forcing x16 recurrence), not a BBP fingerprint.
        from fractions import Fraction as F
        def mutant(A, s):
            z = F(0); out = []
            for n in range(1, 2 * A):
                z = (16 * z + s * rt.source_force(n)) % 1
                if n >= A: out.append(z)
            return out
        for A in (40, 64):
            for s in (3, 5):
                mu = mutant(A, s)
                for h in (100, 200):
                    res = float(abs(rt.coeff(mu, h) - rt.coeff(mu, 16 * h)))
                    self.assertLessEqual(res, rt.eps_bound_rigorous(A, h))

    def test_build_receipt_no_violations(self):
        rec = rt.build_receipt()
        self.assertEqual(rec["rigorous_bound_violations"], 0)
        self.assertEqual(rec["pi_base16_normality"], "OPEN")
        self.assertEqual(
            rec["defect_regression"]["D3_acc_error_true_le_correct_bound"]["violations"], 0)

    # ---- regression tests for the three corrected RT-03 defects + the converse ----

    def test_D1_old_depth_has_wrong_exponent(self):
        # the ORIGINAL per-h depth j*=floor(.5 log16(A^1.5/|h|)) reaches ~A^{3/4} sqrt|h|,
        # NOT A^{3/2}. Lock the defect: reached/A^{3/2} -> 0, reached/(A^{3/4} sqrt|h|) ~ O(1).
        for A in (16 ** 4, 16 ** 8):
            for h in (1, 16, 100):
                reached = rt.reached_frequency_old(A, h)
                self.assertLess(reached / A ** 1.5, 1e-2,
                                msg=f"old depth must NOT reach A^3/2 (A={A},h={h})")
                ratio = reached / (A ** 0.75 * h ** 0.5)
                self.assertTrue(0.2 <= ratio <= 1.01,
                                msg=f"old depth reaches ~A^3/4 sqrt|h| (A={A},h={h}, ratio={ratio})")

    def test_D2_old_depth_noninjective_but_common_depth_injective(self):
        # D2: the per-h depth collapses h=1 and h=16 onto 16^6 at A=16^8.
        A = 16 ** 8
        self.assertEqual(rt.reached_frequency_old(A, 1), rt.reached_frequency_old(A, 16))
        self.assertEqual(rt.reached_frequency_old(A, 1), 16 ** 6)
        # fix: a COMMON depth makes h -> 16^j h injective over the whole band
        H = 64
        j = rt.common_depth(A, H)
        targets = [16 ** j * h for h in range(1, H + 1)]
        self.assertEqual(len(set(targets)), H, "common-depth transport must be injective")

    def test_D3_accumulated_error_correct_bound_and_geometric(self):
        # D3: true accumulated error <= CORRECT bound 2j/A + pi|h|(16^j-1)/(4A(8A-15)).
        for A in (40, 64, 128, 256):
            ph = rt.source_epoch(A)
            for h in (1, 3):
                for j in (1, 2, 3):
                    if 16 ** j * h > A * A:
                        continue
                    t = float(rt.acc_error_true(ph, h, j))
                    self.assertLessEqual(t, rt.acc_error_bound(A, h, j),
                                         msg=f"acc error exceeds corrected bound A={A},h={h},j={j}")
        # the forcing part is GEOMETRIC: bound(j+1)-2(j+1)/A ~ 16*(bound(j)-2j/A)
        A, h = 256, 1
        f1 = rt.acc_error_bound(A, h, 2) - 2.0 * 2 / A
        f2 = rt.acc_error_bound(A, h, 3) - 2.0 * 3 / A
        self.assertGreater(f2 / f1, 10.0, "forcing term must grow geometrically (~16x), not linearly")

    def test_D0_band_to_J_converse_is_false(self):
        # D0: equally-spaced cloud has J_q=1 but unweighted band = 2q. So J=o(K) does
        # NOT imply unweighted-band=o(K); only band=>J is proved (SC-8, sinc^2<=1).
        from fractions import Fraction as F
        for q in (4, 8, 16, 32):
            J, band = rt.band_vs_J_cloud(q)
            self.assertEqual(J, F(1), f"equally-spaced cloud has J_q=1 (q={q})")
            self.assertEqual(band, 2 * q, f"unweighted band = 2q (q={q})")

    def test_common_depth_barrier_is_o1_and_injective_reach(self):
        # corrected RENORM-2: common depth keeps top freq <= A^{3/2} with o(1) edge error < 1.
        for A, H in ((64, 2), (256, 4), (1024, 6)):
            j = rt.common_depth(A, H)
            self.assertLessEqual(16 ** j * H, A ** 1.5)
            self.assertLess(rt.acc_error_bound(A, H, j), 1.0)


if __name__ == "__main__":
    unittest.main()
