"""Source-preserving independent checks for SUCC Fibonacci/observer research.

No third-party dependencies. This checks exact finite identities and numerical
asymptotic diagnostics; the accompanying paper carries the infinite proofs.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction as F
import math
import unittest

S = ((0, 1), (1, 1))
B = ((1, 1), (1, 2))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def qform(u, v):
    return u*u + u*v - v*v


def apply(m, x):
    return (m[0][0]*x[0] + m[0][1]*x[1],
            m[1][0]*x[0] + m[1][1]*x[1])


def fib(n):
    x,y=0,1
    for _ in range(n): x,y=y,x+y
    return x


def R(a):
    a=F(a)
    return (15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))


def EX(a):
    a=F(a)
    p=15*a*a+121*a+240
    return sum((1/(a+s) for s in (0,3,4,5)),F(0))-(30*a+121)/p


def J(a,b, fake=False):
    if fake:
        return F(b-a)*(F(2,a)-F(2,b))
    return F(b-a)*(EX(a)-EX(b))


def debruijn(k,n):
    """Return a cyclic de Bruijn word B(k,n), length k**n."""
    a=[0]*(k*n)
    out=[]
    def db(t,p):
        if t>n:
            if n%p==0: out.extend(a[1:p+1])
        else:
            a[t]=a[t-p];db(t+1,p)
            for j in range(a[t-p]+1,k):
                a[t]=j;db(t+1,t)
    db(1,1)
    return out


class FibonacciClock(unittest.TestCase):
    def test_integral_lorentz_conjugacy(self):
        self.assertEqual(matmul(S,S),B)
        for u in range(-12,13):
            for v in range(-12,13):
                self.assertEqual(qform(*apply(B,(u,v))),qform(u,v))
                self.assertEqual(qform(*apply(S,(u,v))),-qform(u,v))

    def test_fibonacci_matrix(self):
        p=((1,0),(0,1))
        for n in range(1,19):
            p=matmul(p,B)
            self.assertEqual(p,((fib(2*n-1),fib(2*n)),
                                (fib(2*n),fib(2*n+1))))

    def test_four_pole_rational_source(self):
        for a in range(1,150):
            naive=F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)
            self.assertEqual(R(a),naive)
            self.assertGreater(R(a),0)
            self.assertGreater(EX(a),0)
            self.assertLess(EX(a)*a,2)
            if a>1:
                self.assertGreater(EX(a-1),EX(a))

    def test_jeffreys_convergence_and_first_jet(self):
        with localcontext() as ctx:
            ctx.prec=65
            root5=Decimal(5).sqrt()
            phi=(Decimal(1)+root5)/2
            q=(Decimal(1)/phi)**2
            limit_coeff=-Decimal(59)*(root5-1)/Decimal(48)
            last_error=None
            for k in range(5,14):
                a=8*fib(2*k)-7
                b=8*fib(2*k+2)-7
                original=J(a,b)
                fake=J(a,b,True)
                self.assertGreater(original,F(0))
                # source correction is negative and decays like q^k
                self.assertLess(original,fake)
                ratio=(Decimal((original-fake).numerator)/
                       Decimal((original-fake).denominator))/(q**k)
                err=abs(ratio-limit_coeff)
                if last_error is not None:
                    self.assertLess(err,last_error)
                last_error=err
            self.assertLess(last_error,Decimal('0.0001'))
            approx=Decimal(J(8*fib(26)-7,8*fib(28)-7).numerator)/Decimal(J(8*fib(26)-7,8*fib(28)-7).denominator)
            self.assertLess(abs(approx-2),Decimal('0.001'))

    def test_fibonacci_harmonic_offset(self):
        with localcontext() as ctx:
            ctx.prec=55
            phi=(Decimal(1)+Decimal(5).sqrt())/2
            eta=2*phi.ln()
            gamma=Decimal('0.57721566490153286060651209008240243104215933593992')
            target=gamma-Decimal(5).ln()/2
            H=F(0)
            old=0
            errs=[]
            for k in range(2,8):
                N=fib(2*k)
                for j in range(old+1,N+1):H+=F(1,j)
                old=N
                obs=Decimal(H.numerator)/Decimal(H.denominator)-k*eta
                errs.append(abs(obs-target))
            self.assertLess(errs[-1],errs[0])
            self.assertLess(errs[-1],Decimal('.002'))


class NormalObserver(unittest.TestCase):
    def test_debruijn_all_short_circular_blocks_uniform(self):
        for b,m in ((2,6),(4,4)):
            word=debruijn(b,m)
            self.assertEqual(len(word),b**m)
            for ell in range(1,m+1):
                counts={}
                for t in range(len(word)):
                    key=tuple(word[(t+i)%len(word)] for i in range(ell))
                    counts[key]=counts.get(key,0)+1
                self.assertEqual(len(counts),b**ell)
                self.assertEqual(set(counts.values()),{b**(m-ell)})

    def test_wrong_iid_likelihood_exact_rate(self):
        word=debruijn(2,6)
        n=len(word)
        with localcontext() as ctx:
            ctx.prec=40
            logbf=sum(((Decimal(2)* (Decimal(3)/4 if x==0 else Decimal(1)/4)).ln() for x in word),Decimal(0))
            expected=(Decimal(n)/2)*(Decimal(3)/4).ln()
            self.assertLess(abs(logbf-expected),Decimal('1e-35'))
            self.assertLess(logbf,0)

    def test_wrong_one_step_markov_likelihood(self):
        word=debruijn(2,6)
        with localcontext() as ctx:
            ctx.prec=40
            logbf=Decimal(0)
            for t,x in enumerate(word):
                prior=word[(t-1)%len(word)]
                prob=(Decimal(3)/4 if x==0 else Decimal(1)/4) if prior==0 else Decimal(1)/2
                logbf+=(2*prob).ln()
            expected=Decimal(len(word))/4*(Decimal(3)/4).ln()
            self.assertLess(abs(logbf-expected),Decimal('1e-35'))
            self.assertLess(logbf,0)

    def test_no_universal_finite_prefix_horizon(self):
        # A biased beginning of arbitrarily large length is compatible
        # with normality once followed by any normal tail; numerical case
        # only illustrates the initial likelihood advantage.
        for m in (10,100,1000):
            with localcontext() as ctx:
                ctx.prec=30
                logbf=Decimal(m)*(Decimal(3)/2).ln()
                self.assertGreater(logbf,Decimal(0))

    def test_computable_sequence_has_arbitrarily_long_zero_runs(self):
        # Base-2 Champernowne concatenates binary integers: 2**k contributes
        # the literal word '1' + '0'*k, proving arbitrarily long zero runs.
        digits=''.join(format(i,'b') for i in range(1,513))
        for k in range(1,10):
            self.assertIn('1'+'0'*k,digits)


if __name__=='__main__':
    unittest.main(verbosity=2)
