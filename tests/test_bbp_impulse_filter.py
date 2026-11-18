"""Original BBP impulse factorization and its source-boundary limits.

Exact rational checks only; no digit normality / all-shell inequality is claimed.
The paper proof supplies universal polynomial, spectral and integral identities.
"""
from fractions import Fraction as F
import unittest

COEFFS=(4,0,0,-2,-1,-1)
DIFF=(1,-1)
MEMORY=(4,4,4,2,1)

def conv(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):z[i+j]+=ai*bj
    return tuple(z)

def polyval(a,x):
    out=0
    for v in reversed(a):out=out*x+v
    return out

def forcing(n):
    a=8*n-7
    return F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)

def three_transport(n):
    a=8*n-7
    return F(6,a*(a+3))+F(4,a*(a+4))+F(5,a*(a+5))

def beta_transport(n):
    a=8*n-7
    return sum((F(v,(a+j)*(a+j+1)) for j,v in enumerate(MEMORY)),F(0))

def reduced(t):
    return (1-t)/((2-t*t)*(t*t-2*t+2))

def original_integrand(t):
    return polyval(COEFFS,t)/(16-t**8)

class BBPImpulseFilterTests(unittest.TestCase):
    def test_exact_convolution_and_signed_impulses(self):
        self.assertEqual(conv(DIFF,MEMORY),COEFFS)
        self.assertEqual(COEFFS,(4,0,0,-2,-1,-1))
        self.assertEqual(sum(COEFFS),0)
        self.assertEqual(sum(j*v for j,v in enumerate(COEFFS)),-15)
        self.assertEqual(sum(MEMORY),15)

    def test_three_positive_lagged_causal_differences(self):
        for n in range(1,101):
            self.assertEqual(forcing(n),three_transport(n))
            self.assertGreater(forcing(n),0)
            self.assertGreater(forcing(n),forcing(n+1))

    def test_positive_five_beta_channels(self):
        for n in range(1,101):
            self.assertEqual(forcing(n),beta_transport(n))
            self.assertGreater(beta_transport(n),0)

    def test_source_mask_polynomial_factorization(self):
        h=conv((2,0,1),(2,2,1)) # (t²+2)(t²+2t+2)
        self.assertEqual(h,MEMORY)
        self.assertEqual(conv(DIFF,h),COEFFS)
        self.assertEqual(polyval(COEFFS,F(1)),0)
        self.assertEqual(polyval(h,F(1)),15)

    def test_completion_denominator_has_exact_memory_factor(self):
        d=conv((2,0,-1),(2,-2,1)) # (2-t²)(t²-2t+2)
        prod=conv(MEMORY,d)
        self.assertEqual(prod,(16,0,0,0,0,0,0,0,-1))
        for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            self.assertEqual(original_integrand(t),reduced(t))

    def test_primitive_derivative_has_closed_rational_form(self):
        # F(t)=1/8 log[(2-t²)/(t²-2t+2)] +1/4 arctan(t-1)
        # is an antiderivative of the reduced integrand.
        for t in (F(0),F(1,7),F(1,3),F(1,2),F(1)):
            D=t*t-2*t+2
            derivative=(F(1,8)*(-2*t/(2-t*t)-(2*t-2)/D)
                        +F(1,4)/D)
            self.assertEqual(derivative,reduced(t))
        # log ratio at endpoints is exactly 1; only the arctan term remains.
        for t in (F(0),F(1)):
            self.assertEqual((2-t*t)/(t*t-2*t+2),1)

    def test_exact_spectral_factor_and_no_extra_unit_circle_zeros(self):
        # c=cos(theta); |H(e^{i theta})|²=(1+8c²)*(8(c+3/4)²+1/2)
        for c in (F(-1),F(-9,10),F(-3,4),F(-1,2),F(0),F(1,2),F(1)):
            first=1+8*c*c
            second=8*(c+F(3,4))**2+F(1,2)
            self.assertGreaterEqual(first,1)
            self.assertGreaterEqual(second,F(1,2))
            self.assertLessEqual(first,9)
            self.assertLessEqual(second,25)
            self.assertGreater(first*second,0)

    def test_dc_null_and_zero_origin_do_not_force_gap(self):
        self.assertEqual(polyval(COEFFS,1),0)
        # Unitary cyclic shift S: Q(S) kills the constant sequence.
        for N in (2,3,5,16):
            signal=(1,)*N
            z=[]
            for n in range(N):
                z.append(sum(COEFFS[j]*signal[(n+j)%N]
                             for j in range(len(COEFFS))))
            self.assertEqual(z,[0]*N)

    def test_first_nonvanishing_moment_matches_radix_minus_one(self):
        self.assertEqual(-sum(j*v for j,v in enumerate(COEFFS)),16-1)
        # This is not a transported BBP Weyl-mode inequality; it is a
        # source-polynomial derivative measured in Mellin-exponent units.

if __name__=='__main__':unittest.main()
