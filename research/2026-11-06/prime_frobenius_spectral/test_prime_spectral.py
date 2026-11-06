"""Exact BBP/Frobenius controls plus scoped floating spectral diagnostics."""
import unittest
from fractions import Fraction as F
from math import gcd,lcm,cos,sin,pi
from prime_certificate import (source,four_poles,frac_mod,primes_upto,
                               principal_residue,run as first_run)
from full_prime import mid_residue,sieve_set_full,run as full_run
from spectral_probe import details,unit_phases,source_phases


def independent_residue(n,p):
    """Different arithmetic route: enumerate all authentic four pole principal parts."""
    s=0
    for j in range(1,n+1):
        for c,den in ((F(4),8*j-7),(F(-1,2),2*j-1),
                      (F(-1),8*j-3),(F(-1,2),4*j-1)):
            if den%p==0:
                assert den%(p*p)!=0
                s=(s+frac_mod(c/F(den//p),p)*pow(16,n-j,p))%p
    return s


def mobius(n):
    p=2;parity=0
    while p*p<=n:
        if n%p==0:
            n//=p;parity^=1
            if n%p==0:return 0
        p+=1
    if n>1:parity^=1
    return -1 if parity else 1


def totient(n):
    a=n;p=2
    while p*p<=n:
        if n%p==0:
            a-=a//p
            while n%p==0:n//=p
        p+=1
    if n>1:a-=a//n
    return a


def ramanujan(d,h):
    return sum(k*mobius(d//k) for k in range(1,gcd(d,h)+1)
               if gcd(d,h)%k==0)

class OriginalPrimeSpectralTests(unittest.TestCase):
    def test_source_four_poles_and_reduced_odd(self):
        U=F(0)
        for j in range(1,559):
            self.assertEqual(source(j),four_poles(j))
            U=16*U+source(j)
            self.assertEqual(U.denominator%2,1)

    def test_old_preregistered_2n_to_8n_holdouts(self):
        r=first_run()
        self.assertEqual(r['total_selected_prime_residue_checks'],1116)
        self.assertEqual(len(r['holdouts']),8)
        self.assertEqual(r['pi_normality'],'OPEN')

    def test_fresh_full_prime_holdouts_and_p19_exception(self):
        r=full_run()
        self.assertEqual(r['fresh_prime_residue_checks'],1847)
        self.assertEqual(r['piecewise_coefficient_counts'],
                         {'-19/6':178,'-65/21':33,'33/10':56,'47/15':64,'7/2':79})
        for v in r['exception19_controls']:
            self.assertEqual(v['denominator_contains_19'],v['n']>=17)
        self.assertEqual(r['pi_base16_normality'],'OPEN')

    def test_independent_pole_enumeration(self):
        for n in (17,38,73,161,433):
            for p in sieve_set_full(n):
                if p<=2*n:r,_=mid_residue(n,p)
                else:r,_,_=principal_residue(n,p)
                self.assertEqual(independent_residue(n,p),r,(n,p))
                self.assertNotEqual(r,0,(n,p))

    def test_lcm_and_small_prime_exception_scope(self):
        L=1;U=F(0)
        for n in range(1,101):
            j=n;f=(2*j-1,4*j-1,8*j-7,8*j-3)
            for p in primes_upto(8*n):
                if p>5:self.assertLessEqual(sum(v%p==0 for v in f),1,(n,p))
            L=lcm(L,f[0]*f[1]*f[2]*f[3]);U=16*U+source(j)
            self.assertEqual(L%U.denominator,0)

    def test_galois_ramanujan_formula(self):
        for d in (15,21,35,45,105,1155):
            self.assertGreaterEqual(totient(d)**2,d)
            for h in (1,2,3,5,7,10):
                exact=ramanujan(d,h)
                numeric=sum(complex(cos(2*pi*h*u/d),sin(2*pi*h*u/d))
                            for u in range(1,d+1) if gcd(u,d)==1)
                self.assertLess(abs(numeric-exact),1e-9)
                self.assertLessEqual(abs(exact),sum(k for k in range(1,h+1) if h%k==0))

    def test_dyadic_nonnegative_martingale_and_product(self):
        for N in (128,256,512):
            xs=source_phases(N)
            for h in (1,2,3):
                energies,gaps=details(unit_phases(xs,h))
                product=1.0
                for g in gaps:
                    self.assertIsNotNone(g)
                    product*=1-g
                self.assertAlmostEqual(product,energies[0],places=10)
                self.assertAlmostEqual(energies[-1],1.0,places=10)
                self.assertEqual(len(gaps),N.bit_length()-1)

if __name__=='__main__':unittest.main()
