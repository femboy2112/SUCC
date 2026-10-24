#!/usr/bin/env python3
"""Verify the carry-safe Lean kernel: compile, audit axioms, reject a false mutant.

Actual checker execution for formal/CarrySafePolyphase.lean, producing a hashed
JSON receipt. Gates:
  1. no banned tokens (sorry / admit / native_decide / an `axiom` declaration);
  2. the file compiles under the pinned Lean (exit 0);
  3. every theorem's axioms are a subset of the standard kernel set
     {propext, Classical.choice, Quot.sound};
  4. a deliberately false mutation (odx := q*b+r+1) is REJECTED by the checker.

Select the binary with LEAN_BIN or --lean; defaults to `lean` on PATH.
Usage:  python scripts/verify_carry_safe_lean.py [--lean PATH] [--output receipt.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEAN_FILE = REPO / "formal" / "CarrySafePolyphase.lean"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
BANNED = re.compile(r"\b(sorry|admit|native_decide)\b|^\s*axiom\s", re.MULTILINE)
AXIOM_LINE = re.compile(r"'([^']+)' depends on axioms: \[([^\]]*)\]")
THEOREMS = (
    "polyphase_reconstruct", "carry_no_wrap", "carry_wrap",
    "mixed_radix_compose", "fso01_insufficiency",
)


def _lean_bin(cli):
    return cli or os.environ.get("LEAN_BIN") or "lean"


def _strip_comments(text):
    """Remove Lean block (/- -/, /-! -/) and line (--) comments.

    The banned-token scan must flag only real uses, not prose that mentions
    `sorry`/`axiom` to say they are absent.
    """
    text = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
    text = re.sub(r"--[^\n]*", "", text)
    return text


def _compile(lean, path):
    proc = subprocess.run([lean, str(path)], capture_output=True, text=True,
                          timeout=600, cwd=str(REPO))
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean", default=None)
    ap.add_argument("--output", default=str(REPO / "formal" / "carry_safe_lean_receipt.json"))
    args = ap.parse_args()
    lean = _lean_bin(args.lean)

    source = LEAN_FILE.read_text()
    sha = hashlib.sha256(source.encode()).hexdigest()
    receipt = {"file": str(LEAN_FILE.relative_to(REPO)), "sha256": sha,
               "lean": lean, "theorems": {}, "gates": {}}

    # gate 1: banned tokens (scanned on code only, comments stripped)
    banned = [m.group(0).strip() for m in BANNED.finditer(_strip_comments(source))]
    receipt["gates"]["no_banned_tokens"] = not banned
    if banned:
        receipt["banned_hits"] = banned

    # gate 2+3: compile and audit axioms
    rc, out = _compile(lean, LEAN_FILE)
    receipt["gates"]["compiles"] = rc == 0
    found = {name.split(".")[-1]: [a.strip() for a in ax.split(",") if a.strip()]
             for name, ax in AXIOM_LINE.findall(out)}
    all_standard = True
    for thm in THEOREMS:
        axioms = found.get(thm)
        receipt["theorems"][thm] = axioms
        ok = axioms is not None and set(axioms) <= STANDARD_AXIOMS
        all_standard = all_standard and ok
    receipt["gates"]["axioms_standard"] = all_standard
    receipt["gates"]["choice_free"] = all(
        "Classical.choice" not in (found.get(t) or ["Classical.choice"])
        for t in THEOREMS)

    # gate 4: a false mutation must be REJECTED
    mutant = source.replace("def odx (q r b : Nat) : Nat := q * b + r",
                            "def odx (q r b : Nat) : Nat := q * b + r + 1")
    mutated = mutant != source
    with tempfile.TemporaryDirectory() as d:
        mpath = Path(d) / "Mutant.lean"
        mpath.write_text(mutant)
        mrc, _ = _compile(lean, mpath)
    receipt["gates"]["false_mutation_rejected"] = mutated and mrc != 0

    passed = all(receipt["gates"].values())
    receipt["status"] = "PASS" if passed else "FAIL"
    Path(args.output).write_text(json.dumps(receipt, indent=2) + "\n")

    print(json.dumps(receipt["gates"], indent=2))
    print(f"axioms: {receipt['theorems']}")
    print(f"receipt -> {args.output}")
    print(f"STATUS: {receipt['status']}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
