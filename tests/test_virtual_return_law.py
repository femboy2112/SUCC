"""Exact calibration: BBP radial source's signed creation/return law.

Finite checks are regression probes, not proof of all-n sign and period laws.
No pi digits or altered original source/seed are input.
"""
from fractions import Fraction as Q
import unittest

ANG=(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
ORIG=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
D=(Q(1),)+(Q(0),)*7+(Q(-1,16),)

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return tuple(p)

def mul(a,b):
    out=[Q() for _ in range(len(a)+len(b)-1)]
    for j,x in enumerate(a):
        for k,y in enumerate(b):
            out[j+k]+=x*y
    return trim(out)

def plus(a,b):
    out=[Q()] * max(len(a),len(b))
    for j,x in enumerate(a): out[j]+=x
    for j,x in enumerate(b): out[j]+=x
    return trim(out)

def scale(a,q): return trim([q*x for x in a])
def deriv(a): return trim([j*a[j] for j in range(1,len(a))]) if len(a)>1 else (Q(),)

def source(n,w):
    return sum((a/Q(8*(n-1)+j) for j,a in enumerate(w,1)),Q())

class SignedBudget(unittest.TestCase):
    def test_01_exact_initial_and_future_sign_calibration(self):
        self.assertEqual(source(1,RAD),Q(2,105))
        for n in range(2,1000):
            self.assertLess(source(n,RAD),0)

    def test_02_exact_original_source_and_endpoint_cancellation(self):
        self.assertEqual(tuple(a+r for a,r in zip(ANG,RAD)),ORIG)
        self.assertEqual(sum(ORIG),0)
        self.assertEqual(sum(ANG),Q(15,4))
        self.assertEqual(sum(RAD),Q(-15,4))
        for n in range(1,150):
            self.assertEqual(source(n,ORIG),source(n,ANG)+source(n,RAD))

    def test_03_rational_logarithmic_derivative_certificate(self):
        # P_rad/(1-t^8/16) = 2 d/dt log((2-t^2)/(t^2-2t+2)).
        num=(Q(2),Q(0),Q(-1))
        den=(Q(2),Q(-2),Q(1))
        numerator=plus(mul(deriv(num),den),scale(mul(num,deriv(den)),-1))
        self.assertEqual(trim(numerator), (Q(4),Q(-8),Q(2)))
        self.assertEqual(mul(RAD,mul(num,den)),scale(mul(D,numerator),2))
        # F(t)-1 = 2t(1-t)/den(t), as a polynomial equality.
        self.assertEqual(plus(num,scale(den,-1)),(Q(0),Q(2),Q(-2)))

    def test_04_exact_discrete_finite_balance(self):
        z=Q()
        bal=Q()
        for n in range(1,301):
            injection=source(n,RAD)
            z=16*z+injection
            bal+=Q(16)**(1-n)*injection
            self.assertEqual(bal,Q(16)**(1-n)*z)
            self.assertGreater(bal,0)

    def test_05_derivative_weight_sign_for_all_m_ge_8(self):
        # For m=8(n-1): [t^m D(t)]'=t^(m-1)*(m-(m+8)*t^8/16).
        # Bracket is >=(15m-8)/16 on [0,1].
        for n in range(2,1000):
            m=8*(n-1)
            self.assertGreater(Q(15*m-8,16),0)
            self.assertGreaterEqual(m-Q(m+8,16),Q(15*m-8,16))
        self.assertLess(Q(-1,2),0)  # n=1: D'(t)=-t^7/2

    def test_06_exact_nonzero_weighted_probe(self):
        # Constant probe integrates G' to zero; the t-weighted probe
        # is -integral G(t)dt < 0 because F(t)>1 on (0,1).
        for t in (Q(1,100),Q(1,3),Q(1,2),Q(3,4),Q(99,100)):
            f=(Q(2)-t*t)/(t*t-2*t+2)
            self.assertGreater(f,1)
        self.assertEqual(source(1,RAD),Q(2,105))

if __name__=='__main__': unittest.main()
