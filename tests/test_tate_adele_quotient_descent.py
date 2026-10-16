"""Exact finite-adèle additive strong approximation and real-profinite source quotient."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_adele_quotient_descent import (
    AdeleDescentError,LocalFractionalAdeleCell,FiniteAdeleCoset,
    add_cosets,adele_solenoid_proof_contract,
)


class TateFiniteAdeleStrongApproximationTests(unittest.TestCase):
    def test_all_original_p_fractional_parts_reassembled_by_diagonal_Q(self):
        cases=(
            ((2,1,1),(3,1,2)),
            ((2,2,1),(3,1,1),(5,1,4)),
            ((2,3,5),(7,1,3)),
            ((3,2,7),(5,2,6)),
            ((2,2,2),(5,1,3)),
            ((2,1,0),(3,1,0)),
            (),
        )
        for case in cases:
            cells=tuple(LocalFractionalAdeleCell(*x) for x in case)
            obj=FiniteAdeleCoset(cells)
            rec=obj.check()
            self.assertTrue(rec["all_local_classes_reconstructed"])
            self.assertTrue(rec["adelic_Q_diagonal_discrete"])
            self.assertTrue(rec["adelic_A_mod_Q_compact"])
            self.assertFalse(rec["global_Tate_Poisson_proved"])
            self.assertFalse(rec["RH_proved"])
            self.assertEqual(F(rec["constructive_diagonal_Q_lift"])%1,
                             F(rec["global_discrete_Q_mod_Z_class"]))

    def test_original_q_over_z_is_not_a_chosen_real_phase_guess(self):
        v=FiniteAdeleCoset((
            LocalFractionalAdeleCell(2,1,1),
            LocalFractionalAdeleCell(3,1,2),
        )).check()
        self.assertEqual(v["canonical_local_p_fractions"],("1/2","2/3"))
        self.assertEqual(v["constructive_diagonal_Q_lift"],"7/6")
        self.assertEqual(v["global_discrete_Q_mod_Z_class"],"1/6")
        self.assertEqual(v["finite_prime_place_support"],(2,3))

    def test_refinement_of_p_precision_keeps_the_same_global_quotient(self):
        # The 2-adic class 1/2 has another lawful p^-2 residue 2/4.
        one=FiniteAdeleCoset((LocalFractionalAdeleCell(2,1,1),))
        two=FiniteAdeleCoset((LocalFractionalAdeleCell(2,2,2),))
        self.assertEqual(one.class_mod_integers,two.class_mod_integers)
        self.assertEqual(one.check()["global_discrete_Q_mod_Z_class"],"1/2")
        self.assertEqual(two.check()["global_discrete_Q_mod_Z_class"],"1/2")
        self.assertTrue(one.check()["all_local_classes_reconstructed"])

    def test_group_addition_under_all_prime_local_quantities(self):
        cases=(
            ((2,1,1), (2,1,1)),       # p2 carries 1/2+1/2 -> 0
            ((3,1,1), (3,1,2)),       # p3 carries 1/3+2/3 -> 0
            ((2,2,1), (3,1,2)),       # disjoint actual prime sources
            ((5,2,9), (5,1,3)),       # fractional local p5 carry and reduce
        )
        for a,b in cases:
            x=FiniteAdeleCoset((LocalFractionalAdeleCell(*a),))
            y=FiniteAdeleCoset((LocalFractionalAdeleCell(*b),))
            z=add_cosets(x,y)
            self.assertTrue(z["all_prime_local_additions_match_Q_over_Z"])
            self.assertEqual(F(z["result_Q_over_Z"]),
                             (x.rational_lift+y.rational_lift)%1)
            self.assertFalse(z["RH_proved"])

    def test_finite_adeles_have_true_compact_real_profinite_solenoid_quotient(self):
        r=adele_solenoid_proof_contract()
        self.assertEqual(r["additive_strong_approximation"],"A_f=Q+Zhat")
        self.assertEqual(r["integral_intersection"],"Q_intersect_Zhat=Z")
        self.assertIn("DISCRETE_TOPOLOGY",r["finite_adele_quotient"])
        self.assertTrue(r["adelic_quotient_compact"])
        self.assertTrue(r["adelic_diagonal_Q_discrete"])
        self.assertFalse(r["Archimedean_place_identified_by_pure_finite_inverse_limit"])
        self.assertFalse(r["full_Schwartz_adeles_global_Poisson_established_by_this_code"])
        self.assertFalse(r["RH_proved"])

    def test_fake_prime_and_false_adic_record_are_rejected(self):
        for p,e,a in ((6,1,1),(1,1,0),(4,1,1),(2,0,1),
                      (2,1,2),(3,2,9),(2,9,1),(True,1,1),(2,True,1),
                      (2,1,True)):
            with self.assertRaises(AdeleDescentError):
                LocalFractionalAdeleCell(p,e,a)
        with self.assertRaises(AdeleDescentError):
            FiniteAdeleCoset((LocalFractionalAdeleCell(2,1,1),
                              LocalFractionalAdeleCell(2,2,1)))
        with self.assertRaises(AdeleDescentError):
            add_cosets(None,FiniteAdeleCoset(()))


if __name__=="__main__":
    unittest.main()
