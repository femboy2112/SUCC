"""Finite knowledge-aided SUCC: lawful two-observer relay and epistemic ladders.

Separate local physical measurements, imported evidence, snapshot placement
and stronger causal/future synchronization. Source outcomes are toy-model
declared; provenance checks are NOT actual-world authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json

from .absorbing_frames import AbsorbingProtocol, AbsorbingFrame, HornRule, AbsorptionError
from .observer_traps import FiniteProbeWorld


class KnowledgeLadderError(ValueError):
    pass


def _wire(o) -> bytes:
    return json.dumps(o, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _hash(o) -> str:
    return sha256(_wire(o)).hexdigest()


@dataclass(frozen=True)
class SharedKnowledgeBasis:
    world: FiniteProbeWorld
    axioms: tuple[str, ...]
    rules: tuple[HornRule, ...]
    observers: tuple[tuple[str, tuple[str, ...]], ...]

    def __post_init__(self):
        if type(self.observers) is not tuple or len(self.observers) < 2:
            raise KnowledgeLadderError("Two or more registered observers are required")
        seen = set()
        for row in self.observers:
            if type(row) is not tuple or len(row) != 2:
                raise KnowledgeLadderError("Invalid observer and physical probe list")
            name, probes = row
            if (type(name) is not str or not name or name in seen
                    or type(probes) is not tuple or len(set(probes)) != len(probes)
                    or not set(probes).issubset(self.world.probes)):
                raise KnowledgeLadderError("Invalid observer identity or feasible probes")
            seen.add(name)
        _ = self.semantic_protocol
        for name, _ in self.observers:
            _ = self.physical_protocol(name)

    @property
    def semantic_protocol(self):
        # Remote source observations can be *understood* without the
        # recipient owning the source observer's physical instruments.
        return AbsorbingProtocol(self.world, self.axioms, self.rules, self.world.probes)

    def physical_protocol(self, name):
        if name not in dict(self.observers):
            raise KnowledgeLadderError("Unregistered observer")
        return AbsorbingProtocol(
            self.world, self.axioms, self.rules, dict(self.observers)[name])

    @property
    def fingerprint(self):
        return _hash({
            "sources": self.world.sources,
            "probes": self.world.probes,
            "outcomes": self.world.outcomes,
            "axioms": self.axioms,
            "rules": [(rule.premises, rule.conclusion) for rule in self.rules],
            "observers": self.observers,
        })


@dataclass(frozen=True)
class ProbeBatch:
    origin: str
    outcomes: tuple[tuple[str, str], ...]

    def __post_init__(self):
        if type(self.origin) is not str or not self.origin:
            raise KnowledgeLadderError("A genuine provenance label is required")
        if type(self.outcomes) is not tuple or len(self.outcomes) == 0:
            raise KnowledgeLadderError("Every local successor needs a nonempty batch")
        if any(type(pair) is not tuple or len(pair) != 2 or
               any(type(v) is not str or not v for v in pair)
               for pair in self.outcomes):
            raise KnowledgeLadderError("Malformed source observation")
        if len(set(p for p, _ in self.outcomes)) != len(self.outcomes):
            raise KnowledgeLadderError("Duplicate probe in one batch")

    def wire(self):
        return {"origin": self.origin, "outcomes": [list(x) for x in self.outcomes]}


@dataclass(frozen=True)
class AgentKnowledge:
    observer: str
    batches: tuple[ProbeBatch, ...] = ()
    local_frames: int = 0
    informed_steps: int = 0

    def observations(self):
        return tuple(pair for batch in self.batches for pair in batch.outcomes)

    def model(self, basis: SharedKnowledgeBasis):
        if self.observer not in dict(basis.observers):
            raise KnowledgeLadderError("Agent absent from shared basis")
        try:
            return AbsorbingFrame(self.observations()).absorb(basis.semantic_protocol)
        except AbsorptionError as exc:
            raise KnowledgeLadderError("Observation history incompatible with shared basis") from exc

    def placement(self, basis: SharedKnowledgeBasis):
        """Snapshot placement: does NOT prove identical future transitions."""
        model = self.model(basis)
        derived = tuple(atom for atom in model.closure.atoms
                        if not atom.startswith(("obs:", "predict:")))
        return (model.compatible, model.predicted, derived,
                model.epistemically_accessible)

    def placement_digest(self, basis: SharedKnowledgeBasis):
        return _hash(self.placement(basis))

    def history_digest(self, basis: SharedKnowledgeBasis):
        return _hash({"basis": basis.fingerprint,
                      "batches": [batch.wire() for batch in self.batches]})

    def local_succ(self, basis: SharedKnowledgeBasis, actual: str):
        """Observe ALL new currently accessible and physically feasible probes."""
        model = self.model(basis)
        if actual not in model.compatible:
            raise KnowledgeLadderError("Actual source contradicts trusted history")
        existing = {p for p, _ in self.observations()}
        physical = set(dict(basis.observers)[self.observer])
        new = tuple(p for p in model.epistemically_accessible
                    if p in physical and p not in existing)
        if not new:
            return self
        batch = ProbeBatch(self.observer, tuple(
            (p, basis.world.outcome(actual, p)) for p in new))
        result = AgentKnowledge(self.observer, self.batches + (batch,),
                                self.local_frames + 1, self.informed_steps)
        result.model(basis)
        return result

    def advance(self, basis: SharedKnowledgeBasis, actual: str, n: int):
        if type(n) is not int or not 0 <= n <= len(basis.world.probes):
            raise KnowledgeLadderError("Only a bounded finite local path is executable")
        current = self
        for _ in range(n):
            current = current.local_succ(basis, actual)
        return current


def _strict_batch_step(before: AgentKnowledge, batch: ProbeBatch,
                       basis: SharedKnowledgeBasis, sender: str):
    """Check the whole next SOURCE-ACCESSIBLE local batch from existing data."""
    if batch.origin != sender:
        raise KnowledgeLadderError("Unattested third-party observations cannot be relayed")
    observed = {p for p, _ in before.observations()}
    model = before.model(basis)
    physical = set(dict(basis.observers)[sender])
    expected = tuple(p for p in model.epistemically_accessible
                     if p in physical and p not in observed)
    if tuple(p for p, _ in batch.outcomes) != expected or not expected:
        raise KnowledgeLadderError("Sender's claimed observation path was not causally enabled")
    result = AgentKnowledge(before.observer, before.batches + (batch,),
                            before.local_frames, before.informed_steps)
    result.model(basis)  # possible-source test, not authenticating physical reality
    return result


def _parse_wire(packet: bytes, kind: str):
    if type(packet) is not bytes or not 0 < len(packet) <= 1000000:
        raise KnowledgeLadderError("A bounded finite digital packet is required")
    try:
        o = json.loads(packet.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise KnowledgeLadderError("Invalid finite knowledge message") from exc
    fields = {"kind", "basis", "sender", "receiver", "start", "end", "events"}
    if type(o) is not dict or set(o) != fields or o["kind"] != kind:
        raise KnowledgeLadderError("Unexpected knowledge message schema")
    if any(type(o[k]) is not str or not o[k] for k in fields-{"kind", "events"}):
        raise KnowledgeLadderError("Malformed knowledge context")
    if type(o["events"]) is not list or len(o["events"]) > 64:
        raise KnowledgeLadderError("Missing bounded message observations")
    return o


def _parse_batch(origin: str, raw):
    if type(raw) is not list or not raw or any(
        type(v) is not list or len(v) != 2 for v in raw
    ):
        raise KnowledgeLadderError("Invalid observation frame batch")
    return ProbeBatch(origin, tuple(tuple(pair) for pair in raw))


def encode_strict_relay(sender: AgentKnowledge, receiver: AgentKnowledge,
                        basis: SharedKnowledgeBasis):
    """Sender's k lawful local frames, delivered as one receiver K-SUCC."""
    if sender.observer == receiver.observer:
        raise KnowledgeLadderError("A relay connects distinct observers")
    if receiver.batches != sender.batches[:len(receiver.batches)]:
        raise KnowledgeLadderError("Strong relay requires a common causal prefix")
    extra = sender.batches[len(receiver.batches):]
    replay = receiver
    for batch in extra:
        replay = _strict_batch_step(replay, batch, basis, sender.observer)
    if replay.placement(basis) != sender.placement(basis):
        raise KnowledgeLadderError("Source/semantic reconstructed model disagrees")
    return _wire({
        "kind": "strict-ladder-v1",
        "basis": basis.fingerprint,
        "sender": sender.observer,
        "receiver": receiver.observer,
        "start": receiver.history_digest(basis),
        "end": sender.placement_digest(basis),
        "events": [[list(pair) for pair in batch.outcomes] for batch in extra],
    })


