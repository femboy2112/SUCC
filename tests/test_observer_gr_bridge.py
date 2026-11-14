"""Exact tests and mutations for the observational GR carrier's scoped claims."""
from fractions import Fraction as Q
import random
import unittest
from observational_succ.observer_gr_bridge import (
    conformal_factor,metric_2d,scalar_curvature_2d,
    classical_scalar_action_density_2d, classical_scalar_coordinate_stress,
    normalized_rest_energy,massless_coordinate_wave_residual,
    conformal_massless_scalar_density, null_directions_4d,
    minkowski_norm,measurement_row,null_measurements,rank_exact,
    r2_metric_variation_constant_einstein,poisson_volume_intensity,
    finite_bits_entropy_over_log2,jacobson_coupling_from_area_entropy,
    scalar_stress_4d,normalized_thermo_matter_ratio
)

class ObserverGRBridgeTest(unittest.TestCase):
    def test_cones_same_but_curvature_differs(self):
        for t in [Q(-3),Q(-1),Q(0),Q(1,4),Q(1,2)]:
            o=conformal_factor(t)
            g=metric_2d(t)
            self.assertEqual(g,((-o*o,0),(0,o*o)))
            for a,b in [(1,1),(1,-1),(2,2),(3,-3)]:
                self.assertEqual(g[0][0]*a*a+g[1][1]*b*b,0)
        self.assertEqual(scalar_curvature_2d(0),0)
        self.assertEqual(scalar_curvature_2d(1),2)
        self.assertEqual(conformal_factor(Q(1,2)),2)

    def test_massless_scalar_action_and_coordinate_stress_blind_to_scale(self):
        rng=random.Random(173)
        for _ in range(130):
            a,b,k=(Q(rng.randint(-5,5),rng.randint(1,5)) for i in range(3))
            k=abs(k)+Q(1,3)
            expected=k*(a*a-b*b)/2
            stresses=[]
            for omega in [Q(1),Q(2),Q(3,2),Q(7,3)]:
                self.assertEqual(classical_scalar_action_density_2d(omega,a,b,k),expected)
                stresses.append(classical_scalar_coordinate_stress(omega,a,b,k))
            self.assertTrue(all(t==stresses[0] for t in stresses))
        self.assertEqual(normalized_rest_energy(2,1,0),Q(1,8))
        self.assertEqual(normalized_rest_energy(1,1,0),Q(1,2))

    def test_2d_wave_equation_invariant_zero_not_value(self):
        for omega in [Q(1),Q(3,2),Q(2)]:
            self.assertEqual(massless_coordinate_wave_residual(omega,2,2),0)
            self.assertEqual(massless_coordinate_wave_residual(omega,1,2),1/(omega*omega))
        self.assertNotEqual(massless_coordinate_wave_residual(1,1,2),massless_coordinate_wave_residual(2,1,2))

    def test_scaling_dimensional_boundary(self):
        for omega in [Q(1),Q(2),Q(3,2)]:
            self.assertEqual(conformal_massless_scalar_density(2,omega,-3),Q(3,2))
            self.assertEqual(conformal_massless_scalar_density(4,omega,-3),Q(3,2)*omega**2)
        self.assertNotEqual(conformal_massless_scalar_density(4,2,-3),conformal_massless_scalar_density(4,1,-3))

    def test_nine_null_directions_have_rank_nine_and_metric_is_kernel(self):
        directions=null_directions_4d()
        self.assertEqual(len(directions),9)
        self.assertTrue(all(minkowski_norm(k)==0 for k in directions))
        rows=[measurement_row(k) for k in directions]
        self.assertEqual(rank_exact(rows),9)
        eta=((-1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
        self.assertEqual(null_measurements(eta),(0,)*9)
        self.assertEqual(rank_exact(rows[:-1]),8)
        T=[list(row) for row in eta];T[1][2]=T[2][1]=1
        self.assertNotEqual(null_measurements(T)[-3:],(0,0,0))

    def test_null_reconstruction_is_exact_for_random_symmetric_tensors(self):
        rng=random.Random(200)
        eta=[-1,1,1,1]
        for _ in range(50):
            A=[[Q(rng.randint(-4,4)) for _ in range(4)] for _ in range(4)]
            S=[[A[i][j]+A[j][i] for j in range(4)] for i in range(4)]
            nulls=null_measurements(S)
            if nulls==(0,)*9:
                self.assertEqual(S,[[(-S[0][0])*eta[i] if i==j else 0 for j in range(4)] for i in range(4)])
            self.assertEqual(nulls,tuple(sum(k[i]*S[i][j]*k[j] for i in range(4) for j in range(4)) for k in null_directions_4d()))

    def test_two_rival_gravity_actions_share_einstein_backgrounds(self):
        for scalar_R in [Q(-100),Q(-6),Q(0),Q(7,3),Q(12)]:
            self.assertEqual(r2_metric_variation_constant_einstein(scalar_R),0)
        self.assertNotEqual(2*Q(12)*Q(2)-Q(12)**2/2,0) # non-Einstein Ricci candidate

    def test_entropy_not_fixed_by_record_or_graph(self):
        for n in [1,2,3,5,11]:
            self.assertEqual(finite_bits_entropy_over_log2(n,True),n)
            self.assertEqual(finite_bits_entropy_over_log2(n,False),0)
            self.assertGreater(finite_bits_entropy_over_log2(n,True),finite_bits_entropy_over_log2(n,False))
        self.assertRaises(ValueError,finite_bits_entropy_over_log2,-1)

    def test_unfixed_sprinkling_density_conformal_scale_gauge(self):
        for dim in [2,3,4]:
            for scale in [Q(2),Q(3,2),Q(5,3)]:
                self.assertEqual(poisson_volume_intensity(dim,1,1),poisson_volume_intensity(dim,scale,1/scale**dim))
                self.assertNotEqual(poisson_volume_intensity(dim,1,1),poisson_volume_intensity(dim,scale,1))

    def test_null_scalar_flux_blind_to_potential_but_timelike_energy_is_not(self):
        grad=(Q(1),Q(2),Q(-3),Q(4))
        T0=scalar_stress_4d(grad,2,0)
        T7=scalar_stress_4d(grad,2,7)
        self.assertEqual(null_measurements(T0),null_measurements(T7))
        self.assertNotEqual(T0[0][0],T7[0][0])
        for k,flux in zip(null_directions_4d(),null_measurements(T7)):
            self.assertEqual(flux,2*sum(k[i]*grad[i] for i in range(4))**2)

    def test_common_energy_entropy_scaling_is_undetectable_without_calibration(self):
        self.assertEqual(normalized_thermo_matter_ratio(Q(1),Q(2)),
                         normalized_thermo_matter_ratio(Q(3),Q(6)))
        self.assertNotEqual(normalized_thermo_matter_ratio(Q(1),Q(2)),
                            normalized_thermo_matter_ratio(Q(3),Q(2)))

    def test_jacobson_relation_is_conditional_on_alpha(self):
        self.assertEqual(jacobson_coupling_from_area_entropy(Q(1,4)),1)
        self.assertEqual(jacobson_coupling_from_area_entropy(Q(1,8)),2)
        self.assertRaises(ValueError,jacobson_coupling_from_area_entropy,0)

if __name__=='__main__':
    unittest.main(verbosity=2)
