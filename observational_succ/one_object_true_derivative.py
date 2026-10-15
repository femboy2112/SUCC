"""Direct authentic Suzuki finite-J first-Legendre derivative response.

The WHOLE ORIGINAL signed g_J (true prime-powers/Gamma/poles/contact and
infinite-contact original scheme) is integrated analytically, not fitted.

Let a=1/2, u1(y)=y/a=2y. F(x)=int_-a^a g_J(x-y)u1(y)dy.
By integration by parts in y, since g_J is continuous Lipschitz even:
    F'(x) = a^-1 int_(x-a)^(x+a)g_J(t)dt
            -g_J(x-a)-g_J(x+a).
The signed primitive of g_J is computed from analytic original source
pole/prime/contact/Gamma antiderivatives with Fraction outward intervals.
|F'(x)-F'(y)| <= 4 L_J |x-y|, L_J the original-source
explicit Lipschitz upper. Grid-node enclosures plus +/-2L_J*h
yield rigorous squared L2 derivative energy interval of TRUE G_Ju1.

IMPORTANT: this is F=G_J u1 BEFORE the Q30 high projection, not the
required T_(B-DY)'! The source adapter explicitly refuses that promotion.
The missing original 30-mode projection is a separate analytic task.
"""
from __future__ import annotations
from fractions import Fraction as Q
from . import source_weil_hierarchy as source

class DerivativeSourceError(ValueError):pass

def rat(x):
    if type(x) not in (int,Q):
        raise DerivativeSourceError("exact true-source rational parameter required")
    return Q(x)

def original_screw_primitive_positive(R,J):
    """Outward ∫0^R g_J(t)dt from original signed source, no samples."""
    R=rat(R)
    if not 0<=R<=1 or type(J) is not int or not 1<=J<=12:
        raise DerivativeSourceError("original a=1/2 first-prime source window")
    source.assert_original_source_tape()
    E=source.exp_pos(R/2)
    Em=source.exp_neg(R/2)
    pole=-8*(E-1)+8*(Em-1)+8*R
    contact=source.contact_iv()*R*R/4
    prime=source.iv(0)
    for n,p in source.authenticated_prime_wavefront(Q(1,2)):
        logn=source.log_iv(n)
        weight=source.log_iv(p)*source.sqrt_inverse(n)
        t=source.positive_part_interval(source.iv(R)-logn)
        prime+=weight*t*t/2
    gamma=source.iv(0)
    for j in range(J):
        d=4*j+1
        alpha=Q(d,2)
        inner=R-Q(2,d)*(1-source.exp_neg(alpha*R))
        gamma+=-Q(4,d*d)*inner
    return pole+contact+prime+gamma

def original_screw_signed_primitive(x,J):
    """Odd primitive of even g_J, continuous through zero."""
    x=rat(x)
    if not -1<=x<=1:raise DerivativeSourceError("source primitive domain")
    if x>=0:return original_screw_primitive_positive(x,J)
    return -original_screw_primitive_positive(-x,J)

def genuine_first_legendre_derivative_at(x,J):
    """Original F'=a^-1 Δprimitive - original boundary g; interval rigorous."""
    x=rat(x)
    a=Q(1,2)
    if not -a<=x<=a or type(J) is not int or not 1<=J<=12:
        raise DerivativeSourceError("genuine first-window test value")
    int_source=original_screw_signed_primitive(x+a,J)-original_screw_signed_primitive(x-a,J)
    return int_source/a - source.screw_interval(abs(x-a),J) - source.screw_interval(abs(x+a),J)

def _square_nonnegative_bounds(enclosure):
    lo,hi=enclosure.lo,enclosure.hi
    if lo<=0<=hi:return Q(),max(lo*lo,hi*hi)
    return min(lo*lo,hi*hi),max(lo*lo,hi*hi)

def original_first_legendre_H1_energy(J,gridN=64):
    """Rational certified ||(G_J P1(2x))'||² over [-1/2,1/2].

    One exact source interval per derivative sample. The only x-quadrature
    uncertainty is the independently PROVED |F''|<=4L_J Lipschitz law.
    Bound is two-sided and mathematically legitimate even if conservative.
    """
    if type(gridN) is not int or not 2<=gridN<=512:
        raise DerivativeSourceError("bounded finite rational source grid")
    if type(J) is not int or not 1<=J<=12:
        raise DerivativeSourceError("finite true Γ modes 1..12")
    a=Q(1,2)
    h=2*a/gridN
    L=source.lipschitz_safe(a,J)
    spread=2*L*h
    low=Q();high=Q()
    max_node=Q()
    for i in range(gridN):
        x=-a+(Q(2*i+1,2))*h
        raw=genuine_first_legendre_derivative_at(x,J)
        xval=source.I(raw.lo-spread,raw.hi+spread)
        a0,a1=_square_nonnegative_bounds(xval)
        low+=h*a0;high+=h*a1
        max_node=max(max_node,abs(raw.lo),abs(raw.hi))
    if not 0<=low<=high:
        raise ArithmeticError("source signed derivative L2 energy interval invalid")
    return {
      "source":"GENUINE_FIRST_WINDOW_SUZUKI_SIGNED_FINITEJ",
      "source_gamma_scheme":"INFINITE_CONTACT_FINITE_GAMMA",
      "a":a,"Legendre_mode":1,"original_true_prime_powers":source.authenticated_prime_wavefront(a),
      "original_Gamma_modes":J,
      "grid_cells":gridN,
      "source_lipschitz_g":L,
      "first_legendre_derivative_Lipschitz":4*L,
      "source_node_variation_upper":spread,
      "unprojected_GJ_P1_derivative_L2_squared_lower":low,
      "unprojected_GJ_P1_derivative_L2_squared_upper":high,
      "unprojected_GJ_P1_derivative_abs_center_upper":max_node,
      "source_partial_low_derivative_gram_computed":True,
      "genuine_30_mode_Q_projection_done":False,
      "original_residual_DY_included":False,
      "full_original_Suzuki_infinite_Gamma_included":False,
      "RH_proved":False,
    }
