#!/usr/bin/env python3
"""Fresh pinned core kernel check for the Round II public-belief theorem."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.verify_institute_lean import limits, strip_comments


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "research/2026-10-18/round2/causal_kernel_receipt.json")
    args = parser.parse_args()
    source = ROOT / "formal/round2/PublicBelief.lean"
    manifest_path = ROOT / "research/2026-10-18/round2/causal_axioms.json"
    manifest = json.loads(manifest_path.read_text())
    pin = (ROOT / "lean-toolchain").read_text().strip()
    if pin != "leanprover/lean4:v4.14.0" or manifest["toolchain"] != pin:
        raise ValueError("Unexpected compiler pin")
    version = subprocess.check_output(["lean", "--version"], cwd=ROOT, text=True).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise ValueError("Actual compiler does not match pin")
    code = strip_comments(source.read_text())
    for token in ("sorry", "admit", "axiom", "unsafe", "native_decide"):
        if re.search(r"\b" + token + r"\b", code):
            raise ValueError("Forbidden proof token: " + token)
    if re.search(r"^\s*import\s", code, re.M):
        raise ValueError("Only core Lean allowed")
    prefix = "ObservationalSUCC.Round2.PublicBelief."
    named = {prefix + n for n in re.findall(r"^theorem\s+(\w+)", code, re.M)}
    printed = re.findall(r"^#print axioms\s+(\S+)", code, re.M)
    if named != set(manifest["declarations"]) or set(printed) != named or len(printed) != len(named):
        raise ValueError("Every public theorem must be declared and audited exactly once")
    with tempfile.TemporaryDirectory(prefix="succ-round2-causal-") as tmp:
        tmp = Path(tmp)
        negative = tmp / "FalseControl.lean"
        negative.write_text("theorem falseControl : False := by decide\n")
        bad = subprocess.run(["lean", str(negative)], cwd=ROOT, capture_output=True,
                             text=True, timeout=65, preexec_fn=limits)
        if (bad.returncode != 1 or bad.stderr or
                "tactic 'decide' proved that the proposition\n  False\nis false" not in bad.stdout):
            raise ValueError("Negative kernel control failed calibration")
        command = ["lean", "-o", str(tmp / "PublicBelief.olean"), str(source)]
        checked = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                 timeout=65, preexec_fn=limits)
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout + checked.stderr)
        observed = {}
        for line in checked.stdout.splitlines():
            empty = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
            used = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]", line)
            match = empty or used
            if match is None or match.group(1) in observed:
                raise ValueError("Unexpected compiler output: " + line)
            observed[match.group(1)] = [] if empty else [v.strip() for v in used.group(2).split(",")]
        if observed != manifest["declarations"]:
            raise ValueError("Actual axiom report differs from manifest")
        receipt = dict(toolchain=pin, compiler_version=version,
                       source=str(source.relative_to(ROOT)),
                       source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                       manifest=str(manifest_path.relative_to(ROOT)),
                       manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                       command=command, cwd=str(ROOT), exit_code=checked.returncode,
                       negative_control_exit_code=bad.returncode, negative_control_output=bad.stdout,
                       compiler_output=checked.stdout, declarations=observed,
                       checked_utc=datetime.now(timezone.utc).isoformat(),
                       resource_limits=dict(address_space_bytes=1024**3, cpu_seconds=60))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "declarations": len(observed),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
