"""Structural hostile controls; these tests do not authenticate mathematical claims."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import tempfile
import unittest


_path = Path(__file__).resolve().parents[1] / "scripts/verify_duck_pi_dependencies.py"
_spec = importlib.util.spec_from_file_location("duck_dependency_diagnostic", _path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
validate_ledger = _module.validate_ledger


class DependencyDiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "proof.lean").write_text("theorem conditional (h : P) : P := h\n")
        self.base = {
            "schema_version": 1, "diagnostic_only": True,
            "nodes": [
                dict(id="premise", kind="conclusion", status="OPEN", statement="P",
                     requires=[], premises=[], files=["proof.lean"]),
                dict(id="implication", kind="theorem", status="PAPER_PROVED", form="implication",
                     statement="P implies P", requires=[], premises=["premise"], files=["proof.lean"],
                     formal=[dict(path="proof.lean", declaration="conditional")]),
                dict(id="conclusion", kind="conclusion", status="OPEN", statement="P",
                     requires=["implication", "premise"], premises=[], files=["proof.lean"])
            ]}

    def errors(self, ledger):
        return "\n".join(validate_ledger(ledger, self.root))

    def test_proved_implication_does_not_discharge_its_open_premise(self):
        before = deepcopy(self.base)
        self.assertEqual(validate_ledger(self.base, self.root), [])
        self.assertEqual(before, self.base)
        self.base["nodes"][2]["status"] = "PAPER_PROVED"
        self.assertIn("invalid promotion", self.errors(self.base))

    def test_unconditional_theorem_cannot_hide_open_assumption(self):
        self.base["nodes"][1]["form"] = "unconditional"
        self.assertIn("explicit implication", self.errors(self.base))
        self.base["nodes"][1]["premises"] = []
        self.base["nodes"][1]["requires"] = ["premise"]
        self.assertIn("invalid promotion", self.errors(self.base))

    def test_applying_an_implication_cannot_omit_its_premise(self):
        self.base["nodes"][2].update(status="PAPER_PROVED", requires=["implication"])
        self.assertIn("omitted premise", self.errors(self.base))
        self.base["nodes"][2].update(kind="theorem", form="implication", premises=["premise"])
        self.assertEqual(validate_ledger(self.base, self.root), [])
        self.base["nodes"][2].update(form="unconditional", premises=[], requires=["implication", "premise"])
        self.base["nodes"][0]["status"] = "PAPER_PROVED"
        self.assertEqual(validate_ledger(self.base, self.root), [])

    def test_cycles_duplicates_and_missing_nodes_rejected(self):
        self.base["nodes"][0]["requires"] = ["conclusion"]
        self.assertIn("dependency cycle", self.errors(self.base))
        self.base["nodes"][0]["requires"] = ["missing"]
        self.assertIn("missing node", self.errors(self.base))
        self.base["nodes"].append(deepcopy(self.base["nodes"][0]))
        self.assertIn("duplicate node", self.errors(self.base))

    def test_files_declarations_and_traversal_checked_lexically(self):
        self.base["nodes"][1]["formal"][0]["declaration"] = "nonexistent"
        self.assertIn("declaration absent", self.errors(self.base))
        self.base["nodes"][0]["files"] = ["absent.md", "../outside.md"]
        errors = self.errors(self.base)
        self.assertIn("missing file", errors)
        self.assertIn("escapes repository", errors)

    def test_kernel_label_requires_external_record_reference(self):
        self.base["nodes"][1]["status"] = "KERNEL_CHECKED"
        self.assertIn("malformed local reference", self.errors(self.base))
        self.assertEqual(self.base["nodes"][0]["status"], "OPEN")

    def test_structural_pass_does_not_authenticate_a_forged_receipt(self):
        # Deliberately invalid Lean and forged JSON may be structurally
        # consistent. The diagnostic never calls a proof-authority checker.
        (self.root / "untrusted.json").write_text('{"build_succeeded": true}')
        self.base["nodes"][1].update(status="KERNEL_CHECKED", kernel_record="untrusted.json")
        self.assertEqual(validate_ledger(self.base, self.root), [])
        self.assertTrue(self.base["diagnostic_only"])
        self.assertEqual(self.base["nodes"][2]["status"], "OPEN")

    def test_source_definition_and_authority_confusion_rejected(self):
        self.base["nodes"][0].update(kind="source", status="PAPER_PROVED")
        self.assertIn("source reference", self.errors(self.base))
        self.base["nodes"][0].update(kind="definition", status="PAPER_PROVED")
        self.assertIn("definition", self.errors(self.base))
        self.base["diagnostic_only"] = False
        self.assertIn("disclaim proof authority", self.errors(self.base))

    def test_malformed_json_types_fail_without_authority(self):
        for mutation in ({"schema_version": True}, {"nodes": None},
                         {"nodes": [None]}, {"diagnostic_only": "true"}):
            changed = deepcopy(self.base)
            changed.update(mutation)
            self.assertTrue(validate_ledger(changed, self.root))
        self.base["nodes"][1]["form"] = {"not": "a form"}
        self.assertIn("theorem form missing", self.errors(self.base))

    def test_attributed_theorem_reference_and_symlink_boundary(self):
        (self.root / "proof.lean").write_text("@[simp] theorem conditional (h : P) : P := h\n")
        self.assertEqual(validate_ledger(self.base, self.root), [])
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "outside.lean"
            external.write_text("theorem unrelated : True := True.intro\n")
            (self.root / "escape.lean").symlink_to(external)
            self.base["nodes"][0]["files"] = ["escape.lean"]
            self.assertIn("escapes repository", self.errors(self.base))


if __name__ == "__main__":
    unittest.main()
