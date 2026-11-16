from fractions import Fraction as F
from itertools import product
import unittest

import damped_filters as d


def direct_filter(degree,t,h):
    # Product evaluation is separate from the expanded-polynomial compiler.
    z=t**h
    out=z
    for j in range(1,degree):
        out *= (z-t**j)/(1-t**j)
    return out


class DampedTests(unittest.TestCase):
    def test_product_vs_expansion_and_sign(self):
        for degree in (2,4,6,8):
            for t in (F(1,2),F(1,3),F(2,5)):
                a=d.coefficients(degree,t)
                eps=d.leakage(degree,t)
                self.assertEqual(d.polynomial(a,1),1)
                for h in range(1,81):
                    value=d.polynomial(a,t**h)
                    self.assertEqual(value,direct_filter(degree,t,h))
                    self.assertLessEqual(value,0)
                    self.assertGreaterEqual(value,-eps)
                    if h<degree: self.assertEqual(value,0)
                self.assertEqual(d.polynomial(a,t**degree),-eps)

    def test_uniform_coefficient_budget(self):
        for degree in range(2,30,2):
            a=d.coefficients(degree)
            norm=sum(map(abs,a),F())
            independently=F(1)
            for j in range(1,degree):
                independently *= (1+F(1,2)**j)/(1-F(1,2)**j)
            self.assertEqual(norm,independently)
            self.assertLess(norm,F(527,63))

    def test_two_sided_monotone_ratchet(self):
        for t in (F(1,2),F(1,3)):
            for h in range(31):
                lower=[direct_filter(k,t,h) for k in (2,4,6,8)]
                upper=[direct_filter(k,t,h) for k in (1,3,5,7)]
                target=int(h==0)
                self.assertEqual(lower,sorted(lower))
                self.assertEqual(upper,sorted(upper,reverse=True))
                self.assertLessEqual(lower[-1],target)
                self.assertGreaterEqual(upper[-1],target)

    def test_arbitrary_histograms_and_count_recovery(self):
        for counts in product(range(3),repeat=5):
            for degree in (2,4):
                cert=d.histogram_certificate(counts,degree)
                self.assertLessEqual(F(cert['zero_mass_lower']),counts[0])
                self.assertGreaterEqual(F(cert['zero_mass_upper']),counts[0])
                self.assertLessEqual(cert['integer_lower'],counts[0])
                self.assertGreaterEqual(cert['integer_upper'],counts[0])
                if sum(counts)*d.leakage(degree)<1:
                    self.assertTrue(cert['count_recovered'])

    def test_high_grade_and_no_grade_ceiling(self):
        counts=[0]*1001;counts[0]=2;counts[1000]=99
        cert=d.histogram_certificate(counts,4)
        self.assertTrue(cert['count_recovered'])
        self.assertEqual(cert['integer_lower'],2)

    def test_interval_uncertainty_and_integral_promise(self):
        counts=(2,2,3,0,2)
        cert=d.histogram_certificate(counts,4,error=F(1,100))
        self.assertTrue(cert['count_recovered'])
        self.assertEqual(cert['integer_lower'],2)
        # The displayed intervals, not a solver's guess, carry the authority.
        eps=d.leakage(4)
        self.assertLess(sum(counts)*eps+18*F(1,100),1)
        # Audit regression: real masses cannot silently inherit a count promise.
        with self.assertRaises(ValueError):
            d.histogram_certificate((F(1,2),0,4),2)
        general=(F(1,2),0,4)
        values=[d.response(general,F(1,2)**r) for r in (1,2)]
        real_cert=d.certificate(sum(general),[(v,v) for v in values],2)
        self.assertNotIn('integer_lower',real_cert)
        self.assertGreaterEqual(F(real_cert['zero_mass_upper']),F(1,2))

    def test_odd_degree_cannot_be_lower_filter(self):
        self.assertGreater(direct_filter(3,F(1,2),3),0)
        with self.assertRaises(ValueError): d.coefficients(3)

    def test_t_above_half_invalidates_same_leakage(self):
        t=F(3,4)
        self.assertLess(direct_filter(2,t,3),-t**3)
        with self.assertRaises(ValueError): d.coefficients(2,t)

    def test_fractional_grade_would_forge_positive_ground(self):
        # t=1/4, h=1/2 gives z=1/2 and positive response without grade zero.
        self.assertEqual(d.polynomial(d.coefficients(2,F(1,4)),F(1,2)),F(1,6))

    def test_invalid_domains(self):
        for degree in (0,1,True,2.0):
            with self.assertRaises(ValueError): d.coefficients(degree)
        for t in (F(),F(3,4),0.5,True):
            with self.assertRaises(ValueError): d.coefficients(2,t)
        with self.assertRaises(ValueError): d.certificate(-1,[(0,0)]*2,2)
        with self.assertRaises(ValueError): d.certificate(1,[(1,0)]*2,2)
        with self.assertRaises(ValueError): d.certificate(1,[(0,0)],2)
        with self.assertRaises(ValueError): d.histogram_certificate([1,-1],2)


if __name__=='__main__':
    unittest.main()
