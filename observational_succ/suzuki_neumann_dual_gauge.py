"""Suzuki 30-mode NEUMANN DUAL GAUGE: exact Legendre derivative geometry.

Original source prerequisites: genuine signed G_a on H=L²_0(-a,a), actual
Neumann K=V*V, low P_30 span{L_j(x)=P_j(x/a):1<=j<=30},
D_high >= kappa QKQ. For z in QH,
    <L_j',Vz>= -<L_j,z>=0  (Vz ends vanish).
Thus in all high linear functionals -<F',Vz> we may replace
F' by (I-Pi_29)F' without changing *one single* original interaction.
Pi_29 is the L² orthogonal projection onto polynomials degree<=29,
identically span{L_j':1<=j<=30}.

This can sharpen the source-relative upper residual R0 bound, but
C(source derivatives) and its genuine 30×30 Gram are NOT supplied by
generic toy numerical inputs. No LH positivity, original full Weber,
Connes trace or RH is established by a declaration of this theorem.
"""
from __future__ import annotations
from fractions import Fraction as F
from dataclasses import dataclass
from itertools import combinations

class DualGaugeError(ValueError):pass

def q(x):
    if type(x) not in (int,F):
        raise DualGaugeError("exact Fraction/integer only; rejects bool and float")
    return F(x)

def ordinal(n):
    if type(n) is not int or not 1<=n<=30:
        raise DualGaugeError("exact original Legendre moment rank 1..30")
    return n

def matrix(rows,square=False):
    if type(rows) not in (list,tuple) or not rows or len(rows)>30:
        raise DualGaugeError("finite rational matrix bounded rank")
    if type(rows[0]) not in (list,tuple) or not rows[0] or len(rows[0])>30:
        raise DualGaugeError("rectangular mathematical source")
    if any(type(row) not in (list,tuple) or len(row)!=len(rows[0]) for row in rows):
        raise DualGaugeError("common coordinate system missing")
    ans=tuple(tuple(q(v) for v in row) for row in rows)
    if square and len(ans)!=len(ans[0]):
        raise DualGaugeError("quadratic form must be square")
    return ans

def ident(n):
    n=ordinal(n)
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))

def transpose(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def mul(A,B):
    if len(A[0])!=len(B):raise DualGaugeError("original low-to-high dimensions")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F())
                       for j in range(len(B[0]))) for i in range(len(A)))

def minus(A,B):
    if len(A)!=len(B) or any(len(x)!=len(y) for x,y in zip(A,B)):
        raise DualGaugeError("same source matrix basis required")
    return tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(A,B))

def symmetric(A):
    return len(A)==len(A[0]) and A==transpose(A)

def nonnegative_quadratic(A):
    """Exact rational LDL with zero pivots: PSD iff each principal minor >=0.

    Cost O(2^m); intentionally limited to small output Gram m<=5.
    The H1 metric itself has explicit factorization and admits rank=30.
    """
    A=matrix(A,square=True)
    n=len(A)
    if not symmetric(A) or n>5:
        raise DualGaugeError("small exact PSD oracle rank<=5")
    from .suzuki_moment_schur import matinv
    def determinant(B):
        m=len(B);w=[[F(x) for x in row] for row in B];out=F(1)
        for i in range(m):
            p=next((k for k in range(i,m) if w[k][i]),None)
            if p is None:return F()
            if p!=i:w[p],w[i]=w[i],w[p];out=-out
            pivot=w[i][i];out*=pivot
            for j in range(i+1,m):
                factor=w[j][i]/pivot
                for k in range(i+1,m):
                    w[j][k]-=factor*w[i][k]
                w[j][i]=F()
        return out
    return all(determinant(tuple(tuple(A[i][j] for j in I) for i in I))>=0
               for k in range(1,n+1) for I in combinations(range(n),k))

