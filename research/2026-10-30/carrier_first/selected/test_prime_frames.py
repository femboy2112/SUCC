from fractions import Fraction as Q
from math import factorial
import unittest

from prime_frames import (source, selected, weights, error_bound, moving_order,
    reconstruction_order, source_denominator, factor, prime_vector,
    frame_interval, log_integer_interval, reconstruct, primary_part)


class PrimeFrameTests(unittest.TestCase):
    def test_stencil_exact_moments(self):
        for m in range(1, 13):
            for degree in range(2*m+1):
                obs = sum((w*(Q(j,2*m)**degree-Q(-j,2*m)**degree)
                           for j,w in enumerate(weights(m),1)),Q())
                self.assertEqual(obs, int(degree==1))

    def test_first_omitted_monomial_signed(self):
        for m in range(1, 16):
            obs=sum((w*2*Q(j,2*m)**(2*m+1)
                     for j,w in enumerate(weights(m),1)),Q())
            self.assertEqual(obs,(-1)**(m+1)*Q(factorial(m), (2*m)**m)**2)

    def test_stencil_variation_bound(self):
        for m in range(1, 80):
            self.assertLessEqual(2*sum(abs(w) for w in weights(m)),
                                 4*m*sum((Q(1,j) for j in range(1,m+1)),Q()))

    def test_factorial_elementary_exponential_bound(self):
        for m in range(1, 301):
            self.assertLessEqual(Q(factorial(m),m**m)**2,Q(1,2**(m-1)))

    def test_moving_orders_and_summable_budget(self):
        for n in list(range(1,31))+[53,97,101]:
            m=moving_order(n)
            e=error_bound(n,m)
            self.assertLess(e,Q(1,15*(2*m+1)*(n+1)**2))
            self.assertLess(e,Q(1,120*n**3))

    def test_authentic_source_and_unrolled_boundary(self):
        for n in range(0,81):
            q=sum((16**(n-k)*source(k) for k in range(1,n+1)),Q())
            self.assertEqual(selected(n),q)
            self.assertEqual((source_denominator(n)*q).denominator,1)

    def test_integer_log_certificates(self):
        for a in [1,2,3,7,19,239,997,65537]:
            lo,hi=log_integer_interval(a,128,64)
            self.assertLessEqual(lo,hi)
            lo2,hi2=log_integer_interval(a*a,128,64)
            self.assertLessEqual(2*lo,hi2)
            self.assertLessEqual(lo2,2*hi)

    def test_raw_prime_factorization_routes(self):
        for a in range(1,200):
            q=1
            for p,e in factor(a): q*=p**e
            self.assertEqual(q,a)
        # Exact multiplicative source ratio before applying logarithms.
        for n,m,j in [(1,2,1),(2,3,2),(3,2,2)]:
            from math import prod
            u=Q(j,2*m)
            v=Q(1)
            f={}
            for k in range(1,n+1):
                a=8*k-7
                ratio=((a+u)/(a-u))**4*((a+3-u)/(a+3+u))**2
                ratio*=((a+4-u)/(a+4+u))*((a+5-u)/(a+5+u))
                v*=ratio**(16**(n-k))
                for c,d in zip((4,-2,-1,-1),(0,3,4,5)):
                    for sign in (-1,1):
                        for p,e in factor(2*m*(a+d)+sign*j):
                            f[p]=f.get(p,0)+sign*c*16**(n-k)*e
            r=Q(prod(p**e for p,e in f.items() if e>0),
                prod(p**(-e) for p,e in f.items() if e<0))
            self.assertEqual(r,v)

    def test_source_signed_frame_bound_discovery(self):
        for n,m in [(1,1),(2,2),(3,3),(5,4),(8,6)]:
            lo,hi=frame_interval(n,m)
            q=selected(n)
            a,b=(q-hi,q-lo) if m%2==0 else (lo-q,hi-q)
            self.assertGreater(a,0)
            self.assertLess(b,error_bound(n,m))

    def test_source_signed_frame_bound_holdouts(self):
        for n,m in [(4,5),(7,7),(11,10),(17,13)]:
            lo,hi=frame_interval(n,m,256,128)
            q=selected(n)
            a,b=(q-hi,q-lo) if m%2==0 else (lo-q,hi-q)
            self.assertGreater(a,0)
            self.assertLess(b,error_bound(n,m))

    def test_exact_rational_reconstruction(self):
        for n in (1,2,3,5):
            m=reconstruction_order(n)
            self.assertLess(error_bound(n,m),Q(1,4*source_denominator(n)))
            self.assertEqual(reconstruct(n),selected(n))

    def test_all_primary_factors_and_cancelled_conductors(self):
        for n in (1,2,3,17,31,73):
            q=selected(n)
            total=sum((primary_part(q,p) for p,e in factor(q.denominator)),Q())
            self.assertEqual((q-total).denominator,1)
        self.assertTrue(all(primary_part(selected(n),19)==0 for n in range(10,17)))
        self.assertEqual(primary_part(selected(17),19),Q(8,19))
        self.assertEqual(primary_part(selected(274),73),0)

    def test_rational_alias_and_radix_239_obstruction(self):
        for n in range(1,20):
            for s in (Q(1),Q(1,16),Q(7,19)):
                self.assertEqual(selected(n,s)-selected(n),16**n*s)
        self.assertEqual(16**2-16-1,239)
        self.assertEqual(44231**2-44231-1,57121*34249)
        d=15*source(1)+source(2)
        self.assertEqual(d,Q(38599,819))
        self.assertEqual((d.numerator*pow(d.denominator,-1,239))%239,198)


if __name__=='__main__': unittest.main()
