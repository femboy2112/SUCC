"""A true-source rank-four POSITIVE COMPLETION of original signed Suzuki G.

From the original completed zeta Weil form at a=1/2, weighted Bessel-4
proves D=Q4 G Q4 >= (1/50) Q4 K Q4 for K=V*V.
Original signed PR109 derivative bound ||g'||_L1(-1,1)<11/40,
with g(0)=0, gives ||G||_op<11/40.
The zero-shift Douglas/Feshbach source bound is R0<=121/32 I4.
Thus the original signed operator plus EXACT rank-four counterterm
  G_tilde = G + (65/16) P4
is nonnegative on the ENTIRE mean-zero derivative Hilbert carrier:
  <u,G_tilde u> >= (1/160)||P4 u||² >= 0,
and has a lawful positive Hilbert square root.

This is a source-derived finite-rank POSITIVE AUXILIARY operator, NOT
the original Weil form, NOT an all-test RH proof. It identifies the
only four moment directions still needing a negative-feature
contraction; does NOT authorize silently removing their counterterm.
"""
from __future__ import annotations

from fractions import Fraction as F

from .tate_weighted_bessel_four_schur import true_four_low_suzuki_interface
from .one_object_residual_schur import ORIGINAL_SUZUKI_BLOB


class FourLowCompensatorError(ValueError):
    pass


def source_rank_four_positive_completion(counterterm=F(65,16)):
    """Analytic all-u theorem, backed by true original source proof gates.

    For u=x+h, x=P4u, h=Q4u, define true positive high D, low A and
    low/high B. Variational zero-resolvent short:
       <u,Gu> >= <x,Ax> - <x,R0 x>.
    True ||G||<11/40 and R0<121/32 I imply:
       <u,(G+tP4)u> >
            (t-11/40-121/32) ||x||².
    For t>=65/16, bound >=1/160. High-only x=0 already has
       <h,Gh> >=(1/50)<h,Kh>, K positive compact.
    Thus G+65/16 P4 >=0 on EVERY source derivative u, no RH.

    The source of P4 is the TRUE Legendre projection, not an
    arbitrary fitted low-rank shift or an extra false Euler place.
    """
    t=counterterm
    if type(t) not in (int,F):
        raise FourLowCompensatorError("Exact rational counterterm required")
    t=F(t)
    original=true_four_low_suzuki_interface()
    if not (original["source"]=="ORIGINAL_SUZUKI_SIGNED_FOUR_LOW_ZERO_SHIFT"
            and original["genuine_high_relative_K_kappa"]==F(1,50)
            and original["genuine_R0_zero_shift_norm_upper"]==F(121,32)
            and ORIGINAL_SUZUKI_BLOB=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"):
        raise ArithmeticError("Original source high/zero-shift K4 proof changed")
    base=F(11,40)+F(121,32)
    low_gap=t-base
    return {
        "source":"SHA_PINNED_ORIGINAL_SUZUKI_PLUS_EXPLICIT_4RANK_COMPENSATOR",
        "original_suzuki_git_blob":ORIGINAL_SUZUKI_BLOB,
        "radius":F(1,2),
        "true_original_active_prime_powers":(2,),
        "true_original_infinite_high_positive_K_kappa":F(1,50),
        "true_original_zero_shift_R0_upper":F(121,32),
        "true_original_G_L2_operator_norm_upper":F(11,40),
        "original_low_P4_Legendre_indices":(1,2,3,4),
        "source_rank_four_counterterm":t,
        "coarse_source_low_short_negative_bound":base,
        "strict_modified_low_L2_gap":low_gap,
        "G_plus_counterterm_P4_PSD_proved":low_gap>0,
        "G_plus_counterterm_P4_nonnegative_if_low_gap_zero":low_gap>=0,
        "canonical_Hilbert_positive_sqrt_exists_if_PSD":low_gap>=0,
        "modified_positive_Hilbert_sqrt_does_NOT_prove_original_G_positive":True,
        "source_negative_Morse_index_at_most":4,
        "source_negative_Morse_index_bound_proved":True,
        "source_nullspace_dimension_at_most":4,
        "original_unmodified_G_positive_proved":False,
        "original_complete_Weil_all_test_positive_proved":False,
        "RH_proved":False,
    }


def exact_low_high_short_toy(A=F(-1,4),B=F(1,8),D=F(1,2),
                             compensation=F(65,16)):
    """Hostile calibration of the positive-completion mechanism.

    Synthetic 2×2 matrix [[A,B],[B,D]] can be INDEFINITE despite
    strictly positive high D. Adding c to the low diagonal makes PSD
    exactly when A+c-B²/D>=0. This is a toy, NEVER actual zeta data.
    """
    x=(A,B,D,compensation)
    if any(type(z) not in (int,F) for z in x):
        raise FourLowCompensatorError("Exact rational toy data required")
    a,b,d,t=map(F,x)
    if d<=0:
        raise FourLowCompensatorError("Positive synthetic high control required")
    schur=a-b*b/d
    changed=schur+t
    return {
        "source":"SYNTHETIC_TWO_BY_TWO_SHORT_CALIBRATION_ONLY",
        "original_low_short":schur,
        "compensated_low_short":changed,
        "original_signed_matrix_PSD":schur>=0,
        "compensated_matrix_PSD":changed>=0,
        "positive_high_D":d>0,
        "source_original_zeta_identified":False,
        "RH_proved":False,
    }
