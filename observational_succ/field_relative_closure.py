"""Finite source-relative observation/claim factorization, exact and conservative.

A label is a DECLARED model source, not an authenticated physical origin.
An omega classification is NEVER inferred from checking finitely many stages.
This is classical finite partition refinement / elementary Yoneda semantics.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence


class ClosureError(ValueError):
    """Ill-typed source, probe, claim, or unsupported equality."""


@dataclass(frozen=True)
class FactorCertificate:
    source_id: str
    basis_id: str
    probe_names: tuple[str, ...]
    target_name: str
    source_count: int
    decoder: tuple[tuple[tuple[Hashable, ...], Hashable], ...]
    # A pair of exact states with same report and different target, when failing.
    counterexample: tuple[Hashable, Hashable] | None = None

    @property
    def proved(self) -> bool:
        return self.counterexample is None


@dataclass(frozen=True)
class FiniteField:
    """Fixed carrier source class and exact, named, nondestructive probe tables."""
    source_id: str
    basis_id: str
    states: tuple[Hashable, ...]
    probes: Mapping[str, tuple[Hashable, ...]]
    targets: Mapping[str, tuple[Hashable, ...]]

    def __post_init__(self) -> None:
        if (type(self.source_id) is not str or not self.source_id
                or type(self.basis_id) is not str or not self.basis_id):
            raise ClosureError("Declare source and basis versions")
        if type(self.states) is not tuple:
            raise ClosureError("The source class must have an exact immutable tuple")
        if not self.states or len(set(self.states)) != len(self.states):
            raise ClosureError("A finite declared source requires distinct states")
        if not self.probes or not self.targets:
            raise ClosureError("Declare both probe and target tables")
        for k, v in tuple(self.probes.items()) + tuple(self.targets.items()):
            if (not isinstance(k, str) or not k or not isinstance(v, tuple)
                    or len(v) != len(self.states)):
                raise ClosureError("A declared table must cover every carrier state")
            for x in v:
                try:
                    hash(x)
                except TypeError as exc:
                    raise ClosureError("Unhashable report/target") from exc

    def names(self, names: Sequence[str]) -> tuple[str, ...]:
        if isinstance(names, str):
            raise ClosureError("Pass a probe sequence, not a string")
        selected = tuple(names)
        if len(selected) != len(set(selected)) or any(p not in self.probes for p in selected):
            raise ClosureError("Unknown or duplicate probe")
        return selected

    def signature(self, state: Hashable, probes: Sequence[str]) -> tuple[Hashable, ...]:
        names = self.names(probes)
        try:
            i = self.states.index(state)
        except ValueError as exc:
            raise ClosureError("Unknown original source state") from exc
        return tuple(self.probes[p][i] for p in names)

    def factor(self, probes: Sequence[str], target: str) -> FactorCertificate:
        names = self.names(probes)
        if target not in self.targets:
            raise ClosureError("Unknown source-relative target")
        seen: dict[tuple[Hashable, ...], tuple[Hashable, Hashable]] = {}
        for i, state in enumerate(self.states):
            key = tuple(self.probes[p][i] for p in names)
            value = self.targets[target][i]
            if key in seen and value != seen[key][1]:
                return FactorCertificate(self.source_id, self.basis_id, names, target,
                                         len(self.states), (), (seen[key][0], state))
            seen[key] = (state, value)
        decoder = tuple(sorted(((key, val) for key, (_, val) in seen.items()),
                               key=lambda kv: repr(kv[0])))
        return FactorCertificate(self.source_id, self.basis_id, names, target,
                                 len(self.states), decoder)

    def verify(self, cert: FactorCertificate) -> bool:
        """Recompute all source outcomes; a serialized certificate is not authority."""
        if not isinstance(cert, FactorCertificate):
            raise ClosureError("Expected typed certificate")
        if (cert.source_id, cert.basis_id, cert.source_count) != (
                self.source_id, self.basis_id, len(self.states)):
            raise ClosureError("Wrong source, version or source size")
        actual = self.factor(cert.probe_names, cert.target_name)
        if actual != cert:
            raise ClosureError("False, incomplete, or forged decoder/counterexample")
        return True

    def finite_depth(self, staged_probes: Sequence[Sequence[str]], target: str) -> dict:
        """FIRST finite sufficient stage; otherwise UNRESOLVED, never 'omega' by scan."""
        if not staged_probes:
            raise ClosureError("At least one finite stage is required")
        prior: set[str] = set()
        seen = []
        earliest = None
        for stage, probes in enumerate(staged_probes):
            current = self.names(probes)
            if not prior.issubset(set(current)):
                raise ClosureError("Evidence was retracted; new source semantics required")
            prior = set(current)
            cert = self.factor(current, target)
            seen.append({"stage": stage, "probes": current, "proved": cert.proved,
                         "rival": cert.counterexample})
            if cert.proved and earliest is None:
                earliest = (stage, cert)
        if earliest is not None:
            return {"status": "FINITE_CLOSURE", "rank": earliest[0],
                    "certificate": earliest[1], "stages_checked": tuple(seen)}
        return {"status": "UNRESOLVED_FINITE_HORIZON", "rank": None,
                "rival": self.factor(staged_probes[-1], target).counterexample,
                "stages_checked": tuple(seen)}

    def source_fiber(self, records: Sequence[tuple[str, Hashable]]) -> tuple[Hashable, ...]:
        for name, _ in records:
            if name not in self.probes:
                raise ClosureError("Unlicensed empirical probe")
        return tuple(x for i, x in enumerate(self.states)
                     if all(self.probes[p][i] == value for p, value in records))

    def local_realizability(self, records: Sequence[tuple[str, Hashable]]) -> dict:
        """Pairwise compatible reports need not share a single source."""
        evidence = tuple(records)
        pairwise = all(bool(self.source_fiber((evidence[i], evidence[j])))
                       for i in range(len(evidence)) for j in range(i+1, len(evidence)))
        fiber = self.source_fiber(evidence)
        if fiber:
            return {"status": "GLOBAL_SOURCE_REALIZED", "fiber": fiber,
                    "pairwise_realizable": pairwise}
        return {"status": "NO_GLOBAL_SOURCE_WITNESS", "fiber": (),
                "pairwise_realizable": pairwise}


def invariant_orbits(states: tuple[Hashable, ...],
                     permutations: Sequence[tuple[int, ...]],
                     target_values: tuple[Hashable, ...]) -> dict:
    """Exact generator criterion for claim invariance under all frame loops."""
    n = len(states)
    if not states or len(set(states)) != n or len(target_values) != n:
        raise ClosureError("Group action and original-source target must align")
    gen = tuple(permutations)
    for g in gen:
        if len(g) != n or set(g) != set(range(n)):
            raise ClosureError("Each frame generator must be a permutation")
    parent = list(range(n))

    def root(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x
    for g in gen:
        for i, j in enumerate(g):
            a,b=root(i),root(j)
            if a != b:
                parent[b] = a
    orbits: dict[int, list[Hashable]] = {}
    for i, s in enumerate(states):
        orbits.setdefault(root(i), []).append(s)
    violations = tuple((states[i], states[j], target_values[i], target_values[j])
                       for g in gen for i,j in enumerate(g)
                       if target_values[i] != target_values[j])
    return {"claim_is_frame_invariant": not bool(violations),
            "orbits": tuple(sorted((tuple(x) for x in orbits.values()), key=repr)),
            "generator_violation": violations[0] if violations else None,
            "all_history_scope": "generated permutations, not physical interventions"}


@dataclass(frozen=True)
class InconsistencyCertificate:
    source_id: str
    basis_id: str
    minimal_records: tuple[tuple[str,Hashable],...]
    proper_subsets_realizable: bool
    exact_global_witness_count: int


def minimal_inconsistent_core(field: FiniteField,
                              records: Sequence[tuple[str,Hashable]],
                              *,max_subsets:int=65536) -> InconsistencyCertificate|None:
    """Find smallest-cardinality empirically inconsistent report set.

    All proper subsets of a chosen minimum-size core must be realizable, since
    every smaller subset of the total record set was checked. This is an
    internal table proof, not a signature authenticating an external observer.
    """
    from itertools import combinations
    data=tuple(records)
    if field.source_fiber(data):
        return None
    budget=0
    for length in range(1,len(data)+1):
        for idx in combinations(range(len(data)),length):
            if budget>=max_subsets:
                raise ClosureError("Inconsistency core search exhausted: UNKNOWN")
            budget+=1
            part=tuple(data[i] for i in idx)
            if not field.source_fiber(part):
                for smaller in combinations(range(length),length-1):
                    sub=tuple(part[i] for i in smaller)
                    if not field.source_fiber(sub):
                        raise AssertionError("Smaller inconsistent subset missed")
                return InconsistencyCertificate(field.source_id,field.basis_id,
                                                part,True,0)
    raise AssertionError("Known inconsistent record set has no inconsistent core")
