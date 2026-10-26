"""Exact seam products, rigorous tails and hostile source-erasure controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.qgamma_seam import (
    normalized_seam_coefficient, finite_seam_product,
    antiperiodic_factorization, antiperiodic_product_interval,
    qgamma_integer, shifted_twist_gamma_ratio, periodic_lambert_interval,
    q_euler_constant_interval,
)


class QGammaSeamTests(unittest.TestCase):
    def test_finite_factorization_and_integer_gamma_holdouts(self):
        for q in (Q(1,16), Q(1,2), Q(2,3), Q(5,7)):
            for n in (0,1,2,7,16):
                a,b=antiperiodic_factorization(q,n)
                self.assertEqual(a,b)
                direct,gamma=shifted_twist_gamma_ratio(q,n+1)
                self.assertEqual(direct,gamma)
        self.assertEqual(qgamma_integer(Q(1,16),1),1)
        self.assertEqual(qgamma_integer(Q(1,16),3),Q(17,16))

    def test_empty_product_and_singular_periodic_seam(self):
        self.assertEqual(finite_seam_product(Q(1,16),0),1)
        self.assertEqual(finite_seam_product(Q(1,16),12,0),1)
        self.assertEqual(normalized_seam_coefficient(Q(1,16),3,16**3),0)
        self.assertEqual(finite_seam_product(Q(1,16),4,16**3),0)
        self.assertNotEqual(finite_seam_product(Q(1,16),4,-1),
                            finite_seam_product(Q(1,16),4,1))

    def test_source_blind_coefficient_survives_forcing_mutation(self):
        # Finite differences in c recover the coefficient independently of
        # the product formula. The actual endpoint changes with forcing.
        endpoints=[]
        for force in (lambda n:Q(),
                      lambda n:Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)):
            values=[]
            for c in (Q(),Q(1)):
                x=c
                for n in range(1,8):
                    x=16*x+force(n)
                values.append(x+c)  # antiperiodic seam residual X7+X0
            endpoints.append(values[0])
            self.assertEqual((values[1]-values[0])/16**7,
                              normalized_seam_coefficient(Q(1,16),7,-1))
        self.assertEqual(endpoints[0],0)
        self.assertGreater(endpoints[1],0)

    def test_product_certificate_refines_and_rejects_truncation_as_limit(self):
        for q,depth in ((Q(1,16),0),(Q(1,2),2),(Q(2,3),4)):
            broad=antiperiodic_product_interval(q,depth)
            fine=antiperiodic_product_interval(q,depth+12)
            self.assertLessEqual(broad.lower,fine.lower)
            self.assertLessEqual(fine.upper,broad.upper)
            self.assertLess(fine.width,broad.width)
            self.assertLess(finite_seam_product(q,depth,-1),broad.lower)
            # A deliberately flipped twist lies below1, outside the plus interval.
            self.assertLess(finite_seam_product(q,depth+1,1),broad.lower)
        with self.assertRaises(ValueError):
            antiperiodic_product_interval(Q(9,10),0)

    def test_lambert_certificate_refines(self):
        for q in (Q(1,16),Q(1,2),Q(2,3)):
            broad=periodic_lambert_interval(q,2)
            fine=periodic_lambert_interval(q,15)
            self.assertLessEqual(broad.lower,fine.lower)
            self.assertLessEqual(fine.upper,broad.upper)
            head=sum((q**n/(1-q**n) for n in range(1,3)),Q())
            self.assertLess(head,broad.lower)

    def test_q_euler_constant_certified_interval_and_independent_oracle(self):
        import mpmath as mp
        with mp.workdps(65):
            for q in (Q(1,16),Q(1,2)):
                interval=q_euler_constant_interval(q,terms=20,log_terms=100)
                mq=mp.mpf(q.numerator)/q.denominator
                value=-mp.diff(lambda a:mp.log(mp.qgamma(a,mq)),mp.mpf(1))
                lo=mp.mpf(interval.lower.numerator)/interval.lower.denominator
                hi=mp.mpf(interval.upper.numerator)/interval.upper.denominator
                self.assertLess(lo,value)
                self.assertLess(value,hi)
                # Fixed-q gamma is not silently relabelled Euler--Mascheroni.
                self.assertLess(hi,mp.euler)
                self.assertLess(hi-lo,mp.mpf('1e-10'))

    def test_inexact_and_out_of_domain_inputs_rejected(self):
        for q in (0,1,-1,Q(17,16),0.5,True):
            with self.assertRaises(ValueError):
                finite_seam_product(q,2)
        for n in (-1,True,2.0):
            with self.assertRaises(ValueError):
                finite_seam_product(Q(1,16),n)
        for twist in (True,0.5):
            with self.assertRaises(ValueError):
                normalized_seam_coefficient(Q(1,16),1,twist)
        with self.assertRaises(ValueError):
            normalized_seam_coefficient(Q(1,16),0)
        with self.assertRaises(ValueError):
            shifted_twist_gamma_ratio(Q(1,16),0)


if __name__ == '__main__':
    unittest.main()
