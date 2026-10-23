#!/usr/bin/env python3
"""Compile the standalone Reality Pin proofs and reject calibrated mutations.

Uses the repository-pinned Lean 4.14.0; select an installed binary with
LEAN_BIN or --lean. There is no downloader, runtime patch, or proof admission
in this verifier. An optional runtime note records a host compatibility
workaround, but never changes checker behavior or the success criterion.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import tempfile


PREFIX = "ObservationalSUCC.RealityPin."
STANDARD = ["propext", "Classical.choice", "Quot.sound"]
EXPECTED = {
    PREFIX + "calibrated_source_survives": STANDARD,
    PREFIX + "common_reading_bounds_gap": STANDARD,
    PREFIX + "separated_survivors_are_gauge_equivalent": STANDARD,
    PREFIX + "calibrated_identification_within_declared_family": STANDARD,
    PREFIX + "observer_refinement_shrinks_fiber": [],
    PREFIX + "holdout_rejects_candidate": [],
    PREFIX + "equality_margin_counterexample": [],
    PREFIX + "exact_decoder_requires_observable_invariance": ["Quot.sound"],
    PREFIX + "observable_equivalence": [],
    PREFIX + "hidden_label_counterexample": [],
    PREFIX + "walk_displacement_bound": STANDARD,
    PREFIX + "boundary_return_requires_twice_depth": STANDARD,
    PREFIX + "short_history_cannot_visit_depth_and_return": STANDARD,
    PREFIX + "straight_depth_histories": ["propext", "Quot.sound"],
}


def strip_comments(text: str) -> str:
    """Retain all code; handle nested Lean block comments explicitly."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and text.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif text.startswith("--", i):
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError("Unclosed Lean block comment")
    return "".join(out)


def limits() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (1536 * 1024**2, 1536 * 1024**2))
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))


def axiom_manifest(stdout: str) -> dict[str, list[str]]:
    """Parse multiline #print axioms output and reject other compiler output."""
    pattern = re.compile(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^]]*)\])"
    )
    result = {}
    pos = 0
    for match in pattern.finditer(stdout):
        if stdout[pos : match.start()].strip() or match.group(1) in result:
            raise ValueError("Unexpected compiler output or duplicate declaration")
        result[match.group(1)] = (
            [] if match.group(2) is None else [a.strip() for a in match.group(2).split(",")]
        )
        pos = match.end()
    if stdout[pos:].strip():
        raise ValueError("Unexpected trailing compiler output")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default=os.environ.get("LEAN_BIN", "lean"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--runtime-note", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "formal/RealityPin.lean"
    pin = (root / "lean-toolchain").read_text().strip()
    if pin != "leanprover/lean4:v4.14.0":
        raise ValueError("Reality Pin kernel lane requires the declared 4.14.0 pin")
    version = subprocess.check_output([args.lean, "--version"], text=True, cwd=root).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise ValueError("Installed compiler differs from the repository pin")
    text = source.read_text()
    code = strip_comments(text)
    for forbidden in ("sorry", "admit", "axiom", "unsafe", "native_decide"):
        if re.search(r"\b" + forbidden + r"\b", code):
            raise ValueError("Forbidden proof token: " + forbidden)
    if re.search(r"^\s*import\s", code, re.M):
        raise ValueError("This proof lane is core-only and does not allow imports")
    declared = re.findall(r"^theorem\s+(\w+)", code, re.M)
    if {PREFIX + name for name in declared} != set(EXPECTED) or len(declared) != len(EXPECTED):
        raise ValueError("Every and only declared theorem must receive an exact axiom audit")
    controls = {}
    with tempfile.TemporaryDirectory(prefix="succ-reality-pin-lean-") as temp:
        temp = Path(temp)

        def run(path: Path, output: Path | None = None) -> subprocess.CompletedProcess:
            command = [args.lean] + ([] if output is None else ["-o", str(output)]) + [str(path)]
            return subprocess.run(
                command, cwd=root, text=True, capture_output=True, timeout=65, preexec_fn=limits
            )

        checked = run(source, temp / "RealityPin.olean")
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout + checked.stderr)
        actual = axiom_manifest(checked.stdout)
        if actual != EXPECTED:
            raise ValueError("Exact axiom manifest mismatch: " + repr(actual))

        variants = {
            "false_proposition": "theorem falseControl : False := by decide\n",
            "nonstrict_separation": text.replace(
                "radius m q + radius n q < prediction",
                "radius m q + radius n q ≤ prediction",
            ),
            "false_three_times_depth": text.replace(
                "2 * r ≤ inward + outward", "3 * r ≤ inward + outward"
            ),
        }
        if variants["nonstrict_separation"] == text or variants["false_three_times_depth"] == text:
            raise ValueError("Mutation target missing; controls would be vacuous")
        for name, mutated in variants.items():
            path = temp / (name + ".lean")
            path.write_text(mutated)
            outcome = run(path)
            if outcome.returncode != 1 or "error:" not in outcome.stdout or outcome.stderr:
                raise ValueError("Mutation was not rejected by elaboration: " + name)
            # Location-independent raw diagnostics remain reproducible in receipts.
            controls[name] = {
                "source_sha256": hashlib.sha256(mutated.encode()).hexdigest(),
                "exit_code": outcome.returncode,
                "stdout": outcome.stdout.replace(str(temp), "TEMP"),
                "stderr": outcome.stderr,
            }

    runtime_note = None if args.runtime_note is None else json.loads(args.runtime_note.read_text())
    receipt = {
        "schema": "succ-reality-pin-lean-v1",
        "toolchain": pin,
        "compiler_version": version,
        "source": str(source.relative_to(root)),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exit_code": checked.returncode,
        "declarations": actual,
        "compiler_output": checked.stdout,
        "negative_controls": controls,
        "runtime_note": runtime_note,
        "dynamic_preload_present": bool(os.environ.get("LD_PRELOAD")),
        "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "resource_limits": {"address_space_bytes": 1536 * 1024**2, "cpu_seconds": 60},
        "command": ["lean", "-o", "TEMP/RealityPin.olean", "formal/RealityPin.lean"],
        "scope": "Finite observational selection and nearest-neighbor return budget only; no spectral operator or physical measurement certification.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
