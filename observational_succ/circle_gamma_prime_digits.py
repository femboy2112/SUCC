"""Exact finite bridge: polygon circle modes -> Gamma moments -> genuine primes
-> phase-preserving arithmetic transitions -> base-b digit hierarchy.

All computations here are exact Fraction/integer algebra. The analytic heat,
Mellin, Euler-product and smoothed-normality implications are established in
the companion paper dossier; finite tests never certify them for pi.
"""
from fractions import Fraction as Q
from math import factorial

from .pi_polygon_normality import polygon_pi_bracket


def _int(value, label, low=0, high=4096):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"{label} must be an exact integer in [{low},{high}]")
    return value


def _rational(value, label):
    if type(value) not in (int, Q):
        raise ValueError(f"{label} must be an exact integer or Fraction")
    return Q(value)


def _add(a, b):
    return tuple((a[i] if i < len(a) else Q()) +
                 (b[i] if i < len(b) else Q())
                 for i in range(max(len(a), len(b))))


def _sub(a, b):
    return _add(a, tuple(-x for x in b))


def _times_two_minus_x(a):
    return _sub(tuple(2*x for x in a), (Q(),) + tuple(a))


def mode_laplacian_polynomial(mode: int) -> tuple[Q, ...]:
    """Exact polynomial W_n(X)=sin²(nθ/2)/sin²(θ/2), X=4 sin²(θ/2).

    The regular-polygon symmetric nearest-neighbor Laplacian, normalized by
    squared chord length, has W_n(X_m) as eigenvalue for radius 1:
      W_0=0, W_1=1, W_(n+1)=2+(2-X)W_n-W_(n-1).
    It converges to n² for each fixed n as polygon size tends to infinity.
    """
    _int(mode, "mode", 0, 512)
    if mode == 0:
        return (Q(0),)
    old, cur = (Q(0),), (Q(1),)
    for _ in range(1, mode):
        old, cur = cur, _add((Q(2),), _sub(_times_two_minus_x(cur), old))
    return cur


def eval_polynomial(poly: tuple[Q, ...], x) -> Q:
    x = _rational(x, "polynomial argument")
    if not poly or any(type(c) not in (int, Q) for c in poly):
        raise ValueError("exact nonempty polynomial coefficients required")
    value = Q()
    for coefficient in reversed(poly):
        value = value*x + coefficient
    return value


def ordered_succ_gamma_weight(rate, steps: int) -> Q:
    """Unnormalized Poisson n-jump coefficient t^n/Gamma(n+1)=t^n/n!.

    The FULL probability is exp(-t) times this exact rational coefficient.
    Do not mistake these coefficients for a probability distribution.
    """
    rate = _rational(rate, "rate")
    _int(steps, "steps", 0, 512)
    if rate < 0:
        raise ValueError("rate must be nonnegative")
    return rate**steps / factorial(steps)


def pi_heat_mellin_mode_bounds(mode: int, gamma_index: int,
                               polygon_steps: int, precision_bits: int = 192):
    """Exact rational enclosure for the Gaussian mode's Mellin integral.

    For gamma_index=q>=1:
     I_q(n)=int_0^infty t^(q-1) exp(-pi*n²*t) dt
           = Gamma(q)/(pi^q*n^(2q)).
    π is bounded by source-derived polygon enclosures, never user-supplied.
    """
    _int(mode, "positive mode", 1, 1000)
    _int(gamma_index, "gamma index", 1, 32)
    br = polygon_pi_bracket(polygon_steps, precision_bits)
    numerator = Q(factorial(gamma_index-1), mode**(2*gamma_index))
    return numerator/br.upper**gamma_index, numerator/br.lower**gamma_index


def is_prime(n: int) -> bool:
    _int(n, "prime candidate", 2, 1000000)
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    factor = 3
    while factor*factor <= n:
        if n % factor == 0:
            return False
        factor += 2
    return True


