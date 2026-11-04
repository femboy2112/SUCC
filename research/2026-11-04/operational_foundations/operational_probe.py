"""Finite operational inference controls; synthetic models only.

Research adapter, NOT a second categorical core or physical/quantum attestation.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product


class ContractError(ValueError):
    pass


@dataclass(frozen=True)
class Instrument:
    name: str
    output: tuple[str, ...]
    successor: tuple[int, ...]
    cost: int = 1


@dataclass(frozen=True)
class DeclaredSource:
    source: str
    count: int
    instruments: tuple[Instrument, ...]

    def __post_init__(self):
        if not self.source or type(self.count) is not int or not 1 <= self.count <= 64:
            raise ContractError('source must be named; finite state count 1..64')
        if len(set(p.name for p in self.instruments)) != len(self.instruments):
            raise ContractError('duplicate probe names')
        for p in self.instruments:
            if (not p.name or type(p.cost) is not int or p.cost < 1
                    or len(p.output) != self.count or len(p.successor) != self.count
                    or any(type(x) is not int or x < 0 or x >= self.count for x in p.successor)
                    or any(type(x) is not str for x in p.output)):
                raise ContractError('malformed probe/source signature')

    def instrument(self, name: str) -> Instrument:
        for p in self.instruments:
            if p.name == name:
                return p
        raise ContractError('probe absent from declared source toolkit')

    def execute(self, state: int, word: tuple[str, ...]) -> tuple[tuple[str, ...], int]:
        if type(state) is not int or not 0 <= state < self.count:
            raise ContractError('invalid source state')
        results = []
        for name in word:
            p = self.instrument(name)
            results.append(p.output[state])
            state = p.successor[state]
        return tuple(results), state

    def trace(self, state: int, word: tuple[str, ...]) -> tuple[str, ...]:
        return self.execute(state, word)[0]

    def budget(self, word: tuple[str, ...]) -> int:
        return sum(self.instrument(name).cost for name in word)

    def observed_initials(self, word: tuple[str, ...], outcomes: tuple[str, ...],
                          previous: tuple[int, ...] | None = None) -> tuple[int, ...]:
        if len(word) != len(outcomes):
            raise ContractError('one readout for each performed probe')
        states = tuple(range(self.count)) if previous is None else previous
        if len(set(states)) != len(states) or any(type(x) is not int or not 0 <= x < self.count for x in states):
            raise ContractError('candidate initial state IDs invalid')
        return tuple(s for s in states if self.trace(s, word) == outcomes)

    def signature(self, state: int, toolkit: tuple[str, ...], depth: int,
                  budget: int | None = None) -> tuple[tuple[tuple[str, ...], tuple[str, ...]], ...]:
        if type(depth) is not int or depth < 0 or depth > 6:
            raise ContractError('finite depth 0..6')
        if len(set(toolkit)) != len(toolkit):
            raise ContractError('toolkit must list probes once')
        for name in toolkit:
            self.instrument(name)
        if budget is not None and (type(budget) is not int or budget < 0):
            raise ContractError('nonnegative budget')
        words = (w for n in range(depth + 1) for w in product(toolkit, repeat=n))
        return tuple((w, self.trace(state, w)) for w in words
                     if budget is None or self.budget(w) <= budget)

    def observation_classes(self, toolkit: tuple[str, ...], depth: int,
                            budget: int | None = None) -> tuple[tuple[int, ...], ...]:
        groups = {}
        for state in range(self.count):
            groups.setdefault(self.signature(state, toolkit, depth, budget), []).append(state)
        return tuple(tuple(xs) for xs in groups.values())


def bounded_induction_countermodel(k: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Two total computable laws matching through k, then splitting."""
    if type(k) is not int or k < 0 or k > 10000:
        raise ContractError('finite nonnegative evidence horizon')
    return tuple(0 for _ in range(k + 2)), tuple(0 if n <= k else 1 for n in range(k + 2))


def append_witness(journal: tuple[tuple[str, str, str], ...],
                   source: str, action: str, outcome: str) -> tuple[tuple[str, str, str], ...]:
    """Pure append; historical source labels never silently overwritten."""
    if not source or not action or not outcome:
        raise ContractError('cannot append an unlabelled source/action/outcome')
    return journal + ((source, action, outcome),)
