"""Exact hostile controls for proto-SUCC unit d and higher-step unipotent lift."""
from math import comb,gcd
from itertools import product
import unittest

from observational_succ.proto_succ_variable_unit import (
    ProtoSuccError, FormalD, binomial_integer, proto_succ_formal,
    generalized_succ, modular_succ, additive_clock_period,
    modular_orbit, clock_change_isomorphism, shift_dilation_address_defect,
    normalized_defect_mod, prime_jet_directed_gap,
    HigherSuccJet, higher_succ_step_units, clock_unit_change_witness,
    variable_proto_succ_demo,
)


class ProtoSuccVariableUnitTests(unittest.TestCase):
    def test_unit_one_specialization_recovers_original_SUCC_from_zero(self):
        for n in range(30):
            formula=proto_succ_formal(n)
            self.assertEqual(formula,FormalD(0,n))
            self.assertEqual(formula.specialize(1),n)
            self.assertEqual(formula.specialize(0),0)
            self.assertEqual(formula.specialize(7),7*n)
            self.assertEqual(generalized_succ(n,1),n+1)
            self.assertEqual(generalized_succ(n,0),n)
        self.assertEqual(FormalD(5,2).specialize(3),11)
        self.assertEqual(FormalD(3,1)+FormalD(-3,5),FormalD(0,6))
        self.assertEqual(FormalD(3,2).times(-2),FormalD(-6,-4))

    def test_formal_unit_is_not_assumed_invertible_after_specialization(self):
        for d in (-10,-5,-2,0,1,2,5,10):
            formal=FormalD(0,1)
            self.assertEqual(formal.specialize(d),d)
            for p in (3,5):
                if gcd(d,p)==1:
                    self.assertEqual(
                        clock_change_isomorphism(p,2,d)["full_cycle_period"],
                        p**2)
                else:
                    with self.assertRaises(ProtoSuccError):
                        clock_change_isomorphism(p,2,d)
        self.assertEqual(proto_succ_formal(1).specialize(0),0)
        self.assertNotEqual(proto_succ_formal(1),FormalD(0,0))

    def test_exact_additive_clock_period_and_complete_orbit_exhaustion(self):
        # Independent gcd formula and explicit visited states agree.
        count=0
        for p in (2,3,5,7):
            for r in (1,2,3):
                modulus=p**r
                for d in range(-12,13):
                    expected=modulus//gcd(abs(d),modulus)
                    self.assertEqual(additive_clock_period(p,r,d),expected)
                    orbit=modular_orbit(p,r,d)
                    self.assertEqual(len(orbit),expected)
                    self.assertEqual(len(set(orbit)),expected)
                    self.assertEqual(orbit[0],0)
                    self.assertEqual(len(orbit),len(
                        {(i*d)%modulus for i in range(modulus)}))
                    self.assertEqual(modular_succ(0,d,p,r),d%modulus)
                    count+=1
        self.assertEqual(count,300)

    def test_unit_gauge_square_conjugates_S_one_and_S_d(self):
        # If d is a unit, x->d*x is a bijection on the whole clock.
        for p in (2,3,5,7):
            for r in (1,2,3):
                modulus=p**r
                for d in (-7,-2,-1,1,2,3,7):
                    if gcd(d,p)!=1:
                        with self.assertRaises(ProtoSuccError):
                            clock_change_isomorphism(p,r,d)
                        continue
                    item=clock_change_isomorphism(p,r,d)
                    self.assertEqual(item["full_cycle_period"],modulus)
                    self.assertEqual((item["inverse"]*d)%modulus,1)
                    for n in range(min(modulus,20)):
                        left=(d*(n+1))%modulus
                        right=modular_succ(d*n,d,p,r)
                        self.assertEqual(left,right)

    def test_nonunit_clock_changes_reachability_not_just_names(self):
        self.assertEqual(additive_clock_period(5,2,1),25)
        self.assertEqual(additive_clock_period(5,2,5),5)
        self.assertEqual(additive_clock_period(5,2,25),1)
        self.assertEqual(additive_clock_period(5,2,0),1)
        self.assertEqual(modular_orbit(5,2,5),(0,5,10,15,20))
        self.assertEqual(modular_orbit(5,2,25),(0,))
        for bad in (0,5,10,25):
            with self.assertRaises(ProtoSuccError):
                clock_change_isomorphism(5,2,bad)
        self.assertEqual(additive_clock_period(2,4,6),8)

    def test_generalized_ax_plus_b_relation_exact_for_all_integer_units(self):
        for p in (2,3,5,7,11):
            for address in (-3,0,1,13):
                for d in (-10,-2,0,1,2,5,13):
                    direct=generalized_succ(p*address,d)
                    indirect=p*generalized_succ(address,d)
                    self.assertEqual(direct-indirect,(1-p)*d)
                    self.assertEqual(
                        shift_dilation_address_defect(p,address,d),(1-p)*d)
                    # V_p S_d = S_(pd) V_p, a KET LABEL relation.
                    self.assertEqual(p*(address+d),p*address+p*d)
        # A scalar difference of integer destinations is NOT the actual
        # ket-space commutator: |p*n+d> - |p*n+p*d> is a vector.

    def test_normalized_ax_b_defect_is_independent_of_invertible_d(self):
        for p in (2,3,5,7):
            for r in (1,2,3):
                for d in (-7,-2,-1,1,2,3,7):
                    if gcd(d,p)==1:
                        self.assertEqual(
                            normalized_defect_mod(p,r,4,d),
                            (1-p)%(p**r))
                    else:
                        with self.assertRaises(ProtoSuccError):
                            normalized_defect_mod(p,r,4,d)
        self.assertEqual(shift_dilation_address_defect(5,3,0),0)
        self.assertEqual(shift_dilation_address_defect(5,3,5),-20)
        self.assertEqual(-20%5,0)
        self.assertEqual((1-5)%5,1)

    def test_variable_unit_prime_jet_gap_tracks_d(self):
        for p in (2,3,5,7):
            for level in range(5):
                for d in (-3,0,1,2,5):
                    expected=(p-1)*p**level*d
                    self.assertEqual(prime_jet_directed_gap(p,level,d),expected)
        self.assertEqual(prime_jet_directed_gap(5,1,1),20)
        self.assertEqual(prime_jet_directed_gap(5,1,2),40)

    def test_higher_order_succ_yields_linear_and_quadratic_paths(self):
        linear=HigherSuccJet((0,3))
        self.assertEqual([linear.first_coordinate(n) for n in range(7)],
                         [0,3,6,9,12,15,18])
        self.assertEqual(linear.succ().coefficients,(3,3))
        quad=HigherSuccJet((0,2,3))
        self.assertEqual([quad.first_coordinate(n) for n in range(6)],
                         [0,2,7,15,26,40])
        self.assertEqual(quad.at(3).coefficients,(15,11,3))
        self.assertEqual(higher_succ_step_units(quad,5),(2,5,8,11,14))
        for n in range(9):
            self.assertEqual(quad.at(n).coefficients[0],
                             n*2+comb(n,2)*3)
            self.assertEqual(quad.at(n).coefficients[1],2+3*n)
            self.assertEqual(quad.at(n+1),quad.at(n).succ())

    def test_unipotent_Pascal_jet_succ_is_integral_even_mod_two(self):
        for d,a,b in product((-2,0,3),repeat=3):
            jet=HigherSuccJet((0,d,a,b))
            for n in range(7):
                result=jet.at(n)
                self.assertEqual(result.coefficients[0],
                                 n*d+comb(n,2)*a+comb(n,3)*b)
                self.assertEqual(result.coefficients[1],
                                 d+n*a+comb(n,2)*b)
                self.assertEqual(result.coefficients[2],a+n*b)
                self.assertEqual(result.coefficients[3],b)
                self.assertEqual(jet.at(n+1),jet.at(n).succ())
                self.assertEqual(jet.at(n).mod(2,3),
                                 jet.mod(2,3).at(n).mod(2,3))

    def test_unipotent_inverse_works_for_negative_succ_iterations(self):
        for jet in (HigherSuccJet((1,2)),HigherSuccJet((0,1,3)),
                    HigherSuccJet((5,-2,3,-1))):
            self.assertEqual(jet.at(0),jet)
            for n in range(1,9):
                self.assertEqual(jet.at(-n).at(n),jet)
                self.assertEqual(jet.at(n).at(-n),jet)
                self.assertEqual(jet.at(-1).succ(),jet)
        self.assertEqual(binomial_integer(-1,0),1)
        self.assertEqual(binomial_integer(-1,1),-1)
        self.assertEqual(binomial_integer(-1,2),1)
        self.assertEqual(binomial_integer(-2,2),3)

    def test_proto_succ_variable_unit_may_change_local_access_class(self):
        receipt=clock_unit_change_witness()
        self.assertEqual(receipt["starting_jet"],[0,1,4])
        self.assertEqual(receipt["after_meta_succ_jet"],[1,5,4])
        self.assertEqual(receipt["initial_unit_clock_period"],25)
        self.assertEqual(receipt["updated_nonunit_clock_period"],5)
        self.assertFalse(receipt["same_full_clock_coordinate_isomorphism_survives"])
        self.assertTrue(receipt["path_still_exists_as_integer_SUCC"])
        self.assertFalse(receipt["physical_proof_impossibility_claimed"])

    def test_symbolic_coefficient_can_survive_when_specialization_to_zero_fails(self):
        # In the UNIVERSAL FORMAL parameter language (1-p)*D has a
        # meaningful coefficient (1-p); but after d=0 is chosen, its
        # specialized value is ZERO, losing p information.
        for p in (2,3,5,7,11):
            formal=FormalD(0,1-p)
            self.assertEqual(formal.unit_coefficient,1-p)
            self.assertEqual(formal.specialize(0),0)
            self.assertEqual(formal.specialize(1),1-p)
            self.assertEqual(formal.specialize(3),3*(1-p))
        self.assertNotEqual(FormalD(0,-4),FormalD(0,-6))
        self.assertEqual(FormalD(0,-4).specialize(0),
                         FormalD(0,-6).specialize(0))

    def test_invalid_clock_and_jet_source_inputs_fail(self):
        with self.assertRaises(ProtoSuccError):
            proto_succ_formal(-1)
        with self.assertRaises(ProtoSuccError):
            additive_clock_period(6,2,1)
        with self.assertRaises(ProtoSuccError):
            clock_change_isomorphism(2,0,1)
        with self.assertRaises(ProtoSuccError):
            normalized_defect_mod(5,2,1,0)
        with self.assertRaises(ProtoSuccError):
            prime_jet_directed_gap(6,0,1)
        with self.assertRaises(ProtoSuccError):
            HigherSuccJet((1,))
        with self.assertRaises(ProtoSuccError):
            HigherSuccJet((1,True))
        with self.assertRaises(ProtoSuccError):
            FormalD(True,1)
        with self.assertRaises(ProtoSuccError):
            binomial_integer(1,-1)

    def test_typed_reproducible_claim_scope(self):
        d=variable_proto_succ_demo()
        self.assertEqual(d["status"],"VARIABLE_UNIT_PROTO_SUCC_UNIPOTENT_LIFT")
        self.assertEqual(d["formal_first_five_addresses_in_D_units"],[0,1,2,3,4])
        self.assertEqual(d["formal_original_one_step"],"0 -> D")
        self.assertTrue(d["S_one_is_D_equals_one_specialization"])
        self.assertEqual(d["S_unit_mod_25_with_unit_two_period"],25)
        self.assertEqual(d["unit_inverse_mod_25"],13)
        self.assertEqual(d["normalized_shift_dilation_defect"],"1-p")
        self.assertEqual(d["raw_shift_dilation_defect"],"D*(1-p)")
        self.assertTrue(d["symbolic_unit_must_not_be_automatically_assumed_invertible"])
        self.assertEqual(d["quadratic_d0_two_acceleration_three"],[0,2,7,15,26,40])
        self.assertTrue(d["higher_order_integer_binomial_formula"])
        self.assertTrue(d["d_zero_specialization_loses_normalized_defect_information"])
        self.assertFalse(d["new_RH_Gamma_or_Kubota_Leopoldt_theorem_claimed"])


if __name__=="__main__":
    unittest.main()
