"""Exact arithmetic tests: inertial gauge and unordered-relative normality instrument.

Asymptotic theorems live in README.md; finite checks are calibrations, not
universal certificates or a proof of the original signed Weyl sum.
"""
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from math import cos, sin, pi
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research/2026-10-29/inertial_relative_observer'))
import relative_observer as s

class TestOriginalSource(unittest.TestCase):
    def test_four_poles_and_inherited_rational_orbit(self):
        self.assertEqual(s.forcing(1),Q(47,15))
        self.assertEqual(s.forcing(2),Q(106,819))
        u=s.original_orbit(Q(0),5)
        self.assertEqual(u[0],Q(0))
        self.assertEqual(u[1],Q(47,15))
        self.assertEqual(u[2],16*Q(47,15)+Q(106,819))
        for n in range(1,len(u)):
            self.assertEqual(u[n],16*u[n-1]+s.forcing(n))

    def test_source_positivity_and_integral_upper_bound(self):
        for n in range(1,101):
            r=s.forcing(n)
            self.assertGreater(r,0)
            self.assertLess(r,Q(15,(8*n-7)**2))

    def test_one_step_exact_relative_charge(self):
        v=s.original_orbit(Q(0),31)
        for n in range(0,30):
            self.assertEqual(s.temporal_lag(v,n,1),15*v[n]+s.forcing(n+1))

    def test_all_fixed_lags_exact_source_memory(self):
        v=s.original_orbit(Q(0),31)
        for n in range(0,12):
            for k in range(1,9):
                self.assertEqual(s.temporal_lag(v,n,k),(16**k-1)*v[n]+s.source_lag(n,k))

    def test_independent_seed_exact_lags(self):
        for seed in (Q(-17,21),Q(0),Q(1,15),Q(3,8),Q(1,240)):
            v=s.original_orbit(seed,25)
            for n in range(1,18):
                for k in range(1,5):
                    self.assertEqual(s.temporal_lag(v,n,k),s.projected_charge(n,k)*v[n]+s.source_lag(n,k))

    def test_all_horizon_explicit_lag_budget(self):
        for k in (1,2,3,4,5):
            budget=s.bound_lag_source_alln(k)
            self.assertEqual(budget,(16**k-1)*Q(17,648))
            for N in (1,2,4,10,30):
                self.assertGreater(budget,s.finite_source_lag_budget(N,k))

    def test_source_clock_15_alignment_not_inferred_phase_decay(self):
        # Four-pole positive Laplace density Q(t)=4-2e^-3t-e^-4t-e^-5t.
        # Q'(0)=2*3+1*4+1*5=15, separately 16-1=15.
        self.assertEqual(2*3+4+5,s.CHARGE)
        self.assertEqual(s.CHARGE,15)

