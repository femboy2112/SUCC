"""Stand-alone exact rational checks for the mathematical quotient-residual theorem.

Not a substitute for the authentic original Suzuki source gate exercised by
parent PR #149 and existing #137/WB4 regression probes.
"""
import unittest
from fractions import Fraction as F
from observational_succ.four_schur_dual_quotient import (
    DualQuotientError,polynomial_moment_gram,
    derivative_moment_projection_gram,quotient_derivative_cap,
    trace_primitive_polynomial_countermodel,
)

class PrimitiveDualTests(unittest.TestCase):
    def test_moment_gram_exact_parity(self):
        G=polynomial_moment_gram()
        self.assertEqual(G[0],(F(1),F(0),F(1,12),F(0)))
        self.assertEqual(G[1][1],F(1,12))
        self.assertEqual(G[3][3],F(1,448))
        self.assertEqual(G[0][3],F(0))

    def test_normalized_constant_moment_projection(self):
        # For h'=1, only zero-th moment of h' is nonzero. Projection energy 1.
        G=derivative_moment_projection_gram([[F(1)],[F(0)],[F(1,12)],[F(0)]])
        self.assertEqual(G,((F(1),),))

    def test_projection_of_t(self):
        # For h'=t: moments (0,1/12,0,1/80), ||h'||²=1/12.
        G=derivative_moment_projection_gram([[0],[F(1,12)],[0],[F(1,80)]])
        self.assertEqual(G,((F(1,12),),))

    def test_orthogonal_derivative_has_zero_projection(self):
        # h'=18P4(2t) is orthogonal to t^0..t^3; derivative energy 36.
        G=derivative_moment_projection_gram([[0],[0],[0],[0]])
        self.assertEqual(G,((F(0),),))

    def test_source_cap_no_moments(self):
        res=quotient_derivative_cap([[F(1,3),0],[0,F(1,5)]])
        self.assertEqual(res['residual_correction_upper'],
                         ((F(121,96),0),(0,F(121,160))))
        self.assertTrue(res['requires_independent_source_authentication'])
        self.assertFalse(res['RH_proved'])

    def test_moment_subtraction_reduces_bound(self):
        # Source budget C=2 on normGram=1, one deriv h'=1 has proj energy 1.
        r=quotient_derivative_cap([[1]],gprime_L1=2,kappa=F(1,2),
               authenticated_derivative_moments=[[1],[0],[F(1,12)],[0]])
        self.assertEqual(r['residual_correction_upper'],((F(6),),))
        self.assertEqual(r['derivative_moment_subtraction'],((F(1),),))

    def test_forged_moments_rejected(self):
        with self.assertRaises(DualQuotientError):
            quotient_derivative_cap([[1]],gprime_L1=1,kappa=1,
                 authenticated_derivative_moments=[[2],[0],[F(1,6)],[0]])

    def test_not_psd_gram_rejected(self):
        for M in ([[1,2],[2,1]], [[-1]], [[0,1],[1,0]]):
            with self.assertRaises(DualQuotientError):quotient_derivative_cap(M)

    def test_bool_float_wrong_domains(self):
        for M in ([[True]], [[1.]], [[1]],):
            if M==[[1]]: continue
            with self.assertRaises(DualQuotientError):quotient_derivative_cap(M)
        with self.assertRaises(DualQuotientError):polynomial_moment_gram(F(0))
        with self.assertRaises(DualQuotientError):polynomial_moment_gram(degree=-1)

    def test_exact_countermodel(self):
        c=trace_primitive_polynomial_countermodel()
        self.assertEqual(c['projected_derivative_energy']/c['full_derivative_energy'],F(5,3))
        self.assertEqual(c['high_K_dual_energy'],F(36))
        self.assertTrue(c['projection_derivative_contraction_refuted'])

    def test_cross_column_moment_gram(self):
        # h1'=1 and h2'=t; projections orthogonal with energies 1 and 1/12.
        M=[[1,0],[0,F(1,12)],[F(1,12),0],[0,F(1,80)]]
        r=derivative_moment_projection_gram(M)
        self.assertEqual(r,((1,0),(0,F(1,12))))

if __name__=='__main__':unittest.main()
