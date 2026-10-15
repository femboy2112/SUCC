"""Reflected odd/even authentic Weil source and a smaller Suzuki low sector.

The true first-prime completed Weil form is reflection diagonal:
  - even f: negative odd sinh pole VANISHES; positive cosh remains;
  - odd f: positive even cosh vanishes; negative sinh remains;
  - true Gamma OU, scalar contact and symmetric prime shifts preserve parity.

The exact real Gamma Fourier/moment method therefore allows:
  f EVEN, first 14 moments zero, J=256, Omega=217/20:
      Q_zeta(f) > (1/140)||f||².
  f ODD, first 16 moments zero, J=32, Omega=12:
      Q_zeta(f) > (1/20)||f||².

Under u=f' on the original mean-zero Suzuki derivative carrier:
  u odd -> f even, needs P1,P3,...,P13 (7 low observations).
  u even -> f odd, needs P2,P4,...,P16 (8 low observations).
Hence the NONCONTIGUOUS 15-dimensional low space
     P1..P14 plus P16
has high QGQ >=(1/140)Q K Q, K=V*V=(-Delta_N)^-1.
The low Schur sign is still UNVERIFIED and the kappa is worse than
the existing 18-dimensional low sector kappa=1/16. This is a
source-specific tradeoff, not a solution or numerical eigenvalue fit.
"""
from __future__ import annotations

from fractions import Fraction as F

from .tate_central_reflection import (
    central_Gamma_Brownian_contact, TateReflectionGateError
)
from .tate_suzuki_fourier_schur import (
    gamma_fourier_multiplier_lower, moment_taylor_low_fourier_fraction,
    source_first_prime_spectral_budget,
)
from .one_object_residual_schur import (
    ORIGINAL_SUZUKI_BLOB, original_source_cancellation_certificate,
)


def reflection_parity_15_low_source_certificate():
    """Source analytic plus/rank and rigorous independent Gamma bounds."""
    center=central_Gamma_Brownian_contact()
    if center["source_contact_C_infinity_interval"][1]>=F(43,8):
        raise TateReflectionGateError("True Gamma contact not source verified")
    a=F(1,2)
    Omega_even=F(217,20)
    J_even=256
    gamma_even=gamma_fourier_multiplier_lower(Omega_even,J_even)
    eps_even=moment_taylor_low_fourier_fraction(a,Omega_even,14)
    even_negative_budget=F(43,8)+F(1,2)  # h' odd rankone vanishes on even f
    even_gap=gamma_even*(1-eps_even)-even_negative_budget
    if not even_gap>F(1,140):
        raise ArithmeticError("Exact true Gamma EVEN parity 14-moment proof failed")
    odd=source_first_prime_spectral_budget(16)
    odd_gap=odd["original_Weil_L2_gap_strict_lower"]
    if not odd_gap>F(1,20) or odd["true_prime_power_labels"]!=(2,):
        raise ArithmeticError("Original 16-moment ODD source not certified")
    source_low_indices=tuple(range(1,15))+(16,)
    odd_derivative_low=tuple(k for k in source_low_indices if k%2==1)
    even_derivative_low=tuple(k for k in source_low_indices if k%2==0)
    if (odd_derivative_low!=tuple(range(1,14,2))
            or even_derivative_low!=tuple(range(2,17,2))
            or len(source_low_indices)!=15):
        raise ArithmeticError("Parity source selector is not an honest 15D low carrier")
    kappa=F(1,140)
    derivative=original_source_cancellation_certificate()
    if not derivative["gprime_L1_STRICT_upper"]<F(11,40):
        raise ArithmeticError("PR109 original zeta gamma/pole/prime cancellation source failed")
    # The true zero-shift variational Schur bound is finite but very weak.
    bound=F(11,40)**2/kappa
    return {
        "source":"TRUE_ZETA_TATE_GAMMA_REFLECTION_PARITY_WEIL",
        "original_suzuki_git_blob":ORIGINAL_SUZUKI_BLOB,
        "a":a,
        "true_active_prime_powers":(2,),
        "even_f_Gamma_modes":J_even,
        "even_f_Fourier_cutoff":Omega_even,
        "even_f_zero_moment_count":14,
        "even_f_Gamma_multiplier_exact":gamma_even,
        "even_f_low_Fourier_mass_fraction_upper":eps_even,
        "even_f_negative_sinh_pole_vanishes":True,
        "even_f_negative_source_upper":even_negative_budget,
        "even_f_source_gap_strict_lower":even_gap,
        "even_f_certified_gap":F(1,140),
        "odd_f_zero_moment_count":16,
        "odd_f_positive_cosh_pole_vanishes":True,
        "odd_f_source_gap_strict_lower":odd_gap,
        "odd_f_certified_gap":F(1,20),
        "source_low_indices":source_low_indices,
        "odd_derivative_low_modes_even_primitive":odd_derivative_low,
        "even_derivative_low_modes_odd_primitive":even_derivative_low,
        "low_dimension":15,
        "reflection_parity_block_dimensions":(7,8),
        "full_true_high_operator_G_at_least_kappa_K":kappa,
        "true_inverse_Neumann_K":"V*V=(-Delta_N)^-1 on meanzero derivative",
        "source_original_gprime_L1_strict_upper":F(11,40),
        "true_zero_shift_R0_operator_norm_strict_upper":bound,
        "relative_kappa_worse_than_rank18":kappa<F(1,16),
        "rank15_low_Schur_sign_certified":False,
        "all_a_global_positive_Weil_proved":False,
        "RH_proved":False,
    }
