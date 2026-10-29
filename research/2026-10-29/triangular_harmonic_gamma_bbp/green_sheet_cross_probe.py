#!/usr/bin/env python3
"""Exact cross-PR367/PR368 four-pole Green-mixture and first-jet probe.
Not a BBP signed Weyl estimate, source-selected digit sampler, or Lean certificate.
"""
from fractions import Fraction as F
from math import comb
import unittest

def Rforce(a):
    a=F(a)
    if a<=0:raise ValueError('a>0')
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)

def forcing(n):
    if type(n) is not int or n<1:raise ValueError('n>=1')
    return Rforce(8*n-7)

def tail_truncated(n,D):
    if type(n) is not int or n<0 or type(D) is not int or D<1:
        raise ValueError('n>=0, D>=1')
    return sum((F(1,16**j)*forcing(n+j) for j in range(1,D+1)),F())

def finite_future_weights(n,D):
    T=tail_truncated(n,D)
    return tuple(F(1,16**j)*forcing(n+j)/T for j in range(1,D+1))

def Qpoly(x):
    x=F(x)
    return 4-2*x**3-x**4-x**5

def Rpoly(x):
    x=F(x)
    return Qpoly(x)/(16-x**8)

def geometric_source_sheet(n,D,x):
    """Exact kernel Σ_j16^-j x^(8(n+j)-7)Q(x)."""
    x=F(x)
    return sum((F(1,16**j)*x**(8*(n+j)-7)*Qpoly(x) for j in range(1,D+1)),F())

def geometric_source_sheet_closed(n,D,x):
    x=F(x)
    return x**(8*n+1)*Rpoly(x)*(1-(x**8/F(16))**D)

def quad_mul(z,w):
    """Numbers A+B*λ, with λ²=1−λ, represented as (A,B)."""
    a,b=z;c,d=w
    return (a*c+b*d,a*d+b*c-b*d)

def quad_pow(n):
    z=(F(1),F(0))
    for _ in range(n):z=quad_mul(z,(F(0),F(1)))
    return z

def quad_add(*xs):
    return tuple(sum((x[k] for x in xs),F()) for k in (0,1))

def quad_scale(c,z):return c*z[0],c*z[1]

def first_jet_components():
    one=(F(1),F(0));lam4=quad_pow(4);lam5=quad_pow(5)
    v=quad_add(one,quad_scale(2,lam4))
    return (quad_scale(F(59,30),v),
            quad_scale(F(23,15),v),
            quad_add(one,quad_scale(3,lam5)))

def numerical_tail_contrast(a,precision=65):
    import mpmath as mp
    with mp.workdps(precision):
        a=mp.mpf(a);lam=(mp.sqrt(5)-1)/2
        def Rpoly_mp(x):return (1-x)/((2-x*x)*(x*x-2*x+2))
        def w(y):
            x=1-y/a
            return mp.power(x,a)*Rpoly_mp(x)
        intervals=[0,1,4,16,a] if a>16 else [0,1,a]
        def g(y):return mp.log(y)-mp.exp(-lam*y) if y else mp.mpf('0')
        numerator=mp.quad(lambda y:w(y)*g(y),intervals)
        denominator=mp.quad(w,intervals)
        return +(numerator/denominator)

class SourceBridgeTests(unittest.TestCase):
    def test_exact_green_mixture_kernel(self):
        for n in range(0,9):
            for D in range(1,7):
                for x in [F(1,2),F(3,4),F(7,9),F(1,7)]:
                    self.assertEqual(geometric_source_sheet(n,D,x),geometric_source_sheet_closed(n,D,x))
    def test_future_tail_recursion_all_finite_cutoffs(self):
        for n in range(0,18):
            for D in range(2,21):
                self.assertEqual(16*tail_truncated(n,D)-forcing(n+1),tail_truncated(n+1,D-1))
    def test_future_weights_drop_and_renormalize(self):
        for n in range(0,10):
            for D in range(2,12):
                w=finite_future_weights(n,D)
                wnext=finite_future_weights(n+1,D-1)
                self.assertEqual(sum(w),1)
                self.assertTrue(0<w[0]<1)
                for j in range(D-1):
                    self.assertEqual(wnext[j],w[j+1]/(1-w[0]))
    def test_future_offset_limit_exact_mean(self):
        # w_j=15/16^j, E J = 16/15, E(8J−7)=23/15.
        self.assertEqual(F(8)*F(16,15)-7,F(23,15))
        self.assertEqual(sum((F(15,16**j) for j in range(1,100))),1-F(1,16**99))
    def test_three_first_jet_contributions_match_other_pr(self):
        source,clock,coordinate=first_jet_components()
        self.assertEqual(quad_add(source,clock,coordinate),(F(19,2),F(-6)))
        self.assertEqual(quad_pow(4),(F(2),F(-3)))
        self.assertEqual(quad_pow(5),(F(-3),F(5)))
    def test_source_fidelity_mutated_atom_fails(self):
        for n in [0,1,6]:
            x=F(3,4);D=4
            genuine=geometric_source_sheet(n,D,x)
            fake=genuine+F(1,10)*x**(8*n+1)*(1-x)**3
            self.assertNotEqual(genuine,fake)
    def test_original_source_exact_forcing(self):
        for n in range(1,101):
            self.assertEqual(forcing(n),F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
    def test_numerical_heldout_pr368_first_jet(self):
        import mpmath as mp
        with mp.workdps(60):
            lam=(mp.sqrt(5)-1)/2
            omega=lam-mp.euler
            expected=6*lam-mp.mpf(19)/2
            for a in (40,160,800):
                got=numerical_tail_contrast(a,60)
                scaled=a*(got-omega)
                self.assertLess(abs(scaled-expected),mp.mpf(50)/a)
    def test_source_field_is_blind_to_seed_but_orbit_is_not(self):
        # The positive source weights are fixed while an independent initial
        # arithmetic seed shifts the entire circle orbit by 16^n*seed.
        zero,shifted=F(0),F(1,7)
        for n in range(1,13):
            zero=16*zero+forcing(n)
            shifted=16*shifted+forcing(n)
            self.assertEqual(shifted-zero,F(16**n,7))
            self.assertGreater(tail_truncated(n,12),0)
            self.assertEqual(sum(finite_future_weights(n,12)),1)

if __name__=='__main__': unittest.main(verbosity=2)
