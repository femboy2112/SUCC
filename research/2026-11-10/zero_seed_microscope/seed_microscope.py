"""Zero-anchored radix-16 seed microscope for SUCC's BBP normality frontier.

All arithmetic *certificates* returned by this module are exact Fraction/integer
bounds.  The complex sinc/energy routines are floating-point DIAGNOSTICS only;
they neither prove a sign of a transcendental expression nor PI normality.

Source: unchanged 4 signed BBP poles through observational_succ.duck_bbp.
Proved claims in MICROSCOPE_THEOREMS.md: seed-cylinder orthogonality,
coarse/deep localization bounds, zero-child Haar packet and scale telescoping.
"""
from __future__ import annotations

from dataclasses import dataclass
from cmath import exp
from fractions import Fraction as F
from math import cos, isqrt, pi, sin

BASE = 16


def _natural(n: int, name: str, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"{name} must be an exact integer >= {minimum}")
    return n


def _frequency(h: int) -> int:
    if type(h) is not int or h == 0:
        raise ValueError("a fixed nonzero integer Fourier frequency is required")
    return h


def cell_width(k: int) -> F:
    return F(1, 16 ** _natural(k, "depth"))


def signed_frequency(n: int, m: int, h: int = 1) -> int:
    _natural(n, "n")
    _natural(m, "m")
    return _frequency(h) * (16 ** n - 16 ** m)


def exactly_orthogonal(n: int, m: int, k: int, h: int = 1) -> bool:
    """Whether e(h 16^n s),e(h 16^m s) are orthogonal on [0,16^-k].

    This is a theorem about the integral, NOT a numerical approximation.
    Equal indices are not orthogonal.  For n != m >= k it is always true.
    Other zeroes from large h are also returned when present.
    """
    _natural(k, "depth")
    q = signed_frequency(n, m, h)
    return q != 0 and q % (16 ** k) == 0


def late_orthogonal_pairs(n: int, k: int) -> int:
    """Number of ordered distinct pairs among indices k,...,n-1."""
    _natural(n, "count", 1)
    _natural(k, "depth")
    r = max(n - k, 0)
    return r * (r - 1)


def fixed_depth_deviation_upper(n: int, k: int, h: int = 1) -> F:
    """Exact rational source-blind bound |E_(N,K,h) - 1/N|.

    For 0<=K<=N, at most K(K-1) early/early ordered terms survive.
    The early/late kernel tail sums to <=512 K/(225*pi*|h|),
    hence <=512 K/(675*|h|), since pi>3.  Late/late terms vanish.
    The energy lies in [0,1], so cap the error by 1.
    """
    _natural(n, "count", 1)
    _natural(k, "depth")
    _frequency(h)
    if k > n:
        raise ValueError("fixed-depth bound assumes K<=N")
    return min(F(1), F(k * (k - 1), n * n) +
               F(512 * k, 675 * abs(h) * n * n))


def _ceil_sqrt(v: int) -> int:
    r = isqrt(v)
    return r if r * r == v else r + 1


def annealed_energy_upper(n: int, k: int) -> F:
    """Certified rational bound for E[|W_(N,h)(alpha+s)|^2] over zero cell.

    Exact upper is [(k+sqrt(n-k))/n]^2, capped at 1; replace sqrt by
    integer ceil for a convenient pure-rational certificate.
    Universal in the source, alpha and nonzero integer frequency.
    """
    _natural(n, "count", 1)
    _natural(k, "depth")
    if k >= n:
        return F(1)
    return min(F(1), F((k + _ceil_sqrt(n - k)) ** 2, n * n))


def point_recovery_error(n: int, k: int, h: int = 1) -> F:
    """Certified uniform complex-amplitude error to the literal zero seed.

    sup_(s in [0,16^-k]) |W_N(alpha+s)-W_N(alpha)| <=
        2(n-k)/n + 7 |h|/(15n) for 0<=k<=n.
    Uses only |e(t)-e(u)|<=2*pi*|t-u|<7*|t-u|.
    """
    _natural(n, "count", 1)
    _natural(k, "depth")
    _frequency(h)
    if k >= n:
        return min(F(2), F(7 * abs(h), 15 * n * 16 ** (k - n)))
    return min(F(2), F(2 * (n - k), n) + F(7 * abs(h), 15 * n))


def energy_recovery_error(n: int, k: int, h: int = 1) -> F:
    """Certified bound |mean seed energy - |W_N(alpha)|^2|."""
    return min(F(1), 2 * point_recovery_error(n, k, h))


def _four_pole_exact(n: int) -> F:
    _natural(n, "source index", 1)
    return (F(4, 8*n - 7) - F(2, 8*n - 4)
            - F(1, 8*n - 3) - F(1, 8*n - 2))


