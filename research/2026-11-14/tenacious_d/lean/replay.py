"""Replay Fable's pinned verifier and audit the actual cross-module Lean bridge."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compiled(argv, cwd, env, expected=0):
    output = subprocess.run(argv, cwd=cwd, env=env, capture_output=True,
                            text=True, timeout=120)
    if output.returncode != expected or output.stderr:
        raise RuntimeError(f"{argv}: exit {output.returncode}\n{output.stdout}{output.stderr}")
    return output.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default="lean")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    lean = shutil.which(args.lean)
    if lean is None:
        raise RuntimeError(f"Lean unavailable: {args.lean}")
    lean = str(Path(lean).resolve())
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    sources = {
        "ObservatorisQuantale": root / "formal/ObservatorisQuantale.lean",
        "FutureSafeForgetting": root / "formal/FutureSafeForgetting.lean",
        "ObserverBridge": here / "ObserverBridge.lean",
    }
    version = subprocess.check_output([lean, "--version"], text=True).strip()
    if not version.startswith("Lean (version 4.14.0,"):
        raise RuntimeError(f"wrong compiler: {version}")
    pin = (root / "lean-toolchain").read_text().strip()
    if pin != "leanprover/lean4:v4.14.0":
        raise RuntimeError(f"wrong repository pin: {pin}")

    fable_receipt = out / "fable_kernel.json"
    verifier = root / "scripts/check_observatoris_lean.py"
    old = root / "research/2026-11-14/principia_observatoris_second_forge/receipts/lean-kernel.json"
    compiled([sys.executable, str(verifier), "--lean", lean,
              "--output", str(fable_receipt)], root, os.environ.copy())
    if fable_receipt.read_bytes() != old.read_bytes():
        raise RuntimeError("Fable's replay receipt differs from the inherited bytes")
    contract = json.loads(fable_receipt.read_text())
    output_lines = []
    imports = {name: re.findall(r"^import (\w+)$", path.read_text(), re.M)
               for name, path in sources.items()}
    if imports != {"ObservatorisQuantale": [], "FutureSafeForgetting": [],
                   "ObserverBridge": ["FutureSafeForgetting", "ObservatorisQuantale"]}:
        raise RuntimeError(f"unexpected import closure: {imports}")

    namespaces = {"ObservatorisQuantale": "ObservationalSUCC.ObservatorisQuantale.",
                  "FutureSafeForgetting": "ObservationalSUCC.FutureSafeForgetting.",
                  "ObserverBridge": "ObservationalSUCC.TenaciousBridge."}
    decls = {}
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        env = {**os.environ, "LEAN_PATH": str(work)}
        for name, path in sources.items():
            src = work / (name + ".lean")
            shutil.copyfile(path, src)
            raw = compiled([lean, "-o", name + ".olean", src.name], work, env)
            if "warning:" in raw or "error:" in raw:
                raise RuntimeError(raw)
            output_lines.append(f"$ lean -o {name}.olean {src.name}\n{raw}")
            names = re.findall(r"^(?:structure|def|inductive|theorem)\s+(\w+)",
                               src.read_text(), re.M)
            decls[name] = [namespaces[name] + n for n in names]
        lines = ["import ObserverBridge", ""]
        for names in decls.values():
            lines.extend("#print axioms " + n for n in names)
        for n in decls["ObserverBridge"]:
            lines.append("#check @" + n)
        (work / "Declarations.lean").write_text("\n".join(lines) + "\n")
        raw = compiled([lean, "Declarations.lean"], work, env)
        deps = {}
        for n in (n for group in decls.values() for n in group):
            empty = f"'{n}' does not depend on any axioms"
            other = re.search(r"^'" + re.escape(n) + r"' depends on axioms: \[([^\]]*)\]$",
                              raw, re.M)
            if empty in raw:
                deps[n] = []
            elif other:
                deps[n] = [a.strip() for a in other[1].split(",")]
            else:
                raise RuntimeError(f"missing axiom output: {n}")
        if any(deps[n] for n in decls["ObservatorisQuantale"]):
            raise RuntimeError("unexpected Fable axiom dependency")
        bridge = decls["ObserverBridge"]
        expected = {n: (["propext"] if n.endswith("endpointExact_and_wordLift") else [])
                    for n in bridge}
        if {n: deps[n] for n in bridge} != expected:
            raise RuntimeError("bridge axiom profile changed")
        output_lines.append("$ lean Declarations.lean\n" + raw)

        # Rejected bridge statement has an explicitly proved negation.
        base = ("import ObserverBridge\nopen ObservationalSUCC.TenaciousBridge\n"
                "def MissingField := inhabitedRight.le "
                "(inhabitedRight.mul inhabitedRight.one (fun i => i = true)) "
                "(fun i => i = true)\n")
        controls = [("positive", base + "example : ¬ MissingField := left_unit_can_expand\n", 0),
                    ("negative", base + "example : MissingField := left_unit_can_expand\n", 1)]
        mutation_results = {}
        for name, code, rc in controls:
            path = work / f"{name}.lean"
            path.write_text(code)
            msg = compiled([lean, path.name], work, env, expected=rc)
            if (rc and "type mismatch" not in msg) or (not rc and msg):
                raise RuntimeError(msg)
            mutation_results[name] = {"exit": rc, "source_sha256": sha256(path)}
            output_lines.append(f"$ lean {path.name} [exit {rc}]\n{msg}")
    (out / "compiler.log").write_text("\n".join(output_lines))
    summary = {
        "version": version, "pin": pin,
        "module_sha256": {n: sha256(p) for n, p in sources.items()},
        "module_imports": imports,
        "fable_checker_sha256": sha256(verifier),
        "fable_replay_sha256": sha256(fable_receipt),
        "fable_replay_byte_equal": True,
        "fable_contract_exports": len(contract["declarations"]),
        "fable_mutation_pairs": len(contract["controls"]),
        "named_declarations_per_module": {n: len(v) for n, v in decls.items()},
        "axioms_by_named_declaration": deps,
        "left_unit_countermodel_controls": mutation_results,
        "authority": "Pinned local compilation of the listed source bytes",
    }
    (out / "audit.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: summary[k] for k in (
        "version", "fable_contract_exports", "fable_mutation_pairs",
        "named_declarations_per_module", "fable_replay_byte_equal")}, sort_keys=True))


if __name__ == "__main__":
    main()
