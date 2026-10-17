"""Closed-form sparse Legendre certificate for shared Suzuki contact uncertainty.

On (-1/2,1/2), u_k(x)=P_k(2x), k>=1, and V u_k=integral_-1/2^x u_k:
    V u_k=(u_(k+1)-u_(k-1))/(2*(2*k+1)).
Projection Q=1-P_{polynomial<=3} discards Legendre indices 0,1,2,3.
Thus B_{j,k}=(delta_{j,k+1}-delta_{j,k-1})/(2*(2*k+1)), j>=4;
V*Q V=B* diag((2j+1)^-1) B exactly. No floating integration.
"""
from __future__ import annotations
from fractions import Fraction as F


class ContactLadderError(ValueError):
    pass


def projected_contact_legendre_coefficients(rank, degree=3):
    if type(rank) is not int or not 1<=rank<=128:
        raise ContactLadderError("genuine integer Legendre rank 1..128 required")
    if type(degree) is not int or not 0<=degree<=rank+1:
        raise ContactLadderError("polynomial projection degree within 0..rank+1")
    # Matrix rows indexed by actual Legendre j=degree+1,...,rank+1.
    return tuple(
        tuple(
            (F(1,2*(2*k+1)) if j==k+1 else
             -F(1,2*(2*k+1)) if j==k-1 else F(0))
            for k in range(1,rank+1))
        for j in range(degree+1,rank+2)
    )


def projected_contact_gram(rank, degree=3):
    B=projected_contact_legendre_coefficients(rank,degree)
    return tuple(tuple(
        sum((B[j-(degree+1)][k-1]*B[j-(degree+1)][l-1]/
             F(2*j+1) for j in range(degree+1,rank+2)),F(0))
        for l in range(1,rank+1))
        for k in range(1,rank+1))


def projected_contact_trial_gram(V, degree=3):
    """Columns V[k-1][i] are exact low+high Legendre trial coefficients."""
    V=tuple(tuple(x for x in row) for row in V)
    if not V or any(not row or len(row)!=len(V[0]) for row in V):
        raise ContactLadderError("nonempty rectangular source trial matrix required")
    for row in V:
        for x in row:
            if type(x) not in (F,int):
                raise ContactLadderError("exact rational trial required")
    V=tuple(tuple(F(x) for x in row) for row in V)
    B=projected_contact_legendre_coefficients(len(V),degree)
    n=len(V[0])
    W=tuple(tuple(sum((B[j][k]*V[k][i] for k in range(len(V))),F(0))
                  for i in range(n)) for j in range(len(B)))
    return tuple(tuple(
        sum((W[j][i]*W[j][l]/F(2*(degree+1+j)+1)
             for j in range(len(B))),F(0))
        for l in range(n)) for i in range(n))


def exact_contact_low4_certificate():
    K=projected_contact_gram(4,3)
    return {
        "gram":K,
        "mode1_norm2":K[0][0],
        "mode2_norm2":K[1][1],
        "mode3_norm2":K[2][2],
        "mode4_norm2":K[3][3],
        "source_contact_direction_first_two_zero":K[0][0]==K[1][1]==0,
        "mode3_expected":K[2][2]==F(1,1764),
        "mode4_expected":K[3][3]==F(1,3564),
        "all_exact":True,
        "RH_proved":False,
    }
