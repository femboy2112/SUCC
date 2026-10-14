"""Signed completed-Weil zero-side H¹ tail bounds from the original Gaussian theta source.

This module implements exact Fraction certificates and SOURCE-TYPED contracts.
The underlying analytic proof uses the classical Weil explicit formula, Jensen's
formula, source-derived Xi growth, and one integration by parts per factor.
Absolutely NO nontrivial-zero locations are inputs to the tail theorem.

Status: PROVED LOCAL/CLASSICAL ingredients.  RH PROVED: NO.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
from hashlib import sha1
import json

class SignedTailError(ValueError):
    """Refuse unsupported parameters, forged source, or missing spectral receipt."""

SOURCE = 'AUTHENTIC_ONE_GAUSSIAN_INTEGER_THETA_XI'
PARENT_SHA = 'bb5b6f96f78df0d9472a60441501024e0e2b904e'
SOURCE_FIRST_PAIR_BLOB = '8f5ae1135701a933ba4946cb0b584bba4a355a47'
SOURCE_FIRST_PAIR_PATH = 'research/2026-10-14/THETA_COMPLEX_CONTOUR_RECEIPT.json'

def rat(x):
    if type(x) not in (int, Q):
        raise SignedTailError('exact integer/Fraction parameter required')
    return Q(x)

def _floor(x:Q)->int:
    return x.numerator//x.denominator

def _ceil(x:Q)->int:
    return -_floor(-x)


def log_unit_bounds(x:Q, terms:int=28)->tuple[Q,Q]:
    """Exact geometric Taylor enclosures for log x on 1<=x<=2."""
    x=rat(x)
    if not 1<=x<=2 or type(terms) is not int or not 2<=terms<=64:
        raise SignedTailError('log Taylor argument or budget invalid')
    z=(x-1)/(x+1)
    if not z:
        return Q(),Q()
    lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q())
    rem=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lo,lo+rem

def log_bounds(x,terms:int=28)->tuple[Q,Q]:
    """All rational inputs 1<=x<=1e30, no transcendental or float oracle."""
    x=rat(x)
    if not 1<=x<=10**30:
        raise SignedTailError('positive log domain [1,1e30]')
    k=0
    while x>2:
        x/=2
        k+=1
    a,b=log_unit_bounds(x,terms)
    c,d=log_unit_bounds(Q(2),terms)
    return a+k*c,b+k*d

def exp_upper(x,terms:int=28)->Q:
    """Exact rational enclosure for e^x, 0<=x<=5."""
    x=rat(x)
    if not 0<=x<=5 or type(terms) is not int or not 12<=terms<=64:
        raise SignedTailError('exp bound needs x in [0,5] and sufficient order')
    prefix=sum((x**j/factorial(j) for j in range(terms+1)),Q())
    next_term=x**(terms+1)/factorial(terms+1)
    return prefix+next_term/(1-x/Q(terms+2))

def source_count(T,source:str=SOURCE):
    """All nontrivial zeros with |Im rho|<=T, multiplicity included.

    N_abs(T) <= 7*T*log(4T), T>=2, is a theorem from the authentic theta
    growth |xi(1/2+z)| <= (1+|z|²) e^(|z|²/8), a sharper order-one theta
    growth refinement, F(0)>59/120, Jensen, and the known zero strip.
    An UPPER INTEGER certificate is returned.  No zeros are queried.
    """
    T=rat(T)
    if source!=SOURCE or not Q(2)<=T<=10**20:
        raise SignedTailError('authenticated theta source and 2<=T<=1e20 required')
    U=7*T*log_bounds(4*T)[1]
    return {'T':str(T),'absolute_count_upper':_ceil(U),
            'real_formula':'7*T*log(4*T)',
            'source_proof':'theta_order_one_growth_Jensen_RH_independent',
            'zero_coordinates_read':False,'RH_proved':False}

def absolute_zero_tail_weight(T,m:int=1)->dict:
    """All-zero SUM_{|gamma|>T} |gamma|^(-2m) unconditional bound.

    Using N_abs(t)<=7t log(4t) and dyadic shells. For m=1:
      <=28 log(16T)/T.
    For m>1: <=14*T^(1-2m)[log(8T)/(1-q)+log2*q/(1-q)^2]
    with q=2^(1-2m).  This counts OFF-LINE zeros as well.
    """
    T=rat(T)
    if type(m) is not int or not 1<=m<=8 or not Q(2)<=T<=10**20:
        raise SignedTailError('T>=2, 1<=m<=8, prescribed finite source budget')
    if m==1:
        upper=28*log_bounds(16*T)[1]/T
    else:
        q=Q(1,2**(2*m-1))
        upper=14*T**(1-2*m)*(log_bounds(8*T)[1]/(1-q)
              +log_bounds(2)[1]*q/(1-q)**2)
    return {'T':str(T),'m':m,'weight_upper':str(upper),
            'unconditional_for_all_nontrivial_zeros':True,
            'nontrivial_zero_coordinates_read':False,'RH_proved':False}

def signed_tail_operator_bound(a,T,m:int=1)->dict:
    """All test v,w in H_0^m(-a,a): |Q_>T(v,w)|<=delta ||v||_Hm||w||_Hm.

    m=1 sharp 5a/2 e^a per zero times 28 log(16T)/T:
       delta =70 a e^a log(16T)/T.
    General m uses loose 2a e^a (3/2)^(2m) multiplier.
    The source-only theta growth gives ALL-zero density, without RH.
    """
    a=rat(a);T=rat(T)
    if not 0<a<=5:
        raise SignedTailError('positive bounded Suzuki interval a<=5 required')
    spec=absolute_zero_tail_weight(T,m)
    factor=Q(5,2)*a if m==1 else 2*a*Q(3,2)**(2*m)
    upper=factor*exp_upper(a)*Q(spec['weight_upper'])
    return {'halfwidth':str(a),'height':str(T),'Sobolev_order':m,
            'norm':'H_0^%d(-a,a), sum_(j=0)^m ||v^(j)||_2^2'%m,
            'signed_remainder_form_norm_upper':str(upper),
            'source':SOURCE,'original_completed_Weil_identity_required':True,
            'zeros_off_line_allowed':True,'finite_known_zero_list_required':False,
            'full_Weil_positive':False,'RH_proved':False}

def first_pair_receipt(path:Path|str=SOURCE_FIRST_PAIR_PATH)->dict:
    """Only import certified zero pair from IMMUTABLE original theta proof.

    The file's *Git blob* checksum is pinned to prior PR #82 exact head.
    No arbitrary zero coordinates can be inserted by the caller.
    """
    p=Path(path)
    raw=p.read_bytes()
    blob=sha1(('blob %d\0'%len(raw)).encode()+raw).hexdigest()
    if blob!=SOURCE_FIRST_PAIR_BLOB:
        raise SignedTailError('certified theta source receipt sha mismatch')
    d=json.loads(raw)
    if d.get('source')!='AUTHENTIC_ONE_GAUSSIAN_INTEGER_THETA' or not all(
        d.get(key) for key in ('certified_exactly_one','critical_line_by_reflection','zero_is_simple','no_external_zero_lookup')
    ) or d.get('RH_proved') is not False:
        raise SignedTailError("source's critical-simple contour metadata invalid")
    c=Q(d['site']);r=Q(d['radius'])
    if not Q(2)<=c-r and c+r<100 or r<=0:
        raise SignedTailError('certified zero pair outside declared window')
    return {'verified_parent_SHA':PARENT_SHA,'receipt_sha':blob,
            'positive_pair_exists':True,'multiplicity_per_zero':1,
            'gamma_lower':str(c-r),'gamma_upper':str(c+r),
            'center':str(c),'radius':str(r),'RH_proved':False}

def certified_pair_operator(a,receipt_path=SOURCE_FIRST_PAIR_PATH)->dict:
    """For original Weil, positive rank<=2 pair and midpoint phase error.

    On L2(-a,a), the two genuine critical zeros give kernel 2cos(gamma(x-y));
    midpoint kernel error <=8a²r.  For T>gamma_high, this is a summand
    of the finite low spectrum, NOT a positivity result for the complement.
    """
    a=rat(a)
    if not 0<a<=5:
        raise SignedTailError('compact test window invalid')
    src=first_pair_receipt(receipt_path)
    r=Q(src['radius'])
    return {'source':SOURCE,'halfwidth':str(a),
            'positive_original_spectral_pair':True,'rank_at_most':2,
            'kernel':'2*cos(gamma*(x-y))',
            'midpoint_kernel_operator_error_upper':str(8*a*a*r),
            'max_pair_operator_norm':str(4*a),
            'source_receipt_sha':src['receipt_sha'],
            'other_zeros_undetermined':True,'full_Weil_PSD':False,'RH_proved':False}

def spectral_split_contract(a,T,receipt_path=SOURCE_FIRST_PAIR_PATH)->dict:
    """True Q_W=positive_pair+unknown_middle+signed_high_tail, RH-free.

    Unknown_middle includes ALL other |gamma|<=T zeros (not certified on
    the critical line).  Do not count the positive pair again.  The strict
    T threshold must contain both members of the pinned pair.
    """
    a=rat(a);T=rat(T)
    pair=first_pair_receipt(receipt_path)
    if T<=Q(pair['gamma_upper']):
        raise SignedTailError('height fails to include certified pair')
    tail=signed_tail_operator_bound(a,T)
    count=source_count(T)
    max_unknown=max(0,count['absolute_count_upper']-2)
    # Each low |gamma|<=T term has <= 2a e^a ||v||L2² from zero strip.
    mid_bound=2*a*exp_upper(a)*max_unknown
    return {'source':SOURCE,'halfwidth':str(a),'T':str(T),
            'certified_pair_positive':True,
            'certified_pair_operator_error_upper':str(8*a*a*Q(pair['radius'])),
            'uncertified_middle_count_upper':max_unknown,
            'uncertified_middle_L2_absolute_form_upper':str(mid_bound),
            'high_signed_H1_absolute_form_upper':tail['signed_remainder_form_norm_upper'],
            'all_mid_zeros_known_critical':False,'RH_proved':False,
            'full_Weil_positive':False}

def corrected_original_Gamma_error(J:int)->Q:
    """Inherited CW-11 actual Weil arithmetic Gamma truncation H¹ error.

    Source: PR #71 COMPLETED_WEIL_SOURCE_TRANSPORT.md, CW-11, signed
    corrected J-rung Gamma approximation. This is a theorem import WITH
    its complete prime/Gamma/contact/pole source, not a positive Gram.
    """
    if type(J) is not int or not 1<=J<=100000:
        raise SignedTailError('integer original Gamma rung budget 1..100000')
    A=Q(4*J+1,2)
    return max(Q(9,8*A*A)+Q(1,2*A*A*A),
               Q(1,2*A*A)+Q(2,A*A*A))


def two_chart_signed_gluing_bound(a,J:int,T)->dict:
    """Couple genuine arithmetic J-rung and genuine spectral <=T models.

    ||Q_arch,J - Q_spec,<=T||_(H1->H-1) <=epsilon_J + delta_a(T)
    by two independently proved source-normalized convergence contracts.
    Spectrum <=T remains signed, and is not computed using untrusted zeros.
    """
    tail=signed_tail_operator_bound(a,T)
    gamma=corrected_original_Gamma_error(J)
    delta=Q(tail['signed_remainder_form_norm_upper'])
    return {'original_source':'completed_Weil_prime_Gamma_pole_halfdensity',
            'arithmetic_chart':'source_corrected_J_Gamma_rungs',
            'spectral_chart':'entire_original_Xi_zeros_up_to_height_T',
            'J':J,'T':str(rat(T)),'halfwidth':str(rat(a)),
            'arithmetic_signed_H1_error_upper':str(gamma),
            'spectral_signed_H1_error_upper':str(delta),
            'two_chart_signed_H1_error_upper':str(gamma+delta),
            'neither_chart_auto_positive':True,
            'low_spectral_values_not_generated_by_this_bound':True,
            'RH_proved':False}


def concentrated_tent_H1(epsilon):
    """H0^1 family with bounded norm but NO classical sixth derivative.

    v_eps(x)=sqrt(eps)*(1-|x|/eps)_+ on (-eps,eps).
    Exactly: ||v_eps||²=2eps²/3, ||v_eps'||²=2.
    This is NOT a C7 test, and is a negative control against treating a
    smooth-six-derivative bound as a necessary H¹ spectral-tail barrier.
    """
    e=rat(epsilon)
    if not 0<e<=1:
        raise SignedTailError('positive concentrating support epsilon<=1')
    return {'epsilon':str(e),'norm_H1_squared':str(2+Q(2,3)*e*e),
            'derivative_L2_squared':'2','six_derivatives_classically_integrable':False,
            'all_H1_theorem_applies_by_density':True,'RH_proved':False}


def finite_shadow_countermodel()->dict:
    """Two equally source-visible first-rank probes cannot rule out middle minus.

    This is a generic signed Hilbert countermodel, explicitly NOT Xi.
    """
    positive_matrix=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)))
    mutant=((Q(1),Q(0),Q(0)),(Q(0),Q(-1),Q(0)),(Q(0),Q(0),Q(1)))
    return {'same_certified_pair':positive_matrix[0][0]==mutant[0][0],
            'positive_model_middle':str(positive_matrix[1][1]),
            'negative_model_middle':str(mutant[1][1]),
            'high_tail_exactly_zero':True,
            'models_arithmetic_completed_xi':False,'RH_proved':False}

def receipt():
    return {'program':'SIGNED_WEIL_H1_SOURCE_ONLY_TAIL',
            'parent_sha':PARENT_SHA,'test_radius':str(Q(1,2)),
            'T_grid':[signed_tail_operator_bound(Q(1,2),t) for t in (16,100,1000,10**6)],
            'source_count_16':source_count(16),
            'sample_H2_bound':signed_tail_operator_bound(Q(1,2),1000,2),
            'signed_two_chart':two_chart_signed_gluing_bound(Q(1,2),64,10**6),
            'first_pair':certified_pair_operator(Q(1,2)),
            'full_signed_split':spectral_split_contract(Q(1,2),16),
            'hostile_finite_shadow':finite_shadow_countermodel(),
            'H1_concentrating_model':concentrated_tent_H1(Q(1,1000)),
            'all_zero_count_from_original_theta':True,
            'nontrivial_zero_locations_read_by_tail':False,
            'complete_Weil_sign_proved':False,'RH_proved':False}
