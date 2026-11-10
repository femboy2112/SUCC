"""Source-faithful floor-to-threshold and floor-to-Fourier BBP observers.

Research-only.  The phase/threshold identities are exact finite algebra, but
prime marginal uniformity and real selected Weyl decay are separate claims.
The original forcing is imported (not changed) from duck_bbp.
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, pi, sin
from cmath import exp
from typing import Iterable

from .duck_bbp import forcing

RADIX = 16
POLE_SHIFTS = (0, 3, 4, 5)
POLE_COEFFICIENTS = (4, -2, -1, -1)


def _fraction(value: Fraction | int) -> Fraction:
    if not isinstance(value, (Fraction, int)) or isinstance(value, bool):
        raise TypeError("exact integer/Fraction argument required")
    return Fraction(value)


def threshold_vector(phase: Fraction, shift: Fraction) -> tuple[int, ...]:
    """16 exact jump indicators for floor(16*phase+shift).

    Assumes 0<=phase<1 and 0<=shift<1. This is guaranteed for real
    original BBP transitions at n>=2 and for p-primary modular injections.
    """
    x = _fraction(phase)
    r = _fraction(shift)
    if not (0 <= x < 1 and 0 <= r < 1):
        raise ValueError("phase and shift must lie in [0,1)")
    return tuple(int(16*x+r >= j) for j in range(1, 17))


def carry_from_thresholds(phase: Fraction, shift: Fraction) -> int:
    return sum(threshold_vector(phase, shift))


def haar_indicator_masses(shift: Fraction) -> tuple[Fraction, ...]:
    """Continuous, exact Lebesgue integrals of threshold indicators."""
    r = _fraction(shift)
    if not 0 <= r < 1:
        raise ValueError("0<=shift<1 required")
    return tuple(Fraction(16-j,16)+r/16 for j in range(1,17))


def haar_carry_masses(shift: Fraction) -> tuple[Fraction, ...]:
    """p(carry=0,..,16) for a uniform real phase and given shift.

    Modulo 16, the carry is EXACTLY uniform for EVERY fixed shift.
    """
    r = _fraction(shift)
    if not 0 <= r < 1:
        raise ValueError("0<=shift<1 required")
    return ((1-r)/16,) + (Fraction(1,16),)*15 + (r/16,)


def real_carry(phase: Fraction, source_index: int) -> int:
    if type(source_index) is not int or source_index < 2:
        raise ValueError("source_index >= 2 required: first forcing exceeds 1")
    return carry_from_thresholds(phase, forcing(source_index))


def modular_injection(source_index: int, p: int) -> int:
    """[p*r(n)]_p, only where p*r(n) is a p-integral rational."""
    if type(source_index) is not int or source_index < 1:
        raise ValueError("positive source time required")
    if type(p) is not int or p <= 2 or p % 2 == 0:
        raise ValueError("odd prime clock modulus required; primality caller-owned")
    z = p * forcing(source_index)
    if z.denominator % p == 0:
        raise ValueError("below simple p-pole regime")
    return z.numerator * pow(z.denominator, -1, p) % p


def prime_carry(previous_residue: int, injection: int, p: int) -> tuple[int,int]:
    if (type(p) is not int or p <= 2 or p % 2 == 0 or
            type(previous_residue) is not int or not 0 <= previous_residue < p or
            type(injection) is not int or not 0 <= injection < p):
        raise ValueError("canonical residue/injection and odd modulus required")
    x = Fraction(previous_residue, p)
    r = Fraction(injection, p)
    z = carry_from_thresholds(x, r)
    c = (16*previous_residue+injection) % p
    assert z*p+c == 16*previous_residue+injection
    return c,z


def joint_carry_step(real_phase: Fraction, previous_residue: int,
                     source_index: int, p: int) -> dict:
    """Exact real/p-prime threshold slip and complementary-coordinate update."""
    if source_index < 2:
        raise ValueError("first source forcing outside this layer-cake chart")
    r = forcing(source_index)
    injected = modular_injection(source_index, p)
    actual = threshold_vector(real_phase, r)
    local = threshold_vector(Fraction(previous_residue,p), Fraction(injected,p))
    kappa = sum(actual)
    z = sum(local)
    next_real = 16*_fraction(real_phase)+r-kappa
    next_p = (16*previous_residue+injected)%p
    previous_complement = _fraction(real_phase)-Fraction(previous_residue,p)
    next_complement = next_real - Fraction(next_p,p)
    predicted = (16*previous_complement+r-Fraction(injected,p) - (kappa-z))
    assert predicted==next_complement
    return {"kappa":kappa,"prime_carry":z,"slip":kappa-z,
            "threshold_slip":sum(a-b for a,b in zip(actual,local)),
            "next_real":next_real,"next_prime":next_p,
            "next_complement":next_complement, "predicted_complement":predicted}


def _phase(h: int, k: int) -> complex:
    return exp(2j*pi*(h*k)/16)


def centered_floor_character(phase: Fraction, shift: Fraction, h: int) -> complex:
    """Exact threshold representation, evaluated numerically only at output.

    The right side is the discrepancy from the uniform-phase integral (zero).
    """
    if type(h) is not int or h % 16 == 0:
        raise ValueError("h must be a nonzero character modulo 16")
    q = _phase(h,1)
    indicators=threshold_vector(phase,shift)
    haar=haar_indicator_masses(shift)
    return (q-1)*sum(q**(j-1)*(v-t) for j,(v,t) in enumerate(zip(indicators,haar),1))


def floor_fourier_coefficient(m: int, h: int, shift: Fraction | float) -> complex:
    """Exact analytic formula for floor-carry character's circle Fourier mode.

    A floating complex value is returned for visualization/diagnostics only.
    """
    if type(h) is not int or h % 16 == 0 or type(m) is not int:
        raise ValueError("nontrivial carry character and integer m required")
    if m == 0 or (m-h)%16:
        return 0j
    r=float(shift)
    return (16*(1-exp(-2j*pi*h/16))/(2j*pi*m) * exp(2j*pi*m*r/16))


def fejer_floor_character(phase: Fraction, shift: Fraction,
                          h: int, aperture: int) -> complex:
    """Finite, source-phase-twisted Fourier sum; never claim sharp convergence."""
    if type(aperture) is not int or aperture < 2:
        raise ValueError("aperture >= 2 required")
    x=float(_fraction(phase))
    return sum((1-abs(m)/aperture)*floor_fourier_coefficient(m,h,shift)*exp(2j*pi*m*x)
               for m in range(-aperture+1,aperture))


def boundary_distance(phase: Fraction, shift: Fraction) -> Fraction:
    """Circular distance to the nearest of 16 moving carry thresholds."""
    x=(_fraction(phase)+_fraction(shift)/16)%1
    z=16*x
    frac=z - (z.numerator//z.denominator)
    return min(frac,1-frac)/16


def fejer_epoch_budget(phases: Iterable[Fraction], shifts: Iterable[Fraction],
                        radius: Fraction, aperture: int) -> tuple[Fraction,int]:
    """Bound average sharp-minus-Fejer error via boundary occupation.

    A sufficient deterministic estimate, NOT a source-specific asymptotic saving.
    """
    rad=_fraction(radius)
    xs=list(phases)
    rs=list(shifts)
    if len(xs)!=len(rs) or not xs or not 0<rad< Fraction(1,32):
        raise ValueError("nonempty equal lengths, 0<radius<1/32 required")
    if type(aperture) is not int or aperture < 2:
        raise ValueError("aperture>=2 required")
    bad=sum(boundary_distance(x,r)<rad for x,r in zip(xs,rs))
    # Individual error <= min(2,1/(H*distance)); on bad times use 2.
    return Fraction(2*bad,len(xs))+Fraction(1,1)/aperture/rad,bad


def fejer_source_twist_budget(source_index: int, h: int, aperture: int) -> Fraction:
    """Pointwise upper bound for source-twisted vs unforced Fejer floor.

    At n, r(n) positive O(n^-2), and each surviving Fourier mode
    contributes at most 2|sin(pi*h/16)| r(n).  Return a rational
    slightly weaker bound using |sin|<=1, for exact conservatism.

    For the optimal displayed coefficient multiply by |sin(pi*h/16)|.
    This says NOTHING about the unsmoothed actual selected digit.
    """
    if type(source_index) is not int or source_index < 2 or type(h) is not int or h%16==0:
        raise ValueError("source index >=2 and nontrivial character required")
    if type(aperture) is not int or aperture < 2:
        raise ValueError("aperture>=2 required")
    # At most ceil((2*aperture-1)/16) modes; 2*r per mode.
    mode_count=(2*aperture-2)//16+1
    return 2*forcing(source_index)*mode_count