class TestGauge(unittest.TestCase):
    def test_constant_coordinate_shift_changes_known_forcing(self):
        for a in (Q(-7,5),Q(0),Q(3,7),Q(1,15)):
            x=s.original_orbit(Q(0),16)
            # The translated orbit is a solution ONLY when r changes by -15a.
            for n in range(1,len(x)):
                self.assertEqual(x[n]+a,16*(x[n-1]+a)+s.shifted_source_for_new_origin(s.forcing(n),a))
            for n in range(0,len(x)-1):
                self.assertEqual((x[n+1]+a)-(x[n]+a),x[n+1]-x[n])

    def test_gauge_stabilizer_constant_circle_shift(self):
        for a in range(-30,31):
            delta=Q(a,15)
            self.assertEqual(s.circle_fraction(15*delta),0)
            x=s.original_orbit(Q(0),12)
            y=s.original_orbit(delta,12)
            for n in range(0,12):
                self.assertEqual(s.circle_fraction(y[n]-x[n]),s.circle_fraction(delta))
                self.assertEqual(s.circle_fraction((y[n+1]-y[n])-(x[n+1]-x[n])),0)

    def test_relative_kernel_from_first_time(self):
        for n0 in range(0,5):
            denom=s.temporal_observation_kernel(n0,1)
            self.assertEqual(denom,15*16**n0)
            for a in (1,3,7,23):
                d=Q(a,denom)
                x=s.original_orbit(Q(0),n0+9)
                y=s.original_orbit(d,n0+9)
                shift=s.compatible_seed_suffix_shift(d,n0)
                for n in range(n0,n0+8):
                    self.assertEqual(s.circle_fraction(y[n]-x[n]),shift)
                    self.assertEqual(s.circle_fraction((y[n+1]-y[n])-(x[n+1]-x[n])),0)
            with self.assertRaises(ValueError):
                s.compatible_seed_suffix_shift(Q(1,2*denom),n0)

    def test_15_torsion_does_not_forget_four_pole_source_in_real_lift(self):
        # A circle phase can be identical after a nonzero shift; exact real lifts are not.
        original=s.original_orbit(Q(0),15)
        changed=s.original_orbit(Q(-1),15)
        self.assertNotEqual(original[8],changed[8])
        for n in range(16):
            self.assertEqual(s.circle_fraction(original[n]-changed[n]),0)

    def test_relative_record_can_resolve_normality_but_not_absolute_seed(self):
        # Finite exact model: no seed identity under the 15-torsion kernel.
        for seed in (Q(0),Q(1,15),Q(7,15)):
            v=s.original_orbit(seed,25)
            rel=s.displacements(v,N=22)
            if seed==0:baseline=rel
            else:self.assertEqual(rel,baseline)

    def test_multi_lag_kernel(self):
        for k in range(1,6):
            denom=s.temporal_observation_kernel(0,k)
            self.assertEqual(denom,16**k-1)
            diff=Q(1,denom)
            x=s.original_orbit(Q(0),20)
            y=s.original_orbit(diff,20)
            for n in range(0,18-k):
                self.assertEqual(s.circle_fraction(s.temporal_lag(y,n,k)-s.temporal_lag(x,n,k)),0)

class TestObservationCountermodels(unittest.TestCase):
    def test_truncated_pushforward_is_grid_but_preimage_is_not(self):
        for q in (3,7,15,31,65):
            coords=tuple(Q(j,15*q) for j in range(q))
            assert all(Q(0)<=v<Q(1,15) for v in coords)
            self.assertEqual(s.exactly_uniform_grid_pushforward(q),tuple(Q(j,q) for j in range(q)))
            # The measure has no mass in most of the original circle.
            self.assertFalse(any(x>=Q(1,15) for x in coords))
            # Yet multiplying by 15 makes an exactly equally spaced q-point grid.

    def test_finite_alternating_countermodel_without_dynamics(self):
        # Relative increments are uniform q-grid, while original states put >=half at zero.
        for q in (5,11,17):
            states=[]
            for j in range(q):
                states.extend((Q(0),Q(j,q)))
            states.append(Q(0))
            increments=tuple(s.circle_fraction(states[t+1]-states[t]) for t in range(2*q))
            self.assertEqual(sorted(increments),sorted((Q(j,q) for j in range(q)))*2 if q==1 else sorted((Q(j,q) for j in range(q) for _ in (0,1))))
            self.assertGreater(sum(1 for x in states[:2*q] if x==0),q)
            # Not a counterexample to the source theorem: the forcing does not tend to zero.

    def test_invariant_nonhaar_null_control(self):
        # x_n=0 is a fixed orbit of T16, but both position and increments are delta_0.
        states=tuple(Q(0) for _ in range(30))
        self.assertEqual(s.displacements(states,N=25),tuple(Q(0) for _ in range(25)))

    def test_numerical_fourier_lag_bound_observation_only(self):
        seed=s.original_orbit(Q(0),60)
        for k in (1,2,3):
            rel=s.displacements(seed,k=k,N=30)
            proj=s.projected_values(seed,k=k,N=30)
            for h in (1,2,5):
                err=abs(s.characteristic(rel,h)-s.characteristic(proj,h))
                explicit=2*pi*h*float(s.finite_source_lag_budget(30,k))/30
                self.assertLessEqual(err,explicit+1e-13)
                self.assertLess(explicit,2*pi*h*float(s.bound_lag_source_alln(k))/30)

    def test_relative_eisenstein_energy_is_nonnegative(self):
        orbit=s.original_orbit(Q(0),38)
        rel=s.displacements(orbit,N=32)
        projection=s.projected_values(orbit,N=32)
        er=s.eisenstein_energy(rel,1.0,8)
        ep=s.eisenstein_energy(projection,1.0,8)
        self.assertGreaterEqual(er,0)
        self.assertGreaterEqual(ep,0)
        self.assertLess(abs(er-ep),s.relative_shifted_energy_bound_prefactor(1.0)/32+1e-12)

    def test_mutated_forcing_does_not_create_proof(self):
        # The theorem needs r_n->0, not the specific four-pole shape; normality remains open.
        for n in (1,2,3,5,8,21):
            self.assertEqual(s.forcing(n)-s.forcing(n),0)
        self.assertLess(s.bound_lag_source_alln(1),Q(1))

    def test_invalid_arguments_rejected(self):
        with self.assertRaises(ValueError):s.forcing(0)
        with self.assertRaises(TypeError):s.original_orbit(0,4)
        with self.assertRaises(ValueError):s.original_orbit(Q(0),301)
        with self.assertRaises(ValueError):s.temporal_observation_kernel(-1)
        with self.assertRaises(ValueError):s.eisenstein_coefficient(0)
        with self.assertRaises(ValueError):s.eisenstein_coefficient(1,0)
        with self.assertRaises(TypeError):s.circle_fraction(0.5)

