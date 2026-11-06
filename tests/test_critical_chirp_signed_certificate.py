"""Finite signed instrument guards; no asymptotic statistical assertions."""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1]/"research/2026-11-04/critical_chirp_source/signed_probe.py"
SPEC = importlib.util.spec_from_file_location("critical_chirp_signed_certificate", PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


class SignedCertificateTests(unittest.TestCase):
    def test_exact_roots_of_unity_and_periodicity(self):
        for x, target in [(F(0), (1, 0)), (F(1, 4), (0, 1)),
                          (F(1, 2), (-1, 0)), (F(3, 4), (0, -1))]:
            a, b = probe.character_grid(x)
            self.assertLessEqual(abs(F(a, probe.OUTPUT)-target[0])+
                                 abs(F(b, probe.OUTPUT)-target[1]), probe.CHAR_ERROR)
            self.assertEqual((a, b), probe.character_grid(x+10**30))

    def test_maximum_is_not_full_epoch(self):
        points = [probe.character_grid(F(0)), probe.character_grid(F(1, 2))]
        cert = probe.maximal_certificate(points)
        self.assertLessEqual(F(cert["M_lower"]), F(1, 2))
        self.assertGreaterEqual(F(cert["M_upper"]), F(1, 2))
        self.assertEqual(cert["intervals_checked"], 3)

    def test_constant_periodic_control(self):
        points = [probe.character_grid(F(1, 5))]*16
        cert = probe.maximal_certificate(points)
        self.assertLessEqual(F(cert["M_lower"]), 1)
        self.assertEqual(F(cert["M_upper"]), 1)
        self.assertGreater(F(cert["M_lower"]), F(999999, 1000000))

    def test_oracle_and_critical_schedule(self):
        for A in (8, 16, 32, 64):
            self.assertEqual(probe.source_epoch(A), probe.integer_epoch(A))
            for h in (1, 3):
                j, H = probe.critical_schedule(A, h)
                self.assertEqual(H, h*16**j)
                self.assertEqual((j, H), probe.critical_schedule(A, -h))

    def test_integer_diameter_includes_interior_witness(self):
        q = probe.OUTPUT
        cert = probe.maximal_certificate([(q, 0), (0, q), (-q, 0), (0, -q)])
        self.assertEqual(int(cert["grid_max_squared"]), 2*q*q)
        self.assertEqual(cert["intervals_checked"], 10)

    def test_real_source_conjugate_certificates_overlap(self):
        phases = probe.source_epoch(8)
        a = probe.run_case(8, 1, phases)
        b = probe.run_case(8, -1, phases)
        for model in ("zero_seed", "coherent_changed_seed"):
            self.assertLessEqual(F(a[model]["M_lower"]), F(b[model]["M_upper"]))
            self.assertLessEqual(F(b[model]["M_lower"]), F(a[model]["M_upper"]))

    def test_invalid_and_underresolved_inputs_rejected(self):
        for A, h in [(1, 1), (7, 1), (8, 0), (8, 10**20)]:
            with self.assertRaises(ValueError):
                probe.critical_schedule(A, h)
        with self.assertRaises(ArithmeticError):
            probe.character_grid(F(1, 3), F(1, 1000))
        with self.assertRaises(ValueError):
            probe.character_grid(F(1, 3), F(-1))
        with self.assertRaises(ValueError):
            probe.maximal_certificate([])


if __name__ == "__main__":
    unittest.main()
