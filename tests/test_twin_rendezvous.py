"""Independent exact finite hostile controls, no quantum-device claim."""
import itertools
import unittest
from fractions import Fraction as F

from observational_succ.twin_rendezvous import (
    Event, Frame, PresentReport, report_from_source, compare_present, causal_reachability,
    source_invariant, original_bbp_forcing, bell_with_environment, pauli_path,
    controlled_not, rational_overlap_marker, reduced_density,
    purity, bell_probabilities, pauli_pair_syndrome,
    independent_reference_syndrome, exact_marker_coherence,
)


class FrameRendezvousTests(unittest.TestCase):
    def setUp(self):
        self.a,self.b=Frame(F(3,5),F(5,4)),Frame(F(-3,5),F(5,4))
        self.event=Event(3,0)
        self.model=Event(4,F(7,3))

    def test_exact_lorentz_transport(self):
        for frame in (self.a,self.b,Frame()):
            for x in (Event(0,0),Event(3,1),Event(F(-1,4),F(5,7)),self.event):
                self.assertEqual(frame.to_common(frame.from_common(x)),x)
                self.assertEqual(frame.from_common(frame.to_common(x)),x)
                self.assertEqual(frame.to_common(x).square(),x.square())

    def test_frame_differentials_are_not_equal_histories(self):
        lhs,rhs=self.a.from_common(self.event),self.b.from_common(self.event)
        self.assertNotEqual(lhs,rhs)
        self.assertEqual(self.a.to_common(lhs),self.b.to_common(rhs))
        # History events have different proper local coordinates and may not
        # be directly compared, even when they denote the same physical event.
        past=Event(1,F(1,2))
        self.assertNotEqual(self.a.from_common(past),self.b.from_common(past))

    def test_both_agree_only_after_frame_transport(self):
        a=report_from_source('left',self.a,self.event,self.model,clock=3)
        b=report_from_source('right',self.b,self.event,self.model,clock=5)
        self.assertNotEqual(a.model_local,b.model_local)
        self.assertEqual(compare_present(a,b).accepts,True)

    def test_double_wrong_model_agrees_but_does_not_prove_truth(self):
        fake=Event(555,666)
        a=report_from_source('left',self.a,self.event,fake,2)
        b=report_from_source('right',self.b,self.event,fake,3)
        self.assertTrue(compare_present(a,b).accepts)
        self.assertNotEqual(self.model,fake)

    def test_source_pin_catches_common_wrong_seed(self):
        a=report_from_source('left',self.a,self.event,self.model,clock=4,seed=F(1,16))
        b=report_from_source('right',self.b,self.event,self.model,clock=7,seed=F(1,16))
        verdict=compare_present(a,b)
        self.assertTrue(verdict.coincident_event and verdict.same_model)
        self.assertFalse(verdict.source_a_correct)
        self.assertFalse(verdict.source_b_correct)
        self.assertFalse(verdict.accepts)
        self.assertEqual(source_invariant(a.clock,a.selected_unwrapped),F(1,16))
        self.assertEqual(source_invariant(b.clock,b.selected_unwrapped),F(1,16))

    def test_four_pole_matches_independent_rational_source(self):
        # Independently recover the canonical duck_bbp.py polynomial map.
        for n in range(1,51):
            canonical=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(original_bbp_forcing(n),canonical)

    def test_forcing_anchor_is_exact_source_contract(self):
        self.assertEqual(original_bbp_forcing(1),F(47,15))
        self.assertEqual(source_invariant(0,0),0)
        for n in range(0,12):
            r=report_from_source('observer',Frame(),self.event,self.model,n)
            self.assertEqual(source_invariant(n,r.selected_unwrapped),0)

    def test_not_met_not_accepted(self):
        a=report_from_source('left',self.a,self.event,self.model,2)
        b=report_from_source('right',self.b,Event(4,0),self.model,2)
        v=compare_present(a,b)
        self.assertFalse(v.coincident_event)
        self.assertFalse(v.accepts)

    def test_causal_meeting_and_wrong_target_are_rejected(self):
        self.assertTrue(causal_reachability(Event(0,-2),self.event))
        self.assertTrue(causal_reachability(Event(0,2),self.event))
        self.assertFalse(causal_reachability(Event(0,-4),Event(1,0)))
        self.assertFalse(causal_reachability(Event(2,0),Event(1,0)))
        a=report_from_source('a',self.a,self.event,self.model,2)
        b=report_from_source('b',self.b,self.event,self.model,3)
        self.assertTrue(compare_present(a,b,expected_meeting=self.event).accepts)
        self.assertFalse(compare_present(a,b,expected_meeting=Event(4,0)).accepts)

    def test_frame_and_source_validation(self):
        with self.assertRaises(ValueError): Frame(F(2,3),F(5,4))
        with self.assertRaises(ValueError): Frame(1,1)
        with self.assertRaises(ValueError): original_bbp_forcing(0)
        with self.assertRaises(ValueError): source_invariant(-1,0)
        with self.assertRaises(ValueError): report_from_source('a',Frame(),self.event,self.model,-1)
        with self.assertRaises(ValueError): PresentReport('',Frame(),self.event,self.model,1,F(0))


