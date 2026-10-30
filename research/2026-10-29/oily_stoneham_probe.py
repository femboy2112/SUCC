"""Research-only exact probes for Oily / Stoneham / path-sheet laws.
No pi normality, physical gauge field or RH inference.
Use: python research/2026-10-29/oily_stoneham_probe.py -v
"""
from fractions import Fraction as F
from collections import Counter
from math import gcd, isqrt, exp, log
import unittest

def G(x):
    return 1/(2-F(x))**2

def fixed(m):
    q=F(0)
    for _ in range(m):
        q=G(q)
    return q

def harmonic(m):
    return sum((F(1,k) for k in range(1,m+1)), F())

def log_bounds(n,terms=140):
    t=F(n-1,n+1)
    power=t
    val=F(0)
    for j in range(terms):
        val+=2*power/(2*j+1)
        power*=t*t
    return val, val+2*power/((2*terms+1)*(1-t*t))

def omega_bounds(m=12):
    """Rational certificate without numerical Euler constant input."""
    q=fixed(m)
    L,U=log_bounds(m+1)
    a=1-q-harmonic(m)+L
    b=1-q-harmonic(m)+U
    scale=10**24
    s=isqrt(5*scale*scale)
    root_lo,root_hi=F(s,scale),F(s+1,scale)
    lambda_hi=(root_hi-1)/2
    qstar_hi=(3-root_lo)/2
    contraction_hi=2*lambda_hi**3
    return a-qstar_hi*contraction_hi**m-F(1,2*m),b

def pulse(n):
    if n<3: return F()
    x=n
    while x%3==0: x//=3
    return F(1,n) if x==1 else F()

def trajectory(N):
    z=F()
    out=[]
    for n in range(N):
        if n:z=(2*z+pulse(n))%1
        out.append(z)
    return tuple(out)

def stage(p):
    q=3**p
    a=trajectory(3*q)
    return Counter(int(x*q) for x in a[q:3*q])

def ramanujan3(p,h):
    q=3**p
    if h%q==0:return 2*3**(p-1)
    if h%(q//3)==0:return -3**(p-1)
    return 0

def hotspot_bound(N,length):
    assert N>=4 and 0<=length<=1
    p=0
    while 3**(p+1)<=N-1:p+=1
    return F(9,2)*N*length+6*p+3

def possibly_hits(N,left,right):
    z=trajectory(N)
    s=0
    for n,x in enumerate(z):
        if n<3:s+=1;continue
        p=0
        while 3**(p+1)<=n:p+=1
        eps=F(1,2*3**p)
        s+=int(any(left-eps<=x+k<=right+eps for k in (-1,0,1)))
    return s

def source_r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def mat(A,B):
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F())
                       for j in range(len(B[0]))) for i in range(len(A)))

def defect(A,B):
    return mat(A,B)[0][0]-A[0][0]*B[0][0]

def scalar_weight_budget(N,t):
    c=7/16
    return 2*abs(t)*c*exp(2*abs(t)*c)*float(harmonic(N))/N

class ExactChecks(unittest.TestCase):
    def test_source(self):
        self.assertEqual(source_r(1),F(47,15))
        for n in range(1,35):
            self.assertGreater(source_r(n),0)
            self.assertLess(source_r(n+1),source_r(n))

    def test_two_loop_and_one_loop_mutant(self):
        q=fixed(12)
        self.assertTrue(0<q<F(1,2))
        self.assertNotEqual(F(1)/(2-q),q)  # one-loop no longer fixed
        self.assertEqual(G(F(1)),1)

    def test_packet_pgf_coefficients(self):
        for t in (F(0),F(1,2),F(1)):
            approx=sum((F(j+1,2**(j+2))*t**j for j in range(45)), F())
            self.assertLess(abs(approx-G(t)),F(1,100000))

    def test_omega_rational_positive_certificate(self):
        lo,hi=omega_bounds(12)
        self.assertTrue(F(0)<lo<hi<F(1,10))

    def test_stoneham_threefold_unit_sweeps(self):
        for p in range(1,6):
            counts=stage(p)
            self.assertEqual(set(counts),{k for k in range(3**p) if gcd(k,3)==1})
            self.assertEqual(set(counts.values()),{3})

    def test_stage_ramanujan_signs(self):
        from cmath import exp as cexp
        from math import tau
        for p in range(1,6):
            q=3**p
            counts=stage(p)
            for h in (1,2,3,9,27,81):
                numeric=sum(c*cexp(1j*tau*h*a/q) for a,c in counts.items())
                self.assertLess(abs(numeric-3*ramanujan3(p,h)),1e-8)

    def test_stoneham_partial_alpha_tail(self):
        alpha=sum((F(1,3**k*2**(3**k)) for k in range(1,6)),F())
        a=trajectory(100)
        for n in range(3,100):
            d=(2**n*alpha)%1-a[n]
            self.assertTrue(0<=d<F(1,2*n))

    def test_stoneham_hotspot_bound(self):
        intervals=((F(),F(1,16)),(F(1,4),F(1,2)),
                   (F(1,3),F(2,3)),(F(3,7),F(5,7)))
        for N in (4,10,30,60,100,243,500):
            for a,b in intervals:
                self.assertLessEqual(possibly_hits(N,a,b),hotspot_bound(N,b-a))

    def test_mutant_multiplier_not_primitive(self):
        q=9
        self.assertNotEqual({pow(4,j,q) for j in range(6)},
                            {a for a in range(q) if gcd(a,3)==1})

    def test_source_phase_ordering(self):
        b=16
        x,r,s=F(2,9),F(1,7),F(1,11)
        lhs=(b*(b*x+r)+s)%1
        rhs=(b*(b*x+s)+r)%1
        self.assertEqual((lhs-rhs)%1,((b-1)*(r-s))%1)

    def test_nonmultiplicative_compression(self):
        A=((F(1),F(2)),(F(3),F(4)))
        B=((F(2),F(1)),(F(5),F(3)))
        C=((F(3),F(2)),(F(1),F(2)))
        self.assertEqual(defect(A,B),F(10))
        left=defect(mat(A,B),C)+defect(A,B)*C[0][0]
        right=defect(A,mat(B,C))+A[0][0]*defect(B,C)
        self.assertEqual(left,right)
        At=tuple(zip(*A))
        self.assertEqual(defect(At,A),A[1][0]**2)

    def test_no_go_scalar_contrast(self):
        for n in (1,10,100,1000):
            self.assertGreaterEqual(scalar_weight_budget(n,.7),0)
        self.assertLess(scalar_weight_budget(100000,.7),.001)

if __name__=="__main__":
    unittest.main()
