"""Authentic first-prime resonance versus Galois-averaged matrix purity.

The growing-window obstruction concerns the genuine p-PRIMARY COMPONENT
of the original zero-seeded BBP source. It is not a theorem that the full
BBP phases reinforce: their complete p-free complement is retained below.
All executable budgets are exact rationals; analytic claims are paper-proved.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .bbp_twisted_pair import authentic_window_prime
from .integer_bbp_carrier import source_states
from .succ_internal_matrix_walk import authentic_r


def _prime(p):
    if type(p) is not int or not 257 <= p <= 2**40:
        raise ValueError("prime certificate budget requires 257 <= p <= 2**40")
    return authentic_window_prime(p)


def _frequency(h):
    if type(h) is not int or h == 0:
        raise ValueError("nonzero ordinary integer frequency required")
    return h


def _window_length(p):
    length, power = 0, 1
    while 256*power <= p:
        length, power = length+1, 256*power
    return length


@dataclass(frozen=True)
class PrimeResonanceBudget:
    prime: int
    birth_index: int
    window_length: int
    next_pole_gap: int
    width: int
    frequency: int
    primary_phases: tuple[Q, ...]
    selected_sum_deficit_upper: Q
    selected_sum_modulus_lower: Q
    galois_mean_sum_squared: Q
    selected_amplification_lower: Q
    galois_mean_normalized_excess: Q
    selected_normalized_excess_lower: Q
    selected_matrix_deficit_upper: Q
    full_complement_sum_error_upper: Q
    full_complement_root_error_squared_upper: Q
    full_source_cancellation_proved: bool = False


def prime_resonance_budget(p: int, h: int = 1,
                           width: int | None = None) -> PrimeResonanceBudget:
    """Exact all-h bounds on the prescribed K=floor(log_256 p) birth window.

    For the nonresonant primitive average require p not dividing h. The
    matrix width is 1<=H<=p, so none of its nonzero modes is p-resonant.
    The h argument controls only the scalar sum; the matrix always uses
    the unscaled basis with frequencies 0,1,...,H-1.
    Default H=1+isqrt(K) is chosen without observing any source spectrum.
    The code's finite primality budget does not restrict the paper theorem.
    """
    _prime(p)
    _frequency(h)
    if h % p == 0:
        raise ValueError("primitive Galois mean requires p not dividing h")
    K = _window_length(p)
    H = 1+isqrt(K) if width is None else width
    if type(H) is not int or not 1 <= H <= p:
        raise ValueError("ordinary matrix width in [1,p] required")
    phases = tuple(Q(4*16**t, p) for t in range(K))
    # 1-cos(2*pi*x)<=2*pi²*x² and pi<22/7, with the geometric sum exact.
    deficit = Q(15488*h*h*(256**K-1), 12495*p*p)
    lower = max(Q(), Q(K)-deficit)
    mean = Q(K*(p-K), p-1)
    matrix_error = Q(2*H*(H*H-1), 3*p*K)
    base_transport = Q(28*(16**K-1), 15*p*K)
    return PrimeResonanceBudget(
        p, (p+7)//8, K, 3*(p-1)//8, H, h, phases, deficit, lower,
        mean, lower*lower/mean, Q((H-1)*(p-K), K*(p-1)),
        max(Q(), Q(H-1)-matrix_error), matrix_error,
        Q(28*abs(h)*(16**K-1), 15*p),
        base_transport**2 * Q(H*(H*H-1), 6),
    )


@dataclass(frozen=True)
class PrimeSourcePoint:
    source_index: int
    original_lift: Q
    original_forcing: Q
    common_conductor: int
    primary_phase: Q
    full_complement: Q


@dataclass(frozen=True)
class PrimeSourcePassport:
    source_id: str
    initial_state: Q
    prime: int
    birth_index: int
    points: tuple[PrimeSourcePoint, ...]


def authentic_prime_source_passport(p: int) -> PrimeSourcePassport:
    """Replay the original UNWRAPPED source, retaining the complete complement.

    The source engine is the existing integer carrier. Every transition
    from its zero anchor is checked against the literal four-pole adapter.
    No changed seed, projected recurrence, or independent prime law enters.
    """
    _prime(p)
    birth, K = (p+7)//8, _window_length(p)
    last = birth+K-1
    if last > 2000:
        raise ValueError("full source passport exceeds the 2000-step replay budget")
    states = source_states(last)
    previous, result = Q(), []
    for n, state in enumerate(states[1:], 1):
        lifted = Q(state.numerator, state.conductor)
        forcing = authentic_r(n)
        if lifted != 16*previous+forcing:
            raise ArithmeticError("integer source and literal forcing disagree")
        if n >= birth:
            primary = Q(4*16**(n-birth), p)
            complement = lifted-primary
            if complement.denominator % p == 0:
                raise ArithmeticError("complement retained a forbidden p denominator")
            result.append(PrimeSourcePoint(n, lifted, forcing, state.conductor,
                                          primary, complement))
        previous = lifted
    return PrimeSourcePassport("Q:Coherent-Main-X-four-pole-BBP", Q(), p,
                               birth, tuple(result))


def verify_prime_source_passport(passport) -> bool:
    """Exact full replay: a source label alone is not authentication."""
    if type(passport) is not PrimeSourcePassport:
        return False
    try:
        return passport == authentic_prime_source_passport(passport.prime)
    except (ValueError, ArithmeticError):
        return False
