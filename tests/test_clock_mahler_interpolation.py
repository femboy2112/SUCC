"""Exact prime clocks, Mahler finite-difference jets and Kummer tests.

The global Mahler representation and general Kummer congruences are
CLASSICAL external theorems; finite exact arithmetic probes their
hypotheses, particular instances and adversarial failure modes.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest

from observational_succ.clock_mahler_interpolation import (
    ClockInterpolationError, unit_clock_period, prime_jet_return_gap,
    unit_clock_power, unit_clock_indistinguishability,
    local_power_mahler_coefficient, local_euler_from_mahler_truncation,
    integer_power_clock_continuity, bernoulli, corrected_zeta_value,
    raw_zeta_special_value, rational_residue, kummer_clock_witness,
    clock_mahler_demo,
)


class ClockMahlerKummerTests(unittest.TestCase):
    def test_fucc_prime_jet_gap_equals_clock_period(self):
        for p in (3,5,7,11,13,17):
            for r in (1,2,3,4):
                period=(p-1)*p**(r-1)
                self.assertEqual(unit_clock_period(p,r),period)
                self.assertEqual(prime_jet_return_gap(p,r-1),period)
        self.assertEqual(unit_clock_period(5,2),20)
        with self.assertRaises(ClockInterpolationError):
            unit_clock_period(6,2)
        with self.assertRaises(ClockInterpolationError):
            unit_clock_period(2,3)
        with self.assertRaises(ClockInterpolationError):
            unit_clock_period(5,0)

    def test_clock_exponent_equivalence_at_every_unit_address(self):
        for p,r in ((3,1),(3,2),(5,1),(5,2),(7,2)):
            period=unit_clock_period(p,r)
            for base_exp in (-11,0,2,17):
                self.assertTrue(unit_clock_indistinguishability(
                    p,r,base_exp,base_exp+period))
            modulus=p**r
            for unit in range(1,modulus):
                if unit%p==0:
                    continue
                self.assertEqual(unit_clock_power(p,r,unit,3),
                                 unit_clock_power(p,r,unit,3+period))
        with self.assertRaises(ClockInterpolationError):
            unit_clock_indistinguishability(5,2,2,6)

    def test_lower_precision_period_not_valid_at_higher_precision(self):
        self.assertEqual(unit_clock_power(5,1,2,2),
                         unit_clock_power(5,1,2,6))
        self.assertNotEqual(unit_clock_power(5,2,2,2),
                            unit_clock_power(5,2,2,6))
        self.assertEqual(unit_clock_power(5,2,2,2),
                         unit_clock_power(5,2,2,22))
        with self.assertRaises(ClockInterpolationError):
            unit_clock_power(5,2,5,2)
        with self.assertRaises(ClockInterpolationError):
            unit_clock_power(5,2,10,2)

    def test_exact_mahler_jets_of_local_euler_clock(self):
        for p in (2,3,5,7,11):
            for order in range(0,11):
                left=sum((Q((-1)**(order-k)*comb(order,k)*(1-p)**k)
                          for k in range(order+1)),Q())
                right=local_power_mahler_coefficient(p,order)
                self.assertEqual(left,right)
                self.assertEqual(right,(-p)**order)
            self.assertEqual(local_power_mahler_coefficient(p,0),1)

    def test_local_euler_factor_is_exact_mahler_value_at_minus_one(self):
        for p in (2,3,5,7,11):
            for terms in (1,2,3,5,8):
                r=local_euler_from_mahler_truncation(p,terms)
                target=Q(r["continued_local_euler_factor"])
                partial=Q(r["newton_evaluation_at_minus_one"])
                self.assertEqual(target,Q(1,1-p))
                self.assertEqual(partial,sum((Q(p**k) for k in range(terms)),Q()))
                self.assertEqual(target-partial,Q(p**terms,1-p))
                self.assertEqual(r["error_valuation"],terms)
                self.assertEqual(r["local_finite_precision_clock"],str(p**terms))
                self.assertEqual(r["coefficient_valuation_levels"],tuple(range(terms)))
                self.assertTrue(r["residue_one_mod_prime"])
                self.assertFalse(r["p_adic_mahler_theorem_constructed"])

    def test_unit_clock_interpolation_can_fail_without_branch_continuity(self):
        p3=integer_power_clock_continuity(3,-1)
        p2=integer_power_clock_continuity(2,-1)
        self.assertFalse(p3["continuous_integer_power_sequence_over_Zp"])
        self.assertTrue(p3["nontrivial_mod_p_torsion_requires_weight_branch"])
        self.assertTrue(p2["continuous_integer_power_sequence_over_Zp"])
        for j in range(1,6):
            self.assertEqual(3**j%2,1)
            self.assertEqual((-1)**(3**j),-1)
            self.assertEqual((-1)**0,1)
            # In Z_3, 3^j -> 0; the values of (-1)^n do NOT.
        for p in (2,3,5,7):
            self.assertTrue(integer_power_clock_continuity(
                p,1+p)["continuous_integer_power_sequence_over_Zp"])
            self.assertTrue(integer_power_clock_continuity(
                p,1-p)["continuous_integer_power_sequence_over_Zp"])

    def test_bernoulli_values_and_trivial_corrected_weight(self):
        expected={
            0:Q(1),1:Q(-1,2),2:Q(1,6),4:-Q(1,30),
            6:Q(1,42),10:Q(5,66),12:-Q(691,2730),
            22:Q(854513,138),
        }
        for n,b in expected.items():
            self.assertEqual(bernoulli(n),b)
        self.assertEqual(corrected_zeta_value(5,2),Q(1,3))
        self.assertEqual(corrected_zeta_value(7,2),Q(1,2))
        self.assertEqual(raw_zeta_special_value(2),-Q(1,12))

    def test_kummer_five_squared_clock_has_exact_matching_rational_values(self):
        w=kummer_clock_witness(5,2,2)
        self.assertEqual(w["unit_clock_period"],20)
        self.assertEqual(w["SUCC_FUCC_prime_jet_gap"],20)
        self.assertEqual(w["weights"],(2,22))
        self.assertEqual(w["modulus"],25)
        self.assertEqual(w["corrected_zeta_residues"],(17,17))
        self.assertEqual(w["raw_zeta_residues"],(2,17))
        self.assertTrue(w["corrected_values_are_clock_compatible"])
        self.assertFalse(w["uncorrected_values_are_clock_compatible"])
        self.assertFalse(w["global_Kummer_congruence_proved_from_finite_examples"])
        self.assertFalse(w["p_adic_L_function_or_measure_constructed"])

    def test_kummer_higher_precision_clock_examples(self):
        expected=((5,1,2,6,2),(5,3,2,102,42),
                  (7,2,2,44,25),(11,2,2,112,21))
        for p,r,k,neighbor,residue_value in expected:
            with self.subTest(p=p,r=r):
                w=kummer_clock_witness(p,r,k)
                self.assertEqual(w["weights"],(k,neighbor))
                self.assertEqual(w["corrected_zeta_residues"],
                                 (residue_value,residue_value))
                self.assertEqual(w["SUCC_FUCC_prime_jet_gap"],
                                 unit_clock_period(p,r))

    def test_wrong_weight_branch_or_bad_prime_refused(self):
        for p,k in ((3,2),(5,4),(7,6)):
            with self.assertRaises(ClockInterpolationError):
                corrected_zeta_value(p,k)
        with self.assertRaises(ClockInterpolationError):
            corrected_zeta_value(6,2)
        with self.assertRaises(ClockInterpolationError):
            corrected_zeta_value(5,3)
        with self.assertRaises(ClockInterpolationError):
            corrected_zeta_value(5,True)
        with self.assertRaises(ClockInterpolationError):
            kummer_clock_witness(5,2,4)
        with self.assertRaises(ClockInterpolationError):
            kummer_clock_witness(5,4,2) # weight beyond local exact cap

    def test_non_integral_rational_cannot_have_a_zp_clock_residue(self):
        with self.assertRaises(ClockInterpolationError):
            rational_residue(Q(1,5),5,2)
        with self.assertRaises(ClockInterpolationError):
            rational_residue(Q(1,7),7,1)
        self.assertEqual(rational_residue(Q(1,3),5,2),17)
        self.assertNotEqual(rational_residue(Q(-1,12),5,2),
                            rational_residue(Q(1,3),5,2))

    def test_receipt_retains_source_and_rh_firewalls(self):
        d=clock_mahler_demo()
        self.assertEqual(d["status"],"SUCC_CLOCK_MAHLER_KUMMER_COMPATIBILITY")
        self.assertEqual(d["p_five_clock_mod_25_period"],20)
        self.assertEqual(d["p_five_SUCC_jet_gap_at_level_one"],20)
        self.assertEqual(d["mahler_interpolated_minus_one"],"1/(1-p)")
        self.assertTrue(d["unit_clock_period_equals_prime_jet_gap"])
        self.assertTrue(d["wrong_unremoved_Euler_factor_breaks_clock_congruence"])
        self.assertFalse(d["torsion_clock_mod_three_requires_branch"]
                         ["continuous_integer_power_sequence_over_Zp"])
        self.assertTrue(d["parity_clock_mod_two_is_continuous"]
                        ["continuous_integer_power_sequence_over_Zp"])
        self.assertFalse(d["clock_algebra_generates_a_p_adic_zeta_measure_without_extra_proofs"])
        self.assertTrue(d["classical_Mahler_and_Kummer_theorems_imported"])
        self.assertFalse(d["nontrivial_zeta_zeros_used"])
        self.assertFalse(d["RH_claimed"])


if __name__=="__main__":
    unittest.main()
