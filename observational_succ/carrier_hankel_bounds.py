"""Exact finite Hankel minors give model-relative carrier dimension lower bounds.

CLASSICAL Ho--Kalman realization/linear algebra. One finite nonzero r-minor
forces d>=r in EVERY compatible autonomous rational LTI realization
 y_n = c^T A^n b. It NEVER proves a source to be physically linear,
identifies an ontologically 'external' origin, or predicts an unbounded
future from a finite prefix without an independent recurrence contract.
"""
from __future__ import annotations

from fractions import Fraction as F
from typing import Sequence


class RealizationError(ValueError):
    """Invalid exact source, missing Hankel evidence or failed recurrence."""


def q(x: object) -> F:
    if type(x) not in (int,F):
        raise RealizationError("Exact integer/rational observations required")
    return F(x)


def hankel(samples: Sequence[F], rows: int, columns: int) -> tuple[tuple[F,...],...]:
    if any(type(z) is not int or z < 1 for z in (rows,columns)):
        raise RealizationError("Positive finite Hankel dimensions required")
    if len(samples) < rows+columns-1:
        raise RealizationError("Not enough ACTUAL source samples for this Hankel block")
    a = tuple(q(x) for x in samples)
    return tuple(tuple(a[i+j] for j in range(columns)) for i in range(rows))


def rank(matrix: Sequence[Sequence[F]]) -> int:
    if not matrix:
        return 0
    n = len(matrix[0])
    if any(len(row)!=n for row in matrix):
        raise RealizationError("Rectangular matrix required")
    A = [[q(x) for x in row] for row in matrix]
    r = 0
    for j in range(n):
        pivot = next((k for k in range(r,len(A)) if A[k][j]),None)
        if pivot is None:
            continue
        A[r],A[pivot] = A[pivot],A[r]
        inv = A[r][j]
        A[r] = [x/inv for x in A[r]]
        for k in range(len(A)):
            if k == r:
                continue
            m = A[k][j]
            if m:
                A[k] = [u-m*v for u,v in zip(A[k],A[r])]
        r += 1
        if r == len(A):
            break
    return r


def determinant(matrix: Sequence[Sequence[F]]) -> F:
    n = len(matrix)
    if any(len(row)!=n for row in matrix):
        raise RealizationError("Square minor required")
    A = [[q(x) for x in row] for row in matrix]
    sign = 1
    det = F(1)
    for k in range(n):
        p = next((i for i in range(k,n) if A[i][k]),None)
        if p is None:
            return F(0)
        if p!=k:
            A[k],A[p]=A[p],A[k]
            sign = -sign
        t=A[k][k]
        det *= t
        for i in range(k+1,n):
            s=A[i][k]/t
            for j in range(k+1,n):
                A[i][j] -= s*A[k][j]
            A[i][k] = 0
    return sign*det


def hankel_dimension_receipt(samples: Sequence[F], rows: int, columns: int) -> dict:
    """Find an explicit exact NONZERO minor attaining observed Hankel rank.

    Bound is unconditional for ANY REALIZATION within the stated LTI class.
    It says NOTHING about other nonlinear/time-changing/nonobservable classes.
    """
    M = hankel(samples,rows,columns)
    r = rank(M)
    if r == 0:
        return {"linear_state_lower_bound":0,"minor_rows":(),"minor_cols":(),
                "minor_determinant":F(1),"rows":rows,"columns":columns,
                "global_upper_bound_proved":False}
    # Greedy independent rows, then greedy independent columns. Polynomial
    # witness extraction, no exponential minor scan and no floating SVD.
    if rows*columns>4096:
        raise RealizationError("Finite witness extraction budget exceeded")
    chosen_rows=[]
    for i in range(rows):
        candidate=chosen_rows+[i]
        if rank([M[j] for j in candidate])>len(chosen_rows):
            chosen_rows=candidate
        if len(chosen_rows)==r:
            break
    chosen_cols=[]
    for j in range(columns):
        candidate=chosen_cols+[j]
        if rank([[M[i][k] for k in candidate] for i in chosen_rows])>len(chosen_cols):
            chosen_cols=candidate
        if len(chosen_cols)==r:
            break
    ii,jj=tuple(chosen_rows),tuple(chosen_cols)
    det=determinant([[M[i][j] for j in jj] for i in ii])
    if len(ii)!=r or len(jj)!=r or not det:
        raise AssertionError("Exact rank disagrees with selected minor")
    return {"linear_state_lower_bound":r,
            "minor_rows":ii,"minor_cols":jj,
            "minor_determinant":det,
            "rows":rows,"columns":columns,
            "global_upper_bound_proved":False}


