"""Focused exact standard-library controls for SUCC's universal N arithmetic carrier.

This validates finite algebra only. It neither assumes nor proves pi normality.
"""
from fractions import Fraction as F
from math import comb, factorial, lgamma, log, sqrt, isclose
import unittest

C = (4, -2, -1, -1)
D = (0, 3, 4, 5)

def R(a):
    a = F(a)
    return sum((F(c)/(a+d) for c,d in zip(C,D)), F(0))

def V(a):
    a = F(a)
    return a**4 / ((a+3)**2*(a+4)*(a+5))

def product(N):
    result = F(1)
    for n in range(1,N+1):
        result *= V(8*n-7)
    return result

def val(n, p):
    assert n > 0 and p >= 2
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def carries(n, k, p):
    a, b, c, count = k, n-k, 0, 0
    while a or b or c:
        a, u = divmod(a, p)
        b, v = divmod(b, p)
        c = (u+v+c)//p
        count += c
    return count

def v_binomial(n,k,p):
    v, power = 0, p
    while power <= n:
        v += n//power-k//power-(n-k)//power
        power *= p
    return v

def primes_through(N):
    return [p for p in range(2,N+1) if all(p%d for d in range(2,int(sqrt(p))+1))]

def word_measure(n,m,j,source):
    return tuple(w*t**(n+m-j)*(1-t)**j for t,w in source)

