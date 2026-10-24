#!/usr/bin/env python3
"""Replay the Principia-inspired endpoint diagnostic on existing SUCC machines."""
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.ancestral_observer import audit_ancestral_observer
from observational_succ.future_safe_quotient import (
    Edge, Machine, State, audit_representation,
)


def example(edges):
    return Machine(
        tuple(State(s, "declared-example", "") for s in ("a", "b", "c")),
        ("next",), tuple(Edge(x, "next", y, Fraction(1)) for x, y in edges),
    )


def main():
    labels = ("A", "A", "B")
    ghost = example((("b", "c"),))
    slow = example((("a", "b"), ("b", "c")))
    selected_a = audit_ancestral_observer(ghost, labels, "a")
    selected_b = audit_ancestral_observer(ghost, labels, "b")
    slow_results = [audit_ancestral_observer(slow, labels, s.name) for s in slow.states]
    stronger = audit_representation(slow, labels)
    if (selected_a.endpoint_exact or not selected_b.endpoint_exact
            or not all(r.endpoint_exact for r in slow_results)
            or stronger["future_safe"] or stronger["autonomous"]):
        raise RuntimeError("A selected-source control changed its claimed behavior")
    paths = (
        "observational_succ/ancestral_observer.py",
        "observational_succ/future_safe_quotient.py",
        "scripts/principia_ancestral_probe.py",
    )
    payload = {
        "status": "EXACT_FINITE_MODEL",
        "source_hashes": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        "convention": "Reflexive finite-path closure, including isolated states",
        "same_observation_selected_a": asdict(selected_a),
        "same_observation_selected_b": asdict(selected_b),
        "endpoint_exact_but_not_trace_exact": {
            "all_starts_endpoint_exact": all(r.endpoint_exact for r in slow_results),
            "stronger_existing_audit": {
                k: asdict(v) if hasattr(v, "__dataclass_fields__") else v
                for k, v in stronger.items()
            },
        },
        "source_authentication_claimed": False,
        "pi_normality_proved": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
