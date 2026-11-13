"""Exact finite BBP lag/pinbed interface and truth-preserving gauge controls.

The mathematical normality equivalence is a PAPER theorem combining the
Fourier–Yoneda pinbed with the invariant finite-cover lemma in PR #611.
Finite rational output never certifies asymptotic decay or pi normality.
The analytic BBP identity and T_n < 1/(64 n^2) for n>=1 are explicit imports.
No nonflat physical curvature, gravity or new π cancellation is asserted.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from . import duck_bbp


class GaugeProbeError(ValueError):
    """An input is inexact or an attempted gauge/probe is ill-typed."""


def _nat(value: int, name: str, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise GaugeProbeError(f"{name} must be an exact integer >= {minimum}")
    return value


def bernoulli4(t: Q) -> Q:
    """Periodic fourth Bernoulli polynomial, with exact rational remainder."""
    if type(t) not in (int, Q):
        raise GaugeProbeError("exact rational angle required")
    x = Q(t) % 1
    return x**4 - 2*x**3 + x*x - Q(1, 30)


def pinbed_energy(phases: tuple[Q, ...]) -> Q:
    """Exact characteristic B2 surface L2 energy, via independent B4 pairs.

    E = -(1/(6N^2)) sum_(i,j) B4({x_i-x_j}). A finite empirical
    measure always has strictly positive E; E=0 is Haar at law level.
    O(N^2) rational operations; use existing fast pinbed for large N.
    """
    if type(phases) is not tuple or not phases or any(type(p) is not Q for p in phases):
        raise GaugeProbeError("nonempty tuple of exact rational circle phases")
    n = len(phases)
    energy = -sum((bernoulli4(x-y) for x in phases for y in phases), Q()) / (6*n*n)
    if energy <= 0:
        raise ArithmeticError("empirical rational law cannot have zero/negative B2 energy")
    return energy


def selected_unwrapped_states(last: int) -> tuple[Q, ...]:
    """Only zero-seeded original four-pole forcing is admissible."""
    last = _nat(last, "last", 0)
    s = Q()
    states = [s]
    for n in range(1, last + 1):
        s = 16*s + duck_bbp.forcing(n)
        states.append(s)
    return tuple(states)


def original_lag_phases(epoch: int, lag: int) -> tuple[Q, ...]:
    """Full shell [B,2B): Y_(n+lag)-Y_n, represented by rational U."""
    B = _nat(epoch, "epoch")
    ell = _nat(lag, "lag")
    values = selected_unwrapped_states(2*B - 1 + ell)
    return tuple((values[n+ell] - values[n]) % 1 for n in range(B, 2*B))


def source_lag_gauge_control(epoch: int, lag: int, torsion: int) -> bool:
    """Exact equality under s=j/15, a normality-preserving gauge on T_16.

    Nonzero s is NOT the authenticated U0=0 source. This function checks a
    symmetry of the *normality observable*, not a source-identity permission.
    """
    B = _nat(epoch, "epoch")
    ell = _nat(lag, "lag")
    if type(torsion) is not int:
        raise GaugeProbeError("torsion index must be an exact integer")
    s = Q(torsion, 15)
    states = selected_unwrapped_states(2*B - 1 + ell)
    return all(
        (states[n+ell] + 16**(n+ell)*s - states[n] - 16**n*s) % 1
        == (states[n+ell] - states[n]) % 1
        for n in range(B, 2*B)
    )


@dataclass(frozen=True)
class LagPinbedReceipt:
    source: str
    epoch: int
    lag: int
    energy: Q
    surface_norm_transfer_upper_square: Q
    gauge_15torsion_invariant: bool
    normality_decided: bool = False


def lag_pinbed_receipt(epoch: int, lag: int) -> LagPinbedReceipt:
    """Certified *finite* rational data + proved all-lag analytic error budget.

    Completed orbit Y_n=U_n+T_n=16^(n-1) pi. The imported positive,
    decreasing tail with T_n<1/(64 n^2) implies, uniformly in lag ell>=1,
       |sqrt(E(lag-Y))-sqrt(E(lag-U))| < 1/(64 sqrt(3) B^2).
    The returned rational value is its squared upper budget, 1/(12288 B^4).
    This does NOT bound E itself and does not prove normality.
    """
    B = _nat(epoch, "epoch")
    ell = _nat(lag, "lag")
    return LagPinbedReceipt(
        source="bbp-original-four-pole-U0-zero",
        epoch=B,
        lag=ell,
        energy=pinbed_energy(original_lag_phases(B, ell)),
        surface_norm_transfer_upper_square=Q(1, 3*64*64*B**4),
        gauge_15torsion_invariant=source_lag_gauge_control(B, ell, 1),
    )


def phase_rotation_energy(phases: tuple[Q, ...], angle: Q) -> Q:
    """A *common* chart rotation is a legal observer-coordinate gauge."""
    if type(angle) not in (int, Q):
        raise GaugeProbeError("common gauge must be exact rational")
    return pinbed_energy(tuple((x + Q(angle)) % 1 for x in phases))