def decode_strict_relay(receiver: AgentKnowledge, packet: bytes,
                        basis: SharedKnowledgeBasis):
    """One informed successor; the receiver does NOT run sender's probes."""
    o = _parse_wire(packet, "strict-ladder-v1")
    if (o["basis"] != basis.fingerprint or o["receiver"] != receiver.observer
            or o["start"] != receiver.history_digest(basis)
            or o["sender"] not in dict(basis.observers)
            or o["sender"] == receiver.observer):
        raise KnowledgeLadderError("Stale, inconsistent, or foreign-basis relay")
    state = receiver
    for batch_raw in o["events"]:
        batch = _parse_batch(o["sender"], batch_raw)
        state = _strict_batch_step(state, batch, basis, o["sender"])
    if state.placement_digest(basis) != o["end"]:
        raise KnowledgeLadderError("Relayed field placement is not reproduced")
    return AgentKnowledge(receiver.observer, state.batches,
                          receiver.local_frames, receiver.informed_steps + 1)


@dataclass(frozen=True)
class SnapshotWitness:
    facts: tuple[tuple[str, str], ...]
    full_fact_count: int
    minimal_fact_count: int
    causal_history_certified: bool = False
    future_equivalence_certified: bool = False


def minimal_snapshot_delta(sender: AgentKnowledge, receiver: AgentKnowledge,
                           basis: SharedKnowledgeBasis):
    """Exact smallest # facts that reproduce current epistemic placement.

    Never interprets a shortened observation list as proof of A's path or
    of B's ability to make all the same future measurements.
    """
    if sender.observer == receiver.observer:
        raise KnowledgeLadderError("A snapshot relay requires distinct observers")
    if receiver.batches != sender.batches[:len(receiver.batches)]:
        raise KnowledgeLadderError("Snapshot comparison requires common prefix")
    if any(batch.origin != sender.observer
           for batch in sender.batches[len(receiver.batches):]):
        raise KnowledgeLadderError("Snapshot cannot silently launder third-party observations")
    facts = tuple(pair for batch in sender.batches[len(receiver.batches):]
                  for pair in batch.outcomes)
    if len(facts) > 16:
        raise KnowledgeLadderError("Exhaustive finite compression budget exceeded")
    desired = sender.placement(basis)
    for n in range(len(facts) + 1):
        for subset in combinations(facts, n):
            batches = receiver.batches + (
                (ProbeBatch(sender.observer, subset),) if subset else ())
            alternative = AgentKnowledge(receiver.observer, batches)
            if alternative.placement(basis) == desired:
                return SnapshotWitness(subset, len(facts), n)
    raise ArithmeticError("Full facts should always suffice for snapshot placement")


