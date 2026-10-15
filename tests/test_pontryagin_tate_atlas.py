"""Three independent interfaces for SUCC profinite Pontryagin characters."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import ProfiniteProgram
from observational_succ.pontryagin_source_duality import (
    RationalCircleCharacter, PontryaginSourceError
)
from observational_succ.pontryagin_tate_atlas import three_way_tate_duality


class TateCrossAtlasTests(unittest.TestCase):
    def test_rational_and_prime_projector_original_sources(self):
        sources=(
            ProfiniteProgram.integer(0),ProfiniteProgram.integer(7),
            ProfiniteProgram.integer(-13),ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),ProfiniteProgram.projector(5),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.projector(3)),
        )
        for d in (1,2,3,4,6,8,9,10,12,15,18,20,24,30,36):
            for a in (-19,-1,0,1,5,13):
                c=RationalCircleCharacter(F(a,d))
                for x in sources:
                    r=three_way_tate_duality(c,x,extra_primes=(5,7,11))
                    self.assertTrue(r["three_way_compatibility"])
                    self.assertTrue(r["Tate_projection_commutes"])
                    self.assertEqual(r["direct_modular_phase"],
                                     r["finite_adelic_principal_phase"])
                    self.assertEqual((r["direct_modular_phase"]+
                                      r["Tate_finite_negative_phase"])%1,0)
                    self.assertFalse(r["full_topological_duality_proved_by_finite_check"])

    def test_extra_local_places_cannot_change_a_declared_frequency(self):
        rng=random.Random(18102)
        for _ in range(250):
            d=rng.randint(1,120)
            a=rng.randint(-500,500)
            z=ProfiniteProgram.integer(rng.randint(-1000,1000))
            c=RationalCircleCharacter(F(a,d))
            minimal=three_way_tate_duality(c,z)
            extended=three_way_tate_duality(c,z,extra_primes=(2,3,5,7,11))
            self.assertEqual(minimal["direct_modular_phase"],
                             extended["direct_modular_phase"])
            self.assertEqual(minimal["Tate_finite_negative_phase"],
                             extended["Tate_finite_negative_phase"])

    def test_wrong_sign_and_forged_place_rejected(self):
        z=ProfiniteProgram.integer(1)
        c=RationalCircleCharacter(F(1,3))
        r=three_way_tate_duality(c,z,extra_primes=(2,))
        self.assertEqual(r["direct_modular_phase"],F(1,3))
        self.assertEqual(r["Tate_finite_negative_phase"],F(2,3))
        self.assertNotEqual(r["direct_modular_phase"],
                            r["Tate_finite_negative_phase"])
        with self.assertRaises(PontryaginSourceError):
            three_way_tate_duality(c,z,extra_primes=(6,))
        with self.assertRaises(PontryaginSourceError):
            three_way_tate_duality(c,z,extra_primes=(2,2))
        with self.assertRaises(PontryaginSourceError):
            three_way_tate_duality(c,z,extra_primes=[2])
        with self.assertRaises(PontryaginSourceError):
            three_way_tate_duality(
                RationalCircleCharacter(F(1,3),"not-source"),z
            )


if __name__=="__main__":
    unittest.main()
