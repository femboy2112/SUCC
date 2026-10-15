"""Independent exact and hostile controls for coupling discovery.

The exhaustive multiplication/word/decoder checks below use elementary
reference oracles, not the optimized recursive policy search as an oracle.
"""
import unittest
import json
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations, product

from observational_succ.structural_coupling import (
    CyclicExtension, CouplingError, EventReceipt, ObserverContract, OutOfModel,
    PolicyLeaf, PolicyNode, abstract_isomorphism_classes, discover_couplings,
    exact_posterior, gauge_change, gauge_key, gauge_map, groups_isomorphic,
    normalized_cocycle, quotient_darkness_certificate, replay_policy,
    simulate_trace, transcript_signature, verify_gauge_map, winning_policy,
    theoretical_extension_count, cohomology_signature, lift_wrap, cyclic_norm,
    gauge_transported_transcripts, rank_actions_by_target_gain,
)


def frame(actions=((0, 1),), report="kernel", epoch=17):
    return ObserverContract("declared_source", "fixed_basis", epoch, actions, report)


def brute_tables(k, q, multiplier):
    """Independent raw associative table oracle, not the cocycle equation."""
    models = []
    for v in product(range(k), repeat=(q-1)**2):
        f = normalized_cocycle(k, q, v)
        states = tuple(product(range(k), range(q)))
        def op(a, b):
            return ((a[0] + pow(multiplier,a[1],k)*b[0] + f[a[1]*q+b[1]]) % k,
                    (a[1] + b[1]) % q)
        associative = all(op(op(x,y),z)==op(x,op(y,z))
                          for x,y,z in product(states,repeat=3))
        if associative:
            models.append(f)
    return models


def brute_shortest_word(models, actions, mode, labels, depth_limit):
    """All uniform words oracle; for two deterministic hypotheses adaptation adds nothing."""
    for n in range(depth_limit+1):
        for word in product(actions, repeat=n):
            sigs = transcript_signature(models,frame(actions,mode),word)
            if all(labels[i] == labels[j] or sigs[i] != sigs[j]
                   for i in range(len(models)) for j in range(len(models))):
                return n
    return None


