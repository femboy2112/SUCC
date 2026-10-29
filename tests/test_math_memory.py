"""Independent small-fixture checks; never claims repository-wide completeness."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_math_memory import build, main


class MathMemoryTests(unittest.TestCase):
    def fixture(self, root):
        (root / "docs").mkdir()
        (root / "research" / "2026-10-27").mkdir(parents=True)
        registry = {"schema_version": 1, "namespaces": [
            {"namespace": "ALPHA", "bare_prefix": "AA", "fq_prefix": "AA.TEST",
             "supplement_files": ["docs/CLAIM_SUPPLEMENT_ALPHA.md"]},
            {"namespace": "BETA", "bare_prefix": "AA", "fq_prefix": "AA.OTHER",
             "supplement_files": ["docs/CLAIM_SUPPLEMENT_BETA.md"]}]}
        (root / "docs/CLAIM_NAMESPACE_REGISTRY.json").write_text(json.dumps(registry), encoding="utf-8")
        (root / "docs/CLAIM_SUPPLEMENT_ALPHA.md").write_text("# Alpha\n| ID | claim |\n|---|---|\n| AA-01 | First |\n| AA-02B | Second |\n", encoding="utf-8")
        (root / "docs/CLAIM_SUPPLEMENT_BETA.md").write_text("# Beta\n| AA-01 | Other |\n", encoding="utf-8")
        (root / "research/2026-10-27/theorem.md").write_text("# Real theorem\n\nA=1\n",encoding="utf-8")

    def test_collision_safe_fqid_and_original_bare_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            data = build(root)
            self.assertEqual([c["key"] for c in data["claims"]],
                             ["AA.TEST-01", "AA.TEST-02B", "AA.OTHER-01"])
            self.assertEqual(data["coverage"]["claim_rows_found"], 3)
            self.assertEqual(data["coverage"]["source_documents_found"], 1)
            self.assertEqual(data["warnings"], [])

    def test_unregistered_is_visible_not_silently_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.fixture(root)
            (root/"docs/CLAIM_SUPPLEMENT_HIDDEN.md").write_text("| ZZ-01 | hidden |\n",encoding="utf-8")
            data=build(root)
            self.assertTrue(any("UNREGISTERED CLAIM SUPPLEMENT" in w for w in data["warnings"]))
            hidden=[c for c in data["claims"] if c["bare_id"]=="ZZ-01"]
            self.assertEqual(len(hidden),1)
            self.assertFalse(hidden[0]["registered"])
            self.assertTrue(hidden[0]["key"].startswith("UNREGISTERED::"))

    def test_deterministic_manifest_and_stale_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.fixture(root)
            self.assertEqual(main(["--root",str(root),"--write"]),0)
            self.assertEqual(main(["--root",str(root),"--check"]),0)
            path=root/"docs/math_memory/CLAIM_CATALOG.json"
            data=json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(data["not_a_proof_checker"])
            (root/"docs/CLAIM_SUPPLEMENT_ALPHA.md").write_text("| AA-04 | changed |\n",encoding="utf-8")
            self.assertEqual(main(["--root",str(root),"--check"]),1)

    def test_duplicate_fqid_namespace_is_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.fixture(root)
            p=root/"docs/CLAIM_NAMESPACE_REGISTRY.json"
            data=json.loads(p.read_text(encoding="utf-8"))
            data["namespaces"][1]["fq_prefix"]="AA.TEST"
            p.write_text(json.dumps(data),encoding="utf-8")
            self.assertTrue(any("DUPLICATE FQ" in w for w in build(root)["warnings"]))

    def test_dependency_cache_cannot_change_research_catalog(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            before = build(root)
            cache = root / "formal/project/.lake/packages/mathlib/Mathlib"
            cache.mkdir(parents=True)
            (cache / "Dependency.lean").write_text("theorem external : True := by trivial\n")
            (cache / "README.md").write_text("# External package\n")
            self.assertEqual(build(root), before)
            # A neighboring repository proof must still be indexed.
            (root / "formal/project/Local.lean").write_text("theorem localProof : True := by trivial\n")
            paths = {row["path"] for row in build(root)["source_documents"]}
            self.assertIn("formal/project/Local.lean", paths)


if __name__ == "__main__":
    unittest.main()
