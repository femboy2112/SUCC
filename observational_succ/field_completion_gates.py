"""Source-relative finite/global field gates: exact controls, not an oracle.

The words Simple, IdealHard and Fucked classify a TARGET relative to a
source law, toolkit, proof theory and execution model. They are not
intrinsic types of cardinality or topological inverse limits.

This module deliberately cannot claim a Kleene-tree theorem from a finite
halting trace: the infinite theorem is proved separately in the dossier.
It does NOT certify a physical observer, a full adèle or Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .field_relative_closure import FiniteField


class FieldGateError(ValueError):
    """Unknown carrier, invalid finite source or unearned global conclusion."""


def _natural(n: int, name: str, maximum: int = 4096) -> int:
    if type(n) is not int or not 0 <= n <= maximum:
        raise FieldGateError(f"{name} must be an exact integer in 0..{maximum}")
    return n


@dataclass(frozen=True)
class FiniteGlobalSource:
    """A declaration of source/basis/target, not empirical authentication."""
    source_id: str
    basis_id: str
    target_id: str

    def __post_init__(self) -> None:
        if any(type(s) is not str or not s.strip()
               for s in (self.source_id, self.basis_id, self.target_id)):
            raise FieldGateError("A nonempty source, basis and target are mandatory")


@dataclass(frozen=True)
class DyadicGlobalCode:
    """SimpleField positive model: a fixed integer gives a 2-adic point.

    Its FINITE code answers every requested finite residue query, in finite
    time for that query. This does NOT mean every 2-adic integer has a finite
    program, or that infinitely many digits are printed in a finite time.
    """
    source: FiniteGlobalSource
    seed: int

    def __post_init__(self) -> None:
        if type(self.seed) is not int:
            raise FieldGateError("Exact integer source seed, not float/bool")

    def residue(self, depth: int) -> int:
        _natural(depth, "dyadic depth")
        return self.seed % (2 ** depth)

    def coherence(self, fine: int, coarse: int) -> dict:
        _natural(fine, "fine depth")
        _natural(coarse, "coarse depth")
        if fine < coarse:
            raise FieldGateError("fine depth must be at least coarse")
        x_fine, x_coarse = self.residue(fine), self.residue(coarse)
        if x_fine % (2 ** coarse) != x_coarse:
            raise AssertionError("2-adic bonding law failed")
        return {"source_id": self.source.source_id, "target": self.source.target_id,
                "fine_depth": fine, "coarse_depth": coarse,
                "fine_residue": x_fine, "coarse_residue": x_coarse,
                "bonding_verified": True, "global_program": "n -> seed modulo 2^n",
                "covers_all_2_adic_points": False,
                "rh_proved": False}


@dataclass(frozen=True)
class HaltTrace:
    """A declared finite bounded-time machine-output receipt (not an oracle)."""
    program: int
    halt_at_step: int
    value: int

    def __post_init__(self) -> None:
        _natural(self.program, "program index")
        if type(self.halt_at_step) is not int or self.halt_at_step < 1:
            raise FieldGateError("Positive measured halting step required")
        if type(self.value) is not int or self.value not in (0, 1):
            raise FieldGateError("A bit-valued output is required")


def _checked_traces(traces: tuple[HaltTrace, ...]) -> dict[int, HaltTrace]:
    if type(traces) is not tuple or any(type(t) is not HaltTrace for t in traces):
        raise FieldGateError("The finite halting transcript must be an exact tuple")
    if len(set(t.program for t in traces)) != len(traces):
        raise FieldGateError("Each simulated machine may halt only once")
    return {t.program: t for t in traces}


def antidiagonal_tree_member(word: tuple[int, ...],
                             traces: tuple[HaltTrace, ...]) -> bool:
    """Finite model of the DNR2/Kleene tree at depth len(word).

    For each program e which has halted by stage n with bit b,
    the e-th output bit must equal 1-b. Finite traces do NOT prove
    the universal Kleene theorem: the latter quantifies over ALL machines.
    """
    seen = _checked_traces(traces)
    if type(word) is not tuple or any(type(b) is not int or b not in (0, 1)
                                      for b in word):
        raise FieldGateError("Exact tuple of binary bits required")
    n = len(word)
    for e, t in seen.items():
        if e < n and t.halt_at_step <= n and word[e] != 1 - t.value:
            return False
    return True


def antidiagonal_stage(depth: int, traces: tuple[HaltTrace, ...]) -> dict:
    """Build one computable *stage witness*; do not infer nested choices."""
    _natural(depth, "finite diagonal stage", 512)
    seen = _checked_traces(traces)
    bits = tuple(
        1-seen[e].value if e in seen and seen[e].halt_at_step <= depth else 0
        for e in range(depth)
    )
    if not antidiagonal_tree_member(bits, traces):
        raise AssertionError("Every finite horizon must admit a declared witness")
    return {
        "source": "DECLARED_BOUNDED_MACHINE_TRACES", "stage": depth,
        "chosen_prefix": bits, "stage_member": True,
        "path_computable": "NOT_DETERMINED_BY_THIS_FINITE_TEST",
        "infinite_path_exists": "CLASSICAL_KONIG_CONDITIONAL_ON_FULL_TREE",
        "universal_noncomputable_path_theorem_executed": False,
    }


def stagewise_candidate_failure(early: int, late: int,
                                traces: tuple[HaltTrace, ...]) -> dict:
    """Witness a legal earlier chosen stage becoming incompatible later.

    Does not imply that no coherent infinite branch exists.
    """
    _natural(early, "early")
    _natural(late, "late")
    if not early < late:
        raise FieldGateError("Need a strictly later depth")
    before = antidiagonal_stage(early, traces)["chosen_prefix"]
    after = antidiagonal_stage(late, traces)["chosen_prefix"]
    changed = before != after[:early]
    return {"early": early, "late": late, "early_legal": True,
            "late_legal": True, "canonical_stage_choices_nested": not changed,
            "early_prefix_survives_at_late_stage": not changed,
            "global_nonexistence_inferred": False,
            "global_noncomputability_proved_by_finite_trace": False}


def noncompact_escape(horizon: int) -> dict:
    """A noncompact inverse system X_n={k in N:k>=n}, inclusions.

    Every finite stage has witness k=horizon, but no natural k witnesses
    all n, since n=k+1 refutes it. This is a PROVED PAPER no-go,
    with an exact finite witness for the supplied horizon.
    """
    _natural(horizon, "finite horizon")
    k = horizon
    if any(k < n for n in range(horizon + 1)):
        raise AssertionError("Claimed finite-stage witness failed")
    return {
        "source": "NATURAL_UNBOUNDED_INCLUSION_TOWER",
        "stage_domain": "X_n={k in N : k>=n}",
        "finite_horizon": horizon, "witness": k,
        "all_observed_stages_nonempty": True,
        "diagonal_obstruction_stage": k + 1,
        "inverse_limit_empty": True,
        "why": "A global tuple must be one constant natural k, but stage n=k+1 forbids k",
        "finite_stages_compact": False,
        "rh_proved": False,
    }


def phantom_target_receipt(*, add_separating_probe: bool = False) -> dict:
    """Two original sources share all allowed reports but disagree on target.

    The target-collision claim is tested on a COMPLETE DECLARED FINITE field.
    A new actual source probe can separate them; model-only recursion cannot.
    """
    probes: Mapping[str, tuple[str, str]] = {
        "public_clock": ("same", "same"),
        "public_phase": ("zero", "zero"),
    }
    selected = ("public_clock", "public_phase")
    if add_separating_probe:
        probes = {**probes, "real_source_discriminator": ("left", "right")}
        selected = (*selected, "real_source_discriminator")
    field = FiniteField(
        "SIMPLE_IDEAL_FUCKED_SOURCE_PAIR", "finite-2026-10-15",
        ("world_hidden_0", "world_hidden_1"),
        probes,
        {"hidden_target": (0, 1), "public_target": ("certified", "certified")}
    )
    target = field.factor(selected, "hidden_target")
    public = field.factor(selected, "public_target")
    return {
        "source_id": field.source_id, "basis": field.basis_id,
        "available_probes": selected,
        "two_distinct_declared_source_worlds": True,
        "same_all_current_reports": not add_separating_probe,
        "hidden_target_identifiable": target.proved,
        "hidden_target_collision": target.counterexample,
        "public_target_identifiable": public.proved,
        "model_only_recursion_can_separate_hidden_target": False,
        "new_source_probe_can_separate_hidden_target":
            add_separating_probe,
        "new_source_probe_was_added": add_separating_probe,
        "physical_authentication": False,
        "rh_proved": False,
    }


def delayed_discriminator(horizon: int) -> dict:
    """Two infinite bit sources may agree through ANY chosen finite horizon.

    Not 'indistinguishable forever': there is a specific future witness.
    This separates a *no uniform finite deadline* claim from a true
    all-depth observational nonidentifiability claim.
    """
    _natural(horizon, "probe horizon")
    first_difference = horizon + 1
    return {
        "observed_through": horizon,
        "source_a_rule": "a(n)=0 for all n",
        "source_b_rule": f"b(n)=1 iff n={first_difference}; otherwise 0",
        "all_observations_agree_within_budget": True,
        "first_difference": first_difference,
        "eventual_separation_exists": True,
        "uniform_depth_for_all_possible_sources_exists": False,
        "all_depth_indistinguishability_inferred": False,
    }


def factorial_solenoid_clock(source: FiniteGlobalSource,
                             t: int, depth: int) -> dict:
    """Finite exact circle-stage model for the classical Q-solenoid.

    The stage n is the continuous circle S^1, NOT a finite discrete set;
    bonding maps z -> z^(n+1), n>=1, use D_n=(n+1)!.
    A chosen integer t yields a coherent rational-phase family
      theta_n = t / D_n (mod 1).
    This finite evaluator does not enumerate every point of the solenoid.
    """
    from math import factorial
    from fractions import Fraction as F
    if not isinstance(source, FiniteGlobalSource) or type(t) is not int:
        raise FieldGateError("Finite source and exact integer winding needed")
    _natural(depth, "factorial circle depth", 128)
    D_n = factorial(depth + 1)
    phase = F(t, D_n) % 1
    if depth:
        D_prior = factorial(depth)
        previous = F(t, D_prior) % 1
        if (phase * (depth + 1)) % 1 != previous:
            raise AssertionError("Circle-power bonding square failed")
    else:
        previous = phase
    return {
        "source_id": source.source_id,
        "depth": depth,
        "winding_seed": t,
        "D_n": D_n,
        "phase_mod_1": phase,
        "previous_phase_mod_1": previous,
        "bonding_degree": depth + 1 if depth else 1,
        "circle_bonding_coherent": True,
        "stage_topology": "CONNECTED_CONTINUOUS_CIRCLE",
        "all_global_solenoid_points_finitely_executable": False,
        "full_topological_Q_solenoid_iso_proved_by_execution": False,
        "RH_proved": False,
    }
