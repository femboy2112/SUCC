#!/usr/bin/env python3
"""Replay six exact cluster-A result objects; --save writes namespaced receipts."""
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.causal_nerode_succ import SourceChart
from observational_succ.eodcs_relational_choice import RelationalIntervention
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
from observational_succ.cambrian_a_foundations import (
    and_source, bayesian_base_change, forward_evidence, multiobserver_information,
    pointwise_minimal_supports, public_history_square, relational_base_change,
    retained_claims, toolkit_pair_verdict,
)


def build_receipt():
    b = SourceChart("cluster-A-source", 0, "bits", ("x0", "x1"), ("a0", "a1"))
    a = SourceChart("cluster-A-source", 1, "bits", ("y0", "y1"), ("b", "b"))
    diag = RelationalIntervention("identity-with-collapsed-report", b, a,
                                  (("y0",), ("y1",)))
    full = RelationalIntervention("full-supported-rational-law", b, a,
                                  (("y0", "y1"), ("y0", "y1")))
    reset = Instrument("reset", (0, 1), (0, 0), (True, True))
    read = Instrument("read", (0, 1), (0, 1), (True, True))
    history = public_history_square(FiniteCarrier(2, (reset, read), "bit-source", "bits"),
                                    (("reset", "read"),))
    field = and_source(6)
    blind = Instrument("tick", (0, 0), (0, 1), (True, True))
    darkness = toolkit_pair_verdict(FiniteCarrier(2, (blind,), "bit-source", "bits"), 0, 1)
    lamp = toolkit_pair_verdict(FiniteCarrier(2, (blind, read), "bit-source", "bits"), 0, 1)
    common = multiobserver_information(tuple(tuple((s >> i) & 1 for s in range(8))
                                            for i in range(3)))
    result = {
        "01": {"claim_ids": ["CA01"], "status": "CLASSICAL / PROVED LOCAL",
               "question": "Universal source-typed observational state",
               "quantifiers": "Every lawful history; every quotient-invariant function has one unique report decoder",
               "rival": "Current carrier and causal history are interchangeable",
               "evidence": history, "proof": "CAMBRIAN_A_FOUNDATIONS.md#01",
               "cheapest_falsifier": "Two-state reset with preserved versus silent outcome",
               "limitations": "Universal report quotient only; no universal ontology, source authentication or ideal execution"},
        "02": {"claim_ids": ["CA02a", "CA02b", "CA02c"],
               "status": "CLASSICAL / PROVED LOCAL",
               "question": "Changing-source relational and weighted base change",
               "quantifiers": "Every old report event, post report predicate, and nonnull conditional event at the stated gate",
               "rival": "Commuting square or identical support transports every source fact and conditional law",
               "evidence": {"diagonal_gates": asdict(relational_base_change(diag)),
                            "old_evidence": forward_evidence(diag, ("a0",)),
                            "complete_support_gates": asdict(relational_base_change(full)),
                            "independent_law": asdict(bayesian_base_change(full, ((Q(1,4), Q(1,4)), (Q(1,4), Q(1,4))))),
                            "same_support_correlated_mutation": asdict(bayesian_base_change(full, ((Q(1,8), Q(3,8)), (Q(3,8), Q(1,8)))))},
               "proof": "CAMBRIAN_A_FOUNDATIONS.md#02",
               "cheapest_falsifier": "Identity source with collapsed post report, then four-positive rational weight mutation",
               "limitations": "CA02c fixes one declared joint law; does not assert unchanged evidence mass or all-prior descent"},
        "03": {"claim_ids": ["CA03"], "status": "CLASSICAL / PROVED LOCAL",
               "question": "Knowledge lattice and destructive intervention",
               "quantifiers": "Every Boolean fact measurable in the old report",
               "rival": "Each observation increases knowledge of all original and current claims",
               "evidence": {"reset_preserves_old_fact": retained_claims((0,1), (0,0)),
                            "history_preserves_old_fact": retained_claims((0,1), ((0,0),(1,0)))},
               "proof": "CAMBRIAN_A_FOUNDATIONS.md#03",
               "cheapest_falsifier": "Bit erased by reset",
               "limitations": "Compare reports on one source/path domain; current truths require distinct predicates"},
        "04": {"claim_ids": ["CA04"], "status": "CLASSICAL / PROVED LOCAL",
               "question": "Pointwise minimal proof support and distinct cost contracts",
               "quantifiers": "Every rival source with another target value; all AND_n widths under declared bit access",
               "rival": "One scalar or support count bounds physical cost, communication and macro-updates",
               "evidence": {"AND6_true_support": pointwise_minimal_supports(field, 63, "AND"),
                            "AND6_zero_support": pointwise_minimal_supports(field, 0, "AND")},
               "proof": "CAMBRIAN_A_FOUNDATIONS.md#04",
               "cheapest_falsifier": "Cost rescaling, batch-versus-serial access, target-only authorized testimony",
               "limitations": "Static logical support does not certify executable destructive policy or proof authority"},
        "05": {"claim_ids": ["CA05"], "status": "CLASSICAL / PROVED LOCAL",
               "question": "Toolkit-relative darkness, route gaps and uniform-policy trap",
               "quantifiers": "All legal finite action words for each pair; uniform policy uses a stronger quantifier",
               "rival": "A failed route or pairwise separators alone decide uniform acquisition",
               "evidence": {"dark_pair": darkness, "extended_probe_lamp": lamp},
               "proof": "CAMBRIAN_A_FOUNDATIONS.md#05",
               "cheapest_falsifier": "Destructive two-bit parity, every pair separable but no uniform first action wins",
               "limitations": "Finite complete deterministic source and public menus only; no arbitrary infinite grammar decision"},
        "06": {"claim_ids": ["CA06"], "status": "CLASSICAL / PROVED LOCAL",
               "question": "Many observers, common information and fusion",
               "quantifiers": "Any finite family of total reports on one source; every common/fused deterministic target",
               "rival": "Trivial common information or incomplete local states prevents source reconstruction",
               "evidence": common, "proof": "CAMBRIAN_A_FOUNDATIONS.md#06",
               "cheapest_falsifier": "Three coordinate observers; even-parity pairwise-independent source",
               "limitations": "Lag/basis transport, stochastic independence and joint realizability require their own laws"},
    }
    assert result["02"]["evidence"]["diagonal_gates"]["source_lift"]
    assert not result["02"]["evidence"]["diagonal_gates"]["target_lift"]
    assert not result["02"]["evidence"]["same_support_correlated_mutation"]["exact_for_all_old_evidence_and_post_predicates"]
    assert result["06"]["evidence"]["common_classes"] == 1
    assert result["06"]["evidence"]["fused_classes"] == 8
    return {"schema": "succ.cambrian.cluster-A.v1", "base_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
            "python": platform.python_version(), "assignment_count": len(result),
            "researcher_count": 1, "results": result,
            "physical_source_authenticated": False, "RH_proved": False,
            "new_Lean_kernel_proof": False, "academic_novelty_established": False}


def serialize(obj):
    return json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()
    receipt = build_receipt()
    if args.save:
        directory = Path("research/2026-10-13")
        for assignment, result in receipt["results"].items():
            (directory / f"CAMBRIAN_A_{assignment}_RESULT.json").write_text(serialize(result))
        (directory / "CAMBRIAN_A_RECEIPT.json").write_text(serialize(receipt))
        command = ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_cambrian_a_foundations.py", "-v"]
        checked = subprocess.run(command, text=True, capture_output=True)
        code_paths = ("observational_succ/cambrian_a_foundations.py",
                      "tests/test_cambrian_a_foundations.py",
                      "scripts/cambrian_a_foundations_probe.py")
        validation = {"base_sha": receipt["base_sha"], "python": platform.python_version(),
                      "commands": [{"argv": command, "exit_code": checked.returncode,
                                    "stdout": checked.stdout, "stderr": checked.stderr}],
                      "sha256": {path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
                                 for path in code_paths}}
        (directory / "CAMBRIAN_A_VALIDATION.json").write_text(serialize(validation))
        if checked.returncode:
            raise SystemExit(checked.returncode)
    print(serialize(receipt), end="")