class TestFiniteExtensions(unittest.TestCase):
    def test_first_family_two_extensions_two_nonisomorphic_groups(self):
        d = discover_couplings(2, 2)
        self.assertEqual((d.raw_cocycles,len(d.candidates),d.actions),(2,2,(1,)))
        self.assertEqual([c.order_histogram() for c in d.candidates], [
            ((1,1),(2,3)), ((1,1),(2,1),(4,2))])
        self.assertEqual(abstract_isomorphism_classes(d.candidates),((0,),(1,)))
        self.assertFalse(groups_isomorphic(*d.candidates))

    def test_second_family_action_discovers_six_element_nonabelian_group(self):
        d=discover_couplings(3,2)
        self.assertEqual((d.raw_cocycles,len(d.candidates),d.actions),(4,2,(1,2)))
        self.assertEqual([c.is_abelian() for c in d.candidates],[True,False])
        self.assertFalse(groups_isomorphic(*d.candidates))
        self.assertEqual(abstract_isomorphism_classes(d.candidates),((0,),(1,)))

    def test_third_family_frame_class_not_abstract_isomorphism(self):
        d=discover_couplings(3,3)
        self.assertEqual((d.raw_cocycles,len(d.candidates)),(9,3))
        self.assertEqual(abstract_isomorphism_classes(d.candidates),((0,),(1,2)))
        self.assertNotEqual(gauge_key(d.candidates[1]),gauge_key(d.candidates[2]))
        self.assertTrue(groups_isomorphic(d.candidates[1],d.candidates[2]))
        self.assertEqual(d.candidates[0].order_histogram(),((1,1),(3,8)))
        self.assertEqual(d.candidates[1].order_histogram(),((1,1),(3,2),(9,6)))

    def test_four_order_eight_structures_from_one_pair_of_components(self):
        d=discover_couplings(4,2)
        self.assertEqual(len(d.candidates),4)
        self.assertEqual(abstract_isomorphism_classes(d.candidates),
                         ((0,),(1,),(2,),(3,)))
        self.assertEqual([(c.multiplier,lift_wrap(c),c.is_abelian())
                          for c in d.candidates],
                         [(1,0,True),(1,1,True),(3,0,False),(3,2,False)])
        self.assertEqual([c.order_histogram() for c in d.candidates], [
            ((1,1),(2,3),(4,4)), ((1,1),(2,1),(4,2),(8,4)),
            ((1,1),(2,5),(4,2)), ((1,1),(2,1),(4,6))])

    def test_independent_cyclic_cohomology_theorem_predicts_orbit_count(self):
        for k,q in ((2,2),(3,2),(3,3),(2,3),(2,4),(4,2)):
            d=discover_couplings(k,q)
            signatures={cohomology_signature(c) for c in d.candidates}
            self.assertEqual(len(signatures),len(d.candidates))
            self.assertEqual(len(d.candidates),
                             sum(theoretical_extension_count(k,q,g) for g in d.actions))
            for c in d.candidates:
                t=lift_wrap(c)
                self.assertEqual((c.multiplier-1)*t % k,0)
                self.assertEqual(cyclic_norm(k,q,c.multiplier),
                                 sum(pow(c.multiplier,i,k) for i in range(q))%k)
                for z in product(range(k),repeat=q-1):
                    self.assertEqual(cohomology_signature(gauge_change(c,(0,)+z)),
                                     cohomology_signature(c))

    def test_coprime_cyclic_extension_class_collapses(self):
        self.assertEqual(len(discover_couplings(2,3).candidates),1)
        self.assertEqual(len(discover_couplings(2,4).candidates),2)

    def test_independent_full_associativity_unit_inverse_quotient_oracle(self):
        for k,q in ((2,2),(2,3),(3,2),(3,3),(2,4)):
            d=discover_couplings(k,q)
            self.assertEqual(d.raw_cocycles, sum(len(brute_tables(k,q,g)) for g in d.actions))
            for c in d.candidates:
                states=c.elements
                e=(0,0)
                self.assertTrue(all(c.multiply(e,s)==s==c.multiply(s,e) for s in states))
                for x,y,z in product(states,repeat=3):
                    self.assertEqual(c.multiply(c.multiply(x,y),z),c.multiply(x,c.multiply(y,z)))
                for x in states:
                    self.assertTrue(any(c.multiply(x,y)==e and c.multiply(y,x)==e for y in states))
                for x,y in product(states,repeat=2):
                    self.assertEqual(c.multiply(x,y)[1],(x[1]+y[1])%q)

    def test_coboundary_gauge_map_is_true_group_isomorphism(self):
        for k,q in ((2,2),(3,2),(3,3)):
            for c in discover_couplings(k,q).candidates:
                for z in product(range(k),repeat=q-1):
                    t=(0,)+z
                    self.assertTrue(verify_gauge_map(c,t))
                    target=gauge_change(c,t)
                    self.assertEqual(gauge_key(c),gauge_key(target))
                    self.assertEqual(len({gauge_map(c,t,x) for x in c.elements}),k*q)

    def test_reject_nonhom_action_wrong_cocycle_and_invalid_input(self):
        with self.assertRaises(CouplingError):
            CyclicExtension(3,2,0,(0,0,0,0))
        with self.assertRaises(CouplingError):
            CyclicExtension(5,2,2,(0,0,0,0))  # 2**2 != 1 mod 5
        with self.assertRaises(CouplingError):
            CyclicExtension(3,3,1,(0,0,0,0,0,1,0,0,0))
        with self.assertRaises(CouplingError):
            CyclicExtension(3,2,1,(1,0,0,0))
        with self.assertRaises(CouplingError):
            normalized_cocycle(3,3,(0,0))
        with self.assertRaises(CouplingError):
            gauge_change(discover_couplings(2,2).candidates[0],(1,0))
        with self.assertRaises(CouplingError):
            discover_couplings(3,5,max_tables=20)
        with self.assertRaises(CouplingError):
            discover_couplings(2,2,max_tables=0)