def verify_dimension_receipt(samples: Sequence[F], receipt: dict) -> bool:
    """Independent reproduction of a sound linear realization lower bound."""
    rows, columns = receipt["rows"], receipt["columns"]
    M = hankel(samples,rows,columns)
    ii,jj=tuple(receipt["minor_rows"]),tuple(receipt["minor_cols"])
    r=receipt["linear_state_lower_bound"]
    if type(r) is not int or not 0<=r<=min(rows,columns):
        return False
    if r==0:
        return all(x==0 for row in M for x in row)
    if len(set(ii))!=r or len(set(jj))!=r or any(type(i) is not int or i<0 or i>=rows for i in ii) or any(type(j) is not int or j<0 or j>=columns for j in jj):
        return False
    witness=tuple(tuple(M[i][j] for j in jj) for i in ii)
    return determinant(witness)==receipt["minor_determinant"] and receipt["minor_determinant"]!=0


def linear_recurrence_prefix(samples: Sequence[F], order: int) -> dict:
    """Infer one recurrence from finite samples WITH independent holdouts.

    Invertibility of H_r and agreement on finitely many holdouts proves only
    finite consistency. Global continuation requires an independently given
    recurrence/linear-time-invariant source assumption.
    """
    a = tuple(q(x) for x in samples)
    if type(order) is not int or order < 1 or len(a)<2*order:
        raise RealizationError("Need at least 2r exact samples for order r")
    M = [list(row) for row in hankel(a,order,order)]
    rhs = list(a[order:2*order])
    if determinant(M)==0:
        raise RealizationError("First r-by-r Hankel block singular: no unique recurrence")
    for j in range(order):
        p=next(i for i in range(j,order) if M[i][j])
        M[j],M[p]=M[p],M[j]
        rhs[j],rhs[p]=rhs[p],rhs[j]
        inv=M[j][j]
        M[j]=[z/inv for z in M[j]]
        rhs[j]/=inv
        for i in range(order):
            if i==j:
                continue
            fac=M[i][j]
            M[i]=[x-fac*y for x,y in zip(M[i],M[j])]
            rhs[i]-=fac*rhs[j]
    coeffs=tuple(rhs)
    mismatches=[]
    for n in range(len(a)-order):
        prediction=sum((coeffs[j]*a[n+j] for j in range(order)),F(0))
        if prediction != a[n+order]:
            mismatches.append((n,a[n+order],prediction))
    return {"coefficients":coeffs,"all_supplied_samples_match":not mismatches,
            "holdout_count":max(0,len(a)-2*order),
            "mismatches":tuple(mismatches),
            "global_recurrence_certified":False}


def forecast_from_recurrence(prefix: Sequence[F], coefficients: Sequence[F],
                             future_steps: int) -> tuple[F,...]:
    """Mathematical model forecast, NOT observation or empirical proof."""
    c=tuple(q(x) for x in coefficients)
    seq=[q(x) for x in prefix]
    if not c or len(seq)<len(c) or type(future_steps) is not int or future_steps<0:
        raise RealizationError("Declared finite recurrence and horizon required")
    for _ in range(future_steps):
        seq.append(sum((c[j]*seq[-len(c)+j] for j in range(len(c))),F(0)))
    return tuple(seq)


def delayed_impulse(horizon: int) -> tuple[F,...]:
    """Infinite δ_n,horizon has minimal LTI dimension exactly horizon+1.

    Returned finite prefix of length 2h+1 gives a *lower* bound h+1 via
    an antidiagonal determinant. Separate nilpotent shift supplies upper.
    """
    if type(horizon) is not int or not 0<=horizon<=32:
        raise RealizationError("Finite delayed-impulse budget 0..32")
    return tuple(F(int(i==horizon)) for i in range(2*horizon+1))


def impulse_realization_check(horizon: int) -> dict:
    """Exact linear nilpotent shift witness with dimension h+1.

    Start b=e_h, shift A e_i=e_(i-1), observation c=e_0^T.
    Then c^T A^n b=δ_(n,h) for every n>=0 by algebra of the shift.
    """
    seq=delayed_impulse(horizon)
    lower=hankel_dimension_receipt(seq,horizon+1,horizon+1)
    if not verify_dimension_receipt(seq,lower):
        raise AssertionError("Invalid Hankel minor for delay source")
    if lower["linear_state_lower_bound"]!=horizon+1:
        raise AssertionError("Delayed impulse rank calculation failed")
    return {"first_horizon_samples_all_zero":all(v==0 for v in seq[:horizon]),
            "minimal_linear_state_dimension":horizon+1,
            "lower_bound_minor_determinant":lower["minor_determinant"],
            "matching_nilpotent_upper_bound":horizon+1,
            "source_globally_linear_is_a_model_assumption":True}