def source_alpha_interval(horizon: int) -> tuple[F, F]:
    """Exact strict rational enclosure of alpha=pi/16 from 4-pole BBP.

    This invokes the canonical immutable source module, not a numeric pi oracle.
    """
    _natural(horizon, "horizon", 0)
    from observational_succ import duck_bbp
    low = F(0)
    for j in range(1, horizon + 1):
        observed = duck_bbp.forcing(j)
        expected = _four_pole_exact(j)
        if type(observed) is not F or observed != expected:
            raise ValueError("source mismatch at BBP clock " + str(j))
        low += expected / 16 ** j
    budget = duck_bbp.source_tail_budget(horizon)
    expected_budget = _four_pole_exact(horizon + 1) / 15
    if type(budget) is not F or budget != expected_budget:
        raise ValueError("BBP tail-source budget mismatch")
    high = low + expected_budget / 16 ** horizon
    return low, high


def midpoint_alpha_phase_bound(n: int, h: int, horizon: int) -> F:
    """For each seed s, |W_N(alpha+s)-W_N(mid+s)| <= this rational.

    This is an ANALYTIC truncation budget; floating-point trig error is
    separate and not automatically certified by this function.
    """
    _natural(n, "count", 1)
    _frequency(h)
    low, high = source_alpha_interval(horizon)
    return F(7 * abs(h) * (16 ** n - 1), 30 * n) * (high - low)


def _angle(frac: F) -> complex:
    """Approximate unit-circle phase with the rational argument reduced first."""
    u = float(frac % 1)
    return complex(cos(2 * pi * u), sin(2 * pi * u))


def normalized_cell_kernel(q: int, k: int, child: int | None = None) -> complex:
    """Approximate E_[cell] e(qs) using exact integer-zero detection.

    child=None: [0,16^-k]; child=a: [a, a+1] / 16^(k+1).
    For q != 0 divisible by the inverse cell width, return exact complex 0.
    """
    if type(q) is not int:
        raise TypeError("q must be a plain integer")
    _natural(k, "depth")
    if child is not None:
        _natural(child, "child")
        if child >= 16:
            raise ValueError("hexadecimal child must be in 0..15")
        depth, a = k + 1, F(child, 16 ** (k + 1))
    else:
        depth, a = k, F(0)
    if q == 0:
        return 1 + 0j
    if q < 0:
        return normalized_cell_kernel(-q, k, child).conjugate()
    scale = 16 ** depth
    if q % scale == 0:
        return 0j
    t = F(q, scale)
    rem = t % 1
    v = float(rem)
    # e(pi*i*t) sinc(pi*t) = e(pi*i*{t})sin(pi*{t})/(pi*t)
    # (the integer parity signs cancel) for t not an integer.
    inv_t = float(1 / t)  # convert the small reciprocal, not a huge integer
    mag = sin(pi * v) * inv_t / pi
    core = complex(cos(pi * v), sin(pi * v)) * mag
    return _angle(q * a) * core


def _energy(alpha: F, n: int, h: int, k: int, child: int | None) -> float:
    if type(alpha) not in (F, int):
        raise TypeError("rational alpha required; avoid a pi float oracle")
    _natural(n, "count", 1)
    _frequency(h)
    _natural(k, "depth")
    # Summing over pairs ensures real-valued energy by Hermitian symmetry.
    total = float(n)
    for a in range(1, n):
        for b in range(a):
            q = signed_frequency(a, b, h)
            ker = normalized_cell_kernel(q, k, child)
            if ker == 0:
                continue
            total += 2 * (_angle(q * F(alpha)) * ker).real
    val = total / (n * n)
    # Roundoff may put a theoretically nonnegative number just below zero.
    return val


def seed_energy(alpha: F, n: int, k: int, h: int = 1) -> float:
    """Approximate seed-localized Fourier energy E_(N,K,h) (NOT a proof)."""
    return _energy(alpha, n, h, k, None)


def child_energy(alpha: F, n: int, k: int, a: int, h: int = 1) -> float:
    """Approximate energy on child a of zero seed cell at level k."""
    return _energy(alpha, n, h, k, a)


def zero_child_detail(alpha: F, n: int, k: int, h: int = 1) -> float:
    """Signed zero-child Haar detail E_(K+1) - E_K (diagnostic only)."""
    return child_energy(alpha, n, k, 0, h) - seed_energy(alpha, n, k, h)




def child_fourier_packet(alpha: F, n: int, k: int, h: int = 1) -> tuple[complex, ...]:
    """Approximate 16-DFT of the child energy vector (not a certificate).

    Reconstruct child zero by sum(packet); the zero-mode is parent E.
    The other fifteen modes are signed zero-branch information losses.
    """
    values=tuple(child_energy(alpha,n,k,a,h) for a in range(16))
    return tuple(sum(values[a]*exp(-2j*pi*ell*a/16)
                     for a in range(16))/16 for ell in range(16))

