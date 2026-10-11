"""Transactional field-relative observation with replayable, non-erasing history.

A field step registers a contextual observation. Propagation is a separate
atomic operation. A full-history reverse restores engine state using its
retained witnesses; it is NOT physical time reversal or a proof of RH.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any

from .core import (ActualizationError, BasisLift, BudgetExceeded, DomainError,
                   Frame, IncompleteObservation, Scalar, ONE)
from .arithmetic import Limits, ShadowIndex, connected_audit, source_at


SCHEMA = "field-relative-observational_succ/1"


class LossyHistoryError(ActualizationError):
    pass


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(obj):
    return sha256(canonical(obj).encode("utf-8")).hexdigest()


def text(value, label):
    if not isinstance(value, str) or not value or len(value) > 1024:
        raise DomainError(f"{label} must be a nonempty string of at most 1024 characters")
    return value


def conjugate_data(obj):
    """Declared anti-linear coefficient/fiber conjugation; real positions unchanged."""
    if isinstance(obj, dict):
        if set(obj) == {"re", "im"}:
            return Scalar.from_data(obj).conjugate().data()
        return {k: conjugate_data(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [conjugate_data(v) for v in obj]
    return obj


@dataclass(frozen=True)
class Record:
    seq: int
    kind: str
    payload: str
    before: str
    after: str
    previous: str
    hash: str

    def data(self):
        return {"seq": self.seq, "kind": self.kind, "payload": json.loads(self.payload),
                "before": json.loads(self.before), "after": json.loads(self.after),
                "previous": self.previous, "hash": self.hash}


class Engine:
    """A bounded event-sourced state machine with exact arithmetic adapters.

    Event sequence != field coordinate != completed-model revision number.
    The natural arithmetic adapter is deliberately restricted to N_0,+1;
    a residue label is never silently treated as an ordinary integer event.
    """
    def __init__(self, frame: Frame | None = None, start=None, *, arithmetic=False,
                 limits: Limits | None = None, lifts: tuple[BasisLift, ...] = (), conductor: int = 1):
        self.frame = frame or Frame()
        self.limits = limits or Limits()
        if type(arithmetic) is not bool:
            raise DomainError("arithmetic must be boolean")
        self.arithmetic = arithmetic
        if type(conductor) is not int or conductor < 1:
            raise DomainError("Conductor must be a positive integer")
        self.conductor = conductor
        self.lifts = tuple(lifts)
        if len({v.name for v in self.lifts}) != len(self.lifts) or len(lifts) > 16:
            raise DomainError("Basis-lift names must be distinct, at most 16 lifts")
        origin = self.frame.point(start if start is not None else (0,)*self.frame.dimension)
        if self.arithmetic and (self.frame.domain != "natural" or self.frame.step != (1,) or origin != (0,)):
            raise DomainError("Natural arithmetic adapter requires N_0, origin 0, step +1")
        self._config = {"frame": self.frame.data(), "start": list(map(str, origin)),
                        "arithmetic": self.arithmetic, "conductor": self.conductor, "limits": self.limits.data(),
                        "lifts": [lift.data() for lift in self.lifts]}
        self._state = {"coordinate": list(map(str, origin)), "tick": 0, "phase": "ready",
                       "pending": None, "facts": {}, "expectations": {}, "arithmetic": {},
                       "integrations": 0, "fibers": {v.name: [x.data() for x in v.initial] for v in self.lifts},
                       "last_integration": None}
        self._initial = canonical(self._state)
        self._records: list[Record] = []
        self._active: list[int] = []
        self._genesis = digest({"schema": SCHEMA, "config": self._config, "initial": self._state})
        self._bytes = len(self.dumps())
        if self._bytes > self.limits.max_trace_bytes:
            raise BudgetExceeded("Configuration exceeds the trace byte budget")

    @property
    def coordinate(self):
        return self.frame.point(self._state["coordinate"])

    @property
    def state(self):
        """A detached snapshot: callers cannot mutate the live model."""
        return deepcopy(self._state)

    @property
    def records(self):
        return tuple(self._records)

    @property
    def head(self):
        return self._records[-1].hash if self._records else self._genesis

    @property
    def coefficients(self):
        return {int(n): Scalar.from_data(item["value"]) for n, item in self._state["arithmetic"].items()}

    def _ready(self):
        if self._state["phase"] != "ready":
            raise DomainError("Observation pending: propagate it before another field step")

    def _commit(self, kind, payload, state):
        if len(self._records) >= self.limits.max_records:
            raise BudgetExceeded("Journal budget reached; no record has been discarded")
        seq = len(self._records)+1
        body = {"seq": seq, "kind": kind, "payload": deepcopy(payload),
                "before": self.state, "after": deepcopy(state), "previous": self.head}
        r = Record(seq, kind, canonical(payload), canonical(body["before"]),
                   canonical(body["after"]), body["previous"], digest(body))
        new_bytes = self._bytes + len(canonical(r.data())) + int(bool(self._records))
        if new_bytes > self.limits.max_trace_bytes:
            raise BudgetExceeded("Lossless journal byte budget exhausted; state was not changed")
        self._bytes = new_bytes
        self._records.append(r)
        self._state = deepcopy(state)
        if kind != "reverse":
            self._active.append(seq)
        return r

    def step(self, value=None, *, context="default", probe="coordinate", direction=1):
        """Register one local event, without yet filing it in the model."""
        self._ready()
        text(context, "context")
        text(probe, "probe")
        if self.arithmetic and (direction != 1 or value is None):
            raise DomainError("Arithmetic encounter needs an explicit coefficient and forward step")
        coordinate = self.frame.succ(self.coordinate, direction)
        if self.arithmetic and coordinate[0] > self.limits.max_target:
            raise BudgetExceeded("Arithmetic event outside configured target horizon")
        v = None if value is None else Scalar.of(value).data()
        new = self.state
        new["coordinate"] = list(map(str, coordinate))
        new["tick"] += 1
        new["phase"] = "observed"
        new["pending"] = {"event": len(self._records)+1, "tick": new["tick"],
                          "frame": self.frame.name, "coordinate": new["coordinate"],
                          "context": context, "probe": probe, "value": v}
        for lift in self.lifts:
            old = tuple(Scalar.from_data(x) for x in new["fibers"][lift.name])
            new["fibers"][lift.name] = [x.data() for x in lift.apply(old, direction)]
        return self._commit("step", {"value": v, "context": context, "probe": probe,
                                     "direction": direction}, new)

    def propagate(self):
        """Complete one observation transaction; arithmetic uses only filed events."""
        if self._state["phase"] != "observed":
            raise DomainError("No observation awaits propagation")
        new = self.state
        obs = new["pending"]
        key = canonical([obs["frame"], obs["coordinate"], obs["context"], obs["probe"]])
        old = new["facts"].get(key)
        status = "new_context" if old is None else ("filed" if old["value"] == obs["value"] else "revised")
        new["facts"][key] = {"event": obs["event"], "value": obs["value"]}
        report = {"observation": obs["event"], "status": status, "source": None, "expectation": None}
        if self.arithmetic:
            n = int(self.coordinate[0])
            v = Scalar.from_data(obs["value"])
            if n == 1 and v != ONE:
                raise DomainError("a(1) must be 1 in this logarithmic chart; raw observation remains pending")
            new["arithmetic"][str(n)] = {"value": v.data(), "event": obs["event"]}
            if str(n) in new["expectations"]:
                expectation = new["expectations"][str(n)]
                report["expectation"] = "confirmed" if expectation["value"] == v.data() else "refuted"
                expectation["verdict"] = report["expectation"]
                expectation["observation"] = obs["event"]
            if n > 1:
                known = {int(k): Scalar.from_data(x["value"]) for k, x in new["arithmetic"].items()}
                report["source"] = connected_audit(ShadowIndex(known, self.limits), n, self.conductor)
        new["pending"] = None
        new["phase"] = "ready"
        new["integrations"] += 1
        new["last_integration"] = report
        return self._commit("propagate", {}, new)

    def advance(self, value=None, **kwargs):
        """One full event (two journal records); pending observations are not erased on error."""
        # Reserve both records before starting this convenience transaction.
        if len(self._records)+2 > self.limits.max_records:
            raise BudgetExceeded("Two records are needed for advance")
        self.step(value, **kwargs)
        return self.propagate()

    def predict(self, n, value, reason):
        """An explicit model assumption, never a direct encounter or a source leaf."""
        self._ready()
        if not self.arithmetic or type(n) is not int or not 1 <= n <= self.limits.max_target:
            raise DomainError("Prediction target outside natural arithmetic adapter")
        if str(n) in self._state["arithmetic"]:
            raise DomainError("Target already integrated; use an observation for revision")
        text(reason, "prediction provenance")
        new = self.state
        v = Scalar.of(value).data()
        new["expectations"][str(n)] = {"value": v, "reason": reason, "verdict": "unobserved"}
        return self._commit("predict", {"n": n, "value": v, "reason": reason}, new)

    def shadow(self, target, *, witnesses=False):
        if not self.arithmetic:
            raise DomainError("No arithmetic shadow adapter attached to this field")
        index = ShadowIndex(self.coefficients, self.limits)
        out = index.entry(target).data()
        pending = self._state["pending"]
        out["observed"] = out["integrated"] or bool(pending and int(self.coordinate[0]) == target)
        out["stage"] = "integrated" if out["integrated"] else ("observed" if out["observed"] else "shadow")
        if out["integrated"]:
            out["source"] = connected_audit(index, target, self.conductor)
        if witnesses:
            out["witnesses"] = index.witnesses(target)
        return out

    def bare_inverse(self):
        """Only invert the current field coordinate; do not undo an event or model."""
        return self.frame.succ(self.coordinate, -1)

    def shadow_inverse(self):
        """Retained predecessor *event* witnesses; not a uniquely inferred past."""
        matches = []
        for r in self._records:
            if r.kind == "step" and json.loads(r.after)["coordinate"] == self._state["coordinate"]:
                before = json.loads(r.before)
                matches.append({"record": r.seq, "coordinate": before["coordinate"],
                                "tick": before["tick"], "state_commitment": digest(before)})
        return {"current": self._state["coordinate"], "witnesses": matches,
                "unique_event": len(matches) == 1, "scope": "retained history only"}

    def reverse_last(self):
        """Uncompute one active action, retaining the complete forward/reverse journal."""
        if not self._active:
            raise DomainError("No active action to reverse")
        original = self._records[self._active[-1]-1]
        if original.after != canonical(self._state):
            raise ActualizationError("Current state does not match the reverse witness")
        record = self._commit("reverse", {"of": original.seq}, json.loads(original.before))
        self._active.pop()
        return record

    def reverse_all(self):
        if len(self._records)+len(self._active) > self.limits.max_records:
            raise BudgetExceeded("Insufficient journal capacity for lossless full reversal")
        size = self._bytes
        current = self.state
        for j, index in enumerate(reversed(self._active), len(self._records)+1):
            original = self._records[index-1]
            if canonical(current) != original.after:
                raise ActualizationError("Broken causal reverse chain")
            after = json.loads(original.before)
            body = {"seq": j, "kind": "reverse", "payload": {"of": index},
                    "before": current, "after": after, "previous": "0"*64, "hash": "0"*64}
            size += len(canonical(body)) + 1
            current = after
        if size > self.limits.max_trace_bytes:
            raise BudgetExceeded("Insufficient byte budget for full lossless reversal")
        while self._active:
            self.reverse_last()
        return self.state

    def document(self):
        return {"schema": SCHEMA, "config": deepcopy(self._config),
                "records": [r.data() for r in self._records], "head": self.head}

    def dumps(self):
        return canonical(self.document())

    @classmethod
    def _configured(cls, c):
        if not isinstance(c, dict) or set(c) != {"frame", "start", "arithmetic", "conductor", "limits", "lifts"}:
            raise DomainError("Malformed engine configuration")
        if type(c["arithmetic"]) is not bool:
            raise DomainError("arithmetic flag must be boolean")
        return cls(Frame.from_data(c["frame"]), c["start"], arithmetic=c["arithmetic"],
                   limits=Limits.from_data(c["limits"]),
                   lifts=tuple(BasisLift.from_data(x) for x in c["lifts"]), conductor=c["conductor"])

    def _dispatch(self, kind, p):
        if kind == "step" and set(p) == {"value", "context", "probe", "direction"}:
            return self.step(None if p["value"] is None else Scalar.from_data(p["value"]),
                             context=p["context"], probe=p["probe"], direction=p["direction"])
        if kind == "propagate" and p == {}:
            return self.propagate()
        if kind == "predict" and set(p) == {"n", "value", "reason"}:
            return self.predict(p["n"], Scalar.from_data(p["value"]), p["reason"])
        if kind == "reverse" and set(p) == {"of"}:
            if not self._active or self._active[-1] != p["of"]:
                raise DomainError("Reversal is not in causal stack order")
            return self.reverse_last()
        raise DomainError("Unknown or malformed journal action")

    @classmethod
    def loads(cls, data: str, *, expected_head=None):
        if not isinstance(data, str) or len(data.encode("utf-8")) > 32_000_000:
            raise BudgetExceeded("Serialized trace exceeds the 32 MB input bound")
        try:
            def unique_object(pairs):
                out = {}
                for key, value in pairs:
                    if key in out:
                        raise DomainError("Duplicate JSON field")
                    out[key] = value
                return out
            def invalid_constant(value):
                raise DomainError("Nonfinite JSON number")
            d = json.loads(data, object_pairs_hook=unique_object, parse_constant=invalid_constant)
            if not isinstance(d, dict) or d.get("schema") != SCHEMA:
                raise LossyHistoryError("Not a full reconstructible observational_succ history")
            if set(d) != {"schema", "config", "records", "head"}:
                raise DomainError("Unexpected trace fields")
            engine = cls._configured(d["config"])
            if not isinstance(d["records"], list) or len(d["records"]) > engine.limits.max_records:
                raise BudgetExceeded("Trace record budget exceeded")
            for supplied in d["records"]:
                # Recompute semantics AND hashes; hash consistency alone is not validity.
                actual = engine._dispatch(supplied["kind"], supplied["payload"])
                if canonical(actual.data()) != canonical(supplied):
                    raise DomainError("Trace differs from deterministic semantic replay")
            if engine.head != d["head"] or (expected_head is not None and engine.head != expected_head):
                raise DomainError("Trace head commitment mismatch")
            return engine
        except (KeyError, TypeError, json.JSONDecodeError, ZeroDivisionError) as exc:
            raise DomainError("Malformed serialized trace") from exc

    def verify(self):
        return Engine.loads(self.dumps(), expected_head=self.head).state == self.state

    def conjugated(self):
        """Conjugate all Q(i) data and fiber transports and replay, not physical T symmetry."""
        result = Engine._configured(conjugate_data(self._config))
        for r in self._records:
            result._dispatch(r.kind, conjugate_data(json.loads(r.payload)))
        return result

    def view(self, last=4):
        """Deliberately lossy observation window; cannot be loaded as full history."""
        if type(last) is not int or not 0 <= last <= self.limits.max_records:
            raise DomainError("Invalid observation-window size")
        records = self._records[-last:] if last else []
        return {"kind": "lossy_observation_window", "frame": self.frame.data(),
                "coordinate": list(self._state["coordinate"]), "tick": self._state["tick"],
                "phase": self._state["phase"], "visible_events": [{"seq": r.seq, "kind": r.kind} for r in records],
                "head_commitment": self.head, "lossless_reconstruction": False}


def run_arithmetic(horizon=12, *, kind="zeta", overrides=None, limits=None):
    """Convenience driver. Source values are requested exactly at their event."""
    if type(horizon) is not int or horizon < 1:
        raise DomainError("Horizon must be a positive integer")
    engine = Engine(arithmetic=True, limits=limits or Limits(max_target=max(64, horizon)),
                    conductor=5 if kind in {"chi5", "chi5_bar", "mixture5"} else 1)
    for n in range(1, horizon+1):
        engine.advance(source_at(n, kind, overrides), probe="arithmetic_coefficient", context=kind)
    return engine
