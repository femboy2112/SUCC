"""Exact primitive ABC-triple ris-moment sums and a rigorous t<1/2 bound.

Object of study (Moonshot D, SUCC Academic Main V):

    S_t(X) := sum over primitive a+b=c<=X, a,b>0, gcd(a,b)=1, of ris(abc)^t.

Here ``ris(n) = n/rad(n)`` and, on a primitive triple, pairwise coprimality
gives the exact factorisation ``ris(abc) = ris(a)*ris(b)*ris(c)``.  The
enumeration is ORDERED by default: for each c we run a=1..c-1 and set b=c-a
(so each unordered pair is counted twice, except the single (1,1,2)).  This
matches the literal index set "a+b=c, a,b>0".  Pass ``ordered=False`` to count
unordered pairs a<=b instead.

New-to-project elementary arithmetic.  This file proves NO abc conjecture, no
new exceptional-set exponent, no Weil sign, and no RH statement.  It reuses the
``ris^theta`` Dirichlet-convolution lemma ABC-CLK-02 from ``abc_clock_families``.

EXACTNESS DISCIPLINE (AGENTS.md item 8).  For rational t = p/q with q>1 the
value ris(n)^t is an irrational q-th root, so S_t(X) is generally irrational.
Nothing here rounds it to a float certificate.  The exact deliverables are:

  * ``ris_spectrum`` / ``triple_count`` / ``integer_moment`` : integer-exact
    census objects (no roots at all);
  * ``S_t_enclosure`` / ``ratio_enclosure`` : CERTIFIED rational two-sided
    enclosures [lo, hi] with lo <= (true value) <= hi, built from exact integer
    q-th-root brackets (sound interval arithmetic, never a float);
  * ``S_t_constant_upper`` : a rigorous RATIONAL upper bound for the constant
    C_t of the partial theorem below, valid for 0 <= t < 1/2.

Float arithmetic appears nowhere in this module.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd

from .abc_clock_families import ABCClockError, prime_factors, radical, ris


# --------------------------------------------------------------------------
# Exact integer root brackets (floor k-th root; no floats).
# --------------------------------------------------------------------------
def integer_root(n: int, k: int) -> int:
    """Exact floor(n**(1/k)) for integers n>=0, k>=1.  Pure integer arithmetic."""
    if type(n) is not int or type(k) is not int or n < 0 or k < 1:
        raise ABCClockError("integer_root needs n>=0 and k>=1 as ints")
    if k == 1 or n in (0, 1):
        return n
    x = 1 << ((n.bit_length() + k - 1) // k)  # >= true root
    while True:
        t = ((k - 1) * x + n // (x ** (k - 1))) // k
        if t >= x:
            break
        x = t
    while x ** k > n:          # correct any Newton overshoot
        x -= 1
    while (x + 1) ** k <= n:   # correct any undershoot
        x += 1
    return x


def power_enclosure(base: int, num: int, den: int, precision: int) -> tuple[Fraction, Fraction]:
    """Certified rational bracket [lo, hi] with lo <= base**(num/den) <= hi.

    base>=1 integer, num>=0, den>=1 integers, precision>=1 sets the grid 1/precision.
    Exactness: with N = base**num and r = floor((N*precision**den)**(1/den)),
    (r/precision)**den <= N <= ((r+1)/precision)**den, so r/precision and
    (r+1)/precision bracket base**(num/den).  Width is exactly 1/precision.
    """
    if type(base) is not int or base < 1 or type(num) is not int or num < 0:
        raise ABCClockError("power_enclosure needs base>=1, num>=0 integers")
    if type(den) is not int or den < 1 or type(precision) is not int or precision < 1:
        raise ABCClockError("power_enclosure needs den>=1, precision>=1 integers")
    if den == 1:                      # integer exponent: value is exactly rational
        val = Fraction(base ** num)
        return val, val
    scaled = (base ** num) * (precision ** den)
    r = integer_root(scaled, den)
    return Fraction(r, precision), Fraction(r + 1, precision)


# --------------------------------------------------------------------------
# Exact census of primitive triples.
# --------------------------------------------------------------------------
def triple_ris(a: int, b: int, c: int) -> int:
    """Exact ris(abc) for a primitive triple, via ris(a)*ris(b)*ris(c).

    Requires a+b=c, a,b>0, gcd(a,b)=1.  Equals ris(a*b*c) by pairwise
    coprimality (cross-checked by ``ris_product_direct``).
    """
    if any(type(n) is not int or n < 1 for n in (a, b, c)):
        raise ABCClockError("triple entries must be positive integers")
    if a + b != c or gcd(a, b) != 1:
        raise ABCClockError("a+b=c and gcd(a,b)=1 required")
    return ris(a) * ris(b) * ris(c)


def ris_product_direct(a: int, b: int, c: int) -> int:
    """Independent route: ris(a*b*c).  Used to cross-check ``triple_ris``."""
    if any(type(n) is not int or n < 1 for n in (a, b, c)):
        raise ABCClockError("triple entries must be positive integers")
    if a + b != c or gcd(a, b) != 1:
        raise ABCClockError("a+b=c and gcd(a,b)=1 required")
    return ris(a * b * c)


def primitive_triples(X: int, *, ordered: bool = True):
    """Yield (a, b, c) over primitive a+b=c<=X, a,b>0, gcd(a,b)=1.

    ordered=True  : a=1..c-1 (each unordered pair twice, (1,1,2) once).
    ordered=False : a<=b (unordered).
    """
    if type(X) is not int or X < 2:
        raise ABCClockError("need integer X>=2")
    for c in range(2, X + 1):
        top = c if ordered else (c // 2) + 1
        for a in range(1, top):
            b = c - a
            if gcd(a, b) == 1:
                yield a, b, c


def ris_spectrum(X: int, *, ordered: bool = True) -> Counter:
    """Exact multiplicity spectrum {R: number of primitive triples with ris(abc)=R}.

    Integer-exact; this is the full finite census from which every moment of
    S_t(X) is determined.  A finite census is EVIDENCE, never a proof of a
    uniform bound (AGENTS.md items 4, 8).
    """
    spec: Counter = Counter()
    for a, b, c in primitive_triples(X, ordered=ordered):
        spec[ris(a) * ris(b) * ris(c)] += 1
    return spec


def triple_count(X: int, *, ordered: bool = True) -> int:
    """Exact S_0(X): number of primitive triples (ordered or unordered)."""
    return sum(ris_spectrum(X, ordered=ordered).values())


def integer_moment(X: int, k: int, *, ordered: bool = True) -> int:
    """Exact integer moment sum_{triples} ris(abc)^k for integer k>=0.

    This is S_k(X) when k is a nonnegative integer (q=1, no roots needed), so it
    is returned as an exact Python int.  k=0 is the triple count; k=1 is the
    total ris; these are the rational anchors for the enclosure tests.
    """
    if type(k) is not int or k < 0:
        raise ABCClockError("integer_moment needs integer k>=0")
    return sum(mult * (R ** k) for R, mult in ris_spectrum(X, ordered=ordered).items())


# --------------------------------------------------------------------------
# Certified rational enclosure of S_t(X) for rational t.
# --------------------------------------------------------------------------
def _as_fraction_exponent(t) -> tuple[int, int]:
    f = t if isinstance(t, Fraction) else Fraction(t)
    if f < 0 or f.denominator < 1:
        raise ABCClockError("t must be a nonnegative rational Fraction")
    return f.numerator, f.denominator


def S_t_enclosure(X: int, t, *, precision: int = 10 ** 9,
                  ordered: bool = True) -> tuple[Fraction, Fraction]:
    """Certified [lo, hi] rational bracket for the exact S_t(X), t a Fraction.

    lo <= S_t(X) <= hi, with lo, hi exact Fractions.  Each distinct ris value R
    contributes mult(R) copies of the certified bracket for R**(num/den).  For
    t with den=1 (integer exponent) the bracket is exact (lo==hi).
    """
    num, den = _as_fraction_exponent(t)
    spec = ris_spectrum(X, ordered=ordered)
    lo = Fraction(0)
    hi = Fraction(0)
    for R, mult in spec.items():
        rlo, rhi = power_enclosure(R, num, den, precision)
        lo += mult * rlo
        hi += mult * rhi
    return lo, hi


def ratio_enclosure(X: int, t, *, precision: int = 10 ** 9,
                    ordered: bool = True) -> tuple[Fraction, Fraction]:
    """Certified [lo, hi] rational bracket for S_t(X)/X^2."""
    lo, hi = S_t_enclosure(X, t, precision=precision, ordered=ordered)
    return lo / (X * X), hi / (X * X)


def growth_table(t, Xs: tuple[int, ...], *, precision: int = 10 ** 9,
                 ordered: bool = True) -> tuple[dict, ...]:
    """Exact empirical growth table of S_t(X)/X^2 over the documented Xs.

    Each row: {'X', 'count', 'ratio_lo', 'ratio_hi'} with the ratio as a
    certified rational bracket.  The default t is intended to be Fraction(2,5).
    This is a finite experiment, not a limit statement (AGENTS.md item 5).
    """
    if not isinstance(Xs, tuple) or not Xs or any(type(x) is not int or x < 2 for x in Xs):
        raise ABCClockError("Xs must be a nonempty tuple of ints >= 2")
    rows = []
    for X in Xs:
        spec = ris_spectrum(X, ordered=ordered)
        count = sum(spec.values())
        num, den = _as_fraction_exponent(t)
        lo = sum((mult * power_enclosure(R, num, den, precision)[0] for R, mult in spec.items()),
                 Fraction(0))
        hi = sum((mult * power_enclosure(R, num, den, precision)[1] for R, mult in spec.items()),
                 Fraction(0))
        rows.append({"X": X, "count": count,
                     "ratio_lo": lo / (X * X), "ratio_hi": hi / (X * X)})
    return tuple(rows)


# --------------------------------------------------------------------------
# The rigorous upper bound (partial theorem), via ABC-CLK-02.
# --------------------------------------------------------------------------
# Partial theorem (PROVED LOCAL).  For every rational 0 <= t < 1/2,
#
#     S_t(X) <= M(t) * M(2t) * X^2         for all X >= 2,
#
# where M(theta) = prod_p ( 1 + (p^theta - 1) / (p^2 (1 - p^{theta-1})) ) is the
# ABC-CLK-02 ris^theta moment constant (finite for theta < 1).
#
# Proof.  Write S_t(X) = sum_{c<=X} ris(c)^t * I(c) with
# I(c) = sum_{a=1}^{c-1, gcd(a,c)=1} ris(a)^t ris(c-a)^t  >= the ordered inner sum
# (dropping the gcd(a,c)=1 constraint only enlarges a nonnegative sum).  By the
# Cauchy-Schwarz inequality,
#     I(c) <= ( sum_{a<c} ris(a)^{2t} )^{1/2} ( sum_{a<c} ris(c-a)^{2t} )^{1/2}
#          =  sum_{n<c} ris(n)^{2t}  <= M(2t) * c       (ABC-CLK-02 at theta=2t, needs 2t<1).
# Hence S_t(X) <= M(2t) * sum_{c<=X} c * ris(c)^t <= M(2t) * X * sum_{c<=X} ris(c)^t
#              <= M(2t) * X * M(t) * X = M(t) M(2t) X^2  (ABC-CLK-02 at theta=t, needs t<1).
# The BINDING constraint is 2t < 1 (inner Cauchy-Schwarz), i.e. t < 1/2. QED.
#
# EXPONENT ALGEBRA / where uniformity fails.  Any Holder split of the inner
# additive correlation into two ris-moments uses conjugate exponents r, r' with
# 1/r + 1/r' = 1 and needs t*r < 1, t*r' < 1; the symmetric choice r=r'=2
# (Cauchy-Schwarz) minimises max(r,r')=2, forcing 2t<1.  So t<1/2 is the exact
# ceiling of THIS method.  At t >= 1/2 the factor 1/(1 - p^{2t-1}) in M(2t)
# diverges (the Euler product has no finite value), so no uniform constant is
# produced -- the bound is not merely unproven, this route cannot be uniform.
# The prior three-fold Holder route (abc_clock_families section 2/5) needs
# 3t<1, i.e. t<1/3; this Cauchy-Schwarz route strictly improves 1/3 -> 1/2.
# The regime 1/2 <= t < 1 remains OPEN here.


@lru_cache(maxsize=256)
def _primes_upto(P: int) -> tuple[int, ...]:
    if type(P) is not int or P < 2:
        return ()
    sieve = bytearray([1]) * (P + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, integer_root(P, 2) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return tuple(i for i in range(2, P + 1) if sieve[i])


def ris_moment_euler_factor_upper(p: int, theta, precision: int = 10 ** 4) -> Fraction:
    """Exact rational upper bound for the ABC-CLK-02 Euler factor at prime p.

    Factor = 1 + a_p, a_p = (p^theta - 1) / (p^2 (1 - p^{theta-1})), theta<1.
    Upper bound: numerator (p^theta - 1) <= hi(p^theta) - 1; denominator
    p^2 (1 - p^{theta-1}) >= p^2 (1 - 1/lo(p^{1-theta})) with lo>1.
    """
    num, den = _as_fraction_exponent(theta)
    if num >= den:
        raise ABCClockError("theta must be < 1")
    if type(p) is not int or p < 2:
        raise ABCClockError("p must be a prime integer >= 2")
    hi_ptheta = power_enclosure(p, num, den, precision)[1]          # >= p^theta
    lo_p1mt = power_enclosure(p, den - num, den, precision)[0]      # <= p^{1-theta}
    if lo_p1mt <= 1:
        raise ABCClockError("precision too low: need lo(p^{1-theta}) > 1")
    numerator_up = hi_ptheta - 1                                   # >= p^theta - 1
    # 1 - p^{theta-1} = 1 - 1/p^{1-theta} >= 1 - 1/lo_p1mt = (lo-1)/lo
    denom_low = (p * p) * (lo_p1mt - 1) / lo_p1mt                  # <= p^2 (1 - p^{theta-1})
    return 1 + numerator_up / denom_low


def ris_moment_tail_bound(theta, P: int, precision: int = 10 ** 4) -> Fraction:
    """Exact rational upper bound for sum_{p>P} a_p (prime tail of log-ish mass).

    a_p <= p^{theta-2}/(1 - p^{theta-1}); for p>P, 1 - p^{theta-1} >= 1 - (P+1)^{theta-1}.
    sum_{p>P} p^{theta-2} <= sum_{n>P} n^{theta-2} <= integral_P^inf x^{theta-2} dx
      = P^{theta-1}/(1-theta).  All three pieces are bounded by exact rationals.
    """
    num, den = _as_fraction_exponent(theta)
    if num >= den:
        raise ABCClockError("theta must be < 1")
    p0 = P + 1
    lo_p0 = power_enclosure(p0, den - num, den, precision)[0]       # <= p0^{1-theta}
    lo_P = power_enclosure(P, den - num, den, precision)[0]         # <= P^{1-theta}
    if lo_p0 <= 1 or lo_P <= 1:
        raise ABCClockError("precision too low for tail bound")
    c0_up = lo_p0 / (lo_p0 - 1)                                     # >= 1/(1 - p0^{theta-1})
    integral_up = (1 / lo_P) * Fraction(den, den - num)            # >= P^{theta-1}/(1-theta)
    return c0_up * integral_up


@lru_cache(maxsize=64)
def ris_moment_constant_upper(theta, P: int = 0, precision: int = 10 ** 4) -> Fraction:
    """Exact rational C with C >= M(theta) = ABC-CLK-02 constant, theta<1.

    C = ( prod_{p<=P} (1 + a_p)-upper ) * 1/(1 - tau), where tau >= sum_{p>P} a_p
    and tau < 1.  P auto-selects the smallest tabulated cutoff with tau < 9/10.
    The finite product is rounded UP after each factor to keep the rational
    small (rounding up preserves the upper-bound property).
    """
    num, den = _as_fraction_exponent(theta)
    if num >= den:
        raise ABCClockError("theta must be < 1")
    if P == 0:
        for cand in (100, 1000, 5000, 20000, 60000, 150000, 400000):
            if ris_moment_tail_bound(theta, cand, precision) < Fraction(9, 10):
                P = cand
                break
        if P == 0:
            raise ABCClockError("no tabulated cutoff gave tau < 9/10")
    tau = ris_moment_tail_bound(theta, P, precision)
    if tau >= 1:
        raise ABCClockError("tail bound tau >= 1; raise P")
    grid = 10 ** 15
    prod = Fraction(1)
    for p in _primes_upto(P):
        prod *= ris_moment_euler_factor_upper(p, theta, precision)
        # round the running product UP onto a fixed grid (stays an upper bound)
        prod = Fraction(-((-(prod.numerator * grid)) // prod.denominator), grid)
    return prod / (1 - tau)


def S_t_constant_upper(t, *, precision: int = 10 ** 4) -> Fraction:
    """Exact rational C_t with S_t(X) <= C_t * X^2 for all X>=2, valid for 0<=t<1/2.

    C_t = M_upper(t) * M_upper(2t).  Requires 2t < 1 (binding); raises otherwise,
    which is exactly the point at which the method stops being uniform.
    """
    f = t if isinstance(t, Fraction) else Fraction(t)
    if f < 0:
        raise ABCClockError("t must be >= 0")
    if 2 * f >= 1:
        raise ABCClockError("S_t_constant_upper requires t < 1/2 (2t<1 is binding)")
    outer = Fraction(1) if f == 0 else ris_moment_constant_upper(f, 0, precision)
    inner = ris_moment_constant_upper(2 * f, 0, precision)
    return outer * inner


# --------------------------------------------------------------------------
# Hostile families (exact).  Obstruction: no UNIFORM POINTWISE moment bound.
# --------------------------------------------------------------------------
def power_tower_family(X: int, base: int = 2) -> tuple[dict, ...]:
    """Exact deep-prime-power / extreme-imbalance family: (1, base^k - 1, base^k).

    For each k with base^k <= X this is a primitive triple (gcd(1, .)=1).  Its
    ris is exact:  ris(1) * ris(base^k - 1) * ris(base^k).  When base is prime,
    ris(base^k) = base^(k-1), so ris(abc) >= base^(k-1) = c/base grows without
    bound -- a single triple's moment ris(abc)^t is UNBOUNDED in k.

    Returns one dict per k: {'k','a','b','c','ris_c','ris_b','ris_abc'} (ints).
    """
    if type(X) is not int or X < base or type(base) is not int or base < 2:
        raise ABCClockError("need integer X>=base and base>=2")
    out = []
    k = 1
    while base ** k <= X:
        c = base ** k
        a, b = 1, c - 1
        out.append({"k": k, "a": a, "b": b, "c": c,
                    "ris_c": ris(c), "ris_b": ris(b), "ris_abc": ris(a) * ris(b) * ris(c)})
        k += 1
    return tuple(out)


def power_tower_contribution_enclosure(X: int, t, base: int = 2,
                                       precision: int = 10 ** 9) -> tuple[Fraction, Fraction]:
    """Certified [lo, hi] for sum over the (1, base^k-1, base^k) family of ris(abc)^t.

    This exact partial sum demonstrates the HONEST boundary: although each term
    is unbounded, the whole family contributes o(X^2) for t<2, so it does NOT
    refute the X^2 bound -- it refutes only a naive termwise/uniform-pointwise
    moment bound.
    """
    num, den = _as_fraction_exponent(t)
    lo = Fraction(0)
    hi = Fraction(0)
    for row in power_tower_family(X, base):
        rlo, rhi = power_enclosure(row["ris_abc"], num, den, precision)
        lo += rlo
        hi += rhi
    return lo, hi


def pointwise_max_ris(X: int, *, ordered: bool = True) -> tuple[int, tuple[int, int, int]]:
    """Exact max of ris(abc) over primitive triples c<=X, with a maximiser.

    Witnesses that the pointwise moment has no uniform bound: the maximum grows
    with X (the (1, 2^k-1, 2^k) tower forces max >= 2^(floor(log2 X)-1)).
    """
    best = 0
    arg = (0, 0, 0)
    for a, b, c in primitive_triples(X, ordered=ordered):
        r = ris(a) * ris(b) * ris(c)
        if r > best:
            best, arg = r, (a, b, c)
    return best, arg
