"""Source-relative finite shadow factorization, witness suites and limit darkness.

Classical finite quotient/factorization and quantifier-order results. A test
suite is mathematical evidence ONLY when its probe semantics and source class
are justified independently. Adding test reports without source attestation
cannot establish ultimate ontology.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Mapping


class ShadowFiberError(ValueError):
    """Missing source map, invalid probe report, or resource-limited solver."""


@dataclass(frozen=True)
class FiniteShadowSuite:
    source_id: str
    states: tuple[Hashable, ...]
    probe_outcomes: Mapping[str, tuple[Hashable, ...]]
    target: Mapping[Hashable, Hashable]

    def __post_init__(self) -> None:
        if not self.source_id or not self.states or len(set(self.states))!=len(self.states):
            raise ShadowFiberError("Declare one nonempty source class")
        if not self.probe_outcomes or len(set(self.probe_outcomes))!=len(self.probe_outcomes):
            raise ShadowFiberError("Declare a finite accessible probe family")
        if set(self.target) != set(self.states):
            raise ShadowFiberError("Original-source target required at every state")
        for p,values in self.probe_outcomes.items():
            if not p or len(values)!=len(self.states):
                raise ShadowFiberError("Probe response table must cover declared source")
            for v in values:
                hash(v)

    def report(self, state: Hashable, chosen: tuple[str,...]) -> tuple[Hashable,...]:
        if state not in self.states or len(set(chosen))!=len(chosen) or any(
            p not in self.probe_outcomes for p in chosen):
            raise ShadowFiberError("Unknown source or probe in observation")
        i=self.states.index(state)
        return tuple(self.probe_outcomes[p][i] for p in chosen)

    def fiber(self, chosen: tuple[str,...], outcomes: tuple[Hashable,...]) -> tuple[Hashable,...]:
        if len(chosen)!=len(outcomes) or len(set(chosen))!=len(chosen) or any(
            p not in self.probe_outcomes for p in chosen):
            raise ShadowFiberError("Malformed declared source observation")
        return tuple(s for s in self.states if self.report(s,chosen)==outcomes)

    def target_report(self, chosen: tuple[str,...], outcomes: tuple[Hashable,...]) -> dict:
        candidates=self.fiber(chosen,outcomes)
        if not candidates:
            return {"status":"INCONSISTENT_SOURCE", "sources":(), "claim":None}
        values={self.target[s] for s in candidates}
        return {"status":"PROVED" if len(values)==1 else "UNRESOLVED",
                "sources":candidates,
                "claim":next(iter(values)) if len(values)==1 else None}

    def _cross_target_pairs(self):
        return tuple((i,j) for i in range(len(self.states)) for j in range(i+1,len(self.states))
                     if self.target[self.states[i]]!=self.target[self.states[j]])

    def minimal_complete_suite(self, *, max_probes: int=16) -> dict:
        """Exact finite non-destructive set-cover solver with source witness.

        If every cross-target pair is separated by a probe, enumerating a
        minimal hitting suite gives UNIFORM finite identification. Does NOT
        automatically apply to destructive/state-changing observation menus.
        """
        names=tuple(self.probe_outcomes)
        if type(max_probes) is not int or len(names)>max_probes:
            raise ShadowFiberError("Finite search budget exhausted: not a no-go theorem")
        pairs=self._cross_target_pairs()
        for i,j in pairs:
            if all(self.probe_outcomes[p][i]==self.probe_outcomes[p][j] for p in names):
                return {"status":"PERMANENTLY_DARK", "pair":(self.states[i],self.states[j]),
                        "minimum":None,"suite":(),"separated_pairs":0,
                        "source_authenticated":False}
        for n in range(len(names)+1):
            for selected in combinations(names,n):
                if all(any(self.probe_outcomes[p][i]!=self.probe_outcomes[p][j]
                           for p in selected) for i,j in pairs):
                    return {"status":"FINITELY_CERTIFIABLE", "pair":None,
                            "minimum":n,"suite":selected,"separated_pairs":len(pairs),
                            "source_authenticated":False}
        raise AssertionError("All cross-target pairs separated but no finite suite found")


@dataclass(frozen=True)
class DelayedSeparatingTower:
    """Countably many rivals: 0 vs x_k, revealed only by probe p_k.

    Every distinct source is separated after SOME finite stage, but there is
    no fixed finite stage ruling out every rival of the zero-source. This
    refutes the quantifier swap (∀x∃n) ⇒ (∃N∀x).
    """
    source_id: str = "zero versus unbounded delayed alternatives"

    def trace(self, source: int, horizon: int) -> tuple[int, ...]:
        if type(source) is not int or source < 0 or type(horizon) is not int or horizon < 0:
            raise ShadowFiberError("Source index and SUCC horizon must be nonnegative")
        return tuple(int(source==n) for n in range(1,horizon+1))

    def alias_after(self,horizon: int) -> int:
        if type(horizon) is not int or horizon < 0:
            raise ShadowFiberError("Nonnegative horizon required")
        rival=horizon+1
        if self.trace(rival,horizon)!=self.trace(0,horizon):
            raise AssertionError("Finite blind-spot source construction failed")
        return rival

    def first_separator(self,source: int) -> int:
        if type(source) is not int or source <= 0:
            raise ShadowFiberError("Nonzero indexed rival required")
        if self.trace(source,source-1)!=self.trace(0,source-1):
            raise AssertionError("Early false certificate")
        if self.trace(source,source)==self.trace(0,source):
            raise AssertionError("No finite separator for this rival")
        return source

    def bounded_source_horizon(self,max_rival: int) -> int:
        """If X={0,1,...,B} IS JUSTIFIED, exactly B probes suffice."""
        if type(max_rival) is not int or max_rival < 0:
            raise ShadowFiberError("Finite source bound needed")
        return max_rival
