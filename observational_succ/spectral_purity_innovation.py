"""Exact Fejer telescoping and source-authentic spectral Green budgets.

Formal phase equalities live in Q[Q/Z], not in its cyclotomic evaluation.
The finite exceptional-step bound is CONDITIONAL on its displayed inequalities.
The Green budget is an all-N paper theorem specialized to the original BBP
source. Neither instrument proves the missing temporal cancellation estimate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .succ_internal_matrix_walk import PhasePoly, authentic_r


SOURCE_ID = "Q:Coherent-Main-X-four-pole-BBP"


def _natural(value: int, name: str, minimum: int = 1,
             maximum: int = 100000) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be a bounded exact integer")
    return value


def _rational(value, name: str) -> Q:
    if type(value) not in (int, Q):
        raise ValueError(f"{name} must be exact rational")
    return Q(value)


def fejer_polynomial(turns: Q, width: int) -> PhasePoly:
    """Unnormalized |sum_(k<H) e(k*turns)|^2, as a formal polynomial."""
    _natural(width, "width", maximum=64)
    x = _rational(turns, "turns")
    return sum((PhasePoly.monomial(j*x, width-abs(j))
                for j in range(1-width, width)), PhasePoly.zero())


@dataclass(frozen=True)
class SequentialCertificate:
    source_id: str
    history: tuple[Q, ...]
    width: int
    innovations: tuple[PhasePoly, ...]
    weighted_signed_innovation: PhasePoly
    normalized_spectral_excess: PhasePoly
    boundary: Q
    normality_proved: bool = False


def sequential_certificate(history: tuple, width: int, *,
                           authenticate: bool = False) -> SequentialCertificate:
    """Check the pair sum / signed sequential identity exactly.

    The optional source gate checks every UNWRAPPED state, starting at U0=0.
    It rejects chart rotations, integer lift mutations and changed forcing.
    Generic controls remain explicitly unauthenticated. No order is assigned
    to a formal phase polynomial; inequalities concern complex evaluation.
    """
    _natural(width, "width", maximum=64)
    if not isinstance(history, tuple) or not 1 <= len(history) <= 128:
        raise ValueError("nonempty bounded history tuple required")
    data = tuple(_rational(x, "state") for x in history)
    if type(authenticate) is not bool:
        raise ValueError("authenticate must be boolean")
    if authenticate:
        previous = Q(0)
        for n, state in enumerate(data, 1):
            if state != 16*previous+authentic_r(n):
                raise ValueError("original BBP source or unwrapped lift mismatch")
            previous = state
    N = len(data)
    innovations = tuple(
        sum((fejer_polynomial(data[m]-data[j], width)
             for j in range(m)), PhasePoly.zero())/m
        for m in range(1, N)
    )
    signed = sum((m*(q-width) for m, q in enumerate(innovations, 1)),
                 PhasePoly.zero())
    # Independent Fourier expansion, rather than reusing the pair loop.
    energy = PhasePoly.zero()
    for j in range(1, width):
        average = sum((PhasePoly.monomial(j*u) for u in data),
                      PhasePoly.zero())/N
        energy += Q(2*(width-j), width)*average*average.star()
    boundary = Q(width-1, N)
    sequential = boundary+Q(2, N*N*width)*signed
    if energy != sequential:
        raise ArithmeticError("signed Fejer telescoping identity failed")
    return SequentialCertificate(
        SOURCE_ID if authenticate else "generic-rational-control",
        data, width, innovations, signed, energy, boundary,
    )


def authentic_sequential_certificate(horizon: int, width: int) -> SequentialCertificate:
    _natural(horizon, "horizon", maximum=128)
    history = []
    state = Q(0)
    for n in range(1, horizon+1):
        state = 16*state+authentic_r(n)
        history.append(state)
    return sequential_certificate(tuple(history), width, authenticate=True)


@dataclass(frozen=True)
class ExceptionalBudget:
    horizon: int
    width: int
    eta: Q
    exceptional_steps: tuple[int, ...]
    weighted_exceptional_mass: int
    normalized_excess_upper: Q
    good_step_premise_verified: bool = False
    normality_proved: bool = False


def exceptional_budget(horizon: int, width: int, eta,
                       exceptional_steps: tuple[int, ...]) -> ExceptionalBudget:
    """Budget assuming q_m <= H(1+eta) off the supplied exceptional set.

    This function NEVER infers that premise or authenticates a classifier.
    Negative defects are retained in the theorem; no absolute-value premise
    is introduced. The sharper factor (N-1)/N is retained for eta.
    """
    N = _natural(horizon, "horizon")
    H = _natural(width, "width")
    eta = _rational(eta, "eta")
    if eta < 0:
        raise ValueError("nonnegative eta required")
    if not isinstance(exceptional_steps, tuple) or any(
            type(m) is not int or not 1 <= m < N for m in exceptional_steps):
        raise ValueError("exceptional steps must lie in 1..N-1")
    if tuple(sorted(set(exceptional_steps))) != exceptional_steps:
        raise ValueError("exceptional steps must be sorted and unique")
    mass = sum(exceptional_steps)
    upper = Q(H-1, N)+eta*Q(N-1, N)+Q(2*H*mass, N*N)
    return ExceptionalBudget(N, H, eta, exceptional_steps, mass, upper)


@dataclass(frozen=True)
class SpectralGreenBudget:
    source_id: str
    horizon: int
    width: int
    squared_root_energy_error_upper: Q
    square_root_scaling_upper: Q
    summable_lipschitz_upper: Q
    normality_proved: bool = False


def mode_green_error_squared(frequency: int, horizon: int) -> Q:
    """Squared bound for |a_U(h)-a_pi(h)|, using authentic tail decay.

    sum_n min(2,7|h|/(64n^2)) <= sqrt(7|h|/8). The original total
    tail budget additionally gives 119|h|/648. Take the better bound.
    """
    if type(frequency) is not int or frequency == 0 or abs(frequency) > 100000:
        raise ValueError("bounded nonzero integer frequency required")
    N = _natural(horizon, "horizon", maximum=10**12)
    h = abs(frequency)
    return min(Q(7*h, 8), Q(119*h, 648)**2)/(N*N)


def spectral_green_budget(horizon: int, width: int) -> SpectralGreenBudget:
    """Exact squared bound on |sqrt(D_U/H)-sqrt(D_pi/H)|.

    Paper theorem: it is <= sqrt(7(H^2-1)/24)/N. Thus every prescribed
    sublinear width H=o(N) permits spectral-purity transfer in both directions.
    No assertion that either source's spectral energy is small is made.
    """
    N = _natural(horizon, "horizon", maximum=10**12)
    H = _natural(width, "width")
    sharpened = sum((Q(2*(H-j), H)*mode_green_error_squared(j, N)
                     for j in range(1, H)), Q(0))
    root_scaling = Q(7*(H*H-1), 24*N*N)
    lipschitz = Q(119, 648)**2*Q(H*(H*H-1), 6*N*N)
    if sharpened > min(root_scaling, lipschitz):
        raise ArithmeticError("weighted source transport budget failed")
    return SpectralGreenBudget(SOURCE_ID, N, H, sharpened,
                              root_scaling, lipschitz)
