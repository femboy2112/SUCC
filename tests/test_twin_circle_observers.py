"""Exact twin-observer circle: identical capabilities, different mathematical focus.

The bench tests translation, finite probe scheduling, one-step testimony,
and strict post-reconciliation operational equality. These synthetic source
records are not authenticated empirical measurements of a physical observer.
"""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import json
import unittest

from observational_succ.circle_translation import (
    CirclePolynomial, TrigFourierPolynomial,
    cardinal_point, rational_stereographic_chart,
    winding_alias_for_rational_samples,
)
from observational_succ.twin_circle_observers import (
    CircleProbe, CircleEvent, TwinCircleBasis, TwinCircleObserver,
    TwinCircleError, translated_probe_report,
    evaluate_fourier_at_cardinal, normalized_tangent_in_polynomial_language,
    normalized_tangent_in_trig_language, hidden_smooth_loop_between_samples,
    encode_twin_relative_delta, decode_twin_relative_delta, twin_circle_demo,
)


def twins():
    points = tuple(CircleProbe("point", t) for t in
                   (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(1,8)))
    probes = points+(CircleProbe("tangent",Q(0)),)
    basis = TwinCircleBasis((1,5,9),probes)
    common = tuple(CircleEvent(i,probes[i].response(1),"shared")
                   for i in range(5))
    a = TwinCircleObserver("polynomial",tuple(range(7)),common)
    b = TwinCircleObserver("trigonometric",(6,5,0,1,2,3,4),common)
    return basis,a,b


