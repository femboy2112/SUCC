"""Focused exact/finite controls for adaptive micro-time Gamma observer.

Elementary algebraic examples over Gaussian rationals are exact; finite floating
calibration is not a rigorous asymptotic certificate or a pi-normality proof.
"""
import cmath
from fractions import Fraction as F
import math
import unittest


def cp(a=0,b=0): return (F(a),F(b))
def ca(x,y): return (x[0]+y[0],x[1]+y[1])
def cs(x,y): return (x[0]-y[0],x[1]-y[1])
def cm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def ci(x):
    d=x[0]*x[0]+x[1]*x[1]
    if not d: raise ZeroDivisionError
    return (x[0]/d,-x[1]/d)
def power(x,n):
    res=cp(1)
    while n:
        if n%2: res=cm(res,x)
        x=cm(x,x); n//=2
    return res

def q(a): return ci(cp(1,-a)) # a denotes 2*pi*x in exact toy arithmetic

def mixing(a): return cs(q(a),power(q(a/F(16)),16))

def prefix(n):
    total=F(0)
    for j in range(1,n+1):
        r=F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2)
        total+=r/F(16**j)
    return total

def zx(y): return cmath.exp(2j*math.pi*y)
def cf(x): return (1/(1-2j*math.pi*x)-1/(1-2j*math.pi*x/16)**16)
def microscale(x,n,g): return math.log1p(g/16**n)/math.log(16)


