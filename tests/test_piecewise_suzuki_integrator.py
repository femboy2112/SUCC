"""Hostile source-replay tests for spatial-grid-free Suzuki first-prime integrator."""
import unittest
from fractions import Fraction as F

from observational_succ.piecewise_suzuki_integrator import (
    I,ExponentialPolynomial,authentic_mode_piecewise,genuine_piecewise_gram
)
from observational_succ.analytic_suzuki_schur_gate import CertifiedAnalyticSuzukiTrial
from observational_succ.certified_four_schur_trial import (
    authentic_suzuki_mode_derivative_point
)
from observational_succ.suzuki_legendre_source import tight_exp_neg


class RationalExpPolyAlgebra(unittest.TestCase):
    def test_exact_polynomial_exponential_antiderivatives(self):
        e=ExponentialPolynomial(((F(1),((I.of(1)),)),))
        r=e.integrate(0,F(1,2),digits=90)
        lo,hi=tight_exp_neg(F(1,2),90)
        expected=I(F(1,hi)-1,F(1,lo)-1)
        self.assertTrue(r.intersects(expected))
        self.assertLess(r.rad(),F(1,10**65))

    def test_rational_polynomial_exact_integration(self):
        p=ExponentialPolynomial.polynomial((1,2,3))
        ans=p.integrate(F(-1,2),F(1,2))
        self.assertEqual(ans,I.of(F(5,4)))

    def test_malformed_interval_and_source_parameters_fail(self):
        with self.assertRaises(ValueError): I(F(2),F(1))
        with self.assertRaises(ValueError): I.of(1.5)
        with self.assertRaises(ValueError): authentic_mode_piecewise(1,0)
        with self.assertRaises(ValueError): authentic_mode_piecewise(1,21)
        with self.assertRaises(ValueError): genuine_piecewise_gram(1,rank=9)


class AuthenticSourceAnalyticVerification(unittest.TestCase):
    def test_genuine_prime2_activation_and_source_point_cross_oracle(self):
        for k in (1,2,3,4):
            center,activated,b=authentic_mode_piecewise(k,2,digits=100)
            cut=b-F(1,2)
            self.assertLess(cut.hi,F(1,4))
            self.assertGreater(cut.lo,F(1,8))
            for x in (F(1,8),F(1,4),F(2,5)):
                expected=authentic_suzuki_mode_derivative_point(k,x,2)
                result=(center if x<cut.lo else activated).value(x,digits=100)
                self.assertTrue(result.intersects(I(expected.lo,expected.hi)),
                                f"mode {k} at {x} disagrees with independent point oracle")
            if k in (1,2):
                # The genuine wavefront makes an observable nonzero difference.
                self.assertFalse(center.value(F(2,5)).intersects(
                    activated.value(F(2,5))))

    def test_finite_gram_is_exactly_reflection_parity_split(self):
        source=genuine_piecewise_gram(J=2,rank=4,digits=100)
        H=source["Hprime"];M=source["quotient_gram"]
        self.assertTrue(source["source_authenticated"])
        self.assertFalse(source["spatial_quadrature_used"])
        for i in range(4):
            self.assertGreater(H[i][i].lo,0)
            for j in range(4):
                if (i-j)%2:self.assertEqual(M[i][j],I.of(0))
                self.assertTrue(M[i][j].intersects(H[i][j]-source["polynomial_projection_gram"][i][j]))
        self.assertLess(max(M[i][i].rad() for i in range(4)),F(1,10**17))

    def test_actual_finite_to_infinite_first_window_gate(self):
        result=CertifiedAnalyticSuzukiTrial(J_deriv=2,J_galerkin=64,
                                             rank=5,digits=100)
        self.assertTrue(result["source_passport_verified"])
        self.assertTrue(result["no_spatial_quadrature"])
        self.assertFalse(result["RH_proved"])
        self.assertIn(result["verdict"],("AMBIGUOUS","POSITIVE_CERTIFIED"))
        self.assertEqual(len(result["true_S4_Loewner_lower"]),4)

    def test_invalid_eta_refuses_claim(self):
        self.assertEqual(CertifiedAnalyticSuzukiTrial(young_eta=0)["verdict"],
                         "INVALID_SOURCE")


if __name__=="__main__":unittest.main()
