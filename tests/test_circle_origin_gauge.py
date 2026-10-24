"""Source-typed exact reference-frame / cyclotomic counterexample tests."""
import unittest
from fractions import Fraction as Q
from math import gcd

from observational_succ.circle_origin_gauge import (
    mod1, covering,rotate,frame_covering,origin_defect,
    moving_frame_forcing,commuting_origins,commutes_with_fixed_covering,
    fixed_frame_character_average,projective_chord_sq,projective_rotate,
    cyclotomic_at_base,exact_periodic_points,periodic_orbit_count,
    frame_frequency_residues,frame_nonaliased,frame_origin_energy_at_zero,
    order_mod,order_suffices_for_frame,cyclotomic_source_orbit,
    cyclotomic_selected_linear_mean,periodic_origin_grid_w1,
    selected_orbit_w1_zero,selected_orbit_weyl_deviation_bound,
    certified_cyclotomic_pi_shadow,truncated_bbp_connection,
    exact_relative_rms_thirds
)

class OriginCategory(unittest.TestCase):
    def test_static_covariance_and_cyclotomic_cocycle(self):
        for b in (2,3,16):
            for a in (Q(1,7),Q(2,15),Q(13,24)):
                for x in (Q(0),Q(1,3),Q(11,13)):
                    for n in range(8):
                        lhs=mod1(covering(rotate(x,a),b,n)-a)
                        self.assertEqual(lhs,frame_covering(x,b,a,n))
                        self.assertEqual(origin_defect(b,n,a),
                                         mod1((b**n-1)*a))
                        for k in range(5):
                            self.assertEqual(origin_defect(b,n+k,a),
                                mod1(origin_defect(b,n,a)+b**n*origin_defect(b,k,a)))

    def test_commuting_rotations_are_only_fixed_point_torsion(self):
        for b in (3,16):
            a=commuting_origins(b)
            self.assertEqual(len(a),b-1)
            self.assertTrue(all(commutes_with_fixed_covering(b,v) for v in a))
            self.assertFalse(commutes_with_fixed_covering(b,Q(1,b)))
            for h in (1,b-1,2*(b-1)):
                expected=1 if h%(b-1)==0 else 0
                self.assertEqual(fixed_frame_character_average(b,h),expected)
        self.assertEqual(len(commuting_origins(2)),1)

    def test_stereographic_mobius_preserves_intrinsic_chord(self):
        for s,t in ((Q(1,2),Q(-1,3)),(Q(1,5),Q(3,4)),(Q(0),Q(2))):
            for tau in (Q(1,3),Q(-2,5)):
                if s*tau!=1 and t*tau!=1:
                    self.assertEqual(
                        projective_chord_sq(s,t),
                        projective_chord_sq(projective_rotate(s,tau),
                                            projective_rotate(t,tau)))
        self.assertEqual(projective_chord_sq(Q(0),Q(1)),2)
        with self.assertRaises(ValueError):
            projective_rotate(Q(2),Q(1,2))

    def test_expansion_not_uniformly_stable(self):
        for b in (2,16):
            for N in (1,2,3,8):
                difference=Q(1,2*b**N)
                self.assertEqual(covering(difference,b,N),Q(1,2))
                self.assertLessEqual(difference,Q(1,2*b))
        self.assertEqual(exact_relative_rms_thirds(12),Q(1,4))
        self.assertEqual(exact_relative_rms_thirds(100),Q(3,100))


