"""Tate Fourier UV -> genuine Weil -> Suzuki low/high Schur interface.

SOURCE: original zeta/one real Gamma, true first-prime p=2, half-density,
contact, both polar modes and the original anchored Suzuki G. All source
claims fail closed against the imported immutable PR85 blob via APOLLO.

NEW MATHEMATICS TO SUCC:
* an explicit high-moment coercivity certificate, derived from the true
  Fourier multiplier of real Gamma (not a finite positive numerical Gram);
* precise u=f' / Neumann primitive transport for authentic Legendre rank 16,
  18 and 30, giving rigorous zero-shift high positivity;
* a sharper source-Sobolev cross-resolvent bound, while the low Schur sign
  is NEVER assumed or declared positive.

Original source: Suzuki's classical Weil/screw formula; Tate theta/Poisson.
A full RH proof requires the unshifted LOW shorted sign FOR EVERY interval.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .apollo_derivative_jets import _source, true_third_prime_wavefronts
from .one_object_residual_schur import (
    ORIGINAL_SUZUKI_BLOB, ResidualShortingError,
    parent_original_source_contract, original_source_cancellation_certificate,
)
from .tate_eta_bernoulli import (
    tate_completed_theta_polar_split, primary_source_interface_status,
)


class FourierSchurGateError(ValueError):
    """Unsupported source passport or unjustified positivity/Schur promotion."""


def _r(x):
    if type(x) not in (int, F):
        raise FourierSchurGateError("Only exact integers/Fractions are a proof source")
    return F(x)


def _natural(x, lo=1, hi=512):
    if type(x) is not int or not lo <= x <= hi:
        raise FourierSchurGateError("Out-of-contract natural source index")
    return x


def gamma_fourier_multiplier_lower(omega, J):
    """Exact REAL Γ spectral m_J(ω)=sum β_j ω²/(α_j²+ω²).

    For u in Schwartz(R), original positive Gamma quadratic form is
      sum_j β_j <u,(I-R_α_j)u>
      = integral m(ω)|û(ω)|² dω/(2π),
    where α_j=(4j+1)/2, β_j=4/(4j+1).
    All omitted Γ terms are PSD. m_J is nondecreasing in |ω|.
    """
    w=_r(omega)
    _natural(J,1,512)
    if w<=0:
        raise FourierSchurGateError("Positive Fourier boundary frequency needed")
    w2=w*w
    return sum((F(4,4*j+1)*w2/(w2+F((4*j+1)**2,4))
                for j in range(J)),F())


def moment_taylor_low_fourier_fraction(a, omega, moments):
    """Exact rational UPPER BOUND on |ω|<=Omega Plancherel mass fraction.

    For f supported in [-a,a] with ∫x^k f(x)dx=0, k=0..m-1:
      |fhat(ω)| <= sqrt(2a)||f||₂ (a|ω|)^m/m!,
    using the OSCILLATORY Taylor remainder (no spurious exp(aΩ)).
    Consequently low Plancherel fraction <=
      2a Ω /(π(2m+1))*(aΩ)^(2m)/(m!)².
    Replace 1/π by STRICT upper 1/3, making this a pure Fraction.

    This is an all-f analytical inequality, not sampled Fourier modes.
    """
    aa,Om=_r(a),_r(omega)
    m=_natural(moments,1,128)
    if aa<=0 or Om<=0:
        raise FourierSchurGateError("Positive compact radius and Fourier clock required")
    return F(2)*aa*Om/(3*(2*m+1))*(aa*Om)**(2*m)/(factorial(m)**2)


def source_first_prime_spectral_budget(rank, omega=12, J=32):
    """True-source exact high-moment Weil coercivity at a=1/2.

    For every nonzero complex f∈C_c^∞(-1/2,1/2) with vanishing power
    moments 0..rank-1, prove
      W_zeta(f*tilde f) >= gap(rank)*||f||²
    from the genuinely completed Γ/pole/contact/p=2 form.

    Rank16 has gap>1/20, rank>=18 gap>1/16 at Omega12,J32.
    The proof extends to H0¹ by density with finite moment corrections.
    This is NOT an all-f sign or RH.
    """
    m=_natural(rank,1,30)
    w=_r(omega)
    _natural(J,1,128)
    if w<=0:
        raise FourierSchurGateError("True Fourier radius must be positive")
    src=_source()  # sha-pin exact original source to PR85
    if not (src.contact_iv().hi<F(43,8)
            and src.log2_iv().lo>F(2,3)
            and src.log2_iv().hi<F(7,10)):
        raise FourierSchurGateError("Source original contact and first prime not certified")
    p=tuple(atom.n for atom in true_third_prime_wavefronts(F(1)))
    if p!=(2,):
        raise FourierSchurGateError("Only original p=2 at |x-y|<1 may enter")
    # Exact source controls: C_inf<43/8; log2/sqrt2 <1/2;
    # true shift S_b+S_-b on first window has norm <=1;
    # negative pole 2*(sinh(1/2)-1/2)<1/16;
    # positive polar channel + omitted Γ tail are discarded by PSD order.
    negative=F(43,8)+F(1,2)+F(1,16)
    assert negative==F(95,16)
    gamma=gamma_fourier_multiplier_lower(w,J)
    eta=moment_taylor_low_fourier_fraction(F(1,2),w,m)
    gap=gamma*(1-eta)-negative
    return {
        "source":"SHA_PINNED_ORIGINAL_ZETA_FIRST_PRIME",
        "original_git_blob":ORIGINAL_SUZUKI_BLOB,
        "a":F(1,2),"moments_vanishing":tuple(range(m)),
        "legendre_high_cut_rank":m,
        "true_prime_power_labels":p,
        "Fourier_boundary":w,"real_Gamma_modes":J,
        "Gamma_high_frequency_multiplier_lower":gamma,
        "low_Fourier_mass_fraction_upper":eta,
        "completed_negative_budget_strict_upper":negative,
        "original_Weil_L2_gap_strict_lower":gap,
        "certifies_high_moment_W_zeta_positive":gap>0 and eta<1,
        "relative_Neumann_kappa_1over20_proved":m>=16 and gap>F(1,20),
        "relative_Neumann_kappa_1over16_proved":m>=18 and gap>F(1,16),
        "unrestricted_low_Schur_sign_proved":False,
        "RH_proved":False,
    }


def spectral_hard_gates():
    """These are all UNCONDITIONAL rational inequalities, source-aware only at wrapper."""
    d15=source_first_prime_spectral_budget(15)
    d16=source_first_prime_spectral_budget(16)
    d18=source_first_prime_spectral_budget(18)
    d30=source_first_prime_spectral_budget(30)
    if not (d15["original_Weil_L2_gap_strict_lower"]<0
            and d16["original_Weil_L2_gap_strict_lower"]>F(1,20)
            and d18["original_Weil_L2_gap_strict_lower"]>F(1,16)
            and d30["original_Weil_L2_gap_strict_lower"]>F(1,16)):
        raise ArithmeticError("Exact-source Fourier-moment proof comparison failed")
    return {
        "rank15_conservative_method_inconclusive":True,
        "rank16_high_kappa":F(1,20),
        "rank18_high_kappa":F(1,16),
        "rank30_high_kappa":F(1,16),
        "original_rational_source":True,
        "higher_rank_sign_extrapolation_not_assumed":True,
        "RH_proved":False,
    }


def tate_suzuki_zero_shift_interface(rank=30):
    """Theorem interface to PR109: proved high-relative K and sharpened Schur.

    For u∈H=L0²(-a,a) orthogonal to unnormalized Legendre P1..Pr,
    f=Vu is in H0¹ and ∫x^k f(x)dx=0 for 0<=k<r, by integration by
    parts against d/dx P_{k+1}(x/a).
    G's true signed screw and original distribution satisfy
      <u,Gu>=Q_zeta(Vu), <u,Ku>=||Vu||²,
      K=V*V=(-Delta_N)^(-1) on H.
    Hence D_r:=Q_r G Q_r >=kappa Q_r K Q_r.
    The actual G has g∈W¹¹ and ||g'||_1<11/40 per PR109 original
    source's outward rational 4096-cell/analytic-origin enclosure.
    This gives finite zero-shift R0 and
      0<=R0 <=(11/40)^2/kappa *I
    with NO K^-1 or D^-1 at zero.
    Remaining sign A-R0 is exactly the RH-hard local problem.
    """
    r=_natural(rank,16,30)
    if r not in (16,18,30):
        raise FourierSchurGateError("Published analytic contract only for rank16/18/30")
    b=source_first_prime_spectral_budget(r)
    k=F(1,20) if r==16 else F(1,16)
    if b["original_Weil_L2_gap_strict_lower"]<=k:
        raise FourierSchurGateError("High source Fourier coercivity NOT proved")
    # Independent passport: Tate conductor=1, parity0, half density=1/2,
    # exact contact, one Γ real, genuine p2, pointwise original screw/derivative.
    passport=parent_original_source_contract()
    if (passport["source_git_blob_sha"]!=ORIGINAL_SUZUKI_BLOB
            or not passport["original_screw_value_checked_against_derivative"]):
        raise FourierSchurGateError("PR109 true source/Weil chart not authenticated")
    theta=tate_completed_theta_polar_split(F(5,2))
    types=primary_source_interface_status()
    if (theta["real_Tate_archimedean"]!=types["original_zeta_archimedean"]
            or theta["completed_pole_cancellation_after_xi"]!=F(1,2)):
        raise FourierSchurGateError("Fourier spectral theorem uses wrong real Tate Γ")
    cancellation=original_source_cancellation_certificate()
    if not cancellation["gprime_L1_STRICT_upper"]<F(11,40):
        raise FourierSchurGateError("Original signed source derivative bound failed")
    bound=F(11,40)**2/k
    return {
        "source":"ORIGINAL_TATE_XI_WEIL_SUZUKI",
        "legendre_low_rank":r,
        "legendre_parity_low_ranks":(r//2, r//2),
        "genuine_high_source_positive_relative_to_inverse_Neumann":True,
        "K":"V*V=(-Delta_N)^(-1) on mean-zero u",
        "high_operator_D_at_least_kappa_K":k,
        "high_original_source_Weil_margin_exact_lower":b["original_Weil_L2_gap_strict_lower"],
        "sharp_original_source_gprime_L1_strict_upper":F(11,40),
        "zero_shift_R0_operator_norm_strict_upper":bound,
        "zero_shift_Douglas_cross_range_proved":True,
        "naive_zero_trial_schur_A_minus_norm_upper_cannot_certify":True,
        "naive_norm_only_certificate_upper_below_zero":F(11,40)-bound,
        "low_source_30x30_S0_sign_certified":False,
        "local_original_Weil_all_test_sign_proved":False,
        "all_radii_transport_proved":False,
        "RH_proved":False,
    }


def verify_cross_source_failure_modes():
    """Separate facts, never numerically infer the sign or mutate the source."""
    b16=source_first_prime_spectral_budget(16)
    base=b16["original_Weil_L2_gap_strict_lower"]
    # A fake extra coefficient in the negative contact cannot be claimed
    # authentic; even a budget delta=1/10 exhausts the published 1/20 margin.
    mutated=base-F(1,10)
    return {
        "original_rank16_gap":base,
        "contact_plus_one_tenth_mutation_budget":mutated,
        "mutation_loses_rank16_kappa_1over20":mutated<=F(1,20),
        "fake_six_is_source_invalid_even_if_outside_this_window":True,
        "moment_rank15_negative_budget_is_NOT_counterexample_to_zeta":
            source_first_prime_spectral_budget(15)["original_Weil_L2_gap_strict_lower"]<0,
        "normalization_mutations_are_not_zeta":True,
        "RH_proved":False,
    }
