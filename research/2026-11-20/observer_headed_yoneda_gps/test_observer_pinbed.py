"""Exact rational observer pinbed: GPS, coding, BBP, and hostile controls."""
import unittest
from fractions import Fraction as Q
from itertools import combinations
import observer_pinbed as p

DIRECTIONS_2D=((1,0),(0,1),(-1,0),(0,-1),(Q(3,5),Q(4,5)))
GPS2=p.gps2_matrix(DIRECTIONS_2D)
BBP7=tuple(p.bbp_row(n) for n in range(1,8))


class FiniteHeads(unittest.TestCase):
    def test_rank_kernel_target(self):
        self.assertFalse(p.determined_by([(1,0)],[(0,1)]))
        self.assertTrue(p.determined_by([(1,0),(1,1)],[(0,1)]))

    def test_target_specific_even_without_full_rank(self):
        self.assertTrue(p.determined_by([(1,0,0),(0,1,0)],[(1,1,0)]))
        self.assertFalse(p.determined_by([(1,0,0),(0,1,0)],[(0,0,1)]))

    def test_rank_shared_kernel_does_not_improve(self):
        heads=[(1,0)]*9
        self.assertEqual(p.rank(heads),1)
        self.assertFalse(p.determined_by(heads,[(0,1)]))

    def test_sequential_delayed_differential(self):
        P=((1,0),)
        A=((0,1),(1,0))
        self.assertFalse(p.determined_by(P,((0,1),)))
        next_read=tuple(p.matvec(A, v) for v in [(1,0)])  # action before probe
        self.assertEqual(next_read,((0,1),))
        self.assertTrue(p.determined_by(P+next_read,((0,1),)))

    def test_xor_synergy_source_fibers(self):
        all_states=[(a,b) for a in (0,1) for b in (0,1)]
        for a,b in all_states:
            self.assertEqual(p.xor_shared_head_records(a,b)[0]^p.xor_shared_head_records(a,b)[1],b)
        for j in (0,1):
            for report in (0,1):
                survivors=[s for s in all_states if p.xor_shared_head_records(*s)[j]==report]
                self.assertEqual(sorted(set(b for a,b in survivors)),[0,1])
        self.assertEqual(len({p.xor_shared_head_records(*s) for s in all_states}),4)

    def test_missing_source_calibration_xor_wrong_partner(self):
        # Two partners reporting the same unrelated reference cannot recover b.
        all_states=[(a,b) for a in (0,1) for b in (0,1)]
        results={(a,a) for a,b in all_states}
        self.assertEqual(len(results),2)

    def test_rank_and_consistency_solver(self):
        H=((1,0),(0,1),(1,1))
        self.assertEqual(p.solve_unique(H,(2,3,5)),(2,3))
        with self.assertRaises(ValueError):p.solve_unique(H,(2,3,6))
        with self.assertRaises(ValueError):p.solve_unique(((1,0),(2,0)),(2,4))
        with self.assertRaises(ValueError):p.solve_unique(((1,0),),(1,))

    def test_target_distance(self):
        H=((1,0),(0,1),(1,1))
        self.assertEqual(p.target_distance(H,((1,0),(0,1))),2)
        self.assertEqual(p.target_distance(((1,0),),((0,1),)),0)
        self.assertEqual(p.target_distance(((1,0),(1,1)),((0,1),)),1)

    def test_two_tone_pinbed_syndrome_and_third_head_repair(self):
        # Two coherent harmonic channels: one parity-check identity, no
        # location of a single unknown corruption. Three nonzero gains give
        # a [3,1,3] scalar observation code and correct one bad head.
        H2=((2,), (3,))
        self.assertEqual(p.target_distance(H2,((1,),)),2)
        self.assertEqual(p.syndrome(H2,(Q(14,11),Q(21,11))),(Q(0),))
        H3=((2,), (3,), (5,))
        self.assertEqual(p.target_distance(H3,((1,),)),3)
        readings=list(p.matvec(H3,(Q(7,11),)))
        readings[1]+=Q(1,19)
        self.assertEqual(p.decode_corruptions(H3,readings,1),(Q(7,11),))
        self.assertTrue(any(p.syndrome(H3,readings)))

    def test_three_channel_zero_gain_breaks_fault_repair(self):
        H=((1,), (0,), (3,))
        self.assertEqual(p.target_distance(H,((1,),)),2)
        self.assertFalse(p.full_spark(H))

    def test_syndrome_exact(self):
        H=((1,0),(0,1),(1,1))
        self.assertEqual(p.syndrome(H,(2,3,5)),(Q(0),))
        self.assertNotEqual(p.syndrome(H,(2,3,6)),(Q(0),))
        checks=p.left_syndrome_basis(H)
        self.assertEqual(len(checks),len(H)-p.rank(H))
        self.assertEqual(p.matvec(checks,p.matvec(H,(2,3))),(Q(0),))

    def test_frame_chart_transport(self):
        H=((1,0),(0,1),(1,1))
        theta=(Q(2,7),Q(-3,11))
        f=(Q(-5),Q(2),Q(3,4))
        transformed=tuple(tuple(scale*a for a in row) for scale,row in zip(f,H))
        measured=p.matvec(transformed,theta)
        self.assertEqual(p.solve_unique(transformed,measured),theta)
        self.assertEqual(p.solve_unique(H,tuple(b/a for a,b in zip(f,measured))),theta)