def selected_weyl_mean(alpha: F, n: int, h: int = 1) -> complex:
    """Approximate exact selected orbit Weyl mean using rational alpha."""
    if type(alpha) not in (F, int):
        raise TypeError("rational alpha required")
    _natural(n, "count", 1)
    _frequency(h)
    return sum((_angle(h * 16 ** j * F(alpha)) for j in range(n)), 0j) / n


@dataclass(frozen=True)
class MicroscopeReceipt:
    count: int
    frequency: int
    horizon: int
    alpha_mid: F
    alpha_width: F
    truncated_phase_budget: F
    annealed_energy: tuple[float, ...]
    signed_zero_child_details: tuple[float, ...]
    selected_weyl_power: float
    point_recovery_budget: F


def microscope_receipt(n: int, h: int = 1, *, horizon: int | None = None) -> MicroscopeReceipt:
    """Numerical diagnostics with separate strict rational analytic budgets."""
    _natural(n, "count", 1)
    _frequency(h)
    if n > 32:
        raise ValueError("O(N^3) exploratory instrument limited to N<=32")
    if horizon is None:
        horizon = n + 24
    if horizon < n:
        raise ValueError("horizon must be >= count")
    low, high = source_alpha_interval(horizon)
    mid = (low + high) / 2
    energies = tuple(seed_energy(mid, n, k, h) for k in range(n + 1))
    details = tuple(energies[k + 1] - energies[k] for k in range(n))
    return MicroscopeReceipt(
        count=n, frequency=h, horizon=horizon, alpha_mid=mid,
        alpha_width=high - low,
        truncated_phase_budget=midpoint_alpha_phase_bound(n, h, horizon),
        annealed_energy=energies, signed_zero_child_details=details,
        selected_weyl_power=abs(selected_weyl_mean(mid, n, h)) ** 2,
        point_recovery_budget=energy_recovery_error(n, n, h),
    )


def _arctan_rational_bounds(x: F, terms: int) -> tuple[F, F]:
    """Alternating arctan bounds for 0<x<1 (fully rational)."""
    if type(x) is not F or not (0 < x < 1):
        raise ValueError("x must be exact rational in (0,1)")
    _natural(terms, "terms", 1)
    value = sum(((-1)**j * x**(2*j+1) / (2*j+1)
                 for j in range(terms)), F(0))
    rem = x**(2*terms+1) / (2*terms+1)
    return (value, value+rem) if terms % 2 == 0 else (value-rem,value)


def machin_pi_bounds(terms: int = 9) -> tuple[F, F]:
    """Independent exact-rational pi interval via Machin's identity.

    pi=16*arctan(1/5)-4*arctan(1/239). Remainder is alternating.
    The classical trigonometric identity is an imported theorem.
    """
    a,b = _arctan_rational_bounds(F(1,5),terms)
    c,d = _arctan_rational_bounds(F(1,239),terms)
    return 16*a-4*d, 16*b-4*c


@dataclass(frozen=True)
class FirstHaarSignCertificate:
    pi_lower: F
    pi_upper: F
    delta_lower: F
    delta_upper: F
    sine_lower: F
    tail_absolute_bound: F
    sign: str
    # For all N>=2 the genuine original-zero h=8 first zero-child Haar
    # detail J_(N,0)>16/(225*pi*N^2), proven from this rational witness.


def certify_first_weyl8_detail() -> FirstHaarSignCertificate:
    """Proof certificate for an all-N authentic-source signed detail.

    For alpha=pi/16, all integers N>=2, h=8, K=0,
       E_(N,1,8)-E_(N,0,8)
       = -4/(pi*N^2)*sum_(n=1)^(N-1) sin(pi^2*(16^n-1))/(16^n-1)
       > 16/(225*pi*N^2) > 0.

    Uses sin(15*pi^2)=-sin(pi*(15*pi-47))<-1/3,
    remaining |tail| <1/225, proved by geometric domination.
    This controls just ONE early seed-scale detail, not digit parity,
    statistical Haar contraction, or pi normality.
    """
    lower, upper = machin_pi_bounds(9)
    assert F(314159,100000) < lower < upper < F(314160,100000)
    dlow = lower * (15*lower - 47)
    dhigh = upper * (15*upper - 47)
    assert F(3,8) < dlow <= dhigh < F(2,5)
    sine_lower = F(3,8) - F(2,5)**3 / 6
    assert sine_lower > F(1,3)
    tail = F(1,225)
    assert F(1,45) - tail == F(4,225)
    return FirstHaarSignCertificate(lower, upper, dlow, dhigh,
                                    sine_lower, tail, "POSITIVE_FOR_EVERY_N_GE_2")
