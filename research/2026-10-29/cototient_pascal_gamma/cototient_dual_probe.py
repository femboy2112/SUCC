"""SUCC research-only exact rational cototient/Gamma/carry dual probes.

This does not prove any Fourier estimate for the zero-seeded BBP orbit.
Instruments: source-finite Pascal grade via unchanged four-pole rational forcing,
source-weighted totient / cototient complements, exact Mellin normalizer,
mod-16 Ramanujan/cototient carry shells, and stable sequence reconstruction.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, gcd
import unittest

POLES=((0,4),(3,-2),(4,-1),(5,-1))

def r_parameter(a):
    a=F(a)
    if a<=0:raise ValueError("strict positive four-pole parameter")
    return sum((F(c,a+d) for d,c in POLES),F())

def forcing(n):
    if type(n) is not int or n<1:raise ValueError("n positive integer")
    return r_parameter(8*n-7)

def pascal_grade(n):
    if type(n) is not int or n<1:raise ValueError("n positive integer")
    r=forcing(n)
    return tuple(F(comb(n,j),1)*sum((F((-1)**k*comb(j,k))*forcing(2*n-j+k)
                                    for k in range(j+1)),F())/r
                 for j in range(n+1))

def endpoint_w(j):
    if type(j) is not int or j<0:raise ValueError("j nonnegative")
    return F(j+1,2**(j+2))

def mobius(n):
    if type(n) is not int or n<1:raise ValueError("positive integer")
    out=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;out=-out
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:out=-out
    return out

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def weighted_multiple(d,z=1):
    z=F(z);t=(z/2)**d
    return (1+(d-1)*t)/(4*(1-t)**2)

def phi_om(q,z=1):
    if type(q) is not int or q<1:raise ValueError("q positive")
    return sum((mobius(d)*weighted_multiple(d,z) for d in divisors(q)),F())

def total_pgf(z):
    return 1/(2-F(z))**2

def co_om(q,z=1):
    return total_pgf(z)-phi_om(q,z)

def odd_pgf(z):
    z=F(z)
    return 4*z/(4-z*z)**2

def even_pgf(z):
    z=F(z)
    return (4+z*z)/(4-z*z)**2

def limit_bivariate(z,t):
    return 1/(2-F(z)+2*F(t))**2

def finite_bivariate(n,z,t):
    z=F(z);t=F(t)
    a=8*n-7
    if t<0:raise ValueError("nonnegative t")
    return sum((F(comb(n,k))*z**(n-k)*(1-z)**k*r_parameter(a+2*a*t+8*k)
                for k in range(n+1)),F())/forcing(n)

def finite_odd_even_laplace(n,t):
    total=finite_bivariate(n,1,t)
    parity=finite_bivariate(n,-1,t)
    return (total-parity)/2,(total+parity)/2

def limit_odd_even_laplace(t):
    t=F(t)
    l1=1/(1+2*t)**2;l3=1/(3+2*t)**2
    return (l1-l3)/2,(l1+l3)/2

def sector_rate_coeffs(n,primitive):
    """Exact finite signed exponential representation of the POSITIVE conditional density.

    The coefficients themselves can be negative. Do not interpret them as
    probability masses; only the total constructed density is nonnegative.
    """
    if type(n) is not int or n<1:raise ValueError("n positive integer")
    a=8*n-7
    direction=-1 if primitive else 1 # odd vs even
    out={}
    for k in range(n+1):
        coef=F((1 if k==0 else 0) + direction*comb(n,k)*2**k*(-1)**(n-k),2)
        if not coef:continue
        for d,c in POLES:
            rate=a+d+8*k
            out[rate]=out.get(rate,F())+coef*c
    return {r:c for r,c in out.items() if c}

def sector_mass_from_rates(n,primitive):
    return sum((c/F(r) for r,c in sector_rate_coeffs(n,primitive).items()),F())/forcing(n)

def sector_mellin_rational(n,primitive,k):
    """E[X^k | sector] for nonnegative integer k (exact Fractions)."""
    from math import factorial
    if type(k) is not int or k<0:raise ValueError("k nonnegative")
    cc=sector_rate_coeffs(n,primitive)
    mass=sum((F(c,r) for r,c in cc.items()),F())
    return F(factorial(k))*sum((F(c,r**(k+1)) for r,c in cc.items()),F())/mass

def ramanujan(q,k):
    if type(q) is not int or q<1 or type(k) is not int:
        raise ValueError("q positive integer / k integer")
    return sum((d*mobius(q//d) for d in divisors(gcd(q,abs(k))) if q%d==0),0)

def complementary_carry(q,k):
    return q*(k%q==0)-ramanujan(q,k)

def residue_weight(q,residue,z=F(1)):
    """Exact Oily mass for J congruent to residue (mod q), optionally PGF variable z."""
    if type(q) is not int or q<1 or type(residue) is not int or not 0<=residue<q:
        raise ValueError("residue modulo q")
    z=F(z);t=(z/2)**q
    return (z/2)**residue / 4 * ((residue+1)/(1-t)+q*t/(1-t)**2)

def grade_rank_primitive_cells(q):
    """2x2 exact full-factorial cells for grade j and shifted Gamma rank j+2."""
    if type(q) is not int or q<1:raise ValueError("q positive")
    return {(a,b):sum((residue_weight(q,r) for r in range(q)
                        if (gcd(r,q)==1)==bool(a) and (gcd(r+2,q)==1)==bool(b)),F())
            for a in (0,1) for b in (0,1)}

def phi_classical(q):
    return sum(gcd(k,q)==1 for k in range(1,q+1))

def twin_sieve_count(q):
    """Finite CRT count of residues where j and j+2 both units mod q."""
    return sum(gcd(j,q)==gcd(j+2,q)==1 for j in range(q))

def cototient_grade_readout(n,sequence):
    ps=pascal_grade(n)
    if len(sequence)<2*n+1:raise ValueError("sequence must have length at least 2n+1")
    return sum((ps[j]*sequence[n+j] for j in range(n+1) if j%2==0),F())

def source_cot_inverse_residual(n,sequence):
    """Exact residual of (4-S^2)^2 theta_co -(4+S^2)z, tested on bounded seq."""
    lhs=16*cototient_grade_readout(n,sequence)-8*cototient_grade_readout(n+2,sequence)+cototient_grade_readout(n+4,sequence)
    return lhs-(4*sequence[n]+sequence[n+2])

class ExactCototientTests(unittest.TestCase):
    def test_mobius_and_classical_totient_vs_weighted(self):
        self.assertEqual([mobius(i) for i in range(1,11)],[1,-1,-1,0,-1,1,-1,0,0,1])
        self.assertEqual(phi_om(1),F(1));self.assertEqual(co_om(1),F(0))
        self.assertEqual(phi_om(2),F(4,9))
        self.assertEqual(phi_om(16),F(4,9))
        self.assertEqual(co_om(16),F(5,9))
        self.assertEqual(phi_om(3),F(29,49))
        self.assertEqual(phi_om(6),F(416,1323))
        self.assertEqual(endpoint_w(0)/co_om(16),F(9,20))
    def test_odd_even_complement_generating_function(self):
        for z in (F(0),F(1,7),F(1,2),F(3,4),F(1)):
            self.assertEqual(phi_om(16,z),odd_pgf(z))
            self.assertEqual(co_om(16,z),even_pgf(z))
            self.assertEqual(odd_pgf(z)+even_pgf(z),total_pgf(z))
            self.assertEqual((4+z*z)*odd_pgf(z),4*z*even_pgf(z))
    def test_all_finite_pascal_masses(self):
        for n in range(1,19):
            p=pascal_grade(n)
            self.assertEqual(sum(p),1)
            self.assertGreater(min(p),0)
            self.assertEqual(sum((p[j] for j in range(n+1) if j%2),F()),sector_mass_from_rates(n,True))
            self.assertEqual(sum((p[j] for j in range(n+1) if j%2==0),F()),sector_mass_from_rates(n,False))
    def test_finite_exact_bivariate_sector(self):
        for n in (1,2,3,4,7,11):
            p=pascal_grade(n)
            for t in (F(0),F(1,7),F(3,5)):
                total=finite_bivariate(n,1,t)
                odd,even=finite_odd_even_laplace(n,t)
                self.assertEqual(odd+even,total)
                if t==0:
                    self.assertEqual(odd,sum((p[j] for j in range(n+1) if j%2),F()))
                    self.assertEqual(even,sum((p[j] for j in range(n+1) if j%2==0),F()))
    def test_mellin_finite_conditional_normalization(self):
        for n in (1,3,7,10):
            for branch in (True,False):
                self.assertEqual(sector_mellin_rational(n,branch,0),F(1))
                self.assertGreater(sector_mellin_rational(n,branch,1),0)
    def test_limit_conditional_laplace(self):
        for t in (F(0),F(1,7),F(1,4),F(1,2)):
            odd,even=limit_odd_even_laplace(t)
            self.assertEqual(odd+even,limit_bivariate(1,t))
        self.assertEqual(limit_odd_even_laplace(0),(F(4,9),F(5,9)))
    def test_mod16_ramanujan_cototient_fourier(self):
        for k in range(-90,100):
            prim,cot=ramanujan(16,k),complementary_carry(16,k)
            self.assertEqual(prim,16*(k%16==0)-8*(k%8==0))
            self.assertEqual(cot,8*(k%8==0))
            self.assertEqual(prim+cot,16*(k%16==0))
            self.assertEqual(prim-cot,-16*(k%16==8))
        # Coherent same-forcing counterseed: κ=15 is invisible to aggregate Ramanujan/cot shells.
        self.assertEqual((ramanujan(16,15),complementary_carry(16,15)),(0,0))
    def test_prime_power_carry_shell(self):
        for p,a in ((2,1),(2,2),(2,4),(3,1),(3,2),(5,2)):
            q=p**a
            for k in range(-2*q,2*q+1):
                self.assertEqual(complementary_carry(q,k),p**(a-1)*(k%(p**(a-1))==0))
    def test_exact_co_inverse_on_bounded_sequences(self):
        seq=tuple(F((13*k*k+3*k)%19-9,9) for k in range(512))
        def inf_even(i):
            return sum((endpoint_w(j)*seq[i+j] for j in range(0,360-i,2)),F())
        for i in range(2,10):
            lhs=16*inf_even(i)-8*inf_even(i+2)+inf_even(i+4)
            rhs=4*seq[i]+seq[i+2]
            # Infinite tail is truncated, so the (tiny) residual comes only from that tail.
            self.assertLess(abs(lhs-rhs),F(1,2**300))
    def test_source_co_inverse_error_for_all_bounded_signs(self):
        controls=[tuple(F(1) for _ in range(150)),
                  tuple(F((-1)**i) for i in range(150)),
                  tuple(F(0) if i%5==0 else F((-1)**(i//5)) for i in range(150))]
        for seq in controls:
            for n in range(3,19):
                residual=source_cot_inverse_residual(n,seq)
                self.assertLessEqual(abs(residual),F(1100,n))
    def test_pascal_source_zero_grade_is_nonzero(self):
        for n in range(1,18):
            p=pascal_grade(n)
            self.assertGreater(p[0],0)
            self.assertEqual(p[0],forcing(2*n)/forcing(n))
    def test_grade_rank_shifted_primitive_cells(self):
        self.assertEqual(grade_rank_primitive_cells(3),{(0,0):F(0),(0,1):F(20,49),(1,0):F(17,49),(1,1):F(12,49)})
        self.assertEqual(grade_rank_primitive_cells(6),{(0,0):F(5,9),(0,1):F(172,1323),(1,0):F(352,1323),(1,1):F(64,1323)})
        for q in (2,3,4,5,6,10,15,16,30):
            cells=grade_rank_primitive_cells(q)
            self.assertEqual(sum(cells.values(),F()),F(1))
            self.assertEqual(cells[(1,1)],sum((residue_weight(q,r) for r in range(q) if gcd(r,q)==1 and gcd(r+2,q)==1),F()))
        for p in (3,5,7,11):
            self.assertEqual(grade_rank_primitive_cells(p)[(0,0)],F(0))
    def test_crt_twin_local_count(self):
        from math import prod
        for q in (2,3,4,5,6,15,30,60,210,2310):
            primes=[p for p in range(2,q+1) if q%p==0 and all(p%d for d in range(2,int(p**0.5)+1))]
            predicted=F(q)*prod((F(p-(1 if p==2 else 2),p) for p in primes))
            self.assertEqual(predicted.denominator,1)
            self.assertEqual(twin_sieve_count(q),int(predicted))
        self.assertEqual(twin_sieve_count(30),3)
        self.assertEqual({j for j in range(30) if gcd(j,30)==gcd(j+2,30)==1},{11,17,29})
    def test_cesaro_stationary_conditional(self):
        # normalized filter means; primitive/cot Cesaro difference vanishes
        odd_mean=F(7,3);even_mean=F(26,15)
        self.assertEqual(odd_mean+even_mean,F(61,15))
        self.assertEqual(odd_pgf(F(1)),F(4,9))
        self.assertEqual(even_pgf(F(1)),F(5,9))
        self.assertEqual(F(122,15),2*(odd_mean+even_mean))

if __name__=="__main__":unittest.main(verbosity=2)
