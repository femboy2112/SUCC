"""Source-preserving finite Gamma-rung repair; exact Fraction certificates.

A packet contains genuine CONSECUTIVE nonnegative Gamma rungs. Its energy
compensates the negative signed source, not negative energy in another Gamma
rung. No nontrivial zero data and no claim about S4 or RH.
"""
from fractions import Fraction as F

from .gamma_fredholm_completion import (
    authentic_fifth_mode_completion,
    gamma_tail_H01_lower,
    gamma_tail_source_upper,
)


class PacketError(ValueError):
    pass


def rational(x):
    if type(x) not in (F, int, str):
        raise PacketError("exact rational required: no float/bool")
    try:
        return F(x)
    except (ValueError, ZeroDivisionError) as exc:
        raise PacketError("invalid exact rational") from exc


def finite_packet_lower(start, stop, norm_sq, deriv_sq):
    """T_start-T_stop >= L_start-U_stop for authentic Gamma tails."""
    if type(start) is not int or type(stop) is not int or start < 1 or stop <= start:
        raise PacketError("strictly ordered positive integer rung cutoffs")
    norm_sq, deriv_sq = rational(norm_sq), rational(deriv_sq)
    if norm_sq <= 0 or deriv_sq < 0:
        raise PacketError("H1 endpoint-zero energy required")
    return (gamma_tail_H01_lower(start, norm_sq, deriv_sq) -
            gamma_tail_source_upper(stop, norm_sq))


def finite_repair_bound(start, qlo, qhi, norm_sq, deriv_sq, max_stop=1000000):
    """Finite, bounded search of first stop certified by THESE bounds only.

    q_start in [qlo,qhi], qhi<0; strict qlo+L_start>0.
    The source has one genuine u, all rungs PSD, and U_stop -> 0.
    A returned stop proves q_stop>0 for that original SAME direction,
    not all-modes/all-radii positivity or the actual first sign crossing.
    """
    if type(start) is not int or start < 1 or type(max_stop) is not int or max_stop <= start:
        raise PacketError("valid finite rung and observer budget required")
    qlo, qhi, n, d = map(rational, (qlo, qhi, norm_sq, deriv_sq))
    if qlo > qhi or qhi >= 0 or n <= 0 or d < 0:
        raise PacketError("strict negative signed interval and H1 energies required")
    low_tail = gamma_tail_H01_lower(start, n, d)
    if qlo + low_tail <= 0:
        raise PacketError("full-Gamma positive sign not certified: no packet claim")

    def pass_bound(j):
        return qlo + low_tail - gamma_tail_source_upper(j, n) > 0

    last_bad = start
    good = min(max_stop, 2*start)
    while not pass_bound(good):
        if good == max_stop:
            raise PacketError("finite certificate budget exhausted; not a negative source witness")
        last_bad = good
        good = min(max_stop, 2*good)
    while good-last_bad > 1:
        mid = (last_bad+good)//2
        if pass_bound(mid):
            good = mid
        else:
            last_bad = mid
    stop = good
    packet_lo = finite_packet_lower(start, stop, n, d)
    signed_lo = qlo+packet_lo
    if not (qhi < 0 < signed_lo):
        raise ArithmeticError("source packet sign conclusion inconsistent")
    return {
        "source_type": "ABSTRACT_RATIONAL_CERTIFICATE_REQUIRES_AUTHENTIC_PREFIX",
        "start": start,
        "stop_exclusive": stop,
        "rung_count": stop-start,
        "signed_prefix_interval": (str(qlo),str(qhi)),
        "full_gamma_tail_lower": str(low_tail),
        "future_tail_upper": str(gamma_tail_source_upper(stop,n)),
        "consecutive_original_gamma_packet_lower": str(packet_lo),
        "signed_energy_after_packet_lower": str(signed_lo),
        "minimum_stop_under_THIS_bound": True,
        "actual_first_sign_crossing_found": False,
        "S4_positive_proved": False,
        "RH_proved": False,
    }


def original_fifth_mode_packet(max_stop=1000000):
    """Authenticated original signed source from PR #164, exact same u."""
    w=authentic_fifth_mode_completion(64)
    if (w["source_git_blob"] != "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
            or w["genuine_prime_wavefront"] != ((2,2),)
            or not w["truncated_negative_strict"]
            or not w["fully_completed_same_vector_positive_strict"]):
        raise PacketError("original Suzuki signed source gate failed")
    a,b=w["J64_full_signed_source_energy"]
    c=finite_repair_bound(64,a,b,w["witness_norm_squared"],
                          w["witness_derivative_norm_squared"],max_stop)
    c.update({
        "source_type":"AUTHENTIC_COMPLETED_SUZUKI_GAMMA",
        "source_git_blob":w["source_git_blob"],
        "prime_wavefront":w["genuine_prime_wavefront"],
        "modes":w["witness_modes"],
        "endpoint_zero_H1_condition_inherited":True,
    })
    return c


def paired_mode_negative_control():
    """Exact signed surrogate: positive diagonals do not imply positive form."""
    # A = [[1,2],[2,1]], Q(e1)=Q(e2)=1 but Q(e1-e2)=-2.
    return {"source_type":"SYNTHETIC_NOT_WEIL",
            "basis_diagonal":("1","1"),
            "coupled_energy":str(F(1)+F(1)-2*F(2)),
            "determinant":str(F(1)-F(4)),
            "authentic_negative_witness":False,"RH_proved":False}
