#!/usr/bin/env python3
"""Fresh core Lean check of ancestral transport, with paired false-rule controls.

This records actual declaration types and axiom dependencies.  It does not
certify the historical comparison or any Python implementation.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import resource
import subprocess
import tempfile


PIN = "leanprover/lean4:v4.14.0"
NAMESPACE = "ObservationalSUCC.PrincipiaAncestral."
THEOREMS = (
    "reach_preserves",
    "reach_iff_hereditary",
    "reach_maps",
    "quotient_reach_forward",
    "selected_endpoint_exact_iff_saturated_reach_closed",
    "endpoint_exact_iff_saturation_closed",
    "endpoint_exact_iff_same_reachable_reports",
    "closed_invariant_excludes_report",
    "invariant_refutes_endpoint_exact",
)

HEREDITARY_CONTROL = """
open ObservationalSUCC.PrincipiaAncestral
example {X : Type} (R : X → X → Prop) (P : X → Prop)
    (x y : X) (path : Reach R x y) (initial : P x)
    (closed : ForwardClosed R P) : P y :=
  reach_preserves path P closed initial
"""

GHOST_CONTROL = """
open ObservationalSUCC.PrincipiaAncestral
namespace GhostControl
inductive Vertex where
  | a | b | c
  deriving DecidableEq
def edge (x y : Vertex) : Prop := x = .b ∧ y = .c
def report : Vertex → Bool
  | .a => false
  | .b => false
  | .c => true
def invariant (x : Vertex) : Prop := x = .a
theorem closed : ForwardClosed edge invariant := by
  intro x y atA step
  cases atA
  cases step.1
theorem excludes : ∀ y, invariant y → report y ≠ true := by
  intro y atA
  cases atA
  decide
theorem observed : Reach (QuotientEdge edge report) (report .a) true :=
  Reach.tail (Reach.refl _) ⟨.b, .c, rfl, rfl, rfl, rfl⟩
example : ¬ EndpointExact edge report :=
  invariant_refutes_endpoint_exact edge report invariant .a true
    closed rfl excludes observed
end GhostControl
"""


def strip_comments(source: str) -> str:
    """Remove nested Lean block comments and line comments for token guards."""
    out: list[str] = []
    i = depth = 0
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
            i = len(source) if end < 0 else end
        else:
            out.append(source[i])
            i += 1
    if depth:
        raise ValueError("Unclosed Lean comment")
    return "".join(out)


def limits() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))


def run(command: list[str], root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=root, text=True, capture_output=True,
                          timeout=35, preexec_fn=limits, check=False)


def exports(stdout: str) -> dict[str, dict]:
    """Associate each actual #check type with its actual #print axioms output."""
    result: dict[str, dict] = {}
    current: str | None = None
    lines: list[str] = []
    for line in stdout.splitlines():
        if line.startswith(NAMESPACE):
            if current is not None:
                raise ValueError("Missing axiom output before next declaration")
            current = line.split(".{", 1)[0].split(" ", 1)[0]
            lines = [line]
        elif line.startswith("'"):
            match = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
            if (match is None or match.group(1) != current
                    or current in result):
                raise ValueError("Nonempty, mismatched, or duplicate axiom output")
            result[current] = {"type": "\n".join(lines), "axioms": []}
            current = None
            lines = []
        elif current is not None and line.startswith("  "):
            lines.append(line)
        else:
            raise ValueError("Unexpected compiler output: " + line)
    if current is not None or tuple(result) != tuple(NAMESPACE + n for n in THEOREMS):
        raise ValueError("Declaration export set/order differs from the contract")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "formal/PrincipiaAncestral.lean"
    source_bytes = source.read_bytes()
    code = source_bytes.decode("utf-8")
    stripped = strip_comments(code)
    if (root / "lean-toolchain").read_text().strip() != PIN:
        raise ValueError("Unexpected repository Lean toolchain pin")
    for token in ("sorry", "admit", "axiom", "unsafe", "native_decide"):
        if re.search(r"\b" + token + r"\b", stripped):
            raise ValueError("Forbidden proof token: " + token)
    if re.search(r"^\s*import\s", stripped, re.M):
        raise ValueError("This core-only proof lane does not allow imports")
    version = subprocess.check_output(["lean", "--version"], cwd=root, text=True).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise ValueError("Compiler does not match the pinned Lean release")

    with tempfile.TemporaryDirectory(prefix="succ-principia-lean-") as directory:
        tmp = Path(directory)
        checked = run(["lean", "-o", str(tmp / "PrincipiaAncestral.olean"),
                       str(source)], root)
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout + checked.stderr)
        declarations = exports(checked.stdout)
        controls = []
        for name, positive, negative in (
            ("hereditary-premise", HEREDITARY_CONTROL,
             HEREDITARY_CONTROL.replace("(closed : ForwardClosed R P)", "(closed : True)")),
            ("selected-source-ghost", GHOST_CONTROL,
             GHOST_CONTROL.replace("example : ¬ EndpointExact edge report :=",
                                   "example : EndpointExact edge report :=")),
        ):
            if positive == negative:
                raise ValueError("Mutation did not modify the control")
            records = {}
            for label, suffix in (("positive", positive), ("negative", negative)):
                path = tmp / (name + "-" + label + ".lean")
                path.write_text(code + "\n" + suffix)
                process = run(["lean", str(path)], root)
                if label == "positive":
                    if process.returncode or process.stderr:
                        raise RuntimeError("Positive control failed: " + process.stdout + process.stderr)
                    if exports(process.stdout) != declarations:
                        raise ValueError("Control source altered the theorem exports")
                elif (process.returncode != 1 or process.stderr
                      or "type mismatch" not in process.stdout
                      or "unexpected token" in process.stdout
                      or "unknown identifier" in process.stdout):
                    raise RuntimeError("Mutation was not rejected by the expected type check: "
                                       + process.stdout + process.stderr)
                records[label] = {
                    "exit_code": process.returncode,
                    "compiler_output": process.stdout.replace(str(tmp), "TEMP"),
                    "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            controls.append({"name": name, "passed": True, **records})
    unchanged = source.read_bytes() == source_bytes
    if not unchanged:
        raise RuntimeError("Proof source changed during the kernel check")
    record = {
        "status": "KERNEL_CHECKED",
        "toolchain": PIN,
        "compiler_version": version,
        "source": str(source.relative_to(root)),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_unchanged": unchanged,
        "theorem_exports": declarations,
        "paired_controls": controls,
        "compiler_output": checked.stdout,
        "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "resource_limits": {"address_space_bytes": 1024**3, "cpu_seconds": 30},
        "command": ["lean", "-o", "TEMP/PrincipiaAncestral.olean", str(source.relative_to(root))],
        "authority_boundary": "Core endpoint reachability only; no trace, distribution, or pi-normality theorem",
    }
    rendered = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
