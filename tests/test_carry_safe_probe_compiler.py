"""Exact tests for the adaptive weighted-minimax probe compiler (Phase 5)."""
import unittest
from fractions import Fraction as Q

from observational_succ import carry_safe_probe_compiler as pc
from observational_succ.adaptive_proof_policy import (
    conditional_source_field, solve_adaptive_claim,
)


class TestResidueCertification(unittest.TestCase):
    def test_full_register_and_hardest_pair_cost_p(self):
        for p in (2, 3, 4, 5):
            r = pc.residue_certification_cost(p)
            self.assertTrue(r["winning"])
            self.assertEqual(r["full_register_cost"], p)       # 1 warm-up + (p-1) peels
            self.assertEqual(r["unit_rank"], p)                # existing engine agrees
            self.assertEqual(r["bruteforce_cost"], p)          # independent DFS agrees
            self.assertEqual(r["hardest_pair_cost"], p)        # (p-1) advance + 1 warm-up

    def test_weighted_scales_cost(self):
        r = pc.residue_certification_cost(5, probe_cost=Q(3))
        self.assertEqual(r["full_register_cost"], 15)          # 3 * 5
        self.assertEqual(r["hardest_pair_cost"], 15)           # 3 * 5

    def test_pairwise_cost_equals_fso_advance_plus_warmup(self):
        # exact Phase-5 <-> Phase-2 tie: probe cost == min_separation + 1
        for p in (2, 3, 4, 5, 6):
            tie = pc.pairwise_cost_is_fso_advance_plus_warmup(p)
            self.assertEqual(len(tie), p * (p - 1) // 2)       # all residue pairs
            for (r, s), (cost, advance_plus_one) in tie.items():
                self.assertEqual(cost, advance_plus_one)       # cost == (p - s) + 1


class TestCrossChecks(unittest.TestCase):
    def test_unit_cost_reproduces_existing_engine(self):
        # on the existing conditional_source_field, weighted unit-cost == rank
        c = conditional_source_field()
        sources, target = (0, 1, 2, 3), ("0", "1", "1", "0")
        cost = {"Q": Q(1), "R0": Q(1), "R1": Q(1)}
        v = pc.solve_weighted_adaptive(c, cost, sources, target, target_id="xor")
        rank = solve_adaptive_claim(c, sources, target, target_id="xor").rank
        self.assertEqual(v.cost, rank)
        self.assertEqual(v.cost, 2)

    def test_bruteforce_matches_value_iteration(self):
        # independent algorithm agreement on several instances
        c = conditional_source_field()
        cost = {"Q": Q(2), "R0": Q(1), "R1": Q(5)}      # non-unit, asymmetric costs
        v = pc.solve_weighted_adaptive(c, cost, (0, 1, 2, 3), ("0", "1", "1", "0"),
                                       target_id="xor")
        b = pc.bruteforce_worstcase_cost(c, cost, (0, 1, 2, 3), ("0", "1", "1", "0"))
        self.assertEqual(v.cost, b)
        for p in (2, 3, 4):
            field, s, t = pc.residue_observer_carrier(p)
            cc = {"S": Q(7, 2)}
            vv = pc.solve_weighted_adaptive(field, cc, s, t, target_id="r")
            bb = pc.bruteforce_worstcase_cost(field, cc, s, t)
            self.assertEqual(vv.cost, bb)


class TestExpectedMode(unittest.TestCase):
    def test_expected_cost_values(self):
        expected = {2: Q(2), 3: Q(8, 3), 4: Q(13, 4), 5: Q(19, 5)}
        for p, want in expected.items():
            field, s, t = pc.residue_observer_carrier(p)
            prior = {src: Q(1, p) for src in s}
            v = pc.solve_weighted_adaptive(field, {"S": Q(1)}, s, t,
                                           target_id="r", mode="expected", prior=prior)
            self.assertEqual(v.cost, want)

    def test_expected_below_worstcase_for_p3plus(self):
        for p in (3, 4, 5):
            field, s, t = pc.residue_observer_carrier(p)
            prior = {src: Q(1, p) for src in s}
            ec = pc.solve_weighted_adaptive(field, {"S": Q(1)}, s, t,
                                            target_id="r", mode="expected", prior=prior)
            wc = pc.solve_weighted_adaptive(field, {"S": Q(1)}, s, t, target_id="r")
            self.assertLess(ec.cost, wc.cost)

    def test_bad_prior_rejected(self):
        field, s, t = pc.residue_observer_carrier(3)
        with self.assertRaises(pc.ProbeCompilerError):
            pc.solve_weighted_adaptive(field, {"S": Q(1)}, s, t, target_id="r",
                                       mode="expected", prior={0: Q(1, 2), 1: Q(1, 2)})


class TestImpossibility(unittest.TestCase):
    def test_aliased_sources_impossibility_certificate(self):
        field, s, t = pc.aliased_carrier()
        v = pc.solve_weighted_adaptive(field, {"R": Q(1)}, s, t, target_id="x")
        self.assertFalse(v.winning)
        self.assertIsNone(v.cost)
        self.assertEqual(v.impossibility, (0, 1, "aliased: identical outputs under every probe word"))
        self.assertIsNone(pc.bruteforce_worstcase_cost(field, {"R": Q(1)}, s, t))


class TestSimulation(unittest.TestCase):
    def test_policy_certifies_every_source(self):
        for p in (2, 3, 4):
            field, s, t = pc.residue_observer_carrier(p)
            cost = {"S": Q(1)}
            v = pc.solve_weighted_adaptive(field, cost, s, t, target_id="r")
            for src in s:
                label, total, trace = pc.simulate_policy(field, v, cost, src, t)
                self.assertEqual(label, t[src])        # certified the true residue
                self.assertLessEqual(total, v.cost)    # within the worst-case bound

    def test_positive_cost_required(self):
        field, s, t = pc.residue_observer_carrier(3)
        with self.assertRaises(pc.ProbeCompilerError):
            pc.solve_weighted_adaptive(field, {"S": Q(0)}, s, t, target_id="r")
        with self.assertRaises(pc.ProbeCompilerError):
            pc.solve_weighted_adaptive(field, {"S": Q(-1)}, s, t, target_id="r")


if __name__ == "__main__":
    unittest.main()
