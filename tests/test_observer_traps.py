"""Adversarial finite observational-SUCC access and scheduling laboratory."""
from dataclasses import replace
from itertools import product
import unittest

from observational_succ.observer_traps import (
    FiniteProbeWorld, ObserverFrame, ObserverTrapError, ProbePolicy,
    ProbeStep, certify_stationary_pair, observer_trap_demo,
)


def two_source_world():
    return FiniteProbeWorld(("A", "B"), ("echo", "separator"),
                            (("same", "A"), ("same", "B")))


class ObserverTrapTests(unittest.TestCase):
    def test_self_confirming_wrong_model_with_exhaustive_local_assimilation(self):
        w = two_source_world()
        p = ProbePolicy((("A", ("echo",)), ("B", ("echo", "separator"))))
        f = ObserverFrame.initial(w, p, "A")
        c = certify_stationary_pair(w, p, f, "B")
        self.assertEqual(c.status, "access-trap")
        self.assertEqual(c.globally_separating, ("separator",))
        self.assertEqual(c.admissible_menu, ("echo",))
        self.assertEqual(c.future_support, ("echo",))
        self.assertEqual(c.stationary_future_fiber, ("A", "B"))
        self.assertIsNone(c.first_refuting_succ)
        self.assertTrue(c.self_confirming_false_model)
        self.assertFalse(c.observer_can_infer_actual_from_this_certificate)
        for _ in range(12):
            f = f.succ(w, p, "B")
            self.assertEqual(f.preferred, "A")
            self.assertEqual(f.compatible, ("A", "B"))
            self.assertFalse(f.identified)
        self.assertTrue(f.verify(w, p, "B"))
        self.assertEqual(tuple(step.probes for step in f.history), (("echo",),)*12)
        self.assertTrue(all(step.origin == "policy" for step in f.history))
        self.assertEqual(f.compatible, c.stationary_future_fiber)

    def test_exogenous_discriminator_corrects_model_with_authorized_event(self):
        w = two_source_world()
        p = ProbePolicy((("A", ("echo",)), ("B", ("echo", "separator"))))
        f = ObserverFrame.initial(w, p, "A").succ(w, p, "B")
        repaired = f.intervene(w, p, "B", ("separator",))
        self.assertEqual(repaired.compatible, ("B",))
        self.assertEqual(repaired.preferred, "B")
        self.assertTrue(repaired.identified)
        self.assertEqual(repaired.history[-1].origin, "external")
        self.assertTrue(repaired.verify(w, p, "B"))
        # The old actualized echo result is preserved, not retroactively rewritten.
        self.assertEqual(repaired.history[0], f.history[0])
        with self.assertRaises(ObserverTrapError):
            f.intervene(w, p, "B", ("nonexistent",))

    def test_union_of_compatible_model_menus_breaks_epistemic_trap(self):
        w = two_source_world()
        menus = (("A", ("echo",)), ("B", ("echo", "separator")))
        union = ProbePolicy(menus, scope="compatible_union")
        f = ObserverFrame.initial(w, union, "A")
        self.assertEqual(union.accessible(f, w), ("echo", "separator"))
        solved = f.succ(w, union, "B")
        self.assertTrue(solved.identified)
        self.assertEqual(solved.compatible, ("B",))
        self.assertEqual(solved.history[0].origin, "policy")
        self.assertTrue(solved.verify(w, union, "B"))
        # Stationary theorem cannot be applied to menu-changing union scope.
        with self.assertRaises(ObserverTrapError):
            certify_stationary_pair(w, union, f, "B")

    def test_scheduling_trap_and_round_robin_escape(self):
        w = two_source_world()
        menus = (("A", ("echo", "separator")), ("B", ("echo", "separator")))
        bad = ProbePolicy(menus, scheduling="first")
        good = ProbePolicy(menus, scheduling="round_robin")
        f_bad = ObserverFrame.initial(w, bad, "A")
        cert_bad = certify_stationary_pair(w, bad, f_bad, "B")
        self.assertEqual(cert_bad.status, "scheduling-trap")
        self.assertEqual(cert_bad.locally_separating, ("separator",))
        self.assertEqual(cert_bad.eventually_selected_separators, ())
        for _ in range(8):
            f_bad = f_bad.succ(w, bad, "B")
        self.assertFalse(f_bad.identified)
        cert_good = certify_stationary_pair(
            w, good, ObserverFrame.initial(w, good, "A"), "B")
        self.assertEqual(cert_good.status, "eventual-discrimination")
        self.assertEqual(cert_good.first_refuting_succ, 2)
        f_good = ObserverFrame.initial(w, good, "A").succ(w, good, "B")
        self.assertFalse(f_good.identified)
        f_good = f_good.succ(w, good, "B")
        self.assertTrue(f_good.identified)
        self.assertEqual(f_good.preferred, "B")

    def test_globally_indistinguishable_pair_is_not_just_bad_policy(self):
        w = FiniteProbeWorld(("A", "B"), ("echo", "other"),
                             (("same", "value"), ("same", "value")))
        p = ProbePolicy((("A", w.probes), ("B", w.probes)))
        f = ObserverFrame.initial(w, p, "A")
        cert = certify_stationary_pair(w, p, f, "B")
        self.assertEqual(cert.status, "global-probe-blind")
        self.assertEqual(cert.globally_separating, ())
        self.assertEqual(cert.stationary_future_fiber, ("A", "B"))
        for _ in range(4):
            f = f.succ(w, p, "B")
        self.assertEqual(f.compatible, ("A", "B"))
        self.assertFalse(f.identified)

    def test_rational_correction_can_lead_to_new_stable_false_model(self):
        # Initial favorite A is refuted, so observer rationally adopts B.
        # Its revised menu is still blind to true C. This is a DYNAMIC trap.
        w = FiniteProbeWorld(
            ("A", "B", "C"), ("broad", "fine"),
            (("0", "0"), ("1", "0"), ("1", "1")),
        )
        p = ProbePolicy(
            (("A", ("broad",)), ("B", ("broad",)),
             ("C", ("broad", "fine"))))
        f = ObserverFrame.initial(w, p, "A")
        self.assertEqual(
            certify_stationary_pair(w, p, f, "C").status,
            "eventual-discrimination",
        )
        f = f.succ(w, p, "C")
        self.assertEqual(f.compatible, ("B", "C"))
        self.assertEqual(f.preferred, "B")
        self.assertEqual(
            certify_stationary_pair(w, p, f, "C").status, "access-trap",
        )
        for _ in range(9):
            f = f.succ(w, p, "C")
        self.assertEqual(f.preferred, "B")
        self.assertEqual(f.compatible, ("B", "C"))
        widened = ProbePolicy(p.menus, scope="compatible_union")
        # An alternative observer can use the compatible-class union at this
        # already-observed history, but must begin under matching policy.
        corrected = ObserverFrame.initial(w, widened, "A").succ(w, widened, "C")
        self.assertEqual(corrected.compatible, ("C",))

    def test_replay_rejects_forged_outcomes_and_false_preferred_update(self):
        w = two_source_world()
        p = ProbePolicy((("A", ("echo",)), ("B", ("echo", "separator"))))
        f = ObserverFrame.initial(w, p, "A").succ(w, p, "B")
        forged = replace(f, history=(ProbeStep("policy", "A", ("echo",), ("not-same",)),))
        with self.assertRaises(ObserverTrapError):
            forged.verify(w, p, "B")
        forged_model = replace(f, preferred="B")
        with self.assertRaises(ObserverTrapError):
            forged_model.verify(w, p, "B")
        forbidden = replace(f, compatible=("A",))
        with self.assertRaises(ObserverTrapError):
            forbidden.succ(w, p, "B")
        with self.assertRaises(ObserverTrapError):
            f.verify(w, p, "not-in-world")

    def test_invalid_source_and_policy_typing(self):
        with self.assertRaises(ObserverTrapError):
            FiniteProbeWorld(("A", "A"), ("p",), (("0",), ("1",)))
        with self.assertRaises(ObserverTrapError):
            FiniteProbeWorld(("A", "B"), ("p",), (("0",),))
        with self.assertRaises(ObserverTrapError):
            FiniteProbeWorld(("A", "B"), ("p",), ((0,), ("1",)))
        w = two_source_world()
        with self.assertRaises(ObserverTrapError):
            ProbePolicy((("A", ("echo",)), ("B", ("bogus",)))).validate(w)
        with self.assertRaises(ObserverTrapError):
            ProbePolicy((("A", ("echo",)),)).validate(w)
        with self.assertRaises(ObserverTrapError):
            ProbePolicy((("A", ("echo",)), ("B", ("echo",))),
                        scheduling="magical")
        with self.assertRaises(ObserverTrapError):
            ProbePolicy((("A", ("echo",)), ("B", ("echo",))),
                        scope="secret-source")
        with self.assertRaises(ObserverTrapError):
            ProbePolicy((("A", ()), ("B", ("echo",))))
        with self.assertRaises(ObserverTrapError):
            ObserverFrame.initial(
                w, ProbePolicy((("A", ("echo",)), ("B", ("echo",)))), "C")

    def test_exhaustive_two_source_probe_tables_against_future_trajectories(self):
        # 2^4 exact response tables × 3^2 model menus × 3 scheduling
        # regimes × two orientations = 864 distinct small-world controls.
        names = ("p", "q")
        menus = (("p",), ("q",), ("p", "q"))
        comparisons = 0
        for raw in product(("0", "1"), repeat=4):
            w = FiniteProbeWorld(("A", "B"), names,
                                 (tuple(raw[:2]), tuple(raw[2:])))
            for ma, mb in product(menus, repeat=2):
                for mode in ("all", "first", "round_robin"):
                    pol = ProbePolicy((("A", ma), ("B", mb)),
                                      scheduling=mode)
                    for actual, pref in (("A", "B"), ("B", "A")):
                        f = ObserverFrame.initial(w, pol, pref)
                        cert = certify_stationary_pair(w, pol, f, actual)
                        first = None
                        for step in range(1, 5):
                            f = f.succ(w, pol, actual)
                            if f.preferred != pref and first is None:
                                first = step
                        self.assertEqual(first, cert.first_refuting_succ)
                        if first is None:
                            self.assertEqual(f.preferred, pref)
                            self.assertEqual(f.compatible,
                                             cert.stationary_future_fiber)
                            self.assertTrue(cert.self_confirming_false_model)
                        else:
                            self.assertEqual(f.compatible, (actual,))
                            self.assertFalse(cert.self_confirming_false_model)
                        comparisons += 1
        self.assertEqual(comparisons, 864)

    def test_exact_paired_menu_union_separates_every_finite_candidate(self):
        # If for every x!=y, some probe in A(x) union A(y) distinguishes
        # them, exhaustive compatible-union observing separates all sources
        # in ONE SUCC frame. 3 sources × 2 probes binary exhaustive worlds.
        names = ("p", "q")
        all_menus = (("p",), ("q",), ("p", "q"))
        checked = 0
        guaranteed = 0
        for raw in product(("0", "1"), repeat=6):
            w = FiniteProbeWorld(("A", "B", "C"), names,
                                 tuple(tuple(raw[i:i+2])
                                       for i in (0, 2, 4)))
            for choices in product(all_menus, repeat=3):
                pol = ProbePolicy(tuple(zip(w.sources, choices)),
                                  scope="compatible_union")
                pairwise = all(any(
                    w.outcome(x, probe) != w.outcome(y, probe)
                    for probe in set(pol.menu(x)) | set(pol.menu(y)))
                    for i, x in enumerate(w.sources)
                    for y in w.sources[i+1:])
                for actual in w.sources:
                    f = ObserverFrame.initial(w, pol, "A").succ(w, pol, actual)
                    if pairwise:
                        self.assertTrue(f.identified)
                        guaranteed += 1
                    checked += 1
        self.assertEqual(checked, 64 * 27 * 3)
        self.assertGreater(guaranteed, 0)

    def test_counterfactual_truths_yield_identical_endogenous_histories(self):
        # Two possible worlds share the same observations and semantic state.
        # A history-only completion report cannot be correct for both.
        w = two_source_world()
        pol = ProbePolicy((("A", ("echo",)), ("B", ("echo", "separator"))))
        fa = ObserverFrame.initial(w, pol, "A")
        fb = ObserverFrame.initial(w, pol, "A")
        for _ in range(8):
            fa = fa.succ(w, pol, "A")
            fb = fb.succ(w, pol, "B")
            self.assertEqual(fa, fb)
        self.assertFalse(fa.identified)
        self.assertTrue(fa.verify(w, pol, "A"))
        self.assertTrue(fb.verify(w, pol, "B"))

    def test_union_probe_coverage_is_not_equivalent_to_pairwise_menus(self):
        # Only model C has q in its menu. q nevertheless distinguishes all
        # three sources, so union of compatible menus is sufficient.
        w = FiniteProbeWorld(
            ("A", "B", "C"), ("echo", "q"),
            (("same", "a"), ("same", "b"), ("same", "c")),
        )
        pol = ProbePolicy(
            (("A", ("echo",)), ("B", ("echo",)), ("C", ("q",))),
            scope="compatible_union",
        )
        self.assertFalse(any(
            w.outcome("A", probe) != w.outcome("B", probe)
            for probe in set(pol.menu("A")) | set(pol.menu("B"))))
        for source in w.sources:
            f = ObserverFrame.initial(w, pol, "A").succ(w, pol, source)
            self.assertTrue(f.identified)
            self.assertEqual(f.compatible, (source,))

    def test_machine_readable_demo_respects_truth_boundary(self):
        r = observer_trap_demo()
        self.assertEqual(r["status"], "FINITE_OBSERVER_TRAP_CERTIFIED")
        self.assertEqual(r["five_succ_updates_preferred"], "A")
        self.assertEqual(r["five_succ_updates_compatible"], ["A", "B"])
        self.assertTrue(r["external_intervention_identified"])
        self.assertTrue(r["compatible_union_identified"])
        self.assertEqual(r["round_robin_first_refutation_succ"], 2)
        self.assertFalse(r["source_records_rewritten"])
        self.assertFalse(r["physical_cognition_claimed"])
        self.assertFalse(r["RH_or_Godel_independence_claimed"])


if __name__ == "__main__":
    unittest.main()
