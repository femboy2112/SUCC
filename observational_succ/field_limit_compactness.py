"""The precise compactness + identifiability gate for recursive SUCC fields.

Mathematical source theorem (classical):
- Let X be a compact topological source and F_i a family of CLOSED
  observer-fiber conditions. If every FINITE intersection is nonempty,
  their global intersection is nonempty.
- If the observation family separates points, this intersection is
  AT MOST one source. Noncompact original sources can have phantom
  compatible finite reports with no actual global source.
- For a DECIDABLE computably finitely branching binary source tree, if
  there is exactly ONE infinite path, that path is computable (possibly
  without any known uniform runtime bound).
- Infinite computable binary trees can nevertheless have only
  NONcomputable paths (the explicit Kleene tree); this forces
  nonuniqueness and refutes constructive selection from bare compactness.

Finite code only verifies named finite windows; universal results
are proved independently in research/2026-10-15/FIELD_LIMIT_TRICHOTOMY.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from .field_limit_trichotomy import FieldLimitError,kleene_source_tree_accepts


@dataclass(frozen=True)
class CompactnessProfile:
    target: str
    source_carrier: str
    observation_fibers_closed: bool
    source_compact: bool
    finite_intersection_property: str
    source_separating: bool
    actual_global_source_existence: str
    unique_if_realized: bool
    construction_algorithm_delivered: bool
    RH_proved: bool = False


def classical_compact_fiber_theorem() -> CompactnessProfile:
    """Conditional math theorem; does NOT verify arbitrary source compactness."""
    return CompactnessProfile(
        target="lift all compatible observation fibers",
        source_carrier="arbitrary declared compact Hausdorff X",
        observation_fibers_closed=True,
        source_compact=True,
        finite_intersection_property="ASSUMED_FOR_ALL_FINITE_SOURCE_SUBFAMILIES",
        source_separating=True,
        actual_global_source_existence="CLASSICAL_COMPACTNESS_CONDITIONAL_THEOREM",
        unique_if_realized=True,
        construction_algorithm_delivered=False
    )


def finite_closed_cylinder_prefix(
        observations:tuple[tuple[int,...],...]) -> dict:
    """Finite Cantor closed-cylinders source compatibility certificate.

    A word s∈{0,1}^n denotes the closed clopen source set [s] of
    binary infinite histories extending s. Increasing observed words
    must be nested prefixes. This has ONE nonempty finite overlap and,
    if a full infinite nested word family is supplied as mathematics,
    compactness ensures a global history exists. Finite list is not
    proof of the full infinite premise.
    """
    if (type(observations) is not tuple or not 1<=len(observations)<=32
            or any(type(s) is not tuple or len(s)>128 or
                   any(type(b) is not int or b not in (0,1) for b in s)
                   for s in observations)):
        raise FieldLimitError("Typed finite Cantor cylinder observer source required")
    for low,high in zip(observations,observations[1:]):
        if len(high)<len(low) or high[:len(low)]!=low:
            raise FieldLimitError("Closed observer source fibers do not nest")
    return {"observed_levels":len(observations),
            "last_source_prefix":observations[-1],
            "finite_closed_fibers_have_nonempty_intersection":True,
            "source_carrier":"COMPACT_CANTOR_2_POWER_N",
            "infinite_nested_family_exists_as_declared_source":False,
            "global_source_existence_if_all_levels_compatible":
                "CLASSICAL_COMPACTNESS_CONDITIONAL_THEOREM",
            "finitely_verified_global_source":False,
            "RH_proved":False}


def _tree_accepts(word:tuple[int,...],source:str,split_depth:int)->bool:
    if source=="unique-zero":
        return not any(word)
    if source=="two-branches":
        # Global paths 000... and 0^d 111...; d can be arbitrarily large.
        zeros=not any(word)
        shifted=all(b==0 for b in word[:split_depth]) and all(
            b==1 for b in word[split_depth:])
        return zeros or shifted
    if source=="kleene":
        return kleene_source_tree_accepts(word)
    raise FieldLimitError("Explicit decidable source tree must be declared")


def bounded_effective_path_prefix(
        source:str, requested_bits:int, max_height:int,
        *,split_depth:int=5) -> dict:
    """Finite search for a prefix common to ALL surviving level-h nodes.

    Sound when it succeeds: any infinite path has such a finite
    prefix. Under the PROMISE that a computable finitely branching
    source tree has a UNIQUE infinite path, this search eventually
    succeeds for every requested bit length.

    If it fails by budget, no noncomputability/no-path conclusion.
    If it succeeds for a SHORT prefix, it does not prove global
    uniqueness; two paths may still diverge later.
    """
    if (type(source) is not str or source not in
            ("unique-zero","two-branches","kleene")
            or type(requested_bits) is not int
            or type(max_height) is not int
            or type(split_depth) is not int
            or not 1<=requested_bits<=max_height<=12
            or not 1<=split_depth<=12):
        raise FieldLimitError("Bounded decidable source-tree stage certificate")
    for h in range(requested_bits,max_height+1):
        seen=set()
        survivors=0
        for word in product((0,1),repeat=h):
            if _tree_accepts(word,source,split_depth):
                survivors+=1
                seen.add(word[:requested_bits])
                if len(seen)>1:
                    break
        if survivors and len(seen)==1:
            return {"source":source,"prefix":next(iter(seen)),
                    "agreed_level":h,
                    "requested_bits":requested_bits,
                    "all_surviving_level_h_prefixes_agree":True,
                    "every_infinite_path_has_that_prefix":True,
                    "global_uniqueness_from_finite_certificate":False,
                    "source_tree_global_path_computed":False,
                    "RH_proved":False}
    return {"source":source,"prefix":None,
            "agreed_level":None,"requested_bits":requested_bits,
            "all_surviving_level_h_prefixes_agree":False,
            "global_uniqueness_from_finite_certificate":False,
            "budget_exhaustion_does_not_disprove_existence":True,
            "RH_proved":False}


def idealhard_requires_multiple_paths() -> dict:
    """Decidable binary tree + no computable path -> at least TWO paths.

    Proof: by König, infinite finite-branching tree has a path.
    If exactly one path existed, run bounded_effective_path_prefix
    with an UNBOUNDED height search (not limited by current program)
    for every requested bit. Finitely branching compactness forces all
    other branches to expire at finite depth, hence eventually all
    surviving level nodes share that prefix. Thus the unique path
    would be computable, contradicting the Kleene source theorem.
    """
    return {
        "source":"EXPLICIT_COMPUTABLE_KLEENE_BINARY_TREE",
        "each_level_nonempty":"PROVED_BY_BOUNDED_SIMULATION_CONSTRUCTION",
        "infinite_path_exists":"CLASSICAL_KONIG_LEMMA",
        "every_path_noncomputable":"PROVED_BY_SELF_DIAGONALIZATION",
        "global_paths_not_unique":"PROVED_USING_UNIQUE_PATH_EFFECTIVITY",
        "no_one_finite_stage_proves_existence":"MATHEMATICAL_EXHAUSTION_PROOF_REQUIRED",
        "source_naturality_or_uniqueness_implies_RH":False,
        "RH_proved":False
    }


def source_dependent_field_frontier()->dict:
    """No premature intrinsic RH undecidability or field type."""
    return {
        "Simple_relative_to_target":"finite verified symbolic description and query program",
        "IdealHard_relative_to_target":"mathematical existence proof but no computable witness",
        "Fucked_nonexistence":"source-compatible finite snapshots without an actual global source",
        "Fucked_nonidentifiability":"two target rival sources have identical permitted histories",
        "unresolved_observer_ambiguity":"TOOLKIT_RELATIVE_DARK_NOT_PROVED_ABSOLUTE_IMPOSSIBILITY",
        "effective_compact_unique_target":
            "UNIQUE_PATH_COMPUTABLE_UNDER_DECIDABLE_FINITE_BRANCHING_PROMISE",
        "Weil_positive_source_at_all_stages":"UNVERIFIED",
        "RH_intrinsic_field_type":"UNVERIFIED",
        "RH_proved":False
    }
