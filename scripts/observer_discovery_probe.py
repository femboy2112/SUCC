#!/usr/bin/env python3
"""Bounded exact discovery replay; outputs hashes, witnesses and retained debt."""
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.minimal_observation import FiniteObservation
from observational_succ.observer_discovery import discover, joint_probe_minima
from observational_succ.source_character_interaction import character_four


def serializable(value):
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(f"Unsupported receipt value: {type(value)}")


def main():
    sources = (
        "observational_succ/observer_discovery.py", "tests/test_observer_discovery.py",
        "scripts/observer_discovery_probe.py", "observational_succ/minimal_observation.py",
        "observational_succ/recursive_operator_gluing.py",
        "observational_succ/covariant_proof_descent.py",
        "observational_succ/source_character_interaction.py",
        "observational_succ/proof_gluing.py", "provenance/IMPORT_MANIFEST.json",
        "research/2026-10-15/proof_teeth_receipts/final-py313.json",
        "research/2026-10-16/OBSERVER_DISCOVERY_EXPERIMENT.md",
    )
    hashes = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
    # Pin the actual imported local closure, not merely the entry-point name.
    imported_hashes = {}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, "__file__", None)
        if filename:
            path = Path(filename).resolve()
            if path.suffix == ".py" and path.is_relative_to(ROOT / "observational_succ"):
                imported_hashes[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
    historical = json.loads((ROOT / sources[-2]).read_text())["after"]
    inherited_matches = {p: historical.get(p) == h for p, h in imported_hashes.items()
                         if p != "observational_succ/observer_discovery.py"}
    if not all(inherited_matches.values()):
        raise AssertionError("Inherited dependency drifted from the pinned successful receipt")
    p = FiniteObservation("canonical chi4 on the entire residue carrier Z/4", 0,
                          (0, 1, 2, 3), tuple(character_four(x) for x in range(4)),
                          ("whole source Z/4 with canonical periodic chi4 values",
                           "probe 0 is low bit; probe 1 is high bit of standard residue"))
    joint = joint_probe_minima(p, ((0, 1, 0, 1), (0, 0, 1, 1)))
    if joint["minimum_cardinality"] != 2:
        raise AssertionError("Joint minimum calibration failed")
    report = {"experiment": discover(), "joint_chi4_bits": joint,
              "source_hashes_sha256": hashes, "python": platform.python_version(),
              "imported_local_dependency_hashes_sha256": imported_hashes,
              "inherited_hashes_match_previous_receipt": inherited_matches,
              "git_head_at_replay": subprocess.check_output(
                  ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
              "source_identity_boundary": "Hashes pin bytes; external analytic identification is not issued",
              "proof_authority_boundary": "Finite matrix identities and whole finite tables only; paper rules retained",
              "commands": ["python -m unittest discover -s tests -p test_observer_discovery.py -v",
                           "python scripts/observer_discovery_probe.py"],
              "full_suite_executed_by_this_probe": False,
              "hosted_CI_checked_by_this_probe": False}
    print(json.dumps(report, indent=2, sort_keys=True, default=serializable))


if __name__ == "__main__":
    main()
