"""Tate reflection diode: original prime-power jets and Archimedean contact.

The original unramified *forward-over-reflected* local Tate ratio is
  R_p(s,omega)=(1-omega*p^(s-1))/(1-omega*p^(-s)).
This is NOT the inverse (common local gamma convention) and NOT an
ordinary-convergent infinite Euler ratio at Re(s)=1/2.

At s=1/2 every unramified real omega=±1 has R_p=1, but:
  (log R_p)'(1/2)=-2*omega*log(p)/(sqrt(p)-omega).
For genuine omega=1 these are EXACT minus-two original Suzuki Weil
half-density prime-power jets sum_(k>=1)log(p)/p^(k/2).
The ordinary finite-prime slope tends to -infinity, whereas classical
global theta/Poisson reflection gives
  2*zeta'(1/2)/zeta(1/2)=C_inf=-psi(1/4)+log(pi),
where C_inf is the ORIGINAL APOLLO Brownian contact. The finite prime
product cannot simply be multiplied by a finite Gamma value to fix its
divergent raw derivative: global Tate/Poisson is a separate continuation.

A genuinely computable high-jet Euler reflection tail is obtained by
removing the first N local log-power terms. On 1/4<=Re(s)<=3/4,
N>=7 leaves a normally convergent, nonzero holomorphic Euler residual
with log tail after p>P (P>=16) bounded by 1/(2P). Its low-jet
counterterms do NOT thereby acquire global values.

Everything finite-source is Fraction/true-prime/source-SHA authenticated.
Classical functional equation, Euler prime-harmonic divergence, and
Gauss/Tate source charts are clearly identified as imported mathematics.
No nontrivial zeta zeros are construction inputs, and no RH sign is proved.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .apollo_derivative_jets import _source
from .tate_local_contract import _place, chi_mod3, unramified_ball_pair


class TateReflectionGateError(ValueError):
    """Invalid source, local gamma orientation, or fake global continuation."""


def _q(x):
    if type(x) not in (int,F):
        raise TateReflectionGateError("Proof input must be integer/Fraction (not bool/float)")
    return F(x)


def _integer(x,lo=1,hi=997):
    if type(x) is not int or not lo<=x<=hi:
        raise TateReflectionGateError("Positive integer within executable proof budget")
    return x


def reflected_local_prime_central_jet(p,source_profile="zeta"):
    """Original Tate local ratio with real unramified chi(p)=±1.

    For *trivial zeta* choose omega=+1 only. For the genuine primitive
    odd chi_-3, p=3 is RAMIFIED and no unramified ratio can represent
    that place; other primes omega=chi_-3(p).

    With t=p^-1/2, ratio at 1/2 is exactly 1, and its logarithmic
    derivative has the SHA-pinned exact-rational outward enclosure
      -2*omega*log(p)*t/(1-omega*t).
    Sign detects wrong character/polarity at p=2. Neither ratio is a
    globally normalized completed L-function without its conductor/
    local epsilon factors and proper Archimedean parity.
    """
    _integer(p,2)
    try:
        _place(p)
    except Exception as exc:
        raise TateReflectionGateError("Primitive composite cannot be a local Tate place") from exc
    if source_profile=="zeta":
        omega=1
    elif source_profile=="chi_minus_3":
        if p==3:
            raise TateReflectionGateError("Conductor p=3 is RAMIFIED, not unramified chi")
        omega=chi_mod3(p)
        if omega not in (-1,1):
            raise TateReflectionGateError("Wrong genuine conductor character")
    else:
        raise TateReflectionGateError("Only zeta/primitive chi_-3 source passports")
    src=_source()
    r=src.sqrt_inverse(p)
    logp=src.log_iv(p)
    denom=src.iv(1)-src.iv(omega)*r
    slope=src.iv(-2*omega)*logp*r/denom
    if (omega==1 and slope.hi>=0) or (omega==-1 and slope.lo<=0):
        raise ArithmeticError("True central reflection phase slope has wrong sign")
    at_two=unramified_ball_pair(p,0,2,omega)
    return {
        "source":"ORIGINAL_ZETA_TRIVIAL_TATE" if omega==1 and source_profile=="zeta"
                else "ORIGINAL_CHI_MINUS3_UNRAMIFIED_TATE",
        "p":p,"omega":omega,
        "source_profile":source_profile,
        "local_Tate_forward_over_reflected_at_center":F(1),
        "local_Tate_forward_over_reflected_at_s_two":at_two.forward_over_dual,
        "opposite_common_local_gamma_at_s_two":at_two.inverse_tate_gamma,
        "true_half_density_p_inverse_sqrt_interval":(r.lo,r.hi),
        "genuine_logp_interval":(logp.lo,logp.hi),
        "local_center_logarithmic_slope_interval":(slope.lo,slope.hi),
        "derivative_formula":"-2*omega*log(p)/(sqrt(p)-omega)",
        "unramified_local_ratio_reflection_inverse":True,
        "on_critical_line_unramified_local_ratio_unit_modulus":True,
        "center_probe_value_only_cannot_see_real_unramified_omega":True,
        "center_first_jet_detects_omega_parity":True,
        "valid_global_gamma_conductor_epsilon_completion_constructed":False,
        "RH_proved":False,
    }


def original_finite_prime_reflection_slope(prime_cutoff=19):
    """EXACT true-prime truncation of CENTER differential mirror.

    Sum only true zeta prime places p<=cutoff:
       (log product_p R_p)'(1/2)=-2 sum_p logp/(sqrtp-1) <0.
    Every additional p makes it STRICTLY more negative. By the
    classical Euler theorem sum_p 1/p diverges, the all-prime slope
    diverges to -infinity; a finite check alone cannot prove that.
    """
    P=_integer(prime_cutoff,2,997)
    src=_source()
    primes=[]
    total=src.iv(0)
    for p in range(2,P+1):
        if src.real_prime_power(p)==p:
            z=reflected_local_prime_central_jet(p)
            primes.append(p)
            lo,hi=z["local_center_logarithmic_slope_interval"]
            total+=src.I(lo,hi)
    if not primes or total.hi>=0:
        raise ArithmeticError("Nontrivial actual prime Euler reflection source missing")
    return {
        "source":"SHA_PINNED_ZETA_ALL_ACTUAL_PRIMES_UP_TO_CUTOFF",
        "last_prime":primes[-1],
        "actual_prime_labels":tuple(primes),
        "finite_Tate_ratio_exact_value_at_center":F(1),
        "finite_logarithmic_slope_interval":(total.lo,total.hi),
        "finite_slope_is_strictly_negative":True,
        "adding_true_prime_strictly_decreases_exact_slope":True,
        "all_prime_raw_center_slope_diverges_to_negative_infinity":
            True,  # imported classical divergence of sum_p 1/p
        "classical_Euler_prime_harmonic_divergence_imported":True,
        "finite_enumeration_alone_proves_divergence":False,
        "ordinary_prime_product_equals_analytic_zeta_ratio_at_half_neighborhood":False,
        "RH_proved":False,
    }


def real_reflection_diodes(sigma):
    """Classical real 0<sigma<1 sign/collapse of raw zeta local ratios.

    For sigma>1/2 each true factor 0<R_p(sigma)<1; the product over
    primes tends to 0. For sigma<1/2 each >1 and product -> +infinity.
    Exactly at 1/2 every R_p=1, hence product exactly 1.

    Proof uses log(1-a)-log(1-b), and divergence of sum_p 1/p.
    This is NOT global Λ(s)/Λ(1-s), which is constructed via Poisson.
    """
    x=_q(sigma)
    if not 0<x<1:
        raise TateReflectionGateError("The real center diode is stated on 0<sigma<1")
    side="center" if x==F(1,2) else ("right" if x>F(1,2) else "left")
    result="1" if side=="center" else ("0" if side=="right" else "+infinity")
    return {
        "source":"REAL_ZETA_UNRAMIFIED_REFLECTION_RATIOS",
        "sigma":x,"reflection_center":F(1,2),
        "each_finite_p_factor_relation_to_one":
            "=" if side=="center" else ("<" if side=="right" else ">"),
        "ordinary_all_prime_product_extended_limit":result,
        "this_is_NOT_the_analytic_zeta_reflection_ratio":True,
        "Euler_prime_harmonic_divergence_as_proof_input":True,
        "Gamma_R_ratio_is_nonzero_and_finite_in_this_real_strip":True,
        "raw_prime_product_and_Gamma_R_do_NOT_give_Global_Tate_continuation":
            True,
        "RH_proved":False,
    }


def central_Gamma_Brownian_contact():
    """Classical central reflection ONE-JET identity in original source gauge.

    Γ_R(s)=pi^-s/2 Γ(s/2), C_inf=-psi(1/4)+log pi.
      (Γ_R'/Γ_R)(1/2)=-C_inf/2.
    ζ(1/2)!=0: η(1/2)>0 by alternating series and
    ζ(s)=η(s)/(1-2^(1-s)) on real 0<s<1 => ζ(1/2)<0.
    Completed Λ=Γ_R ζ obeys Λ(s)=Λ(1-s) by Tate Poisson; hence
      ζ'/ζ(1/2)=+C_inf/2.
      (log Γ_R(s)/Γ_R(1-s))'center=-C_inf.
      (log ζ(s)/ζ(1-s))'center=+C_inf.

    THIS is the exact original APOLLO Brownian/contact scalar, not a
    proof that its signed Brownian operator is positive. The raw
    local prime slope tends to -infinity and must not be equated to
    this analytic global value by finite-prime multiplication.
    """
    src=_source()
    c=src.contact_iv()
    if not F(5)<c.lo<c.hi<F(43,8):
        raise ArithmeticError("Original completed real Gamma contact invalid")
    return {
        "source":"SHA_PINNED_ORIGINAL_ZETA_GAMMA_CONTACT",
        "center":F(1,2),
        "source_contact_C_infinity_interval":(c.lo,c.hi),
        "Gamma_R_log_derivative_center_interval":(-c.hi/2,-c.lo/2),
        "Gamma_R_reflection_ratio_log_slope_interval":(-c.hi,-c.lo),
        "zeta_log_derivative_center_interval":(c.lo/2,c.hi/2),
        "analytic_global_finite_reflection_log_slope_interval":(c.lo,c.hi),
        "zeta_half_nonzero":True,
        "zeta_half_nonzero_by_positive_alternating_eta":True,
        "completed_Lambda_central_log_derivative":F(0),
        "raw_finite_prime_slopes_do_NOT_converge_to_global_slope":True,
        "source_contact_equals_twice_analytic_zeta_log_derivative":True,
        "completed_RH_positive_Weil_form_proved":False,
        "RH_proved":False,
    }


def actual_center_high_prime_power_tail(prime_limit=19):
    """High jet k>=3 at central line is an ABSOLUTELY convergent source.

    For each genuine prime p:
       sum_(k>=3) Lambda(p^k)/sqrt(p^k)
       = log(p) p^-3/2 /(1-p^-1/2).
    Its negative 2x coefficient is the k>=3 part of the reflected
    local first derivative. Sum over p converges by comparison to
    sum_n log(n)n^-3/2. k=1 and k=2 BOTH diverge separately across p.
    """
    P=_integer(prime_limit,2,997)
    src=_source()
    summands=[]
    total=src.iv(0)
    for p in range(2,P+1):
        if src.real_prime_power(p)==p:
            r=src.sqrt_inverse(p)
            z=src.log_iv(p)*r*r*r/(src.iv(1)-r)
            if z.lo<=0:
                raise ArithmeticError("Original prime-power high-jet energy not positive")
            summands.append((p,z.lo,z.hi))
            total+=z
    return {
        "source":"SHA_PINNED_TRUE_VON_MANGOLD_HALF_DENSITY",
        "center":F(1,2),
        "prime_labels":tuple(p for p,_,_ in summands),
        "k_at_least_three_positive_source_partial_interval":(total.lo,total.hi),
        "reflection_slope_partial_high_jet_interval":(-2*total.hi,-2*total.lo),
        "k_at_least_three_all_prime_source_absolutely_convergent":True,
        "k_one_and_k_two_source_prime_sums_both_diverge":True,
        "Euler_prime_harmonic_divergence_imported":True,
        "low_k_one_two_renormalized_source_sign_established":False,
        "RH_proved":False,
    }


def high_jet_reflection_residual_contract(prime_cutoff=32, subtract_k_through=7):
    """Exact analytic tail for PRIME-ONLY, nonzero holomorphic reflection residual.

    Let R_p(s)=(1-p^(s-1))/(1-p^-s), and for integer N>=7:
      C_(p,N)(s)=sum_(k<=N)(p^-ks-p^-k(1-s))/k.
      H_N(s)=exp(sum_p [log R_p(s)-C_(p,N)(s)])
            =exp(sum_(p,k>N) (p^-ks-p^-k(1-s))/k).
    For 1/4<=Re(s)<=3/4, p>P>=16:
       |sum_(p>P,k>N)...| <= 1/(2P), independently of Im(s).
    Proof: with z=p^-1/4<=1/2, N+1>=8,
      sum_(k>N)|two terms|/k <= (1/2)p^-2;
      sum_(p>P)p^-2 <=sum_(n>P)n^-2 <=1/P.
    This proves a computable normally convergent and NONZERO residual
    with H_N(1-s)=H_N(s)^-1 and |H_N(1/2+it)|=1.
    Missing low k<=N counterterms are divergent prime sums: H_N
    alone is NOT zeta(s)/zeta(1-s), global positivity or RH.
    """
    P=_integer(prime_cutoff,16,997)
    N=_integer(subtract_k_through,7,32)
    return {
        "source":"ORIGINAL_ZETA_TRUE_PRIME_HIGH_JET_REFLECTION_RESIDUAL",
        "real_strip_closed":(F(1,4),F(3,4)),
        "prime_cutoff":P,
        "subtracted_actual_prime_power_jet_orders":tuple(range(1,N+1)),
        "first_residual_jet_order":N+1,
        "complex_log_residual_tail_absolute_upper":F(1,2*P),
        "valid_for_every_imaginary_part":True,
        "residual_holomorphic_nonzereo_and_normal_convergence":True,
        "reflection_relation":"H_N(1-s)=1/H_N(s)",
        "critical_line_residual_unit_modulus":True,
        "high_jet_residual_constructible_from_true_primes":True,
        "missing_k_le_N_low_jet_global_analytic_continuation":True,
        "raw_global_Euler_product_convergence_claimed":False,
        "global_completed_Weil_positivity_proved":False,
        "RH_proved":False,
    }


def finite_prime_reflection_counterterm_tape(primes=(2,3),order=7):
    """Original prime-power finite phase-counterterms at each true prime.

    This emits (n=p^k, p, 1/k), the exact coefficient in the
    logarithm of the local reflection factor:
      log R_p(s)=sum_(k>=1)(p^-ks-p^-k(1-s))/k.
    Differentiating at s=1/2 cancels the 1/k and gives -2*log(p)
    *p^-k/2 = -2*Lambda(p^k)/sqrt(p^k), EXACT original Suzuki jets.
    """
    N=_integer(order,1,32)
    if type(primes) not in (tuple,list) or not primes:
        raise TateReflectionGateError("Nonempty sequence of actual prime places required")
    seq=tuple(primes)
    if len(seq)>20 or any(type(x) is not int for x in seq) or tuple(sorted(set(seq)))!=seq:
        raise TateReflectionGateError("Strict increasing distinct prime labels required")
    for p in seq:
        _integer(p,2)
        try:
            _place(p)
        except Exception as exc:
            raise TateReflectionGateError("Composite source cannot form a prime jet") from exc
    tape=tuple((p**k,p,F(1,k)) for p in seq for k in range(1,N+1))
    return {
        "source":"TRUE_VON_MANGOLD_PRIME_POWER_REFLECTION_LOG_JETS",
        "genuine_prime_bases":seq,
        "jet_order_cutoff":N,
        "source_coefficients_n_parent_and_exact_1overk":tape,
        "center_first_derivative_k_cancels_denominator":True,
        "true_source_half_density_weight_formula":"Lambda(p^k)/sqrt(p^k)=log(p)/p^(k/2)",
        "primitive_composite_six_in_tape":any(n==6 for n,_,_ in tape),
        "actual_original_Euler_source_without_fake_six":True,
        "all_prime_sum_of_low_jet_renormalized":False,
        "RH_proved":False,
    }


def theta_selfdual_reflection_gauge(heat_log_weight=F(1,4)):
    """Canonical quarter-density in HEAT log coordinate from theta Poisson.

    Let Theta(t)=sum_(n∈Z)exp(-pi*n²*t), t>0. Its classically
    imported Poisson law Theta(t)=t^-1/2*Theta(1/t) yields:
       H_w(x)=exp(w*x)*Theta(exp(x)),
       H_w(-x)/H_w(x)=exp((1/2-2w)*x).
    Therefore H_w is even for every x iff w=1/4.
    At x=0 the value reflection is blind to every w; its first
    logarithmic derivative detects (1/2-2w), a true source-normalized
    reflection-probe repair. This quarter-weight in log heat time is
    not to be equated naively to the Dirichlet source n^-1/2.
    """
    w=_q(heat_log_weight)
    return {
        "source":"ORIGINAL_ONE_REAL_GAUSSIAN_THETA_POISSON",
        "heat_log_density_exponent":w,
        "unique_exact_theta_selfdual_exponent":F(1,4),
        "log_reflection_ratio_slope_in_heat_log_coordinate":F(1,2)-2*w,
        "Theta_poisson_identity_imported":
            "Theta(t)=t^(-1/2)*Theta(1/t)",
        "value_only_at_reflection_fixed_heat_time_t_one_blind":True,
        "derivative_detects_wrong_normalization":w!=F(1,4),
        "full_theta_log_kernel_even_for_all_x":w==F(1,4),
        "real_Gamma_R_and_polar_completion_still_required":True,
        "global_W_eil_sign_proved":False,
        "RH_proved":False,
    }


def reflected_center_jet_offline_mutant(m):
    """Hostile NON-EULER control defeating finite center and pole observations.

    Let x=s-1/2 and
      M_m(s)=1+(16*4^(2m)/3)*s*(s-1)*x^(2m).
    Then M_m(1-s)=M_m(s), M_m(0)=M_m(1)=M_m(1/2)=1,
    derivatives of orders 1..2m-1 at center all vanish.
    But M_m(1/4)=M_m(3/4)=0: off-critical line zeros in strip.
    Xi_mutant=Xi*M_m has same reflection symmetry, central jets through
    order 2m-1, and original polar residues, but no original Euler source.
    Mutant's first changed center derivative is
      -(4^(2m+1)/3)*(2m)!.
    No original Xi zeros are read, and RH is NOT contradicted.
    """
    k=_integer(m,1,16)
    coef=F(16*4**(2*k),3)
    def mutant(s):
        x=_q(s)
        return 1+coef*x*(x-1)*(x-F(1,2))**(2*k)
    if not (mutant(0)==mutant(1)==mutant(F(1,2))==1
            and mutant(F(1,4))==mutant(F(3,4))==0):
        raise ArithmeticError("Reflection mutant polynomial arithmetic changed")
    first_changed=F(-4**(2*k+1)*factorial(2*k),3)
    return {
        "source":"EXPLICIT_NON_EULER_REFLECTION_SYMMETRIC_MUTANT",
        "order_parameter":k,
        "function":"1+(16*4^(2m)/3)*s*(s-1)*(s-1/2)^(2m)",
        "values_at_zero_center_one":(mutant(0),mutant(F(1,2)),mutant(1)),
        "off_critical_line_zeros":(F(1,4),F(3,4)),
        "all_center_derivatives_through_order":2*k-1,
        "first_changed_center_derivative_order":2*k,
        "first_changed_center_derivative":first_changed,
        "preserves_completed_xi_reflection_symmetry":True,
        "preserves_original_completed_pole_residues":True,
        "preserves_original_prime_Euler_multiplicativity":False,
        "center_jet_or_completion_alone_does_NOT_force_RH":True,
        "RH_proved":False,
    }
