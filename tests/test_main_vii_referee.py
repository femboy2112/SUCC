"""Independent permanent controls: historical fixture classification and arithmetic."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/"scripts"/(name+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RefereeControls(unittest.TestCase):
    def test_fixture_outcomes_are_not_confused(self):
        replay = load("main_vii_hostile_replay")
        base = {"id":"F01_SOURCE_FLAG_MISMATCH"}
        self.assertEqual(replay.classify(dict(base,state="exposed"),{}),"STILL EXPOSED")
        self.assertEqual(replay.classify(dict(base,state="not_exposed"),{}),"FIXED")
        self.assertEqual(replay.classify(dict(base,state="rejected_or_exception",
                         exception="FrozenInstanceError"),{}),"FIXED")
        self.assertEqual(replay.classify(dict(base,state="rejected_or_exception",
                         exception="ImportError"),{}),"INVALID TEST")
        self.assertEqual(replay.classify(dict(base,state="unexpected"),{}),"NEW FAILURE")
        self.assertEqual(replay.classify({"id":"F06_NONINTEGER_CUTOFF",
            "state":"rejected_or_exception","exception":"GoldbachCircleError"},{}),"FIXED")

    def test_independent_arithmetic_and_mutations(self):
        arithmetic = load("main_vii_arithmetic_holdout")
        result = arithmetic.audit(max_x=12,max_divisor=5)
        self.assertEqual(result["failures"],0)
        self.assertNotEqual(result["coprime_k_mutation"]["actual"],
                            result["coprime_k_mutation"]["wrong"])
        self.assertEqual(result["integer_first_moment_census"][-1],[12,45,119])


if __name__ == "__main__":
    unittest.main()
