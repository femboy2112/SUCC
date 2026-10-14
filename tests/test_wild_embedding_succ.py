"""Adversarial, exact tests for Alexander wild-embedding SUCC offshoot.

Finite source algebra is executable; infinite topology and operator theorems
are paper proofs with imported classical prerequisites, NOT finite-test claims.
"""
from __future__ import annotations
import json
import random
import unittest
from fractions import Fraction as Q
from math import comb
from observational_succ.wild_embedding_succ import (
    WildSUCCError, genuine_prime, free_reduce, inverse, commutator,
    horn_step, horn_transport, abelian_shadow, meridian_report,
    leading_magnus, magnus_monomial_count, truncated_magnus,
    nilpotent_visibility, unitriangular_meridian, periodic_prime_sphere, localized_rational,
    delayed_prime_bonds, flattened_warp, benign_inverse_distortion,
    wavefront_shadow, escape_witness, two_chart_schur, receipt,
    gaussian_prime_phase_packets, dense_prime_clock_collision,
)


class AlexanderSourceTests(unittest.TestCase):
    def test_group_reduce_inverse(self):
        self.assertEqual(free_reduce((1,2,-2,-1,3,-3)),())
        self.assertEqual(inverse((1,2,-1)),(1,-2,-1))
        for s in ((1,), (1,2,-1), (1,-1,2,3,-3),(-1,-2,1,2)):
            a=free_reduce(s)
            self.assertEqual(free_reduce(a+inverse(a)),())

    def test_basic_commutator_is_nonabelian(self):
        w=commutator((1,),(2,))
        self.assertEqual(w,(1,2,-1,-2))
        self.assertEqual(abelian_shadow(w,1),(0,0))
        self.assertNotEqual(w,())

    def test_stage_map_exact_hatcher(self):
        self.assertEqual(horn_step((1,),0),(1,2,-1,-2))
        self.assertEqual(horn_step((-1,),0),(2,1,-2,-1))
        self.assertEqual(horn_step((1,),1),(1,2,-1,-2))
        self.assertEqual(horn_step((2,),1),(3,4,-3,-4))

    def test_homomorphism_and_reduced_identities(self):
        samples=[(1,),(-1,),(2,), (1,2,-1), (1,2,-2,3,-3,-1)]
        for u in samples:
            for v in samples:
                self.assertEqual(horn_step(free_reduce(u+v),2),
                                 free_reduce(horn_step(u,2)+horn_step(v,2)))

    def test_nonabelian_meridian_survives_six_stages(self):
        for k in range(7):
            x=meridian_report(k)
            self.assertEqual(x['free_word_length'],4**k)
            self.assertEqual(x['rank'],2**k)
            self.assertTrue(x['survives_nonabelian'])
            self.assertEqual(x['abelian_shadow'],[0]*(2**k) if k else [1])

    def test_all_stage_abelian_maps_annihilate(self):
        rand=random.Random(8271)
        for stage in range(4):
            for _ in range(35):
                word=tuple(rand.choice((-1,1))*rand.randint(1,2**stage)
                           for _ in range(8))
                self.assertEqual(abelian_shadow(horn_step(word,stage),stage+1),
                                 (0,)*(2**(stage+1)))

    def test_direct_transport_equals_iterated_step(self):
        for start in range(4):
            for depth in range(3):
                w=(1,)
                direct=horn_transport(w,start,depth)
                for d in range(depth):
                    w=horn_step(w,start+d)
                self.assertEqual(w,direct)

    def test_direct_limit_deep_root_length(self):
        for k in range(6):
            x=horn_transport((1,),0,k)
            self.assertEqual(len(x),4**k)
            self.assertEqual(len(set(abs(q) for q in x)),2**k)

    def test_leading_magnus_exact_hall_commutator(self):
        for depth in range(5):
            lead=leading_magnus(depth)
            self.assertEqual(len(lead),magnus_monomial_count(depth))
            self.assertEqual({len(k) for k in lead},{2**depth})
            self.assertEqual(set(lead.values()),{1,-1} if depth else {1})
            self.assertTrue(all(len(set(k))==len(k) for k in lead))

    def test_independent_magnus_truncation(self):
        for depth in (1,2):
            w=horn_transport((1,),0,depth)
            full=truncated_magnus(w,depth,2**depth)
            low=truncated_magnus(w,depth,2**depth-1)
            self.assertEqual(low,{():1})
            leading={monom:c for monom,c in full.items() if monom}
            self.assertEqual(leading,leading_magnus(depth))

    def test_nilpotent_depth_visibility(self):
        for depth in range(1,10):
            q=nilpotent_visibility(depth,2**depth-1)
            self.assertTrue(q['nilpotent_probe_cannot_detect'])
            self.assertTrue(q['nonabelian_direct_limit_survives'])
            self.assertFalse(nilpotent_visibility(depth,2**depth)['nilpotent_probe_cannot_detect'])

    def test_sharp_finite_dimensional_nilpotent_detector(self):
        # First 4 stages admit exact unipotent algebra detectors of class 2^k.
        # These do NOT glue into a nilpotent representation of the global G.
        for k in range(4):
            x=unitriangular_meridian(k)
            self.assertEqual(x['matrix_dimension'],2**k+1)
            self.assertEqual(x['nilpotency_class'],2**k)
            self.assertEqual(x['nonzero_top_right'],1)
            self.assertTrue(x['not_compatible_with_entire_perfect_direct_limit'])

    def test_no_false_global_phi1_statement(self):
        # F_n has H1 rank 2^n; its transported generators vanish in H1
        # of F_(n+1). The final direct limit is perfect, but nontrivial.
        for n in range(6):
            w=(1,)
            self.assertNotEqual(abelian_shadow(w,n),(0,)*(2**n))
            self.assertEqual(abelian_shadow(horn_step(w,n),n+1),(0,)*(2**(n+1)))


