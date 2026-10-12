"""Exact finite source-shadow SUCC/FUCC, independently enumerated controls."""
import random
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.shadow_source_inference import (
    ShadowCarrier, EmpiricalForm, ShadowSourceError,combined_shadow_rank,
    dot, solve_system)

class ShadowSourceInferenceTests(unittest.TestCase):
    def setUp(self):
        self.c=ShadowCarrier('actual-rational-carrier',0,'source-basis',3)

    def test_one_empirical_form_leaves_orthogonal_source_undetermined(self):
        a=self.c.report('read-a','A',(1,0,0),Q(2))
        result=self.c.shadow_fucc((a,), (1,1,0))
        self.assertEqual(result['status'],'UNRESOLVED')
        self.assertNotEqual(*result['different_target_values'])
        self.assertEqual(result['same_observed_values'],(Q(2),))

    def test_two_independent_empirical_forms_prove_global_claim(self):
        a=self.c.report('read-a','A',(1,0,0),Q(2))
        b=self.c.report('read-b','B',(0,1,0),Q(-3))
        result=self.c.shadow_fucc((a,b),(1,1,0))
        self.assertEqual(result['status'],'PROVED')
        self.assertEqual(result['claim'],-1)
        self.assertEqual(result['proof_coefficients'],(1,1))
        self.assertEqual(result['source_forms'],('read-a','read-b'))

    def test_shadow_fucc_combines_dependent_forms_exactly(self):
        a=self.c.report('sum','A',(1,1,0),Q(7))
        b=self.c.report('difference','B',(1,-1,0),Q(1))
        r=self.c.shadow_fucc((a,b),(1,0,0))
        self.assertEqual(r['status'],'PROVED')
        self.assertEqual(r['claim'],4)
        self.assertEqual(r['proof_coefficients'],(Q(1,2),Q(1,2)))

    def test_shadow_succ_is_monotone_for_one_unchanged_source(self):
        a=self.c.report('sum','A',(1,1,0),7)
        b=self.c.report('difference','B',(1,-1,0),1)
        report=self.c.successor((a,),b,(1,0,0))
        self.assertEqual(report['before']['status'],'UNRESOLVED')
        self.assertEqual(report['after']['status'],'PROVED')
        self.assertEqual(report['epistemic_step_count'],1)
        self.assertEqual(report['new_physical_events'],1)

    def test_incompatible_joint_shadows_are_not_a_proof_of_everything(self):
        a=self.c.report('sum','A',(1,1,0),7)
        b=self.c.report('difference','B',(1,-1,0),1)
        c=self.c.report('third','C',(2,0,0),99)
        out=self.c.shadow_fucc((a,b,c),(0,1,0))
        self.assertEqual(out['status'],'INCONSISTENT_SOURCE')
        proof=out['contradiction']
        self.assertNotEqual(proof['nonzero_value'],0)
        self.assertEqual(sum((w*r.value for w,r in zip(proof['row_combination'],(a,b,c))),Q(0)),
                         proof['nonzero_value'])

    def test_prevent_duplicate_and_wrong_source_reports(self):
        a=self.c.report('a','Alice',(1,0,0),1)
        b=self.c.report('a','Bob',(0,1,0),2)
        with self.assertRaises(ShadowSourceError):
            self.c.shadow_fucc((a,b),(1,0,0))
        other=ShadowCarrier('actual-rational-carrier',1,'source-basis',3)
        with self.assertRaises(ShadowSourceError):
            self.c.shadow_fucc((a,other.report('b','Bob',(0,1,0),2)),(1,0,0))
        with self.assertRaises(ShadowSourceError):
            self.c.report('bad','A',(0.5,0,0),2)
        with self.assertRaises(ShadowSourceError):
            self.c.report('bad','A',(1,0),2)

    def test_diagonal_towers_target_sufficiency_without_full_source(self):
        a=self.c.report('A-ladder','A2',(1,0,0),1)
        b=self.c.report('B-ladder','B2',(0,1,0),2)
        out=combined_shadow_rank(self.c,((a,),(b,)),(1,-1,0))
        self.assertEqual(out['result']['claim'],-1)
        self.assertEqual(out['result']['status'],'PROVED')
        self.assertEqual(out['result']['rank'],2) # Third carrier coordinate not known

    def test_homogeneous_zero_claim_is_a_theorem_without_new_measurement(self):
        r=self.c.shadow_fucc((),(0,0,0))
        self.assertEqual(r['status'],'PROVED')
        self.assertEqual(r['claim'],0)
        self.assertEqual(r['proof_coefficients'],())
        self.assertEqual(self.c.shadow_fucc((),(0,1,0))['status'],'UNRESOLVED')

    def test_row_span_kernel_annihilator_exhaustive_small_rational_forms(self):
        carrier=ShadowCarrier('f',0,'b',2)
        base=[(Q(a),Q(b)) for a,b in product(range(-1,2),repeat=2)]
        count=0
        for va in base:
            for vb in base:
                rs=[carrier.report('a','A',va,0),carrier.report('b','B',vb,0)]
                for target in base:
                    result=carrier.shadow_fucc(rs,target)
                    if result['status']=='PROVED':
                        z=result['proof_coefficients']
                        self.assertEqual(tuple(z[0]*va[j]+z[1]*vb[j] for j in range(2)),target)
                    else:
                        h=result['missing_direction']
                        self.assertEqual(dot(va,h),0)
                        self.assertEqual(dot(vb,h),0)
                        self.assertNotEqual(dot(target,h),0)
                    count+=1
        self.assertEqual(count,9**3)

    def test_rank_growth_bounded_by_new_observations(self):
        rng=random.Random(271828)
        carrier=ShadowCarrier('signal',7,'same-basis',5)
        for _ in range(100):
            rows=[tuple(Q(rng.randrange(-4,5)) for _ in range(5)) for _ in range(4)]
            stages=[solve_system(rows[:n],[0]*n,5)['rank'] for n in range(5)]
            self.assertTrue(all(0<=stages[i+1]-stages[i]<=1 for i in range(4)))

