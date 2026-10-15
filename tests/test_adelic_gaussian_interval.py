"""Rigorous rational interval falsification, distinct from analytic proof."""
import unittest
from fractions import Fraction as F

from observational_succ.adelic_gaussian_interval import (
    certified_gaussian_poisson_probe, wrong_haar_amplitude_witness
)
from observational_succ.adelic_poisson_reconstruction import AdelicPoissonError


class RigorousAdelicGaussianTests(unittest.TestCase):
    def test_standard_and_shifted_gaussian_rational_outward_bounds(self):
        for D,t,N in (
            (F(1),F(1),5),
            (F(2),F(1),3),
            (F(1),F(4,9),4),
            (F(1,2),F(4),5),
            (F(3,2),F(1),3),
        ):
            for shift in (False,True):
                r=certified_gaussian_poisson_probe(D,t,shift,N)
                A,B=r["primal_global_enclosure"],r["dual_global_enclosure"]
                self.assertTrue(r["rigorous_intervals_overlap"])
                self.assertGreaterEqual(A[1],B[0])
                self.assertGreaterEqual(B[1],A[0])
                self.assertGreater(r["primal_tail_bound"],0)
                self.assertGreater(r["dual_tail_bound"],0)
                self.assertFalse(r["infinite_identity_proved_by_finite_intervals"])
                self.assertFalse(r["RH_proved"])

    def test_computably_negative_Haar_mutation_is_refuted_by_bounds(self):
        r=wrong_haar_amplitude_witness()
        self.assertTrue(r["mutant_wrong_Haar_refuted_with_rational_bounds"])
        self.assertTrue(r["no_float_sign_assumptions"])
        good=r["correct_primal_global_enclosure"]
        wrong=r["wrong_mutated_dual_global_enclosure"]
        self.assertTrue(wrong[0]>good[1] or wrong[1]<good[0])
        self.assertFalse(r["RH_proved"])

    def test_mutated_source_or_uncontrolled_precision_not_falsely_certified(self):
        bad_args=(
            (F(0),F(1),False,3),
            (F(1),F(0),False,3),
            (F(1),F(2),False,3),  # non-rational sqrt(2), not current certificate
            (F(1),F(1),0,3),
            (F(1),F(1),False,1),
            (F(2),F(1),False,6),  # exponent pi*144 outside proven exp range
        )
        for args in bad_args:
            with self.subTest(args=args),self.assertRaises(AdelicPoissonError):
                certified_gaussian_poisson_probe(*args)

if __name__=="__main__":
    unittest.main()
