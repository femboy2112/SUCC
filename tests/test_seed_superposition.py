"""Exact source-faithful seed-superposition regression. No pi proof from finite tests."""
import sys
import unittest
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
    "research" / "2026-10-31" / "seed_superposition"))
from seed_superposition import (
    forcing,states,seed_lift_identity,recurrence_resonance,prefix_cylinder,
    future_integral_is_zero,covariance_late,late_second_moment,
    early_anchor_error_coefficient,cell_mean_prefix_equivalence,
    phase_relation_unique_for_equal_counts,iid_balanced_moment,
    direct_balanced_moment,first_equal_count_carry_resonance,
    concentration_bound,exact_grid_seed_alias,grid_alias_onset,
    exact_discrete_grid_character_sum,source_tail_upper,
    coherent_changed_seed_bound,seed_phase_boundary,
    dyadic_seed_coalescence_time,finite_dyadic_measure_coalescence,
    late_gradient_energy_coefficient,selected_point_lipschitz_obstruction,
    late_radix_resonance_error_coefficient,
)

class TestOriginalSeedSuperposition(unittest.TestCase):
    def test_01_frozen_original_source(self):
        self.assertEqual(forcing(1),F(47,15))
        self.assertEqual(forcing(2),F(106,819))
        for n in range(1,70):
            self.assertEqual(forcing(n),F(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
        self.assertEqual(states(3),(F(0),F(47,15),16*F(47,15)+F(106,819)))

    def test_02_exact_seed_lift_and_recurrence(self):
        for s in (0,F(1,3),F(-13,47),F(17,32)):
            for n in range(0,40):
                self.assertTrue(seed_lift_identity(n,s))
                self.assertEqual(recurrence_resonance(n,s,1),-forcing(n+1))
                self.assertEqual(recurrence_resonance(n,s,11),-11*forcing(n+1))

    def test_03_fixed_source_superposition_not_selected_point(self):
        for m in range(0,8):
            a=16**m-1
            lo,hi=prefix_cylinder(m,a)
            self.assertEqual(hi-lo,F(1,16**m))
            self.assertEqual(lo,F(a,16**m))
            self.assertTrue(seed_phase_boundary(F(-1,3),m)['selected_point_unproved'])
        with self.assertRaises(ValueError):prefix_cylinder(2,256)

    def test_04_future_modes_exactly_conditional_zero(self):
        for m in (0,1,2,5,10):
            for n in (m,m+1,m+7,m+29):
                for h in (-31,-1,1,2,17):
                    self.assertTrue(future_integral_is_zero(m,n,h))
        with self.assertRaises(ValueError):future_integral_is_zero(4,3)

    def test_05_late_phase_gram_exactly_diagonal(self):
        for m in (0,1,7):
            for i in range(m,m+8):
                for j in range(m,m+8):
                    self.assertEqual(covariance_late(m,i,j),int(i==j))
            self.assertEqual(late_second_moment(m,m+8),8)

    def test_06_selected_anchor_and_cylinder_mean_error(self):
        for m in range(1,15):
            a=early_anchor_error_coefficient(m,m)
            self.assertEqual(a,F(1,15)*(1-F(1,16**m)))
            self.assertLess(a,F(1,15))
            for N in (m,m+1,2*m):
                score=cell_mean_prefix_equivalence(m,N,-7)
                self.assertEqual(score['early_time_count'],m)
                self.assertEqual(score['late_time_count'],N-m)
                self.assertEqual(score['error_coefficient_times_pi_abs_h'],a)

    def test_07_fixed_early_horizon_regression(self):
        for m in (1,3,8):
            for N in range(m):
                c=early_anchor_error_coefficient(m,N)
                self.assertEqual(c,F(16**N-1,15*16**m))

    def test_08_conditional_moment_formulas(self):
        for k in range(1,9):
            self.assertEqual(iid_balanced_moment(k,1),k)
            self.assertEqual(iid_balanced_moment(k,2),2*k*k-k)
            self.assertLessEqual(iid_balanced_moment(k,3),factorial(3)*k**3)

    def test_09_independent_frequency_collision_oracle(self):
        for k,r in ((1,1),(3,2),(5,3),(4,5),(2,10)):
            self.assertEqual(iid_balanced_moment(k,r),
                direct_balanced_moment(k,r))

    def test_10_first_equal_cardinality_carry_at_17(self):
        for r in range(17):
            self.assertTrue(phase_relation_unique_for_equal_counts(r))
        self.assertFalse(phase_relation_unique_for_equal_counts(17))
        x=first_equal_count_carry_resonance()
        self.assertTrue(x['equal'])
        self.assertTrue(x['distinct_multisets'])
        self.assertEqual(x['terms_each'],17)

    def test_11_conditional_tail_concentration(self):
        for K in (3,40,100,1000):
            for r in (1,2,4,8):
                bound=concentration_bound(K,r,F(1,2))
                self.assertGreaterEqual(bound,0)
                self.assertLessEqual(bound,1)
            if K>=100:
                self.assertLess(concentration_bound(K,2,F(1,2)),F(1,10))

    def test_12_exact_grid_alias_threshold(self):
        for m,d in ((0,1),(2,3),(4,5)):
            self.assertEqual(grid_alias_onset(m,d,1),m+d)
            for n in range(m,m+d):
                self.assertEqual(exact_grid_seed_alias(m,d,n,1),0)
                self.assertTrue(future_integral_is_zero(m,n))
            for n in range(m+d,m+d+8):
                self.assertEqual(exact_grid_seed_alias(m,d,n,1),1)
                self.assertTrue(future_integral_is_zero(m,n))

    def test_13_grid_alias_high_divisible_h(self):
        for m,d in ((0,4),(3,3)):
            for n in range(m,m+d+4):
                h=16**2
                self.assertEqual(exact_grid_seed_alias(m,d,n,h),
                    int(n>=m+max(0,d-2)))

    def test_14_independent_finite_group_character_sum(self):
        for d in range(1,5):
            order=16**d
            for exp in (0,1,16,16**d,16**(d+2),-1):
                result=exact_discrete_grid_character_sum(order,exp)
                self.assertEqual(result,order if exp%order==0 else 0)

    def test_15_valid_bound_and_coherent_seed_countercontrol(self):
        self.assertEqual(coherent_changed_seed_bound(1),F(1,16))
        for n in range(1,100):
            self.assertGreater(source_tail_upper(n),0)
            self.assertLess(source_tail_upper(n),F(1,64*n*n))
        self.assertLess(sum((source_tail_upper(n) for n in range(1,4000)),F(0)),F(1,32))

    def test_16_no_bad_input_silently_accepted(self):
        for fn,args in ((forcing,(0,)),(states,(-1,)),
            (states,(2,0.1)),(prefix_cylinder,(1,-1)),
            (future_integral_is_zero,(3,0)),
            (covariance_late,(3,2,4)),
            (iid_balanced_moment,(3,17)),
            (concentration_bound,(0,2,F(1,2))),
            (grid_alias_onset,(3,-1)),
            (source_tail_upper,(0,)),
            (recurrence_resonance,(3,0,0))):
            with self.assertRaises(ValueError):fn(*args)

    def test_17_finite_dyadic_paths_collapse_to_rank_one(self):
        for d in range(1,11):
            seeds=tuple(F(j,16**d) for j in range(16))
            weights=tuple(F(1,len(seeds)) for _ in seeds)
            z=finite_dyadic_measure_coalescence(seeds,weights)
            self.assertLessEqual(z['coalescence_time'],d)
            self.assertEqual(z['future_phase_gram_rank'],1)
            for s in seeds:
                self.assertEqual((16**d*s).denominator,1)
        self.assertEqual(dyadic_seed_coalescence_time(F(1,2**19)),5)
        with self.assertRaises(ValueError):dyadic_seed_coalescence_time(F(1,3))

    def test_18_independent_cyclotomic_anti_aliasing(self):
        from independent_oracle import independent_cyclic_grid
        for order in (16,256,4096):
            for freq in (0,1,16,256,4096,order-1):
                vec=independent_cyclic_grid(order,freq)
                self.assertEqual(all(x==0 for x in vec),freq%order!=0)
                self.assertEqual(sum(abs(x) for x in vec),order if freq%order==0 else 0)

    def test_19_source_independent_moment_boundary_at_r17(self):
        from independent_oracle import direct_equal_count_collisions
        for k in (3,4):
            for r in range(1,17):
                _, collisions=direct_equal_count_collisions(k,r)
                self.assertEqual(collisions,0,(k,r))
            _, collisions=direct_equal_count_collisions(k,17)
            self.assertGreater(collisions,0)

    def test_20_independent_moment_in_original_source(self):
        from independent_oracle import direct_haar_moment_tuples
        for k,r in ((2,9),(3,6),(5,5)):
            self.assertEqual(iid_balanced_moment(k,r),
                             direct_haar_moment_tuples(k,r))

    def test_21_resistance_dirichlet_gradient_energy_exact(self):
        for depth in (0,1,3,6):
            for K in (0,1,2,4,10):
                stop=depth+K
                predicted=sum(16**(2*n) for n in range(depth,stop))
                self.assertEqual(late_gradient_energy_coefficient(depth,stop),predicted)
                self.assertGreaterEqual(predicted,0)
            if depth<6:
                self.assertGreater(late_gradient_energy_coefficient(depth,depth+8),
                                   16**(2*(depth+7)))

    def test_22_point_evaluation_cost_and_early_repair(self):
        for depth in (1,3,7):
            self.assertLess(selected_point_lipschitz_obstruction(depth,depth),F(1,15))
            self.assertGreater(selected_point_lipschitz_obstruction(depth,depth+4),
                               F(16**4-1,15))
            for stop in (depth,depth+1,depth+5):
                if stop>=depth:
                    self.assertLessEqual(early_anchor_error_coefficient(depth,stop),
                                         selected_point_lipschitz_obstruction(depth,stop))

    def test_23_original_late_resonance_is_almost_coherent(self):
        for start in (2,4,9,20,40):
            source_sum=sum((forcing(n+1) for n in range(start, 800)),F(0))
            self.assertLess(2*source_sum,late_radix_resonance_error_coefficient(start))
            self.assertEqual(late_radix_resonance_error_coefficient(start,7),
                             7*late_radix_resonance_error_coefficient(start,1))
        self.assertGreater(late_radix_resonance_error_coefficient(2),
                           late_radix_resonance_error_coefficient(10))

    def test_24_pr432_exact_73_point_tomography_and_tenth_mode_alias(self):
        # Sibling PR #432's classical (73,9,1) difference set, independently
        # checked here as an integration/provenance guard, not new discovery.
        p=73
        d=[pow(16,n,p) for n in range(1,10)]
        self.assertEqual(len(set(d)),9)
        oriented=[(d[i]-d[j])%p for i in range(9)
                  for j in range(9) if i!=j]
        self.assertEqual(len(oriented),72)
        self.assertEqual(sorted(oriented),list(range(1,p)))
        self.assertEqual(pow(16,10,p),d[0])
        self.assertEqual({(p*delta)%p for delta in oriented},{0})
        self.assertEqual(9*(9-1)+1,73)
        self.assertLess(73,10*(10-1)+1)

    def test_25_every_fixed_cyclic_seed_sampling_grid_eventually_aliases(self):
        # This is an exact finite observation-horizon NO-GO, not an
        # obstruction to growing-grid PR #432 tomography.
        for modulus in (2,16,17,19,73,127,256,257,1201):
            seen=set()
            collided=False
            for n in range(modulus+1):
                v=pow(16,n,modulus)
                if v in seen:
                    collided=True
                    break
                seen.add(v)
            self.assertTrue(collided,(modulus,n))
        for depth,resolution in ((0,1),(2,2),(7,4)):
            onset=grid_alias_onset(depth,resolution,1)
            self.assertEqual(onset,depth+resolution)
            self.assertEqual(exact_grid_seed_alias(depth,resolution,onset,1),1)
            self.assertTrue(future_integral_is_zero(depth,onset,1))

if __name__=='__main__':unittest.main()
