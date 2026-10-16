"""True-source Tate/Suzuki seven-moment positivity via exact spherical Bessel tails.

At a=1/2 the original completed zeta Weil form Q_zeta is coercive
on ALL f∈C_c^∞(-a,a) satisfying moments k=0,...,6. The proof uses:

1. genuine first 128 real Gamma OU modes and their positive Fourier
   multiplier at Omega=49/4;
2. exact real Legendre expansion of exp(i omega t), and an analytically
   bounded low Fourier projection after seven vanished power moments;
3. rational spherical-Bessel polynomial integrals, with explicit
   Taylor/geometric/spectral tails and π>3;
4. original C_inf contact, half-density true prime p=2 (sharp two-cell
   shift norm 1), positive cosh pole, and the negative sinh pole
   suppressed by the same seven moments.

Source result: Q_zeta(f)>||f||²/16, for EVERY nonzero such test, NOT
just seven sample vectors or a positive surrogate.

For u=f' on original Suzuki H=L²_0, this yields the authentic
D_7=Q_7 G Q_7 >=(1/16)Q_7 K Q_7, K=V*V=(-Delta_N)^(-1),
with real 7×7 low Schur sign still unverified. No zeta zero positions
are read; existing source provenance is immutable.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .apollo_derivative_jets import _source, true_third_prime_wavefronts
from .tate_suzuki_fourier_schur import gamma_fourier_multiplier_lower
from .one_object_residual_schur import (
    ORIGINAL_SUZUKI_BLOB,
    parent_original_source_contract,
    original_source_cancellation_certificate,
)
from .suzuki_moment_schur import inverse_neumann_boundary_channels


class BesselSchurError(ValueError):
    """Source, interval, parity or proof domain is not authenticated."""


def _q(x):
    if type(x) not in (int,F):
        raise BesselSchurError("Only original-source exact int/Fraction allowed")
    return F(x)


def _nat(x,lo=1,hi=256):
    if type(x) is not int or not lo<=x<=hi:
        raise BesselSchurError("Natural proof cutoff outside declared finite range")
    return x


def odd_double_factorial(odd):
    """(2l+1)!!, no float approximations."""
    z=_nat(odd,1,511)
    if z%2!=1:
        raise BesselSchurError("Odd double factorial requires odd input")
    result=1
    for k in range(1,z+1,2):
        result*=k
    return result


def spherical_bessel_polynomial_l2(l, order, A):
    """Exact ∫_0^A P_l(z)^2 dz and UNIFORM analytic series remainder.

    Original spherical Bessel identity, a classical Fourier-Legendre law:
      j_l(z)=z^l/(2l+1)!! Σ_{k>=0}(-1)^k
                  z^(2k)/[2^k*k!*Π_{q=1}^k(2l+2q+1)].
    P_l is the truncation through k=order. For 0<=z<=A:
      |j_l-P_l| <= δ_l
    with δ_l = first omitted absolute power / (1-r), where the
    subsequent series ratio is at most
      r=A²/[2(order+2)(2l+2order+5)]<1.
    This is an absolute tail bound, not an unlicensed alternating
    monotonicity assertion.
    """
    L=_nat(l,0,128)
    K=_nat(order,0,64)
    z=_q(A)
    if z<=0:
        raise BesselSchurError("Positive actual source Fourier integration upper required")
    c=[F(1,odd_double_factorial(2*L+1))]
    for k in range(K):
        c.append(-c[-1]/(2*(k+1)*(2*L+2*k+3)))
    # P_l(z)=Σ_{k=0}^K c_k z^(l+2k).
    integral=F()
    for i,x in enumerate(c):
        for j,y in enumerate(c):
            power=2*L+2*(i+j)
            integral+=x*y*z**(power+1)/(power+1)
    if integral<0:
        raise ArithmeticError("Nonnegative exact polynomial square integral was lost")
    ratio=z*z/F(2*(K+2)*(2*L+2*K+5))
    if ratio>=1:
        raise BesselSchurError("Taylor remainder requires geometric ratio <1")
    first=abs(c[-1])*z**(L+2*(K+1))/(
        2*(K+1)*(2*L+2*K+3)
    )
    delta=first/(1-ratio)
    return {
        "l":L,"Taylor_order":K,"A":z,
        "polynomial_L2_squared_exact":integral,
        "pointwise_absolute_Bessel_remainder_upper":delta,
        "geometric_next_ratio_upper":ratio,
        "rigorous_for_every_real_z_from_zero_to_A":True,
        "RH_proved":False,
    }


def exact_legendre_low_frequency_enclosure(m=7, Omega=F(49,4),
                                          a=F(1,2), L=20, order=10,
                                          eta=F(1,10000)):
    """Rigorous ∫_{|ω|<=Ω} |fhat|² dω/(2π) <= eps ||f||².

    Hypothesis: all first m Lebesgue polynomial moments of f on
    I=(-a,a) vanish. The exact Legendre projection identity gives
      ||P_{>=m}e^(iωt)||² = 2a Σ_{l>=m}(2l+1) j_l(aω)².
    Plancherel low band is thus
      <=(2/π)∫_0^{aΩ}Σ_{l>=m}(2l+1)j_l(z)² dz ||f||².
    Replace 1/π by strict 1/3, then prove a Fraction enclosure:

    for l=m,..,L-1 use finite rational P_l and
      j_l²<=(1+η)P_l²+(1+1/η)δ_l²;
    for l>=L use the true real spherical-Bessel integral bound
      |j_l(z)|<=z^l/(2l+1)!!,
    so tail <= A^(2L+1)/((2L+1)!!)^2 /(1-(A/(2L+3))²).
    All stages operate on exact rationals, no zeta zero fitting,
    and no unbounded polynomial interpolation output.
    """
    mm=_nat(m,1,30); rank=_nat(L,mm+1,64)
    om=_q(Omega); aa=_q(a); slack=_q(eta)
    K=_nat(order,0,32)
    if om<=0 or aa<=0 or slack<=0 or mm>=rank:
        raise BesselSchurError("Positive Fourier/source chart and rank-tail required")
    A=aa*om
    total=F()
    modebounds=[]
    for ell in range(mm,rank):
        z=spherical_bessel_polynomial_l2(ell,K,A)
        integral=z["polynomial_L2_squared_exact"]
        delta=z["pointwise_absolute_Bessel_remainder_upper"]
        bound=(1+slack)*integral+(1+1/slack)*A*delta*delta
        total+=(2*ell+1)*bound
        modebounds.append((ell,bound))
    if A>=2*rank+3:
        raise BesselSchurError("High spherical Bessel factorial tail does not contract")
    geometric=(A/F(2*rank+3))**2
    tail=A**(2*rank+1)/odd_double_factorial(2*rank+1)**2/(1-geometric)
    mass=F(2,3)*(total+tail)
    if not 0<mass<1:
        raise ArithmeticError("Finite original low-band source bound outside [0,1]")
    return {
        "source":"CLASSICAL_LEGENDRE_BESSEL_FOURIER_ORIGINAL_L2",
        "a":aa,"Omega":om,"vanishing_power_moments":mm,
        "spherical_Bessel_exact_modes_from":mm,
        "spherical_Bessel_exact_modes_through":rank-1,
        "Taylor_order":K,"series_square_slack":slack,
        "spherical_Bessel_high_l_tail":tail,
        "low_Fourier_mass_fraction_strict_upper":mass,
        "low_Fourier_mass_below_1_over_61":mass<F(1,61),
        "Plancherel_polynomial_projection_all_complex_f":True,
        "RH_proved":False,
    }


def original_seven_moment_weil_certificate():
    """UNCONDITIONAL source-derived completed Weil seven-moment theorem.

    On a=1/2, true prime=2 and ∥compressed symmetric shift∥=1.
    Contact C_inf<43/8, prime w2<1/2. The negative sinh
    polar form is -2|∫ f sinh(t/2)|²; because f kills all
    polynomials degree<=6, Taylor of sinh through degree six
    with |sinh^{(7)}|<=2*(1/2)^7 on [-1/2,1/2] gives
      |∫ f sinh(t/2)| <= sqrt(2a)||f|| 2*(a/2)^7/7!.
    Thus the negative polar <=8*(a/2)^14/(7!)² ||f||².
    Gamma128 positive multiplier at Omega=49/4 and an analytic
    EXACT upper for low Fourier mass establish:
      Gamma128>3019/500, epsilon_7<1/61,
      polar_debt<1/10000.
    Hence complete signed Q >[3019/500*60/61-47/8-1/10000]
        ||f||² > ||f||²/16.
    Source includes original pole CONTACT, one Γ_R, genuine true p2.
    """
    src=_source()
    if not (src.contact_iv().hi<F(43,8)
            and src.log2_iv().lo>F(1,2)
            and src.log2_iv().hi<F(7,10)):
        raise BesselSchurError("Original gamma/contact/prime2 normalization changed")
    labels=tuple(z.n for z in true_third_prime_wavefronts(F(1)))
    if labels!=(2,):
        raise BesselSchurError("First-prime genuine von Mangoldt tape mismatch")
    weight=src.log2_iv()*src.sqrt_inverse(2)
    if weight.lo<=0 or weight.hi>=F(1,2):
        raise BesselSchurError("Half-density prime2 weight does not obey strict source bound")
    a=F(1,2);O=F(49,4);m=7;J=128
    epsilon=exact_legendre_low_frequency_enclosure(
        m=m,Omega=O,a=a,L=20,order=10,eta=F(1,10000)
    )["low_Fourier_mass_fraction_strict_upper"]
    gamma=gamma_fourier_multiplier_lower(O,J)
    pole=F(8)*((a/2)**(2*m))/factorial(m)**2
    actual_lower=gamma*(1-epsilon)-F(47,8)-pole
    if not (epsilon<F(1,61) and gamma>F(3019,500)
            and pole<F(1,10000) and actual_lower>F(1,16)):
        raise ArithmeticError("Original seven-moment true Weil positivity not certified")
    simpler=F(3019,500)*(1-F(1,61))-F(47,8)-F(1,10000)
    if not simpler>F(1,16):
        raise ArithmeticError("Exact elementary source-free rational final proof failed")
    return {
        "source":"SHA_PINNED_ORIGINAL_ZETA_COMPLETED_FIRST_PRIME",
        "original_source_git_blob":ORIGINAL_SUZUKI_BLOB,
        "source_halfwidth":a,"true_prime_power_labels":labels,
        "source_half_density_prime2_weight_upper":F(1,2),
        "original_C_infinity_upper":F(43,8),
        "moment_count":m,"Gamma_real_modes":J,"Fourier_Omega":O,
        "exact_Gamma_multiplier":gamma,
        "exact_low_frequency_fraction_upper":epsilon,
        "sinh_polar_moment_residual_upper":pole,
        "negative_contact_plus_prime_budget":F(47,8),
        "actual_exact_L2_gap_lower":actual_lower,
        "simple_rational_L2_gap_lower":simpler,
        "genuine_original_Q_zeta_strictly_above_K_1over16":True,
        "all_complex_smooth_tests_with_seven_moments":True,
        "all_original_first_window_tests_positive":False,
        "original_global_RH_proved":False,
        "RH_proved":False,
    }


def original_seven_low_suzuki_schur_interface():
    """TRUE ORIGINAL 7×7 low / infinite-high zero-shift Feshbach gate.

    On derivative-coordinate H=L²_0(I), V u(t)=∫_{-a}^t u, K=V*V.
    Orthogonality to actual Legendre P1..P7 makes f=Vu
    annihilate x^0...x^6 by integration by parts.
    Therefore D_7=Q_7GQ_7>=(1/16)Q_7KQ_7.

    Source PR109 original signed derivative ∥g'∥1<11/40 yields
      0<=R0<=(11/40)²/(1/16) I7=121/100 I7
    with finite true zero-shift, no compact D^-1 assumption.
    The low 7×7 Schur S0=A-R0 remains RH-hard and UNKNOWN.
    """
    cert=original_seven_moment_weil_certificate()
    stamp=parent_original_source_contract()
    if (stamp["source_git_blob_sha"]!=ORIGINAL_SUZUKI_BLOB or
            not stamp["original_screw_value_checked_against_derivative"]):
        raise BesselSchurError("Source-original signed G/Weil identity no longer matches")
    derivative=original_source_cancellation_certificate()
    if derivative["gprime_L1_STRICT_upper"]>=F(11,40):
        raise BesselSchurError("True source derivative signed cancellation missing")
    couplings=inverse_neumann_boundary_channels(F(1,2),7)
    if couplings["K_low_high_cross_rank"]!=2:
        raise BesselSchurError("Authentic Neumann source boundary channels not preserved")
    return {
        "source":"SHA_PINNED_ORIGINAL_SUZUKI_ZERO_SHIFT",
        "low_unnormalized_Legendre_indices":tuple(range(1,8)),
        "low_dimension":7,"parity_block_low_dimensions":(4,3),
        "first_prime_radius":F(1,2),"actual_prime_jet_labels":(2,),
        "source_high_K_relative_kappa":F(1,16),
        "source_K":"V*V=(-Delta_N)^(-1) on mean-zero derivative u",
        "true_source_K_low_high_boundary_rank":2,
        "zero_shift_R0_operator_norm_strict_upper":F(121,100),
        "zero_shift_Douglas_range_finite":True,
        "low_7x7_actual_S0_sign_certified":False,
        "source_all_window_W_zeta_positivity_certified":False,
        "all_radius_low_sign_certified":False,
        "RH_proved":False,
    }
