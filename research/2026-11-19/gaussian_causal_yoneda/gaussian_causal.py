"""Exact-rational BBP source and Gaussian-circle observer calibration.

Research-only. All Gaussian formulas are deterministic analytic identities; no
random sampling, pi-normality assumption, or source-forcing mutation is used.
"""

from fractions import Fraction
import cmath
import math

POLES = (7, 4, 3, 2)
COEFFS = (4, -2, -1, -1)


def forcing(n, coeffs=COEFFS):
    if n < 1 or len(coeffs) != 4:
        raise ValueError("positive integer n and four coefficients required")
    return sum((Fraction(c, 8 * n - b) for c, b in zip(coeffs, POLES)), Fraction(0))


def state(n, seed=Fraction(0), coeffs=COEFFS):
    if n < 0:
        raise ValueError("n must be nonnegative")
    u = Fraction(seed)
    for j in range(1, n + 1):
        u = 16 * u + forcing(j, coeffs)
    return u


def finite_tail(n, horizon):
    """Exact source-tail contribution from times n+1 through horizon."""
    if n < 0 or horizon < n:
        raise ValueError("require 0 <= n <= horizon")
    return sum((Fraction(1, 16**j) * forcing(n + j)
                for j in range(1, horizon - n + 1)), Fraction(0))


def prefix_x(horizon):
    """Exact rational BBP prefix for x = pi/16."""
    return sum((Fraction(1, 16**j) * forcing(j)
                for j in range(1, horizon + 1)), Fraction(0))


def tail_upper(n):
    if n < 1:
        raise ValueError("bound is stated for n >= 1")
    return Fraction(1, 64 * n * n)


def jacobian_row(n):
    """Derivative d U_n / d(seed,c1,c2,c3,c4) in the affine family."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return (Fraction(16**n),) + tuple(
        sum((Fraction(16**(n - j), 8 * j - b)
             for j in range(1, n + 1)), Fraction(0))
        for b in POLES)


def fraction_mod1(x):
    x = Fraction(x)
    return float(Fraction(x.numerator % x.denominator, x.denominator))


def gaussian_sums(cutoff=12, lam=1.0):
    """Two-sided truncated Q=sum w, S=sum k^2 w, R=sum |k|w."""
    if cutoff < 1 or lam <= 0:
        raise ValueError("positive cutoff and heat parameter required")
    weights = [math.exp(-lam * k * k) for k in range(1, cutoff + 1)]
    return (2 * sum(weights),
            2 * sum(k * k * w for k, w in enumerate(weights, 1)),
            2 * sum(k * w for k, w in enumerate(weights, 1)))


def gaussian_tail(power, cutoff=6, lam=1.0):
    """Rigorous real-arithmetic geometric upper bound for two-sided tails.

    Up to the floating-point evaluation of exp. For a formal/certified numeric
    bound, outward-round these elementary operations with interval arithmetic.
    """
    if power < 0 or cutoff < 1 or lam <= 0:
        raise ValueError("invalid tail inputs")
    start = cutoff + 1
    a = start**power * math.exp(-lam * start * start)
    ratio = ((start + 1) / start)**power * math.exp(-lam * (2 * start + 1))
    if ratio >= 1:
        raise ValueError("increase cutoff to make geometric bound valid")
    return 2 * a / (1 - ratio)


def gaussian_displacement(phase, cutoff=12, lam=1.0):
    """Truncated ||K(.-phase)-K||_L2^2 on the unit circle."""
    if cutoff < 1 or lam <= 0:
        raise ValueError("positive cutoff and heat parameter required")
    return 8 * sum(math.exp(-lam * k * k) *
                   math.sin(math.pi * k * phase)**2
                   for k in range(1, cutoff + 1))


def phase_moment(phases, h):
    if not phases:
        raise ValueError("need at least one phase")
    return sum((cmath.exp(2j * math.pi * h * p) for p in phases), 0j) / len(phases)


def gaussian_haar_discrepancy(phases, cutoff=12, lam=1.0):
    """Truncated ||B^-1 sum K(.-phase)-1||_L2^2."""
    return 2 * sum(math.exp(-lam * h * h) * abs(phase_moment(phases, h))**2
                   for h in range(1, cutoff + 1))


def gaussian_shell_source(B, cutoff=12, lam=1.0):
    """Truncated rational-source Ehat and Vhat; phases come from exact U_n."""
    if B < 1:
        raise ValueError("B must be >=1")
    phases = [fraction_mod1(state(n)) for n in range(B, 2 * B)]
    return (sum(gaussian_displacement(p, cutoff, lam) for p in phases) / B,
            gaussian_haar_discrepancy(phases, cutoff, lam))


def gaussian_phase_attenuation(n, sigma, h=1):
    """Exact analytic multiplier for Gaussian noise added to the BBP seed."""
    return math.exp(-2 * math.pi**2 * (h * (16**n) * sigma)**2)


def output_covariance(row_a, row_b, variance):
    """Cov(U_a,U_b) for independent Gaussian parameter innovations."""
    if len(row_a) != len(row_b):
        raise ValueError("incompatible Jacobian rows")
    return Fraction(variance) * sum((a*b for a, b in zip(row_a, row_b)), Fraction(0))


def terminal_shell_source(B, horizon=None, cutoff=12, lam=1.0):
    """Finite rational terminal x_M and Gaussian shell energies, B<=n<2B."""
    if B < 1:
        raise ValueError("B must be positive")
    if horizon is None:
        horizon = 2*B
    if horizon < 2*B:
        raise ValueError("horizon must cover entire target shell")
    endpoint = prefix_x(horizon)
    phases = [fraction_mod1(16**n * endpoint) for n in range(B,2*B)]
    return (sum(gaussian_displacement(p,cutoff,lam) for p in phases)/B,
            gaussian_haar_discrepancy(phases,cutoff,lam))


def terminal_phase_error_upper(B, horizon=None):
    """Rational bound on |16^n*(x-P_horizon)| for every B<=n<2B."""
    if B < 1:
        raise ValueError("B must be positive")
    if horizon is None:
        horizon = 2*B
    if horizon < 2*B:
        raise ValueError("horizon must cover entire target shell")
    return Fraction(1, 16**(horizon-(2*B-1))*64*horizon*horizon)


def source_gaussian_step_defect(n, cutoff=12, lam=1.0):
    """Squared Gaussian diagram defect ||K_(U_(n+1))-K_(16U_n)||^2."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return gaussian_displacement(float(forcing(n+1)),cutoff,lam)
