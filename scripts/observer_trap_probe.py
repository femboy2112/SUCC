#!/usr/bin/env python3
"""Machine-readable finite model-dependent observer trap and repair receipt.

External access to the toy world's true source is declared, never smuggled
into the trapped observer's local observations.
"""
from __future__ import annotations

import json

from observational_succ.observer_traps import observer_trap_demo


def main():
    data = observer_trap_demo()
    assert data["status"] == "FINITE_OBSERVER_TRAP_CERTIFIED"
    assert data["model_access_trap"] == "access-trap"
    assert data["five_succ_updates_preferred"] == "A"
    assert data["five_succ_updates_compatible"] == ["A", "B"]
    assert data["global_separator"] == ["separator"]
    assert data["external_intervention_identified"] is True
    assert data["compatible_union_identified"] is True
    assert data["round_robin_first_refutation_succ"] == 2
    assert data["source_records_rewritten"] is False
    assert data["physical_cognition_claimed"] is False
    assert data["RH_or_Godel_independence_claimed"] is False
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
