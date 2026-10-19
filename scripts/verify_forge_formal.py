#!/usr/bin/env python3
"""Build pinned PR178/179 interfaces, checked adapters and game certificates.

Uses an isolated temporary Lean module path. The two historical dependencies
are content pinned; the copied PR178 file is the only selectively reused source.
No compiler installation or repository mutation is performed by this checker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL = {
    "FutureSafeForgetting": {
        "path": "formal/FutureSafeForgetting.lean",
        "commit": "81684b4b8956f9f5da56c376ba7e4339277eb665",
        "origin_path": "formal/FutureSafeForgetting.lean",
        "git_blob": "b0b1a395de924f343777da728fb56fdb1a558c32",
        "sha256": "986609101f0efafdf56453edc6da4919971ad00f34d4d76b417ecb234cd087f6",
    },
    "InstituteCausal": {
        "path": "research/2026-10-19/formal_inputs/InstituteCausal.PR178.lean",
        "commit": "e42096ec0186228dd0f748767599e470f2ca2e1d",
        "origin_path": "formal/InstituteCausal.lean",
        "git_blob": "360ba66fc1a271d2411fb7c7a0942e350b9fa8ad",
        "sha256": "7d88fe4123e07d0b5776f229d82c4b1ab593435bbe62fa1106d50fadf53016fc",
    },
}
EXPECTED = {
    "FutureSafeForgetting": {
        "fiber_safe_iff_descent": [], "descended_structure_unique": [],
        "finite_trace_preserved": ["propext"], "availability_reflected": ["propext"],
        "quotient_step_lifts_from_each_representative": [],
        "quotient_path_lifts_from_each_representative": ["propext"],
    },
    "InstituteCausal": {
        "quotient_exists_iff_fiber_congruent": ["Classical.choice"],
        "run_naturality": [], "every_representative_lifts": ["propext"],
        "lawful_quotient_iff": ["propext", "Classical.choice"],
        "path_preserves_source": [], "reachable_iff_single_source_path": ["propext"],
        "exclusion_refutes_path": [], "no_path_iff_excluded": [],
    },
    "ForgeQuotientAdapters": {
        "swap_involutive": [], "swap_injective": [], "project_adapt": [],
        "fiber_safe_iff_label_congruence": [], "successful_run_compatibility": [],
        "label_congruence_does_not_preserve_current_report": [],
        "failed_runs_can_hide_different_traces": ["propext", "Quot.sound"],
    },
    "ForgeGameCertificates": {
        "positive_policy_is_lawful": [], "lawful_path_preserves_origin": [],
        "adversary_run_shorter_than_rank": [], "ranked_certificate_forces_finite_failure": [],
        "positive_and_ranked_regions_disjoint": [],
        "alternating_adversary_run_shorter_than_rank": [],
        "alternating_ranked_forces_finite_failure": [], "alternating_certificates_disjoint": [],
    },
}


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def uncomment(source):
    out, i, depth = [], 0, 0
    while i < len(source):
        if source.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and source.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif source.startswith("--", i):
            end = source.find("\n", i)
            i = len(source) if end == -1 else end
        else:
            out.append(source[i])
            i += 1
    require(depth == 0, "unclosed comment")
    return "".join(out)


def check_output(module, stdout):
    rows = {}
    prefix = "ObservationalSUCC." + module + "."
    for line in stdout.splitlines():
        empty = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
        nonempty = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]", line)
        m = empty or nonempty
        require(m is not None and m[1].startswith(prefix), "unexpected output: " + line)
        name = m[1][len(prefix):]
        require(name not in rows, "duplicate axiom report")
        rows[name] = [] if empty else [s.strip() for s in m[2].split(",")]
    require(rows == EXPECTED[module], f"exact axiom mismatch for {module}: {rows}")
    return rows


def audit(lean):
    require((ROOT / "lean-toolchain").read_text().strip() == "leanprover/lean4:v4.14.0",
            "root toolchain pin changed")
    version = subprocess.run([lean, "--version"], text=True, capture_output=True, check=True,
                             timeout=30).stdout.strip()
    require(version.startswith("Lean (version 4.14.0,"), "incorrect compiler version")
    receipt = {"compiler": version, "historical_inputs": HISTORICAL,
               "modules": {}, "controls": {}, "kernel_checks_are_actual": True,
               "algorithms_formalized": False, "public_belief_compiler_formalized": False}
    with tempfile.TemporaryDirectory(prefix="succ-forge-lean-") as temp:
        tmp = Path(temp)
        env = dict(os.environ, LEAN_PATH=str(tmp))
        for module in EXPECTED:
            source = ROOT / (HISTORICAL[module]["path"] if module in HISTORICAL
                             else "formal/" + module + ".lean")
            raw = source.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            if module in HISTORICAL:
                blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                require(digest == HISTORICAL[module]["sha256"] and
                        blob == HISTORICAL[module]["git_blob"], "historical source changed")
            code = uncomment(raw.decode())
            require(not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", code),
                    "forbidden proof token in " + module)
            imports = re.findall(r"^\s*import\s+([^\n]+)", code, re.M)
            require(imports == (["FutureSafeForgetting", "InstituteCausal"]
                                if module == "ForgeQuotientAdapters" else []),
                    "unapproved imports in " + module)
            local = tmp / (module + ".lean")
            shutil.copyfile(source, local)
            run = subprocess.run([lean, "-DwarningAsError=true", "-o",
                                  str(local.with_suffix(".olean")), str(local)],
                                 cwd=tmp, env=env, text=True, capture_output=True, timeout=120)
            require(run.returncode == 0 and not run.stderr, run.stdout + run.stderr)
            rows = check_output(module, run.stdout)
            receipt["modules"][module] = {"sha256": digest, "exit": run.returncode,
                                          "axioms": rows, "stdout": run.stdout}

        common = """import ForgeGameCertificates
