#!/usr/bin/env python3
"""Compare Main XXV replay diagnostics without rewriting historical receipts.

Exact source decisions, thresholds, counts and statuses must match. Only the
listed floating diagnostics in RESULTS_analytic.json admit bounded roundoff.
This checks reproducibility of finite computations; it is not an error bound
for a theorem or permission to promote any mathematical claim.
"""
from __future__ import annotations

import math

ANALYTIC = "RESULTS_analytic.json"
IDENTITY = "c^U_d_equals_shell_mean_of_A_Z"
CONTROLS = {"1_true", "2_coherent", "3_shadow", "4_alias", "5_hijack"}
ROUND_OFF = 1e-14
# This is an already-computed cancellation residual divided by a small bound;
# it is a diagnostic, not the bound or the pass/fail decision itself.
RATIO_ROUND_OFF = 1e-10


def _diagnostic_bound(path: tuple) -> float | None:
    if len(path) < 3 or path[0] != "shells":
        return None
    if len(path) == 8 and path[2] == "iad01" and path[5] == "windows" and path[7] == "R_definition":
        return ROUND_OFF
    if len(path) == 7 and path[2:4] == ("PR-2", "PR-2.2") and path[4] == "observed" and path[6] == "true_abs_cU":
        return ROUND_OFF
    if path[2] == "iad06":
        if len(path) == 8 and path[5] in ("c_U_d_for_d_1_to_dmax", "c_d_for_d_1_to_dmax") and type(path[6]) is int and path[7] in (0, 1):
            return ROUND_OFF
        if len(path) == 7 and path[5] == "random_H_rhs" and type(path[6]) is int:
            return ROUND_OFF
        if len(path) == 6 and path[5] == "transport_max_ratio_to_bound":
            return RATIO_ROUND_OFF
    if path[2:6] == ("PR-1", "checks", "PR-1.6", IDENTITY):
        if len(path) == 7 and path[6] == "max_abs_error":
            return ROUND_OFF
        if len(path) == 8 and path[6:] == ("worst", "error"):
            return ROUND_OFF
    return None


def _roundoff_witness(slot: dict, shell: str) -> bool:
    """Validate the sole permitted machine-roundoff argmax witness class.

    Both archived and replay slots are independently checked by the full probe;
    an argmax below 1e-14 can change identity under rounding. Neither witness is
    claimed to be a mathematically distinguished worst case. Counts, tolerance,
    failures and every other discrete field remain exact in the outer comparison.
    """
    try:
        w = slot["worst"]
        B = int(shell)
        lag = w["lag"]
        return (
            slot["kind"] == "identity" and slot["failures"] == 0
            and slot["counterexamples"] == [] and slot["tolerance"] == 1e-12
            and type(slot["max_abs_error"]) is float
            and math.isfinite(slot["max_abs_error"])
            and 0 <= slot["max_abs_error"] < ROUND_OFF
            and w["error"] == slot["max_abs_error"]
            and w["B"] == B and w["h"] in (1, 3, 8)
            and w["control"] in CONTROLS
            and type(lag) is int and lag > 0 and 16 ** (2 * lag) <= B ** 9
        )
    except (KeyError, TypeError, ValueError, OverflowError):
        return False


def compare(expected, actual, filename: str) -> dict:
    """Return every changed leaf with its rule; reject unlisted differences."""
    differences = []
    numeric_mode = filename == ANALYTIC
    witness_slots: set[tuple] = set()
    if numeric_mode:
        for shell, old in expected.get("shells", {}).items():
            try:
                prefix = ("shells", shell, "PR-1", "checks", "PR-1.6", IDENTITY)
                a = old["PR-1"]["checks"]["PR-1.6"][IDENTITY]
                b = actual["shells"][shell]["PR-1"]["checks"]["PR-1.6"][IDENTITY]
                if _roundoff_witness(a, shell) and _roundoff_witness(b, shell):
                    witness_slots.add(prefix)
            except (KeyError, TypeError):
                pass

    def changed(path, old, new, accepted=False, rule="exact"):
        differences.append(dict(path=list(path), archived=old, replay=new,
                                accepted=accepted, rule=rule))

    def walk(old, new, path=()):
        if type(old) is not type(new):
            changed(path, old, new, rule="type must match")
        elif isinstance(old, dict):
            if old.keys() != new.keys():
                changed(path, list(old), list(new), rule="keys must match")
                return
            for k in old:
                walk(old[k], new[k], path + (k,))
        elif isinstance(old, list):
            if len(old) != len(new):
                changed(path, len(old), len(new), rule="length must match")
                return
            for i, (a, b) in enumerate(zip(old, new)):
                walk(a, b, path + (i,))
        elif old != new:
            bound = _diagnostic_bound(path) if numeric_mode else None
            if type(old) is float and bound is not None:
                ok = math.isfinite(old) and math.isfinite(new) and abs(old - new) <= bound
                changed(path, old, new, ok, f"diagnostic absolute drift <= {bound}")
            elif len(path) == 8 and path[:6] in witness_slots and path[6] == "worst" and path[7] in ("control", "lag"):
                changed(path, old, new, True, "validated roundoff-scale argmax witness")
            else:
                changed(path, old, new)
    walk(expected, actual)
    return dict(status="PASS" if all(d["accepted"] for d in differences) else "FAIL",
                differences=differences,
                difference_count=len(differences),
                accepted_difference_count=sum(d["accepted"] for d in differences),
                policy="exact decisions; explicit analytic diagnostic roundoff only")
