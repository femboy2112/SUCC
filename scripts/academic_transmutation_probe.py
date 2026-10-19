#!/usr/bin/env python3
"""Reproduce the exact foundational spine and optional pinned Lean audit.

This external harness invokes the generator and a separate checker. The checker
itself imports neither this harness nor the generator. Source authenticity and
infinite analytic sign are not consequences of finite table acceptance.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import future_safe_quotient as Q
from observational_succ import lawful_history_gluing as G
from observational_succ.arithmetic_source_minimality import LateBeurlingPair
from check_academic_certificate import check_certificate


def run():
    states = tuple(Q.State(x, "declared-source", "1" if x == "z" else "0")
                   for x in ("p", "p_copy", "q", "u", "v", "z"))
    edges = [Q.Edge(x, "fast", "z", F(7)) for x in ("p", "p_copy")]
    edges += [Q.Edge(x, "a", "u", F(1, 3)) for x in ("p", "p_copy")]
    edges += [Q.Edge("q", "fast", "q", F(7)), Q.Edge("q", "a", "v", F(1, 3)),
              Q.Edge("u", "b", "z", F(1, 2)), Q.Edge("v", "b", "v", F(1, 2))]
    machine = Q.Machine(states, ("fast", "a", "b"), tuple(edges))
    certificate = Q.minimize(machine)
    payload = Q.certificate_payload(machine, certificate)
    checked = check_certificate(payload)
    threshold = Q.minimum_distinguishing_budget(machine, "p", "q")
    assert threshold.budget == F(5, 6) and threshold.word == ("a", "b")
    assert Q.distinguishing_word(machine, "p", "q") == ("fast",)
    assert checked["blocks"] == 5

    p, u, v, z = (G.PrivateState("original", x, y)
                  for x, y in (("p", "P"), ("u", "M"), ("v", "M"), ("z", "Z")))
    graph = G.SourceGraph((p, u, v, z), frozenset((p,)),
                          frozenset(((p, "a", u), (v, "b", z))))
    audit = G.audit_projection(graph, "original")
    cut = audit.certificate
    assert audit.status == "SPURIOUS_PATH" and G.verify_cut(graph, cut)
    assert G.locally_compatible(graph, cut.source, cut.reports, cut.actions)

    model = LateBeurlingPair.beyond(100)
    arithmetic = model.first_braid_witness()
    assert model.count(100) == 100 and arithmetic["defect"] == -1
    return payload, {
        "status": "EXACT_SPINE_VERIFIED",
        "finite_quotient": checked,
        "minimum_budget": {"value": str(threshold.budget), "word": list(threshold.word),
                           "shortest_word": ["fast"], "shortest_word_cost": "7"},
        "gluing": {"local_report_compatibility": True, "private_lift": False,
                   "cut_layers": [[x.name for x in sorted(layer)] for layer in cut.layers],
                   "reports": list(cut.reports), "actions": list(cut.actions),
                   "obstruction_bound": G.obstruction_bound(graph, "original")},
        "arithmetic": {"matched_horizon": 100, "first_omitted_prime": model.p,
                       "second_replaced_prime": model.q,
                       "replacement_values": [str(model.a), str(model.b)],
                       "density_multiplier": str(model.density_multiplier()),
                       "braid_witness": arithmetic},
        "physical_source_authenticated": False,
        "original_S4_sign": "OPEN", "RH_proved": False,
    }


def lean_audit(lean):
    source = ROOT / "formal/FutureSafeForgetting.lean"
    expected = {
        "fiber_safe_iff_descent": [], "descended_structure_unique": [],
        "finite_trace_preserved": ["propext"], "availability_reflected": ["propext"],
        "quotient_step_lifts_from_each_representative": [],
        "quotient_path_lifts_from_each_representative": ["propext"],
    }
    from cambrian_audit_c_lean import uncomment
    assert re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b",
                     uncomment(source.read_text())) is None
    version = subprocess.run([lean, "--version"], capture_output=True, text=True, check=True)
    assert "version 4.14.0," in version.stdout, "Use unchanged root pinned toolchain"
    result = subprocess.run([lean, "-DwarningAsError=true", str(source)],
                            capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stdout + result.stderr
    actual = {}
    for name in expected:
        prefix = "'ObservationalSUCC.FutureSafeForgetting." + name + "'"
        lines = [line for line in result.stdout.splitlines() if line.startswith(prefix)]
        assert len(lines) == 1, result.stdout
        if "does not depend on any axioms" in lines[0]:
            actual[name] = []
        else:
            m = re.search(r"depends on axioms: \[(.*)\]$", lines[0])
            assert m, lines[0]
            actual[name] = [x.strip() for x in m.group(1).split(",")]
    assert actual == expected, actual
    controls = {}
    with tempfile.TemporaryDirectory(prefix="succ-formal-controls-") as temp:
        for name, claim in {
            "false": "False",
            "phantom_availability": "(none : Option (Bool × Nat)) = some (false, 0)",
            "changed_cost": "(some (true, 1) : Option (Bool × Nat)) = some (true, 2)",
        }.items():
            path = Path(temp) / (name + ".lean")
            path.write_text("example : " + claim + " := by decide\n")
            bad = subprocess.run([lean, str(path)], capture_output=True, text=True, timeout=60)
            assert bad.returncode != 0 and "is false" in bad.stdout, bad.stdout + bad.stderr
            controls[name] = "REJECTED"
    return {"compiler": version.stdout.strip(), "kernel_exit": result.returncode,
            "axioms": actual, "false_controls": controls,
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate-output", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--lean")
    args = parser.parse_args()
    certificate, result = run()
    if args.lean:
        result["formal"] = lean_audit(args.lean)
    if args.certificate_output:
        args.certificate_output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    if args.output:
        args.output.write_text(json.dumps(serial(result), indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "blocks": result["finite_quotient"]["blocks"],
                      "minimum_budget": result["minimum_budget"]["value"],
                      "private_path_cut": result["gluing"]["cut_layers"],
                      "arithmetic_braid_defect": -1,
                      "formal_kernel_checked": "formal" in result,
                      "RH_proved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
