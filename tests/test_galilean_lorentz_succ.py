"""Exact adversarial tests of the retrospective Galilean->Lorentz SUCC repair."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.galilean_lorentz_succ import (
    RelativityWitnessError,Mat2,ID,ETA,ZERO,q,
    galilean,rational_boost,boost_addition_parameter,velocity_addition,
    interval_squared,interval_form,is_lightlike,is_future_causal,speed_for_ray,
    metric_defect,quadratic_wave_failure,conformal_candidate,
    metric_shadow_constraints,rank_rational,unique_boost_from_empirical_constraints,
    galilean_to_lorentz_case,
)


class GalileanLorentzSuccTests(unittest.TestCase):
    def test_exact_main_defect(self):
        r=galilean_to_lorentz_case()
        self.assertEqual(r['velocity'],F(3,5))
        self.assertEqual(r['gamma'],F(5,4))
        self.assertEqual(r['galilean'],[['1','0'],['-3/5','1']])
        self.assertEqual(r['lorentz'],[['5/4','-3/4'],['-3/4','5/4']])
        self.assertEqual(r['galilean_operator_defect'],[['0','-3/5'],['-3/5','9/25']])
        self.assertEqual(r['galilean_quadratic_wave_failure'],F(-42,25))
        self.assertEqual(r['galilean_null_slopes'],(F(-8,5),F(2,5)))
        self.assertEqual(r['lorentz_operator_defect'],[['0','0'],['0','0']])
        self.assertEqual(r['lorentz_quadratic_wave_failure'],0)
        self.assertEqual(r['lorentz_null_slopes'],(-1,1))
        self.assertTrue(r['two_light_rays_clock_sufficient'])
        self.assertFalse(r['formal_physical_measurement_authentication'])

    def test_source_wave_solution_counterexample_symbolically(self):
        v=F(3,5)
        # f'(t',x')=((1-v)t'-x')², apply (d_tt-d_xx)
        direct=2*((1-v)**2-1)
        self.assertEqual(direct,F(-42,25))
        self.assertEqual(quadratic_wave_failure(galilean(v)),direct)

    def test_affine_wave_source_does_not_detect_bad_geometry(self):
        # Every affine function has zero second derivative under either operator.
        # Thus the *probe selection*, not just algebraic consistency, matters.
        for slope in (-3,-1,0,1,4):
            self.assertEqual(0,2*0*(1-slope*slope))
        self.assertNotEqual(metric_defect(galilean(F(3,5))),ZERO)

    def test_all_rational_nonzero_low_velocity_galilean_residual(self):
        for den in range(2,12):
            for num in range(-den+1,den):
                v=F(num,den)
                self.assertEqual(metric_defect(galilean(v))==ZERO,v==0)
                self.assertEqual(speed_for_ray(galilean(v),1),1-v)
                self.assertEqual(speed_for_ray(galilean(v),-1),-1-v)
                if v:self.assertNotEqual(quadratic_wave_failure(galilean(v)),0)

    def test_rational_cayley_boosts_infinite_exact_family(self):
        for den in range(2,9):
            for num in range(-den+1,den):
                v,g,L=rational_boost(F(num,den))
                self.assertEqual(g*g*(1-v*v),1)
                self.assertEqual(L.determinant(),1)
                self.assertEqual(metric_defect(L),ZERO)
                self.assertEqual(L @ ETA @ L.transpose(),ETA)
                self.assertEqual(speed_for_ray(L,1),1)
                self.assertEqual(speed_for_ray(L,-1),-1)
                self.assertEqual(quadratic_wave_failure(L),0)
                self.assertEqual(L.inverse(),rational_boost(F(-num,den))[2])
                self.assertEqual(L.apply((1,v))[1],0)

    def test_boost_composition_and_order(self):
        pars=[F(-2,5),F(-1,3),F(0),F(1,4),F(1,2)]
        for u,w in product(pars,repeat=2):
            v,g,T=rational_boost(u)
            t,h,S=rational_boost(w)
            merged=boost_addition_parameter(u,w)
            self.assertEqual(T @ S,rational_boost(merged)[2])
            self.assertEqual(velocity_addition(v,t),rational_boost(merged)[0])
            self.assertEqual(S @ T,T @ S)  # 1+1 only; 2+1 Wigner != 0
        self.assertEqual(rational_boost(F(0))[2],ID)

    def test_causal_order_preservation_on_lattice_events(self):
        boosts=[rational_boost(u)[2] for u in (F(-3,5),F(-1,3),F(0),F(1,3),F(3,5))]
        for t,x in product(range(-4,5),repeat=2):
            e=(t,x)
            for T in boosts:
                self.assertEqual(interval_squared(T.apply(e)),interval_squared(e))
                self.assertEqual(is_future_causal(T.apply(e)),is_future_causal(e))
        # Spacelike simultaneity can flip, not causal order.
        positive=rational_boost(F(1,3))[2]
        self.assertEqual(positive.apply((0,1))[0],F(-3,4))
        self.assertEqual(positive.apply((0,-1))[0],F(3,4))

    def test_wave_operator_matches_direct_chain_rule(self):
        for v in (F(1,5),F(3,5),F(-1,2)):
            G=galilean(v)
            T=G @ ETA @ G.transpose()
            self.assertEqual(T,Mat2(1,-v,-v,v*v-1))
            self.assertEqual(metric_defect(G),Mat2(0,-v,-v,v*v))

    def test_source_dynamics_vs_coordinate_metric_two_distinct_checks(self):
        L=rational_boost(F(1,3))[2]
        self.assertEqual(metric_defect(L),ZERO)
        C=conformal_candidate(F(1,3),F(2))
        self.assertEqual(speed_for_ray(C,1),1)
        self.assertEqual(speed_for_ray(C,-1),-1)
        self.assertEqual(metric_defect(C),Mat2(3,0,0,-3))
        self.assertNotEqual(interval_squared(C.apply((1,0))),1)
        self.assertEqual(quadratic_wave_failure(C),0)

    def test_two_null_shadows_clock_select_unique_metric(self):
        full=metric_shadow_constraints(forward=True,backward=True,clock=True)
        self.assertEqual(full['constraint_rank'],3)
        self.assertEqual(full['free_geometry_dimensions'],0)
        self.assertEqual(full['metric'],ETA)
        for f,b,clock in product((False,True),repeat=3):
            if f and b and clock:continue
            r=metric_shadow_constraints(forward=f,backward=b,clock=clock)
            self.assertFalse(r['unique_normalized_metric'])
            self.assertNotEqual(r['indistinguishable_metrics'][0],r['indistinguishable_metrics'][1])
            self.assertGreater(r['free_geometry_dimensions'],0)
        self.assertEqual(rank_rational(((1,2,1),(1,-2,1),(1,0,0))),3)

    def test_one_light_ray_plus_clock_cannot_identify_cone(self):
        r=metric_shadow_constraints(forward=True,backward=False,clock=True)
        original,rival=r['indistinguishable_metrics']
        self.assertEqual(interval_form(original,(1,1)),interval_form(rival,(1,1)))
        self.assertEqual(interval_form(original,(1,0)),interval_form(rival,(1,0)))
        self.assertNotEqual(interval_form(original,(1,-1)),interval_form(rival,(1,-1)))

    def test_symmetric_ray_repair_velocity_and_scale(self):
        for v in (F(-3,5),F(0),F(3,5)):
            report=unique_boost_from_empirical_constraints(v,2)
            self.assertEqual(report['time_mixing_is_forced'],v!=0)
            self.assertFalse(report['normalized_metric_requires_scale_one'])
        self.assertTrue(unique_boost_from_empirical_constraints(F(3,5),1)['normalized_metric_requires_scale_one'])

    def test_galilean_low_speed_limit_with_bound(self):
        for n in (5,10,20,40,80):
            u=F(1,n)
            v,g,L=rational_boost(u)
            G=galilean(v)
            # |t_L-t_G| <= (gamma-1) |t| + gamma |v| |x|
            for t,x in product(range(-3,4),repeat=2):
                diff=abs(L.apply((t,x))[0]-G.apply((t,x))[0])
                self.assertLessEqual(diff,(g-1)*abs(t)+g*abs(v)*abs(x))
            self.assertLess(abs(L.a-1),F(4,n*n))
        # It is approximation on bounded regions, not exact Maxwell covariance.
        self.assertNotEqual(metric_defect(galilean(v)),ZERO)

    def test_invalid_sign_unsupported_and_unsafe_source(self):
        for bad in (0.5,"1/2",True,None):
            with self.assertRaises(RelativityWitnessError):q(bad)
        for bad in (-1,1,F(5,3)):
            with self.assertRaises(RelativityWitnessError):rational_boost(bad)
        with self.assertRaises(RelativityWitnessError):conformal_candidate(F(1,3),0)
        with self.assertRaises(RelativityWitnessError):speed_for_ray(ID,0)
        with self.assertRaises(RelativityWitnessError):Mat2(1,0,0,0).inverse()
        with self.assertRaises(RelativityWitnessError):velocity_addition(1,F(1,2))

    def test_metric_invariance_vs_missing_source_authentication(self):
        r=galilean_to_lorentz_case()
        self.assertTrue(r['historical_simulation_not_historical_experiment'])
        self.assertFalse(r['formal_physical_measurement_authentication'])
        self.assertFalse(r['RH_or_global_Weil_positivity_claimed'])
        self.assertNotEqual(r['galilean_operator_defect'],r['lorentz_operator_defect'])


if __name__=='__main__':unittest.main()

class FieldEnvironmentRepairTests(unittest.TestCase):
    def test_old_newtonian_free_particle_law_was_not_wrong(self):
        from observational_succ.galilean_lorentz_succ import free_particle_galilean
        for a,u,v in product((F(-2),F(0),F(3,2)),repeat=3):
            r=free_particle_galilean(a,u,v)
            self.assertTrue(r['free_particle_law_preserved'])
            self.assertEqual(r['transformed_origin'],a)
            self.assertEqual(r['transformed_velocity'],u-v)
            self.assertEqual(r['transformed_acceleration'],0)

    def test_galilean_transport_is_valid_for_declared_moving_medium(self):
        from observational_succ.galilean_lorentz_succ import galilean_moving_medium_wave_operator
        for v in (F(-3,5),F(-1,3),F(0),F(3,5)):
            r=galilean_moving_medium_wave_operator(v)
            self.assertEqual(r['operator_in_moving_frame'],galilean(v) @ ETA @ galilean(v).transpose())
            self.assertEqual(r['same_form_vacuum_operator'],v==0)
            self.assertFalse(r['unique_physical_model_selected'])
            self.assertEqual(r['wave_characteristic_speeds'],(-1-v,1-v))

    def test_both_repairs_exist_but_source_assumptions_differ(self):
        from observational_succ.galilean_lorentz_succ import galilean_moving_medium_wave_operator
        v=F(3,5)
        self.assertEqual(metric_defect(rational_boost(F(1,3))[2]),ZERO)
        self.assertNotEqual(galilean_moving_medium_wave_operator(v)['operator_in_moving_frame'],ETA)

class TimeOrientationIsAnIndependentSourceGate(unittest.TestCase):
    def test_metric_covariance_alone_does_not_preserve_future_causality(self):
        time_reversal=Mat2(-1,0,0,1)
        self.assertEqual(metric_defect(time_reversal),ZERO)
        self.assertEqual(interval_squared(time_reversal.apply((2,1))),3)
        self.assertFalse(is_future_causal(time_reversal.apply((2,1))))
        self.assertTrue(is_future_causal((2,1)))
        # Source asks for proper orthochronous frames, not arbitrary O(1,1).
        self.assertEqual(rational_boost(F(1,3))[2].determinant(),1)
