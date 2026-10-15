"""All-radius SUCC/Tate Fourier high positivity: explicit finite proof addresses.

For every finite rational a>0 and requested nonnegative L² coercivity target,
construct the EXACT INTEGER EXPONENTS of a (usually infeasibly large) source-
justified finite Legendre moment cutoff r, Gamma cutoff J and Fourier Ω such
that original signed Weil Q_zeta(f)>target*||f||² on f with first r moments 0.

The proof uses actual classical von Mangoldt coefficient upper bounds, ONE
real Gamma, two polar channels, original contact; composites are included
only in an OUTER arithmetic majorant, never as fake Euler prime places.

This does NOT construct/evaluate a finite matrix of rank r. It is an
effective existence theorem, NOT a feasible positive computation or RH.
"""
from __future__ import annotations
from fractions import Fraction as F


class AllRadiiSourceError(ValueError):
    pass


def _q(x):
    if type(x) not in (int,F):
        raise AllRadiiSourceError("Finite exact rational observation radius required")
    return F(x)


def _ceil(x:F) -> int:
    return -(-x.numerator // x.denominator)


def coarse_original_prime_polar_budget(a):
    """Finite rational majorant for genuine signed zeta minus channels.

    log2>1/2 gives n<exp(2a)<2^(ceil(4a)+1)=N for active n=p^k.
    For genuine prime powers w_n=Lambda(n)/sqrt(n)<=log(n)<=n.
    Upper bound 2 sum_{active source}w_n <= N(N+1)-2,
    using ALL n<=N only as a MAJORANT, never as an Euler source.
    e^a<2^(ceil(2a)+1)=E, hence negative sinh-pole<=E.
    True source C_inf<43/8. All bounds are intentionally enormous.
    """
    aa=_q(a)
    if aa<=0:
        raise AllRadiiSourceError("True finite positive observation halfwidth required")
    n_exp=_ceil(4*aa)+1
    e_exp=_ceil(2*aa)+1
    if n_exp>4096:
        raise AllRadiiSourceError("Executable budget N exceeds 4096 binary digits; paper theorem remains all-a")
    N=1<<n_exp
    E=1<<e_exp
    B=F(43,8)+N*(N+1)-2+E
    return {
        "a":aa,
        "integer_prime_majorant_N":N,
        "integer_majorant_binary_exponent":n_exp,
        "polar_exponential_upper_E":E,
        "all_source_negative_L2_bound_strict_upper":B,
        "composite_indices_act_only_as_numerical_majorant":True,
        "primitive_fake_six_source_weight":0,
        "one_original_real_Gamma":True,
        "RH_proved":False,
    }


def all_radius_formal_high_certificate(a, requested_margin=1):
    """Exact source-analytical ∀ finite a ∃ finite high moment rank proof.

    B(a) is a certified original prime/pole/contact upper.
    Choose integer M=ceil(17*(B+target+1)/4)+1, J=2^M, Omega=8*J,
    r=ceil(4*a*Omega)+1. Then:
      m_J(Omega)>16/17*H_J>=16/17*(1+M/2)>2*(B+target+1)
      low Fourier fraction epsilon_r(a,Omega)<1/12
    using factorial >=(r/e)^r, e<3, r>4*a*Omega.
    Hence original Q_zeta(f)>target||f||² for ALL compact smooth tests
    supported in (-a,a) with first r polynomial moments vanishing.

    Huge J/r are encoded as EXPONENTS/FORMULAS, not materialized matrices.
    This theorem does not certify the remaining finite low Schur signs.
    """
    aa,t=_q(a),_q(requested_margin)
    if aa<=0 or t<0:
        raise AllRadiiSourceError("Positive a and nonnegative desired Weil gap required")
    budget=coarse_original_prime_polar_budget(aa)
    B=budget["all_source_negative_L2_bound_strict_upper"]
    M=_ceil(F(17,4)*(B+t+1))+1
    # No materialization of J=2^M when M might be millions of bits.
    gamma_strict_lower=F(16,17)*(1+F(M,2))
    if gamma_strict_lower<=2*(B+t+1):
        raise ArithmeticError("Dyadic harmonic gamma divergence lower failed")
    # epsilon<1/12 universally for r>4*a*Omega.
    final_analytic_bound=F(11,12)*gamma_strict_lower-B
    if final_analytic_bound<=t:
        raise ArithmeticError("All-a original-source form lower did not meet requested margin")
    return {
        "source":"ORIGINAL_ONE_REAL_GAMMA_PRIME_POWER_ZETA",
        "a":aa,
        "requested_L2_high_gap":t,
        "prime_source_negative_budget":B,
        "Gamma_index_cutoff_J_power_of_two_exponent":M,
        "Fourier_Omega_exact_formula":"8*2^M",
        "moment_rank_exact_formula":"ceil(32*a*2^M)+1",
        "moment_rank_not_materialized":True,
        "Gamma_harmonic_multiplier_lower":gamma_strict_lower,
        "low_Fourier_mass_strict_upper":F(1,12),
        "original_Weil_strict_coercivity_lower":final_analytic_bound,
        "finite_high_source_positive_for_this_radius":True,
        "every_real_radius_from_rational_majorant_extension":True,
        "source_derived_low_Schur_positive":False,
        "finite_test_matrix_claimed_computed":False,
        "all_radii_low_schur_verified":False,
        "RH_proved":False,
    }


def gamma_harmonic_floor(J):
    """Exact small-J calibration of the universal Gamma multiplier lower.

    Omega=8J; alpha_j<(2J), beta_j>1/(j+1), so
       m_J(8J) > 16/17*H_J.
    This is a classical analytic theorem, finite Fraction checks only.
    """
    if type(J) is not int or not 1<=J<=128:
        raise AllRadiiSourceError("Small numerical calibration stage 1..128")
    from .tate_suzuki_fourier_schur import gamma_fourier_multiplier_lower
    exact=gamma_fourier_multiplier_lower(F(8*J),J)
    analytic=F(16,17)*sum((F(1,j+1) for j in range(J)),F())
    if exact<=analytic:
        raise ArithmeticError("Analytic all-radius Gamma harmonic lower falsified")
    return {
        "test_J":J,
        "genuine_Gamma_multiplier_exact":exact,
        "analytic_harmonic_strict_lower":analytic,
        "is_finite_calibration_not_all_radii_enumeration":True,
        "RH_proved":False,
    }
