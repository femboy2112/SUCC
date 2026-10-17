"""Exact-rational four-moment primitive-dual Schur geometry.

MATH ONLY: arbitrary matrices given to this module are NOT source-authenticated.
Authentic Suzuki/Gamma/prime data must enter through the gated parent
certified_four_schur_trial module. No zeta zeros or RH-sign conclusion.

For I=(-a,a), H=L^2_0(I), Q=I-P_{Legendre 1..4}, Vw(t)=int_-a^t w:

    closure_{L2}(V QH) = (span{1,t,t^2,t^3})^perp.

For h in H^1(I) and r=Qh, the variational dual norm relative to
K=V*V on QH is EXACTLY

    sup_{w in QH, w != 0} |<r,w>|^2 / <Kw,w>
      = ||(I-P_{polynomial degree<=3}) h'||_2^2.

The equality does NOT assert ||(Qh)'|| <= ||h'|| (false).  Together with
h=G(x-Ux) and genuine ||g'||_L1 < 11/40, it yields a rigorous, U-dependent
but potentially conservative bound with no high Legendre derivative tail.

Polynomial projection may later sharpen it, *if* the input h'-moments are
independently authenticated. A caller-supplied matrix is not an attestation.
"""
from __future__ import annotations

from fractions import Fraction as F


class DualQuotientError(ValueError):
    """A typed exact proof input is missing or malformed."""


def _f(x):
    if type(x) not in (int, F):
        raise DualQuotientError("Only exact int/Fraction allowed (not bool or float)")
    return F(x)


def _matrix(M, rows=None, cols=None):
    if type(M) not in (tuple, list) or not M:
        raise DualQuotientError("Nonempty matrix required")
    out = tuple(tuple(_f(x) for x in row) for row in M)
    if not out[0] or any(len(row) != len(out[0]) for row in out):
        raise DualQuotientError("Rectangular exact matrix required")
    if rows is not None and len(out) != rows:
        raise DualQuotientError("Wrong row count")
    if cols is not None and len(out[0]) != cols:
        raise DualQuotientError("Wrong column count")
    return out