class TwinCircleTests(unittest.TestCase):
    def test_same_source_knowledge_opportunity_and_inference_power(self):
        basis,a,b=twins()
        self.assertEqual(a.validate(basis),(1,5,9))
        self.assertEqual(b.validate(basis),(1,5,9))
        self.assertEqual(a.available(basis),b.available(basis))
        self.assertEqual(a.normalized_semantic_position(basis),
                         b.normalized_semantic_position(basis))
        self.assertEqual(a.knowledge_position(basis),
                         b.knowledge_position(basis))
        self.assertEqual(a.next_preferred_probe(basis),5)
        self.assertEqual(b.next_preferred_probe(basis),6)
        self.assertEqual(basis.reasoning_signature,
                         "exact-rational-circle-ring-plus-angular-derivative-v1")
        self.assertEqual(a.records,b.records)

    def test_focus_changes_actual_experiment_not_physical_capability(self):
        basis,a,b=twins()
        after_a=a.local_succ(basis,1)
        after_b=b.local_succ(basis,1)
        self.assertEqual(after_a.available(basis),after_b.available(basis))
        self.assertEqual(after_a.validate(basis),(1,9))
        self.assertEqual(after_b.validate(basis),(1,))
        self.assertEqual(after_a.records[-1].probe_index,5)
        self.assertEqual(after_b.records[-1].probe_index,6)
        self.assertEqual(after_a.local_steps,1)
        self.assertEqual(after_b.local_steps,1)
        self.assertEqual(after_a.knowledge_aided_steps,0)
        self.assertEqual(after_b.knowledge_aided_steps,0)

    def test_one_remote_succ_copies_knowledge_not_physical_event_or_full_history(self):
        basis,a,b=twins()
        a=a.local_succ(basis,1)
        b=b.local_succ(basis,1)
        packet=encode_twin_relative_delta(b,a,basis)
        d=json.loads(packet.decode("utf-8"))
        self.assertEqual(d["protocol"],"twin-circle-relative-v1")
        self.assertEqual(d["steps"],[[0,0,"trigonometric"]])
        self.assertNotIn("absolute_winding",d)
        self.assertNotIn("source_state",d)
        informed=decode_twin_relative_delta(a,packet,basis)
        self.assertEqual(informed.validate(basis),(1,))
        self.assertEqual(informed.knowledge_position(basis),b.knowledge_position(basis))
        self.assertNotEqual(informed.normalized_semantic_position(basis),
                            b.normalized_semantic_position(basis))
        self.assertEqual(informed.local_steps,a.local_steps)
        self.assertEqual(informed.knowledge_aided_steps,1)
        self.assertEqual(informed.records[-1].origin,"trigonometric")

    def test_two_way_epistemic_exchange_aligns_future_single_use_probes(self):
        basis,a,b=twins()
        a=a.local_succ(basis,1)
        b=b.local_succ(basis,1)
        informed_a=decode_twin_relative_delta(a,encode_twin_relative_delta(b,a,basis),basis)
        informed_b=decode_twin_relative_delta(b,encode_twin_relative_delta(informed_a,b,basis),basis)
        self.assertEqual(informed_a.normalized_semantic_position(basis),
                         informed_b.normalized_semantic_position(basis))
        self.assertEqual(informed_a.validate(basis),informed_b.validate(basis))
        self.assertEqual(informed_a.available(basis),informed_b.available(basis))
        self.assertEqual(informed_a.local_steps,1)
        self.assertEqual(informed_b.local_steps,1)
        self.assertEqual(informed_a.knowledge_aided_steps,1)
        self.assertEqual(informed_b.knowledge_aided_steps,1)
        self.assertNotEqual(informed_a.records,informed_b.records)
        self.assertEqual(informed_a.records[-2].origin,"polynomial")
        self.assertEqual(informed_b.records[-2].origin,"trigonometric")
        # With identical future menu, different focus may choose different
        # *order*, but neither observer is denied any physical observation.
        self.assertEqual(
            {i for i in informed_a.available(basis)
             if i not in {e.probe_index for e in informed_a.records}},
            {i for i in informed_b.available(basis)
             if i not in {e.probe_index for e in informed_b.records}},
        )

    def test_shared_raw_probe_results_translate_to_both_mathematical_languages(self):
        x,y=CirclePolynomial.x(),CirclePolynomial.y()
        test_points=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
        for t in test_points:
            assert cardinal_point(int(4*t),1) is not None
            for a,b in product(range(4),repeat=2):
                f=x.power(a)*y.power(b)
                report_a,report_b=translated_probe_report(f,t)
                self.assertEqual(report_a,report_b)
            relation=x*x+y*y-CirclePolynomial.scalar(1)
            self.assertEqual(translated_probe_report(relation,t),(Q(0),Q(0)))
        with self.assertRaises(TwinCircleError):
            translated_probe_report(x,Q(1,8))
        with self.assertRaises(TwinCircleError):
            evaluate_fourier_at_cardinal(TrigFourierPolynomial.cos(),Q(1,8))

    def test_tangent_observation_has_exact_same_polynomial_and_trig_result(self):
        # On uniform gamma_k, the normalized tangent/area-form contraction
        # is exactly the integer k. This ONE probe removes the old
        # point-sampling-only omega ambiguity for this declared family.
        for numerator,denominator in [(-3,7),(0,1),(1,2),(2,3),(3,1)]:
            x,y=rational_stereographic_chart(Q(numerator,denominator))
            for winding in (-9,-3,-1,0,1,5,9):
                value_a=normalized_tangent_in_polynomial_language(x,y,winding)
                value_b=normalized_tangent_in_trig_language(winding)
                self.assertEqual(value_a,value_b)
                self.assertEqual(value_a,Q(winding))
        with self.assertRaises(TwinCircleError):
            normalized_tangent_in_polynomial_language(0,0,1)

    def test_same_sparse_data_ambiguity_affects_both_twins(self):
        basis,a,b=twins()
        times=tuple(p.time for p in basis.probes if p.kind=="point")[:5]
        alias=winding_alias_for_rational_samples(1,times)
        self.assertEqual(alias.aliased_turns,5)
        self.assertTrue(alias.finite_samples_equal)
        self.assertEqual(a.validate(basis),b.validate(basis))
        self.assertEqual(a.validate(basis),(1,5,9))
        self.assertFalse(a.knowledge_position(basis)[1] == (1,))

    def test_finite_full_jet_samples_cannot_reveal_hidden_smooth_loop(self):
        samples=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
        plan=hidden_smooth_loop_between_samples(samples,1)
        left,right=plan.open_gap
        self.assertGreater(right,left)
        self.assertTrue(all(not left<t<right for t in plan.sample_times))
        self.assertEqual(plan.original_winding,1)
        self.assertEqual(plan.shifted_winding,2)
        self.assertTrue(plan.all_finite_sample_jets_same_by_flat_step_proof)
        self.assertFalse(plan.physical_infinite_jet_measurements_executed)
        with self.assertRaises(TwinCircleError):
            hidden_smooth_loop_between_samples((1.25,),1)

    def test_probe_and_language_schema_strict_controls(self):
        basis,a,b=twins()
        with self.assertRaises(TwinCircleError):
            CircleProbe("xray",Q(0))
        with self.assertRaises(TwinCircleError):
            CircleProbe("point",Q(2))
        with self.assertRaises(TwinCircleError):
            CircleProbe("point",0.1)
        with self.assertRaises(TwinCircleError):
            TwinCircleBasis(basis.winding_sources,basis.probes,orientation=-1)
        with self.assertRaises(TwinCircleError):
            TwinCircleBasis((1,1),basis.probes)
        with self.assertRaises(TwinCircleError):
            TwinCircleBasis(basis.winding_sources,basis.probes+(basis.probes[0],))
        with self.assertRaises(TwinCircleError):
            replace(a,focus_order=(5,6)).validate(basis)
        with self.assertRaises(TwinCircleError):
            replace(a,language="nope").validate(basis)
        with self.assertRaises(TwinCircleError):
            replace(a,records=a.records+(a.records[0],)).validate(basis)

    def test_relay_disallows_forged_unknown_values_and_old_context(self):
        basis,a,b=twins()
        a=a.local_succ(basis,1)
        b=b.local_succ(basis,1)
        packet=json.loads(encode_twin_relative_delta(b,a,basis).decode())
        for change in (
            lambda d:d.update(basis="not-the-shared-basis"),
            lambda d:d.update(start="stale"),
            lambda d:d.update(end="bad"),
            lambda d:d.update(steps=[[0,None,"trigonometric"]]),
            lambda d:d.update(steps=[[0,False,"trigonometric"]]),
            lambda d:d.update(steps=[[0,5,"trigonometric"]]),
            lambda d:d.update(steps=[[99,0,"trigonometric"]]),
        ):
            altered=json.loads(json.dumps(packet))
            change(altered)
            with self.subTest(altered=altered):
                with self.assertRaises(TwinCircleError):
                    decode_twin_relative_delta(a,json.dumps(altered).encode(),basis)
        changed=TwinCircleBasis(basis.winding_sources,basis.probes,
                                 reasoning_signature="a different purported law")
        with self.assertRaises(TwinCircleError):
            decode_twin_relative_delta(a,json.dumps(packet).encode(),changed)

    def test_same_raw_observation_history_cannot_produce_different_laws(self):
        basis,a,b=twins()
        for k in range(len(basis.probes)):
            # Force SAME empirical probe (not focus-driven), then recompute
            # both absorptions through independent language representations.
            probe=basis.probes[k]
            obs=CircleEvent(k,probe.response(1),"shared")
            if all(e.probe_index!=k for e in a.records):
                a=replace(a,records=a.records+(obs,))
                b=replace(b,records=b.records+(obs,))
            self.assertEqual(a.knowledge_position(basis),
                             b.knowledge_position(basis))
            self.assertEqual(a.normalized_semantic_position(basis),
                             b.normalized_semantic_position(basis))
        self.assertEqual(a.validate(basis),(1,))
        self.assertEqual(b.validate(basis),(1,))

    def test_twin_demo_explicitly_does_not_assert_physical_authentication(self):
        r=twin_circle_demo()
        self.assertEqual(r["status"],"EXACT_TWIN_OBSERVER_LANGUAGE_INVARIANCE")
        self.assertTrue(r["initial_mathematical_knowledge_equal"])
        self.assertTrue(r["physical_probe_capabilities_identical"])
        self.assertTrue(r["reasoning_capability_identical"])
        self.assertEqual(r["initial_candidate_windings"],[1,5,9])
        self.assertEqual(r["after_polynomial_focus_candidates"],[1,9])
        self.assertEqual(r["after_trig_focus_candidates"],[1])
        self.assertTrue(r["post_first_relay_knowledge_equal"])
        self.assertFalse(r["post_first_relay_operational_history_equal"])
        self.assertTrue(r["post_reciprocal_relay_operational_position_equal"])
        self.assertTrue(r["algebraic_and_trig_normalized_tangent_agree"])
        self.assertTrue(r["smooth_path_finite_jets_can_still_hide_an_extra_loop"])
        self.assertFalse(r["full_physical_continuum_trajectory_measured"])
        self.assertFalse(r["source_provenance_cryptographically_authenticated"])
        self.assertFalse(r["RH_claimed"])


if __name__=="__main__":
    unittest.main()
