#!/usr/bin/env python3
"""B13: bounded exact support extraction; no arithmetic proof certification.

The Horn proof builder and exhaustive valuation checker are separate instruments.
Only this investigator's receipt is written. No package bytecode is generated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import signal
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ATOMS = ("a", "b", "c")


def powerset(items):
    items = tuple(items)
    return [frozenset(items[i] for i in range(len(items)) if mask >> i & 1)
            for mask in range(1 << len(items))]


def derive(axioms, rules, births, order=None):
    """Finite proof DAG, with stage support computed bottom-up."""
    known = set(axioms)
    supports = {a: births[("axiom", a)] for a in axioms}
    trace = []
    order = tuple(range(len(rules))) if order is None else tuple(order)
    while True:
        before = len(known)
        for i in order:
            premises, conclusion = rules[i]
            if premises <= known and conclusion not in known:
                support = max([births[("rule", premises, conclusion)]]
                              + [supports[p] for p in premises])
                known.add(conclusion)
                supports[conclusion] = support
                trace.append((tuple(sorted(premises)), conclusion, support))
        if len(known) == before:
            return frozenset(known), supports, trace


def semantic_consequences(axioms, rules, atoms=ATOMS):
    """Independent complete finite semantics; never invokes derive()."""
    admitted = []
    for truth in powerset(atoms):
        if all(a in truth for a in axioms) and all(
                not all(p in truth for p in premises) or conclusion in truth
                for premises, conclusion in rules):
            admitted.append(truth)
    assert admitted  # the all-true valuation models positive Horn theories
    return frozenset(a for a in atoms if all(a in truth for truth in admitted))


def stage(axioms, rules, births, n):
    return (frozenset(a for a in axioms if births[("axiom", a)] <= n),
            tuple((p, c) for p, c in rules if births[("rule", p, c)] <= n))


def replay(axioms, rules, trace, n):
    """Check the actual transported finite proof edges, not only its conclusion."""
    known = set(axioms)
    for premises, conclusion, support in trace:
        if support <= n:
            assert (frozenset(premises), conclusion) in rules
            assert all(p in known for p in premises)
            known.add(conclusion)
    return known


def horn_exhaustion():
    pool = tuple((p, c) for c in ATOMS
                 for p in powerset(a for a in ATOMS if a != c) if p)
    births = {("axiom", a): i + 1 for i, a in enumerate(ATOMS)}
    births.update({("rule", p, c): 1 + i % 3
                   for i, (p, c) in enumerate(pool)})
    configurations = semantic_checks = support_replays = order_checks = 0
    for axioms in powerset(ATOMS):
        for selected in powerset(range(len(pool))):
            rules = tuple(pool[i] for i in sorted(selected))
            configurations += 1
            union, supports, trace = derive(axioms, rules, births)
            reverse, _, _ = derive(axioms, rules, births,
                                    reversed(range(len(rules))))
            assert reverse == union
            order_checks += 1
            stage_union = set()
            for n in (1, 2, 3):
                a_n, r_n = stage(axioms, rules, births, n)
                local, _, _ = derive(a_n, r_n, births)
                assert local == semantic_consequences(a_n, r_n)
                semantic_checks += 1
                stage_union.update(local)
            assert frozenset(stage_union) == union
            for atom, support in supports.items():
                a_s, r_s = stage(axioms, rules, births, support)
                assert atom in replay(a_s, r_s, trace, support)
                assert atom in semantic_consequences(a_s, r_s)
                support_replays += 1
            # Inclusion transport leaves every formula and proof edge intact.
            for p, c, support in trace:
                for destination in range(support, 4):
                    _, r_d = stage(axioms, rules, births, destination)
                    assert (frozenset(p), c) in r_d
    return {"atom_count": 3, "possible_rules": len(pool),
            "theories_exhausted": configurations,
            "independent_stage_semantics_checks": semantic_checks,
            "support_replays": support_replays,
            "opposite_rule_order_checks": order_checks,
            "stage_birth_patterns_exhausted": False,
            "birth_pattern": "axioms 1,2,3; rules 1+i mod 3"}


def hostile_controls():
    # Instance facts do not imply a fresh universal/report atom.
    premises = frozenset(("P0", "P1", "P2"))
    atoms = tuple(sorted(premises)) + ("ALL_P",)
    witnesses = [sorted(w) for w in powerset(atoms)
                 if premises <= w and "ALL_P" not in w]
    assert witnesses == [["P0", "P1", "P2"]]
    # Actual first-order finite structure: named instances miss an unnamed point.
    domain = (0, 1, 2)
    named = (0, 1)
    predicate = {0: True, 1: True, 2: False}
    assert all(predicate[c] for c in named)
    assert not all(predicate[x] for x in domain)
    # Directedness matters: union combines premises unavailable in either branch.
    rule = ((frozenset(("a", "b")), "c"),)
    births = {("axiom", "a"): 1, ("axiom", "b"): 1,
              ("rule", frozenset(("a", "b")), "c"): 1}
    left = derive(frozenset(("a",)), rule, births)[0]
    right = derive(frozenset(("b",)), rule, births)[0]
    joined = derive(frozenset(("a", "b")), rule, births)[0]
    assert "c" not in left | right and "c" in joined
    # Retiring an old rule prevents transport of its old proof.
    old_rules = ((frozenset(("a",)), "b"),)
    old_births = {("axiom", "a"): 1,
                  ("rule", frozenset(("a",)), "b"): 1}
    old = derive(frozenset(("a",)), old_rules, old_births)[0]
    revised = derive(frozenset(("a",)), (), old_births)[0]
    assert "b" in old and "b" not in revised
    return {"all_instance_facts_universal_false_model": witnesses[0],
            "unnamed_element_first_order_model": {
                "domain": domain, "named_constants": named,
                "P_true_at": named, "universal_counterexample": 2},
            "not_a_Godel_proof": True,
            "nondirected_branches": {"left": sorted(left), "right": sorted(right),
                                     "union_theory": sorted(joined)},
            "rule_retirement": {"before": sorted(old), "after": sorted(revised)},
            "expected_failure_count": 4}


def native_smoke():
    sys.path.insert(0, str(ROOT))
    from observational_succ.godel_succ import (
        delayed_halt, machine_prefix, two_counter_loop)
    from observational_succ.ordinal_succ_report import exact_bounded_time_horizon
    from observational_succ.checkpoint_meta_tower import (
        GroundRule, HornTheory, MetaTowerError, Report, growing_theory_checkpoints)
    loop = two_counter_loop()
    delayed = delayed_halt(3)
    traces = []
    for n in range(3):
        a, b = machine_prefix(loop, n), machine_prefix(delayed, n)
        assert a == b and not a.universal_claim_proved
        traces.append(a.__dict__)
    later = machine_prefix(delayed, 3)
    assert later.status == "refuted" and later.first_counterexample == 3
    horizon = exact_bounded_time_horizon((0, 1))
    assert horizon["certified_source_SUCC_horizon"] == 3
    first = HornTheory("source", "basis", (), (GroundRule(("e",), "a"),))
    second = HornTheory("source", "basis", (), first.rules +
                        (GroundRule(("a",), "b"),))
    delivery = ((Report("id", "source", "basis", 1, "owner", "e"),), ())
    records = growing_theory_checkpoints(
        (first, second), delivery, trusted_event_ids=frozenset(("id",)), target="b")
    assert [x["target_certified"] for x in records] == [False, True]
    rejected = []
    for mutated in (first, HornTheory("source", "changed-basis", (), second.rules)):
        try:
            growing_theory_checkpoints((second, mutated), delivery,
                trusted_event_ids=frozenset(("id",)), target="b")
        except MetaTowerError as exc:
            rejected.append(str(exc))
        else:
            raise AssertionError("Incompatible theory must reject proof transport")
    return {"shared_boolean_monitor_prefixes": traces,
            "delayed_halt_first_counterexample": later.__dict__,
            "finite_report_source_horizon_for_0_1": 3,
            "numeric_Gamma_report_executed": False,
            "growing_rule_target_certified": [x["target_certified"] for x in records],
            "transport_mutations_rejected": rejected}


def provenance():
    manifest = json.loads((ROOT / "provenance/IMPORT_MANIFEST.json").read_text())
    paths = ("observational_succ/godel_succ.py", "observational_succ/ordinal_succ_report.py",
             "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_GODEL_BRIDGE.md",
             "provenance/origins/fuckingrh/research/2026-10-10/OMEGA_SUCC_SECOND_ORDER_WEIL_REPORT.md")
    records = []
    for entry in manifest["entries"]:
        if entry["destination_path"] not in paths:
            continue
        actual = subprocess.check_output(["git", "hash-object", entry["destination_path"]],
                                         cwd=ROOT, text=True).strip()
        assert actual == entry["destination_git_blob_sha"]
        origin = subprocess.check_output([
            "git", "-C", "/home/leah/FuckingRH", "rev-parse",
            manifest["source_commit"] + ":" + entry["original_path"]], text=True).strip()
        assert origin == entry["original_git_blob_sha"]
        records.append({"path": entry["destination_path"], "current_git_blob": actual,
                        "origin_git_blob": origin, "matched_manifest": True})
    assert len(records) == 4
    return {"source_commit": manifest["source_commit"], "checked_paths": records,
            "native_checkpoint_git_blob": subprocess.check_output([
                "git", "hash-object", "observational_succ/checkpoint_meta_tower.py"],
                cwd=ROOT, text=True).strip(), "physical_authentication": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("25s budget")))
    signal.alarm(25)
    started = time.monotonic()
    result = {"id": "B13", "claim_id": "SWM-B13", "parent_sha": PARENT,
              "branch": "research/swm-b13-2026-10-13",
              "proof_status": "PROVED LOCAL finite support; CLASSICAL conditional Godel guard",
              "probe_status": "TESTED MODEL",
              "proof_assistant_kernel_checked": False,
              "full_suite_run": False, "compiler_run": False,
              "physical_infinity_performed": False, "academic_novelty_claimed": False,
              "provenance": provenance(), "exact_horn_probe": horn_exhaustion(),
              "hostile_controls": hostile_controls(), "native_smoke": native_smoke()}
    result["elapsed_seconds"] = round(time.monotonic() - started, 6)
    result["probe_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["command"] = ("PYTHONDONTWRITEBYTECODE=1 timeout 30s python "
        "research/2026-10-13/SWARM_ATLAS/B13_probe.py --receipt "
        "research/2026-10-13/SWARM_ATLAS/B13_receipt.json")
    result["exit_code"] = 0
    result["preserved_setup_failures"] = [
        {"command": "cat research/2026-10-12/CHECKPOINT_META_OBSERVER_TOWER.md", "exit": 1,
         "reason": "wrong guessed dossier name; corrected by rg to CARRIER_RELATIVE_META_SUCC_AND_DOVETAIL.md"},
        {"command": "git cat-file -t ba075348b7bcc66d938b3e0ca96c26e95bba340a", "exit": 128,
         "reason": "origin absent from SUCC object database; verified in /home/leah/FuckingRH"}]
    result["primary_sources"] = [
        {"url": "https://people.math.ethz.ch/~halorenz/4students/Literatur/TuringOrdinalLogic.pdf",
         "locator": "Turing original pp.193-197,203; separate editorial preface", "browsed": True},
        {"url": "https://arxiv.org/html/2405.09275v2",
         "locator": "Introduction: fixed c.e. axiomatization and local versus uniform reflection",
         "browsed": True},
        {"url": "https://link.springer.com/article/10.1007/BF01700692",
         "locator": "Godel 1931 publisher record; full original text not obtained", "browsed": True}]
    serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        expected = Path(__file__).with_name("B13_receipt.json")
        if args.receipt.resolve() != expected:
            raise ValueError("Write only the assigned B13 receipt")
        expected.write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