def _trans(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def _mul(a, b):
    if len(a[0]) != len(b):
        raise DualQuotientError("Incompatible matrix maps")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def _subtract(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise DualQuotientError("Incompatible Gram matrices")
    return tuple(tuple(a[i][j]-b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def _scale(a, c):
    c = _f(c)
    return tuple(tuple(c*x for x in row) for row in a)


def _inverse(a):
    """Exact rational inverse; raises on singular input, no floating pivots."""
    a=_matrix(a)
    n=len(a)
    if n!=len(a[0]):
        raise DualQuotientError("Only square matrices invertible")
    rows=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        piv=next((k for k in range(j,n) if rows[k][j]),None)
        if piv is None:
            raise DualQuotientError("Singular moment Gram")
        rows[j],rows[piv]=rows[piv],rows[j]
        c=rows[j][j]
        rows[j]=[x/c for x in rows[j]]
        for i in range(n):
            if i==j:continue
            d=rows[i][j]
            if d:rows[i]=[x-d*y for x,y in zip(rows[i],rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def polynomial_moment_gram(radius=F(1,2), degree=3):
    """Exact Gram of 1,t,...,t^degree on (-radius,radius)."""
    a=_f(radius)
    if not a>0 or type(degree) is not int or not 0<=degree<=12:
        raise DualQuotientError("Positive exact radius and degree 0..12 required")
    return tuple(tuple((a**(i+j+1)-(-a)**(i+j+1))/F(i+j+1)
                       for j in range(degree+1)) for i in range(degree+1))


def derivative_moment_projection_gram(moments, radius=F(1,2)):
    """Exact Gram of L2 projection of derivative vectors onto polynomials 0..3.

    moments[j][i] MUST equal int_I t^j h_i'(t) dt, i.e. four rows.
    This is pure algebra. Not a source passport. Do not use unverified moments
    as a certified original Weil/Suzuki lower-bound improvement.
    """
    E=_matrix(moments,rows=4)
    gram=polynomial_moment_gram(radius,3)
    return _mul(_mul(_trans(E),_inverse(gram)),E)


def _is_psd(a):
    """Exact rational symmetric PSD check via principal minors, n<=8."""
    from itertools import combinations
    a=_matrix(a)
    n=len(a)
    if n>8 or n!=len(a[0]) or any(a[i][j]!=a[j][i] for i in range(n) for j in range(n)):
        raise DualQuotientError("Symmetric rational Gram of size <=8 required")
    for k in range(1,n+1):
        for ids in combinations(range(n),k):
            sub=tuple(tuple(a[i][j] for j in ids) for i in ids)
            # Determinant by exact fraction-free-ish Gaussian elimination with pivoting.
            R=[list(row) for row in sub]; det=F(1)
            for j in range(k):
                piv=next((i for i in range(j,k) if R[i][j]),None)
                if piv is None:det=F(0);break
                if piv!=j:R[j],R[piv]=R[piv],R[j];det=-det
                pivot=R[j][j];det*=pivot
                for i in range(j+1,k):
                    f=R[i][j]/pivot
                    for col in range(j+1,k):R[i][col]-=f*R[j][col]
                    R[i][j]=F(0)
            if det<0:return False
    return True


def quotient_derivative_cap(norm_gram, gprime_L1=F(11,40),
                            kappa=F(1,50), authenticated_derivative_moments=None,
                            radius=F(1,2)):
    """Exact finite conditional bound on K-dual high residual source energy.

    Premises: 
      - H=L2_0(I), Q=orth projection off first 4 nonconstant Legendre modes;
      - G is mean-zero compression of convolution with even anchored g;
      - ||g'||_{L1(I-I)} < gprime_L1 and D>=kappa Q K Q;
      - v_i in H have authentic L2 Gram norm_gram;
      - IF moments given, each is independently certified ∫t^j (Gv_i)' dt.
    Then residual response correction is <= this PSD matrix in Loewner order.
    Inputs are NOT authenticated by this mathematical function itself.
    """
    W=_matrix(norm_gram)
    n=len(W)
    if n>8 or n!=len(W[0]) or not _is_psd(W):
        raise DualQuotientError("Norm Gram must be symmetric PSD of size <=8")
    C=_f(gprime_L1); k=_f(kappa)
    if not C>0 or not k>0:
        raise DualQuotientError("Positive source L1 budget and K-coercivity premise required")
    full=_scale(W,C*C)
    projection=None
    if authenticated_derivative_moments is not None:
        projection=derivative_moment_projection_gram(authenticated_derivative_moments,radius)
        if len(projection)!=n:
            raise DualQuotientError("Derivative-moment column count != source vectors")
        difference=_subtract(full,projection)
        if not _is_psd(difference):
            raise DualQuotientError("Input moments violate source Young inequality; forged certificate")
    else:
        difference=full
    return {"residual_correction_upper":_scale(difference,F(1)/k),
            "source_L1_budget":C,"kappa":k,"derivative_moment_subtraction":projection,
            "requires_independent_source_authentication":True,
            "projected_derivative_norm_not_assumed_contracting":True,
            "RH_proved":False}



def vanishing_boundary_moment_lower(mid_rows, error_rows, eta=F(1,2)):
    """Exact Loewner lower for two original-source derivative projection channels.

    At a=1/2, phi_e=t^2-1/4 and phi_o=t*(t^2-1/4) vanish at both
    endpoints. For h_i=Gv_i, integration by parts gives
       <h_i',phi_e> = - <P1(2t), h_i>,
       <h_i',phi_o> = -(1/2)<P2(2t),h_i>.
    ||phi_e||^2=1/30 and ||phi_o||^2=1/840, orthogonal by parity.
    Therefore the true degree<=3 projection energy dominates the matrix
       30 c1*c1^T + 210 c2*c2^T,
    where c_j,i=<P_j,Gv_i> are authentic *source* channels.

    Given exact interval rows c_k,i in [mid_k,i +- error_k,i], bound for
    every x using (a+b)^2 >= (1-eta)a^2 -(eta^-1-1)b^2:
       c_k c_k^T >= (1-eta) mid_k mid_k^T
                       -(eta^-1-1)||error_k||^2 I.
    Returning a matrix that may be INDEFINITE is mathematically valid as a
    lower Loewner bound; never clamp its negative eigenvalues to zero.

    This function does NOT authenticate rows. Only parent source-gated
    CertifiedTrial may call it with pinned G_J plus rigorous Gamma-tail errors.
    """
    M=_matrix(mid_rows,rows=2)
    E=_matrix(error_rows,rows=2,cols=len(M[0]))
    t=_f(eta)
    if not 0<t<1 or any(x<0 for row in E for x in row):
        raise DualQuotientError("0<eta<1 and nonnegative row error bounds required")
    n=len(M[0])
    result=[[F(0)]*n for _ in range(n)]
    for weight,row,errors in ((F(30),M[0],E[0]),(F(210),M[1],E[1])):
        radius2=sum((x*x for x in errors),F())
        for i in range(n):
            for j in range(n):
                result[i][j]+=weight*((1-t)*row[i]*row[j]
                                      - ((1/t)-1)*radius2*(i==j))
    return tuple(tuple(row) for row in result)


def trace_primitive_polynomial_countermodel():
    """Exact h=P5(2t)-P3(2t): derivative projection is NOT contractive.

    h'=18 P4(2t), ||h'||^2=36. L2 projection Q onto Legendre
    modes >=5 gives Qh=P5(2t), and ||(Qh)'||^2=60 >36.
    Yet the K-dual high residual is ||(I-P_poly<=3)h'||^2=36.
    """
    return {"full_derivative_energy":F(36),"projected_derivative_energy":F(60),
            "high_K_dual_energy":F(36),
            "false_projection_contraction_factor":F(5,3),
            "projection_derivative_contraction_refuted":True,"RH_proved":False}


__all__=["DualQuotientError","polynomial_moment_gram",
         "derivative_moment_projection_gram","quotient_derivative_cap",
         "vanishing_boundary_moment_lower",
         "trace_primitive_polynomial_countermodel"]
