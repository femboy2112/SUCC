"""Exact finite controls for the fixed complex-bank obstruction.

The paper theorem permits arbitrary complex nodes. These controls use Q(i)
so every phase, sign, source count and triangle identity is exact. A finite
prefix check never certifies an all-grade minorant or an asymptotic claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, prod


def rational(value):
    if type(value) not in (int, F):
        raise ValueError("exact int or Fraction required")
    return F(value)


def natural(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("integer outside the permitted range")
    return value


@dataclass(frozen=True)
class Gaussian:
    real: F = F(0)
    imag: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "real", rational(self.real))
        object.__setattr__(self, "imag", rational(self.imag))

    def __add__(self, other):
        other = exact_complex(other)
        return Gaussian(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-exact_complex(other))

    def __rsub__(self, other):
        return exact_complex(other) - self

    def __mul__(self, other):
        other = exact_complex(other)
        return Gaussian(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = exact_complex(other)
        norm = other.norm_squared()
        if not norm:
            raise ValueError("zero divisor")
        numerator = self * other.conjugate()
        return Gaussian(numerator.real / norm, numerator.imag / norm)

    def __rtruediv__(self, other):
        return exact_complex(other) / self

    def __pow__(self, exponent):
        natural(exponent)
        answer, base = Gaussian(1), self
        while exponent:
            if exponent % 2:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer

    def conjugate(self):
        return Gaussian(self.real, -self.imag)

    def norm_squared(self):
        return self.real * self.real + self.imag * self.imag


def exact_complex(value):
    if type(value) is Gaussian:
        return value
    return Gaussian(rational(value))


ZERO, ONE, I = Gaussian(), Gaussian(1), Gaussian(0, 1)


@dataclass(frozen=True)
class Bank:
    """A normalized conjugation-paired bank, with NO global sign assertion."""

    terms: tuple

    def __post_init__(self):
        terms = tuple((exact_complex(z), exact_complex(b)) for z, b in self.terms)
        if not terms or len({z for z, _ in terms}) != len(terms):
            raise ValueError("nonempty bank with distinct nodes required")
        if any(z == ZERO or z.norm_squared() > 1 or b == ZERO for z, b in terms):
            raise ValueError("nonzero nodes and coefficients, with |z| <= 1, required")
        lookup = dict(terms)
        if any(lookup.get(z.conjugate()) != b.conjugate() for z, b in terms):
            raise ValueError("nodes and coefficients must be conjugation paired")
        if sum((b for _, b in terms), ZERO) != ONE:
            raise ValueError("q(0) must equal one")
        object.__setattr__(self, "terms", terms)

    def evaluate(self, grade):
        natural(grade)
        value = sum((b * z**grade for z, b in self.terms), ZERO)
        if value.imag:
            raise ArithmeticError("paired bank returned a nonreal value")
        return value.real

    def first_positive_grade(self, through):
        """Return a witnessed failure in this finite range, never a proof."""
        natural(through)
        return next((h for h in range(1, through + 1) if self.evaluate(h) > 0), None)

    def dominant_circle(self):
        radius_squared = max(z.norm_squared() for z, _ in self.terms)
        terms = tuple((z, b) for z, b in self.terms if z.norm_squared() == radius_squared)
        positive_coefficient = next(
            (b.real for z, b in terms if z.imag == 0 and z.real > 0), F(0)
        )
        return {
            "radius_squared": radius_squared,
            "positive_real_coefficient": positive_coefficient,
            "energy": sum((b.norm_squared() for _, b in terms), F(0)),
            "terms": terms,
        }


def canonical_bank(terms):
    merged = {}
    for z, b in terms:
        z, b = exact_complex(z), exact_complex(b)
        merged[z] = merged.get(z, ZERO) + b
    return Bank(tuple((z, b) for z, b in merged.items() if b != ZERO))


def twist_bank(bank, strength=1):
    """Multiply q(h) by 1 + strength*(1-cos(pi*h/2)), which is >= 1."""
    strength = rational(strength)
    if strength < 0:
        raise ValueError("nonnegative twist strength required")
    terms = []
    for z, b in bank.terms:
        terms.extend(((z, (1 + strength) * b),
                      (I * z, -strength * b / 2),
                      (-I * z, -strength * b / 2)))
    return canonical_bank(terms)


def two_node_minorant(radius=1, inner=F(1, 2)):
    """q(h)=(radius*inner^h-inner*radius^h)/(radius-inner)."""
    radius, inner = rational(radius), rational(inner)
    if not 0 < inner < radius <= 1:
        raise ValueError("require 0 < inner < radius <= 1")
    return Bank(((Gaussian(inner), Gaussian(radius / (radius - inner))),
                 (Gaussian(radius), Gaussian(-inner / (radius - inner)))))


def damped_minorant(order, damping=F(1, 2)):
    """Even-order geometric extrapolation; the all-grade proof is in the note."""
    natural(order, 2)
    damping = rational(damping)
    if order % 2 or not 0 < damping <= F(1, 2):
        raise ValueError("positive even order and 0 < damping <= 1/2 required")
    nodes = [damping**r for r in range(1, order + 1)]
    weights = [prod(-nodes[s] / (nodes[r] - nodes[s])
                    for s in range(order) if s != r)
               for r in range(order)]
    return Bank(tuple((Gaussian(z), Gaussian(b)) for z, b in zip(nodes, weights)))


def finite_prefix_impostor():
    """q(h)=(i^h+(-1)^h+(-i)^h)/3; first false minorant grade is 4."""
    return Bank(((I, Gaussian(F(1, 3))),
                 (Gaussian(-1), Gaussian(F(1, 3))),
                 (-I, Gaussian(F(1, 3)))))


def omega_sieve(limit):
    natural(limit, 1)
    smallest = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if smallest[p] == p:
            for m in range(p * p, limit + 1, p):
                if smallest[m] == m:
                    smallest[m] = p
    omega = [0] * (limit + 1)
    for m in range(2, limit + 1):
        omega[m] = omega[m // smallest[m]] + 1
    return tuple(omega)


def _source_node(z):
    z = exact_complex(z)
    if z == ZERO or z.norm_squared() > 1:
        raise ValueError("source node must satisfy 0 < |z| <= 1")
    return z


def source_response(z, midpoint):
    z = _source_node(z)
    natural(midpoint, 2)
    omega = omega_sieve(2 * midpoint)
    return sum((z**(omega[midpoint + a] + omega[midpoint - a] - 2)
                for a in range(midpoint - 1)), ZERO)


def bank_response(bank, midpoint):
    natural(midpoint, 2)
    omega = omega_sieve(2 * midpoint)
    return sum((bank.evaluate(omega[midpoint + a] + omega[midpoint - a] - 2)
                for a in range(midpoint - 1)), F(0))


def source_cumulative_direct(z, cutoff):
    natural(cutoff, 2)
    return sum((source_response(z, n) for n in range(2, cutoff + 1)), ZERO)


def source_cumulative_triangle(z, cutoff):
    """Ordered parity triangle plus the algebraic (not modulus) diagonal."""
    z = _source_node(z)
    natural(cutoff, 2)
    bound = 2 * cutoff
    omega = omega_sieve(bound)
    weights = [ZERO, ZERO] + [z**(omega[m] - 1) for m in range(2, bound + 1)]
    prefixes = [[ZERO] * (bound + 1) for _ in range(2)]
    for m in range(1, bound + 1):
        for parity in (0, 1):
            prefixes[parity][m] = prefixes[parity][m - 1]
        prefixes[m % 2][m] = prefixes[m % 2][m] + weights[m]
    triangle = sum((weights[m] * prefixes[m % 2][bound - m]
                    for m in range(2, bound - 1)), ZERO)
    diagonal = sum((weights[m]**2 for m in range(2, cutoff + 1)), ZERO)
    return (triangle + diagonal) / 2


def cumulative_bank(bank, cutoff):
    natural(cutoff, 2)
    return sum((bank_response(bank, n) for n in range(2, cutoff + 1)), F(0))


def control_report():
    bank = twist_bank(two_node_minorant())
    impostor = finite_prefix_impostor()
    return {
        "scope": "Exact finite Q(i) controls; no numerical asymptotic inference.",
        "true_minorant_cumulative_2_through_6":
            [str(cumulative_bank(bank, n)) for n in range(2, 7)],
        "true_minorant_dominant_coefficient":
            str(bank.dominant_circle()["positive_real_coefficient"]),
        "impostor_first_positive_grade": impostor.first_positive_grade(8),
        "impostor_has_positive_dominant_node":
            any(z.imag == 0 and z.real > 0 for z, _ in impostor.terms),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(control_report(), indent=2))