def legendre_derivative_metric(a=F(1,2),rank=30):
    """CLASSICAL exact metric H_jk=∫ L_j'(x)L_k'(x) dx.

    H_jk = [j+k even] min(j,k)(min(j,k)+1)/a,
    L_j(x)=P_j(x/a) on (-a,a). Source is a genuine Neumann
    dual geometry, not the original signed Weil G operator.
    """
    a=q(a);rank=ordinal(rank)
    if a<=0:raise DualGaugeError("positive source window required")
    return tuple(tuple((F(min(i,j)*(min(i,j)+1))/a if (i+j)%2==0 else F())
                       for j in range(1,rank+1))
                 for i in range(1,rank+1))

def inverse_derivative_metric(a=F(1,2),rank=30):
    """CLASSICAL exact inverse: independent odd/even Brownian min blocks.

    For each parity sequence n_i=p,p+2,..., set c_i=n_i(n_i+1),
    increments δ_i=c_i-c_(i-1)>0. H=(1/a)*L diag(δ) L*,
    where L is cumulative sum. H^-1=a Δ*diag(δ^-1) Δ.
    This is parity TRIDIAGONAL in source original Legendre index order.
    """
    a=q(a);rank=ordinal(rank)
    if a<=0:raise DualGaugeError("positive source halfwidth")
    out=[[F() for _ in range(rank)] for _ in range(rank)]
    for first in (1,2):
        levels=list(range(first,rank+1,2))
        vals=[n*(n+1) for n in levels]
        increments=[vals[i]-(vals[i-1] if i else 0)
                    for i in range(len(vals))]
        assert all(v>0 for v in increments)
        m=len(levels)
        for i,n in enumerate(levels):
            diag=F(1,increments[i])+(F(1,increments[i+1]) if i+1<m else F())
            out[n-1][n-1]=a*diag
            if i+1<m:
                val=-a*F(1,increments[i+1])
                out[n-1][levels[i+1]-1]=val
                out[levels[i+1]-1][n-1]=val
    H=legendre_derivative_metric(a,rank)
    ret=tuple(tuple(row) for row in out)
    if mul(H,ret)!=ident(rank) or mul(ret,H)!=ident(rank):
        raise ArithmeticError("genuine Neumann-dual Legendre inverse identity failed")
    return ret

@dataclass(frozen=True)
class GaugeCertificate:
    source:str
    low_rank:int
    derivative_gram:tuple
    mixed_derivative_moments:tuple
    ungauged_gram:tuple
    projected_derivative_gram:tuple
    improvement_gram:tuple
    true_suzuki_derivative_moments_authenticated:bool=False
    original_full_30mode_Schur_PSD:bool=False
    rh_proved:bool=False

def finite_dual_gauge_derivative_gram(T,moments,a=F(1,2)):
    """Mathematical orthogonal projection identity for exact SMALL models.

    Input T_ij=<f_i',f_j'> and moments M_ki=<L_k',f_i'>.
    CHECKS that source-neutral block [[H,M],[M*,T]] is PSD;
    it may not be stamped with original Suzuki source identification
    solely by satisfying rational inequalities. Returns optimized
    residual Gram C=T-M*H^-1 M <= T.

    For m=30 this is EXACT 30-gauge projector with small number
    of test directions (m_low<=5) to keep rigorous minors affordable.
    """
    T=matrix(T,square=True);M=matrix(moments)
    rank,nvec=len(M),len(T)
    if len(M[0])!=nvec or nvec>5 or not symmetric(T):
        raise DualGaugeError("exact gauge source/test columns mismatch")
    a=q(a)
    H=legendre_derivative_metric(a,rank)
    Hinv=inverse_derivative_metric(a,rank)
    improvement=mul(mul(transpose(M),Hinv),M)
    residual=minus(T,improvement)
    if not nonnegative_quadratic(residual):
        raise DualGaugeError("input inconsistent with any real Hilbert-space source")
    return GaugeCertificate("DECLARED_EXACT_SOURCE_NEUTRAL_GRAM",rank,H,M,T,
                            residual,improvement)

def normalized_parity_blocks(rank=30):
    """One actual parity decomposition 15+15 for full source k<=30."""
    rank=ordinal(rank)
    return {"low_odd":tuple(range(1,rank+1,2)),
            "low_even":tuple(range(2,rank+1,2)),
            "source":"GENUINE_LEGENDRE_NEUMANN_DUAL_GEOMETRY",
            "original_weil_sign":False}
