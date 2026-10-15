"""Tate x eta: canonical Bernoulli transport vs accidental Weil margins.

This research instrument keeps three DIFFERENT mathematically typed sources:
1. The original zeta Weil/Suzuki bound from DYSPON-SPHERE I (real Gamma,
   authentic prime-2, contact and poles; no zeta-zero inputs);
2. Dedekind's modular eta q-product over ALL positive integers, whose
   q^(1/24) exponent is fixed by classical modular inversion;
3. The Eisenstein divisor-current Dirichlet series zeta(s) zeta(s-1),
   whose TWO prime-power log-derivative channels cancel to -zeta'/zeta.

It does not identify eta modular positivity with original Weil positivity.
Everything finite/arithmetic uses int/Fraction, never sampled RH zeros.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .tate_prime_clock_uv import (
    genuine_first_prime_sparse_weil_certificate, PrimeClockGateError
)


class EtaTransportError(ValueError):
    """Refused an invalid or silently retyped source/normalization."""


def _rational(x) -> F:
    if type(x) not in (int, F):
        raise EtaTransportError("Exact int/Fraction parameter required")
    return F(x)


def bernoulli_heat_ledger() -> dict:
    """The exact constant term of sum_{n>=1} n exp(-n t).

    Identity for t>0: e^-t/(1-e^-t)^2 = 1/(4 sinh(t/2)^2).
    Formal Taylor:
      2 sinh(t/2)/t = 1 + t^2/24 + t^4/1920 + ...
      1/(4 sinh(t/2)^2) = t^-2 - 1/12 + t^2/240 + ...
    The heat constant equals analytically continued zeta(-1), NOT the
    ordinary divergent sum 1+2+3+...
    """
    u = F(1, 2**2 * factorial(3))  # 1/24
    v = F(1, 2**4 * factorial(5))  # 1/1920
    heat_constant = -2 * u
    heat_t2 = 3*u*u - 2*v
    eta_exponent = -heat_constant/2
    assert heat_constant == F(-1, 12) and heat_t2 == F(1, 240)
    assert eta_exponent == F(1, 24)
    return {
        "B2": F(1, 6),
        "zeta_of_minus_one": heat_constant,
        "heat_laurent_coefficient_t_minus_two": F(1),
        "heat_laurent_constant": heat_constant,
        "heat_laurent_t_squared": heat_t2,
        "canonical_eta_exponent": eta_exponent,
        "interprets_divergent_sum_as_analytic_continuation": True,
        "RH_proved": False,
    }


def original_weil_margin_ablation() -> dict:
    """Recover exact APOLLO/DYSPON original-source lower, not a new constant."""
    old = genuine_first_prime_sparse_weil_certificate()
    margin = old["uniform_source_margin_exact_lower"]
    exact = sum((F(4,4*j+1) for j in range(16)), F()) - F(111,16)
    if margin != exact:
        raise ArithmeticError("Original zeta source lower no longer matches gamma/prime/contact")
    # Genuine pinned source confirms the theorem; target rational cutoffs are
    # completely free BELOW its actual exact conservative lower margin.
    return {
        "source": old["source"],
        "original_source_lower": margin,
        "one_twenty_fourth_works": margin > F(1,24),
        "one_twenty_second_works": margin > F(1,22),
        "one_twenty_first_not_certified_by_this_bound": margin < F(1,21),
        "equal_to_eta_exponent": margin == F(1,24),
        "free_choice_of_all_rational_thresholds_below_lower": True,
        "arithmetic_eta_normalization_inferred_from_Weil_bound": False,
        "RH_proved": False,
    }


def eta_modular_s_defect(alpha, t_over_pi):
    """EXACT coefficient of pi in the log of the modular S defect.

    E_alpha(t) = exp(-alpha*t) prod_{n>=1}(1-exp(-n*t)).
    Classical Dedekind eta (alpha=1/24) obeys
      E(t) = sqrt(2*pi/t) E(4*pi^2/t).
    For t = c*pi, division by this canonical modular relation gives
      exp(-pi*(alpha-1/24)*(c-4/c)).
    Return the rational coefficient of pi. Zero at c=2 for EVERY alpha,
    hence testing only the self-dual point is a PROBE GAP.
    """
    aa,c=_rational(alpha),_rational(t_over_pi)
    if c<=0:
        raise EtaTransportError("Positive Archimedean modular time required")
    delta=aa-F(1,24)
    return {
        "chosen_q_exponent": aa,
        "canonical_q_exponent": F(1,24),
        "t_over_pi": c,
        "log_defect_over_minus_pi": delta*(c-F(4)/c),
        "S_transport_passes_at_this_clock": delta*(c-F(4)/c)==0,
        "all_positive_clocks_S_transport": delta==0,
        "self_dual_false_pass_possible": c==2 and delta!=0,
        "RH_proved": False,
    }


def eta_selfdual_first_jet(alpha) -> dict:
    """Weakest local probe repairing the exact modular S fixed-point gap.

    The modular S defect of E_alpha is exp[-delta*(t-4*pi^2/t)].
    At t0=2*pi its VALUE is 1 for every alpha, while
      d/dt log defect at t0 = -2*delta.
    Thus a single source-indexed FIRST DERIVATIVE, unlike a point
    value, determines alpha uniquely within the declared family.
    Equivalent sourced formula:
       alpha = sum sigma1(n)*exp(-2*pi*n) + 1/(8*pi) = 1/24,
    where the last equality follows from classical eta modular S
    and its self-dual Lambert reciprocity.
    No RH spectral zero observations or positive Weil claim.
    """
    aa=_rational(alpha)
    delta=aa-F(1,24)
    return {
        "probe_clock":"t=2*pi",
        "value_only_modular_S_defect":F(0),
        "logarithmic_first_derivative_defect":-2*delta,
        "first_jet_separates_normalization":True,
        "canonical_alpha_identified_by_zero_first_jet":delta==0,
        "source_current_formula":"alpha = F(2*pi)+1/(8*pi), F=sum sigma1(n)*exp(-n*t)",
        "exact_alpha_if_classical_modular_S":F(1,24),
        "all_Weil_tests_positive":False,
        "RH_proved":False,
    }


def eta_T_multiplier_exponent(alpha) -> dict:
    """T: tau->tau+1 determines multiplier alpha mod Z, not the exact alpha."""
    aa=_rational(alpha)
    delta=aa-F(1,24)
    return {
        "eta_T_exponent": aa,
        "canonical_exponent": F(1,24),
        "canonical_T_character": delta.denominator == 1,
        "S_still_required_to_fix_integer_gauge": delta!=0,
        "eta_power_24_cusp_order": 24*aa,
        "simple_cusp_zero_if_normalized": 24*aa==1,
        "RH_proved": False,
    }


def _divisors(n:int) -> tuple[int,...]:
    if type(n) is not int or n<1:
        raise EtaTransportError("Positive source integer required")
    return tuple(d for d in range(1,n+1) if n%d==0)


def _valuation(n:int) -> dict[int,int]:
    if type(n) is not int or n<1:
        raise EtaTransportError("Positive source integer required")
    out={}
    p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out


def sigma_one(n:int) -> int:
    """Finite divisor-source coefficient of eta logarithmic derivative."""
    return sum(_divisors(n))


def eta_q_log_derivative_coefficients(N:int, alpha=F(1,24)) -> tuple[F,...]:
    """Independently compute q*d/dq log E_alpha from the finite q-product.

    Truncation to q^N is EXACT: factors 1-q^m for m>N cannot affect
    any coefficient up to q^N.  Returned coefficients index 0..N.
    Coeff(0)=alpha; Coeff(n)=-sigma_1(n) for n>=1.
    """
    if type(N) is not int or not 1<=N<=256:
        raise EtaTransportError("Finite q-polynomial truncation 1..256 required")
    a=_rational(alpha)
    product=[0]*(N+1)
    product[0]=1
    for k in range(1,N+1):
        for j in range(N,k-1,-1):
            product[j]-=product[j-k]
    inverse=[0]*(N+1)
    inverse[0]=1
    for n in range(1,N+1):
        inverse[n]=-sum(product[k]*inverse[n-k] for k in range(1,n+1))
    answer=[a]
    for n in range(1,N+1):
        answer.append(F(sum(k*product[k]*inverse[n-k] for k in range(1,n+1))))
    return tuple(answer)


def _dirichlet_inverse(coeff:tuple[int,...]) -> tuple[int,...]:
    """Formal Dirichlet inverse of a(1)=1 with full finite coefficient exactness."""
    N=len(coeff)-1
    if N<2 or coeff[0]!=0 or coeff[1]!=1 or any(type(v) is not int for v in coeff):
        raise EtaTransportError("Source tuple a[0]=0,a[1]=1; integer coefficients required")
    out=[0]*(N+1)
    out[1]=1
    for n in range(2,N+1):
        out[n]=-sum(coeff[d]*out[n//d] for d in _divisors(n) if d>1)
    return tuple(out)


def formal_dirichlet_log_derivative(coeff:tuple[int,...]) -> tuple[dict[int,int],...]:
    """Exact n^-s Dirichlet coefficients of -D'(s)/D(s), in log-prime basis.

    Because log n = sum_p v_p(n) log p, the coefficient of n^-s
    is represented as a dict {p: integer multiple of log(p)}. This
    avoids transcendental fits and detects fake composite source atoms.
    """
    inv=_dirichlet_inverse(coeff)
    N=len(coeff)-1
    values=[{}]
    for n in range(1,N+1):
        row={}
        for d in _divisors(n):
            for p,k in _valuation(d).items():
                row[p]=row.get(p,0)+coeff[d]*k*inv[n//d]
        values.append({p:v for p,v in row.items() if v})
    return tuple(values)


def _subtract_rows(a:dict[int,int], b:dict[int,int]) -> dict[int,int]:
    return {p:v for p in set(a)|set(b) if (v:=a.get(p,0)-b.get(p,0))}


def eta_eisenstein_prime_transducer(N:int=64, fake_composite_six=False) -> dict:
    """Exact all-coefficients-through-N Eisenstein -> original Euler prime jet.

    From eta q-derivative -sigma1(n), form the DIRICHLET rather than
    ordinary q-series D(s)=sum sigma1(n)n^-s = zeta(s)zeta(s-1) (Re s>2).
    Its log derivative is a two-channel genuine prime source
      -D'/D = sum_{p,k} (1+p^k)*log(p) / p^(ks).
    Subtract shifted zeta(s-1) log derivative, n*log(p) on prime powers,
    obtaining exactly -zeta'/zeta = sum log(p)/p^(ks).
    The fake n=6 mutation breaks this, and must NOT be source-laundered.
    """
    if type(N) is not int or not 6<=N<=256:
        raise EtaTransportError("Finite 6..256 Dirichlet source horizon required")
    if type(fake_composite_six) is not bool:
        raise EtaTransportError("Explicit boolean source mutation flag required")
    div=[0]+[sigma_one(n) for n in range(1,N+1)]
    if fake_composite_six:
        div[6]+=1
    shift=[0]+list(range(1,N+1))
    zeta=[0]+[1]*N
    eisen=formal_dirichlet_log_derivative(tuple(div))
    shifted=formal_dirichlet_log_derivative(tuple(shift))
    original=formal_dirichlet_log_derivative(tuple(zeta))
    rows=tuple(_subtract_rows(eisen[n],shifted[n]) for n in range(N+1))
    mismatches=tuple(n for n in range(2,N+1) if rows[n]!=original[n])
    composite6=rows[6]
    # Strong check of separate channels only for the *unmutated* source.
    if not fake_composite_six:
        for n in range(2,N+1):
            val=_valuation(n)
            source={} if len(val)!=1 else {next(iter(val)):(n+1)}
            shift_source={} if len(val)!=1 else {next(iter(val)):n}
            if eisen[n]!=source or shifted[n]!=shift_source:
                raise ArithmeticError("Exact original divisor prime-current identity failed")
        if mismatches or composite6:
            raise ArithmeticError("Original prime log-current transport failed")
    else:
        if 6 not in mismatches or composite6!={2:1,3:1}:
            raise ArithmeticError("Fake-composite negative control no longer discriminates")
    return {
        "source_type": "EISENSTEIN_SIGMA1" if not fake_composite_six else "MUTATED_NON_EULER_SIGMA1",
        "finite_horizon": N,
        "mellin_source": "Gamma(s)*zeta(s)*zeta(s-1) for Re(s)>2",
        "prime_jet_parent": "(-D'/D)=(1+n)*Lambda(n) on n=p^k",
        "prime_jet_shifted": "-zeta'(s-1)/zeta(s-1)=n*Lambda(n) on n=p^k",
        "prime_jet_difference": "-zeta'(s)/zeta(s)=Lambda(n) on n=p^k",
        "composite_six_residual_prime_log_basis": composite6,
        "mismatch_indices": mismatches,
        "transport_preserves_genuine_von_mangoldt": not mismatches,
        "source_authentic": not fake_composite_six,
        "all_critical_line_transport_certified": False,
        "original_Weil_Gamma_contact_identified": False,
        "RH_proved": False,
    }


def sigma_one_dirichlet_tail_majorant(sigma:int, N:int) -> F:
    """Rigorous source-first absolute tail on Re(s)=sigma, sigma>=4.

    sigma1(n)<=n^2 (at most n positive divisors, each <=n), hence
    sum_{n>N} sigma1(n)/n^sigma
    <=sum_{n>N}n^(2-sigma)
    <=integral_N^infinity x^(2-sigma) dx
    =N^(3-sigma)/(sigma-3).
    The same bound holds for complex s with Re(s)=sigma.
    It does NOT control s on or near the critical line.
    """
    if type(sigma) is not int or sigma<4 or type(N) is not int or N<2:
        raise EtaTransportError("Source Mellin majorant requires integer sigma>=4,N>=2")
    return F(1,(sigma-3)*N**(sigma-3))


def modular_discriminant_formal_passport(N:int=12) -> dict:
    """Distinguish eta^24 cusp coefficients tau(n) from Eisenstein sigma1(n).

    Delta(q)=q prod(1-q^n)^24 has Fourier coefficients tau(n), while
    q dlog Delta/dq = E2 = 1-24 sum sigma1(n)q^n.
    The two coefficient sequences are NOT the same arithmetic source.
    All coefficients through q^N are computed by exact integer polynomial
    multiplication and exact power-series reciprocal, not modular sampling.
    """
    if type(N) is not int or not 3<=N<=48:
        raise EtaTransportError("Formal discriminant coefficient cutoff 3..48 required")
    M=N-1
    p=[0]*(M+1)
    p[0]=1
    for n in range(1,M+1):
        for k in range(M,n-1,-1):
            p[k]-=p[k-n]
    power=[0]*(M+1)
    power[0]=1
    for _ in range(24):
        new=[0]*(M+1)
        for i in range(M+1):
            if power[i]:
                for k in range(M-i+1):
                    if p[k]:
                        new[i+k]+=power[i]*p[k]
        power=new
    coeff=(0,)+tuple(power)
    inv=[0]*(M+1)
    inv[0]=1
    for n in range(1,M+1):
        inv[n]=-sum(power[j]*inv[n-j] for j in range(1,n+1))
    e2=[1]
    for n in range(1,M+1):
        e2.append(sum(j*power[j]*inv[n-j] for j in range(1,n+1)))
    exact=(1,)+tuple(-24*sigma_one(n) for n in range(1,M+1))
    if tuple(e2)!=exact or coeff[2]!=-24 or coeff[3]!=252:
        raise ArithmeticError("The eta^24 cusp/Eisenstein source contrast failed")
    return {
        "Delta_q_coefficients_through_degree_N":coeff,
        "q_dlog_Delta_coefficients_through_degree_N_minus_one":tuple(e2),
        "E2_comparison_exact":True,
        "Delta_Ramanujan_tau_coefficients_are_sigma1":False,
        "Gamma_of_Delta_L_series_identified_with_Gamma_zeta":False,
        "Delta_is_eta_to_24_power":True,
        "cusp_order_exactly_one":True,
        "RH_proved":False,
    }


def completed_two_critical_track_passport() -> dict:
    """Functional-equation decomposition without consulting zeta zero positions.

    For completed xi(s)=xi(1-s), X(s)=xi(s)*xi(s-1) satisfies
       X(2-s)=X(s).
    Every zero rho of xi yields product zero labels rho and 1+rho
    (taking multiplicities). So even CONDITIONAL ON RH, the product
    has two critical vertical tracks Re(s)=1/2 and Re(s)=3/2, not
    a single track at its symmetry center Re(s)=1. This is a
    structural warning, NOT a numerical scan or proof of RH.
    """
    return {
        "completed_object":"xi(s)*xi(s-1)",
        "functional_equation":"X(2-s)=X(s)",
        "symmetry_center_real_part":F(1),
        "conditional_on_RH_two_real_tracks":(F(1,2),F(3,2)),
        "formal_zero_translation":"rho maps to rho and 1+rho",
        "nontrivial_zero_locations_used_as_inputs":False,
        "single_track_at_center_not_implied":True,
        "source_projection_out_shifted_factor_required":True,
        "original_Weil_positivity_proved":False,
        "RH_proved":False,
    }


def mobius_exact(n:int) -> int:
    """True integer Möbius mu(n), no unknown source labels."""
    val=_valuation(n)
    if any(e>1 for e in val.values()):
        return 0
    return -1 if len(val)%2 else 1


def eta_mobius_heat_transducer(N:int=128, fake_six:bool=False) -> dict:
    """A DIRECT positive-output signed Möbius transducer in heat time.

    F(t)=sum sigma1(n)e^(-nt) is the eta logarithmic divisor heat current.
    T_mu F(t)=sum_{m>=1} mu(m)*m*F(m*t).
    By sigma1 * (mu*id) = 1 exactly, this equals
          H(t)=sum_{n>=1}e^(-nt)=1/(e^t-1)  for every t>0.
    Absolute convergence at each t>0 follows from exponential bounds,
    independent of any zeta zero positions.  Source weights include SIGNS;
    positive output does not assert T_mu is a positive operator on all F.
    """
    if type(N) is not int or not 6<=N<=512:
        raise EtaTransportError("Finite source coefficients horizon 6..512 required")
    if type(fake_six) is not bool:
        raise EtaTransportError("Explicit fake-six boolean mutation required")
    coeff=[]
    for n in range(1,N+1):
        # We must mutate sigma1(6) WITHIN every divisor convolution term,
        # not just the n=6 endpoint.  See inner loop below.
        r=sum(mobius_exact(d)*d*
              (sigma_one(n//d)+(1 if fake_six and n//d==6 else 0))
              for d in _divisors(n))
        coeff.append(r)
    wrong=tuple(n for n,c in enumerate(coeff,1) if c!=1)
    if not fake_six and wrong:
        raise ArithmeticError("Eta/Möbius exact original heat transducer failed")
    if fake_six and (6 not in wrong or coeff[5]!=2):
        raise ArithmeticError("Composite-six mutant did not produce heat-source defect")
    return {
        "source":"ORIGINAL_DIVISOR_SIGMA1" if not fake_six else "FORGED_SIGMA1_AT_SIX",
        "source_horizon":N,
        "positive_output_coefficients":tuple(coeff),
        "wrong_coefficient_indices":wrong,
        "exact_heat_identity":not wrong,
        "heat_output":"sum_n exp(-n*t) = 1/(exp(t)-1) for t>0",
        "original_mellin_after_cancellation":"Gamma(s)*zeta(s) for Re(s)>1",
        "operator_has_signed_Mobius_weights":True,
        "source_positive_operator_on_every_positive_input_proved":False,
        "Gaussian_real_place_positivity_preserved":False,
        "RH_proved":False,
    }


def gaussian_linear_heat_positive_mixing_no_go() -> dict:
    """Sharp no-go: NO source-blind positive Laplace mixing to Gaussian n^2.

    Suppose for u>0 a positive measure K_u(dt) on t>=0 gave
          exp(-pi*u*n^2) = integral exp(-n*t) K_u(dt)
    for every integer n>=1 (a linear-heat -> Gaussian-heat positive
    kernel that is independent of source label n).
    Then a_n=integral exp(-n*t)K is a log-convex moment sequence:
          a_(n+1)^2 <= a_n*a_(n+2) (Cauchy-Schwarz).
    But Gaussian a_n gives
          a_(n+1)^2/(a_n*a_(n+2)) = exp(2*pi*u)>1.
    Contradiction for every u>0, already at labels n=1,2,3.
    This only excludes this restricted positive Laplace mixture, not
    all nonlinear, signed, source-indexed or Gaussian Poisson transport.
    """
    return {
        "input_linear_spectrum":"exp(-n*t)",
        "target_gaussian_spectrum":"exp(-pi*u*n*n)",
        "required_positive_mixture_moment_inequality":"a_(n+1)^2<=a_n*a_(n+2)",
        "gaussian_ratio_exact":"exp(2*pi*u)>1 for u>0",
        "contradiction_at_labels":(1,2,3),
        "source_blind_positive_laplace_mixing":False,
        "source_indexed_or_signed_transport_ruled_out":False,
        "actual_Tate_theta_Gamma_R_identified_solely_by_mixture":False,
        "RH_proved":False,
    }


def tate_gaussian_fourier_stage(N:int, u, taylor_order:int=20,
                                phase_shift=F(0)) -> dict:
    """Lawful FINITE Fourier/Poisson replacement for impossible positive mix.

    Declare Tate real additive character psi_infinity(x)=exp(-2*pi*i*x).
    Classical Gaussian Fourier self-duality says, for all integer n and u>0:
      u^(-1/2)*int_R exp(-pi*x^2/u)*exp(-2*pi*i*n*x) dx
        = exp(-pi*u*n^2).
    Summing n=1..N is legitimate. The omitted positive theta tail obeys
      sum_{n>N} exp(-pi*u*n^2)
        <= exp(-pi*u*N^2)/(2*pi*u*N)
        < 1/(6*u*N*sum_{k=0}^K (3*u*N^2)^k/k!)
    using pi>3 and exp(z)>=sum_{k<=K} z^k/k!.
    The output is EXACT rational; the Gaussian Fourier identity is a
    stated classical analytical premise, not a finite numerical proof.
    A wrong character phase n+delta changes the Gaussian label to
    (n+delta)^2: it is not the authentic source unless delta=0.
    """
    if type(N) is not int or not 1<=N<=128:
        raise EtaTransportError("Fourier stage finite source N in 1..128 required")
    v=_rational(u)
    sh=_rational(phase_shift)
    if v<=0:
        raise EtaTransportError("Positive real Gaussian clock required")
    if type(taylor_order) is not int or not 0<=taylor_order<=64:
        raise EtaTransportError("Rational exponential tail order 0..64 required")
    z=3*v*N*N
    denominator=sum((z**k/F(factorial(k)) for k in range(taylor_order+1)),F())
    tail=F(1)/(6*v*N*denominator)
    return {
        "source_N":N,
        "gaussian_u":v,
        "declared_Fourier_character":"exp(-2*pi*i*(n+phase_shift)*x)",
        "Fourier_normalization":"1/sqrt(u)",
        "phase_shift":sh,
        "source_label_squares":tuple((F(n)+sh)**2 for n in range(1,N+1)),
        "authentic_integer_phase":sh==0,
        "classical_Fourier_identity_for_each_label":True,
        "Gaussian_theta_tail_strict_rational_upper":tail,
        "theta_tail_uses_only_positive_source":True,
        "real_Tate_Gamma_factor":"pi^(-s/2)*Gamma(s/2)",
        "real_Tate_zeta_Mellin_domain":"Re(s)>1",
        "nontrivial_zero_locations_used":False,
        "global_Weil_distribution_identified":False,
        "RH_proved":False,
    }


def tate_completed_theta_polar_split(s) -> dict:
    """EXACT rational polar calculation in the imported theta/Poisson completion.

    With theta_plus(u)=sum_{n>=1} exp(-pi*n^2*u), classical Poisson gives
      theta_plus(u)=u^-1/2 theta_plus(1/u)+(u^-1/2-1)/2.
    On Re(s)>1:
      Gamma_R(s)*zeta(s)
       = 1/(s-1)-1/s
         +int_1^infty theta_plus(u)*
           [u^(s/2-1)+u^(-(s+1)/2)]du.
    Rational s>1 checks the polar part by exact Fraction algebra.
    Xi(s)=s(s-1)/2 times this completed zeta, analytically entire
    and symmetric s<->1-s via the imported classical theta theorem.
    This constructs no source-derived all-test Weil sign.
    """
    z=_rational(s)
    if z<=1:
        raise EtaTransportError("Original theta Mellin germ starts at Re(s)>1")
    pole=F(1)/(z-1)-F(1)/z
    if pole!=F(1)/(z*(z-1)):
        raise ArithmeticError("Completed theta pole normalization failed")
    return {
        "s":z,
        "declared_source":"theta_plus(u)=sum_n>=1 exp(-pi*n*n*u)",
        "real_Tate_archimedean":"pi^(-s/2)*Gamma(s/2)",
        "Poisson_transport":"theta_plus(u)=u^-1/2*theta_plus(1/u)+(u^-1/2-1)/2",
        "completed_pole_part":pole,
        "completed_pole_cancellation_after_xi":F(1,2),
        "xi_definition":"xi(s)=s*(s-1)/2*Gamma_R(s)*zeta(s)",
        "xi_functional_equation":"xi(s)=xi(1-s) (classical imported Poisson)",
        "nontrivial_zero_lookup_used":False,
        "all_test_Weil_sign_proved":False,
        "RH_proved":False,
    }


def primary_source_interface_status() -> dict:
    """Typed map explicitly prevents illicit eta->RH promotion."""
    return {
        "canonical_Bernoulli_eta_q_exponent":F(1,24),
        "eta_dirichlet_domain":"Re(s)>2",
        "eta_heat_archimedean":"Gamma(s)",
        "original_zeta_prime_dirichlet_domain":"Re(s)>1",
        "original_zeta_Weil_half_density":F(1,2),
        "original_zeta_archimedean":"pi^(-s/2)*Gamma(s/2)",
        "eta_product_over":"ALL_POSITIVE_INTEGERS",
        "zeta_Euler_product_over":"GENUINE_PRIMES",
        "missing_transport":"source-faithful completed signed Weil Schwarz-Bruhat map with pole/contact and global positivity",
        "eta_modular_transport_is_not_Weil_positivity":True,
        "RH_proved":False,
    }
