"""Finitary toy tests only; none is a 4D Yang--Mills mass-gap theorem."""
import unittest
from fractions import Fraction as Q

from observational_succ.ym_mass_gap_certificate import (
    GapCertificateError, exact_psd, gram_gap_at_one_time,
    entrywise_error_gap, spectral_gram, two_block_gap,
    weighted_block_gap, two_state_ratio, GaussianQ, exact_hermitian_psd,
    coherent_spectral_gram, hermitian_gap_at_one_time,
    coherent_entrywise_error_gap,
)


class MassGapCertificateTests(unittest.TestCase):

    def test_psd_singular_and_negative(self):
        self.assertTrue(exact_psd(((Q(1), Q(1)), (Q(1), Q(1)))))
        self.assertFalse(exact_psd(((Q(1), Q(2)), (Q(2), Q(1)))))
        self.assertTrue(exact_psd(((Q(0), Q(0)), (Q(0), Q(0)))))

    def test_all_principal_minors_not_only_leading(self):
        self.assertFalse(exact_psd(((Q(0), Q(0)), (Q(0), Q(-1)))))

    def test_nonsymmetric_rejected(self):
        with self.assertRaises(GapCertificateError):
            exact_psd(((Q(1), Q(1)), (Q(0), Q(1))))

    def test_non_rational_rejected(self):
        with self.assertRaises(GapCertificateError):
            exact_psd(((1,),))

    def test_gapped_toy_universal_physical_time_q(self):
        for n in range(2, 129):
            spectrum = (Q(1), two_state_ratio(n, "gapped"))
            bank = ((Q(0), Q(1)),)
            self.assertTrue(gram_gap_at_one_time(
                spectral_gram(spectrum, bank, 0),
                spectral_gram(spectrum, bank, n), Q(2, 3)), n)

    def test_gapless_toy_fails_fixed_q_near_continuum(self):
        n = 128
        spectrum = (Q(1), two_state_ratio(n, "gapless"))
        bank = ((Q(0), Q(1)),)
        self.assertFalse(gram_gap_at_one_time(
            spectral_gram(spectrum, bank, 0),
            spectral_gram(spectrum, bank, n), Q(2, 3)))
        self.assertGreater(spectrum[1] ** n, Q(9, 10))

    def test_gapped_calibration_all_rational(self):
        for n in (2, 3, 11, 97, 1001):
            x = Q(1, 4*n)
            r = two_state_ratio(n, "gapped")
            self.assertLessEqual(r, 1/(1+2*x))
            self.assertLessEqual(r ** n, Q(2, 3))

    def test_gapless_bernoulli_bound(self):
        for n in (5, 8, 32, 128):
            r = two_state_ratio(n, "gapless")
            self.assertGreaterEqual(r ** n, 1-Q(2*n, n*n+1))

    def test_incomplete_bank_hides_slow_mode(self):
        n = 32
        spectrum = (Q(1), 1-Q(1, n*n), 1-Q(1, n))
        coarse = ((Q(0), Q(0), Q(1)),)
        complete = (coarse[0], (Q(0), Q(1), Q(0)))
        self.assertTrue(gram_gap_at_one_time(
            spectral_gram(spectrum, coarse, 0),
            spectral_gram(spectrum, coarse, n), Q(1, 2)))
        self.assertFalse(gram_gap_at_one_time(
            spectral_gram(spectrum, complete, 0),
            spectral_gram(spectrum, complete, n), Q(1, 2)))

    def test_mixed_bank_basis_invariance(self):
        spectrum = (Q(1), Q(1,4), Q(2,5))
        bank = ((Q(0), Q(1), Q(1)), (Q(0), Q(1), Q(-1)))
        self.assertTrue(gram_gap_at_one_time(
            spectral_gram(spectrum, bank, 0),
            spectral_gram(spectrum, bank, 1), Q(1, 2)))

    def test_dependent_bank_and_null_vectors(self):
        spectrum = (Q(1), Q(1,4))
        bank = ((Q(0), Q(1)), (Q(0), Q(1)), (Q(1), Q(0)))
        self.assertTrue(gram_gap_at_one_time(
            spectral_gram(spectrum, bank, 0),
            spectral_gram(spectrum, bank, 1), Q(1, 2)))

    def test_negative_transfer_and_wrong_vacuum_forbidden(self):
        with self.assertRaises(GapCertificateError):
            spectral_gram((Q(1), Q(-1,2)), ((Q(0), Q(1)),), 1)
        with self.assertRaises(GapCertificateError):
            spectral_gram((Q(1,2), Q(1,4)), ((Q(0), Q(1)),), 1)

    def test_source_error_budget_passes_and_fails(self):
        g0, gt = ((Q(1),),), ((Q(1,2),),)
        self.assertTrue(entrywise_error_gap(g0, gt, Q(3,4), Q(0), Q(1,10)))
        self.assertFalse(entrywise_error_gap(g0, gt, Q(3,4), Q(0), Q(3,10)))

    def test_error_margin_scales_with_bank_size(self):
        eye = ((Q(1), Q(0)), (Q(0), Q(1)))
        small = ((Q(1,2), Q(0)), (Q(0), Q(1,2)))
        self.assertTrue(entrywise_error_gap(eye, small, Q(3,4), Q(0), Q(1,10)))
        self.assertFalse(entrywise_error_gap(eye, small, Q(3,4), Q(0), Q(1,5)))

    def test_block_margin_rational(self):
        self.assertTrue(two_block_gap(Q(2,5), Q(3,5), Q(1,10)))
        self.assertTrue(weighted_block_gap(
            Q(2,5), Q(3,5), Q(1,10), Q(1), Q(1), Q(7,10)))
        self.assertFalse(weighted_block_gap(
            Q(2,5), Q(3,5), Q(1,10), Q(1), Q(1), Q(2,3)))

    def test_detail_coherence_closes_gap(self):
        self.assertFalse(two_block_gap(Q(3,5), Q(3,5), Q(2,5)))
        self.assertFalse(gram_gap_at_one_time(
            ((Q(1), Q(0)), (Q(0), Q(1))),
            ((Q(3,5), Q(2,5)), (Q(2,5), Q(3,5))), Q(9,10)))

    def test_qi_hermitian_phase_and_mutation(self):
        z = GaussianQ(Q(0), Q(1))
        self.assertTrue(exact_hermitian_psd(((Q(1), z), (-z, Q(1)))))
        self.assertFalse(exact_hermitian_psd(((Q(1), z*Q(2)), (-z*Q(2), Q(1)))))
        with self.assertRaises(GapCertificateError):
            exact_hermitian_psd(((Q(1), z), (z, Q(1))))

    def test_qi_coherent_observer_bank(self):
        z = GaussianQ(Q(0), Q(1))
        bank = ((Q(0), Q(1), Q(1)), (Q(0), Q(1), z))
        spectrum = (Q(1), Q(1,4), Q(2,5))
        g0, g1 = coherent_spectral_gram(spectrum, bank, 0), coherent_spectral_gram(spectrum, bank, 1)
        self.assertEqual(g1[0][1], GaussianQ(Q(1,4), Q(2,5)))
        self.assertEqual(g1[1][0], g1[0][1].conjugate())
        self.assertTrue(hermitian_gap_at_one_time(g0, g1, Q(1,2)))
        self.assertFalse(hermitian_gap_at_one_time(g0, g1, Q(1,3)))

    def test_qi_arithmetic_and_dependent_channels(self):
        z = GaussianQ(Q(1,2), Q(2,3))
        self.assertEqual(z/z, GaussianQ(Q(1)))
        bank = ((Q(0), z), (Q(0), z*Q(2)))
        spectrum = (Q(1), Q(1,4))
        self.assertTrue(hermitian_gap_at_one_time(
            coherent_spectral_gram(spectrum, bank, 0),
            coherent_spectral_gram(spectrum, bank, 1), Q(1,2)))

    def test_qi_source_error_margin(self):
        z = GaussianQ(Q(0), Q(1,10))
        a = ((Q(1), z), (-z, Q(1)))
        b = ((Q(1,3), z*Q(1,3)), (-z*Q(1,3), Q(1,3)))
        self.assertTrue(coherent_entrywise_error_gap(a, b, Q(2,3), Q(0), Q(1,20)))
        self.assertFalse(coherent_entrywise_error_gap(a, b, Q(2,3), Q(0), Q(1,5)))

    def test_invalid_q_and_errors_rejected(self):
        with self.assertRaises(GapCertificateError):
            gram_gap_at_one_time(((Q(1),),), ((Q(1,2),),), Q(1))
        with self.assertRaises(GapCertificateError):
            entrywise_error_gap(((Q(1),),), ((Q(1,2),),), Q(3,4), Q(-1), Q(0))


    def test_unique_vacuum_gapless_coherence_cutoffs(self):
        # On the direct-sum excitation bank, each finite block has q_N<1
        # but q_N -> 1, while every diagonal coarse/detail bound is 3/5.
        for n in (2, 4, 8, 32, 128):
            cross = Q(2, 5)*(1-Q(1, n))
            t = ((Q(3, 5), cross), (cross, Q(3, 5)))
            eye = ((Q(1), Q(0)), (Q(0), Q(1)))
            q_n = 1-Q(2, 5*n)
            self.assertTrue(two_block_gap(Q(3, 5), Q(3, 5), cross))
            self.assertTrue(gram_gap_at_one_time(eye, t, q_n))
            self.assertFalse(gram_gap_at_one_time(eye, t, Q(3, 4)))
            self.assertEqual(Q(3, 5)+cross, q_n)


if __name__ == "__main__":
    unittest.main()
