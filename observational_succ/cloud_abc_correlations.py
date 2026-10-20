"""Exact checks for the cloud primitive ABC moment theorem, 0 <= t < 2/3.

The universal result is a paper proof in CLOUD_ABC_CORRELATIONS.md. Finite
checks here certify arithmetic identities and countermodels, not the theorem.
No float, oracle metadata, BBLT exceptional-set import, or zero data is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_clock_families import prime_factors, radical, ris
from .abc_triple_moment import power_enclosure


def _positive_int(n: int, name: str) -> None:
    if type(n) is not int or n < 1:
        raise ValueError(f"{name} must be a positive integer")


def divisors(n: int) -> tuple[int, ...]:
    _positive_int(n, "n")
    values = [1]
    for p, k in prime_factors(n):
        values = [d * p**j for d in values for j in range(k + 1)]
    return tuple(sorted(values))


def mobius(n: int) -> int:
    _positive_int(n, "n")
    factors = prime_factors(n)
    return 0 if any(k > 1 for _, k in factors) else (-1)**len(factors)


def powerful(n: int) -> bool:
    _positive_int(n, "n")
    return all(k >= 2 for _, k in prime_factors(n))


def g_integer(n: int, t: int) -> int:
    """Exact g_t=mu*f_t for nonnegative INTEGER t (no rounded real power)."""
    _positive_int(n, "n")
    if type(t) is not int or t < 0:
        raise ValueError("t must be a nonnegative integer")
    value = 1
    for p, k in prime_factors(n):
        if k == 1:
            return 0
        value *= p**(t * (k - 1)) - p**(t * (k - 2))
    return value


def progression_count(c: int, d: int, e: int) -> int:
    """Count 1<=a<c with d|a and e|(c-a), by generalized CRT and floors."""
    for name, value in (("c", c), ("d", d), ("e", e)):
        _positive_int(value, name)
    h = gcd(d, e)
    if c % h:
        return 0
    e1 = e // h
    x = 0 if e1 == 1 else ((c // h) * pow(d // h, -1, e1)) % e1
    r, modulus = d * x, d * e1
    return (c - 1 - r) // modulus - (-r) // modulus


def primitive_pair_count(c: int, d: int, e: int) -> int:
    """Exact primitive CRT count, with global Mobius inversion over divisors c."""
    for name, value in (("c", c), ("d", d), ("e", e)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d * e, c) != 1:
        return 0
    return sum(mobius(h) * progression_count(c, d * h, e) for h in divisors(c))


def primitive_divisor_count(X: int, d: int, e: int, f: int) -> int:
    """Exact count d|a,e|b,f|c in the primitive triangle; incompatible gives 0."""
    for name, value in (("X", X), ("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
        return 0
    return sum(primitive_pair_count(c, d, e) for c in range(f, X + 1, f))


def packing_upper(X: int, d: int, e: int, f: int) -> Fraction:
    """Universal primitive bound 1+X^2/(def); rejects missing hypotheses."""
    for name, value in (("X", X), ("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
        raise ValueError("packing theorem requires pairwise-coprime moduli")
    return 1 + Fraction(X * X, d * e * f)


def density_upper(X: int, d: int, e: int, f: int) -> Fraction:
    """Bound 2X^2/(def), available only when def<=X^2."""
    packing_upper(X, d, e, f)
    if d * e * f > X * X:
        raise ValueError("density-only bound requires def <= X^2")
    return Fraction(2 * X * X, d * e * f)


def inner_expansion(c: int, t: int, *, primitive: bool = False) -> int:
    """Exact additive divisor-congruence expansion, integer exponent only."""
    _positive_int(c, "c")
    g_integer(1, t)
    support = [(d, g_integer(d, t)) for d in range(1, c)]
    support = [(d, g) for d, g in support if g]
    counter = primitive_pair_count if primitive else progression_count
    return sum(gd * ge * counter(c, d, e)
               for d, gd in support for e, ge in support)


def triple_expansion(X: int, t: int) -> int:
    """Exact full primitive three-divisor expansion; finite holdout only."""
    _positive_int(X, "X")
    g_integer(1, t)
    support = [(d, g_integer(d, t)) for d in range(1, X + 1)]
    support = [(d, g) for d, g in support if g]
    return sum(gd * ge * gf * primitive_divisor_count(X, d, e, f)
               for d, gd in support for e, ge in support for f, gf in support)


def low_ris_divisor_gate(a: int, b: int, d: int, e: int, f: int) -> bool:
    """Check exact prerequisites and D<=ris(abc)^2; no claimed positive verdict."""
    for name, value in (("a", a), ("b", b), ("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    c = a + b
    if gcd(a, b) != 1 or a % d or b % e or c % f:
        raise ValueError("need primitive triple and divisors d|a,e|b,f|c")
    if not all(powerful(n) for n in (d, e, f)):
        raise ValueError("need powerful divisor support")
    return d * e * f <= ris(a * b * c)**2


@dataclass(frozen=True)
class MomentBudget:
    """Theorem constant <=2*2^low_power+(2/delta)*2^tail_power.

    This is an explicit very loose constant. The paper proof, not this
    dataclass or a successful finite check, supplies universal authority.
    """
    t: Fraction
    delta: Fraction
    eta: Fraction
    low_power: int
    tail_power: int

    def constant_upper(self) -> Fraction:
        return 2 * Fraction(2)**self.low_power + (2 / self.delta) * Fraction(2)**self.tail_power


def moment_budget(t: Fraction | int, *, precision: int = 10**6) -> MomentBudget:
    """Rational-power certified constants for rational 0<=t<2/3.

    Powers of two are encoded by integer exponents, avoiding giant printed
    integer certificates near the endpoint. Floats are deliberately rejected.
    """
    if type(t) not in (int, Fraction):
        raise ValueError("t must be an int or Fraction")
    t = Fraction(t)
    if not 0 <= t < Fraction(2, 3):
        raise ValueError("proved range is 0 <= t < 2/3")
    if type(precision) is not int or precision < 1:
        raise ValueError("precision must be a positive integer")
    delta = Fraction(2, 3) - t
    eta = delta / 2

    def lower_two_power(x: Fraction) -> Fraction:
        lo, _ = power_enclosure(2, x.numerator, x.denominator, precision)
        if lo <= 1:
            raise ValueError("increase precision to resolve the positive exponent")
        return lo

    one_minus = 1 - 1 / lower_two_power(1 - t)
    eta_minus = 1 - 1 / lower_two_power(eta)
    low_exp = 3 / ((1 - t) * one_minus)
    tail_exp = 2 / (eta * eta_minus)

    def ceiling(x: Fraction) -> int:
        return -((-x.numerator) // x.denominator)

    return MomentBudget(t, delta, eta, ceiling(2 * low_exp), ceiling(2 * tail_exp))


def powerful_singleton_witness() -> dict[str, int | bool | str]:
    """Counterexample to applying 2X²/D beyond its determinant gate."""
    a, b, c = 441, 400, 841
    D = a * b * c
    count = primitive_divisor_count(c, a, b, c)
    return {
        "a": a, "b": b, "c": c, "D": D, "X_squared": c*c,
        "all_powerful": all(powerful(n) for n in (a, b, c)),
        "primitive_count": count,
        "false_density_bound": str(Fraction(2*c*c, D)),
        "refutes_density_only": count > Fraction(2*c*c, D),
    }


def primitive_density_multiplier(d: int, e: int, f: int) -> Fraction:
    """Fixed-divisor density divided by 1/(2*zeta(2)), as an exact rational.

    This returns D^-1 prod_(p|D) p/(p+1), with zero for incompatible slots.
    The limiting theorem is proved in the dossier; this rational is not an
    automatically checked infinite certificate.
    """
    for name, value in (("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
        return Fraction(0)
    D = d * e * f
    value = Fraction(1, D)
    for p, _ in prime_factors(D):
        value *= Fraction(p, p+1)
    return value
