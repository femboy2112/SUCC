"""Adversarial exact finite controls for effective field-classification boundaries."""
import unittest
from itertools import product
from observational_succ.effective_field_gates import (
    FieldGateError, cantor_pair, cantor_unpair, encode_counter_program,
    decode_counter_program, bounded_self_output, diagonal_tree_admissible,
    diagonal_tree_level_witness, tree_level_report, AutomaticSource,
    finite_support_shadow, dark_pair, pulse_finite_adversary,
    halting_gated_pair, effective_field_demo,
)
from observational_succ.godel_succ import delayed_halt, two_counter_loop


class EffectiveFieldGatesTests(unittest.TestCase):
    def test_godel_pair_roundtrip_without_unbounded_oracle(self):
        for a,b in product(range(40),repeat=2):
            self.assertEqual(cantor_unpair(cantor_pair(a,b)),(a,b))
        for z in range(3500):
            self.assertEqual(cantor_pair(*cantor_unpair(z)),z)

    def test_small_program_syntax_decodes_and_encodes(self):
        valid=((),((0,),),((1,0),),((2,0),),
               ((3,0,0),),((4,0,0),),((1,1),(0,)),
               ((3,1,0),(2,0),(0,)))
        for program in valid:
            idx=encode_counter_program(program)
            self.assertEqual(decode_counter_program(idx),program)
            # Decoder is a total computable map even for unused codes.
        for idx in range(1000):
            program=decode_counter_program(idx)
            self.assertIsInstance(program,tuple)
        self.assertEqual(encode_counter_program(((0,),)),1)
        self.assertEqual(bounded_self_output(0,0),0)
        self.assertEqual(bounded_self_output(1,0),1)

    def test_dnr_tree_all_tested_levels_and_prefix_closure(self):
        for n in range(0,34):
            word=diagonal_tree_level_witness(n)
            self.assertTrue(diagonal_tree_admissible(word))
            self.assertEqual(len(word),n)
            for shorter in range(n+1):
                self.assertTrue(diagonal_tree_admissible(word[:shorter]))
        self.assertFalse(tree_level_report(8)['infinite_path_constructed_by_code'])

    def test_finite_negative_diagonal_mutations_are_decisive(self):
        one=diagonal_tree_level_witness(1)
        self.assertEqual(one,(1,))
        self.assertFalse(diagonal_tree_admissible((0,)))
        n=12
        witness=diagonal_tree_level_witness(n)
        for e in range(n):
            out=bounded_self_output(e,n)
            if out is not None:
                bad=list(witness)
                bad[e]=out
                self.assertFalse(diagonal_tree_admissible(tuple(bad)))

    def test_simple_finite_generator_proof_and_countermodel(self):
        zero=AutomaticSource((0,0,0),(1,2,1))
        cert=zero.global_zero_certificate()
        self.assertTrue(cert['all_future_outputs_zero'])
        self.assertEqual(cert['reachable_states'],[0,1,2])
        self.assertEqual(cert['cycle_entry'],1)
        self.assertFalse(cert['infinite_physical_execution_claimed'])
        bad=AutomaticSource((0,1,0),(1,2,1))
        self.assertFalse(bad.global_zero_certificate()['all_future_outputs_zero'])
        self.assertEqual(bad.global_zero_certificate()['first_bad_state'],1)
        # Unreachable bad state does not invalidate all-future claim from initial.
        unused=AutomaticSource((0,0,1),(1,0,2))
        self.assertTrue(unused.global_zero_certificate()['all_future_outputs_zero'])

    def test_no_ghost_finite_source_realization_is_not_infinite(self):
        for n in (0,1,2,7,30):
            report=finite_support_shadow(n)
            self.assertEqual(report['formal_prefix'],[1]*n)
            self.assertTrue(report['every_finite_prefix_source_realized'])
            self.assertFalse(report['global_all_ones_source_realized'])

    def test_ambiguous_ideal_global_target_and_admissible_repair(self):
        for n in (0,1,3,16):
            for repair in (False,True):
                cert=dark_pair(n,odd_bit_probe_enabled=repair)
                self.assertTrue(cert['all_even_probes_forever_equal'])
                self.assertFalse(cert['target_bit_one_equal'])
                self.assertFalse(cert['source_identified_from_even_probes'])
                self.assertEqual(cert['conditional_repair_available'],repair)

    def test_arbitrarily_late_finite_witness_trap(self):
        for n in (0,2,50,1000):
            cert=pulse_finite_adversary(n)
            self.assertEqual(cert['counterexample_pulse_position'],n)
            self.assertFalse(cert['finite_observation_proves_absence'])
            self.assertTrue(cert['counterexample_same_observations'])

    def test_halting_gated_boundary_probe_and_negative_control(self):
        for n in (1,2,3,5,9):
            program=delayed_halt(n)
            for h in range(n+2):
                cert=halting_gated_pair(program,h)
                self.assertEqual(cert['distinguished_by_this_horizon'],h>=n)
                self.assertFalse(cert['full_source_classification_decided'])
                self.assertFalse(cert['dark_forever_proved_by_failed_prefix'])
        for n in (0,1,25,500):
            cert=halting_gated_pair(two_counter_loop(),n)
            self.assertFalse(cert['distinguished_by_this_horizon'])
            self.assertFalse(cert['dark_forever_proved_by_failed_prefix'])

    def test_exact_domain_guards(self):
        for bad in (True,-1,1.5,'2'):
            with self.assertRaises(FieldGateError):
                diagonal_tree_level_witness(bad)
            with self.assertRaises(FieldGateError):
                cantor_unpair(bad)
        for bad in ((0,2),(True,),[0,1]):
            with self.assertRaises(FieldGateError):
                diagonal_tree_admissible(bad)
        with self.assertRaises(FieldGateError):
            AutomaticSource((0,1),(1,2))
        with self.assertRaises(FieldGateError):
            AutomaticSource((0,),(0,),True)
        with self.assertRaises(FieldGateError):
            encode_counter_program(((4,2),))

    def test_frozen_receipt_false_global_promotions(self):
        r=effective_field_demo()
        self.assertTrue(r['simple_finite_generator_all_future_zero'])
        self.assertTrue(r['idealhard_decidable_tree_each_level_nonempty'])
        self.assertFalse(r['idealhard_computable_infinite_path_constructed'])
        self.assertTrue(r['fucked_no_source_global_shadow'])
        self.assertTrue(r['fucked_even_probe_dark_pair'])
        self.assertFalse(r['classification_from_finite_survey_only'])
        self.assertFalse(r['global_weil_sign_or_RH_proved'])


if __name__=='__main__':
    unittest.main()
