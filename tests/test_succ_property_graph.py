"""Adversarial bootstrap tests for the typed SUCC proof-property graph.

Exact finite controls are mathematical *smoke tests*, not RH certificates.
Run: python -m unittest discover -s tests -p 'test_succ_property_graph.py'
"""
import copy
from fractions import Fraction as Q
import json
import unittest
from pathlib import Path

from scripts.verify_succ_property_graph import DEFAULT, verify
from observational_succ.zero_centered_residue import (
    coefficients, value, blackout, receipt, distance_interval,
)
from observational_succ.zero_centered_arch_dilation import (
    block_certificate, finite_dilation_receipt,
)


class PropertyGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = json.loads(DEFAULT.read_text(encoding="utf-8"))

    @staticmethod
    def change(graph, key):
        return next(node for node in graph["nodes"] if node["id"] == key)

    def test_graph_is_a_dag_with_three_alternative_RH_routes(self):
        report = verify(self.snapshot)
        self.assertGreaterEqual(report["node_count"], 75)
        self.assertEqual(report["status"], "TYPED_DEPENDENCY_GRAPH_VALID")
        self.assertFalse(report["proves_RH"])
        self.assertEqual(set(report["rh_exits"]["R04"]["alternatives"]),
                         {("R01",), ("R02",), ("R03",)})
        self.assertEqual(len(report["topological_order"]),report["node_count"])

    def test_mislabelled_and_conjunctive_RH_routes_are_detected(self):
        g = copy.deepcopy(self.snapshot)
        self.change(g, "R04")["requires_any"] = [["R01", "R02", "R03"]]
        with self.assertRaisesRegex(ValueError,"ALTERNATIVE"):
            verify(g)

    def test_cycles_are_not_considered_research_dependencies(self):
        g = copy.deepcopy(self.snapshot)
        self.change(g,"C01")["requires_all"]=["R04"]
        with self.assertRaisesRegex(ValueError,"cycle"):
            verify(g)

    def test_global_positivity_cannot_drop_source_identification(self):
        g = copy.deepcopy(self.snapshot)
        self.change(g,"P07")["requires_all"].remove("P03")
        with self.assertRaisesRegex(ValueError,"completed source"):
            verify(g)

    def test_proved_RH_label_needs_actual_independent_receipts(self):
        g = copy.deepcopy(self.snapshot)
        self.change(g,"R04")["status"]="PROVED_LOCAL"
        with self.assertRaisesRegex(ValueError,"global proof"):
            verify(g)

    def test_refuted_premise_is_not_usable_as_positive_evidence(self):
        g = copy.deepcopy(self.snapshot)
        self.change(g,"A07")["status"]="REFUTED"
        with self.assertRaisesRegex(ValueError,"REFUTED claim used"):
            verify(g)

    def test_finite_perfect_fit_has_global_lcm_blindspot(self):
        for K in (3,4,5,6,8):
            a=coefficients(K)
            self.assertTrue(all(value(k,a)==1 for k in range(1,K+1)))
            L=blackout(a)["lcm_cell"]
            self.assertEqual(value(L,a),0)
            lower,upper=distance_interval(a, 512)
            self.assertLess(lower,upper)
            self.assertGreaterEqual(upper,Q(1,L*L))

    def test_fabricated_prime_six_fails_source_authentication(self):
        true=receipt(8)
        false=receipt(8,{6:-1})
        self.assertTrue(true["all_prefix_cells_exact"])
        self.assertFalse(false["all_prefix_cells_exact"])
        self.assertEqual(false["first_bad_divisor"],6)
        self.assertFalse(true["RH_proved"])

    def test_normalized_mellin_isometry_is_not_zero_selection(self):
        for q in (2,3,5):
            for s in (1,2,3):
                self.assertTrue(block_certificate(q,2,s)["exact"])
                r=finite_dilation_receipt({1:Q(1),2:Q(-3,4),4:Q(5,7)},q,s)
                self.assertTrue(r["Mellin_covariance_exact"])
                self.assertFalse(r["critical_line_alone_forces_zeros"])
                self.assertFalse(r["RH_proved"])


if __name__=="__main__":
    unittest.main()
