"""Exact finite charts for the 16-solenoid natural extension of the circle.

Research addendum to SUCC PR #320 and original zero-seeded four-pole BBP.

Convention: (t,z) ~ (t+1,z-1); x=t mod 1, z=floor(t) for
unwrapped lift [(t,0)]. The global map is multiplication by 16,
represented in a cut chart by (x,z)->({16x},16z+floor(16x)).

A finite chart is NOT a full solenoid point and does not carry an
invertible fixed-depth map: an exact inverse loses one hex digit of
adic precision. Never infer pi normality from finite chart probes.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

RADIX = 16
SOURCE_TAG = "original-four-pole-BBP-zero-seed; winding-lift natural extension"


def _exact_q(value, name: str) -> Q:
    if type(value) not in (int, Q):
        raise ValueError(f"{name}: exact integer or Fraction required")
    return Q(value)


def _depth(value, *, minimum: int = 1, maximum: int = 64) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"depth must be an integer in [{minimum}, {maximum}]")
    return value


@dataclass(frozen=True)
class FiniteSolenoidChart:
    """Right-open real-circle cut and a Z2 memory residue at finite precision.

    Chart identity: changing an unwrapped t to t+1 changes z to z-1.
    Coordinates: circle in [0,1), memory mod 16**depth.
    """
    circle: Q
    memory: int
    depth: int

    def __post_init__(self) -> None:
        _depth(self.depth)
        circle = _exact_q(self.circle, "circle")
        if not 0 <= circle < 1:
            raise ValueError("circle coordinate must belong to [0,1)")
        if type(self.memory) is not int or not 0 <= self.memory < RADIX**self.depth:
            raise ValueError("memory must be the canonical residue mod 16**depth")
        object.__setattr__(self, "circle", circle)

    @classmethod
    def from_unwrapped(cls, value, depth: int) -> "FiniteSolenoidChart":
        """Original real winding lift [(value, 0)], not odd-torsion section."""
        d = _depth(depth)
        x = _exact_q(value, "unwrapped real")
        integer_part = x.numerator // x.denominator
        return cls(x - integer_part, integer_part % (RADIX**d), d)

    def advance(self) -> tuple["FiniteSolenoidChart", int]:
        """Multiply a solenoid point by 16; digit is floor(16 * circle)."""
        total = RADIX * self.circle
        digit = total.numerator // total.denominator
        return (FiniteSolenoidChart(total - digit,
                                    (RADIX * self.memory + digit) % (RADIX**self.depth),
                                    self.depth), digit)

    def inverse_with_precision_loss(self) -> tuple["FiniteSolenoidChart", int]:
        """Inverse T at reduced depth: z_prev=(z-digit)/16 in Z2.

        Dividing by 16 consumes one *known* hex digit. Full T is a
        homeomorphism on the infinite solenoid, not on a finite chart.
        """
        _depth(self.depth, minimum=2)
        old_digit = self.memory % RADIX
        return (FiniteSolenoidChart((self.circle + old_digit) / RADIX,
                                    ((self.memory - old_digit) // RADIX)
                                    % (RADIX ** (self.depth - 1)),
                                    self.depth - 1), old_digit)

    def character_phase(self, numerator: int, denominator_depth: int = 0) -> Q:
        """Exact argument mod 1 of chi_(numerator/16**denominator_depth).

        In the convention of the pre-existing SUCC solenoid cut chart,
        chi_(m/16**k)(x,z)=exp(2*pi*i*m*(x+[z]_(16**k))/16**k).
        """
        if type(numerator) is not int:
            raise ValueError("integer character numerator required")
        k = _depth(denominator_depth, minimum=0, maximum=self.depth)
        q = RADIX**k
        return (Q(numerator) * (self.circle + (self.memory % q)) / q) % 1


def two_adic_residue(value, depth: int) -> int:
    """Odd-denominator rational interpreted as an element of Z2."""
    q = RADIX**_depth(depth)
    v = _exact_q(value, "two-adic rational")
    if v.denominator % 2 == 0:
        raise ValueError("even reduced denominator: not an element of Z2")
    return (v.numerator * pow(v.denominator, -1, q)) % q


def rational_character_split(value, depth: int, h: int) -> tuple[Q, Q, Q]:
    """Phase of e(h*value/16**depth) as adic phase + denominator defect.

    If value=A/B, q=16**depth, R=A/B (mod q), K=(B*R-A)/q,
    then A/(B*q)=R/q-K/B (exactly, not approximately).
    The return is (real, adic, complementary) modulo 1.
    """
    v = _exact_q(value, "rational state")
    d = _depth(depth)
    if type(h) is not int or v.denominator % 2 == 0:
        raise ValueError("integer h and odd denominator required")
    q = RADIX**d
    R = two_adic_residue(v, d)
    K, remainder = divmod(v.denominator * R - v.numerator, q)
    if remainder:
        raise ArithmeticError("failed exact residue lift")
    real = (Q(h) * v / q) % 1
    adic = Q(h * R, q) % 1
    complement = (-Q(h * K, v.denominator)) % 1
    if (adic + complement) % 1 != real:
        raise ArithmeticError("exact character factorization failed")
    return real, adic, complement


def authentic_four_pole(n: int) -> Q:
    """Independent source identity, for comparison with SUCC authentic_r(n)."""
    if type(n) is not int or n < 1:
        raise ValueError("positive BBP index required")
    return (Q(4, 8*n - 7) - Q(2, 8*n - 4)
            - Q(1, 8*n - 3) - Q(1, 8*n - 2))


def canceled_four_pole(n: int) -> Q:
    """Original signed forcing in the exact, odd-denominator rational chart."""
    if type(n) is not int or n < 1:
        raise ValueError("positive BBP index required")
    return Q(120*n*n - 89*n + 16,
             (2*n - 1)*(4*n - 1)*(8*n - 7)*(8*n - 3))


def bbp_zero_seed_state(n: int) -> Q:
    """Exact recurrence U_0=0, U_n=16U_(n-1)+r(n); not a pi proof."""
    if type(n) is not int or not 0 <= n <= 2000:
        raise ValueError("BBP time must be in [0,2000]")
    state = Q(0)
    for k in range(1, n+1):
        state = RADIX*state + authentic_four_pole(k)
    return state


def digit_archive_residue(digits: tuple[int, ...], depth: int, initial_memory=0) -> int:
    """z_N = 16**N*z_0 + sum 16**(N-1-j)*digit_j, mod 16**depth."""
    q = RADIX**_depth(depth)
    if type(initial_memory) is not int:
        raise ValueError("integer initial winding memory required")
    z = initial_memory % q
    for digit in digits:
        if type(digit) is not int or not 0 <= digit < RADIX:
            raise ValueError("hexadecimal digit must be 0..15")
        z = (RADIX*z + digit) % q
    return z
