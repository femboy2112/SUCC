from fractions import Fraction as Q
import random
import unittest
from source_probe import origin_average, circular_discrepancy, sinc_squared, SCALE, phase, Box


def direct(local,p,M,a,b):
    cuts=sorted({Q(0),Q(1)}|{Q(M*r%p,p) for r in local})
    result=Q(0)
    for left,right in zip(cuts,cuts[1:]):
        t=(left+right)/2
        buckets={}
        for j,r in enumerate(local):
            label=(Q(M*r,p)-t).__floor__()%M
            buckets.setdefault(label,[]).append(j)
        product=sum((sum(a[j] for j in js)*sum(b[j] for j in js)/len(js)
                     for js in buckets.values()),Q(0))/len(local)
        result+=(right-left)*product
    return result


class SourceProbeTests(unittest.TestCase):
    def test_sweep_independent_repartition(self):
        rng=random.Random(61217)
        for N in (1,2,5,13,31):
            for p in (1,5,17,37):
                for M in (1,2,4,16,41):
                    local=[rng.randrange(p) for _ in range(N)]
                    a=[Q(rng.randrange(-5,6),7) for _ in local]
                    b=[Q(rng.randrange(-5,6),11) for _ in local]
                    self.assertEqual(origin_average(local,p,M,a,b),direct(local,p,M,a,b))
    def test_endpoints_duplicates_saturation(self):
        x=[0,0,1,2,3,3];a=list(map(Q,[1,1,3,-2,0,0]));b=list(map(Q,[2,3,4,5,6,7]))
        expected=sum(u*v for u,v in zip(a,b))/len(a)
        for M in (4,8,17):
            self.assertEqual(origin_average(x,4,M,a,b),expected)
    def test_discrepancy_grid(self):
        for p in (1,2,7,29):
            self.assertEqual(circular_discrepancy(list(range(p)),p),Q(1,p))
            self.assertEqual(circular_discrepancy([0]*9,p),Q(1))
    def test_discrepancy_rotation(self):
        x=[0,0,2,5,7,7,10]
        d=circular_discrepancy(x,13)
        for k in range(13):
            self.assertEqual(circular_discrepancy([(r+k)%13 for r in x],13),d)
    def test_interval_sweep_contains_rational_control(self):
        x=[0,1,2,3]; a=[phase(r,4) for r in x]; b=[v.conjugate() for v in a]
        for M in (1,2,4,7):
            F=origin_average(x,4,M,a,b,zero=Box(),divide=lambda z,n:z.divide(n))
            target={1:Q(0),2:Q(1,2),4:Q(1),7:Q(1)}[M]
            self.assertLessEqual(F.re.lo*target.denominator,target.numerator*SCALE)
            self.assertGreaterEqual(F.re.hi*target.denominator,target.numerator*SCALE)
            self.assertLessEqual(F.im.lo,0);self.assertGreaterEqual(F.im.hi,0)
    def test_sinc_zero_and_alias(self):
        self.assertEqual(sinc_squared(0,4).lo,SCALE)
        for h in (4,8):
            x=sinc_squared(h,4)
            self.assertLessEqual(x.lo,0);self.assertGreaterEqual(x.hi,0)
    def test_invalid_data(self):
        for args in (([],3,2,[],[]),([3],3,2,[Q(1)],[Q(1)]),([0],3,0,[Q(1)],[Q(1)])):
            with self.assertRaises(ValueError):origin_average(*args)

if __name__=='__main__':unittest.main()