def encode_snapshot_relay(sender: AgentKnowledge, receiver: AgentKnowledge,
                          basis: SharedKnowledgeBasis):
    witness = minimal_snapshot_delta(sender, receiver, basis)
    return _wire({
        "kind": "snapshot-only-v1",
        "basis": basis.fingerprint,
        "sender": sender.observer,
        "receiver": receiver.observer,
        "start": receiver.history_digest(basis),
        "end": sender.placement_digest(basis),
        "events": [list(pair) for pair in witness.facts],
    })


def decode_snapshot_relay(receiver: AgentKnowledge, packet: bytes,
                          basis: SharedKnowledgeBasis):
    """Assume authenticated observation facts; do NOT claim a lawful path."""
    o = _parse_wire(packet, "snapshot-only-v1")
    if (o["basis"] != basis.fingerprint or o["receiver"] != receiver.observer
            or o["start"] != receiver.history_digest(basis)
            or o["sender"] not in dict(basis.observers)
            or o["sender"] == receiver.observer):
        raise KnowledgeLadderError("Unverifiable or stale snapshot basis")
    if any(type(pair) is not list or len(pair) != 2 for pair in o["events"]):
        raise KnowledgeLadderError("Malformed snapshot facts")
    facts = tuple(tuple(pair) for pair in o["events"])
    batches = receiver.batches + (
        (ProbeBatch(o["sender"], facts),) if facts else ())
    result = AgentKnowledge(receiver.observer, batches, receiver.local_frames,
                            receiver.informed_steps + 1)
    if result.placement_digest(basis) != o["end"]:
        raise KnowledgeLadderError("Snapshot facts fail to reproduce placement")
    return result


