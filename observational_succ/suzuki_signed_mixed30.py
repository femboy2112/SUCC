"""Original zeta finite-J signed Suzuki: FULL 30x30 dual derivative moments.

On true a=1/2, u_i(x)=P_i(2x), F_i=G_J u_i, the REAL-SOURCE matrix
  M_(j,i)=<(G_J u_i)',u_j'>_L2
has the integration-by-parts identity
  M_(j,i)=[F_i u_j']_-a^a -<F_i,u_j''>.
Boundary values and constant pairing are EXACTLY sourced from one-dimensional
integrals of the same signed original g_J:
  F_i(a)= ∫_0^1 g_J(t) P_i(1-2t) dt;
  <F_i,1>=-2∫_0^1 g_J(t) [∫_0^t P_i(1-2s)ds] dt  (i even).
All other <F_i,u_k> are the SHA-pinned genuine suzuki_legendre_source
analytic low entries (prime2, one Gamma, pole, infinite-contact, half-density).

Every polynomial integral uses source-correct outward rational exp/log/
sqrt/gamma enclosures, NOT zero coordinates or auxiliary PSD kernels.

This module computes the complete 30x30 M at FINITE J. This alone is
NOT T_ij=<(G_J u_i)',(G_J u_j)'>, NOT a high response Y, and NOT RH.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from dataclasses import dataclass

from .suzuki_neumann_dual_gauge import legendre_derivative_metric, inverse_derivative_metric, q

class OriginalMixedGaugeError(ValueError):pass

def polynomial_integral(poly,power=0):
    if type(power) is not int or not 0<=power<=2:
        raise OriginalMixedGaugeError("original test polynomial power 0..2")
    if type(poly) is not tuple or len(poly)>35 or not poly:
        raise OriginalMixedGaugeError("finite integer-coefficient polynomial required")
    return sum((q(v)/F(k+power+1) for k,v in enumerate(poly)),F()) if power==0 else sum(
        (q(v)/F(k+power+1) for k,v in enumerate(poly)),F())

@lru_cache(maxsize=34,typed=True)
def shifted_legendre(n):
    """EXACT P_n(1-2t) source test, n<=30, Legendre recurrence."""
    from . import suzuki_legendre_source as L
    if type(n) is not int or not 0<=n<=30:
        raise OriginalMixedGaugeError("original Legendre n<=30")
    a,b=(F(1),),(F(1),F(-2))
    if n==0:return a
    if n==1:return b
    for k in range(1,n):
        a,b=b,L.poly_add(
            L.poly_scale(L.poly_mul(b,(F(1),F(-2))),F(2*k+1,k+1)),
            a,-F(k,k+1))
    if polynomial_integral(b) !=0:
        raise ArithmeticError("shifted Legendre source zero-mean drift")
    return b

@lru_cache(maxsize=128,typed=True)
def exponential_moments(lam,degree=32):
    """Certify ∫0^1 t^k exp(lam*t)dt simultaneously to degree k<=32.

    Source exponential from suzuki_legendre_source.tight_exp_neg
    uses directed exact Fraction Taylor/geometric remainder, at 190 digits.
    Recurrence from integration by parts is an analytic exact identity.
    """
    from . import suzuki_legendre_source as L
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    lam=q(lam)
    if type(degree) is not int or not 0<=degree<=34 or not -256<=lam<=F(1,2):
        raise OriginalMixedGaugeError("valid true Γ/Arch polynomial moments")
    if lam==0:
        return tuple(src.iv(F(1,k+1)) for k in range(degree+1))
    if lam<0:lo,hi=L.tight_exp_neg(-lam,digits=190)
    else:
        lo,hi=L.tight_exp_neg(lam,digits=190)
        lo,hi=F(1,hi),F(1,lo)
    E=src.I(lo,hi)
    v=(E-1)/lam
    moments=[v]
    for k in range(1,degree+1):
        v=(E-k*v)/lam
        moments.append(v)
    return tuple(moments)

@lru_cache(maxsize=2048,typed=True)
def polynomial_exp_integral(poly,lam):
    """Outward authentic ∫ poly(t)*exp(lam*t) dt, no floating source."""
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    if type(poly) is not tuple or not poly or len(poly)>35:
        raise OriginalMixedGaugeError("exact finite source polynomial")
    if any(type(c) not in (int,F) for c in poly):
        raise OriginalMixedGaugeError("fake floating source coefficient")
    moments=exponential_moments(q(lam),len(poly)-1)
    return sum((q(c)*moments[k] for k,c in enumerate(poly)),src.iv(0))

@lru_cache(maxsize=256,typed=True)
def original_prime2_hinge_integral(poly):
    """Rational outgoing source enclosure for ∫_log2^1 (t-log2)poly(t)dt."""
    from . import suzuki_legendre_source as L
    src=L._pinned_source()
    lo,hi=L.tight_log2(digits=190)
    old=src.log2_iv()
    if lo>old.hi or hi<old.lo:
        raise OriginalMixedGaugeError("different prime clocks disagreed")
    if not F(0)<lo<=hi<F(1):
        raise OriginalMixedGaugeError("real original log(2) not enclosed in (0,1)")
    # For the monomial t^k, the exact positive hinge integral is
    #
    #   H_k(b) = 1/(k+2) - b/(k+1)
    #            + b**(k+2)/((k+1)*(k+2)).
    #
    # H'_k(b)=-(1-b**(k+1))/(k+1) < 0 for 0<b<1.
    # Thus its TRUE enclosure is [H_k(hi),H_k(lo)], retaining the
    # correlation between both occurrences of the SAME original log2.
    # Work with exact 190-digit rational endpoints throughout rather
    # than exponentiating src.I (which has no __pow__) or rounding each
    # enormous shifted-Legendre coefficient to the 32-digit source grid.
    def hinge_monomial(k,b):
        return (F(1,k+2)-b/F(k+1)
                +b**(k+2)/F((k+1)*(k+2)))
    lower=F()
    upper=F()
    for k,c in enumerate(poly):
        v=q(c)
        if not v:
            continue
        term_lo=hinge_monomial(k,hi)
        term_hi=hinge_monomial(k,lo)
        if term_lo>term_hi:
            raise ArithmeticError("original source prime hinge lost monotonicity")
        if v>0:
            lower+=v*term_lo
            upper+=v*term_hi
        else:
            lower+=v*term_hi
            upper+=v*term_lo
    return src.I(lower,upper)

@lru_cache(maxsize=512,typed=True)
def signed_source_poly_moment(poly,J):
    """True original ∫0^1 g_J(t)poly(t)dt, sign never altered."""
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    if type(J) is not int or not 1<=J<=64:
        raise OriginalMixedGaugeError("true finite Γ source stage J<=64")
    if type(poly) is not tuple or not poly or len(poly)>35:
        raise OriginalMixedGaugeError("finite original polynomial input")
    src.assert_original_source_tape()
    mass=polynomial_integral(poly)
    pm=polynomial_exp_integral(poly,F(1,2))
    mm=polynomial_exp_integral(poly,-F(1,2))
    pole=-4*(pm+mm-2*mass)
    contact=src.contact_iv()*polynomial_integral(poly,1)/2
    b=src.log2_iv()
    w=b*src.sqrt_inverse(2)
    prime=w*original_prime2_hinge_integral(poly)
    gamma=src.iv(0)
    for j in range(J):
        d=4*j+1
        gamma-=F(4,d*d)*(mass-polynomial_exp_integral(poly,-F(d,2)))
    return pole+contact+prime+gamma

@lru_cache(maxsize=80,typed=True)
def original_boundary_F(i,J):
    """TRUE F_i(+1/2)=∫0^1 g_J(t)P_i(1-2t)dt."""
    if type(i) is not int or not 1<=i<=30:
        raise OriginalMixedGaugeError("original P_i i<=30")
    return signed_source_poly_moment(shifted_legendre(i),J)

@lru_cache(maxsize=80,typed=True)
def original_G_constant_channel(i,J):
    """TRUE ∫_-1/2^1/2 (G_J P_i)(x)dx; for odd i exactly zero."""
    from . import suzuki_legendre_source as L
    src=L._pinned_source()
    if type(i) is not int or not 1<=i<=30:
        raise OriginalMixedGaugeError("original low source label")
    if i%2:return src.iv(0)
    pi=shifted_legendre(i)
    qpoly=(F(),)+tuple(q(v)/F(k+1) for k,v in enumerate(pi))
    if polynomial_integral(pi)!=0 or sum(qpoly)!=0:
        raise ArithmeticError("source shifted Legendre primitive boundary")
    return -2*signed_source_poly_moment(qpoly,J)

@lru_cache(maxsize=480,typed=True)
def original_signed_low_pair(i,k,J):
    """Original SHA-pinned full SIGNED low Legendre pair, no source forgery."""
    from . import suzuki_legendre_source as L
    if type(i) is not int or type(k) is not int or not (1<=i<=30 and 1<=k<=30):
        raise OriginalMixedGaugeError("low source basis P1..P30")
    if (i+k)%2:return L._pinned_source().iv(0)
    return L.authentic_full_low_entry(i,k,a=F(1,2),J=J)

@lru_cache(maxsize=31,typed=True)
def original_second_derivative_expansion(j):
    """u_j''=sum_k c_(j,k) u_k, EXACT, including possible constant u0."""
    from . import suzuki_legendre_source as L
    if type(j) is not int or not 1<=j<=30:
        raise OriginalMixedGaugeError("original second derivative mode 1..30")
    a=F(1,2)
    source=L.legendre_polynomial(j,a)
    dd=L.poly_derivative(L.poly_derivative(source))
    terms=[]
    recovered=(F(),)
    for k in range(j-1):
        if (j+k)%2:continue
        P=L.legendre_polynomial(k,a)
        norm=F(2*a,2*k+1)
        coeff=L.poly_integral(L.poly_mul(dd,P),-a,a)/norm
        if coeff:
            terms.append((k,coeff))
            recovered=L.poly_add(recovered,L.poly_scale(P,coeff))
    if L.poly_add(recovered,dd,-1)!=(F(),):
        raise ArithmeticError("signed derivative polynomial projection incomplete")
    return tuple(terms)

@dataclass(frozen=True)
class GenuineMixedMoments:
    source:str
    J:int
    rank:int
    low_modes:tuple
    matrix_intervals:tuple
    original_source_blob:str
    odd_even_parity_separated:bool=True
    original_finite_Gamma_infinite_contact:bool=True
    original_full_infinite_Gamma_done:bool=False
    high_response_Y_calculated:bool=False
    true_pure_H1_derivative_Gram_done:bool=False
    low_shorted_sign_proved:bool=False
    rh_proved:bool=False

@lru_cache(maxsize=8,typed=True)
def original_mixed_derivative_gram(J,rank=30,low_modes=None):
    """Entire source M_(j,i)=<u_j',(G_Ju_i)'>, dimension rank×len(low_modes).

    Rank30 / modes1..30 is the FULL original signed source mixed H1
    moment map, not yet the pure derivative Gram nor its Schur PSD.
    """
    from . import suzuki_legendre_source as L
    if type(rank) is not int or not 1<=rank<=30:
        raise OriginalMixedGaugeError("full Legendre dual rank<=30")
    if low_modes is None:low_modes=tuple(range(1,rank+1))
    if type(low_modes) is not tuple or not low_modes or len(set(low_modes))!=len(low_modes):
        raise OriginalMixedGaugeError("distinct original low source modes")
    if any(type(i) is not int or not 1<=i<=30 for i in low_modes):
        raise OriginalMixedGaugeError("source low modes from original 30")
    src=L._pinned_source()
    a=F(1,2)
    matrix=[]
    boundary={i:original_boundary_F(i,J) for i in low_modes}
    constant={i:original_G_constant_channel(i,J) if i%2==0 else src.iv(0)
              for i in low_modes}
    for j in range(1,rank+1):
        row=[]
        expansion=original_second_derivative_expansion(j)
        for i in low_modes:
            if (i+j)%2:
                row.append(src.iv(0))
                continue
            value=F(j*(j+1),1)/a*boundary[i]
            for k,coeff in expansion:
                term=constant[i] if k==0 else original_signed_low_pair(k,i,J)
                value-=coeff*term
            row.append(value)
        matrix.append(tuple(row))
    return GenuineMixedMoments(
       source="AUTHENTIC_Q_ZETA_SUZUKI_G_J_TRUE_LOWHIGH_DERIVATIVE",
       J=J,rank=rank,low_modes=low_modes,matrix_intervals=tuple(matrix),
       original_source_blob="0cc8510b71d178fc79e8d410a86d8b6014cf9178")

def _square_interval(v):
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    if v.lo<=0<=v.hi:return src.I(F(),max(v.lo*v.lo,v.hi*v.hi))
    return src.I(min(v.lo*v.lo,v.hi*v.hi),max(v.lo*v.lo,v.hi*v.hi))

def projected_gauge_diag_energy(moments:GenuineMixedMoments):
    """Source-authentic lower/upper of M*H^-1M diagonal via sum SQUARES.

    Finite rank30 H inverse uses original Brownian min-kernel parity
    first differences. No interval negative cancellation: each square
    is positive independently. For a=1/2 H^-1=a Δ*diag(delta^-1)Δ.
    """
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    if type(moments) is not GenuineMixedMoments or not moments.source.startswith("AUTHENTIC_Q_ZETA_SUZUKI"):
        raise OriginalMixedGaugeError("exact true source mixed moment type")
    if moments.rank!=30 or any(len(row)!=len(moments.low_modes) for row in moments.matrix_intervals):
        raise OriginalMixedGaugeError("full 30-dimensional genuine derivative basis only")
    if (moments.J<1 or moments.original_source_blob!="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
        or any(type(r) is not tuple or any(
            type(v) is not src.I or type(v.lo) is not F or type(v.hi) is not F
            for v in r) for r in moments.matrix_intervals)):
        raise OriginalMixedGaugeError("original source/coordinate/interval types drift")
    if moments!=original_mixed_derivative_gram(moments.J,30,moments.low_modes):
        raise OriginalMixedGaugeError("forged source moments or projection matrix")
    out=[]
    for col in range(len(moments.low_modes)):
        total=src.iv(0)
        for first in (1,2):
            rows=list(range(first,31,2))
            last_q=0
            last_m=src.iv(0)
            for mode in rows:
                quantum=mode*(mode+1)
                delta=quantum-last_q
                current=moments.matrix_intervals[mode-1][col]
                total+=F(1,2)/delta*_square_interval(current-last_m)
                last_m=current;last_q=quantum
        out.append((total.lo,total.hi))
    return tuple(out)
