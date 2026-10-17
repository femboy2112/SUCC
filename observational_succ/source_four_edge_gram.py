"""Source-exact two-edge mismatch moments of the ORIGINAL four Schur columns.

The true first-prime shift b=log2 in (1/2,1) induces two connected
edge intervals. For g_k=-Qpoly<=3 (G P_k)', the phase difference on
R=(b-1/2,1/2) is:
  odd derivative carrier k odd:  g_k(x)-g_k(b-x), antisymmetric,
  even derivative carrier k even: g_k(x)+g_k(b-x), symmetric.
Thus ORIGINAL edge mismatch weighted observations are exactly:
  k odd: m_k= 2 integral_R (x-b/2) Q(G P_k)'(x) dx,
  k even: m_k=2 integral_R Q(G P_k)'(x) dx.
The original finite Gamma source is piecewise exponential-polynomial,
integrated analytically with TRUE b intervals; omitted Gamma derivative
H1 and source-common contact scalar errors are added by Cauchy-Schwarz.

This is a SOURCE-CONDITIONAL lower Gram for true edge mismatch energy,
not a claim that the actual full high correction has been evaluated.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache

from .source_four_center_gram import (
    SourceCenterError,_out,_source_I,_make_interval,
    _rational_sqrt_upper,_rational_sqrt_lower,
)
from .authentic_prime_surplus import original_prime_surplus_source_passport
from .source_four_prime_schur import _parity_lower


def _eta_true_gamma_derivative(k,J):
    from . import suzuki_legendre_source as L
    if type(k) is not int or not 1<=k<=4 or type(J) is not int or not 1<=J<=20:
        raise SourceCenterError("genuine source low k=1..4 real Gamma J 1..20")
    a=F(1,2);d=4*J+1
    p=L.legendre_polynomial(k,a)
    derivative=L.poly_derivative(p)
    grad=L.poly_integral(L.poly_mul(derivative,derivative),-a,a)
    edges=abs(L.poly_eval(p,a))+abs(L.poly_eval(p,-a))
    root=_rational_sqrt_lower(F(d))
    return 2*_rational_sqrt_upper(grad)*(F(1,d*d)+F(8,d*d*d)) + \
           edges*(F(2,3)/(d*root)+F(4)/(d*d*root))


def _source_mixed_moments(trial):
    from .piecewise_suzuki_integrator import I
    means=trial["source_full_four_moment_L_mid"]
    errors=trial["source_full_four_moment_L_error"]
    return tuple(tuple(I(F(means[j][k])-F(errors[j][k]),
                         F(means[j][k])+F(errors[j][k]))
                       for k in range(4)) for j in range(4))


@lru_cache(maxsize=6)
def authentic_four_edge_moments(J=8,J_G=64,digits=100):
    """All 4 genuine original P1..P4 two-edge moment interval vectors."""
    from . import suzuki_legendre_source as L
    from .certified_four_schur_trial import CertifiedTrial
    from .piecewise_suzuki_integrator import (
        I,ExponentialPolynomial,authentic_mode_piecewise
    )
    if type(J) is not int or not 1<=J<=20 or \
       type(J_G) is not int or not 32<=J_G<=75 or \
       type(digits) is not int or not 40<=digits<=180:
        raise SourceCenterError("exact original source Gamma J<=20, source J_G<=75 and digits 40..180")
    src=original_prime_surplus_source_passport()
    trial=CertifiedTrial((),J=J_G,rank=5)
    if trial.get("verdict")=="INVALID_SOURCE" or not trial.get("certified"):
        raise SourceCenterError("original full mixed signed Suzuki source not certified")
    moments=_source_mixed_moments(trial)
    source_contact=L._pinned_source().contact_iv()
    common_contact_error=F(source_contact.hi-source_contact.lo,2)
    modes=tuple(authentic_mode_piecewise(k,J,digits=digits)
                for k in range(1,5))
    b=modes[0][2]
    if any(m[2]!=b for m in modes):
        raise ArithmeticError("genuine p2 phase source drift")
    source_log=src["log2_interval"]
    if not (b.lo<=source_log[1] and source_log[0]<=b.hi and
            F(1,2)<b.lo<b.hi<F(1)):
        raise SourceCenterError("genuine log2 source mismatch for 2-edge dual")
    length=I(F(1)-b.hi,F(1)-b.lo)
    if length.lo<=0:raise ArithmeticError("prime2 right edge vanished")
    low=b-F(1,2)
    hi=F(1,2)
    S=[]
    for k,(inactive,active,_) in enumerate(modes,start=1):
        weight=ExponentialPolynomial.polynomial(
            (-b/F(2),I.of(F(1))) if k%2 else (I.of(F(1)),)
        )
        projection=ExponentialPolynomial.polynomial((F(0),))
        for j in range(4):
            pj=L.legendre_polynomial(j,F(1,2))
            projection=projection+ExponentialPolynomial.polynomial(pj).scale(
                -(2*j+1)*moments[j][k-1]
            )
        G=active+projection
        integral=2*(G*weight).integrate(low,hi,digits=digits)
        norm_upper=(
            _rational_sqrt_upper(length.hi**3/F(12)) if k%2
            else _rational_sqrt_upper(length.hi)
        )
        primitive=L.poly_primitive_zero_at_left(
            L.legendre_polynomial(k,F(1,2)),F(1,2))
        primitive_norm2=L.poly_integral(L.poly_mul(primitive,primitive),
                                       -F(1,2),F(1,2))
        error=2*norm_upper*(
            _eta_true_gamma_derivative(k,J)
            +common_contact_error*_rational_sqrt_upper(primitive_norm2)
        )
        result=_make_interval(integral.lo-error,integral.hi+error)
        S.append(result)
    nominal=tuple(_out((v.lo+v.hi)/2) for v in S)
    errors=tuple(_out(max(abs(v.lo-nominal[i]),abs(v.hi-nominal[i])),
                      side="upper") for i,v in enumerate(S))
    for i in range(4):
        if not nominal[i]-errors[i]<=S[i].lo<=S[i].hi<=nominal[i]+errors[i]:
            raise ArithmeticError("unsound outward genuine prime edge residual interval")
    return {
        "source":"PINNED_TRUE_PRIME2_EDGE_FULL_FOUR_SOURCE_MISMATCH",
        "source_sha":src["source_sha"],"source_prime":src["true_prime_power_label"],
        "J":J,"J_G":J_G,
        "phase_interval":(b.lo,b.hi),
        "edge_width_interval":(length.lo,length.hi),
        "intervals":tuple((_out(v.lo,side="lower"),_out(v.hi,side="upper")) for v in S),
        "nominal":nominal,"errors":errors,
        "relevant_phase_antisymmetric_low_modes":(1,3),
        "relevant_phase_symmetric_low_modes":(2,4),
        "original_poles_contact_Gamma_and_true_p2":True,
        "true_signed_S4_sign":"UNVERIFIED","RH_proved":False,
    }


def phase_edge_energy_for_direction(cert,x):
    """Exact all-directions source mismatch Gram lower on true right edge.

    Lower =12/ell_hi³ * positive-part interval moment² for (P1,P3)
          +1/ell_hi * positive-part interval moment² for (P2,P4).
    """
    if not isinstance(x,(tuple,list)) or len(x)!=4 or \
       any(type(y) not in (int,F) for y in x):
        raise SourceCenterError("four exact rational low direction required")
    x=tuple(F(y) for y in x)
    e=cert["errors"];m=cert["nominal"];ell=cert["edge_width_interval"][1]
    ans=F(0)
    for sec,w in (((0,2),F(12)/ell**3),((1,3),F(1)/ell)):
        ctr=abs(sum((x[i]*m[i] for i in sec),F(0)))
        err=sum((abs(x[i])*e[i] for i in sec),F(0))
        ans+=w*max(F(0),ctr-err)**2
    return ans


def phase_edge_Young_gram_lower(cert,eta=F(1,8)):
    """Authenticated 4x4 source phase Gram lower; may be indefinite."""
    if type(eta) not in (int,F) or not 0<F(eta)<=1:
        raise SourceCenterError("rational Young eta in (0,1] required")
    eta=F(eta)
    # Important: all four J=8 source moment intervals can contain zero.
    # Their Cartesian product then includes the zero vector. No nonzero
    # POSITIVE semidefinite Loewner lower for a rank-one uncertainty Gram
    # can be justified from these observations alone. The exact ZERO
    # comparator is optimal in the PSD Loewner cone in this case; it
    # prevents error-only negative diagonals from worsening the S4 lower.
    if all(lo<=0<=hi for lo,hi in cert["intervals"]):
        return tuple(tuple(F(0) for _ in range(4)) for _ in range(4))
    ell=cert["edge_width_interval"][1]
    odd=_parity_lower((0,2),cert["nominal"],cert["errors"],
                      F(12)/ell**3,eta)
    even=_parity_lower((1,3),cert["nominal"],cert["errors"],
                       F(1)/ell,eta)
    return tuple(tuple(odd[i][j]+even[i][j] for j in range(4)) for i in range(4))
