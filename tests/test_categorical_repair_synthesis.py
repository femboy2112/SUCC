"""Source-independent/adversarial checks of the categorical model-repair compiler."""
import itertools
import random
import unittest
from fractions import Fraction as Q

from observational_succ.categorical_repair_synthesis import (
    FiniteMealy, RepairError, StieltjesLaw, F, determinant, invert, product,
    positive_definite, minimal_behavioral_quotient, shortest_distinguishing_word,
    proposed_quotient_defect, universal_observer_factor, positive_passive_alias,
    hankel_memory_repair, discover_boundary_memory, categorical_repair_demo,
)
from observational_succ.dynamic_boundary_inverse import (
    BoundaryReceipt, observe, star, triangle, twin_hubs, serial_pendant,
    reconstruct_y_triangle,
)


class FiniteCategoricalObserverTests(unittest.TestCase):
    @staticmethod
    def source():
        return FiniteMealy(("look", "read"), ((0,0,0,0),(0,0,1,1)),
                           ((1,2,3,3),(0,1,2,3)))

    def test_source_minimal_behavioral_quotient_has_three_states(self):
        m=self.source();q=minimal_behavioral_quotient(m)
        self.assertEqual(q.blocks,((0,),(1,),(2,3)))
        self.assertEqual(q.refinement_steps,2)
        self.assertEqual(q.block_of(2),q.block_of(3))
        self.assertTrue(q.factors_claim((1,0,0,0))["proved"])
        self.assertFalse(q.factors_claim((0,0,1,0))["proved"])

    def test_shortest_actual_future_distinguishes_delayed_pair(self):
        m=self.source()
        self.assertEqual(shortest_distinguishing_word(m,0,1),("look","read"))
        self.assertEqual(shortest_distinguishing_word(m,1,2),("read",))
        self.assertIsNone(shortest_distinguishing_word(m,2,3))
        self.assertIsNone(shortest_distinguishing_word(m,0,0))

    def test_static_source_partition_fails_causal_naturality(self):
        d=proposed_quotient_defect(self.source(),(0,0,1,1))
        self.assertFalse(d["commutes"])
        self.assertEqual(d["failure"],"TRANSITION_NOT_FACTORED")
        self.assertEqual(d["states"],(0,1))
        self.assertEqual(d["action"],"look")

    def test_true_behavioral_quotient_commutes_on_generators(self):
        self.assertTrue(proposed_quotient_defect(self.source(),(0,1,2,2))["commutes"])

    def test_universal_map_from_finer_quotient(self):
        u=universal_observer_factor(self.source(),(10,11,12,13))
        self.assertTrue(u["commutes"])
        self.assertEqual(u["universal_factor"],((10,0),(11,1),(12,2),(13,2)))
        self.assertTrue(u["all_generated_action_words_preserved"])
        merged=universal_observer_factor(self.source(),(0,1,2,2))
        self.assertEqual(merged["universal_factor"],((0,0),(1,1),(2,2)))

    def test_invalid_quotient_has_explicit_generator_witness(self):
        u=universal_observer_factor(self.source(),(0,0,1,1))
        self.assertFalse(u["commutes"])
        self.assertEqual(u["failure"],"TRANSITION_NOT_FACTORED")

    def test_quotient_replays_every_causal_word_up_to_six_steps(self):
        m=self.source();q=minimal_behavioral_quotient(m)
        for n in range(7):
            for word in itertools.product(m.actions,repeat=n):
                for state in range(m.count):
                    current=q.block_of(state);seen=[]
                    for action in word:
                        ai=m.actions.index(action)
                        seen.append(q.action_outputs[ai][current])
                        current=q.action_transitions[ai][current]
                    self.assertEqual(tuple(seen),m.observe(state,word))

    def test_two_indistinguishable_source_states_cannot_be_separated_by_any_word(self):
        m=self.source()
        for n in range(8):
            for word in itertools.product(m.actions,repeat=n):
                self.assertEqual(m.observe(2,word),m.observe(3,word))

    def test_random_machine_behaviors_agree_with_exhaustive_short_words(self):
        rng=random.Random(2504)
        for _ in range(220):
            m=FiniteMealy(("a","b"),
                tuple(tuple(rng.randrange(2) for _ in range(4)) for _ in range(2)),
                tuple(tuple(rng.randrange(4) for _ in range(4)) for _ in range(2)))
            q=minimal_behavioral_quotient(m)
            self.assertLessEqual(q.refinement_steps,3)
            for i in range(4):
                for j in range(i+1,4):
                    witness=shortest_distinguishing_word(m,i,j)
                    same=(q.block_of(i)==q.block_of(j))
                    self.assertEqual(witness is None,same)
                    if witness:
                        self.assertNotEqual(m.observe(i,witness),m.observe(j,witness))
                        for length in range(len(witness)):
                            for w in itertools.product(m.actions,repeat=length):
                                self.assertEqual(m.observe(i,w),m.observe(j,w))

    def test_exhaustive_two_state_two_action_family(self):
        total=0
        for values in itertools.product((0,1),repeat=8):
            m=FiniteMealy(("a","b"),
                (tuple(values[:2]),tuple(values[2:4])),
                (tuple(values[4:6]),tuple(values[6:8])))
            q=minimal_behavioral_quotient(m)
            w=shortest_distinguishing_word(m,0,1)
            self.assertEqual(w is None,len(q.blocks)==1)
            if w:self.assertNotEqual(m.observe(0,w),m.observe(1,w))
            total+=1
        self.assertEqual(total,256)

    def test_source_validation_rejects_forged_and_malformed_tables(self):
        with self.assertRaises(RepairError):FiniteMealy(("a","a"),((0,0),(0,0)),((0,0),(0,0)))
        with self.assertRaises(RepairError):FiniteMealy(("a",),((0,0),),((0,2),))
        with self.assertRaises(RepairError):self.source().observe(0,("foreign",))
        with self.assertRaises(RepairError):proposed_quotient_defect(self.source(),(0,0,0))
        with self.assertRaises(RepairError):minimal_behavioral_quotient(None)


