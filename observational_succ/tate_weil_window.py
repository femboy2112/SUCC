"""Support-aware true von Mangoldt wavefront for compact Weil tests.

Only exact finite source reconstruction and a conservative proof-bearing
integer cutoff. Real Gamma/poles and their uniform analytic estimates are
provided by existing completed_weil_transport infrastructure and are NOT
replaced by the finite source table. No positivity claims.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .completed_weil_transport import von_mangoldt_labels
from .diagonal_adele_zeta import rational


class WeilWindowError(ValueError):
    """Unsupported source cutoff, missing actual prime or compact domain."""


@dataclass(frozen=True)
class CompactWeilSourceWindow:
    """Observer access for tests phi supported in [-a,a], a>0 rational."""
    a: F

    def __post_init__(self):
        try:
            v = rational(self.a)
        except ValueError as err:
            raise WeilWindowError("A rational support horizon is required") from err
        if v <= 0:
            raise WeilWindowError("Positive test half-support required")
        object.__setattr__(self, "a", v)

    @property
    def exponent_ceiling(self) -> int:
        """Smallest integer L >= 2a: 0<2a<=L and exp(2a)<3^L."""
        r = 2*self.a
        return (r.numerator+r.denominator-1)//r.denominator

    @property
    def source_ceiling(self) -> int:
        """INTEGER upper bound on every genuine prime-power impulse in h."""
        L = self.exponent_ceiling
        if L > 10:
            raise WeilWindowError("No silent oversampling beyond 3^10")
        return 3**L

    def certificate(self) -> dict:
        N = self.source_ceiling
        # f supported [-a,a] => autocorrelation supported [-2a,2a].
        # If n>=3^ceil(2a), log n>=ceil(2a)log 3>2a, so h(log n)=0.
        # e<3 follows from the factorial series (n!>=2^(n-1)).
        labels = von_mangoldt_labels(N-1)
        if any(n >= N for n,p in labels):
            raise AssertionError("Outside-prime support leaked into finite oracle")
        if any(n==6 for n,p in labels):
            raise AssertionError("Fake composite 6 is not a von Mangoldt event")
        return {
            "half_support": self.a,
            "autocorrelation_support": (-2*self.a, 2*self.a),
            "ceil_2a": self.exponent_ceiling,
            "strict_integer_cutoff": N,
            "included_genuine_prime_power_labels": labels,
            "genuine_prime_power_count": len(labels),
            "support_bounded_without_exp_floats": True,
            "cutoff_is_conservative": True,
            "analytic_fact_used": "e<3, log(3)>1, hence n>=3^ceil(2a) lies outside",
            "source_specific": "actual von Mangoldt coefficients; no fake 6",
            "Gamma_poles_in_this_module": False,
            "full_Weil_form_proved_PSD": False,
            "RH_proved": False,
        }


def support_cofinality_receipt(level: int) -> dict:
    """Countably cofinal rational support scales a_n=n/2, n>=1.

    A countable exhaustion is NOT finite, and PSD at sampled levels does
    not establish PSD on every level. Every individual smooth compactly
    supported test fits within some a_n by Archimedean boundedness.
    """
    if type(level) is not int or not 1 <= level <= 100_000:
        raise WeilWindowError("Positive finite exhaustion level required")
    return {
        "level": level,
        "half_support": F(level, 2),
        "larger_half_support": F(level+1, 2),
        "nested": True,
        "union_contains_all_compact_supports": "CLASSICAL_THEOREM_OVER_ALL_LEVELS",
        "observed_finitely_many_levels_prove_global_positive": False,
        "RH_proved": False,
    }


def invisible_prime_window(p: int, a: F) -> dict:
    """No-float strict support no-go via integer lower bound on log p.

    If p >= 3^ceil(2a), then log p > 2a and the prime impulse cannot be
    sampled by any autocorrelation of phi supported in [-a,a].
    This is a sufficient (not necessary) exact inequality.
    """
    from .diagonal_adele_zeta import prime
    a = CompactWeilSourceWindow(a)
    if type(p) is not int or not prime(p):
        raise WeilWindowError("Original arithmetic prime impulse required")
    guaranteed = p >= a.source_ceiling
    return {
        "p": p, "a": a.a, "integer_cutoff": a.source_ceiling,
        "outside_compact_source_window_proved": guaranteed,
        "is_source_zero_by_bounded_support": guaranteed,
        "no_statement_about_unbounded_support": True,
        "RH_proved": False,
    }
