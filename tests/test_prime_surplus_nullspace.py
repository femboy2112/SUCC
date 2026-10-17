"""Finite exact phase-coherent prime2 high-null counterexamples."""
import unittest
from fractions import Fraction as F
from observational_succ.prime_surplus_nullspace import (
    PrimeKernelError,exact_finite_four_moment_edge_kernel,
    source_prime_kernel_no_uniform_gap,
)


class PhaseCoherenceNullspaceTests(unittest.TestCase):
    def test_four_moments_with_true_source_edge_shape_cannot_force_mismatch(self):
        for b in (F(2,3),F(7,10),F(3,4)):
            for n in (5,6,9):
                witness=exact_finite_four_moment_edge_kernel(b=b,cells=n)
                self.assertEqual(witness["four_exact_moments"],(0,0,0,0))
                self.assertGreater(witness["whole_primitive_norm2"],0)
                self.assertEqual(witness["prime_edge_surplus"],0)
                self.assertEqual(witness["right_amplitudes"],
                                 witness["left_amplitudes"])
                self.assertFalse(witness["full_high_uniform_scalar_gain"])
                self.assertFalse(witness["RH_proved"])

    def test_wrong_grammar_and_insufficient_degrees_of_freedom_rejected(self):
        with self.assertRaises(PrimeKernelError):
            exact_finite_four_moment_edge_kernel(cells=4)
        with self.assertRaises(PrimeKernelError):
            exact_finite_four_moment_edge_kernel(cells=True)
        with self.assertRaises(Exception):
            exact_finite_four_moment_edge_kernel(b=F(1,3))
        with self.assertRaises(Exception):
            exact_finite_four_moment_edge_kernel(b=F(1))

    def test_genuine_original_source_kernel_theorem_fires_only_with_real_log2(self):
        result=source_prime_kernel_no_uniform_gap()
        self.assertEqual(result["source_sha"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertTrue(result["infinite_dimensional_nullspace"])
        self.assertFalse(result["source_prime_surplus_uniform_positive_scalar"])
        self.assertTrue(result["nonzero_smooth_moment_null_shift_coherent_source_test_exists"])
        self.assertFalse(result["RH_proved"])


if __name__=="__main__":
    unittest.main()
