#!/usr/bin/env python3
"""Compile C's actual theorem, then reject a semantically false quantifier mutation.

Only a temporary scratch copy is mutated. The target source remains unchanged.
The stronger conclusion is false for initial={dead,live}, R={(live,live)}.
Compiler failure calibrates the formal checker; it is not a proof of the
counterexample, whose source states and missing dead edge are explicit.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--preload", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    env = dict(os.environ)
    if args.preload:
        env["LD_PRELOAD"] = str(args.preload)
    raw = args.source.read_text()
    source_hash = sha256(args.source.read_bytes()).hexdigest()
    positive = subprocess.run([str(args.lean), str(args.source)], env=env, capture_output=True,
                              text=True, timeout=60)
    assert positive.returncode == 0, positive.stdout + positive.stderr
    assert "sorryAx" not in positive.stdout, "Positive theorem used sorry recovery"
    needle = """    ∃ history : (t : Nat) → S t,
      history 0 ∈ initial ∧ ∀ t, R t (history t) (history (t+1)) := by"""
    replacement = """    ∀ start : S 0, start ∈ initial → ∃ history : (t : Nat) → S t,
      history 0 = start ∧ ∀ t, R t (history t) (history (t+1)) := by"""
    assert raw.count(needle) == 1
    mutant = raw.replace(needle, replacement)
    with tempfile.TemporaryDirectory(prefix="cambrian_audit_a_") as directory:
        path = Path(directory) / "false_every_initial_history.lean"
        path.write_text(mutant)
        negative = subprocess.run([str(args.lean), str(path)], env=env, capture_output=True,
                                  text=True, timeout=60)
    assert negative.returncode != 0, "False quantifier mutant compiled"
    assert source_hash == sha256(args.source.read_bytes()).hexdigest()
    version = subprocess.run([str(args.lean), "--version"], env=env, capture_output=True,
                             text=True, timeout=60)
    result = {"source_sha256": source_hash, "source_path": str(args.source),
              "source_unchanged": True, "compiler_version": version.stdout.strip(),
              "compiler_preload": str(args.preload) if args.preload else None,
              "positive_exit_code": positive.returncode,
              "positive_stdout": positive.stdout, "positive_stderr": positive.stderr,
              "mutant_sha256": sha256(mutant.encode()).hexdigest(),
              "mutation": "exists one initial state replaced by every initial state",
              "expected_countermodel": "initial={dead,live}, only live->live; all finite depths exist but dead has no edge",
              "negative_exit_code": negative.returncode,
              "negative_stdout": negative.stdout, "negative_stderr": negative.stderr,
              "semantically_false_mutant_rejected": True,
              "failed_mutant_sorryAx_is_error_recovery_not_a_pass": "sorryAx" in negative.stdout}
    content = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
