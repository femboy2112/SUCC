"""Small negative controls for the observation parser, not a substitute for Lean."""
import json
import unittest

from generate import parse_exports, sha256


class ExportParserControls(unittest.TestCase):
    def line(self, name="Example.theorem", axioms=None, expr="Expr.const Nat []"):
        return "SUCC_THEOREM_JSON " + json.dumps({"name": name, "type_expr": expr,
            "universe_parameters": [], "axioms": axioms or ["propext"]})

    def test_exact_type_hash(self):
        result = parse_exports(self.line(), ["Example.theorem"])
        self.assertEqual(result["Example.theorem"]["type_sha256"], sha256(b"Expr.const Nat []"))

    def test_unapproved_axiom(self):
        with self.assertRaises(ValueError):
            parse_exports(self.line(axioms=["sorryAx"]), ["Example.theorem"])

    def test_wrong_or_duplicate_name(self):
        for log in [self.line(name="Other.theorem"), self.line() + "\n" + self.line()]:
            with self.assertRaises(ValueError):
                parse_exports(log, ["Example.theorem"])

    def test_absent_type_or_theorem(self):
        for log in [self.line(expr=""), "ordinary build output"]:
            with self.assertRaises(ValueError):
                parse_exports(log, ["Example.theorem"])


if __name__ == "__main__":
    unittest.main()
