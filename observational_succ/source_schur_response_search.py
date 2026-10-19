"""Find rational parity-preserving finite high response U from genuine source blocks.

This is an optimization CANDIDATE generator, never a positivity theorem.
Every proposed U must be independently re-certified on original infinite
Suzuki source using CertifiedAnalyticSuzukiTrial. A positive surrogate
Galerkin matrix is not an original Weil sign certificate.
"""
from __future__ import annotations
from fractions import Fraction as F

from .direct_quotient_schur import _inverse,_mul,exact_pd
from .certified_four_schur_trial import (
    _g_block,CertifiedTrial,CertifiedTrialError,
)


class SourceResponseSearchError(ValueError):
    pass


def original_source_rational_response(rank=6,J=64,denominator=10000):
    if type(rank) is not int or not 5<=rank<=8:
        raise SourceResponseSearchError("rank 5..8 required")
    if type(J) is not int or not 32<=J<=75:
        raise SourceResponseSearchError("original Gamma J 32..75 required")
    if type(denominator) is not int or not 10<=denominator<=10**6:
        raise SourceResponseSearchError("rationalization denominator 10..10^6")
    parent=CertifiedTrial((),J=J,rank=rank)
    if parent["verdict"]=="INVALID_SOURCE":
        raise SourceResponseSearchError("original source proof receipt invalid")
    G=_g_block(rank,J)
    m=rank-4
    midpoint=tuple(tuple((G[i][j].lo+G[i][j].hi)/2
                         for j in range(rank)) for i in range(rank))
    D=tuple(tuple(midpoint[4+i][4+j] for j in range(m))
            for i in range(m))
    B=tuple(tuple(midpoint[4+i][j] for j in range(4))
            for i in range(m))
    # The finite D may be uncertified PD despite the *true* source high
    # coercivity, because a positive Gamma tail was truncated. Use a stated,
    # symbolic rational SPD regularizer only as a candidate-search method.
    ridge=None
    for value in (F(0),F(1,10**6),F(1,10**4),F(1,100),F(1,10),F(1),F(10)):
        test=tuple(tuple(D[i][j]+(value if i==j else F(0))
                         for j in range(m)) for i in range(m))
        if exact_pd(test):
            ridge=value
            inv=_inverse(test)
            U0=_mul(inv,B)
            break
    if ridge is None:
        raise SourceResponseSearchError("no positive finite Galerkin candidate")
    U=[]
    for h in range(m):
        row=[]
        for low in range(4):
            if (h+4-low)%2:
                row.append(F(0));continue
            val=U0[h][low]
            scaled=val*denominator
            # Exact nearest-rational approximation: no floating sample.
            n=(2*scaled.numerator+scaled.denominator) //(2*scaled.denominator)
            row.append(F(n,denominator))
        U.append(tuple(row))
    U=tuple(U)
    if all(x==0 for row in U for x in row):
        raise SourceResponseSearchError("rounded response collapsed to zero")
    return {
        "U":U,"rank":rank,"J":J,
        "ridge":ridge,
        "rational_denominator":denominator,
        "original_source_verified":True,
        "surrogate_finite_D_positive":True,
        "U_has_original_S4_sign_certificate":False,
        "RH_proved":False,
    }


def source_response_analytic_trial(rank=6,J_source=64,J_deriv=4,denominator=10000):
    from .analytic_suzuki_schur_gate import CertifiedAnalyticSuzukiTrial
    candidate=original_source_rational_response(rank=rank,J=J_source,
                                                denominator=denominator)
    audited=CertifiedAnalyticSuzukiTrial(
        candidate["U"],rank=rank,J_galerkin=J_source,
        J_deriv=J_deriv,digits=100
    )
    return {
        "candidate":candidate,
        "genuine_S4_source_audited":audited.get("source_passport_verified",False),
        "genuine_first_window_verdict":audited["verdict"],
        "certificate":audited,
        "RH_proved":False,
    }
