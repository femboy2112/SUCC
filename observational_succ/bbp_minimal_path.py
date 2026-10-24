"""Compatibility surface for the two independent BBP minimal-path families.

Two SUCC draft PRs independently authored ``observational_succ/bbp_minimal_path.py``
with DIFFERENT, disjoint public APIs and different source models:

- **#260** (gauge / missing-prime / spectral-bulk) ->
  :mod:`observational_succ.bbp_minimal_path_gauge`.
  Parent PR #256 head ``0683f8f166b9106ab8405a2d6538415b5ac84ba3`` (carries the
  final filtered p^2 Witt contribution).
- **#261** (odd-prime births / minimal rational recurrence / Galois selection) ->
  :mod:`observational_succ.bbp_minimal_path_births`.
  Stacked on draft #258 at ``9aa55b3a6e1150d1690612c740a38e86adc081db``.

Their public symbol sets are disjoint (verified: empty intersection), so this
module re-exports both families flat for backward compatibility AND exposes each
family under its own submodule namespace (``gauge`` and ``births``).

It intentionally does **not** re-export the private ``_prime`` helpers: they carry
DIFFERENT domains -- the gauge family permits the even prime ``p=2`` (a missing
prime may be 2), while the births family requires an odd rational prime ``p>=3``.
Those helpers must stay module-local; see
``docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md`` for the claim-ID crosswalk and the
two source dossiers. No in-tree module imports symbols through this path today; it
exists as the scoped compatibility surface mandated by the coherent-main
integration, and ``tests/test_bbp_minimal_path.py`` guards that it stays coherent.
"""
from __future__ import annotations

from . import bbp_minimal_path_births as births
from . import bbp_minimal_path_gauge as gauge
from .bbp_minimal_path_births import (
    check_first_birth_against_real_state,
    counterfeit_birth_step,
    counterfeit_denominator_witness,
    counterfeit_first_step,
    counterfeit_selected_state,
    finite_prime_support_no_go,
    green_homogeneous_second_order,
    green_order_two_residual_interval,
    integer_root_floor,
    prime_birth_count_formula,
    prime_births_through,
    prime_power_birth_count,
    prime_power_birth_test,
    prime_power_first_birth,
    primes_at_most,
    rational_first_order_impossibility,
)
from .bbp_minimal_path_gauge import (
    circle_distance,
    is_prime_power_denominator,
    nearest_integer,
    period_phase,
    rational_target_proxy,
    single_missing_prime_counterfeit,
)

__all__ = [
    # family namespaces
    "gauge",
    "births",
    # gauge family (#260): source-gauge, missing-prime, spectral bulk
    "circle_distance",
    "is_prime_power_denominator",
    "nearest_integer",
    "period_phase",
    "rational_target_proxy",
    "single_missing_prime_counterfeit",
    # births family (#261): odd-prime births, minimal recurrence, Galois
    "check_first_birth_against_real_state",
    "counterfeit_birth_step",
    "counterfeit_denominator_witness",
    "counterfeit_first_step",
    "counterfeit_selected_state",
    "finite_prime_support_no_go",
    "green_homogeneous_second_order",
    "green_order_two_residual_interval",
    "integer_root_floor",
    "prime_birth_count_formula",
    "prime_births_through",
    "prime_power_birth_count",
    "prime_power_birth_test",
    "prime_power_first_birth",
    "primes_at_most",
    "rational_first_order_impossibility",
]
