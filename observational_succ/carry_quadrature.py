"""Exact source-pulse and carry-quadrature instruments for the original BBP.

The uniform pulse theorem is in research/2026-11-15/carry_quadrature_assault/.
These instruments certify finite observations; they do not prove a positive
lower density of carry events or pi normality. No floating-point pi oracle is
used. The source and its certified integer prefix implementation are inherited.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from observational_succ.bbp_spatial_haar_lift import bulk_pi_hex_digits
from observational_succ.duck_bbp import forcing, tail_interval


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def pulse_scale(n: int) -> tuple[int, int]:
    """Exact m=ceil(log_16(n^2)), q=16^m, without rounded logarithms."""
    _nat(n, 4)
    m, q = 0, 1
    while q < n*n:
        m += 1
        q *= 16
    return m, q


@dataclass(frozen=True)
class SourcePulse:
    n: int
    delay: int
    harmonic: int
    response: Fraction


def source_pulse(n: int) -> SourcePulse:
    """R=U_(n+m)-16^m U_n from a finite forward forcing path only."""
    m, q = pulse_scale(n)
    response = Fraction()
    for j in range(1, m+1):
        response = 16*response + forcing(n+j)
    return SourcePulse(n, m, q, response)


def selected_event(carry: int) -> bool:
    """The exact fourth-root non-locking event, allowing negative controls."""
    if type(carry) is not int:
        raise ValueError("integer carry required")
    return carry % 4 in (1, 2)


def carry_quadrature(carry: int) -> int:
    """Re((1+i)*i^carry), exactly +1 or -1."""
    return 1 - 2*int(selected_event(carry))


def dyadic_residue(value: Fraction, bits: int) -> int:
    """Finite dyadic residue of an odd-denominator rational, not real bits."""
    _nat(bits, 1)
    if not isinstance(value, Fraction) or value.denominator % 2 == 0:
        raise ValueError("an odd-denominator Fraction is required")
    modulus = 1 << bits
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def nearest_winding(u: Fraction, v: Fraction) -> tuple[int, Fraction, Fraction]:
    """Integer nearest-point winding and the two centered real errors."""
    if not isinstance(u, Fraction) or not isinstance(v, Fraction):
        raise ValueError("exact Fraction states required")
    a = (u + Fraction(1, 2)).__floor__()
    b = (v + Fraction(1, 2)).__floor__()
    return b-16*a, u-a, v-b


def borrow_decision(n: int, phase_lo: Fraction, phase_hi: Fraction,
                    depth: int = 8) -> tuple[int | None, str]:
    """Certify beta=1_{Y_n<T_n}; None means the enclosure is insufficient.

    Input must enclose the completed phase with 0<=lo<=Y_n<hi<=1.
    First use the proved n^-2 tail enclosure, then the exact finite Green sum.
    No ambiguous comparison is guessed.
    """
    _nat(n, 1)
    _nat(depth)
    if not isinstance(phase_lo, Fraction) or not isinstance(phase_hi, Fraction):
        raise ValueError("exact Fraction phase bounds required")
    if not 0 <= phase_lo < phase_hi <= 1:
        raise ValueError("a nonempty phase interval in [0,1] is required")
    lo = Fraction(15, 1024*(n+1)**2)
    hi = Fraction(1, 64*n*n)
    if phase_lo >= hi:
        return 0, "analytic_n2"
    if phase_hi <= lo:
        return 1, "analytic_n2"
    lo, hi = tail_interval(n, depth)
    if phase_lo >= hi:
        return 0, "finite_green"
    if phase_hi <= lo:
        return 1, "finite_green"
    return None, "ambiguous"


@dataclass(frozen=True)
class CarryObservation:
    n: int
    completed_digit: int
    borrow: int
    carry_mod4: int
    cofactor_mod4: int
    phase_width: int
    tail_depth: int
    certificate: str


def certified_carry_observations(horizon: int, initial_width: int = 8,
                                 max_width: int = 32
                                 ) -> tuple[str, tuple[CarryObservation, ...]]:
    """Certify C_n mod4 for 1<=n<=horizon from the authentic four-pole source.

    A BBP outward integer enclosure certifies the completed pi prefix. The
    Green-tail comparison then pays the difference between completed digits
    and the actual raw carries. Prefix index zero is pi's first fractional
    hexadecimal digit; the completed digit at n=1 is its integer digit 3.
    Returns the certified prefix as well as the finite observations.
    """
    _nat(horizon, 1)
    _nat(initial_width, 1)
    _nat(max_width, initial_width)
    prefix = bulk_pi_hex_digits(horizon + max_width)
    observations = []
    for n in range(1, horizon+1):
        width = initial_width
        while True:
            word = int(prefix[n-1:n-1+width], 16)
            denominator = 16**width
            lo, hi = Fraction(word, denominator), Fraction(word+1, denominator)
            depth = max(8, width)
            borrow, certificate = borrow_decision(n, lo, hi, depth)
            if borrow is not None:
                break
            if width == max_width:
                raise ArithmeticError(f"uncertified boundary at n={n}; increase max_width")
            width = min(2*width, max_width)
        digit = 3 if n == 1 else int(prefix[n-2], 16)
        carry = (digit-borrow) % 4
        # Original source satisfies [U_n]_4=n mod4. This cofactor is an
        # exact transported coordinate, not a statistically independent sample.
        cofactor = (n-carry) % 4
        observations.append(CarryObservation(n, digit, borrow, carry, cofactor,
                                             width, depth, certificate))
    return prefix, tuple(observations)


def shell_statistics(observations: tuple[CarryObservation, ...],
                     start: int, length: int) -> dict:
    """Exact finite counts; the shell need not have dyadic length."""
    _nat(start, 1)
    _nat(length, 1)
    if start+length-1 > len(observations):
        raise ValueError("shell exceeds the certified horizon")
    counts = [0]*4
    clock_cofactor = [[0]*4 for _ in range(4)]
    borrows = 0
    longest = run = 0
    for observation in observations[start-1:start+length-1]:
        counts[observation.carry_mod4] += 1
        clock_cofactor[observation.n % 4][observation.cofactor_mod4] += 1
        borrows += observation.borrow
        run = 0 if selected_event(observation.carry_mod4) else run+1
        longest = max(longest, run)
    hits = counts[1]+counts[2]
    return {"start": start, "length": length, "counts_mod4": counts,
            "selected_events": hits, "selected_fraction": str(Fraction(hits, length)),
            "mean_quadrature": str(Fraction(length-2*hits, length)),
            "tail_borrows": borrows, "longest_no_hit_run": longest,
            "clock_cofactor_counts": clock_cofactor}
