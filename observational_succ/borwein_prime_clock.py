"""Exact Borwein-uniform convolution, modular delta gates, and SUCC walk.

This is a CALIBRATED arithmetic model, not a derived global prime distribution.
Sinc kernels encode independent CONTINUOUS uniform jumps; residues need a
SEPARATE exact prime-clock projector. Brownian diffusion arises only under a
declared small-step scaling, not merely from naming a Borwein product.

No floating-point quadrature, zero locations, quantum phases, Weil positivity,
ABC proof, or RH proof enter the finite exact computations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import factorial, gcd, isqrt, prod

MAX_WIDTH_COUNT = 11
MAX_PRIME = 1000
MAX_WHEEL = 30030
MAX_STEPS = 12


class BorweinClockError(ValueError):
    """Malformed prime source, nonadmissible step, or finite resource budget."""


def _int(n: int, name: str, lo: int = 0, hi: int = 1_000_000) -> int:
    if type(n) is not int or not lo <= n <= hi:
        raise BorweinClockError(f"{name} must be an exact integer in {lo}..{hi}")
    return n


def _widths(widths: tuple[Q, ...]) -> tuple[Q, ...]:
    if type(widths) is not tuple or not 1 <= len(widths) <= MAX_WIDTH_COUNT:
        raise BorweinClockError("nonempty finite tuple of at most 11 widths required")
    if any(type(a) is not Q or a <= 0 for a in widths):
        raise BorweinClockError("every jump half-width must be a positive Fraction")
    return widths


def prime(q: int) -> bool:
    if type(q) is not int or q < 2 or q > MAX_PRIME:
        return False
    return all(q % d for d in range(2, isqrt(q)+1))


def prime_clocks(clocks: tuple[int, ...]) -> tuple[int, ...]:
    if type(clocks) is not tuple or not 1 <= len(clocks) <= MAX_WIDTH_COUNT:
        raise BorweinClockError("nonempty prime-clock tuple required")
    if clocks != tuple(sorted(set(clocks))) or not all(prime(q) for q in clocks):
        raise BorweinClockError("distinct ascending genuine primes required")
    return clocks


def positive_part_power(x: Q, k: int) -> Q:
    return max(x, Q(0)) ** k


def uniform_sum_cdf(widths: tuple[Q, ...], threshold: Q) -> Q:
    """Exact CDF of independent uniform[-a_j,+a_j] jumps.

    Finite nonidentical-uniform inclusion/exclusion. The 1/m! comes from
    m-dimensional simplex volume. This is an EXACT rational computation.
    """
    widths = _widths(widths)
    if type(threshold) is not Q:
        raise BorweinClockError("exact rational threshold required")
    m = len(widths)
    if threshold < -sum(widths):
        return Q(0)
    if threshold >= sum(widths):
        return Q(1)
    t = threshold + sum(widths)
    signed = Q(0)
    for mask in range(1<<m):
        displaced = 2 * sum((widths[j] for j in range(m)
                             if mask & (1<<j)), Q(0))
        term = positive_part_power(t-displaced, m)
        signed += -term if mask.bit_count() % 2 else term
    result = signed / (2**m * factorial(m) * prod(widths))
    if not Q(0) <= result <= Q(1):
        raise AssertionError("inclusion-exclusion produced an invalid CDF")
    return result


def borwein_window_mass(widths: tuple[Q, ...], shift: Q = Q(0)) -> Q:
    """Probability |shift + sum_j U[-a_j,+a_j]| <= 1.

    Equals 2/pi times integral_0^infinity sinc(x) cos(shift*x)
    product_j sinc(a_j*x) dx; no numerical oscillatory integration.
    """
    widths = _widths(widths)
    if type(shift) is not Q:
        raise BorweinClockError("shift must be a Fraction")
    p = uniform_sum_cdf(widths, Q(1)-shift) - uniform_sum_cdf(
        widths, -Q(1)-shift)
    if not Q(0) <= p <= Q(1):
        raise AssertionError("exact Borwein window mass leaves [0,1]")
    return p


def first_boundary_leak(widths: tuple[Q, ...]) -> Q:
    """Exact Borwein leakage simplex formula ONLY at first shallow crossing."""
    widths = _widths(widths)
    excess = sum(widths) - 1
    if excess <= 0:
        return Q(0)
    if excess > 2 * min(widths):
        raise BorweinClockError("beyond first-simplex boundary; use full formula")
    m = len(widths)
    return excess**m / (2**(m-1) * factorial(m) * prod(widths))


def prime_borwein_widths(clocks: tuple[int, ...]) -> tuple[Q, ...]:
    """A user-chosen analytic model a_q=1/q; DOES NOT inspect n modulo q."""
    return tuple(Q(1, q) for q in prime_clocks(clocks))


def clock_gate(n: int, q: int, kind: str = "one") -> bool:
    """Genuine prime-clock projector onto phase 1, -1 or a nonzero residue."""
    _int(n, "state", 0, 10**12)
    if not prime(q):
        raise BorweinClockError("only genuine prime clocks allowed")
    if kind == "one":
        return n % q == 1
    if kind == "minus_one":
        return n % q == q-1
    if kind == "nonzero":
        return n % q != 0
    raise BorweinClockError("kind must be one, minus_one, or nonzero")


def exact_character_projector(n: int, q: int, phase: int) -> int:
    """Cyclotomic orthogonality: (1/q) sum exp(2pi*i*j*(n-phase)/q).

    Evaluate symbolically: q if the character exponent is 0 mod q, else
    all q distinct powers sum to zero. No floating-point root comparisons.
    """
    _int(n, "state", 0, 10**12)
    _int(phase, "target residue", 0, MAX_PRIME-1)
    if not prime(q) or phase >= q:
        raise BorweinClockError("target phase must belong to a genuine q-clock")
    exponents = sorted((j*(n-phase)) % q for j in range(q))
    if exponents == [0]*q:
        return 1
    if exponents != list(range(q)):
        raise AssertionError("prime-clock character orthogonality violated")
    return 0


def phase_distance(n: int, q: int) -> Q:
    """Canonical circular distance to residue 1, normalized by q."""
    if not prime(q):
        raise BorweinClockError("phase source must be prime")
    k = (n-1) % q
    return Q(min(k, q-k), q)


def softened_prime_clock_score(n: int, clocks: tuple[int, ...],
                               scale: Q = Q(1)) -> Q:
    """Explicit arbitrary SOFT model; not a replacement for exact deltas.

    Sum of nonnegative circular distances D(n) is shifted into a Borwein
    uniform window. Plateau may hide real source-phase distinctions.
    """
    _int(n, "integer", 1, 10**12)
    clocks = prime_clocks(clocks)
    if type(scale) is not Q or scale < 0:
        raise BorweinClockError("nonnegative rational scale required")
    shift = scale * sum((phase_distance(n, q) for q in clocks), Q(0))
    return borwein_window_mass(prime_borwein_widths(clocks), shift)


@dataclass(frozen=True)
class GatedStep:
    """Uniform integer jitter then a genuine SUCC shift then a delta gate."""
    half_width: int
    succ: int
    prime: int
    kind: str

    def __post_init__(self) -> None:
        _int(self.half_width, "uniform discrete half-width", 0, 10)
        _int(self.succ, "SUCC displacement", 0, 100)
        if not prime(self.prime) or self.kind not in ("one", "minus_one", "nonzero"):
            raise BorweinClockError("gated transition has invalid prime or residue")


@dataclass(frozen=True)
class GatedWalk:
    modulus: int
    survivors: Q
    final_distribution: tuple[tuple[int, Q], ...]

    @property
    def discarded(self) -> Q:
        return Q(1)-self.survivors


def exact_gated_succ_walk(start: int, clocks: tuple[int, ...],
                          steps: tuple[GatedStep, ...]) -> GatedWalk:
    """Exact sub-Markov composition P_m S^s_m K_m ... P_1 S^s_1 K_1.

    K_j has discrete uniform jumps [-h_j,h_j], S is +1 SUCC.
    Modular gates P_q are independent SOURCE readouts, not sinc kernels.
    """
    _int(start, "start state", 0, 10**12)
    clocks = prime_clocks(clocks)
    W = prod(clocks)
    if W > MAX_WHEEL:
        raise BorweinClockError("finite wheel modulus budget exceeded")
    if type(steps) is not tuple or not 1 <= len(steps) <= MAX_STEPS:
        raise BorweinClockError("bounded tuple of 1..12 gated transitions needed")
    if any(type(s) is not GatedStep or s.prime not in clocks for s in steps):
        raise BorweinClockError("all gates must belong to the declared wheel")
    weights = {start % W: Q(1)}
    for s in steps:
        next_weights: dict[int, Q] = {}
        for state, mass in weights.items():
            for jump in range(-s.half_width, s.half_width+1):
                nxt = (state+jump+s.succ) % W
                if clock_gate(nxt, s.prime, s.kind):
                    next_weights[nxt] = next_weights.get(nxt, Q(0)) + (
                        mass / (2*s.half_width+1))
        weights = next_weights
    survival = sum(weights.values(), Q(0))
    if not Q(0) <= survival <= Q(1):
        raise AssertionError("sub-Markov prime gates created mass")
    return GatedWalk(W, survival, tuple(sorted(weights.items())))


def symmetric_succ_return_coefficients(wheel: int, max_jumps: int
                                        ) -> tuple[Q, ...]:
    """Coefficients c_m=Prob(symmetric +/-1 walker returns to 0 after m).

    Continuous-time symmetric Poisson SUCC return is exactly
    exp(-t)*sum_{m>=0} t**m/m! * c_m. This routine returns finite
    c_m, not an unjustified exact infinite series or Brownian identity.
    """
    _int(wheel, "cyclic wheel size", 3, MAX_WHEEL)
    _int(max_jumps, "jump-count bound", 0, 100)
    weights = {0: Q(1)}
    out = [Q(1)]
    for _ in range(max_jumps):
        next_weights: dict[int, Q] = {}
        for x, mass in weights.items():
            for d in (-1, +1):
                nxt = (x+d) % wheel
                next_weights[nxt] = next_weights.get(nxt, Q(0)) + mass/2
        weights = next_weights
        out.append(weights.get(0, Q(0)))
    return tuple(out)


def uniform_cumulant_four(widths: tuple[Q, ...]) -> Q:
    """Independent uniform jump fourth cumulant: -2/15 sum_j a_j^4.

    A strictly negative value REFUTES an EXACT Gaussian law for any
    nontrivial finite uniform sum, even if Gaussian approximation is useful.
    """
    widths = _widths(widths)
    return -Q(2, 15)*sum((a**4 for a in widths), Q(0))
