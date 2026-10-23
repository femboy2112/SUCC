"""Phase 7 hostile matrix: positive/negative/null/mutation controls.

Each test either confirms a guard fires (negative control) or shows a wrong
convention is DETECTED (mutation control). The mandatory failure modes from the
carry-safe round are enumerated; d'Alembert's live attack found no computational
kill, and these controls regression-protect that result.
"""
import unittest
from fractions import Fraction as Q

import sympy as sp

from observational_succ import carry_safe_polyphase as csp
from observational_succ import future_sufficient_information as fsi
from observational_succ import source_controlled_tomography as sct
from observational_succ import residue_hilbert_defect as hd
from observational_succ.reciprocal_succ_fucc import ReciprocalSourceError


class TestOneBasedOrigin(unittest.TestCase):
    def test_one_based_reconstruct_not_zero_based(self):
        # correct: n = q(m-1)+r+1. A zero-based mutation q*m'+r (no +1) gives n-1.
        for q in (2, 3, 5):
            for n in range(1, 30):
                m, r = csp.polyphase_coords(n, q)
                self.assertEqual(csp.from_polyphase_coords(m, r, q), n)      # correct
                zero_based = q * (m - 1) + r                                 # mutant
                self.assertEqual(zero_based, n - 1)                          # off by one
                self.assertNotEqual(zero_based, n)

    def test_origin_maps_to_block_one_residue_zero(self):
        for q in (2, 3, 5):
            self.assertEqual(csp.polyphase_coords(1, q), (1, 0))


class TestTerminalResidueAndCarry(unittest.TestCase):
    def test_terminal_residue_p_minus_1_not_0(self):
        for p in (2, 3, 5, 7):
            self.assertEqual(csp.u_image(1, p, p - 1), p)          # V_p: 1 -> p
            for n in range(2, 8):
                self.assertEqual(csp.u_image(n, p, p - 1), p * n)
                self.assertNotEqual(csp.u_image(n, p, 0), p * n)   # residue 0 is wrong

    def test_carry_at_every_boundary(self):
        for q in (2, 3, 4, 5):
            for n in range(1, 60):
                self.assertTrue(csp.carry_successor_holds(n, q))
            # mutation: a no-carry successor ignoring r=q-1 breaks n+1
            m, r = csp.polyphase_coords(q, q)          # (1, q-1): at the boundary
            no_carry = (m, r + 1)                      # wrong: residue q is illegal
            with self.assertRaises(csp.PolyphaseError):
                csp.from_polyphase_coords(*no_carry, q)   # residue out of range


class TestCuntzCutoffNotFull(unittest.TestCase):
    def test_finite_cutoff_has_horizon_defect(self):
        # treating a finite compression as a full Cuntz rep is a mutation:
        rep = csp.cuntz_relations(3, source_dim=5, target_dim=20)
        self.assertFalse(rep.clean)                    # NOT the infinite relation
        self.assertEqual(rep.defect_rank, 5)
        self.assertEqual(rep.defect_support, tuple(range(16, 21)))

    def test_clean_only_when_target_is_q_times_source(self):
        clean = csp.cuntz_relations(3, source_dim=5)   # target_dim defaults to 15
        self.assertTrue(clean.clean)
        self.assertEqual(clean.defect_rank, 0)

    def test_adjoint_zero_on_nondivisible(self):
        iso = csp.residue_isometry(3, 1, source_dim=6)  # images 2,5,8,11,14,17
        adj = iso.adjoint()
        self.assertIsNone(adj.apply(4))                 # 4 not an image -> 0
        self.assertEqual(adj.apply(2), 1)               # 2 = u_image(1,3,1)
        self.assertEqual(adj.apply(5), 2)               # 5 = u_image(2,3,1)


class TestMixedRadixWrongPermutation(unittest.TestCase):
    def test_correct_convention_matches_literal_composition(self):
        self.assertTrue(csp.closed_form_matches([(2, 1), (3, 2)], dim=8))

    def test_wrong_convention_detected(self):
        # correct digit is p*s+r; the reversed order q*r+s (a valid residue but
        # the WRONG composition order) disagrees with the literal composition.
        p, r, q, s, n = 2, 1, 3, 1, 4
        correct_q, correct_R = csp.two_factor_compose(p, r, q, s)    # (6, 3)
        _, reversed_R = csp.reversed_two_factor(p, r, q, s)          # 4 != 3
        literal = csp.compose_on_basis([(p, r), (q, s)], n)
        self.assertEqual(csp.u_image(n, correct_q, correct_R), literal)
        self.assertNotEqual(correct_R, reversed_R)                  # order matters
        self.assertNotEqual(csp.u_image(n, correct_q, reversed_R), literal)

    def test_noncoprime_is_not_crt(self):
        coprime, _ = csp.is_crt_decomposition(2, 2)
        self.assertFalse(coprime)


