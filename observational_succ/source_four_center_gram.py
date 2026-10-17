"""Full four-column source-attested first-prime central Schur residual.

The canonical original signed Suzuki source, not an auxiliary covariance:
 g_k=-Q_poly<=3 (G P_k(2x))', k=1..4; Q projects derivative response
 off the four actual polynomial moments.

On C0=[-1/8,1/8] the original prime-2 derivative vanishes since
 the actual source log2>5/8. Integrate finite-J ORIGINAL poles, contact,
 Gamma OU analytically against 1 or x; attach the inherited analytic B3
 omitted-Gamma derivative L2 tail; subtract the independent ORIGINAL
 completed mixed derivative Legendre moments from CertifiedTrial.

One true center functional survives in each derivative parity sector:
  ell0(g_1), ell0(g_3)    (primitive even / odd derivative)
  ell1(g_2), ell1(g_4)    (primitive odd / even derivative).
Bessel on the real prime2 center gives rank-two PSD source form:
  T_center >=4 c_even*c_even^* +768 c_odd*c_odd^*
in quadratic-form sense. It is NOT an identity of the entire center Gram.

Interval vectors cannot support a nonzero universally PSD rank-one matrix
lower bound without a fixed direction: emit a conservative spectral Loewner
lower and separately an EXACT direction-wise nonlinear robust lower.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as F

from .source_prime_center_alignment import (
    SourceCenterError, _source_eneg,
)
from .authentic_prime_surplus import original_prime_surplus_source_passport


def _source_I(v):
    from .source_weil_hierarchy import I
    v=F(v)
    return I(v,v)


def _precheck(k,J,t):
    if type(k) is not int or not 1<=k<=4 or \
       type(J) is not int or not 1<=J<=128 or \
       type(t) is not int or t not in (0,1):
        raise SourceCenterError("original k=1..4, gamma J=1..128, center weight t=0,1")


@lru_cache(maxsize=128)
def _exp_center_integral(rate,t):
    """Exact outward source interval for int_C0 x^t exp(rate*x) dx."""
    _precheck(1,1,t)
    from .source_weil_hierarchy import I
    rate=F(rate)
    s=F(1,8)
    if rate==0:
        return _source_I(2*s if t==0 else 0)
    plus=_source_eneg(-rate*s)
    minus=_source_eneg(rate*s)
    if t==0:
        return (plus-minus)/rate
    return s*(plus+minus)/rate - (plus-minus)/(rate*rate)


@lru_cache(maxsize=500)
def _real_gamma_center_edges(d,t):
    """True finite rung edge moments with decaying original-domain exponents.

    Returns ∫x^t exp[-alpha*(x+a)] and ∫x^t exp[-alpha*(a-x)]
    on C0; alpha=d/2, a=1/2; avoids any growing-exponential interval.
    """
    from .source_weil_hierarchy import I
    if type(d) is not int or d<1 or d%4!=1 or d>509 or t not in (0,1):
        raise SourceCenterError("actual Gamma rung d=4j+1 <=509")
    alpha=F(d,2);s=F(1,8);a=F(1,2)
    near=_source_eneg(alpha*(a-s))
    far=_source_eneg(alpha*(a+s))
    if t==0:
        z=(near-far)/alpha
        return z,z
    left=-s*(near+far)/alpha + (near-far)/(alpha*alpha)
    return left,-left


def _poly_moment(poly,t):
    from .suzuki_legendre_source import poly_integral,poly_mul
    return poly_integral(poly_mul(poly,(F(1),) if t==0 else (F(0),F(1))),
                         -F(1,8),F(1,8))


@lru_cache(maxsize=32)
def authentic_four_mode_finite_center_moment(k,J=64,t=None):
    """True ORIGINAL ∫C0 x^t (G_J P_k)' with ONLY original source atoms."""
    from . import suzuki_legendre_source as L
    from .source_weil_hierarchy import contact_iv,log2_iv,I
    from .tate_suzuki_shorting import verify_original_suzuki_source
    if t is None:t=0 if k%2 else 1
    _precheck(k,J,t)
    verify_original_suzuki_source()
    b=log2_iv()
    if b.lo <= F(5,8) or b.hi>=1:
        raise SourceCenterError("genuine log2 prime edge not proven disjoint from C0")
    # A reflection-forced zero must remain EXACTLY zero, not an interval.
    if (k+t)%2==0:
        return I(F(0),F(0))
    a=F(1,2)
    p=L.legendre_polynomial(k,a)
    primitive=L.poly_primitive_zero_at_left(p,a)
    if L.poly_eval(primitive,-a) or L.poly_eval(primitive,a):
        raise SourceCenterError("invalid original mean-zero source primitive")
    fp=L.exp_antiderivative_poly(p,F(1,2),+1)
    fm=L.exp_antiderivative_poly(p,F(1,2),-1)
    em=_source_eneg(a/F(2))
    ep=_source_I(1)/em
    Iplus=ep*L.poly_eval(fp,a)-em*L.poly_eval(fp,-a)
    Iminus=em*L.poly_eval(fm,a)-ep*L.poly_eval(fm,-a)
    pole= -2*Iminus*_exp_center_integral(F(1,2),t) + \
            2*Iplus*_exp_center_integral(F(-1,2),t)
    contact=contact_iv()*_poly_moment(primitive,t)
    gamma=I(F(0),F(0))
    for j in range(J):
        d=4*j+1
        alpha=F(d,2)
        plus=L.exp_antiderivative_poly(p,alpha,+1)
        minus=L.exp_antiderivative_poly(p,alpha,-1)
        bulk=_poly_moment(L.poly_add(plus,minus),t)
        left,right=_real_gamma_center_edges(d,t)
        gamma += -F(2,d)*(
            _source_I(bulk)
            -L.poly_eval(plus,-a)*left
            -L.poly_eval(minus,a)*right
        )
    return pole+contact+gamma


