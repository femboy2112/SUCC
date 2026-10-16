"""Finite indexed effects over SUCC-lambda and declared recording histories.

This interpreter checks model-relative data flow, not instrument authenticity.
Only replay refers to primitive recording identities. Pure derivation,
testimony, predictions, miniature models and analytic imports cannot mint one.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .source_lambda import (Atlas, Passport, Report, FuncT, PairT, check,
                           execute, signed_witness, AccessGap, TypeFault)


class EffectError(ValueError):
    pass


class Kind(str, Enum):
    RECORDED = "RECORDED_OBSERVATION_REPLAY"
    DERIVED = "DERIVED_MATHEMATICAL_VALUE"
    PROGRAM = "UNEXECUTED_LATENT_PROGRAM"
    PREDICTED = "COUNTERFACTUAL_PREDICTION"
    TESTIMONY = "EXTERNAL_TESTIMONY"
    INTERVENTION = "SOURCE_CHANGING_MODEL_INTERVENTION"
    MINIATURE = "CERTIFIED_MINIATURE_ACTION_MODEL"
    ANALYTIC = "CLASSICAL_IMPORTED_WITH_OBLIGATIONS"
    EXACT = "EXACT_FINITE_CHECK"


def _name(value):
    if type(value) is not str or not value:
        raise EffectError("nonempty identity required")


def _program_type(t):
    return isinstance(t, FuncT) or (isinstance(t, PairT) and
                                   (_program_type(t.left) or _program_type(t.right)))


@dataclass(frozen=True)
class Event:
    identity: str
    origin: str
    passport: Passport
    modulus: int
    value: int
    history: tuple[str, ...] = ()

    def __post_init__(self):
        _name(self.identity)
        _name(self.origin)
        Atlas(self.passport, ((self.modulus, self.value),))
        if type(self.history) is not tuple:
            raise EffectError("immutable event history required")
        for a in self.history:
            _name(a)


@dataclass(frozen=True)
class Context:
    passport: Passport
    events: tuple[Event, ...]
    # A declared realized global action path, not a union of possible paths.
    history: tuple[str, ...] = ()

    def __post_init__(self):
        if not isinstance(self.passport, Passport) or type(self.events) is not tuple:
            raise EffectError("source passport and immutable recording registry required")
        if any(not isinstance(e, Event) for e in self.events):
            raise EffectError("invalid recording")
        if len({e.identity for e in self.events}) != len(self.events):
            raise EffectError("one recording identity cannot name two events")
        if type(self.history) is not tuple:
            raise EffectError("immutable source history required")
        for a in self.history:
            _name(a)
        # Registry can archive other epochs. Admission happens only on replay.
        rows = {}
        for e in self.events:
            if e.passport == self.passport and self.history[:len(e.history)] == e.history:
                if e.modulus in rows and rows[e.modulus] != e.value:
                    raise EffectError("inconsistent frozen-source recording history")
                rows[e.modulus] = e.value
        Atlas(self.passport, tuple(sorted(rows.items())))

    def event(self, identity):
        for e in self.events:
            if e.identity == identity:
                if e.passport != self.passport:
                    raise EffectError("foreign source, epoch or basis")
                if self.history[:len(e.history)] != e.history:
                    raise AccessGap("record belongs to an unperformed incompatible path")
                return e
        raise AccessGap("unperformed recording identity")


@dataclass(frozen=True)
class Replay:
    event: str
    actor: str


@dataclass(frozen=True)
class Derive:
    term: object
    inputs: tuple[int, ...]
    actor: str


@dataclass(frozen=True)
class Predict:
    term: object
    hypothetical: Atlas
    actor: str


@dataclass(frozen=True)
class Relay:
    input: int
    sender: str
    recipient: str


@dataclass(frozen=True)
class AnalyticImport:
    statement: str
    assumptions: tuple[str, ...]
    inputs: tuple[int, ...] = ()


@dataclass(frozen=True)
class ExactQuadratic:
    matrix: tuple
    vector: tuple
    inputs: tuple[int, ...] = ()


@dataclass(frozen=True)
class Artifact:
    kind: Kind
    passport: Passport
    value: object
    origins: frozenset[str]
    audience: frozenset[str]
    obligations: frozenset[str]
    # Provenance is not a decoder permission. A compressed derived report may
    # cite a richer event without giving its receiver the underlying reading.
    readable_events: frozenset[str]
    # Immediate dataflow edges retain causal lineage independently of origins.
    parents: tuple[int, ...]


@dataclass(frozen=True)
class Execution:
    artifacts: tuple[Artifact, ...]
    grade: tuple[tuple[str, int], ...]
    referenced_origins: frozenset[str]
    new_physical_measurements: int = 0
    original_source_authenticated: bool = False
    global_theorem_proved: bool = False


def run(program: tuple, context: Context) -> Execution:
    """Evaluate a finite DAG of effects; indices must reference earlier outputs.