class PassiveAliasTests(unittest.TestCase):
    def test_exact_nonunique_four_frequency_stieltjes_sources(self):
        x=positive_passive_alias((0,1,2,3))
        self.assertEqual((x.lower.degree,x.higher.degree),(2,3))
        self.assertEqual(x.lower.poles,(Q(2),Q(4)))
        self.assertEqual(x.higher.poles,(Q(1),Q(3),Q(5)))
        self.assertEqual(x.lower.weights,(Q(20,450),Q(140,450)))
        self.assertEqual(x.higher.weights,(Q(1,450),Q(90,450),Q(70,450)))
        self.assertEqual(x.residue_identity,(Q(1),Q(-20),Q(90),Q(-140),Q(70)))
        for s in (0,1,2,3):self.assertEqual(x.lower.response(s),x.higher.response(s))
        self.assertEqual(x.lower.response(0),Q(1,10))
        self.assertEqual(x.first_holdout,4)
        self.assertEqual(abs(x.holdout_residual),Q(1,283500))
        self.assertNotEqual(x.lower.response(4),x.higher.response(4))

    def test_all_passive_weights_positive(self):
        for samples in ((0,1,2,3),(1,2,3),(0,2,5,7),(0,1),(3,)):
            a=positive_passive_alias(samples)
            self.assertTrue(all(w>0 for w in a.lower.weights+a.higher.weights))
            self.assertNotEqual(a.lower.degree,a.higher.degree)
            for s in samples:self.assertEqual(a.lower.response(s),a.higher.response(s))
            self.assertNotEqual(a.lower.response(a.first_holdout),a.higher.response(a.first_holdout))

    def test_arbitrary_finite_samples_random_exact_alias(self):
        rng=random.Random(9237)
        for _ in range(240):
            ss=tuple(sorted(rng.sample(range(0,30),rng.randrange(1,9))))
            a=positive_passive_alias(ss,pole_start=rng.randrange(1,7),static_target=Q(1,rng.randrange(2,12)))
            self.assertEqual(a.lower.response(0),a.higher.response(0))
            self.assertNotEqual(a.lower.degree,a.higher.degree)
            for s in ss:self.assertEqual(a.lower.response(s),a.higher.response(s))

    def test_stieltjes_positive_hankel_ranks_match_distinct_poles(self):
        a=positive_passive_alias((0,1,2,3))
        for law in (a.lower,a.higher):
            m=tuple(law.moment(k) for k in range(2*law.degree+4))
            fit=hankel_memory_repair(m,max_modes=law.degree)
            self.assertEqual(fit.dimension,law.degree)
            for s in (0,1,2,3,4,11):self.assertEqual(fit.response(s),law.response(s))

    def test_no_arbitrary_global_uniqueness_from_same_finite_samples(self):
        a=positive_passive_alias((0,1,2,3))
        self.assertTrue(all(a.lower.response(s)==a.higher.response(s) for s in a.probe_points))
        self.assertNotEqual(a.lower.moment(0),a.higher.moment(0))

    def test_reject_nonpositive_and_float_sources(self):
        for poles,weights in [((1,2),(1,-1)),((1,1),(1,1)),((0,2),(1,1))]:
            with self.assertRaises(RepairError):StieltjesLaw(poles,weights)
        with self.assertRaises(RepairError):positive_passive_alias((0,0,1))
        with self.assertRaises(RepairError):positive_passive_alias((0,1.0,2))
        with self.assertRaises(RepairError):positive_passive_alias((0,1,2),static_target=-1)
        with self.assertRaises(RepairError):positive_passive_alias(())
        with self.assertRaises(RepairError):StieltjesLaw((1,),(1,)).response(-1)


