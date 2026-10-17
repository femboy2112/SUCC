"""Original-source first-prime Gamma/edge compensation; exact K-relative theorem.

For source b=log(2), w=log(2)/sqrt(2), contact C, full original pole
channels and Gamma tower, any mean-zero u with F=Vu supported in the two
new prime-edge strips satisfies Q_original(u) > 11/128 ||F||^2 whenever
0<delta=2a-b<=1/32. This is an isolated *edge-subspace* positive theorem,
not whole-H positivity, a first-window Schur sign, or RH.

Pure arithmetic below is independently testable; original source gate separately
checks the exact, frozen Weil/Suzuki module's b,w,C and prime activation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt


class CompensationError(ValueError):
    pass


def rational(x):
    if type(x) not in (int, Q):
        raise CompensationError('exact int/Fraction required; no float/bool')
    return Q(x)


def harmonic_gamma_lower(terms, support_length):
    """Gamma from true d_j=4j+1 OU rungs; support-only Young/CS certificate.

    For u=F', F=0 at endpoints, the j-th source Gamma energy is
       (4/d_j)||F||² - <F,exp(-d_j|x-y|/2)F>.
    Kernel positive definite; the integral over E×E has norm <= |E| ||F||².
    All omitted Gamma rungs are nonnegative. A negative finite-rung bound is
    sound but not useful; no sign change or positive part is smuggled in.
    """
    if type(terms) is not int or not 1 <= terms <= 10000:
        raise CompensationError('finite nonempty Gamma mode budget')
    ell=rational(support_length)
    if ell<0:
        raise CompensationError('nonnegative support measure required')
    return sum((Q(4,4*j+1) for j in range(terms)),Q())-ell*terms


def true_first_edge_packet(delta, terms=16):
    """Conditional on original b,C,w bounds: valid for 0<delta<=1/32.

    Certificates use explicit source assumptions C+w<47/8, b<7/10,
    log3>log2+delta. Pole lower >= -delta/4 from sinh(a/2)<1/4.
    """
    delta=rational(delta)
    if not 0<delta<=Q(1,32):
        raise CompensationError('theorem only at first-prime birth 0<delta<=1/32')
    if type(terms) is not int or not 1<=terms<=10000:
        raise CompensationError('positive true-Gamma mode count required')
    ell=2*delta
    gamma=harmonic_gamma_lower(terms,ell)
    # Exact SOURCE assumptions to be checked independently against the frozen
    # signed Weil input before an authentic-source verdict is licensed.
    total=gamma-Q(47,8)-delta/4
    return {'delta':delta,'support_measure':ell,'gamma_modes':terms,
            'finite_gamma_relative_lower':gamma,'contact_plus_prime_upper':Q(47,8),
            'negative_pole_magnitude_upper':delta/4,
            'total_K_relative_lower':total,
            'positive_rational_margin':total>0,
            'uniform_11_over_128_if_16_modes': terms==16 and total>Q(11,128),
            'source_checked':False,'RH_proved':False}


def proof_by_exact_harmonic_arithmetic():
    """Rational calculation establishing uniform 11/128 on 0<delta<=1/32."""
    s=sum((Q(4,4*j+1) for j in range(16)),Q())
    assert s>Q(223,32), 'sixteen original Gamma rungs insufficient'
    margin=s-Q(1)-Q(47,8)-Q(1,128)
    assert margin>Q(11,128)
    assert Q(4,61)>Q(1,16) # each of 16 individually positive at support <=1/16
    return {'true_gamma_partial_sum':s,'partial_sum_better_than':Q(223,32),
            'uniform_K_margin_lower':margin, 'claimed_K_margin':Q(11,128),
            'modal_terms':16,'RH_proved':False}


def signed_two_port_bound(left_norm2, right_norm2, mixed_real, weight):
    """A cross measurement is essential; isolated diagonal energies do not decide sign."""
    a,b,q,w=map(rational,(left_norm2,right_norm2,mixed_real,weight))
    if a<0 or b<0 or q*q>a*b:
        raise CompensationError('non-realizable inner-product coupling')
    return {'edge_energy':-2*w*q,'K_energy':a+b,
            'sharp_absolute_cap':abs(w)*(a+b),
            'diagonal_reports_insufficient':a*b>0 and q*q<=a*b,
            'RH_proved':False}


def source_authenticated_compensation(delta=Q(1,32)):
    """Freeze exact parent source and independently check its interval claims.

    The radius a=(log2+delta)/2 is irrational: wavefront is certified by
    exact interval comparisons, NOT by inserting a rounded a into a wavefront
    checker with ambiguous equality. All tests are exact Fraction inequalities.
    """
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from . import source_weil_hierarchy as src
    result=proof_by_exact_harmonic_arithmetic()
    value=true_first_edge_packet(delta)
    pin=verify_original_suzuki_source()
    b=src.log2_iv(); invsqrt=src.sqrt_inverse(2)
    C=src.contact_iv(); log3=src.log_iv(3)
    w_lo=b.lo*invsqrt.lo
    w_hi=b.hi*invsqrt.hi
    if not (Q(2,3)<b.lo<=b.hi<Q(7,10)):
        raise CompensationError('original log2 boundary failed')
    if not (Q(0)<w_lo<=w_hi<Q(1,2)):
        raise CompensationError('authentic prime-2 half-density failed')
    if not C.lo>0 or not C.hi+w_hi<Q(47,8):
        raise CompensationError('original real Gamma/contact constant budget failed')
    if not b.hi+rational(delta)<log3.lo:
        raise CompensationError('original source has additional prime active')
    # At first-prime birth: a=(b+delta)/2, so a<b and a/2<1/5.
    if not b.lo>rational(delta) or not (b.hi+rational(delta))/4<Q(1,5):
        raise CompensationError('edge windows overlap or sinh bound inapplicable')
    # Elementary: for 0<=x<=1/5, sinh x <= x/(1-x^2) <= 5/24 <1/4.
    assert Q(5,24)<Q(1,4)
    if not result['uniform_K_margin_lower']>Q(11,128):
        raise CompensationError('false rational harmonic positivity')
    return {**value,'source_checked':True,'source_receipt':pin,
            'authentic_log2_interval':(str(b.lo),str(b.hi)),
            'authentic_weight_interval':(str(w_lo),str(w_hi)),
            'authentic_contact_interval':(str(C.lo),str(C.hi)),
            'true_prime2_only':True,'other_primes_inactive':True,
            'first_prime_born':True,'universal_edge_K_bound':Q(11,128),
            'completed_Weil_form_source_preserved':True,
            'all_high_space_coercivity_proved':False,
            'RH_proved':False}


def resolution_cost_bound(delta):
    """Poincare edge window for F in H0^1 supported in two length-delta bands.

    ||u||² >= pi²/delta² ||Vu||² > 9/delta² ||Vu||².
    The 9 bound uses only pi>3, hence is exact rational.
    """
    delta=rational(delta)
    if not 0<delta<=Q(1,32):
        raise CompensationError('prime birth width required')
    return {'delta':delta,'strict_squared_L2_to_K_lower':Q(9,1)/delta**2,
            'specific_four_moment_witness_squared_ratio':Q(234)/delta**2,
            'source_l2_bandwidth_claim':False,'RH_proved':False}


def countermodel_gluing():
    """Two source chart restrictions positive, mixed chart Gram indefinite."""
    G=((Q(1),Q(2)),(Q(2),Q(1)))
    e=(Q(1),Q(-1))
    energy=sum((e[i]*G[i][j]*e[j] for i in range(2) for j in range(2)),Q())
    assert energy==-2
    return {'positive_local_diagonals':(G[0][0],G[1][1]),
            'negative_joint_vector':e,'negative_joint_energy':energy,
            'mathematically_synthetic':True,'RH_proved':False}


def _atan_interval(t, K):
    """Exact alternating arctan enclosure for rational 0<=t<1."""
    t=rational(t)
    if not Q(0)<=t<Q(1) or type(K) is not int or K<2:
        raise CompensationError('arctan Taylor certificate domain')
    acc=sum(((-1)**j*t**(2*j+1)/Q(2*j+1) for j in range(K)),Q())
    nxt=(-1)**K*t**(2*K+1)/Q(2*K+1)
    return min(acc,acc+nxt),max(acc,acc+nxt)


def _log_interval(x, K=64):
    """Positive atanh series with exact rational geometric remainder."""
    x=rational(x)
    if not Q(1)<=x<=Q(4) or type(K) is not int or not 2<=K<=300:
        raise CompensationError('logarithm rational interval domain')
    t=(x-1)/(x+1)
    partial=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(K)),Q())
    tail=2*t**(2*K+1)/(Q(2*K+1)*(1-t*t))
    return partial,partial+tail


def rational_source_constant_control():
    """Independent all-Fraction source constants with no mpmath or source import.

    Uses exact Machin pi, atanh logs, the n=16 Euler-Maclaurin bound
    γ∈[H16−log16−1/(2·16)+1/(12·16²)−1/(120·16⁴)+
       1/(252·16⁶)−1/(240·16⁸), same without last remainder],
    and a rational sqrt(2) bracket. Under their standard classical analytic
    remainder proofs this confirms the literal source's constants.
    """
    l5,h5=_atan_interval(Q(1,5),20)
    l239,h239=_atan_interval(Q(1,239),6)
    pi_lo,pi_hi=16*l5-4*h239,16*h5-4*l239
    if not Q(3)<pi_lo<pi_hi<Q(22,7):
        raise ArithmeticError('Machin source pi bounds not validated')
    b_lo,b_hi=_log_interval(Q(2),32)
    logpi_lo=_log_interval(pi_lo)[0]
    logpi_hi=_log_interval(pi_hi)[1]
    # n=16 Euler-Maclaurin correction relative to H_n - log(n)
    n=16
    H=sum((Q(1,j) for j in range(1,n+1)),Q())
    base=H-Q(1,2*n)+Q(1,12*n*n)-Q(1,120*n**4)+Q(1,252*n**6)
    gamma_lo=base-4*b_hi-Q(1,240*n**8)
    gamma_hi=base-4*b_lo
    D=10**18
    q=isqrt(2*D*D)
    sqrt2_lo,sqrt2_hi=Q(q,D),Q(q+1,D)
    inv_lo,inv_hi=1/sqrt2_hi,1/sqrt2_lo
    w_lo,w_hi=b_lo*inv_lo,b_hi*inv_hi
    C_lo=gamma_lo+pi_lo/2+3*b_lo+logpi_lo
    C_hi=gamma_hi+pi_hi/2+3*b_hi+logpi_hi
    if not (Q(2,3)<b_lo<b_hi<Q(7,10) and Q(0)<w_lo<w_hi<Q(1,2)):
        raise ArithmeticError('source b,w constants out of range')
    if not C_lo<C_hi and C_lo!=C_hi:
        raise ArithmeticError('invalid contact interval')
    if not C_hi+w_hi<Q(47,8):
        raise ArithmeticError('entire source contact plus half-density does not fit 47/8')
    # Proof computation above is full Fraction arithmetic. Present only a
    # separate explicitly outward-rounded 36-decimal display enclosure,
    # avoiding enormous unreduced-rational JSON receipts. The strict test
    # was already performed on the unrounded exact endpoints.
    SCALE=10**36
    def floor(v): return Q(v.numerator*SCALE//v.denominator,SCALE)
    def ceil(v): return -floor(-v)
    return {'log2':(floor(b_lo),ceil(b_hi)),'weight2':(floor(w_lo),ceil(w_hi)),
            'pi':(floor(pi_lo),ceil(pi_hi)),
            'gamma_euler':(floor(gamma_lo),ceil(gamma_hi)),
            'contact':(floor(C_lo),ceil(C_hi)), 'combined_upper':ceil(C_hi+w_hi),
            'strictly_below_47_over_8':True,'source_import_used':False,
            'analytic_remainders_imported_classical':True,'RH_proved':False}


def gamma_logarithmic_edge_lower(support_length):
    """Explicit diverging Γ/K lower as supports shrink, valid for any F.

    Let ell=|supp F| <=1/8, M=floor(1/(8ell)). Since 4/(4j+1)>=1/(j+1),
    Gamma(F) >= [H_M-M ell]||F||² >= (H_M-1/8)||F||².
    Proof uses exact all-positive original Gamma OU tower, no zero inputs.
    """
    ell=rational(support_length)
    if not Q(0)<ell<=Q(1,8):
        raise CompensationError('positive sufficiently narrow source support')
    M=(Q(1)/(8*ell)).numerator//(Q(1)/(8*ell)).denominator
    if M<1:
        raise ArithmeticError('support-to-mode budget contradiction')
    H=sum((Q(1,j) for j in range(1,M+1)),Q())
    exact_gain=harmonic_gamma_lower(M,ell)
    if exact_gain < H-Q(1,8):
        raise ArithmeticError('Gamma source harmonic bound invalid')
    return {'support_length':ell,'number_of_gamma_rungs':M,
            'whole_gamma_K_lower':H-Q(1,8),
            'exact_used_rung_lower':exact_gain,'logarithmic_growth':True,
            'source_calibration_required':True,'RH_proved':False}


def buffered_edge_bulk_gluing(delta, gap, bulk_support_measure, bulk_K_margin):
    """Conditional REAL-SOURCE gamma/contact/poles/prime IMS two-chart gate.

    Fe is supported in the two prime edge strips (measure ell=2delta).
    Fb has disjoint central support of measure beta<=1 at distance >=gap>0
    from Fe; Fe and Fb are H0^1 primitive packets. Assume the genuine full
    original source satisfies Q(Fb') >= c_B ||Fb||². This is an *external*
    original-source bulk certification, not supplied by this routine.

    The original Gamma cross-kernel (in primitive coordinates) is exactly
        sum_(j>=0) exp(-(4j+1)r/2) = exp(-r/2)/(1-exp(-2r)).
    For r>=gap, <= 1+1/(2gap). Genuine original pole cross is bounded using
    cosh(a)<=4/3 (as a<1/2). Contact is diagonal; prime hinge has no bulk
    contribution when Fb is zero on edge strips. Hence
         Q(Fe'+Fb') >= (11/128)||Fe||²+c_B||Fb||²-2eta||Fe||||Fb||
    with eta² <= ell*beta*(11/3+1/(2gap))².
    This is an explicitly conditional *gluing theorem*, not full positivity.
    """
    delta,gap,beta,c=map(rational,(delta,gap,bulk_support_measure,bulk_K_margin))
    if not Q(0)<delta<=Q(1,32) or not Q(0)<gap or not Q(0)<beta<=Q(1):
        raise CompensationError('certified edge, separation, and bulk measure required')
    if c<0:
        raise CompensationError('bulk coercivity must be source-proven nonnegative')
    # For first prime a=(b+delta)/2 and E strips total measure 2delta;
    # the central available interval has length b-delta. Need enough space
    # for both positive gaps, as certified by b>2/3, never invent overlap.
    if beta+2*gap+delta >= Q(2,3):
        raise CompensationError('no justified central bulk support with two gaps')
    eta2=2*delta*beta*(Q(11,3)+Q(1,2)/gap)**2
    edge_margin=Q(11,128)
    return {'delta':delta,'buffer_gap':gap,'bulk_support_measure':beta,
            'bulk_margin_assumption':c,'edge_K_margin':edge_margin,
            'mixed_cross_coefficient_squared_upper':eta2,
            'positive_if_bulk_proved_and_product_strict':edge_margin*c>eta2,
            'bulk_source_coercivity_authenticated':False,
            'source_overlap_geometry_declaration_required':True,
            'RH_proved':False}
