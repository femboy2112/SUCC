"""Rational winding, bounded contour source transport and adversarial controls."""
import unittest
from fractions import Fraction as Q
from observational_succ import certified_contour_observer as c

class ExactContourTests(unittest.TestCase):
    def test_constant_winding(self):
        cert=c.certified_contour((c.point(2),),c.square(1),2,Q(1,2))
        self.assertEqual(cert.count,0)
        self.assertGreater(cert.lower_clearance,0)
        self.assertEqual(cert.sample_count,4)
        self.assertEqual(cert.source_status,'CONDITIONAL_SUPPLIED_ERROR')

    def test_one_root(self):
        self.assertEqual(
            c.certified_contour((c.point(-1,-1),c.point(1)),c.square(2),3).count,1)

    def test_two_real_roots(self):
        self.assertEqual(
            c.certified_contour((c.point(1),c.point(0),c.point(-1)),c.square(2),3).count,2)

    def test_two_imaginary_roots(self):
        self.assertEqual(
            c.certified_contour((c.point(1),c.point(0),c.point(1)),c.square(2),3).count,2)

    def test_double_zero(self):
        self.assertEqual(
            c.certified_contour((c.point(0),c.point(0),c.point(1)),c.square(2),3).count,2)

    def test_reversed_winding_fails(self):
        with self.assertRaises(c.ContourError):
            c.certified_contour((c.point(0),c.point(1)),tuple(reversed(c.square(1))),2)

    def test_unknown_uniform_error_rejected(self):
        with self.assertRaises(c.ContourError):
            c.certified_contour((c.point(1),),c.square(1),2,2,max_depth=7)

    def test_contour_boundary_root_fails(self):
        with self.assertRaises(c.ContourError):
            c.certified_contour((c.point(-1),c.point(1)),c.square(1),2,max_depth=10)

    def test_domain_and_float_mutants(self):
        for fn in (
          lambda:c.certified_contour((c.point(1),),c.square(2),2),
          lambda:c.certified_contour((c.point(1),),c.square(1),2,error=0.01),
          lambda:c.certified_contour(((1.0,0),),c.square(1),2),
          lambda:c.certified_contour((c.point(1),),c.square(1),2,max_depth=100)
        ):
          with self.assertRaises(c.ContourError):fn()

    def test_translation_winding(self):
        self.assertEqual(
            c.certified_contour((c.point(1),c.point(1)),c.square(2),3).count,1)

    def test_polynomial_orders_independently(self):
        for m in range(1,5):
            P=tuple(c.point(0) for _ in range(m))+(c.point(1),)
            self.assertEqual(c.certified_contour(P,c.square(1),2,max_depth=18).count,m)

    def test_genuine_theta_source_replay_and_contour(self):
        from observational_succ.theta_taylor_jets import jets, JetError
        source=jets(degree=20,modes=3,T=8,cells=1536)
        result=c.authentic_theta_square(source,Q(3),Q(11,2),13)
        self.assertEqual(result.count,0)
        self.assertGreater(result.lower_clearance,0)
        self.assertEqual(result.source_status,'AUTHENTIC_REPLAYED_INTEGER_THETA')
        self.assertFalse(result.is_zero_lookup)
        self.assertFalse(result.is_weil_positivity)
        forged=dict(source)
        forged['a']=tuple(source['a'][1:])+tuple(source['a'][:1])
        with self.assertRaises(JetError):
            c.authentic_theta_square(forged,Q(3),Q(11,2),13)

if __name__=='__main__':
    unittest.main()
