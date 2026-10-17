"""Exact prime-edge inverse and source-compatible Schur residual saving.

Source premise (from authentic_prime_surplus):
   D_high(w,w) >= kappa ||Vw||² + w2 <Vw,(I-A_b)Vw>.
In the primitive energy variable F=Vw on E=(P_poly<=3)^\perp,
the comparator is kappa I+w2(I-A_b). At b=log(2)>1/2,
A_b flips two equal-width edge strips and vanishes on the center.

It has an EXACT inverse on ambient L²(I):
  symmetric edge eigenvalue kappa, antisymmetric edge kappa+2w2,
  center eigenvalue kappa+w2.
Restricting the variational supremum to E can only make the upper
Schur correction smaller. No original source zero positions are used.
"""
from __future__ import annotations
from fractions import Fraction as F


class PrimeDualError(ValueError):
    pass


def q(x):
    if type(x) not in (int,F):raise PrimeDualError("exact int/Fraction; no float/bool")
    return F(x)


def _row(v):
    try: w=tuple(q(x) for x in v)
    except (TypeError,ValueError) as exc:raise PrimeDualError("finite rational vector") from exc
    if not w:raise PrimeDualError("nonempty finite observation")
    return w


def _norm(v):return sum((x*x for x in v),F(0))


def exact_primitive_edge_dual(left,right,center,*,kappa,w):
    """Finite equal-measure cell calibration, with exact source comparator.

    Actual continuous L² uses the same formula with Hilbert norms. These
    numerical vectors are NOT independent original signed source readings.
    """
    left,right,center=_row(left),_row(right),_row(center)
    if len(left)!=len(right):
        raise PrimeDualError("original edges must have matched source measure")
    kappa,w=q(kappa),q(w)
    if kappa<=0 or w<=0:
        raise PrimeDualError("strict positive Bessel and true prime weight required")
    full=_norm(left)+_norm(right)+_norm(center)
    mismatch=_norm(tuple(a-b for a,b in zip(left,right)))
    raw=full/kappa
    gain_center=w*_norm(center)/(kappa*(kappa+w))
    gain_edge=w*mismatch/(kappa*(kappa+2*w))
    improved=raw-gain_center-gain_edge
    # Independent direct inverse of [[kappa+w,-w],[-w,kappa+w]]
    direct=_norm(center)/(kappa+w)+sum(
        ((kappa+w)*(a*a+b*b)+2*w*a*b)/(kappa*(kappa+2*w))
        for a,b in zip(left,right)
    )
    if improved!=direct or improved<0:
        raise ArithmeticError("exact prime-2 inverse/Loewner saving mismatch")
    return {
        "source_type":"EXACT_EDGE_MODEL_NOT_AUTOMATIC_WEIL",
        "scalar_only_dual":raw,"strict_source_prime_dual_upper":improved,
        "center_saving":gain_center,"edge_phase_saving":gain_edge,
        "total_strict_saving":gain_center+gain_edge,
        "actual_source_residual_recognized":False,"RH_proved":False
    }


def source_dual_coefficients(parity):
    """Source-gated scalar coefficients for all-high primitive Schur residuals.

    Given genuine g=Q_poly<=3((Gv)'), formula supplies
      correction <= ||g||²/kappa
                   - c_C ||g_C||² - c_edge ||g_R-T_b g_L||².
    The source map from particular low x to g must be independently certified.
    """
    if parity not in ("odd","even"):
        raise PrimeDualError("original derivative-parity label required")
    from .authentic_prime_surplus import original_prime_surplus_source_passport
    src=original_prime_surplus_source_passport()
    k=src["kappa_"+parity]
    w=src["positive_source_weight_floor"]
    return {
        "sector":parity,
        "source_sha":src["source_sha"],
        "kappa":k,"w2_lower":w,
        "C_center":w/(k*(k+w)),
        "C_phase_mismatch":w/(k*(k+2*w)),
        "scalar_residual_multiplier":1/k,
        "positive_center_error_is_a_subtraction":True,
        "RH_proved":False
    }