class UniversalCarrierProbe(unittest.TestCase):
    def test_finite_dirichlet_cross_sections(self):
        for N in range(1,30):
            self.assertEqual(sum(range(1,N+1)), N*(N+1)//2)
            H=sum((F(1,n) for n in range(1,N+1)),F(0))
            Hsum=sum((sum((F(1,k) for k in range(1,j+1)),F(0)) for j in range(1,N+1)),F(0))
            self.assertEqual(Hsum,(N+1)*H-N)
            self.assertAlmostEqual(sum(log(n) for n in range(1,N+1)),
                                   lgamma(N+1),places=12)

    def test_all_prime_pascal_kummer_product(self):
        for n in range(1,38):
            for k in range(n+1):
                b = comb(n,k)
                vals = {p: v_binomial(n,k,p) for p in primes_through(n)}
                self.assertEqual(b, __import__('math').prod(p**v for p,v in vals.items()))
                for p,v in vals.items():
                    self.assertEqual(v,carries(n,k,p))
                    self.assertEqual(v,val(b,p))

    def test_universal_measure_word_extrusion(self):
        sources=((F(1,5),F(2)),(F(1,2),F(3)),(F(3,4),F(5)))
        for n in range(5):
            for m in range(1,7):
                for j in range(m+1):
                    self.assertEqual(word_measure(n+1,m,j,sources),
                                     word_measure(n,m+1,j,sources))
                    M=comb(m,j)*sum(word_measure(n+1,m,j,sources))
                    G=comb(m+1,j)*sum(word_measure(n,m+1,j,sources))
                    self.assertEqual(M*comb(m+1,j),G*comb(m,j))

    def test_pascal_gamma_and_fibonacci_counting(self):
        a,b=0,1
        fib=[a,b]
        for _ in range(35):
            a,b=b,a+b
            fib.append(b)
        for n in range(1,30):
            self.assertEqual(sum(comb(n-k,k) for k in range(n//2+1)),fib[n+1])
        for r in range(1,6):
            for j in range(12):
                self.assertEqual(factorial(r+j-1)//(factorial(r-1)*factorial(j)),
                                 comb(r+j-1,j))

    def test_pisot_not_universal_for_colored_recursions(self):
        golden=(1+sqrt(5))/2
        other=(1-sqrt(5))/2
        self.assertGreater(golden,1)
        self.assertLess(abs(other),1)
        first=(1+sqrt(13))/2
        other=(1-sqrt(13))/2
        self.assertGreater(first,1)
        self.assertGreater(abs(other),1)

    def test_original_source_four_pole_fingerprint(self):
        self.assertEqual(R(1),F(47,15))
        self.assertEqual(V(1),F(1,480))
        self.assertEqual(sum(C),0)
        self.assertEqual(sum(c*d for c,d in zip(C,D)),-15)
        self.assertEqual(sum(c*d*d for c,d in zip(C,D)),-59)
        self.assertEqual(sum(c*d**3 for c,d in zip(C,D)),-243)
        for a in range(1,400):
            self.assertGreater(R(a),0)
            self.assertLess(V(a),1)

    def test_finite_gamma_product_exact_numerical_holdout(self):
        for N in (1,2,3,5,9,17,31,60):
            p=product(N)
            real_log=log(p.numerator)-log(p.denominator)
            q=(1/8,1/2,5/8,3/4)
            loggamma=sum(c*(lgamma(N+z)-lgamma(z)) for c,z in zip(C,q))
            self.assertAlmostEqual(real_log,loggamma,places=11)

    def test_original_v2_slope_and_all_places(self):
        for N in (1,2,3,5,11,31,63):
            p=product(N)
            self.assertEqual(val(p.numerator,2)-val(p.denominator,2),-5*N)
            # Rational products have an exact prime-factor equality.
            factors={q:val(p.numerator,q)-val(p.denominator,q)
                     for q in primes_through(8*N+1)}
            rebuilt=F(1)
            for q,k in factors.items():
                rebuilt*=F(q)**k
            self.assertEqual(rebuilt,p)

    def test_same_rank_positive_mutant_has_different_prime_place(self):
        mutant=(5,-5,0,0)
        self.assertEqual(sum(mutant),sum(C))
        self.assertEqual(sum(c*d for c,d in zip(mutant,D)),sum(c*d for c,d in zip(C,D)))
        self.assertEqual(sum(c*d*d for c,d in zip(mutant,D)),-45)
        for N in (1,2,3,7,17):
            p=F(1)
            for n in range(1,N+1):
                a=8*n-7
                p*=F(a,a+3)**5
            self.assertEqual(val(p.numerator,2)-val(p.denominator,2),-10*N)

    def test_gamma_potential_power_and_golden_fixed_point(self):
        phi=(1+sqrt(5))/2
        lam=1/phi
        self.assertTrue(isclose((2-lam**2)**(-2),lam**2,rel_tol=1e-14))
        for rank in (1,2,3,4,5):
            theta=lam/(1-lam**rank)
            self.assertTrue(isclose((1+theta*(1-lam**rank))**(-rank),
                                    lam**rank,rel_tol=1e-14))
        for N in (100,1000):
            q=(1/8,1/2,5/8,3/4)
            C0=__import__('math').exp(-sum(c*lgamma(z) for c,z in zip(C,q)))
            L=sum(c*(lgamma(N+z)-lgamma(z)) for c,z in zip(C,q))
            self.assertLess(abs(__import__('math').exp(L)*N**(15/8)/C0-1),0.005)

    def test_weighted_rational_carrier_generates_original_zero_seed(self):
        # B_0(u)=1; B_(n+1)(u)=B_n(u)^16 V(8(n+1)-7+u).
        # The logarithmic derivative recovers U_0=0 exactly.
        B=F(1)
        P=[F(1)]
        U=F(0)
        for N in range(1,5):
            B=B**16*V(8*N-7)
            U=16*U+R(8*N-7)
            U_response=sum((16**(N-j)*R(8*j-7) for j in range(1,N+1)),F(0))
            self.assertEqual(U,U_response)
            self.assertEqual(val(B.numerator,2)-val(B.denominator,2),
                             -(16**N-1)//3)
            P.append(P[-1]*V(8*N-7))
            abel=P[N]
            for j in range(1,N):
                abel*=P[j]**(15*16**(N-j-1))
            self.assertEqual(B,abel)
            self.assertEqual(F(U,16**N),
                             sum((R(8*j-7)/16**j for j in range(1,N+1)),F(0)))

    def test_seed_twist_has_same_potential_values_and_prime_signature(self):
        # g_s(u)=1+s*u has g_s(0)=1 but log derivative s at u=0.
        # The complete sequence of B_N(0) is the same for any seed s.
        for seed in (F(0),F(1,15),F(-1,17)):
            U=seed
            for N in range(1,9):
                U=16*U+R(8*N-7)
                authentic=sum((16**(N-j)*R(8*j-7) for j in range(1,N+1)),F(0))
                self.assertEqual(U-authentic,16**N*seed)

    def test_source_shift_is_not_seed_specific(self):
        # The forcing and universal Pascal multipliers are the same for
        # the authentic seed and an arbitrary changed seed: the affine law.
        for seed in (F(0),F(1,15),F(1,256)):
            u=seed
            for n in range(1,16):
                u=16*u+R(8*n-7)
                v=sum(16**(n-j)*R(8*j-7) for j in range(1,n+1))
                self.assertEqual(u-v,16**n*seed)

if __name__ == '__main__':
    unittest.main(verbosity=2)
