"""Independent exact endpoint-null Legendre H1 minimax and Suzuki source gates."""
import unittest
from fractions import Fraction as F
from observational_succ.endpoint_null_suzuki_trials import (
    EndpointNullError,legendre_derivative_pair,
    first_high_same_parity,endpoint_null_minimal_energy,
    endpoint_null_U,endpoint_null_gamma_tail_certificate,
    genuine_endpoint_null_S4_trial,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_derivative,poly_mul,poly_integral,poly_eval,
)


class EndpointNullLemma(unittest.TestCase):
    def test_exact_orthogonal_derivative_pair_formula(self):
        a=F(1,2)
        for k in range(1,9):
            p=poly_derivative(legendre_polynomial(k,a))
            for m in range(1,9):
                q=poly_derivative(legendre_polynomial(m,a))
                self.assertEqual(poly_integral(poly_mul(p,q),-a,a),
                                 legendre_derivative_pair(k,m))

    def test_original_first_high_minimizers_and_endpoint_nullity(self):
        expected={1:(5,56),2:(6,72),3:(5,36),4:(6,44)}
        a=F(1,2)
        for k,(m,d) in expected.items():
            self.assertEqual((first_high_same_parity(k),
                              endpoint_null_minimal_energy(k)["derivative_energy_min"]),(m,d))
            L=legendre_polynomial(k,a)
            H=legendre_polynomial(m,a)
            self.assertEqual(poly_eval(L,a)-poly_eval(H,a),0)
            self.assertEqual(poly_eval(L,-a)-poly_eval(H,-a),0)
            for trial in (m+2,m+4):
                self.assertGreater(2*(trial*(trial+1)-k*(k+1)),d)

    def test_exact_rational_U_and_input_rejection(self):
        self.assertEqual(endpoint_null_U(),(
            (F(1),F(0),F(1),F(0)),
            (F(0),F(1),F(0),F(1))
        ))
        for bad in (True,5,13):
            with self.assertRaises(EndpointNullError):endpoint_null_U(rank=bad)


class OriginalGammaSourceTail(unittest.TestCase):
    def test_true_B3_tail_improvement_is_J_relative(self):
        first=endpoint_null_gamma_tail_certificate(2)
        last=endpoint_null_gamma_tail_certificate(20)
        self.assertFalse(first["all_low_columns_strict_improvement"])
        self.assertTrue(last["all_low_columns_strict_improvement"])
        self.assertTrue(all(c["endpoint_term_exactly_zero"] for c in last["sector_comparison"]))
        self.assertEqual([r["high_mode"] for r in last["sector_comparison"]],[5,6,5,6])
        self.assertFalse(last["RH_proved"])

    def test_original_signed_S4_endpoint_trial_recertifies(self):
        report=genuine_endpoint_null_S4_trial(J_deriv=2,J_galerkin=64)
        self.assertTrue(report["original_source_authentication"])
        self.assertIn(report["first_window_verdict"],("AMBIGUOUS","POSITIVE_CERTIFIED"))
        self.assertFalse(report["RH_proved"])


if __name__=="__main__":unittest.main()
