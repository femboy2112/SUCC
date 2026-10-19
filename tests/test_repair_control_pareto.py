"""Exact controls for the repair/control 3-way Pareto frontier.

Independent oracles recompute the Gini mutual information from the Bayes
posterior (not the production summation identity) and the carrier fidelity by
brute survival. All arithmetic is exact ``Fraction``; no float appears.
"""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.repair_control_pareto import (
    RepairControlError, Source, Probe, ScheduledProbe, Vertex,
    RepairControlModel, gini,
)


def perfect(target, cost, destructive, symbols=(0, 1)):
    channel = tuple((s, tuple((o, Q(1) if o == s else Q(0)) for o in symbols))
                    for s in symbols)
    return Probe(f"{'D' if destructive else 'N'}{target}", target, channel,
                 Q(cost), destructive)


def model():
    # Correlated binary pair; marginals are both fair coins (Gini 1/2 each).
    source = Source(2, (
        ((0, 0), Q(2, 5)), ((0, 1), Q(1, 10)),
        ((1, 0), Q(1, 10)), ((1, 1), Q(2, 5)),
    ))
    noisy = Probe("P", 1, (
        (0, ((0, Q(3, 4)), (1, Q(1, 4)))),
        (1, ((0, Q(1, 4)), (1, Q(3, 4)))),
    ), Q(1, 10), False)
    probes = (
        perfect(1, Q(3, 10), False),   # N1 perfect non-destructive on X1
        perfect(1, Q(1, 10), True),    # D1 perfect destructive on X1 (cheaper)
        perfect(2, Q(3, 10), False),   # N2 perfect non-destructive on X2
        noisy,                         # P  imperfect (noisy) on X1
    )
    return RepairControlModel(source, probes, arrivals=(1, 2))


def oracle_retained(m, schedule):
    """Independent Gini MI via explicit Bayes posteriors."""
    joint = m.source.joint()
    prior_gini = gini(tuple(joint.items()))
    probes = [m.probes[p] for p in schedule]
    if not probes:
        return Q(0)
    alphabets = [sorted({o for _, obs in p.channel for o, _ in obs}, key=repr)
                 for p in probes]
    # P(x, y)
    pxy = {}
    for outcome, px in joint.items():
        for combo in product(*alphabets):
            w = px
            for p, y in zip(probes, combo):
                w *= dict(p.row(outcome[p.target - 1])).get(y, Q(0))
            if w:
                pxy[(outcome, combo)] = pxy.get((outcome, combo), Q(0)) + w
    py = {}
    for (outcome, combo), w in pxy.items():
        py[combo] = py.get(combo, Q(0)) + w
    expected_post = Q(0)
    for combo, p_y in py.items():
        post = {outcome: w / p_y for (outcome, c), w in pxy.items() if c == combo}
        expected_post += p_y * (Q(1) - sum(v * v for v in post.values()))
    return prior_gini - expected_post


def oracle_fidelity(m, schedule):
    destroyed = {m.probes[p].target for p in schedule if m.probes[p].destructive}
    total = Q(0)
    for i in range(1, m.source.arity + 1):
        if i not in destroyed:
            total += gini(tuple(m.source.marginal(i).items()))
    return total


