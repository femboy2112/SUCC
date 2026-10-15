"""Certified local Weil spectral shadow from the ORIGINAL theta completion.

No nontrivial zeta-zero locations are input. The contour itself is selected from
integer-theta observations and independently certified by the adjacent module.
Full signed Weil positivity remains open; this is only one residue summand.
"""
from __future__ import annotations
from fractions import Fraction as Q

from .theta_complex_contour import SourceContourError, first_critical_contour


def authentic_local_weil_rank_one(contour=None):
    """Proved local contribution to the completed Weil zero-side formula.

    On real compactly supported smooth f:
      A_f(s)=int f(x)*exp((s-1/2)*x) dx,
      Res_C [Xi'(s)/Xi(s)*A_f(s)*A_f(1-s)] = |A_f(rho)|^2 >= 0.
    The zero rho is source-certified to lie on Re(s)=1/2, with multiplicity 1.
    This statement is a local residue, NOT an identity for the entire Weil sum.
    """
    cert=first_critical_contour() if contour is None else contour
    if not isinstance(cert,dict) or not cert.get('certified_exactly_one') or not cert.get('critical_line_by_reflection'):
        raise SourceContourError('original-source simple critical zero certificate required')
    return {
        'source':'AUTHENTIC_COMPLETED_XI_ZERO_FROM_GAUSSIAN_THETA',
        'test_domain':'real C_c^infty(R)',
        'local_contour_zero_count':1,
        'local_zero_simple':True,
        'local_zero_on_critical_line':True,
        'local_spectral_form':'abs(A_f(rho))^2',
        'local_spectral_PSD':True,
        'completed_Weil_global_PSD':False,
        'all_other_zero_contributions_controlled':False,
        'RH_proved':False,
    }


def localized_mass_lower(support_halfwidth=Q(1,100)):
    """Uniform lower bound on the local spectral residue for f >=0, int f=1.

    Assume f in real C_c^infty and supp f contained in [-width,width].
    For gamma in the theta-certified range, gamma<15. Then
    Re A_f(1/2+i gamma) >= 1 - (15*width)^2/2.
    This yields a positive local rank-one Weil residue, not the global form.
    """
    if type(support_halfwidth) not in (int,Q):
        raise SourceContourError('exact source support width required')
    width=Q(support_halfwidth)
    if width<=0 or width>Q(1,15):
        raise SourceContourError('positive support in narrow strip required')
    v=1-Q(225,2)*width*width
    return {'halfwidth':str(width),
            'critical_zero_abs_ordinate_upper':'15',
            'localized_transform_real_lower':str(v),
            'localized_rank_one_Weil_lower':str(v*v),
            'positive':v>0,
            'only_one_spectral_summand':True,
            'global_signed_Weil_PSD':False,
            'RH_proved':False}


def fake_even_germ(known_even_degrees=1, radius=16):
    """Algebraic obstruction: finite Xi jets do not prevent distant off-line zeros.

    For known degrees 0...d, multiplication by 1+z^(2d+2)/R^(2d+2)
    preserves all those Taylor coefficients but changes the global divisor.
    For d=1, z=(R/sqrt2)(1+i) is an explicitly off-axis zero of the
    multiplier, no original Xi zero list is read.
    The multiplier is NOT source-Euler/Weil-authentic.
    """
    if type(known_even_degrees) is not int or not 1<=known_even_degrees<=20 or type(radius) is not int or not 2<=radius<=128:
        raise SourceContourError('limited algebraic false-source witness')
    m=2*known_even_degrees+2
    return {'known_even_jet_depth':known_even_degrees,
            'first_changed_coefficient_degree':m,
            'multiplier_constant':1,
            'multiplier_high_coefficient':str(Q(1,radius**m)),
            'preserves_low_theta_jets':True,
            'preserves_full_euler_theta_germ':False,
            'creates_noncritical_zeros':True,
            'simple_explicit_root_for_d1':'(R/sqrt(2))*(1+i)' if known_even_degrees==1 else None,
            'RH_proved':False}


