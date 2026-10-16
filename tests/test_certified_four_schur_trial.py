"""Regression tests for the certified four-mode Suzuki/Weil Schur instrument.

Fast configuration (small rank, small Gamma depth J): the VERDICT LOGIC and
the Loewner bracket STRUCTURE are J-independent, so a shallow J exercises them
cheaply. Deeper J (certifying A_4 > 0 and tightening the enclosure) is exercised
by scripts/certified_four_schur_trial_probe.py, not in the unit suite.
"""
import unittest
from fractions import Fraction as F

from observational_succ.certified_four_schur_trial import (
    CertifiedTrial, CertifiedTrialError, min_eig_lower, max_eig_upper,
    legendre_L2_norm2, ZERO_SHIFT_CAP, GPRIME_L1_UPPER, KAPPA,
)
from observational_succ.suzuki_moment_schur import positive_definite


RANK, J = 6, 3


class EigenvalueEnclosureTests(unittest.TestCase):
    def test_min_eig_lower_diagonal(self):
        M = ((F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)))
        lo = min_eig_lower(M, depth=40)
        self.assertLess(lo, F(1))              # strict lower bound on min eig 1
        self.assertGreater(lo, F(1) - F(1, 1000000))
        self.assertTrue(positive_definite(tuple(
            tuple(M[i][j] - (lo if i == j else F(0)) for j in range(3)) for i in range(3))))

    def test_max_eig_upper_diagonal(self):
        M = ((F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)))
        hi = max_eig_upper(M, depth=40)
        self.assertGreater(hi, F(3))
        self.assertLess(hi, F(3) + F(1, 1000000))

    def test_min_eig_lower_indefinite(self):
        M = ((F(1), F(2)), (F(2), F(1)))       # eigenvalues 3, -1
        self.assertLess(min_eig_lower(M, depth=40), F(0))
        self.assertGreater(max_eig_upper(M, depth=40), F(0))

    def test_legendre_L2_norm2(self):
        self.assertEqual(legendre_L2_norm2(1), F(1, 3))
        self.assertEqual(legendre_L2_norm2(4), F(1, 9))


class ConstantsTests(unittest.TestCase):
    def test_zero_shift_cap(self):
        self.assertEqual(GPRIME_L1_UPPER, F(11, 40))
        self.assertEqual(KAPPA, F(1, 50))
        self.assertEqual(ZERO_SHIFT_CAP, F(121, 32))
        self.assertEqual(ZERO_SHIFT_CAP, GPRIME_L1_UPPER ** 2 / KAPPA)


class SourceContractTests(unittest.TestCase):
    def test_parity_violating_U_is_invalid_source(self):
        # high mode 5 (odd) responding to low mode 2 (even): parity mismatch -> reject
        U = [[F(0), F(1, 10), F(0), F(0)]] + [[F(0)] * 4 for _ in range(RANK - 5)]
        out = CertifiedTrial(U=U, J=J, rank=RANK)
        self.assertEqual(out["verdict"], "INVALID_SOURCE")
        self.assertIn("parit", out["reason"].lower())

    def test_bad_J_is_invalid_source(self):
        self.assertEqual(CertifiedTrial(U=(), J=0, rank=RANK)["verdict"], "INVALID_SOURCE")
        self.assertEqual(CertifiedTrial(U=(), J=999, rank=RANK)["verdict"], "INVALID_SOURCE")

    def test_bad_rank_is_invalid_source(self):
        self.assertEqual(CertifiedTrial(U=(), J=J, rank=4)["verdict"], "INVALID_SOURCE")
        self.assertEqual(CertifiedTrial(U=(), J=J, rank=99)["verdict"], "INVALID_SOURCE")


class CertifiedBracketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = CertifiedTrial(U=(), J=J, rank=RANK, diagnostic=False)

    def test_u0_verdict_is_ambiguous(self):
        # the Young-capped lower bracket is indefinite and the upper bracket is
        # PSD -> the sign of S_4 is genuinely undetermined (CERTIFIED AMBIGUOUS).
        self.assertEqual(self.base["verdict"], "AMBIGUOUS")
        self.assertTrue(self.base["U_is_zero"])

    def test_upper_psd_lower_not_psd(self):
        self.assertTrue(self.base["upper_bracket_is_psd"])
        self.assertFalse(self.base["lower_bracket_is_psd"])

    def test_brackets_are_ordered_loewner(self):
        # upper_bracket - lower_bracket must be PSD (a genuine enclosure).
        up = tuple(tuple(F(x) for x in row) for row in self.base["upper_bracket"])
        lo = tuple(tuple(F(x) for x in row) for row in self.base["lower_bracket"])
        diff = tuple(tuple(up[i][j] - lo[i][j] for j in range(4)) for i in range(4))
        self.assertGreaterEqual(min_eig_lower(diff, depth=40), F(0))

    def test_brackets_symmetric_and_parity_block(self):
        for key in ("upper_bracket", "lower_bracket"):
            M = tuple(tuple(F(x) for x in row) for row in self.base[key])
            for i in range(4):
                for j in range(4):
                    self.assertEqual(M[i][j], M[j][i], f"{key} not symmetric")
                    if (i - j) % 2:
                        self.assertEqual(M[i][j], F(0), f"{key} off-parity nonzero")

    def test_no_nontrivial_zeros_and_rh_open(self):
        self.assertFalse(self.base["nontrivial_zero_coordinates_used"])
        self.assertFalse(self.base["RH_proved"])
        self.assertTrue(self.base["first_window_only_not_RH"])

    def test_deterministic(self):
        again = CertifiedTrial(U=(), J=J, rank=RANK, diagnostic=False)
        self.assertEqual(again["upper_bracket"], self.base["upper_bracket"])
        self.assertEqual(again["lower_bracket"], self.base["lower_bracket"])

    def test_parity_respecting_U_certifies_and_stays_ambiguous(self):
        # high mode 5 (odd) -> low modes 1,3 (odd): parity-respecting
        U = [[F(1, 10), F(0), F(1, 20), F(0)]] + [[F(0)] * 4 for _ in range(RANK - 5)]
        out = CertifiedTrial(U=U, J=J, rank=RANK)
        self.assertIn(out["verdict"], ("AMBIGUOUS", "POSITIVE_CERTIFIED", "NEGATIVE_CERTIFIED"))
        self.assertEqual(out["verdict"], "AMBIGUOUS")  # a finite trial does not decide the sign
        self.assertFalse(out["U_is_zero"])


if __name__ == "__main__":
    unittest.main()