The additive grade counts effect executions, not statistical independence.
Origin sets compose by union and copying is idempotent on physical origins.
Analytic debts compose by union and no constructor discharges them.
"""
    if type(program) is not tuple or not isinstance(context, Context):
        raise EffectError("finite program tuple and explicit context required")
    outputs = []
    counts = {k.value: 0 for k in Kind}

    def refs(indices):
        if type(indices) is not tuple or any(type(i) is not int or not 0 <= i < len(outputs)
                                             for i in indices):
            raise EffectError("only already executed dataflow references are allowed")
        return [outputs[i] for i in indices]

    for command in program:
        origins = frozenset()
        audience = frozenset()
        debts = frozenset()
        readable = frozenset()
        parents = ()
        if isinstance(command, Replay):
            e = context.event(command.event)
            if command.actor != e.origin:
                raise EffectError("recipient cannot claim the origin's recording")
            kind, value = Kind.RECORDED, Report(e.passport, e.modulus, e.value, (e.identity,))
            origins, audience = frozenset((e.identity,)), frozenset((e.origin,))
            readable = origins
        elif isinstance(command, Derive):
            _name(command.actor)
            parents = command.inputs
            inputs = refs(parents)
            for a in inputs:
                if a.kind not in (Kind.RECORDED, Kind.DERIVED, Kind.TESTIMONY):
                    raise EffectError("predictions, proof imports and latent programs are not readings")
                if command.actor not in a.audience:
                    raise EffectError("evidence must actually be communicated to the actor")
            available = frozenset().union(*(a.readable_events for a in inputs))
            events = [context.event(i) for i in sorted(available)]
            rows = tuple(sorted({(e.modulus, e.value) for e in events}))
            result = execute(command.term, Atlas(context.passport, rows))
            origins = frozenset(e.identity for e in events if e.modulus in result.observed)
            kind = Kind.PROGRAM if _program_type(result.type) else Kind.DERIVED
            value = result.value
            audience = frozenset((command.actor,))
            debts = frozenset().union(*(a.obligations for a in inputs))
        elif isinstance(command, Predict):
            _name(command.actor)
            if command.hypothetical.passport != context.passport:
                raise EffectError("prediction must name the declared current source model")
            result = execute(command.term, command.hypothetical)
            kind, value = Kind.PREDICTED, result.value
            audience = frozenset((command.actor,))
            debts = frozenset(("COUNTERFACTUAL_NOT_RECORDED",))
        elif isinstance(command, Relay):
            parents = (command.input,)
            a, = refs(parents)
            _name(command.recipient)
            if command.sender not in a.audience:
                raise EffectError("sender never received this evidence")
            if a.kind not in (Kind.RECORDED, Kind.DERIVED, Kind.TESTIMONY):
                raise EffectError("testimony cannot launder a prediction or latent program")
            kind, value = Kind.TESTIMONY, a.value
            origins, debts = a.origins, a.obligations
            readable = a.readable_events
            audience = a.audience | frozenset((command.recipient,))
        elif isinstance(command, AnalyticImport):
            _name(command.statement)
            if type(command.assumptions) is not tuple:
                raise EffectError("explicit immutable analytic assumptions required")
            for assumption in command.assumptions:
                _name(assumption)
            parents = command.inputs
            inputs = refs(parents)
            kind, value = Kind.ANALYTIC, command.statement
            debts = frozenset(command.assumptions) | frozenset((
                "IMPORTED_STATEMENT_PROOF_NOT_REPLAYED", "SOURCE_TO_THEOREM_IDENTIFICATION"))
            debts |= frozenset().union(*(a.obligations for a in inputs))
            origins = frozenset().union(*(a.origins for a in inputs))
        elif isinstance(command, ExactQuadratic):
            parents = command.inputs
            inputs = refs(parents)
            value = signed_witness(command.matrix, command.vector)
            kind = Kind.EXACT
            origins = frozenset().union(*(a.origins for a in inputs))
            debts = frozenset(("FINITE_MATRIX_TO_ORIGINAL_SOURCE_IDENTIFICATION",))
            debts |= frozenset().union(*(a.obligations for a in inputs))
        else:
            raise EffectError("unregistered effect constructor")
        counts[kind.value] += 1
        outputs.append(Artifact(kind, context.passport, value, origins, audience, debts,
                                readable, parents))
    return Execution(tuple(outputs), tuple(counts.items()),
                     frozenset().union(*(a.origins for a in outputs)))


@dataclass(frozen=True)
class MacroState:
    """Finite model state for a uniformly legal, capability-consuming action.

