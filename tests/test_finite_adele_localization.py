"""Independent exact tests: Zhat localizations and bona fide finite-adele carrier."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    EdgeCarrierError, ProfiniteProgram, RationalSpan,
)
from observational_succ.finite_adele_localization import (
    FiniteAdeleSpan, RationalArchimedeanAdeleChart,
    local_idempotent_is_a_nonrational_adele,
    finite_adele_nonfield_control,
)


class FiniteAdeleCarrierTests(unittest.TestCase):
    def test_rational_diagonal_is_ring_homomorphism_on_all_probes(self):
        rng=random.Random(4342)
        for _ in range(125):
            a=RationalSpan(rng.randint(-25,25),rng.randint(1,20))
            b=RationalSpan(rng.randint(-25,25),rng.randint(1,20))
            x=FiniteAdeleSpan.diagonal_rational(a)
            y=FiniteAdeleSpan.diagonal_rational(b)
            plus=x.add(y)
            times=x.multiply(y)
            oracle_plus=FiniteAdeleSpan.diagonal_rational(a.add(b))
            oracle_times=FiniteAdeleSpan.diagonal_rational(a.multiply(b))
            for modulus in (2,3,4,5,6,8,9,10,12,15,30,64,97):
                self.assertTrue(plus.cross_relation_at(oracle_plus,modulus)["agrees_at_this_probe"])
                self.assertTrue(times.cross_relation_at(oracle_times,modulus)["agrees_at_this_probe"])

    def test_Qp_local_scaled_residues_genuine_invertible_unit(self):
        x=FiniteAdeleSpan.diagonal_rational(RationalSpan(7,18))
        for p in (2,3,5,7):
            for k in (1,2,3):
                r=x.local_integral_scaled(p,k)
                d=18
                v=0
                while d%p==0:
                    d//=p
                    v+=1
                self.assertEqual(r["denominator_p_order"],v)
                self.assertEqual(r["residue_of_p_to_v_times_x"],
                                 (7*pow(d,-1,p**k))%(p**k))
                self.assertFalse(r["exact_qp_element_computed"])
        self.assertEqual(x.local_integral_scaled(2,4)["declared_scale_exponent"],-1)
        self.assertEqual(x.local_integral_scaled(3,4)["declared_scale_exponent"],-2)

    def test_CRT_idempotent_is_a_non_rational_adele(self):
        for p in (2,3,5,7,11):
            r=local_idempotent_is_a_nonrational_adele(p)
            self.assertFalse(r["is_diagonal_rational"])
            self.assertTrue(r["lies_in_Zhat"])
            self.assertTrue(r["lies_in_finite_adeles"])
            self.assertEqual(r["at_p"]["residue_of_p_to_v_times_x"],1)
            self.assertEqual(r["at_q"]["residue_of_p_to_v_times_x"],0)

    def test_ring_has_nontrivial_zero_divisors_not_a_field(self):
        for p,q in ((2,3),(3,2),(5,7)):
            r=finite_adele_nonfield_control(p,q)
            self.assertTrue(r["left_nonzero"])
            self.assertTrue(r["right_nonzero"])
            self.assertFalse(r["finite_adeles_are_a_field"])
        with self.assertRaises(EdgeCarrierError):
            finite_adele_nonfield_control(2,2)
        with self.assertRaises(EdgeCarrierError):
            finite_adele_nonfield_control(4,3)

    def test_localized_non_integer_adelic_coordinates(self):
        point=FiniteAdeleSpan(ProfiniteProgram.projector(2),2)
        for k in (1,2,3,4,5):
            a=point.local_integral_scaled(2,k)
            b=point.local_integral_scaled(3,k)
            self.assertEqual(a["declared_scale_exponent"],-1)
            self.assertEqual(a["residue_of_p_to_v_times_x"],1)
            self.assertEqual(b["declared_scale_exponent"],0)
            self.assertEqual(b["residue_of_p_to_v_times_x"],0)
        self.assertTrue(point.multiply(point).numerator.bonding(18,6)["ring_bonding_compatible"])

    def test_finite_local_equality_is_not_global_equality(self):
        # Two distinct authentic diagonal Q points agree modulo all
        # bounded finite probes; localization equality is stricter.
        from math import lcm
        L=1
        for k in range(1,13):
            L=lcm(L,k)
        zero=FiniteAdeleSpan.diagonal_rational(RationalSpan(0))
        alias=FiniteAdeleSpan.diagonal_rational(RationalSpan(L))
        for m in range(1,13):
            r=zero.cross_relation_at(alias,m)
            self.assertTrue(r["agrees_at_this_probe"])
            self.assertFalse(r["global_fraction_equality_from_one_probe"])
        self.assertFalse(zero.cross_relation_at(alias,L+1)["agrees_at_this_probe"])

    def test_product_rules_and_denominator_normalization(self):
        a=FiniteAdeleSpan(ProfiniteProgram.projector(2),3)
        b=FiniteAdeleSpan(ProfiniteProgram.projector(3),5)
        s=a.add(b)
        self.assertEqual(s.denominator,15)
        for n in range(1,100):
            r=(5*a.numerator.residue(n)+3*b.numerator.residue(n))%n
            self.assertEqual(s.numerator.residue(n),r)
            self.assertEqual(a.multiply(b).numerator.residue(n),0)

    def test_archimedean_chart_is_only_Q_dense_submodel_of_R(self):
        a=RationalArchimedeanAdeleChart.diagonal_rational(RationalSpan(2,3))
        b=RationalArchimedeanAdeleChart.diagonal_rational(RationalSpan(-7,15))
        self.assertEqual(a.real,F(2,3))
        self.assertEqual(a.add(b).real,F(1,5))
        self.assertEqual(a.multiply(b).real,F(-14,45))
        for modulus in (2,5,10,15):
            correct=FiniteAdeleSpan.diagonal_rational(RationalSpan(1,5))
            self.assertTrue(a.add(b).finite.cross_relation_at(correct,modulus)["agrees_at_this_probe"])
        with self.assertRaises(EdgeCarrierError):
            RationalArchimedeanAdeleChart(0.5,a.finite)

    def test_source_epoch_and_invalid_local_probes_rejected(self):
        a=FiniteAdeleSpan(ProfiniteProgram.integer(1,source_id="a",epoch=0))
        b=FiniteAdeleSpan(ProfiniteProgram.integer(1,source_id="b",epoch=0))
        with self.assertRaises(EdgeCarrierError):
            a.add(b)
        with self.assertRaises(EdgeCarrierError):
            FiniteAdeleSpan(ProfiniteProgram.integer(1),0)
        with self.assertRaises(EdgeCarrierError):
            FiniteAdeleSpan(ProfiniteProgram.integer(1),True)
        for p,k in ((4,2),(2,0),(2,31),(True,1)):
            with self.assertRaises(EdgeCarrierError):
                a.local_integral_scaled(p,k)


if __name__ == "__main__":
    unittest.main()
