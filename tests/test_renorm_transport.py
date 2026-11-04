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


if __name__ == "__main__":
    unittest.main()
