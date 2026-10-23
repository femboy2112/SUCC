#!/usr/bin/env python3
"""Source-bound, UNADMITTED kernel observation for PrimeBridge (Lean 4.14).

The generated JSON records actual compiler success and exported theorem types.
It does not install formal authority in SUCC's trusted catalogue. False claims
are checked as negative elaboration controls, not accepted by source scanning.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ObservationalSUCC.PrimeBridge."
NAMES = [
    "decode_codeword", "decode_encodePair", "encodePair_decode",
    "codeword_gram_count", "singleton_partial_trace_count", "matrix_unit_intertwining_count",
    "singleton_label_alias", "wrong_middle_decoder_receipt",
    "wrong_semigroup_braid_receipt",
    "commuting_reconstructions_force_logical_commutation",
    "mirror_recurrence_along_words",
]
ARCHIVE_SHA256 = "320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a"
NEGATIVES = {
    "wrong_inverse": "example : fsub (share 1 0 2) (share 1 0 0) = (1 : Trit) := by decide\n",
    "wrong_coherence": "example : singletonTraceCount 0 0 1 0 0 = 1 := by decide\n",
    "wrong_braid": "example : (2 : Nat) * (1 + 1) = 2 * 1 + 1 := by decide\n",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default="lean")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    receipt = out / "kernel-observation.json"
    receipt.unlink(missing_ok=True)  # a failed run must not retain success
    env = os.environ.copy()

    def run(label: str, cmd: list[str], *, expected_success: bool = True) -> str:
        process = subprocess.run(cmd, cwd=ROOT, env=env, text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 timeout=240)
        (out / f"{label}.log").write_text(process.stdout)
        if expected_success and process.returncode != 0:
            raise RuntimeError(f"{label} failed ({process.returncode}); see {out / (label + '.log')}")
        if not expected_success:
            if (process.returncode == 0 or
                    "proved that the proposition" not in process.stdout or
                    "is false" not in process.stdout):
                raise RuntimeError(f"{label} did not reject the intended false proposition")
        return process.stdout

    source = ROOT / "formal/PrimeBridge.lean"
    exporter = ROOT / "formal/kernel_audit/ExportCommand.lean"
    # This inexpensive hygiene gate is NOT the proof checker.
    scrubbed = re.sub(r"/\-.*?\-/|--[^\n]*", "", source.read_text(), flags=re.S)
    if re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", scrubbed):
        raise RuntimeError("proof shortcut token in formal source")
    version = run("version", [args.lean, "--version"]).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise RuntimeError(f"unexpected Lean version: {version}")
    with tempfile.TemporaryDirectory(prefix="succ-prime-bridge-") as temp:
        build = Path(temp)
        env["LEAN_PATH"] = str(build)
        run("positive", [args.lean, "--root", str(source.parent), "-o",
                         str(build / "PrimeBridge.olean"), str(source)])
        run("exporter", [args.lean, "--root", str(exporter.parent), "-o",
                         str(build / "ExportCommand.olean"), str(exporter)])
        audit = build / "Audit.lean"
        audit.write_text("import PrimeBridge\nimport ExportCommand\n" + "\n".join(
            f"#check {PREFIX}{name}\n#print axioms {PREFIX}{name}\n#succ_export {PREFIX}{name}"
            for name in NAMES) + "\n")
        # --root declares the source root, not an executable-location workaround.
        exported = run("types", [args.lean, "--root", str(build), str(audit)])
        records = []
        for line in exported.splitlines():
            if "SUCC_THEOREM_JSON " in line:
                record = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
                record["type_sha256"] = hashlib.sha256(record["type_expr"].encode()).hexdigest()
                records.append(record)
        if [r["name"] for r in records] != [PREFIX + n for n in NAMES]:
            raise RuntimeError("theorem export missing, duplicated, or reordered")
        if any(set(r["axioms"]) - {"propext"} for r in records):
            raise RuntimeError("unexpected axiom; only standard propext is permitted")
        for label, statement in NEGATIVES.items():
            control = build / f"{label}.lean"
            control.write_text("import PrimeBridge\nopen ObservationalSUCC.PrimeBridge\n" + statement)
            run(label, [args.lean, "--root", str(build), str(control)], expected_success=False)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    status = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=ROOT, text=True)
    record = {
        "schema": "prime-bridge-kernel-observation-v1",
        "status": "KERNEL_CHECKED_UNADMITTED",
        "formal_authority_admission": "NOT_REQUESTED_NOT_INSTALLED",
        "commit": commit,
        "tracked_worktree_clean": not bool(status.strip()),
        "compiler_version": version,
        "official_archive_sha256_expected": ARCHIVE_SHA256,
        "sources": {str(p.relative_to(ROOT)): sha(p) for p in
                    [source, exporter, Path(__file__), ROOT / "lean-toolchain",
                     ROOT / ".github/workflows/prime-bridge-formal.yml"]},
        "theorems": records,
        "negative_controls_rejected": list(NEGATIVES),
        "logs": {p.name: sha(p) for p in sorted(out.glob("*.log"))},
        "boundary": "Finite code combinatorics, conditional word transport and abstract commutation only; no analytic TFD or Hilbert linear-extension formalization.",
    }
    receipt.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": record["status"], "theorems": len(records),
                      "negative_controls": len(NEGATIVES), "receipt": str(receipt)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
