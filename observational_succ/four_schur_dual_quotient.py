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


def _sector_rank_one_lower(weight, mid_row, err_row, sector_indices, n, strict_parity=True):
    """Exact Loewner lower bound on weight * c^T c for an interval row c in [m - e, m + e]
    supported on `sector_indices`.

    For any x, |(c_i c_j - m_i m_j)| <= |m_i| e_j + e_i |m_j| + e_i e_j =: Delta_{ij}.
    On the subspace R^{sector}, the symmetric nonnegative matrix Delta has spectral
    radius bounded by r_S = max_{i in S} sum_{j in S} Delta_{ij}.
    Hence weight * c^T c >= weight * (m^T m - r_S I_S), preserving 100% of m^T m at zero
    error and never leaking even-sector error radii onto odd-sector diagonal entries.
    """
    w = _f(weight)
    if w <= 0:
        raise DualQuotientError("Positive channel weight required")
    if any(x < 0 for x in err_row):
        raise DualQuotientError("Nonnegative interval row errors required")
    sector_set = set(sector_indices)
    if strict_parity:
        for idx in range(n):
            if idx not in sector_set and (mid_row[idx] != 0 or err_row[idx] != 0):
                raise DualQuotientError("Row violates reflection parity sector")
    active = tuple(range(n)) if not strict_parity else tuple(sector_indices)
    r_s = F(0)
    for i in active:
        row_err = sum(
            (abs(mid_row[i]) * err_row[j] + err_row[i] * abs(mid_row[j]) + err_row[i] * err_row[j]
             for j in active),
            F(0),
        )
        if row_err > r_s:
            r_s = row_err
    out = [[F(0)] * n for _ in range(n)]
    for i in active:
        for j in active:
            out[i][j] = w * (mid_row[i] * mid_row[j] - (r_s if i == j else F(0)))
    return out


def parity_isolated_two_moment_lower(mid_rows, error_rows, strict_parity=True):
    """Parity-isolated Loewner lower bound for 30 c_1^T c_1 + 210 c_2^T c_2.

    Eliminates both the cross-parity error contamination (where weight-210 even
    errors penalized odd modes 1 and 3) and the 50% signal loss of hardcoded eta=1/2.
    """
    M = _matrix(mid_rows, rows=2)
    E = _matrix(error_rows, rows=2, cols=len(M[0]))
    n = len(M[0])
    odd_sector = tuple(i for i in range(n) if i % 2 == 0)
    even_sector = tuple(i for i in range(n) if i % 2 == 1)
    odd_part = _sector_rank_one_lower(F(30), M[0], E[0], odd_sector, n, strict_parity=strict_parity)
    even_part = _sector_rank_one_lower(F(210), M[1], E[1], even_sector, n, strict_parity=strict_parity)
    return tuple(tuple(odd_part[i][j] + even_part[i][j] for j in range(n)) for i in range(n))


def monomial_moments_from_mixed_rows(mixed_mid_rows, mixed_error_rows, strict_parity=True):
    """Exact transformation from mixed Legendre derivative rows M_{k,i} = <u_k', h_i'>
    (k=1..4, u_k(t)=P_k(2t) on (-1/2,1/2)) to monomial derivative moments
    E_{j,i} = int_{-1/2}^{1/2} t^j h_i'(t) dt (j=0..3):

        E_0 = (1/2) M_1
        E_1 = (1/12) M_2
        E_2 = (1/40) M_1 + (1/60) M_3
        E_3 = (1/112) M_2 + (1/280) M_4
    """
    M = _matrix(mixed_mid_rows, rows=4)
    Err = _matrix(mixed_error_rows, rows=4, cols=len(M[0]))
    if any(x < 0 for row in Err for x in row):
        raise DualQuotientError("Nonnegative mixed-moment error bounds required")
    n = len(M[0])
    if strict_parity:
        for k in range(4):
            for i in range(n):
                if (k - i) % 2 and (M[k][i] != 0 or Err[k][i] != 0):
                    raise DualQuotientError("Mixed derivative row violates reflection parity")
    E_mid = [
        tuple(F(1, 2) * M[0][i] for i in range(n)),
        tuple(F(1, 12) * M[1][i] for i in range(n)),
        tuple(F(1, 40) * M[0][i] + F(1, 60) * M[2][i] for i in range(n)),
        tuple(F(1, 112) * M[1][i] + F(1, 280) * M[3][i] for i in range(n)),
    ]
    E_err = [
        tuple(F(1, 2) * Err[0][i] for i in range(n)),
        tuple(F(1, 12) * Err[1][i] for i in range(n)),
        tuple(F(1, 40) * Err[0][i] + F(1, 60) * Err[2][i] for i in range(n)),
        tuple(F(1, 112) * Err[1][i] + F(1, 280) * Err[3][i] for i in range(n)),
    ]
    return tuple(E_mid), tuple(E_err)