def genuine_prime_smooth_coefficients(primes: tuple[int, ...], max_power: int,
                                      sigma: int) -> dict[int, Q]:
    """All finite prime boxes with each exponent <= max_power.

    Output is n -> n^(-sigma), one coefficient per genuine n. This finite
    Dirichlet polynomial is the expansion of product_p sum_(k=0)^K p^(-k*s).
    It is not the full Euler product until power and prime cutoffs grow.
    """
    _int(max_power, "max_power", 0, 10)
    _int(sigma, "sigma", 2, 32)
    if not primes or type(primes) is not tuple or any(type(p) is not int or
              p < 2 or p > 1000000 or not is_prime(p) for p in primes):
        raise ValueError("source must be genuine prime tuple")
    if len(set(primes)) != len(primes):
        raise ValueError("duplicate prime place forbidden")
    result = {1: Q(1)}
    for prime in primes:
        next_stage = {}
        for n, weight in result.items():
            for k in range(max_power+1):
                target = n * prime**k
                assert target not in next_stage
                next_stage[target] = weight * Q(1, prime**(sigma*k))
        result = next_stage
    return result


def phase_turn(n: int, phase) -> Q:
    """Normalized additive Fourier angle (n−1)x modulo one full turn."""
    _int(n, "mode", 1, 10000000)
    x = _rational(phase, "phase")
    return ((n-1)*x) % 1


def mixed_prime_turn(m: int, n: int, phase) -> Q:
    """Exact cross-prime phase cocycle: (m−1)(n−1)x mod 1."""
    _int(m, "first factor", 1, 10000000)
    _int(n, "second factor", 1, 10000000)
    x = _rational(phase, "phase")
    return ((m-1)*(n-1)*x) % 1


def factorized_phase_with_mixed_terms(factors: tuple[int, ...], phase):
    """Reconstruct e((n−1)x) from ALL prime-power factors and cross terms.

    Returns (target_n, direct_turn, sum_of_factor_turns, mixed_turns).
    The latter three must satisfy direct == factor_sum+mixed modulo 1.
    This is the phase debt of the additive Fourier character relative to
    the multiplicative decomposition of an integer mode.
    """
    if type(factors) is not tuple or not factors:
        raise ValueError("nonempty genuine prime-power factor list required")
    x = _rational(phase, "phase")
    factors = tuple(_int(f, "factor", 1, 10000000) for f in factors)
    product, factor_sum, mixed = 1, Q(0), Q(0)
    for factor in factors:
        factor_sum += phase_turn(factor, x)
        mixed += mixed_prime_turn(product, factor, x)
        product *= factor
    direct = phase_turn(product, x)
    assert (direct-factor_sum-mixed) % 1 == 0
    return product, direct, factor_sum % 1, mixed % 1


def rational_digits(phase, base: int, length: int) -> tuple[int, ...]:
    """Exact finite digit observation for rational phase controls only."""
    phase = _rational(phase, "phase") % 1
    _int(base, "base", 2, 36)
    _int(length, "length", 0, 100000)
    digits = []
    for _ in range(length):
        phase *= base
        digit = phase.numerator // phase.denominator
        digits.append(digit)
        phase -= digit
    return tuple(digits)


def cyclic_debruijn_edge_flow(digits: tuple[int, ...], base: int,
                              block_length: int):
    """Source-complete, boundary-preserving block/transition flow.

    Uses periodic closure of the *declared finite word*, not an assertion that
    the underlying irrational orbit is periodic. Returns exact edge counts,
    in-degree and out-degree, and balanced vertex flows.
    """
    _int(base, "base", 2, 36)
    _int(block_length, "block_length", 2, 10)
    if type(digits) is not tuple or not digits or any(type(d) is not int or
                         d < 0 or d >= base for d in digits):
        raise ValueError("declared finite digit word required")
    k, size = block_length, len(digits)
    edges, incoming, outgoing = {}, {}, {}
    for i in range(size):
        block = tuple(digits[(i+j) % size] for j in range(k))
        tail, head = block[:-1], block[1:]
        edges[block] = edges.get(block, 0) + 1
        outgoing[tail] = outgoing.get(tail, 0) + 1
        incoming[head] = incoming.get(head, 0) + 1
    assert set(incoming) == set(outgoing)
    assert all(incoming[s] == outgoing[s] for s in incoming)
    return edges, incoming, outgoing