class PrimeSphereTowerTests(unittest.TestCase):
    def test_source_primitive_primes(self):
        for p in (2,3,5,7,11,97):
            self.assertEqual(genuine_prime(p),p)
        for m in (1,4,6,8,9,10,12,21,49):
            with self.assertRaises(WildSUCCError):
                genuine_prime(m)

    def test_tower_cech_H2_nonstandard(self):
        x=periodic_prime_sphere((2,3,2))
        self.assertEqual(x['limit_cech_H2'],'Z[1/2,1/3]')
        self.assertEqual(x['source_prime_cycle'],[2,3,2])
        self.assertFalse(x['limit_is_S2'])
        self.assertTrue(x['not_the_Alexander_horned_sphere'])

    def test_single_prime_tower(self):
        self.assertEqual(periodic_prime_sphere((5,))['limit_cech_H2'],'Z[1/5]')
        with self.assertRaises(WildSUCCError):
            periodic_prime_sphere((6,))

    def test_localized_rational_decision(self):
        for numerator in (-13,1,22,45):
            for b in range(7):
                for c in range(4):
                    q=Q(numerator,2**b*3**c)
                    self.assertTrue(localized_rational(q,(2,3)))
        self.assertFalse(localized_rational(Q(1,5),(2,3)))
        self.assertTrue(localized_rational(Q(10,25),(2,5)))
        self.assertTrue(localized_rational(Q(),(3,)))

    def test_delayed_prime_twist_hidden_to_finite_probe(self):
        for delay in (5,9,14):
            x=delayed_prime_bonds(delay,delay+3,2)
            self.assertTrue(x['same_as_identity_source'])
            self.assertEqual(x['observed_bonds'],[1]*delay)
            self.assertNotEqual(x['identity_limit_H2'],x['delayed_twist_limit_H2'])
            y=delayed_prime_bonds(delay+1,delay,2)
            self.assertFalse(y['same_as_identity_source'])
            self.assertEqual(y['observed_bonds'][-1],2)

    def test_no_sphere_global_from_stagewise_spheres(self):
        for x in ((2,),(2,3),(2,3,5)):
            q=periodic_prime_sphere(x)
            self.assertEqual(q['every_finite_stage_topology'],'S2')
            self.assertFalse(q['limit_is_S2'])


