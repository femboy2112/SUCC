"""A finite original-state presheaf over lawful instrument-report prefixes.

Original identity, altered carrier, and actual history are separate types.
No fresh preparation, reset, or unperformed branch is silently available.
This is a mathematical source contract; it does not authenticate physical data.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
from typing import Hashable


class HistoryError(ValueError):
    pass


@dataclass(frozen=True)
class Instrument:
    name: str
    after: tuple[int, ...]
    outcome: tuple[Hashable, ...]
    enabled: tuple[bool, ...]


@dataclass(frozen=True)
class LawfulSource:
    source_id: str
    initial: tuple[int, ...]
    instruments: tuple[Instrument, ...]

    def __post_init__(self):
        if (not isinstance(self.source_id, str) or not self.source_id or
                type(self.initial) is not tuple or type(self.instruments) is not tuple or
                not self.initial or not self.instruments or
                any(not isinstance(a, Instrument) for a in self.instruments)):
            raise HistoryError("Explicit original preparations and instruments required")
        n = len(self.instruments[0].after)
        if not 1 <= n <= 512 or len({a.name for a in self.instruments}) != len(self.instruments):
            raise HistoryError("Finite distinct instrument signature required")
        if any(type(x) is not int or not 0 <= x < n for x in self.initial):
            raise HistoryError("Preparation outside declared current carrier")
        for a in self.instruments:
            if (not isinstance(a.name, str) or not a.name or
                    any(type(t) is not tuple or len(t) != n for t in (a.after, a.outcome, a.enabled))):
                raise HistoryError("Instrument tables must have common carrier")
            if any(type(x) is not int or not 0 <= x < n for x in a.after) or any(type(x) is not bool for x in a.enabled):
                raise HistoryError("Malformed transition/availability")
            for y in a.outcome:
                try:
                    hash(y)
                except TypeError as exc:
                    raise HistoryError("Outcomes must be hashable") from exc

    @property
    def count(self):
        return len(self.instruments[0].after)

    @property
    def digest(self):
        return sha256(repr((self.source_id, self.initial, self.instruments)).encode()).hexdigest()

    def instrument(self, name):
        for a in self.instruments:
            if name == a.name:
                return a
        raise HistoryError("Unlicensed instrument; no implicit reset")


@dataclass(frozen=True)
class Event:
    action: str
    outcome: Hashable


@dataclass(frozen=True)
class HistoryFiber:
    source_digest: str
    history: tuple[Event, ...]
    configurations: tuple[tuple[int, int], ...]

    @property
    def originals(self):
        return frozenset(o for o, _ in self.configurations)


@dataclass(frozen=True)
class OriginalTargetVerdict:
    status: str
    value: Hashable | None


def replay_fiber(source, history):
    configurations = list(enumerate(source.initial))
    for event in history:
        if not isinstance(event, Event):
            raise HistoryError("History entries must be typed events")
        a = source.instrument(event.action)
        configurations = [(o, a.after[c]) for o, c in configurations
                          if a.enabled[c] and a.outcome[c] == event.outcome]
    return HistoryFiber(source.digest, tuple(history), tuple(configurations))


def extend_fiber(source, fiber, event):
    if not isinstance(event, Event) or fiber != replay_fiber(source, fiber.history):
        raise HistoryError("Stale or forged prefix")
    a = source.instrument(event.action)
    configurations = tuple((o, a.after[c]) for o, c in fiber.configurations
                           if a.enabled[c] and a.outcome[c] == event.outcome)
    return HistoryFiber(source.digest, fiber.history + (event,), configurations)


def restrict_fiber(source, fiber, length):
    """Contravariant restriction sends each surviving ORIGINAL to its prefix.

    It reconstructs the earlier current carrier by lawful replay, rather than
    pretending a destructive physical map has an inverse.
    """
    if fiber != replay_fiber(source, fiber.history) or type(length) is not int or not 0 <= length <= len(fiber.history):
        raise HistoryError("Checked prefix restriction required")
    earlier = dict(replay_fiber(source, fiber.history[:length]).configurations)
    return tuple((o, earlier[o]) for o, _ in fiber.configurations)


def certifies_original(source, fiber, target):
    if fiber != replay_fiber(source, fiber.history) or len(target) != len(source.initial):
        raise HistoryError("Original target outside source")
    values = {target[o] for o in fiber.originals}
    # Empty support is model contradiction, never an ex-falso empirical receipt.
    if not values:
        return OriginalTargetVerdict("INCONSISTENT", None)
    if len(values) != 1:
        return OriginalTargetVerdict("AMBIGUOUS", None)
    return OriginalTargetVerdict("CERTIFIED_MODEL_RELATIVE", next(iter(values)))


def quotient_source(source, labels):
    """A checked current-carrier congruence preserves the ORIGINAL presheaf.

    Availability and every primitive outcome must descend, as well as updates.
    Original preparations remain individually indexed even after current merging.
    """
    from .swarm_discovery import partition
    if len(labels) != source.count or partition(labels) != labels:
        raise HistoryError("Canonical carrier quotient required")
    reps = tuple(labels.index(k) for k in range(len(set(labels))))
    descended = []
    for a in source.instruments:
        after = tuple(labels[a.after[c]] for c in reps)
        outcome = tuple(a.outcome[c] for c in reps)
        enabled = tuple(a.enabled[c] for c in reps)
        if any(after[labels[c]] != labels[a.after[c]] or outcome[labels[c]] != a.outcome[c]
               or enabled[labels[c]] != a.enabled[c] for c in range(source.count)):
            raise HistoryError("Quotient loses outcome, feasibility, or update meaning")
        descended.append(Instrument(a.name, after, outcome, enabled))
    return LawfulSource(source.source_id + ":quotient", tuple(labels[c] for c in source.initial), tuple(descended))


def synchronized_original_support(source, quotient, labels, history):
    """Execute both independently; tests the all-history factorization theorem."""
    a, b = replay_fiber(source, history), replay_fiber(quotient, history)
    return (a.originals == b.originals and
            tuple((o, labels[c]) for o, c in a.configurations) == b.configurations)


def legal_histories(source, depth):
    if type(depth) is not int or not 0 <= depth <= 8:
        raise HistoryError("Declared finite history horizon 0..8 required")
    level, result = [replay_fiber(source, ())], []
    for _ in range(depth + 1):
        result.extend(level)
        later = []
        for fiber in level:
            for a in source.instruments:
                outcomes = sorted({a.outcome[c] for _, c in fiber.configurations if a.enabled[c]}, key=repr)
                later.extend(extend_fiber(source, fiber, Event(a.name, y)) for y in outcomes)
        level = later
    return tuple(result)
