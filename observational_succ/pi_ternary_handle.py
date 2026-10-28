"""Certified fractional base-3 digits of pi through actual ternary BBP sources.

Original/derivative sources:
  Bailey (2023), Compendium of BBP-Type Formulas, (69) for pi*sqrt(3),
  (76) for pi**2. https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf
  Bailey-Borwein-Plouffe (1997) for the signed 4-pole original pi series.
  Machin's arctangent identity for an independent arithmetic witness.

IMPORTANT: A request for digit at position n DOES compute information through
position n. This is certified interval-based digit access, NOT a proof of a
BBP-style ternary random-access spigot for pi, nor of normality of pi.
Every arithmetic comparison uses integer ratios; no binary floating point.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from typing import Optional, Tuple

Q = Fraction

# Exact coefficients from Bailey's April 8, 2023 compendium, section 9.
# P(s,b,l,a) = sum(k>=0, b**-k * sum(j=1..l,a[j-1]/(l*k+j)**s)).
TERNARY_PISQRT3 = (81, -54, 0, -9, 0, -12, -3, -2, 0, -1, 0, 0)
TERNARY_PI2 = (243, -405, 0, -81, -27, -72, -9, -9, 0, -5, 1, 0)
BBP_ORIGINAL = (4, 0, 0, -2, -1, -1, 0, 0)
SOURCE_ID = {
    "ternary-pi2": "Bailey-2023-eq76-pi-squared",
    "ternary-pisqrt3": "Bailey-2023-eq69-pi-sqrt3",
    "original-bbp": "BBP-1997-original-four-signed-poles",
    "machin": "Machin-1706-two-arctangent-alternating",
}
SOURCES = tuple(SOURCE_ID)


@dataclass(frozen=True)
class Interval:
    low: Q
    high: Q
    source: str
    terms: int
    form: str  # direct pi; pi-square; pi-root3

    def __post_init__(self):
        if self.low > self.high:
            raise ValueError("reversed interval")
        if self.terms < 1 or self.source not in SOURCE_ID:
            raise ValueError("unknown certified interval source")


def _finite(n: int, label: str, floor: int = 1, ceiling: int = 100_000) -> int:
    if type(n) is not int or not floor <= n <= ceiling:
        raise ValueError(f"{label} must be an integer from {floor} to {ceiling}")
    return n


def bbp_interval(terms: int, *, coefficients: Tuple[int, ...], degree: int,
                 base: int, prefactor: Q, source: str, form: str) -> Interval:
    """Rigorous absolute tail from positive monotonic denominators.

    |R_K| <= |prefactor| base^-K base/(base-1)
                 sum_j |a_j|/(lK+j)^degree .
    Unconditionally valid for every positive K, including cancellation-heavy
    signed coefficient vectors. Certificate does not assume termwise sign.
    """
    _finite(terms, "terms")
    if base < 2 or degree < 1 or not coefficients:
        raise ValueError("invalid BBP source")
    prefactor = Q(prefactor)
    period = len(coefficients)
    value = Q(0)
    power = 1
    for k in range(terms):
        source_block = sum((Q(a, (period*k+j)**degree)
                            for j, a in enumerate(coefficients, 1) if a), Q(0))
        value += source_block / power
        power *= base
    value *= prefactor
    remainder = abs(prefactor) * Q(base, (base-1)*power) * sum(
        (Q(abs(a), (period*terms+j)**degree)
         for j, a in enumerate(coefficients, 1) if a), Q(0))
    return Interval(value-remainder, value+remainder, source, terms, form)


def ternary_pi2_interval(terms: int) -> Interval:
    return bbp_interval(terms, coefficients=TERNARY_PI2, degree=2, base=3**6,
                        prefactor=Q(2, 27), source="ternary-pi2", form="pi-square")


def ternary_pisqrt3_interval(terms: int) -> Interval:
    return bbp_interval(terms, coefficients=TERNARY_PISQRT3, degree=1, base=3**6,
                        prefactor=Q(1, 9), source="ternary-pisqrt3", form="pi-root3")


def original_bbp_interval(terms: int) -> Interval:
    """An independent original signed-BBP pi bound with sharp Green tail."""
    _finite(terms, "terms")
    partial = sum((Q(4, (8*k+1)*16**k) - Q(2, (8*k+4)*16**k)
                   - Q(1, (8*k+5)*16**k) - Q(1, (8*k+6)*16**k)
                   for k in range(terms)), Q(0))
    n = terms
    den = (8*n+1)*(8*n+2)
    lower_green = Q(1, den)-Q(6, den*(8*n+3))
    upper_green = Q(1, den)
    if lower_green <= 0:
        raise AssertionError("invalid original positive Green bound")
    factor = Q(1, 16**(n-1))
    return Interval(partial+factor*lower_green, partial+factor*upper_green,
                    "original-bbp", terms, "direct")


def _arctan_interval(denominator: int, terms: int) -> Tuple[Q,Q]:
    _finite(terms, "terms")
    if denominator <= 1:
        raise ValueError("denominator must exceed one")
    partial = sum((Q((-1)**k, (2*k+1)*denominator**(2*k+1))
                   for k in range(terms)), Q(0))
    remainder = Q(1, (2*terms+1)*denominator**(2*terms+1))
    return ((partial, partial+remainder) if terms%2==0
            else (partial-remainder, partial))


def machin_interval(terms: int) -> Interval:
    a,b = _arctan_interval(5,terms), _arctan_interval(239,terms)
    return Interval(16*a[0]-4*b[1],16*a[1]-4*b[0],"machin",terms,"direct")


def interval_for(source: str, terms: int) -> Interval:
    if source == "ternary-pi2": return ternary_pi2_interval(terms)
    if source == "ternary-pisqrt3": return ternary_pisqrt3_interval(terms)
    if source == "original-bbp": return original_bbp_interval(terms)
    if source == "machin": return machin_interval(terms)
    raise ValueError("unsupported source")


def floor_fraction(value: Q) -> int:
    return value.numerator // value.denominator


def floor_scaled_pi(bound: Q, scale: int, form: str) -> int:
    """Exact floor(scale*pi) for a given lower/upper algebraic bound.

    Positive algebraic roots handled via integer sqrt, without evaluating a
    decimal or rounding a floating-point sqrt. For q=a/b >=0:
      floor(scale * sqrt(q)) = isqrt(floor(scale**2*a/b)).
    """
    if bound < 0 or scale < 1:
        raise ValueError("nonnegative algebraic bound and positive scale needed")
    if form == "direct":
        return floor_fraction(bound * scale)
    if form == "pi-square":
        return isqrt((scale*scale*bound.numerator)//bound.denominator)
    if form == "pi-root3":
        return isqrt((scale*scale*bound.numerator**2)//(3*bound.denominator**2))
    raise ValueError("unknown algebraic reconstruction")


def ternary_word(n: int, width: int) -> str:
    _finite(width, "width", 0)
    if n < 0 or n >= 3**width:
        raise ValueError("invalid width for ternary word")
    out = ["0"]*width
    for j in range(width-1,-1,-1):
        n,d = divmod(n,3)
        out[j] = str(d)
    return "".join(out)


@dataclass(frozen=True)
class PrefixCertificate:
    source: str
    terms: int
    digits: int
    prefix: str
    floor_lower: int
    floor_upper: int
    bound: Interval

    def as_dict(self, include_rationals: bool = True) -> dict:
        content = {
            "type":"CERTIFIED_TERNARY_PI_PREFIX_v1",
            "source":SOURCE_ID[self.source],
            "terms":self.terms,
            "fractional_digits":self.digits,
            "radix":3,
            "base3_pi":"10."+self.prefix,
            "floor_3pow_n_pi_lower":str(self.floor_lower),
            "floor_3pow_n_pi_upper":str(self.floor_upper),
            "certified":self.floor_lower==self.floor_upper,
            "interval_form":self.bound.form,
        }
        lower = str(self.bound.low.numerator)+"/"+str(self.bound.low.denominator)
        upper = str(self.bound.high.numerator)+"/"+str(self.bound.high.denominator)
        content["exact_bounds_sha256"] = sha256((lower+"\n"+upper).encode()).hexdigest()
        if include_rationals:
            content["exact_lower"] = lower
            content["exact_upper"] = upper
        return content


def certify_prefix(digits: int, source: str = "ternary-pi2",
                   max_terms: Optional[int] = None) -> PrefixCertificate:
    _finite(digits,"digits",1,4096)
    if source not in SOURCE_ID: raise ValueError("unsupported source")
    k = max(2, digits//6+1 if source.startswith("ternary-")
             else digits//2+1)
    if max_terms is None: max_terms = max(80, 4*digits+32)
    _finite(max_terms, "max_terms",1,100_000)
    power3 = 3**digits
    while k <= max_terms:
        v = interval_for(source,k)
        if v.low > 0:
            low = floor_scaled_pi(v.low,power3,v.form)
            high = floor_scaled_pi(v.high,power3,v.form)
            if low == high and low//power3 == 3:
                return PrefixCertificate(source,k,digits,
                                         ternary_word(low-3*power3,digits),
                                         low,high,v)
        k += max(1,k//10)
    raise ArithmeticError("requested ternary digit boundary not certified at max_terms")


def digit_range(start: int, count: int, *, sources: Tuple[str,...] =
                ("ternary-pi2","ternary-pisqrt3","original-bbp","machin")) -> Tuple[str,tuple]:
    _finite(start,"start",1,4096)
    _finite(count,"count",1,4096)
    end = start+count-1
    _finite(end,"end",1,4096)
    if not sources or len(set(sources)) != len(sources):
        raise ValueError("nonempty unique source list required")
    certs = tuple(certify_prefix(end,s) for s in sources)
    if len({c.prefix for c in certs}) != 1:
        raise ArithmeticError("INDEPENDENT TERNARY SOURCES DISAGREE; block publication")
    return certs[0].prefix[start-1:end], certs


def ternary_pole_depth(k: int) -> int:
    """Authentic sixth-slot denominator valuation v3(2k+1)."""
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative exact integer")
    d = 2*k+1
    r = 0
    while d%3==0:
        d//=3
        r+=1
    return r


def sixth_slot_dual(k: int) -> Tuple[Q,Q]:
    """Exact sixth-channel taps of published ternary sources.

    pi sqrt3 has (−12)/(12k+6), pi² has (−72)/(12k+6)^2,
    i.e. −2/(2k+1) and −2/(2k+1)^2 respectively.
    These are local source terms inside a real-convergent sum, not p-adic
    convergent series or independent random variables.
    """
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative exact integer")
    den = 2*k+1
    return Q(-12,12*k+6), Q(-72,(12*k+6)**2)


def source_pole_distribution(depth: int) -> dict:
    """For k mod3^L, exact count of r=v3(2k+1), clipped at L."""
    _finite(depth,"depth",1,15)
    p = 3
    return {r: (2*3**(depth-r-1) if r<depth else 1)
            for r in range(depth+1)}
