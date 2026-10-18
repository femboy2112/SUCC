"""Exact homotopy-defect source trace: arbitrary prime orientation pivots."""
import unittest
from fractions import Fraction as F

from observational_succ.source_homotopy_defect import (
    HomotopyDefectError, homotopy_defect_trace, grade_zero_defect,
    pivot_invariance, signed_prime_distribution_receipt,
)
from observational_succ.koszul_prime_cancellation import source_multidegree
from observational_succ.completed_weil_transport import von_mangoldt_labels


class SourceHomotopyDefectTests(unittest.TestCase):
    def test_grade_zero_defect_is_unity_for_every_actual_nonunit_integer(self):
        for n in range(2,151):
            r=grade_zero_defect(n)
            self.assertEqual(r["ordinary_source_supertrace"],1)
            self.assertEqual(r["homotopy_defect_supertrace"],1)
            self.assertTrue(r["exact_graded_cyclicity"])
            self.assertFalse(r["source_T_commutes_with_d"])
            self.assertFalse(r["Weil_PSD_proved"])
        unit=grade_zero_defect(1)
        self.assertEqual(unit["ordinary_source_supertrace"],1)
        self.assertEqual(unit["homotopy_defect_supertrace"],0)
        self.assertEqual(unit["homology_contact_at_unit"],1)

    def test_genuine_arbitrary_orientation_pivot_does_not_change_trace(self):
        for n in (6,12,15,30,36,42,60,90,210):
            r=pivot_invariance(n)
            self.assertTrue(r["distinct_homotopies_give_same_source_trace"])
            self.assertEqual(r["observable_prime_defect"],1)
            self.assertTrue(r["contractible_auxiliary_trace_redundant"])
            c=source_multidegree(n)
            self.assertEqual(r["pivots"],c.active)
            if len(c.active)>1:
                a,b=c.active[:2]
                self.assertNotEqual(c.exterior_creation(a,()),c.exterior_creation(b,()))
                self.assertEqual(grade_zero_defect(n,a)["homotopy_defect_supertrace"],
                                 grade_zero_defect(n,b)["homotopy_defect_supertrace"])

    def test_independent_general_diagonal_trace_identity_including_negative_tests(self):
        for n in (2,4,6,8,12,30,36,210):
            f=source_multidegree(n)
            basis=f.basis()
            for pivot in f.active:
                probes=(
                    {S:F(1) for S in basis},
                    {S:F(3*len(S)-2) for S in basis},
                    {S:F(-5) if len(S)%2==0 else F(7,3) for S in basis},
                    {S:F(0) if S else F(11,5) for S in basis},
                )
                for diag in probes:
                    expected=sum(((-1)**len(S))*v for S,v in diag.items())
                    actual=homotopy_defect_trace(n,diag,pivot)
                    self.assertEqual(actual["ordinary_source_supertrace"],expected)
                    self.assertEqual(actual["homotopy_defect_supertrace"],expected)

    def test_chain_compatible_scalar_probes_still_have_zero_supertrace(self):
        for n in (2,3,4,6,8,9,30):
            fiber=source_multidegree(n)
            for p in fiber.active:
                diag=dict.fromkeys(fiber.basis(),F(17,4))
                r=homotopy_defect_trace(n,diag,p)
                self.assertTrue(r["source_T_commutes_with_d"])
                self.assertEqual(r["ordinary_source_supertrace"],0)
                self.assertEqual(r["homotopy_defect_supertrace"],0)

    def test_finite_signed_weil_prime_side_matches_entire_original_tape(self):
        N=75
        source=dict(von_mangoldt_labels(N))
        values={n:(F(1),F(-2)) for n in source}
        values.update({6:(F(100),F(100)),12:(F(77),F(-33)),
                       1:(F(9),F(9))})
        r=signed_prime_distribution_receipt(N,values)
        self.assertEqual(r["original_Tate_prime_power_tape"],von_mangoldt_labels(N))
        self.assertEqual(len(r["prime_terms"]),len(source))
        self.assertEqual(r["ignored_nonprimepower_log_probe_labels"],(1,6,12))
        self.assertTrue(r["no_composite6_source_term"])
        self.assertTrue(r["exact_finite_signed_prime_distribution_only"])
        for term in r["prime_terms"]:
            n,p=term["original_prime_power"],term["primitive_prime"]
            self.assertEqual(source[n],p)
            self.assertEqual(term["signed_source_test_multiplier"],F(1))
            self.assertEqual(term["half_density_amplitude_squared"],F(1,n))
            self.assertTrue(term["homotopy_pivot_independent"])
            self.assertFalse(term["contact_Gamma_or_pole_included"])
        self.assertFalse(r["completed_Weil_PSD_proved"])

    def test_independent_second_original_weil_primepower_oracle(self):
        from observational_succ.source_weil_hierarchy import real_prime_power
        for N in (9,30,75,140):
            tape=dict(von_mangoldt_labels(N))
            second={n:real_prime_power(n) for n in range(2,N+1)
                    if real_prime_power(n) is not None}
            self.assertEqual(tape,second)
            self.assertNotIn(6,tape)
            self.assertEqual(tape[4],2)
            if N>=30:
                self.assertEqual(tape[27],3)

    def test_source_even_prime_square_not_accidentally_deleted(self):
        r=signed_prime_distribution_receipt(40,{
            2:(F(1),F(0)),4:(F(2),F(3)),8:(F(3),F(-1)),
            9:(F(1),F(1)),6:(F(111),F(111))
        })
        items={x["original_prime_power"]:x for x in r["prime_terms"]}
        self.assertEqual(items[4]["primitive_prime"],2)
        self.assertEqual(items[4]["half_density_amplitude_squared"],F(1,4))
        self.assertEqual(items[4]["signed_source_test_multiplier"],F(-5))
        self.assertIn("log(2)/sqrt(4)",items[4]["symbolic_complete_weight"])
        self.assertIn(9,items)
        self.assertNotIn(6,items)
        self.assertIn(6,r["ignored_nonprimepower_log_probe_labels"])

    def test_minus_first_orientation_gauge_cancels_in_defect_trace(self):
        # Under J=(-1)^degree, d -> -d and h -> -h;
        # [T,-d](-h)=[T,d]h for even T. Compare actual source readings.
        for n in (2,6,12,30):
            r=grade_zero_defect(n)
            self.assertEqual(r["homotopy_defect_supertrace"],r["ordinary_source_supertrace"])
            self.assertTrue(r["orientation_auxiliary_removed"])

    def test_source_contract_rejects_float_fake_pivot_and_partial_oracles(self):
        for n in (2,6,30):
            fiber=source_multidegree(n)
            diag={s:F(1) for s in fiber.basis()}
            for p in (0,1,6,True,F(2),100003):
                with self.assertRaises(HomotopyDefectError):
                    homotopy_defect_trace(n,diag,p)
        with self.assertRaises(HomotopyDefectError):
            homotopy_defect_trace(1,{():1},2)
        with self.assertRaises(HomotopyDefectError):
            homotopy_defect_trace(6,{():1},2)
        with self.assertRaises(HomotopyDefectError):
            signed_prime_distribution_receipt(10,{4:(1.0,2)})
        with self.assertRaises(HomotopyDefectError):
            signed_prime_distribution_receipt(10,{12:(1,2)})
        with self.assertRaises(HomotopyDefectError):
            signed_prime_distribution_receipt(10,[(2,(1,1))])


if __name__=="__main__":
    unittest.main()
