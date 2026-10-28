"""Exact tests for pointed-circle / solenoid cut source mathematical dossier.

Local isolated tests use an inspected faithful source shim; the committed
module imports the full repository source interface in native CI.
"""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from itertools import product
from math import gcd
from observational_succ import solenoid_cut_source as s
from observational_succ.succ_internal_matrix_walk import authentic_r

class PointedCircleTests(unittest.TestCase):
    def test_countability_and_metric_seam(self):
        for k in (2,3,5,13,40):
            w=s.cut_seam_receipt(k)
            self.assertEqual(w['circle_distance'],Q(2,2**k))
            self.assertEqual(w['flat_distance'],1-Q(2,2**k))
            self.assertLessEqual(w['circle_distance'],w['flat_distance'])
        self.assertEqual(s.dyadic_root(7,3),Q(7,8))
        self.assertEqual(s.dyadic_root(9,3),Q(1,8))

    def test_reference_cut_chart(self):
        for a in (0,Q(1,3),Q(1,2),Q(15,16)):
            self.assertEqual(s.cut_coordinate(a,a),0)
            self.assertEqual(s.cut_coordinate(a+Q(1,8),a),Q(1,8))
            self.assertEqual(s.cut_coordinate(a- Q(1,8),a),Q(7,8))
        with self.assertRaises(ValueError):s.cut_coordinate(1.25)

    def test_cofinal_exact_restoration(self):
        for root in (Q(1,3),Q(2,7),Q(1,17),Q(5,31)):
            hexhistory=s.odd_solenoid_levels(root,4)
            binhistory=s.cofinal_16_to_2(hexhistory)
            self.assertEqual(s.cofinal_2_to_16(binhistory),hexhistory)
            self.assertEqual(len(binhistory),17)
        for bad in ((Q(0),Q(1,7)),(Q(1,3),Q(2,3))):
            with self.assertRaises(ValueError):s.cofinal_16_to_2(bad)

    def test_seam_odometer_positive_increment(self):
        for k in (1,2,4):
            m=16**k
            for z in (0,1,m-1,m+7):
                self.assertEqual(s.seam_memory_glue(z,k),(z+1)%m)
        with self.assertRaises(ValueError):s.seam_memory_glue(0,0)

