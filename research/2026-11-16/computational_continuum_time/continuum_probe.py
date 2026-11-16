"""Independent stdlib exact/finite probes for computational continuum time.

Research-only instrument. No pi normality claim. Original BBP four-pole forcing,
zero seed, source-lift histories and integer deck shifts remain typed separately.
"""

from fractions import Fraction
from math import cos, sin, pi, log, sqrt


def forcing(n: int) -> Fraction:
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def rational_history(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    y = Fraction(seed)
    for j in range(1, n+1):
        y = 16*y + forcing(j)
    return y


def source_tail_interval(n: int, depth: int) -> tuple[Fraction, Fraction]:
    """Original source's strict rational tail interval (upper endpoint conservative)."""
    if not isinstance(n, int) or n < 0 or not isinstance(depth, int) or depth < 0:
        raise ValueError("n and depth must be nonnegative integers")
    partial = sum((forcing(n+j)/16**j for j in range(1, depth+1)), Fraction())
    return partial, partial + forcing(n+depth+1)/Fraction(15*16**depth)


def completed_orbit_interval(n: int, depth: int) -> tuple[Fraction, Fraction]:
    y = rational_history(n)
    low, high = source_tail_interval(n, depth)
    return y+low, y+high


def fractional_part(x: Fraction) -> Fraction:
    x = Fraction(x)
    return x - (x.numerator // x.denominator)


def solenoid_history(x: Fraction, depth: int) -> tuple[Fraction, ...]:
    """Canonical source-selected inverse-limit prefix from the REAL lift x.

    The returned coordinates are x/16**j mod 1, not a continuously traversed
    2-adic path. Other prehistories of the same circle point exist.
    """
    if depth < 1:
        raise ValueError("depth >= 1 required")
    x = Fraction(x)
    return tuple(fractional_part(x / 16**j) for j in range(depth))


def solenoid_shift(prefix: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Finite prefix of natural-extension homeomorphism, length preserved."""
    if not prefix:
        raise ValueError("nonempty prefix required")
    return (fractional_part(16*prefix[0]),) + prefix[:-1]


def relative_winding(k: int, n: int = 0) -> int:
    """Relative winding for real-lift deck shift k on tick [n,n+1]."""
    if not isinstance(k, int) or not isinstance(n, int) or n < 0:
        raise ValueError("integer k and n >= 0 required")
    return 15*k*16**n


def complex_phase(t: float, x: float) -> complex:
    angle = 2*pi*(16**t)*x
    return complex(cos(angle), sin(angle))


def path_distance_squared(x: float, y: float, segments: int = 4096) -> float:
    """Simpson approximation to integral_0^1 |gamma_x-gamma_y|^2 dt.

    Numerical diagnostics only. Analytic proof and integer-k bound are in
    THEOREMS.md; this function is not interval arithmetic.
    """
    if segments <= 0 or segments % 2:
        raise ValueError("positive even number of segments required")
    diff = float(x)-float(y)
    def integrand(s):
        return 2-2*cos(2*pi*diff*16**s)
    accum = integrand(0)+integrand(1)
    for j in range(1, segments):
        accum += (4 if j % 2 else 2)*integrand(j/segments)
    return accum/(3*segments)


def integer_deck_metric_bound(k: int) -> tuple[float, float]:
    """Proved analytic enclosure for path-distance squared when x-y=k."""
    if not isinstance(k, int) or k == 0:
        raise ValueError("nonzero integer deck shift required")
    eps = 15/(16*pi*abs(k)*log(16))
    return 2-eps, 2+eps


def gamma_alpha_one_upper_bound(x: float, t: float) -> float:
    """Analytic upper bound on |E gamma_x(t+Exp(1))|, x != 0."""
    if x == 0 or t < 0:
        raise ValueError("nonzero real x and t >= 0 required")
    return 1/(pi*abs(x)*log(16)*16**t)


def gamma_translation_multiplier(alpha: float, omega: float) -> complex:
    """Gamma(shape alpha, rate 1) time-translation multiplier for exp(i omega t)."""
    if alpha < 0:
        raise ValueError("positive probability depth required")
    return (1-1j*omega)**(-alpha)


def gamma_variance_identity(observations: list[complex], weights: list[float]) -> tuple[float, float, float]:
    if len(observations) != len(weights) or not observations:
        raise ValueError("equal nonempty lengths required")
    if min(weights) < 0 or abs(sum(weights)-1) > 1e-12:
        raise ValueError("normalized nonnegative weights required")
    m = sum(w*z for w,z in zip(weights, observations))
    total = sum(w*(abs(z)**2) for w,z in zip(weights, observations))
    variance = sum(w*(abs(z-m)**2) for w,z in zip(weights, observations))
    return total, abs(m)**2, variance


if __name__ == "__main__":
    print("source", forcing(1), "U2", rational_history(2))
    print("lifted step winding k=1 n=3", relative_winding(1, 3))
    for k in (1, 2, 5, 11):
        d2 = path_distance_squared(0, k, 8192)
        print("deck k", k, "metric_sq", round(d2, 10),
              "rigorous_enclosure", integer_deck_metric_bound(k))
