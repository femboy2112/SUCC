"""Research-only exact checks: native Pólya defect and complex-tilt source fidelity."""
from fractions import Fraction as Q
import cmath
import math
import unittest


def fidelity(r, m):
    r = Q(r)
    v = [r**k for k in range(m)]
    return sum(v)**2 / (m*sum(x*x for x in v))


def polya_birth(r, m):
    r = Q(r)
    out = [Q(0)]*(m+1)
    for k in range(m):
        out[k] += Q(m-k,m+1)*r**k
        out[k+1] += Q(k+1,m+1)*r**k
    return out


class SourceStability(unittest.TestCase):
    def test_fidelity_geometric_closed_form(self):
        for r in [Q(1,3),Q(1,2),Q(1),Q(2),Q(4)]:
            for m in range(1,35):
                expected = Q(1) if r == 1 else (1+r)*(1-r**m)/(m*(1-r)*(1+r**m))
                self.assertEqual(fidelity(r,m),expected)
                if r != 1 and m > 1:
                    self.assertLess(expected,1)

    def test_exact_polya_derivative_defect(self):
        for r in [Q(1,2),Q(1),Q(3,2),Q(2)]:
            for m in range(1,30):
                original=polya_birth(r,m)
                expected=[Q(m,m+1)*r**k + (Q(0) if k==0 else Q(1-r,m+1)*k*r**(k-1)) for k in range(m+1)]
                self.assertEqual(original,expected)
                self.assertEqual(original[m] == Q(m,m+1)*r**m,r==1)

    def test_unitary_character_zero_is_not_norm_loss(self):
        L=math.log(2)
        t=math.pi/(2*L)
        amplitudes=[cmath.exp(1j*t*d*L) for d in [-1,1]]
        self.assertLess(abs(sum(amplitudes)),1e-12)
        self.assertAlmostEqual(sum(abs(x)**2 for x in amplitudes)/2,1)

    def test_prime_marked_nonunitary_norm_grows(self):
        eps=.2
        old=0.
        for p in [2,3,5,11,29,97,1013]:
            norm2=math.cosh(2*eps*math.log(p))
            self.assertGreater(norm2,old)
            old=norm2

    def test_sharp_scaling_window(self):
        for c in [.2,1.,3.,8.]:
            target=math.tanh(c)/c
            m=3001
            observed=math.tanh(c)/(m*math.tanh(c/m))
            self.assertGreaterEqual(observed,target-1e-12)
            self.assertLessEqual(observed-target,c*math.tanh(c)/(3*m*m)+1e-12)

    def test_positive_fourier_offline_control(self):
        for a in [1.01,1.5,2.,3.7]:
            d=math.acosh(a)/4
            self.assertTrue(0<d<.5)
            s=.5+d+1j*math.pi/4
            self.assertLess(abs(a+cmath.cosh(4*(s-.5))),1e-11)
            self.assertGreater(a-1,0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
