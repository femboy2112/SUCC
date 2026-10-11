"""Constructive-LEM and non-omega-continuous closure negative controls."""
import unittest

from observational_succ.constructive_frontier import (
    Formula, FrontierError, KripkeModel, atom, neg, disj, implication,
    intuitionistic_lem_demo, finite_successor_stage, SymbolicOmegaStage,
    omega_plus_one_demo, fixed_width_message_capacity,
)


class ConstructiveFrontierTests(unittest.TestCase):
    def setUp(self):
        self.model = KripkeModel(
            ("root", "left", "right"),
            (("root", "left"), ("root", "right")),
            (("root", ()), ("left", ("P",)), ("right", ())),
        )
        self.p = atom("P")

    def test_genuine_intuitionistic_nonforcing_of_lem_without_inconsistency(self):
        k = self.model
        p = self.p
        self.assertFalse(k.forces("root", p))
        self.assertFalse(k.forces("root", neg(p)))
        self.assertFalse(k.excluded_middle("root", p))
        self.assertTrue(k.forces("left", p))
        self.assertFalse(k.forces("left", neg(p)))
        self.assertTrue(k.forces("right", neg(p)))
        self.assertTrue(k.excluded_middle("left", p))
        self.assertTrue(k.excluded_middle("right", p))
        self.assertFalse(k.forces("root", neg(disj(p, neg(p)))))
        self.assertTrue(k.forces("root", neg(neg(disj(p, neg(p))))))
        self.assertTrue(k.forces("root", implication(p, p)))
        for node in k.nodes:
            self.assertFalse(k.forces(node, Formula("bottom")))

    def test_classical_lem_remains_a_boolean_tautology(self):
        for classical_assignment in (False, True):
            self.assertTrue(classical_assignment or not classical_assignment)
        report = intuitionistic_lem_demo()
        self.assertFalse(report["root_forces_P_or_not_P"])
        self.assertTrue(report["yes_forces_P_or_not_P"])
        self.assertTrue(report["no_forces_P_or_not_P"])
        self.assertFalse(report["classical_excluded_middle_invalidated"])
        self.assertFalse(report["contradictory_physical_observation_required"])

    def test_kripke_monotonicity_and_wellformedness_controls(self):
        with self.assertRaises(FrontierError):
            KripkeModel(("root", "leaf"), (("root", "leaf"),),
                        (("root", ("P",)), ("leaf", ())))
        with self.assertRaises(FrontierError):
            KripkeModel(("root", "leaf"), (("root", "leaf"), ("leaf", "root")),
                        (("root", ()), ("leaf", ())))
        with self.assertRaises(FrontierError):
            KripkeModel(("root", "leaf"), (),
                        (("root", ()), ("leaf", ())))
        with self.assertRaises(FrontierError):
            Formula("or", (self.p,))
        with self.assertRaises(FrontierError):
            Formula("atom", (), "")
        with self.assertRaises(FrontierError):
            self.model.forces("unknown", self.p)
        with self.assertRaises(FrontierError):
            self.model.forces("root", "P")

    def test_non_omega_continuity_and_symbolic_omega_plus_one_gate(self):
        for n in range(0, 100):
            stage = finite_successor_stage(n)
            self.assertEqual(stage, tuple(range(n)))
            self.assertNotIn("seal", stage)
            self.assertEqual(finite_successor_stage(n + 1), stage + (n,))
        report = omega_plus_one_demo()
        self.assertEqual(report["status"], "SYMBOLIC_NON_OMEGA_CONTINUOUS_CLOSURE")
        self.assertTrue(report["omega_contains_all_naturals"])
        self.assertFalse(report["omega_contains_seal"])
        self.assertTrue(report["omega_plus_one_contains_seal"])
        self.assertFalse(report["physical_infinite_iteration_executed"])
        self.assertFalse(report["infinitary_rule_licensed_by_finite_data"])
        symbolic = SymbolicOmegaStage(True, False)
        self.assertEqual(symbolic.next_declared_limit_rule(), SymbolicOmegaStage(True, True))
        self.assertEqual(SymbolicOmegaStage(False, False).next_declared_limit_rule(),
                         SymbolicOmegaStage(False, False))
        with self.assertRaises(FrontierError):
            finite_successor_stage(float(1))

    def test_fixed_bit_count_pigeonhole_and_overselling_negative_control(self):
        self.assertEqual(fixed_width_message_capacity(0), 1)
        self.assertEqual(fixed_width_message_capacity(1), 2)
        self.assertEqual(fixed_width_message_capacity(8), 256)
        self.assertGreater(257, fixed_width_message_capacity(8))
        self.assertLessEqual(256, fixed_width_message_capacity(8))
        with self.assertRaises(FrontierError):
            fixed_width_message_capacity(-1)
        with self.assertRaises(FrontierError):
            fixed_width_message_capacity(True)

if __name__ == "__main__":
    unittest.main()
