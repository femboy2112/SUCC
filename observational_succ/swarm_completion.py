"""Exact finite experiments for SWM-B09--B16.

These functions operate on declared mathematical sources. They never infer
physical preparation, an infinite source realization, or total computability
from a bounded search. General proofs live in the indexed research dossiers.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, Hashable, Iterable, Mapping


class CompletionError(ValueError):
    """Malformed finite evidence or incompatible source declaration."""


def _nat(value: int) -> int:
    if type(value) is not int or value < 0:
        raise CompletionError("An exact nonnegative integer is required")
    return value


@dataclass(frozen=True)
class PartialEvidence:
    """A finite partial report, ordered by extension, with no default tail."""
    entries: tuple[tuple[int, Hashable], ...] = ()

    def __post_init__(self):
        if type(self.entries) is not tuple:
            raise CompletionError("Evidence must be an immutable tuple")
        keys = []
        for entry in self.entries:
            if type(entry) is not tuple or len(entry) != 2:
                raise CompletionError("Evidence entries must be address/value pairs")
            key, value = entry
            _nat(key)
            try:
                hash(value)
            except TypeError as exc:
                raise CompletionError("Report values must be hashable") from exc
            keys.append(key)
        if keys != sorted(set(keys)):
            raise CompletionError("Evidence addresses must be sorted and unique")

    @classmethod
    def from_mapping(cls, mapping: Mapping[int, Hashable]) -> PartialEvidence:
        return cls(tuple(sorted(mapping.items())))

    def extends(self, older: PartialEvidence) -> bool:
        return set(older.entries) <= set(self.entries)

    def join(self, other: PartialEvidence) -> PartialEvidence:
        merged = dict(self.entries)
        for key, value in other.entries:
            if key in merged and merged[key] != value:
                raise CompletionError("Conflicting reports have no lawful common upper bound")
            merged[key] = value
        return PartialEvidence.from_mapping(merged)

    def shift(self) -> PartialEvidence:
        """Information transport under x(n) -> x(n+1), forgetting address 0."""
        return PartialEvidence(tuple((n-1, v) for n, v in self.entries if n > 0))

    def agrees(self, stream: Callable[[int], Hashable]) -> bool:
        return all(stream(n) == value for n, value in self.entries)


@dataclass(frozen=True)
class LassoStream:
    """An exact infinite stream defined by a finite prefix and nonempty period."""
    prefix: tuple[Hashable, ...]
    period: tuple[Hashable, ...]

    def __post_init__(self):
        if type(self.prefix) is not tuple or type(self.period) is not tuple or not self.period:
            raise CompletionError("Finite immutable prefix and nonempty period required")
        for symbol in self.prefix + self.period:
            try:
                hash(symbol)
            except TypeError as exc:
                raise CompletionError("Symbols must be hashable") from exc

    def __call__(self, n: int) -> Hashable:
        _nat(n)
        if n < len(self.prefix):
            return self.prefix[n]
        return self.period[(n-len(self.prefix)) % len(self.period)]


def patch_tail(evidence: PartialEvidence, tail: tuple[Hashable, ...],
               *, default: Hashable = 0) -> LassoStream:
    """A genuine ultimately periodic completion, not an observed tail."""
    size = 1 + max((n for n, _ in evidence.entries), default=-1)
    prefix = [default] * size
    for n, value in evidence.entries:
        prefix[n] = value
    return LassoStream(tuple(prefix), tail)


def power_marker_patch(evidence: PartialEvidence, *, default: Hashable = 0,
                       marker: Hashable = 1) -> Callable[[int], Hashable]:
    """Nonperiodic completion: a marker at sufficiently late powers of two.

    Finitely many observed values are preserved. Distinct marker/default
    symbols and unbounded marker gaps prove non-ultimate-periodicity.
    """
    if marker == default:
        raise CompletionError("Distinct marker and default symbols required")
    patch = dict(evidence.entries)
    cutoff = 1 + max(patch, default=-1)
    def stream(n: int) -> Hashable:
        _nat(n)
        if n in patch:
            return patch[n]
        return marker if n >= cutoff and n > 0 and n & (n-1) == 0 else default
    return stream


def finite_refutation_search(states: tuple[Hashable, ...],
        trace: Callable[[Hashable, Hashable], Hashable],
        profile: Callable[[Hashable], Hashable],
        probes: Iterable[Hashable]) -> dict:
    """Eliminate a COMPLETE finite source by enumerated exact probe tests.

    An infinite complete probe enumeration terminates iff no source realizes
    the profile. A finite exhausted probe list returns UNRESOLVED, never
    REALIZED. At most one retained witness per original source is needed.
    """
    if type(states) is not tuple or len(set(states)) != len(states):
        raise CompletionError("Complete distinct immutable source enumeration required")
    alive = set(states)
    witnesses = {}
    inspected = 0
    if not alive:
        return {"status": "REFUTED", "inspected_probe_count": 0,
                "witnesses": (), "retained_probes": ()}
    for probe in probes:
        inspected += 1
        target = profile(probe)
        for state in states:
            if state in alive and trace(state, probe) != target:
                alive.remove(state)
                witnesses[state] = probe
        if not alive:
            ordered = tuple((s, witnesses[s]) for s in states)
            return {"status": "REFUTED", "inspected_probe_count": inspected,
                    "witnesses": ordered,
                    "retained_probes": tuple(dict.fromkeys(w for _, w in ordered))}
    return {"status": "UNRESOLVED", "inspected_probe_count": inspected,
            "remaining_states": tuple(s for s in states if s in alive),
            "witnesses": tuple((s, witnesses[s]) for s in states if s in witnesses)}


def verify_refutation(states: tuple[Hashable, ...],
        trace: Callable[[Hashable, Hashable], Hashable],
        profile: Callable[[Hashable], Hashable], receipt: Mapping) -> bool:
    """Replay every retained witness; source completeness remains a premise."""
    if receipt.get("status") != "REFUTED":
        return False
    witnesses = receipt.get("witnesses", ())
    if len(witnesses) != len(states) or {s for s, _ in witnesses} != set(states):
        return False
    return all(trace(s, w) != profile(w) for s, w in witnesses)


def minimum_prefix_generator(word: tuple[Hashable, ...]) -> dict:
    """Sharp stationary autonomous Moore-source state count for a finite word.

    For nonempty w of length L, minimize mu+p subject to p>0, mu>=0,
    mu+p<=L and w[t]=w[t-p] for mu+p<=t<L. The selected lasso realizes
    the whole word using exactly that many declared source states.
    Empty observation needs one source state if a nonempty carrier is required.
    This is source-state complexity, not observer/storage/energy complexity.
    """
    if type(word) is not tuple:
        raise CompletionError("Immutable finite word required")
    for symbol in word:
        try:
            hash(symbol)
        except TypeError as exc:
            raise CompletionError("Symbols must be hashable") from exc
    if not word:
        return {"state_count": 1, "preperiod": 0, "period": 1,
                "stream": LassoStream((), (0,)), "observed_length": 0}
    for count in range(1, len(word)+1):
        for mu in range(count):
            p = count-mu
            if all(word[t] == word[t-p] for t in range(count, len(word))):
                return {"state_count": count, "preperiod": mu, "period": p,
                        "stream": LassoStream(word[:mu], word[mu:count]),
                        "observed_length": len(word)}
    raise AssertionError("The full observed word is always a finite lasso witness")


def marker_gap_bound(word: tuple[Hashable, ...], start: int, stop: int) -> dict:
    """A terminal marker absent in the previous gap forces stop-start+1 states.

    Interior values may differ from one another. Only exclusion of the endpoint
    marker is needed. Exact lower bound, not generally the full minimum count.
    """
    _nat(start); _nat(stop)
    if not start <= stop < len(word):
        raise CompletionError("A finite observed gap with an observed endpoint is required")
    marker = word[stop]
    if any(word[t] == marker for t in range(start, stop)):
        raise CompletionError("The endpoint marker occurs inside the declared gap")
    return {"state_lower_bound": stop-start+1, "start": start,
            "stop": stop, "marker": marker,
            "statement": "pairwise-distinct stationary original source states"}


@dataclass(frozen=True)
class MooreSource:
    """Complete finite deterministic source with multi-action futures."""
    states: tuple[Hashable, ...]
    actions: tuple[Hashable, ...]
    outputs: tuple[Hashable, ...]
    transitions: tuple[tuple[Hashable, ...], ...]

    def __post_init__(self):
        if (not self.states or type(self.states) is not tuple or type(self.actions) is not tuple
                or type(self.outputs) is not tuple or type(self.transitions) is not tuple
                or len(set(self.states)) != len(self.states)
                or len(set(self.actions)) != len(self.actions)
                or len(self.outputs) != len(self.states)
                or len(self.transitions) != len(self.states)):
            raise CompletionError("Complete finite immutable state/action source required")
        for row in self.transitions:
            if type(row) is not tuple or len(row) != len(self.actions) or not set(row) <= set(self.states):
                raise CompletionError("Every action must have a lawful successor at every state")
        for symbol in self.outputs:
            try:
                hash(symbol)
            except TypeError as exc:
                raise CompletionError("Reports must be hashable") from exc

    def observe(self, state: Hashable, word: tuple[Hashable, ...]) -> Hashable:
        if state not in self.states:
            raise CompletionError("Unknown original state")
        for action in word:
            if action not in self.actions:
                raise CompletionError("Unlicensed action")
            state = self.transitions[self.states.index(state)][self.actions.index(action)]
        return self.outputs[self.states.index(state)]

    def separator(self, left: Hashable, right: Hashable) -> tuple[Hashable, ...] | None:
        """Shortest lawful counterfactual future word, or behavioral equivalence."""
        if left not in self.states or right not in self.states:
            raise CompletionError("Unknown source state")
        queue = deque([(left, right, ())])
        seen = {(left, right)}
        while queue:
            s, t, word = queue.popleft()
            i, j = self.states.index(s), self.states.index(t)
            if self.outputs[i] != self.outputs[j]:
                return word
            for a, action in enumerate(self.actions):
                pair = self.transitions[i][a], self.transitions[j][a]
                if pair not in seen:
                    seen.add(pair)
                    queue.append((*pair, word+(action,)))
        return None

    def behavioral_classes(self) -> tuple[tuple[Hashable, ...], ...]:
        """The final-trace kernel, a lawful action congruence."""
        groups = []
        for state in self.states:
            for group in groups:
                if self.separator(state, group[0]) is None:
                    group.append(state)
                    break
            else:
                groups.append([state])
        return tuple(tuple(group) for group in groups)

    def minimal_quotient(self) -> MooreSource:
        groups = self.behavioral_classes()
        index = {s: i for i, group in enumerate(groups) for s in group}
        rows = []
        outputs = []
        for group in groups:
            representative = group[0]
            r = self.states.index(representative)
            row = tuple(index[t] for t in self.transitions[r])
            for state in group:
                k = self.states.index(state)
                if self.outputs[k] != self.outputs[r] or tuple(index[t] for t in self.transitions[k]) != row:
                    raise AssertionError("Final-trace kernel must preserve report and action squares")
            rows.append(row)
            outputs.append(self.outputs[r])
        return MooreSource(tuple(range(len(groups))), self.actions, tuple(outputs), tuple(rows))


def least_proof_support_stage(support: tuple[Hashable, ...],
                             stages: tuple[frozenset[Hashable], ...]) -> int | None:
    """Locate a supplied finite proof's axioms in nested finite theory stages.

    No proof search, rule soundness, reflection axiom or omega-rule is added.
    None means absent from the SUPPLIED finite stages, not globally unprovable.
    """
    if type(support) is not tuple or type(stages) is not tuple or any(type(s) is not frozenset for s in stages):
        raise CompletionError("Immutable finite proof support and finite stage list required")
    if any(not a <= b for a, b in zip(stages, stages[1:])):
        raise CompletionError("Theory stages must increase")
    return next((i for i, stage in enumerate(stages) if set(support) <= stage), None)
