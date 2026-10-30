import unittest
from fractions import Fraction as F
from moving_frequency import (source, orbit, distance, deficit_lower,
    lag_energy_lower, green_interval, SIGNED_CONSTANT, LAG_CONSTANT)


class MovingFrequency(unittest.TestCase):
    def test_exact_authentic_source(self):
        self.assertEqual(source(1), F(47,15))
        self.assertEqual(source(2), F(106,819))
        for n in (1,2,7,31,97,257):
            expected = F(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(source(n), expected)

    def test_source_two_sided(self):
        for n in range(1,301):
            self.assertLessEqual(F(15,(8*n-2)**2),source(n))
            self.assertLessEqual(source(n),F(15,(8*n-7)**2))
            gap=source(n)-source(n+1)
            self.assertLessEqual(F(240,(8*n+6)**3),gap)
            self.assertLessEqual(gap,F(240,(8*n-7)**3))

    def test_quarter_separation(self):
        for a in (4,12,28,44,76):
            for h in ((a*a+1)//2,3*a*a//4,a*a):
                smallest=h*(source(5*a//4)-source(7*a//4+1))
                largest=h*(source(a+1)-source(2*a))
                self.assertGreaterEqual(smallest,F(9,245))
                self.assertLessEqual(largest,F(15,64))

    def test_source_signed_certificate(self):
        for a in (4,12,28,44,76):
            for h in (a*a//2,3*a*a//4,a*a):
                q=[h*source(n+1) for n in range(a,2*a)]
                self.assertGreaterEqual(deficit_lower(q)/289,SIGNED_CONSTANT*a)

    def test_selected_and_rational_seed_certificates(self):
        for a in (4,12,28):
            for seed in (F(),F(1,3),F(1,16),F(-7,19)):
                vals=orbit(2*a,seed)
                for h in (a*a//2,a*a):
                    lower=deficit_lower([h*vals[n] for n in range(a,2*a+1)])
                    self.assertGreaterEqual(lower,SIGNED_CONSTANT*a)

    def test_cubic_source_lag_band(self):
        for a in (2,4,12,28,44,76):
            for h in ((a**3+1)//2,3*a**3//4,a**3):
                gaps=[h*(source(n+1)-source(n+2)) for n in range(a,2*a-1)]
                self.assertGreaterEqual(min(gaps),F(15,512))
                self.assertLessEqual(max(gaps),F(15,32))
                lower=sum((8*distance(g)**2 for g in gaps),F())/289
                self.assertGreaterEqual(lower,(a-1)*LAG_CONSTANT)

    def test_selected_cubic_energy(self):
        for a in (4,12,28,44,76):
            vals=orbit(2*a)
            for h in ((a**3+1)//2,3*a**3//4,a**3):
                self.assertGreaterEqual(lag_energy_lower(vals,a,h),(a-1)*LAG_CONSTANT)

    def test_exact_eventual_alias(self):
        normal=orbit(60)
        alias=orbit(60,F(1,16))
        self.assertTrue(all(distance(a-b)==0 for a,b in zip(normal[1:],alias[1:])))

    def test_coherent_tail_interval(self):
        for n in (4,12,28,44,76):
            lo,hi=green_interval(n)
            self.assertTrue(0<lo<hi<F(1,(8*n+1)**2))
            l2,h2=green_interval(n+1)
            self.assertTrue(lo-h2>0)
            self.assertLess(hi-l2,F(16,(8*n+1)**3))

    def test_zero_source_refutes_unqualified_claim(self):
        self.assertEqual(deficit_lower([F()]*17),0)
        self.assertEqual(source(5,(0,0,0,0)),0)
        self.assertGreater(SIGNED_CONSTANT*16,0)

    def test_mutants_are_not_original_source_certificates(self):
        # Same age/rank family and same-ratio mutant retain positive decay;
        # they are distinct sources and cannot inherit the exact constants by fiat.
        for c in ((6,-8,1,1),(4,0,-1,0),(5,-2,-1,-1)):
            self.assertNotEqual(source(7,c),source(7))
        self.assertGreater(source(7,(6,-8,1,1)),0)


if __name__=='__main__': unittest.main(verbosity=2)