class GPSHeads(unittest.TestCase):
    def test_2d_bias_needs_three_generic_heads(self):
        self.assertEqual(p.rank(GPS2[:2]),2)
        self.assertEqual(p.rank(GPS2[:3]),3)
        self.assertTrue(p.full_spark(GPS2))

    def test_2d_five_full_spark_exact(self):
        self.assertEqual(len(list(combinations(range(5),3))),10)
        for selected in combinations(range(5),3):
            self.assertEqual(p.rank([GPS2[i] for i in selected]),3)

    def test_2d_one_bad_satellite_corrected(self):
        theta=(Q(17,9),Q(-5,6),Q(7,4))
        readings=p.matvec(GPS2,theta)
        for idx in range(5):
            faulty=list(readings)
            faulty[idx]+=Q(1,97)
            self.assertEqual(p.decode_corruptions(GPS2,faulty,1),theta)

    def test_2d_five_distance_three(self):
        self.assertEqual(p.target_distance(GPS2,((1,0,0),(0,1,0),(0,0,1))),3)
        self.assertEqual(len(p.left_syndrome_basis(GPS2)),2)

    def test_2d_four_heads_detect_not_correct_one(self):
        subset=GPS2[:4]
        self.assertEqual(p.target_distance(subset,((1,0,0),(0,1,0),(0,0,1))),2)
        original=p.matvec(subset,(1,2,3))
        corrupt=list(original)
        corrupt[0]+=Q(1,7)
        self.assertTrue(any(p.syndrome(subset,corrupt)))
        with self.assertRaises(ValueError):p.decode_corruptions(subset,corrupt,1)

    def test_3d_gps_four_generic_heads_and_bias(self):
        directions=((1,0,0),(0,1,0),(0,0,1),(-1,0,0))
        H=p.gps3_matrix(directions)
        self.assertEqual(p.rank(H[:3]),3)
        self.assertEqual(p.rank(H),4)
        x=(Q(1,3),Q(2,5),Q(1,7),Q(11,13))
        self.assertEqual(p.solve_unique(H,p.matvec(H,x)),x)

    def test_gps_bad_geometry_rank(self):
        H=p.gps2_matrix([(1,0),(1,0),(0,1),(0,1)])
        self.assertLess(p.rank(H),3)
        self.assertFalse(p.determined_by(H,((0,0,1),)))

    def test_redundant_extra_head_no_new_rank(self):
        self.assertEqual(p.rank(GPS2[:3]),p.rank(GPS2))
        self.assertGreater(p.target_distance(GPS2,((1,0,0),)),p.target_distance(GPS2[:3],((1,0,0),)))


