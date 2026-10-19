"""Hostile controls for the standalone checker, using hand-written fixtures.

The control corpus is independently specified.  One interface test imports the
generator solely to exercise its public JSON boundary; the checker never does.
"""
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_academic_certificate.py"
_SPEC = importlib.util.spec_from_file_location("academic_checker", _PATH)
checker = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(checker)


def fixture():
    return {"states": [
        {"name": "x", "source": "s", "observation": "0", "tasks": []},
        {"name": "y", "source": "s", "observation": "0", "tasks": []},
        {"name": "z", "source": "s", "observation": "1", "tasks": []}],
        "actions": ["a"],
        "edges": [
            {"start": "x", "action": "a", "target": "z", "cost": [1, 2]},
            {"start": "y", "action": "a", "target": "z", "cost": [2, 4]}],
        "certificate": {"blocks": [["x", "y"], ["z"]],
                        "separators": [{"left": "x", "right": "z", "word": []}]}}


class AcademicCheckerTests(unittest.TestCase):
    def rejected(self, doc, pattern):
        with self.assertRaisesRegex(checker.CertificateError, pattern):
            checker.check_certificate(doc)

    def test_positive_exact_fraction_and_null_action_set(self):
        result = checker.check_certificate(fixture())
        self.assertEqual(result["blocks"], 2)
        self.assertFalse(result["generator_imported"])
        doc = fixture()
        doc["actions"] = []
        doc["edges"] = []
        self.assertEqual(checker.check_certificate(doc)["local_squares_checked"], 0)

    def test_output_source_and_task_mutations(self):
        for key, value in (("observation", "changed"), ("source", "other"),
                           ("tasks", [["proof", "undischarged"]])):
            with self.subTest(key=key):
                doc = fixture()
                doc["states"][1][key] = value
                self.rejected(doc, "output/task/source|task schema")

    def test_empty_outputs_and_ordered_task_schema(self):
        doc = fixture()
        for s in doc["states"]:
            s["tasks"] = [["first", ""], ["second", "result"]]
        doc["states"][0]["observation"] = ""
        doc["states"][1]["observation"] = ""
        self.assertEqual(checker.check_certificate(doc)["blocks"], 2)
        doc["states"][1]["tasks"].reverse()
        self.rejected(doc, "ordered task schema")

    def test_generator_json_boundary_empty_output_and_task_result(self):
        from fractions import Fraction
        from observational_succ.future_safe_quotient import (
            State, Edge, Machine, minimize, certificate_payload,
        )
        model = Machine(
            (State("x", "s", "", (("proof", ""),)),
             State("y", "s", "", (("proof", ""),)),
             State("z", "s", "finished", (("proof", ""),))),
            ("a",),
            (Edge("x", "a", "z", Fraction(1, 3)),
             Edge("y", "a", "z", Fraction(1, 3))))
        result = checker.check_certificate(certificate_payload(model, minimize(model)))
        self.assertEqual(result["blocks"], 2)
        self.assertEqual(result["separators_checked"], 1)

    def test_availability_cost_and_successor_mutations(self):
        doc = fixture()
        doc["edges"].pop()
        self.rejected(doc, "availability mismatch")
        doc = fixture()
        doc["edges"][1]["cost"] = [3, 4]
        self.rejected(doc, "cost mismatch")
        doc = fixture()
        doc["edges"][1]["target"] = "x"
        self.rejected(doc, "successor quotient mismatch")

    def test_false_nonminimal_partition_rejected(self):
        doc = fixture()
        doc["certificate"]["blocks"] = [["x"], ["y"], ["z"]]
        doc["certificate"]["separators"] = [
            {"left": "x", "right": "y", "word": ["a"]},
            {"left": "x", "right": "z", "word": []},
            {"left": "y", "right": "z", "word": []}]
        self.rejected(doc, "does not separate")

    def test_missing_and_duplicate_separator_rejected(self):
        doc = fixture()
        doc["certificate"]["separators"] = []
        self.rejected(doc, "every distinct block pair")
        doc = fixture()
        doc["certificate"]["separators"] *= 2
        self.rejected(doc, "duplicate block-pair")

    def test_structural_availability_and_cost_witnesses(self):
        for mutation, kind in (("missing", "STRUCTURAL_LAWFULNESS"), ("cost", "EXACT_COST")):
            doc = fixture()
            doc["states"] = doc["states"][:2]
            doc["certificate"] = {"blocks": [["x"], ["y"]],
                                  "separators": [{"left": "x", "right": "y", "word": ["a"]}]}
            doc["edges"][0]["target"] = "x"
            doc["edges"][1]["target"] = "y"
            if mutation == "missing":
                doc["edges"].pop()
            else:
                doc["edges"][1]["cost"] = [2, 1]
            result = checker.check_certificate(doc)
            self.assertEqual(result["witnesses"][0]["kind"], kind)
            self.assertFalse(result["availability_assumed_observable"])

    def test_delayed_difference_replay(self):
        doc = fixture()
        doc["edges"][0]["target"] = "x"
        doc["certificate"] = {"blocks": [["x"], ["y"], ["z"]], "separators": [
            {"left": "x", "right": "y", "word": ["a"]},
            {"left": "x", "right": "z", "word": []},
            {"left": "y", "right": "z", "word": []}]}
        self.assertEqual(checker.check_certificate(doc)["separators_checked"], 3)
        doc["certificate"]["separators"][0]["word"] = []
        self.rejected(doc, "does not separate")

    def test_unavailable_common_prefix_rejected(self):
        doc = fixture()
        doc["states"][2]["observation"] = "0"
        doc["edges"] = []
        doc["certificate"]["separators"][0]["word"] = ["a"]
        self.rejected(doc, "unavailable on both")

    def test_unused_suffix_rejected(self):
        doc = fixture()
        doc["certificate"]["separators"][0]["word"] = ["a"]
        self.rejected(doc, "unused suffix")

    def test_malformed_fraction_controls(self):
        for value in ([True, 1], [1, False], [1, 0], [-1, 1], [1.0, 2], "1/2"):
            with self.subTest(value=value):
                doc = fixture()
                doc["edges"][0]["cost"] = value
                self.rejected(doc, "cost|rational")

    def test_nondeterministic_table_and_partition_controls(self):
        doc = fixture()
        doc["edges"].append(deepcopy(doc["edges"][0]))
        self.rejected(doc, "repeat an edge key")
        for blocks in ([["x", "y"]], [["x", "y"], ["y", "z"]], [["x", "y"], []]):
            doc = fixture()
            doc["certificate"]["blocks"] = blocks
            self.rejected(doc, "cover|exactly once|nonempty")


if __name__ == "__main__":
    unittest.main()