def rational_polynomial_dual_center_witness(primitive,*,parity="odd"):
    """A genuine-SOURCE-coefficient lower saving for a DECLARED polynomial g.

    This does not identify g with any actual Suzuki low/high residual.
    On the true log2 center, [-1/8,1/8] is source-justified. Hence
      saving >= c_C integral_-1/8^1/8 g(x)^2 dx.
    """
    from .authentic_prime_surplus import original_prime_surplus_source_passport,poly_int,poly_mul
    src=original_prime_surplus_source_passport()
    if parity not in ("odd","even"):
        raise PrimeDualError("odd or even derivative-sector source needed")
    p=_row(primitive)
    if any(p[j]!=0 for j in range(len(p)) if (j%2)!= (0 if parity=="odd" else 1)):
        raise PrimeDualError("primitive reflection parity inconsistent with derivative sector")
    k=src["kappa_"+parity];w=src["positive_source_weight_floor"]
    center=poly_int(poly_mul(p,p),-F(1,8),F(1,8))
    norm=poly_int(poly_mul(p,p),-F(1,2),F(1,2))
    saving=w*center/(k*(k+w))
    return {"center_norm2_exact":center,"full_norm2_exact":norm,
            "source_arithmetic_dual_saving_lower":saving,
            "old_dual_upper":norm/k,
            "new_dual_upper":norm/k-saving,
            "actual_original_G_residual_identified":False,
            "source_sha":src["source_sha"],"RH_proved":False}


def _mat(A):
    try:A=tuple(tuple(q(x) for x in row) for row in A)
    except (TypeError,ValueError) as exc:raise PrimeDualError("exact matrix required") from exc
    if not A or len(A)>10 or any(len(row)!=len(A) for row in A):
        raise PrimeDualError("square matrix <=10 required")
    return A


def _transpose(A):return tuple(zip(*A))
def _mv(A,x):return tuple(sum((a*b for a,b in zip(row,x)),F(0)) for row in A)
def _dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))


def _inv(A):
    """Exact small Gauss-Jordan inverse. Input PD must be certified."""
    n=len(A)
    R=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        piv=next((i for i in range(k,n) if R[i][k]!=0),None)
        if piv is None:raise PrimeDualError("singular positive-form matrix")
        R[k],R[piv]=R[piv],R[k]
        t=R[k][k];R[k]=[v/t for v in R[k]]
        for i in range(n):
            if i!=k:
                c=R[i][k];R[i]=[a-c*b for a,b in zip(R[i],R[k])]
    return tuple(tuple(row[n:]) for row in R)


def _det(A):
    n=len(A);M=[list(row) for row in A];result=F(1)
    for k in range(n):
        piv=next((i for i in range(k,n) if M[i][k]!=0),None)
        if piv is None:return F(0)
        if piv!=k:M[k],M[piv]=M[piv],M[k];result=-result
        d=M[k][k];result*=d
        for i in range(k+1,n):
            t=M[i][k]/d
            for j in range(k+1,n):M[i][j]-=t*M[k][j]
            M[i][k]=F(0)
    return result


def _pd(A):
    if any(A[i][j]!=A[j][i] for i in range(len(A)) for j in range(len(A))):
        return False
    return all(_det(tuple(tuple(A[i][j] for j in range(k)) for i in range(k)))>0
               for k in range(1,len(A)+1))


def exact_constrained_dual(B,g,poly_constraints):
    """Finite exact Hilbert-observer counterpart of polynomial-quotient inverse.

    B must be strict PD; constraints are independent column vectors p_i.
    Dual on E=span(p_i)^\perp equals:
      g*B^-1 g -
      (P*B^-1 g)* (P*B^-1 P)^-1 (P*B^-1 g).
    This does NOT create actual original source readings.
    """
    B=_mat(B);g=_row(g);n=len(B)
    if len(g)!=n or not _pd(B):
        raise PrimeDualError("positive definite comparator with matched source residual required")
    cols=tuple(_row(v) for v in poly_constraints)
    if not cols or len(cols)>=n or any(len(v)!=n for v in cols):
        raise PrimeDualError("independent genuine observation constraint vectors required")
    BI=_inv(B)
    BG=_mv(BI,g)
    raw=_dot(g,BG)
    PB=tuple(_mv(BI,p) for p in cols)
    gram=tuple(tuple(_dot(p,q_) for q_ in PB) for p in cols)
    if not _pd(gram):raise PrimeDualError("dependent polynomial observer constraints")
    moment=tuple(_dot(p,BG) for p in cols)
    corrected=_dot(moment,_mv(_inv(gram),moment))
    constrained=raw-corrected
    if constrained<0 or corrected<0 or constrained>raw:
        raise ArithmeticError("finite constrained dual greater than unconstrained")
    return {"unrestricted_inverse_energy":raw,
            "polynomial_orthogonality_saving":corrected,
            "constrained_inverse_energy":constrained,
            "complete_original_Weil_operator":False,"RH_proved":False}
