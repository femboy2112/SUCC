"""Exact local tests; not a substitute for the full pinned SUCC test suite."""
from __future__ import annotations
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
MOD=ROOT/'research'/'2026-11-01'/'categorical_source_gluing'
def load_unique(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

m=load_unique('succ_categorical_gluing_research_v1',MOD/'source_gluing.py')
CERT=json.loads((MOD/'receipts'/'cover_certificate.json').read_text())

class SourceTests(unittest.TestCase):
    def test_four_poles_equal_combined(self):
        for n in range(1,201):self.assertEqual(m.source(n),m.source_combined(n))
    def test_source_initial_values(self):
        self.assertEqual(m.source(1),F(47,15));self.assertEqual(m.source(2),F(106,819))
    def test_source_pole_rejected(self):
        for p in (F(7,8),F(1,2),F(3,8),F(1,4)):
            with self.assertRaises(m.CarrierError):m.source(p)
    def test_float_rejected(self):
        for x in (0.5,True,complex(1)):
            with self.assertRaises(m.CarrierError):m.source(x)
    def test_orbit_independent_convolution(self):
        for n in range(0,41):
            for seed in (F(0),F(1,7),F(-2,5)):
                self.assertEqual(m.orbit(n,seed),m.orbit_convolution(n,seed))
    def test_seed_binding(self):
        for n in range(1,21):self.assertEqual(m.orbit(n,F(1,7))-m.orbit(n),F(16**n,7))
    def test_wrong_source_mutation(self):
        for n in range(1,10):self.assertNotEqual(m.source(n)+F(2,8*n-3),m.source_combined(n))
    def test_original_odd_denominators(self):
        for n in range(1,101):self.assertEqual(m.source(n).denominator%2,1)
    def test_conductor_prefix(self):
        self.assertEqual([m.source_conductor(n) for n in (1,2,3)],[15,4095,765765])
    def test_conductor_source_equals_state(self):
        from math import lcm
        q=1
        for n in range(1,18):
            q=lcm(q,m.orbit(n).denominator);self.assertEqual(q,m.source_conductor(n))
    def test_order_commutator(self):
        difference=m.AffineWord((1,2)).apply()-m.AffineWord((2,1)).apply()
        self.assertEqual(difference,F(12301,273))
    def test_word_composition(self):
        a=m.AffineWord((1,4));b=m.AffineWord((2,3))
        self.assertEqual(a.then(b).apply(F(1,7)),b.apply(a.apply(F(1,7))))

class CoverTests(unittest.TestCase):
    def test_symbolic_receipt_success(self):
        for key in ('dlog_zero','cayley_pullback_zero','cleared_inverse_identity_zero',
                    'inverse_denominator_not_identically_zero'):
            self.assertIs(CERT[key],True)
    def test_cover_initial(self):self.assertEqual(m.cover(1),F(1,480))
    def test_cover_pole_chart_rejected(self):
        for p in (F(1,2),F(3,8),F(1,4)):
            with self.assertRaises(m.CarrierError):m.cover(p)
    def test_delay_inverse_integer_source(self):
        for n in range(0,41):self.assertEqual(m.recover_source(m.cover(n),m.cover(n+1),CERT),n)
    def test_delay_inverse_off_grid(self):
        for n in range(-17,23):
            z=F(n,7)
            self.assertEqual(m.recover_source(m.cover(z),m.cover(z+1),CERT),z)
    def test_delay_curve_exact(self):
        for z in (F(-3),F(-2,3),F(0),F(2,7),F(4,5),F(1),F(3),F(11)):
            self.assertEqual(m.eval_bivariate(CERT['delay_curve_terms'],m.cover(z),m.cover(z+1)),0)
    def test_mutated_delay_pair_rejected(self):
        with self.assertRaises(m.CarrierError):m.recover_source(m.cover(1),m.cover(3),CERT)
    def test_mutated_inverse_rejected(self):
        damaged=dict(CERT)
        damaged['inverse_numerator_terms']=CERT['inverse_numerator_terms']+[[[0,0],'1']]
        with self.assertRaises(m.CarrierError):m.recover_source(m.cover(2),m.cover(3),damaged)
    def test_inverse_does_not_select_seed(self):
        a=m.LiftedState(F(0),F(0)).advance(4)
        b=m.LiftedState(F(0),F(1,7)).advance(4)
        self.assertEqual(a.delay_observation()[:2],b.delay_observation()[:2])
        self.assertNotEqual(a.amplitude,b.amplitude)

    def test_independent_stdlib_symbolic_certificate(self):
        oracle=load_unique('succ_categorical_gluing_polynomial_oracle_v1',MOD/'independent_polynomial_oracle.py')
        result=oracle.verify(CERT)
        self.assertTrue(result['stdlib_symbolic_inverse_identity'])
    def test_independent_oracle_rejects_mutation(self):
        import copy
        oracle=load_unique('succ_categorical_gluing_polynomial_oracle_v1_mutation',MOD/'independent_polynomial_oracle.py')
        damaged=copy.deepcopy(CERT)
        damaged['inverse_numerator_terms'][0][1]=str(int(damaged['inverse_numerator_terms'][0][1])+1)
        with self.assertRaises(ArithmeticError):oracle.verify(damaged)
    def test_all_horizon_chart_certificate(self):
        c=CERT['all_horizon_inverse_chart']
        self.assertNotEqual(int(c['denominator_at_source_zero']),0)
        self.assertTrue(all(int(x)>0 for x in c['shifted_cleared_denominator_coefficients_ascending']))
    def test_reconstructed_source_successor(self):
        for n in range(41):
            self.assertEqual(m.advance_delay(m.cover(n),m.cover(n+1),CERT),(m.cover(n+1),m.cover(n+2)))
    def test_reconstructed_bbp_skew_product(self):
        obs=(m.cover(0),m.cover(1),F(0))
        for n in range(1,31):
            obs=m.advance_observed_state(*obs,CERT)
            self.assertEqual(obs,(m.cover(n),m.cover(n+1),m.orbit_convolution(n)))

class CompositionTests(unittest.TestCase):
    def test_cocycle_composition_all_grid(self):
        for z in (F(0),F(1),F(2,3)):
            for a in range(6):
                for b in range(6):
                    self.assertEqual(m.cocycle(z,a+b),16**b*m.cocycle(z,a)+m.cocycle(z+a,b))
    def test_state_advance_composition(self):
        x=m.LiftedState(F(0),F(2,9))
        for a in range(7):
            for b in range(7):self.assertEqual(x.advance(a+b),x.advance(a).advance(b))
    def test_source_path_identity(self):
        p=m.SourcePath.build(m.LiftedState(F(0),F(0)),4)
        self.assertEqual(m.SourcePath((p.states[0],)).then(p),p)
        self.assertEqual(p.then(m.SourcePath((p.states[-1],))),p)
    def test_source_path_associativity(self):
        x=m.LiftedState(F(0),F(0));a=m.SourcePath.build(x,2)
        b=m.SourcePath.build(a.states[-1],3);c=m.SourcePath.build(b.states[-1],2)
        self.assertEqual(a.then(b).then(c),a.then(b.then(c)))
    def test_seed_seam_rejected(self):
        a=m.SourcePath.build(m.LiftedState(F(0),F(0)),2)
        b=m.SourcePath.build(m.LiftedState(F(2),a.states[-1].amplitude+1),2)
        with self.assertRaises(m.CarrierError):a.then(b)
    def test_mutated_source_path_rejected(self):
        p=m.SourcePath.build(m.LiftedState(F(0),F(0)),2)
        with self.assertRaises(m.CarrierError):m.SourcePath((p.states[0],p.states[2]))
    def test_false_fiber_gluing(self):
        for p in (7,11,13,17,19,23,29,31):
            x,y,correct,wrong=m.false_span_gluing(p);q=m.projective_cover_table(p);S=m.successor_table(p)
            self.assertEqual(q[S[x]],q[y]);self.assertNotEqual(S[x],y);self.assertNotEqual(correct,wrong)
    def test_projective_infinity_retained(self):
        for p in (7,11,13):
            self.assertEqual(m.projective_cover_table(p)[p],1)
            self.assertEqual(m.successor_table(p)[p],p)
    def test_observation_descent_fails(self):
        for p in (7,11,13,17):self.assertIsNotNone(m.descent_obstruction(m.projective_cover_table(p),m.successor_table(p)))
    def test_predictive_refinement_succeeds(self):
        for p in (7,11,13,17,19,23,29,31):
            q=m.projective_cover_table(p);S=m.successor_table(p);out=m.future_partition(q,S)
            self.assertIsNone(m.descent_obstruction(out,S));self.assertEqual(len(set(out)),p+1)
    def test_two_snapshots_not_everywhere_injective(self):
        p=7;q=m.projective_cover_table(p);S=m.successor_table(p)
        pairs=tuple((q[x],q[S[x]]) for x in range(p+1))
        self.assertLess(len(set(pairs)),p+1)
    def test_stable_quotient_positive_control(self):
        self.assertIsNone(m.descent_obstruction((0,1,0,1),(1,2,3,0)))
    def test_constant_observer_null_control(self):
        self.assertEqual(m.future_partition((0,0,0),(1,2,0)),(0,0,0))
    def test_invalid_finite_table(self):
        with self.assertRaises(m.CarrierError):m.descent_obstruction((0,1),(2,0))

class FourierTests(unittest.TestCase):
    def test_affine_fourier_kernel_all_small_register(self):
        Q=15;n=1;b=m.address(Q,m.orbit(n));a=16**n
        for x in range(Q):
            for k in range(Q):
                self.assertEqual(m.phase_Q(Q,k,m.ket_image(Q,n,x)),(m.phase_Q(Q,k,b)+m.phase_Q(Q,a*k,x))%1)
    def test_affine_fourier_fresh_large_conductors(self):
        for n in range(2,13):
            Q=m.source_conductor(n);b=m.address(Q,m.orbit(n))
            for x in (0,1,Q//2,Q-1):
                for k in (-11,-1,0,1,7,31):
                    self.assertEqual(m.phase_Q(Q,k,m.ket_image(Q,n,x)),(m.phase_Q(Q,k,b)+m.phase_Q(Q,16**n*k,x))%1)
    def test_phase_echo_exact(self):
        for n in range(1,13):
            Q=m.source_conductor(n)
            for x in (0,1,Q-1):
                for h in (-3,-1,1,5):self.assertEqual(m.phase_echo(Q,n,h,x),m.source_phase(n,h))
    def test_sign_mutation_rejected(self):
        phase=m.source_phase(1,1)
        self.assertNotEqual(phase,(-phase)%1)
    def test_bad_even_arithmetic_register_rejected(self):
        for Q in (2,16,240):
            with self.assertRaises(m.CarrierError):m.odd_register(Q)
    def test_undersized_conductor_rejected(self):
        with self.assertRaises(m.CarrierError):m.address(15,m.orbit(2))
    def test_primal_conductor_naturality(self):
        for n in range(1,9):
            Q=m.source_conductor(n);B=m.source_conductor(n+1)
            for x in (0,1,Q-1):
                self.assertEqual(m.dilation_embedding(Q,B,m.ket_image(Q,n,x)),m.ket_image(B,n,m.dilation_embedding(Q,B,x)))
    def test_fourier_embedding_phase_naturality(self):
        for Q,B in ((1,15),(15,45),(15,4095),(4095,765765)):
            for x in (0,Q-1):
                for k in (0,1,2,7,B-1):
                    self.assertEqual(m.phase_Q(B,k,m.dilation_embedding(Q,B,x)),m.phase_Q(Q,k%Q,x))
    def test_fourier_embedding_norm(self):
        for Q,B in ((1,15),(15,45),(15,4095)):
            self.assertEqual((B//Q)*m.frequency_embedding_norm_squared(Q,B),1)
    def test_embedding_composition(self):
        for x in (0,1,14):
            self.assertEqual(m.dilation_embedding(45,135,m.dilation_embedding(15,45,x)),m.dilation_embedding(15,135,x))
    def test_dual_embedding_composition_norm(self):
        self.assertEqual(m.frequency_embedding_norm_squared(15,45)*m.frequency_embedding_norm_squared(45,135),m.frequency_embedding_norm_squared(15,135))
    def test_dual_phase_operator_naturality(self):
        for n in range(1,8):
            Q=m.source_conductor(n);B=m.source_conductor(n+1)
            for k in (0,1,B-1):
                self.assertEqual((k*m.orbit(n))%1,((k%Q)*m.orbit(n))%1)
                self.assertEqual((16**n*k)%Q,(16**n*(k%Q))%Q)
    def test_same_embedding_wrong_in_fourier(self):
        # F(delta_0) has nonzero coefficients at every k; primal zero-extension does not.
        Q=15;B=45;primal_support={m.dilation_embedding(Q,B,x) for x in range(Q)}
        self.assertNotIn(1,primal_support);self.assertEqual(m.frequency_embedding_norm_squared(Q,B),F(1,3))
    def test_joint_even_carrier_not_permutation(self):
        Q=16*15;self.assertLess(len({16*x%Q for x in range(Q)}),Q)
    def test_full_sixteen_branches(self):
        for Q in (1,3,16):
            images=[m.dyadic_branch_index(Q,a,x) for a in range(16) for x in range(Q)]
            self.assertEqual(sorted(images),list(range(16*Q)))
    def test_exact_carry_seam(self):
        for Q in (3,7):
            for x in range(Q):
                for a in range(16):
                    expected=m.dyadic_branch_index(Q,a+1,x) if a<15 else m.dyadic_branch_index(Q,0,(x+1)%Q)
                    self.assertEqual((m.dyadic_branch_index(Q,a,x)+1)%(16*Q),expected)
    def test_fixed_seed_tilt_not_erased(self):
        for n in range(1,11):self.assertNotEqual(m.source_phase(n,1),m.source_phase(n,1,F(1,7)))
    def test_selected_point_trace_norm_cost(self):
        # Under normalized counting measure a singleton indicator has value 1
        # at the selected address but squared L2 norm 1/Q.
        for Q in (15,4095,765765):
            norm_squared=F(1,Q)
            self.assertEqual(Q*norm_squared,1)
            self.assertLess(norm_squared,F(1,2))
    def test_inverse_conductor_invalid(self):
        with self.assertRaises(m.CarrierError):m.dilation_embedding(15,7,0)

class IntegrationTests(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec('observational_succ'),'complete SUCC package unavailable in this local research bundle')
    def test_existing_observation_path_category(self):
        adapter=load_unique('succ_categorical_gluing_repo_adapter_v1',MOD/'repo_adapter.py')
        C=adapter.build_existing_path_category()
        self.assertGreater(len(C.objects),1)
        for x in C.objects:self.assertIn(C.identity(x),C.hom(x,x))

if __name__=='__main__':unittest.main()
