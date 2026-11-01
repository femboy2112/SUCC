"""Separate, exact-oracle routes; deliberately no imports from arctan_chiral.py."""
from fractions import Fraction
from math import gcd


def four_poles(n):
    n=Fraction(n)
    return sum((Fraction(c,1)/(8*n-k) for c,k in ((4,7),(-2,4),(-1,3),(-1,2))),Fraction(0))


def direct_unwrapped(n):
    u=Fraction(0)
    for j in range(1,n+1):
        u=16*u+four_poles(j)
    return u


def finite_fourier_witness(k,l):
    """Exact 8-coordinate cyclotomic ring witness, direct parity source formula."""
    ans=[0]*8
    for n in range(16):
        r=(-n+2*(n%2))%16
        exponent=(l*n-k*r)%16
        ans[exponent%8]+=(-1 if exponent>=8 else 1)
    return tuple(ans)


def source_mod_via_horner(n,modulus):
    n%=modulus
    A=(n*(120*n-89)+16)%modulus
    # Independent multiply exact factors, not the four rational term evaluation.
    den=1
    for mul,off in ((2,-1),(4,-1),(8,-7),(8,-3)):
        den=(den*(mul*n+off))%modulus
    return A*pow(den,-1,modulus)%modulus


def machin_gaussian():
    # Independent integer-Gaussian arithmetic, not complex floating point.
    a,b=5,1
    for _ in range(3):a,b=a*5-b,a+b*5
    return (a,b), (2*(239-1),2*(239+1))


def machin_interval(k):
    def alt(inv):
        s=Fraction(0)
        for j in range(k): s+=Fraction((-1)**j,(2*j+1)*inv**(2*j+1))
        err=Fraction(1,(2*k+1)*inv**(2*k+1))
        return (s,s+err) if k%2==0 else (s-err,s)
    a,b=alt(5);c,d=alt(239)
    return 16*a-4*d,16*b-4*c


def cyclic_coset_DFT_square(index,modulus):
    """Group-character orthogonality: Q^-1 sum_k zeta^{k(x+y)} = delta_(x+y,0)."""
    return (-index)%modulus


def finite_chiral_orbit(q, steps):
    """Independent modular odd-torsion state and dual in Z/(2Q), with source ints."""
    original=0
    chiral=q
    for n in range(1,steps+1):
        r=four_poles(n)
        assert q%r.denominator==0
        br=(r.numerator*(q//r.denominator))%q
        original=(16*original+2*br)%(2*q)
        chiral=(16*chiral+q-2*br)%(2*q)
        assert original%2==0 and chiral%2==1
        assert chiral==(q-original)%(2*q)
    return original,chiral
