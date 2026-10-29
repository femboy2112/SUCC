"""Hostile authority guards and exact semantic controls for the new Lean audit."""

from fractions import Fraction as F
import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("growth_audit", ROOT / "scripts/check_lonely_runner_growth_lean.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class GrowthAuthorityTests(unittest.TestCase):
    def item(self, name="source_theorem", axioms=None, type_expr="exact kernel expression"):
        return {"name": name, "axioms": ["propext"] if axioms is None else axioms,
                "type_expr": type_expr, "universe_parameters": []}

    def test_complete_exact_exports_receive_type_hash(self):
        result = AUDIT.validate_exports([self.item()], ["source_theorem"])
        self.assertEqual(result["source_theorem"]["type_sha256"], AUDIT.sha(b"exact kernel expression"))

    def test_zero_missing_duplicate_and_invented_exports_fail(self):
        for items, names in (([], []), ([], ["source_theorem"]),
                             ([self.item(), self.item()], ["source_theorem"]),
                             ([self.item("other")], ["source_theorem"])):
            with self.assertRaises(ValueError):
                AUDIT.validate_exports(items, names)

    def test_nonstandard_axiom_and_empty_type_fail(self):
        for item in (self.item(axioms=["sorryAx"]), self.item(axioms=["inventedSourceLaw"]),
                     self.item(type_expr="")):
            with self.assertRaises(ValueError):
                AUDIT.validate_exports([item], ["source_theorem"])

    def test_band_width_mutation_has_exact_countermodel(self):
        delta, velocity = F(1, 3), 1
        left, right = -delta, delta
        # This is precisely the k=0 closed bad band. Its open interior is
        # covered; replacing its true 2*delta/v width by delta/v is false.
        self.assertEqual(right-left, 2*delta/velocity)
        self.assertGreater(right-left, delta/velocity)

    def test_integer_spacing_mutation_has_exact_countermodel(self):
        denominator, left_numerator, right_numerator = 3, 1, 2
        width = F(right_numerator-left_numerator, denominator)
        self.assertEqual(width, F(1, denominator))
        self.assertLess(width, F(2, denominator))

    def test_scope_keeps_the_general_hole_hypothesis_explicit(self):
        source = (ROOT / "formal/LonelyRunnerGrowth.lean").read_text()
        general = source.split("theorem inserted_speed_bound_from_hole", 1)[1].split(" := by", 1)[0]
        self.assertIn("hhole : ∃ t₀ : ℝ", general)
        final = source.split("theorem upper_half_cubic_growth", 1)[1].split(" := by", 1)[0]
        self.assertIn("hupper : n-1 < 2*r", final)
        self.assertIn("hcover : Covers", final)
        self.assertNotIn("hhole", final)
        self.assertNotIn("occupancy", final)


if __name__ == "__main__":
    unittest.main()
