"""Exact finite probe-repair certificates: the missing-data obstruction.

A candidate probe is a mathematical possibility. It is NOT thereby physically
accessible, nondestructive, or capable of authenticating the source.
Minimal cardinality search is exponential; the general problem subsumes set cover.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Sequence

from .field_relative_closure import FiniteField, ClosureError


@dataclass(frozen=True)
class RepairCertificate:
    source_id: str
    basis_id: str
    target: str
    baseline: tuple[str, ...]
    candidate_menu: tuple[str, ...]
    selected: tuple[str, ...]
    conflicting_pairs: tuple[tuple[Hashable, Hashable], ...]
    uncovered_pair: tuple[Hashable, Hashable] | None
    tested_subsets: int

    @property
    def possible(self) -> bool:
        return self.uncovered_pair is None


def unresolved_pairs(field: FiniteField, baseline: Sequence[str], target: str) -> tuple[tuple[int,int],...]:
    baseline = field.names(baseline)
    if target not in field.targets:
        raise ClosureError("Unknown original-source target")
    return tuple((i,j) for i in range(len(field.states)) for j in range(i+1,len(field.states))
                 if field.targets[target][i] != field.targets[target][j]
                 and all(field.probes[p][i] == field.probes[p][j] for p in baseline))


def repair(field: FiniteField, baseline: Sequence[str], candidates: Sequence[str],
           target: str, *, max_subsets: int=1_000_000) -> RepairCertificate:
    """Return minimum-size new probe family, or a source pair none can separate.

    Exhausted finite resources -> explicit error, never an impossibility claim.
    This is a STATIC observation problem, not the adaptive executable policy.
    """
    old, menu = field.names(baseline), field.names(candidates)
    if set(old) & set(menu):
        raise ClosureError("Repair menu should contain only NEW probes")
    if type(max_subsets) is not int or max_subsets < 1:
        raise ClosureError("Positive finite search budget required")
    conflict = unresolved_pairs(field, old, target)
    all_pairs = tuple((field.states[i],field.states[j]) for i,j in conflict)
    for i,j in conflict:
        if all(field.probes[p][i] == field.probes[p][j] for p in menu):
            return RepairCertificate(field.source_id,field.basis_id,target,old,menu,
                                     (),all_pairs,(field.states[i],field.states[j]),0)
    searched = 0
    for size in range(len(menu)+1):
        for subset in combinations(menu,size):
            if searched >= max_subsets:
                raise ClosureError("Probe-repair search budget exhausted: UNRESOLVED")
            searched += 1
            if all(any(field.probes[p][i] != field.probes[p][j] for p in subset)
                   for i,j in conflict):
                return RepairCertificate(field.source_id,field.basis_id,target,old,menu,
                                         tuple(subset),all_pairs,None,searched)
    raise AssertionError("Full menu separates all conflicts yet no repair exists")


def verify_repair(field: FiniteField, cert: RepairCertificate) -> bool:
    """Independent exhaustive minimality check; validates source truth.

    Certified minimum is by NUMBER of new probes, not elapsed time, bandwidth,
    physical action budget, or cryptographic trust.
    """
    if not isinstance(cert, RepairCertificate):
        raise ClosureError("Not a probe-repair certificate")
    if (cert.source_id,cert.basis_id) != (field.source_id,field.basis_id):
        raise ClosureError("Forged source or semantic basis")
    old,menu=field.names(cert.baseline),field.names(cert.candidate_menu)
    expected = unresolved_pairs(field,old,cert.target)
    reported=tuple((field.states[i],field.states[j]) for i,j in expected)
    if reported != cert.conflicting_pairs:
        raise ClosureError("Forged conflicting-source witnesses")
    if cert.uncovered_pair is not None:
        pair=cert.uncovered_pair
        if pair not in reported:
            raise ClosureError("Uncovered pair not target-distinct or not baseline-aliased")
        i,j=field.states.index(pair[0]),field.states.index(pair[1])
        if any(field.probes[p][i]!=field.probes[p][j] for p in menu):
            raise ClosureError("An available probe actually resolves the alleged darkness")
        return True
    if not set(cert.selected).issubset(menu):
        raise ClosureError("Undeclared new probe in repair")
    if not field.factor(old+cert.selected,cert.target).proved:
        raise ClosureError("Selected repair does not settle target")
    # Exhaust the entire smaller cardinalities; different witness from the
    # production search ensures source records cannot forge minimality.
    for k in range(len(cert.selected)):
        if any(field.factor(old+tuple(subset),cert.target).proved
               for subset in combinations(menu,k)):
            raise ClosureError("Nonminimal repair")
    return True


def set_cover_field(universe: int, subsets: Sequence[Sequence[int]]) -> FiniteField:
    """Reduction from finite SET COVER to target-relative probe repair.

    State space consists of two source versions for each element i. A baseline
    context identifies i but aliases the two versions. Probe S distinguishes
    those versions exactly when i belongs to subset S. Hence repairs ARE covers.
    """
    if type(universe) is not int or not 1 <= universe <= 24:
        raise ClosureError("Finite reduction universe must have 1..24 elements")
    cover = tuple(tuple(s) for s in subsets)
    if any(len(set(s)) != len(s) or any(type(v) is not int or not 0 <= v < universe for v in s)
           for s in cover):
        raise ClosureError("Malformed set-cover incidence")
    states = tuple((i,b) for i in range(universe) for b in (0,1))
    probes: dict[str,tuple[Hashable,...]] = {"pair_index":tuple(i for i,b in states)}
    for k,S in enumerate(cover):
        probes[f"cover_{k}"] = tuple(b if i in S else 0 for i,b in states)
    return FiniteField("set-cover-reduction","finite-hitting-set",states,probes,
                       {"original_bit":tuple(b for i,b in states)})