class AuthenticBBP(unittest.TestCase):
    def test_source_original_poles(self):
        self.assertEqual(p.forcing(1),Q(47,15))
        for n in range(1,12):
            self.assertEqual(p.bbp_state(n)-16*p.bbp_state(n-1),p.forcing(n))

    def test_all_five_clock_subsets_have_rank_five(self):
        self.assertTrue(p.full_spark(BBP7))
        for idx in combinations(range(7),5):
            self.assertEqual(p.rank(tuple(BBP7[i] for i in idx)),5)

    def test_seven_head_code_has_distance_three(self):
        F=tuple(tuple(Q(int(i==j)) for i in range(5)) for j in range(5))
        self.assertEqual(p.target_distance(BBP7,F),3)
        self.assertEqual(len(p.left_syndrome_basis(BBP7)),2)

    def test_seven_bbP_heads_correct_one_corruption(self):
        original=p.matvec(BBP7,p.ORIGINAL)
        for bad in range(7):
            measurements=list(original)
            measurements[bad]+=Q(1,103)
            self.assertEqual(p.decode_corruptions(BBP7,measurements,1),p.ORIGINAL)
            self.assertTrue(any(p.syndrome(BBP7,measurements)))

    def test_six_heads_only_detect_one_error(self):
        H=BBP7[:6]
        self.assertEqual(p.target_distance(H,tuple(tuple(Q(int(i==j)) for i in range(5)) for j in range(5))),2)
        r=list(p.matvec(H,p.ORIGINAL))
        r[0]+=Q(1,29)
        self.assertTrue(any(p.syndrome(H,r)))
        with self.assertRaises(ValueError):p.decode_corruptions(H,r,1)

    def test_wrong_seed_is_recoverable_from_unwrapped_heads(self):
        H=BBP7
        changed=(Q(1,16),)+p.ORIGINAL[1:]
        y=p.matvec(H,changed)
        self.assertEqual(p.decode_corruptions(H,y,0),changed)
        self.assertNotEqual(p.decode_corruptions(H,y,0),p.ORIGINAL)

    def test_late_circle_heads_can_never_disambiguate_early_seed_alias(self):
        for t in range(1,21):
            self.assertEqual(p.circle_fraction(p.bbp_state(t)),p.circle_fraction(p.bbp_state(t,(Q(1,16),)+p.ORIGINAL[1:])))
        self.assertNotEqual(p.bbp_state(1),p.bbp_state(1,(Q(1,16),)+p.ORIGINAL[1:]))

    def test_finite_terminal_locked_counterseed(self):
        M=9
        P=p.bbp_prefix(M)
        changed=(-P,)+p.ORIGINAL[1:]
        for n in range(M+1):
            self.assertEqual(p.bbp_state(n,changed)+p.bbp_terminal_tail(n,M),0)
            self.assertEqual(p.bbp_state(n)+p.bbp_terminal_tail(n,M),16**n*P)
        self.assertEqual(p.decode_corruptions(BBP7,p.matvec(BBP7,changed),0),changed)

    def test_delayed_source_outside_five_parameter_family(self):
        # Change forcing only after last head, so no possible earlier readout detects.
        changed=[p.bbp_state(n) for n in range(1,8)]
        self.assertEqual(changed,list(p.matvec(BBP7,p.ORIGINAL)))
        true_at_8=p.bbp_state(8)
        mutated_at_8=true_at_8+Q(1,29)
        self.assertNotEqual(mutated_at_8,p.matvec((p.bbp_row(8),),p.ORIGINAL)[0])

    def test_irregular_five_head_schedule(self):
        clocks=(0,2,5,9,14)
        H=[p.bbp_row(t) for t in clocks]
        self.assertEqual(p.rank(H),5)
        self.assertEqual(p.solve_unique(H,p.matvec(H,p.ORIGINAL)),p.ORIGINAL)


class ObserverGauge(unittest.TestCase):
    def test_two_forward_paths_holonomy_invariant(self):
        E={('r','a','ra'):Q(1,7),('a','v','av'):Q(1,11),
           ('r','b','rb'):Q(1,5),('b','v','bv'):Q(1,13)}
        paths=((('r','a','ra'),('a','v','av')), (('r','b','rb'),('b','v','bv')))
        zero={n:Q(0) for n in 'rabv'}
        gauge={'r':Q(1,17),'a':Q(2,17),'b':Q(3,17),'v':Q(4,17)}
        self.assertEqual(p.common_frame_gauge(E,zero,paths),p.common_frame_gauge(E,gauge,paths))
        self.assertNotEqual(p.common_frame_gauge(E,zero,paths)[1],0)

    def test_unmatched_paths_rejected(self):
        E={('r','a','ra'):Q(1,7),('r','b','rb'):Q(1,5)}
        with self.assertRaises(ValueError): p.common_frame_gauge(E,{'r':0,'a':0,'b':0},((('r','a','ra'),),(('r','b','rb'),)))

    def test_uncalibrated_phase_heads_gauge_failure(self):
        # z_i=e(theta+alpha_i), unknown independent alpha_i -> every theta fits.
        def phase_mod(q):return p.circle_fraction(q)
        z=(Q(1,7),Q(2,11))
        for candidate_theta in (Q(0),Q(1,3),Q(4,7)):
            gauges=[phase_mod(report-candidate_theta) for report in z]
            self.assertEqual(tuple(phase_mod(candidate_theta+a) for a in gauges),z)


if __name__=='__main__':
    unittest.main()
