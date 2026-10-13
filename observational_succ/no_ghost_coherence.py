"""Exact private-history coherence calibration for NO-GHOST.

This is a finite declared stochastic carrier, not an empirical event log.  Each
one-use action draws an independent private fair bit, records public ``ok``,
and adds its occurrence ID to the current completed-event set.  Original
source, payload, basis and source ID remain fixed.  No reset or source query
is available.  All histories enumerated here are positive-weight *possible*
histories; enumeration never asserts they were physically performed.

Selected pair comparisons are bijections of complete private path spaces.
They may relabel the two exchanged events' private bit values.  Their scope
therefore does NOT include preserving fixed per-event branch-value claims.
The token-preserving comparison is coherent; an equally measure-preserving
but token-relabeling comparison need not be.  This is chosen-map holonomy,
not a failure of stochastic commutation or of existence of coherent maps.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from typing import Hashable


Q = Fraction
BitPair = tuple[int, int]
PairTable = tuple[BitPair, BitPair, BitPair, BitPair]
TOKEN_SWAP: PairTable = ((0, 0), (1, 0), (0, 1), (1, 1))
CNOT_RELABEL: PairTable = ((0, 0), (0, 1), (1, 1), (1, 0))


class CoherenceError(ValueError):
    """A declared history/comparison is outside the finite model contract."""


@dataclass(frozen=True)
class CarrierPoint:
    payload: Hashable
    completed: frozenset[str]


@dataclass(frozen=True)
class PrivateStep:
    occurrence: str
    private_bit: int
    receipt: str
    before: CarrierPoint
    after: CarrierPoint
    probability: Q


@dataclass(frozen=True)
class PrivateHistory:
    source_id: str
    basis: str
    original: Hashable
    steps: tuple[PrivateStep, ...]

    @property
    def schedule(self) -> tuple[str, ...]:
        return tuple(step.occurrence for step in self.steps)

    @property
    def bits(self) -> tuple[int, ...]:
        return tuple(step.private_bit for step in self.steps)

    @property
    def endpoint(self) -> CarrierPoint:
        if self.steps:
            return self.steps[-1].after
        return CarrierPoint(self.original, frozenset())

    @property
    def weight(self) -> Q:
        ans = Q(1)
        for step in self.steps:
            ans *= step.probability
        return ans

    @property
    def public_record(self) -> frozenset[tuple[str, str]]:
        return frozenset((step.occurrence, step.receipt) for step in self.steps)

    @property
    def event_tokens(self) -> frozenset[tuple[str, int]]:
        return frozenset((step.occurrence, step.private_bit) for step in self.steps)


@dataclass(frozen=True)
class FairTokenCarrier:
    """A finite instrument contract with a fully declared branch refinement.

    Payload equals the immutable original at preparation and is never changed.
    Enabledness depends only on already performed IDs, available publicly.
    The branch bit is genuine additional stochastic noise in the declared
    kernel, not a fictitious duplicate path inserted by a comparison map.
    """

    source_id: str = "no-ghost-fair-token-source"
    basis: str = "event-occurrence-and-private-bit"
    events: tuple[str, ...] = ("a", "b", "c")
    originals: tuple[Hashable, ...] = (0, 1)

    def __post_init__(self) -> None:
        if not self.source_id or not self.basis or not self.events or not self.originals:
            raise CoherenceError("Nonempty source, basis, events and originals required")
        if (any(type(e) is not str or not e for e in self.events)
                or len(set(self.events)) != len(self.events)):
            raise CoherenceError("Distinct named event occurrences required")
        if len(set(self.originals)) != len(self.originals):
            raise CoherenceError("Distinct original labels required")

    def branches(self, state: CarrierPoint, event: str) -> tuple[PrivateStep, ...]:
        if (state.payload not in self.originals
                or not state.completed <= frozenset(self.events)
                or event not in self.events or event in state.completed):
            raise CoherenceError("Unavailable action or ill-typed current state")
        after = CarrierPoint(state.payload, state.completed | {event})
        return tuple(PrivateStep(event, bit, "ok", state, after, Q(1, 2))
                     for bit in (0, 1))

    def history(self, original: Hashable, schedule: tuple[str, ...],
                bits: tuple[int, ...]) -> PrivateHistory:
        """Replay one declared possible branch; never mark it performed."""
        if original not in self.originals or len(schedule) != len(bits):
            raise CoherenceError("Unknown source or mismatched branch path")
        state = CarrierPoint(original, frozenset())
        steps = []
        for event, bit in zip(schedule, bits):
            if type(bit) is not int or bit not in (0, 1):
                raise CoherenceError("Exact private bit required")
            step = self.branches(state, event)[bit]
            steps.append(step)
            state = step.after
        return PrivateHistory(self.source_id, self.basis, original, tuple(steps))

    def check(self, history: PrivateHistory) -> bool:
        try:
            return history == self.history(history.original, history.schedule, history.bits)
        except (CoherenceError, TypeError, AttributeError):
            return False

    def full_histories(self, schedule: tuple[str, ...]) -> tuple[PrivateHistory, ...]:
        if len(schedule) != len(self.events) or set(schedule) != set(self.events):
            raise CoherenceError("A full schedule must contain each occurrence exactly once")
        return tuple(self.history(original, schedule, bits)
                     for original in self.originals
                     for bits in product((0, 1), repeat=len(schedule)))


def check_pair_table(table: PairTable, *, involutive: bool = True) -> bool:
    if (type(table) is not tuple or len(table) != 4
            or any(type(pair) is not tuple or len(pair) != 2
                   or any(type(v) is not int or v not in (0, 1) for v in pair)
                   for pair in table)
            or len(set(table)) != 4):
        return False
    return not involutive or all(table[2 * x + y] == pair
                                 for pair in product((0, 1), repeat=2)
                                 for x, y in (table[2 * pair[0] + pair[1]],))


def adjacent_compare(model: FairTokenCarrier, history: PrivateHistory,
                     position: int, table: PairTable = TOKEN_SWAP) -> PrivateHistory:
    if not model.check(history) or not check_pair_table(table):
        raise CoherenceError("A lawful history and involutive pair bijection are required")
    if type(position) is not int or not 0 <= position < len(history.steps) - 1:
        raise CoherenceError("Adjacent position outside the history")
    schedule, bits = list(history.schedule), list(history.bits)
    x, y = bits[position:position + 2]
    bits[position:position + 2] = table[2 * x + y]
    schedule[position], schedule[position + 1] = schedule[position + 1], schedule[position]
    return model.history(history.original, tuple(schedule), tuple(bits))


def compare_path(model: FairTokenCarrier, history: PrivateHistory,
                 path: tuple[int, ...], table: PairTable) -> PrivateHistory:
    for position in path:
        history = adjacent_compare(model, history, position, table)
    return history


def verify_pair_family(model: FairTokenCarrier, table: PairTable,
                       *, preserve_event_tokens: bool = False) -> bool:
    """Exhaust all full schedules/fibers; intended for this small experiment."""
    if not check_pair_table(table):
        return False
    for schedule in permutations(model.events):
        for original_history in model.full_histories(schedule):
            for position in range(len(schedule) - 1):
                moved = adjacent_compare(model, original_history, position, table)
                if (moved.original != original_history.original
                        or moved.source_id != original_history.source_id
                        or moved.basis != original_history.basis
                        or moved.endpoint != original_history.endpoint
                        or moved.public_record != original_history.public_record
                        or moved.weight != original_history.weight
                        or adjacent_compare(model, moved, position, table) != original_history):
                    return False
                if preserve_event_tokens and moved.event_tokens != original_history.event_tokens:
                    return False
                # The map is private-history-local: unrelated occurrences keep tokens.
                pair = frozenset(schedule[position:position + 2])
                before = original_history.event_tokens
                after = moved.event_tokens
                if {x for x in before if x[0] not in pair} != {x for x in after if x[0] not in pair}:
                    return False
    return True


@dataclass(frozen=True)
class CoherenceFailure:
    status: str
    initial: PrivateHistory
    pair_table: PairTable
    left_path: tuple[int, ...]
    right_path: tuple[int, ...]
    left_bits: tuple[int, ...]
    right_bits: tuple[int, ...]
    final_schedule: tuple[str, ...]


def find_braid_failure(model: FairTokenCarrier,
                       table: PairTable = CNOT_RELABEL) -> CoherenceFailure | None:
    if len(model.events) != 3 or not verify_pair_family(model, table):
        raise CoherenceError("This calibration requires three lawful independent events")
    for history in model.full_histories(model.events):
        left = compare_path(model, history, (0, 1, 0), table)
        right = compare_path(model, history, (1, 0, 1), table)
        if left != right:
            return CoherenceFailure("HIGHER_COHERENCE_FAILURE", history, table,
                                    (0, 1, 0), (1, 0, 1), left.bits, right.bits,
                                    left.schedule)
    return None


def verify_coherence_failure(model: FairTokenCarrier, cert: CoherenceFailure) -> bool:
    """Check a finite negative certificate with an independent raw tuple replay.

    It validates all pair maps before accepting the larger-loop discrepancy.
    It checks a *particular chosen map family*, never nonexistence of all
    coherent families.  No solver, timeout or floating point enters this gate.
    """
    if (type(cert) is not CoherenceFailure or cert.status != "HIGHER_COHERENCE_FAILURE"
            or len(model.events) != 3 or not model.check(cert.initial)
            or len(cert.initial.steps) != 3
            or not verify_pair_family(model, cert.pair_table)
            or cert.left_path != (0, 1, 0) or cert.right_path != (1, 0, 1)):
        return False

    # This path oracle does not use adjacent_compare or compare_path.
    outputs = []
    for path in (cert.left_path, cert.right_path):
        schedule = list(cert.initial.schedule)
        bits = list(cert.initial.bits)
        for i in path:
            index = (bits[i] << 1) | bits[i + 1]
            bits[i], bits[i + 1] = cert.pair_table[index]
            old = schedule[i]
            schedule[i] = schedule[i + 1]
            schedule[i + 1] = old
        outputs.append((tuple(schedule), tuple(bits)))
    return (outputs[0][0] == outputs[1][0] == cert.final_schedule
            and outputs[0][1] == cert.left_bits
            and outputs[1][1] == cert.right_bits
            and outputs[0][1] != outputs[1][1])
