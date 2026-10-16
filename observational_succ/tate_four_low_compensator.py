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


def exact_four_source_moment_polarization(moments,coefficient=F(65,16)):
    """Complete explicit four-moment version of original Weil correction.

    Let m_k=∫_{-1/2}^{1/2}t^k f(t)dt, k=0..3, for complex f∈H0¹.
    Original derivative carrier u=f'. Genuine Legendre P_j(2t):
      <u,P1> = -2 m0,
      <u,P2> = -12 m1,
      <u,P3> = +3 m0-60 m2,
      <u,P4> = +30 m1-280 m3.
    Their norms ||P_j(2t)||²=1/(2j+1). Therefore
      ||P4 u||² =
       3|-2m0|² +5|-12m1|²
      +7|3m0-60m2|²+9|30m1-280m3|².
    With coefficient 65/16 this is EXACT rank-four correction
    to genuine original Weil Q_zeta(f). Its presence makes the
    MODIFIED form PSD; it does NOT show original Q_zeta PSD.

    All scalars modeled by rational (real,imag) pairs, not floating.
    """
    if type(moments) not in (tuple,list) or len(moments)!=4:
        raise FourLowCompensatorError("Exactly four declared complex source moments required")
    def c(x):
        if type(x) in (int,F):
            return (F(x),F())
        if type(x) in (tuple,list) and len(x)==2 and all(
            type(t) in (int,F) for t in x
        ):
            return (F(x[0]),F(x[1]))
        raise FourLowCompensatorError("Moment coefficients require exact rational real/imag")
    ms=tuple(c(x) for x in moments)
    if type(coefficient) not in (int,F) or F(coefficient)<0:
        raise FourLowCompensatorError("Only nonnegative exact polarization coefficient")
    lam=F(coefficient)
    def lin(x,y,alpha,beta):
        return (alpha*x[0]+beta*y[0],alpha*x[1]+beta*y[1])
    c1=lin(ms[0],ms[0],-2,F(0))
    c2=lin(ms[1],ms[1],-12,F(0))
    c3=lin(ms[0],ms[2],3,-60)
    c4=lin(ms[1],ms[3],30,-280)
    coords=(c1,c2,c3,c4)
    energy=sum(((2*j+3)*(x*x+y*y)
                for j,(x,y) in enumerate(coords)),F())
    vanishes=energy==0
    if vanishes != all(x==0 and y==0 for x,y in ms):
        raise ArithmeticError("Original Legendre four-moment coefficient map lost rank")
    return {
        "source":"ORIGINAL_LEGENDRE_FOUR_LOW_MOMENT_POLARIZATION",
        "radius":F(1,2),
        "complex_test_moments_0_to_3":ms,
        "derivative_Legendre_pairings_P1_to_P4":coords,
        "source_Ker_P4_exactly_moment_null":True,
        "L2_projection_P4_source_energy_exact":energy,
        "finite_rank_correction_coefficient":lam,
        "modified_positive_source_correction_exact":lam*energy,
        "counterterm_vanishes_for_these_moments":vanishes,
        "counterterm_alone_is_RH_positivity":False,
        "RH_proved":False,
    }
