"""Exact tests for the general-radix polyphase carry-safe algebra (CSA-01..04)."""
import unittest
from fractions import Fraction as Q
from math import gcd

from observational_succ import carry_safe_polyphase as csp
from observational_succ.reciprocal_succ_fucc import (
    residue_clock,
    from_residue_clock,
    direct_mixed_radix_change,
    ReciprocalSourceError,
)


class TestCSA01Coordinates(unittest.TestCase):
    def test_roundtrip_bijection(self):
        for q in range(2, 8):
            seen = set()
            for n in range(1, 60):
                m, r = csp.polyphase_coords(n, q)
                self.assertGreaterEqual(m, 1)
                self.assertTrue(0 <= r < q)
                self.assertEqual(csp.from_polyphase_coords(m, r, q), n)
                self.assertNotIn((m, r), seen)
                seen.add((m, r))

    def test_agrees_with_prime_residue_clock(self):
        # Consistency check (same closed form as reciprocal_succ_fucc.residue_clock),
        # NOT an independent oracle; the independent route is the explicit numpy
        # divmod/permutation-matrix verification in the Daniel instrument pass.
        for p in (2, 3, 5, 7):
            for n in range(1, 50):
                self.assertEqual(csp.polyphase_coords(n, p), residue_clock(n, p))
                m, r = csp.polyphase_coords(n, p)
                self.assertEqual(csp.from_polyphase_coords(m, r, p),
                                 from_residue_clock(m, r, p))

    def test_carry_successor_incl_origin_and_wrap(self):
        # origin (n=1) and the first wrap (n=q) are explicitly exercised
        for q in range(2, 9):
            for n in range(1, 80):
                self.assertTrue(csp.carry_successor_holds(n, q))
            # first wrap: coords(q) = (1, q-1) -> coords(q+1) = (2, 0)
            self.assertEqual(csp.polyphase_coords(q, q), (1, q - 1))
            self.assertEqual(csp.polyphase_coords(q + 1, q), (2, 0))

    def test_tensor_unitary_clean_and_defective(self):
        # clean prefix N = q*M : W_q is onto, no unhit tensor slots
        w = csp.tensor_unitary(12, 3)
        self.assertTrue(w.onto)
        self.assertEqual(w.unhit, ())
        self.assertEqual(w.blocks, 4)
        # partial last block : isometry with a horizon defect
        w2 = csp.tensor_unitary(11, 3)   # M = 4, q*M = 12 > 11
        self.assertFalse(w2.onto)
        self.assertEqual(w2.blocks, 4)
        self.assertEqual(w2.unhit, ((4, 2),))  # the single missing slot -> n=12


class TestCSA02Cuntz(unittest.TestCase):
    def test_isometry_and_orthogonality_exact(self):
        for q in range(2, 7):
            rep = csp.cuntz_relations(q, source_dim=10)
            self.assertTrue(rep.isometry_exact)

    def test_completeness_clean_when_target_is_q_times_source(self):
        for q in range(2, 7):
            rep = csp.cuntz_relations(q, source_dim=8)  # target_dim defaults to q*8
            self.assertTrue(rep.clean)
            self.assertEqual(rep.defect_rank, 0)
            self.assertEqual(rep.defect_support, ())

    def test_finite_horizon_defect_is_exact_tail_projection(self):
        q, D = 3, 5          # clean completeness would need target 15
        rep = csp.cuntz_relations(q, source_dim=D, target_dim=20)
        self.assertFalse(rep.clean)
        self.assertEqual(rep.defect_rank, 20 - q * D)          # 5
        self.assertEqual(rep.defect_support, tuple(range(16, 21)))

    def test_target_prefix_too_small_rejected(self):
        with self.assertRaises(csp.PolyphaseError):
            csp.cuntz_relations(3, source_dim=5, target_dim=10)  # < 15

    def test_u_image_matches_isometry_action(self):
        iso = csp.residue_isometry(4, 2, source_dim=6)
        for n in range(1, 7):
            self.assertEqual(iso.apply(n), csp.u_image(n, 4, 2))


