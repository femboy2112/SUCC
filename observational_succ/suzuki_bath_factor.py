"""Exact completed Archimedean OU-bath decomposition of Suzuki's G_a.

On mean-zero L²(-a,a), source-derived Archimedean operator is:
  B_a - C K_a + 8 |P sinh(x/2)><P sinh(x/2)|
                 - 8 |P cosh(x/2)><P cosh(x/2)|,
where B_a = sum_(j>=0) alpha_j^-2 P e^(-alpha_j|x-y|) P,
alpha_j=2j+1/2, C=gamma+pi/2+3log2+logpi,
K_a=(-Delta_N)^-1. B_a is PSD (OU covariance kernels).
The genuine prime wavefronts must be added separately, signed.

All operator claims have paper proofs. This is NOT global Weil positivity.
"""
from __future__ import annotations
from fractions import Fraction as Q
from .suzuki_prime_boundary import SuzukiWavefrontError, exact_fraction
from .suzuki_arch_intervals import (
    gamma_interval,pi_interval,log2_interval,log_pi_interval,
    exp_minus_interval,
)


def alpha(j:int)->Q:
    if type(j) is not int or not 0<=j<=100_000:
        raise SuzukiWavefrontError("invalid OU mode")
    return Q(4*j+1,2)


def bath_weight(j:int)->Q:
    return 1/alpha(j)**2


def gamma_linear_coefficient_interval()->tuple[Q,Q]:
    """Outward rational bounds on C = gamma+pi/2+3log2+logpi."""
    g0,g1=gamma_interval(8)
    p0,p1=pi_interval(9)
    l0,l1=log2_interval(18)
    lp0,lp1=log_pi_interval(24)
    return g0+p0/2+3*l0+lp0, g1+p1/2+3*l1+lp1


def bath_tail_mass_interval(N:int)->tuple[Q,Q]:
    """Σ_(j>=N) alpha_j^-2 bracketed by decreasing integral test."""
    if type(N) is not int or not 1<=N<=100_000:
        raise SuzukiWavefrontError("bath cutoff 1<=N<=100000 required")
    A=alpha(N)
    return 1/(2*A), 1/(2*A)+1/A**2


def bath_tail_operator_norm_upper(N:int, a_upper)->Q:
    """On (-a,a), || sum_(j>=N) alpha_j^-2 R_alpha || <= 2a sum alpha_j^-2.

    Input a_upper>=a is a user-supplied justified interval upper bound.
    The tail is PSD, so dropping it gives a rigorous LOWER quadratic bound.
    """
    a_upper=exact_fraction(a_upper)
    if a_upper<=0:
        raise SuzukiWavefrontError("positive certified interval radius required")
    _,s_hi=bath_tail_mass_interval(N)
    return 2*a_upper*s_hi


def elementary_rational_ou_psd(rho, values:tuple[Q,...])->dict:
    """Independent exact PSD finite OU covariance control (not actual source data).

    Matrix rho^|i-j| for 0<rho<1, with positive AR(1) covariance.
    Check exact LDL innovation factorization:
      v^T K v= h_0²+(1-rho²)sum_(j=1..m-1) h_j²,
      h_i=sum_(k=i..m-1) v_k rho^(k-i).
    """
    rho=exact_fraction(rho)
    vals=tuple(exact_fraction(v) for v in values)
    if not Q(0)<rho<Q(1) or not vals:
        raise SuzukiWavefrontError("0<rho<1 and nonempty exact vector required")
    n=len(vals)
    quadratic=sum((vals[i]*vals[j]*rho**abs(i-j)
                   for i in range(n) for j in range(n)),Q())
    # K= L D L^T, L_(i,j)=rho^(i-j) for i>=j,
    # D_0=1 and D_j=1-rho² for j>=1.
    tail_sums=[sum((vals[k]*rho**(k-j) for k in range(j,n)),Q())
               for j in range(n)]
    independent=tail_sums[0]**2 + (1-rho**2)*sum(
        (v**2 for v in tail_sums[1:]),Q())
    if quadratic!=independent:
        raise ArithmeticError("OU innovation square identity failed")
    return {"n":n,"rho":str(rho),"quadratic":str(quadratic),
            "independent_positive_factor":str(independent),
            "nonnegative":quadratic>=0,"not_an_actual_prime_kernel":True,
            "RH_proved":False}


