import unittest
from fractions import Fraction as F
from signed_transport import (
    forcing,orbit,split_primary,projected_history,order16,birth,energy_interval,
    tail_interval,tail_difference_interval,minimum_energy_certificate,
    universal_floor_certificate,fc,
)


class SignedTransportTests(unittest.TestCase):
    def test_source_unrolled_oracle(self):
        values=orbit(30)
        for n in range(1,31):
            unrolled=sum((F(16**(n-j))*(F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2))
                          for j in range(1,n+1)),F())
            self.assertEqual(values[n],unrolled%1)

    def test_primary_projection_homomorphism(self):
        for p in (2,3,5,13,19,73):
            for x,y in [(F(1,15),F(2,39)),(F(7,2*p*p*19),F(17,3*p)),(F(3,7),F(5,11))]:
                a,b=split_primary(x,p);c,d=split_primary(y,p)
                self.assertEqual(split_primary(x+y,p),((a+c)%1,(b+d)%1))

    def test_full_projected_history(self):
        values=orbit(90)
        for p in (2,3,5,7,13,19,73):
            a,v=projected_history(90,p)
            self.assertEqual([split_primary(u,p) for u in values],list(zip(a,v)))

    def test_no_pole_window_cofiber_formula(self):
        values=orbit(150)
        for p in (13,29,73,97,101):
            b,L=birth(p),order16(p)
            v0=split_primary(values[b],p)[1]
            for j in range(L):
                v=(16**j*v0+sum((16**(j-t)*forcing(b+t) for t in range(1,j+1)),F()))%1
                self.assertEqual(v,split_primary(values[b+j],p)[1])

    def test_known_conductor_disappearances(self):
        v=orbit(274)
        self.assertTrue(all(split_primary(v[n],19)[0]==0 for n in range(10,17)))
        self.assertNotEqual(split_primary(v[17],19)[0],0)
        self.assertEqual(split_primary(v[274],73)[0],0)

    def test_lag_source_recurrence_exact(self):
        values=orbit(50,F(17,123))
        for n in range(1,48):
            defect=values[n+2]-17*values[n+1]+16*values[n]
            self.assertEqual((defect-forcing(n+2)+forcing(n+1))%1,0)

    def test_green_difference_positive(self):
        for n in (1,2,7,32,127,383):
            a,b=tail_difference_interval(n)
            self.assertGreater(a,0)
            self.assertLess(b,F(1,(8*n+1)**2))
            ta,tb=tail_interval(n)
            ua,ub=tail_interval(n+1)
            self.assertLessEqual(ta-ub,b)
            self.assertGreaterEqual(tb-ua,a)

    def test_leading_tail_difference_scale(self):
        for n in (32,128,512):
            a,b=tail_difference_interval(n)
            self.assertGreater(32*n**3*a,F(9,10))
            self.assertLess(32*n**3*b,F(11,10))

    def test_minimum_certified_branch_and_interval(self):
        for A,L,h in ((32,16,1),(64,32,3),(128,21,7)):
            c=minimum_energy_certificate(A,L,h)
            self.assertTrue(c['unwrap'])
            lo,hi=c['mean_minimum']
            self.assertGreater(lo,0)
            self.assertLessEqual(lo,hi)
            self.assertLessEqual(hi,c['mean_coherent'][1])

    def test_quadratic_projection_independent_pairwise_formula(self):
        # ||d||²-<a,d>²/||a||² equals pairwise determinant energy /||a||².
        a=[F(1,16**j) for j in range(5)]
        d=[tail_difference_interval(40+j)[0] for j in range(5)]
        aa=sum(x*x for x in a)
        direct=sum(x*x for x in d)-sum(x*y for x,y in zip(a,d))**2/aa
        pair=sum((a[i]*d[j]-a[j]*d[i])**2 for i in range(5) for j in range(i+1,5))/aa
        self.assertEqual(direct,pair)

    def test_universal_floor_multiple_seeds(self):
        for seed in (F(),F(7,31),F(1,16),F(1,15)):
            values=orbit(90,seed)
            for A,L,h in ((10,20,1),(32,40,3),(75,10,7)):
                E,lower=universal_floor_certificate(values,A,L,h)
                self.assertGreaterEqual(E[0],lower[1])

    def test_exact_circle_and_constant_twist_aliases(self):
        values=orbit(50)
        for seed in (F(1,16),F(1,15)):
            altered=orbit(50,seed)
            self.assertEqual(energy_interval(values[1:],7),energy_interval(altered[1:],7))

    def test_invalid_domains_rejected(self):
        for p in (1,2,9):
            with self.assertRaises(ValueError):order16(p)
        for A,L,h in ((0,2,1),(1,1,1),(1,2,0)):
            with self.assertRaises(ValueError):minimum_energy_certificate(A,L,h)


if __name__=='__main__':unittest.main(verbosity=2)
