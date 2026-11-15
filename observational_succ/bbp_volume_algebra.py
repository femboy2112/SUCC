"""Bounded exact algebra for labelled causal sums and rational BBP lifts.

The universal identities are proved in
research/2026-11-15/bbp_volume_algebra/THEOREMS.md.  A word is an inclusive,
zero-seeded nested Green sum.  Its source factors and each stage's radix
remain visible.  Products normalize by a radix-graded quasi-shuffle rule.
This is a sound finite fragment, not an equality oracle for all sequences,
an infinite phase expansion, or a signed asymptotic cancellation theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from typing import Mapping, Sequence


MAX_DEPTH = 8
MAX_TERMS = 20_000
MAX_HORIZON = 256
MAX_POLYNOMIAL_DEGREE = 16
MAX_GAMMA_GRADE = 256


def _rational(value: int | Q, name: str) -> Q:
    if type(value) not in (int, Q):
        raise TypeError(f"{name} must be an int or Fraction; no floats or booleans")
    return Q(value)


def _natural(value: int, name: str, maximum: int | None = None) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a natural number")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} exceeds the declared budget {maximum}")
    return value


@dataclass(frozen=True, order=True)
class Stage:
    """G_radix(product of labelled source channels times the remaining word)."""

    radix: Q
    factors: tuple[str, ...]

    def __post_init__(self) -> None:
        radix = _rational(self.radix, "radix")
        if radix <= 0:
            raise ValueError("positive rational radix required")
        if type(self.factors) is not tuple or any(
            type(label) is not str or not label for label in self.factors
        ):
            raise TypeError("source factors must be a tuple of nonempty labels")
        object.__setattr__(self, "radix", radix)
        object.__setattr__(self, "factors", tuple(sorted(self.factors)))


Word = tuple[Stage, ...]


def _word(word: Word) -> Word:
    if type(word) is not tuple or any(type(stage) is not Stage for stage in word):
        raise TypeError("a word must be a tuple of Stage objects")
    if len(word) > MAX_DEPTH:
        raise ValueError("word exceeds the declared depth budget")
    return word


def _collect(items: Sequence[tuple[Word, Q]]) -> tuple[tuple[Word, Q], ...]:
    coefficients: dict[Word, Q] = {}
    for word, coefficient in items:
        word = _word(word)
        coefficient = _rational(coefficient, "coefficient")
        total = coefficients.get(word, Q(0)) + coefficient
        if total:
            coefficients[word] = total
        else:
            coefficients.pop(word, None)
        if len(coefficients) > MAX_TERMS:
            raise ValueError("normal form exceeds the declared term budget")
    return tuple(sorted(coefficients.items()))


@dataclass(frozen=True)
class WordPolynomial:
    """Canonical coefficient collection for this chosen word representation.

    Equality means equality of these formal terms.  Different formal words
    can evaluate equally on a special source, so inequality is not a semantic
    non-equality certificate.  The empty word evaluates to the constant one.
    """

    terms: tuple[tuple[Word, Q], ...] = ()

    def __post_init__(self) -> None:
        if type(self.terms) is not tuple:
            raise TypeError("terms must be a tuple")
        object.__setattr__(self, "terms", _collect(self.terms))

    @classmethod
    def one(cls) -> WordPolynomial:
        return cls((((), Q(1)),))

    @classmethod
    def atom(cls, radix: int | Q, label: str) -> WordPolynomial:
        word = (Stage(radix, (label,)),)
        return cls(((word, Q(1)),))

    def scale(self, coefficient: int | Q) -> WordPolynomial:
        coefficient = _rational(coefficient, "coefficient")
        return WordPolynomial(tuple((w, c * coefficient) for w, c in self.terms))

    def __add__(self, other: WordPolynomial) -> WordPolynomial:
        if type(other) is not WordPolynomial:
            return NotImplemented
        return WordPolynomial(self.terms + other.terms)

    def __mul__(self, other: WordPolynomial) -> WordPolynomial:
        if type(other) is not WordPolynomial:
            return NotImplemented
        terms: dict[Word, Q] = {}
        for left, a in self.terms:
            for right, b in other.terms:
                if len(left) + len(right) > MAX_DEPTH:
                    raise ValueError("product exceeds the declared depth budget")
                for word, coefficient in _multiply_words(left, right):
                    total = terms.get(word, Q(0)) + a * b * coefficient
                    if total:
                        terms[word] = total
                    else:
                        terms.pop(word, None)
                    if len(terms) > MAX_TERMS:
                        raise ValueError("product exceeds the declared term budget")
        return WordPolynomial(tuple(terms.items()))

    def power(self, degree: int) -> WordPolynomial:
        _natural(degree, "degree", MAX_DEPTH)
        result = WordPolynomial.one()
        for _ in range(degree):
            result = result * self
        return result


@lru_cache(maxsize=4096)
def _multiply_words(left: Word, right: Word) -> tuple[tuple[Word, Q], ...]:
    if not left:
        return ((right, Q(1)),)
    if not right:
        return ((left, Q(1)),)
    a, b = left[0], right[0]
    radix = a.radix * b.radix
    terms: list[tuple[Word, Q]] = []
    choices = (
        (Stage(radix, a.factors), left[1:], right, Q(1)),
        (Stage(radix, b.factors), left, right[1:], Q(1)),
        (Stage(radix, a.factors + b.factors), left[1:], right[1:], Q(-1)),
    )
    for stage, ltail, rtail, sign in choices:
        for word, coefficient in _multiply_words(ltail, rtail):
            terms.append(((stage,) + word, sign * coefficient))
    return _collect(terms)


def green_sum(values: Sequence[int | Q], radix: int | Q, seed: int | Q = 0) -> tuple[Q, ...]:
    """Return F_0=seed and F_n=radix*F_(n-1)+values[n-1]."""
    _natural(len(values), "horizon", MAX_HORIZON)
    radix = _rational(radix, "radix")
    seed = _rational(seed, "seed")
    if radix <= 0:
        raise ValueError("positive rational radix required")
    result = [seed]
    for value in values:
        result.append(radix * result[-1] + _rational(value, "source value"))
    return tuple(result)


def evaluate(
    expression: WordPolynomial,
    channels: Mapping[str, Sequence[int | Q]],
    horizon: int,
) -> tuple[Q, ...]:
    """Evaluate a finite labelled expression without forgetting its clock.

    Channel row j-1 supplies the source value at time j.  Every supplied row
    must cover exactly the declared horizon; a missing channel fails closed.
    """
    if type(expression) is not WordPolynomial:
        raise TypeError("expected a WordPolynomial")
    _natural(horizon, "horizon", MAX_HORIZON)
    table: dict[str, tuple[Q, ...]] = {}
    for label, row in channels.items():
        if type(label) is not str or not label:
            raise TypeError("source labels must be nonempty strings")
        if len(row) != horizon:
            raise ValueError("source row length does not match the declared horizon")
        table[label] = tuple(_rational(v, "source value") for v in row)
    needed = {f for word, _ in expression.terms for stage in word for f in stage.factors}
    if not needed.issubset(table):
        raise ValueError(f"missing source channels: {sorted(needed - table.keys())}")
    cache: dict[Word, tuple[Q, ...]] = {(): (Q(1),) * (horizon + 1)}

    def evaluate_word(word: Word) -> tuple[Q, ...]:
        if word in cache:
            return cache[word]
        stage, tail = word[0], word[1:]
        inside = evaluate_word(tail)
        driver = []
        for n in range(1, horizon + 1):
            value = inside[n]
            for factor in stage.factors:
                value *= table[factor][n - 1]
            driver.append(value)
        cache[word] = green_sum(driver, stage.radix)
        return cache[word]

    result = [Q(0)] * (horizon + 1)
    for word, coefficient in expression.terms:
        row = evaluate_word(word)
        result = [a + coefficient * b for a, b in zip(result, row)]
    return tuple(result)


BBP_POLES = (("pole_1", 1, 4), ("pole_4", 4, -2), ("pole_5", 5, -1), ("pole_6", 6, -1))


def bbp_channels(horizon: int) -> dict[str, tuple[Q, ...]]:
    _natural(horizon, "horizon", MAX_HORIZON)
    return {
        label: tuple(Q(1, 8 * n + offset) for n in range(horizon))
        for label, offset, _ in BBP_POLES
    }


def bbp_expression() -> WordPolynomial:
    """The original four signed poles, radix 16, and zero seed, without pi input."""
    result = WordPolynomial()
    for label, _, coefficient in BBP_POLES:
        result = result + WordPolynomial.atom(16, label).scale(coefficient)
    return result


def polynomial_lift_matrix(radix: int | Q, forcing: int | Q, degree: int) -> tuple[tuple[Q, ...], ...]:
    """Exact action on (1,u,...,u^degree) under u -> radix*u+forcing."""
    radix = _rational(radix, "radix")
    forcing = _rational(forcing, "forcing")
    _natural(degree, "degree", MAX_POLYNOMIAL_DEGREE)
    if radix <= 0:
        raise ValueError("positive rational radix required")
    return tuple(
        tuple(Q(comb(k, j)) * radix**j * forcing ** (k - j) if j <= k else Q(0)
              for j in range(degree + 1))
        for k in range(degree + 1)
    )


@dataclass(frozen=True)
class RationalLift:
    """Exact integer lift plus a canonical fractional representative in [0,1)."""

    integer: int
    fraction: Q

    def __post_init__(self) -> None:
        if type(self.integer) is not int:
            raise TypeError("integer lift must be an int")
        fraction = _rational(self.fraction, "fraction")
        if not 0 <= fraction < 1:
            raise ValueError("fraction must lie in [0,1)")
        object.__setattr__(self, "fraction", fraction)

    @classmethod
    def from_rational(cls, value: int | Q) -> RationalLift:
        value = _rational(value, "value")
        integer = value.numerator // value.denominator
        return cls(integer, value - integer)

    @property
    def value(self) -> Q:
        return self.integer + self.fraction


@dataclass(frozen=True)
class AffineStep:
    """Integer dilation and rational forcing, with chronological composition."""

    radix: int
    forcing: Q

    def __post_init__(self) -> None:
        if type(self.radix) is not int or self.radix < 1:
            raise ValueError("circle-compatible positive integer radix required")
        object.__setattr__(self, "forcing", _rational(self.forcing, "forcing"))

    def after(self, earlier: AffineStep) -> AffineStep:
        if type(earlier) is not AffineStep:
            raise TypeError("expected an AffineStep")
        return AffineStep(self.radix * earlier.radix,
                          self.radix * earlier.forcing + self.forcing)

    def apply(self, state: RationalLift) -> tuple[RationalLift, int]:
        if type(state) is not RationalLift:
            raise TypeError("expected a RationalLift")
        raw_fraction = self.radix * state.fraction + self.forcing
        carry = raw_fraction.numerator // raw_fraction.denominator
        return RationalLift(self.radix * state.integer + carry,
                            raw_fraction - carry), carry


def phase_residue(value: int | Q, harmonic: int = 1) -> Q:
    """Exact exponent modulo one, not an approximate complex root of unity."""
    if type(harmonic) is not int:
        raise TypeError("harmonic must be an integer")
    value = harmonic * _rational(value, "value")
    return value - value.numerator // value.denominator


def carry_cocycle(left: int | Q, right: int | Q) -> int:
    """The additive section defect floor({left}+{right})."""
    total = RationalLift.from_rational(left).fraction + RationalLift.from_rational(right).fraction
    return total.numerator // total.denominator


def lift_moduli(weights: Sequence[int | Q], harmonic: int = 1) -> tuple[int, ...]:
    """Minimal coordinatewise integer-lift moduli for phase after a real sum.

    Fundamental input phases exp(2*pi*i*U_j), equivalently U_j modulo one,
    suffice exactly when all returned moduli equal 1.  Input phases only at
    harmonic h forget additional fractional information when abs(h)>1.
    This statement quantifies over arbitrary finite rational lifts, not over
    free re-seedings of the fixed BBP orbit.
    """
    if type(harmonic) is not int:
        raise TypeError("harmonic must be an integer")
    return tuple((harmonic * _rational(w, "weight")).denominator for w in weights)


def integer_gamma_weights(shape: int, last_grade: int, rate: int | Q = 1) -> tuple[Q, ...]:
    """A prefix of (rate/(rate+1-z))**shape; never renormalize omitted mass."""
    if type(shape) is not int or not 1 <= shape <= MAX_POLYNOMIAL_DEGREE:
        raise ValueError("positive integer shape within budget required")
    _natural(last_grade, "last grade", MAX_GAMMA_GRADE)
    rate = _rational(rate, "rate")
    if rate <= 0:
        raise ValueError("positive Gamma rate required")
    return tuple(Q(comb(j + shape - 1, j)) * rate**shape / (rate + 1)**(j + shape)
                 for j in range(last_grade + 1))


def gamma_geometric_sum(shape: int, rate: int | Q, growth: int | Q) -> Q:
    """Sum of Gamma weights times growth**j, with the convergence gate intact.

    For nonnegative growth >= rate+1 the positive series diverges.  A formal
    rational resolvent value is not returned in place of that series.
    """
    if type(shape) is not int or not 1 <= shape <= MAX_POLYNOMIAL_DEGREE:
        raise ValueError("positive integer shape within budget required")
    rate = _rational(rate, "rate")
    growth = _rational(growth, "growth")
    if rate <= 0 or growth < 0:
        raise ValueError("positive rate and nonnegative growth required")
    if growth >= rate + 1:
        raise ValueError("Gamma series diverges: growth must be strictly below rate+1")
    return (rate / (rate + 1 - growth))**shape