def bath_source_receipt()->dict:
    C0,C1=gamma_linear_coefficient_interval()
    cuts=[]
    for n in (4,8,16,32,64,128):
        s0,s1=bath_tail_mass_interval(n)
        cuts.append({"N":n,"tail_weight_lower":str(s0),
                     "tail_weight_upper":str(s1),
                     "operator_tail_bound_when_a_le_1":str(bath_tail_operator_norm_upper(n,Q(1)))})
    return {"archimedean_source": "Suzuki (1.3), source-only OU bath",
            "alpha_j":"2j+1/2", "c_arch_lower":str(C0),"c_arch_upper":str(C1),
            "gamma_ou_bath_is_PSD":True,
            "signed_finite_rank_pole_modes":["+8 sinh rank-one","-8 cosh rank-one"],
            "signed_inverse_neumann_term":"-C K_a",
            "genuine_prime_power_translations_must_be_added":True,
            "tail_certificates":cuts,"RH_proved":False}


def certified_prime_free_small_interval(a, N:int=64)->dict:
    """UNCONDITIONAL explicit Weil positivity lower bound for 0<a'<=a.

    On H0^1(-a',a'), before the first prime at 2a'<log2, the exact
    gamma OU factorization gives
      lambda_(a') >= sum_(j<N) (2/alpha_j)exp(-alpha_j*a)
                    - C - 2(sinh(a)-a).
    We bound each exponential by positive rational Taylor intervals;
    C is enclosed from rational Machin arctan, atanh log and gamma harmonic
    bounds.  The positive remaining OU modes and +2 cosh pole are discarded.
    This gives a *whole-space* bound, not a Galerkin-eigenvalue guess.
    """
    from .suzuki_arch_intervals import (
        log2_interval,exp_interval,exp_minus_interval,outward_decimal_interval,
    )
    a=exact_fraction(a)
    if type(N) is not int or not 1<=N<=100:
        raise SuzukiWavefrontError("invalid finite OU truncation")
    if not Q(0)<2*a<log2_interval(18)[0]:
        raise SuzukiWavefrontError("whole interval must be before true prime 2")
    positive_lower=sum((Q(2)*exp_minus_interval(alpha(j)*a)[0]/alpha(j)
                        for j in range(N)),Q())
    C_hi=gamma_linear_coefficient_interval()[1]
    sinh_penalty_hi=exp_interval(a)[1]-exp_minus_interval(a)[0]-2*a
    lower=positive_lower-C_hi-sinh_penalty_hi
    clipped=outward_decimal_interval(lower,lower,10)[0]
    return {"radius_a":str(a),"N_positive_gamma_modes":N,
            "lambda_a_whole_space_lower_rational":str(clipped),
            "lambda_a_strictly_positive_certified":lower>0,
            "all_smaller_radii_included":True,
            "prime_source_actually_absent":True,
            "gamma_pole_terms_accounted_for":True,
            "uncertainty_method":"rational Taylor, arctan Machin, atanh log, harmonic gamma",
            "global_RH_proved":False}


def high_frequency_bath_tail_lower(N:int,omega:int)->dict:
    """Certified partial Fourier lower bound for unbounded D*R_tail D.

    m_N(omega)=sum_(j>=N)2 omega²/[alpha_j(alpha_j²+omega²)].
    Whenever alpha_j<=omega, its summand >=1/alpha_j.
    Hence m_N(omega)>=sum_(N<=j,alpha_j<=omega)1/alpha_j,
    a diverging harmonic sum as omega->infinity (N fixed).
    The infinite statement is proved by harmonic divergence, not finite tests.
    """
    if type(N) is not int or not 1<=N<=100_000 or type(omega) is not int or not 1<=omega<=100_000:
        raise SuzukiWavefrontError("positive bounded integer cutoff/frequency required")
    result=Q()
    j=N
    while alpha(j)<=omega:
        result+=1/alpha(j)
        j+=1
    return {"N":N,"frequency":omega,"m_tail_at_frequency_lower":str(result),
            "terms_used":j-N,"divergence_as_frequency_grows_is_analytic_theorem":True,
            "cannot_bound_differentiated_tail_by_small_compact_G_norm":True,
            "RH_proved":False}
