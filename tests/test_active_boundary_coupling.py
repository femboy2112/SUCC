"""Exact adversarial controls for finite quantum alphabet/backaction barriers."""
import unittest
from fractions import Fraction as Q

from observational_succ.active_boundary_coupling import (
    InstrumentContractError, rational, vector, inner, overlap_components,
    nondemolition_label_possible, gram_isometry_defects,
    gram_marker_isometry_possible, quantitative_leakage_requirement,
    budget_passes_necessary_bound, ReadoutRotation, cnot_meter_on_real_qubit,
    bbp_seed_phase_alias,
)


class ActiveCouplingTests(unittest.TestCase):
    def test_connected_nonorthogonality_chain(self):
        # |0> and |1> are orthogonal but connected *through* the third state.
        states=((1,0),(0,1),(Q(3,5),Q(4,5)))
        self.assertEqual(overlap_components(states),((0,1,2),))
        self.assertFalse(nondemolition_label_possible(states,("zero","one","bridge")))
        self.assertTrue(nondemolition_label_possible(states,("same",)*3))

    def test_disjoint_qnd_classes(self):
        states=((1,0,0),(2,0,0),(0,3,0),(0,0,1))
        self.assertEqual(overlap_components(states),((0,1),(2,),(3,)))
        self.assertTrue(nondemolition_label_possible(states,("a","a","b","c")))
        self.assertFalse(nondemolition_label_possible(states,("a","x","b","c")))

    def test_orthogonal_signaling_without_state_change(self):
        states=((1,0),(0,1))
        markers=((1,0),(0,1))
        self.assertTrue(gram_marker_isometry_possible(states,markers))
        self.assertTrue(nondemolition_label_possible(states,(0,1)))

    def test_nonorthogonal_perfect_marker_forbidden(self):
        states=((1,0),(Q(3,5),Q(4,5)))
        markers=((1,0),(0,1))
        defects=gram_isometry_defects(states,markers)
        self.assertEqual(defects[0][1],Q(3,5))
        self.assertFalse(gram_marker_isometry_possible(states,markers))

    def test_nondisturbing_has_no_probe_information(self):
        states=((1,0),(Q(3,5),Q(4,5)))
        self.assertTrue(gram_marker_isometry_possible(states,((1,0),(1,0))))
        self.assertFalse(gram_marker_isometry_possible(states,((1,0),(Q(3,5),Q(4,5)))))
        self.assertEqual(quantitative_leakage_requirement(*states,(1,0),(1,0)),0)

    def test_transitive_chain_prevents_perfect_label_record(self):
        states=((1,0),(0,1),(Q(3,5),Q(4,5)))
        self.assertFalse(nondemolition_label_possible(states,(0,1,0)))
        self.assertFalse(nondemolition_label_possible(states,(0,1,1)))

    def test_gram_stability_on_rational_rescalings(self):
        states=((2,0),(0,4),(3,4))
        self.assertEqual(overlap_components(states),((0,1,2),))
        self.assertEqual(inner((Q(3,5),Q(4,5)),(1,0)),Q(3,5))

    def test_leakage_bound_tight_type(self):
        s1=(1,0);s2=(Q(3,5),Q(4,5))
        e1=(1,0);e2=(0,1)
        loss=quantitative_leakage_requirement(s1,s2,e1,e2)
        self.assertEqual(loss,Q(3,5))
        self.assertFalse(budget_passes_necessary_bound(loss,Q(1,4)))
        self.assertTrue(budget_passes_necessary_bound(loss,Q(3,10)))

    def test_leakage_degenerate_orthogonal(self):
        self.assertEqual(quantitative_leakage_requirement((1,0),(0,1),(1,0),(0,1)),0)

    def test_active_transduction_and_echo(self):
        p=ReadoutRotation()
        for a in range(-3,4):
            for b in range(-3,4):
                out=p.apply(a,b)
                self.assertEqual(p.reconstruct_hidden(a,out[0]),b)
                self.assertEqual(p.inverse(*out),(Q(a),Q(b)))
                self.assertEqual(sum(x*x for x in out),Q(a*a+b*b))

    def test_active_unmixable_rejected(self):
        with self.assertRaises(InstrumentContractError): ReadoutRotation(1,0)
        with self.assertRaises(InstrumentContractError): ReadoutRotation(3,4)
        with self.assertRaises(InstrumentContractError): ReadoutRotation(Q(3,5),Q(3,5))

    def test_passive_hidden_indistinguishability(self):
        p=ReadoutRotation()
        # Same unforced readout; different active readout.
        pre1 = (Q(2), Q(3))
        pre2 = (Q(2), Q(7))
        self.assertEqual(pre1[0],pre2[0])
        self.assertNotEqual(p.apply(2,3)[0],p.apply(2,7)[0])

    def test_cnot_full_marker_quantifies_backaction(self):
        v=cnot_meter_on_real_qubit((Q(3,5),Q(4,5)))
        self.assertEqual(v["probe_click_one_probability"],Q(16,25))
        self.assertEqual(v["system_survival_fidelity"],Q(337,625))
        self.assertEqual(v["system_fidelity_loss"],Q(288,625))
        self.assertEqual(v["joint_purity"],1)

    def test_qnd_computational_basis(self):
        self.assertEqual(cnot_meter_on_real_qubit((1,0))["system_fidelity_loss"],0)
        self.assertEqual(cnot_meter_on_real_qubit((0,1))["system_fidelity_loss"],0)
        self.assertEqual(cnot_meter_on_real_qubit((0,1))["probe_click_one_probability"],1)

    def test_partial_meter_does_not_purely_measure_nonorthogonal(self):
        v=cnot_meter_on_real_qubit((Q(3,5),Q(4,5)))
        self.assertLess(v["system_purity"],1)
        self.assertNotEqual(v["probe_diagonal"],(Q(1),Q()))

    def test_phase_alias_needs_independent_seed(self):
        self.assertFalse(bbp_seed_phase_alias(0,Q(1,16),0))
        for n in range(1,20):
            self.assertTrue(bbp_seed_phase_alias(0,Q(1,16),n))
        self.assertFalse(bbp_seed_phase_alias(0,Q(1,3),20))
        self.assertTrue(bbp_seed_phase_alias(Q(1,256),0,2))
        self.assertFalse(bbp_seed_phase_alias(Q(1,256),0,1))

    def test_bad_types_and_malformed_contracts(self):
        for f in [lambda:rational(.5),lambda:vector((0,0)),
                  lambda:vector((Q(3,5),Q(1,5)),normalized=True),
                  lambda:inner((1,0),(1,0,0)),
                  lambda:overlap_components(((1,0),(1,0,0))),
                  lambda:nondemolition_label_possible(((1,0),),(0,1)),
                  lambda:gram_isometry_defects(((1,0),),((2,0),)),
                  lambda:bbp_seed_phase_alias(0,1,-1),
                  lambda:budget_passes_necessary_bound(-1,0)]:
            with self.subTest(f=f):
                with self.assertRaises(InstrumentContractError): f()


if __name__ == "__main__":
    unittest.main()
