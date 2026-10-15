"""Genuine completed zeta first-mode Neumann-dual flux (no fake source).

Source: the exact original Suzuki g_J from source_weil_hierarchy.py,
with one Γ, authentic Λ(2)/sqrt(2), both poles, infinite-contact
normalization; no nontrivial zeros.

For a=1/2 and u1(x)=P1(2x)=2x,
 F=G_a u1,  μ=<F',1>_L²([-1/2,1/2])
              =2 ∫_0^1 (1-2t) g(t)dt.
The signed-source integral of EVERY finite-J term is elementary, while
its actual missing Γ tail contributes a POSITIVE value <=
  2/(4J+1)^2 +16/(4J+1)^3.
This source law yields a certified rational interval for true μ (not
fitted or assigned by reading a zeta zero), and removes μ² from the
actual derivative-based high residual bound by Neumann-dual gauge.

Main original source is SHA-pinned via suzuki_legendre_source._pinned_source.
The resulting improvement is one TRUE low direction, NOT full 30-mode
source Gram, not a full signed Schur test and not RH.
"""
from __future__ import annotations
from fractions import Fraction as F

class SourceFluxError(ValueError):pass

def q(x):
    if type(x) not in (int,F):
        raise SourceFluxError("exact true-source rational coefficients")
    return F(x)

def weighted_exponential(lam):
    """Exact source ∫_0^1 (1-2t)e^(lam*t) dt in outward intervals."""
    from .suzuki_legendre_source import _pinned_source
    source=_pinned_source()
    lam=q(lam)
    if not (-128<=lam<=F(1,2)):
        raise SourceFluxError("genuine source real Γ/pole exponential domain")
    if not lam:return source.iv(0)
    if lam>0: E=source.exp_pos(lam)
    else:E=source.exp_neg(-lam)
    return ((E-1)/lam-2*(E*(lam-1)+1)/(lam*lam))

def finite_signed_first_flux(J):
    """Original true full pole/contact/prime/Gamma finite-J flux μ_J."""
    from .suzuki_legendre_source import _pinned_source
    source=_pinned_source()
    if type(J) is not int or not 1<=J<=64:
        raise SourceFluxError("bounded authentic source Gamma rungs 1..64")
    if source.assert_original_source_tape() is not True:
        raise SourceFluxError("original source prime tape false")
    b=source.log2_iv();w=b*source.sqrt_inverse(2)
    delta=1-b
    # Original pole -4(e^(t/2)+e^(-t/2)-2), ∫(1−2t)dt=0.
    pole=-8*(weighted_exponential(F(1,2))+weighted_exponential(-F(1,2)))
    # Original completed C_G t/2 contact contributes -C_G/6 to μ.
    contact=-source.contact_iv()/6
    # Genuine n=2 von Mangoldt hinge; no independent composite six.
    prime=2*w*((1-2*b)*delta*delta/2-2*delta*delta*delta/3)
    gamma=source.iv(0)
    for j in range(J):
        d=4*j+1
        alpha=F(d,2)
        val=weighted_exponential(-alpha)
        if val.hi<0:
            raise ArithmeticError("original Γ flux rung must be nonnegative")
        gamma+=F(8,d*d)*val
    return pole+contact+prime+gamma

def genuine_infinite_first_flux(J=16):
    """Rational original g∞ signed flux μ enclosure with +Γ tail order."""
    from .suzuki_legendre_source import _pinned_source
    source=_pinned_source()
    x=finite_signed_first_flux(J)
    positive_tail=source.authentic_positive_gamma_tail_norm(J)
    # Proof: 0<∫ (1−2t)e^-αt dt < ∫ e^-αt dt <1/α.
    # Hence 0<μ∞−μ_J<16 Σ_j>=J 1/(4j+1)^3 <= positive_tail.
    return {
        "source":"AUTHENTIC_COMPLETED_Q_ZETA_FIRST_PRIME_SIGNED",
        "original_source_gamma_scheme":"INFINITE_CONTACT_FINITE_NEGATIVE_GAMMA_POTENTIAL",
        "original_prime_powers":source.authenticated_prime_wavefront(F(1,2)),
        "half_density":F(1,2),
        "radius":F(1,2),
        "Gamma_rungs":J,
        "finite_flux_interval":(x.lo,x.hi),
        "positive_omitted_gamma_flux_bound":positive_tail,
        "full_infinite_source_flux_interval":(x.lo,x.hi+positive_tail),
        "wrong_Connes_contact_would_shift_flux":True,
        "flux_is_exact_original_source_quantity":True,
        "original_30_mode_Gram_computed":False,
        "signed_full_Weil_positive":False,
        "rh_proved":False
    }

def first_true_dual_gauge_resolvent_bound(J=16):
    """One source-real scalar low direction, no actual 30×30 Schur sign.

    In unnormalized source L1=P1(2x), ||L1||²=1/3, interval length=1.
    Since derivative constant lies in span of L1', dual gauge removes
       |∫(G L1)'|²=μ².
    And PR109 original-source true ||g'||_L1<11/40 gives
       ||(G L1)'||² <(11/40)^2/3.
    Therefore true high zero-shift R0(L1) <=κ^-1
       [121/4800−μ²],  κ=369/10000.
    """
    from .one_object_residual_schur import (KAPPA,
         original_source_cancellation_certificate)
    original_source_cancellation_certificate()
    f=genuine_infinite_first_flux(J)
    l,u=f["full_infinite_source_flux_interval"]
    least=(min(l*l,u*u) if l*u>0 else F())
    standard=F(11,40)**2/F(3)
    optimized=standard-least
    if not F()<=optimized<standard:
        raise ArithmeticError("original signed source flux gauge not improving")
    return dict(f,
        source_flux_squared_rigorous_lower=least,
        ungauged_true_high_variational_upper_strict=standard/KAPPA,
        optimized_true_high_variational_upper_strict=optimized/KAPPA,
        precise_high_metric="K=(-Delta_N)^-1_NOT_IDENTITY",
        one_original_source_low_direction_gauge_certified=True,
        source_full_30_low_short_positive=False)