def _rational_sqrt_upper(x):
    from .certified_four_schur_trial import _sqrt_rat_upper
    return _sqrt_rat_upper(F(x))


def _rational_sqrt_lower(x):
    from .certified_four_schur_trial import _sqrt_rat_lower
    return _sqrt_rat_lower(F(x))


def B3_weighted_center_tail_upper(k,J,t):
    """Original Γ differentiated L2 norm bound times actual center test norm.

    J<=128 is a theorem-level OU-series bound; original pointwise oracle
    J<=20 runtime guard does not determine the analytic series domain.
    """
    from . import suzuki_legendre_source as L
    _precheck(k,J,t)
    a=F(1,2)
    p=L.legendre_polynomial(k,a)
    deriv=L.poly_derivative(p)
    deriv_sq=L.poly_integral(L.poly_mul(deriv,deriv),-a,a)
    e=abs(L.poly_eval(p,a))+abs(L.poly_eval(p,-a))
    d=4*J+1
    rootd=_rational_sqrt_lower(F(d))
    tail32=F(2,3)/(d*rootd)+F(4)/(d*d*rootd)
    tail2=F(1,d*d)+F(8,d*d*d)
    norm=2*_rational_sqrt_upper(deriv_sq)*tail2+e*tail32
    moment_norm2=(F(1,4) if t==0 else F(1,768))
    return norm*_rational_sqrt_upper(moment_norm2)


def _out(v,digits=18,side="lower"):
    if type(v) not in (int,F):raise SourceCenterError("exact output only")
    v=F(v);q=10**digits
    a=v.numerator*q//v.denominator
    if side=="upper" and F(a,q)<v:a+=1
    return F(a,q)


def _make_interval(lo,hi):
    from .source_weil_hierarchy import I
    return I(F(lo),F(hi))


