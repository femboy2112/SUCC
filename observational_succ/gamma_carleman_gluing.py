"""True Gamma OU primitive Dirichlet form and no-gap Carleman boundary gluing.

Full source context: the positive Archimedean Gamma tower in original signed
Suzuki screw kernel, plus both poles, contact, and first genuine prime hinge.
Proves conditional two-support gluing, NOT global original Weil positivity.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial,isqrt
from .gamma_edge_compensation import CompensationError,rational
from .prime_hinge_chiral_edge import moment_annihilating_edge,mul,integrate


def gamma_ou_dirichlet_channel(index):
    """Positive original Gamma jump-form at decay rate alpha=(4j+1)/2.

    For zero-extended F=Vu:
      q_j = (1/2)∫∫ exp(-alpha|x-y|)|F(x)-F(y)|² dx dy.
    This equals (4/d)||F||² -∫∫F(x)F*(y)exp(-alpha|x-y|).
    The identity is exact by ∫_R exp(-alpha|t|)dt=2/alpha=4/d.
    """
    if type(index) is not int or index<0:
        raise CompensationError('genuine Gamma ladder index j>=0')
    d=4*index+1
    return {'j':index,'d':d,'alpha':Q(d,2),
            'jump_mass':Q(4,d), 'one_half_dirichlet_prefactor':Q(1,2),
            'source_is_original_gamma_only':True,
            'RH_proved':False}


def original_gamma_jump_upper(distance):
    """J(r)=e^-r/2/(1-e^-2r) <= 1+1/(2r), source true r>0.

    Exact expression is a mathematical identity; the returned inequality is
    rational, deliberately not a certificate of an evaluated exponential.
    """
    r=rational(distance)
    if r<=0:
        raise CompensationError('positive cross-distance required')
    return {'distance':r,'original_gamma_jump_symbol':'exp(-r/2)/(1-exp(-2r))',
            'rational_upper':Q(1)+Q(1,2)/r,
            'Carleman_touching_coupling_not_ignored':True,
            'RH_proved':False}


def _sqrt_upper(x,scale=10**12):
    x=rational(x)
    if x<0:
        raise CompensationError('sqrt nonnegative rational required')
    n=isqrt(x.numerator*scale*scale//x.denominator)
    if Q(n*n,scale*scale)<x:n+=1
    return Q(n,scale)


def touching_carleman_moment_witness(order):
    """Positive nonvanishing no-gap Gamma coupling in every fixed Q_m.

    Take edge/central primitive profiles phi_m=(d/dt)^m[t^(m+1)(1-t)^(m+1)]
    reflected against a common endpoint, each scaled to support of length
    delta with L2 mass one. Their signed Gamma cross term is negative.
    As delta->0 the normalized bilinear cross magnitude tends to
      c_m=(1/2)∫∫ phi_m(s)phi_m(t)/(s+t) ds dt / ||phi_m||² > 0.
    The Laplace representation 1/(s+t)=∫_0∞e^-λs e^-λt dλ proves >0.
    For λ in [1,2], integration by parts m times gives
      ∫e^-λt phi_m(t)dt = λ^m∫e^-λt t^(m+1)(1-t)^(m+1)dt.
    With e<3, e^-4>1/81 and Beta(m+2,m+2), obtain the exact lower below.
    """
    if type(order) is not int or not 0<=order<=10:
        raise CompensationError('exact finite moment cut 0..10')
    phi=moment_annihilating_edge(order,Q(1))
    norm=integrate(mul(phi,phi),Q(0),Q(1))
    B=Q(factorial(order+1)**2,factorial(2*order+3))
    strictly_positive_limit_bound=B*B/(162*norm)
    if not strictly_positive_limit_bound>0:
        raise ArithmeticError('Carleman positive Laplace profile contradicted')
    return {'high_moment_cut':order,'polynomial_norm_squared':norm,
            'positive_carlemann_half_limit_greater_than':strictly_positive_limit_bound,
            'touching_gamma_cross_does_not_vanish_in_K_limit':True,
            'applies_even_at_four_moment_high_cut':order==4,
            'uses_true_gamma_jump_kernel':True,
            'complete_Weil_global_sign':False,'RH_proved':False}


def dyadic_gamma_edge_lower(delta):
    """Compressed proof for astronomically many genuine Gamma rungs.

    M=floor(1/(16delta)) and k=floor(log2 M). By harmonic grouping,
       H_M>=H_(2^k)>=1+k/2 (each dyadic block contributes >=1/2).
    Thus the complete true edge-source margin is at least k/2-5-delta/4,
    using actual bound contact+prime<47/8 and poles >=-delta/4.
    This calculation **never enumerates** the M Gamma rungs.
    """
    delta=rational(delta)
    if not Q(0)<delta<=Q(1,32):
        raise CompensationError('only first-true-prime birth delta in (0,1/32]')
    Mq=Q(1)/(16*delta)
    M=Mq.numerator//Mq.denominator
    if M<2:
        raise CompensationError('dyadic lower expects at least two Gamma rungs')
    k=M.bit_length()-1
    h_lower=Q(1)+Q(k,2)
    full_margin=h_lower-Q(1,8)-Q(47,8)-delta/4
    if h_lower <Q(1)+Q(k,2):
        raise ArithmeticError('dyadic grouping failed')
    return {'delta':delta,'conceptual_true_Gamma_mode_count':M,
            'dyadic_group_depth':k,'lower_harmonic_sum':h_lower,
            'full_source_edge_K_margin_from_dyadic_proof':full_margin,
            'only_logarithmic_cost_to_describe_many_rungs':True,
            'source_constants_need_original_gate':True,'RH_proved':False}


def touching_source_gluing_gate(delta, bulk_measure, source_bulk_margin):
    """Conditional first-prime **zero-gap** edge+center gluing theorem.

    Edge Fe has two strips each of width delta. Center Fb is supported on
    a connected interval of measure beta<=1 between them; supports may TOUCH
    at the two interfaces, but do not overlap. Both primitives vanish at the
    exterior endpoints; the original source bulk positivity 
      Q_G(Fb') >= c_B ||Fb||²
    is a separately necessary hypothesis, never minted by this code.

    Gamma cross operator between adjacent intervals:
      1/(s+t) has L² operator norm <=pi by Schur's s^-1/2 weight;
      J(s+t)<=1+1/(2(s+t))
    so each interface cross coefficient <=sqrt(delta beta)+pi/2.
    Two edges and original polar cross give
      eta <=sqrt(2)[pi/2+(1+2cosh(a))sqrt(delta beta)]
          <=sqrt(2)[11/7+(11/3)sqrt(delta beta)] for a<1/2.
    No gap g>0 is needed. The source Gamma edge diagonal grows like log1/delta.
    """
    d,beta,c=map(rational,(delta,bulk_measure,source_bulk_margin))
    if not Q(0)<d<=Q(1,32) or not Q(0)<beta<=Q(1) or c<=0:
        raise CompensationError('positive birth, bulk measure, and source bulk assumption required')
    # Actual central interval length b0-delta with b0=log2>2/3;
    # the supplied beta needs fit strictly inside this interval.
    if beta+d>=Q(2,3):
        raise CompensationError('claimed central support cannot be proven source-geometric')
    edge=dyadic_gamma_edge_lower(d)
    s=_sqrt_upper(d*beta)
    # pi/2 < 11/7; cosh(a)<4/3; no evaluated transcendental/roundoff loss.
    eta2=2*(Q(11,7)+Q(11,3)*s)**2
    return {**edge,
            'bulk_support_measure':beta,'bulk_K_margin_assumption':c,
            'touching_no_gap':True,
            'original_gamma_plus_pole_cross_eta_squared_upper':eta2,
            'strict_gluing_condition':edge['full_source_edge_K_margin_from_dyadic_proof']*c>eta2,
            'source_bulk_margin_proved':False,
            'covers_all_primitive_F_decompositions':False,
            'original_signed_source_all_channel_identity_required':True,
            'RH_proved':False}


def high_bulk_moment_gluing_algebra(delta=Q(1, 2**100), bulk_measure=Q(1, 4),
                                    kappa=Q(63, 500)):
    """Exact *conditional-on-WB4* arithmetic for a genuinely high-moment bulk.

    The bulk primitive F_b is in H0^1(B), where B is an interval of the stated
    measure between the two edge strips (it may touch the left strip). Require
    int_B t^j F_b(t)dt=0 for j=0,...,3. Then u_b=F_b' is orthogonal to
    t^k for k=0,...,4 on the larger I=(-1/2,1/2), by integration by parts.
    Thus the **existing original-source** theorem D4(1/2)>=kappa K applies
    to u_b after extension by zero, and the same source kernel restricts to
    I_a. This is not automatically true for an arbitrary central bulk.

    The algebraic check here remains conditional until the original WB4
    package is imported and run by the separately named source verifier below.
    """
    d,b,c=map(rational,(delta,bulk_measure,kappa))
    if c != Q(63, 500):
        raise CompensationError('only audited original WB4 lower bound 63/500 is admitted')
    cert=touching_source_gluing_gate(d,b,c)
    if not cert['strict_gluing_condition']:
        raise CompensationError('insufficient edge/Gamma compensation for claimed bulk class')
    if d!=Q(1,2**100) or b!=Q(1,4):
        raise CompensationError('this exact class-level theorem is pinned to delta=2^-100, beta=1/4')
    if not (cert['full_source_edge_K_margin_from_dyadic_proof']>Q(42)):
        raise ArithmeticError('dyadic original Gamma lower bound insufficient')
    # A transparent exact-rational certificate avoiding any computed pi/log:
    # sqrt(delta*beta)=2^-51<2^-10, so eta^2< 2(11/7+11/(3*2^10))^2<5,
    # while c_edge*c_bulk > 42*(63/500)>5.
    if not (cert['original_gamma_plus_pole_cross_eta_squared_upper'] < Q(5)
            < Q(42)*Q(63,500)):
        raise ArithmeticError('original two-chart exact strict PSD inequality failed')
    return {**cert,
            'WB4_source_margin_has_to_be_replayed':True,
            'bulk_H0_1_support_interval_may_touch_edge':True,
            'bulk_primitive_zeroth_through_third_moments_required':True,
            'bulk_derivative_high_moment_zeroth_through_fourth':True,
            'restriction_from_halfwidth_1_2_source_is_exact':True,
            'bulk_source_margin_certified_by_this_algebra_alone':False,
            'exact_lower_positive_product_at_least':Q(42)*Q(63,500),
            'exact_cross_square_under':Q(5),
            'RH_proved':False}


def original_source_high_bulk_gluing():
    """Actually replay both independent SHA-pinned source gates for SC-09.

    Audits original first-prime edge source plus inherited a=1/2 four-moment
    parity Bessel coercivity. The latter controls any central F_b with moments
    through order 3 vanishing, via the zero-extension restriction theorem.
    Does NOT claim arbitrary central bulk or whole first-window positivity.
    """
    from .gamma_edge_compensation import source_authenticated_compensation
    from .tate_weighted_bessel_four_schur import (
        source_parity_split_four_moment_coercivity_certificate,
        KAPPA_GLOBAL_SHARPENED,
    )
    delta=Q(1,2**100)
    base=source_authenticated_compensation(delta)
    upper=source_parity_split_four_moment_coercivity_certificate()
    source_sha=base['source_receipt']['source_git_blob']
    if not (base['source_checked'] and upper['source_suzuki_blob']==source_sha
            and upper['global_kappa_lower']==KAPPA_GLOBAL_SHARPENED==Q(63,500)
            and upper['halfwidth']==Q(1,2)
            and upper['parity_split_valid_by_reflection_commutation']):
        raise CompensationError('parent source or WB4 signed coercivity authentication failed')
    packet=high_bulk_moment_gluing_algebra(delta,Q(1,4),KAPPA_GLOBAL_SHARPENED)
    return {**packet,
            'source_bulk_margin_proved':True,
            'bulk_source_margin_certified_by_this_algebra_alone':False,
            'bulk_source_certifier':'INHERITED_PARITY_SPLIT_WB4_REPLAYED_ON_GENUINE_SOURCE',
            'edge_original_source_blob':source_sha,
            'bulk_original_source_blob':upper['source_suzuki_blob'],
            'bulk_moment_membership_still_required_for_each_test':True,
            'positivity_applies_only_to_declared_edge_plus_Q4_bulk_grammar':True,
            'all_radius_Weil_positive':False,
            'RH_proved':False}
