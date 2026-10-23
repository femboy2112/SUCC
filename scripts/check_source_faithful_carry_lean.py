#!/usr/bin/env python3
"""Check the pinned finite carry core, export theorem expressions, kill mutants.

The verifier never downloads or modifies a compiler. LEAN_BIN / --lean select
an installed Lean 4.14.0 executable. A disclosed optional runtime note describes
host compatibility only; clean hosted CI executes without dynamic preloads.
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

PREFIX = "ObservationalSUCC.SourceFaithfulCarry."
PQ = ["propext", "Quot.sound"]
EXPECTED = {
    "source_reconstruction": PQ,
    "residue_bound": [],
    "coordinates_of_encoding": ["propext"],
    "no_carry_successor": PQ,
    "terminal_carry_successor": PQ,
    "authentic_multiplier_terminal": PQ,
    "affine_successor": [],
    "mixed_radix_address": PQ,
    "triple_address_coherence": PQ,
    "decoded_no_carry": PQ,
    "decoded_terminal_carry": PQ,
    "binary_quotient_failure": [],
    "binary_quotient_has_no_successor": [],
    "distinct_digits_have_finite_witness": PQ,
    "finite_quotient_transcript_injective": PQ,
    "quotient_horizon_sharp": PQ,
    "exact_successor_quotient_compression_injective": PQ,
    "future_refines_present": [],
    "future_stable": [],
    "future_equivalence": [],
    "coarsest_future_safe_refinement": [],
    "exact_compression_preserves_futures": [],
}
EXPECTED = {PREFIX + name: axioms for name, axioms in EXPECTED.items()}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strip_comments(text: str) -> str:
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


def parse_axioms(stdout: str) -> dict[str, list[str]]:
    pattern = re.compile(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^]]*)\])"
    )
    result, end = {}, 0
    for match in pattern.finditer(stdout):
        if stdout[end : match.start()].strip() or match.group(1) in result:
            raise ValueError("Unexpected compiler output or duplicate declaration")
        result[match.group(1)] = (
            [] if match.group(2) is None else [a.strip() for a in match.group(2).split(",")]
        )
        end = match.end()
    if stdout[end:].strip():
        raise ValueError("Unexpected trailing compiler output")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default=os.environ.get("LEAN_BIN", "lean"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--runtime-note", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "formal/SourceFaithfulCarry.lean"
    export_helper = root / "formal/kernel_audit/ExportCommand.lean"
    pin = (root / "lean-toolchain").read_text().strip()
    if pin != "leanprover/lean4:v4.14.0":
        raise ValueError("Finite carry lane requires the declared 4.14.0 pin")
    version = subprocess.check_output([args.lean, "--version"], text=True, cwd=root).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise ValueError("Installed compiler differs from repository pin")
    text = source.read_text()
    helper = export_helper.read_text()
    code = strip_comments(text)
    for forbidden in ("sorry", "admit", "axiom", "unsafe", "native_decide"):
        if re.search(r"\b" + forbidden + r"\b", code):
            raise ValueError("Forbidden proof token: " + forbidden)
    if re.search(r"^\s*import\s", code, re.M):
        raise ValueError("The proof source is core-only; only the exporter imports Lean")
    declared = re.findall(r"^theorem\s+(\w+)", code, re.M)
    if {PREFIX + name for name in declared} != set(EXPECTED) or len(declared) != len(EXPECTED):
        raise ValueError("Every and only declared theorem must be audited")

    with tempfile.TemporaryDirectory(prefix="succ-carry-lean-") as temp_name:
        temp = Path(temp_name)

        def run(name: str, contents: str, output: bool = False) -> subprocess.CompletedProcess:
            path = temp / (name + ".lean")
            path.write_text(contents)
            command = [args.lean]
            if output:
                command += ["-o", str(temp / (name + ".olean"))]
            command += [str(path)]
            return subprocess.run(command, cwd=temp, text=True, capture_output=True,
                                  timeout=65, preexec_fn=limits)

        checked = run("SourceFaithfulCarry", text, True)
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout + checked.stderr)
        actual = parse_axioms(checked.stdout)
        if actual != EXPECTED:
            raise ValueError("Exact axiom manifest mismatch: " + repr(actual))

        # Re-elaborate the exact same source snapshot with only its print commands
        # removed, then inspect kernel theorem ConstantInfo rather than labels.
        audit_source = re.sub(r"^#print axioms .*\n?", "", text, flags=re.M)
        export_text = helper + "\n" + audit_source + "\n" + "\n".join(
            "#succ_export " + name for name in EXPECTED
        ) + "\n"
        exported = run("CarryExpressions", export_text)
        if exported.returncode or exported.stderr:
            raise RuntimeError(exported.stdout + exported.stderr)
        expressions = {}
        for line in exported.stdout.splitlines():
            if not line.startswith("SUCC_THEOREM_JSON "):
                raise ValueError("Unexpected expression-export output: " + line)
            entry = json.loads(line.removeprefix("SUCC_THEOREM_JSON "))
            name = entry["name"]
            if name not in EXPECTED or name in expressions:
                raise ValueError("Unexpected or duplicate expression export")
            if sorted(entry["axioms"]) != sorted(EXPECTED[name]) or not entry["type_expr"]:
                raise ValueError("Expression export has wrong dependencies or empty type")
            expressions[name] = entry
        if set(expressions) != set(EXPECTED):
            raise ValueError("Missing theorem expressions")

        replacements = {
            "wrong_terminal_origin": (
                "a * n = encode a (n - 1) (a - 1)",
                "a * n = encode a (n - 1) 0"),
            "quotient_commutes_with_successor": (
                "quotient 2 (1 + 1) ≠ quotient 2 (2 + 1)",
                "quotient 2 (1 + 1) = quotient 2 (2 + 1)"),
            "incorrect_mixed_radix_weight": (
                "encode (a * b) q (a * s + r)",
                "encode (a * b) q (b * s + r)"),
            "shortened_separation_horizon": (
                "same : ∀ t, t ≤ a - 1 → quotient a (n + t) = quotient a (m + t)",
                "same : ∀ t, t < a - 1 → quotient a (n + t) = quotient a (m + t)"),
        }
        variants = {"false_proposition": "theorem falseControl : False := by decide\n"}
        for name, (before, after) in replacements.items():
            if text.count(before) != 1:
                raise ValueError("Mutation target absent or not unique: " + name)
            variants[name] = text.replace(before, after)
        controls = {}
        for name, mutated in variants.items():
            outcome = run(name, mutated)
            if outcome.returncode != 1 or "error:" not in outcome.stdout or outcome.stderr:
                raise ValueError("Mutation was not rejected by elaboration: " + name)
            controls[name] = {
                "source_sha256": digest(mutated.encode()),
                "exit_code": outcome.returncode,
                "stdout": outcome.stdout.replace(str(temp), "TEMP"),
                "stderr": outcome.stderr,
            }

    runtime_note = None if args.runtime_note is None else json.loads(args.runtime_note.read_text())
    receipt = {
        "schema": "succ-source-faithful-carry-lean-v1",
        "toolchain": pin,
        "compiler_version": version,
        "source": str(source.relative_to(root)),
        "source_sha256": digest(text.encode()),
        "verifier_sha256": digest(Path(__file__).read_bytes()),
        "export_helper": str(export_helper.relative_to(root)),
        "export_helper_sha256": digest(helper.encode()),
        "expression_audit_source_sha256": digest(export_text.encode()),
        "exit_code": checked.returncode,
        "declarations": actual,
        "theorem_expressions": expressions,
        "compiler_output": checked.stdout,
        "negative_controls": controls,
        "runtime_note": runtime_note,
        "dynamic_preload_present": bool(os.environ.get("LD_PRELOAD")),
        "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "resource_limits": {"address_space_bytes": 1536 * 1024**2, "cpu_seconds": 60},
        "scope": "One-based finite carry, mixed-radix address coherence, sharp quotient observation horizon and deterministic future-safe refinement; no Hilbert, analytic, physical, or signed arithmetic certification.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"declarations": len(actual), "rejected_mutations": len(controls),
                      "toolchain": pin, "source_sha256": receipt["source_sha256"],
                      "dynamic_preload_present": receipt["dynamic_preload_present"],
                      "receipt": None if args.output is None else str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
