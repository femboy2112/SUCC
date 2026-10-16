#!/usr/bin/env python3
"""Deterministic replay/communication/authority discriminator."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.collective_effects import (
    AnalyticImport, Context, Derive, Event, ExactQuadratic, Relay, Replay, run,
)
from observational_succ.source_lambda import Join, Passport, Read


def receipt():
    p = Passport("collective-effects-declared-fixture", 1)
    c = Context(p, (Event("A:2:0", "A", p, 2, 1), Event("B:3:0", "B", p, 3, 2)))
    result = run((Replay("A:2:0", "A"), Replay("B:3:0", "B"),
                  Relay(1, "B", "A"), Derive(Join(Read(2), Read(3)), (0, 2), "A")), c)
    repeated = run((Replay("A:2:0", "A"),) * 8, c)
    debt = run((AnalyticImport("source tail implication", ("OPEN_SOURCE_TAIL",)),
                AnalyticImport("consequence", (), (0,)),
                ExactQuadratic(((1, 2), (2, 1)), (1, -1), (1,))), c)
    return {"status": "EXACT_FINITE_DECLARED_MODEL",
            "joint_modulus": result.artifacts[-1].value.modulus,
            "joint_value": result.artifacts[-1].value.value,
            "origins": sorted(result.referenced_origins),
            "replays": 8, "replayed_origin_count": len(repeated.referenced_origins),
            "transitive_debts": sorted(debt.artifacts[-1].obligations),
            "physical_measurements_performed": 0,
            "original_source_authenticated": False, "RH_proved": False}


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
