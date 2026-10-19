"""Independent exact inverse of the true source two-edge flip comparator."""
import unittest
from fractions import Fraction as F

from observational_succ.prime_surplus_dual import (
    PrimeDualError, exact_primitive_edge_dual,source_dual_coefficients,
    rational_polynomial_dual_center_witness,exact_constrained_dual,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_primitive_zero_at_left,
)
from observational_succ.authentic_prime_surplus import (
    poly_int,poly_mul,edge_energy_polynomial,
)


class ExactSourceDualAlgebra(unittest.TestCase):
    def test_direct_block_inverse_equals_source_saving(self):
        report=exact_primitive_edge_dual(
            (F(1),F(-2)),(F(3),F(1)),(F(4),F(-1)),
            kappa=F(63,500),w=F(12,25))
        self.assertGreater(report["center_saving"],0)
        self.assertGreater(report["edge_phase_saving"],0)
        self.assertGreater(report["total_strict_saving"],0)
        self.assertLess(report["strict_source_prime_dual_upper"],
                        report["scalar_only_dual"])
        self.assertFalse(report["actual_source_residual_recognized"])

    def test_null_kernel_is_symmetric_edge_with_empty_center(self):
        result=exact_primitive_edge_dual((1,2),(1,2),(0,),
                                         kappa=F(63,500),w=F(12,25))
        self.assertEqual(result["total_strict_saving"],0)
        self.assertEqual(result["strict_source_prime_dual_upper"],
                         result["scalar_only_dual"])

    def test_center_only_saves_exact_source_non_scalar_inverse(self):
        k=F(63,500);w=F(12,25)
        result=exact_primitive_edge_dual((0,),(0,),(1,),kappa=k,w=w)
        self.assertEqual(result["strict_source_prime_dual_upper"],1/(k+w))
        self.assertEqual(result["scalar_only_dual"],1/k)

    def test_negative_and_wrong_source_inputs_fail(self):
        for k,w in ((0,1),(-1,1),(1,0),(1,-2),(True,1),(F(1,2),0.1)):
            with self.assertRaises(PrimeDualError):
                exact_primitive_edge_dual((1,),(2,),(3,),kappa=k,w=w)
        with self.assertRaises(PrimeDualError):
            exact_primitive_edge_dual((1,2),(2,),(1,),kappa=1,w=1)


class ActualSourceResidualInstrument(unittest.TestCase):
    def test_original_source_dual_coefficients_not_generic_trace(self):
        for sector,k in (("odd",F(63,500)),("even",F(153,500))):
            r=source_dual_coefficients(sector)
            w=F(12,25)
            self.assertEqual(r["kappa"],k)
            self.assertEqual(r["w2_lower"],w)
            self.assertEqual(r["C_center"],w/(k*(k+w)))
            self.assertEqual(r["C_phase_mismatch"],w/(k*(k+2*w)))
            self.assertGreater(r["C_center"],r["C_phase_mismatch"])
            self.assertEqual(r["source_sha"],
                             "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        with self.assertRaises(PrimeDualError):
            source_dual_coefficients("fake-prime6")

    def test_true_source_center_probe_gives_strict_dual_saving_on_high_shape(self):
        for n,sector in ((5,"odd"),(6,"even")):
            f=poly_primitive_zero_at_left(legendre_polynomial(n,F(1,2)),F(1,2))
            proof=rational_polynomial_dual_center_witness(f,parity=sector)
            self.assertGreater(proof["center_norm2_exact"],0)
            self.assertGreater(proof["source_arithmetic_dual_saving_lower"],0)
            self.assertLess(proof["new_dual_upper"],proof["old_dual_upper"])
            self.assertFalse(proof["actual_original_G_residual_identified"])
        with self.assertRaises(PrimeDualError):
            rational_polynomial_dual_center_witness((1,2),parity="odd")


class ExactRestrictedVariationalDual(unittest.TestCase):
    def test_polynomial_constraint_reduces_uncertainty(self):
        B=((F(2),F(-1),F(0)),
           (F(-1),F(2),F(0)),
           (F(0),F(0),F(1)))
        g=(F(1),F(0),F(2))
        result=exact_constrained_dual(B,g,((F(1),F(1),F(0)),))
        self.assertGreater(result["unrestricted_inverse_energy"],
                           result["constrained_inverse_energy"])
        self.assertGreater(result["polynomial_orthogonality_saving"],0)
        self.assertFalse(result["complete_original_Weil_operator"])

    def test_orthogonal_observer_constraint_no_fake_gain(self):
        B=((F(2),F(0)),(F(0),F(3)))
        g=(F(1),F(0))
        result=exact_constrained_dual(B,g,((F(0),F(1)),))
        self.assertEqual(result["polynomial_orthogonality_saving"],0)
        self.assertEqual(result["constrained_inverse_energy"],
                         result["unrestricted_inverse_energy"])

    def test_dependent_and_uncoercive_operators_rejected(self):
        with self.assertRaises(PrimeDualError):
            exact_constrained_dual(((0,1),(1,0)),(1,1),((1,0),))
        with self.assertRaises(PrimeDualError):
            exact_constrained_dual(((1,0),(0,1)),(1,1),((1,0),(2,0)))
        with self.assertRaises(PrimeDualError):
            exact_constrained_dual(((1,0),(0,1)),(1,1),((1,0),(0,1)))


if __name__=="__main__":
    unittest.main()
