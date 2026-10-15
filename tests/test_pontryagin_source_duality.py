"""Independent exact probes for dual(Zhat) = Q/Z.

The full Pontryagin/topological theorem is proved in the paper and attributed
to classical sources. These tests exercise *specific finite source charts*
with exact Fraction/CyclotomicElement arithmetic and hostile mutations.
"""
import random
import unittest
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    ProfiniteProgram, finite_clock_collision
)
from observational_succ.pontryagin_source_duality import (
    FiniteCyclicCharacter, RationalCircleCharacter, PontryaginSourceError,
    phase_separation, finite_character_orthogonality, wrong_dual_arrow_witness,
)


class FiniteCharacters(unittest.TestCase):
    def test_cyclic_source_character_group_has_exactly_n_distinct_labels(self):
        for n in range(1,25):
            spectra=set()
            for k in range(n):
                c=FiniteCyclicCharacter(n,k)
                signature=tuple(c.phase(x) for x in range(n))
                spectra.add(signature)
                self.assertEqual(c.rational_frequency,F(k,n)%1)
                self.assertEqual(c.phase(n+x if n else x),c.phase(x))
            self.assertEqual(len(spectra),n)

    def test_dual_arrows_natural_on_nested_reduction(self):
        for n in range(1,17):
            for factor in (1,2,3,4,5):
                m=n*factor
                for label in (-17,-1,0,1,5,n+1):
                    c=FiniteCyclicCharacter(n,label)
                    higher=c.lift(m)
                    self.assertEqual(higher.label,(label%n*factor)%m)
                    for x in (-m-3,-1,0,1,7,m-1,m+2):
                        r=c.naturality(x,m)
                        self.assertEqual(r["phase_small"],r["phase_large"])
                    self.assertEqual(higher.rational_frequency,c.rational_frequency)

    def test_wrong_dual_direction_and_source_type(self):
        r=wrong_dual_arrow_witness()
        self.assertTrue(r["bad_dual_arrow_refuted"])
        self.assertNotEqual(r["mutant_phase"],r["correct_phase"])
        with self.assertRaises(PontryaginSourceError):
            FiniteCyclicCharacter(3,1).lift(5)
        for bad in (True,0,-5,2.0):
            with self.assertRaises(PontryaginSourceError):
                FiniteCyclicCharacter(bad,1)
        with self.assertRaises(PontryaginSourceError):
            FiniteCyclicCharacter(3,1.5)
        with self.assertRaises(PontryaginSourceError):
            FiniteCyclicCharacter(3,1,source_id="")

    def test_independent_exact_cyclotomic_orthogonality(self):
        for n in range(1,22):
            for a in range(-2,2*n+2):
                r=finite_character_orthogonality(n,a)
                self.assertTrue(r["finite_character_orthogonality_exact"])
                self.assertEqual(r["expected_zero"], a%n != 0)
                self.assertFalse(r["general_duality_from_finite_samples"])
        self.assertEqual(FiniteCyclicCharacter(6,1).phase(1),F(1,6))
        # Composite six is a LEGITIMATE finite cyclic modulus, not a
        # fake prime place in an Euler product.


class PontryaginInfiniteSourceCharts(unittest.TestCase):
    def test_normalized_rational_classes_and_group_law(self):
        for q in (F(0),F(1,6),F(-1,6),F(13,30),F(-201,70),F(1)):
            a=RationalCircleCharacter(q)
            self.assertEqual(a.frequency,q%1)
            self.assertEqual(a.add(a.neg()).frequency,0)
            self.assertEqual(a.add(RationalCircleCharacter(1)).frequency,a.frequency)
            self.assertEqual(a.multiply_integer(6).frequency,(6*q)%1)
        self.assertEqual(RationalCircleCharacter(F(2,6)),
                         RationalCircleCharacter(F(1,3)))
        with self.assertRaises(PontryaginSourceError):
            RationalCircleCharacter(0.5)

    def test_evaluate_against_independent_integer_modular_oracle(self):
        rng=random.Random(70351)
        for _ in range(400):
            n=rng.randint(1,100)
            a=rng.randint(-200,200)
            k=rng.randint(-1000,1000)
            x=ProfiniteProgram.integer(k)
            ch=RationalCircleCharacter(F(a,n))
            phase=ch.evaluate(x)
            self.assertEqual(phase,F(a*k,n)%1)
            modulus=ch.frequency.denominator * rng.choice((1,2,3))
            r=ch.evaluate_via_refinement(x,modulus)
            self.assertTrue(r["character_gluing_verified"])

    def test_prime_projector_and_mutated_source_actions(self):
        rng=random.Random(4441)
        for p in (2,3,5,7,11):
            x=ProfiniteProgram.projector(p)
            y=x.add(ProfiniteProgram.integer(11))
            for _ in range(45):
                n=rng.randint(1,80)
                a=rng.randint(-30,30)
                c=RationalCircleCharacter(F(a,n))
                self.assertEqual(c.evaluate(x),F(c.frequency.numerator*x.residue(c.frequency.denominator),
                                                   c.frequency.denominator)%1)
                translation=c.dual_SUCC_translation(x,rng.randint(-100,100))
                multiplication=c.dual_FUCC_multiplication(y,rng.randint(-25,25))
                self.assertTrue(translation["translation_covariance"])
                self.assertTrue(multiplication["dual_multiplication_covariance"])

    def test_bidual_phase_recovers_every_chosen_finite_clock(self):
        sources=[
            ProfiniteProgram.integer(-123),
            ProfiniteProgram.integer(1),
            ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.integer(17)),
        ]
        for x in sources:
            for n in range(1,160):
                receipt=phase_separation(x,n)
                self.assertEqual(receipt["recovered_residue"],x.residue(n))
                self.assertTrue(receipt["stage_separation_proved"])

    def test_no_uniform_finite_horizon_identifies_z_integer_source(self):
        for H in (2,4,8,12,16):
            pair=finite_clock_collision(H)
            zero,alias=pair["distinct_source_integers"]
            left=ProfiniteProgram.integer(zero)
            right=ProfiniteProgram.integer(alias)
            for n in range(1,H+1):
                ch=RationalCircleCharacter(F(1,n))
                self.assertEqual(ch.evaluate(left),ch.evaluate(right))
            ch=RationalCircleCharacter(F(1,alias+1))
            self.assertNotEqual(ch.evaluate(left),ch.evaluate(right))
        # The full collection of character labels remains separating;
        # that does not impose a uniform finite experimental deadline.

    def test_source_namespace_epoch_and_conductor_negative_controls(self):
        x=ProfiniteProgram.integer(7,source_id="old",epoch=3)
        c=RationalCircleCharacter(F(2,5),"old",3)
        self.assertEqual(c.evaluate(x),F(4,5))
        with self.assertRaises(PontryaginSourceError):
            RationalCircleCharacter(F(2,5),"forged",3).evaluate(x)
        with self.assertRaises(PontryaginSourceError):
            RationalCircleCharacter(F(2,5),"old",4).evaluate(x)
        with self.assertRaises(PontryaginSourceError):
            c.on_finite_clock(7)
        with self.assertRaises(PontryaginSourceError):
            c.evaluate_via_refinement(x,7)
        with self.assertRaises(PontryaginSourceError):
            c.add(RationalCircleCharacter(F(2,5),"other",3))


if __name__=="__main__":
    unittest.main()
