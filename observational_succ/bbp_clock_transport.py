"""Sharp Fourier-energy transport and locally congruent hostile BBP seeds.

This is a narrow rederivation, not an import of the conflicting sibling
mobius_refined_matrix module. Comparison source: PR299, exact commit
1d5df4509c6e2042406e3067991b33b8b9fd41fe. All arithmetic instruments are
exact; analytic inequalities are proved in BBP_CLOCK_TRANSPORT.md.
No normality conclusion is inferred from a transport or a counterfeit.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt, prod

from .succ_internal_matrix_walk import PhasePoly, authentic_r


def _integer(value, name, minimum=1, maximum=100000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"invalid exact integer {name}")
    return value


def _rational(value, name):
    if type(value) not in (int, Q):
        raise ValueError(f"exact rational {name} required")
    return Q(value)


def _probabilities(weights, length):
    if not isinstance(weights, tuple) or len(weights) != length:
        raise ValueError("weight tuple must match the history")
    values = tuple(_rational(x, "weight") for x in weights)
    if any(x < 0 for x in values) or sum(values, Q()) != 1:
        raise ValueError("nonnegative weights of total mass one required")
    return values


def _phases(history):
    if not isinstance(history, tuple) or not 1 <= len(history) <= 256:
        raise ValueError("nonempty bounded exact history tuple required")
    return tuple(_rational(x, "phase") for x in history)


def _mode(history, weights, frequency):
    return sum((PhasePoly.monomial(frequency*x, w)
                for x, w in zip(history, weights)), PhasePoly.zero())


def weighted_spectral_excess(history, weights, width):
    """Formal E=tr(A^2)/H-1 for a declared weighted circle history."""
    xs = _phases(history)
    ws = _probabilities(weights, len(xs))
    H = _integer(width, "width", maximum=64)
    result = PhasePoly.zero()
    for j in range(1, H):
        mean = _mode(xs, ws, j)
        result += Q(2*(H-j), H)*mean*mean.star()
    return result


def weighted_feature_difference_squared(history, first, second, width):
    """Exact squared norm BEFORE the reverse-triangle transport step."""
    xs = _phases(history)
    a = _probabilities(first, len(xs))
    b = _probabilities(second, len(xs))
    H = _integer(width, "width", maximum=64)
    result = PhasePoly.zero()
    for j in range(1, H):
        change = _mode(xs, a, j)-_mode(xs, b, j)
        result += Q(2*(H-j), H)*change*change.star()
    return result


def root_energy_transport_squared(width, l1_distance):
    """Bound |sqrt(E_mu)-sqrt(E_nu)|^2 by H*||mu-nu||_1^2/2.

    Width one is identically zero. For labelled samples the supplied l1
    may exceed the pushforward measure distance, which is still safe.
    """
    H = _integer(width, "width")
    delta = _rational(l1_distance, "l1 distance")
    if not 0 <= delta <= 2:
        raise ValueError("probability l1 distance must be between zero and two")
    return Q() if H == 1 else Q(H, 2)*delta*delta


def balanced_clock_weights(horizon, modulus):
    """Reweight the actual times 1..N; every residue must be observed."""
    N = _integer(horizon, "horizon")
    modulus = _integer(modulus, "modulus", maximum=N)
    counts = [0]*modulus
    for n in range(1, N+1):
        counts[n % modulus] += 1
    return tuple(Q(1, modulus*counts[n % modulus]) for n in range(1, N+1))


@dataclass(frozen=True)
class ClockTransportBudget:
    horizon: int
    modulus: int
    width: int
    l1_distance: Q
    squared_root_energy_error: Q
    coarse_squared_error: Q
    balanced_energy_proved_small: bool = False
    normality_proved: bool = False


def clock_transport_budget(horizon, modulus, width):
    N = _integer(horizon, "horizon")
    modulus = _integer(modulus, "modulus", maximum=N)
    H = _integer(width, "width")
    remainder = N % modulus
    delta = Q(2*remainder*(modulus-remainder), N*modulus)
    sharp = root_energy_transport_squared(H, delta)
    coarse = Q() if H == 1 else Q(H*modulus*modulus, 8*N*N)
    if sharp > coarse:
        raise ArithmeticError("exact clock cost exceeds its analytic envelope")
    return ClockTransportBudget(N, modulus, H, delta, sharp, coarse)


def conditional_energy(history, labels, weights, frequency=1):
    """Formal weighted conditional energy; empty/zero-mass cells contribute 0."""
    xs = _phases(history)
    ws = _probabilities(weights, len(xs))
    if (not isinstance(labels, tuple) or len(labels) != len(xs)
            or any(type(label) is not int for label in labels)):
        raise ValueError("integer partition labels must match the history")
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero integer frequency required")
    result = PhasePoly.zero()
    for label in sorted(set(labels)):
        members = tuple(i for i, value in enumerate(labels) if value == label)
        mass = sum((ws[i] for i in members), Q())
        if not mass:
            continue
        mean = sum((PhasePoly.monomial(frequency*xs[i], ws[i])
                    for i in members), PhasePoly.zero())
        result += mean*mean.star()/mass
    return result


def refinement_gain(history, coarse, fine, weights, frequency=1):
    """Nested conditional gain, not an unordered Mobius contrast."""
    # Validate both partitions, even before checking refinement membership.
    coarse_energy = conditional_energy(history, coarse, weights, frequency)
    fine_energy = conditional_energy(history, fine, weights, frequency)
    membership = {}
    for a, b in zip(coarse, fine):
        if b in membership and membership[b] != a:
            raise ValueError("fine partition does not refine the coarse partition")
        membership[b] = a
    return fine_energy-coarse_energy


def _prime(value):
    _integer(value, "prime", minimum=2, maximum=10000)
    if any(value % d == 0 for d in range(2, isqrt(value)+1)):
        raise ValueError("genuine prime required")
    return value


def rational_valuation(value, prime):
    """Finite p-adic valuation; zero has no finite integer valuation."""
    x = _rational(value, "valuation input")
    p = _prime(prime)
    if x == 0:
        raise ValueError("zero has infinite valuation")
    numerator, denominator = abs(x.numerator), x.denominator
    result = 0
    while numerator % p == 0:
        numerator //= p
        result += 1
    while denominator % p == 0:
        denominator //= p
        result -= 1
    return result


@dataclass(frozen=True)
class CongruentSeedControl:
    horizon: int
    start: int
    prime_depths: tuple[tuple[int, int], ...]
    local_modulus: int
    rounding_denominator: int
    target_seed: Q
    initial: Q
    authentic_history: tuple[Q, ...]
    changed_history: tuple[Q, ...]
    seed_rounding_error_upper: Q
    window_radius: Q
    gain_upper_h1: Q
    authentic_zero_initial: bool = False
    infinite_nonnormal_orbit_established: bool = False


def _prime_depths(depths):
    if not isinstance(depths, tuple) or len(depths) > 32:
        raise ValueError("bounded prime-depth tuple required")
    if any(not isinstance(item, tuple) or len(item) != 2 for item in depths):
        raise ValueError("prime/depth pairs required")
    for p, k in depths:
        _prime(p)
        _integer(k, "prime depth", maximum=100)
    if tuple(sorted(depths)) != depths or len({p for p, _ in depths}) != len(depths):
        raise ValueError("prime-depth pairs must be sorted and distinct")
    return depths


def congruent_seed_control(horizon, start, prime_depths=()):
    """Exact BBP forcing, finite local state agreement, WRONG initial seed.

    Constraining the rounded numerator to a multiple of M preserves any
    supplied finite p-adic precisions at every time. The integer zero anchor
    is deliberately violated; this is not an alternate authenticated source.
    """
    N = _integer(horizon, "horizon", maximum=256)
    m = _integer(start, "start", maximum=N)
    depths = _prime_depths(prime_depths)
    M = prod(p**k for p, k in depths)
    target = -sum((authentic_r(j)/16**j for j in range(1, N+1)), Q())
    D = 1+128*m*m*M*16**N
    rounding = D*target/M+Q(1, 2)
    initial = Q(M*(rounding.numerator//rounding.denominator), D)
    original, changed = Q(), initial
    history, mutant = [], []
    for n in range(1, N+1):
        original = 16*original+authentic_r(n)
        changed = 16*changed+authentic_r(n)
        history.append(original)
        mutant.append(changed)
    result = CongruentSeedControl(
        N, m, depths, M, D, target, initial, tuple(history), tuple(mutant),
        Q(1, 256*m*m*16**N), Q(5, 256*m*m), Q(5, 128*m**4),
    )
    verify_congruent_seed_control(result)
    return result


def verify_congruent_seed_control(control):
    """Recheck source forcing, lift, local congruences and finite coherence."""
    if type(control) is not CongruentSeedControl:
        raise ValueError("congruent-seed certificate required")
    c = control
    N = _integer(c.horizon, "horizon", maximum=256)
    m = _integer(c.start, "start", maximum=N)
    depths = _prime_depths(c.prime_depths)
    M = prod(p**k for p, k in depths)
    D = 1+128*m*m*M*16**N
    target = -sum((authentic_r(j)/16**j for j in range(1, N+1)), Q())
    rounding = D*target/M+Q(1, 2)
    initial = Q(M*(rounding.numerator//rounding.denominator), D)
    if (c.local_modulus != M or c.rounding_denominator != D or c.target_seed != target
            or c.initial != initial or c.initial == 0 or gcd(D, M) != 1 or D % 2 != 1):
        raise ValueError("constrained rounding or source target mismatch")
    if (c.seed_rounding_error_upper != Q(1, 256*m*m*16**N)
            or c.window_radius != Q(5, 256*m*m)
            or c.gain_upper_h1 != Q(5, 128*m**4)
            or c.authentic_zero_initial or c.infinite_nonnormal_orbit_established):
        raise ValueError("countermodel bound or authority mismatch")
    if abs(initial-target) >= c.seed_rounding_error_upper:
        raise ArithmeticError("seed rounding bound failed")
    if len(c.authentic_history) != N or len(c.changed_history) != N:
        raise ValueError("source horizon mismatch")
    original, changed = Q(), initial
    for n, (u, v) in enumerate(zip(c.authentic_history, c.changed_history), 1):
        if type(u) is not Q or type(v) is not Q:
            raise ValueError("exact lifted state required")
        if u != 16*original+authentic_r(n) or v != 16*changed+authentic_r(n):
            raise ValueError("original forcing or authentic lift mismatch")
        difference = v-u
        if difference != 16**n*initial:
            raise ArithmeticError("seed difference recurrence failed")
        for p, k in depths:
            if rational_valuation(difference, p) < k+(4*n if p == 2 else 0):
                raise ArithmeticError("finite local state precision lost")
        if n >= m and abs(v) >= c.window_radius:
            raise ArithmeticError("coherent finite window bound failed")
        original, changed = u, v
    for p, k in depths:
        if rational_valuation(initial, p) < k:
            raise ArithmeticError("initial local precision lost")
    return True


def seed_gain_upper(control, frequency=1):
    """Upper bound uniform over every partition and probability weighting."""
    verify_congruent_seed_control(control)
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero integer frequency required")
    return control.gain_upper_h1*frequency*frequency


def seed_matrix_deficit_upper(control, width):
    """Bound (H-1)-E, uniformly over weights on the coherent finite window."""
    verify_congruent_seed_control(control)
    H = _integer(width, "width")
    return Q(5*H*(H*H-1), 768*control.start**4)
