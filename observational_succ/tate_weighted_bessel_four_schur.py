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


KAPPA_ODD_LOWER = F(63, 500)
KAPPA_EVEN_LOWER = F(153, 500)
KAPPA_GLOBAL_SHARPENED = F(63, 500)


def _parity_bessel_integral_polynomial(m, L, order):
    """Exact antiderivative for sum_{ell=m, ell==m (mod 2)}^{L-1} (2*ell+1) P_ell(z)^2.

    When w in Q_4 H has definite reflection parity, f = Vw in H_0^1(-a,a) has the
    OPPOSITE reflection parity:
      - w odd  => f = Vw even => <f, P_{2k+1}> = 0 for all k => only even ell=4,6,8,... active.
      - w even => f = Vw odd  => <f, P_{2k}> = 0 for all k (including P_4!) => only odd ell=5,7,9,... active.
    """
    mm = _integer(m, 1, 20)
    LL = _integer(L, mm + 1, 32)
    K = _integer(order, 0, 24)
    group = {}
    modes = []
    for ell in range(mm, LL, 2):
        c = _bessel_source_coefficients(ell, K)
        modes.append((ell, c))
        for i, ci in enumerate(c):
            for j, cj in enumerate(c):
                power = 2 * ell + 2 * (i + j) + 1
                group[power] = group.get(power, F()) + F(2 * ell + 1) * ci * cj / power
    return tuple(sorted(group.items())), tuple(modes)


def parity_weighted_Bessel_leakage_upper(
    sector="odd", J=256, Omega=None, a=F(1, 2),
    angular_modes=20, series_order=14,
    error_slack=F(1, 2000), spectral_cells=128,
):
    """Parity-refined weighted low-Fourier Bessel leakage upper bound on Q_4 H_{sector}.

    Uses:
      1. Exact parity selection on f = Vw:
         - sector='odd'  (w odd,  f=Vw even): active angular modes ell in {4, 6, 8, ...};
         - sector='even' (w even, f=Vw odd):  active angular modes ell in {5, 7, 9, ...}.
      2. Source-pinned 2/pi upper bound `2 / _source().pi_iv().lo < 2/3`.
    """
    if sector not in ("odd", "even"):
        raise WeightedBesselSourceError("sector must be 'odd' or 'even'")
    m_start = 4 if sector == "odd" else 5
    if Omega is None:
        Omega = F(16) if sector == "odd" else F(18)
    j = _integer(J, 1, 256)
    O = _q(Omega)
    aa = _q(a)
    slack = _q(error_slack)
    L = _integer(angular_modes, m_start + 2, 32)
    K = _integer(series_order, 0, 24)
    cells = _integer(spectral_cells, 2, 256)
    if O <= 0 or aa <= 0 or slack <= 0:
        raise WeightedBesselSourceError("Positive Fourier/source geometry required")
    A = aa * O
    if A >= 2 * L + 3:
        raise WeightedBesselSourceError("High spherical Bessel angular tail not geometrically controlled")
    src = _source()
    two_over_pi_hi = F(2) / src.pi_iv().lo
    if not F(3, 5) < two_over_pi_hi < F(2, 3):
        raise WeightedBesselSourceError("Pinned source pi interval invalid")
    antiderivative, modes = _parity_bessel_integral_polynomial(m_start, L, K)

    def Fpoly(z):
        return sum((coef * z ** power for power, coef in antiderivative), F())

    gamma = gamma_fourier_multiplier_lower(O, j)
    weighted = F()
    prev_Z = F()
    prev_poly = F()
    for i in range(cells):
        freq_lo = O * i / cells
        freq_hi = O * (i + 1) / cells
        Z = aa * freq_hi
        next_poly = Fpoly(Z)
        polynomial_piece = next_poly - prev_poly
        if polynomial_piece < 0:
            raise ArithmeticError("Exact integral of positive squared polynomial went negative")
        band_slack = (1 + slack) * polynomial_piece
        remainder = F()
        for ell, co in modes:
            d = _bessel_series_absolute_error(ell, co, Z)
            remainder += (2 * ell + 1) * d * d
        band_slack += (1 + 1 / slack) * (Z - prev_Z) * remainder
        left_multiplier = F(0) if i == 0 else gamma_fourier_multiplier_lower(freq_lo, j)
        gap = gamma - left_multiplier
        if gap < 0 or band_slack < 0:
            raise ArithmeticError("Gamma monotone source or positive Bessel bound broken")
        weighted += gap * band_slack
        prev_Z = Z
        prev_poly = next_poly
    geom = (A / F(2 * L + 3)) ** 2
    if not 0 < geom < 1:
        raise ArithmeticError("Spectral angular tail ratio must lie in (0,1)")
    angular_tail = A ** (2 * L + 1) / odd_double_factorial(2 * L + 1) ** 2 / (1 - geom)
    W = two_over_pi_hi * (weighted + gamma * angular_tail)
    return {
        "source": "PARITY_REFINED_LEGENDRE_BESSEL_GAMMA_WEIGHTED_ENCLOSURE",
        "derivative_sector": sector,
        "primitive_Vw_parity": "even" if sector == "odd" else "odd",
        "first_active_angular_mode": m_start,
        "active_angular_modes": tuple(ell for ell, _ in modes),
        "a": aa,
        "Omega": O,
        "Gamma_real_modes": j,
        "Gamma_multiplier_exact": gamma,
        "two_over_pi_upper": two_over_pi_hi,
        "weighted_low_Fourier_leakage_exact_upper": W,
        "RH_proved": False,
    }