open ObservationalSUCC.ForgeGameCertificates
def trap : AlternatingGame Bool Unit Unit := {
  requested := fun _ _ => True
  enabled := fun _ _ _ => True
  outcome := fun _ _ _ _ => True }
"""
        controls = {
            "positive_all_outcomes": (common +
                "example : AlternatingPositive trap (fun _ => True) (fun _ _ => ()) := by\n  intro s hs r hr\n  exact ⟨True.intro, ⟨false, True.intro⟩, fun _ _ => True.intro⟩\n", True),
            "false_proposition": ("example : False := by decide\n", False),
            "existential_outcome_is_not_universal": (common +
                "example : AlternatingPositive trap (fun s => s = false) (fun _ _ => ()) := by\n  intro s hs r hr\n  refine ⟨True.intro, ⟨false, True.intro⟩, ?_⟩\n  intro t ht\n  cases t\n  · rfl\n  · decide\n", False),
            "nonstrict_rank_cannot_force_failure": (
                "example : (1 : Nat) < 1 := by decide\n", False),
            "lost_current_report": ("example : false = true := by decide\n", False),
        }
        for name, (source, accepted) in controls.items():
            local = tmp / (name + ".lean")
            local.write_text(source)
            result = subprocess.run([lean, str(local)], cwd=tmp, env=env,
                                    text=True, capture_output=True, timeout=60)
            if accepted:
                require(result.returncode == 0 and not result.stderr, result.stdout + result.stderr)
            else:
                require(result.returncode == 1 and
                        "tactic 'decide' proved that the proposition" in result.stdout and
                        "is false" in result.stdout, result.stdout + result.stderr)
            receipt["controls"][name] = {"expected_acceptance": accepted,
                                          "exit": result.returncode,
                                          "source": source, "stdout": result.stdout}
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default="lean")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = audit(args.lean)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "KERNEL_ACCEPTED_WITH_EXACT_AXIOMS",
                      "historical_declarations": 14, "new_declarations": 15,
                      "positive_controls": 1, "rejected_false_controls": 4,
                      "compiler": receipt["compiler"]}, sort_keys=True))


if __name__ == "__main__":
    main()
