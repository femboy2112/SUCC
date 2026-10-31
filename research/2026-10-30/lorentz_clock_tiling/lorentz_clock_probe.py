"""Research-only Lorentz-like normalized observer clocks for original four-pole BBP.

No physical Lorentz symmetry or pi-normality conclusion. All finite tests use
fractions; root-eigenvalue controls use integer matrix identities.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb, gcd
import unittest


def r(a):
    a = F(a)
    if a <= 0:
        raise ValueError("source Laplace parameter must be positive")
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)


def r_fake(a):
    a = F(a)
    if a <= 0:
        raise ValueError("fake source Laplace parameter must be positive")
    return F(15)/a**2


@lru_cache(None)
def per_word(n, m, successes, fake=False):
    if not (isinstance(n,int) and n>=1 and isinstance(m,int) and m>=0
            and isinstance(successes,int) and 0<=successes<=m):
        raise ValueError("invalid exact native Pascal indices")
    a=8*n-7
    R=r_fake if fake else r
    return sum(((-1)**k*comb(successes,k)*R(a+8*(m-successes+k))
                for k in range(successes+1)),F())/R(a)


def finite_split(n, m1, m2, fake=False):
    if not (0 <= m1 and 0 <= m2 and m1+m2==n):
        raise ValueError("one total native observation budget must be preserved")
    return tuple(tuple(F(comb(m1,j)*comb(m2,k))*per_word(n,n,j+k,fake)
                       for k in range(m2+1)) for j in range(m1+1))


def finite_total(n, fake=False):
    return tuple(comb(n,s)*per_word(n,n,s,fake) for s in range(n+1))


def w(s):
    if not isinstance(s,int) or s<0:raise ValueError("nonnegative total grade")
    return F(s+1,2**(s+2))


def limiting_joint(j,k,p):
    j=int(j);k=int(k);p=F(p)
    if j<0 or k<0 or not 0<=p<=1:
        raise ValueError("indices and observation share")
    return w(j+k)*comb(j+k,j)*p**j*(1-p)**k


def limiting_pgf(z,w_,p):
    p,z,w_=F(p),F(z),F(w_)
    if not 0<=p<=1:raise ValueError("share must lie in unit interval")
    return 1/(2-p*z-(1-p)*w_)**2


def boost_share(p,t):
    """Projectivized 1+1 Lorentz boost: t=tanh(rapidity), exact rational."""
    p,t=F(p),F(t)
    if not (0<=p<=1 and -1<t<1):raise ValueError("invalid share/velocity")
    v=2*p-1
    return p*(1+t)/(1+v*t)


def velocity_sum(t,u):
    t,u=F(t),F(u)
    if not -1<t<1 or not -1<u<1:raise ValueError("subunit boost")
    return (t+u)/(1+t*u)


def lorentz_norm(v):
    """Integral signature-(1,1) form retained by the golden SL_2(Z) matrix."""
    a,b=map(F,v)
    return 2*(b*b-a*a-a*b)


def fibonacci_boost(v):
    a,b=map(F,v)
    return (a+b,a+2*b)


def theoretical_clock_jet(z,w_,p):
    """Coeff. n^-1 for m1+m2=n, m1/n=p exactly (rational fixed p)."""
    z,w_,p=F(z),F(w_),F(p)
    a,b=1-z,1-w_
    C=p*a+(1-p)*b
    D=p*a*(1-a)+(1-p)*b*(1-b)
    den=1+C
    return -F(151,120)*C/den**3+3*D/den**4


def theoretical_jet_difference_fake(z,w_,p):
    C=F(p)*(1-F(z))+(1-F(p))*(1-F(w_))
    return F(59,120)*C/(1+C)**3


def exact_split_pgf(n,m1,m2,z,w_,fake=False):
    z,w_=F(z),F(w_)
    P=finite_split(n,m1,m2,fake)
    return sum((mass*z**j*w_**k for j,row in enumerate(P) for k,mass in enumerate(row)),F())


def tv_split_to_limit(n,m1,m2):
    """Exact TV, including the whole infinite negative-binomial tail."""
    if m1+m2!=n:raise ValueError("split")
    p=F(m1,n)
    finite=finite_split(n,m1,m2)
    total=F()
    for j in range(n+1):
        for k in range(n-j+1):
            q=finite[j][k] if j<=m1 and k<=m2 else F()
            total+=abs(q-limiting_joint(j,k,p))
    tail=F(n+3,2**(n+2))
    return (total+tail)/2


def parity_covariance(p):
    p=F(p)
    return (F(1,9)-1/((1+2*p)**2*(3-2*p)**2))/4


class LorentzClockTests(unittest.TestCase):
    def test_authentic_source(self):
        self.assertEqual(r(1), F(47,15))
        self.assertEqual(r(9), F(4,9)-F(2,12)-F(1,13)-F(1,14))
        self.assertNotEqual(r(9),r_fake(9))

    def test_finite_source_probability(self):
        for n in range(1,14):
            for m1 in {0,n,n//2}:
                P=finite_split(n,m1,n-m1)
                self.assertEqual(sum(map(sum,P)),1)
                self.assertTrue(all(x>0 for row in P for x in row))

    def test_vandermonde_total_and_hypergeometric(self):
        for n in (3,6,10):
            m1=n//2;m2=n-m1;P=finite_split(n,m1,m2)
            total=finite_total(n)
            for s in range(n+1):
                self.assertEqual(sum((P[j][s-j] for j in range(m1+1)
                                      if 0<=s-j<=m2),F()),total[s])
                for j in range(m1+1):
                    k=s-j
                    if 0<=k<=m2:
                        self.assertEqual(P[j][k]/total[s],F(comb(m1,j)*comb(m2,k),comb(n,s)))

    def test_lorentz_velocity_composition(self):
        for p in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
            for a,b in ((F(1,3),F(-1,4)),(F(3,5),F(1,7)),(F(0),F(0))):
                self.assertEqual(boost_share(boost_share(p,a),b),boost_share(p,velocity_sum(a,b)))
                self.assertEqual(boost_share(boost_share(p,a),-a),p)

    def test_total_gold_clock_is_invariant(self):
        for p in (F(0),F(1,3),F(1,2),F(3,4),F(1)):
            for v in (F(0),F(1,3),F(-1,2)):
                pp=boost_share(p,v)
                for z in (F(0),F(1,5),F(2,3),F(1)):
                    self.assertEqual(limiting_pgf(z,z,pp),1/(2-z)**2)

    def test_split_totient_parity_is_not_invariant(self):
        self.assertEqual(parity_covariance(F(1,2)), F(7,576))
        self.assertEqual(parity_covariance(F(0)),0)
        self.assertEqual(parity_covariance(F(1)),0)
        self.assertLess(parity_covariance(F(1,3)),parity_covariance(F(1,2)))

    def test_exact_negative_binomial_finite_bound(self):
        for n in (3,4,5,6,8,10,12,16):
            for m1 in {0,n,n//2}:
                val=tv_split_to_limit(n,m1,n-m1)
                self.assertLessEqual(val,min(F(1),F(28,n)))

    def test_golden_lorentz_integral_form(self):
        self.assertEqual(lorentz_norm((1,2)),lorentz_norm(fibonacci_boost((1,2))))
        for a in range(-6,7):
            for b in range(-6,7):
                self.assertEqual(lorentz_norm((a,b)),lorentz_norm(fibonacci_boost((a,b))))
        self.assertEqual(fibonacci_boost((1,0)),(F(1),F(1)))
        self.assertEqual(fibonacci_boost((0,1)),(F(1),F(2)))

    def test_cannot_claim_fourier_lorentz_invariance(self):
        self.assertEqual(limiting_pgf(-1,1,F(1,2)), F(1,4))
        self.assertEqual(limiting_pgf(-1,-1,F(1,2)), F(1,9))
        self.assertNotEqual(limiting_pgf(-1,1,F(1,2)),limiting_pgf(-1,-1,F(1,2)))

    def test_nontrivial_source_memory(self):
        for n in (2,4,8,14):
            a=8*n-7
            v=r(a+16)/r(a)-(r(a+8)/r(a))**2
            self.assertGreater(v,0)

    def test_clock_first_source_jet(self):
        self.assertEqual(theoretical_jet_difference_fake(1,1,F(1,2)),0)
        self.assertEqual(theoretical_clock_jet(1,1,F(1,2)),0)
        for z,w_ in ((F(0),F(1)),(F(1,3),F(1,2))):
            p=F(1,2)
            self.assertNotEqual(theoretical_jet_difference_fake(z,w_,p),0)
            for n in (40,80):
                val=exact_split_pgf(n,n//2,n-n//2,z,w_)
                approx=limiting_pgf(z,w_,p)+theoretical_clock_jet(z,w_,p)/n
                self.assertLess(abs(val-approx),F(1,8*n*n))

    def test_no_selected_pi_cancellation_from_clock(self):
        for p in (F(0),F(1,2),F(4,5),F(1)):
            self.assertEqual(limiting_pgf(1,1,p),1)
        self.assertNotEqual(parity_covariance(F(1,2)),0)

if __name__=='__main__':unittest.main(verbosity=2)
