"""Independent tests: exact BBP gauge/four-root algebra plus noncertifying holdouts.
No π digits as input. No changes to the original zero-seeded source.
"""
from __future__ import annotations
from fractions import Fraction as Q
import math
import unittest

P=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
DUAL=(Q(0),Q(8),Q(4),Q(4),Q(0),Q(0),Q(-1),Q(0))
ANG=tuple((2*x+y)/4 for x,y in zip(P,DUAL))
RAD=tuple((2*x-y)/4 for x,y in zip(P,DUAL))
D8=(Q(1),)+(Q(0),)*7+(Q(-1,16),)

def add(*ps):
    m=max(map(len,ps))
    return tuple(sum((p[j] if j<len(p) else Q(0) for p in ps),Q(0)) for j in range(m))

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):
            out[j+k]+=x*y
    return tuple(out)

def scaled(a,q):
    return tuple(q*x for x in a)

def eq(a,b):
    return all((a[j] if j<len(a) else Q(0))==(b[j] if j<len(b) else Q(0))
               for j in range(max(len(a),len(b))))

def diff(a):
    return tuple(j*a[j] for j in range(1,len(a))) or (Q(0),)

def wlam(lam):
    return tuple(a+Q(lam)*r for a,r in zip(ANG,RAD))

def source(n,w):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(w,1)),Q(0))

def state(n,w):
    x=Q(0)
    for k in range(1,n+1):
        x=16*x+source(k,w)
    return x

def shadow(a,w):
    sign={1:1,3:-1,5:-1,7:1}[a]
    out=[]
    for ell in range(1,9):
        j=(a*ell-1)%8+1
        out.append(Q(sign)**(8-ell)*Q(2)**((j-ell)//2)*w[j-1])
    return tuple(out)

def gm(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c

def gp(x,n):
    z=(Q(1),Q(0))
    for _ in range(n):
        z=gm(z,x)
    return z

def radial_tail_float(x):
    return -sum(16.**(-m)*sum(float(c)/(8*(x+m-1)+j)
                for j,c in enumerate(RAD,1)) for m in range(1,24))

class TestVirtualGaugeCircle(unittest.TestCase):
    def test_01_original_preserved(self):
        self.assertEqual(add(ANG,RAD),P)
        self.assertEqual(wlam(1),P)
        self.assertEqual(wlam(-1),tuple(q/2 for q in DUAL))
        self.assertEqual(ANG,(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0)))
        self.assertEqual(RAD,(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0)))

    def test_02_angular_exact_rational_kernel(self):
        # P_ang/(1-t^8/16)=4/(t^2-2t+2)
        self.assertTrue(eq(mul(ANG,(Q(2),Q(-2),Q(1))),scaled(D8,4)))

    def test_03_radial_exact_log_coboundary(self):
        # P_rad/D8=2 d/dt log[(2-t²)/(t²-2t+2)]
        a=(Q(2),Q(0),Q(-1)); b=(Q(2),Q(-2),Q(1))
        lhs=mul(RAD,mul(a,b))
        rhs=scaled(mul(D8,add(mul(diff(a),b),scaled(mul(a,diff(b)),-1))),2)
        self.assertTrue(eq(lhs,rhs))
        self.assertEqual(a[0],b[0])
        self.assertEqual(sum(a),sum(b))

    def test_04_unique_original_endpoint_pin(self):
        self.assertEqual(sum(ANG),Q(15,4))
        self.assertEqual(sum(RAD),Q(-15,4))
        for lam in (Q(-5),Q(-1),Q(0),Q(1),Q(2),Q(7,3)):
            self.assertEqual(sum(wlam(lam)),Q(15,4)*(1-lam))
        self.assertEqual(sum(wlam(1)),Q(0))

    def test_05_exact_frobenius_mirror(self):
        for lam in (Q(-5),Q(-1),Q(0),Q(1),Q(2),Q(7,3)):
            for a in (1,5):
                self.assertEqual(shadow(a,wlam(lam)),wlam(lam))
            for a in (3,7):
                self.assertEqual(shadow(a,wlam(lam)),tuple(-q for q in wlam(-lam)))

    def test_06_all_four_gaussian_rotations(self):
        u=(Q(1,2),Q(1,2))
        quarter=(Q(0),Q(1))
        self.assertEqual(gp(u,8),(Q(1,16),Q(0)))
        for k in range(4):
            v=gm(gp(quarter,k),u)
            self.assertEqual(gp(v,8),(Q(1,16),Q(0)))
            taps=tuple(4*gp(v,j)[1] for j in range(1,9))
            denominator=(Q(1),-2*v[0],v[0]**2+v[1]**2)
            self.assertTrue(eq(mul(taps,denominator),scaled(D8,4*v[1])))
            if k==0:
                self.assertEqual(taps,ANG)

    def test_07_gaussian_quarter_turn_periods_diagnostic(self):
        targets=(math.pi,4*math.atan(1/3),-4*math.atan(1/3),-math.pi)
        for k in range(4):
            v=(1j)**k*complex(0.5,0.5)
            actual=-4*math.atan2((-v).imag,(1-v).real)
            self.assertAlmostEqual(actual,targets[k],places=13)

    def test_08_odd_denominator_fiber(self):
        for lam in (Q(-1),Q(0),Q(1),Q(2),Q(7,3)):
            x=Q(0); w=wlam(lam)
            for n in range(1,101):
                x=16*x+source(n,w)
                self.assertEqual(x.denominator%2,1,(lam,n))

    def test_09_radial_source_positive_but_not_zero(self):
        u=y=z=Q(0)
        for n in range(1,201):
            u=16*u+source(n,P)
            y=16*y+source(n,ANG)
            z=16*z+source(n,RAD)
            self.assertEqual(u,y+z)
            self.assertGreater(z,0)
            self.assertLess(z,Q(1,32*n+16))
        self.assertLess(abs(200*float(z)-1/32),0.0003)

    def test_10_zero_seed_equals_infinite_radial_tail(self):
        for n in (1,5,17,53):
            actual=state(n,RAD)
            tail=-sum((Q(16)**(-j))*source(n+j,RAD) for j in range(1,65))
            self.assertLess(abs(actual-tail),Q(1,10**43))

    def test_11_preregistered_new_epoch_holdouts(self):
        # Floating diagnostics, NOT asymptotic theorem certificates.
        for A in (307,953,1901):
            H=16**int(math.log(A*A*math.log(A),16))
            self.assertGreaterEqual(H,A*A*math.log(A)/16)
            self.assertLessEqual(H,A*A*math.log(A))
            zs=[radial_tail_float(n) for n in range(A,2*A)]
            hi=sum(complex(math.cos(2*math.pi*H*z),math.sin(2*math.pi*H*z)) for z in zs)
            lo=sum(complex(math.cos(2*math.pi*z),math.sin(2*math.pi*z)) for z in zs)
            self.assertLess(abs(hi)/A,0.25)
            self.assertGreater(abs(lo)/A,0.99)

    def test_12_radial_second_difference_holdout(self):
        for n in (307,953,1901):
            d2=radial_tail_float(n+1)-2*radial_tail_float(n)+radial_tail_float(n-1)
            self.assertLess(abs(16*n**3*d2-1),0.02)

if __name__=="__main__":
    unittest.main()
