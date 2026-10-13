"""Independent exact checks of two-chiral-component vacuum Maxwell adaptation."""
import unittest
from itertools import product
from fractions import Fraction as F
from observational_succ.galilean_lorentz_succ import (
    RelativityWitnessError,rational_boost,Mat2,ID
)
from observational_succ.maxwell_transverse_shadow import (
    SWAP,TransverseMaxwellWave,poly_eval,poly_derivative,
    transformed_field_direct,galilean_maxwell_flux,
    galilean_field_mix_obstruction,maxwell_subsystem_demo,
)

class MaxwellShadowTests(unittest.TestCase):
    def test_every_polynomial_chiral_pair_satisfies_full_transverse_pde(self):
        waves=[TransverseMaxwellWave((F(0),F(1)),(F(0),)),
               TransverseMaxwellWave((F(1),F(0),F(-1)),(F(0),F(2),F(0),F(4))),
               TransverseMaxwellWave((F(1,8),F(2),F(3),F(-4),F(5)),(F(2,3),F(-1))) ]
        for w in waves:
            for t,x in product(range(-4,5),repeat=2):
                self.assertEqual(w.residual(t,x),(0,0))

    def test_lorentz_coordinates_and_field_mixing_are_both_required(self):
        wave=TransverseMaxwellWave((F(0),F(0),F(1)),(F(0),F(1),F(-2)))
        for u in (F(-1,2),F(-1,3),F(0),F(1,4),F(1,3),F(2,5)):
            after=wave.lorentz_transform(u)
            for t,x in product((F(-3),F(0),F(2,5),F(1)),repeat=2):
                self.assertEqual(after.field(t,x),transformed_field_direct(wave,u,t,x))
                self.assertEqual(after.residual(t,x),(0,0))

    def test_lorentz_wave_group_representation(self):
        wave=TransverseMaxwellWave((F(3),F(2),F(-1),F(4)),(F(-2),F(1),F(5)))
        for u,w in product((F(-1,4),F(0),F(1,3),F(1,2)),repeat=2):
            a=wave.lorentz_transform(u).lorentz_transform(w)
            merged=(u+w)/(1+u*w)
            self.assertEqual(a,wave.lorentz_transform(merged))
            self.assertEqual(a.lorentz_transform(-merged),wave)

    def test_field_no_go_even_with_pointwise_invertible_mix(self):
        for den in range(2,10):
            for num in range(-den+1,den):
                v=F(num,den)
                r=galilean_field_mix_obstruction(v)
                self.assertEqual(r['trace_obstruction'],-2*v)
                self.assertEqual(r['any_pointwise_invertible_field_mix_repairs'],v==0)
                self.assertEqual(sum(r['source_characteristic_speeds']),-2*v)

    def test_independent_similarity_trace_is_unchanged(self):
        for v in (F(-3,5),F(-1,4),F(0),F(3,5)):
            M=galilean_maxwell_flux(v)
            for R in (Mat2(1,1,0,1),Mat2(2,0,1,3),Mat2(1,2,3,7)):
                conjugated=R @ M @ R.inverse()
                self.assertEqual(conjugated.a+conjugated.d,M.a+M.d)
                if v:self.assertNotEqual(conjugated,SWAP)

    def test_finite_lightlike_field_space_not_ether_ontology(self):
        r=maxwell_subsystem_demo()
        self.assertTrue(r['maxwell_sector_covariance'])
        self.assertEqual(r['velocity'],F(3,5))
        self.assertEqual(r['galilean_principal_trace'],F(-6,5))
        self.assertFalse(r['actual_physical_experiment_attested'])

    def test_exact_polynomial_derivative_against_hand_formula(self):
        self.assertEqual(poly_derivative((F(2),F(-1),F(4),F(3))),
                         (F(-1),F(8),F(9)))
        self.assertEqual(poly_eval((F(2),F(3),F(4)),F(1,2)),F(9,2))

    def test_invalid_wave_source_controls(self):
        with self.assertRaises(RelativityWitnessError):TransverseMaxwellWave((),(0,))
        with self.assertRaises(RelativityWitnessError):TransverseMaxwellWave((F(1),0.1),(F(1),))
        with self.assertRaises(RelativityWitnessError):TransverseMaxwellWave((F(1),),(F(0),)*33)

if __name__=='__main__':unittest.main()