def legendre_moments_from_mixed_rows(mixed_mid_rows, mixed_error_rows, strict_parity=True):
    """Exact transformation from M_{k,i} = <u_k', h_i'> (k=1..4) to shifted-Legendre
    derivative moments L_{m,i} = <P_m(2t), h_i'(t)> (m=0..3):

        L_0 = (1/2) M_1
        L_1 = (1/6) M_2
        L_2 = (1/10) (M_3 - M_1)
        L_3 = (1/14) (M_4 - M_2)
    """
    M = _matrix(mixed_mid_rows, rows=4)
    Err = _matrix(mixed_error_rows, rows=4, cols=len(M[0]))
    if any(x < 0 for row in Err for x in row):
        raise DualQuotientError("Nonnegative mixed-moment error bounds required")
    n = len(M[0])
    if strict_parity:
        for k in range(4):
            for i in range(n):
                if (k - i) % 2 and (M[k][i] != 0 or Err[k][i] != 0):
                    raise DualQuotientError("Mixed derivative row violates reflection parity")
    L_mid = (
        tuple(F(1, 2) * M[0][i] for i in range(n)),
        tuple(F(1, 6) * M[1][i] for i in range(n)),
        tuple(F(1, 10) * (M[2][i] - M[0][i]) for i in range(n)),
        tuple(F(1, 14) * (M[3][i] - M[1][i]) for i in range(n)),
    )
    L_err = (
        tuple(F(1, 2) * Err[0][i] for i in range(n)),
        tuple(F(1, 6) * Err[1][i] for i in range(n)),
        tuple(F(1, 10) * (Err[2][i] + Err[0][i]) for i in range(n)),
        tuple(F(1, 14) * (Err[3][i] + Err[1][i]) for i in range(n)),
    )
    return L_mid, L_err


def complete_four_moment_lower(c_mid_rows, c_error_rows, m34_mid_rows, m34_error_rows, strict_parity=True):
    """Exact Loewner lower bound for the complete degree<=3 polynomial derivative
    projection E^* P^{-1} E using the orthogonal interior-plus-boundary decomposition:

        P_{<=3}(-1/2,1/2) = span{phi_e, phi_o} (+) span{u_3', u_4'},
        E^* P^{-1} E = 30 c_1^T c_1 + 210 c_2^T c_2 + (1/24) M_3^T M_3 + (1/40) M_4^T M_4,

    where c_{1,i}=<P_1, h_i>, c_{2,i}=<P_2, h_i> are the interior low Galerkin channels
    and M_{3,i}=<u_3', h_i'>, M_{4,i}=<u_4', h_i'> are the orthogonal boundary channels.
    """
    C_mid = _matrix(c_mid_rows, rows=2)
    C_err = _matrix(c_error_rows, rows=2, cols=len(C_mid[0]))
    M_mid = _matrix(m34_mid_rows, rows=2, cols=len(C_mid[0]))
    M_err = _matrix(m34_error_rows, rows=2, cols=len(C_mid[0]))
    n = len(C_mid[0])
    odd_sector = tuple(i for i in range(n) if i % 2 == 0)
    even_sector = tuple(i for i in range(n) if i % 2 == 1)
    p_c1 = _sector_rank_one_lower(F(30), C_mid[0], C_err[0], odd_sector, n, strict_parity=strict_parity)
    p_c2 = _sector_rank_one_lower(F(210), C_mid[1], C_err[1], even_sector, n, strict_parity=strict_parity)
    p_m3 = _sector_rank_one_lower(F(1, 24), M_mid[0], M_err[0], odd_sector, n, strict_parity=strict_parity)
    p_m4 = _sector_rank_one_lower(F(1, 40), M_mid[1], M_err[1], even_sector, n, strict_parity=strict_parity)
    return tuple(
        tuple(p_c1[i][j] + p_c2[i][j] + p_m3[i][j] + p_m4[i][j] for j in range(n))
        for i in range(n)
    )


