"""Finite adelic principal-part quotient, dual/Tate pairing and nonsplit controls."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.diagonal_adele_zeta import (
    additive_reciprocity, fractional_padic_part, factor_positive
)
from observational_succ.edge_carrier_reconstruction import ProfiniteProgram, RationalSpan
from observational_succ.finite_adele_localization import FiniteAdeleSpan
from observational_succ.pontryagin_source_duality import (
    RationalCircleCharacter, PontryaginSourceError
)
from observational_succ.finite_adelic_character_bridge import (
    finite_principal_parts, finite_adele_phase, finite_tate_character_phase,
    quotient_receipt, quotient_additive_naturality, diagonal_rational_reciprocity,
    character_adele_pairing, annihilator_probe, finite_adelic_extension_non_split,
)


def _diagonal(q,*,source_id="Z-integer-modular-source",epoch=0):
    q=F(q)
    return FiniteAdeleSpan.diagonal_rational(
        RationalSpan(q.numerator,q.denominator),source_id=source_id,epoch=epoch
    )


class FiniteAdeleQuotientTests(unittest.TestCase):
    def test_rational_p_principal_parts_vs_independent_arithmetic(self):
        for q in (F(0),F(1),F(-1),F(1,6),F(5,6),F(-5,42),
                  F(13,60),F(17,121),F(-201,140),F(1,1001)):
            x=_diagonal(q)
            parts=finite_principal_parts(x)
            expected={p:fractional_padic_part(q,p)
                      for p in factor_positive(q.denominator)
                      if fractional_padic_part(q,p)}
            self.assertEqual(parts,expected)
            self.assertEqual(finite_adele_phase(x),q%1)
            self.assertEqual(finite_tate_character_phase(x),(-q)%1)
            self.assertEqual(quotient_receipt(x)["quotient_phase"],q%1)
            self.assertTrue(diagonal_rational_reciprocity(q)["global_diagonal_character_trivial"])
            self.assertTrue(additive_reciprocity(q)["diagonal_character_trivial"])

    def test_actual_nonrational_profinite_source_in_quotient(self):
        e2=ProfiniteProgram.projector(2)
        e3=ProfiniteProgram.projector(3)
        x=FiniteAdeleSpan(e2,6)
        y=FiniteAdeleSpan(e3,6)
        self.assertEqual(finite_principal_parts(x),{2:F(1,2)})
        self.assertEqual(finite_principal_parts(y),{3:F(2,3)})
        self.assertEqual(finite_adele_phase(x),F(1,2))
        self.assertEqual(finite_adele_phase(y),F(2,3))
        self.assertEqual(finite_adele_phase(x.add(y)),F(1,6))
        self.assertEqual(finite_adele_phase(_diagonal(F(1,6))),F(1,6))
        self.assertTrue(quotient_additive_naturality(x,y)["quotient_homomorphism_verified"])
        # Equality in Af/Zhat does not mean the numerator's adelic
        # element itself equals the rational source 1/6.

    def test_quotient_kernel_iff_all_p_integral(self):
        for p in (2,3,5,7):
            e=ProfiniteProgram.projector(p)
            self.assertTrue(quotient_receipt(FiniteAdeleSpan(e))["exact_kernel_agreement"])
            self.assertTrue(quotient_receipt(FiniteAdeleSpan(e))["kernel_by_global_Q_mod_Z_phase"])
            x=FiniteAdeleSpan(e,p)
            r=quotient_receipt(x)
            self.assertFalse(r["kernel_by_local_p_integrality"])
            self.assertFalse(r["kernel_by_global_Q_mod_Z_phase"])
            self.assertEqual(r["exceptional_prime_principal_parts"],((p,F(1,p)),))

    def test_additivity_original_affine_profinite_denominators(self):
        rng=random.Random(95018)
        bases=[
            ProfiniteProgram.integer(-17), ProfiniteProgram.integer(7),
            ProfiniteProgram.projector(2), ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(5),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.projector(3))
        ]
        for _ in range(250):
            x=FiniteAdeleSpan(rng.choice(bases),rng.randint(1,50))
            y=FiniteAdeleSpan(rng.choice(bases),rng.randint(1,50))
            r=quotient_additive_naturality(x,y)
            self.assertTrue(r["quotient_homomorphism_verified"])
            self.assertEqual(r["phase_of_sum"],r["sum_of_phases"])

    def test_wrong_sign_real_plus_and_finite_plus_not_global(self):
        q=F(1,6)
        r=diagonal_rational_reciprocity(q)
        self.assertEqual((r["real_positive_phase"]+
                          r["finite_negative_Tate_phase"])%1,0)
        self.assertNotEqual((r["real_positive_phase"]+
                             r["finite_positive_phase"])%1,0)
        self.assertEqual(r["finite_positive_phase"],F(1,6))

    def test_source_mismatch_float_and_resource_budget(self):
        a=_diagonal(F(1,6),source_id="a",epoch=1)
        b=_diagonal(F(1,6),source_id="b",epoch=1)
        with self.assertRaises(PontryaginSourceError):
            quotient_additive_naturality(a,b)
        with self.assertRaises(PontryaginSourceError):
            finite_principal_parts(_diagonal(F(1,2000001)))
        with self.assertRaises(PontryaginSourceError):
            diagonal_rational_reciprocity(0.5)


class CrossCarrierCharacterTests(unittest.TestCase):
    def test_pontryagin_tate_intertwining_on_independent_source_programs(self):
        rng=random.Random(10686)
        programs=[
            ProfiniteProgram.integer(-21), ProfiniteProgram.integer(0),
            ProfiniteProgram.integer(91), ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3), ProfiniteProgram.projector(5),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.integer(7)),
            ProfiniteProgram.projector(2).multiply(ProfiniteProgram.projector(3)),
        ]
        for _ in range(350):
            n=rng.randint(1,105)
            a=rng.randint(-200,200)
            z=rng.choice(programs)
            char=RationalCircleCharacter(F(a,n))
            receipt=character_adele_pairing(char,z)
            self.assertTrue(receipt["dual_Tate_square_commutes"])
            self.assertEqual(receipt["character_phase"],char.evaluate(z))
            self.assertEqual((receipt["finite_Tate_negative_phase"]+
                              receipt["character_phase"])%1,0)
            self.assertFalse(receipt["global_topological_duality_verified_by_finite_test"])

    def test_p_primary_character_detects_projector_locations(self):
        z2=ProfiniteProgram.projector(2)
        z3=ProfiniteProgram.projector(3)
        c2=RationalCircleCharacter(F(1,2))
        c3=RationalCircleCharacter(F(1,3))
        self.assertEqual(c2.evaluate(z2),F(1,2))
        self.assertEqual(c2.evaluate(z3),0)
        self.assertEqual(c3.evaluate(z2),0)
        self.assertEqual(c3.evaluate(z3),F(1,3))
        self.assertEqual(character_adele_pairing(c2,z2)["character_phase"],F(1,2))

    def test_source_epoch_forgery_rejected(self):
        x=ProfiniteProgram.integer(3,source_id="actual",epoch=2)
        for name,epoch in (("actual",3),("forged",2)):
            with self.assertRaises(PontryaginSourceError):
                character_adele_pairing(RationalCircleCharacter(F(1,7),name,epoch),x)

    def test_annihilator_separating_actual_prime_projector(self):
        for p in (2,3,5,7,11):
            e=ProfiniteProgram.projector(p)
            integral=annihilator_probe(FiniteAdeleSpan(e))
            self.assertTrue(integral["lies_in_Zhat"])
            self.assertTrue(integral["annihilates_Zhat"])
            nonintegral=annihilator_probe(FiniteAdeleSpan(e,p))
            self.assertFalse(nonintegral["lies_in_Zhat"])
            self.assertFalse(nonintegral["annihilates_Zhat"])
            self.assertEqual(nonintegral["separating_prime"],p)
            self.assertNotEqual(nonintegral["separating_Tate_phase"],0)

    def test_nonsplit_extension_is_not_set_theoretic_obstruction(self):
        for n in (2,3,4,5,6,7,9,10,12,15,20,101):
            r=finite_adelic_extension_non_split(n)
            self.assertEqual(r["torsion_order"],n)
            self.assertTrue(r["n_times_lift_is_Zhat_nonzero"])
            self.assertEqual(r["n_times_lift_phase"],0)
            self.assertFalse(r["exact_sequence_splits_as_groups"])
            self.assertFalse(r["a_set_theoretic_section_is_forbidden"])
            self.assertFalse(r["full_theorem_proved_by_one_example"])


if __name__=="__main__":
    unittest.main()
