"""Projector-FIRST rational Schur instruments, with explicit analytic/source gates.

Three levels never conflated:
  (1) EXACT: finite piecewise-constant L2 polynomial quotient Gram;
  (2) CONDITIONAL: error theorem if given *proved* pointwise Lipschitz and
      omitted source derivative L2 column tail bounds;
  (3) UNVERIFIED: all-radius positivity or source-operator identification.

No L2 projector is differentiated; in general ||(Qh)'|| > ||h'||.
No Hilbert positivity is transported to the completed signed Weil form.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import isqrt


class DirectQuotientError(ValueError):
    """Invalid exact input, domain, or unproved transport."""


def _rat(x):
    if type(x) not in (int,F):
        raise DirectQuotientError("exact integers/Fractions only; bool and float invalid")
    return F(x)


def _matrix(rows, *, square=False):
    try:
        rows=tuple(tuple(_rat(x) for x in row) for row in rows)
    except (TypeError, ValueError) as exc:
        raise DirectQuotientError("rectangular rational matrix required") from exc
    if not rows or not rows[0] or any(len(row)!=len(rows[0]) for row in rows):
        raise DirectQuotientError("nonempty rational matrix required")
    if square and len(rows)!=len(rows[0]):
        raise DirectQuotientError("square matrix required")
    return rows


def _t(A): return tuple(zip(*A))
def _mul(A,B): return tuple(tuple(sum((v*w for v,w in zip(row,col)),F(0)) for col in _t(B)) for row in A)
def _sub(A,B): return tuple(tuple(a-b for a,b in zip(row,s)) for row,s in zip(A,B))
def _add(A,B): return tuple(tuple(a+b for a,b in zip(row,s)) for row,s in zip(A,B))
def _scale(A,c): return tuple(tuple(c*v for v in row) for row in A)


def _det(M):
    M=[list(r) for r in M]; n=len(M); d=F(1)
    for j in range(n):
        k=next((k for k in range(j,n) if M[k][j]),None)
        if k is None: return F(0)
        if k!=j: M[k],M[j]=M[j],M[k];d=-d
        t=M[j][j];d*=t
        for i in range(j+1,n):
            factor=M[i][j]/t
            for z in range(j+1,n): M[i][z]-=factor*M[j][z]
            M[i][j]=F(0)
    return d


def _inverse(M):
    M=_matrix(M,square=True);n=len(M)
    A=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None: raise DirectQuotientError("singular matrix")
        A[k],A[j]=A[j],A[k]
        p=A[j][j]; A[j]=[t/p for t in A[j]]
        for i in range(n):
            if i!=j:
                x=A[i][j];A[i]=[a-x*b for a,b in zip(A[i],A[j])]
    return tuple(tuple(row[n:]) for row in A)


def _sym(M): return all(M[i][j]==M[j][i] for i in range(len(M)) for j in range(len(M)))


def exact_psd(M):
    """All-principal-minors rational PSD test, for matrices <= 8."""
    M=_matrix(M,square=True);n=len(M)
    if n>8 or not _sym(M): raise DirectQuotientError("symmetric matrix <=8 required")
    for k in range(1,n+1):
        for ids in combinations(range(n),k):
            if _det(tuple(tuple(M[i][j] for j in ids) for i in ids)) < 0:
                return False
    return True


def exact_pd(M):
    """Sylvester leading-minors rational PD test, for symmetric matrices <=8."""
    M=_matrix(M,square=True);n=len(M)
    return n<=8 and _sym(M) and all(_det(tuple(tuple(M[i][j] for j in range(k)) for i in range(k)))>0 for k in range(1,n+1))


def _sqrt_upper(x, digits=12):
    x=_rat(x)
    if x<0: raise DirectQuotientError("cannot bound square root of negative energy")
    if type(digits) is not int or not 2<=digits<=30: raise DirectQuotientError("sqrt digits 2..30")
    scaled=(x.numerator*10**(2*digits)+x.denominator-1)//x.denominator
    v=isqrt(scaled)
    if v*v<scaled: v+=1
    return F(v,10**digits)


def _monomial_gram(radius, degree):
    a=_rat(radius)
    if a<=0 or type(degree) is not int or not 0<=degree<=6:
        raise DirectQuotientError("positive rational radius and polynomial degree 0..6")
    return tuple(tuple((a**(i+j+1)-(-a)**(i+j+1))/F(i+j+1) for j in range(degree+1)) for i in range(degree+1))


def projected_step_gram(values, *, radius=F(1,2), degree=3):
    """Exact T_step* (I-P_{polynomial<=degree}) T_step.

    values[cell][column] is a rational piecewise-constant VALUE on the
    equally-spaced partition of (-radius,radius); not point approximations.
    The subtraction is computed exactly BEFORE taking any error bound.
    """
    V=_matrix(values)
    a=_rat(radius); n=len(V); p=len(V[0]);h=2*a/n
    if n<2: raise DirectQuotientError("at least two cells required")
    if p>8: raise DirectQuotientError("at most eight columns")
    gram=_monomial_gram(a,degree)
    mom=tuple(tuple(sum((V[cell][i]*((-a+(cell+1)*h)**(k+1)-(-a+cell*h)**(k+1))/F(k+1) for cell in range(n)),F(0)) for i in range(p)) for k in range(degree+1))
    full=tuple(tuple(sum((h*V[cell][i]*V[cell][j] for cell in range(n)),F(0)) for j in range(p)) for i in range(p))
    projected=_sub(full,_mul(_mul(_t(mom),_inverse(gram)),mom))
    if not exact_psd(projected):
        raise ArithmeticError("exact polynomial projection produced non-PSD Gram")
    return {"projected_gram":projected,"unprojected_gram":full,"moments":mom,
            "polynomial_gram":gram,"cells":n,"degree":degree}


def certified_projector_first_upper(positive_source_intervals, lipschitz, omitted_tail,
                                    *, eta=F(1,4), radius=F(1,2)):
    """Conditional, anisotropic Loewner upper for Q T, where Q=I-P_<=3.

    Positive-half cells only. Source must prove parity of derivative column i:
       f_i(-t)=(-1)**i * f_i(t),  i=0,1,2,3.
    True truncated f_J has point interval at each positive cell midpoint
    and a VALID column Lipschitz L_i. Omitted source derivative error must
    obey ||f_i - f_{J,i}||_2 <= omitted_tail[i]. This routine CANNOT prove
    those analytic premises by itself. A midpoint piecewise-constant proxy is
    projected EXACTLY, and its total L2 error bounded before Young.

    In each parity block, E*E <= diag(e_i * sum_{j in block} e_j), a more
    informative comparison than (sum e_i^2) I for unbalanced errors.
    """
    try:
        pts=tuple(tuple(tuple(_rat(z) for z in iv) for iv in row) for row in positive_source_intervals)
    except (TypeError,ValueError) as exc: raise DirectQuotientError("exact interval rows required") from exc
    if not pts or any(len(row)!=4 or any(len(iv)!=2 or iv[0]>iv[1] for iv in row) for row in pts):
        raise DirectQuotientError("positive-half rows must have 4 ordered interval columns")
    L=tuple(_rat(x) for x in lipschitz)
    tail=tuple(_rat(x) for x in omitted_tail)
    if len(L)!=4 or len(tail)!=4 or any(x<0 for x in L+tail):
        raise DirectQuotientError("4 nonnegative Lipschitz and source-tail upper bounds required")
    eta=_rat(eta);a=_rat(radius)
    if eta<=0 or a<=0: raise DirectQuotientError("positive exact Young eta and radius required")
    cells=2*len(pts);h=2*a/cells
    # Reconstruct negative side using parity. The positive-only input must
    # originate from a source whose reflection covariance has been proved.
    values=[[F(0)]*4 for _ in range(cells)]
    radius_at=[[F(0)]*4 for _ in range(cells)]
    for k,row in enumerate(pts):
        for j,iv in enumerate(row):
            center=(iv[0]+iv[1])/2;rad=(iv[1]-iv[0])/2
            values[cells//2+k][j]=center
            radius_at[cells//2+k][j]=rad
            values[cells//2-1-k][j]=center if j%2==0 else -center
            radius_at[cells//2-1-k][j]=rad
    G=projected_step_gram(values,radius=a,degree=3)["projected_gram"]
    if any(G[i][j] for i in range(4) for j in range(4) if (i-j)%2):
        raise ArithmeticError("reflected source approximation violates parity")
    er2=[]
    for j in range(4):
        bound=sum((h*radius_at[k][j]**2 + radius_at[k][j]*L[j]*h*h/2
                   +L[j]**2*h**3/12 for k in range(cells)),F(0))
        er2.append(bound)
    er=tuple(_sqrt_upper(x)+tail[j] for j,x in enumerate(er2))
    bound_diag=[F(0)]*4
    for group in ((0,2),(1,3)):
        total=sum((er[j] for j in group),F(0))
        for j in group: bound_diag[j]=er[j]*total
    top=tuple(tuple((1+eta)*G[i][j] + ((1+1/eta)*bound_diag[i] if i==j else F(0)) for j in range(4)) for i in range(4))
    if not exact_psd(top): raise ArithmeticError("upper must be PSD")
    return {"quotient_proxy_gram":G,"error_squared_cell_bounds":tuple(er2),
            "error_l2_column_upper":er,"error_gram_operator_diagonal_upper":tuple(bound_diag),
            "quotient_loewner_upper":top,"young_eta":eta,"grid":cells,
            "analytic_premises_authenticated":False,"original_signed_schur_sign":"UNVERIFIED", "RH_proved":False}


def exact_finite_operator_schur(A,B,D,C,U):
    """Finite exact anisotropic residual theorem, CONDITIONAL analog for Suzuki.

    D>=C>0, where C may include source-JUSTIFIED rank-one coercivity upgrades.
    Low A n*n; B high*n; high D,C h*h; response U high*n.
    Returns A-L_U-r* C^-1 r <= A-B*D^-1B <= A-L_U.
    The model NEVER asserts that D,C represent the genuine infinite Suzuki
    operator. Finite PD does not imply first-window positivity.
    """
    A=_matrix(A,square=True);D=_matrix(D,square=True);C=_matrix(C,square=True)
    B=_matrix(B);U=_matrix(U)
    n=len(A);h=len(D)
    if len(B)!=h or len(B[0])!=n or len(U)!=h or len(U[0])!=n:
        raise DirectQuotientError("low/high response shape mismatch")
    if not _sym(A) or not _sym(D) or not _sym(C) or not exact_pd(C) or not exact_psd(_sub(D,C)):
        raise DirectQuotientError("D>=C>0 must be proved, not assumed")
    residual=_sub(B,_mul(D,U))
    # L=U*B+B*U-U*D*U
    L=_sub(_add(_mul(_t(U),B),_mul(_t(B),U)),_mul(_t(U),_mul(D,U)))
    upper=_sub(A,L)
    lower=_sub(upper,_mul(_t(residual),_mul(_inverse(C),residual)))
    actual=_sub(A,_mul(_t(B),_mul(_inverse(D),B)))
    if not exact_psd(_sub(actual,lower)) or not exact_psd(_sub(upper,actual)):
        raise ArithmeticError("finite Schur enclosure failed")
    return {"lower":lower,"upper":upper,"actual":actual,
            "source_D_minus_C_psd":True,"lower_positive":exact_psd(lower),
            "actual_positive":exact_psd(actual),"original_source_identified":False,
            "RH_proved":False}


def rank_one_coercivity_gain(K, coupling, *, kappa=F(1,50), delta=F(1,2)):
    """Exact Woodbury improvement for C=kappa K+delta z z*. Source gate: D>=C.

    Returns the PSD residual-correction saved relative to (kappa K)^-1.
    No claim that a genuine Suzuki D dominates this C until independently proved.
    """
    K=_matrix(K,square=True); z=tuple(_rat(v) for v in coupling)
    kappa=_rat(kappa);delta=_rat(delta)
    if kappa<=0 or delta<0 or len(z)!=len(K) or not exact_pd(K):
        raise DirectQuotientError("positive K, kappa and nonnegative exact delta required")
    inv=_inverse(K)
    q=sum((z[i]*inv[i][j]*z[j] for i in range(len(z)) for j in range(len(z))),F(0))
    gain=delta/(kappa*(kappa+delta*q))
    return {"gain_coefficient":gain,"K_dual_z_norm2":q,
            "strict_gain_when_coupled":delta>0 and bool(q),
            "source_D_ge_comparator_proved":False,"RH_proved":False}