class TestFakePrimeAndPrimePower(unittest.TestCase):
    def test_composite_label_rejected(self):
        for composite in (4, 6, 8, 9, 15):
            with self.assertRaises(ReciprocalSourceError):
                csp.prime_fucc_embedding(composite, dim=5)

    def test_prime_power_handled_in_hdef_not_rejected(self):
        # von Mangoldt sees p^r as a prime power (Lambda = log p), not rejected
        for p, r in [(2, 2), (3, 2), (2, 3)]:
            a, b = hd.von_mangoldt_reconstruction(p, r)
            self.assertEqual(sp.simplify(a - b), 0)

    def test_k_off_diagonal_rejects_bad_multiplier(self):
        with self.assertRaises(sct.TomographyError):
            sct.k_off_diagonal(1, 2, 1, 2, multipliers=(1,))   # multiplier < 2


class TestTomographyFirewallAndCounterfeit(unittest.TestCase):
    def test_counterfeit_v6_invisible_then_detected(self):
        self.assertTrue(sct.counterfeit_invisible(6, [(2, 3), (1, 3), (1, 5)]))
        self.assertFalse(sct.counterfeit_invisible(6, [(1, 6)]))

    def test_physical_access_blocked(self):
        for bad in (2, 3, 4, 5, 1.0, True):
            with self.assertRaises(sct.TomographyError):
                sct.assert_mathematical_only(bad)
        self.assertTrue(sct.assert_mathematical_only(1))

    def test_sigma_bound_holds_near_eta_one(self):
        from math import log
        sigma = 2
        q13, q15 = 1 / 3 ** sigma, 1 / 5 ** sigma
        for eta in (Q(9, 10), Q(99, 100)):
            bound = sct.sigma_error_bound(eta)
            e = float(eta)
            worst = max(abs(log((q13 * s13) / (q15 * s15)) / log(5 / 3) - sigma)
                        for s13, s15 in ((1 + e, 1 - e), (1 - e, 1 + e)))
            self.assertLessEqual(worst, float(bound) + 1e-9)


class TestHilbertNullAndPhaseControls(unittest.TestCase):
    def test_overlap_is_not_one(self):
        # null control: the coarse overlap is 1/sqrt(p), never 1 (information IS lost)
        d = hd.diagnostics(4, 5)
        self.assertNotEqual(sp.simplify(d.coarse_overlap - 1), 0)
        self.assertEqual(sp.simplify(d.coarse_overlap - 1 / sp.sqrt(5)), 0)

    def test_phase_recovery_scope_boundary(self):
        # non-coprime character does NOT recover the residue (mutation of the claim)
        _, distinct = hd.magnitude_blind_phase_informative(4, 2)
        self.assertFalse(distinct)
        _, distinct_ok = hd.magnitude_blind_phase_informative(5, 1)
        self.assertTrue(distinct_ok)

    def test_magnitude_does_not_authenticate_primality(self):
        po, co = hd.magnitude_cannot_authenticate_primality(4, 5, 6)
        self.assertEqual(sp.simplify(po - 1 / sp.sqrt(5)), 0)
        self.assertEqual(sp.simplify(co - 1 / sp.sqrt(6)), 0)     # composite, same form

    def test_weil_firewall_rh_not_proved(self):
        self.assertEqual(hd.weil_firewall()["RH_PROVED"], "NO")


class TestFiniteNotInfinite(unittest.TestCase):
    def test_fso01_finite_prefix_sharp_bound(self):
        # the finite certificate proves the sharp pairwise bound, not an infinite
        # Hilbert statement; the infinite theorem is the paper argument.
        cert = fsi.fso01_certificate(5, N=23)
        self.assertEqual(cert.sharp_bound, 4)
        self.assertEqual(cert.max_length_observed, 4)
        self.assertTrue(cert.all_distinct_separated)


if __name__ == "__main__":
    unittest.main()
