import unittest
from fractions import Fraction as Q
from probes import (forcing,states,distance,source_tail_bound,sparse_interval,
                    sparse_fraction_interval,lag_tail_interval,distance_interval,
                    coherent_windows)

class DiophantineTests(unittest.TestCase):
    def test_source_rational_positive_decomposition(self):
        for n in (1,2,3,19,73,127):
            a=8*n-7
            alt=Q(6,a*(a+3))+Q(4,a*(a+4))+Q(5,a*(a+5))
            self.assertEqual(forcing(n),alt)
    def test_rational_derivative_certificate(self):
        for a in (1,5,19,257):
            for d in (3,4,5):
                self.assertEqual(Q(2,a**3)-Q(2*a+d,a*a*(a+d)**2),
                                 Q(d*(3*a+2*d),a**3*(a+d)**2))
    def test_source_difference_bound(self):
        for n in range(1,80):
            d=forcing(n)-forcing(n+1)
            self.assertTrue(0<d<Q(240,(8*n-7)**3))
    def test_multilag_source_interval(self):
        for n in (1,7,29,83):
            for ell in (1,2,5,13):
                lo,hi=lag_tail_interval(n,ell)
                self.assertTrue(0<lo<hi<source_tail_bound(n,ell))
    def test_no_wrap_exact(self):
        for q in (17,53,181,1009):
            aa=[a for a in range(-q,q) if -q<17*a<q]
            for a in aa:
                for b in aa:
                    if (16*a-b)%q==0:self.assertEqual(b,16*a)
    def test_threshold_two_cycle(self):
        self.assertEqual(16*Q(1,17)-Q(-1,17),1)
        self.assertEqual(16*Q(-1,17)-Q(1,17),-1)
    def test_sparse_truncations_reduced_and_nested(self):
        for m in (3,4,5):
            for j in range(4):
                lo,hi,d=sparse_interval(m,m**j)
                lo2,hi2,_=sparse_interval(m,m**(j+1))
                self.assertEqual(lo.denominator,16**(m**j))
                self.assertTrue(lo<lo2<hi2<hi)
                self.assertTrue(Q(1,16**d)<hi-lo)
    def test_sparse_digit_interval(self):
        for m in (3,4,5):
            for n in (1,7,19,67):
                blo,bhi,_=sparse_interval(m,n+15)
                lo,hi=sparse_fraction_interval(m,n,15)
                val=blo*16**(n-1)
                self.assertEqual(val-val.numerator//val.denominator,lo)
                self.assertEqual((bhi-blo)*16**(n-1),hi-lo)
    def test_distance_interval_wrap_safe(self):
        lo,hi=distance_interval(Q(99,100),Q(101,100))
        self.assertEqual(lo,0)
        self.assertEqual(hi,Q(3,100))
    def test_cubic_band_source_budget(self):
        for a in (19,37,61,107):
            self.assertLess((a**3//6)*source_tail_bound(a),Q(1,180))
    def test_exact_alias_and_periodic_translation(self):
        u=states(40)
        for n in range(1,39):
            self.assertEqual(distance((u[n+1]+16**n)-(u[n]+16**(n-1))),
                             distance(u[n+1]-u[n]))
            self.assertEqual((16**(n+2)-16**n)%17,0)
    def test_whole_sparse_windows(self):
        self.assertEqual(len(coherent_windows()),9)

if __name__=='__main__':unittest.main(verbosity=2)