def knowledge_ladder_demo():
    """Alternating 2 discovery frames : 1 informed catch-up, for 3 rungs."""
    probes = tuple(f"p{i}" for i in range(6))
    outcomes = (("same",)*5+("A",), ("same",)*5+("B",))
    world = FiniteProbeWorld(("A", "B"), probes, outcomes)
    rules = tuple(HornRule((f"obs:p{i}:same",), f"can:p{i+1}")
                  for i in range(5))
    basis = SharedKnowledgeBasis(world, ("can:p0",), rules,
                                 (("Alice", probes), ("Bob", probes)))
    a, b = AgentKnowledge("Alice"), AgentKnowledge("Bob")
    receipts = []
    for speaker in ("Alice", "Bob", "Alice"):
        original = a if speaker == "Alice" else b
        recipient = b if speaker == "Alice" else a
        advanced = original.advance(basis, "B", 2)
        pkt = encode_strict_relay(advanced, recipient, basis)
        caught = decode_strict_relay(recipient, pkt, basis)
        assert caught.placement(basis) == advanced.placement(basis)
        assert caught.batches == advanced.batches
        assert caught.local_frames == recipient.local_frames
        assert caught.informed_steps == recipient.informed_steps + 1
        receipts.append({
            "discoverer": speaker,
            "local_discovery_steps": advanced.local_frames-original.local_frames,
            "receiver_informed_steps": 1,
            "packet_bytes": len(pkt),
            "surviving_sources": list(caught.model(basis).compatible),
        })
        if speaker == "Alice":
            a, b = advanced, caught
        else:
            b, a = advanced, caught
    assert a.placement(basis) == b.placement(basis)
    return {
        "status": "EXACT_FINITE_INTEROBSERVER_KNOWLEDGE_LADDER",
        "rungs": receipts,
        "discovery_succ_steps": sum(x["local_discovery_steps"] for x in receipts),
        "receiver_knowledge_aided_steps": len(receipts),
        "end_source_class": list(a.model(basis).compatible),
        "full_shared_semantics_and_causal_records_match": True,
        "sender_outcomes_cryptographically_authenticated": False,
        "physical_time_speedup_proved": False,
        "infinite_ladder_executed": False,
        "RH_claimed": False,
    }


def complementary_observers_demo():
    """Distributed XOR target: individually unknown, jointly exact.

    Alice can read only the left bit; Bob can read only the right bit.
    No observer ever magically acquires the other's physical instrument.
    The truth is used only by each agent's local probe simulator.
    """
    sources = ("00", "01", "10", "11")
    world = FiniteProbeWorld(
        sources, ("left", "right"),
        tuple((source[0], source[1]) for source in sources),
    )
    basis = SharedKnowledgeBasis(
        world, ("can:left", "can:right"), (),
        (("Alice", ("left",)), ("Bob", ("right",))),
    )
    target = {source: str(int(source[0]) ^ int(source[1])) for source in sources}
    a = AgentKnowledge("Alice")
    b = AgentKnowledge("Bob")
    actual = "10"
    a_left = a.local_succ(basis, actual)
    b_right = b.local_succ(basis, actual)
    alice_only = a_left.model(basis).compatible
    bob_only = b_right.model(basis).compatible
    assert set(target[x] for x in alice_only) == {"0", "1"}
    assert set(target[x] for x in bob_only) == {"0", "1"}
    assert len(alice_only) == len(bob_only) == 2
    # Sequential exchange with exact common prefix.
    b_after_left = decode_strict_relay(
        b, encode_strict_relay(a_left, b, basis), basis)
    b_both = b_after_left.local_succ(basis, actual)
    a_both = decode_strict_relay(
        a_left, encode_strict_relay(b_both, a_left, basis), basis)
    assert a_both.placement(basis) == b_both.placement(basis)
    assert a_both.model(basis).compatible == (actual,)
    assert b_both.model(basis).compatible == (actual,)
    assert a_both.local_frames == b_both.local_frames == 1
    return {
        "status": "EXACT_DISTRIBUTED_EPISTEMIC_COMPLEMENTARITY",
        "alice_only": list(alice_only),
        "bob_only": list(bob_only),
        "alice_only_xor_identified": False,
        "bob_only_xor_identified": False,
        "shared_source": list(a_both.model(basis).compatible),
        "shared_xor": target[actual],
        "physical_probes_each": {"Alice": ["left"], "Bob": ["right"]},
        "replayed_remote_knowledge_not_local_measurement": True,
        "full_continuation_equivalence_of_physical_devices_claimed": False,
        "RH_claimed": False,
    }