def legendre_four_moment_lower(L_mid_rows, L_error_rows, strict_parity=True):
    """Exact Loewner lower bound for E^* P^{-1} E = L_0^T L_0 + 3 L_1^T L_1 + 5 L_2^T L_2 + 7 L_3^T L_3
    from shifted-Legendre derivative moments L_{m,i} = <P_m(2t), h_i'(t)> (m=0..3).
    """
    L_mid = _matrix(L_mid_rows, rows=4)
    L_err = _matrix(L_error_rows, rows=4, cols=len(L_mid[0]))
    n = len(L_mid[0])
    odd_sector = tuple(i for i in range(n) if i % 2 == 0)
    even_sector = tuple(i for i in range(n) if i % 2 == 1)
    parts = (
        _sector_rank_one_lower(F(1), L_mid[0], L_err[0], odd_sector, n, strict_parity=strict_parity),
        _sector_rank_one_lower(F(3), L_mid[1], L_err[1], even_sector, n, strict_parity=strict_parity),
        _sector_rank_one_lower(F(5), L_mid[2], L_err[2], odd_sector, n, strict_parity=strict_parity),
        _sector_rank_one_lower(F(7), L_mid[3], L_err[3], even_sector, n, strict_parity=strict_parity),
    )
    return tuple(
        tuple(sum((p[i][j] for p in parts), F(0)) for j in range(n))
        for i in range(n)
    )


def hodge_legendre_endpoint_free_gram(m=4, radius=F(1, 2)):
    """Theorem L.1 (Hodge-Legendre Cochain Isomorphism for general m >= 2).

    On I=(-a,a), the polynomial space P_{<=m-1}(I) decomposes L^2-orthogonally as:
        P_{<=m-1}(I) = V(F_{m-2}) (+) span{L_{m-1}', L_m'},
    where phi_k(t) = (V L_k)(t) = int_{-a}^t P_k(s/a) ds = (a/(2k+1))(P_{k+1}(t/a) - P_{k-1}(t/a))
    for k=1..m-2 vanish at both endpoints +-a, and L_{m-1}', L_m' carry the boundary channels.

    The L^2(I) Gram matrix of {phi_1,...,phi_{m-2}} is identically the tridiagonal
    inverse-Neumann submatrix K_a^{[1..m-2]}:
        G_{jk} = <V L_j, V L_k> = <L_j, K_a L_k> = (K_a)_{jk}.
    At m=4, a=1/2: K_{1/2}^{[1..2]} = diag(1/30, 1/210), explaining the weights (30, 210).
    At m>=5, K_a^{[1..m-2]} is tridiagonal within each parity sector.
    """
    a = _f(radius)
    if type(m) is not int or not 2 <= m <= 12 or a <= 0:
        raise DualQuotientError("Integer m in 2..12 and positive exact radius required")
    dim = m - 2
    if dim == 0:
        return {
            "m": m, "radius": a, "endpoint_free_dim": 0,
            "K_gram": (), "K_inverse": (),
            "boundary_complement_norms_squared": (F(m * (m - 1)) / a, F(m * (m + 1)) / a),
            "RH_proved": False,
        }
    K_gram = []
    for j in range(1, dim + 1):
        row = []
        for k in range(1, dim + 1):
            if j == k:
                val = F(2) * (a ** 3) * (F(1, (2 * j - 1) * (2 * j + 1) ** 2)
                                         + F(1, (2 * j + 1) ** 2 * (2 * j + 3)))
            elif abs(j - k) == 2:
                s = min(j, k)
                val = -F(2) * (a ** 3) / F((2 * s + 1) * (2 * s + 3) * (2 * s + 5))
            else:
                val = F(0)
            row.append(val)
        K_gram.append(tuple(row))
    K_gram = tuple(K_gram)
    K_inv = _inverse(K_gram)
    return {
        "m": m,
        "radius": a,
        "endpoint_free_dim": dim,
        "K_gram": K_gram,
        "K_inverse": K_inv,
        "boundary_complement_norms_squared": (F(m * (m - 1)) / a, F(m * (m + 1)) / a),
        "orthogonality_to_boundary_complement_exact": True,
        "RH_proved": False,
    }


