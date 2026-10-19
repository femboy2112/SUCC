"""Original Suzuki P1 low/high residual alignment with TRUE prime2 surplus.

Zero nontrivial zeta zeros read. This is a SOURCE-CERTIFIED single original
low direction (P1), not an arbitrary or optimized surrogate residual.

The arithmetic improvement is:
  R_4(P1) <= ||g_1||²/kappa_odd
             - [w2/(kappa_odd*(kappa_odd+w2))] ||(g_1)_center||²,
  g_1=-Q_poly<=3 (G P1)'.
The source true b=log2>5/8 licenses C0=[-1/8,1/8].
A rigorous lower on ||g_1||_center² is 4|int_C0 g_1|²,
and the latter source moment is certified by:
  * analytic integration of ORIGINAL truncated pole+contact+Gamma derivative
    on C0 (the genuine prime term has ZERO direct support there);
  * original B3 differentiated Gamma tail with a strict L2 norm bound;
  * inherited COMPLETED original mixed derivative moment intervals L0,L2.
This proves a STRICT correction saving for actual P1 source if interval excludes 0.
An external arbitrary positive matrix, fake composite 6, or output of the
analytic integrator itself is never a source of the moment rows.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache


class SourceCenterError(ValueError):
    pass


def _compact_fraction(q,digits=16,side="lower"):
    q=F(q);scale=10**digits
    floor=q.numerator*scale//q.denominator
    return F(floor if side=="lower" else
             (q.numerator*scale+q.denominator-1)//q.denominator,scale)


def _source_eneg(x,digits=90):
    from . import suzuki_legendre_source as L
    from .source_weil_hierarchy import I
    x=F(x)
    if x>=0:
        lower,upper=L.tight_exp_neg(x,digits)
        return I(lower,upper)
    lower,upper=L.tight_exp_neg(-x,digits)
    return I(F(1,upper),F(1,lower))


def _original_finite_center_derivative_integral(k,J):
    """Exact analytic source interval for int_-1/8^1/8 (G_J P_k)' dx.

    Works for k=1 or 2, 1<=J<=128; prime2 absent on centered interval.
    All coefficients are ORIGINAL signed Suzuki formulas, not an invented
    exponential-polynomial source. Gamma is the TRUE first J OU ladder.
    """
    from . import suzuki_legendre_source as L
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .source_weil_hierarchy import I,log2_iv,contact_iv
    if type(k) is not int or k not in (1,2) or \
       type(J) is not int or not 1<=J<=128:
        raise SourceCenterError("genuine low mode k=1,2 and real Gamma J=1..128")
    source=verify_original_suzuki_source()
    a=F(1,2);s=F(1,8)
    b=log2_iv()
    if not b.lo>a+s or b.hi>=2*a:
        raise SourceCenterError("prime wavefront contaminates assumed central zero region")
    p=L.legendre_polynomial(k,a)
    v=L.poly_primitive_zero_at_left(p,a)
    if L.poly_eval(v,-a) or L.poly_eval(v,a):
        raise SourceCenterError("non-original boundary primitive")
    # ORIGINAL pole signs and orientation from certified_four_schur_trial.py:
    # -2 exp(+x/2) I_minus +2 exp(-x/2) I_plus.
    fp=L.exp_antiderivative_poly(p,F(1,2),+1)
    fm=L.exp_antiderivative_poly(p,F(1,2),-1)
    em=_source_eneg(a/2)
    ep=I(F(1),F(1))/em
    Iplus=ep*L.poly_eval(fp,a)-em*L.poly_eval(fp,-a)
    Iminus=em*L.poly_eval(fm,a)-ep*L.poly_eval(fm,-a)
    sh=_source_eneg(-s/2)-_source_eneg(s/2)
    pole=F(4)*sh*(Iplus-Iminus)
    C=contact_iv()
    contact=C*L.poly_integral(v,-s,s)
    gamma=I(F(0),F(0))
    for j in range(J):
        d=4*j+1
        alpha=F(d,2)
        plus=L.exp_antiderivative_poly(p,alpha,+1)
        minus=L.exp_antiderivative_poly(p,alpha,-1)
        bulk=L.poly_integral(L.poly_add(plus,minus),-s,s)
        # The true OU edge integrations are positive-lag DIFFERENCES:
        # exp(-alpha*a) int_-s^s exp(±alpha*x)dx
        # = [exp(-alpha*(a-s))-exp(-alpha*(a+s))]/alpha.
        edge=(_source_eneg(alpha*(a-s))-
              _source_eneg(alpha*(a+s)))/alpha
        gamma+=-F(2,d)*(I(F(bulk),F(bulk))-
                        edge*(L.poly_eval(plus,-a)+L.poly_eval(minus,a)))
    return pole+contact+gamma


def _original_B3_center_integral_tail(k,J):
    """Source-conditional B3 H1 Gamma tail, converted to center integral."""
    from . import suzuki_legendre_source as L
    from .certified_four_schur_trial import _sqrt_rat_upper,_sqrt_rat_lower
    if type(k) is not int or k not in (1,2) or \
       type(J) is not int or not 1<=J<=128:
        raise SourceCenterError("k in (1,2), 1<=J<=128 source bound")
    a=F(1,2);d=4*J+1
    p=L.legendre_polynomial(k,a)
    deriv=L.poly_derivative(p)
    derivative_norm2=L.poly_integral(L.poly_mul(deriv,deriv),-a,a)
    amplitude=abs(L.poly_eval(p,a))+abs(L.poly_eval(p,-a))
    sqrt_d_lo=_sqrt_rat_lower(F(d))
    t32=F(2,3)/(d*sqrt_d_lo)+F(4)/(d*d*sqrt_d_lo)
    t2=F(1,d*d)+F(8,d*d*d)
    tail=2*_sqrt_rat_upper(derivative_norm2)*t2+amplitude*t32
    # ||1_C0||_2=sqrt(1/4)=1/2 EXACT.
    return tail/F(2)


@lru_cache(maxsize=8)
def certified_true_P1_center_residual(J=64,J_G=64):
    """Return a RIGOROUS strict original P1 arithmetic Schur saving.

    If any original-source center interval contains zero, returns a zero
    strict-signal gate, NEVER inventing positivity or a numerical sign.
    """
    from .certified_four_schur_trial import CertifiedTrial
    from .authentic_prime_surplus import (
        original_prime_surplus_source_passport
    )
    from .source_weil_hierarchy import I
    if type(J_G) is not int or not 32<=J_G<=75:
        raise SourceCenterError("legitimate completed source Galerkin J_G 32..75")
    finite=_original_finite_center_derivative_integral(1,J)
    tail=_original_B3_center_integral_tail(1,J)
    actual_center=finite+I(-tail,tail)

    source=original_prime_surplus_source_passport()
    trial=CertifiedTrial((),J=J_G,rank=5)
    if trial.get("verdict")=="INVALID_SOURCE" or not trial.get("certified"):
        raise SourceCenterError("full original signed Suzuki mixed-moment source unavailable")
    means=trial["source_full_four_moment_L_mid"]
    errs=trial["source_full_four_moment_L_error"]
    L0=I(F(means[0][0])-F(errs[0][0]),
         F(means[0][0])+F(errs[0][0]))
    L2=I(F(means[2][0])-F(errs[2][0]),
         F(means[2][0])+F(errs[2][0]))
    # projection h' -> L0*P0 +5L2*P2; exact C0 integrals:
    # int_C0 P0=1/4, int_C0 P2=-15/128.
    moment=actual_center-F(1,4)*L0+F(75,128)*L2
    abs_lower=(moment.lo if moment.lo>0 else
               -moment.hi if moment.hi<0 else F(0))
    center_energy_lower=F(4)*abs_lower**2
    kappa=source["kappa_odd"]
    w=source["positive_source_weight_floor"]
    # true w2>=w implies B(w2)>=B(w) and the high inverse is <= B(w)^-1.
    original_arithmetic_dual_saving_lower=(
        w*center_energy_lower/(kappa*(kappa+w))
    )
    return {
        "source":"REAL_COMPLETED_SUZUKI_P1_ARITHMETIC_CENTER_RESIDUAL",
        "source_sha":source["source_sha"],
        "actual_p1_low_high_residual_not_model":True,
        "real_prime_tape":source["true_prime_power_label"],
        "finite_true_Gamma_modes":J,"completed_mixed_moment_Galerkin_J":J_G,
        "true_center_integral_interval":(
            _compact_fraction(actual_center.lo,16,"lower"),
            _compact_fraction(actual_center.hi,16,"upper")),
        "omitted_Gamma_center_integral_abs_upper":
            _compact_fraction(tail,16,"upper"),
        "true_P1_projected_residual_center_moment_interval":(
            _compact_fraction(moment.lo,16,"lower"),
            _compact_fraction(moment.hi,16,"upper")),
        "true_P1_abs_center_moment_certified_lower":abs_lower,
        "true_P1_center_energy_certified_lower":center_energy_lower,
        "true_P1_source_prime_dual_saving_lower":
            original_arithmetic_dual_saving_lower,
        "source_nonstrict_when_interval_hits_zero":abs_lower==0,
        "source_signed_S4_sign":"UNVERIFIED",
        "RH_proved":False,
    }
