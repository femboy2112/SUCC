"""Relative path/value deltas and operational knowledge synchronization.

This is an exact finite, deterministic research instrument. It strengthens
the earlier snapshot definition of field placement to include knowledge,
the complete epistemically/physically accessible probe frontier, used probes,
and the public inference language. Raw event origin remains in a separate
causal ledger. Sender testimony requires external trust; SHA-256 is ONLY a
context-consistency checksum and cannot authenticate a physical measurement.

A relative packet never transmits a source-state snapshot or absolute probe
name. Each path token means "perform the next causally enabled sender batch";
its value tokens encode only non-deducible outcomes relative to the receiver's
last knowledge position. The complete public source table and interpretation
are assumed shared and therefore excluded from packet costs.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import json

from .absorbing_frames import HornRule
from .knowledge_ladder import (
    AgentKnowledge, ProbeBatch, SharedKnowledgeBasis, KnowledgeLadderError,
    _strict_batch_step, _wire, _hash,
)
from .observer_traps import FiniteProbeWorld


class RelativeDeltaError(ValueError):
    """A different basis, false code, illegal path, or unsupported inference."""


def operational_position(agent: AgentKnowledge, basis: SharedKnowledgeBasis) -> tuple:
    """A deterministic same-knowledge, same-probes, same-reasoner signature.

    Includes the set of already-observed probe/value pairs, because a future
    source experiment cannot be repeated merely to fake progress. Event
    origin and local clock count are excluded from this *epistemic* signature;
    provenance is checked separately through the strict trace.
    """
    model = agent.model(basis)
    registered = dict(basis.observers)
    feasible = tuple(p for p in basis.world.probes
                     if p in registered[agent.observer])
    already = {p for p, _ in agent.observations()}
    observed = tuple((p, dict(agent.observations())[p]) for p in basis.world.probes
                     if p in already)
    currently_accessible = tuple(p for p in model.epistemically_accessible
                                 if p in feasible)
    unobserved = tuple(p for p in currently_accessible if p not in already)
    return (basis.fingerprint, model.compatible, model.predicted,
            model.closure.atoms, model.epistemically_accessible, feasible,
            currently_accessible, observed, unobserved)


def operational_digest(agent: AgentKnowledge, basis: SharedKnowledgeBasis) -> str:
    return _hash(operational_position(agent, basis))


@dataclass(frozen=True)
class ContinuationCertificate:
    equivalent: bool
    sources_checked: tuple[str, ...]
    local_transitions_checked: int
    reason: str
    scope: str = "finite deterministic source probes; no concurrent/asynchronous transport"


def certify_finite_continuation(
    a: AgentKnowledge, b: AgentKnowledge, basis: SharedKnowledgeBasis,
) -> ContinuationCertificate:
    """Independent exhaustive finite bisimulation-style positive control.

    For this single-use deterministic source system, equal operational
    position implies the same set of probe actions and the same source
    outcome for each compatible actual source at every later SUCC step.
    This implementation enumerates every possible remaining actual source.
    General stochastic, quantum, semantic-language-revision and physical
    elapsed-time bisimulation are NOT established.
    """
    if operational_position(a, basis) != operational_position(b, basis):
        return ContinuationCertificate(False, (), 0, "Initial operational position differs")
    sources = a.model(basis).compatible
    checked = 0
    for actual in sources:
        left, right = a, b
        for _ in range(len(basis.world.probes) + 1):
            if operational_position(left, basis) != operational_position(right, basis):
                return ContinuationCertificate(False, sources, checked, "Transition mismatch")
            nleft = left.local_succ(basis, actual)
            nright = right.local_succ(basis, actual)
            checked += 1
            if operational_position(nleft, basis) != operational_position(nright, basis):
                return ContinuationCertificate(False, sources, checked, "Observation mismatch")
            if nleft == left and nright == right:
                break
            left, right = nleft, nright
        else:
            raise ArithmeticError("Finite single-use source observation did not terminate")
    return ContinuationCertificate(True, sources, checked,
                                   "All compatible-source continuations matched")


def _enabled_new_probes(
    state: AgentKnowledge, basis: SharedKnowledgeBasis, sender: str
) -> tuple[str, ...]:
    model = state.model(basis)
    used = {p for p, _ in state.observations()}
    feasible = set(dict(basis.observers)[sender])
    return tuple(p for p in model.epistemically_accessible
                 if p in feasible and p not in used)


def _choices(state: AgentKnowledge, basis: SharedKnowledgeBasis, probe: str):
    model = state.model(basis)
    return tuple(sorted({basis.world.outcome(x, probe) for x in model.compatible}))


def encode_relative_delta(
    sender: AgentKnowledge, receiver: AgentKnowledge, basis: SharedKnowledgeBasis,
) -> bytes:
    """One bounded patch, relative to the recipient's exact last position.

    path = indices in the NEXT permitted local probe frontier.
    values = None when all remaining source candidates agree, otherwise
             the index of the actual outcome among their possible values.
    """
    if sender.observer == receiver.observer:
        raise RelativeDeltaError("Must transfer between distinct observers")
    if receiver.batches != sender.batches[:len(receiver.batches)]:
        raise RelativeDeltaError("An exact common causal prefix is required")
    additional = sender.batches[len(receiver.batches):]
    if len(additional) > 64:
        raise RelativeDeltaError("Bounded finite relay step budget exceeded")
    trial = receiver
    steps = []
    for batch in additional:
        enabled = _enabled_new_probes(trial, basis, sender.observer)
        if batch.origin != sender.observer or tuple(p for p, _ in batch.outcomes) != enabled:
            raise RelativeDeltaError("Source-attested batch violates available path")
        choices = []
        for p, value in batch.outcomes:
            outputs = _choices(trial, basis, p)
            if value not in outputs:
                raise RelativeDeltaError("The actual outcome is impossible in current model")
            choices.append(None if len(outputs) == 1 else outputs.index(value))
        steps.append({"path": list(range(len(enabled))), "values": choices})
        trial = _strict_batch_step(trial, batch, basis, sender.observer)
    if operational_position(trial, basis) != operational_position(sender, basis):
        raise RelativeDeltaError("Causal trace does not reconstruct sender state")
    return _wire({
        "kind": "relative-path-value-v1",
        "basis": basis.fingerprint,
        "sender": sender.observer,
        "receiver": receiver.observer,
        "from": receiver.history_digest(basis),
        "to_history": sender.history_digest(basis),
        "to_position": operational_digest(sender, basis),
        "steps": steps,
    })


def decode_relative_delta(
    receiver: AgentKnowledge, packet: bytes, basis: SharedKnowledgeBasis,
) -> AgentKnowledge:
    """One knowledge-aided SUCC, preserving A-origin causality without B measurement."""
    if type(packet) is not bytes or not 0 < len(packet) <= 1000000:
        raise RelativeDeltaError("A bounded finite digital packet is required")
    try:
        data = json.loads(packet.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise RelativeDeltaError("Malformed relative delta") from exc
    fields = {"kind", "basis", "sender", "receiver", "from", "to_history",
              "to_position", "steps"}
    if type(data) is not dict or set(data) != fields:
        raise RelativeDeltaError("Malformed relative delta shape")
    if (data["kind"] != "relative-path-value-v1"
            or data["basis"] != basis.fingerprint
            or data["from"] != receiver.history_digest(basis)
            or data["receiver"] != receiver.observer
            or type(data["sender"]) is not str
            or data["sender"] not in dict(basis.observers)
            or data["sender"] == receiver.observer
            or type(data["steps"]) is not list
            or len(data["steps"]) > 64):
        raise RelativeDeltaError("Stale, foreign or untrusted-format relay")
    state = receiver
    for step in data["steps"]:
        if type(step) is not dict or set(step) != {"path", "values"}:
            raise RelativeDeltaError("Invalid relative step")
        enabled = _enabled_new_probes(state, basis, data["sender"])
        if (type(step["path"]) is not list
                or type(step["values"]) is not list
                or len(step["values"]) != len(enabled)
                or len(enabled) == 0
                or len(step["path"]) != len(enabled)
                or any(type(x) is not int for x in step["path"])
                or step["path"] != list(range(len(enabled)))):
            raise RelativeDeltaError("Relative path cannot be realized from the last frame")
        outcomes = []
        for p, code in zip(enabled, step["values"]):
            possible = _choices(state, basis, p)
            if len(possible) == 1:
                if code is not None:
                    raise RelativeDeltaError("Known outcome may not invent new information")
                y = possible[0]
            else:
                if type(code) is not int or not 0 <= code < len(possible):
                    raise RelativeDeltaError("Invalid contingent outcome code")
                y = possible[code]
            outcomes.append((p, y))
        state = _strict_batch_step(
            state, ProbeBatch(data["sender"], tuple(outcomes)),
            basis, data["sender"])
    if (state.history_digest(basis) != data["to_history"]
            or operational_digest(state, basis) != data["to_position"]):
        raise RelativeDeltaError("Relative transport did not reach its declared position")
    return AgentKnowledge(receiver.observer, state.batches,
                          receiver.local_frames, receiver.informed_steps + 1)


def encode_position_delta(
    sender_before: AgentKnowledge, sender_after: AgentKnowledge,
    recipient: AgentKnowledge, basis: SharedKnowledgeBasis,
) -> bytes:
    """Transport from equal OPERATIONAL positions, not identical histories.

    The sender's history must have a lawful new suffix after its own previous
    position. The recipient may have *independently observed* its equal
    starting position, and so its old event-origin labels may differ.
    The common anchor is the full operational-state digest, not a shared
    source-event transcript hash.
    """
    if (sender_before.observer != sender_after.observer
            or sender_before.observer == recipient.observer
            or sender_after.batches[:len(sender_before.batches)]
                != sender_before.batches):
        raise RelativeDeltaError("Sender path must grow from its own local history")
    if operational_position(sender_before, basis) != operational_position(recipient, basis):
        raise RelativeDeltaError("Recipient has a different last known field position")
    appended = sender_after.batches[len(sender_before.batches):]
    if len(appended) > 64:
        raise RelativeDeltaError("Too many bounded relative path frames")
    trial = recipient
    steps = []
    for batch in appended:
        enabled = _enabled_new_probes(trial, basis, sender_before.observer)
        if (batch.origin != sender_before.observer
                or tuple(p for p, _ in batch.outcomes) != enabled):
            raise RelativeDeltaError("Sender's new relative path was not lawful")
        values = []
        for p, y in batch.outcomes:
            possible = _choices(trial, basis, p)
            if y not in possible:
                raise RelativeDeltaError("Source-incompatible observed value")
            values.append(None if len(possible) == 1 else possible.index(y))
        steps.append({"path": list(range(len(enabled))), "values": values})
        trial = _strict_batch_step(trial, batch, basis, sender_before.observer)
    if operational_position(trial, basis) != operational_position(sender_after, basis):
        raise RelativeDeltaError("Relative sender path changed the intended field placement")
    return _wire({
        "kind": "position-anchored-delta-v1",
        "basis": basis.fingerprint,
        "source": sender_before.observer,
        "receiver": recipient.observer,
        "anchor": operational_digest(recipient, basis),
        "result": operational_digest(sender_after, basis),
        "steps": steps,
    })


def decode_position_delta(
    recipient: AgentKnowledge, packet: bytes, basis: SharedKnowledgeBasis,
) -> AgentKnowledge:
    """One K-SUCC preserving recipient's independently sourced past.

    No source-state snapshot or identical past event-prefix is required.
    Old receiver events retain their actual origins; sender's new measured
    events are appended explicitly as sender-origin testimony.
    """
    if type(packet) is not bytes or not 0 < len(packet) <= 1000000:
        raise RelativeDeltaError("Bounded finite position-delta bytes required")
    try:
        data = json.loads(packet.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise RelativeDeltaError("Malformed positional delta message") from exc
    fields = {"kind", "basis", "source", "receiver", "anchor", "result", "steps"}
    if (type(data) is not dict or set(data) != fields
            or data["kind"] != "position-anchored-delta-v1"
            or data["basis"] != basis.fingerprint
            or data["anchor"] != operational_digest(recipient, basis)
            or data["receiver"] != recipient.observer
            or type(data["source"]) is not str
            or data["source"] not in dict(basis.observers)
            or data["source"] == recipient.observer
            or type(data["steps"]) is not list
            or len(data["steps"]) > 64):
        raise RelativeDeltaError("Foreign basis, stale position or malformed sender")
    current = recipient
    for step in data["steps"]:
        enabled = _enabled_new_probes(current, basis, data["source"])
        if (type(step) is not dict or set(step) != {"path", "values"}
                or type(step["path"]) is not list
                or type(step["values"]) is not list
                or len(enabled) == 0
                or len(step["values"]) != len(enabled)
                or any(type(n) is not int for n in step["path"])
                or step["path"] != list(range(len(enabled)))):
            raise RelativeDeltaError("Relative path cannot be executed from receiver placement")
        outcomes = []
        for p, code in zip(enabled, step["values"]):
            possible = _choices(current, basis, p)
            if len(possible) == 1:
                if code is not None:
                    raise RelativeDeltaError("Redundant outcome token may not fake novelty")
                value = possible[0]
            else:
                if type(code) is not int or not 0 <= code < len(possible):
                    raise RelativeDeltaError("Invalid contingent source result index")
                value = possible[code]
            outcomes.append((p, value))
        current = _strict_batch_step(
            current, ProbeBatch(data["source"], tuple(outcomes)), basis, data["source"])
    if operational_digest(current, basis) != data["result"]:
        raise RelativeDeltaError("Position-anchored transport did not reach declared endpoint")
    return AgentKnowledge(recipient.observer, current.batches,
                          recipient.local_frames, recipient.informed_steps + 1)


@dataclass(frozen=True)
class ProbeOptionResult:
    name: str
    is_an_epistemic_option: bool
    possible_values: tuple[str, ...]
    inferable_without_measuring: bool
    inferred_value: str | None
    source_consistent_certificate: bool


def probe_option_result(
    observer: AgentKnowledge, basis: SharedKnowledgeBasis, probe: str,
) -> ProbeOptionResult:
    """A probe's *optionhood* alone does not reveal an unknown outcome.

    If every surviving source returns the same value, the mathematical
    observation is deductively inferable; otherwise its possible outputs
    remain distinct, even if the probe is a known executable option.
    """
    if probe not in basis.world.probes:
        raise RelativeDeltaError("The proposed probe is not in this basis")
    model = observer.model(basis)
    possible = tuple(sorted({basis.world.outcome(x, probe)
                             for x in model.compatible}))
    known = len(possible) == 1
    return ProbeOptionResult(
        probe, probe in model.epistemically_accessible, possible,
        known, possible[0] if known else None, known)


@dataclass(frozen=True)
class ProbeValueProof:
    """A contextual proof of a probe result, NOT an actual observation."""
    basis: str
    context_position: str
    probe: str
    value: str
    witness_sources: tuple[str, ...]
    proof_method: str = "finite exhaustive agreement on compatible sources"


def prove_probe_value(
    observer: AgentKnowledge, basis: SharedKnowledgeBasis, probe: str,
) -> ProbeValueProof:
    """Build an exact proof only when the probe is constant on K(observer).

    The mathematical existence of a probe function is insufficient.
    This proof's existence is informative because its *type includes the
    claimed value* and its construction checks every compatible source.
    """
    report = probe_option_result(observer, basis, probe)
    if not report.inferable_without_measuring:
        raise RelativeDeltaError(
            "Probe may be available, but no unique result follows from this model")
    return ProbeValueProof(basis.fingerprint, operational_digest(observer, basis),
                           probe, report.inferred_value,
                           observer.model(basis).compatible)


def verify_probe_value(
    observer: AgentKnowledge, basis: SharedKnowledgeBasis, certificate: ProbeValueProof,
) -> bool:
    """Recheck a proof-carrying value in the recipient's exact current context.

    A valid certificate changes no causal measurement history: the result
    was *inferred*, not newly observed with an instrument.
    """
    if not isinstance(certificate, ProbeValueProof):
        raise RelativeDeltaError("A typed value-proof certificate is required")
    if (certificate.basis != basis.fingerprint
            or certificate.context_position != operational_digest(observer, basis)
            or certificate.probe not in basis.world.probes
            or certificate.witness_sources != observer.model(basis).compatible):
        raise RelativeDeltaError("Probe proof is stale or source-context incompatible")
    outputs = probe_option_result(observer, basis, certificate.probe)
    if (not outputs.inferable_without_measuring
            or outputs.inferred_value != certificate.value):
        raise RelativeDeltaError("Probe proof does not establish the claimed value")
    return True


@dataclass(frozen=True)
class DerivedBooleanConcept:
    """A source-independent verified definition, not a physical discovery."""
    new_probe: str
    operator: str
    operands: tuple[str, ...]

    def __post_init__(self):
        if (type(self.new_probe) is not str or not self.new_probe
                or ":" in self.new_probe
                or type(self.operands) is not tuple):
            raise RelativeDeltaError("Malformed derived probe definition")
        if self.operator not in ("xor", "and", "not"):
            raise RelativeDeltaError("Unsupported proof-operation signature")
        expected = 1 if self.operator == "not" else 2
        if len(self.operands) != expected or any(
            type(p) is not str or not p for p in self.operands
        ):
            raise RelativeDeltaError("Wrong operand arity or probe symbol")


def extend_shared_basis(
    basis: SharedKnowledgeBasis, recipe: DerivedBooleanConcept,
) -> SharedKnowledgeBasis:
    """A proof-checked definitional language extension on the same sources.

    A new *epistemic* query is defined as a truth-functional combination
    of existing probe responses. Crucially no physical instrument is added,
    and no previously unavailable contingent source response is smuggled in.
    """
    if not isinstance(recipe, DerivedBooleanConcept):
        raise RelativeDeltaError("Require a typed verified definitional extension")
    old = basis.world
    if recipe.new_probe in old.probes or any(p not in old.probes
                                            for p in recipe.operands):
        raise RelativeDeltaError("Unknown operand or duplicate proposed probe")
    cols = [old.probes.index(p) for p in recipe.operands]
    out_rows = []
    for row in old.outcomes:
        values = tuple(row[i] for i in cols)
        if any(v not in ("0", "1") for v in values):
            raise RelativeDeltaError("Only total binary probes support this definition")
        if recipe.operator == "xor":
            result = str(int(values[0]) ^ int(values[1]))
        elif recipe.operator == "and":
            result = str(int(values[0]) & int(values[1]))
        else:
            result = str(1-int(values[0]))
        out_rows.append(row + (result,))
    new_world = FiniteProbeWorld(old.sources, old.probes + (recipe.new_probe,),
                                 tuple(out_rows))
    rule = HornRule(tuple(f"can:{x}" for x in recipe.operands),
                    f"can:{recipe.new_probe}")
    return SharedKnowledgeBasis(
        new_world, basis.axioms, basis.rules + (rule,), basis.observers)


def encode_concept_upgrade(basis: SharedKnowledgeBasis,
                           recipe: DerivedBooleanConcept) -> bytes:
    new_basis = extend_shared_basis(basis, recipe)
    return _wire({
        "kind": "verified-concept-v1",
        "base": basis.fingerprint, "result": new_basis.fingerprint,
        "new": recipe.new_probe, "operator": recipe.operator,
        "operands": list(recipe.operands),
    })


def receive_concept_upgrade(basis: SharedKnowledgeBasis, packet: bytes
                            ) -> SharedKnowledgeBasis:
    if type(packet) is not bytes or not 0 < len(packet) <= 65536:
        raise RelativeDeltaError("Finite concept-delta packet required")
    try:
        data = json.loads(packet.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise RelativeDeltaError("Invalid concept packet") from exc
    if (type(data) is not dict
            or set(data) != {"kind", "base", "result", "new", "operator", "operands"}
            or data["kind"] != "verified-concept-v1"
            or data["base"] != basis.fingerprint
            or type(data["operands"]) is not list):
        raise RelativeDeltaError("Unverifiable or stale basis extension")
    try:
        recipe = DerivedBooleanConcept(
            data["new"], data["operator"], tuple(data["operands"]))
        new_basis = extend_shared_basis(basis, recipe)
    except (TypeError, ValueError) as exc:
        if isinstance(exc, RelativeDeltaError):
            raise
        raise RelativeDeltaError("Bad conceptual probe definition") from exc
    if new_basis.fingerprint != data["result"]:
        raise RelativeDeltaError("Concept recipe fails shared interpretation")
    return new_basis


def frozen_base_minimum_worst_case_bits(prefix_length: int) -> int:
    """Exact fixed-B0 worst-case bound for all 2^n arbitrary bit prefixes.

    There are 2^n possible length-n prefixes and only 2^n-1 binary
    strings of length at most n-1. Some source therefore needs >= n bits.
    This does not rule out short descriptions of special infinite objects.
    """
    if type(prefix_length) is not int or not 0 <= prefix_length <= 256:
        raise RelativeDeltaError("Bounded nonnegative prefix required")
    return prefix_length


def relative_delta_demo() -> dict:
    """Two local steps -> one direction-coded step, then frozen basis rejection."""
    probes = ("long_observational_probe_alpha",
              "long_observational_probe_beta", "long_observational_probe_gamma")
    world = FiniteProbeWorld(
        ("A", "B"), probes,
        (("same", "same", "A"), ("same", "same", "B")))
    rules = (
        HornRule((f"obs:{probes[0]}:same",),f"can:{probes[1]}"),
        HornRule((f"obs:{probes[1]}:same",),f"can:{probes[2]}"),
    )
    basis = SharedKnowledgeBasis(world,(f"can:{probes[0]}",),rules,
                                 (("Alice",probes),("Bob",probes)))
    a = AgentKnowledge("Alice").advance(basis,"B",3)
    b = AgentKnowledge("Bob")
    packet = encode_relative_delta(a,b,basis)
    updated = decode_relative_delta(b,packet,basis)
    future = certify_finite_continuation(a,updated,basis)
    assert future.equivalent and updated.local_frames == 0
    data = json.loads(packet.decode())
    # The packet has only relative path indices and value-choice codes.
    assert data["steps"] == [
        {"path":[0], "values":[None]},
        {"path":[0], "values":[None]},
        {"path":[0], "values":[1]},
    ]
    return {
        "status": "EXACT_RELATIVE_PATH_VALUE_RELAY",
        "physical_discovery_frames": a.local_frames,
        "recipient_knowledge_steps": updated.informed_steps,
        "receiver_physical_frames": updated.local_frames,
        "steps": data["steps"],
        "same_knowledge_empirical_access_and_reasoner": future.equivalent,
        "continuations_checked": future.local_transitions_checked,
        "shared_basis_hash": basis.fingerprint,
        "no_state_snapshot_or_absolute_probe_names_in_steps": True,
        "source_authentication_claimed": False,
        "physical_speedup_claimed": False,
        "infinite_communication_claimed": False,
    }



def position_anchored_demo() -> dict:
    """Independent histories, same operational position, one relative SUCC."""
    world=FiniteProbeWorld(
        ("A","B"),("p0","p1","p2"),
        (("same","same","A"),("same","same","B")))
    rules=(
        HornRule(("obs:p0:same",),"can:p1"),
        HornRule(("obs:p1:same",),"can:p2"),
    )
    basis=SharedKnowledgeBasis(
        world,("can:p0",),rules,
        (("Alice",world.probes),("Bob",world.probes)))
    alice_before=AgentKnowledge("Alice").local_succ(basis,"B")
    bob_before=AgentKnowledge("Bob").local_succ(basis,"B")
    assert (alice_before.batches != bob_before.batches
            and operational_position(alice_before,basis)
                == operational_position(bob_before,basis))
    alice_after=alice_before.advance(basis,"B",2)
    packet=encode_position_delta(alice_before,alice_after,bob_before,basis)
    bob_after=decode_position_delta(bob_before,packet,basis)
    equality=certify_finite_continuation(alice_after,bob_after,basis)
    assert equality.equivalent
    assert (bob_after.batches[0].origin=="Bob"
            and tuple(batch.origin for batch in bob_after.batches[1:])
                == ("Alice","Alice")
            and bob_after.informed_steps==1
            and bob_after.local_frames==1)
    return {
        "status":"EXACT_POSITION_ANCHORED_KNOWLEDGE_SUCC",
        "independent_prior_histories":True,
        "same_prior_knowledge_access_and_reasoning":True,
        "relative_informed_steps":bob_after.informed_steps,
        "additional_sender_local_frames":2,
        "old_receiver_event_origin_preserved":"Bob",
        "new_sender_event_origins":["Alice","Alice"],
        "operational_continuation_verified":equality.equivalent,
        "continuations_checked":equality.local_transitions_checked,
        "cryptographic_measurement_authentication_claimed":False,
        "physical_speedup_claimed":False,
    }


def proof_shape_and_basis_demo() -> dict:
    world=FiniteProbeWorld(
        ("00","01","10","11"),("left","right"),
        (("0","0"),("0","1"),("1","0"),("1","1")))
    base=SharedKnowledgeBasis(
        world,("can:left","can:right"),(),
        (("Alice",world.probes),("Bob",world.probes)))
    recipe=DerivedBooleanConcept("parity","xor",("left","right"))
    packet=encode_concept_upgrade(base,recipe)
    upgraded=receive_concept_upgrade(base,packet)
    observer=AgentKnowledge("Alice")
    before=probe_option_result(observer,upgraded,"parity")
    assert before.is_an_epistemic_option and not before.inferable_without_measuring
    measured=observer.local_succ(upgraded,"10")
    after=probe_option_result(measured,upgraded,"parity")
    proof=prove_probe_value(measured,upgraded,"parity")
    assert (after.inferable_without_measuring
            and after.inferred_value=="1"
            and verify_probe_value(measured,upgraded,proof))
    return {
        "status":"VERIFIED_CONSERVATIVE_PROOF_PROBE_UPGRADE",
        "old_basis":base.fingerprint,
        "new_basis":upgraded.fingerprint,
        "new_epistemic_probe":"parity",
        "new_physical_instrument_created":False,
        "option_alone_determined_result":False,
        "proof_after_primitive_evidence_determined_result":True,
        "proved_value":proof.value,
        "parity_physically_observed":False,
        "frozen_base_minimum_worst_case_bits_for_eight_arbitrary_bits":
            frozen_base_minimum_worst_case_bits(8),
        "universal_finite_omega_message_claimed":False,
    }
