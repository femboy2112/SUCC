"""Source-covariant SUCC/FUCC localization: exact finite algebra and source gates.

The finite Fraction model is an exact *discrete model* of the identities proved
in research/2026-10-17/SOURCE_COVARIANT_IMS_AND_BAND_CUTOFF.md.  It is NOT a
numerical or analytic discretization that authenticates original Suzuki G.
The separate source gate byte-checks the existing ORIGINAL source and computes
only finite rational *bounds*, not its full spectrum or Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from typing import Sequence


class LocalizationError(ValueError):
    pass


def q(value):
    if type(value) not in (int, F):
        raise LocalizationError("exact int/Fraction required; floats and bools rejected")
    return F(value)


def _vec(values):
    v = tuple(q(x) for x in values)
    if not v:
        raise LocalizationError("nonempty exact vector required")
    return v


def _prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def prime_power_parent(n):
    """True one-prime-power label; a composite 6 is not an Euler impulse."""
    if type(n) is not int or n < 2:
        raise LocalizationError("integer prime-power source label >=2 required")
    if _prime(n):
        return n
    for p in range(2, isqrt(n) + 1):
        if not _prime(p):
            continue
        m = p * p
        while m < n:
            m *= p
        if m == n:
            return p
    return None


def affine_succ_fucc_square(n, p):
    """An exact source arithmetic square, not a unitary embedding in L2(R).

    The distributional map e_n -> delta_(log n) intertwines V_p with
    translation by log p, but additive S acts with state-dependent log steps.
    """
    if type(n) is not int or n < 1 or not _prime(p):
        raise LocalizationError("positive unit-origin state and genuine prime required")
    return {
        "Vp_after_S": p * (n + 1),
        "Sp_after_Vp": p * n + p,
        "commuting_square": True,
        "additive_SUCC_is_fixed_log_translation": False,
        "Hilbert_space_unitary_equivalence_claimed": False,
    }


@dataclass(frozen=True)
class FiniteToySource:
    """Rational graph surrogate; not authenticated Suzuki or an Euler source."""
    jump: tuple[tuple[F, ...], ...]
    lag_weights: tuple[tuple[int, F], ...]
    contact: F
    pole_cosh: tuple[F, ...]
    pole_sinh: tuple[F, ...]

    def __post_init__(self):
        n = len(self.jump)
        if n < 2 or any(len(row) != n for row in self.jump):
            raise LocalizationError("jump matrix must be square, size >=2")
        if any(type(x) is not F for row in self.jump for x in row):
            raise LocalizationError("explicit Fraction jump weights required")
        for i in range(n):
            if self.jump[i][i] != 0:
                raise LocalizationError("jump diagonal must be zero")
            for j in range(n):
                if self.jump[i][j] < 0 or self.jump[i][j] != self.jump[j][i]:
                    raise LocalizationError("symmetric nonnegative jump kernel required")
        if type(self.contact) is not F or self.contact < 0:
            raise LocalizationError("nonnegative exact contact required")
        if len(self.pole_cosh) != n or len(self.pole_sinh) != n or any(
            type(x) is not F for x in self.pole_cosh + self.pole_sinh
        ):
            raise LocalizationError("exact polar channel lengths required")
        seen = set()
        for b, w in self.lag_weights:
            if type(b) is not int or not 1 <= b < n or type(w) is not F or w < 0 or b in seen:
                raise LocalizationError("distinct finite positive shift and exact nonnegative weight")
            seen.add(b)

    @property
    def length(self):
        return len(self.jump)

    def components(self, values):
        f = _vec(values)
        n = self.length
        if len(f) != n:
            raise LocalizationError("source vector length mismatch")
        gamma = sum((self.jump[i][j] * (f[i] - f[j]) ** 2
                     for i in range(n) for j in range(n)), F()) / 2
        prime = sum((-2 * w * sum((f[i] * f[i + lag] for i in range(n - lag)), F())
                     for lag, w in self.lag_weights), F())
        contact = -self.contact * sum((z * z for z in f), F())
        c = sum((self.pole_cosh[i] * f[i] for i in range(n)), F())
        s = sum((self.pole_sinh[i] * f[i] for i in range(n)), F())
        polar = 2 * (c * c - s * s)
        return {"Gamma_jump":gamma,"prime_shift":prime,"contact":contact,
                "completed_polar":polar,"total":gamma + prime + contact + polar}


def finite_ims(source: FiniteToySource, values, chart_rows):
    """Exact signed IMS including prime-shift and rank-two pole interfaces.

    All arithmetic is rational.  The partition rows chi_j obey sum_j chi_j^2=1
    sitewise.  The correction terms are *not positive operators in general*.
    """
    if type(source) is not FiniteToySource:
        raise LocalizationError("finite mathematical source explicitly required")
    f = _vec(values)
    n = source.length
    if len(f) != n:
        raise LocalizationError("source length mismatch")
    charts = tuple(_vec(row) for row in chart_rows)
    if not charts or any(len(row) != n for row in charts):
        raise LocalizationError("complete finite chart family required")
    if any(sum((row[i] ** 2 for row in charts), F()) != 1 for i in range(n)):
        raise LocalizationError("partition sum chi_j^2 = 1 must hold at every site")
    source_Q = source.components(f)
    local = tuple(source.components(tuple(row[i] * f[i] for i in range(n)))
                  for row in charts)
    total_local = sum((item["total"] for item in local), F())
    chi_diff = lambda i,j: sum(((row[i] - row[j]) ** 2 for row in charts), F())
    gamma_iface = sum((source.jump[i][j] * f[i] * f[j] * chi_diff(i, j)
                      for i in range(n) for j in range(n)), F()) / 2
    prime_iface = sum((w * sum((f[i] * f[i + lag] * chi_diff(i, i + lag)
                                for i in range(n - lag)), F())
                       for lag, w in source.lag_weights), F())
    pole_iface = source_Q["completed_polar"] - sum(
        (item["completed_polar"] for item in local), F())
    assert source_Q["contact"] == sum((item["contact"] for item in local), F())
    reconstructed = total_local - gamma_iface - prime_iface + pole_iface
    if reconstructed != source_Q["total"]:
        raise ArithmeticError("IMS algebra failed: missing/laundered source interface")
    return {"actual":source_Q["total"],"reconstructed":reconstructed,
            "local_total":total_local,"Gamma_interface":gamma_iface,
            "prime_interface":prime_iface,"polar_reassembly":pole_iface,
            "contact_cancels_exactly":True,
            "original_Suzuki_source_authenticated":False,
            "global_Weil_sign_proved":False,"RH_proved":False}


def first_legendre_prime_overlap(a, b):
    """Exact original first-Legendre prime lag/hinge channel for rational b.

    For u=P1(x/a)=x/a, F=(x²-a²)/(2a), and 0<b<2a, prove:
        <F,T_b F> = ((2a-b)^3*(4a²+6ab+b²))/(120 a²).
    The original hinge Q_hinge = -2 * w * this number.  There is NO
    claim a supplied rational b equals log(p); the source gate supplies that.
    """
    a, b = q(a), q(b)
    if a <= 0 or not 0 < b < 2*a:
        raise LocalizationError("lawful positive radius and strictly active lag")
    corr = ((2*a-b)**3 * (4*a*a+6*a*b+b*b)) / (120*a*a)
    return {"lag_correlation":corr,"hinge_energy_per_unit_weight":-2*corr,
            "contact_or_gamma_included":False,"source_prime_authenticated":False}



def gamma_prefix_multiplier(xi, limit=4096):
    """Exact finite, *authentic-formula* Gamma multiplier partial sum.

    Proves the rational comparison 4*xi^2/[d(xi^2+d^2/4)] >= 16/(5*d)
    for every retained d=4j+1<=xi.  The analytic harmonic -> logarithmic
    lower bound is in the companion paper; no transcendental float is used.
    """
    xi = q(xi)
    if xi < 1:
        raise LocalizationError("xi >= 1 required")
    n = int((xi - 1) // 4)
    if n + 1 > limit:
        raise LocalizationError("explicit finite mode budget; use paper harmonic bound")
    terms = tuple(4 * xi * xi / (F(4 * j + 1) * (xi * xi + F((4 * j + 1) ** 2, 4)))
                  for j in range(n + 1))
    lower = sum((F(16, 5 * (4 * j + 1)) for j in range(n + 1)), F())
    actual = sum(terms, F())
    if actual < lower:
        raise ArithmeticError("Gamma multiplier comparison failed")
    return {"mode_count":n+1,"partial_multiplier":actual,
            "rational_harmonic_lower":lower,"global_source_multiplier_certified":False}


def first_prime_window_frequency_packet():
    """All-rational analytic cutoff packet, *conditional on source bounds*.

    The source adapter below must verify gamma/contact/prime provenance.
    Proves: if Q_original(F')<0 then more than half of ||F||^2 is in
    Fourier band |xi| <= 2^24, at a=1/2, given the paper Fourier identity.
    Also a finite rational-midpoint Fourier grid of 2^49 points captures >1/3
    of ||F||^2 (assuming actual lawful Fourier evaluation of F).
    """
    log2_lower = 2 * sum((F(1, 3 ** (2 * j + 1) * (2 * j + 1))
                          for j in range(3)), F())
    if not log2_lower > F(69, 100):
        raise ArithmeticError("elementary log(2) source lower bound failed")
    B_upper = F(43, 8) + 1 + F(1, 16)  # contact, prime2, negative sine polar
    R = 2 ** 24
    gamma_floor = F(4, 5) * 24 * F(69, 100)
    if not gamma_floor > 2 * B_upper:
        raise ArithmeticError("specified finite spectral band is not sufficient")
    return {"a":"1/2","negative_source_budget_upper":str(B_upper),
            "log2_exact_rational_lower":str(log2_lower),
            "high_Gamma_multiplier_rational_floor":str(gamma_floor),
            "band_radius":R,"Fourier_midpoint_sample_count":2 * R * R,
            "negative_direction_low_band_mass_fraction_strict_lower":"1/2",
            "negative_direction_finite_sample_mass_fraction_strict_lower":"1/3",
            "conditional_on_authentic_completed_signed_source":True,
            "analytic_proof_in_companion_dossier":True,
            "negative_original_direction_exhibited":False,
            "RH_proved":False}


def authenticated_first_prime_window_packet():
    """Fail-closed source check, not a claim that such a negative test exists."""
    from .source_weil_hierarchy import (authenticated_prime_wavefront,
                                         contact_iv, log2_iv, sqrt_inverse)
    from .tate_suzuki_shorting import verify_original_suzuki_source
    original = verify_original_suzuki_source()  # exact Git source blob
    if authenticated_prime_wavefront(F(1,2)) != ((2,2),):
        raise LocalizationError("genuine prime-2-only wavefront mismatch")
    if contact_iv().hi >= F(43,8):
        raise LocalizationError("actual completed source contact is outside analytic band budget")
    if (log2_iv() * sqrt_inverse(2)).hi >= F(1,2):
        raise LocalizationError("true prime2 half-density source outside budget")
    ret = first_prime_window_frequency_packet()
    return dict(ret, pinned_source_blob=original["source_git_blob"],
                genuine_wavefront=((2,2),),
                source_gate_verified=True)
