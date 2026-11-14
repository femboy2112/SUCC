#!/usr/bin/env python3
"""Fresh core Lean check of the weighted ancestral theorems, with false controls.

Records the actual declaration types and axiom dependencies printed by the
pinned compiler, and requires two mutated statements to be rejected.  A
successful run certifies the encoded statements only.  It certifies neither a
Python implementation nor that any declared table describes a real source.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

PIN = "leanprover/lean4:v4.14.0"
NAMESPACE = "ObservationalSUCC.ObservatorisQuantale."
THEOREMS = (
    "closed_star",
    "star_closed",
    "star_le_of_closed",
    "star_le_quot_star",
    "push_star_le_quot_star",
    "exactAt_iff_saturated_star_closed",
    "exact_iff_fibreConstant",
    "exact_iff_satClosed",
    "exact_iff_pushClosed",
    "quotAll_star_le_push_star",
    "closure_push_adjunction",
    "closure_push_star_le_quot_star",
    "quot_star_le_closure_push_star",
    "exactAt_iff_closure_push_le",
    "exactAt_map",
    "star_propQ_iff",
)

# The three-state ghost of PAP-04, replayed through the truth-value instance.
GHOST_CONTROL = """
open ObservationalSUCC.ObservatorisQuantale
namespace WeightedGhostControl
inductive Vertex where
  | a | b | c
def edge (x y : Vertex) : Prop := x = .b ∧ y = .c
def report : Vertex → Bool
  | .a => false
  | .b => false
  | .c => true
theorem stays {x z : Vertex} (h : Reach edge x z) : x = .a → z = .a := by
  induction h with
  | refl => intro e; exact e
  | tail _ step ih => intro e; have h2 := ih e; subst h2; cases step.1
theorem observed :
    star propQ (quot propQ edge report) (report .a) true :=
  ⟨_, PathW.tail PathW.refl, True.intro, ⟨_, ⟨.b, .c, rfl, rfl, rfl⟩, rfl, rfl⟩⟩
theorem ghost : ¬ ExactAt propQ edge report .a := by
  intro exact
  cases exact true observed with
  | intro t ht =>
    cases ht with
    | intro hu ht =>
      cases hu with
      | intro u hu =>
        cases hu with
        | intro hq e =>
          subst e
          have h2 := stays ((star_propQ_iff edge .a u).mp ht) rfl
          subst h2
          exact absurd hq (by decide)
end WeightedGhostControl
"""

# The must-side bound is not a may-side bound.
SANDWICH_CONTROL = """
open ObservationalSUCC.ObservatorisQuantale
example {V X Y : Type} (K : LaxQuantale V) (R : X → X → V) (q : X → Y)
    (x : X) (b : Y) :
    K.le (star K (quotAll K R q) (q x) b) (push K q (star K R x) b) :=
  quotAll_star_le_push_star K R q x b
"""

CONTROLS = (
    ("selected-source-ghost", GHOST_CONTROL,
     GHOST_CONTROL.replace("theorem ghost : ¬ ExactAt propQ edge report .a",
                           "theorem ghost : ¬ ExactAt propQ edge report .b")),
    ("must-is-not-may", SANDWICH_CONTROL,
     SANDWICH_CONTROL.replace("star K (quotAll K R q) (q x) b",
                              "star K (quot K R q) (q x) b")),
)


def strip_comments(source: str) -> str:
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


def run(lean: str, path: Path, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([lean, str(path)], cwd=root, text=True,
                          capture_output=True, timeout=120, check=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default=shutil.which("lean") or "lean")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "formal/ObservatorisQuantale.lean"
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
    version = subprocess.check_output([args.lean, "--version"], cwd=root, text=True).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise ValueError("Compiler does not match the pinned Lean release")

    queries = "\n".join(f"#check @{NAMESPACE}{name}\n#print axioms {NAMESPACE}{name}"
                        for name in THEOREMS)
    declarations = []
    controls = []
    with tempfile.TemporaryDirectory(prefix="succ-observatoris-lean-") as directory:
        tmp = Path(directory)
        plain = run(args.lean, source, root)
        if plain.returncode or plain.stdout or plain.stderr:
            raise RuntimeError("Source did not compile silently: " + plain.stdout + plain.stderr)
        export = tmp / "export.lean"
        export.write_text(code + "\n" + queries + "\n")
        checked = run(args.lean, export, root)
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout + checked.stderr)
        blocks = re.split(r"(?m)^(?=@" + re.escape(NAMESPACE) + ")", checked.stdout)
        blocks = [b for b in blocks if b.strip()]
        if len(blocks) != len(THEOREMS):
            raise ValueError("Declaration export count differs from the contract")
        for name, block in zip(THEOREMS, blocks):
            full = NAMESPACE + name
            marker = f"'{full}' does not depend on any axioms"
            if not block.startswith("@" + full + " :") or marker not in block:
                raise ValueError("Missing, misordered or axiom-dependent export: " + name)
            declarations.append({
                "name": full,
                "type": block.split(marker)[0].strip(),
                "axioms": [],
            })
        for name, positive, negative in CONTROLS:
            if positive == negative:
                raise ValueError("Mutation did not modify the control")
            record = {"name": name}
            for label, suffix in (("positive", positive), ("negative", negative)):
                path = tmp / f"{name}-{label}.lean"
                path.write_text(code + "\n" + suffix)
                process = run(args.lean, path, root)
                if label == "positive":
                    if process.returncode or process.stdout or process.stderr:
                        raise RuntimeError("Positive control failed: "
                                           + process.stdout + process.stderr)
                elif (process.returncode != 1 or "error" not in process.stdout
                      or "unexpected token" in process.stdout
                      or "unknown identifier" in process.stdout
                      or "unknown constant" in process.stdout):
                    raise RuntimeError("Mutation was not rejected by a type error: "
                                       + process.stdout + process.stderr)
                record[label] = {
                    "exit_code": process.returncode,
                    "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            record["passed"] = True
            controls.append(record)
    if source.read_bytes() != source_bytes:
        raise RuntimeError("Proof source changed during the kernel check")
    receipt = {
        "status": "KERNEL_CHECKED",
        "scope": ("Encoded statements only; no source authentication, no signed-weight "
                  "claim, no Python implementation is certified."),
        "toolchain": PIN,
        "compiler_version": version,
        "source": str(source.relative_to(root)),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "imports": [],
        "declarations": declarations,
        "controls": controls,
    }
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