class TestCSA03PrimeEmbedding(unittest.TestCase):
    def test_embedding_and_braid(self):
        for p in (2, 3, 5, 7, 11):
            checks = csp.prime_fucc_embedding(p, dim=30)
            self.assertTrue(all(checks.values()))

    def test_terminal_residue_is_essential(self):
        # V_p uses residue p-1, not 0: u_image(n,p,0) = p(n-1)+1 != p*n for n>1
        for p in (2, 3, 5):
            self.assertEqual(csp.u_image(1, p, p - 1), p)      # |1> -> |p>
            self.assertEqual(csp.u_image(2, p, p - 1), 2 * p)  # |2> -> |2p>
            self.assertNotEqual(csp.u_image(2, p, 0), 2 * p)   # residue 0 is wrong

    def test_composite_label_rejected(self):
        for composite in (4, 6, 9, 15):
            with self.assertRaises(ReciprocalSourceError):
                csp.prime_fucc_embedding(composite, dim=5)


class TestCSA04MixedRadix(unittest.TestCase):
    def test_two_factor_closed_form(self):
        for p in range(2, 6):
            for q in range(2, 6):
                for r in range(p):
                    for s in range(q):
                        Qtot, R = csp.two_factor_compose(p, r, q, s)
                        self.assertEqual((Qtot, R), (p * q, p * s + r))
                        # literal basis action agrees
                        self.assertTrue(csp.closed_form_matches([(p, r), (q, s)], dim=8))

    def test_reversed_order_differs_in_general(self):
        # U_{p,r}U_{q,s} = U_{pq, ps+r} ;  U_{q,s}U_{p,r} = U_{qp, qr+s}
        p, r, q, s = 2, 1, 3, 2
        self.assertEqual(csp.two_factor_compose(p, r, q, s), (6, 2 * 2 + 1))   # (6,5)
        self.assertEqual(csp.reversed_two_factor(p, r, q, s), (6, 3 * 1 + 2))  # (6,5)
        # pick a case where they genuinely differ
        p, r, q, s = 2, 1, 3, 1
        self.assertNotEqual(csp.two_factor_compose(p, r, q, s)[1],
                            csp.reversed_two_factor(p, r, q, s)[1])

    def test_n_factor_associativity_and_closed_form(self):
        factors = [(2, 1), (3, 2), (5, 4), (2, 0)]
        Qtot, R = csp.mixed_radix_compose(factors)
        self.assertEqual(Qtot, 2 * 3 * 5 * 2)
        # little-endian: R = 1 + 2*2 + 4*6 + 0*30 = 1 + 4 + 24 = 29
        self.assertEqual(R, 1 + 2 * 2 + 4 * (2 * 3) + 0 * (2 * 3 * 5))
        self.assertTrue(csp.closed_form_matches(factors, dim=12))
        # associativity: fold pairwise vs all-at-once
        left = csp.two_factor_compose(*factors[0], *factors[1])  # (6, R01)
        # compose (6,R01) with (5,4): U_{6,R01}U_{5,4} = U_{30, 6*4 + R01}
        q01, r01 = left
        step2 = (q01 * 5, q01 * 4 + r01)
        q012, r012 = step2
        step3 = (q012 * 2, q012 * 0 + r012)
        self.assertEqual(step3, (Qtot, R))

    def test_digit_convention_bijections(self):
        for p in range(2, 6):
            for q in range(2, 6):
                perm = csp.digit_convention_permutation(p, q)
                self.assertEqual(len(perm), p * q)
                self.assertEqual({v[0] for v in perm.values()}, set(range(p * q)))
                self.assertEqual({v[1] for v in perm.values()}, set(range(p * q)))

    def test_prime_pair_cross_check_reciprocal_module(self):
        # reciprocal_succ_fucc.direct_mixed_radix_change(s, r, p, q) maps the
        # base-p residue r and base-q "digit" s to (R//q, R%q) with R = p*s + r.
        for p in (2, 3, 5):
            for q in (2, 3, 5):
                for s in range(q):
                    for r in range(p):
                        R = p * s + r
                        self.assertEqual(direct_mixed_radix_change(s, r, p, q),
                                         (R // q, R % q))
                        self.assertEqual(csp.two_factor_compose(p, r, q, s)[1], R)

    def test_crt_distinction(self):
        coprime, _ = csp.is_crt_decomposition(2, 3)
        self.assertTrue(coprime)
        noncoprime, _ = csp.is_crt_decomposition(2, 2)
        self.assertFalse(noncoprime)
        self.assertEqual(gcd(2, 2), 2)       # receipt: 2,2 share a factor
        # base-4 digit of U_{2,r}U_{2,s} = U_{4, 2s+r} is a genuine base change,
        # not a CRT split (which would require coprime moduli)
        self.assertEqual(csp.two_factor_compose(2, 1, 2, 1), (4, 3))


if __name__ == "__main__":
    unittest.main()
