"""Mahler 3/2 boundary observer, exact finite arithmetic only.

This is an AUXILIARY chart of rational-base dynamics and 2-adic journals.
It does not replace SUCC's authentic four-pole BBP forcing or U_0=0.
Python stdlib, no floating-point arithmetic and no global-claim oracle.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Optional

HALF = Fraction(1, 2)
THIRD = Fraction(1, 3)
TWO_THIRDS = Fraction(2, 3)
THREE_HALVES = Fraction(3, 2)


@dataclass(frozen=True)
class StepReport:
    integer: int
    remainder: Fraction
    parity: int
    chart_eligible: bool
    boundary: str
    chart_integer: int
    chart_remainder: Fraction
    actual_integer: int
    actual_remainder: Fraction


def mahler_integer_step(integer: int) -> int:
    """W(g) = (3g + (g mod 2))/2, an integer for every g."""
    return (3 * integer + (integer & 1)) // 2


def collatz_shortcut_step(integer: int) -> int:
    """C(g) = g/2 (even), (3g+1)/2 (odd); distinct from W."""
    return integer // 2 if not (integer & 1) else (3 * integer + 1) // 2


def true_rational_step(integer: int, remainder: Fraction) -> tuple[int, Fraction]:
    """Actual (3/2)(g+r) integer/remainder transport; 0 <= r < 1."""
    if not isinstance(integer, int) or not Fraction(0) <= remainder < 1:
        raise ValueError("integer register and 0 <= rational remainder < 1 required")
    value = THREE_HALVES * (integer + remainder)
    new_integer = value.numerator // value.denominator
    return new_integer, value - new_integer


def boundary_step(integer: int, remainder: Fraction) -> StepReport:
    """Check whether W's real-remainder chart is valid for this step.

    True transport is always computed independently.  The W chart is valid
    only when input and output lie in J=[0,1/2) and the parity guard holds.
    The report never silently continues a failed W chart.
    """
    g1, r1 = true_rational_step(integer, remainder)
    bit = integer & 1
    wg = mahler_integer_step(integer)
    wr = THREE_HALVES * remainder - Fraction(bit, 2)
    if not 0 <= remainder < HALF:
        boundary = "outside_J"
    elif bit == 0 and remainder >= THIRD:
        boundary = "even_exit_at_one_third"
    elif bit == 1 and remainder < THIRD:
        boundary = "odd_branch_mismatch_at_one_third"
    else:
        boundary = "none"
    eligible = boundary == "none"
    if eligible:
        assert wg == g1 and wr == r1 and 0 <= r1 < HALF
    return StepReport(integer, remainder, bit, eligible, boundary,
                      wg, wr, g1, r1)


def first_boundary(integer: int, remainder: Fraction, horizon: int) -> Optional[tuple[int, StepReport]]:
    """Return earliest invalid W/J step, or None over the inspected horizon.

    The true (3/2) map provides continuation, independently of eligibility.
    A finite None never means infinite Z-number admissibility.
    """
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    for n in range(horizon):
        report = boundary_step(integer, remainder)
        if not report.chart_eligible:
            return n, report
        integer, remainder = report.actual_integer, report.actual_remainder
    return None


def survivor_interval(integer: int, steps: int) -> Optional[tuple[Fraction, Fraction]]:
    """Exact half-open interval of r0 in J giving `steps` guarded W steps.

    Given initial nonnegative integer g0 and r0 in [0,1/2), g_k=W^k(g0)
    is predetermined.  r_k=a_k*r0+c_k (a_k>0), and each guard is a
    half-open interval for r_k.  Intersect the pullbacks using Fractions.
    None means provably no finite survivors.  Non-None is finite only.
    """
    if not isinstance(integer, int) or integer < 0 or steps < 0:
        raise ValueError("nonnegative integer and nonnegative horizon required")
    left, right = Fraction(0), HALF
    a, c = Fraction(1), Fraction(0)
    g = integer
    for _ in range(steps):
        b = g & 1
        permitted_left = THIRD if b else Fraction(0)
        permitted_right = HALF if b else THIRD
        left = max(left, (permitted_left - c) / a)
        right = min(right, (permitted_right - c) / a)
        if left >= right:
            return None
        a, c = THREE_HALVES * a, THREE_HALVES * c - Fraction(b, 2)
        g = mahler_integer_step(g)
    return left, right


def parity_bits(integer: int, steps: int, *, kind: str = "mahler") -> tuple[int, ...]:
    """Chronological parity bits of W or shortcut C for an integer seed."""
    if not isinstance(integer, int) or steps < 0:
        raise ValueError("integer seed and nonnegative horizon required")
    step = {"mahler": mahler_integer_step,
            "collatz": collatz_shortcut_step}.get(kind)
    if step is None:
        raise ValueError("kind must be 'mahler' or 'collatz'")
    bits = []
    for _ in range(steps):
        bits.append(integer & 1)
        integer = step(integer)
    return tuple(bits)


def bits_from_hex_journal(hex_digits: str) -> tuple[int, ...]:
    """Each chronological nibble is unpacked least-significant-bit first.

    This is the SUCC #681 symbolic convention, not ordinary integer bit order.
    """
    if not isinstance(hex_digits, str) or not hex_digits:
        raise ValueError("expected at least one hexadecimal digit")
    try:
        digits = [int(c, 16) for c in hex_digits]
    except ValueError as exc:
        raise ValueError("non-hexadecimal digit") from exc
    return tuple((d >> j) & 1 for d in digits for j in range(4))


def inverse_parity_residue(bits: Iterable[int], *, kind: str) -> int:
    """Unique compatible 2-adic starting residue modulo 2^N.

    Reverse N branches from the zero terminal representative.  Every inverse
    branch contracts 2-adically by 1/2; the unknown tail affects only 2^N.
    """
    word = tuple(bits)
    if kind not in {"mahler", "collatz"} or any(b not in (0, 1) for b in word):
        raise ValueError("kind and bits must be valid")
    modulus = 1 << len(word)
    if modulus == 1:
        return 0
    inv3 = pow(3, -1, modulus)
    x = 0
    for b in reversed(word):
        if kind == "mahler":
            x = ((2*x - b) * inv3) % modulus
        else:
            x = ((2*x - 1) * inv3 if b else 2*x) % modulus
    return x


def weighted_parity_prefix(bits: Iterable[int]) -> Fraction:
    """Mahler's common rational prefix S_N = sum b_j (2/3)^j."""
    total = Fraction(0)
    factor = Fraction(1)
    for b in bits:
        if b not in (0, 1):
            raise ValueError("parity must be binary")
        total += b * factor
        factor *= TWO_THIRDS
    return total


