"""Exact finite controls for INSTITUTE_ATOMIC_HAAR.md, not an infinity oracle.

Cylinder functions are genuine locally constant functions on Zhat, represented
at a finite quotient. Division extends the period; it never inverts a nonunit
inside an unchanged finite residue ring. All scalar arithmetic is rational.
Write B_p = U_p/sqrt(p), C_p = sqrt(p) U_p*. Normalization is tested after
clearing those positive square roots.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, lcm, prod
from typing import Iterable


def _positive_integer(value: int) -> None:
    if type(value) is not int or value < 1:
        raise ValueError("expected a positive integer")


def _prime_family(primes: Iterable[int]) -> tuple[int, ...]:
    family = tuple(primes)
    for prime in family:
        _positive_integer(prime)
        if prime < 2 or any(prime % d == 0 for d in range(2, isqrt(prime) + 1)):
            raise ValueError("the index family must consist of primes")
    if len(family) != len(set(family)):
        raise ValueError("prime indices must be distinct")
    return tuple(sorted(family))


@dataclass(frozen=True)
class Cylinder:
    """A rational function on Zhat factoring through Z/period Z."""

    values: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if not self.values:
            raise ValueError("a cylinder has a nonempty residue table")
        if any(type(value) not in (int, Fraction) for value in self.values):
            raise TypeError("cylinder values must be exact rational numbers")
        object.__setattr__(self, "values", tuple(Fraction(x) for x in self.values))

    @property
    def period(self) -> int:
        return len(self.values)

    def __call__(self, integer: int) -> Fraction:
        return self.values[integer % self.period]

    def inner(self, other: "Cylinder") -> Fraction:
        """Real bilinear Haar pairing, evaluated at a common quotient."""
        period = lcm(self.period, other.period)
        return sum((self(i) * other(i) for i in range(period)), Fraction()) / period

    def multiply_pullback(self, factor: int) -> "Cylinder":
        """C_factor f(x) = f(factor*x)."""
        _positive_integer(factor)
        return Cylinder(tuple(self(factor * x) for x in range(self.period)))

    def divide_cutoff(self, factor: int) -> "Cylinder":
        """B_factor f(x) = 1_[factor Zhat](x) f(x/factor)."""
        _positive_integer(factor)
        return Cylinder(tuple(
            self(x // factor) if x % factor == 0 else Fraction()
            for x in range(factor * self.period)
        ))

    def equivalent(self, other: "Cylinder") -> bool:
        period = lcm(self.period, other.period)
        return all(self(i) == other(i) for i in range(period))


def haar_unit_mass(primes: Iterable[int]) -> Fraction:
    """The finite Euler product mu({x: p does not divide x for p in F})."""
    return prod((Fraction(p - 1, p) for p in _prime_family(primes)), start=Fraction(1))


def mobius_coefficients(primes: Iterable[int]) -> dict[int, int]:
    """Coefficients of product_(p in F) (I - range_projection_p)."""
    coefficients = {1: 1}
    for prime in _prime_family(primes):
        coefficients.update({prime * n: -sign for n, sign in tuple(coefficients.items())})
    return coefficients


def mobius_value(primes: Iterable[int], integer: int) -> int:
    _positive_integer(integer)
    return sum(sign for divisor, sign in mobius_coefficients(primes).items()
               if integer % divisor == 0)


def residue_unit_mass(primes: Iterable[int], *, maximum_period: int = 100_000) -> Fraction:
    """Independent finite quotient count; no Euler-product calculation."""
    family = _prime_family(primes)
    modulus = prod(family)
    if modulus > maximum_period:
        raise ValueError("finite residue enumeration exceeds the declared cap")
    return Fraction(sum(gcd(x, modulus) == 1 for x in range(modulus)), modulus)


def valuation_shell(primes: Iterable[int], exponents: Iterable[int]) -> Cylinder:
    """Indicator that each selected p-adic valuation equals its exponent."""
    original_primes = tuple(primes)
    _prime_family(original_primes)
    powers = tuple(exponents)
    if len(original_primes) != len(powers):
        raise ValueError("each selected prime needs one exponent")
    if any(type(k) is not int or k < 0 for k in powers):
        raise ValueError("valuation exponents must be nonnegative integers")
    modulus = prod(p ** (k + 1) for p, k in zip(original_primes, powers))
    if modulus > 100_000:
        raise ValueError("valuation shell exceeds the declared finite cap")
    return Cylinder(tuple(Fraction(all(
        x % p ** k == 0 and x % p ** (k + 1) != 0
        for p, k in zip(original_primes, powers)
    )) for x in range(modulus)))


def harmonic_pairing_norm_squared(size: int) -> Fraction:
    """Norm squared of a -> sum_(n<=size) a_n/sqrt(n)."""
    _positive_integer(size)
    return sum((Fraction(1, n) for n in range(1, size + 1)), Fraction())


def harmonic_graph_witness(size: int, period: int) -> dict:
    """Exact cylinder coordinates of a graph sequence tending to (0,Haar).

    The atomic coefficients are a_n=1/(sqrt(n)*H_size), n<=size.
    Squared source norm and all distributional cylinder masses are rational.
    This finite receipt supports AH7; the convergence proof is not a test.
    """
    _positive_integer(size)
    _positive_integer(period)
    harmonic = harmonic_pairing_norm_squared(size)
    masses = tuple(sum((Fraction(1, n) for n in range(1, size + 1)
                        if n % period == r), Fraction()) / harmonic
                   for r in range(period))
    bound = 1 / harmonic
    return {"source_norm_squared": bound, "masses": masses,
            "haar_cylinder_mass": Fraction(1, period),
            "coordinate_error_bound": bound}


def exact_control_report() -> dict:
    """Small reproducible controls; the universal theorem is a paper proof."""
    families = [(), (2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]
    constant = Cylinder((Fraction(1),))
    return {
        "authority": "EXACT_FINITE_CONTROLS_ONLY",
        "haar_unit_masses": [
            {"primes": list(family), "euler": str(haar_unit_mass(family)),
             "residue_count": str(residue_unit_mass(family)),
             "atomic_vacuum_survives": mobius_value(family, 1)}
            for family in families
        ],
        "missing_sqrt_two_mutation": {
            "atomic_vacuum_norm_squared": "1",
            "unnormalized_cutoff_norm_squared": str(
                constant.divide_cutoff(2).inner(constant.divide_cutoff(2))),
        },
        "omitted_prime_mutation": {
            "selected_primes": [2, 3, 5], "witness_integer": 7,
            "finite_projector_value": mobius_value((2, 3, 5), 7),
            "after_adding_7": mobius_value((2, 3, 5, 7), 7),
        },
        "unweighted_dirac_mutation": {
            "test": "constant_one", "prime": 2,
            "J_V2_e1_pairing_squared": str(constant(2) ** 2),
            "U2_distribution_J_e1_pairing_squared": str(
                constant.multiply_pullback(2)(1) ** 2 / 2),
        },
        "weak_dual_extension_obstruction": [
            {"cutoff": n, "functional_norm_squared": str(harmonic_pairing_norm_squared(n))}
            for n in (1, 2, 4, 8, 16, 64)
        ],
        "not_certified_by_finite_report": [
            "vanishing of the infinite Euler product",
            "strong operator convergence",
            "distributional support classification",
            "academic novelty",
        ],
    }


if __name__ == "__main__":
    import json
    print(json.dumps(exact_control_report(), indent=2, sort_keys=True))
