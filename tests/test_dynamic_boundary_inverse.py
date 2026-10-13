"""Exact, adversarial RC source-repair regression tests. No floating/zero oracle."""
from fractions import Fraction as Q
import random
import unittest

from observational_succ.dynamic_boundary_inverse import (
    BoundarySourceError, RCNetwork, BoundaryReceipt, observe,
    mat,mm,madd,inv,rank,zeros,quad,
    star,triangle,twin_hubs,serial_pendant,
    reconstruct_y_triangle,filter_candidates,
    scalar_h_from_response,reciprocal_three_frequency_defect,
    scalar_moment_witness,block_hankel,spectral_mode_lower_bound,
    reconstruct_serial_from_moments,reconstruct_serial_from_finite_responses,
    reconstruct_serial_from_receipts,change_interior_capacitance,
    certified_reciprocal_defect,noncommuting_kron_storage_witness,
    exact_star_boundary_memory,demonstration,
)


class SourceNetworkTests(unittest.TestCase):
    def test_exact_static_response(self):
        w=serial_pendant()
        self.assertEqual(w.response(0),(
            (Q(8,5),Q(-3,5),Q(-1)),
            (Q(-3,5),Q(21,10),Q(-3,2)),
            (Q(-1),Q(-3,2),Q(5,2)),
        ))

    def test_static_triangle_star_and_serial_indistinguishable(self):
        self.assertEqual(triangle().response(0),star().response(0))
        self.assertEqual(serial_pendant().response(0),star().response(0))

    def test_static_repair_constructed_without_hidden_model(self):
        report=serial_pendant().response(0)
        cand=reconstruct_y_triangle(report)
        self.assertEqual(cand['arms'],(Q(2),Q(3),Q(5)))
        self.assertNotEqual(cand['triangle'].vertices,cand['star'].vertices)
        self.assertFalse(cand['source_selection_proved'])

    def test_DC_Schur_energy_is_nonnegative(self):
        for w in (star(),triangle(),serial_pendant(),twin_hubs()):
            L=w.response(0)
            for v in ((0,0,0),(1,0,0),(1,-1,0),(2,-3,4)):
                self.assertGreaterEqual(quad(L,v),0)
            self.assertEqual(quad(L,(1,1,1)),0)

    def test_DtN_rows_sum_zero_only_at_static_s_zero(self):
        self.assertTrue(all(sum(row)==0 for row in star().response(0)))
        self.assertTrue(any(sum(row)!=0 for row in star().response(1)))

    def test_matrix_exact_inverse_and_ranks(self):
        A=mat(((2,1),(1,2)))
        Ai=inv(A)
        self.assertEqual(mm(A,Ai),mat(((1,0),(0,1))))
        self.assertEqual(rank(A),2)
        self.assertEqual(rank(mat(((1,2),(2,4)))),1)
        self.assertEqual(rank(mat(((0,0),(0,0)))),0)

    def test_matrix_inversion_rejects_singular(self):
        with self.assertRaises(BoundarySourceError):inv(mat(((1,2),(2,4))))

    def test_forged_negative_conductance_rejected(self):
        with self.assertRaises(BoundarySourceError):star((2,-1,5))
        with self.assertRaises(BoundarySourceError):RCNetwork('bad',('a','b'),('a',),(('a','b',Q(-1)),))

    def test_forged_negative_capacity_rejected(self):
        with self.assertRaises(BoundarySourceError):star(cap=-1)
        with self.assertRaises(BoundarySourceError):serial_pendant(cap0=-1)

    def test_invalid_Laplace_frequency_rejected(self):
        with self.assertRaises(BoundarySourceError):star().response(-1)
        with self.assertRaises(BoundarySourceError):star().response(0.1)

    def test_missing_boundary_anchor_rejected(self):
        with self.assertRaises(BoundarySourceError):
            RCNetwork('unanchored',('a','h1','h2'),('a',),(('h1','h2',Q(2)),))

    def test_duplicate_edges_and_cap_rejected(self):
        with self.assertRaises(BoundarySourceError):
            RCNetwork('dupl',('a','h'),('a',),(('a','h',Q(2)),('h','a',Q(2))))
        with self.assertRaises(BoundarySourceError):
            RCNetwork('capdupl',('a','h'),('a',),(('a','h',Q(2)),),(('h',Q(2)),('h',Q(3))))

    def test_wrong_boundary_as_cap_rejected(self):
        with self.assertRaises(BoundarySourceError):
            RCNetwork('capB',('a','h'),('a',),(('a','h',Q(2)),),(('a',Q(1)),))

    def test_static_bad_source_law_rejected(self):
        with self.assertRaises(BoundarySourceError):
            reconstruct_y_triangle(mat(((2,-1,-1),(-2,3,-1),(-1,-1,2))))
        with self.assertRaises(BoundarySourceError):
            reconstruct_y_triangle(mat(((1,1,-2),(1,1,-2),(-2,-2,4))))

    def test_dynamic_star_differs_from_triangle(self):
        self.assertNotEqual(star().response(1),triangle().response(1))
        self.assertEqual(triangle().response(0),triangle().response(100))

    def test_dynamic_twin_hubs_equal_for_all_test_rates(self):
        w=star((2,3,5),Q(2))
        twin=twin_hubs((2,3,5),Q(2))
        self.assertEqual(len(w.interior),1)
        self.assertEqual(len(twin.interior),2)
        for s in (0,1,2,3,4,11,99,Q(1,10),Q(1001,11)):
            self.assertEqual(w.response(s),twin.response(s))

    def test_twin_hubs_hidden_mode_redundant(self):
        self.assertEqual(spectral_mode_lower_bound(twin_hubs(),2)['rank'],1)
        self.assertEqual(spectral_mode_lower_bound(star(),2)['rank'],1)

    def test_one_pole_Hankel_determinant_zero(self):
        for cap in (1,2,3,Q(7,13)):
            w=star(cap=cap)
            m=w.moments(3)
            self.assertEqual(scalar_moment_witness(m,(2,3,5))['hankel_determinant'],0)

    def test_two_pole_hankel_witness_exact(self):
        w=serial_pendant()
        m=w.moments(3)
        self.assertEqual(scalar_moment_witness(m,(2,3,5)),dict(
            m0=Q(1,2),m1=Q(7,2),m2=Q(155,6),hankel_determinant=Q(2,3)))
        self.assertEqual(rank(block_hankel(m,2)),2)

    def test_two_mode_independent_hankel_rank_lowerbound(self):
        w=serial_pendant()
        self.assertEqual(spectral_mode_lower_bound(w,1)['rank'],1)
        self.assertEqual(spectral_mode_lower_bound(w,2)['rank'],2)
        self.assertEqual(spectral_mode_lower_bound(w,3)['rank'],2)

    def test_triangle_no_dynamic_Markov_coefficient(self):
        self.assertEqual(triangle().moments(4),tuple(zeros(3,3) for _ in range(4)))

    def test_all_moments_rational_symmetric(self):
        for w in (star(),twin_hubs(),serial_pendant()):
            for a in w.moments(5):
                self.assertEqual(a,tuple(zip(*a)))
                self.assertTrue(all(x.denominator>=1 for row in a for x in row))

    def test_one_mode_invisible_to_static_cannot_be_forged_by_dynamic(self):
        dc=serial_pendant().response(0)
        report=observe(serial_pendant(),1)
        m=filter_candidates((triangle(),star(),serial_pendant()),(observe(serial_pendant(),0),report))
        self.assertEqual(m['survivors'],('serial',))
        self.assertIn('triangle',m['rejected'])

    def test_wrong_star_matching_static_and_first_dynamic(self):
        source=serial_pendant()
        fake=star(cap=Q(26,7),name='imposter')
        self.assertEqual(source.response(0),fake.response(0))
        self.assertEqual(source.response(1),fake.response(1))
        self.assertNotEqual(source.response(2),fake.response(2))

    def test_inverse_transfer_finite_difference(self):
        r=reciprocal_three_frequency_defect(serial_pendant(),(2,3,5))
        self.assertEqual(r['h'],(Q(1,10),Q(7,96),Q(5,82)))
        self.assertEqual(r['q'],(Q(10),Q(96,7),Q(82,5)))
        self.assertEqual(r['second_difference'],Q(-36,35))

    def test_one_mode_reciprocal_exact_linear(self):
        for cap in (1,2,5,Q(2,3)):
            r=reciprocal_three_frequency_defect(star(cap=cap),(2,3,5))
            self.assertEqual(r['second_difference'],0)
            self.assertEqual(r['q'],(Q(10),Q(10)+cap,Q(10)+2*cap))

    def test_rebuild_params_from_observed_highfreq_moments(self):
        source=serial_pendant()
        out=reconstruct_serial_from_moments(source.response(0),source.moments(3))
        self.assertEqual(tuple(out[k] for k in ('c0','link','c1')),(Q(2),Q(4),Q(3)))
        for s in (0,1,2,3,11,Q(4,3)):
            self.assertEqual(out['replay_graph'].response(s),source.response(s))

    def test_bad_moments_rejected_as_unrealizable(self):
        src=serial_pendant()
        M=[list(map(list,m)) for m in src.moments(3)]
        for a in range(3):
            for b in range(3):
                M[2][a][b]=Q(0)
        with self.assertRaises(BoundarySourceError):
            reconstruct_serial_from_moments(src.response(0),tuple(mat(m) for m in M))

    def test_bad_source_epochs_not_glued(self):
        src=serial_pendant()
        with self.assertRaises(BoundarySourceError):
            filter_candidates((src,),(observe(src,0,epoch=0),observe(src,1,epoch=1)))
        with self.assertRaises(BoundarySourceError):
            filter_candidates((src,),(observe(src,0,basis='A'),observe(src,1,basis='B')))

    def test_distinct_observers_same_source_legal(self):
        src=serial_pendant()
        result=filter_candidates((src,),(observe(src,0,observer='A'),observe(src,1,observer='B')))
        self.assertEqual(result['survivors'],('serial',))
        self.assertFalse(result['source_attested'])

    def test_forged_frequency_matrix_is_falsification(self):
        src=serial_pendant()
        false=BoundaryReceipt('shared-RC-carrier',0,'three-terminal-current-v1','fake',Q(1),triangle().response(0))
        self.assertFalse(filter_candidates((src,),(observe(src,0),false))['survivors'])

    def test_underdetermination_stays_after_multiple_frequencies(self):
        w=star()
        twin=twin_hubs()
        receipts=tuple(observe(w,s) for s in (0,1,2,5,10))
        self.assertEqual(filter_candidates((w,twin),receipts)['survivors'],('star','twin'))

    def test_one_pole_2pole_absolutely_different_frequency_response(self):
        serial=serial_pendant()
        starcap=star(cap=Q(26,7))
        self.assertNotEqual(serial.response(2),starcap.response(2))
        self.assertEqual(scalar_h_from_response(serial,(2,3,5),0,2),Q(5,82))
        self.assertEqual(scalar_h_from_response(starcap,(2,3,5),0,2),Q(7,122))

    def test_source_change_static_facts_transport_but_dynamic_do_not(self):
        before=serial_pendant()
        after=change_interior_capacitance(before,{'h1':Q(4)})
        self.assertEqual(before.response(0),after.response(0))
        self.assertNotEqual(before.response(1),after.response(1))
        self.assertNotEqual(before.moments(3),after.moments(3))
        self.assertFalse(filter_candidates((before,),(observe(after,1,epoch=1),))['survivors'])

    def test_illegal_source_capacity_change_rejected(self):
        with self.assertRaises(BoundarySourceError):
            change_interior_capacitance(serial_pendant(),{'fake':2})
        with self.assertRaises(BoundarySourceError):
            change_interior_capacitance(serial_pendant(),{'h1':-2})

    def test_interval_observation_certifies_strict_negative_curvature(self):
        w=serial_pendant()
        q=reciprocal_three_frequency_defect(w,(2,3,5))['q']
        eps=Q(1,10)
        result=certified_reciprocal_defect(tuple((v-eps,v+eps) for v in q))
        self.assertEqual(result['defect_interval'],(Q(-36,35)-4*eps,Q(-36,35)+4*eps))
        self.assertTrue(result['strictly_negative'])
        self.assertFalse(result['inconclusive'])

    def test_inadequate_measurement_precision_is_not_a_proof(self):
        q=reciprocal_three_frequency_defect(serial_pendant(),(2,3,5))['q']
        eps=Q(1,3)
        result=certified_reciprocal_defect(tuple((v-eps,v+eps) for v in q))
        self.assertTrue(result['inconclusive'])
        self.assertFalse(result['strictly_negative'])

    def test_bad_interval_not_authenticated(self):
        for x in (((Q(0),Q(1)),(Q(1),Q(2)),(Q(2),Q(3))),
                  ((Q(2),Q(1)),(Q(1),Q(2)),(Q(2),Q(3)))):
            with self.assertRaises(BoundarySourceError):
                certified_reciprocal_defect(x)

    def test_kron_elimination_and_storage_change_do_not_commute(self):
        receipt=noncommuting_kron_storage_witness(star(),1)
        self.assertTrue(receipt['no_terminal_local_capacitance_repair_at_this_rate'])
        self.assertEqual(receipt['obstruction'],(0,1,Q(1,10)))

    def test_static_triangle_no_hidden_storage_obstruction(self):
        receipt=noncommuting_kron_storage_witness(triangle(),1)
        self.assertFalse(receipt['no_terminal_local_capacitance_repair_at_this_rate'])
        self.assertIsNone(receipt['obstruction'])

    def test_memory_kernel_reproduces_complete_laplace_transfer(self):
        m=exact_star_boundary_memory((2,3,5),Q(2))
        self.assertEqual(m['decay_rate'],Q(5))
        self.assertEqual(m['amplitude_matrix'][0][1],Q(3))
        self.assertFalse(m['boundary_ontology_selected'])

    def test_wrong_memory_kernel_source_rejected(self):
        with self.assertRaises(BoundarySourceError):
            exact_star_boundary_memory((2,3,5),0)

    def test_exact_symbolic_memory_not_instantaneous_fake(self):
        m=exact_star_boundary_memory()
        self.assertIn('exp(',m['memory_kernel_exact_symbolic'])
        self.assertNotEqual(star().response(1)[0][1],star().response(0)[0][1])

    def test_full_research_receipt_exact(self):
        x=demonstration()
        self.assertEqual(x['initial_candidates'],('static-triangle','fitted-one-mode'))
        self.assertEqual(x['after_s1'],('fitted-one-mode',))
        self.assertEqual(x['after_s2'],())
        self.assertTrue(x['new_repair_predicts_unseen_s_4_11_17'])
        self.assertEqual(x['two_mode_minimal_dimension'],2)
        self.assertEqual(x['twin_observable_mode_lower_bound'],1)
        self.assertFalse(x['physical_source_authenticated'])

    def test_source_repair_from_four_finite_responses(self):
        w=serial_pendant()
        data=[w.response(s) for s in range(4)]
        r=reconstruct_serial_from_finite_responses(*data)
        self.assertEqual(tuple(r[x] for x in ('arms','c0','link','c1')),
                         ((Q(2),Q(3),Q(5)),Q(2),Q(4),Q(3)))
        self.assertEqual(r['observed_cross_ratio'],Q(13,7))
        self.assertEqual(r['repaired_graph'].response(17),w.response(17))
        self.assertFalse(r['physical_topology_proved'])

    def test_finite_probe_repair_rejects_one_mode(self):
        w=star()
        with self.assertRaises(BoundarySourceError):
            reconstruct_serial_from_finite_responses(*(w.response(s) for s in range(4)))

    def test_finite_probe_repair_rejects_mutated_source_table(self):
        w=serial_pendant()
        rows=[w.response(s) for s in range(4)]
        m=[list(row) for row in rows[-1]]
        m[0][0]+=Q(1,13)
        rows[-1]=tuple(tuple(row) for row in m)
        with self.assertRaises(BoundarySourceError):
            reconstruct_serial_from_finite_responses(*rows)

    def test_finite_E_tower_receipts_source_correct(self):
        w=serial_pendant()
        r=tuple(observe(w,s,observer='A' if s%2 else 'B') for s in range(4))
        p=reconstruct_serial_from_receipts(r)
        self.assertEqual((p['c0'],p['link'],p['c1']),(Q(2),Q(4),Q(3)))

    def test_finite_E_receipts_reject_epoch_and_basis_mixing(self):
        w=serial_pendant()
        r=tuple(observe(w,s,epoch=int(s==3)) for s in range(4))
        with self.assertRaises(BoundarySourceError):reconstruct_serial_from_receipts(r)
        r=tuple(observe(w,s,basis='different' if s==3 else 'normal') for s in range(4))
        with self.assertRaises(BoundarySourceError):reconstruct_serial_from_receipts(r)

    def test_finite_E_receipts_reject_unsourced_frequency_alias(self):
        w=serial_pendant()
        r=tuple(observe(w,s) for s in (0,1,2,2))
        with self.assertRaises(BoundarySourceError):reconstruct_serial_from_receipts(r)

    def test_finite_probe_repair_random_160(self):
        rng=random.Random(160331)
        for _ in range(160):
            arms=tuple(Q(rng.randint(1,18),rng.randint(1,9)) for j in range(3))
            c0=Q(rng.randint(1,8),rng.randint(1,7))
            link=Q(rng.randint(1,13),rng.randint(1,8))
            c1=Q(rng.randint(1,12),rng.randint(1,6))
            world=serial_pendant(arms,c0,link,c1)
            r=reconstruct_serial_from_finite_responses(*(world.response(s) for s in range(4)))
            self.assertEqual((r['arms'],r['c0'],r['link'],r['c1']),
                             (arms,c0,link,c1))
            self.assertEqual(r['repaired_graph'].response(Q(19,5)),world.response(Q(19,5)))

    def test_random_static_Y_delta_oracle_240(self):
        rng=random.Random(471329)
        for _ in range(240):
            arms=tuple(Q(rng.randint(1,40),rng.randint(1,9)) for i in range(3))
            s=star(arms,cap=Q(rng.randint(1,15),rng.randint(1,7)))
            t=triangle(arms)
            self.assertEqual(s.response(0),t.response(0))
            self.assertEqual(reconstruct_y_triangle(s.response(0))['arms'],arms)
            self.assertNotEqual(s.response(1),t.response(1))

    def test_random_serial_moment_parameter_recovery_140(self):
        rng=random.Random(434221)
        for _ in range(140):
            arms=tuple(Q(rng.randint(1,13),rng.randint(1,5)) for _ in range(3))
            c0=Q(rng.randint(1,7),rng.randint(1,5)); h=Q(rng.randint(1,11),rng.randint(1,7))
            c1=Q(rng.randint(1,10),rng.randint(1,4))
            g=serial_pendant(arms,c0,h,c1)
            m=g.moments(3)
            reconstruction=reconstruct_serial_from_moments(g.response(0),m)
            self.assertEqual(tuple(reconstruction[k] for k in ('arms','c0','link','c1')),(arms,c0,h,c1))
            self.assertEqual(reconstruction['hankel_determinant'],h*h/(c0**3*c1))
            self.assertEqual(reconstruction['replay_graph'].response(Q(3,4)),g.response(Q(3,4)))

    def test_random_dynamical_twin_equivalence_100(self):
        rng=random.Random(837317)
        for _ in range(100):
            arms=tuple(Q(rng.randint(1,20),rng.randint(1,8)) for _ in range(3))
            c=Q(rng.randint(1,11),rng.randint(1,6))
            w=star(arms,c)
            d=twin_hubs(arms,c)
            for s in (0,Q(1,3),Q(7,2)):
                self.assertEqual(w.response(s),d.response(s))
            self.assertEqual(spectral_mode_lower_bound(d,2)['rank'],1)

    def test_random_Loewner_first_and_second_difference_100(self):
        rng=random.Random(319833)
        for _ in range(100):
            arms=tuple(Q(rng.randint(1,17),rng.randint(1,7)) for _ in range(3))
            w=serial_pendant(arms,Q(rng.randint(1,5)),Q(rng.randint(1,7)),Q(rng.randint(1,6)))
            L0,L1,L2=(w.response(i) for i in (0,1,2))
            D1=madd(L1,L0,sign=-1)
            D2=madd(madd(L2,L1,sign=-2),L0)
            for v in ((1,0,0),(1,1,0),(1,-2,3),(4,-1,7)):
                self.assertGreaterEqual(quad(D1,v),0)
                self.assertLessEqual(quad(D2,v),0)

    def test_low_precision_claim_not_promoted(self):
        # Exact rational equalities are source-law conditional, not physical claims.
        x=demonstration()
        self.assertFalse(x['canonical_geometry_unique_outside_source_class'])
        self.assertFalse(x['RH_or_Weil_positivity_proved'])


if __name__=='__main__':
    unittest.main()