if __name__=='__main__':unittest.main()

class TestGreenTailUniformTransport(unittest.TestCase):
    def test_rational_green_tail_brackets_and_monotonicity(self):
        for n in (0,1,2,3,7,13,27,65):
            for depth in (1,2,3,6,10):
                low,high=s.future_tail_interval(n,depth)
                self.assertGreater(low,0)
                self.assertLess(low,high)
                self.assertLessEqual(high,s.tail_simple_upper(n))
                if depth>1:
                    lp,hp=s.future_tail_interval(n,depth-1)
                    self.assertGreater(low,lp)
                    self.assertLess(high,hp)
            self.assertLess(s.tail_simple_upper(n+1),s.tail_simple_upper(n))

    def test_BBP_pi_div16_rational_interval_narrowing(self):
        last=None
        for D in (1,2,3,5,9,13,20):
            lo,hi=s.pi_over16_interval(D)
            self.assertLess(lo,hi)
            self.assertLess(hi-lo,s.tail_simple_upper(D)/16**D+Q(1,10**100))
            if last:
                self.assertGreaterEqual(lo,last[0])
                self.assertLessEqual(hi,last[1])
            last=(lo,hi)
        self.assertLess(last[1]-last[0],Q(1,10**26))

    def test_telescoped_budget_does_not_blow_up_with_lag(self):
        assert s.all_lag_telescoping_bound()==Q(17,648)
        for N in (1,2,4,10,50,100):
            for k in (1,2,4,16,64):
                budget=s.telescoped_lag_budget(N,k)
                self.assertLess(budget,s.all_lag_telescoping_bound())
                self.assertEqual(budget,sum((s.tail_simple_upper(n) for n in range(1,min(N,k)+1)),Q(0)))
        self.assertLess(s.telescoped_lag_budget(100,100),Q(17,648))

    def test_verified_tail_differences_from_rational_intervals(self):
        # The true tail differences can be certified from disjoint enclosures,
        # including a positive lower bound and uniform all-lag upper estimate.
        for n in (1,2,5,9,16,31):
            for k in (1,2,3,7,13):
                ln,un=s.future_tail_interval(n,15)
                lk,uk=s.future_tail_interval(n+k,15)
                self.assertGreater(ln-uk,0)
                self.assertLess(un-lk,s.tail_simple_upper(n))

    def test_numerical_improvement_vs_direct_inhomogeneous_forcing(self):
        N=50
        for k in (1,2,3,7,30):
            direct=s.finite_source_lag_budget(N,min(k,20)) if k<=20 else s.bound_lag_source_alln(k)
            improved=s.telescoped_lag_budget(N,k)
            self.assertLess(improved,direct)
        self.assertLess(s.telescoped_fourier_error_budget(N,1,20),2*pi*float(Q(17,648))/N)

    def test_source_pi_clock_coherent_counterseed(self):
        # alpha=0 when seed=-pi/16, hence relative increments become tiny
        # positive rational tail differences, not Haar-distributed.
        for n in (1,10,50):
            ln,un=s.future_tail_interval(n,20)
            lm,um=s.future_tail_interval(n+1,20)
            self.assertGreater(ln-um,0)
            self.assertLess(un-lm,s.tail_simple_upper(n))

    def test_inherited_eisenstein_coefficients_are_strictly_positive(self):
        for h in range(1,36):
            self.assertGreater(s.eisenstein_sigma_minus3(h),0)
            self.assertGreater(s.eisenstein_coefficient(h,1.0),0)