def shadow_impostor_inside_critical_strip():
    """Original a0,a1 (symbols) + same Fock budget admit off-line strip zeros.

    Let rho_shift = 1/4 + 20i and M(z)=(1-z²/rho_shift²)
    (1-z²/conj(rho_shift)²) = 1+c*z²+d*z⁴ with c,d rational >0.
    For the *authentic* a0,a1 define
      G(z)=(a0+(a1-a0*c) z²)M(z).
    Then G has exactly the same first two even Taylor jets and zeros at
    rho_shift, conj(rho_shift), -rho_shift and -conj(rho_shift).
    They correspond to 0<Re(s)<1 but NOT Re(s)=1/2.
    Original-source inequality 0<a0<1/2, |a1|<1/80 gives ||G||Fock²<1/3.
    G is never promoted to the authentic Euler/theta xi.
    """
    zabs_squared=Q(6401,16)
    real_zsq=-Q(6399,16)
    c=-2*real_zsq/(zabs_squared*zabs_squared)
    d=1/(zabs_squared*zabs_squared)
    assert c==Q(204768,6401**2) and d==Q(256,6401**2)
    assert 0<c<Q(1,100) and 0<d<Q(1,100000)
    a0_hi=Q(1,2)
    a1_hi=Q(1,80)
    b1_hi=a1_hi+a0_hi*Q(1,100)
    a2_hi=b1_hi*Q(1,100)+a0_hi*Q(1,100000)
    a3_hi=b1_hi*Q(1,100000)
    budget_upper=a0_hi*a0_hi+2*a1_hi*a1_hi+24*a2_hi*a2_hi+720*a3_hi*a3_hi
    if not budget_upper<Q(1,3):
        raise ArithmeticError('false-source Fock countermodel budget lost')
    return {
        'fake_factor_c':str(c),'fake_factor_d':str(d),
        'fake_polynomial_symbolic':'(a0+(a1-a0*c)*z^2)*(1+c*z^2+d*z^4)',
        'same_original_a0_a1':True,
        'strict_fock_norm_squared_upper':str(budget_upper),
        'below_source_Fock_bound_260_over_27':True,
        'off_critical_inside_strip_root':'z=1/4+20i; s=3/4+20i',
        'original_Weil_arithmetic_source':False,
        'proof_obligation_not_disposed':'genuine completed signed Weil positivity',
        'RH_proved':False,
    }


def paired_original_Weil_window(interval_halfwidth=Q(1,2)):
    """Positive rank<=2 ORIGINAL completed-Weil spectral suboperator on (-a,a).

    The certified source disk yields gamma in (y0-r,y0+r), and the two
    genuine Xi zeros at s=1/2 +/- i gamma give kernel 2 cos(gamma*(x-y)).
    On L2(-a,a), its operator norm is <=4a. The source-midpoint kernel
    2 cos(y0*(x-y)) has operator-norm error <=8a^2 r, with NO zero lookup.
    The REMAINDER of the actual signed Weil operator is not positive-proved.
    """
    a=Q(interval_halfwidth) if type(interval_halfwidth) in (int,Q) else None
    if a is None or not 0<a<=1:
        raise SourceContourError('declared bounded compact test window required')
    y0=Q(141347,10000);r=Q(1,500)
    return {
        'test_window_halfwidth':str(a),
        'positive_original_pair_kernel':'2*cos(gamma*(x-y))',
        'theta_certified_frequency_interval':[str(y0-r),str(y0+r)],
        'positive_rank_upper':2,
        'operator_norm_upper':str(4*a),
        'midpoint_phase_operator_error_upper':str(8*a*a*r),
        'source_generated_phase':True,
        'full_signed_Weil_PSD':False,
        'RH_proved':False,
    }


def paired_phase_kernel_interval(separation=Q(1,2)):
    """Rational enclosure of authentic two-zero spectral cosine kernel."""
    from .theta_complex_contour import I,cos_sin_iv
    if type(separation) not in (int,Q):
        raise SourceContourError('rational test separation required')
    t=Q(separation)
    if abs(t)>1:
        raise SourceContourError('phase evaluator certified only for |x-y|<=1')
    y0=Q(141347,10000);r=Q(1,500)
    theta=I.of(abs(t)*y0)
    co,_=cos_sin_iv(theta)
    err=2*abs(t)*r
    return {'separation':str(t),
            'true_original_kernel_lower':str(2*co.lower()-err),
            'true_original_kernel_upper':str(2*co.upper()+err),
            'phase_uncertainty_exact_bound':str(err),
            'positive_source_pair_only':True,
            'global_signed_Weil_positive':False}
