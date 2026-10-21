"""Main VIII ancestry, provenance, namespace and installed-proposition gates.

These checks establish recorded invariants, not universal mathematical or
software correctness. Run on the exact candidate tree before main admission.
"""
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
    baseline = json.loads((ROOT / "docs/academic_main_viii/live_dag_and_coverage.json").read_text())
    for sha in [baseline["main"], *baseline["heads"].values()]:
        subprocess.run(["git", "merge-base", "--is-ancestor", sha, "HEAD"], cwd=ROOT, check=True)
    manifest = ROOT / "provenance/IMPORT_MANIFEST.json"
    assert hashlib.sha256(manifest.read_bytes()).hexdigest() == baseline["provenance_manifest_sha256"]
    archives = {e["destination_path"] for e in json.loads(manifest.read_text())["entries"]}
    changed = set(git("diff", "--name-only", baseline["main"], "HEAD").splitlines())
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
    for namespace, bare in [("DUAL_COFACTOR", "COF-01"), ("EXTERIOR_ASCENT", "EXT-04"),
                            ("SIMPLEX_ASCENT", "SMP-02"), ("PI_POLYGON_NORMALITY", "POL-09")]:
        assert fqid(namespace, bare) == bare
    record = json.loads((ROOT / "formal/kernel_audit/admitted/kernel-attestation.json").read_text())
    assert len(record["theorem_exports"]) == 19
    assert sum(n.startswith("ObservationalSUCC.PrimitiveSlope.") for n in record["theorem_exports"]) == 9
    for name in record["theorem_exports"]:
        theorem = FormalTheorem.from_receipt(name, record)
        assert Claim(name, theorem.proposition, "C", scope="global").discharge(theorem, receipt=record).status == "VERIFIED"
        for unproved in ("The Riemann hypothesis is true.", "The t=2/3 abc moment is quadratic."):
            assert Claim(name, unproved, "C", scope="global").discharge(theorem, receipt=record).status != "VERIFIED"
    # Check the new research navigation without rewriting unrelated historical links.
    docs = list((ROOT / "docs/academic_main_viii").glob("*.md"))
    docs.append(ROOT / "docs/CLAIM_SUPPLEMENT_EXTERIOR_ASCENT.md")
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            assert (doc.parent / target.split("#", 1)[0]).exists(), (str(doc), target)
    print(json.dumps({"status": "MAIN_VIII_RECORDED_GATES_PASS", "git_commit": git("rev-parse", "HEAD"),
                      "git_tree": git("rev-parse", "HEAD^{tree}"),
                      "working_tree_dirty": bool(git("status", "--porcelain", "--untracked-files=no")),
                      "incoming_heads": baseline["heads"], "archives_unchanged": len(archives),
                      "namespaces": len(entries), "qualified_claims": len(qualified),
                      "actual_formal_exports": len(record["theorem_exports"]),
                      "admitted_record_digest": record_digest(record),
                      "open_conjectures_proved": False}, indent=2))


if __name__ == "__main__":
    main()
