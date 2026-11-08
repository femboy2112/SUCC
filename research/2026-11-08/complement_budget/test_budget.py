import unittest
from fractions import Fraction as Q
from math import isqrt

from certified_fft import PrimeDFT, fft, center, SCALE, phase
from source_budget import Box, Interval, magnitude_upper, stream_source, unpacked
from source_budget import certify, packed, mean, clock, source_xi, order16


class CertifiedTransformTests(unittest.TestCase):
    def test_radix_two_against_direct_interval_sum(self):
        for n in (1,2,4,8,16,32):
            values = [(SCALE*((j*7)%11-5)//7,SCALE*((j*j)%13-6)//9) for j in range(n)]
            for sign in (-1,1):
                observed,radius = fft(values,0,sign)
                for k,(x,y) in enumerate(observed):
                    exact = Box()
                    for j,(a,b) in enumerate(values):
                        exact = exact + Box(Interval(a,a),Interval(b,b))*phase(sign*j*k,n)
                    distance = max(abs(x-exact.re.lo),abs(x-exact.re.hi))+max(abs(y-exact.im.lo),abs(y-exact.im.hi))
                    # Direct enclosures have their own outward width; midpoint
                    # discrepancy must fit summed independent radii.
                    midpoint,rr = center(exact)
                    self.assertLessEqual(abs(x-midpoint[0])+abs(y-midpoint[1]),radius+rr)

    def test_bluestein_prime_and_composite_lengths(self):
        for n in (2,3,5,7,9,17,31):
            boxes = [phase(j*j+2*j,19) for j in range(n)]
            inputs = [center(b) for b in boxes]
            out,rad = PrimeDFT(n).transform([v for v,r in inputs],max(r for v,r in inputs))
            for k,(x,y) in enumerate(out):
                exact = Box()
                for j,b in enumerate(boxes):
                    exact = exact+b*phase(-j*k,n)
                midpoint,rr = center(exact)
                self.assertLessEqual(abs(x-midpoint[0])+abs(y-midpoint[1]),rad+rr)
            self.assertLess(Q(rad,SCALE),Q(1,10**12))

    def test_impulse_constant_and_sign(self):
        for n in (5,17):
            engine = PrimeDFT(n)
            for index in (0,1,n-1):
                values = [(0,0)]*n
                values[index] = (SCALE,0)
                out,rad = engine.transform(values)
                for k,value in enumerate(out):
                    expected,rr = center(phase(-index*k,n))
                    self.assertLessEqual(abs(value[0]-expected[0])+abs(value[1]-expected[1]),rad+rr)

    def test_dual_bound_allows_unbounded_resonance(self):
        # Exact real orthogonal r,u on four points; no float or FFT.
        r = [Q(1)]*4
        B = [Q(1),Q(-1),Q(0),Q(0)]
        atom = [Q(1),Q(-1),Q(1),Q(-1)]
        E = sum(x*x for x in B)/4
        W = sum(B)/4
        M = abs(sum(x*y for x,y in zip(B,atom))/4) # weight1
        lower = (E-W*W)/(max(1,M)+abs(W))
        for R in (Q(-100),Q(0),Q(1,7),Q(100)):
            for c in (Q(-2),Q(0),Q(1,2),Q(3)):
                rho = sum(abs(b-R-c*a) for b,a in zip(B,atom))/4
                self.assertGreaterEqual(rho+abs(c),lower)
        # A perfect resonance must not acquire a spurious obstruction.
        self.assertEqual((Q(1)-Q(1)**2)/(1+Q(1)),0)

    def test_reject_invalid_fft_inputs(self):
        for values in ([],[(0,0)]*3):
            with self.assertRaises(ValueError):fft(values)
        with self.assertRaises(ValueError):PrimeDFT(1)

    def test_complete_menu_known_controls(self):
        import contextlib
        import io
        p = 73
        xs = clock(p,source_xi(p))
        m = order16(p)
        for label,B in [('zero',[Box() for _ in xs]),
                        ('coherent',[phase(-x,p) for x in xs]),
                        ('nonresonant',[phase(2*x,p) for x in xs])]:
            W = mean(b*phase(x,p) for x,b in zip(xs,B))
            data = {'A':0,'p':p,'m':m,'rows':[{'h':1,'B':[packed(b) for b in B],'W':packed(W)}]}
            with contextlib.redirect_stdout(io.StringIO()):
                receipt = certify(data)
            for row in receipt['rows'][0]['menu_certificates']:
                value = row['rho_plus_budget_lower']
                lower = Q(value['numerator'],value['denominator'])
                if label in ('zero','coherent'):
                    self.assertEqual(lower,0)
                else:
                    # Known exact fit has rho=0 and arithmetic cost sqrt(p)/m.
                    self.assertGreater(lower,0)
                    self.assertLessEqual(lower*lower,Q(p,m*m))


if __name__ == '__main__':
    unittest.main()
