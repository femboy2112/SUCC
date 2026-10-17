"""Exact finite conditional transport of nested Schur Loewner enclosures.

Given source-authenticated symmetric finite L <= S <= U on F_low+F_mid,
AND strictly positive middle compression of L, variational infimum yields

    Short_low(L) <= Short_low(S) <= Short_low(U).

This module checks algebra, not source provenance. A PSD 30-mode bracket is NOT
a supplied actual original Suzuki S30; no arbitrary U=lower or upper may be
relabeled as authenticated. No regularized inverse of compact D and no RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations

class NestedShortError(ValueError):
    pass


def _q(x):
    if type(x) not in (int,F):raise NestedShortError("Exact int/Fraction required")
    return F(x)


def _sq(M):
    if type(M) not in (tuple,list) or not M:raise NestedShortError("Nonempty matrix")
    m=tuple(tuple(_q(x) for x in row) for row in M)
    n=len(m)
    if n>32 or any(len(row)!=n for row in m) or any(m[i][j]!=m[j][i] for i in range(n) for j in range(n)):
        raise NestedShortError("Symmetric square rational matrix size<=32")
    return m


def _sub(M,N):
    return tuple(tuple(M[i][j]-N[i][j] for j in range(len(M))) for i in range(len(M)))


def _inv(D):
    n=len(D)
    a=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(D)]
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:raise NestedShortError("Middle matrix singular")
        a[k],a[p]=a[p],a[k]
        d=a[k][k]
        a[k]=[x/d for x in a[k]]
        for i in range(n):
            if i==k:continue
            c=a[i][k]
            a[i]=[x-c*y for x,y in zip(a[i],a[k])]
    return tuple(tuple(row[n:]) for row in a)


def _positive_definite(M):
    M=_sq(M);n=len(M)
    a=[list(row) for row in M]
    for k in range(n):
        d=a[k][k]
        if d<=0:return False
        for i in range(k+1,n):
            for j in range(i,n):
                a[j][i]-=a[i][k]*a[j][k]/d
                a[i][j]=a[j][i]
    return True


def _psd(M):
    M=_sq(M)
    # For n<=8, exhaustive principal-minor PSD. For n>8 refuse rather than
    # silently equate a positive pivot heuristic with semidefiniteness.
    n=len(M)
    if n>8:raise NestedShortError("Exact PSD validation supported only for n<=8")
    for k in range(1,n+1):
        for idx in combinations(range(n),k):
            a=[[M[i][j] for j in idx] for i in idx]
            det=F(1)
            for j in range(k):
                p=next((i for i in range(j,k) if a[i][j]),None)
                if p is None:det=F(0);break
                if p!=j:a[j],a[p]=a[p],a[j];det=-det
                pivot=a[j][j];det*=pivot
                for i in range(j+1,k):
                    c=a[i][j]/pivot
                    for col in range(j+1,k):a[i][col]-=c*a[j][col]
                    a[i][j]=F(0)
            if det<0:return False
    return True


def short_to_low(M, low_rank):
    M=_sq(M);n=len(M)
    if type(low_rank) is not int or not 1<=low_rank<n:
        raise NestedShortError("Proper positive low rank required")
    D=tuple(tuple(M[i][j] for j in range(low_rank,n)) for i in range(low_rank,n))
    inv=_inv(D)
    ans=[]
    for i in range(low_rank):
        row=[]
        for j in range(low_rank):
            correction=sum((M[i][low_rank+k]*inv[k][l]*M[low_rank+l][j]
                             for k in range(n-low_rank) for l in range(n-low_rank)),F())
            row.append(M[i][j]-correction)
        ans.append(tuple(row))
    return tuple(ans)


def monotone_nested_short_bounds(lower,upper,low_rank):
    """Conditional certificate; ONLY after independently authenticating L<=S<=U.

    Returns exact Schur lower and upper; checks L<=U, the required positivity
    of the discarded middle block of L, and that the resulting order holds.
    This test must NEVER claim L/U are original source data on its own.
    """
    L=_sq(lower);U=_sq(upper)
    if len(L)!=len(U):raise NestedShortError("Mismatched packet shape")
    if len(L)>8:raise NestedShortError("Principal-minor checker bounded at dimension 8")
    if not _psd(_sub(U,L)):
        raise NestedShortError("Upper does not dominate lower in Loewner order")
    if type(low_rank) is not int or not 1<=low_rank<len(L):
        raise NestedShortError("Invalid nested reduction size")
    D=tuple(tuple(L[i][j] for j in range(low_rank,len(L)))
            for i in range(low_rank,len(L)))
    if not _positive_definite(D):
        raise NestedShortError("LOWER packet's discarded middle block not strictly positive")
    SL=short_to_low(L,low_rank);SU=short_to_low(U,low_rank)
    if not _psd(_sub(SU,SL)):
        raise AssertionError("Proved monotone shorting identity failed")
    return {"low_short_lower":SL,"low_short_upper":SU,
            "finite_rational_order_verified":True,
            "original_source_identified":False,
            "source_condition":"caller must separately prove L <= actual S30 <= U",
            "all_radii_positive_proved":False,"RH_proved":False}


def sign_switch_countermodel():
    """When discarded block crosses 0, even L<=U cannot order Schur forms."""
    L=((F(0),F(1)),(F(1),F(-1)))
    U=((F(0),F(1)),(F(1),F(1)))
    return {"lower":L,"upper":U,"short_lower":short_to_low(L,1),
            "short_upper":short_to_low(U,1),
            "U_minus_L_PSD":_psd(_sub(U,L)),
            "short_order_reversed":short_to_low(L,1)[0][0]>short_to_low(U,1)[0][0],
            "discarded_block_strict_positive_missing":True,"RH_proved":False}

__all__=["NestedShortError","short_to_low","monotone_nested_short_bounds",
         "sign_switch_countermodel"]
