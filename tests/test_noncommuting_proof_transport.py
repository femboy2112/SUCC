"""Hostile controls for source-changing, noncommuting event/trace proof transport."""
from itertools import product
import random
import unittest

from observational_succ.noncommuting_proof_transport import (
    SourceTransportError, Instrument, FiniteCarrier, ProofFactor,
    _bit_field, factor_original_claim, check_source_semantics,
    partition_refinement_witness,
    lost_future_original_claim, finite_future_equivalence, finite_separator,
    noncommuting_proof_demo,
)


def independent_partition(field, sources, path, target):
    groups={}
    for x in sources:
        signature=field.run(x,path).observed_values
        groups.setdefault(signature,set()).add(target[x])
    return all(len(v)==1 for v in groups.values())


class NoncommutingCarrierTests(unittest.TestCase):
    def setUp(self):
        self.field=_bit_field()
        self.sources=(0,1,2,3)
        self.parity=("0","1","1","0")

    def test_both_orders_erase_payload_but_leave_different_record(self):
        for x in self.sources:
            ab=self.field.run(x,("A","B"))
            ba=self.field.run(x,("B","A"))
            self.assertEqual(ab.terminal_state,0)
            self.assertEqual(ba.terminal_state,0)
            self.assertEqual(ab.observed_values,(x//2,0))
            self.assertEqual(ba.observed_values,(x%2,0))
            self.assertEqual([r.epoch for r in ab.records],[1,2])
            self.assertEqual([r.source_id for r in ab.records],
                             [self.field.source_id]*2)
            self.assertEqual(ab.public_signature[0][0],"A")
            self.assertEqual(ab.public_signature[1][0],"B")
            self.assertEqual(ab.public_signature[0][2],1)
        self.assertNotEqual(
            self.field.run(2,("A","B")).observed_values,
            self.field.run(2,("B","A")).observed_values)

    def test_independent_full_16_predicates_each_path_against_fiber_oracle(self):
        for bits in product(("0","1"),repeat=4):
            for path in ((),("A",),("B",),("A","B"),("B","A"),
                         ("A","B","A"),("B","A","B")):
                certificate=factor_original_claim(
                    self.field,self.sources,bits,path,target_id="T")
                self.assertEqual(certificate.valid,
                                 independent_partition(
                                     self.field,self.sources,path,bits))
                if certificate.valid:
                    for x in self.sources:
                        outcomes=self.field.run(x,path).observed_values
                        self.assertEqual(certificate.decode(
                            outcomes,source_id=self.field.source_id,
                            basis_id=self.field.basis_id,
                            target_id="T",path=path),bits[x])
                else:
                    x,y=certificate.collision
                    self.assertNotEqual(bits[x],bits[y])
                    self.assertEqual(self.field.run(x,path).observed_values,
                                     self.field.run(y,path).observed_values)

    def test_source_history_refinement_monotone_despite_payload_erasure(self):
        for first in ((),("A",),("B",),("A","B"),("B","A")):
            for further in ((),("A",),("B",),("A","B")):
                self.assertIsNone(partition_refinement_witness(
                    self.field,self.sources,first+further,first))
        self.assertIsNotNone(partition_refinement_witness(
            self.field,self.sources,("A","B"),("B","A")))
        self.assertIsNotNone(partition_refinement_witness(
            self.field,self.sources,("B","A"),("A","B")))

    def test_irretrievable_original_source_shadow_both_first_actions(self):
        for first,pair in (("A",(0,1)),("B",(0,2))):
            shadow=lost_future_original_claim(
                self.field,*pair,self.parity,(first,))
            self.assertIsNotNone(shadow)
            self.assertEqual(shadow.terminal_state,0)
            self.assertNotEqual(shadow.first_target,shadow.second_target)
            for tail in product(("A","B"),repeat=4):
                x=self.field.run(pair[0],(first,)+tail)
                y=self.field.run(pair[1],(first,)+tail)
                self.assertEqual(x.public_signature,y.public_signature)
                self.assertEqual(x.terminal_state,y.terminal_state)

    def test_source_semantics_gate_independent_from_observation_decoder(self):
        # A read of original a leaves it unchanged, whereas B destroys it.
        first=("0","0","1","1")
        correct=check_source_semantics(self.field,self.sources,first,first,("A",))
        wrong=check_source_semantics(self.field,self.sources,first,first,("B",))
        self.assertTrue(correct.source_semantics_preserved)
        self.assertFalse(wrong.source_semantics_preserved)
        self.assertEqual(wrong.mismatch[0],2)
        self.assertEqual(wrong.mismatch[1],0)
        self.assertEqual(wrong.mismatch[2:],("1","0"))
        parity_changed=check_source_semantics(
            self.field,self.sources,self.parity,self.parity,("A","B"))
        self.assertFalse(parity_changed.source_semantics_preserved)
        self.assertNotEqual(
            self.parity[parity_changed.mismatch[0]],
            self.parity[parity_changed.mismatch[1]])
        # Same post-source decoder is not necessarily source-true.
        self.assertFalse(factor_original_claim(
            self.field,self.sources,self.parity,("A","B"),
            target_id="original-parity").valid)
        readable=_bit_field(nondestructive=True)
        self.assertTrue(check_source_semantics(
            readable,self.sources,self.parity,self.parity,
            ("A","B")).source_semantics_preserved)

    def test_semantic_source_square_composes_for_declared_matching_targets(self):
        # If each stage preserves a claimed invariant, the composition does.
        constant=("yes",)*4
        for first,second in product(("A","B"),repeat=2):
            for t in (constant,):
                self.assertTrue(check_source_semantics(
                    self.field,self.sources,t,t,(first,)).source_semantics_preserved)
                self.assertTrue(check_source_semantics(
                    self.field,self.sources,t,t,(second,)).source_semantics_preserved)
                self.assertTrue(check_source_semantics(
                    self.field,self.sources,t,t,
                    (first,second)).source_semantics_preserved)
        with self.assertRaises(SourceTransportError):
            check_source_semantics(self.field,self.sources,
                                   ("x",),constant,("A",))

    def test_empty_or_first_action_adaptive_parity_impossible_one_copy(self):
        self.assertFalse(factor_original_claim(
            self.field,self.sources,self.parity,(),target_id="xor").valid)
        for action in ("A","B"):
            shadows=[
                (x,y) for x in self.sources for y in self.sources
                if x<y and lost_future_original_claim(
                    self.field,x,y,self.parity,(action,)) is not None]
            self.assertTrue(shadows)
        # First action is fixed before any reports. Every first choice
        # admits indistinguishable but opposite-parity initial sources.

    def test_non_destructive_and_joint_evidence_repair(self):
        from observational_succ.noncommuting_proof_transport import _bit_field
        nondestructive=_bit_field(nondestructive=True)
        with_joint=_bit_field(with_joint=True)
        for path,field in ((("A","B"),nondestructive),
                           (("B","A"),nondestructive),
                           (("JOINT",),with_joint)):
            certificate=factor_original_claim(field,self.sources,self.parity,path,
                                              target_id="initial-parity")
            self.assertTrue(certificate.valid)
            for source in self.sources:
                result=certificate.decode(
                    field.run(source,path).observed_values,
                    source_id=field.source_id,basis_id=field.basis_id,
                    target_id="initial-parity",path=path)
                self.assertEqual(result,self.parity[source])

    def test_source_labels_provenance_context_is_not_an_external_signature(self):
        certificate=factor_original_claim(
            _bit_field(nondestructive=True),self.sources,self.parity,
            ("A","B"),target_id="T")
        with self.assertRaises(SourceTransportError):
            certificate.decode((0,0),source_id="different",
                               basis_id=self.field.basis_id,
                               target_id="T",path=("A","B"))
        with self.assertRaises(SourceTransportError):
            certificate.decode((0,0),source_id=self.field.source_id,
                               basis_id="different",target_id="T",
                               path=("A","B"))
        with self.assertRaises(SourceTransportError):
            certificate.decode((0,0),source_id=self.field.source_id,
                               basis_id=self.field.basis_id,
                               target_id="other",path=("A","B"))
        with self.assertRaises(SourceTransportError):
            certificate.decode((0,0),source_id=self.field.source_id,
                               basis_id=self.field.basis_id,
                               target_id="T",path=("B","A"))
        with self.assertRaises(SourceTransportError):
            certificate.decode((23,),source_id=self.field.source_id,
                               basis_id=self.field.basis_id,
                               target_id="T",path=("A","B"))

    def test_unavailable_intervention_cannot_silently_restrict_source_class(self):
        a=Instrument("READ",(0,0,1,1),(0,1,2,3),
                     (True,False,False,False))
        field=FiniteCarrier(4,(a,),"known-carrier","basis")
        with self.assertRaises(SourceTransportError):
            factor_original_claim(field,(0,1,2,3),
                                  ("0","0","1","1"),("READ",),target_id="T")
        self.assertTrue(factor_original_claim(
            field,(0,),("0","0","1","1"),("READ",),target_id="T").valid)
        with self.assertRaises(SourceTransportError):
            field.run(1,("READ",))

    def test_invalid_inputs_and_rejected_fake_action_replay(self):
        yes=(True,)*4
        for bad in (
            Instrument("fake",(0,1,0,1),(0,1,2,4),yes),
            Instrument("fake",(0,1,0,True),(0,1,2,3),yes),
            Instrument("fake",(0,1,0,1),(0,1,2,3),(1,1,1,1)),
        ):
            with self.assertRaises(SourceTransportError):
                FiniteCarrier(4,(bad,),"source","basis")
        with self.assertRaises(SourceTransportError):
            FiniteCarrier(4,(self.field.actions[0],
                            self.field.actions[0]),"source","basis")
        with self.assertRaises(SourceTransportError):
            self.field.run(0,("INVENTED",))
        with self.assertRaises(SourceTransportError):
            factor_original_claim(self.field,(3,2),self.parity,("A",),
                                  target_id="target")
        with self.assertRaises(SourceTransportError):
            factor_original_claim(self.field,self.sources,("x",),
                                  ("A",),target_id="target")

    def test_finite_observational_bisimulation_greatest_fixed_point(self):
        # All combinations of deterministic 2-state, 2-action maps where
        # outcomes and next state are independently assigned Boolean values.
        specs=tuple(product((0,1),repeat=4))
        for left in specs:
            for right in specs:
                actions=[]
                for name,values in (("L",left),("R",right)):
                    actions.append(Instrument(
                        name,values[:2],values[2:],(True,True)))
                f=FiniteCarrier(2,tuple(actions),"S","B")
                relation=finite_future_equivalence(f)
                separator=finite_separator(f,0,1)
                self.assertEqual((0,1) in relation, separator is None)
                if separator is not None:
                    a,b=0,1
                    for index,name in enumerate(separator):
                        act=f.action(name)
                        if (act.outputs[a] != act.outputs[b] or
                                act.enabled[a] != act.enabled[b]):
                            self.assertEqual(index,len(separator)-1)
                            break
                        a,b=act.transitions[a],act.transitions[b]
                    else:
                        self.fail("BFS separator never yielded a distinguishable step")

    def test_masked_future_menus_and_random_multi_state_controls(self):
        rng=random.Random(90210)
        for i in range(130):
            count=rng.choice((2,3,4,5))
            actions=[]
            for name in ("A","B","C"):
                outputs=tuple(rng.randrange(3) for _ in range(count))
                moves=tuple(rng.randrange(count) for _ in range(count))
                enabled=tuple(bool(rng.randrange(2)) for _ in range(count))
                actions.append(Instrument(name,outputs,moves,enabled))
            f=FiniteCarrier(count,tuple(actions),f"S{i}","basis")
            relation=finite_future_equivalence(f)
            for a in range(count):
                for b in range(a,count):
                    separator=finite_separator(f,a,b)
                    self.assertEqual((a,b) in relation,separator is None)

    def test_machine_receipt(self):
        output=noncommuting_proof_demo()
        self.assertEqual(output["status"],
                         "NONCOMMUTING_SOURCE_PROOF_TRANSPORT_EXACT")
        self.assertEqual(output["all_four_two_action_endpoints"],"00")
        self.assertFalse(output["AB_parity_original_decodable"])
        self.assertFalse(output["BA_parity_original_decodable"])
        self.assertFalse(output["AB_vs_BA_partition_refinement"])
        self.assertFalse(output["BA_vs_AB_partition_refinement"])
        self.assertFalse(output["post_source_parity_is_original_parity"])
        self.assertTrue(output["A_preserves_original_a_semantics"])
        self.assertFalse(output["B_preserves_original_a_semantics"])
        self.assertTrue(output["all_distinct_initial_sources_pairwise_separable"])
        self.assertTrue(output["no_uniform_adaptive_original_parity_protocol"])
        self.assertTrue(output["same_shadow_no_future_adaptive_proof"])
        self.assertTrue(output["nondestructive_AB_repairs_original_parity"])
        self.assertTrue(output["source_joint_read_repairs_original_parity"])
        self.assertTrue(output["pre_source_truth_labels_not_leaked_into_reports"])
        self.assertFalse(output["quantum_physical_or_RH_theorem_claimed"])


if __name__=="__main__":
    unittest.main()