def general_endpoint_free_moment_lower(c_mid_rows, c_error_rows, radius=F(1, 2), strict_parity=True):
    """Generalization of PDQ-04b to arbitrary cut m >= 3:
    For d = m - 2 rows c_k,i = <P_k(t/a), h_i> (k=1..m-2), bounds
        C^T (K_a^{[1..m-2]})^{-1} C <= ||Pi_{<=m-1} h'||^2
    in Loewner order, isolated by parity sector.
    """
    C_mid = _matrix(c_mid_rows)
    d = len(C_mid)
    n = len(C_mid[0])
    C_err = _matrix(c_error_rows, rows=d, cols=n)
    if any(x < 0 for row in C_err for x in row):
        raise DualQuotientError("Nonnegative error bounds required")
    m = d + 2
    hodge = hodge_legendre_endpoint_free_gram(m=m, radius=radius)
    W = hodge["K_inverse"]
    if strict_parity:
        for k in range(d):
            for i in range(n):
                if (k - i) % 2 and (C_mid[k][i] != 0 or C_err[k][i] != 0):
                    raise DualQuotientError("Channel row violates reflection parity")
    mid_gram = _mul(_mul(_trans(C_mid), W), C_mid)
    out = [list(row) for row in mid_gram]
    for parity in (0, 1):
        ch_ix = tuple(k for k in range(d) if k % 2 == parity)
        col_ix = tuple(i for i in range(n) if i % 2 == parity) if strict_parity else tuple(range(n))
        if not ch_ix or not col_ix:
            continue
        r_s = F(0)
        for i in col_ix:
            row_rad = F(0)
            for j in col_ix:
                err_ij = F(0)
                for k in ch_ix:
                    for l in ch_ix:
                        w_kl = abs(W[k][l])
                        if not w_kl:
                            continue
                        err_ij += w_kl * (
                            abs(C_mid[k][i]) * C_err[l][j]
                            + C_err[k][i] * abs(C_mid[l][j])
                            + C_err[k][i] * C_err[l][j]
                        )
                row_rad += err_ij
            if row_rad > r_s:
                r_s = row_rad
        for i in col_ix:
            out[i][i] -= r_s
    return tuple(tuple(r) for r in out)