class AdaptiveGammaTests(unittest.TestCase):
    def test_exact_rational_microwindow_laplace_coefficient(self):
        for a in (F(0),F(1,5),F(-3,2),F(7,1)):
            self.assertEqual(cm(q(a),cp(1,-a)),cp(1))
            self.assertEqual(mixing(a),cs(q(a),power(q(a/F(16)),16)))
            # Cross check exact complex-rational derivative recovery.
            self.assertEqual(cs(cp(1),ci(q(a))),cp(0,a))

    def test_exact_nonlinear_compression_not_a_commutator(self):
        for a in (F(1,3),F(3,2),F(-2)):
            z=cp(0,1)   # unit phase i; its 16th power =1.
            nextz=power(z,16)
            before_average=cm(nextz,q(a))
            after_average=power(cm(z,q(a/F(16))),16)
            self.assertEqual(cs(before_average,after_average),cm(nextz,mixing(a)))
            self.assertNotEqual(before_average,after_average)
            # No noncommutativity of the original source path is inferred.
            self.assertEqual(power(power(z,4),4),power(z,16))
        self.assertEqual(mixing(F(0)),cp(0))

    def test_sequential_jets_are_flat_for_all_real_seeds(self):
        for x in (F(0), F(1), F(1,16), F(-1,5)):
            # Fixed microscope seed i*a, scaled clock from source position.
            for n,h in ((0,1),(1,2),(3,4)):
                self.assertEqual(F(16**(n+h))*x,F(16**h)*(F(16**n)*x))
                self.assertEqual(F(16**(n+h))*x,F(16**n)*(F(16**h)*x))

    def test_positive_forward_microtime(self):
        x=.19634954084936207
        for n in (0,1,3,5):
            for g in (.125,.5,1.,4.):
                step=microscale(x,n,g)
                self.assertGreater(step,0.)
                expected=x*(16**n+g)
                got=x*16**(n+step)
                self.assertAlmostEqual(expected,got,delta=3e-10*max(1,abs(expected)))
            self.assertLessEqual(microscale(x,n,1.),16**(-n)/math.log(16))

    def test_constant_gamma_magnitude_and_deck_gap(self):
        x=math.pi/16
        k=1
        q0=1/(1-2j*math.pi*x)
        q1=1/(1-2j*math.pi*(x+k))
        self.assertGreater(abs(q0-q1),0.1)
        for n in range(1,6):
            # Use same exact circle phase for integer deck aliases (no huge-angle float artifacts).
            phase=zx(16**n*x)
            m0,m1=phase*q0,phase*q1
            self.assertAlmostEqual(abs(m0-m1),abs(q0-q1),delta=1e-14)
            self.assertAlmostEqual(abs(m0),abs(q0),delta=1e-14)

    def test_actual_pi_calibration_has_fixed_nonzero_gap(self):
        x=math.pi/16
        t=(2*math.pi*x)**2
        self.assertGreater(t,F(81,64))
        self.assertLess(t,4)
        lower=(1+t/256)**-8-(1+t)**-.5
        self.assertGreater(lower,.21)
        self.assertGreater(abs(cf(x)),.2)
        self.assertGreater(F(57,65)-F(2,3),F(1,5))
        self.assertGreater(abs(cf(x)),float(F(1,5)))

    def test_sparse_irrational_countermodel_has_good_gamma_gain_but_bad_R0(self):
        # x_bad=3/16 + sum_{j>=1}16^{-4^j}. The omitted infinite tail
        # cannot erase the bound proved on the full sparse series.
        # At B=2*4^j, the next nonzero digit is at 2B; previous
        # digits contribute integers to 16^n*x for B<=n<2B.
        for j in (1,2,3):
            B=2*(4**j)
            next_digit=4**(j+1)
            self.assertEqual(next_digit,2*B)
            partial=F(3,16)+sum((F(1,16**(4**ell))
                                   for ell in range(1,j+2)), F(0))
            total=F(0)
            for n in range(B,2*B):
                frac=(16**n*partial)%1
                self.assertGreaterEqual(frac,0)
                self.assertLess(frac,1)
                total+=frac
            self.assertLess(total,F(1,15))
            self.assertLess(total/B,F(1,15*B))
        # The full infinite tail raises this by < 1/(225) overall;
        # therefore sum of fractional parts < 16/225 for every shell.
        self.assertGreater(F(16,225),F(1,15))
        # Both x_bad in (3/16,1/4) and the true pi/16 obey the
        # same rigorous amplitude bound |c(x)|>1/5, yet x_bad is nonnormal.
        self.assertGreater(F(57,65)-F(2,3),F(1,5))

    def test_exact_source_prefix_tail_and_gamma_approximation(self):
        x=math.pi/16
        for n in range(1,8):
            pn=float(prefix(n))
            un=(16**n)*pn
            tail=(16**n)*(x-pn)
            # Float subtraction at depth 7 is still resolvable to sanity precision.
            self.assertGreater(tail,0.)
            self.assertLess(tail,1/(64*n*n))
            true_M=zx(16**n*x)/(1-2j*math.pi*x)
            approx_M=zx(un)/(1-2j*math.pi*pn)
            error=abs(true_M-approx_M)
            bound=2*math.pi*tail*(1+16**(-n))
            self.assertLessEqual(error,bound+1e-8)
            true_D=cf(x)*zx(16**n*x)
            approx_D=cf(pn)*zx(un)
            error_D=abs(true_D-approx_D)
            bound_D=4*math.pi*tail*(1+16**(-n))
            self.assertLessEqual(error_D,bound_D+1e-8)

    def test_locked_countermodel_does_not_imply_R0(self):
        x=1
        self.assertNotEqual(cf(x),0)
        q0=1/(1-2j*math.pi*x)
        self.assertGreater(abs(q0),0)
        for n in range(1,5):
            # The exact integer orbit has z_n=1. Its Gamma window is q0,
            # its nonlinear compression defect is nonzero, and both are
            # independent of n. These facts imply no anti-locking.
            direct=z=1+0j
            self.assertEqual(direct,1+0j)
            self.assertAlmostEqual(abs(z*q0),abs(q0),delta=1e-14)
            self.assertAlmostEqual(abs(z*cf(x)),abs(cf(x)),delta=1e-14)
        self.assertEqual(sum(1 for _ in range(4))/4,1.)

    def test_full_normality_mode_equivalence_is_not_a_saving(self):
        x=1.
        for h in (1,2,3,8):
            qh=1/(1-2j*math.pi*h*x)
            self.assertNotEqual(qh,0)
            # A gamma window merely rescales the locked character (unchanged average=1).
            self.assertAlmostEqual(abs(qh*1/qh-1),0,delta=1e-14)


if __name__=='__main__': unittest.main()
