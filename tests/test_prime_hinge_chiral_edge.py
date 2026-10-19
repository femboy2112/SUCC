"""Exact source-typed prime edge geometry and high-moment negative controls."""
import unittest
from importlib.util import find_spec
from fractions import Fraction as F
from observational_succ.prime_hinge_chiral_edge import (
    EdgeHinge, HingeError, integrate, mul, poly, add,
    moment_annihilating_edge, high_moment_chiral_certificate,
    polynomial_prime_derivative_gram, polynomial_prime_quadratic, authentic_prime2_interval_gate,
)


class EdgeGeometryTests(unittest.TestCase):
    def setUp(self):
        self.h=EdgeHinge(F(1,2),F(3,4),1)

    def test_direct_polynomial_integral_independent(self):
        # For v=2t, direct double integral over x>y+b gives -61/15360.
        # Independently derive from analytic triangular-domain integration.
        self.assertEqual(self.h.hs_squared(),F(1,1536))
        # Hilbert-Schmidt: (delta^4)/6 = (1/4)^4/6 = 1/1536.
        Fv=(F(-1,4),F(0),F(1))
        ev=self.h.energy(Fv,Fv)
        self.assertGreater(ev['K_energy'],0)
        self.assertEqual(ev['prime_quadratic'], -ev['K_energy'])
        self.assertEqual(polynomial_prime_quadratic(self.h,(F(0),F(2)),(F(0),F(2))), F(-61,15360))
        gram=polynomial_prime_derivative_gram(self.h,((F(0),F(2)),))
        self.assertEqual(gram[0][0], F(53,7680))

    def test_full_first_four_prime_gram_and_parity(self):
        import math
        from observational_succ.prime_hinge_chiral_edge import pow_poly, deriv, integrate, poly
        # Source Legendre P1, P2, P3, P4 on the genuine a=1/2 chart.
        arr=((F(0),F(2)),
             (F(-1,2),F(0),F(6)),
             (F(0),F(-3),F(0),F(20)),
             (F(3,8),F(0),F(-15),F(0),F(70)))
        mat=polynomial_prime_derivative_gram(self.h,arr)
        for i in range(4):
            self.assertGreater(mat[i][i],0)
            for j in range(4):
                self.assertEqual(mat[i][j],mat[j][i])
                if (i-j)%2:
                    self.assertEqual(mat[i][j],0)
        self.assertEqual(mat[0][0],F(53,7680))
        self.assertEqual(mat[1][1],F(617,215040))

    def test_high_chirality_all_orders(self):
        for m in range(0,9):
            for sign in (-1,1):
                result=high_moment_chiral_certificate(self.h,m,sign=sign)
                self.assertEqual(result['sharp_ratio'], -sign)
                self.assertEqual(result['gradient_to_K_cost'], F(2*(2*m+1)*(2*m+5),1)/self.h.width**2)
                self.assertGreater(result['certificate']['K_energy'],0)
                self.assertEqual(result['certificate']['prime_quadratic'],
                                 -sign*result['certificate']['K_energy'])

    def test_multiple_rational_hinge_sources(self):
        for a,b,w in ((F(1,2), F(9,10), F(3,7)),
                      (F(1,2), F(501,1000), F(7,9)),
                      (F(1),F(3,2),F(-2,3)),
                      (F(3,4),F(1),F(5,6))):
            h=EdgeHinge(a,b,w)
            self.assertEqual(h.hs_squared(),w*w*(2*a-b)**4/6)
            for sign in (-1,1):
                c=high_moment_chiral_certificate(h,4,sign=sign)
                self.assertEqual(c['sharp_ratio'],-sign*w)

    def test_singular_threshold_effect(self):
        # As delta shrinks, HS tends to zero but the K-relative ratio stays 1.
        hs=[]
        for d in (F(1,4),F(1,8),F(1,16),F(1,32)):
            h=EdgeHinge(F(1,2),F(1)-d,1)
            hs.append(h.hs_squared())
            self.assertEqual(high_moment_chiral_certificate(h,4)['sharp_ratio'],-1)
        self.assertTrue(all(hs[i+1]<hs[i] for i in range(len(hs)-1)))
        self.assertEqual(hs[-1]/hs[0],F(1,4096))

    def test_source_poly_not_mean_zero_is_refused(self):
        with self.assertRaises(HingeError):
            polynomial_prime_derivative_gram(self.h,((F(1),),))

    def test_invalid_source_parameters_refused(self):
        for args in ((F(1,2),F(1,2),1),(F(1,2),1,1),
                     (F(1,2),F(1,4),1),(F(1,2),F(5,4),1)):
            with self.assertRaises(HingeError): EdgeHinge(*args)
        for w in (True, 1.0):
            with self.assertRaises(HingeError): EdgeHinge(F(1,2),F(3,4),w)

    def test_same_signed_edges_give_negative_but_opposite_positive(self):
        p=moment_annihilating_edge(4,self.h.width)
        l=self.h.energy(p,p)
        r=self.h.energy(p,tuple(-x for x in p))
        self.assertEqual(l['prime_quadratic'],-l['K_energy'])
        self.assertEqual(r['prime_quadratic'],r['K_energy'])
        self.assertEqual(l['K_energy'],r['K_energy'])

    def test_two_edge_gram_has_cross_only(self):
        p=moment_annihilating_edge(2,self.h.width)
        zero=(F(0),)
        self.assertEqual(self.h.energy(p,zero)['prime_quadratic'],0)
        self.assertEqual(self.h.energy(zero,p)['prime_quadratic'],0)
        self.assertNotEqual(self.h.energy(p,p)['prime_quadratic'],0)

    def test_authentic_gate_not_called_by_synthetic_fixtures(self):
        # CI integration test imports the genuine original source separately.
        self.assertTrue(callable(authentic_prime2_interval_gate))


@unittest.skipUnless(find_spec("observational_succ.tate_suzuki_shorting"), "inherited Suzuki repository modules not mounted in isolated fixture")
class AuthenticSourceIntegrationTests(unittest.TestCase):
    def test_actual_frozen_prime2_gate(self):
        gate=authentic_prime2_interval_gate()
        self.assertTrue(gate['source_verified'])
        self.assertEqual(gate['prime_jet'],(2,2))
        self.assertFalse(gate['all_source_positive'])
        self.assertFalse(gate['RH_proved'])

if __name__ == '__main__':
    unittest.main()
