"""Exact finite-horizon π base-16 Weyl phase transfer from Krylov brackets.

Certifies how an authentic rational pi bracket controls phase discrepancy
between real pi orbit and the rational reference. It does NOT prove either
orbit's cancellation, normality, or a polynomial bit-complexity algorithm.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from .vacuum_parameter_bbp import VacuumBridgeError, krylov_certificate


@dataclass(frozen=True)
class PhaseHorizonCertificate:
    frequency: int
    horizon: int
    krylov_dimension: int
    rational_reference: Q
    pi_distance_cap: Q
    normalized_weyl_gap_cap: Q
    absolute_weyl_gap_cap: Q
    bound_is_source_selected: bool
    cancellation_proved: bool


def certified_weyl_phase_transport(frequency: int, horizon: int,
                                   krylov_dimension: int) -> PhaseHorizonCertificate:
    """For h!=0 and N>=1, |S_N(h,pi)-S_N(h,a_d)| <=

        8 |h| [(16^N-1)/15] * rho_d,

    where a_d=(lower+upper)/2 and rho_d=(upper-lower)/2 are exact
    rational values from the authenticated BBP positive resolvent.
    Uses |exp(2πix)-exp(2πiy)|<=2π|x-y|<=8|x-y| (π<4).
    No signed Fourier cancellation is claimed.
    """
    if type(frequency) is not int or frequency==0 or abs(frequency)>100_000:
        raise VacuumBridgeError("fixed nonzero integer Weyl frequency required")
    if type(horizon) is not int or not 1<=horizon<=1000:
        raise VacuumBridgeError("bounded positive finite orbit horizon required")
    c=krylov_certificate(krylov_dimension)
    midpoint=(c.lower+c.upper)/2
    radius=(c.upper-c.lower)/2
    unnormalized=Q(8*abs(frequency)*(16**horizon-1),15)*radius
    normalized=unnormalized/horizon
    return PhaseHorizonCertificate(
        frequency,horizon,krylov_dimension,midpoint,radius,
        normalized,unnormalized,True,False,
    )
