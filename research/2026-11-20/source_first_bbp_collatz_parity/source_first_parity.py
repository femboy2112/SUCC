"""Source-first, finite signed BBP->Collatz observations.

Uses the literal original four signed BBP poles, zero seed and rigorous
rational tail bound. The prime-square swap is a *counterfactual* experiment,
not the unmodified pi orbit. No R0, normality or positive-Collatz theorem.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

POLES = (4, -2, -1, -1)


def forcing(j: int) -> F:
    if type(j) is not int or j < 1:
        raise ValueError("BBP index must be positive integer")
    return F(4, 8*j-7)-F(2, 8*j-4)-F(1, 8*j-3)-F(1, 8*j-2)


_PREFIX = [F(0)]


def bbp_partial(m: int) -> F:
    """Iterative exact source prefix cache; no implicit recursion-depth limit."""
    if type(m) is not int or m < 0:
        raise ValueError("prefix length must be a nonnegative integer")
    while len(_PREFIX) <= m:
        j = len(_PREFIX)
        _PREFIX.append(_PREFIX[-1] + forcing(j)/16**j)
    return _PREFIX[m]


def bbp_interval(m: int) -> tuple[F, F]:
    """Source-proved enclosure for x=pi/16 (classical BBP identity input)."""
    if type(m) is not int or m < 0:
        raise ValueError("nonnegative integer required")
    a = bbp_partial(m)
    return a, a+forcing(m+1)/F(15*16**m)


def source_parity_bit(clock: int, bit: int, terms: int|None=None,
                      extra_terms: int=512) -> tuple[int, int, tuple[F, F]]:
    """Certify Collatz parity at time 4*clock+bit with NO hex digit decoding.

    Source-first Rademacher formula:
      epsilon_(4n+j) = floor(2**(4-j)*16**n*x) mod 2.
    Its Fourier interpretation is sign(sin(2*pi*2**(3-j)*16**n*x)).
    Returns (signed-parity bit, source terms used, scaled interval).
    """
    if type(clock) is not int or clock < 0 or type(bit) is not int or not 0 <= bit < 4:
        raise ValueError("clock>=0, bit=0..3 required")
    if type(extra_terms) is not int or extra_terms < 0:
        raise ValueError("nonnegative search budget required")
    m0 = clock+2 if terms is None else terms
    if type(m0) is not int or m0 < 0:
        raise ValueError("nonnegative source terms required")
    multiplier = (1 << (4-bit))*16**clock
    for m in range(m0, m0+extra_terms+1):
        lo, hi = bbp_interval(m)
        a, b = multiplier*lo, multiplier*hi
        if a.numerator//a.denominator == b.numerator//b.denominator:
            return ((a.numerator//a.denominator)&1, m, (a,b))
    raise ValueError("source precision insufficient for specified parity bit")


def source_parity_address(nibbles: int) -> tuple[int, int]:
    """First 4*nibbles chronological parity bits; does NOT decode digits."""
    if type(nibbles) is not int or nibbles < 1:
        raise ValueError("positive nibble count required")
    address=0;max_terms=0
    for n in range(nibbles):
        for b in range(4):
            eps,m,_ = source_parity_bit(n,b)
            address |= eps << (4*n+b)
            max_terms=max(max_terms,m)
    return address,max_terms


def inverse_parity_mod(address: int, bits: int) -> int:
    """Classical Bernstein-Lagarias inverse parity homeomorphism mod 2**bits."""
    if type(address) is not int or type(bits) is not int or bits<0 or address<0:
        raise ValueError("nonnegative integral parity data required")
    mod=1<<bits;k=0;s=0
    for j in range(bits):
        if (address>>j)&1:
            k+=1
            s-= (1<<j)*pow(3,-k,mod)
    return s % mod


def shortcut(a: int) -> int:
    return a//2 if a%2==0 else (3*a+1)//2


def parity_address(a: int, bits: int) -> int:
    if type(bits) is not int or bits<0:
        raise ValueError("nonnegative bit count required")
    word=0
    for j in range(bits):
        word|=(a&1)<<j
        a=shortcut(a)
    return word


def swapped_source_defect(j: int) -> F:
    """Original-vs-adjacent-source-swap unwrapped discrepancy at j+1."""
    if type(j) is not int or j < 1:
        raise ValueError("positive source clock required")
    return 15*(forcing(j)-forcing(j+1))


def prime_square_order_clock(p: int) -> int:
    if type(p) is not int or p<7 or p%2==0:
        raise ValueError("odd prime p>=7 expected")
    # Deterministic primality check ensures pole really is a prime-square seam.
    for q in range(3,isqrt(p)+1,2):
        if p%q==0:
            raise ValueError("nonprime prime-square label")
    return (p*p-1)//8


def signed_prime_swap(p: int) -> tuple[int,int,F]:
    """Return (order clock j, propagation delay d, delta) with 1/64<=delta<1/4.

    Initial defect is D_j=15(r(j)-r(j+1)). Compare original zero-seeded
    completed source against a different source swapping only r(j),r(j+1).
    At phase clock m=j+1+d, z_orig * conjugate(z_swap)=exp(2*pi*i*delta).
    """
    j=prime_square_order_clock(p)
    D=swapped_source_defect(j)
    if D<=0 or D>=F(1,4):
        raise AssertionError("prime-square order defect out of certified domain")
    d=0;delta=D
    while delta < F(1,64):
        d+=1
        delta*=16
    if not F(1,64)<=delta<F(1,4):
        raise AssertionError("failed logarithmic response window")
    return j,d,delta


def signed_carry_from_source(p: int, terms: int|None=None,
                             extra_terms: int=512) -> tuple[int, int, int, F]:
    """Certify *orientation* of 2-hex-digit original-vs-swapped response.

    Returns (sign, terms_used, observation_clock, delta). Positive sign
    means original two-digit block > swapped two-digit block; negative means
    the crossed circle-zero seam reverses the order. Uses direct source
    enclosure and a single carry comparison; DOES NOT construct any digits.
    """
    j,d,delta=signed_prime_swap(p)
    obs=j+1+d
    m0=obs+2 if terms is None else terms
    if type(m0) is not int or m0<0 or type(extra_terms) is not int or extra_terms<0:
        raise ValueError("nonnegative precision budget required")
    scale=16**obs
    for m in range(m0,m0+extra_terms+1):
        a,b=bbp_interval(m)
        low,high=scale*a,scale*b
        fl=low.numerator//low.denominator
        fh=high.numerator//high.denominator
        if fl!=fh:continue
        l,h=low-fl,high-fl
        if h<delta:
            return -1,m,obs,delta
        if l>delta:
            return +1,m,obs,delta
    raise ValueError("failed to separate source phase from counterfactual carry threshold")


def two_hex_block_from_source(clock: int, m: int) -> int:
    """Test/reference decoder, NOT part of signed source-first carry predictor."""
    a,b=bbp_interval(m)
    factor=16**(clock+2)
    x,y=a*factor,b*factor
    f=x.numerator//x.denominator
    g=y.numerator//y.denominator
    if f!=g:raise ValueError("insufficient terms")
    return f%256


def two_hex_block_swapped(clock: int, j: int, m: int) -> int:
    """Counterfactual test-only decoder using its globally changed source value."""
    a,b=bbp_interval(m)
    source_delta=swapped_source_defect(j)/16**(j+1)
    factor=16**(clock+2)
    x,y=(a-source_delta)*factor,(b-source_delta)*factor
    f=x.numerator//x.denominator
    g=y.numerator//y.denominator
    if f!=g:raise ValueError("insufficient terms")
    return f%256


def chi3_from_gap(gap: int) -> int:
    """For a finite integer accelerated odd Collatz return, output mod3."""
    if type(gap) is not int or gap <1:
        raise ValueError("odd-to-next-odd gap must be positive")
    return 1 if gap%2==0 else 2


def odd_return_residues_from_parity(address: int, bits: int) -> tuple[tuple[int,int,int],...]:
    """Return (odd_clock, exact v2(3a+1), returned odd state mod3).

    Strictly finite symbolic cylinder; no 3-adic coordinate is assigned to an
    arbitrary infinite 2-adic state. The final incomplete odd run is omitted.
    """
    hits=[j for j in range(bits) if (address>>j)&1]
    return tuple((left,right-left,chi3_from_gap(right-left)) for left,right in zip(hits,hits[1:]))


def source_quarter_haar(clock: int) -> tuple[int,int]:
    """Source-first middle-half / BBP quarter-root seam bit without digit decoding.

    epsilon_(4n+2) XOR epsilon_(4n+3) equals 1 exactly when
    fractional(16**n*pi/16) is in (1/4,3/4), because pi is irrational.
    Does NOT assert positive all-shell density.
    """
    b2,m2,_=source_parity_bit(clock,2)
    b3,m3,_=source_parity_bit(clock,3)
    return b2 ^ b3, max(m2,m3)
