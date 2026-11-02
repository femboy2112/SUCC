#!/usr/bin/env python3
"""Exact causal source-prefix / moment-null / rational quadrature controls.

Pure standard-library Fraction tests. These do not prove normality or
perform source-independent inference. Derivations in PROOFS.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, comb
import unittest

A, B = F(1,4), F(1,2)

def source(n):
    assert n >= 1
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def add(P,Q):
    R=[F(0)]*max(len(P),len(Q))
    for i,c in enumerate(P): R[i]+=c
    for i,c in enumerate(Q): R[i]+=c
    return tuple(R)

def mul(P,Q):
    R=[F(0)]*(len(P)+len(Q)-1)
    for i,c in enumerate(P):
        for j,d in enumerate(Q):R[i+j]+=c*d
    return tuple(R)

def derivative(P,order):
    for _ in range(order):
        P=tuple(P[i]*i for i in range(1,len(P))) or (F(0),)
    return P

def integrate(P,lo=A,hi=B):
    return sum((c*(hi**(j+1)-lo**(j+1))/(j+1) for j,c in enumerate(P)),F(0))

def g_poly(M):
    P=(F(1),)
    for _ in range(M+1):
        P=mul(P,(-A,F(1)))
        P=mul(P,(B,-F(1)))
    return P

def echo_profile(M):
    D=derivative(g_poly(M),M)
    bound=sum(abs(c) for c in D) # |x|<=1 => sup |D(x)| <= bound
    assert bound>0
    eps=F(1,1000)/bound
    return D,eps,bound

def echo_delta_moment(M,epsilon,n):
    D,_epsilon,_B=echo_profile(M)
    # integral x^(n-1) D(x) dx on [1/4,1/2]
    return epsilon*integrate((F(0),)*(n-1)+D)

def delta_step(n,M,eps):
    return source(n)+echo_delta_moment(M,eps,n)

def state(n,rfunc):
    u=F(0)
    for k in range(1,n+1):u=16*u+rfunc(k)
    return u

# Strictly positive rational atomic measure, found by a separate LP then
# verified exactly; each coefficient is a positive rational, not a float.
ATOMS_M4=(
 (F(1,80),F(93606744115,32218183998)),
 (F(5,16),F(992400341,7594857270)),
 (F(1,2),F(1011071983,11951906967)),
 (F(63,80),F(23100710,1823277183)),
)

def r_atomic(n,atoms=ATOMS_M4):
    return sum((w*x**(n-1) for x,w in atoms),F(0))

def alpha_atomic(atoms=ATOMS_M4):
    return sum((w/(16-x) for x,w in atoms),F(0))

class CausalEchoTests(unittest.TestCase):
    def test_original_source_poles_and_finite_recurrence(self):
        self.assertEqual(source(1),F(47,15))
        for n in range(1,30):
            a=8*n-7
            self.assertEqual(source(n),F(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5)))
        self.assertEqual(state(0,source),0)

    def test_echo_null_moments_exact_every_finite_prefix(self):
        for M in (1,2,3,4,5,6):
            D,eps,bound=echo_profile(M)
            self.assertEqual(len(D)-1,M+2)
            self.assertGreater(eps,0)
            for n in range(1,M+1):
                self.assertEqual(echo_delta_moment(M,eps,n),0,(M,n))
                self.assertEqual(delta_step(n,M,eps),source(n))
                self.assertEqual(state(n,lambda j:delta_step(j,M,eps)),state(n,source))
            self.assertNotEqual(echo_delta_moment(M,eps,M+1),0)

    def test_echo_exponentially_decays_and_95pct_density(self):
        for M in (1,2,3,4,5,6):
            D,eps,B1=echo_profile(M)
            # Derived pointwise analytic lower f(x) > 1/32 on [1/4,1/2].
            self.assertLess(eps*B1,F(1,640))
            for n in range(1,60):
                err=abs(echo_delta_moment(M,eps,n))
                self.assertLessEqual(err,eps*B1*(B-A)*B**(n-1))
                mu=delta_step(n,M,eps)
                self.assertGreater(mu,0)
                self.assertGreaterEqual(mu,F(19,20)*source(n))
                self.assertLessEqual(mu,F(21,20)*source(n))

    def test_echo_all_integer_source_jets_95pct(self):
        for M in (1,2,3,4,5):
            _,eps,_=echo_profile(M)
            rnew=lambda n:delta_step(n,M,eps)
            for n in range(1,8):
                for d in range(0,9):
                    true=sum(((-1)**j*comb(d,j)*source(n+j) for j in range(d+1)),F())
                    altered=sum(((-1)**j*comb(d,j)*rnew(n+j) for j in range(d+1)),F())
                    self.assertGreater(true,0)
                    self.assertGreater(altered,0)
                    self.assertLessEqual(F(19,20)*true,altered)
                    self.assertLessEqual(altered,F(21,20)*true)

    def test_echo_completed_boundary_nonzero(self):
        for M in (1,2,3,4,5):
            D,eps,_=echo_profile(M)
            # Since first M perturbed moments vanish, first nonzero
            # is n=M+1 with sign (-1)^M by integration by parts.
            first=echo_delta_moment(M,eps,M+1)
            self.assertGreater((-1)**M*first,0)
            # Monotone series with support x<=1/2 has geometric tail.
            s=sum((echo_delta_moment(M,eps,n)/16**n for n in range(M+1,M+21)),F())
            self.assertGreater((-1)**M*s,0)

    def test_exact_rational_atomic_quadrature_M4(self):
        for x,w in ATOMS_M4:
            self.assertTrue(F(0)<x<F(1))
            self.assertGreater(w,0)
        for n in range(1,5):
            self.assertEqual(r_atomic(n),source(n))
            self.assertEqual(state(n,r_atomic),state(n,source))
        self.assertNotEqual(r_atomic(5),source(5))
        q=alpha_atomic()
        self.assertTrue(F(0)<q<F(1))
        self.assertEqual(q,F(4062342947075618,20689342837729335))
        self.assertGreater(q.denominator,1)
        # Every eventual phase with h=den(q) is coherent since
        # b^n hq is integer and atomic positive tail tends zero.
        self.assertEqual((q*q.denominator).denominator,1)
        for n in (5,10,20,30):
            t=sum((w*x**n/(16-x) for x,w in ATOMS_M4),F())
            self.assertGreater(t,0)
            self.assertLess(t,F(63,80)**n)
            self.assertEqual(state(n,r_atomic),16**n*q-t)

    def test_positive_source_alpha_prefix_bound(self):
        # For any measures with same first M moments and mass r1,
        # |alpha1-alpha2| <= 2*r1/(15*16^M).
        q=alpha_atomic()
        for M in range(1,5):
            # Use a strict elementary enclosure of pi via the
            # alternating Machin formula, no decimal pi digits.
            def atan_bounds(n,N=22):
                val=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(N)),F())
                t=F(1,(2*N+1)*n**(2*N+1))
                return (val,val+t) if N%2==0 else (val-t,val)
            l5,h5=atan_bounds(5)
            l239,h239=atan_bounds(239)
            pi_low=16*l5-4*h239
            pi_high=16*h5-4*l239
            alpha_low,alpha_high=pi_low/16,pi_high/16
            bound=2*source(1)/(15*16**M)
            self.assertLess(max(abs(q-alpha_low),abs(q-alpha_high)),bound)

    def test_seed_v_source_past_data_observer(self):
        M=4
        _,eps,_=echo_profile(M)
        R=lambda n:delta_step(n,M,eps)
        for n in range(M+1):
            self.assertEqual(state(n,R),state(n,source))
        self.assertNotEqual(state(M+1,R),state(M+1,source))
        self.assertEqual(state(M+1,R)-state(M+1,source),echo_delta_moment(M,eps,M+1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
