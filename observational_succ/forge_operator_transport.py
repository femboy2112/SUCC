"""Exact finite controls for the Forge II atomic/Haar transport theorem.

These rational cylinder computations do not certify an infinite limit.  The
proof is in research/2026-10-19/PAPER_B_ATOMIC_HAAR_TRANSPORT.tex.  This module
is independent of the sibling PR178 implementation: no truncated quotient is
mistaken for an injective profinite dilation.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, lcm, prod
from typing import Iterable, Mapping


def _positive_integer(value: int) -> int:
    if type(value) is not int or value < 1:
        raise ValueError("expected a positive exact integer")
    return value


def _rational(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError("expected an exact integer or Fraction")
    return Fraction(value)


def prime_set(values: Iterable[int]) -> tuple[int, ...]:
    values = tuple(values)
    for p in values:
        _positive_integer(p)
        if p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            raise ValueError("selected factors must be prime")
    if len(set(values)) != len(values):
        raise ValueError("selected primes must be distinct")
    return tuple(sorted(values))


def valuation(n: int, p: int) -> int:
    _positive_integer(n)
    prime_set((p,))
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


@dataclass(frozen=True)
class PrimeShell:
    """The clopen set v_p(x)=v_p(n) for each selected prime p."""

    primes: tuple[int, ...]
    n: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "primes", prime_set(self.primes))
        _positive_integer(self.n)

    @property
    def selected_part(self) -> int:
        return prod(p ** valuation(self.n, p) for p in self.primes)

    @property
    def unit_mass(self) -> Fraction:
        return prod((Fraction(p - 1, p) for p in self.primes), start=Fraction(1))

    @property
    def mass(self) -> Fraction:
        return self.unit_mass / self.selected_part

    @property
    def modulus(self) -> int:
        return self.selected_part * prod(self.primes)

    def contains(self, residue: int) -> bool:
        if type(residue) is not int:
            raise ValueError("expected an exact integer residue")
        return all(
            residue % (p ** valuation(self.n, p)) == 0
            and residue % (p ** (valuation(self.n, p) + 1)) != 0
            for p in self.primes
        )

    def counted_mass(self, max_modulus: int = 100_000) -> Fraction:
        _positive_integer(max_modulus)
        if self.modulus > max_modulus:
            raise ValueError("finite cylinder exceeds the declared resource cap")
        return Fraction(sum(self.contains(r) for r in range(self.modulus)), self.modulus)

    def cylinder_integral(self, values: Iterable[int | Fraction]) -> Fraction:
        values = tuple(_rational(x) for x in values)
        if not values:
            raise ValueError("a cylinder must have positive period")
        period = lcm(self.modulus, len(values))
        if period > 100_000:
            raise ValueError("finite cylinder exceeds the declared resource cap")
        return sum(
            (values[r % len(values)] for r in range(period) if self.contains(r)),
            start=Fraction(0),
        ) / period


def good_cylinder_primes(primes: Iterable[int], modulus: int) -> tuple[int, ...]:
    _positive_integer(modulus)
    return tuple(p for p in prime_set(primes) if modulus % p != 0)


def forward_cylinder_bound_squared(
    primes: Iterable[int], n: int, modulus: int,
    operator_norm_squared: int | Fraction = 1,
    test_norm_squared: int | Fraction = 1,
) -> Fraction:
    """Squared M sqrt(m alpha_G/d_G(n)) ||g||_2 bound, g of period m.

    G excludes selected primes dividing m.  This is a theorem parameter, not
    a test that a supplied operator is an intertwiner.
    """
    norm_t = _rational(operator_norm_squared)
    norm_g = _rational(test_norm_squared)
    if norm_t < 0 or norm_g < 0:
        raise ValueError("squared norms must be nonnegative")
    shell = PrimeShell(good_cylinder_primes(primes, modulus), n)
    return norm_t * norm_g * modulus * shell.mass


def multiplication_pullback(values: Iterable[int | Fraction], factor: int) -> tuple[Fraction, ...]:
    """The unnormalized cylinder operator g(x) -> g(factor*x)."""
    _positive_integer(factor)
    values = tuple(_rational(x) for x in values)
    if not values:
        raise ValueError("a cylinder must have positive period")
    return tuple(values[factor * r % len(values)] for r in range(len(values)))


def cylinder_norm_squared(values: Iterable[int | Fraction]) -> Fraction:
    values = tuple(_rational(x) for x in values)
    if not values:
        raise ValueError("a cylinder must have positive period")
    return sum((x * x for x in values), start=Fraction(0)) / len(values)


def geometric_orbit_mass(primes: Iterable[int], depth: int) -> Fraction:
    """Sum 1/k over the finite exponent box 0 <= v_p(k) <= depth."""
    primes = prime_set(primes)
    if type(depth) is not int or depth < 0:
        raise ValueError("depth must be a nonnegative exact integer")
    return prod(
        (sum((Fraction(1, p ** k) for k in range(depth + 1)), start=Fraction(0))
         for p in primes), start=Fraction(1),
    )


def cylinder_atomic_lift(masses: Iterable[int | Fraction]) -> dict[int, Fraction]:
    """Lift a cylinder distribution using atoms 1,...,m.

    Output b_n is the Dirac mass, i.e. the source coefficient is sqrt(n)*b_n.
    Working with b keeps the finite interpolation receipt rational and exact.
    """
    masses = tuple(_rational(x) for x in masses)
    if not masses:
        raise ValueError("a cylinder must have positive period")
    return {n: masses[n % len(masses)] for n in range(1, len(masses) + 1)}


def project_atomic_masses(atoms: Mapping[int, int | Fraction], modulus: int) -> tuple[Fraction, ...]:
    _positive_integer(modulus)
    out = [Fraction(0) for _ in range(modulus)]
    for n, mass in atoms.items():
        _positive_integer(n)
        out[n % modulus] += _rational(mass)
    return tuple(out)


def finite_control_report() -> dict[str, object]:
    shell = PrimeShell((2, 11), 2 ** 3 * 11 * 17)
    return {
        "status": "EXACT_FINITE_CONTROLS_ONLY",
        "infinite_limit_proved_by_this_code": False,
        "fresh_shell_selected_part": shell.selected_part,
        "fresh_shell_formula_mass": str(shell.mass),
        "fresh_shell_counted_mass": str(shell.counted_mass()),
        "unselected_factor_mutation": str(PrimeShell((2, 3), 5).mass),
        "forward_good_primes_period_6": good_cylinder_primes((2, 3, 5, 11), 6),
        "interpolation_period_5": tuple(map(str, project_atomic_masses(
            cylinder_atomic_lift((2, -1, Fraction(3, 7), 0, 5)), 5))),
    }
