import itertools
import math
import unittest
from fractions import Fraction as F
from kernel_transport import (source,positive_source,tail_interval,rational_states,
    coefficient_moments,fejer,energy,hard,transport_budget,pointwise_budget,
    entropy_bound_check,surgery_counts)


class KernelTransportTests(unittest.TestCase):
    def test_exact_source_identity(self):
        for n in list(range(1,101))+[997,65537]:
            self.assertEqual(source(n),positive_source(n))
        self.assertEqual(source(1),F(47,15))

    def test_exact_tail_interval_bound(self):
        for n in list(range(1,40))+[73,239,4099]:
            lo,hi=tail_interval(n)
            self.assertGreater(lo,0)
            self.assertLess(hi,F(1,(8*n+1)*(8*n+4)))
            self.assertLess(hi,F(1,64*n*n))

    def test_nested_tail_intervals(self):
        for n in (1,2,19,73):
            lo,hi=tail_interval(n,8)
            lo2,hi2=tail_interval(n,16)
            self.assertLess(lo,lo2)
            self.assertLess(hi2,hi)

    def test_exact_coefficient_moments(self):
        for H in range(2,80):
            self.assertEqual(coefficient_moments(H),(F(H),F(0),F(H*(H*H-1),6)))

    def test_derivative_coefficient_moment(self):
        for H in range(2,80):
            first=sum(F(abs(h)*(H-abs(h)),H) for h in range(1-H,H))
            self.assertEqual(first,F(H*H-1,3))

    def test_feature_distance_bounds(self):
        for H in (2,3,8,31,128):
            D2=4*math.pi**2*H*(H*H-1)/6
            for t in (F(1,997),F(3,100),F(1,2),F(1,H),F(0)):
                dist2=2*(H-fejer(t,H))
                self.assertLessEqual(dist2,2*H+1e-8)
                self.assertLessEqual(dist2,D2*float(t)**2+1e-8)

    def test_original_seed_transport(self):
        for N,H in ((8,8),(16,32),(32,64)):
            xs=rational_states(N)
            ts=[tail_interval(n)[0] for n in range(1,N+1)]
            ys=[(x+t)%1 for x,t in zip(xs,ts)]
            gap=abs(math.sqrt(energy(xs,H))-math.sqrt(energy(ys,H)))
            self.assertLessEqual(gap,pointwise_budget(ts,H)+1e-9)
            self.assertLessEqual(pointwise_budget(ts,H),transport_budget(N,H)+1e-9)

    def test_rational_seed_alias_transport(self):
        for s in (F(1,3),F(1,16),F(-5,7)):
            xs=rational_states(17,s)
            ts=[tail_interval(n)[0] for n in range(1,18)]
            ys=[(x+t)%1 for x,t in zip(xs,ts)]
            self.assertLessEqual(abs(math.sqrt(energy(xs,19))-math.sqrt(energy(ys,19))),
                                 transport_budget(17,19)+1e-9)

    def test_coherent_seed_preserves_large_energy(self):
        for N,H in ((32,16),(64,64)):
            ts=[-tail_interval(n)[0] for n in range(1,N+1)]
            root=math.sqrt(energy(ts,H))
            self.assertLessEqual(math.sqrt(H)-root,transport_budget(N,H)+1e-9)
            self.assertGreater(root,0.95*math.sqrt(H))

    def test_smaller_band_seams(self):
        for q in (16,256):
            pts=[F(0),F(1,q)-F(1,100000),F(1,q),F(1,q)+F(1,100000),F(1,2)]
            for H in (q//4,3*q//8,q//2):
                a=H/q
                C=math.pi**2*a/math.sin(math.pi*a)**2
                self.assertLessEqual(float(hard(pts,q)),C*energy(pts,H)+1e-8)

    def test_constant_improvement(self):
        C=3*math.pi**2/(2*(2+math.sqrt(2)))
        self.assertLess(C,math.pi**2/2)
        self.assertAlmostEqual(C,math.pi**2*(3/8)/math.sin(3*math.pi/8)**2)

    def test_entropy_overlapping_census(self):
        for digits in itertools.product(range(2),repeat=8):
            for k in (1,2,4):
                l1,Q,bound=entropy_bound_check(digits,5,4,k)
                self.assertGreaterEqual(Q,1)
                self.assertLessEqual(float(l1),bound+1e-12)

    def test_surgery_exact_witnesses(self):
        for j in range(2,16):
            row=surgery_counts(j)
            self.assertGreater(row['zero_starts'],0)
            self.assertLess(row['density'],F(1,j))
            self.assertGreater(row['Q_lower'],1)

    def test_sampling_floor(self):
        pts=[F(1,7),F(2,7),F(3,7)]
        for H in (4,8,16,32):
            self.assertGreaterEqual(energy(pts,H)+1e-9,H/len(pts))


if __name__=='__main__': unittest.main(verbosity=2)
