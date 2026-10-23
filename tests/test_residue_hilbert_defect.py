"""Exact tests for the residue/Hilbert retention-defect certificates (HDEF-01..04)."""
import unittest
from fractions import Fraction as Q

import sympy as sp

from observational_succ import residue_hilbert_defect as hd


class TestHDEF01Diagnostics(unittest.TestCase):
    def test_five_diagnostics_exact(self):
        for p in (2, 3, 5):
            for M in (1, 3, 4):
                d = hd.diagnostics(M, p)
                cf = hd.closed_forms(p)
                self.assertEqual(sp.simplify(d.coarse_overlap - cf["coarse_overlap"]), 0)
                self.assertEqual(sp.simplify(d.norm_diff_sq - cf["norm_diff_sq"]), 0)
                self.assertEqual(d.projection_prob, cf["projection_prob"])
                self.assertEqual(d.complementary, cf["complementary"])

    def test_overlap_is_one_over_sqrt_p(self):
        d = hd.diagnostics(4, 5)
        self.assertEqual(sp.simplify(d.coarse_overlap - 1 / sp.sqrt(5)), 0)
        self.assertEqual(d.projection_prob, Q(1, 5))

    def test_diagnostics_are_distinct(self):
        for p in (2, 3, 5):
            self.assertTrue(hd.diagnostics(3, p).all_distinct)


class TestHDEF02Environment(unittest.TestCase):
    def test_residue_environment_certificate(self):
        for p in (2, 3, 5):
            cert = hd.environment_certificate(4, p)
            self.assertTrue(cert.orthonormal)
            self.assertTrue(cert.vp_is_terminal_sector)        # V_p u_M == h^{(p-1)}
            self.assertTrue(cert.uniform_decomposition)
            self.assertEqual(sp.simplify(cert.uniform_channel_amplitude - 1 / sp.sqrt(p)), 0)
            self.assertTrue(cert.outcomes_sum_to_one)
            self.assertEqual(len(cert.outcome_probs), p)

    def test_vp_equals_terminal_residue_sector(self):
        M, p = 3, 5
        Vu = hd.dilate(hd.uniform_block(M), p)
        term = hd.residue_sector(M, p, p - 1)
        self.assertEqual(set(Vu), set(term))
        self.assertEqual(set(Vu), {5, 10, 15})


class TestHDEF03Fourier(unittest.TestCase):
    def test_magnitude_blind_phase_informative(self):
        for p in (3, 5, 7):
            mags_equal, phases_distinct = hd.magnitude_blind_phase_informative(p, 1)
            self.assertTrue(mags_equal)
            self.assertTrue(phases_distinct)

    def test_phase_encodes_residue(self):
        p = 5
        o0 = hd.character_sector_overlap(p, 1, 0)   # phase 1
        o1 = hd.character_sector_overlap(p, 1, 1)   # phase omega
        self.assertEqual(sp.simplify(sp.Abs(o0) - sp.Abs(o1)), 0)   # same magnitude
        self.assertNotEqual(sp.simplify(o0 - o1), 0)                # different phase

    def test_orientation_reversal_conjugates(self):
        for p in (3, 5):
            for r in range(1, p):
                self.assertTrue(hd.orientation_reversal_conjugates(p, 1, r))


class TestHDEF03ScopeBoundary(unittest.TestCase):
    """Pin the gcd(k,p)=1 hypothesis that HDEF-03 phase recovery requires (D'Alembert F1)."""

    def test_phase_recovery_fails_when_not_coprime(self):
        # non-coprime (k,p): distinct residues share a phase -> not recoverable
        for (p, k) in [(4, 2), (6, 2), (6, 3), (5, 5), (9, 3)]:
            mags_equal, phases_distinct = hd.magnitude_blind_phase_informative(p, k)
            self.assertTrue(mags_equal)
            self.assertFalse(phases_distinct)         # the honest False

    def test_phase_recovery_holds_when_coprime(self):
        for (p, k) in [(5, 1), (7, 1), (5, 2), (7, 3)]:
            _, phases_distinct = hd.magnitude_blind_phase_informative(p, k)
            self.assertTrue(phases_distinct)

    def test_collapsing_overlaps_receipt(self):
        # (p,k)=(4,2): phases 1,-1,1,-1 -> residues 0,2 collapse, 1,3 collapse
        vals = [hd.character_sector_overlap(4, 2, r) for r in range(4)]
        self.assertEqual(sp.simplify(vals[0] - vals[2]), 0)   # residue 0 == 2
        self.assertEqual(sp.simplify(vals[1] - vals[3]), 0)   # residue 1 == 3
        self.assertNotEqual(sp.simplify(vals[0] - vals[1]), 0)


class TestHDEF01BornRelationDerived(unittest.TestCase):
    """projection prob and outcome probs are DERIVED from the overlaps (D'Alembert F2)."""

    def test_projection_prob_is_overlap_squared(self):
        for p in (2, 3, 5):
            d = hd.diagnostics(3, p)
            # Born relation: the stored projection_prob equals |coarse_overlap|^2
            self.assertEqual(sp.simplify(d.coarse_overlap ** 2 - d.projection_prob), 0)
            self.assertEqual(d.projection_prob + d.complementary, 1)

    def test_outcome_probs_are_amplitudes_squared(self):
        for p in (2, 3, 5):
            cert = hd.environment_certificate(4, p)
            # each outcome prob equals |uniform_channel_amplitude|^2 = 1/p
            self.assertTrue(all(sp.simplify(sp.Abs(cert.uniform_channel_amplitude) ** 2 - pr) == 0
                                for pr in cert.outcome_probs))
            self.assertEqual(sum(cert.outcome_probs), 1)


class TestHDEF04PrimePowerAndFirewall(unittest.TestCase):
    def test_prime_power_overlap(self):
        for p in (2, 3):
            for r in (1, 2, 3):
                ov = hd.prime_power_overlap(3, p, r)
                self.assertEqual(sp.simplify(ov - 1 / sp.sqrt(p ** r)), 0)

    def test_log_commutator_eigenvalue(self):
        for p in (2, 3, 5):
            for n in (1, 2, 7):
                self.assertEqual(sp.simplify(hd.log_commutator_eigenvalue(p, n) - sp.log(p)), 0)

    def test_von_mangoldt_reconstruction(self):
        for p in (2, 3, 5):
            for r in (1, 2, 3):
                a, b = hd.von_mangoldt_reconstruction(p, r)
                self.assertEqual(sp.simplify(a - b), 0)
                # the coefficient is log p / p^{r/2}
                self.assertEqual(sp.simplify(a - sp.log(p) / sp.sqrt(p ** r)), 0)

    def test_magnitude_cannot_authenticate_primality(self):
        po, co = hd.magnitude_cannot_authenticate_primality(4, 5, 6)
        self.assertEqual(sp.simplify(po - 1 / sp.sqrt(5)), 0)
        self.assertEqual(sp.simplify(co - 1 / sp.sqrt(6)), 0)   # same 1/sqrt form
        self.assertGreater(float(po), 0)
        self.assertGreater(float(co), 0)

    def test_weil_firewall(self):
        fw = hd.weil_firewall()
        self.assertEqual(fw["RH_PROVED"], "NO")
        self.assertEqual(fw["is_not"], "the completed signed Weil distribution")
        self.assertIn("Gamma factor", fw["missing"])
        self.assertIn("signed positivity", " ".join(fw["missing"]))


if __name__ == "__main__":
    unittest.main()
