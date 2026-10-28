from fractions import Fraction as F
from math import gcd
import unittest

from observational_succ.lonely_runner_referee_bounds import (
    short_unit_set,short_coprime_denominator,inverse_time,refined_bounds,endpoint_spacing,
    phase_unit,upper_half_gap)
from observational_succ.lonely_runner_two_entry import uncovered_intervals,periodic_occupancy


class RefereeBounds(unittest.TestCase):
    def test_explicit_units_and_every_cyclic_gap(self):
        for r in range(1,1001):
            units=short_unit_set(r)
            self.assertTrue(all(gcd(x,r)==1 for x in units))
            gaps=[b-a for a,b in zip(units,(*units[1:],units[0]+r))]
            self.assertLessEqual(max(gaps),r//2+1)
            if r>=7:self.assertLessEqual(2*max(gaps),r-2)

    def test_constructed_source_witness_not_only_gcd(self):
        for n in range(5,55):
            for r in range(1,(n-1)//2+1):
                t,mu=inverse_time(n,r)
                d=short_coprime_denominator(n,r)
                self.assertGreaterEqual(d,n+r)
                self.assertTrue(0<=t<=1)
                for v in range(1,n):
                    if v!=r:
                        x=v*t%1
                        self.assertGreaterEqual(min(x,1-x),mu)

    def test_sharp_small_bounds_and_integer_ceiling(self):
        self.assertEqual(refined_bounds(5,1,3)['first_strict_bound'],F(18))
        for n in range(5,35):
            for r in range(1,n):
                for s in range(r+1,n):
                    b=refined_bounds(n,r,s)
                    self.assertLess(b['first_integer_max'],b['first_strict_bound'])
                    self.assertGreaterEqual(b['first_integer_max']+1,b['first_strict_bound'])
                    self.assertLess(b['second_multiplier']*b['first_strict_bound'],2*n**3)

    def test_oriented_endpoint_bound_and_same_label(self):
        for n in range(3,10):
            for u in range(1,18):
                for v in range(1,18):
                    lower=endpoint_spacing(n,u,v)
                    for k in range(3):
                        for l in range(3):
                            length=F(n*l-1,n*v)-F(n*k+1,n*u)
                            if length>0:self.assertGreaterEqual(length,lower)
        self.assertEqual(endpoint_spacing(5,7,7),F(3,35))
        # Equal-label adjacency is much stronger than 1/(n*v).
        self.assertGreater(endpoint_spacing(5,7,7),F(1,35))

    def test_two_band_connected_components(self):
        # Independent full union and exact complementary lengths. Each
        # connected covered component must satisfy the paper two-band bound.
        for n in range(5,10):
            for u in range(n,n+7):
                for v in range(u+1,u+8):
                    gaps=uncovered_intervals(n,(u,v))
                    covered=[];a=F(0)
                    for left,right in gaps:
                        covered.append((a,left));a=right
                    covered.append((a,F(1)))
                    for a,b in covered:
                        self.assertLessEqual(b-a,F(2,n*u)+F(4,n*v))

    def test_occupancy_boundary_is_attained(self):
        for n in (5,6,17,101):
            w=n*n+1
            a,b=F(-1,n*w),F(1,n*w)
            actual=periodic_occupancy(n,w,a,b)
            self.assertEqual(actual-2*(b-a)/n,F(2*(n-2),n*n*w))

    def test_wrong_domains_and_endpoint_orientation(self):
        for x in (True,2.0):
            with self.assertRaises(TypeError):short_unit_set(x)
        with self.assertRaises(ValueError):inverse_time(8,4)
        with self.assertRaises(ValueError):refined_bounds(6,2,2)
        # Opposite orientation cannot be substituted: endpoints of one band
        # are 2/(nv) apart, less than the good gap (n-2)/(nv) at n>=5.
        self.assertLess(F(2,35),endpoint_spacing(5,7,7))

    def test_unit_phase_and_sharp_sixth(self):
        for r in range(2,151):
            for w in range(1,r):
                p=phase_unit(r,w)
                self.assertEqual(gcd(p,r),1)
                x=F(w*p,r)%1
                self.assertGreaterEqual(min(x,1-x),F(1,6))
        # q=6 shows why a uniform 1/5 strengthening fails.
        self.assertEqual(max(min(F(p,6)%1,1-F(p,6)%1)
                             for p in range(6) if gcd(p,6)==1),F(1,6))

    def test_quadratic_gap_source_semantics_and_huge_multiples(self):
        from math import lcm
        counts={'unit phase':0,'common multiple':0}
        for n in range(7,30):
            for r in range((n-1)//2+1,n-1):
                for s in range(r+1,n):
                    for w in (n,n*n+1,lcm(r,s)*10**45):
                        if w<n:continue
                        gap=upper_half_gap(n,r,s,w)
                        counts[gap['branch']]+=1
                        a,b=gap['left'],gap['right'];center=(a+b)/2
                        self.assertTrue(0<a<b<1)
                        for v in (*[i for i in range(1,n) if i not in (r,s)],w):
                            k=(v*center).numerator//(v*center).denominator
                            # Independent exact good-band semantics, all real
                            # points in (a,b), including endpoint equality.
                            self.assertGreaterEqual(v*a,k+F(1,n))
                            self.assertLessEqual(v*b,k+1-F(1,n))
                        if gap['branch']=='common multiple':
                            self.assertGreaterEqual(b-a,gap['length_lower'])
                        else:
                            # Center is an exact integer for every potential
                            # covering v2 divisible by the nominated deletion.
                            self.assertEqual(F(gap['unit']*gap['deleted'],gap['deleted']).denominator,1)
        self.assertTrue(all(counts.values()))


if __name__=='__main__':unittest.main()
