"""Exact integration metadata/source gates; mathematical proofs remain separate."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.claim_namespaces import fqid, load_registry, unregistered_prefix_collisions
from observational_succ.proof_authority import Claim, FormalTheorem, record_digest


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    inputs = json.loads((ROOT / "docs/academic_main_vii/live_dag_and_coverage.json").read_text())
    for sha in inputs["heads"].values():
        subprocess.run(["git", "merge-base", "--is-ancestor", sha, "HEAD"], cwd=ROOT, check=True)
    manifest = ROOT / "provenance/IMPORT_MANIFEST.json"
    assert hashlib.sha256(manifest.read_bytes()).hexdigest() == inputs["provenance_manifest_sha256"]
    archives = {e["destination_path"] for e in json.loads(manifest.read_text())["entries"]}
    changed = set(git("diff", "--name-only", inputs["main"], "HEAD").splitlines())
    assert not archives & changed, sorted(archives & changed)
    entries = load_registry()["namespaces"]
    for key in ("namespace", "fq_prefix"):
        assert len({e[key] for e in entries}) == len(entries), key
    assert not unregistered_prefix_collisions()
    qualified = set()
    for entry in entries:
        declared = []
        pattern = re.compile(r"^\|\s*(" + re.escape(entry["bare_prefix"]) + r"-\d+[A-Z]?)\s*\|", re.M)
        for rel in entry["supplement_files"]:
            declared.extend(pattern.findall((ROOT / rel).read_text()))
        assert len(declared) == len(set(declared)), entry["namespace"]
        for bare in declared:
            name = fqid(entry["namespace"], bare)
            assert name not in qualified, name
            qualified.add(name)
    record = json.loads((ROOT / "formal/kernel_audit/admitted/kernel-attestation.json").read_text())
    for name in record["theorem_exports"]:
        theorem = FormalTheorem.from_receipt(name, record)
        assert Claim(name, theorem.proposition, "C", scope="global").discharge(theorem, receipt=record).status == "VERIFIED"
        assert Claim("RH", "The Riemann hypothesis is true.", "C", scope="global").discharge(theorem, receipt=record).status != "VERIFIED"
    print(json.dumps({"status": "INTEGRATION_METADATA_AND_ADMITTED_SOURCE_GATES_PASS",
                      "git_commit": git("rev-parse", "HEAD"), "git_tree": git("rev-parse", "HEAD^{tree}"),
                      "working_tree_dirty": bool(git("status", "--porcelain", "--untracked-files=no")),
                      "incoming_heads": inputs["heads"], "archives_unchanged": len(archives),
                      "namespaces": len(entries), "qualified_claims": len(qualified),
                      "actual_formal_exports": len(record["theorem_exports"]),
                      "admitted_record_digest": record_digest(record),
                      "universal_software_correctness_or_open_conjectures_proved": False}, indent=2))


if __name__ == "__main__":
    main()