def source_parity_split_four_moment_coercivity_certificate():
    """Sharpened high-sector K-coercivity certificate on Q_4 H = Q_4 H_odd (+) Q_4 H_even:

        D_{4,odd}  >= (63/500)  K_odd   (kappa_odd  = 0.126 > 6.3  * (1/50))
        D_{4,even} >= (153/500) K_even  (kappa_even = 0.306 > 15.3 * (1/50))
        D_4        >= (63/500)  Q_4 K Q_4.

    Mathematical mechanism:
      1. Both G and K = V^*V commute with reflection (Rf)(t) = f(-t), so Q_4 H splits
         orthogonally into Q_4 H_odd and Q_4 H_even.
      2. For w in Q_4 H_odd, f = Vw is EVEN: <f, sinh(t/2)> = 0 identically (zero
         negative pole leakage) and only even spherical Bessel modes ell=4,6,8,... enter.
      3. For w in Q_4 H_even, f = Vw is ODD: <f, P_4(2t)> = 0 automatically, so f in V_5
         (5 vanishing moments 0..4) and only odd spherical Bessel modes ell=5,7,9,... enter.
      4. Uses the pinned source interval upper bounds `contact_iv().hi` and
         `(log2_iv() * sqrt_inverse(2)).hi` (< 5.83902 vs coarse 47/8 = 5.875) and
         `2 / pi_iv().lo` (< 0.63662 vs coarse 2/3).
    """
    src = _source()
    source_contract = parent_original_source_contract()
    if source_contract["source_git_blob_sha"] != ORIGINAL_SUZUKI_BLOB:
        raise WeightedBesselSourceError("Original Suzuki source blob mismatch")
    p = tuple(x.n for x in true_third_prime_wavefronts(F(1)))
    if p != (2,):
        raise WeightedBesselSourceError("Only true p=2 prime wavefront active at a=1/2")
    c_hi = src.contact_iv().hi
    w2_hi = (src.log2_iv() * src.sqrt_inverse(2)).hi
    if not (F(5) < c_hi < F(43, 8) and F(0) < w2_hi < F(1, 2)):
        raise WeightedBesselSourceError("Pinned source contact/prime2 interval out of bounds")
    contact_plus_p2_hi = c_hi + w2_hi

    odd_leak = parity_weighted_Bessel_leakage_upper(
        sector="odd", J=256, Omega=F(16), a=F(1, 2),
        angular_modes=20, series_order=14, error_slack=F(1, 2000), spectral_cells=128,
    )
    even_leak = parity_weighted_Bessel_leakage_upper(
        sector="even", J=256, Omega=F(18), a=F(1, 2),
        angular_modes=21, series_order=14, error_slack=F(1, 2000), spectral_cells=128,
    )
    # Odd derivative sector: f = Vw is even => <f, sinh(t/2)> = 0 identically!
    odd_polar = F(0)
    # Even derivative sector: f = Vw is odd in V_5 => m=5 polar bound 8*(1/4)^10 / (5!)^2
    even_polar = F(8) * (F(1, 4) ** 10) / (factorial(5) ** 2)

    kappa_odd_exact = (
        odd_leak["Gamma_multiplier_exact"]
        - odd_leak["weighted_low_Fourier_leakage_exact_upper"]
        - contact_plus_p2_hi
        - odd_polar
    )
    kappa_even_exact = (
        even_leak["Gamma_multiplier_exact"]
        - even_leak["weighted_low_Fourier_leakage_exact_upper"]
        - contact_plus_p2_hi
        - even_polar
    )
    if not (kappa_odd_exact > KAPPA_ODD_LOWER > F(1, 8) > F(1, 50)):
        raise ArithmeticError("Certified odd-sector coercivity fell below 63/500")
    if not (kappa_even_exact > KAPPA_EVEN_LOWER > F(3, 10) > KAPPA_ODD_LOWER):
        raise ArithmeticError("Certified even-sector coercivity fell below 153/500")

    return {
        "source": "SHA_PINNED_PARITY_SPLIT_BESSEL_FOUR_MOMENT_COERCIVITY",
        "source_suzuki_blob": ORIGINAL_SUZUKI_BLOB,
        "halfwidth": F(1, 2),
        "genuine_prime_power_labels": p,
        "contact_plus_p2_exact_upper": contact_plus_p2_hi,
        "odd_sector": {
            "Fourier_Omega": F(16),
            "real_Gamma_J": 256,
            "active_angular_modes": odd_leak["active_angular_modes"],
            "Gamma_multiplier_exact": odd_leak["Gamma_multiplier_exact"],
            "weighted_Bessel_leakage_upper": odd_leak["weighted_low_Fourier_leakage_exact_upper"],
            "negative_pole_leakage_upper": odd_polar,
            "kappa_odd_exact_lower": kappa_odd_exact,
            "kappa_odd_certified_rational": KAPPA_ODD_LOWER,
            "improvement_factor_over_1_over_50": KAPPA_ODD_LOWER / F(1, 50),
        },
        "even_sector": {
            "Fourier_Omega": F(18),
            "real_Gamma_J": 256,
            "active_angular_modes": even_leak["active_angular_modes"],
            "Gamma_multiplier_exact": even_leak["Gamma_multiplier_exact"],
            "weighted_Bessel_leakage_upper": even_leak["weighted_low_Fourier_leakage_exact_upper"],
            "negative_pole_leakage_upper": even_polar,
            "kappa_even_exact_lower": kappa_even_exact,
            "kappa_even_certified_rational": KAPPA_EVEN_LOWER,
            "improvement_factor_over_1_over_50": KAPPA_EVEN_LOWER / F(1, 50),
        },
        "global_kappa_lower": KAPPA_GLOBAL_SHARPENED,
        "parity_split_valid_by_reflection_commutation": True,
        "RH_proved": False,
    }