class WildMetricAndWeilControls(unittest.TestCase):
    def test_flattening_warp_inverse_debt(self):
        for n in (2,3,5,20,100):
            x=flattened_warp(Q(1,n))
            self.assertEqual(x['inverse_Lipschitz'],n)
            self.assertEqual(x['left_slope'],Q(1,n))
            self.assertEqual(x['right_slope'],2-Q(1,n))
            self.assertEqual(x['uniform_forward_error_at_most'],Q(1,2*n))

    def test_distortion_not_sufficient_for_wildness(self):
        for n in (2,4,9,100):
            for r in (Q(-1),Q(-1,3),Q(0),Q(1,2),Q(1)):
                x=benign_inverse_distortion(Q(1,n),r)
                self.assertLessEqual(abs(x['value']-x['limit_homeomorphism_value']),
                                     Q(1,n))
                self.assertTrue(x['limit_is_tame_homeomorphism'])
                self.assertEqual(x['inverse_lipschitz'],n+1)

    def test_exact_wavefront_two_tent_states(self):
        for n in range(1,9):
            eps=Q(1,2**n)
            x=wavefront_shadow(eps,Q(2,3))
            self.assertEqual(x['normalized_symmetric_Rayleigh'],-Q(2,3))
            self.assertEqual(x['normalized_antisymmetric_Rayleigh'],Q(2,3))
            self.assertEqual(x['unit_L2_tent_H1_derivative_energy'],12/eps**2)
            self.assertEqual(x['continuous_hinge_HS_norm_squared'],Q(4,9)*eps**4/6)
            self.assertEqual(x['true_H1_Riesz_norm_squared_upper'],Q(4,9)*eps**4/6)
            self.assertEqual(x['H1_tent_negative_Rayleigh'],-Q(2,3)/(1+12/eps**2))

    def test_strong_but_not_operator_norm(self):
        x=wavefront_shadow(Q(1,2**20),Q(2,3))
        self.assertLess(x['continuous_hinge_HS_norm_squared'],Q(1,10**20))
        self.assertEqual(x['offdiagonal_operator_norm'],Q(2,3))
        self.assertGreater(x['unit_L2_tent_H1_derivative_energy'],10**12)
        self.assertTrue(x['strong_not_norm_convergence_if_c_fixed_positive'])

    def test_H1_metric_restores_norm_control(self):
        x=wavefront_shadow(Q(1,1024),Q(2,3))
        self.assertLess(x['true_H1_Riesz_norm_squared_upper'],Q(1,10**12))
        self.assertLess(abs(x['H1_tent_negative_Rayleigh']),Q(1,10**6))
        self.assertEqual(x['offdiagonal_operator_norm'],Q(2,3))

    def test_generic_negative_hidden_rank_one(self):
        for n in (10,100,1000):
            r=escape_witness(n,10*n)
            self.assertTrue(r['all_observed_compressions_zero'])
            self.assertEqual(r['actual_full_operator_negative_eigenvalue'],-1)
            self.assertTrue(r['collective_compactness_fails'])
            self.assertTrue(r['not_the_actual_Weil_operator'])

    def test_actual_source_schur_boundary_not_automatic(self):
        self.assertFalse(two_chart_schur(1,1,2)['global_nonnegative'])
        self.assertEqual(two_chart_schur(1,1,2)['schur_remainder'],-3)
        self.assertTrue(two_chart_schur(2,2,1)['global_nonnegative'])
        self.assertEqual(two_chart_schur(2,2,1)['schur_remainder'],Q(3,2))
        self.assertTrue(two_chart_schur(1,1,1)['global_nonnegative'])

    def test_invalid_inputs_refused(self):
        funcs=[lambda:free_reduce((0,)),lambda:horn_step((3,),1),
               lambda:horn_transport((1,),3,7),lambda:truncated_magnus((1,),0,6),
               lambda:genuine_prime(True),lambda:genuine_prime(6),
               lambda:periodic_prime_sphere((6,)),lambda:localized_rational(.5,(2,)),
               lambda:flattened_warp(0),lambda:wavefront_shadow(Q(),1),
               lambda:benign_inverse_distortion(Q(1,2),Q(2)),
               lambda:escape_witness(5,5),lambda:two_chart_schur(0,1,1)]
        for fn in funcs:
            with self.subTest(fn=str(fn)),self.assertRaises(WildSUCCError):
                fn()

    def test_source_typed_gaussian_solenoid_packets(self):
        p=gaussian_prime_phase_packets((2,3), (Q(),Q(1,2),Q(1,3)),
                                        32,Q(1),Q(1))
        self.assertTrue(p['all_characters_verified'])
        self.assertTrue(p['approximate_isometry_verified'])
        self.assertLess(Q(p['offdiag_gram_operator_upper']),Q(1,5))
        self.assertLess(Q(p['translation_residual_norm_squared_upper']),Q(1,250))
        self.assertEqual(Q(p['individual_compact_window_mass_upper']),Q(3,32))
        self.assertFalse(p['bounded_global_solenoid_to_L2_intertwiner_exists'])
        self.assertTrue(p['prime_character_source_is_circle_solenoid_not_sphere'])
        self.assertTrue(p['distributional_limit_not_L2_limit'])

    def test_gaussian_packet_approximation_rate(self):
        last_t=last_g=last_m=Q(100)
        for n in (8,16,32,64,128):
            p=gaussian_prime_phase_packets((2,), (Q(),Q(1,2)),n,Q(2),Q(3))
            t=Q(p['translation_residual_norm_squared_upper'])
            g=Q(p['offdiag_gram_operator_upper'])
            m=Q(p['individual_compact_window_mass_upper'])
            self.assertTrue(0<t<last_t and 0<g<last_g and 0<m<last_m)
            last_t,last_g,last_m=t,g,m

    def test_dense_local_frequencies_defeat_one_packet_scale(self):
        for prime in (2,3,5):
            for n in (2,7,32,1000):
                x=dense_prime_clock_collision(prime,n)
                self.assertGreater(Q(x['Gram_offdiagonal_strict_lower']),Q(9,10))
                self.assertTrue(x['no_uniform_all_frequency_isometry'])
                self.assertEqual(x['genuine_prime'],prime)

    def test_gaussian_source_guards_not_generic_complex_wavepackets(self):
        bad=[lambda:gaussian_prime_phase_packets((6,),(Q(),),8,1,1),
             lambda:gaussian_prime_phase_packets((2,),(Q(1,3),),8,1,1),
             lambda:gaussian_prime_phase_packets((2,), (Q(),Q()),8,1,1),
             lambda:gaussian_prime_phase_packets((2,), (Q(1,2),),1,1,1),
             lambda:gaussian_prime_phase_packets((2,), (Q(1,2),),8,-1,1),
             lambda:gaussian_prime_phase_packets((2,), (Q(1,2),),8,1,-1),
             lambda:gaussian_prime_phase_packets((2,), (Q(1,2),),8,.5,1),
             lambda:dense_prime_clock_collision(6,10)]
        for f in bad:
            with self.subTest(f=str(f)),self.assertRaises(WildSUCCError):f()

    def test_exact_receipt_roundtrip_and_firewall(self):
        a=receipt()
        b=json.loads(json.dumps(a))
        self.assertEqual(a,b)
        self.assertFalse(a['completed_Weil_positive'])
        self.assertFalse(a['RH_proved'])
        self.assertEqual(a['meridian_tower'][-1]['free_word_length'],256)
        self.assertEqual(a['leading_Lie_terms']['3']['count'],128)


if __name__=='__main__':
    unittest.main()
