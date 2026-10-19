"""Sharp source-surplus rank-one Loewner gate via Douglas square-root range.

CLASSICAL operator lemma, not a new Weil positivity theorem:
 A>=delta |v><v| (delta>0) iff v in ran(A**(1/2)),
 with optimal delta=1/||A**(-1/2) v||**2 on its minimum-norm range.
 Exact finite rational solver and hostile infinite diagonal calibrations.
 Actual Suzuki source-surplus D4-kappa*K is NOT identified by this module.
"""
from __future__ import annotations
from fractions import Fraction as F

from .direct_quotient_schur import exact_psd


class SurplusRangeError(ValueError):
    pass


def _rat(x):
    if type(x) not in (int,F):
        raise SurplusRangeError("exact integer/Fraction required")
    return F(x)


def _rect(A):
    try:
        A=tuple(tuple(_rat(z) for z in row) for row in A)
    except (TypeError,ValueError) as e:
        raise SurplusRangeError("exact rational matrix required") from e
    if not A or len(A)>8 or any(len(row)!=len(A) for row in A):
        raise SurplusRangeError("square rational size 1..8 required")
    return A


def source_surplus_rank_one_gate(A, v):
    """Exact rational n<=8 certificate for A>=delta vv*.

    Finite theorem is rigorous; does not claim original analytic A is a
    finite matrix. For v=0 the rank-one gate is vacuous and rejected.
    """
    A=_rect(A)
    try:
        v=tuple(_rat(x) for x in v)
    except (TypeError,ValueError) as e:
        raise SurplusRangeError("exact nonzero vector required") from e
    n=len(A)
    if len(v)!=n or not any(v):
        raise SurplusRangeError("nonzero vector matching A required")
    if not exact_psd(A):
        raise SurplusRangeError("positive original-source surplus not proved")
    M=[list(row)+[v[i]] for i,row in enumerate(A)]
    pivots=[]
    row=0
    for col in range(n):
        pivot=next((i for i in range(row,n) if M[i][col]),None)
        if pivot is None:continue
        M[row],M[pivot]=M[pivot],M[row]
        factor=M[row][col]
        M[row]=[q/factor for q in M[row]]
        for j in range(n):
            if j!=row:
                t=M[j][col]
                if t:M[j]=[a-t*b for a,b in zip(M[j],M[row])]
        pivots.append(col)
        row+=1
        if row==n:break
    compatible=all(any(M[i][j] for j in range(n)) or not M[i][n]
                   for i in range(n))
    if not compatible:
        return {"square_root_range_holds":False,
                "positive_delta_exists":False,"best_delta":None,
                "reason":"v not in finite range(A) (equivalently range(A^1/2))",
                "original_source_surplus_identified":False,"RH_proved":False}
    x=[F(0)]*n
    for i,col in enumerate(pivots):x[col]=M[i][n]
    if any(sum((A[i][j]*x[j] for j in range(n)),F(0))!=v[i]
           for i in range(n)):
        raise ArithmeticError("exact range-system verification failed")
    dual=sum((v[i]*x[i] for i in range(n)),F(0))
    if dual<=0:raise ArithmeticError("nonzero PSD range source must have positive dual norm")
    delta=1/dual
    def difference(k):
        return tuple(tuple(A[i][j]-k*v[i]*v[j] for j in range(n))
                     for i in range(n))
    if not exact_psd(difference(delta)) or exact_psd(difference(delta+F(1,1000))):
        raise ArithmeticError("exact optimal rank-one Loewner delta failed")
    return {"square_root_range_holds":True,"positive_delta_exists":True,
            "best_delta":delta,"dual_squared":dual,
            "rank":len(pivots),"verified_psd_at_best":True,
            "verified_not_psd_above_best":True,
            "original_source_surplus_identified":False,"RH_proved":False}


def infinite_diagonal_surplus_obstruction(N):
    """Exact finite-prefix spectral receipt; infinite conclusion is paper proof.

    A=diag(n^-4). v^hard_n=n^-2 => sum |v|²/lambda=N,
    so no uniform delta>0 on ell² as N->infinity despite all finite
    blocks positive. v^soft_n=n^-3 => sum n^-2 <2,
    so uniform delta=1/2 works; source-free toy, NOT Suzuki.
    """
    if type(N) is not int or not 1<=N<=10**5:
        raise SurplusRangeError("positive bounded integer horizon required")
    harmonic2=sum((F(1,n*n) for n in range(1,N+1)),F(0))
    return {
        "N":N,
        "hard_dual_squared":F(N),
        "hard_exact_finite_delta":F(1,N),
        "hard_no_uniform_positive_delta_in_infinite_limit":True,
        "soft_dual_squared":harmonic2,
        "soft_certified_uniform_delta":F(1,2),
        "soft_partial_delta_gt_half":harmonic2<F(2),
        "premise": "diagonal infinite toy, not original Suzuki source",
        "RH_proved":False
    }


def positive_diagonal_not_rank_one_certificate():
    A=((F(1),F(1)),(F(1),F(1)))
    no=source_surplus_rank_one_gate(A,(F(1),F(0)))
    yes=source_surplus_rank_one_gate(A,(F(1),F(1)))
    return {"positive_diagonal":A[0][0]>0,
            "wrong_direction_delta_exists":no["positive_delta_exists"],
            "aligned_direction_best_delta":yes["best_delta"],
            "RH_proved":False}
