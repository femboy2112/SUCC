"""Exact quantitative reorientation from a full-rank source-defined observation frame.

The same CM theta coefficient matrix enters local (integer) and real Gaussian
frames; this computes the *cost of inverting* its actual weighted realization.
It is not the automorphic Petersson period map or an RH inequality.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction

from .principia_cm_theta import CMThetaCertificate, verify_cm_theta_certificate
from .principia_reorientation import ReorientationError


@dataclass(frozen=True)
class BalanceFrame:
    source: CMThetaCertificate
    analytic: bool
    observation: tuple[tuple[Fraction,...],...]
    inverse: tuple[tuple[Fraction,...],...]
    inverse_infinity_norm: Fraction


def exact_inverse(rows) -> tuple[tuple[Fraction,...],...]:
    a=[list(map(Fraction,row)) for row in rows]
    n=len(a)
    if not n or any(len(row)!=n for row in a):
        raise ReorientationError('reorientation requires square full-rank frame')
    augmented=[row+[Fraction(i==j) for j in range(n)] for i,row in enumerate(a)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if augmented[i][col]),None)
        if pivot is None:
            raise ReorientationError('frame has a hidden indistinguishable direction')
        augmented[col],augmented[pivot]=augmented[pivot],augmented[col]
        scale=augmented[col][col]
        augmented[col]=[x/scale for x in augmented[col]]
        for i in range(n):
            if i!=col and augmented[i][col]:
                scalar=augmented[i][col]
                augmented[i]=[x-scalar*y for x,y in zip(augmented[i],augmented[col])]
    return tuple(tuple(row[n:]) for row in augmented)


def infinity_norm(rows) -> Fraction:
    return max(sum((abs(x) for x in row),Fraction(0)) for row in rows)


def cm_balance_frame(c: CMThetaCertificate, *, analytic: bool) -> BalanceFrame:
    report=verify_cm_theta_certificate(c)
    if report['determinant']==0:
        raise ReorientationError('zero CM theta minor has no inverse')
    rows=tuple(tuple(Fraction(value)*(c.q**c.gaussian_norms[j] if analytic else 1)
                     for j,value in enumerate(row)) for row in c.matrix)
    inv=exact_inverse(rows)
    out=BalanceFrame(c,analytic,rows,inv,infinity_norm(inv))
    verify_balance_frame(out)
    return out


def verify_balance_frame(frame: BalanceFrame) -> BalanceFrame:
    # Reconstruct the matrix from the SAME genuine Z[i] source, not merely from
    # a plausible source label or an algebraically invertible guessed matrix.
    if type(frame.analytic) is not bool:
        raise ReorientationError('missing analytic/integral frame tag')
    try:
        verify_cm_theta_certificate(frame.source)
    except Exception as exc:
        raise ReorientationError('unverified actual Gaussian source') from exc
    c=frame.source
    expected=tuple(tuple(Fraction(a)*(c.q**c.gaussian_norms[j] if frame.analytic else 1)
                         for j,a in enumerate(row)) for row in c.matrix)
    if frame.observation!=expected:
        raise ReorientationError('altered observed CM theta period/heat normalization')
    n=len(frame.observation)
    if not n or len(frame.inverse)!=n or any(len(row)!=n for row in frame.inverse+frame.observation):
        raise ReorientationError('dimension mismatch in claimed reorientation')
    if any(type(x) is not Fraction for row in frame.inverse+frame.observation for x in row):
        raise ReorientationError('source frame must use exact rational coordinates')
    for i in range(n):
        for j in range(n):
            result=sum((frame.observation[i][k]*frame.inverse[k][j] for k in range(n)),Fraction(0))
            if result!=Fraction(i==j):
                raise ReorientationError('forged inverse/source transport')
    if infinity_norm(frame.inverse)!=frame.inverse_infinity_norm:
        raise ReorientationError('unpaid analytic inverse-norm factor')
    return frame


def source_error_bound(frame: BalanceFrame, observation_error: Fraction) -> Fraction:
    verify_balance_frame(frame)
    eps=Fraction(observation_error)
    if eps<0:
        raise ReorientationError('error radius cannot be negative')
    return frame.inverse_infinity_norm*eps