class TestObserverRelativeDiscovery(unittest.TestCase):
    def test_split_vs_nonsplit_two_step_minimax_and_independent_word_oracle(self):
        cs=discover_couplings(2,2).candidates
        o=frame()
        labels=("split","nonsplit")
        result=winning_policy(cs,o,labels,3)
        self.assertEqual((result.status,result.depth),("DECISIVE_IN_DECLARED_MODEL",2))
        self.assertEqual(result.depth,brute_shortest_word(cs,o.actions,o.readout,labels,3))
        self.assertIsInstance(result.policy,PolicyNode)
        for i,c in enumerate(cs):
            value,events=replay_policy(result.policy,c,o)
            self.assertEqual(value,labels[i])
            self.assertEqual(tuple(a for a,b in events),((0,1),(0,1)))
            self.assertEqual(events[-1][1],i)

    def test_action_coupling_requires_two_different_actuators(self):
        cs=discover_couplings(3,2).candidates
        o=frame(((0,1),(1,0)))
        labels=("trivial_action","inversion_action")
        result=winning_policy(cs,o,labels,3)
        self.assertEqual(result.depth,2)
        self.assertEqual(result.depth,brute_shortest_word(cs,o.actions,o.readout,labels,3))
        for i,c in enumerate(cs):
            label,rows=replay_policy(result.policy,c,o)
            self.assertEqual(label,labels[i])
            self.assertEqual(rows[-1][1],i+1)
        # Remove the kernel generator: available language is weaker.
        self.assertEqual(winning_policy(cs,frame(),labels,6).status,
                         "UNRESOLVED_WITHIN_HORIZON")

    def test_three_extension_classes_must_not_be_confused_with_two_groups(self):
        cs=discover_couplings(3,3).candidates
        o=frame()
        labels=("one","two","three")
        result=winning_policy(cs,o,labels,4)
        self.assertEqual(result.depth,3)
        self.assertEqual(result.depth,brute_shortest_word(cs,o.actions,o.readout,labels,4))
        self.assertEqual([replay_policy(result.policy,c,o)[0] for c in cs],list(labels))
        # No mathematical contradiction: two framed alternatives are abstractly isomorphic.
        self.assertTrue(groups_isomorphic(cs[1],cs[2]))

    def test_quotient_only_is_unbounded_darkness_not_just_a_search_timeout(self):
        for k,q in ((2,2),(3,2),(3,3)):
            cs=discover_couplings(k,q).candidates
            o=frame(((0,1),(1,0)),"quotient")
            self.assertTrue(quotient_darkness_certificate(cs,o))
            for length in range(5):
                for word in product(o.actions,repeat=length):
                    signatures=transcript_signature(cs,o,word)
                    self.assertEqual(len(set(signatures)),1)
            if len(cs)>1:
                labels=tuple(str(i) for i in range(len(cs)))
                self.assertEqual(winning_policy(cs,o,labels,6).status,
                                 "UNRESOLVED_WITHIN_HORIZON")
        self.assertFalse(quotient_darkness_certificate(cs,frame()))

    def test_gauge_equivalent_math_needs_actuator_and_sensor_transport(self):
        c=discover_couplings(3,2).candidates[0]
        t=(0,1)
        target=gauge_change(c,t)
        self.assertEqual(gauge_key(c),gauge_key(target))
        o=frame(((0,1),(1,0)),"kernel")
        # Untransported 'same-named' lifts are DIFFERENT physical setups.
        self.assertNotEqual(transcript_signature((c,),o,((0,1),(0,1))),
                            transcript_signature((target,),o,((0,1),(0,1))))
        # Transport EVERYTHING across the justified mathematical isomorphism.
        for n in range(5):
            for word in product(o.actions,repeat=n):
                l,r=gauge_transported_transcripts(c,t,o,word)
                self.assertEqual(l,r)
        with self.assertRaises(CouplingError):
            gauge_transported_transcripts(c,t,frame(),((1,0),))

    def test_eight_element_four_way_discovery_uses_adaptive_policy(self):
        cs=discover_couplings(4,2).candidates
        o=frame(((0,1),(1,0)))
        labels=("direct_product","cyclic8","dihedral8","quaternion8")
        plan=winning_policy(cs,o,labels,5)
        self.assertEqual(plan.depth,3)
        self.assertEqual(plan.depth,brute_shortest_word(cs,o.actions,o.readout,labels,5))
        self.assertEqual([replay_policy(plan.policy,c,o)[0] for c in cs],list(labels))
        self.assertTrue(quotient_darkness_certificate(cs,frame(o.actions,"quotient")))

    def test_bounded_failure_is_not_theorem_and_disallowed_probe_rejected(self):
        cs=discover_couplings(2,2).candidates
        self.assertEqual(winning_policy(cs,frame(),("A","B"),1).status,
                         "UNRESOLVED_WITHIN_HORIZON")
        self.assertEqual(winning_policy(cs,frame(),("A","B"),2).status,
                         "DECISIVE_IN_DECLARED_MODEL")
        with self.assertRaises(CouplingError):
            transcript_signature(cs,frame(),((1,0),))
        with self.assertRaises(CouplingError):
            winning_policy(cs,frame(),("only one",),2)
        with self.assertRaises(CouplingError):
            winning_policy(cs,frame(),("A","B"),-1)
        with self.assertRaises(CouplingError):
            frame(actions=((0,1),(0,1)))

    def test_non_uniform_carriers_and_gauge_clones_fail_closed(self):
        cs=discover_couplings(2,2).candidates
        with self.assertRaises(CouplingError):
            winning_policy((cs[0],discover_couplings(3,2).candidates[0]),frame(),("A","B"),1)
        with self.assertRaises(CouplingError):
            winning_policy((cs[0],cs[0]),frame(),("A","B"),1)
        gauge_clone=gauge_change(cs[0],(0,1))
        # q=2,k=2 happens to have trivial coboundary. Use k=3,q=2 instead.
        two=discover_couplings(3,2).candidates[0]
        clone=gauge_change(two,(0,1))
        self.assertNotEqual(two,clone)
        with self.assertRaises(CouplingError):
            winning_policy((two,clone),frame(),("A","B"),2)
        self.assertEqual(gauge_key(two),gauge_key(clone))
        self.assertEqual(gauge_key(cs[0]),gauge_key(gauge_clone))

    def test_exact_bayes_update_with_actual_synthetic_receipt_and_late_split(self):
        cs=discover_couplings(2,2).candidates
        o=frame()
        prior=(Q(1,2),Q(1,2))
        events=simulate_trace(cs[1],o,((0,1),(0,1)))
        self.assertEqual(exact_posterior(cs,o,prior,events[:1]),prior)
        self.assertEqual(exact_posterior(cs,o,prior,events),(Q(0),Q(1)))
        self.assertEqual(exact_posterior(cs,o,prior,()),prior)
        # This posterior is conditional on a DECLARED model class, not proof of source.
        self.assertEqual(events[0].origin,"declared_simulation")
        with self.assertRaises(OutOfModel):
            exact_posterior(cs,o,prior,(EventReceipt(o.source_id,o.basis_id,o.epoch,(0,1),99),))

    def test_contextual_prior_changes_heuristic_action_ranking(self):
        cs=discover_couplings(4,2).candidates
        o=frame(((0,1),(1,0)),"kernel")
        labels=("A","B","C","D")
        prior=(Q(1,4),)*4
        initial=rank_actions_by_target_gain(cs,o,labels,prior)
        self.assertEqual([v.target_gini_gain for v in initial],[0,0])
        e=simulate_trace(cs[0],o,((0,1),))
        ranked=rank_actions_by_target_gain(cs,o,labels,prior,e)
        self.assertEqual(ranked[0].action,(0,1))
        self.assertEqual(ranked[0].target_gini_gain,Q(1,2))
        self.assertEqual(ranked[1].target_gini_gain,Q(1,4))
        expensive=ObserverContract(o.source_id,o.basis_id,o.epoch,o.actions,o.readout,
                                   (Q(4),Q(1)))
        ranked2=rank_actions_by_target_gain(cs,expensive,labels,prior,e)
        self.assertEqual(ranked2[0].action,(1,0))
        self.assertEqual(ranked2[0].gain_per_cost,Q(1,4))
        # Wrong source-conditioned receipt never earns information gain.
        with self.assertRaises(OutOfModel):
            rank_actions_by_target_gain(cs,o,labels,prior,(
                EventReceipt(o.source_id,o.basis_id,o.epoch,(0,1),999),))
        with self.assertRaises(CouplingError):
            ObserverContract(o.source_id,o.basis_id,o.epoch,o.actions,o.readout,
                             (Q(0),Q(1)))

    def test_foreign_stale_or_unlicensed_receipts_are_rejected(self):
        cs=discover_couplings(2,2).candidates
        o=frame()
        prior=(Q(1,2),Q(1,2))
        e=simulate_trace(cs[0],o,((0,1),))[0]
        for row in (
            EventReceipt("forged",e.basis_id,e.epoch,e.action,e.observed),
            EventReceipt(e.source_id,"wrong_basis",e.epoch,e.action,e.observed),
            EventReceipt(e.source_id,e.basis_id,e.epoch+1,e.action,e.observed),
            EventReceipt(e.source_id,e.basis_id,e.epoch,(1,0),e.observed),
        ):
            with self.assertRaises(CouplingError):
                exact_posterior(cs,o,prior,(row,))
        with self.assertRaises(CouplingError):
            exact_posterior(cs,o,(0.5,0.5),())
        with self.assertRaises(CouplingError):
            exact_posterior(cs,o,(1,1),())
        with self.assertRaises(CouplingError):
            simulate_trace(cs[0],o,((1,0),))

    def test_receipt_is_recomputed_not_hardcoded(self):
        from scripts.structural_coupling_probe import receipt
        frozen=Path(__file__).resolve().parents[1] / "research/2026-10-13/STRUCTURAL_COUPLING_RECEIPT.json"
        self.assertEqual(receipt(),json.loads(frozen.read_text(encoding="utf8")))
        self.assertTrue(all(x["negative_controls"].values() for x in [receipt()]))

    def test_no_witness_of_real_executability_from_labeled_synthetic_sources(self):
        cs=discover_couplings(2,2).candidates
        contract=frame()
        self.assertEqual(contract.source_id,"declared_source")
        self.assertNotIn("authenticated", simulate_trace(cs[0],contract,((0,1),))[0].origin)
        self.assertEqual(winning_policy(cs,contract,("V4","C4"),2).status,
                         "DECISIVE_IN_DECLARED_MODEL")


if __name__ == "__main__":
    unittest.main()
