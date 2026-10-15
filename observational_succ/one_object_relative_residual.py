"""Exact rational finite relative-Schur residual proof laboratory.

Infinite paper theorem (see research/2026-10-15/ONE_OBJECT_RESIDUAL_SCHUR.md):
 D >= kappa Q K Q, K=(-Delta_N)^(-1), H=low ⊕ high;
 Y is a finite high response, r=B-DY;
 L_Y=Y*B+B*Y-Y*DY, T_r[i,j]=<r_i',r_j'>.
 Then L_Y <= B*D^{-1}B <= L_Y + T_r/kappa (quadratic/shorting
 interpretation; NO bounded D^{-1} on infinite Hilbert space assumed).

The code below tests the theorem on exact finite rational declared TOYS.
It is NOT a source certificate for the completed Weil form or RH.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations,product

class ResidualSourceError(ValueError):pass

def q(x):
    if type(x) not in (int,F):
        raise ResidualSourceError("exact integer/Fraction only, no float/bool")
    return F(x)

def matrix(rows,square=False):
    if type(rows) not in (list,tuple) or not rows or len(rows)>8:
        raise ResidualSourceError("bounded nonempty original matrix")
    if type(rows[0]) not in (list,tuple) or not rows[0] or len(rows[0])>8:
        raise ResidualSourceError("bounded nonempty rectangular rows")
    n=len(rows[0])
    if any(type(r) not in (list,tuple) or len(r)!=n for r in rows):
        raise ResidualSourceError("incompatible finite coordinates")
    A=tuple(tuple(q(v) for v in row) for row in rows)
    if square and len(A)!=n:raise ResidualSourceError("square form required")
    return A

def shape(A):return len(A),len(A[0])
def trans(A):return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))
def zero(m,n):return tuple(tuple(F() for _ in range(n)) for _ in range(m))
def eye(n):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def mm(A,B):
    if len(A[0])!=len(B):raise ResidualSourceError("composition dimensions")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F())
                       for j in range(len(B[0]))) for i in range(len(A)))
def add(A,B,scale=1):
    scale=q(scale)
    if shape(A)!=shape(B):raise ResidualSourceError("addition dimensions")
    return tuple(tuple(A[i][j]+scale*B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))
def scale(c,A):
    c=q(c);return tuple(tuple(c*x for x in row) for row in A)
def gram(A,B):return mm(trans(A),B)
def sym(A):
    return len(A)==len(A[0]) and all(A[i][j]==A[j][i]
                for i in range(len(A)) for j in range(len(A)))

def det(A):
    A=matrix(A,square=True)
    n=len(A);W=[list(row) for row in A];sgn=1;prod=F(1)
    for j in range(n):
        pivot=next((r for r in range(j,n) if W[r][j]),None)
        if pivot is None:return F()
        if pivot!=j:W[j],W[pivot]=W[pivot],W[j];sgn=-sgn
        p=W[j][j];prod*=p
        for i in range(j+1,n):
            if W[i][j]:
                a=W[i][j]/p
                for k in range(j+1,n):W[i][k]-=a*W[j][k]
                W[i][j]=F()
    return sgn*prod

def psd(A):
    A=matrix(A,square=True)
    if not sym(A):return False
    for size in range(1,len(A)+1):
        for ix in combinations(range(len(A)),size):
            M=tuple(tuple(A[i][j] for j in ix) for i in ix)
            if det(M)<0:return False
    return True

def pd(A):
    A=matrix(A,square=True)
    return sym(A) and all(det(tuple(tuple(A[i][j] for j in range(k))
                       for i in range(k)))>0 for k in range(1,len(A)+1))

def inv(A):
    A=matrix(A,square=True);n=len(A)
    W=[list(A[i])+list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if W[i][j]),None)
        if p is None:raise ResidualSourceError("finite inverse singular")
        W[j],W[p]=W[p],W[j]
        val=W[j][j];W[j]=[v/val for v in W[j]]
        for i in range(n):
            if i==j:continue
            coeff=W[i][j]
            if coeff:W[i]=[v-coeff*w for v,w in zip(W[i],W[j])]
    return tuple(tuple(row[n:]) for row in W)

def quadratic(A,x):
    x=tuple(q(v) for v in x)
    if len(x)!=len(A):raise ResidualSourceError("vector dimension")
    return sum((x[i]*A[i][j]*x[j] for i in range(len(A))
                for j in range(len(A))),F())

def finite_negative_vector(A,amplitude=3):
    if len(A)>4:raise ResidualSourceError("small exact witness only")
    if type(amplitude) is not int or not 1<=amplitude<=5:
        raise ResidualSourceError("integer witness budget")
    for x in product(range(-amplitude,amplitude+1),repeat=len(A)):
        if any(x) and quadratic(A,x)<0:return x
    return None

@dataclass(frozen=True)
class FiniteRelativeSchur:
    source:str
    kappa:F
    A:tuple
    D:tuple
    K:tuple
    B:tuple
    Y:tuple
    lower_response:tuple
    upper_response:tuple
    true_response:tuple
    residual:tuple
    residual_K_inverse_gram:tuple
    whole_space_positive_from_lower_schur:bool
    exact_finite_negative_witness:tuple|None
    authentic_suzuki_source:bool=False
    rh_proved:bool=False

def _partial_Y(D,B,indices):
    h,l=shape(B)
    if type(indices) is not tuple or len(set(indices))!=len(indices) or any(
       type(i) is not int or not 0<=i<h for i in indices):
        raise ResidualSourceError("lawful finite high observer coordinates")
    if not indices:return zero(h,l)
    W=tuple(tuple(D[i][j] for j in indices) for i in indices)
    R=mm(inv(W),tuple(B[i] for i in indices))
    Y=[[F() for _ in range(l)] for _ in range(h)]
    for idx,i in enumerate(indices):Y[i]=list(R[idx])
    return tuple(tuple(row) for row in Y)

def finite_relative_short(A,D,B,K,kappa,seen=()):
    """Exact two-sided residual bound, declared finite toy only."""
    A,D,B,K=map(matrix,(A,D,B,K))
    kap=q(kappa);h,l=shape(B)
    if (kap<=0 or shape(A)!=(l,l) or shape(D)!=(h,h) or shape(K)!=(h,h)
        or l>4 or not sym(A) or not sym(D) or not pd(K)
        or not psd(add(D,K,-kap))):
        raise ResidualSourceError("original relative K gap not proved")
    Y=_partial_Y(D,B,seen)
    r=add(B,mm(D,Y),-1)
    L=add(add(gram(Y,B),gram(B,Y)),mm(gram(Y,D),Y),-1)
    penalty=mm(gram(r,inv(K)),r)
    U=add(L,penalty,1/kap)
    Rtrue=mm(gram(B,inv(D)),B)
    if not psd(add(Rtrue,L,-1)) or not psd(add(U,Rtrue,-1)):
        raise ArithmeticError("failed exact finite residual Schur theorem")
    lower_short=add(A,U,-1)
    upper_short=add(A,L,-1)
    witness=finite_negative_vector(upper_short)
    if psd(lower_short) and not psd(add(A,Rtrue,-1)):
        raise ArithmeticError("false finite positivity from residual")
    if witness is not None and quadratic(add(A,Rtrue,-1),witness)>=0:
        raise ArithmeticError("fake signed negative certificate")
    return FiniteRelativeSchur("DECLARED_FINITE_RELATIVE_NEUMANN_TOY",kap,
        A,D,K,B,Y,L,U,Rtrue,r,penalty,psd(lower_short),witness)

def missing_H1_obstruction(N):
    """Toy D=K=diag(n^-2), b_n=1/n: b in l2, response R_N=N."""
    if type(N) is not int or not 1<=N<=4096:
        raise ResidualSourceError("bounded positive finite level")
    return {"source":"NONSOBOLEV_TOY","level":N,"finite_response":F(N),
            "bounded_zero_shift_response":False,"authentic_weil":False}

def finite_residual_approaching_zero(N):
    """Toy D=K=diag(n^-2), b_n=n^-2.

    y_n=1 through N only. The infinite inverse vector would be all ones
    (not in l2), while the scalar response is finite. For n>N,
    residual H1 squared =sum n^-2 <=1/N.
    """
    if type(N) is not int or not 1<=N<=4096:
        raise ResidualSourceError("positive approximation level")
    return {"source":"COMPACT_NONINVERTIBLE_TOY","level":N,
            "finite_response":sum((F(1,n*n) for n in range(1,N+1)),F()),
            "residual_H1_squared_upper":F(1,N),
            "infinite_high_inverse_vector_in_l2":False,
            "finite_scalar_zero_shift_response":True,
            "authentic_weil":False}
