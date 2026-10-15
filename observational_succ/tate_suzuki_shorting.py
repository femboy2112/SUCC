"""Tate–Suzuki source passport and zero-shift residual shorting laboratory.

Exact rational finite algebra is executable. Infinite-dimensional source theorems
are proved in research/2026-10-15/TATE_SUZUKI_ZERO_SHIFT.md; their hypotheses
are NOT manufactured by finite matrices. Original Weil all-test sign is OPEN.

The actual original-source adapter checks the pinned source_weil_hierarchy.py
Git blob before validating the genuine prime-power tape. This module is
stdlib-only and can run isolated finite synthetic tests without that adapter.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib


class ShortingContractError(ValueError):
    """Wrong source, unsupported domain, or invalid rational proof certificate."""


def rat(x):
    if type(x) not in (int, F):
        raise ShortingContractError("only exact int/Fraction mathematical data")
    return F(x)


def positive_integer(n, at_least=1):
    if type(n) is not int or n < at_least:
        raise ShortingContractError("positive integer source index required")
    return n


def is_genuine_prime(p):
    if type(p) is not int or p < 2:
        return False
    return all(p % d for d in range(2, isqrt(p) + 1))


def prime_power_parent(n):
    positive_integer(n, 2)
    if is_genuine_prime(n):
        return n
    for p in range(2, isqrt(n) + 1):
        if not is_genuine_prime(p):
            continue
        v = n
        while v % p == 0:
            v //= p
        if v == 1:
            return p
    return None


@dataclass(frozen=True)
class TateSourcePassport:
    """Only the ordinary Q/zeta completion; no hidden character/extra Γ."""
    source_id: str = "Q_AUTHENTIC_EULER_GAUSSIAN"
    epoch: int = 0
    half_density: F = F(1, 2)
    gaussian_scale: F = F(1)
    real_gamma_count: int = 1
    conductor: int = 1
    character_parity: int = 0
    trace_model_identified: bool = False

    def __post_init__(self):
        if self.source_id != "Q_AUTHENTIC_EULER_GAUSSIAN":
            raise ShortingContractError("incorrect original arithmetic source")
        if type(self.epoch) is not int or self.epoch != 0:
            raise ShortingContractError("source epoch mismatch")
        if type(self.half_density) is not F or self.half_density != F(1, 2):
            raise ShortingContractError("critical half-density normalization mismatch")
        if type(self.gaussian_scale) is not F or self.gaussian_scale != 1:
            raise ShortingContractError("Tate original self-dual Gaussian scale required")
        if type(self.real_gamma_count) is not int or self.real_gamma_count != 1:
            raise ShortingContractError("one global Archimedean Gamma factor required")
        if type(self.conductor) is not int or self.conductor != 1:
            raise ShortingContractError("conductor-1 ordinary zeta source required")
        if type(self.character_parity) is not int or self.character_parity != 0:
            raise ShortingContractError("wrong Dirichlet character parity")
        if self.trace_model_identified is not False:
            raise ShortingContractError("Connes/trace realization not identified")


PINNED_SOURCE_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
PINNED_TAPE = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2))


def verify_original_suzuki_source():
    """Check actual integrated SUCC module byte blob, and exact prime tape.

    Never silently substitutes a synthetic or identically-valued source.
    Runs in the real GitHub checkout; isolated overlay can test algebra only.
    """
    from . import source_weil_hierarchy as src
    raw = Path(src.__file__).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    if blob != PINNED_SOURCE_BLOB:
        raise ShortingContractError("SOURCE_BLOB_DRIFT: authentic source code changed")
    if src.AUTHENTIC_TAPE != PINNED_TAPE or src.assert_original_source_tape() is not True:
        raise ShortingContractError("genuine prime-power Euler source mismatch")
    if src.contact_iv().lo <= 0 or src.log2_iv().lo <= 0:
        raise ShortingContractError("source Gamma/contact normalization failed")
    return {"source_git_blob":blob,"prime_power_tape":PINNED_TAPE,
            "half_density":"1/2","real_gamma_count":1,
            "original_weil_sign_proved":False}


def true_prime_tape(N):
    positive_integer(N, 2)
    if N > 4096:
        raise ShortingContractError("local arithmetic demonstration budget N<=4096")
    return tuple((n, p) for n in range(2, N+1) if (p := prime_power_parent(n)) is not None)


def euler_p_shell(p, sigma, depth):
    """Tate Q_p unramified zeta at integer sigma>=2.

    Multiplicative Haar vol(Z_p^×)=1. Returns exact finite shell sum
    and exact *positive* omitted tail, with locally normalized p^{-k sigma}.
    Full Euler assembly ONLY licensed on Re s>1.
    """
    if not is_genuine_prime(p):
        raise ShortingContractError("not a genuine p-adic place")
    positive_integer(sigma, 2)
    if type(depth) is not int or not 0 <= depth <= 1000:
        raise ShortingContractError("finite p-adic shell depth required")
    t = F(1, p**sigma)
    return {"finite":sum((t**j for j in range(depth+1)), F()),
            "omitted":t**(depth+1)/(1-t),
            "exact_local_factor":1/(1-t), "source_prime":p}


def log_derivative_coefficient_tape(N, sigma=2):
    """Formal coefficient of log(p) in -zeta'/zeta(sigma) truncated at n<=N.
    No floating logs, no invented primitive composite source.
    """
    positive_integer(sigma, 2)
    out = {}
    for n,p in true_prime_tape(N):
        out[p] = out.get(p,F()) + F(1, n**sigma)
    return tuple(sorted(out.items()))


def gammas_from_prime_mutation(tape):
    """Fail-closed mutation guard before a Weil source may be claimed."""
    if tuple(tape) != PINNED_TAPE:
        raise ShortingContractError("source jet mutation: missing/extra/fake composite")
    return True


def first_window_derivative_l1_cap(a=F(1,2)):
    """PROVED ANALYTIC bound ||g'||_{L1(-1,1)} < 26 for true a=1/2.

    g is Suzuki (1.3), with pole, true prime-2 hinge, one completed
    contact and one gamma tower. This is a FORMULA certificate; a numeric
    source evaluation must separately pass verify_original_suzuki_source.
    """
    if type(a) is not F or a != F(1, 2):
        raise ShortingContractError("analytic L1 constant proved only for a=1/2")
    TateSourcePassport()
    return F(26)


def original_gamma_derivative_l1_tail(J):
    """PROVED L1 derivative tail bound on [-1,1] for true Gamma rungs.

    |(g_Gamma-g_Gamma,J)'|_L1 <= 8 sum_{j>=J} (4j+1)^-2
                                    <= 2/d + 8/d^2, d=4J+1.
    Positive scalar coefficient is exact Fraction (conservative).
    """
    positive_integer(J)
    d = 4*J+1
    return F(2,d) + F(8,d*d)


def original_gamma_kernel_l1_tail(J):
    """Same bound on ||g_gamma-g_gamma,J||_L1([-1,1])."""
    return original_gamma_derivative_l1_tail(J)


def integral_comparison_tail(J):
    """Exact two-sided bounds for sum 8/(4j+1)^2, j>=J.

    Integral comparison with decreasing f: integral_J^inf f <= sum_{j>=J} f
    <= f(J)+integral_J^inf f. The L1 Gamma bound is strictly below upper.
    """
    positive_integer(J)
    d=4*J+1
    return (F(2,d),F(2,d)+F(8,d*d))


def mat(A):
    if not isinstance(A,(list,tuple)) or not A:
        raise ShortingContractError("nonempty exact matrix required")
    try:
        rows=tuple(tuple(rat(x) for x in row) for row in A)
    except TypeError as e:
        raise ShortingContractError("bad matrix rows") from e
    if not rows or any(len(r) != len(rows[0]) for r in rows) or not rows[0]:
        raise ShortingContractError("nonempty rectangular exact matrix")
    return rows


def mt(A): return tuple(tuple(row[j] for row in A) for j in range(len(A[0])))

def mm(A,B):
    if len(A[0])!=len(B):
        raise ShortingContractError("incompatible matrix dimensions")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F()) for j in range(len(B[0]))) for i in range(len(A)))

def ma(A,B,scale=F(1)):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        raise ShortingContractError("matrix dimension mismatch")
    return tuple(tuple(A[i][j]+scale*B[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def scalar(A,s): return tuple(tuple(x*rat(s) for x in row) for row in A)

def symmetric(A): return len(A)==len(A[0]) and all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))

def ident(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))

def quadratic(A,x): return sum((x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),F())


def rational_inverse(A):
    A=mat(A)
    if not symmetric(A):
        raise ShortingContractError("exact symmetric inverse required")
    n=len(A); W=[list(A[i])+list(ident(n)[i]) for i in range(n)]
    for i in range(n):
        k=next((j for j in range(i,n) if W[j][i]),None)
        if k is None:
            raise ShortingContractError("source high metric is singular")
        W[i],W[k]=W[k],W[i]
        z=W[i][i]; W[i]=[v/z for v in W[i]]
        for j in range(n):
            if j==i:continue
            z=W[j][i]
            W[j]=[W[j][p]-z*W[i][p] for p in range(2*n)]
    return tuple(tuple(row[n:]) for row in W)


def rational_psd(A):
    """Exact semidefinite congruence, including zero pivots.

    Return (True,None) or (False, nonzero integer/rational witness x with
    x^T A x<0). No numerical eigensolvers and no positive pivot assumption.
    """
    A=mat(A)
    if not symmetric(A):
        raise ShortingContractError("PSD must be symmetric")
    n=len(A)
    B=[list(row) for row in A]
    T=[list(row) for row in ident(n)] # columns map current coords -> original
    for k in range(n):
        d=B[k][k]
        if d<0:
            w=tuple(T[i][k] for i in range(n))
            assert quadratic(A,w)<0
            return (False,w)
        if d==0:
            j=next((j for j in range(k+1,n) if B[k][j]!=0),None)
            if j is not None:
                # At zero diagonal, q(e_k + t e_j) = 2t B_kj+t²B_jj.
                a=B[k][j]; b=B[j][j]
                t=F(-1 if a>0 else 1, 1) * abs(a)/(abs(b)+2*abs(a)+1)
                w=tuple(T[i][k]+t*T[i][j] for i in range(n))
                assert quadratic(A,w)<0
                return (False,w)
            continue
        # Positive pivot: congruent Schur elimination on remaining variables.
        for j in range(k+1,n):
            coeff=B[k][j]/d
            if coeff:
                for i in range(n):T[i][j]-=coeff*T[i][k]
        for i in range(k+1,n):
            for j in range(i,n):
                B[i][j]-=B[i][k]*B[k][j]/d
                B[j][i]=B[i][j]
        for j in range(k+1,n):B[k][j]=B[j][k]=F()
    return (True,None)


@dataclass(frozen=True)
class ResidualSchurResult:
    """Finite rational theorem control, NOT automatically original Weil."""
    source_scope: str
    low_block: tuple
    trial_root_matrix: tuple
    residual_matrix: tuple
    conservative_schur_matrix: tuple
    semidefinite: bool
    witness: tuple | None
    original_weil_sign_proved: bool = False


def synthetic_residual_schur(A,B,D,K,kappa,Z,*,source_scope="SYNTHETIC_FINITE_MODEL"):
    """Exact rational finite analogue of true zero-shift theorem.

    A: low x low, B: low x high, D,K: high x high,
    Z: high x low finite trial map. D>=kappa K, K>0.
    Returns exact sufficient S = A-BZ-(BZ)^T+Z^T D Z - R^T K^-1 R/kappa,
    R=B^T-D Z. A positive S certifies the FINITE input block only.
    To use on G_zeta, construct authenticated source M and H1 residual
    derivative Gram and prove D>=kappa K_H (never deduce from this toy).
    """
    if source_scope != "SYNTHETIC_FINITE_MODEL":
        raise ShortingContractError("cannot self-authorize an original Weil certificate")
    A,B,D,K,Z=map(mat,(A,B,D,K,Z));k=rat(kappa)
    if k<=0:raise ShortingContractError("positive complement constant needed")
    m,n=len(A),len(D)
    if not symmetric(A) or not symmetric(D) or not symmetric(K) or len(K)!=n:
        raise ShortingContractError("symmetric source operator/metric required")
    if len(B)!=m or len(B[0])!=n or len(Z)!=n or len(Z[0])!=m:
        raise ShortingContractError("block or trial dimensions incompatible")
    if not rational_psd(ma(D,K,-k))[0]:
        raise ShortingContractError("D>=kappa K is an actual obligation")
    Kinv=rational_inverse(K)
    if not rational_psd(K)[0] or not rational_psd(Kinv)[0]:
        raise ShortingContractError("strictly positive source metric required")
    BZ=mm(B,Z)
    trial=ma(ma(ma(A,BZ,-1),mt(BZ),-1),mm(mt(Z),mm(D,Z)))
    residual=ma(mt(B),mm(D,Z),-1)
    upper=scalar(mm(mt(residual),mm(Kinv,residual)),1/k)
    schur=ma(trial,upper,-1)
    good,w=rational_psd(schur)
    return ResidualSchurResult(source_scope,A,trial,residual,schur,good,w)


def schur_hilbert_grid_lower(A,depth):
    """Exact finite-grid bound on q_A over [-1,1]^2.

    Grid resolution h=2^-depth, includes endpoints. Uses rational 
    operator bound max abs row sum and delta_2 <=sqrt(2)h (coarsely
    sqrt(2) replaced by 2). If min_grid>= L*4*h*(2+h), all cube PSD.
    This is a rational *coverage* proof, not an authentic Weil sign.
    """
    A=mat(A)
    if len(A)!=2 or not symmetric(A):
        raise ShortingContractError("only 2D Hilbert-grid mathematics")
    if type(depth) is not int or not 0<=depth<=8:
        raise ShortingContractError("dyadic grid budget 0..8")
    h=F(1,2**depth)
    pts=tuple(F(j,2**depth) for j in range(-2**depth,2**depth+1))
    mi=min(quadratic(A,(x,y)) for x in pts for y in pts)
    L=max(sum(abs(z) for z in row) for row in A)
    # Norm <=sqrt2*max |coord|; epsilon <=sqrt2*h.
    return {"grid_minimum":mi,"error_budget":L*2*h*(2+h),
            "global_lower":mi-L*2*h*(2+h),
            "all_square_nonnegative":mi-L*2*h*(2+h)>=0}


def source_legendre_30_projection_derivative_cap():
    """At a=1/2, ||(P_low f)'||_2 <= 961 ||f||_2.

    The exact squared Hilbert--Schmidt derivative bound is 922560,
    computed with normalized P_k(x/a) for k=1..30. In particular
    sqrt(922560) < 961, all rational/integer arithmetic.
    """
    square = sum(2*(2*k+1)*k*(k+1) for k in range(1,31))
    assert square == 922560 and square < 961*961
    return {"derivative_projection_HS_square":square,"integer_upper":961}


def actual_source_high_derivative_truncation(J):
    """||[(P_high(G-G_J) f)]'||_2 <= 962 E_J ||f||_2.

    Exact a=1/2, 30 genuine mean-zero Legendre low modes, G is
    Suzuki's full ORIGINAL g, G_J only genuine first J positive Gamma
    rungs, E_J = 2/d+8/d^2. This is a conservative sufficient bound.
    """
    first_window_derivative_l1_cap()
    projection=source_legendre_30_projection_derivative_cap()
    return F(1+projection['integer_upper'])*original_gamma_derivative_l1_tail(J)


def hilbert_xy(level,d):
    """Integer Hilbert-curve order of 2^level x 2^level dyadic address cells."""
    if type(level) is not int or not 1 <= level <= 8:
        raise ShortingContractError("Hilbert level 1..8")
    n=2**level
    if type(d) is not int or not 0 <= d < n*n:
        raise ShortingContractError("Hilbert ordinal outside grid")
    x=y=0; t=d; s=1
    while s<n:
        rx=1 & (t//2)
        ry=1 & (t^rx)
        if ry==0:
            if rx==1:
                x=s-1-x;y=s-1-y
            x,y=y,x
        x+=s*rx;y+=s*ry
        t//=4;s*=2
    return (x,y)


def hilbert_boundary_matrix_certificate(A,level=4):
    """Certified strict PD on two real coordinates via finite Hilbert order.

    Every ||x||_infinity=1 lies within h/2 in L2 of a boundary grid
    point, h=2/(2^level-1). For L=max row sum |A_ij|, the rational
    bound L*h*(2+h) is conservative for q_A differences. A positive
    certified boundary lower extends to q_A(x)>0 for every x!=0 by
    homogeneity. In all other cases status UNRESOLVED, NOT NEGATIVE.
    The 30-mode Weil application needs authentic low Schur entries first.
    """
    A=mat(A)
    if len(A)!=2 or not symmetric(A):
        raise ShortingContractError("2D real symmetric finite block required")
    if type(level) is not int or not 1<=level<=8:
        raise ShortingContractError("finite Hilbert traversal level 1..8")
    n=2**level
    seen=set();samples=[]
    for k in range(n*n):
        i,j=hilbert_xy(level,k)
        if i in (0,n-1) or j in (0,n-1):
            seen.add((i,j))
            x=F(-1)+F(2*i,n-1);y=F(-1)+F(2*j,n-1)
            samples.append(quadratic(A,(x,y)))
    assert len(samples)==4*(n-1) and len(seen)==len(samples)
    mi=min(samples)
    h=F(2,n-1)
    L=max(sum(abs(z) for z in row) for row in A)
    budget=L*h*(2+h)
    return {"sample_count":len(samples), "boundary_minimum":mi,
            "uniform_direction_error":budget,"certified_margin":mi-budget,
            "strictly_positive_definite":mi>budget,
            "interpretation":"PD if strict; otherwise UNRESOLVED"}


def authentic_suzuki_legendre_derivative_point(k, x, J, *, a=F(1,2)):
    """REAL ORIGINAL-SOURCE INTERVAL: (G_J P_k(x/a))'(x) at rational x.

    This is a *pointwise* signed source derivative, NOT an integral of the
    squared high residual, NOT a 30x30 shorted matrix and NOT an RH test.

    Exact polynomial--exponential convolution on [-a,a], with the ORIGINAL
    n=2 prime hinge, C_G contact, both signed poles and the first J real
    Gamma rungs. All transcendental quantities enclosed by source-pinned
    rational intervals, not a fitted mpmath oracle. The only permitted
    radius is a=1/2, 1<=k<=4, 1<=J<=20, x rational with |x|<a and
    no crossing of an uncertain prime activation boundary.
    """
    from . import suzuki_legendre_source as L
    source = L._pinned_source()
    verify_original_suzuki_source()
    if type(a) is not F or a!=F(1,2) or type(k) is not int or not 1<=k<=4:
        raise ShortingContractError("authenticated low Legendre k=1..4 at a=1/2 only")
    if type(J) is not int or not 1<=J<=20:
        raise ShortingContractError("source derivative J=1..20 budget")
    x=rat(x)
    if not -a<x<a:
        raise ShortingContractError("strict compact window interior required")
    poly=L.legendre_polynomial(k,a)
    primitive=L.poly_primitive_zero_at_left(poly,a)
    if L.poly_eval(primitive,a):
        raise ShortingContractError("original meanzero/source domain violation")
    # All arithmetic below retains exact rational ranges until the FINAL
    # source quantization to 32 digits, rather than rounding each canceled
    # polynomial exponential term separately.
    digits=90
    def constant(v):
        v=rat(v); return v,v
    def exp_minus(t):
        t=rat(t)
        if t>=0: return L.tight_exp_neg(t,digits)
        lo,hi=L.tight_exp_neg(-t,digits)
        return F(1,hi),F(1,lo)
    def sub(left,right):
        return L.interval_add(left,L.interval_scale(right,-1))
    def mul(left,right):
        return L.interval_mul(left,right)
    # Original completed two-pole signed source, not a replacement Γ.
    fp=L.exp_antiderivative_poly(poly,F(1,2),+1)
    fm=L.exp_antiderivative_poly(poly,F(1,2),-1)
    integral_plus=sub(mul(exp_minus(-a/2),constant(L.poly_eval(fp,a))),
                      mul(exp_minus(a/2),constant(L.poly_eval(fp,-a))))
    integral_minus=sub(mul(exp_minus(a/2),constant(L.poly_eval(fm,a))),
                       mul(exp_minus(-a/2),constant(L.poly_eval(fm,-a))))
    pole=L.interval_add(L.interval_scale(mul(exp_minus(-x/2),integral_minus),-2),
                        L.interval_scale(mul(exp_minus(x/2),integral_plus),2))
    # Exact original contact derivative: meanzero polynomial primitive.
    cg=source.contact_iv()
    contact=mul((cg.lo,cg.hi),constant(L.poly_eval(primitive,x)))
    # Genuine p=2 only: derivative hinge of (|x-y|-log2)_+.
    b=L.tight_log2(digits)
    srcb=source.log2_iv()
    if not (b[0]<=srcb.hi and srcb.lo<=b[1]):
        raise ShortingContractError("prime/arch log2 phase source disagreement")
    prim=constant(0)
    lower=(x-b[1],x-b[0])
    upper=(x+b[0],x+b[1])
    if lower[0]>=-a:
        prim=L.interval_add(prim,L.interval_poly_eval(primitive,lower))
    elif lower[1]>-a:
        raise ShortingContractError("uncertain left prime activation; refine x")
    if upper[1]<=a:
        prim=L.interval_add(prim,L.interval_poly_eval(primitive,upper))
    elif upper[0]<a:
        raise ShortingContractError("uncertain right prime activation; refine x")
    srcinv=source.sqrt_inverse(2)
    weight=mul(b,(srcinv.lo,srcinv.hi))
    prime=mul(weight,prim)
    # Real original Gamma ladder, differentiated from the authentic g_J.
    gamma=constant(0)
    for j in range(J):
        d=4*j+1;alpha=F(d,2)
        plus=L.exp_antiderivative_poly(poly,alpha,+1)
        minus=L.exp_antiderivative_poly(poly,alpha,-1)
        both=constant(L.poly_eval(plus,x)+L.poly_eval(minus,x))
        edge1=mul(exp_minus(alpha*(x+a)),constant(L.poly_eval(plus,-a)))
        edge2=mul(exp_minus(alpha*(a-x)),constant(L.poly_eval(minus,a)))
        single=L.interval_scale(sub(sub(both,edge1),edge2),F(-2,d))
        gamma=L.interval_add(gamma,single)
    total=L.interval_add(L.interval_add(pole,contact),L.interval_add(prime,gamma))
    return L.source_interval_round(source,total)


def original_first_prime_derivative_bv_bound(J):
    """True g_J'' is a signed finite measure on [-1,1].

    Its total variation has source-justified upper bound
    V_J=16+8 sum_{j<J}1/(4j+1); all terms include original poles,
    contact, genuine prime-2 atoms and genuine J Gamma rungs.
    """
    positive_integer(J)
    if J > 20:
        raise ShortingContractError("research g_J'' finite variation budget J<=20")
    return F(16)+F(8)*sum((F(1,4*j+1) for j in range(J)),F())


def genuine_low_legendre_sup_coarse(k):
    """Exact polynomial coefficient sup bound on [-1/2,1/2].

    P_k(2x) for k=1..4; sum |coeff_i| (1/2)^i is a sound
    rational L-infinity bound, does not assume a floating Legendre oracle.
    """
    if type(k) is not int or k not in (1,2,3,4):
        raise ShortingContractError("k=1..4 research first-prime Legendre bound")
    coefficients={1:(F(),F(2)),
                  2:(-F(1,2),F(),F(6)),
                  3:(F(),-F(3),F(),F(20)),
                  4:(F(3,8),F(),-F(15),F(),F(70))}[k]
    return sum((abs(c)*F(1,2)**i for i,c in enumerate(coefficients)),F())


def original_suzuki_legendre_derivative_energy(k,J,grid=8):
    """AUTHENTIC SOURCE exact rational energy enclosure, not sample-only.

    Finite J genuine signed ∫ |(G_J P_k)'|² dx on (-1/2,1/2)
    bounded via finite midpoint source INTERVALS plus a proved global
    Lipschitz constant V_J||P_k||_infinity for the derivative; the
    variation measure g_J'' includes correct contact/prime atoms.

    For untruncated true G, Gamma tail in W^{1,1} gives
      ||(G P_k)'||² <= 2*upper_J + 2*eta_J²/(2k+1),
    an exact source-derived, conservative Hilbert energy certificate.
    This is NOT yet ||(P_H G P_k)'||² (the Schur cross residual).
    """
    if type(grid) is not int or not 2 <= grid <= 64:
        raise ShortingContractError("finite first-prime quadrature grid 2..64")
    verify_original_suzuki_source()
    sup=genuine_low_legendre_sup_coarse(k)
    lip=original_first_prime_derivative_bv_bound(J)*sup
    h=F(1,grid)
    wiggle=lip*h/2
    lo_energy=F();hi_energy=F()
    for i in range(grid):
        x=-F(1,2)+F(2*i+1,2*grid)
        v=authentic_suzuki_legendre_derivative_point(k,x,J)
        low,high=v.lo-wiggle,v.hi+wiggle
        umax=max(abs(low),abs(high))
        if low>0:lmin=low
        elif high<0:lmin=-high
        else:lmin=F()
        lo_energy+=h*lmin*lmin
        hi_energy+=h*umax*umax
    eta=original_gamma_derivative_l1_tail(J)
    true_upper=2*hi_energy+F(2)*eta*eta/F(2*k+1)
    return {
        "source":"ACTUAL_ZETA_SUZUKI_G_J_FIRST_PRIME",
        "k":k,"J":J,"grid":grid,
        "derivative_Lipschitz_rational":lip,
        "finite_J_energy_lower":lo_energy,
        "finite_J_energy_upper":hi_energy,
        "infinite_true_G_derivative_energy_upper":true_upper,
        "true_high_projected_cross_energy_certified":False,
        "original_all_test_weil_positive":False,
    }
