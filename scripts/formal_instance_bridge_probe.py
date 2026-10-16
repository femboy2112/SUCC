#!/usr/bin/env python3
"""Generate fixed finite SUCC models; optionally replay in the pinned YEAN kernel.

The optional replay requires the fresh YEAN dependency manifest. It validates
source and compiled artifact bytes before AND after invoking Lean. It never runs
commands found in a packet, nor accepts an external prewritten proof.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.formal_instance_bridge import (  # noqa: E402
    affine_packet, retract_packet, lean_source, replay_packet, verify_pins,
    RUNTIME_PINS, LEAN_PINS, SOURCE_OBLIGATIONS, BridgeError,
)


def sha(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_environment(yean, manifest):
    verify_pins(ROOT, RUNTIME_PINS)
    verify_pins(yean, LEAN_PINS)
    if manifest["audit_trust_level"] != 0:
        raise BridgeError("Trust-zero formal manifest required")
    prefix = Path(subprocess.check_output(["lean", "--print-prefix"], cwd=yean, text=True).strip())
    if sha(prefix / "bin/lean") != manifest["lean_binary_sha256"]:
        raise BridgeError("Lean executable changed")
    version = subprocess.check_output(["lean", "--version"], cwd=yean, text=True).strip()
    if version != manifest["versions"]["lean"] or "4.29.1" not in version:
        raise BridgeError("Lean toolchain mismatch")
    for record in manifest["dependencies"].values():
        if sha(record["source"]) != record["source_sha256"]:
            raise BridgeError("Dependency source changed: " + record["source"])
        for artifact in record["artifacts"]:
            if sha(artifact["path"]) != artifact["sha256"]:
                raise BridgeError("Compiled dependency changed: " + artifact["path"])
    return version


def rebuild_local_imports(yean, manifest, output):
    """Bind the pinned local Lean text to fresh oleans, not a claimed cache hash."""
    packages = json.loads((yean / "lake-manifest.json").read_text())["packages"]
    supplied = {p["name"]: p for p in manifest["dependency_pins"]}
    paths = []
    for package in packages:
        pin = supplied[package["name"]]
        path = Path(pin["path"])
        head = subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
        status = subprocess.check_output(["git", "-C", str(path), "status", "--porcelain"], text=True)
        if head != package["rev"] or status:
            raise BridgeError("External dependency is not clean and pinned")
        paths.append(str(path / ".lake/build/lib/lean"))
    build = (output / "build").resolve()
    build.mkdir(exist_ok=True)
    env = dict(os.environ, LEAN_PATH=":".join([str(build)] + paths), LEAN_NUM_THREADS="1")
    built, receipts = set(), []

    def compile_module(module):
        if not module.startswith("Yean.") or module in built:
            return
        source = yean / (module.replace(".", "/") + ".lean")
        record = manifest["dependencies"][module]
        if sha(source) != record["source_sha256"]:
            raise BridgeError("Fresh local source differs from formal audit")
        for dependency in record["imports"]:
            compile_module(dependency)
        target = build / (module.replace(".", "/") + ".olean")
        target.parent.mkdir(parents=True, exist_ok=True)
        command = ["lean", "-j1", "-M2304", "-DElab.async=false", "-t0", "-o", str(target), str(source)]
        start = time.monotonic()
        process = subprocess.run(command, cwd=yean, env=env, text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
        log = output / ("compile-" + module + ".txt")
        log.write_text(process.stdout)
        receipts.append({"module": module, "argv": command, "exit_code": process.returncode,
                         "elapsed_seconds": round(time.monotonic()-start, 3),
                         "source_sha256": sha(source), "log": log.name, "log_sha256": sha(log)})
        (output / "fresh-local-compilation.json").write_text(json.dumps(receipts, indent=2)+"\n")
        if process.returncode:
            raise BridgeError("Fresh local Lean compile failed: " + str(log))
        built.add(module)

    for module in ("Yean.SUCC.TwoPoint", "Yean.SUCC.FiniteRetract"):
        compile_module(module)
    return env, sorted(built)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--yean", type=Path)
    p.add_argument("--formal-manifest", type=Path)
    args = p.parse_args()
    if bool(args.yean) != bool(args.formal_manifest):
        p.error("--yean and --formal-manifest must be supplied together")
    args.output.mkdir(parents=True, exist_ok=True)
    verify_pins(ROOT, RUNTIME_PINS)
    owned = [Path(__file__), ROOT / "observational_succ/formal_instance_bridge.py"]
    own_hashes = {str(p.relative_to(ROOT)): sha(p) for p in owned}
    packets = [affine_packet([("S", 1), ("V", 2), ("S", 3), ("V", 3)],
                             source_id="natural-successor-prime-source", epoch=0),
               retract_packet(4, 2, source_id="integer-residue-source", epoch=0)]
    result = {"schema": "FINITE_MODEL_KERNEL_REPLAY_v1", "instances": [],
              "kernel_verification_performed": False,
              "source_obligations": list(SOURCE_OBLIGATIONS),
              "universal_python_correctness": False, "physical_source_authenticated": False,
              "hosted_CI_claimed": False, "RH_proved": False,
              "implementation_sha256": own_hashes, "kernel_mutants": []}
    manifest = None
    if args.yean:
        args.yean = args.yean.resolve()
        manifest = json.loads(args.formal_manifest.read_text())
        result["lean_version"] = verify_environment(args.yean, manifest)
        result["formal_manifest_sha256"] = sha(args.formal_manifest)
        env, local_modules = rebuild_local_imports(args.yean, manifest, args.output)
        result["fresh_local_modules"] = local_modules
    for i, packet in enumerate(packets):
        code, names = lean_source(packet)
        source = (args.output / f"instance-{i}.lean").resolve()
        source.write_text(code)
        (args.output / f"instance-{i}.json").write_text(json.dumps(packet, indent=2) + "\n")
        record = {"translation": replay_packet(packet, source_id=packet["source_id"], epoch=packet["epoch"]),
                  "source": source.name, "source_sha256": sha(source), "declarations": names,
                  "kernel_status": "NOT_RUN"}
        if manifest:
            command = ["lean", "-j1", "-M2304", "-DElab.async=false", "-t0", str(source)]
            start = time.monotonic()
            process = subprocess.run(command, cwd=args.yean, env=env, text=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
            log = args.output / f"instance-{i}-kernel.txt"
            log.write_text(process.stdout)
            observed = {}
            for name, axioms, none in re.findall(
                    r"'([^']+)' (?:depends on axioms:\s*\[([^]]*)\]|(does not depend on any axioms))",
                    process.stdout):
                observed[name] = [] if none else [re.sub(r"\.\{[^}]*\}", "", a.strip())
                                                 for a in axioms.split(",") if a.strip()]
            ok = (process.returncode == 0 and set(observed) == set(names)
                  and all(set(a) <= {"propext", "Quot.sound", "Classical.choice"} for a in observed.values())
                  and sha(source) == record["source_sha256"])
            record.update(argv=command, cwd=str(args.yean), exit_code=process.returncode,
                          elapsed_seconds=round(time.monotonic()-start, 3), axioms=observed,
                          full_elaborated_types=log.name, log_sha256=sha(log),
                          kernel_status="EXACT_GENERATED_DECLARATIONS_CHECKED" if ok else "FAILED")
            if not ok:
                result["instances"].append(record)
                (args.output / "replay.json").write_text(json.dumps(result, indent=2)+"\n")
                raise BridgeError("Kernel rejected generated instance; see " + str(log))
        result["instances"].append(record)
        if manifest:
            # Deliberately bypass packet validation to challenge the kernel itself.
            old, new = (("⟨6, 15⟩", "⟨6, 16⟩") if i == 0 else
                        ("((1 : ℚ) / 2)", "((1 : ℚ) / 1)"))
            if old not in code:
                raise BridgeError("Fixed mutation target missing")
            mutant = args.output.resolve() / f"mutant-{i}.lean"
            mutant.write_text(code.replace(old, new, 1))
            command = ["lean", "-j1", "-M2304", "-DElab.async=false", "-t0", str(mutant)]
            process = subprocess.run(command, cwd=args.yean, env=env, text=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
            log = args.output / f"mutant-{i}-kernel.txt"
            log.write_text(process.stdout)
            rejected = (process.returncode == 1 and re.search(r"\berror(?:\([^)]*\))?:", process.stdout)
                        and not any(s in process.stdout.lower() for s in
                                    ("unknown module prefix", "object file", "memory", "timeout")))
            result["kernel_mutants"].append({"source": mutant.name, "source_sha256": sha(mutant),
                "mutation": "wrong affine offset" if i == 0 else "omitted fiber normalization",
                "argv": command, "exit_code": process.returncode, "rejected": bool(rejected),
                "log": log.name, "log_sha256": sha(log)})
            if not rejected:
                raise BridgeError("Invalid kernel mutation outcome: " + str(log))
    if manifest:
        verify_environment(args.yean, manifest)
        result["kernel_verification_performed"] = True
    result["implementation_unchanged"] = own_hashes == {str(p.relative_to(ROOT)): sha(p) for p in owned}
    if not result["implementation_unchanged"]:
        raise BridgeError("Bridge implementation changed during replay")
    (args.output / "replay.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