@lru_cache(maxsize=8)
def authentic_four_center_certificate(J=64,J_G=64):
    """All four true G low-mode central projected residual moment INTERVALS."""
    from . import suzuki_legendre_source as L
    from .certified_four_schur_trial import CertifiedTrial
    _precheck(1,J,0)
    if type(J_G) is not int or not 32<=J_G<=75:
        raise SourceCenterError("source-completed mixed moments require J_G 32..75")
    src=original_prime_surplus_source_passport()
    base=CertifiedTrial((),J=J_G,rank=5)
    if base.get("verdict")=="INVALID_SOURCE" or not base.get("certified"):
        raise SourceCenterError("untrusted original signed Weil mixed moment packet")
    m=base["source_full_four_moment_L_mid"]
    err=base["source_full_four_moment_L_error"]
    source_L=tuple(tuple(_make_interval(F(m[row][col])-F(err[row][col]),
                                       F(m[row][col])+F(err[row][col]))
                         for col in range(4)) for row in range(4))
    center_basis=tuple(
        tuple(_poly_moment(L.legendre_polynomial(q,F(1,2)),t) for q in range(4))
        for t in (0,1)
    )
    center_intervals=[]
    for k in range(1,5):
        t=0 if k%2 else 1
        finite=authentic_four_mode_finite_center_moment(k,J,t)
        tail=B3_weighted_center_tail_upper(k,J,t)
        total=finite+_make_interval(-tail,tail)
        projection=sum(((2*q+1)*center_basis[t][q]*source_L[q][k-1]
                        for q in range(4)),_source_I(0))
        projected=total-projection
        center_intervals.append(projected)
    odd=(0,2);even=(1,3)
    # Source-parity double-check: exact mathematical support, not numerical.
    nominal=tuple(_out((z.lo+z.hi)/2) for z in center_intervals)
    errors=tuple(_out(max(z.hi-m,zlo) if False else
                    max(z.hi-(z.lo+z.hi)/2,(z.lo+z.hi)/2-z.lo),side="upper")
                 for z in center_intervals)
    # Quantities above are outward-rounded diagnostics; contain the entire
    # original true moment interval by increasing eps by the midpoint shift.
    eps=tuple(max(abs(center_intervals[i].lo-nominal[i]),
                  abs(center_intervals[i].hi-nominal[i])) for i in range(4))
    eps=tuple(_out(x,side="upper") for x in eps)
    for i in range(4):
        if center_intervals[i].lo<nominal[i]-eps[i] or \
           center_intervals[i].hi>nominal[i]+eps[i]:
            raise ArithmeticError("center source moment not in rational enclosure")
    # Exact C0 Bessel source Gram LOWER (may be indefinite due to intervals).
    values=tuple(nominal)
    weights={odd:F(4),even:F(768)}
    loewner=[[F(0)]*4 for _ in range(4)]
    midpoint=[[F(0)]*4 for _ in range(4)]
    widths={}
    for sec,weight in weights.items():
        for i in sec:
            for j in sec:
                midpoint[i][j]=weight*values[i]*values[j]
        r=max(sum((weight*(abs(values[i])*eps[j]+eps[i]*abs(values[j])+eps[i]*eps[j])
                   for j in sec),F(0)) for i in sec)
        widths["odd" if sec==odd else "even"]=r
        for i in sec:
            for j in sec:
                loewner[i][j]=midpoint[i][j]-(r if i==j else 0)
    p1=center_intervals[0]
    p1min=(p1.lo if p1.lo>0 else -p1.hi if p1.hi<0 else F(0))
    from .source_prime_center_alignment import certified_true_P1_center_residual
    independently=certified_true_P1_center_residual(J=J,J_G=J_G)
    check=independently["true_P1_projected_residual_center_moment_interval"]
    if p1.lo>check[1] or p1.hi<check[0]:
        raise ArithmeticError("independent original P1 analytic center cert disagree")
    return {
        "source":"AUTHENTIC_ORIGINAL_COMPLETED_SUZUKI_FOUR_CENTER_MOMENTS",
        "source_sha":src["source_sha"],"source_prime":src["true_prime_power_label"],
        "J":J,"J_G":J_G,
        "intervals":tuple((_out(z.lo,side="lower"),_out(z.hi,side="upper"))
                          for z in center_intervals),
        "nominal":values,"errors":eps,
        "center_rigorous_Gram_Loewner_lower":tuple(tuple(row) for row in loewner),
        "center_nominal_ranktwo_Gram":tuple(tuple(row) for row in midpoint),
        "center_Loewner_error_radii_by_parity":widths,
        "original_p1_replay_agrees":True,
        "actual_p1_abs_center_integral_lower":p1min,
        "actual_p1_center_energy_lower":F(4)*p1min**2,
        "source_signed_S4_sign":"UNVERIFIED","RH_proved":False,
    }


def robust_center_energy_for_direction(c,x):
    """Exact all-x source lower on center residual Gram, not a matrix fit.

    For any *real* four-vector x, true center residual squared norm >=
      4 max(0,abs(sum_i x_i nominal_i)-sum_i |x_i| eps_i)^2 [odd]
    +768 max(0,abs(sum_i x_i nominal_i)-sum_i |x_i| eps_i)^2 [even].
    No matrix sign is invented and the off-diagonal correlations are retained.
    """
    x=tuple(F(y) for y in x)
    if len(x)!=4:raise SourceCenterError("exact four-dimensional direction required")
    m=c["nominal"];e=c["errors"]
    ans=F(0)
    for sec,w in (((0,2),F(4)),((1,3),F(768))):
        center=abs(sum((x[i]*m[i] for i in sec),F(0)))
        uncertainty=sum((abs(x[i])*e[i] for i in sec),F(0))
        gap=max(F(0),center-uncertainty)
        ans+=w*gap*gap
    return ans
