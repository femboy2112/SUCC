"""BBP Gamma first jets, exact source-block finite parts, and q-Euler audits.

Research only: classical BBP is an imported identity; nothing here proves
normality of pi. Frozen forcing is read from duck_bbp, not modified.
All source/rational/valuation claims use exact integer Fraction arithmetic.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd, log

POLES: tuple[tuple[int, int], ...] = ((0, 4), (3, -2), (4, -1), (5, -1))
RADIX = 16


def _positive_int(n: int, label: str) -> int:
    if type(n) is not int or n < 1:
        raise ValueError(f"{label} must be a positive integer")
    return n


def forcing(n: int) -> F:
    """Original four-pole r(n) with a_n=8n-7, no replacement source."""
    _positive_int(n, "n")
    a = 8*n - 7
    return sum((F(w, a+d) for d, w in POLES), F())


def block_source(g: int, k: int = 1) -> F:
    """Exact original g-step forcing at grouped source index k."""
    _positive_int(g, "g"); _positive_int(k, "k")
    return sum((16**(g-j)*forcing(g*(k-1)+j) for j in range(1, g+1)), F())


def blocking_coefficients(g: int) -> tuple[int, ...]:
    _positive_int(g, "g")
    return tuple(16**(g-1-j) for j in range(g))


def block_laplace_mass(g: int, a: int | F) -> F:
    """Integral exp(-a x) Q(x) B_g(exp(-8x)) dx, exactly rational."""
    _positive_int(g, "g")
    a = F(a)
    if a <= 0:
        raise ValueError("a must be positive")
    return sum((F(coeff*w, a+8*j+d)
                for j, coeff in enumerate(blocking_coefficients(g))
                for d,w in POLES), F())


def source_endpoint_jets(g: int) -> tuple[int, int]:
    """Exact Q_g'(0), Q_g''(0); Q_g=Q B_g."""
    _positive_int(g, "g")
    s0 = sum(blocking_coefficients(g))
    s1 = sum(j*c for j,c in enumerate(blocking_coefficients(g)))
    return 15*s0, -59*s0 - 240*s1


def mellin_first_jet_coefficient(g: int) -> F:
    """The exact 1/a term of 1-E[log(aX)]-gamma at fixed g."""
    _positive_int(g, "g")
    first, second = source_endpoint_jets(g)
    x = F(-second, 2*first)
    assert x == F(5, 2)-F(8*g, 16**g-1)
    return x


def bbp_gamma_log_argument(g: int) -> F:
    """Canonical source-clock logarithm argument C_g=64 R_g(1)/(16^g-1)."""
    _positive_int(g, "g")
    return F(64)*block_source(g)/(16**g-1)


def bbp_gamma_deformation(g: int) -> float:
    """gamma_BBP,g = EulerGamma - (1/2)log C_g, float diagnostic only."""
    import math
    _positive_int(g, "g")
    # math.euler_gamma not consistently present in supported Python versions.
    euler_gamma = 0.57721566490153286060651209008240243104
    c = bbp_gamma_log_argument(g)
    return euler_gamma-0.5*(log(c.numerator)-log(c.denominator))


def blocked_free_energy(g: int, cutoff: int) -> float:
    """Exact source ratios followed by float logs; approaches log(g² C_g)-2gamma."""
    _positive_int(g, "g"); _positive_int(cutoff, "cutoff")
    left, right = block_source(g, 1), block_source(g, cutoff)
    h = sum((F(1,j) for j in range(1,cutoff)), F())
    ratio = left/right
    return log(ratio.numerator)-log(ratio.denominator)-2*float(h)


def prime_factorization(n: int) -> dict[int,int]:
    """Exact elementary factoring for finite source/support oracles."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer to factor")
    fac: dict[int,int] = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            fac[p] = fac.get(p, 0)+1
            n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        fac[n] = fac.get(n, 0)+1
    return fac


def valuation(q: F, p: int) -> int:
    """p-adic exponent v_p(q), never conflating prime p and prime power."""
    if F(q) == 0:
        raise ValueError("valuation of zero is infinite")
    if type(p) is not int or p < 2:
        raise ValueError("prime base p>=2 required")
    a, b = abs(F(q).numerator), F(q).denominator
    v = 0
    while a % p == 0:
        a //= p; v += 1
    while b % p == 0:
        b //= p; v -= 1
    return v


def log_linear_prime_coefficients(g: int, a: int = 1) -> dict[int,F]:
    """Exact coefficients L_p in gamma_Mellin(a,g)-gamma=1+sum_p L_p log p.

    Derivative of normalized Mellin E[(aX)^s]/Gamma(s+2) at s=0.
    Requires positive INTEGER clock a, so all arguments factor over Q.
    Returns only nonzero prime coefficients, not the additive constant 1.
    """
    _positive_int(g, "g"); _positive_int(a, "a")
    mass = block_laplace_mass(g, a)
    fa = prime_factorization(a)
    coefficients: dict[int,F] = {}
    for j, block in enumerate(blocking_coefficients(g)):
        for d, w in POLES:
            t = a+8*j+d
            term = F(block*w, t)/mass
            for p in set(prime_factorization(t))|set(fa):
                v = prime_factorization(t).get(p,0)-fa.get(p,0)
                if v:
                    coefficients[p] = coefficients.get(p,F())+term*v
    return dict(sorted((p,c) for p,c in coefficients.items() if c))


def mellin_gamma_correction(g: int, a: int = 1) -> float:
    """float of gamma_Mellin(a,g)-EulerGamma, 1 + rational-log coefficients."""
    return 1+sum(float(c)*log(p) for p,c in log_linear_prime_coefficients(g,a).items())


def q_lambert_partial(terms: int) -> F:
    """Partial Lambert series at q=1/16, exact rational."""
    if type(terms) is not int or terms < 0:
        raise ValueError("nonnegative terms required")
    return sum((F(1,16**n-1) for n in range(1, terms+1)), F())


def q_lambert_tail_bound(terms: int) -> F:
    """Upper bound for omitted terms: sum_{n>m}1/(16^n-1)."""
    if type(terms) is not int or terms < 0:
        raise ValueError("nonnegative terms required")
    return F(1, 15*16**terms) / (1-F(1, 16**(terms+1)))


def divisor_count(n: int) -> int:
    """Number of positive divisors; coefficient of q^n in Lambert series."""
    _positive_int(n,"n")
    total = 1
    for e in prime_factorization(n).values():
        total *= e+1
    return total


def divisor_lambert_partial(terms: int) -> F:
    """First coefficients of sum_{m>=1}tau(m)16^-m, exact rational."""
    if type(terms) is not int or terms < 0:
        raise ValueError("nonnegative terms required")
    return sum((F(divisor_count(n),16**n) for n in range(1, terms+1)), F())


def multiplicative_order_16(modulus: int) -> int:
    """Pure exact integer order for modulus relatively prime to 16."""
    _positive_int(modulus,"modulus")
    if modulus == 1 or gcd(16,modulus)!=1:
        raise ValueError("odd modulus >=3 required")
    v,n = 16%modulus,1
    while v != 1:
        v=(16*v)%modulus
        n+=1
    return n


def q_block_polynomial(g: int, t: F) -> F:
    """Exact B_g(t)=(16^g-t^g)/(16-t), finite sum, not q-Euler itself."""
    _positive_int(g,"g"); t=F(t)
    return sum((16**(g-1-j)*t**j for j in range(g)),F())
