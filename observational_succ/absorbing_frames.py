"""Finite absorbing-model / Hard-SUCC research laboratory.

An absorbing model is not a favored candidate. It is the full compatible
source class, the strongest agreed probe predictions in that source class,
and the LEAST closure of actual outcomes under declared monotone Horn rules.

The research model separates:
  * epistemic access (derived 'can:<probe>' atoms);
  * physical feasibility (an explicitly declared feasible probe set);
  * actual measurement outcomes (immutable, never inferred from preference);
  * theoretically predicted outcomes (tagged, never forged as measurements);
  * eventual finite transmission (shared protocol + finite record).

The default hard_succ exhausts the finite local universe with instantaneous
assimilation, not physical infinity or transfinite proofs. Neither replay
nor decoding independently authenticates real-world measurement outcomes.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Mapping

from .observer_traps import FiniteProbeWorld


class AbsorptionError(ValueError):
    """Invalid model, causal data, ability, channel, or completion claim."""


def _symbols(items, *, title: str, allow_empty: bool = True) -> tuple[str, ...]:
    if type(items) is not tuple or len(items) > 128 or (not allow_empty and not items):
        raise AbsorptionError(f"{title}: expected a bounded immutable tuple")
    if any(type(v) is not str or not v or len(v) > 128 for v in items):
        raise AbsorptionError(f"{title}: expected nonempty bounded symbols")
    if len(set(items)) != len(items):
        raise AbsorptionError(f"{title}: duplicate symbol")
    return items


@dataclass(frozen=True)
class HornRule:
    """Finite-premise, positive, monotone semantic inference rule."""

    premises: tuple[str, ...]
    conclusion: str

    def __post_init__(self):
        _symbols(self.premises, title="Rule premises")
        if type(self.conclusion) is not str or not self.conclusion or len(self.conclusion) > 128:
            raise AbsorptionError("Rule conclusion must be a bounded symbol")
        if self.conclusion.startswith("obs:") or self.conclusion.startswith("predict:"):
            raise AbsorptionError("Inference cannot fabricate observed or predicted outcomes")


@dataclass(frozen=True)
class ClosureCertificate:
    """Exact finite fixed point of a declared positive rule system."""

    atoms: tuple[str, ...]
    added_rounds: tuple[tuple[str, ...], ...]
    stationary: bool

    def knows(self, proposition: str) -> bool:
        return proposition in self.atoms


def least_horn_closure(seed: tuple[str, ...], rules: tuple[HornRule, ...]) -> ClosureCertificate:
    """Monotone least closure via all simultaneously enabled finite Horn rules.

    All atoms derive from finite initial facts and finitely many rule conclusions.
    Every round adds at least one fresh atom, so the process terminates.
    """
    _symbols(seed, title="Initial facts")
    if type(rules) is not tuple or len(rules) > 128 or any(not isinstance(r, HornRule) for r in rules):
        raise AbsorptionError("Expected a bounded tuple of Horn rules")
    facts = set(seed)
    rounds: list[tuple[str, ...]] = []
    for _ in range(len(seed) + len(rules) + 2):
        found = tuple(sorted({r.conclusion for r in rules
                             if all(p in facts for p in r.premises)
                             and r.conclusion not in facts}))
        if not found:
            return ClosureCertificate(tuple(sorted(facts)), tuple(rounds), True)
        rounds.append(found)
        facts.update(found)
    raise ArithmeticError("Finite monotone closure exceeded its proved atom bound")


@dataclass(frozen=True)
class AbsorbingProtocol:
    """Publicly shared language, probe semantics and finite closure rules."""

    world: FiniteProbeWorld
    seeds: tuple[str, ...]
    rules: tuple[HornRule, ...]
    feasible: tuple[str, ...]

    def __post_init__(self):
        if not isinstance(self.world, FiniteProbeWorld):
            raise AbsorptionError("A declared finite source/probe world is required")
        _symbols(self.seeds, title="Initial symbols")
        _symbols(self.feasible, title="Physically executable probes")
        if any(p not in self.world.probes for p in self.feasible):
            raise AbsorptionError("Physical feasibility must refer to global probes")
        if any(v.startswith("obs:") or v.startswith("predict:") for v in self.seeds):
            raise AbsorptionError("Initial axioms may not impersonate source observations")
        least_horn_closure(self.seeds, self.rules)
        for r in self.rules:
            for atom in (r.conclusion, *r.premises):
                if atom.startswith("can:") and atom[4:] not in self.world.probes:
                    raise AbsorptionError("Rule may not unlock an undeclared probe")
                if atom.startswith("obs:") or atom.startswith("predict:"):
                    if not self._valid_outcome_atom(atom):
                        raise AbsorptionError("Rule refers to an impossible outcome token")

    def _valid_outcome_atom(self, atom: str) -> bool:
        # Encoded tokens are checked against the entire public response table.
        return any(atom == f"{prefix}{p}:{self.world.outcome(x, p)}"
                   for prefix in ("obs:", "predict:")
                   for x in self.world.sources for p in self.world.probes)


@dataclass(frozen=True)
class AbsorbedModel:
    compatible: tuple[str, ...]
    observed: tuple[tuple[str, str], ...]
    predicted: tuple[tuple[str, str], ...]
    epistemically_accessible: tuple[str, ...]
    physically_accessible: tuple[str, ...]
    physically_blocked: tuple[str, ...]
    closure: ClosureCertificate

    @property
    def identified(self) -> bool:
        return len(self.compatible) == 1


@dataclass(frozen=True)
class AbsorbingFrame:
    """Never discard actualized events; blocked attempts are separate events."""

    observations: tuple[tuple[str, str], ...] = ()
    blocked_attempts: tuple[str, ...] = ()
    frames: int = 0

    def __post_init__(self):
        if type(self.observations) is not tuple or type(self.blocked_attempts) is not tuple:
            raise AbsorptionError("Causal history must be immutable tuples")
        if type(self.frames) is not int or self.frames < 0:
            raise AbsorptionError("Frame count must be a nonnegative exact integer")
        names = []
        for record in self.observations:
            if type(record) is not tuple or len(record) != 2:
                raise AbsorptionError("Observation event must be a (probe, outcome) pair")
            p, y = record
            if type(p) is not str or type(y) is not str or not p or not y:
                raise AbsorptionError("Invalid recorded probe/outcome")
            names.append(p)
        if len(set(names)) != len(names):
            raise AbsorptionError("A probe cannot be observed twice in this finite toy model")
        _symbols(self.blocked_attempts, title="Blocked probe attempts")
        if set(names).intersection(self.blocked_attempts):
            raise AbsorptionError("Probe cannot be recorded both blocked and measured")

    def absorb(self, protocol: AbsorbingProtocol) -> AbsorbedModel:
        if not isinstance(protocol, AbsorbingProtocol):
            raise AbsorptionError("Missing shared probe/closure protocol")
        world = protocol.world
        if any(p not in world.probes for p, _ in self.observations):
            raise AbsorptionError("Transcript mentions an undeclared probe")
        if any(p not in world.probes for p in self.blocked_attempts):
            raise AbsorptionError("Blocked attempt mentions an undeclared probe")
        if any(p not in protocol.feasible for p, _ in self.observations):
            raise AbsorptionError("A physically infeasible event cannot be actualized")
        if any(p in protocol.feasible for p in self.blocked_attempts):
            raise AbsorptionError("Cannot claim a physically feasible probe was blocked")

        compatible = tuple(x for x in world.sources
                           if all(world.outcome(x, p) == y for p, y in self.observations))
        if not compatible:
            raise AbsorptionError("Evidence contradicts all declared sources: repair model class")

        # Identical response across compatible sources is soundly predictable,
        # but a prediction is NOT an observed causal event.
        predicted = tuple((p, world.outcome(compatible[0], p))
                          for p in world.probes
                          if all(world.outcome(x, p) == world.outcome(compatible[0], p)
                                 for x in compatible))
        seed = protocol.seeds + tuple(f"obs:{p}:{y}" for p, y in self.observations) + tuple(
            f"predict:{p}:{y}" for p, y in predicted)
        closure = least_horn_closure(seed, protocol.rules)
        epistemic = tuple(p for p in world.probes if closure.knows(f"can:{p}"))
        physical = tuple(p for p in epistemic if p in protocol.feasible)
        blocked = tuple(p for p in epistemic if p not in protocol.feasible)
        return AbsorbedModel(compatible, self.observations, predicted, epistemic,
                             physical, blocked, closure)

    def succ(self, protocol: AbsorbingProtocol, actual: str) -> "AbsorbingFrame":
        """One maximal model-relative probe batch plus immediate absorption."""
        model = self.absorb(protocol)
        if actual not in model.compatible:
            raise AbsorptionError("Actual source inconsistent with causal history")
        used = {p for p, _ in self.observations}
        blocked = set(self.blocked_attempts)
        fresh = [p for p in model.epistemically_accessible if p not in used and p not in blocked]
        if not fresh:
            return self
        observed_next = tuple((p, protocol.world.outcome(actual, p))
                              for p in fresh if p in protocol.feasible)
        blocked_next = tuple(p for p in fresh if p not in protocol.feasible)
        result = AbsorbingFrame(self.observations + observed_next,
                                self.blocked_attempts + blocked_next, self.frames + 1)
        result.absorb(protocol)
        return result

    def quiescent(self, protocol: AbsorbingProtocol) -> bool:
        model = self.absorb(protocol)
        used = {p for p, _ in self.observations}.union(self.blocked_attempts)
        return all(p in used for p in model.epistemically_accessible)

    def hard_succ(self, protocol: AbsorbingProtocol, actual: str) -> "AbsorbingFrame":
        """Finite exhaustive closure with a uniform finite termination bound."""
        if actual not in protocol.world.sources:
            raise AbsorptionError("Actual source must exist in the declared world")
        state = self
        for _ in range(len(protocol.world.probes) + 1):
            nxt = state.succ(protocol, actual)
            if nxt == state:
                if not state.quiescent(protocol):
                    raise ArithmeticError("SUCC unexpectedly stopped before full absorption")
                return state
            state = nxt
        raise ArithmeticError("Finite probe exhaustion failed to terminate")


def target_values(model: AbsorbedModel, target: Mapping[str, str]) -> tuple[str, ...]:
    if any(x not in target or type(target[x]) is not str or not target[x]
           for x in model.compatible):
        raise AbsorptionError("Target must be defined for every surviving source")
    return tuple(sorted({target[x] for x in model.compatible}))


def transmit_frame(frame: AbsorbingFrame, protocol: AbsorbingProtocol,
                   target: Mapping[str, str]) -> bytes:
    """Finite-channel completion of target ONLY if all compatible sources agree.

    The actual measurement outcomes are presumed to have authenticated causal
    provenance *externally*, using a trusted measurement channel. This payload
    itself is not cryptographic evidence of their truth.
    """
    if not frame.quiescent(protocol):
        raise AbsorptionError("Cannot label unfinished probe exploration complete")
    model = frame.absorb(protocol)
    values = target_values(model, target)
    if len(values) != 1:
        raise AbsorptionError("No finite message can justify one target for indistinguishable candidates")
    record = {
        "protocol": "obs-succ-absorbing-v1",
        "observed": [[p, y] for p, y in frame.observations],
        "blocked": list(frame.blocked_attempts),
        "target": values[0],
    }
    return json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")


def receive_frame(payload: bytes, protocol: AbsorbingProtocol,
                  target: Mapping[str, str]) -> tuple[AbsorbingFrame, str]:
    """Recompute the claim from a shared public protocol and trusted outcomes.

    This rejects forged *semantic assertions* inconsistent with the data; it
    cannot authenticate the channel source or the measurement hardware.
    """
    if type(payload) is not bytes or len(payload) > 1_000_000:
        raise AbsorptionError("Transmission requires bounded finite bytes")
    try:
        obj = json.loads(payload.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise AbsorptionError("Malformed finite message") from exc
    if type(obj) is not dict or set(obj) != {"protocol", "observed", "blocked", "target"}:
        raise AbsorptionError("Message must use exactly the declared public schema")
    if obj["protocol"] != "obs-succ-absorbing-v1" or type(obj["target"]) is not str:
        raise AbsorptionError("Unknown transmission language or invalid target assertion")
    try:
        if type(obj["observed"]) is not list or type(obj["blocked"]) is not list:
            raise AbsorptionError("Malformed outcome list")
        frame = AbsorbingFrame(
            tuple(tuple(entry) if type(entry) is list else entry for entry in obj["observed"]),
            tuple(obj["blocked"]),
            0,
        )
        model = frame.absorb(protocol)
        if not frame.quiescent(protocol):
            raise AbsorptionError("Receiver detects incomplete frame")
        possible = target_values(model, target)
        if len(possible) != 1 or possible[0] != obj["target"]:
            raise AbsorptionError("Transmitted completion contradicts surviving source class")
    except (TypeError, KeyError, ValueError) as exc:
        if isinstance(exc, AbsorptionError):
            raise
        raise AbsorptionError("Invalid finite completion message") from exc
    return frame, possible[0]


def absorbing_demo() -> dict:
    """New epistemic probes arise from consistent information; hardware may block."""
    world = FiniteProbeWorld(
        ("A", "B"), ("coarse", "fine"),
        (("same", "A"), ("same", "B")),
    )
    rules = (HornRule(("obs:coarse:same",), "can:fine"),)
    open_system = AbsorbingProtocol(world, ("can:coarse",), rules, world.probes)
    physical_system = AbsorbingProtocol(world, ("can:coarse",), rules, ("coarse",))
    initial = AbsorbingFrame()
    first = initial.succ(open_system, "B")
    end = first.hard_succ(open_system, "B")
    blocked_end = initial.hard_succ(physical_system, "B")
    target = {"A": "A", "B": "B"}
    packet = transmit_frame(end, open_system, target)
    decoded, reconstructed = receive_frame(packet, open_system, target)
    assert (first.absorb(open_system).compatible == ("A", "B")
            and end.absorb(open_system).identified
            and blocked_end.absorb(physical_system).epistemically_accessible == world.probes
            and blocked_end.absorb(physical_system).compatible == ("A", "B")
            and not blocked_end.absorb(physical_system).identified
            and reconstructed == "B"
            and decoded.observations == end.observations)
    return {
        "status": "FINITE_ABSORBING_HARD_SUCC_CERTIFIED",
        "initial_compatible": list(initial.absorb(open_system).compatible),
        "after_noncontradictory_coarse": list(first.absorb(open_system).compatible),
        "new_epistemic_probe": "fine",
        "full_hard_succ_identified": end.absorb(open_system).identified,
        "closed_frame_count": end.frames,
        "blocked_epistemically_known": list(blocked_end.absorb(physical_system).physically_blocked),
        "physical_barrier_remaining_candidates": list(blocked_end.absorb(physical_system).compatible),
        "finite_transmission_bytes": len(packet),
        "receiver_reconstructed_target": reconstructed,
        "authenticated_real_world_source": False,
        "infinite_physical_process_executed": False,
        "classical_LEM_refuted": False,
        "RH_claimed": False,
    }
