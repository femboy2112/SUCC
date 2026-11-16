"""Fault injection for integration byte/ancestry checks, without full suite replay."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "scripts/main_xxvi_manifest.py"
SPEC = importlib.util.spec_from_file_location("main_xxvi_manifest", PATH)
manifest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(manifest)


class ManifestMutations(unittest.TestCase):
    def test_changed_entries_preserve_mode_and_deletion(self):
        a = {"deleted": {"blob": "a"}, "mode": {"blob": "x", "mode": "100644"}}
        b = {"added": {"blob": "b"}, "mode": {"blob": "x", "mode": "100755"}}
        self.assertEqual(set(manifest.changed(a, b)), {"deleted", "added", "mode"})
        self.assertIsNone(manifest.changed(a, b)["deleted"])

    def fixture(self):
        entry = {"blob": "b", "mode": "100644", "type": "blob"}
        data = {"baseline": {"commit": manifest.BASE},
                "donors": [{"pr": n, "head": "head", "tree": "tree", "parents": ["parent"],
                            "own_delta": []} for n in sorted(manifest.EXPECTED_PRS)],
                "excluded_final_change_paths": [manifest.DEFAULT_MANIFEST, manifest.CATALOG],
                "final_changes": {"new": entry},
                "protected_baseline_entries": {}, "declared_integration_overrides": []}
        return data, entry

    def run_check(self, data, final, ancestor=True):
        with patch.object(manifest, "tree", side_effect=lambda ref: {} if ref == manifest.BASE else final), \
             patch.object(manifest, "ancestor", return_value=ancestor), \
             patch.object(manifest, "protected_paths", return_value=[]), \
             patch.object(manifest, "git", side_effect=lambda *a: "tree" if a[0] == "rev-parse" else "parent"):
            return manifest.check(data, "integration")

    def test_new_file_and_changed_blob_mutants_rejected(self):
        data, entry = self.fixture()
        self.assertEqual(self.run_check(data, {"new": entry}), [])
        self.assertTrue(any("added" in x for x in self.run_check(data, {"new": entry, "added": entry})))
        self.assertTrue(any("new" in x for x in self.run_check(data, {"new": {**entry, "blob": "mutant"}})))
        self.assertTrue(any("new" in x for x in self.run_check(data, {})))

    def test_missing_ancestry_and_exclusion_mutants_rejected(self):
        data, entry = self.fixture()
        self.assertTrue(any("ancestry" in x for x in self.run_check(data, {"new": entry}, False)))
        data["excluded_final_change_paths"].append("secret-extra-exclusion")
        self.assertIn("unexpected final-byte exclusions", self.run_check(data, {"new": entry}))


if __name__ == "__main__":
    unittest.main()
