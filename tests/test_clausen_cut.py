"""Independent small-source controls for Clausen zero-seed selection pressure.
Unwrapped exact rational BBP source; high precision special-function diagnostics.
"""
import unittest
from fractions import Fraction as Q
from math import gcd, log, pi, asin
import mpmath as mp
mp.mp.dps=48

T=(Q(4),Q(),Q(),Q(-2),Q(-1),Q(-1),Q(),Q())

def source(n):
    x=sum((w/Q(8*(n-1)+j) for j,w in enumerate(T,1)),Q())
    assert x==Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    return x

def states(end):
    u=Q();data={}
    for n in range(1,end+1):
        u=16*u+source(n);data[n]=u
    return data

def asmp(x):return mp.mpf(x.numerator)/x.denominator

def primitive(x):
    f=x%1
    if f==0:return mp.mpf(0)
    return -mp.im(mp.polylog(2,mp.e**(2j*mp.pi*asmp(f))))/mp.pi

def pairmean(i,j,K,u):
    alpha=(u[j]-u[i])%1
    Qfreq=Q(16**j-16**i,16**K)
    if Qfreq.denominator==1:return mp.mpf(0)
    return (primitive(alpha+Qfreq)-primitive(alpha))/asmp(Qfreq)

def parts(A,K,u):
    out={'future':mp.mpf(0),'cross':mp.mpf(0),'past':mp.mpf(0)}
    for i in range(A,2*A):
        for j in range(i+1,2*A):
            cat='future' if i>=K else 'cross' if j>=K else 'past'
            out[cat]+=pairmean(i,j,K,u)/A**2
    return out

def cross_bound(A):
    return (mp.mpf(512)/225)*(mp.mpf(1)/15+mp.mpf(16)/225*mp.log(16))/A**2

def past_bound(A,t):
    return (t*(t-1)*(1+mp.log(mp.mpf(16)/15))+
            mp.log(16)*t*(t-1)*(t+1)/3)/A**2

class ClausenCut(unittest.TestCase):
    def test_01_exact_original_source(self):
        self.assertEqual(source(1),Q(47,15))
        for n in (2,7,11,13,39):self.assertGreater(source(n),0)
        self.assertEqual(states(2)[2]%1,Q(1076,4095))

    def test_02_exact_future_and_cross_cut_frequencies(self):
        for A in (7,11,13):
            for K in (A,A+1,A+2,2*A):
                for i in range(A,2*A):
                    for j in range(i+1,2*A):
                        q=Q(16**j-16**i,16**K)
                        if i>=K:self.assertEqual(q.denominator,1)
                        if i<K<=j:
                            self.assertEqual(q,Q(16**(j-K))-Q(1,16**(K-i)))

    def test_03_primitive_of_log_kernel(self):
        for x in (Q(1,10),Q(1,6),Q(1,3),Q(2,5)):
            h=Q(1,100000)
            diff=(primitive(x+h)-primitive(x-h))/(2*asmp(h))
            expected=2*mp.log(2*mp.sin(mp.pi*asmp(x)))
            self.assertLess(abs(diff-expected),mp.mpf('1e-7'))
        self.assertEqual(primitive(Q(0)),0)
        self.assertEqual(primitive(Q(1)),0)

    def test_04_cross_short_arc_identity_and_sign(self):
        u=states(26)
        for i,j,K in ((7,9,9),(7,10,9),(9,11,11),(11,13,13)):
            delta=Q(1,16**(K-i))
            alpha=(u[j]-u[i])%1
            q=Q(16**j-16**i,16**K)
            self.assertEqual(q,Q(16**(j-K))-delta)
            direct=(primitive(alpha-delta)-primitive(alpha))/asmp(q)
            self.assertLess(abs(pairmean(i,j,K,u)-direct),mp.mpf('1e-39'))

    def test_05_fresh_actual_source_cross_bound(self):
        for A in (7,11,13):
            u=states(2*A-1)
            for K in (A,A+1,A+2,3*A//2,2*A):
                d=parts(A,K,u)
                self.assertLessEqual(abs(d['cross']),cross_bound(A)+mp.mpf('1e-35'))
                self.assertLessEqual(abs(d['past']),past_bound(A,K-A)+mp.mpf('1e-35'))
                self.assertLess(abs(d['future']),mp.mpf('1e-35'))

    def test_06_zero_pressure_until_epoch_start(self):
        for A in (7,11,13):
            d=parts(A,A,states(2*A-1))
            self.assertEqual(d['past'],0)
            self.assertEqual(d['cross'],0)
            self.assertEqual(d['future'],0)

    def test_07_unforced_source_moment_negative(self):
        for A,t in ((16,4),(25,6)):
            u={n:Q(0) for n in range(A,2*A)}
            d=parts(A,A+t,u)
            actual=sum(d.values())
            leading=-mp.log(16)*t*(t-1)*(t+1)/(3*A*A)
            self.assertLess(actual,0)
            self.assertLess(abs(actual-leading),mp.mpf('0.1'))

    def test_08_gaussian_information_pressure_and_digit_bias(self):
        rho=Q(1,2)
        self.assertAlmostEqual(1/4+asin(float(rho))/(2*pi),1/3,places=14)
        I=2/3*log(4/3)+1/3*log(2/3)
        self.assertGreater(I,.05)
        self.assertLess(log(16)-I,log(16))
        self.assertAlmostEqual(-.5*log(1-float(rho*rho)),-.5*log(.75))

    def test_09_terminating_rational_seed_has_same_eventual_circle_orbit(self):
        u=states(20)
        for K in (1,2,3):
            s=Q(7,16**K)
            for n in range(K,21):
                self.assertEqual((u[n]+16**n*s)%1,u[n]%1)

    def test_10_source_gcd_arithmetic_not_independent(self):
        for i,j,k,l in ((7,9,8,13),(11,14,11,19),(7,12,8,17)):
            q1=16**j-16**i;q2=16**l-16**k
            self.assertEqual(gcd(q1,q2),16**min(i,k)*(16**gcd(j-i,l-k)-1))

    def test_11_cross_screening_uniform_over_nonzero_prefixes(self):
        for A in (7,11):
            u=states(2*A-1)
            K=A+2
            for d in (0,1,15,255):
                cross=past=mp.mpf(0)
                s0=Q(d,16**K)
                for i in range(A,2*A):
                    for j in range(i+1,2*A):
                        Qfreq=Q(16**j-16**i,16**K)
                        beta=(u[j]-u[i]+(16**j-16**i)*s0)%1
                        v=(primitive(beta+Qfreq)-primitive(beta))/asmp(Qfreq)
                        if i<K<=j:cross+=v/A**2
                        if i<j<K:past+=v/A**2
                self.assertLessEqual(abs(cross),cross_bound(A))
                self.assertLessEqual(abs(past),past_bound(A,K-A))

    def test_12_markov_digit_children_reassemble_parent_integral(self):
        A=7;K=8;u=states(2*A-1)
        for i,j in ((7,9),(7,11),(8,10)):
            freq=16**j-16**i
            alpha=(u[j]-u[i])%1
            Qparent=Q(freq,16**K)
            parent=(primitive(alpha+Qparent)-primitive(alpha))/asmp(Qparent)
            Qchild=Q(freq,16**(K+1))
            child=mp.mpf(0)
            for d in range(16):
                beta=alpha+freq*Q(d,16**(K+1))
                child+=(primitive(beta+Qchild)-primitive(beta))/asmp(Qchild)/16
            self.assertLess(abs(parent-child),mp.mpf('1e-38'))

if __name__=='__main__':unittest.main()