Every action changes the epoch conservatively. Its output is a possibility
set, never a source observation. Actual instrumental execution is external.
"""
    original: Passport
    current: Passport
    possible: frozenset[str]
    capabilities: frozenset[str]
    history: tuple[str, ...] = ()

    def __post_init__(self):
        if not isinstance(self.original, Passport) or not isinstance(self.current, Passport):
            raise EffectError("original and current passports required")
        if type(self.possible) is not frozenset or type(self.capabilities) is not frozenset:
            raise EffectError("immutable possible states and capabilities required")
        if type(self.history) is not tuple or self.current.epoch < self.original.epoch:
            raise EffectError("invalid chronological macro state")
        for value in (*self.possible, *self.capabilities, *self.history):
            _name(value)


def miniature_action(state: MacroState, port, action: str, capability: str):
    from .consensus_lambda import MiniPort
    if not isinstance(state, MacroState) or not isinstance(port, MiniPort):
        raise EffectError("declared macro state and real MATRYOSHKA port required")
    if state.current.source_id != state.original.source_id or state.current.basis != state.original.basis:
        raise EffectError("intervention cannot silently relabel source or basis")
    port.validate(state.current)
    if capability not in state.capabilities or not state.possible:
        raise AccessGap("unavailable or consumed macro capability")
    if not state.possible <= set(port.parent.states) or action not in port.macros:
        raise EffectError("unknown parent state or miniature action")
    states = set(state.possible)
    word = port.macros[action]
    for token in word:
        targets = {port.parent.actions[token][s] for s in states}
        if None in targets:
            raise AccessGap("macro unsafe in a surviving source state")
        states = targets
    nxt = MacroState(state.original,
                     Passport(state.current.source_id, state.current.epoch + 1, state.current.basis),
                     frozenset(states), state.capabilities - {capability}, state.history + word)
    receipt = {"effects": (Kind.MINIATURE.value, Kind.INTERVENTION.value),
               "status": "EXACT_FINITE_TRANSITION_MODEL", "word": word,
               "physical_action_executed": False, "new_observations": 0,
               "original_source_retained": state.original == nxt.original}
    return nxt, receipt
