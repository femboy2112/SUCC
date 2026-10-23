"""Exact witnesses for clock blow-ups, heat normalization and lost carry sectors.

Universal geometric/operator limits are PAPER proofs in
research/2026-10-23/SOURCE_FAITHFUL_LIMITS_HEAT.md.  This module supplies exact
finite witnesses and rational enclosures, not an executed infinite limit.
The heat carrier is a bilateral clock, not the one-based arithmetic isometry.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt


class ClockLimitError(ValueError):
    """Invalid carrier, topology, or exact certificate input."""


def _int(n, lower=0):
    if type(n) is not int or n < lower:
        raise ClockLimitError(f"exact integer >= {lower} required")
    return n


def _q(x, positive=False):
    if type(x) not in (int, Q):
        raise ClockLimitError("exact rational input required, not a float/bool")
    x = Q(x)
    if positive and x <= 0:
        raise ClockLimitError("strictly positive rational required")
    return x


def signed_representative(n, size):
    """Representative in [-floor(N/2), ceil(N/2)-1]."""
    _int(size, 2)
    if type(n) is not int:
        raise ClockLimitError("integer source address required")
    return (n + size // 2) % size - size // 2


def cycle_distance(i, j, size):
    _int(size, 2)
    if type(i) is not int or type(j) is not int:
        raise ClockLimitError("integer source addresses required")
    delta = (i - j) % size
    return min(delta, size - delta)


def local_chart_certificate(size, epsilon, radius):
    """When N*epsilon>4R, the R-ball embeds isometrically in [-R,R].

    Its Hausdorff error is <epsilon (<=epsilon is returned). This local
    certificate proves pointed GH convergence when epsilon->0, N*epsilon->inf.
    """
    _int(size, 2)
    epsilon = _q(epsilon, True)
    radius = _q(radius)
    if radius < 0:
        raise ClockLimitError("nonnegative radius required")
    circumference = size * epsilon
    if circumference <= 4 * radius:
        raise ClockLimitError("pairwise chart needs circumference > 4*radius")
    horizon = radius // epsilon
    return {"radius_steps": horizon, "circumference": circumference,
            "distortion": Q(0), "hausdorff_error_upper": epsilon,
            "maximum_chart_separation": 2 * horizon * epsilon}


def nearest_integer(x):
    """Nearest integer, ties toward +infinity; exact error at most 1/2."""
    x = _q(x)
    return (x + Q(1, 2)).numerator // (x + Q(1, 2)).denominator


def action_horizon(size, epsilon, initial_radius, word):
    """Error/extent induction for translations and positive integer multipliers.

    The ordered alphabet is ('translate', rational t) or ('multiply', int p).
    Operations are maps of points; no Hilbert isometry is asserted.
    """
    _int(size, 2)
    epsilon = _q(epsilon, True)
    radius = _q(initial_radius)
    if radius < 0:
        raise ClockLimitError("nonnegative initial radius required")
    error = Q(0)
    stages = []
    for operation, value in word:
        if operation == "translate":
            value = _q(value)
            shift = nearest_integer(value / epsilon)
            radius += abs(value)
            error += abs(epsilon * shift - value)
            datum = shift
        elif operation == "multiply":
            _int(value, 1)
            radius *= value
            error *= value
            datum = value
        else:
            raise ClockLimitError("unknown authorized point-map operation")
        stages.append({"operation": operation, "discrete_parameter": datum,
                       "continuum_radius": radius, "error_upper": error,
                       "no_wrap": 2 * (radius + error) < size * epsilon})
    return {"stages": tuple(stages), "error_upper": error,
            "no_wrap": (2 * initial_radius < size * epsilon
                        and all(s["no_wrap"] for s in stages))}


def cyclic_multiplier_defect(size, multiplier):
    """Exact rank/kernel/norm data for e_n -> e_(p*n mod N)."""
    _int(size, 2)
    _int(multiplier, 1)
    d = gcd(size, multiplier)
    return {"fiber_size": d, "rank": size // d,
            "kernel_dimension": size - size // d,
            "operator_norm_squared": d, "is_isometry": d == 1}


def laplacian_column(index, size):
    """Integer column of 2I-S-S*, with multiplicity at N=2 retained."""
    _int(size, 2)
    if type(index) is not int:
        raise ClockLimitError("integer address required")
    out = [Q(0)] * size
    out[index % size] += 2
    out[(index - 1) % size] -= 1
    out[(index + 1) % size] -= 1
    return tuple(out)


def compressed_laplacian_column(radix, coarse_size, index=0):
    """Independent finite block calculation of J*LJ=(2I-T-T*)/radix.

    Repeat the coarse vector without sqrt(radix), apply L, then average.
    The omitted sqrt factors cancel between J and J*.
    """
    _int(radix, 2)
    _int(coarse_size, 3)
    if type(index) is not int:
        raise ClockLimitError("integer address required")
    size = radix * coarse_size
    fine = [Q(0)] * size
    for r in range(radix):
        fine[(radix * index + r) % size] = Q(1)
    applied = [2 * fine[j] - fine[(j - 1) % size] - fine[(j + 1) % size]
               for j in range(size)]
    return tuple(sum(applied[radix * j:radix * (j + 1)], Q(0)) / radix
                 for j in range(coarse_size))


def hidden_heat_defect(radix, epsilon=1):
    """Squared norm of (I-JJ*)L_epsilon J delta_0 on the bilateral source.

    delta_0 has norm one in ordinary ell^2; radix>=2.  This is the exact
    second-derivative discrepancy of compressed heat and compressed generator.
    """
    _int(radix, 2)
    epsilon = _q(epsilon, True)
    return Q(4 * radix - 6, radix * radix) / epsilon**4


@dataclass(frozen=True)
class RationalBracket:
    lower: Q
    upper: Q

    def __post_init__(self):
        if type(self.lower) is not Q or type(self.upper) is not Q:
            raise ClockLimitError("Fraction endpoints required")
        if self.lower > self.upper:
            raise ClockLimitError("reversed interval")


def exp_negative_bracket(x, terms=24):
    """Certified e^-x, 0<=x<=64, by positive Taylor remainder and squaring."""
    x = _q(x)
    _int(terms, 2)
    if not 0 <= x <= 64 or terms > 80:
        raise ClockLimitError("finite certificate range x<=64, terms<=80")
    reduced = x
    squarings = 0
    while reduced > Q(1, 2):
        reduced /= 2
        squarings += 1
    term = total = Q(1)
    for j in range(1, terms + 1):
        term *= reduced / j
        total += term
    tail = term * reduced / (terms + 1) / (1 - reduced / (terms + 2))
    lo, hi = total, total + tail
    for _ in range(squarings):
        lo *= lo
        hi *= hi
    return RationalBracket(1 / hi, 1 / lo)


def cycle_heat_brackets(size, epsilon, time, terms=64):
    """Certified transition probabilities via Poisson uniformization.

    L=epsilon^-2(2I-S-S*), z=2*time/epsilon^2; exact nearest-neighbor
    probabilities are weighted by e^-z*z^j/j!. No spectral float is trusted.
    Divide these probability intervals by epsilon for Lebesgue densities.
    """
    _int(size, 2)
    _int(terms, 2)
    epsilon = _q(epsilon, True)
    time = _q(time)
    z = 2 * time / epsilon**2
    if not 0 <= z <= 64 or terms > 256 or terms + 2 <= z or size > 512:
        raise ClockLimitError("finite enclosure cap or invalid Poisson tail")
    exponential = exp_negative_bracket(z)
    walk = [Q(0)] * size
    walk[0] = Q(1)
    sums = walk.copy()
    weight = Q(1)
    for j in range(1, terms + 1):
        walk = [(walk[(n - 1) % size] + walk[(n + 1) % size]) / 2
                for n in range(size)]
        weight *= z / j
        sums = [s + weight * w for s, w in zip(sums, walk)]
    tail = weight * z / (terms + 1) / (1 - z / (terms + 2))
    return tuple(RationalBracket(exponential.lower * s,
                                 min(Q(1), exponential.upper * (s + tail)))
                 for s in sums)


def _atan_reciprocal_bracket(denominator, terms):
    x = Q(1, denominator)
    total = sum(((-1)**j * x**(2*j + 1) / (2*j + 1)
                 for j in range(terms)), Q(0))
    next_term = (-1)**terms * x**(2*terms + 1) / (2*terms + 1)
    return RationalBracket(min(total, total + next_term),
                           max(total, total + next_term))


def pi_bracket(terms=20):
    """Machin identity with alternating-series rational remainder bounds."""
    _int(terms, 2)
    if terms > 64:
        raise ClockLimitError("finite Machin certificate cap")
    a = _atan_reciprocal_bracket(5, terms)
    b = _atan_reciprocal_bracket(239, terms)
    return RationalBracket(16*a.lower - 4*b.upper, 16*a.upper - 4*b.lower)


def sqrt_bracket(x, bits=64):
    x = _q(x)
    _int(bits, 1)
    if x < 0 or bits > 256:
        raise ClockLimitError("nonnegative radicand and bits<=256 required")
    scale = 1 << bits
    n = isqrt((x.numerator * scale * scale) // x.denominator)
    lo = Q(n, scale)
    hi = lo if lo * lo == x else Q(n + 1, scale)
    return RationalBracket(lo, hi)


def gaussian_heat_bracket(time, x):
    """Certified g_t(x)=(4*pi*t)^(-1/2)*exp(-x^2/(4t))."""
    time = _q(time, True)
    x = _q(x)
    p = pi_bracket()
    low_root = sqrt_bracket(4 * p.lower * time).lower
    high_root = sqrt_bracket(4 * p.upper * time).upper
    if low_root <= 0:
        raise ClockLimitError("sqrt precision insufficient for tiny heat time")
    e = exp_negative_bracket(x*x / (4*time))
    return RationalBracket(e.lower / high_root, e.upper / low_root)


def heat_density_error_bound(size, epsilon, sqrt_time_lower, radius):
    """Rational bound uniform over t>=a^2 and |n*epsilon|<=R, N even.

    A deliberately conservative version of the Fourier proof: all constants
    use 3<pi<4 and e^-x<=1/(1+x). Not a fitted error estimate.
    """
    _int(size, 2)
    if size % 2:
        raise ClockLimitError("this Nyquist certificate requires even N")
    epsilon = _q(epsilon, True)
    a = _q(sqrt_time_lower, True)
    radius = _q(radius)
    if radius < 0:
        raise ClockLimitError("nonnegative radius required")
    dispersion = epsilon**2 / a**3
    fourier_tail = epsilon / (18*a*a*(1 + 9*a*a/epsilon**2))
    quadrature = (8 + 4*radius/a) / (size * epsilon)
    return {"dispersion": dispersion, "fourier_tail": fourier_tail,
            "quadrature": quadrature,
            "total": dispersion + fourier_tail + quadrature}


def rational_character_product_exponent(a, b):
    """Global character compatibility at rational x=a/b (b>0).

    Return x-sum_p {x}_p, an exact integer.  Here {x}_p is reconstructed
    by CRT at each prime-power denominator; the real character has + sign,
    the finite local characters have - sign.  This is not a physical probe.
    """
    if type(a) is not int:
        raise ClockLimitError("integer numerator required")
    _int(b, 1)
    x = Q(a, b)
    denominator = x.denominator
    factors = []
    p = 2
    remaining = denominator
    while p*p <= remaining:
        if remaining % p == 0:
            power = 1
            while remaining % p == 0:
                remaining //= p
                power *= p
            factors.append(power)
        p += 1
    if remaining > 1:
        factors.append(remaining)
    pieces = []
    for power in factors:
        unit = denominator // power
        residue = x.numerator * pow(unit, -1, power) % power
        pieces.append(Q(residue, power))
    exponent = x - sum(pieces, Q(0))
    if exponent.denominator != 1:
        raise ArithmeticError("rational source character product failed")
    return {"real_exponent": x, "finite_fractional_parts": tuple(pieces),
            "total_exponent": exponent}
