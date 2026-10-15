"""TATE WEIGHTED BESSEL-4: genuine completed Weil from FOUR vanished moments.

Improve prior source Bessel-7 by weighting the low-frequency leakage with
the ACTUAL positive real Gamma spectral multiplier rather than replacing it
everywhere with its Fourier-boundary maximum.

This yields on a=1/2, for EVERY nonzero f∈C_c^∞(-a,a;C)
with ∫t^k f(t)dt=0 for k=0,...,3:
      Q_zeta(f) > (1/50)*||f||_2².
This is a sourced all-f infinite-dimensional inequality, NOT a sampled
positive finite matrix or a global RH proof.

Original source remains one real Gamma_R, both polar channels, C_inf,
only genuine von Mangoldt n=2 half-density prime, and Weil test domain.
No nontrivial zero coordinates are construction inputs.

On original Suzuki derivative carrier: P1..P4 low (2 odd+2 even);
D4=Q4 G Q4 >= (1/50)Q4 K Q4, K=V*V=(-Delta_N)^-1.
The actual four-low zero-shift Schur sign remains UNKNOWN / RH OPEN.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial
from hashlib import sha256

from .tate_bessel_seven_schur import odd_double_factorial
from .tate_suzuki_fourier_schur import gamma_fourier_multiplier_lower
from .apollo_derivative_jets import _source, true_third_prime_wavefronts
from .one_object_residual_schur import (
    ORIGINAL_SUZUKI_BLOB, parent_original_source_contract,
    original_source_cancellation_certificate,
)
from .suzuki_moment_schur import inverse_neumann_boundary_channels


class WeightedBesselSourceError(ValueError):
    """Invalid real arithmetic source, proof cutoff or sign transport."""


def _q(value):
    if type(value) not in (int,F):
        raise WeightedBesselSourceError("Exact proof scalar int/Fraction only")
    return F(value)


def _integer(value,lo=1,hi=256):
    if type(value) is not int or not lo<=value<=hi:
        raise WeightedBesselSourceError("Exact finite mathematical index required")
    return value


def _bessel_source_coefficients(ell,order):
    """j_l(z)=Σ_k c_k z^(ell+2k), classical NIST 10.53.1."""
    l=_integer(ell,0,64)
    K=_integer(order,0,32)
    coeff=[F(1,odd_double_factorial(2*l+1))]
    for k in range(K):
        coeff.append(-coeff[-1]/(2*(k+1)*(2*l+2*k+3)))
    return tuple(coeff)


def _bessel_series_absolute_error(ell,coeff,upper):
    """Uniform real-z error of Bessel polynomial for 0<=z<=upper."""
    l=_integer(ell,0,64)
    A=_q(upper)
    K=len(coeff)-1
    if A<=0:
        raise WeightedBesselSourceError("Positive frequency endpoint required")
    ratio=A*A/F(2*(K+2)*(2*l+2*K+5))
    if ratio>=1:
        raise WeightedBesselSourceError("Real Bessel remainder cannot be bounded geometrically")
    first=abs(coeff[-1])*A**(l+2*(K+1))/(
        2*(K+1)*(2*l+2*K+3)
    )
    return first/(1-ratio)


def _finite_bessel_integral_polynomial(m,L,order):
    """Exact antiderivative for Σ_(ell=m)^(L-1) (2ell+1) P_ell(z)^2.

    Coefficients use an ordinary polynomial in z; all integrals are
    Fraction-exact. Compiling one antiderivative avoids independent
    catastrophic-cancellation evaluations for each spectral cell.
    """
    mm=_integer(m,1,20);LL=_integer(L,mm+1,32);K=_integer(order,0,24)
    group={}
    modes=[]
    for ell in range(mm,LL):
        c=_bessel_source_coefficients(ell,K)
        modes.append((ell,c))
        for i,ci in enumerate(c):
            for j,cj in enumerate(c):
                power=2*ell+2*(i+j)+1
                group[power]=group.get(power,F())+F(2*ell+1)*ci*cj/power
    return tuple(sorted(group.items())),tuple(modes)


def weighted_Bessel_leakage_upper(m=4,J=128,Omega=F(13),a=F(1,2),
                                  angular_modes=16,series_order=12,
                                  error_slack=F(1,1000),spectral_cells=96):
    """Finite-rational *universal* weighted low Fourier loss bound.

    m_J(omega) monotone in |omega| and >=0, so
    Q_Gamma(f)>= m_J(Omega)||f||² -
      [∫_{|omega|<=Omega}(m_J(Omega)-m_J(|omega|))
        |fhat(omega)|² dω/(2pi)].

    If f annihilates power moments 0..m-1, the bracket <=
      (2/pi)∫_0^(aOmega) (m_J(Omega)-m_J(z/a))
            Σ_{ell>=m}(2ell+1)j_ell(z)^2 dz ||f||².
    Bound 2/pi < 2/3.

    Partition omega∈[0,Omega] into T exact rational cells.
    Since multiplier increases, the positive gap on each cell is
    upper-bounded by its LEFT endpoint weight.

    For finite angular modes ell=m..L-1, use an exact rational
    polynomial antiderivative for spherical j_l Taylor truncations and
    Young |P+error|²<=(1+eta)P²+(1+1/eta)error². The error is bounded
    at the RIGHT cell endpoint via full geometric series majorant.

    For omitted ell>=L, original integral representation gives
      |j_l(z)|<=z^l/(2l+1)!!,
    so full-band tail <= A^(2L+1)/((2L+1)!!)^2 /
                           [1-(A/(2L+3))^2].
    Multiply by the GLOBAL MAX m_J(Omega) to cover its spectral weight.

    This is a proved analytical all-f bound with finite exact calculations,
    NOT an approximation inferred from sampled frequencies or ζ zeros.
    """
    mm=_integer(m,1,16);j=_integer(J,1,256)
    O=_q(Omega);aa=_q(a);slack=_q(error_slack)
    L=_integer(angular_modes,mm+1,32)
    K=_integer(series_order,0,24)
    cells=_integer(spectral_cells,2,256)
    if O<=0 or aa<=0 or slack<=0:
        raise WeightedBesselSourceError("Positive actual Fourier/source geometry needed")
    A=aa*O
    if A>=2*L+3:
        raise WeightedBesselSourceError("High spherical Bessel angular tail not geometrically controlled")
    antiderivative,modes=_finite_bessel_integral_polynomial(mm,L,K)
    def Fpoly(z):
        return sum((coef*z**power for power,coef in antiderivative),F())
    gamma=gamma_fourier_multiplier_lower(O,j)
    weighted=F()
    prev_Z=F()
    prev_poly=F()
    for i in range(cells):
        freq_lo=O*i/cells
        freq_hi=O*(i+1)/cells
        Z=aa*freq_hi
        next_poly=Fpoly(Z)
        polynomial_piece=next_poly-prev_poly
        if polynomial_piece<0:
            raise ArithmeticError("Exact integral of positive squared polynomial went negative")
        band_slack=(1+slack)*polynomial_piece
        remainder=F()
        for ell,co in modes:
            d=_bessel_series_absolute_error(ell,co,Z)
            remainder+=(2*ell+1)*d*d
        band_slack+=(1+1/slack)*(Z-prev_Z)*remainder
        left_multiplier=(F(0) if i==0 else
                         gamma_fourier_multiplier_lower(freq_lo,j))
        gap=gamma-left_multiplier
        if gap<0 or band_slack<0:
            raise ArithmeticError("Gamma monotone source or positive Bessel bound broken")
        weighted+=gap*band_slack
        prev_Z=Z
        prev_poly=next_poly
    geom=(A/F(2*L+3))**2
    if not 0<geom<1:
        raise ArithmeticError("Original spectral angular tail ratio must lie in (0,1)")
    angular_tail=A**(2*L+1)/odd_double_factorial(2*L+1)**2/(1-geom)
    W=F(2,3)*(weighted+gamma*angular_tail)
    if W<=0:
        raise ArithmeticError("Positive weighted low-band leakage cannot vanish")
    return {
        "source":"CLASSICAL_LEGENDRE_BESSEL_TRUE_GAMMA_WEIGHTED_ENCLOSURE",
        "a":aa,"Omega":O,"vanishing_moments":mm,
        "Gamma_real_modes":j,
        "Gamma_multiplier_exact":gamma,
        "spectral_cells":cells,
        "finite_angular_modes":tuple(range(mm,L)),
        "angular_power_series_order":K,
        "Young_rational_slack":slack,
        "omitted_angular_mode_tail":angular_tail,
        "weighted_low_Fourier_leakage_exact_upper":W,
        "weighted_low_Fourier_leakage_below_2013over10000":W<F(2013,10000),
        "source_all_finite_band_and_angular_errors_included":True,
        "RH_proved":False,
    }


def exact_fraction_bytes(fraction):
    """Unambiguous integer big-endian representation, no huge decimal str.

    Some rational denominators have >4300 decimal digits. Never weaken a
    mathematical proof to floats or disable Python's integer text guard
    just to freeze a scientific receipt.
    """
    v=_q(fraction)
    def part(integer):
        sign=b"-" if integer<0 else b"+"
        raw=abs(integer).to_bytes(max(1,(abs(integer).bit_length()+7)//8),"big")
        return sign+len(raw).to_bytes(4,"big")+raw
    return part(v.numerator)+part(v.denominator)


def source_weighted_four_moment_certificate():
    """Original Weil source > 1/50 ||f||² on moment-null rank FOUR.

    At a=1/2 only genuine p=2 acts. Contact C_inf<43/8; prime
    two-cell symmetric shift norm 1 and w2<1/2.
    Negative sinh polar is ≤8*(a/2)^(2m)/(m!)² for m moment nulls,
    so for m=4 < 10^-6. Positive cosh and all omitted Γ modes PSD.

    Exact source Γ128(13)>6097/1000 and independently derived weighted
    Fourier loss W4<2013/10000. Source complete lower:
      > [6097/1000-2013/10000-47/8-1/1000000]
         ||f||² =20699/1000000 ||f||²>1/50||f||².
    This is ALL complex smooth compact original Weil f with 4
    vanished polynomial moments, not a 4-vector Galerkin toy or RH.
    """
    src=_source()
    if not (src.contact_iv().hi<F(43,8)
            and src.log2_iv().lo>F(1,2)
            and src.log2_iv().hi<F(7,10)):
        raise WeightedBesselSourceError("Original Weil real contact/prime2 source missing")
    p=tuple(x.n for x in true_third_prime_wavefronts(F(1)))
    if p!=(2,):
        raise WeightedBesselSourceError("Only true p=2 prime wavefront may be present")
    weight=src.log2_iv()*src.sqrt_inverse(2)
    if weight.lo<=0 or weight.hi>=F(1,2):
        raise WeightedBesselSourceError("Original Weil prime half-density is invalid")
    a=F(1,2)
    data=weighted_Bessel_leakage_upper(
        m=4,J=128,Omega=F(13),a=a,
        angular_modes=16,series_order=12,error_slack=F(1,1000),
        spectral_cells=96
    )
    G=data["Gamma_multiplier_exact"]
    W=data["weighted_low_Fourier_leakage_exact_upper"]
    polar=F(8)*(a/2)**8/factorial(4)**2
    lower=G-W-F(47,8)-polar
    simple=F(6097,1000)-F(2013,10000)-F(47,8)-F(1,1000000)
    if not (G>F(6097,1000) and W<F(2013,10000)
            and polar<F(1,1000000) and
            lower>simple>F(1,50)):
        raise ArithmeticError("TRUE original completed Weil four-moment positivity FAILS")
    fingerprint=sha256(
        b"SUCC-BESSEL4-SOURCE-20261015\x00"+
        exact_fraction_bytes(G)+exact_fraction_bytes(W)+
        exact_fraction_bytes(lower)
    ).hexdigest()
    return {
        "source":"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_FIRST_PRIME",
        "source_suzuki_blob":ORIGINAL_SUZUKI_BLOB,
        "halfwidth":a,"genuine_prime_power_labels":p,
        "real_Gamma_J":128,"Fourier_Omega":F(13),
        "vanishing_polynomial_moments":4,
        "exact_positive_Gamma_multiplier":G,
        "exact_weighted_Bessel_leakage_upper":W,
        "negative_pole_moment_tail_upper":polar,
        "true_contact_plus_p2_bound":F(47,8),
        "original_Weil_L2_lower_exact":lower,
        "elementary_rational_lower":simple,
        "source_fraction_bytes_sha256":fingerprint,
        "completed_Weil_four_moment_strictly_above_1over50":True,
        "genuine_four_moment_infinite_dimensional_test_class":True,
        "first_prime_all_test_Weil_positivity_proved":False,
        "all_radii_low_Schur_positivity_proved":False,
        "RH_proved":False,
    }


def true_four_low_suzuki_interface():
    """Actual original signed Suzuki K-relative high proof with only P1..P4 low.

    For derivative u∈L²_0 orthogonal to genuine Legendre P1..P4, the
    Neumann primitive f=Vu∈H0¹ has power moments 0..3 zero.
    Q_zeta(f)=<u,Gu> and <u,Ku>=||Vu||², so
      Q4GQ4 >=(1/50)Q4KQ4, K=V*V=(-Delta_N)^-1.
    True source PR109 ||g'||1<11/40 gives
      R0 <= [(11/40)^2/(1/50)] I4=121/32 I4.
    The 4x4 original low short S0=A-R0 is OPEN.
    """
    true=source_weighted_four_moment_certificate()
    source=parent_original_source_contract()
    if (source["source_git_blob_sha"]!=ORIGINAL_SUZUKI_BLOB or
            not source["original_screw_value_checked_against_derivative"]):
        raise WeightedBesselSourceError("Original Suzuki source passport is incompatible")
    norm=original_source_cancellation_certificate()
    if norm["gprime_L1_STRICT_upper"]>=F(11,40):
        raise WeightedBesselSourceError("True signed original derivative budget invalid")
    k=inverse_neumann_boundary_channels(F(1,2),4)
    if k["K_low_high_cross_rank"]!=2:
        raise WeightedBesselSourceError("Original inverse Neumann low/high K rank drift")
    return {
        "source":"ORIGINAL_SUZUKI_SIGNED_FOUR_LOW_ZERO_SHIFT",
        "radius":F(1,2),
        "true_prime_power_labels":true["genuine_prime_power_labels"],
        "low_Legendre_modes":(1,2,3,4),
        "low_dimension":4,
        "reflection_parity_low_blocks":(2,2),
        "true_K_inverse_Neumann":"V*V=(-Delta_N)^-1 on meanzero derivative u",
        "K_low_high_source_boundary_rank":2,
        "genuine_high_relative_K_kappa":F(1,50),
        "genuine_R0_zero_shift_norm_upper":F(121,32),
        "zero_shift_Douglas_range_and_finiteness":True,
        "actual_complete_low_4x4_S0_sign_proved":False,
        "original_full_first_prime_all_f_positive_proved":False,
        "all_a_global_Weil_positive_proved":False,
        "RH_proved":False,
    }
