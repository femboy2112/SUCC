"""Exact global A_Q/Q solenoid character/gauge and source witnesses."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    ProfiniteProgram, RationalSpan
)
from observational_succ.finite_adele_localization import FiniteAdeleSpan
from observational_succ.pontryagin_source_duality import PontryaginSourceError
from observational_succ.adelic_solenoid_duality import (
    RationalSolenoidChart, quotient_adele_representative,
    adelic_solenoid_abstract_duality_receipt
)


class RationalSolenoidTests(unittest.TestCase):
    def test_diagonal_integer_gauge_and_canonical_chart(self):
        rng=random.Random(5603)
        sources=(
            ProfiniteProgram.integer(0),
            ProfiniteProgram.integer(-17),
            ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.integer(9))
        )
        for _ in range(140):
            z=rng.choice(sources)
            real=F(rng.randint(-40,40),rng.randint(1,35))
            x=RationalSolenoidChart(real,z)
            y=x.canonical()
            self.assertGreaterEqual(y.real,0)
            self.assertLess(y.real,1)
            self.assertEqual(y,y.canonical())
            for k in (-25,-3,-1,0,1,5,12):
                shifted=x.diagonal_integer_shift(k)
                for q in (F(0),F(1),F(1,2),F(1,3),F(-5,6),F(17,35)):
                    t=shifted.character(q)
                    self.assertEqual(t["global_Tate_character_phase"],
                                     x.character(q)["global_Tate_character_phase"])
                    self.assertTrue(x.gauge_character_naturality(q,k)["global_quotient_naturality"])
                    self.assertEqual(t["source_id"],z.source_id)

    def test_global_dual_includes_all_rational_labels_not_only_integers(self):
        z=ProfiniteProgram.projector(2)
        x=RationalSolenoidChart(F(0),z)
        self.assertEqual(x.character(F(1))["global_Tate_character_phase"],0)
        self.assertEqual(x.character(F(1,2))["global_Tate_character_phase"],F(1,2))
        self.assertEqual(x.character(F(1,3))["global_Tate_character_phase"],0)
        y=RationalSolenoidChart(F(1,5),ProfiniteProgram.integer(0))
        self.assertEqual(y.character(F(1))["global_Tate_character_phase"],F(1,5))
        self.assertEqual(y.character(F(5))["global_Tate_character_phase"],0)
        # Only integer characters see real coordinate mod1, not all
        # independent profinite directions.

    def test_actual_global_source_three_way_tate_atlas_sign_and_extra_places(self):
        rng=random.Random(29017)
        xs=(
            ProfiniteProgram.integer(0),
            ProfiniteProgram.integer(11),
            ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(5).add(ProfiniteProgram.integer(-7))
        )
        for _ in range(190):
            x=RationalSolenoidChart(
                F(rng.randint(-30,30),rng.randint(1,29)),
                rng.choice(xs)
            )
            q=F(rng.randint(-30,30),rng.randint(1,45))
            a=x.crosscheck_tate_S_atlas(q)
            b=x.crosscheck_tate_S_atlas(q,extra_primes=(2,3,5,7))
            self.assertTrue(a["three_way_exact_agreement"])
            self.assertTrue(b["three_way_exact_agreement"])
            self.assertEqual(a["original_character_phase"],b["original_character_phase"])
            self.assertTrue(b["classical_Tate_refinement_square"])

    def test_per_target_finite_separation_with_actual_source_witness(self):
        samples=[
            RationalSolenoidChart(F(1,4),ProfiniteProgram.integer(0)),
            RationalSolenoidChart(F(-7,5),ProfiniteProgram.integer(11)),
            RationalSolenoidChart(F(0),ProfiniteProgram.projector(2)),
            RationalSolenoidChart(F(0),ProfiniteProgram.projector(3))
        ]
        witnesses=(None,None,2,3)
        for sample,modulus in zip(samples,witnesses):
            r=sample.exact_nonzero_witness(modulus)
            self.assertTrue(r["certified_distinct_from_zero_in_quotient"])
            self.assertNotEqual(r["nontrivial_phase"],0)
            self.assertFalse(r["all_profinite_points_zero_decidable"])
        with self.assertRaises(PontryaginSourceError):
            RationalSolenoidChart(0,ProfiniteProgram.projector(3)).exact_nonzero_witness(2)
        with self.assertRaises(PontryaginSourceError):
            RationalSolenoidChart(0,ProfiniteProgram.integer(0)).exact_nonzero_witness(7)

    def test_residue_probe_equality_is_not_global_source_equivalence(self):
        from math import lcm
        L=1
        for n in range(1,14):
            L=lcm(L,n)
        zero=RationalSolenoidChart(0,ProfiniteProgram.integer(0))
        hidden=RationalSolenoidChart(0,ProfiniteProgram.integer(L))
        for n in range(1,14):
            self.assertTrue(zero.equal_on_probe(hidden,n))
        self.assertFalse(zero.equal_on_probe(hidden,L+1))

    def test_source_identity_and_invalid_probe_firewalls(self):
        x=RationalSolenoidChart(F(1,2),ProfiniteProgram.integer(1,source_id="x",epoch=5))
        y=RationalSolenoidChart(F(1,2),ProfiniteProgram.integer(1,source_id="other",epoch=5))
        with self.assertRaises(PontryaginSourceError):
            x.equal_on_probe(y,2)
        with self.assertRaises(PontryaginSourceError):
            x.equal_on_probe(x,0)
        with self.assertRaises(PontryaginSourceError):
            x.character(0.5)
        with self.assertRaises(PontryaginSourceError):
            x.diagonal_integer_shift(F(1,2))
        with self.assertRaises(PontryaginSourceError):
            RationalSolenoidChart(0.5,ProfiniteProgram.integer(0))


class QuotientAdeleSourceTests(unittest.TestCase):
    def test_original_rational_finite_adele_to_solenoid_canonical_lift(self):
        for real in (F(0),F(1,5),F(-7,3),F(11)):
            for q in (F(0),F(1,6),F(-3,10),F(7,2),F(-1)):
                point=FiniteAdeleSpan.diagonal_rational(
                    RationalSpan(q.numerator,q.denominator))
                recovered=quotient_adele_representative(real,point)
                self.assertEqual(recovered["principal_part"],q%1)
                self.assertEqual(recovered["solenoid_real"],real-q%1)
                self.assertTrue(recovered["finite_component_integral"])
                self.assertFalse(recovered["every_integral_finite_adele_computably_resolved"])

    def test_nonrational_finite_adele_can_be_lifted_to_integral_fiber(self):
        sources=(
            ProfiniteProgram.projector(2),
            ProfiniteProgram.projector(3),
            ProfiniteProgram.projector(2).add(ProfiniteProgram.projector(3)),
        )
        for source in sources:
            for d in (2,3,6,12,18):
                point=FiniteAdeleSpan(source,d)
                r=quotient_adele_representative(F(1,3),point)
                self.assertTrue(r["finite_component_integral"])
                self.assertEqual(r["integral_finite_adele_source"].denominator>0,True)

    def test_abstract_topological_contract_keeps_unproved_gates(self):
        r=adelic_solenoid_abstract_duality_receipt()
        self.assertEqual(r["completed_global_dual"],"Q with discrete topology")
        self.assertEqual(r["diagonal_Q_annihilator"],"Q")
        self.assertFalse(r["inferred_from_samples"])
        self.assertFalse(r["RH_proved"])


if __name__=="__main__":
    unittest.main()
