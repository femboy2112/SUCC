"""Odd-conductor inverse selection and the resolution obstruction.

Original BBP forcing/history are imported unchanged.  The all-N paper theorem
is that exact future-tail conditioning is deterministic on the odd torsion
carrier: it maximizes conditional branch energy, rather than annihilating it.
This module provides sparse exact certificates, not a normality estimate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import lcm

from .beck_chevalley_source import Square, finite_map
from .lambda_source_duality import (
    Cyclo16, branch_fourier, exact_int, fraction, verify_original_history,
)
from .succ_internal_matrix_walk import authentic_r, circle


def _positive_integer(value, name):
    return exact_int(value, name, 1)


@dataclass(frozen=True)
class OddInverse:
    tail: Q
    digit: int
    predecessor: Q


def exact_odd_inverse(tail) -> OddInverse:
    """Unique odd-denominator predecessor of t under x -> {16x}.

    For reduced t=a/q, q odd, j=(-a*q^{-1}) mod16.  Among all 16
    real preimages, this is the unique one whose denominator is odd.
    The condition is arithmetic; it does not identify the source time.
    """
    tail = fraction(tail)
    if not 0 <= tail < 1 or tail.denominator % 2 == 0:
        raise ValueError("canonical rational tail with odd denominator required")
    digit = (-tail.numerator * pow(tail.denominator, -1, 16)) % 16
    predecessor = (digit + tail) / 16
    if predecessor.denominator % 2 == 0 or circle(16*predecessor) != tail:
        raise ArithmeticError("odd-conductor inverse law failed")
    return OddInverse(tail, digit, predecessor)


def odd_carrier_affine_map(conductor, forcing):
    """Native FiniteMap for x -> 16x+r on D_Q, a permutation for odd Q.

    Enumerated only for bounded finite witnesses.  This is a common carrier
    for a finite prefix, not a replacement source or an invariant measure
    assertion about the selected orbit.
    """
    exact_int(conductor, "odd conductor", 1, 4095)
    forcing = fraction(forcing)
    if conductor % 2 == 0 or (conductor*forcing).denominator != 1:
        raise ValueError("odd conductor must contain the forcing denominator")
    values = tuple(Q(a, conductor) for a in range(conductor))
    result = finite_map(values, values, lambda x: circle(16*x+forcing))
    if len({y for _, y in result.pairs}) != conductor:
        raise ArithmeticError("odd affine source step is not a permutation")
    return result


def selected_fiber_square(tail):
    """Selected odd lift included in the full real inverse fiber.

    This commutative native source square is NOT cartesian: 15 full-fiber
    witnesses are absent.  Signed base change cannot be inferred from it.
    """
    selected = exact_odd_inverse(tail)
    all_predecessors = tuple((j+selected.tail)/16 for j in range(16))
    source = (selected.predecessor,)
    tails = (selected.tail,)
    return Square(
        all_predecessors, source, tails, tails,
        finite_map(all_predecessors, tails, lambda _: selected.tail),
        finite_map(tails, tails, lambda t: t),
        finite_map(source, all_predecessors, lambda x: x),
        finite_map(source, tails, lambda _: selected.tail),
        source_id="odd-conductor-selected-preimage-versus-real-ensemble",
    )


def carrier_resolution_lower(conductor, bins) -> Q:
    """All-measure lower bound Delta >= 16/min(16,ceil(Q/M))-1.

    A tail bin contains at most ceil(Q/M) points of D_Q and therefore
    at most that many selected digits.  This is a lower, not upper, bound.
    """
    _positive_integer(conductor, "conductor")
    _positive_integer(bins, "bins")
    if conductor % 2 == 0:
        raise ValueError("odd conductor required")
    support = min(16, (conductor+bins-1)//bins)
    return Q(16, support)-1


@dataclass(frozen=True)
class ResolutionCertificate:
    observations: int
    bins: int
    conductor: int
    # Only occupied rows: no allocation proportional to the enormous Q_N.
    counts: tuple[tuple[int, tuple[int, ...]], ...]
    chi_squared: Q
    carrier_lower_bound: Q
    exact_tail_partition: bool

    def conditional_mode_energy(self, frequency):
        exact_int(frequency, "frequency")
        result = Cyclo16.zero()
        for _, row in self.counts:
            mass = sum(row)
            value = branch_fourier(tuple(Q(n, mass) for n in row), frequency)
            result += value*value.conjugate()*Q(mass, self.observations)
        return result


def authentic_resolution_certificate(states, bins=None) -> ResolutionCertificate:
    """Authenticate original U_0=0 history and certify its sparse tail table.

    Default M=Q_N.  At any M>=Q_N the certificate has Delta=15 and
    conditional mode energy one at EVERY integer frequency. Repeated
    tail values are allowed; they necessarily have the same selected digit.
    """
    if not verify_original_history(states):
        raise ValueError("original zero-initialized four-pole history required")
    conductor = 1
    for n in range(1, len(states)+1):
        conductor = lcm(conductor, authentic_r(n).denominator)
    if conductor % 2 == 0:
        raise ArithmeticError("authentic four-pole cancellation lost odd conductor")
    if bins is None:
        bins = conductor
    _positive_integer(bins, "bins")
    rows = {}
    tails_by_bin = {}
    for state in states:
        x = circle(state)
        tail = circle(16*x)
        inverse = exact_odd_inverse(tail)
        if inverse.predecessor != x or (conductor*tail).denominator != 1:
            raise ArithmeticError("source history escaped the common odd carrier")
        b = (bins*tail).__floor__()
        rows.setdefault(b, [0]*16)[inverse.digit] += 1
        tails_by_bin.setdefault(b, set()).add(tail)
    N = len(states)
    delta = sum((Q(16, N*sum(row))*sum(v*v for v in row)
                 for row in rows.values()), Q())-1
    lower = carrier_resolution_lower(conductor, bins)
    isolated = all(len(tails) == 1 for tails in tails_by_bin.values())
    if delta < lower or (bins >= conductor and (not isolated or delta != 15)):
        raise ArithmeticError("finite resolution obstruction failed")
    return ResolutionCertificate(N, bins, conductor,
                                 tuple((b, tuple(row)) for b, row in sorted(rows.items())),
                                 delta, lower, isolated)


def odd_tail_near(target, digit, tolerance):
    """Exact discontinuity witness with any chosen branch arbitrarily nearby.

    Returns odd t' with |t'-target|<tolerance and selected digit equal
    to digit. The center may be any rational in [0,1).
    """
    target, tolerance = fraction(target), fraction(tolerance)
    exact_int(digit, "selected digit", 0, 15)
    if not 0 <= target < 1 or tolerance <= 0:
        raise ValueError("canonical center and positive rational tolerance required")
    inverse_tol, inverse_boundary = 1/tolerance, 1/(1-target)
    L = max(1, inverse_tol.__ceil__(), inverse_boundary.__ceil__())
    q = 16*L+1
    k = (q*target).__floor__()
    a = k+((-digit-k) % 16)  # q=1 mod16; select the numerator residue.
    witness = exact_odd_inverse(Q(a, q))
    if not abs(witness.tail-target) < tolerance or witness.digit != digit:
        raise ArithmeticError("exact nearby-branch witness failed")
    return witness


def status_flags():
    return {"odd_conductor_inverse_deterministic": True,
            "fine_resolution_conditional_energy_maximal": True,
            "selected_weyl_saving_proved": False,
            "pi_base16_normality_proved": False}