class RepairControlParetoTest(unittest.TestCase):
    def setUp(self):
        self.m = model()
        self.all_schedules = tuple(
            tuple(s for s, keep in zip(("N1", "D1", "N2", "P"), mask) if keep)
            for mask in product((0, 1), repeat=4))

    def test_pinned_exact_values(self):
        m = self.m
        self.assertEqual(m.retained_information(()), Q(0))
        self.assertEqual(m.retained_information(("N1",)), Q(17, 50))
        self.assertEqual(m.retained_information(("D1",)), Q(17, 50))
        self.assertEqual(m.carrier_fidelity(()), Q(1))
        self.assertEqual(m.carrier_fidelity(("D1",)), Q(1, 2))
        self.assertEqual(m.carrier_fidelity(("N1",)), Q(1))
        self.assertEqual(m.acquisition_cost(("N1", "N2")), Q(3, 5))
        # Full perfect non-destructive recovers the full prior Gini.
        self.assertEqual(m.retained_information(("N1", "N2")),
                         gini(tuple(m.source.joint().items())))

    def test_matches_independent_bayes_oracle(self):
        for s in self.all_schedules:
            self.assertEqual(self.m.retained_information(s), oracle_retained(self.m, s))
            self.assertEqual(self.m.carrier_fidelity(s), oracle_fidelity(self.m, s))

    def test_retained_information_nonnegative_and_monotone(self):
        m = self.m
        for s in self.all_schedules:
            self.assertGreaterEqual(m.retained_information(s), Q(0))
        # Adding a probe never decreases retained information (data processing).
        base = m.retained_information(("N1",))
        self.assertGreaterEqual(m.retained_information(("N1", "N2")), base)
        self.assertGreaterEqual(m.retained_information(("N1", "P")), base)
        # Imperfect probe retains strictly less than the perfect one.
        self.assertLess(m.retained_information(("P",)), m.retained_information(("N1",)))

    def test_all_objective_records_disclaim_rh(self):
        for s in self.all_schedules:
            self.assertEqual(self.m.objectives(s)["RH_proved"], False)
            self.assertEqual(self.m.objectives(s)["status"], "VERIFIED-EXACT-MODEL")
        self.assertEqual(self.m.classical_corner()["RH_proved"], False)

    def test_frontier_is_nondominated_and_complete(self):
        m = self.m
        frontier = m.pareto_frontier(self.all_schedules)
        fset = {(v.retained, v.cost, v.fidelity) for v in frontier}
        # No frontier vertex dominates another.
        for a in frontier:
            for b in frontier:
                if a is not b:
                    self.assertFalse(m.dominates(a, b))
        # Every candidate is dominated by (or equal to) some frontier vertex.
        for s in self.all_schedules:
            v = m.vertex(s)
            key = (v.retained, v.cost, v.fidelity)
            self.assertTrue(key in fset
                            or any(m.dominates(w, v) for w in frontier))

    def test_destructive_and_nondestructive_are_both_boundary(self):
        # Same R, but D1 wins on cost and N1 wins on fidelity -> both Pareto.
        m = self.m
        frontier = m.pareto_frontier(self.all_schedules)
        keys = {(v.retained, v.cost, v.fidelity) for v in frontier}
        self.assertIn((Q(17, 50), Q(1, 10), Q(1, 2)), keys)   # D1
        self.assertIn((Q(17, 50), Q(3, 10), Q(1)), keys)      # N1

    def test_classical_corner_is_limiting_and_dominant(self):
        m = self.m
        corner = m.classical_corner()
        self.assertEqual(corner["retained"], gini(tuple(m.source.joint().items())))
        self.assertEqual(corner["cost"], Q(0))
        self.assertEqual(corner["fidelity"], Q(1))
        ideal = Vertex((), corner["retained"], corner["cost"], corner["fidelity"])
        # The free lossless corner dominates every costly/destructive schedule.
        for s in self.all_schedules:
            v = m.vertex(s)
            if (v.retained, v.cost, v.fidelity) != (
                    ideal.retained, ideal.cost, ideal.fidelity):
                self.assertTrue(m.dominates(ideal, v))
        # ...yet it is unreachable in the actual costly catalog: no zero-cost
        # schedule attains full retained information.
        for s in self.all_schedules:
            if m.acquisition_cost(s) == 0:
                self.assertLess(m.retained_information(s), corner["retained"])

    def test_realizable_static_policies_pass(self):
        m = self.m
        for s in self.all_schedules:
            if s:
                audit = m.audit_realizability(m.static_policy(s))
                self.assertTrue(audit["realizable"])
                self.assertEqual(audit["RH_proved"], False)

    def test_falsifier_acausal_improvement_rejected(self):
        m = self.m
        # A prescient "improvement": decide the cheap destructive probe on X1
        # at t=1 by conditioning on an observation of X2 that only exists at t=2.
        prescient = (
            ScheduledProbe("N2", 2, ()),
            ScheduledProbe("D1", 1, conditions_on=("N2",)),
        )
        audit = m.audit_realizability(prescient)
        self.assertFalse(audit["realizable"])
        self.assertEqual(audit["violation"][0], "acausal")
        with self.assertRaises(RepairControlError):
            m.reject_acausal_improvement(prescient)
        # A premature probe (before its datum arrives) is also rejected.
        premature = (ScheduledProbe("N2", 1, ()),)   # X2 arrives at t=2
        self.assertFalse(m.audit_realizability(premature)["realizable"])
        self.assertEqual(m.audit_realizability(premature)["violation"][0], "premature")

    def test_lawful_adaptive_conditioning_accepted(self):
        m = self.m
        lawful = (
            ScheduledProbe("N1", 1, ()),
            ScheduledProbe("N2", 2, conditions_on=("N1",)),  # conditions on past
        )
        self.assertTrue(m.reject_acausal_improvement(lawful)["realizable"])

    def test_malformed_inputs_rejected(self):
        with self.assertRaises(RepairControlError):
            Source(2, (((0, 0), Q(1, 2)),))                  # probs don't sum to 1
        with self.assertRaises(RepairControlError):
            Source(2, (((0,), Q(1)),))                       # wrong arity tuple
        with self.assertRaises(RepairControlError):
            Probe("x", 1, ((0, ((0, Q(1, 2)),)),), Q(1), False)  # row sums to 1/2
        with self.assertRaises(RepairControlError):
            Probe("x", 1, ((0, ((0, Q(1)),)),), Q(-1), False)    # negative cost
        with self.assertRaises(RepairControlError):
            self.m.retained_information(("N1", "N1"))        # duplicate in schedule
        with self.assertRaises(RepairControlError):
            self.m.retained_information(("ghost",))          # unknown probe
        with self.assertRaises(RepairControlError):
            RepairControlModel(self.m.source,
                               (perfect(1, Q(1), False),), arrivals=(1,))  # arity


if __name__ == "__main__":
    unittest.main()