class CyclotomicGroupoids(unittest.TestCase):
    def test_cyclotomic_and_primitive_period_counts_are_distinct(self):
        for b in (2,3,16):
            for d in range(1,9):
                prod=1
                for e in range(1,d+1):
                    if d%e==0:
                        prod*=cyclotomic_at_base(b,e)
                self.assertEqual(prod,b**d-1)
                count=exact_periodic_points(b,d)
                self.assertEqual(count% d,0)
                self.assertEqual(periodic_orbit_count(b,d)*d,count)
                if d>=2:
                    self.assertNotEqual(cyclotomic_at_base(b,d),count)
        self.assertEqual(
            [(exact_periodic_points(16,d),periodic_orbit_count(16,d))
             for d in range(1,5)],
            [(15,15),(240,120),(4080,1360),(65280,16320)])
        self.assertEqual(cyclotomic_at_base(16,2),17)

    def test_exact_cyclic_frame_sample_rms(self):
        self.assertEqual(order_mod(16,7),3)
        self.assertEqual(order_mod(16,15),1)
        self.assertTrue(order_suffices_for_frame(16,1,3,7))
        self.assertFalse(order_suffices_for_frame(16,1,3,15))
        self.assertEqual(frame_origin_energy_at_zero(16,1,3,7,holonomy=True),Q(1,3))
        self.assertEqual(frame_origin_energy_at_zero(16,1,3,15,holonomy=True),Q(1))
        self.assertEqual(frame_origin_energy_at_zero(16,1,3,17,holonomy=True),Q(5,9))
        self.assertEqual(frame_origin_energy_at_zero(16,1,3,4095,holonomy=True),Q(1,3))
        self.assertTrue(frame_nonaliased(16,1,3,7,holonomy=True))
        self.assertFalse(frame_nonaliased(16,1,3,15,holonomy=True))
        self.assertEqual(frame_frequency_residues(16,1,3,7,holonomy=True),(1,3,0))
        with self.assertRaises(ValueError):
            order_mod(16,8)

    def test_cyclotomic_selected_maximal_period_is_nonnormal(self):
        for b in (3,16):
            for d in range(2,8):
                seq=cyclotomic_source_orbit(b,d)
                self.assertEqual(len(set(seq)),d)
                self.assertEqual(seq[0],Q(1,b**d-1))
                self.assertEqual(covering(seq[0],b,d),seq[0])
                for j in range(1,d):
                    self.assertNotEqual(covering(seq[0],b,j),seq[0])
                mean=Q(1,d*(b-1))
                self.assertEqual(cyclotomic_selected_linear_mean(b,d),mean)
                self.assertEqual(selected_orbit_w1_zero(b,d),mean)
                self.assertEqual(periodic_origin_grid_w1(b,d),Q(1,4*(b**d-1)))
                self.assertEqual(selected_orbit_weyl_deviation_bound(b,d),mean)

    def test_finite_origin_tomography_exact_no_alias(self):
        for d in (2,3,4):
            m=16**d-1
            self.assertTrue(frame_nonaliased(16,1,d,m))
            self.assertTrue(frame_nonaliased(16,1,d,m,holonomy=True))
            self.assertEqual(frame_origin_energy_at_zero(16,1,d,m),Q(1,d))
            self.assertEqual(frame_origin_energy_at_zero(16,1,d,m,holonomy=True),Q(1,d))
            self.assertEqual(order_mod(16,m),d)
        self.assertEqual(frame_origin_energy_at_zero(16,1,4,4095,holonomy=True),Q(3,8))

    def test_true_periodic_origin_ensemble_has_exact_zero_fourier_mean(self):
        for d in (2,3,4,5):
            m=16**d-1
            for h in (1,2,7,13):
                self.assertGreater(m,abs(h))
                # (1/m)*sum_r e(h*(16^j)*r/m)=0 for every j,
                # by gcd(16,m)=1 and m>h, so ensemble Weyl mean=0.
                self.assertEqual(gcd(16,m),1)
                self.assertNotEqual(h%m,0)

    def test_hostile_refusal_of_misapplied_sample_frames(self):
        self.assertEqual(
            frame_origin_energy_at_zero(16,1,3,15,holonomy=True),Q(1))
        # Fifteen truly commuting origins kill complex averages for h=1
        # but do not reduce the magnitude of ANY individual selected orbit.
        self.assertEqual(fixed_frame_character_average(16,1),0)
        self.assertEqual(fixed_frame_character_average(16,15),1)
        with self.assertRaises(ValueError):
            frame_frequency_residues(16,0,3,7)
        with self.assertRaises(ValueError):
            cyclotomic_source_orbit(16,1)


class SelectedBBPAndPi(unittest.TestCase):
    def test_bbp_forcing_is_exact_moving_origin_connection(self):
        from observational_succ.bbp_source_memory import forcing
        for n in range(5):
            for depth in (1,3,8):
                residual=truncated_bbp_connection(n,depth)
                self.assertEqual(residual,-forcing(n+depth+1)/16**depth)
                self.assertLess(residual,0)
                self.assertLess(abs(residual),Q(1,16**depth)*forcing(n+1))

    def test_actual_pi_has_certified_periodic_cyclotomic_shadows(self):
        from observational_succ.circle_collision_rigidity import pi_interval
        lo,hi=pi_interval(16,80)
        for d in (2,3,4,5):
            k,m,err=certified_cyclotomic_pi_shadow(lo,hi,16,d)
            self.assertTrue(0<k<m and m==16**d-1)
            self.assertLess(err,Q(1,2*m)+(hi-lo))
            self.assertEqual(covering(Q(k,m),16,d),Q(k,m))
            for j in range(d//2):
                self.assertLess(16**j*err,Q(1,16**(d-j-1)))
        with self.assertRaises(ValueError):
            certified_cyclotomic_pi_shadow(Q(3),Q(4),16,4)

if __name__=="__main__":
    unittest.main()
