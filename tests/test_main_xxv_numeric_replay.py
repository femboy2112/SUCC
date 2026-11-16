"""Mutation controls for the narrow Main XXV numerical replay boundary."""
import copy
import importlib.util
import math
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "main_xxv_numeric_replay", Path(__file__).resolve().parents[1] / "scripts/main_xxv_numeric_replay.py")
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


class NumericReplayBoundary(unittest.TestCase):
    def setUp(self):
        self.slot = {"kind": "identity", "checks": 90, "failures": 0,
                     "counterexamples": [], "tolerance": 1e-12, "max_abs_error": 2e-16,
                     "worst": {"B": 64, "h": 1, "lag": 5, "control": "2_coherent", "error": 2e-16}}
        self.old = {"meta": {"tolerance": 1e-12}, "summary": {"failed": False},
                    "shells": {"64": {"PR-1": {"checks": {"PR-1.6": {replay.IDENTITY: self.slot}}},
                                      "iad06": {"1_true": {"1": {
                                          "c_U_d_for_d_1_to_dmax": [[0.02, -0.03]],
                                          "random_H_rhs": [0.5], "transport_max_ratio_to_bound": 0.003}}}}}}

    def result(self, new, filename=replay.ANALYTIC):
        return replay.compare(self.old, new, filename)

    def test_exact_receipt_and_small_listed_roundoff_pass(self):
        self.assertEqual(self.result(self.old)["difference_count"], 0)
        new = copy.deepcopy(self.old)
        new["shells"]["64"]["iad06"]["1_true"]["1"]["c_U_d_for_d_1_to_dmax"][0][0] = math.nextafter(0.02, 1)
        self.assertEqual(self.result(new)["status"], "PASS")
        self.assertEqual(self.result(new, "RESULTS_arithmetic.json")["status"], "FAIL")

    def test_threshold_count_status_and_type_mutants_fail(self):
        variants = []
        a = copy.deepcopy(self.old); a["meta"]["tolerance"] = math.nextafter(1e-12, 1); variants.append(a)
        a = copy.deepcopy(self.old); a["summary"]["failed"] = True; variants.append(a)
        a = copy.deepcopy(self.old); a["shells"]["64"]["PR-1"]["checks"]["PR-1.6"][replay.IDENTITY]["checks"] += 1; variants.append(a)
        a = copy.deepcopy(self.old); a["meta"]["tolerance"] = "1e-12"; variants.append(a)
        for a in variants:
            self.assertEqual(self.result(a)["status"], "FAIL")

    def test_unlisted_float_and_large_or_nan_diagnostic_fail(self):
        for value in (0.04, float("nan"), float("inf")):
            a = copy.deepcopy(self.old)
            a["shells"]["64"]["iad06"]["1_true"]["1"]["c_U_d_for_d_1_to_dmax"][0][0] = value
            self.assertEqual(self.result(a)["status"], "FAIL")
        a = copy.deepcopy(self.old); a["meta"]["tolerance"] += 1e-20
        self.assertEqual(self.result(a)["status"], "FAIL")

    def test_machine_roundoff_argmax_class_is_validated(self):
        a = copy.deepcopy(self.old)
        s = a["shells"]["64"]["PR-1"]["checks"]["PR-1.6"][replay.IDENTITY]
        s["max_abs_error"] = s["worst"]["error"] = 3e-16
        s["worst"].update(control="5_hijack", lag=2)
        self.assertEqual(self.result(a)["status"], "PASS")
        for field, value in (("control", "invented"), ("lag", 1000), ("h", 3)):
            b = copy.deepcopy(a)
            b["shells"]["64"]["PR-1"]["checks"]["PR-1.6"][replay.IDENTITY]["worst"][field] = value
            self.assertEqual(self.result(b)["status"], "FAIL")
        s["max_abs_error"] = s["worst"]["error"] = 2e-14
        self.assertEqual(self.result(a)["status"], "FAIL")

    def test_missing_key_and_truncated_array_fail(self):
        a = copy.deepcopy(self.old); del a["summary"]
        self.assertEqual(self.result(a)["status"], "FAIL")
        a = copy.deepcopy(self.old); a["shells"]["64"]["iad06"]["1_true"]["1"]["random_H_rhs"] = []
        self.assertEqual(self.result(a)["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
