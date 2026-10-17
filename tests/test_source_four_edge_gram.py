"""Genuine first-prime edge mismatch all-four and signed source S4 test suite."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.source_four_edge_gram import (
    authentic_four_edge_moments,phase_edge_energy_for_direction,
    phase_edge_Young_gram_lower,_eta_true_gamma_derivative,
)
from observational_succ.source_four_phase_schur import CertifiedFourPrimeFullPhaseSchurTrial
from observational_succ.source_four_center_gram import SourceCenterError
from observational_succ.direct_quotient_schur import exact_psd
from observational_succ.authentic_prime_surplus import poly_int,poly_mul,poly_add


class TruePrimeEdgePhaseModel(unittest.TestCase):
    def test_parity_and_prime_connected_symmetry_in_polynomial_model(self):
        # Independent polynomial control b=7/10, actual two-edge geometry.
        a=F(1,2);b=F(7,10);lo=b-a;hi=a
        # even g=x^2: mismatch g(x)-g(b-x), odd about b/2.
        even=(F(0),F(0),F(1))
        reflected=(b*b,-2*b,F(1))
        mismatch=poly_add(even,reflected,-1)
        phi=(-b/2,F(1))
        actual=poly_int(poly_mul(phi,mismatch),lo,hi)
        source_half=2*poly_int(poly_mul(phi,even),lo,hi)
        self.assertEqual(actual,source_half)
        self.assertEqual(poly_int(mismatch,lo,hi),F(0))
        # odd g=x: mismatch g(x)+g(b-x)=b, even about b/2.
        odd=(F(0),F(1))
        swapped=(b,-F(1))
        actualodd=poly_int(poly_add(odd,swapped),lo,hi)
        self.assertEqual(actualodd,2*poly_int(odd,lo,hi))
        self.assertEqual(actualodd,b*(2*a-b))

    def test_true_Gamma_derivative_error_bound_monotone(self):
        for k in range(1,5):
            self.assertGreater(_eta_true_gamma_derivative(k,2),
                               _eta_true_gamma_derivative(k,8))
            self.assertGreater(_eta_true_gamma_derivative(k,8),
                               _eta_true_gamma_derivative(k,20))

    def test_original_suzuki_four_edge_interval_source(self):
        c=authentic_four_edge_moments(J=8,J_G=64,digits=100)
        self.assertEqual(c["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(c["source_prime"],(2,2))
        lo,hi=c["edge_width_interval"]
        self.assertTrue(F(0)<lo<hi<F(1,2))
        self.assertTrue(c["original_poles_contact_Gamma_and_true_p2"])
        self.assertEqual(c["relevant_phase_antisymmetric_low_modes"],(1,3))
        self.assertEqual(c["relevant_phase_symmetric_low_modes"],(2,4))
        for i in range(4):
            a,b=c["intervals"][i]
            self.assertLessEqual(c["nominal"][i]-c["errors"][i],a)
            self.assertGreaterEqual(c["nominal"][i]+c["errors"][i],b)

    def test_source_interval_vector_corner_Young_loewner(self):
        c=authentic_four_edge_moments(J=8,J_G=64,digits=100)
        low=phase_edge_Young_gram_lower(c,F(1,8))
        ell=c["edge_width_interval"][1]
        w=(F(12)/ell**3,F(1)/ell)
        for signs in product((-1,1),repeat=4):
            m=tuple(c["nominal"][i]+signs[i]*c["errors"][i] for i in range(4))
            actual=tuple(tuple((w[0] if i%2==0 else w[1])*m[i]*m[j]
                               if (i-j)%2==0 else F(0) for j in range(4))
                         for i in range(4))
            diff=tuple(tuple(actual[i][j]-low[i][j] for j in range(4))
                       for i in range(4))
            self.assertTrue(exact_psd(diff),str(signs))

    def test_all_direction_bounds_for_corner_moments(self):
        c=authentic_four_edge_moments(J=8,J_G=64,digits=100)
        ell=c["edge_width_interval"][1]
        weights=(F(12)/ell**3,F(1)/ell)
        for x in ((1,0,0,0),(0,1,0,0),(1,0,1,0),(1,0,-1,0),
                  (0,1,0,1),(0,1,0,-1),(1,2,3,4)):
            lower=phase_edge_energy_for_direction(c,x)
            for s in product((-1,1),repeat=4):
                v=tuple(c["nominal"][i]+s[i]*c["errors"][i] for i in range(4))
                true=weights[0]*(x[0]*v[0]+x[2]*v[2])**2+\
                     weights[1]*(x[1]*v[1]+x[3]*v[3])**2
                self.assertLessEqual(lower,true)

    def test_invalid_edge_source_grammar(self):
        for bad in (0,21,True,2.0):
            with self.assertRaises(SourceCenterError):
                authentic_four_edge_moments(J=bad)
        for eta in (0,F(-1),F(2),True,0.25):
            with self.assertRaises(SourceCenterError):
                phase_edge_Young_gram_lower({"edge_width_interval":(F(1,4),F(1,3))},eta)


class OriginalSignedS4WithGenuinePrimeEdge(unittest.TestCase):
    def test_complete_source_four_signed_schur_plus_edge_gate(self):
        cert=CertifiedFourPrimeFullPhaseSchurTrial(J_center=64,J_G=64,
                                                    J_deriv=2,J_edge=8,
                                                    eta=F(1,8),digits=100)
        self.assertEqual(cert["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertFalse(cert["RH_proved"])
        self.assertIn(cert["original_S4_verdict"],
                      ("AMBIGUOUS","POSITIVE_CERTIFIED_FIRST_WINDOW"))
        self.assertGreater(cert["full_source_direction_certificates"]["P1"]["arithmetic_center_strict_saving"],0)
        for i in range(4):
            for j in range(4):
                self.assertEqual(cert["original_complete_S4_center_plus_edge_Loewner_lower"][i][j],
                                 cert["original_complete_S4_center_plus_edge_Loewner_lower"][j][i])
                if (i-j)%2:self.assertEqual(cert["edge_source_four_Loewner_improvement_lower"][i][j],0)
        self.assertFalse(cert["source_positive_S4_first_window"] and cert["RH_proved"])


if __name__=="__main__":
    unittest.main()
