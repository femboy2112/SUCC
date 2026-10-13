"""Carrier-indexed observational SUCC: original source, mutable state, actual history.

This module is an ADAPTER/UNIVERSAL CONTRACT over established finite source
and stochastic-history machinery, not an incompatible replacement.

A carrier consists of original preparation labels X, a current state stage C,
a nonnegative rational preparation law J_0 on X x C, lawful named instruments
C -> Prob(Receipt x C'), and an actual receipt history h.

The fundamental state of E after h is the UNNORMALIZED original/current law
    J_h(x,c) = P(original=x, current=c, actually recorded receipts=h).
Normalized posteriors arise only when P(h)>0. No original state is overwritten.

A carrier quotient q:C->Q is lawful when enabledness is fiber-constant and
every enabled instrument's FULL JOINT law (receipt, q'(next)) is fiber-constant.
Then, by finite reindexing, all source-indexed unnormalized history laws,
evidence probabilities and positive-event original posteriors are preserved.
The condition is sufficient and necessary for ALL initial Dirac source laws.
An exact finite stationary repair finds the COARSEST stable refinement of
a supplied current-state partition; it does not construct a new real sensor.

All source labels, stages, basis names, and probabilities are declared
MATHEMATICAL data. They do NOT authenticate real-world preparations,
license counterfactual cloning or resets, nor imply completed Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Hashable, Iterable


class CarrierError(ValueError):
    """A typed source, history, action access, or exact-law gate failed."""


def _label(x: Hashable) -> None:
    try:
        hash(x)
    except TypeError as exc:
        raise CarrierError("Carrier labels and reports must be hashable") from exc


def rat(x) -> Q:
    if type(x) is int or type(x) is Q:
        return Q(x)
    raise CarrierError("Use exact int/Fraction, never float or bool")


def labels_partition(labels: Iterable[int]) -> tuple[int, ...]:
    labels = tuple(labels)
    if not labels or any(type(x) is not int or x < 0 for x in labels):
        raise CarrierError("Finite nonempty partition labels required")
    seen: dict[int, int] = {}
    return tuple(seen.setdefault(x, len(seen)) for x in labels)


def _mass(rows: tuple[tuple[Q, ...], ...], width: int,
          *, normalized: bool) -> tuple[tuple[Q, ...], ...]:
    if (type(rows) is not tuple or not rows or type(width) is not int
            or width < 1 or any(type(row) is not tuple or len(row) != width
                               for row in rows)):
        raise CarrierError("Total rectangular original/current source law required")
    exact = tuple(tuple(rat(v) for v in row) for row in rows)
    if any(v < 0 for row in exact for v in row):
        raise CarrierError("Negative source probability forbidden")
    total = sum((sum(row, Q(0)) for row in exact), Q(0))
    if normalized and total != 1:
        raise CarrierError("Initial source preparation must be a normalized joint law")
    if not normalized and not (0 < total <= 1):
        raise CarrierError("An actual receipt history needs positive subprobability")
    return exact


def mass_total(rows: tuple[tuple[Q, ...], ...]) -> Q:
    return sum((sum(row, Q(0)) for row in rows), Q(0))


@dataclass(frozen=True)
class CarrierStage:
    source_id: str
    basis: str
    epoch: int
    name: str
    states: tuple[Hashable, ...]

    def __post_init__(self):
        if (any(type(x) is not str or not x for x in
                (self.source_id, self.basis, self.name))
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.states) is not tuple or not self.states):
            raise CarrierError("Explicit source, basis, epoch and finite carrier required")
        for state in self.states:
            _label(state)
        if len(set(self.states)) != len(self.states):
            raise CarrierError("Carrier states must be distinct")

    @property
    def count(self) -> int:
        return len(self.states)


@dataclass(frozen=True)
class Carrier:
    """Prepared source object: immutable original labels and a current stage."""
    originals: tuple[Hashable, ...]
    stage: CarrierStage
    preparation: tuple[tuple[Q, ...], ...]
    empirically_authenticated: bool = False

    def __post_init__(self):
        if type(self.originals) is not tuple or not self.originals:
            raise CarrierError("Explicit original-source labels required")
        for x in self.originals:
            _label(x)
        if len(set(self.originals)) != len(self.originals):
            raise CarrierError("Original source labels must be distinct")
        prep = _mass(self.preparation, self.stage.count, normalized=True)
        object.__setattr__(self, "preparation", prep)
        if len(self.preparation) != len(self.originals):
            raise CarrierError("One prepared current-state law per original label")
        if self.empirically_authenticated:
            raise CarrierError("A declared finite simulator cannot attest empirical source")

    def root(self) -> "ActualHistory":
        return ActualHistory(self, self.stage, self.preparation)


@dataclass(frozen=True)
class CarrierInstrument:
    """A typed stochastic instrument, including access and the full joint law."""
    name: str
    before: CarrierStage
    after: CarrierStage
    receipts: tuple[Hashable, ...]
    enabled: tuple[bool, ...]
    rows: tuple[tuple[tuple[int, int, Q], ...], ...]
    cost: Q = Q(1)

    def __post_init__(self):
        if (type(self.name) is not str or not self.name
                or self.before.source_id != self.after.source_id
                or self.before.basis != self.after.basis
                or self.after.epoch < self.before.epoch
                or type(self.receipts) is not tuple or not self.receipts
                or type(self.enabled) is not tuple
                or len(self.enabled) != self.before.count
                or any(type(x) is not bool for x in self.enabled)
                or type(self.rows) is not tuple
                or len(self.rows) != self.before.count):
            raise CarrierError("Unlawful source/basis/epoch or incomplete instrument")
        for r in self.receipts:
            _label(r)
        if len(set(self.receipts)) != len(self.receipts):
            raise CarrierError("Distinct typed receipts required")
        if rat(self.cost) < 0:
            raise CarrierError("Instrument has negative declared cost")
        checked = []
        for row in self.rows:
            if type(row) is not tuple or not row:
                raise CarrierError("Every source state needs a complete joint kernel")
            masses: dict[tuple[int, int], Q] = {}
            for z, after, weight in row:
                if (type(z) is not int or not 0 <= z < len(self.receipts)
                        or type(after) is not int
                        or not 0 <= after < self.after.count):
                    raise CarrierError("Joint atom outside typed receipt or next state")
                p = rat(weight)
                if p < 0:
                    raise CarrierError("Negative joint atom")
                masses[(z, after)] = masses.get((z, after), Q(0)) + p
            if sum(masses.values(), Q(0)) != 1:
                raise CarrierError("Each declared joint action row must sum to one")
            checked.append(tuple((z, y, p) for (z, y), p in sorted(masses.items()) if p))
        object.__setattr__(self, "rows", tuple(checked))
        object.__setattr__(self, "cost", rat(self.cost))

    def receipt_index(self, receipt: Hashable) -> int:
        _label(receipt)
        try:
            return self.receipts.index(receipt)
        except ValueError as exc:
            raise CarrierError("Unknown/unavailable receipt") from exc


@dataclass(frozen=True)
class CarrierEvent:
    action: str
    receipt: Hashable
    conditional_likelihood: Q
    before: str
    after: str


@dataclass(frozen=True)
class CarrierVerdict:
    status: str
    value: Hashable | None = None


@dataclass(frozen=True)
class ActualHistory:
    """A single ACTUAL public history and its original/current subprobability."""
    root_source: Carrier
    current: CarrierStage
    mass: tuple[tuple[Q, ...], ...]
    events: tuple[CarrierEvent, ...] = ()

    def __post_init__(self):
        if (self.current.source_id != self.root_source.stage.source_id
                or self.current.basis != self.root_source.stage.basis
                or self.current.epoch < self.root_source.stage.epoch
                or type(self.events) is not tuple
                or any(type(e) is not CarrierEvent for e in self.events)):
            raise CarrierError("Unlicensed changing-source history")
        mass = _mass(self.mass, self.current.count, normalized=False)
        object.__setattr__(self, "mass", mass)
        if len(self.mass) != len(self.root_source.originals):
            raise CarrierError("Original-indexed joint law changed its source")

    @property
    def evidence(self) -> Q:
        return mass_total(self.mass)

    @property
    def original_posterior(self) -> tuple[Q, ...]:
        return tuple(sum(row, Q(0)) / self.evidence for row in self.mass)

    @property
    def originals_supported(self) -> frozenset[Hashable]:
        return frozenset(x for x, row in zip(self.root_source.originals, self.mass)
                         if any(v > 0 for v in row))

    def decide_original(self, target: tuple[Hashable, ...]) -> CarrierVerdict:
        if type(target) is not tuple or len(target) != len(self.root_source.originals):
            raise CarrierError("Original target requires one label per original state")
        vals = {value for value, row in zip(target, self.mass)
                if any(p > 0 for p in row)}
        if not vals:
            return CarrierVerdict("INCONSISTENT_SOURCE", None)
        if len(vals) != 1:
            return CarrierVerdict("AMBIGUOUS", None)
        return CarrierVerdict("CERTIFIED_MODEL_RELATIVE", next(iter(vals)))

    def available(self, instrument: CarrierInstrument) -> bool:
        if instrument.before != self.current:
            raise CarrierError("Instrument is not typed to the current carrier stage")
        return all(instrument.enabled[c] for row in self.mass
                   for c, p in enumerate(row) if p > 0)

    def advance(self, instrument: CarrierInstrument,
                receipt: Hashable) -> "ActualHistory":
        if instrument.before != self.current:
            raise CarrierError("Instrument source/basis/epoch/current mismatch")
        if not self.available(instrument):
            # Do not secretly learn hidden source state through action availability.
            raise CarrierError("Action unavailable for some currently supported carrier state")
        z = instrument.receipt_index(receipt)
        target = [[Q(0) for _ in range(instrument.after.count)]
                  for _ in self.root_source.originals]
        for o, original_row in enumerate(self.mass):
            for c, mass in enumerate(original_row):
                if not mass:
                    continue
                for report, after, weight in instrument.rows[c]:
                    if report == z:
                        target[o][after] += mass * weight
        result = tuple(tuple(row) for row in target)
        probability = mass_total(result)
        if not probability:
            raise CarrierError("Impossible observation is not an actualized history")
        event = CarrierEvent(instrument.name, receipt, probability / self.evidence,
                             instrument.before.name, instrument.after.name)
        return ActualHistory(self.root_source, instrument.after, result,
                             self.events + (event,))

    def verify(self, registry: dict[str, CarrierInstrument]) -> bool:
        replay = self.root_source.root()
        for event in self.events:
            if event.action not in registry:
                raise CarrierError("History lacks an actual instrument contract")
            replay = replay.advance(registry[event.action], event.receipt)
        if replay != self:
            raise CarrierError("Forged, stale or probability-corrupted history")
        return True


@dataclass(frozen=True)
class CarrierQuotient:
    """A source/stage-pinned surjective current carrier report (not source erasure)."""
    stage: CarrierStage
    labels: tuple[int, ...]
    view: str

    def __post_init__(self):
        if (type(self.labels) is not tuple or len(self.labels) != self.stage.count
                or labels_partition(self.labels) != self.labels
                or type(self.view) is not str or not self.view):
            raise CarrierError("Complete canonical carrier partition required")

    @property
    def image(self) -> CarrierStage:
        return CarrierStage(self.stage.source_id, self.stage.basis,
                            self.stage.epoch, self.view,
                            tuple(range(len(set(self.labels)))))

    def push(self, mass: tuple[tuple[Q, ...], ...]) -> tuple[tuple[Q, ...], ...]:
        old = _mass(mass, self.stage.count, normalized=False)
        result = [[Q(0) for _ in self.image.states] for _ in old]
        for i, row in enumerate(old):
            for c, p in enumerate(row):
                result[i][self.labels[c]] += p
        return tuple(tuple(row) for row in result)

    def root(self, source: Carrier) -> Carrier:
        if source.stage != self.stage:
            raise CarrierError("Preparation and quotient carriers differ")
        return Carrier(source.originals, self.image, self.push(source.preparation))


@dataclass(frozen=True)
class CarrierObstruction:
    action: str
    state_a: Hashable
    state_b: Hashable
    old_view: int
    issue: str
    report_a: tuple
    report_b: tuple


@dataclass(frozen=True)
class CarrierDescent:
    valid: bool
    witness: CarrierObstruction | None
    quotient_instrument: CarrierInstrument | None


def _joint_signature(instrument: CarrierInstrument, current: int,
                     future: CarrierQuotient) -> tuple:
    masses: dict[tuple[int, int], Q] = {}
    for report, after, p in instrument.rows[current]:
        atom = (report, future.labels[after])
        masses[atom] = masses.get(atom, Q(0)) + p
    return tuple(sorted((z, q, p) for (z, q), p in masses.items() if p))


def audit_descent(instrument: CarrierInstrument, before: CarrierQuotient,
                  after: CarrierQuotient) -> CarrierDescent:
    """Necessary and sufficient *all-prior* joint-instrument law criterion."""
    if instrument.before != before.stage or instrument.after != after.stage:
        raise CarrierError("Invalid source-indexed quotient/action square")
    representatives: dict[int, int] = {}
    for c, block in enumerate(before.labels):
        if block not in representatives:
            representatives[block] = c
            continue
        rep = representatives[block]
        if instrument.enabled[rep] != instrument.enabled[c]:
            return CarrierDescent(False, CarrierObstruction(
                instrument.name, before.stage.states[rep], before.stage.states[c],
                block, "ENABLEDNESS", (instrument.enabled[rep],),
                (instrument.enabled[c],)), None)
        if instrument.enabled[c]:
            left = _joint_signature(instrument, rep, after)
            right = _joint_signature(instrument, c, after)
            if left != right:
                return CarrierDescent(False, CarrierObstruction(
                    instrument.name, before.stage.states[rep], before.stage.states[c],
                    block, "JOINT_RECEIPT_AND_NEXT", left, right), None)
    newrows = []
    enabled = []
    for block in range(len(representatives)):
        c = representatives[block]
        available = instrument.enabled[c]
        enabled.append(available)
        if available:
            newrows.append(_joint_signature(instrument, c, after))
        else:
            # This dummy total row is INACCESSIBLE: the enabled flag blocks use.
            newrows.append(((0, 0, Q(1)),))
    descended = CarrierInstrument(
        instrument.name, before.image, after.image,
        instrument.receipts, tuple(enabled), tuple(newrows), instrument.cost)
    return CarrierDescent(True, None, descended)


def checked_descent(instrument: CarrierInstrument, before: CarrierQuotient,
                    after: CarrierQuotient) -> CarrierInstrument:
    result = audit_descent(instrument, before, after)
    if not result.valid:
        raise CarrierError("Carrier quotient obstruction: " + str(result.witness))
    assert result.quotient_instrument is not None
    return result.quotient_instrument


def compare_histories(history: ActualHistory,
                      before: CarrierQuotient,
                      after: CarrierQuotient,
                      action: CarrierInstrument,
                      receipt: Hashable) -> dict:
    """Independently execute both sides of a witnessed commuting square."""
    if history.current != before.stage or history.root_source.stage != before.stage:
        raise CarrierError("One-step comparison requires a prepared before-stage root")
    small_root = before.root(history.root_source)
    coarse_action = checked_descent(action, before, after)
    original_next = history.advance(action, receipt)
    coarse_next = small_root.root().advance(coarse_action, receipt)
    if after.push(original_next.mass) != coarse_next.mass:
        raise AssertionError("Original-indexed unnormalized carrier law failed transport")
    if original_next.evidence != coarse_next.evidence:
        raise AssertionError("Probability of actual receipt failed transport")
    if original_next.original_posterior != coarse_next.original_posterior:
        raise AssertionError("Original-source posterior failed transport")
    return {"source":history.root_source.stage.source_id,
            "fine_evidence":original_next.evidence,
            "coarse_evidence":coarse_next.evidence,
            "original_posterior":original_next.original_posterior,
            "lawful_original_preservation":True}


@dataclass(frozen=True)
class RefinementStep:
    split_action: str
    before_classes: int
    after_classes: int
    old_partition: tuple[int, ...]
    new_partition: tuple[int, ...]


@dataclass(frozen=True)
class CarrierRepair:
    partition: tuple[int, ...]
    steps: tuple[RefinementStep, ...]
    validated_actions: tuple[str, ...]
    stabilized: bool


def _action_profiles(actions: tuple[CarrierInstrument, ...],
                     c: int, labels: tuple[int, ...]) -> tuple:
    out = []
    for action in actions:
        if not action.enabled[c]:
            out.append((action.name, False, ()))
        else:
            totals: dict[tuple[int, int], Q] = {}
            for receipt, after, p in action.rows[c]:
                key = (receipt, labels[after])
                totals[key] = totals.get(key, Q(0)) + p
            out.append((action.name, True, tuple(sorted(
                (r, block, value) for (r, block), value in totals.items() if value))))
    return tuple(out)


def minimal_stationary_repair(
        stage: CarrierStage, actions: tuple[CarrierInstrument, ...],
        seed_labels: tuple[int, ...] | None = None) -> CarrierRepair:
    """Least extra observational information for ALL permitted future words.

    This is classical probabilistic partition refinement for the full
    joint receipt/next-state law and availability. No oracle completeness
    is certified by the algorithm: the menu/table completeness is a premise.
    """
    if type(actions) is not tuple or not actions or any(
            a.before != stage or a.after != stage for a in actions):
        raise CarrierError("Complete stationary source action menu required")
    if len({a.name for a in actions}) != len(actions):
        raise CarrierError("Duplicate action names")
    labels = tuple(0 for _ in stage.states) if seed_labels is None else labels_partition(seed_labels)
    if len(labels) != stage.count:
        raise CarrierError("Seed partition must cover every carrier state")
    steps = []
    for _ in range(stage.count):
        signatures = tuple((labels[c], _action_profiles(actions, c, labels))
                           for c in range(stage.count))
        seen: dict[tuple, int] = {}
        refined = tuple(seen.setdefault(key, len(seen)) for key in signatures)
        if refined == labels:
            view = CarrierQuotient(stage, labels, stage.name + ":repaired")
            for action in actions:
                if not audit_descent(action, view, view).valid:
                    raise AssertionError("Stationary repair failed to stabilize")
            return CarrierRepair(labels, tuple(steps), tuple(a.name for a in actions), True)
        if len(set(refined)) <= len(set(labels)):
            raise AssertionError("Strict nonmonotonic carrier refinement")
        # Record a concrete action separating some previously aliased pair.
        action_name = next((a.name for a in actions if
                            any(labels[c] == labels[d] and refined[c] != refined[d]
                                and _action_profiles((a,), c, labels) !=
                                _action_profiles((a,), d, labels)
                                for c in range(stage.count) for d in range(c))), "")
        steps.append(RefinementStep(action_name, len(set(labels)),
                                    len(set(refined)), labels, refined))
        labels = refined
    raise AssertionError("Finite complete carrier should stabilize in at most |C| steps")


def from_deterministic_lawful_source(source, prior: tuple[Q, ...]):
    """Lossless adapter for SWM F48's LawfulSource, with EXPLICIT prior.

    This does not equate counterfactual branches with performed events.
    """
    from .swarm_lawful_history import LawfulSource
    if not isinstance(source, LawfulSource):
        raise CarrierError("Require a checked deterministic LawfulSource")
    prior = tuple(rat(v) for v in prior)
    if len(prior) != len(source.initial) or sum(prior, Q(0)) != 1 or any(p < 0 for p in prior):
        raise CarrierError("Original preparation prior must be explicit")
    stage = CarrierStage(source.source_id, source.digest, 0, "lawful-current",
                         tuple(range(source.count)))
    prep = tuple(tuple(prob if c == source.initial[o] else Q(0)
                       for c in range(source.count))
                 for o, prob in enumerate(prior))
    root = Carrier(tuple(range(len(source.initial))), stage, prep)
    actions = {}
    for act in source.instruments:
        receipt_labels = tuple(dict.fromkeys(act.outcome))
        rows = tuple(((receipt_labels.index(act.outcome[c]), act.after[c], Q(1)),)
                     for c in range(source.count))
        actions[act.name] = CarrierInstrument(
            act.name, stage, stage, receipt_labels, act.enabled, rows)
    return root, actions


def from_stochastic_history(history, instrument):
    """Lossless adapter for an EXISTING prepared SWM StochasticHistory."""
    from .swarm_probability import StochasticHistory, StochasticInstrument
    if not isinstance(history, StochasticHistory) or not isinstance(instrument, StochasticInstrument):
        raise CarrierError("Require exact existing stochastic source objects")
    if (history.source_id != instrument.source_id or
            history.current_space != instrument.input_space):
        raise CarrierError("Original stochastic source context mismatch")
    if history.events or history.path_probability != 1:
        raise CarrierError(
            "A lossless prepared-history adapter cannot erase past receipts; "
            "supply a source-aware checkpoint transport instead")
    stage = CarrierStage(history.source_id, history.initial_space, 0,
                         history.current_space,
                         tuple(range(len(history.joint[0]))))
    after = CarrierStage(history.source_id, history.initial_space, 1,
                         instrument.output_space, tuple(range(instrument.after_count)))
    origin = Carrier(tuple(range(len(history.initial_joint))), stage,
                     history.joint)
    receipts = tuple(dict.fromkeys(r for row in instrument.rows for r, _, _ in row))
    adapted_rows = tuple(tuple((receipts.index(r), y, Q(p))
                               for r, y, p in row)
                         for row in instrument.rows)
    adapted = CarrierInstrument(
        instrument.name, stage, after, receipts,
        tuple(True for _ in stage.states), adapted_rows, instrument.cost)
    return origin, adapted
