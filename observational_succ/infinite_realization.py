"""Infinite realization of finite observation: a bounded, exact Ind/Yoneda model.

Finite stages L_N=lcm(1,...,N) are never the terminal divisibility object.
The filtered colimit of their representables IS the terminal presheaf;
this is an ind-object, not a finite integer or the Archimedean place.

Also provides independent rational Cauchy enclosures for e, pi and zeta(s>1),
plus an exact countermodel showing why finite-stage indefinite forms can
converge pointwise to a positive global form. Nothing is an RH certificate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Mapping

from .arithmetic import factorization
from .core import BudgetExceeded, DomainError
from .resource_probe import ValuationWord, lcm_word


def _index(n: int, *, lower: int = 1, upper: int = 10000, name: str = "index") -> int:
    if type(n) is not int:
        raise DomainError(f"{name} must be an exact integer, not a float or boolean")
    if not lower <= n <= upper:
        raise BudgetExceeded(f"{name} must be in {lower}..{upper}")
    return n


def _rational(x) -> Fraction:
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise DomainError("Only exact integer or Fraction values, not floats")


@dataclass(frozen=True)
class RationalEnclosure:
    """A finite proof-bearing interval; NOT the limiting real itself."""

    lower: Fraction
    upper: Fraction
    origin: str

    def __post_init__(self):
        lower, upper = _rational(self.lower), _rational(self.upper)
        if lower > upper or not isinstance(self.origin, str) or not self.origin:
            raise DomainError("A valid rational enclosure and provenance are required")
        object.__setattr__(self, "lower", lower)
        object.__setattr__(self, "upper", upper)

    @property
    def width(self):
        return self.upper - self.lower

    def nested_in(self, older: "RationalEnclosure") -> bool:
        if not isinstance(older, RationalEnclosure):
            raise DomainError("Compare rational enclosures")
        return older.lower <= self.lower <= self.upper <= older.upper

    def contains_rational(self, q) -> bool:
        q = _rational(q)
        return self.lower <= q <= self.upper

    def report(self):
        return {"lower": str(self.lower), "upper": str(self.upper),
                "width": str(self.width), "method": self.origin,
                "status": "finite enclosure, not the exact realized infinite limit"}


def e_enclosure(n: int) -> RationalEnclosure:
    """Certified e=exp(1) from the factorial series; n=0,..,64.

    After 1/(n+1)!, successive tail ratios are at most 1/(n+2).
    Thus remainder <= (n+2)/((n+1)(n+1)!), strictly for n>=0.
    """
    _index(n, lower=0, upper=64, name="e truncation")
    partial = sum((Fraction(1, factorial(k)) for k in range(n + 1)), Fraction())
    remainder = Fraction(n + 2, (n + 1) * factorial(n + 1))
    return RationalEnclosure(partial, partial + remainder, "exp Taylor tail")


def _atan_unit_fraction_enclosure(denominator: int, n: int) -> RationalEnclosure:
    _index(denominator, lower=2, upper=10000, name="arctan denominator")
    _index(n, lower=0, upper=64, name="arctan truncation")
    partial = sum((Fraction((-1)**k, (2*k+1)*denominator**(2*k+1))
                   for k in range(n + 1)), Fraction())
    next_term = Fraction(1, (2*n+3)*denominator**(2*n+3))
    # Alternating-series sign, not merely an absolute error estimate.
    if n % 2 == 0:
        return RationalEnclosure(partial-next_term, partial, "alternating arctan")
    return RationalEnclosure(partial, partial+next_term, "alternating arctan")


def pi_enclosure(n: int) -> RationalEnclosure:
    """Certified Machin identity pi=16atan(1/5)-4atan(1/239).

    The identity itself follows by tangent addition:
    tan(4atan(1/5))=120/119 and
    tan(4atan(1/5)-atan(1/239))=1, with the angle in (0,pi/2).
    """
    a, b = _atan_unit_fraction_enclosure(5, n), _atan_unit_fraction_enclosure(239, n)
    return RationalEnclosure(16*a.lower-4*b.upper, 16*a.upper-4*b.lower,
                             "Machin identity and alternating arctan bounds")


def zeta_euler_enclosure(n: int, exponent: int = 2) -> RationalEnclosure:
    """Only the safe real Euler half-plane, integer s>=2.

    Integral comparison: sum_{k>n} k^-s < n^(1-s)/(s-1).
    No analytic continuation, zero location or RH claim.
    """
    _index(n, lower=1, upper=2000, name="Dirichlet horizon")
    _index(exponent, lower=2, upper=8, name="integer s")
    partial = sum((Fraction(1, k**exponent) for k in range(1, n+1)), Fraction())
    return RationalEnclosure(partial, partial+Fraction(1, (exponent-1)*n**(exponent-1)),
                             "Euler-region Dirichlet series and integral tail")


def _is_prime_power(n: int) -> bool:
    return len(factorization(n)) == 1


@dataclass(frozen=True)
class LCMIndRealization:
    """Finite stages with explicit probe-relative shadows of an ind-object.

    The unlimited terminal profile is a mathematical theorem about the entire
    filtered diagram, not a runtime infinite computation.
    """

    def stage(self, horizon: int) -> ValuationWord:
        _index(horizon, name="finite realization horizon")
        return lcm_word(horizon)

    def observed_probe(self, horizon: int, query: int) -> bool:
        _index(horizon, name="finite observation horizon")
        _index(query, upper=horizon, name="permitted probe label")
        # The result is true by the defining lcm property, not an assumed oracle.
        assert self.stage(horizon).divisible_by(query)
        return True

    def hypothetical_probe(self, horizon: int, query: int) -> bool:
        """Extra probes DO NOT count as observations within horizon."""
        _index(horizon, name="finite observation horizon")
        _index(query, upper=1_000_000, name="counterfactual probe")
        return self.stage(horizon).divisible_by(query)

    def activation_stage(self, query: int) -> int:
        """Finite stage when the named probe becomes stably true."""
        _index(query, upper=1_000_000, name="finite probe")
        return max((p**k for p, k in factorization(query)), default=1)

    def verify_compatibility(self, old: int, new: int) -> bool:
        """Every earlier source divisibility answer remains true."""
        _index(old)
        _index(new)
        if new < old:
            raise DomainError("Realization horizon may not move backward")
        a, b = self.stage(old), self.stage(new)
        return all(b.exponent(p) >= k for p, k in a.factors)

    def first_missed_prime_power(self, horizon: int) -> int:
        """First genuinely new probe. It is always a prime power."""
        _index(horizon, name="finite observation horizon")
        j = horizon + 1
        while not _is_prime_power(j):
            j += 1
        assert not self.stage(horizon).divisible_by(j)
        return j

    def nonrepresentability_witness(self, finite_integer: int) -> int:
        """j=m+1 is a finite probe on which h_m differs from terminal F_inf."""
        _index(finite_integer, upper=1_000_000, name="finite candidate")
        return finite_integer + 1  # m+1 never divides m

    def limit_profile(self, finite_queries) -> dict:
        """Sample a theorem about the Ind-limit; never claim that it was run."""
        qs = tuple(finite_queries)
        if not qs or len(qs) > 256:
            raise BudgetExceeded("A nonempty finite sample of <=256 probes is required")
        for j in qs:
            _index(j, upper=1_000_000, name="test probe")
        stage = max(self.activation_stage(j) for j in qs)
        return {
            "queries": list(qs),
            "joint_eventual_stage": stage,
            "all_true_from_that_stage": True,
            "limit_object": "terminal divisibility presheaf, ind-representable",
            "represented_by_finite_integer": False,
            "scope": "theorem on a declared infinite diagram; not an executed infinity",
        }


def escaping_defect_form(horizon: int, vector: Mapping[int, object]) -> Fraction:
    """Q_N(x)=||x||^2-2|x_N|^2 on finitely supported rational l2 vectors.

    Q_N(e_N)=-1 for every finite N, but Q_N(x) is eventually ||x||^2
    for *every fixed* finitely supported x. Hence pointwise limit is PSD
    even though NO finite Q_N is PSD. Generic analogy, RH-inert.
    """
    _index(horizon, upper=1_000_000, name="form stage")
    if not isinstance(vector, Mapping) or len(vector) > 10000:
        raise BudgetExceeded("Finitely supported mapping with <=10000 entries required")
    norm = Fraction(0)
    picked = Fraction(0)
    for k, raw in vector.items():
        _index(k, upper=1_000_000, name="basis coordinate")
        a = _rational(raw)
        norm += a*a
        if k == horizon:
            picked = a
    return norm - 2*picked*picked


def escaping_defect_limit(vector: Mapping[int, object]) -> tuple[Fraction, int]:
    """Exact limit value and stage AFTER which all Q_N match that value."""
    if not isinstance(vector, Mapping) or len(vector) > 10000:
        raise BudgetExceeded("Finitely supported rational vector required")
    norm = Fraction(0)
    final_support = 0
    for k, raw in vector.items():
        _index(k, upper=1_000_000, name="basis coordinate")
        a = _rational(raw)
        norm += a*a
        if a:
            final_support = max(final_support, k)
    return norm, final_support + 1


def pinned_negative_form(horizon: int, vector: Mapping[int, object]) -> Fraction:
    """Adversarial control: same finite indefiniteness but a NEGATIVE limit.

    R_N(x)=||x||^2-2|x_1|^2 is indefinite for all N, and the negative
    direction e_1 NEVER escapes. Finite indefinite signatures alone do not
    tell us whether the limiting form will be positive.
    """
    _index(horizon, upper=1_000_000, name="form stage")
    norm, _ = escaping_defect_limit(vector)
    anchor = _rational(vector.get(1, 0))
    return norm - 2*anchor*anchor