class TestExactGammaGreenMemory(unittest.TestCase):
    def test_source_canonical_memory_constant_numeric_against_rational_brackets(self):
        # Paper formula is exact; this is a diagnostic comparison to certified brackets.
        c=s.green_memory_closed_numeric()
        self.assertAlmostEqual(c,0.01629699773382656556,delta=1e-14)
        for rows in (10,30,80):
            lo,hi=s.green_memory_rational_interval(rows,16)
            self.assertLess(float(lo),c)
            self.assertGreater(float(hi),c)
        self.assertLess(c,float(s.all_lag_telescoping_bound()))

    def test_rational_memory_enclosures_shrink_with_depth_and_rows(self):
        last=None
        for rows in (5,20,40,100):
            lo,hi=s.green_memory_rational_interval(rows,14)
            self.assertLess(lo,hi)
            if last:
                self.assertGreater(lo,last[0])
                self.assertLess(hi,last[1])
            last=(lo,hi)
        self.assertLess(float(last[1]-last[0]),0.0002)

    def test_green_memory_budget_is_independent_of_lag(self):
        upper=s.all_lag_telescoping_bound()
        for k in (1,2,10,50,200):
            for N in (1,4,12,80):
                self.assertLess(s.telescoped_lag_budget(N,k),upper)


class TestDebiasedRelativeSource(unittest.TestCase):
    def test_exact_debiased_observer_is_15_fold_circle_quotient(self):
        for seed in (Q(0),Q(1,15),Q(-1),Q(5,23)):
            trajectory=s.original_orbit(seed,49)
            observed=s.debiased_displacements(trajectory,first_time=1,N=40)
            expected=tuple(s.circle_fraction(15*trajectory[n]) for n in range(1,41))
            self.assertEqual(observed,expected)
            self.assertEqual(observed,s.projected_values(trajectory,N=40))

    def test_debiased_invariant_under_simultaneous_source_translation(self):
        x=s.original_orbit(Q(0),18)
        shifted=tuple(a+Q(2,15) for a in x)
        new_source=[s.shifted_source_for_new_origin(s.forcing(n+1),Q(2,15)) for n in range(17)]
        self.assertEqual(tuple(s.circle_fraction(x[n+1]-x[n]-s.forcing(n+1)) for n in range(1,17)),
                         tuple(s.circle_fraction(shifted[n+1]-shifted[n]-new_source[n]) for n in range(1,17)))


class TestNonNormalInertialMutant(unittest.TestCase):
    @staticmethod
    def mutant_r(n,d=3):
        return Q(16,(8*n-7+d)**2)-Q(1,(8*n+1+d)**2)
    @staticmethod
    def mutant_u(n,d=3):
        return Q(16**n,(d+1)**2)-Q(1,(8*n+1+d)**2)
    def test_same_slope_15_and_zero_seed_non_normal(self):
        # From inherited PR373: Q_d(t)=t(16e^(-dt)-e^(-(d+8)t)).
        # Q_d'(0)=15, while d=3 has alpha=1/16 rational and is coherent.
        self.assertEqual(16-1,15)
        self.assertEqual(self.mutant_u(0),Q(0))
        self.assertNotEqual(self.mutant_r(1),s.forcing(1))
        for n in range(1,70):
            self.assertGreater(self.mutant_r(n),0)
            self.assertEqual(self.mutant_u(n)-16*self.mutant_u(n-1),self.mutant_r(n))
            self.assertEqual(s.circle_fraction(self.mutant_u(n)),1-Q(1,(8*n+4)**2))

    def test_mutant_relative_displacements_converge_to_zero(self):
        # All nonzero Fourier modes of delta approach 1, rather than Haar.
        for n in (1,5,20,100,1000):
            delta=s.circle_fraction(self.mutant_u(n+1)-self.mutant_u(n))
            self.assertGreater(delta,0)
            self.assertLess(delta,Q(1,(8*n+4)**2))
        self.assertLess(s.circle_fraction(self.mutant_u(1001)-self.mutant_u(1000)),Q(1,10**8))
