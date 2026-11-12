"""Serial pinned Lean check of ZSCCarryFlux.lean: exports, axioms and mutant controls.

Kernel-checks small exact lemmas of
research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md (ZSC-06(d) null relation,
ZSC-02 locality lemma, ZSC-03 renewal lemma) against the repository's pinned toolchain
(leanprover/lean4:v4.14.0) and mathlib pin (formal/mathlib_bridge/lake-manifest.json).

--dependency-project may point to an existing compatible build of the bridge (a prebuilt
copy of formal/mathlib_bridge). Its package sources and revisions are verified
against the manifest before read-only use; nothing is rebuilt. This produces a local
observation, not an admission into the historical authority catalogue.

Each mutant control has three legs, all required:
  positive  the exact closed statement P compiles from the theorem;
  mutant    the mechanically mutated statement P' (one exact substring replacement in P)
            does NOT compile from the same theorem (semantic "type mismatch", no
            infrastructure error) -- the repository's paired-control convention;
  refuted   the negation of P' compiles from the `refute_*` theorem of the module, so P'
            is kernel-checked FALSE, not merely unproved.

No BBP series identity, Baker rigidity, statistical, Diophantine or asymptotic statement of
the dossier is certified, and no claim about pi is made.
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
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PROJECT = ROOT / "formal/mathlib_bridge"
SOURCE = HERE / "ZSCCarryFlux.lean"
MODULE = "ZSCCarryFlux"
NAMESPACE = "ObservationalSUCC.ZSCCarryFlux"
DOSSIER = ROOT / "research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md"
EXPORT_COMMAND = ROOT / "formal/kernel_audit/ExportCommand.lean"
PIN = "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84"
TOOLCHAIN = "leanprover/lean4:v4.14.0"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
FORBIDDEN = r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by|extern)\b"
INFRASTRUCTURE = ("unknown module", "unknown constant", "unknown identifier",
                  "unexpected token", "unknown namespace", "deterministic timeout",
                  "maximum recursion")

# (label, theorem, proof term, closed statement P, exact substring of P, replacement,
#  refutation theorem proving the negation of the mutated statement).
CONTROLS = (
    ("partial-fraction-sign", "zsc06_null_partial_fraction",
     "fun z h1 h2 => zsc06_null_partial_fraction z h1 h2",
     "∀ z : ℚ, z ^ 2 - 2 ≠ 0 → z ^ 2 - 2 * z + 2 ≠ 0 → "
     "(z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) = "
     "z / (z ^ 2 - 2) - (z - 1) / (z ^ 2 - 2 * z + 2)",
     "= z / (z ^ 2 - 2) - (z - 1)", "= z / (z ^ 2 - 2) + (z - 1)",
     "refute_partial_fraction_sign_flip"),
    ("null-numerator-coefficient", "zsc06_null_numerator", "zsc06_null_numerator",
     "((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (X ^ 2 - 4 * X + 2 : ℚ[X]) = "
     "8 - 8 * X - 4 * X ^ 2 - 8 * X ^ 3 - 2 * X ^ 4 - 2 * X ^ 5 + X ^ 6",
     "- 8 * X ^ 3", "+ 8 * X ^ 3",
     "refute_null_numerator_coefficient"),
    ("sixteen-factorisation", "zsc06_sixteen_factorisation", "zsc06_sixteen_factorisation",
     "(16 - X ^ 8 : ℚ[X]) = "
     "((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * ((2 - X ^ 2) * (X ^ 2 - 2 * X + 2))",
     "((2 - X ^ 2)", "((2 + X ^ 2)",
     "refute_sixteen_factorisation"),
    ("null-integral-numerator", "zsc06_null_integral", "zsc06_null_integral",
     "∫ z in (0:ℝ)..1, (z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) = 0",
     "4 * z + 2) /", "4 * z + 3) /",
     "refute_null_integral_numerator"),
    ("locality-change-threshold", "zsc02_locality_change", "zsc02_locality_change",
     "∀ (ξ : ℝ) (n : ℕ), |15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| < 1 / 256 → "
     "hexDigit ξ n = hexDigit ξ (n + 1)",
     "< 1 / 256", "< 1 / 200",
     "refute_locality_change_threshold"),
    ("locality-run-constant", "zsc02_locality_run", "zsc02_locality_run",
     "∀ (ξ : ℝ) (n k : ℕ), (∀ i < k, hexDigit ξ (n + i) = hexDigit ξ n) → "
     "|15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| ≤ 15 / 16 ^ k",
     "≤ 15 / 16 ^ k", "≤ 14 / 16 ^ k",
     "refute_locality_run_constant"),
    ("window-two-n", "zsc03_window", "zsc03_window",
     "∀ n L : ℕ, 1 ≤ n → 4 ^ L ≤ 2 * n → 16 / 15 * 16 ^ L * rPi (n + 1) ≤ 1",
     "4 ^ L ≤ 2 * n", "4 ^ L ≤ 4 * n",
     "refute_window_four_n"),
    ("renewal-kernel-overrun", "zsc03_renewal_kernel", "zsc03_renewal_kernel",
     "∀ (U r : ℕ → ℝ) (n J : ℕ), (∀ m, U (m + 1) = 16 * U m + r (m + 1)) → "
     "(∀ i, 0 ≤ r (n + 1 + i)) → (∀ i, r (n + 1 + i) ≤ r (n + 1)) → "
     "⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16 → 16 / 15 * 16 ^ J * r (n + 1) ≤ 1 → "
     "∀ j, 1 ≤ j → j ≤ J → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0",
     "j ≤ J →", "j ≤ J + 1 →",
     "refute_renewal_kernel_overrun"),
    ("renewal-lemma-overrun", "zsc03_renewal_lemma", "zsc03_renewal_lemma",
     "∀ (U : ℕ → ℝ) (n : ℕ), (∀ m, U (m + 1) = 16 * U m + rPi (m + 1)) → "
     "⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16 → "
     "∀ j : ℕ, 1 ≤ j → (j : ℤ) ≤ Jn n → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0",
     "(j : ℤ) ≤ Jn n →", "(j : ℤ) ≤ Jn n + 1 →",
     "refute_renewal_lemma_overrun"),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def output(command: list[str], cwd: Path) -> str:
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def uncomment(source: str) -> str:
    """Remove nested Lean comments (same logic as scripts/cambrian_audit_c_lean.py)."""
    out = []
    i = 0
    depth = 0
    while i < len(source):
        if source.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and source.startswith("-/", i):
            depth -= 1
            i += 2
        elif not depth and source.startswith("--", i):
            end = source.find("\n", i)
            i = len(source) if end < 0 else end
        else:
            if not depth:
                out.append(source[i])
            elif source[i] == "\n":
                out.append("\n")
            i += 1
    if depth:
        raise ValueError("unterminated Lean comment")
    return "".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, required=True,
                        help="directory for logs, build products and the full observation")
    parser.add_argument("--dependency-project", type=Path, default=PROJECT)
    parser.add_argument("--receipt", type=Path, default=None,
                        help="optional path for the compact receipt (hashes, axioms, controls)")
    args = parser.parse_args()
    started = time.monotonic()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    observation = destination / "kernel-observation.json"
    # An interrupted rerun must not leave an earlier success at these locations.
    for stale in (observation, args.receipt):
        if stale is not None and stale.exists():
            stale.unlink()
    build = Path(tempfile.mkdtemp(prefix="zsc-carry-flux-build-", dir=destination))
    dependency = args.dependency_project.resolve()
    manifest_path = PROJECT / "lake-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    pins = {package["name"]: package["rev"] for package in manifest["packages"]}
    if pins.get("mathlib") != PIN:
        raise RuntimeError("Unexpected repository mathlib pin")
    if (ROOT / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise RuntimeError("Unexpected repository Lean pin")
    if (PROJECT / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise RuntimeError("Unexpected bridge Lean pin")
    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = dependency / ".lake/packages" / name
        actual = output(["git", "rev-parse", "HEAD"], package)
        dirty = output(["git", "status", "--porcelain", "--untracked-files=no"], package)
        if actual != revision or dirty:
            raise RuntimeError(f"Dependency source mismatch: {name}: {actual} {dirty}")
        library = package / ".lake/build/lib"
        if name == "mathlib" and not library.is_dir():
            raise RuntimeError(f"Missing compiled mathlib cache: {library}")
        paths.append(str(library))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    # cwd=ROOT so that elan resolves the repository's lean-toolchain pin.
    version = output(["lean", "--version"], ROOT)
    if not re.search(r"version 4\.14\.0,", version):
        raise RuntimeError(f"Unexpected Lean compiler: {version}")
    source_paths = (SOURCE, Path(__file__).resolve(), ROOT / "lean-toolchain", manifest_path,
                    EXPORT_COMMAND, DOSSIER)
    hashes = {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in source_paths}
    for path in source_paths:
        if path.suffix == ".lean" and re.search(FORBIDDEN, uncomment(path.read_text())):
            raise RuntimeError(f"Forbidden proof authority token: {path}")
    if re.search(r"^\s*set_option\s+maxHeartbeats\s+0", SOURCE.read_text(), re.M):
        raise RuntimeError("Unbounded heartbeats in source")
    names = [NAMESPACE + "." + name for name in
             re.findall(r"^theorem\s+(\w+)", uncomment(SOURCE.read_text()), re.M)]
    if not names:
        raise RuntimeError("No theorem declarations found")
    commands = []
    failures = []
    exports = {}
    controls = []
    commit = output(["git", "rev-parse", "HEAD"], ROOT)
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", str(SOURCE)], cwd=ROOT,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

    def run(label: str, path: Path, *, compile_module: bool = False):
        command = ["lean", "-j", "1", "-M", "4096", "-DmaxHeartbeats=1200000"]
        if compile_module:
            command += ["-o", str(build / f"{MODULE}.olean")]
        command.append(str(path))
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=900)
        log = destination / f"{label}.log"
        log.write_text(result.stdout)
        commands.append({"label": label, "command": command, "cwd": str(ROOT),
                         "exit_code": result.returncode,
                         "seconds": round(time.monotonic() - start, 3),
                         "log": log.name, "log_sha256": sha(result.stdout.encode())})
        print(f"{label}: exit {result.returncode}", flush=True)
        return result

    def clean(result) -> bool:
        text = result.stdout.lower()
        return result.returncode == 0 and "error" not in text and "sorry" not in text

    result = run("module-kernel", SOURCE, compile_module=True)
    if not clean(result):
        failures.append("module-kernel")
    else:
        export = build / f"{MODULE}Export.lean"
        export.write_text(
            f"import {MODULE}\n" + EXPORT_COMMAND.read_text() + "\n" +
            "".join(f"#check @{name}\n#print axioms {name}\n#succ_export {name}\n"
                    for name in names))
        result = run("axiom-export", export)
        if result.returncode:
            failures.append("axiom-export")
        for line in result.stdout.splitlines():
            if "SUCC_THEOREM_JSON " not in line:
                continue
            item = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
            name = item.pop("name")
            if name in exports or name not in names or set(item["axioms"]) - ALLOWED_AXIOMS:
                raise RuntimeError(f"Unapproved theorem export: {name}")
            item["type_sha256"] = sha(item["type_expr"].encode())
            exports[name] = item
        if set(exports) != set(names):
            failures.append("incomplete-exports")

        header = f"import {MODULE}\nopen Polynomial\nopen {NAMESPACE}\n"
        for label, theorem, proof, claim, old, new, refutation in CONTROLS:
            if claim.count(old) != 1:
                raise RuntimeError(f"Mutation site not unique in control {label}")
            if NAMESPACE + "." + theorem not in exports or \
                    NAMESPACE + "." + refutation not in exports:
                failures.append(f"{label}-missing-export")
                continue
            mutated = claim.replace(old, new)
            bodies = {
                "positive": header + f"example : {claim} :=\n  {proof}\n",
                "mutant": header + f"example : {mutated} :=\n  {proof}\n",
                "refuted": header + f"example : ¬ ({mutated}) :=\n  {refutation}\n",
            }
            legs = {}
            for kind, body in bodies.items():
                path = build / f"{label}_{kind}.lean"
                path.write_text(body)
                legs[kind] = run(f"{label}-{kind}", path), sha(body.encode())
            positive, mutant, refuted = (legs[k][0] for k in ("positive", "mutant", "refuted"))
            mutant_text = mutant.stdout.lower()
            infrastructure_error = any(token in mutant_text for token in INFRASTRUCTURE)
            passed = (clean(positive) and mutant.returncode != 0 and
                      "type mismatch" in mutant_text and not infrastructure_error and
                      clean(refuted))
            controls.append({
                "name": label, "theorem": NAMESPACE + "." + theorem,
                "refutation": NAMESPACE + "." + refutation,
                "statement": claim, "mutation": {"old": old, "new": new},
                "positive_exit": positive.returncode, "mutant_exit": mutant.returncode,
                "mutant_type_mismatch": "type mismatch" in mutant_text,
                "mutant_infrastructure_error": infrastructure_error,
                "refuted_exit": refuted.returncode, "passed": passed,
                "positive_sha256": legs["positive"][1], "mutant_sha256": legs["mutant"][1],
                "refuted_sha256": legs["refuted"][1]})
            if not passed:
                failures.append(label)

    unchanged = hashes == {str(path.relative_to(ROOT)): sha(path.read_bytes())
                           for path in source_paths}
    if not unchanged:
        failures.append("source-changed-during-check")
    runtime = round(time.monotonic() - started, 1)
    scope = {
        "kernel_checked_dossier_items": [
            "ZSC-06(d) partial fraction (any field), 16-z^8=K*m, g_pi=K*(1-z), g_0=K*(z^2-4z+2) "
            "with coefficient vector A_0, g_H expansion (Q[X])",
            "ZSC-06(d) integral of (z^2-4z+2)/m over [0,1] is 0; integral of g_0/(16-z^8) is 0; "
            "L(A_0)=sum_j A_j v_j=0 with v_j in integral form",
            "ZSC-02 Lemma 1 (every xi, n, k) and Lemma 2 (every xi, n); two-digit form",
            "ZSC-03 renewal lemma for the four-pole forcing rPi, every real seed, with "
            "J(n)=floor(logb 16 (15/(16 r(n+1)))); J(n) >= floor(logb 4 (2n)) for n>=1; "
            "abstract kernel; r(n+1)>0, r decreasing, r(n+1)<=15/((8n+1)(8n+2))",
        ],
        "not_formalised": [
            "BBP series form v_j = sum_k 16^(-k-1)/(8k+j) and xi = pi/16",
            "rPi(n) = integral of z^(8n-8) g_pi(z) over [0,1] (rPi is taken in closed form)",
            "ZSC-06(e) Baker rigidity and ZSC-06(f)",
            "RIO-09 upper window for the zero run; ZSC-03 Corollaries 1-2",
            "ZSC-01, ZSC-02 Theorem (a)-(d), ZSC-04, ZSC-05, (CH), normality, RH",
        ],
    }
    record = {
        "schema": "succ.zsc-carry-flux.lean-observation.v1",
        "status": "KERNEL_CHECKED" if not failures else "FAILED",
        "commit_at_start": commit,
        "commit_at_end": output(["git", "rev-parse", "HEAD"], ROOT),
        "source_tracked_at_commit": tracked,
        "lean_version": version, "toolchain": TOOLCHAIN, "mathlib_pin": PIN,
        "dependency_project": (str(dependency.relative_to(ROOT)) if ROOT in dependency.parents
                               else "external prebuilt formal/mathlib_bridge (pins verified)"), "dependency_revisions": pins,
        "source_hashes": hashes, "sources_unchanged": unchanged,
        "allowed_axioms": sorted(ALLOWED_AXIOMS), "commands": commands,
        "theorem_exports": exports, "negative_controls": controls,
        "failures": failures, "runtime_seconds": runtime, "scope": scope,
        "normality_proved": False, "historical_authority_modified": False,
    }
    observation.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    if args.receipt is not None:
        compact = {key: value for key, value in record.items()
                   if key not in ("commands", "theorem_exports", "negative_controls")}
        compact["schema"] = "succ.zsc-carry-flux.lean-receipt.v1"
        compact["observation_sha256"] = sha(observation.read_bytes())
        compact["theorems"] = {
            name: {"axioms": item["axioms"], "type_sha256": item["type_sha256"]}
            for name, item in sorted(exports.items())}
        compact["axiom_union"] = sorted({a for item in exports.values() for a in item["axioms"]})
        compact["negative_controls"] = [
            {key: control[key] for key in ("name", "theorem", "refutation", "mutation",
                                            "positive_exit", "mutant_exit",
                                            "mutant_type_mismatch", "refuted_exit", "passed")}
            for control in controls]
        compact["command_seconds"] = {c["label"]: c["seconds"] for c in commands}
        args.receipt.write_text(json.dumps(compact, indent=2, sort_keys=True) + "\n")
    print(record["status"], len(exports), "theorems;", len(controls), "mutant controls;",
          f"{runtime}s", flush=True)
    if failures:
        print("failures:", failures, flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
