"""Exact family of admissible but noncanonical Fourier-self-dual zeta completions.

A *virtual zero* here means a zero of an admissible C_epsilon(s) times the
standard completed zeta, under a restricted source-observation signature
that does NOT identify epsilon. It is NOT a zero of actual Riemann zeta.

All tests/proof certificates here are rational inequalities and exact
Mellin samples, with analytic Gaussian Fourier/Hurwitz theorems provided
separately in the dossier. No unknown zeta zeros are input or queried.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Sequence

from .diagonal_adele_zeta import DiagonalSourceError


def _f(v: object) -> F:
    if type(v) in (int, F):
        return F(v)
    raise DiagonalSourceError("Only exact rational Archimedean source parameters")


def mellin_factor_integer(epsilon: int | F, s: int) -> F:
    """C_e(s)=(1+e*(4^-s+4^(s-1)))/(1+5e/4), integer s."""
    e = _f(epsilon)
    if e < 0 or type(s) is not int:
        raise DiagonalSourceError("Nonnegative real Gaussian-pair weight, integer Mellin index")
    return (1 + e * (F(4) ** (-s) + F(4) ** (s - 1))) / (1 + F(5, 4) * e)


def epsilon_from_mellin2(value: int | F) -> F:
    """Invert a genuinely measured exact C_e(2) within the declared family.

    This is a model-dependent identification, NOT a derivation from finite
    Euler primes or an observer seeing only normalization/Fourier symmetry.
    """
    m = _f(value)
    if not 1 <= m < F(13, 4):
        raise DiagonalSourceError("Impossible exact C(2) for finite epsilon >= 0")
    e = F(16) * (m - 1) / (65 - 20 * m)
    if e < 0 or mellin_factor_integer(e, 2) != m:
        raise AssertionError("Exact Mellin source-identification fails")
    return e


def zero_class(epsilon: int | F) -> str:
    """Classify zeros of C_e on the CLOSED critical strip, exactly.

    Set t=4^(s-1/2), and for epsilon>0 obtain
      t^2+(2/epsilon)t+1=0.
    For 0<epsilon<1, negative reciprocal roots have |t|=R and 1/R.
    The critical strip condition 1<R<2 is exactly 4/5<epsilon<1.
    """
    e = _f(epsilon)
    if e < 0:
        raise DiagonalSourceError("Negative coefficients break source-positive family")
    if e == 0:
        return "CANONICAL_MULTIPLIER_NO_ZEROS"
    if e < F(4, 5):
        return "EXTRA_ZEROS_OUTSIDE_CLOSED_CRITICAL_STRIP"
    if e == F(4, 5):
        return "EXTRA_ZEROS_ON_CRITICAL_STRIP_BOUNDARY"
    if e < 1:
        return "EXTRA_OFFLINE_ZEROS_INSIDE_OPEN_CRITICAL_STRIP"
    if e == 1:
        return "EXTRA_DOUBLE_ZEROS_ON_CRITICAL_LINE"
    return "EXTRA_ZEROS_ON_CRITICAL_LINE"


def model_completion_receipt(epsilon: int | F) -> dict:
    """Observable source signature and algebraic root-location certificate.

    Full exact zeta zeros and Fourier transforms are not computed here.
    The analytic Fourier-self-dual source is
      f_e=(G1+e G16+(e/4) G1/16)/(1+5e/4).
    Gaussian Fourier identity and Mellin integrals justify the formulas.
    """
    e = _f(epsilon)
    status = zero_class(e)
    if mellin_factor_integer(e, 0) != 1 or mellin_factor_integer(e, 1) != 1:
        raise AssertionError("Pole/normalization signature broken")
    f2 = mellin_factor_integer(e, 2)
    if epsilon_from_mellin2(f2) != e:
        raise AssertionError("Independent one-probe model selector broken")
    quad = None if e == 0 else (F(1), F(2) / e, F(1))
    if e == F(10, 11):
        if quad != (F(1), F(11, 5), F(1)):
            raise AssertionError("Prior DZ9 witness recovered incorrectly")
    return {
        "epsilon": e, "source_positive_Schwartz": True,
        "source_normalized_at_zero": True,
        "source_Fourier_self_dual_analytically": True,
        "finite_Euler_factors_unchanged": True,
        "functional_equation_symmetry": True,
        "Mellin_C0": mellin_factor_integer(e, 0),
        "Mellin_C1": mellin_factor_integer(e, 1),
        "Mellin_C2": f2,
        "quadratic_t_constant_first": quad,
        "zero_classification": status,
        "zero_locations_derived_from_zeta_zeros": False,
        "actual_Riemann_zeta_modified": False,
    }


@dataclass(frozen=True)
class VirtualCompletionObserver:
    """One observer's currently admissible alternative source completions.

    The observer knows only an exact interval of epsilon values. This is a
    SOURCE CLASS, not a statement that the world randomizes epsilon.
    """
    lower: F
    upper: F
    source_id: str
    source_version: int = 0

    def __post_init__(self) -> None:
        lo, hi = _f(self.lower), _f(self.upper)
        if lo < 0 or hi < lo or not self.source_id or type(self.source_version) is not int or self.source_version < 0:
            raise DiagonalSourceError("Source hypothesis interval and provenance required")
        object.__setattr__(self, 'lower', lo)
        object.__setattr__(self, 'upper', hi)

    def classify(self) -> dict:
        lo, hi = self.lower, self.upper
        possible_offline = (hi > F(4, 5) and lo < 1)
        forced_offline = (lo > F(4, 5) and hi < 1)
        canonical_possible = lo == 0
        return {
            "source_id": self.source_id, "source_version": self.source_version,
            "epsilon_interval": (lo, hi),
            "offcritical_strip_zero_possible_in_a_completion": possible_offline,
            "offcritical_strip_zero_forced_in_every_completion": forced_offline,
            "canonical_completion_still_possible": canonical_possible,
            "canonical_zeta_offcritical_zero_claimed": False,
            "physical_measurement_authenticated": False,
        }

    def observe_exact_mellin2(self, result: int | F, *,
                              source_id: str, source_version: int) -> 'VirtualCompletionObserver':
        if source_id != self.source_id or source_version != self.source_version:
            raise DiagonalSourceError("Stale or mismatched source/basis observational report")
        e = epsilon_from_mellin2(result)
        if not self.lower <= e <= self.upper:
            raise DiagonalSourceError("Measured Mellin constraint inconsistent with source class")
        return VirtualCompletionObserver(e, e, self.source_id, self.source_version + 1)


def virtual_zero_parameter_threshold_report(epsilon: int | F) -> dict:
    """Exact critical-strip threshold + compact-normal-limit countercontrol.

    For epsilon<4/5, the whole closed strip obeys
    |epsilon*(4^-s+4^(s-1))|<=5 epsilon/4<1.
    All zeros of C_e therefore leave that strip. As epsilon->0,
    C_e->1 uniformly on compact subsets of C and by Hurwitz no zero
    can persist in a fixed compact where the limit 1 is nonzero.
    """
    e = _f(epsilon)
    status = zero_class(e)
    return {
        "epsilon": e,
        "source_class_status": status,
        "strict_stripsup_bound": F(5,4)*e,
        "proves_no_C_zeros_in_closed_strip_by_triangle": e < F(4,5),
        "root_equation_valid_for_e_positive": e > 0,
        "compact_convergence_to_one_as_e_to_zero": True,
        "no_C_zeros_persist_on_any_fixed_compact_in_limit": True,
        "Hurwitz_assumptions_needed": "holomorphic and locally uniform convergence",
        "RH_or_zero_free_statement_about_xi": False,
    }


def positive_gaussian_mixture_mellin2(
        sources: Sequence[tuple[int | F, int | F]]) -> dict:
    """Rigidity of ONE Mellin observation in positive selfdual Gaussian mixtures.

    Each pair f_r=[G_(r²)+r^-1 G_(r^-2)]/(1+r^-1), for r>0, is
    normalized positive Fourier-selfdual, and
      C_r(2) = r + r^-1 - 1,
      C_r(2)-1 = (r-1)^2/r >=0.
    A finite nonnegative convex mixture of f_r therefore has C(2)=1
    iff every positive-weight component has r=1, i.e. the canonical G1.
    This does NOT establish uniqueness among all Schwartz selfdual tests.
    """
    data = tuple((_f(r), _f(w)) for r, w in sources)
    if not data or any(r <= 0 or w < 0 for r, w in data):
        raise DiagonalSourceError("Positive scales and nonnegative finite weights required")
    total = sum((w for _,w in data), F())
    if total <= 0:
        raise DiagonalSourceError("Nontrivial positive total Gaussian test weight required")
    gap = sum((w * (r-1)**2 / r for r,w in data), F()) / total
    value = sum((w * (r + 1/r - 1) for r,w in data), F()) / total
    if value != 1+gap or gap < 0:
        raise AssertionError("Gaussian mixture Mellin rigidity fails")
    canonical = all(w == 0 or r == 1 for r, w in data)
    if canonical != (gap == 0):
        raise AssertionError("Positivity of mixture is load-bearing")
    return {"Mellin2": value, "nonnegative_rigidity_gap": gap,
            "unique_canonical_G1_in_declared_mixture_class": canonical,
            "full_Schwartz_class_uniqueness_claimed": False}