class BellRendezvousTests(unittest.TestCase):
    def test_clean_bell_and_locals(self):
        state=bell_with_environment(1)
        rho=reduced_density(state,(0,1))
        self.assertEqual(purity(rho),1)
        self.assertEqual(bell_probabilities(rho),{'Phi+':1,'Phi-':0,'Psi+':0,'Psi-':0})
        self.assertEqual(reduced_density(state,(0,)),((F(1,2),0),(0,F(1,2))))
        self.assertEqual(reduced_density(state,(1,)),((F(1,2),0),(0,F(1,2))))

    def test_single_pauli_errors_stay_pure_entangled_but_flip_syndrome(self):
        expected={'I':'Phi+','X':'Psi+','Z':'Phi-','XZ':'Psi-'}
        for gate,outcome in expected.items():
            state=pauli_path(bell_with_environment(),0,gate)
            self.assertEqual(purity(reduced_density(state)),1)
            self.assertEqual(pauli_pair_syndrome(gate,'I'),outcome)
            self.assertEqual(reduced_density(state,(0,)),((F(1,2),0),(0,F(1,2))))
        # The quantum entanglement is not 'collapsed' by an incoherent unitary path.

    def test_double_wrong_paths_look_correct_at_middle(self):
        gates=('I','X','Z','XZ')
        groups={label:[] for label in ('Phi+','Phi-','Psi+','Psi-')}
        for a,b in itertools.product(gates,repeat=2):
            groups[pauli_pair_syndrome(a,b)].append((a,b))
        self.assertEqual(set(groups['Phi+']),{('I','I'),('X','X'),('Z','Z'),('XZ','XZ')})
        self.assertEqual(tuple(len(v) for v in groups.values()),(4,4,4,4))

    def test_independent_reference_pairs_detect_both_local_pauli_errors(self):
        gates=('I','X','Z','XZ')
        outcomes={independent_reference_syndrome(a,b) for a,b in itertools.product(gates,repeat=2)}
        self.assertEqual(len(outcomes),16)
        self.assertEqual([p for p in itertools.product(gates,repeat=2)
                          if independent_reference_syndrome(*p)==('Phi+','Phi+')],[('I','I')])
        # Only holds if one path's error acts uniformly on twin and its distinct witness qubit.

    def test_which_path_carrier_record_dephases_without_measurement(self):
        clean=bell_with_environment(1)
        marked=controlled_not(clean,0,2)
        rho=reduced_density(marked,(0,1))
        self.assertEqual(purity(rho),F(1,2))
        self.assertEqual(bell_probabilities(rho),{'Phi+':F(1,2),'Phi-':F(1,2),'Psi+':0,'Psi-':0})
        # Both local models/marginals remain I/2; joint coherence lost.
        for k in (0,1):
            self.assertEqual(reduced_density(marked,(k,)),((F(1,2),0),(0,F(1,2))))
        self.assertEqual(purity(reduced_density(marked,(0,1,2))),1)
        self.assertEqual(controlled_not(marked,0,2),clean)

    def test_same_environment_can_be_uncomputed_by_both_interactions(self):
        clean=bell_with_environment(1)
        once=controlled_not(clean,0,2)
        twice=controlled_not(once,1,2)
        self.assertEqual(twice,clean)
        self.assertEqual(purity(reduced_density(twice,(0,1))),1)
        self.assertEqual(bell_probabilities(reduced_density(twice,(0,1)))['Phi+'],1)
        # Both interacted with the carrier; it retains zero which-path record at meeting.

    def test_two_distinct_environment_records_are_not_erased(self):
        clean=bell_with_environment(2)
        marked=controlled_not(controlled_not(clean,0,2),1,3)
        self.assertEqual(purity(reduced_density(marked,(0,1))),F(1,2))
        self.assertEqual(bell_probabilities(reduced_density(marked,(0,1)))['Phi+'],F(1,2))
        self.assertEqual(purity(reduced_density(marked,(0,1,2,3))),1)

    def test_rational_partial_marker_exact_visibility_distinguishability(self):
        for t in (F(0),F(1,3),F(1,2),F(1),F(2)):
            gamma,Fbell,p,d2=exact_marker_coherence(t)
            marked=rational_overlap_marker(t)
            rho=reduced_density(marked,(0,1))
            self.assertEqual(bell_probabilities(rho)['Phi+'],Fbell)
            self.assertEqual(purity(rho),p)
            self.assertEqual(1-gamma*gamma,d2)
            self.assertEqual(purity(reduced_density(marked,(0,1,2))),1)
        self.assertEqual(exact_marker_coherence(F(1,2)),(F(3,5),F(4,5),F(17,25),F(16,25)))

    def test_bell_plus_click_from_mixed_state_is_not_purity_certificate(self):
        rho=reduced_density(controlled_not(bell_with_environment(1),0,2),(0,1))
        self.assertEqual(bell_probabilities(rho)['Phi+'],F(1,2))
        self.assertNotEqual(purity(rho),1)

    def test_local_measurement_is_not_necessary_for_decoherence(self):
        # Coherent CNOT entangles with E and alone changes reduced AB purity.
        a=bell_with_environment(1)
        b=controlled_not(a,0,2)
        self.assertEqual(purity(reduced_density(a)),1)
        self.assertEqual(purity(reduced_density(b)),F(1,2))

    def test_frame_twist_corrected_only_at_rendezvous(self):
        encoded=pauli_path(bell_with_environment(),1,'Z')
        self.assertEqual(bell_probabilities(reduced_density(encoded))['Phi+'],0)
        transported=pauli_path(encoded,1,'Z')
        self.assertEqual(bell_probabilities(reduced_density(transported))['Phi+'],1)
        # Correct basis transport is an additional trusted frame operation.

    def test_invalid_gates_and_registers_rejected(self):
        state=bell_with_environment(1)
        with self.assertRaises(ValueError): pauli_path(state,3,'X')
        with self.assertRaises(ValueError): pauli_path(state,0,'H')
        with self.assertRaises(ValueError): controlled_not(state,0,0)
        with self.assertRaises(ValueError): reduced_density(state,(0,0))
        with self.assertRaises(ValueError): bell_probabilities(((1,0),(0,1)))
        with self.assertRaises(ValueError): bell_with_environment(-1)
        with self.assertRaises(ValueError): purity(((1,0),))


if __name__ == '__main__':
    unittest.main()