def rational_mod_2_power(q: Fraction, exponent: int) -> int:
    """Reduce a rational with odd denominator modulo 2^exponent."""
    if exponent < 0:
        raise ValueError("exponent nonnegative")
    modulus = 1 << exponent
    if q.denominator % 2 == 0:
        raise ValueError("non-2-adic-integer rational")
    return q.numerator * pow(q.denominator, -1, modulus) % modulus if exponent else 0


def fibonacci_language_count(length: int) -> int:
    """Number of length-N binary strings without neighboring ones."""
    if length < 0:
        raise ValueError("length nonnegative")
    no_one, ending_one = 1, 0
    for _ in range(length):
        no_one, ending_one = no_one + ending_one, no_one
    return no_one + ending_one


PI_12_HEX_DIGITS = "3243F6A8885A"  # imported finite certificate, SUCC #681


@dataclass(frozen=True)
class RadialSpectralCertificate:
    """m(Q(sqrt(q)*z)) = log(constant) + log_q_factor * log(q).

    Away from source-root radii, winding and Toeplitz index are exact.
    At critical radii winding/index are undefined, not continuous values.
    This is an AUXILIARY radial analytic family, not a BBP time update.
    """
    squared_radius: Fraction
    region: str
    log_constant: int
    log_q_factor: Fraction
    winding: Optional[int]
    toeplitz_index: Optional[int]


def radial_spectral_certificate(squared_radius: Fraction) -> RadialSpectralCertificate:
    """Exact Jensen/argument-principle phase chart for Q=(1-t)H.

    H=(t^2+2)(t^2+2t+2).  Its 4 roots have |t|^2=2.
    Q adds one root |t|^2=1. For ρ=sqrt(q),
        m(Q(ρe^{iθ}))=max(0,logρ)+4*max(log(sqrt2),logρ).
    The derivative wrt logρ equals winding only off the roots.
    """
    q = Fraction(squared_radius)
    if q <= 0:
        raise ValueError("squared radius must be positive")
    if q < 1:
        return RadialSpectralCertificate(q, "inner", 4, Fraction(0), 0, 0)
    if q == 1:
        return RadialSpectralCertificate(q, "first_root_boundary", 4, Fraction(0), None, None)
    if q < 2:
        return RadialSpectralCertificate(q, "middle", 4, Fraction(1, 2), 1, -1)
    if q == 2:
        return RadialSpectralCertificate(q, "four_root_boundary", 4, Fraction(1, 2), None, None)
    return RadialSpectralCertificate(q, "outer", 1, Fraction(5, 2), 5, -5)