def observer_interior_boundary_synergy_certificate():
    """Theorem J.1: Strict Schur/distinguishability resolution gain from joining the
    interior low-Galerkin observer O_int(c_1, c_2) and the boundary observer O_bdry(E_0, E_1).

    Witness h(t) = P_3(2t) on (-1/2, 1/2):
      - h'(t) = 60 t^2 - 3, ||h'||_2^2 = 24.
      - O_int sees c_1 = <P_1(2t), P_3(2t)> = 0, c_2 = <P_2(2t), P_3(2t)> = 0 -> energy 0.
      - O_bdry(E_0) alone sees E_0 = h(1/2) - h(-1/2) = 2 -> energy E_0^2 = 4.
      - Joined observer O_int v O_bdry computes M_3 = 12(E_0 - 5 c_1) = 24 -> energy
        30 c_1^2 + M_3^2 / 24 = 0 + 576/24 = 24 = 100% of ||h'||_2^2!
      - The K-dual high residual drops from 24 (under O_int) to 0 (under O_int v O_bdry).
    """
    c_mid = ((F(0),), (F(0),))
    z_err = ((F(0),), (F(0),))
    m34_mid = ((F(24),), (F(0),))
    int_only = parity_isolated_two_moment_lower(c_mid, z_err)[0][0]
    bdry_E0_only = F(2) ** 2
    joined = complete_four_moment_lower(c_mid, z_err, m34_mid, z_err)[0][0]
    full_hprime_sq = F(24)
    return {
        "witness": "h(t) = P_3(2t) on (-1/2, 1/2)",
        "full_derivative_energy": full_hprime_sq,
        "interior_observer_c1_c2_energy": int_only,
        "boundary_observer_E0_only_energy": bdry_E0_only,
        "joined_observer_complete_4moment_energy": joined,
        "strict_synergy_over_sum_of_parts": joined > int_only + bdry_E0_only,
        "residual_under_interior_only": full_hprime_sq - int_only,
        "residual_under_joined_observer": full_hprime_sq - joined,
        "RH_proved": False,
    }


def cross_contact_gauge_no_ghost_countermodel():
    """Theorem J.2: Cross-contact-gauge stitching creates a false join (ghost positivity).

    For the contact operator K_{1/2} on (-1/2, 1/2) acting on u_1(t) = 2t:
      - (K_{1/2} u_1)'(t) = -(V u_1)(t) = 1/4 - t^2, ||(K_{1/2} u_1)'||_2^2 = 1/30.
      - True gauge (c=1): c_1 = 1/30, E_0 = 1/6, so M_3 = 12(E_0 - 5 c_1) = 0,
        and 30 c_1^2 + M_3^2/24 = 1/30 = ||h'||_2^2.
      - Cross-gauge stitching: if O_int reads c_1 = 1/30 from gauge c=1 while O_bdry
        reads E_0 = -1/6 from shifted gauge c=-1, then the stitched M_3_ghost = 12(-1/6 - 5/30) = -4,
        giving apparent projection energy 1/30 + 16/24 = 7/10 > 1/30 = ||h'||_2^2,
        violating Bessel's inequality and fabricating a negative residual -2/3!
    """
    true_hprime_sq = F(1, 30)
    c1_gauge1 = F(1, 30)
    E0_gauge1 = F(1, 6)
    E0_gauge_minus1 = -F(1, 6)
    M3_true = 12 * (E0_gauge1 - 5 * c1_gauge1)
    M3_ghost = 12 * (E0_gauge_minus1 - 5 * c1_gauge1)
    true_proj = 30 * c1_gauge1 ** 2 + F(1, 24) * M3_true ** 2
    ghost_proj = 30 * c1_gauge1 ** 2 + F(1, 24) * M3_ghost ** 2
    return {
        "true_derivative_energy": true_hprime_sq,
        "true_gauge_invariant_M3": M3_true,
        "true_projection_energy": true_proj,
        "stitched_cross_gauge_M3_ghost": M3_ghost,
        "stitched_ghost_projection_energy": ghost_proj,
        "violates_bessel_inequality": ghost_proj > true_hprime_sq,
        "forged_apparent_residual": true_hprime_sq - ghost_proj,
        "no_ghost_gluing_requires_shared_contact_gauge": True,
        "RH_proved": False,
    }


__all__=["DualQuotientError","polynomial_moment_gram",
         "derivative_moment_projection_gram","quotient_derivative_cap",
         "vanishing_boundary_moment_lower",
         "trace_primitive_polynomial_countermodel",
         "parity_isolated_two_moment_lower",
         "monomial_moments_from_mixed_rows",
         "legendre_moments_from_mixed_rows",
         "complete_four_moment_lower",
         "legendre_four_moment_lower",
         "hodge_legendre_endpoint_free_gram",
         "general_endpoint_free_moment_lower",
         "observer_interior_boundary_synergy_certificate",
         "cross_contact_gauge_no_ghost_countermodel"]

