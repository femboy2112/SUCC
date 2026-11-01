"""Finite-history/constant-curvature bridge: independent exact oracles and mutants."""
from __future__ import annotations
import importlib.util
from pathlib import Path
from fractions import Fraction as F
import unittest

HERE=Path(__file__).resolve().parents[1] / 'research' / '2026-11-01' / 'finite_history_circle'

def load(name, file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

b=load('new_finite_memory_source','finite_history.py')
o=load('new_independent_future_oracle','independent_oracle.py')


class SourceRigidityTests(unittest.TestCase):
    def test_01_four_poles_match(self):
        for n in range(1,70):self.assertEqual(b.source(n),o.exact_source(n))
    def test_02_one_step_original(self):
        self.assertEqual(b.source(1),F(47,15))
    def test_03_two_step_original(self):
        self.assertEqual(b.source(2),F(106,819))
    def test_04_original_positive(self):
        self.assertTrue(all(b.source(n)>0 for n in range(1,101)))
    def test_05_original_decreasing(self):
        self.assertTrue(all(b.source(n)>b.source(n+1) for n in range(1,70)))
    def test_06_original_unwrap_interval(self):
        self.assertTrue(all(0<b.source(n)<1 for n in range(2,90)))
    def test_07_zero_seed(self):
        self.assertEqual(b.source_orbit(1)[0],0)
    def test_08_seven_reconstruction(self):
        want=((F(1,32),F(-89,512),F(15,64)),
              (F(21,512),F(-103,256),F(89,64),F(-2),F(1)))
        self.assertEqual(b.original_seven_model(),want)
    def test_09_forecast_100(self):
        f=b.original_seven_model()
        for n in [8,9,17,31,100,211]:self.assertEqual(b.rational_eval(f,n),b.source(n))
    def test_10_shifted_seven(self):
        for start in [2,6,13,67]:
            m=b.fit_type_24([(j,o.exact_source(j)) for j in range(start,start+7)])
            for j in [1,2,7,100]:self.assertEqual(b.rational_eval(m,j),b.source(j))
    def test_11_arbitrary_seven(self):
        m=b.fit_type_24([(n,b.source(n)) for n in (1,4,5,17,30,37,105)])
        self.assertEqual(m,b.original_seven_model())
    def test_12_cramer_independent(self):
        for nodes in [list(range(1,8)),[2,3,5,8,9,12,17],list(range(35,42))]:
            x=[(n,o.exact_source(n)) for n in nodes]
            self.assertEqual(b.fit_type_24(x),o.fit_by_cramer(x))
    def test_13_seven_repeated_rejected(self):
        with self.assertRaises(ValueError):b.fit_type_24([(1,b.source(1))]*7)
    def test_14_six_rejected(self):
        with self.assertRaises(ValueError):b.fit_type_24([(n,b.source(n)) for n in range(1,7)])
    def test_15_spoof_exact_poly_identity(self):
        lhs,rhs=b.spoof_polynomial_certificate()
        self.assertEqual(lhs,rhs)
    def test_16_spoof_six_match(self):
        for n in range(1,7):self.assertEqual(b.spoof_six(n),b.source(n))
    def test_17_spoof_seventh_diff(self):
        self.assertGreater(b.spoof_six(7)-b.source(7),0)
    def test_18_spoof_positive_integer(self):
        for n in range(1,151):self.assertGreater(b.spoof_six(n),0)
    def test_19_spoof_positive_fractional(self):
        for x in [F(5,4),F(3,2),F(9,4),F(101,2),F(500001,100)]:
            self.assertGreater(b.spoof_six(x),0)
    def test_20_spoof_phase_prefix(self):
        self.assertEqual(b.circle_phase_history(6),b.circle_phase_history(6,source_fn=b.spoof_six))
        self.assertNotEqual(b.circle_phase_history(7),b.circle_phase_history(7,source_fn=b.spoof_six))


class CircleClockTests(unittest.TestCase):
    def test_21_eight_exact_phases(self):
        m=b.source_from_eight_circle_phases(b.circle_phase_history(8)[1:])
        self.assertEqual(m,b.original_seven_model())
    def test_22_phase_unwrap_2to8(self):
        phase=b.circle_phase_history(8)
        for n in range(2,9):
            self.assertEqual(b.frac_mod_one(phase[n]-16*phase[n-1]),b.source(n))
    def test_23_phase_fraction_representative(self):
        self.assertEqual(b.frac_mod_one(F(-7,3)),F(2,3))
    def test_24_inverse_sixteen(self):
        end=F(7,11);r=F(3,14)
        choices=b.inverse_branches(end,r)
        self.assertEqual(len(set(choices)),16)
        self.assertTrue(all(b.frac_mod_one(16*x+r)==end for x in choices))
    def test_25_inverse_N_expansion(self):
        for N in [1,2,3]:
            end=b.circle_phase_history(N)[-1]
            ss={b.n_step_preimage_formula(N,end,j) for j in range(16**N)}
            self.assertEqual(len(ss),16**N)
            for s in tuple(ss)[:64]:
                self.assertEqual(b.circle_phase_history(N,seed=s)[-1],end)
    def test_26_past_seed_invisible(self):
        for j in range(16):
            self.assertEqual(b.circle_phase_history(9,F(j,16))[1:],b.circle_phase_history(9)[1:])
    def test_27_initial_seed_visible(self):
        self.assertNotEqual(b.circle_phase_history(1,F(1,16))[0],b.circle_phase_history(1)[0])
    def test_28_seed_not_arithmetic_forcing(self):
        s=F(1,16)
        a=b.source_orbit(8,s)
        c=b.source_orbit(8)
        self.assertTrue(all(a[n]-c[n]==16**n*s for n in range(9)))
    def test_29_phase_six_spoof_fails_rigidity(self):
        s=b.circle_phase_history(8,source_fn=b.spoof_six)
        model=b.source_from_eight_circle_phases(s[1:])
        self.assertNotEqual(model,b.original_seven_model())
    def test_30a_seven_circle_source_with_declared_branch(self):
        phases=b.circle_phase_history(7)[1:]
        self.assertEqual(b.source_from_seven_zero_seed_phases(phases,3),b.original_seven_model())
    def test_30b_wrong_first_branch_not_original(self):
        phases=b.circle_phase_history(7)[1:]
        # Wrong declared integer lift can produce a different exact source law
        # or fail its degree class, but must never be certified original.
        try:
            bad=b.source_from_seven_zero_seed_phases(phases,2)
        except ValueError:
            return
        self.assertNotEqual(bad,b.original_seven_model())
    def test_30_wrong_phase_count_rejected(self):
        with self.assertRaises(ValueError):b.source_from_eight_circle_phases((F(1),)*7)


class GeometryProjectionTests(unittest.TestCase):
    def test_31_sqrt_interval(self):
        a,b_=b.sqrt_dyadic_bounds(F(2),128)
        self.assertLessEqual(a*a,2)
        self.assertGreaterEqual(b_*b_,2)
    def test_32_zero_circle(self):
        self.assertEqual(b.circle_polygon_interval(0),(F(2),F(2)))
    def test_33_refinement_1_brackets_sqrt2(self):
        l,u=b.circle_polygon_interval(1)
        self.assertLess(l*l,8)
        self.assertGreater(u*u,8)
    def test_34_monotone_circle_polygon(self):
        lo=[]
        for k in range(2,16):
            lo.append(b.circle_polygon_interval(k,bits=256)[0])
        self.assertTrue(all(x<y for x,y in zip(lo,lo[1:])))
    def test_35_independent_direct_future(self):
        for n in range(1,8):
            for J in (1,2,3,5):
                self.assertEqual(b.finite_wilson_future(n,J),o.independent_future(n,J))
    def test_36_boundary_required(self):
        n,J=2,3
        curvature=sum(((1-F(1,16**k))*b.wilson_curvature(n+k) for k in range(1,J+1)),F(0))/225
        self.assertEqual(b.finite_wilson_future(n,J)-curvature,
                         (1-F(1,16**J))*b.source(n+J+1)/15)
    def test_37_tail_interval(self):
        for n in range(1,7):
            for J in (1,2,5,8):
                low,upper=b.future_tail_lower_upper(n,J)
                # Verify using 20 additional rational terms and positive tail.
                approximate=b.normalized_bbpfuture(n,J+20)
                self.assertLess(low,approximate)
                self.assertLess(approximate,upper)
    def test_38_refinement_scale(self):
        for N in range(1,100):
            k,L,J=b.refinement_plan(N,2)
            self.assertEqual(k,2*N+L)
            self.assertGreaterEqual(4**L,N*N)
            self.assertGreaterEqual(16**J,N*N)
            if L:self.assertLess(4**(L-1),N*N)
            if J>1:self.assertLess(16**(J-1),N*N)
    def test_39_weyl_global_bound(self):
        for N in range(1,64):
            for h in [-11,-1,1,5]:
                self.assertLessEqual(b.absolute_weyl_transport_bound(N,h,2),
                                     b.universal_power_bound(N,h,2))
    def test_40_arbitrary_power(self):
        for p in range(1,6):
            for N in (1,2,7,64):
                self.assertLessEqual(b.absolute_weyl_transport_bound(N,7,p),
                                     b.universal_power_bound(N,7,p))
    def test_41_echo_operator_bound(self):
        for N in range(1,40):
            for h in [-5,1,3]:
                self.assertLessEqual(b.controlled_echo_operator_bound(N,h),
                                     b.universal_controlled_echo_bound(N,h))
    def test_42_projected_state_interval(self):
        for N in (1,2,3,6,10):
            for n in (1,N):
                lo,hi=b.geometric_predictor_interval(n,N,bits=256)
                self.assertLess(lo,hi)
                self.assertLess(hi-lo,F(1,10**10) if N<10 else F(1,10**6))
    def test_43_eight_history_forecasts_all_finite_tails(self):
        recovered=b.source_from_eight_circle_phases(b.circle_phase_history(8)[1:])
        for n in (1,7,23,65):
            for J in (1,3,9):
                expected=b.finite_wilson_future(n,J)
                actual=b.finite_wilson_future(n,J,lambda x:b.rational_eval(recovered,x))
                self.assertEqual(expected,actual)
    def test_44_source_seven_unwrapped_states(self):
        o0=b.source_orbit(7)
        values=[(n,o0[n]-16*o0[n-1]) for n in range(1,8)]
        self.assertEqual(b.fit_type_24(values),b.original_seven_model())
    def test_45_nonzero_h_required(self):
        with self.assertRaises(ValueError):b.absolute_weyl_transport_bound(5,0)
        with self.assertRaises(ValueError):b.controlled_echo_operator_bound(5,0)
    def test_46_invalid_future_time(self):
        with self.assertRaises(ValueError):b.finite_wilson_future(1,0)
        with self.assertRaises(ValueError):b.normalized_bbpfuture(1,0)
    def test_47_wrong_source_domain(self):
        with self.assertRaises(ValueError):b.source(F(0))
        with self.assertRaises(ValueError):b.spoof_six(F(-1))
    def test_48_absolute_budget_shrinks(self):
        self.assertLess(b.universal_power_bound(32,1,2),b.universal_power_bound(16,1,2))
    def test_49_energy_branch_count_4bits(self):
        self.assertEqual(16**3,4096)
        self.assertEqual(16,2**4)
    def test_50_counterseed_not_detected_by_curvature(self):
        # Source data and Wilson source differences do not depend on altered seed.
        shifted=b.source_orbit(8,F(3,16)); zero=b.source_orbit(8)
        d0=[15*((zero[n]-16*zero[n-1])-(zero[n+1]-16*zero[n])) for n in range(1,8)]
        ds=[15*((shifted[n]-16*shifted[n-1])-(shifted[n+1]-16*shifted[n])) for n in range(1,8)]
        self.assertEqual(d0,ds)

# Additional standalone exact integer/rational holdouts (discovered with unittest).
class IndependentRationalGeometryCertificates(unittest.TestCase):
    def test_51_pi_independent_machin(self):
        lo,hi=o.machin_pi_bounds(80)
        self.assertLess(lo,hi)
        self.assertLess(hi-lo,F(1,10**80))
        self.assertLess(F(3),lo)
        self.assertLess(hi,F(22,7))
    def test_52_circle_path_below_arctan_pi(self):
        pi_lo,pi_hi=o.machin_pi_bounds(110)
        for k in [0,1,2,4,7,12,18,26,43,67]:
            lo,hi=b.circle_polygon_interval(k,bits=320)
            self.assertLess(hi,pi_lo)
            self.assertLess(pi_hi-hi,F(8,3*4**k))
    def test_53_full_projector_rational_phase_closeness(self):
        # An exact arithmetic certification for authentic U_n, no mpmath.
        for N in [1,2,4,7,16,31]:
            k,L,J=b.refinement_plan(N,2)
            old=b.source_orbit(N)
            pi_low,pi_high=b.circle_polygon_interval(k,bits=320)
            for n in range(1,N+1):
                v1=16**(n-1)*pi_low-b.finite_wilson_future(n,J)
                v2=16**(n-1)*pi_high-b.finite_wilson_future(n,J)
                proof_budget=16**(n-1)*F(8,3*4**k)+F(1,64*16**J*(n+J)**2)
                self.assertLess(max(abs(old[n]-v1),abs(old[n]-v2)),proof_budget)

if __name__=='__main__':
    unittest.main()