class AutoConstructiveMemoryTests(unittest.TestCase):
    def test_source_free_inverse_discovers_memory_category(self):
        data=categorical_repair_demo()
        self.assertEqual(data["mode_dimension"],2)
        self.assertEqual(data["static_conductances"],(Q(2),Q(3),Q(5)))
        self.assertEqual(data["rational_reciprocal_coefficients"],(Q(5),Q(3,2),Q(3,4)))
        self.assertEqual(data["observed_hankel_determinant"],Q(2,3))
        self.assertEqual(data["independent_holdouts_confirmed"],(4,11,17))
        self.assertEqual(data["smallest_delayed_separator"],("look","read"))
        self.assertFalse(data["all_frequency_physical_ontology_unique"])
        self.assertFalse(data["source_physically_authenticated"])
        self.assertFalse(data["RH_or_Weil_positivity_proved"])

    def test_exact_generator_is_derived_from_hankel_not_preloaded_circuit(self):
        source=serial_pendant()
        obs=tuple(observe(source,s) for s in range(4))
        law=discover_boundary_memory(obs)
        self.assertEqual(law.linear_memory.generator,((Q(0),Q(-20,3)),(Q(1),Q(25,3))))
        self.assertEqual(law.linear_memory.initial,(Q(1),Q(0)))
        self.assertEqual(law.linear_memory.output,(Q(1,2),Q(7,2)))
        self.assertEqual(determinant(law.linear_memory.H),Q(2,3))
        self.assertTrue(positive_definite(law.linear_memory.H))
        self.assertTrue(positive_definite(law.linear_memory.H_shift))
        self.assertEqual(len(law.failed_repairs),3)
        for s in (0,1,2,3,4,7,11,17,25):
            self.assertEqual(law.response(s),source.response(s))
        for k in range(8):
            self.assertEqual(law.linear_memory.moment(k),source.moments(8)[k][0][0]/Q(4))

    def test_multiple_observers_same_basis_epoch_meet_at_E(self):
        source=serial_pendant()
        r=tuple(observe(source,s,observer=f"E{i}") for i,s in enumerate((0,1,2,3)))
        model=discover_boundary_memory(r,holdouts=(observe(source,4,observer="independent"),))
        self.assertEqual(model.linear_memory.dimension,2)
        self.assertEqual(model.source_id,"shared-RC-carrier")

    def test_random_exact_passive_two_mode_sources_have_correct_reconstructions(self):
        rng=random.Random(4425)
        for _ in range(180):
            arms=tuple(rng.randint(1,8) for _ in range(3))
            c0,c1,h=(rng.randint(1,8) for _ in range(3))
            source=serial_pendant(arms,c0,h,c1)
            receipts=tuple(observe(source,s,observer=f"climber{s}") for s in range(4))
            model=discover_boundary_memory(receipts)
            self.assertEqual(model.arms,tuple(map(Q,arms)))
            self.assertEqual(model.alpha,Q(c0+c1))
            self.assertEqual(model.beta,Q(c0*c1,h))
            self.assertEqual(model.gamma,Q(c1,h))
            self.assertEqual(model.linear_memory.dimension,2)
            for s in (4,5,11):self.assertEqual(model.response(s),source.response(s))

    def test_candidate_is_equivariant_under_nontrivial_basis_change(self):
        src=serial_pendant()
        mod=discover_boundary_memory(tuple(observe(src,s) for s in range(4)))
        r=mod.linear_memory
        T=((Q(1),Q(1)),(Q(0),Q(1)))
        audit=r.basis_change(T)
        self.assertNotEqual(audit["generator"],r.generator)
        self.assertTrue(audit["representation_preserves_all_words_by_similarity"])
        for k in range(30):
            state=audit["initial"]
            for _ in range(k):state=tuple(sum((a*b for a,b in zip(row,state)),Q(0)) for row in audit["generator"])
            self.assertEqual(sum((a*b for a,b in zip(audit["output"],state)),Q(0)),r.moment(k))

    def test_singular_basis_cannot_claim_equivariant_transport(self):
        m=discover_boundary_memory(tuple(observe(serial_pendant(),s) for s in range(4)))
        with self.assertRaises(RepairError):m.linear_memory.basis_change(((1,0),(1,0)))

    def test_hankel_invariants_prevent_one_mode_repair(self):
        src=serial_pendant()
        m=tuple(src.moments(8)[i][0][0]/4 for i in range(8))
        model=hankel_memory_repair(m)
        self.assertEqual(model.dimension,2)
        self.assertEqual(determinant(model.H),Q(2,3))
        with self.assertRaises(RepairError):hankel_memory_repair(m,max_modes=1)

    def test_truthful_single_mode_data_are_not_claimed_two_mode(self):
        src=star()
        with self.assertRaisesRegex(RepairError,"does not yet force"):
            discover_boundary_memory(tuple(observe(src,s) for s in range(4)))

    def test_static_triangle_never_forces_memory_category(self):
        src=triangle()
        with self.assertRaisesRegex(RepairError,"No dynamic evidence"):
            discover_boundary_memory(tuple(observe(src,s) for s in range(4)))

    def test_identical_input_output_different_hidden_node_count_is_unresolved(self):
        a=star();b=twin_hubs()
        self.assertEqual(len(a.interior),1)
        self.assertEqual(len(b.interior),2)
        for s in (0,1,2,3,4,7,100):self.assertEqual(a.response(s),b.response(s))

    def test_mutated_epoch_source_and_basis_rejected(self):
        src=serial_pendant()
        good=[observe(src,s) for s in range(4)]
        for k,v in (("source_id","wrong"),("source_epoch",1),("basis_id","wrong")):
            bad=good.copy();copy=bad[2]
            payload=dict(source_id=copy.source_id,source_epoch=copy.source_epoch,basis_id=copy.basis_id,observer=copy.observer,laplace_s=copy.laplace_s,response=copy.response)
            payload[k]=v
            bad[2]=BoundaryReceipt(**payload)
            with self.assertRaises(RepairError):discover_boundary_memory(bad)

    def test_wrong_report_frequency_and_bad_holdout_rejected(self):
        src=serial_pendant()
        good=[observe(src,s) for s in range(4)]
        good[2]=observe(src,5)
        with self.assertRaises(RepairError):discover_boundary_memory(good)
        good=[observe(src,s) for s in range(4)]
        with self.assertRaises(RepairError):discover_boundary_memory(good,holdouts=(observe(star(),4),))

    def test_rank_one_boundary_source_signature_cannot_be_forged(self):
        src=serial_pendant()
        good=[observe(src,s) for s in range(4)]
        s=good[1]
        response=[list(row) for row in s.response]
        response[1][2]+=Q(1,1000)
        good[1]=BoundaryReceipt(s.source_id,s.source_epoch,s.basis_id,s.observer,s.laplace_s,tuple(tuple(x) for x in response))
        with self.assertRaisesRegex(RepairError,"rank-one"):
            discover_boundary_memory(good)

    def test_two_mode_complexity_bound_stated_not_discovered_as_ontology(self):
        src=serial_pendant()
        good=[observe(src,s) for s in range(4)]
        with self.assertRaises(RepairError):discover_boundary_memory(good,max_modes=1)

    def test_invalid_moment_sequence_is_not_assumed_passive(self):
        with self.assertRaises(RepairError):hankel_memory_repair((1,2,1,2,1))
        with self.assertRaises(RepairError):hankel_memory_repair((0,0,0,0,0))
        with self.assertRaises(RepairError):hankel_memory_repair((1.0,2,3,4))

    def test_finite_moments_necessarily_do_not_fix_unrestricted_future(self):
        m=tuple(serial_pendant().moments(8)[i][0][0]/4 for i in range(8))
        # A high-order formal series can share any finite prefix then diverge.
        changed=m+(Q(1),)
        base=hankel_memory_repair(m)
        self.assertNotEqual(base.moment(8),changed[8])
        with self.assertRaises(RepairError):hankel_memory_repair(changed)


if __name__=="__main__":unittest.main()
