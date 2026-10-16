"""Exact finite-source tests for reduction of genuine adelic Schwartz Poisson."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    ProfiniteProgram, RationalSpan
)
from observational_succ.finite_adele_localization import FiniteAdeleSpan
from observational_succ.adelic_poisson_reconstruction import (
    AdelicPoissonError, RationalCoset, GaussianPoissonGenerator,
    finite_adele_rational_coset_representative,
    restricted_generators_are_dense_claim,
)


class GenuineSchwartzFiniteCosetTests(unittest.TestCase):
    def test_canonical_rational_coset_no_ghost_coordinate(self):
        for D in (F(1),F(2),F(1,3),F(6,5),F(21,4)):
            for u in (F(0),F(1),F(-1,3),F(13,35),F(-25,17)):
                a=RationalCoset(u,D)
                self.assertEqual(a,RationalCoset(u+D*17,D))
                self.assertEqual(a,RationalCoset(u-D*23,D))
                self.assertEqual(a.additive_haar_volume,1/D)
                self.assertGreaterEqual(a.shift,0)
                self.assertLess(a.shift,D)
                for n in (-11,-1,0,1,6):
                    q=u+D*n
                    r=a.primal_diagonal(q)
                    self.assertTrue(r["within_finite_compact_open_support"])
                    self.assertIsNotNone(r["integer_lattice_label"])
                if D>0:
                    outside=a.primal_diagonal(u+D*F(1,2))
                    self.assertFalse(outside["within_finite_compact_open_support"])

    def test_annihilator_is_inverse_rational_scale_and_paired_source(self):
        rng=random.Random(7761)
        for _ in range(275):
            D=F(rng.randint(1,35),rng.randint(1,30))
            u=F(rng.randint(-35,35),rng.randint(1,25))
            a=RationalCoset(u,D)
            for m in (-7,-1,0,1,3,8):
                freq=F(m)/D
                direct=a.dual_diagonal(freq)
                x=a.dual_source_crosscheck(freq)
                self.assertTrue(direct["dual_within_finite_support"])
                self.assertTrue(x["annihilator_support_crosschecked"])
                self.assertEqual(x["independent_Tate_negative_phase"],
                                 direct["finite_character_phase"])
                self.assertEqual(direct["finite_haar_amplitude"],1/D)
                self.assertEqual(direct["annihilator_lattice_label"],m)
            if D:
                fake=a.dual_diagonal(F(1,2)/D)
                self.assertFalse(fake["dual_within_finite_support"])
                self.assertTrue(a.dual_source_crosscheck(F(1,2)/D)["annihilator_support_crosschecked"])

    def test_canonicalization_does_not_erase_affine_but_preserves_support(self):
        for D in (F(1,2),F(2),F(7,3)):
            a=RationalCoset(F(1,5),D)
            moved=a.affine(F(-3,2),F(7,6))
            expected=RationalCoset(F(-3,2)*a.shift+F(7,6),F(3,2)*D)
            self.assertEqual(moved,expected)
            self.assertEqual(moved.additive_haar_volume,F(2,3)/D)
            with self.assertRaises(AdelicPoissonError):
                a.affine(0,1)

    def test_type_prime_place_and_bad_hypotheses(self):
        for u,D in ((0,0),(0,-1),(F(1,2),0),(0,0.5)):
            with self.assertRaises(AdelicPoissonError):
                RationalCoset(u,D)
        with self.assertRaises(AdelicPoissonError):
            RationalCoset(0,1,"",0)
        with self.assertRaises(AdelicPoissonError):
            RationalCoset(0,1,"actual",-1)
        with self.assertRaises(AdelicPoissonError):
            RationalCoset(0,1).dual_diagonal(1.2)


class GaussianAdelicPoissonControls(unittest.TestCase):
    def test_standard_shifted_theta_source_vs_dual_integer_indices(self):
        rng=random.Random(11041)
        for _ in range(90):
            D=F(rng.randint(1,15),rng.randint(1,13))
            u=F(rng.randint(-20,20),rng.randint(1,15))
            center=F(rng.randint(-13,13),rng.randint(1,13))
            heat=F(rng.randint(1,7),rng.randint(1,8))
            g=GaussianPoissonGenerator(RationalCoset(u,D),center,heat)
            for n,m in ((0,0),(1,1),(-1,-2),(5,-3),(-9,7)):
                receipt=g.source_lattice_receipt(n,m)
                P=receipt["primal"]
                Q=receipt["dual"]
                self.assertEqual(P["Gaussian_exponent_coefficient_of_pi"],
                                 heat*(P["diagonal_source_rational"]-center)**2)
                self.assertEqual(Q["Gaussian_exponent_coefficient_of_pi"],
                                 Q["dual_rational_frequency"]**2/heat)
                self.assertEqual(Q["global_Fourier_phase"],
                                 (center-g.coset.shift)*F(m)/D%1)
                self.assertTrue(receipt["correct_Fourier_normalizations"])
                self.assertFalse(receipt["infinite_sum_equality_proved_by_this_finite_receipt"])

    def test_wrong_Haar_wrong_shift_wrong_sign_mutations(self):
        coset=RationalCoset(F(1,5),F(6,7))
        g=GaussianPoissonGenerator(coset,F(11,10),F(4,9))
        m=1
        q=g.dual_integer(m)
        self.assertEqual(q["finite_haar_amplitude"],F(7,6))
        self.assertNotEqual(q["finite_haar_amplitude"],1)
        self.assertNotEqual(q["global_Fourier_phase"],
                            (g.center+g.coset.shift)*q["dual_rational_frequency"]%1)
        self.assertNotEqual(q["global_Fourier_phase"],
                            g.center*q["dual_rational_frequency"]%1)
        self.assertTrue(g.coset.dual_source_crosscheck(q["dual_rational_frequency"])["annihilator_support_crosschecked"])

    def test_tate_generator_generalization_does_not_use_only_Gaussians(self):
        receipt=restricted_generators_are_dense_claim()
        self.assertEqual(receipt["finite_adelic_indicator_span"],"EXACT_CLASSICAL")
        self.assertEqual(receipt["real_schwartz_factor"],"S(R) FULL, NOT ONLY GAUSSIANS")
        self.assertTrue(receipt["analytic_real_Poisson_import_required"])
        self.assertFalse(receipt["theta_example_alone_proves_general_poisson"])


class FiniteAdeleCosetSufficiencyControls(unittest.TestCase):
    def test_non_rational_original_source_cosets_have_rational_representatives(self):
        rng=random.Random(3345)
        programs=(
            ProfiniteProgram.integer(-19),
            ProfiniteProgram.integer(0),
            ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.projector(3))
        )
        for _ in range(225):
            D=F(rng.randint(1,12),rng.randint(1,12))
            point=FiniteAdeleSpan(rng.choice(programs),rng.randint(1,24))
            rec=finite_adele_rational_coset_representative(point,D)
            self.assertTrue(rec["source_difference_scaled_is_Zhat"])
            self.assertLess(rec["rational_representative"],D)
            self.assertGreaterEqual(rec["rational_representative"],0)
            q=rec["rational_representative"]
            local=RationalCoset(q,D)
            self.assertEqual(local.shift,q)
            self.assertFalse(rec["all_adelic_points_computably_namable"])

    def test_diagonal_rational_source_reduces_to_original_lattice(self):
        for q in (F(-5,6),F(2,3),F(0),F(11,5),F(5)):
            for D in (F(1),F(2),F(1,4),F(5,3)):
                point=FiniteAdeleSpan.diagonal_rational(
                    RationalSpan(q.numerator,q.denominator)
                )
                rec=finite_adele_rational_coset_representative(point,D)
                self.assertEqual(rec["rational_representative"],D*((q/D)%1))

    def test_source_identity_and_epoch_boundary(self):
        point=FiniteAdeleSpan(
            ProfiniteProgram.projector(2,source_id="alpha",epoch=3),6
        )
        receipt=finite_adele_rational_coset_representative(point,F(1,7))
        self.assertEqual(receipt["source_id"],"alpha")
        self.assertEqual(receipt["epoch"],3)
        with self.assertRaises(AdelicPoissonError):
            finite_adele_rational_coset_representative(point,0)

if __name__=="__main__":
    unittest.main()