if __name__=='__main__':unittest.main()

class SourceChangingShadowBaseChangeTests(unittest.TestCase):
    def test_valid_factorization_survives_unfaithful_source_refinement(self):
        from observational_succ.shadow_source_inference import verify_shadow_base_change
        # p1=(1,0),p2=(0,1), target=2p1+3p2.
        r=verify_shadow_base_change(((1,0),(0,1)),(2,3),((1,),(1,)))
        self.assertTrue(r['old_target_factored'])
        self.assertTrue(r['new_target_factored'])
        self.assertEqual(r['new_target'],(5,))
        self.assertFalse(r['physical_source_authentication'])

    def test_target_can_descend_after_restriction_but_not_before(self):
        from observational_succ.shadow_source_inference import verify_shadow_base_change
        r=verify_shadow_base_change(((1,0),),(0,1),((1,),(1,)))
        self.assertFalse(r['old_target_factored'])
        self.assertTrue(r['new_target_factored'])
        self.assertTrue(r['converse_unjustified'])

    def test_pullback_composes_in_correct_contravariant_order(self):
        from observational_succ.shadow_source_inference import pullback_form
        A=((1,2),(3,4)) # first source Q2 -> Q2
        B=((5,),(6,))  # second source Q1 -> Q2
        direct=((1*5+2*6,),(3*5+4*6,))
        target=(Q(7),Q(11))
        self.assertEqual(pullback_form(pullback_form(target,A),B),
                         pullback_form(target,direct))

class ShadowProofDesignAndEscapeTests(unittest.TestCase):
    def test_minimal_empirical_probe_support_is_built_before_answers(self):
        from observational_succ.shadow_source_inference import minimal_shadow_probe_design
        forms=((1,0,0),(0,1,0),(1,1,0),(0,0,1))
        r=minimal_shadow_probe_design(forms,(1,1,0))
        self.assertEqual(r['min_num_probes'],1)
        self.assertEqual(r['probe_indices'],(2,))
        self.assertEqual(r['coefficients'],(1,))

    def test_unavailable_probe_menu_is_not_global_impossibility(self):
        from observational_succ.shadow_source_inference import minimal_shadow_probe_design
        self.assertEqual(minimal_shadow_probe_design(((1,0,0),(0,1,0)),(0,0,1))['status'],
                         'UNRESOLVED_MENU')
        with self.assertRaises(ShadowSourceError):
            minimal_shadow_probe_design(((1,0),)*13,(1,0))

    def test_claim_error_bound_is_independent_of_hidden_source_dimensions(self):
        from observational_succ.shadow_source_inference import shadow_claim_error_budget
        self.assertEqual(shadow_claim_error_budget((Q(1,2),Q(-3,2)),
                                                    (Q(1,10),Q(1,20))),Q(1,8))
        with self.assertRaises(ShadowSourceError):
            shadow_claim_error_budget((1,),(Q(-1),))

    def test_escape_to_infinity_undermines_unif_completion(self):
        from observational_succ.shadow_source_inference import receding_shadow_escape
        for n in (1,2,10,100,10000):
            r=receding_shadow_escape(n)
            self.assertGreaterEqual(r['target_at_witness'],Q(1,2))
            self.assertNotEqual(r['target_at_actual'],r['target_at_witness'])
        with self.assertRaises(ShadowSourceError):
            receding_shadow_escape(0)
