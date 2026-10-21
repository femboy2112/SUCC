"""Exact arithmetic for the Duck/BBP analytic research dossier.

These functions evaluate finite rational objects and theorem error budgets.
They do not decide normality, prove transcendence, or issue proof authority.
The rational-pole solver takes a COMPLETE supplied partial fraction list;
it is not a source-authentication or symbolic-factorization service.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Callable, Iterable


def _integer(value: int, minimum: int, name: str) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _rational(value: int | Fraction, name: str) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError(f"{name} must be an exact integer or Fraction")
    return Fraction(value)


def fractional_part(value: int | Fraction) -> Fraction:
    value = _rational(value, "value")
    return value - value.numerator // value.denominator


def circle_distance(left: int | Fraction, right: int | Fraction) -> Fraction:
    difference = fractional_part(_rational(left, "left") - _rational(right, "right"))
    return min(difference, 1 - difference)


def bbp_force(n: int) -> Fraction:
    """Independent four-fraction form, indexed from n=1."""
    _integer(n, 1, "n")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_force_positive_form(n: int) -> Fraction:
    """A three-positive-term identity, independent of polynomial expansion."""
    _integer(n, 1, "n")
    first = 8*n-7
    return (Fraction(6, first*(8*n-4)) + Fraction(4, first*(8*n-3))
            + Fraction(5, first*(8*n-2)))


def bbp_shadow_budget(n: int) -> Fraction:
    """Upper bound r(n+1)/15 for the infinite BBP shadow tail at n>=1.

    Positivity and monotonicity follow from the three-positive-term form.
    This is at most 1/(8*n+1)^2; its leading coefficient 1/64 is sharp.
    """
    _integer(n, 1, "n")
    return bbp_force_positive_form(n+1) / 15


def forced_orbit(force: Callable[[int], Fraction], base: int, length: int) -> tuple[Fraction, ...]:
    _integer(base, 2, "base")
    _integer(length, 0, "length")
    result = [Fraction(0)]
    for n in range(1, length + 1):
        result.append(fractional_part(base*result[-1] + _rational(force(n), "forcing")))
    return tuple(result)


def bbp_tail_partial(n: int, terms: int) -> tuple[Fraction, Fraction]:
    """Return a finite tail sum and a rigorous upper bound on its remainder.

    n>=1. The enclosure uses positivity and monotonicity of r(m).
    Its relation to Real.pi additionally uses the classical BBP identity.
    """
    _integer(n, 1, "n")
    _integer(terms, 0, "terms")
    total = sum((bbp_force(n+k) / 16**k for k in range(1, terms+1)), Fraction(0))
    remainder = bbp_shadow_budget(n+terms) / 16**terms
    return total, remainder


def square_tail_majorant(start: int, length: int) -> Fraction:
    """Upper bound for sum_{n=start}^{start+length-1} (n+1)^(-2)."""
    _integer(start, 1, "start")
    _integer(length, 0, "length")
    end = start + length
    return (Fraction(1, start) + Fraction(1, start+1)
            - Fraction(1, end) - Fraction(1, end+1)) / 2


def bbp_shadow_sum_budget(start: int, length: int) -> Fraction:
    """Bound sum of BBP shadow errors on a moving window, at most 1/40.

    Uses 1/(8*n+1)^2 <= 1/((8*n-3)*(8*n+5)) and telescopes.
    """
    _integer(start, 1, "start")
    _integer(length, 0, "length")
    return (Fraction(1, 8*start-3) - Fraction(1, 8*(start+length)-3)) / 8


def fourier_sum_transport_budget(h: int, start: int, length: int) -> Fraction:
    """Rational upper budget for the DIFFERENCE of BBP/digit Fourier sums.

    Uses |exp(2πihx)-exp(2πihy)| <= 2π|h|d(x,y), π<4,
    and d(x_n,16^(n-1)π)<=1/(8*n+1)^2. Not a bound on either sum.
    """
    if type(h) is not int:
        raise ValueError("h must be an integer")
    majorant = bbp_shadow_sum_budget(start, length)
    return min(Fraction(2*length), 8*abs(h)*majorant)


def arc_discrepancy_transport_budget(length: int) -> tuple[Fraction, int]:
    """Bound |D_arc(x[1:N])-D_arc(y[1:N])|, with optimal discarded prefix.

    This is the supremum discrepancy over ALL oriented circle arcs, not
    a claim that either discrepancy is itself small.
    """
    _integer(length, 1, "length")
    candidates = ((min(Fraction(1), Fraction(k, length) + 2*bbp_shadow_budget(k+1)), k)
                  for k in range(length+1))
    return min(candidates)


@dataclass(frozen=True)
class PoleTerm:
    pole: Fraction
    order: int
    coefficient: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "pole", _rational(self.pole, "pole"))
        _integer(self.order, 1, "pole order")
        object.__setattr__(self, "coefficient", _rational(self.coefficient, "coefficient"))


def _combine(terms: Iterable[PoleTerm]) -> tuple[PoleTerm, ...]:
    combined: dict[tuple[Fraction, int], Fraction] = {}
    for term in terms:
        if type(term) is not PoleTerm:
            raise ValueError("all terms must be PoleTerm instances")
        key = (term.pole, term.order)
        combined[key] = combined.get(key, Fraction(0)) + term.coefficient
    return tuple(PoleTerm(pole, order, coefficient)
                 for (pole, order), coefficient in sorted(combined.items()) if coefficient)


def weighted_pole_invariants(terms: Iterable[PoleTerm], base: int) -> dict[tuple[Fraction, int], Fraction]:
    """Orbit/order invariants for r(z)=base*q(z-1)-q(z).

    Poles are grouped as a+j with a in [0,1), j integral; the invariant
    is sum_j base**(-j)*coefficient_j. COMPLETE rational-pole input only.
    """
    _integer(base, 2, "base")
    result: dict[tuple[Fraction, int], Fraction] = {}
    for term in _combine(terms):
        shift = term.pole.numerator // term.pole.denominator
        key = (term.pole-shift, term.order)
        result[key] = result.get(key, Fraction(0)) + Fraction(base)**(-shift)*term.coefficient
    return result


def rational_coboundary(terms: Iterable[PoleTerm], base: int) -> tuple[PoleTerm, ...]:
    _integer(base, 2, "base")
    result = []
    for term in _combine(terms):
        result.extend((PoleTerm(term.pole+1, term.order, base*term.coefficient),
                       PoleTerm(term.pole, term.order, -term.coefficient)))
    return _combine(result)


def solve_rational_coboundary(terms: Iterable[PoleTerm], base: int) -> tuple[PoleTerm, ...] | None:
    """Exact solver on proper rational functions with supplied rational poles.

    Returns None precisely when a weighted orbit invariant is nonzero.
    Every returned finite certificate is replayed by rational_coboundary.
    """
    terms = _combine(terms)
    if any(weighted_pole_invariants(terms, base).values()):
        return None
    groups: dict[tuple[Fraction, int], dict[int, Fraction]] = {}
    for term in terms:
        shift = term.pole.numerator // term.pole.denominator
        key = (term.pole-shift, term.order)
        groups.setdefault(key, {})[shift] = term.coefficient
    answer = []
    for (residue, order), coefficients in groups.items():
        previous = Fraction(0)
        for shift in range(min(coefficients), max(coefficients)+1):
            previous = base*previous-coefficients.get(shift, Fraction(0))
            if previous:
                answer.append(PoleTerm(residue+shift, order, previous))
        if previous:
            raise ArithmeticError("internal boundary certificate failed")
    answer = _combine(answer)
    if rational_coboundary(answer, base) != terms:
        raise ArithmeticError("internal rational certificate replay failed")
    return answer


BBP_POLES = (PoleTerm(Fraction(7, 8), 1, Fraction(1, 2)),
             PoleTerm(Fraction(1, 2), 1, Fraction(-1, 4)),
             PoleTerm(Fraction(3, 8), 1, Fraction(-1, 8)),
             PoleTerm(Fraction(1, 4), 1, Fraction(-1, 8)))


def leading_matched_impostor(n: int) -> Fraction:
    """Positive rational forcing ~15/(64 n²), with a rational attractor."""
    _integer(n, 1, "n")
    return (Fraction(16, n*n) - Fraction(1, (n+1)**2)) / 64


@dataclass(frozen=True)
class PrefixImpostor:
    base: int
    initial: Fraction
    differences: tuple[Fraction, ...]
    denominator_power: int

    def __post_init__(self) -> None:
        _integer(self.base, 2, "base")
        initial = _rational(self.initial, "initial")
        differences = tuple(_rational(value, "difference") for value in self.differences)
        if not differences or differences[0] != initial:
            raise ValueError("nonempty differences must encode the stated initial value")
        _integer(self.denominator_power, len(differences)+1, "denominator power")
        object.__setattr__(self, "initial", initial)
        object.__setattr__(self, "differences", differences)

    def correction(self, n: int) -> Fraction:
        _integer(n, 0, "n")
        return sum((coefficient*comb(n, k) for k, coefficient in enumerate(self.differences)
                    if k <= n), Fraction(0)) / (n+1)**self.denominator_power

    def force(self, n: int) -> Fraction:
        _integer(n, 1, "n")
        return self.base*self.correction(n-1)-self.correction(n)


def prefix_impostor(samples: Iterable[Fraction], base: int = 16,
                    initial: Fraction = Fraction(0)) -> PrefixImpostor:
    """Fit ANY finite forcing prefix by a rational telescoping impostor.

    q(n)=P(n)/(n+1)^(L+2), deg P<=L; r(n)=base*q(n-1)-q(n).
    It matches the L input samples and has q(n)=O(n^-2), rational q(0).
    The shadow radix orbit is rational. No positivity promise is made.
    """
    _integer(base, 2, "base")
    initial = _rational(initial, "initial")
    samples = tuple(_rational(sample, "sample") for sample in samples)
    values = [initial]
    for sample in samples:
        values.append(base*values[-1]-sample)
    power = len(samples)+2
    row = [value*(n+1)**power for n, value in enumerate(values)]
    differences = []
    while row:
        differences.append(row[0])
        row = [right-left for left, right in zip(row, row[1:])]
    return PrefixImpostor(base, initial, tuple(differences), power)