class GenuineSourceCut(unittest.TestCase):
    def test_authentic_forcing_cancelled_polynomial(self):
        for n in (1,2,3,7,31,97,257,1009):
            self.assertEqual(s.source_forcing_polynomial(n),authentic_r(n))
            self.assertEqual(s.canonical_forcing_odd(n),authentic_r(n))
            self.assertEqual(authentic_r(n).denominator%2,1)

    def test_chart_carry_coboundary_source(self):
        for a in (0,Q(1,7),Q(1,2),Q(11,16),Q(15,16)):
            seq=s.authentic_cut_history(30,a,7)
            x=Q(0)
            for i,entry in enumerate(seq,1):
                self.assertEqual(entry.x,x)
                self.assertEqual(entry.phase_before,entry.phase_recovered)
                self.assertEqual(entry.forcing,authentic_r(i))
                self.assertEqual(entry.cut_carry-entry.original_carry,
                                 entry.seam_y-16*entry.seam_x)
                self.assertEqual(entry.y,(16*x+authentic_r(i))%1)
                x=entry.y
            self.assertEqual(s.seam_coboundary_telescope(seq)['weighted_carry_change'],
                             seq[-1].seam_y-16**len(seq)*seq[0].seam_x)

    def test_cut_phases_agree_under_all_prescribed_marks(self):
        steps0=s.authentic_cut_history(40,0,-13)
        for a in (Q(1,2),Q(1,19),Q(8,17)):
            altered=s.authentic_cut_history(40,a,-13)
            self.assertEqual([v.phase_recovered for v in altered],
                             [v.phase_recovered for v in steps0])
            self.assertNotEqual([v.cut_carry for v in altered],
                                [v.cut_carry for v in steps0])

    def test_signed_midpoint_transport_without_dropping_forcing(self):
        for anchor in (0,Q(1,3),Q(15,16)):
            for ss in s.authentic_cut_history(30,anchor):
                for h in (1,4,8,-13):
                    for M in (1,3,16,31):
                        u=s.cut_midpoint_character_certificate(ss,h,M)
                        self.assertLessEqual(u['phase_circle_distance'],
                                             Q(abs(h),32*M))
                        self.assertFalse(u['selected_signed_saving_proved'])

    def test_integer_lift_matches_original_states(self):
        states=s.source_unwrapped_states(25)
        for n,ss in enumerate(s.authentic_cut_history(25,0),1):
            v0,v1=states[n-1:n+1]
            self.assertEqual(ss.original_carry,
                             v1.numerator//v1.denominator-16*(v0.numerator//v0.denominator))

    def test_unique_odd_torsion_lifts_and_memory_gap(self):
        states=s.source_unwrapped_states(27)
        for u in states:
            code=s.torsion_memory_code(u%1,4)
            m=s.memory_gap_certificate(u,4)
            self.assertEqual(m['gap'],s.modadic(u,4))
            self.assertEqual(m['odd_torsion_memory'],code[-1])
        with self.assertRaises(ValueError):s.odd_solenoid_levels(Q(1,16))
        for k in (1,2,4):
            with self.assertRaises(ValueError):s.modadic(Q(1,2),k)

    def test_solenoid_memory_code_explicit(self):
        self.assertEqual(s.torsion_memory_code(Q(1,3),3)[0],5)
        self.assertEqual(s.memory_gap_certificate(Q(4,3),1)['gap'],s.modadic(Q(4,3),1))
        for x in (Q(1,3),Q(1,5),Q(2,7)):
            z=s.torsion_memory_code(x,3)
            self.assertEqual(z[-1],(-s.modadic(x,3))%16**3)

class TwoAdicUniformityTests(unittest.TestCase):
    def test_isometry_on_diverse_indices(self):
        for a,b in product(range(-14,20),repeat=2):
            self.assertTrue(s.two_adic_isometry_mod(a,b,3),(a,b))

    def test_early_authentic_state_time_clock(self):
        states=s.source_unwrapped_states(110)
        for k in (1,2):
            for n in range(k,100):
                self.assertEqual(s.modadic(states[n],k),s.time_clock_value(n,k))
                self.assertEqual(s.time_clock_value(n,k),
                                 s.time_clock_value(n+16**k,k))

    def test_all_residue_permutation_level_1_to_3(self):
        for k in (1,2,3):
            report=s.time_clock_certificate(k)
            self.assertEqual(report['distinct_count'],16**k)
            self.assertFalse(report['real_circle_normality_proved'])

    def test_every_residue_exactly_once_and_orthogonality(self):
        k=2; m=16**k
        v=[s.time_clock_value(k+n,k) for n in range(m)]
        self.assertEqual(sorted(v),list(range(m)))
        # Exact Z/2 and Z/4 nontrivial characters vanish in EVERY completed period.
        self.assertEqual(sum((-1)**x for x in v),0)
        self.assertEqual(sum(1 if x%4==0 else -1 if x%4==2 else 0 for x in v),0)

class SolenoidCountercontrols(unittest.TestCase):
    def test_uniform_circle_nonhaar_odd_solenoid(self):
        for m in (1,3,16,257):
            xs, inv=s.rational_odd_grid(m)
            self.assertEqual(len(xs),m)
            self.assertTrue(all(16*b%1==a for a,b in zip(xs,inv)))
            self.assertTrue(all(v < Q(1,16) for v in inv))
            receipt=s.nonhaar_grid_witness(m)
            self.assertGreater(receipt['fractional_character_real_lower'],Q(9,10))
            self.assertFalse(receipt['normality_of_pi_proved'])

    def test_root_and_odd_carriers_intersect_only_at_zero(self):
        for k in range(1,6):
            for a in range(1,2**k):
                self.assertNotEqual(s.dyadic_root(a,k).denominator%2,1)

    def test_bad_type_rejected(self):
        for invalid in (True,1.0,-1):
            with self.assertRaises(ValueError):s.authentic_cut_history(invalid)
        with self.assertRaises(ValueError):s.time_clock_value(1,2)
        with self.assertRaises(ValueError):s.dyadic_root(0,49)

    def test_counterfeit_zero_seed_positive_same_leading_and_non_normal(self):
        self.assertEqual(s.decoy_tail(0),1)
        self.assertEqual(s.decoy_forcing(1),Q(2158,135))
        self.assertNotEqual(s.decoy_forcing(1),authentic_r(1))
        for n in (1,2,3,9,77,819):
            self.assertGreater(s.decoy_tail(n-1),s.decoy_tail(n))
            self.assertGreater(s.decoy_forcing(n),0)
            self.assertEqual(s.decoy_forcing(n),16*s.decoy_tail(n-1)-s.decoy_tail(n))
            self.assertEqual((16**n-s.decoy_tail(n))%1,(-s.decoy_tail(n))%1)
        for depth in (1,2,3):
            result=s.decoy_source_control(depth)
            self.assertEqual(result['checked_permutation_size'],16**depth)
            self.assertEqual(result['real_fourier_average_limit'],1)
            self.assertFalse(result['pi_normality_from_isometry_proved'])

    def test_authentic_two_adic_signed_character_saving(self):
        for k in (1,2,3):
            m=16**k
            for N in (k,k+1,k+m,k+3*m+5):
                for h in (1,m-1):
                    u=s.two_adic_character_prefix_upper(N,k,h)
                    self.assertLessEqual(u,1)
                    self.assertGreaterEqual(u,0)
                self.assertLessEqual(s.two_adic_character_prefix_upper(k-1+10*m,k,1),
                                     Q(k-1, k-1+10*m))
        with self.assertRaises(ValueError):s.two_adic_character_prefix_upper(100,2,256)

    def test_status_is_not_normality(self):
        w=s.finite_status()
        self.assertTrue(w['source_two_adic_time_haar'])
        self.assertFalse(w['selected_real_circle_fourier_cancellation_proved'])
        self.assertFalse(w['pi_base16_normality_proved'])

if __name__=='__main__':unittest.main()
