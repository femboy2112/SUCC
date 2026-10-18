"""Independent exact rivals for equivariant SUCC/FUCC Koszul redundancy.

No finite enumeration is promoted into a universal theorem. Universal proofs
are in the companion research paper, with classical chain Lefschetz inputs.
"""
import unittest
from fractions import Fraction as F
from itertools import combinations

from observational_succ.equivariant_koszul_descent import (
    EquivariantDescentError, matrix_chain_diagonal,
    trace_obstruction, prime_chain_lift, unit_succ_dimension_control,
    original_prime_source_supertrace_gate, normalized_prime_clock_retraction,
    prime_multiplication_nullhomotopy,
)
from observational_succ.koszul_prime_cancellation import source_multidegree
from observational_succ.completed_weil_transport import von_mangoldt_labels


class EquivariantKoszulDescentTests(unittest.TestCase):
    def test_acyclic_supertrace_is_zero_for_all_nonunit_sources(self):
        for n in range(1,201):
            source=source_multidegree(n)
            scalar=matrix_chain_diagonal(n,{s:F(13,7) for s in source.basis()})
            self.assertTrue(scalar["commutes_with_d"])
            self.assertEqual(scalar["supertrace"], F(13,7) if n==1 else 0)
            self.assertEqual(scalar["supertrace"],scalar["supertrace_of_source_cohomology"])
            self.assertFalse(scalar["has_spectral_Weil_distribution"])

    def test_independent_supertrace_boolean_alternating_signs(self):
        for n in (1,2,4,6,8,12,30,36,60,210):
            states=source_multidegree(n).basis()
            expected=sum((-1)**len(s) for s in states)
            self.assertEqual(expected,int(n==1))
            self.assertEqual(matrix_chain_diagonal(n,dict.fromkeys(states,1))["supertrace"],
                             expected)

    def test_grade_zero_prime_probe_is_visible_but_breaks_d_compatibility(self):
        for n in (2,3,4,5,6,8,9,12,27,30):
            rec=trace_obstruction(n)
            self.assertEqual(rec["chain_compatible_supertrace"],0)
            self.assertEqual(rec["grade_zero_projector_supertrace"],1)
            self.assertFalse(rec["grade_zero_projector_commutes_with_d"])
            self.assertTrue(rec["graded_defect_edges"])
            self.assertTrue(rec["acyclic_prime_signal_is_a_chain_defect_if_exposed"])
        one=trace_obstruction(1)
        self.assertTrue(one["grade_zero_projector_commutes_with_d"])
        self.assertEqual(one["chain_compatible_supertrace"],1)

    def test_exact_diagonal_rival_operators_and_commutator(self):
        c=source_multidegree(6)
        basis=c.basis()
        values={s:F(2) if len(s)%2==0 else F(-3) for s in basis}
        rec=matrix_chain_diagonal(6,values)
        self.assertFalse(rec["commutes_with_d"])
        self.assertEqual(rec["supertrace"], F(10))
        self.assertGreater(len(rec["commutator_defect_edges"]),0)
        constant=matrix_chain_diagonal(6,dict.fromkeys(basis,F(2)))
        self.assertTrue(constant["commutes_with_d"])
        self.assertEqual(constant["supertrace"],0)

    def test_origin_first_prime_is_homologically_nonredundant(self):
        for p in (2,3,5,7,11):
            rec=prime_chain_lift(1,p)
            self.assertTrue(rec["chain_map_Vp_commutes_with_d"])
            self.assertTrue(rec["Vp_star_fails_to_intertwine_dstar"])
            self.assertEqual(rec["quotient_homology"],{1:1})
            self.assertFalse(rec["quotient_acyclic"])
            self.assertEqual(rec["new_exterior_basis"],((p,),))
            self.assertTrue(rec["origin_to_prime_homology_defect"])
            self.assertFalse(rec["new_data_is_derived_redundant_relative_to_source"])

    def test_repeated_p_jet_is_exact_chain_isomorphism(self):
        for n,p in ((2,2),(4,2),(9,3),(12,2),(15,3),(72,3),(125,5)):
            rec=prime_chain_lift(n,p)
            self.assertEqual(rec["source_dim"],rec["target_dim"])
            self.assertEqual(rec["new_exterior_basis"],())
            self.assertEqual(rec["quotient_homology"],{})
            self.assertFalse(rec["Vp_star_fails_to_intertwine_dstar"])
            self.assertTrue(rec["quotient_acyclic"])

    def test_new_prime_after_source_is_derived_acyclic_but_adjoint_sensitive(self):
        for n,p in ((2,3),(6,5),(4,7),(9,2),(30,7),(72,5)):
            rec=prime_chain_lift(n,p)
            self.assertTrue(rec["chain_map_Vp_commutes_with_d"])
            self.assertTrue(rec["Vp_star_fails_to_intertwine_dstar"])
            self.assertTrue(rec["chain_adjoint_defects"])
            self.assertTrue(rec["new_exterior_basis"])
            self.assertEqual(rec["quotient_homology"],{})
            self.assertTrue(rec["new_data_is_derived_redundant_relative_to_source"])
            self.assertFalse(rec["origin_to_prime_homology_defect"])
            self.assertEqual(rec["target_dim"],2*rec["source_dim"])

    def test_independent_quotient_boundary_chain_for_n2_p3(self):
        # Target K_6: degree-two (2,3) -> (3)-(2).
        # Modulo image K_2, only (3) survives; quotient has
        # ((2,3) --1--> (3)), which is acyclic.
        r=prime_chain_lift(2,3)
        self.assertEqual(r["new_exterior_basis"],((3,),(2,3)))
        self.assertEqual(r["quotient_homology"],{})
        k=source_multidegree(6)
        self.assertEqual(k.boundary((2,3)),(((3,),1),((2,),-1)))

    def test_unit_successor_dimensional_no_isometry_obstruction(self):
        r=unit_succ_dimension_control(6)
        self.assertEqual((r["source_dimension"],r["next_dimension"]),(4,2))
        self.assertFalse(r["literal_fiberwise_isometric_S_possible"])
        self.assertFalse(r["genuine_SUCC_observables_preserved_by_an_invented_ancilla"])
        self.assertTrue(unit_succ_dimension_control(1)["literal_fiberwise_isometric_S_possible"])
        self.assertFalse(unit_succ_dimension_control(1)["genuine_SUCC_observables_preserved_by_an_invented_ancilla"])

    def test_genuine_fucc_is_exact_chain_boundary_even_at_prime_origin(self):
        for p in (2,3,5,7,11):
            for n in (1,2,3,4,6,8,9,12,25,30,36):
                rec=prime_multiplication_nullhomotopy(n,p)
                self.assertTrue(rec["exact_d_epsilon_plus_epsilon_d_is_Vp"])
                self.assertTrue(rec["chain_map_original_Vp_nonzero"])
                self.assertEqual(rec["target_n"],p*n)
                self.assertFalse(rec["Koszul_homology_faithfully_represents_original_FUCC"])
                self.assertEqual(len(rec["checked_source_wedges"]),
                                 len(source_multidegree(n).basis()))
                for S,output in rec["checked_source_wedges"]:
                    self.assertEqual(output,{S:F(1)})
        self.assertTrue(prime_multiplication_nullhomotopy(1,2)
                        ["first_activation_extra_homology_retained_as_relative_defect"])
        self.assertFalse(prime_multiplication_nullhomotopy(4,2)
                         ["first_activation_extra_homology_retained_as_relative_defect"])
        with self.assertRaises(EquivariantDescentError):
            prime_multiplication_nullhomotopy(2,6)

    def test_source_restricted_trace_removes_augmented_wedge_multiplicity(self):
        for n,p in ((1,2),(2,3),(6,5),(4,2),(9,3),(30,7),(72,2)):
            r=normalized_prime_clock_retraction(n,p)
            self.assertEqual(r["source_log_valuation_delta"],((p,1),))
            self.assertEqual(r["raw_source_trace_prime_log_coefficient"],
                             len(source_multidegree(n).basis()))
            self.assertEqual(r["normalized_trace_prime_log_coefficient"],F(1))
            self.assertEqual(r["symbolic_clock_result"],f"log({p})")
            self.assertTrue(r["source_prime_jet_energy_survives"])
            self.assertFalse(r["canonical_Connes_trace_proved"])
            if p not in source_multidegree(n).active:
                self.assertEqual(r["target_wedge_dimension"],2*r["source_wedge_dimension"])
        with self.assertRaises(EquivariantDescentError):
            normalized_prime_clock_retraction(2,6)

    def test_original_von_mangoldt_tape_has_nonzero_acyclic_witnesses(self):
        for N in (4,9,30,75,140):
            r=original_prime_source_supertrace_gate(N)
            self.assertEqual(r["original_wavefront"],von_mangoldt_labels(N))
            self.assertEqual(len(r["chain_invariant_supertrace_tape"]),len(r["original_wavefront"]))
            self.assertTrue(all(v==0 for n,p,v in r["chain_invariant_supertrace_tape"]))
            self.assertTrue(all(v==1 and not chain for n,p,v,chain
                                in r["grade_zero_nonchain_trace_tape"]))
            self.assertTrue(r["nonzero_original_prime_power_distribution_missing"])
            self.assertFalse(r["Connes_full_global_trace"])
            self.assertFalse(r["RH_proved"])

    def test_mutations_reject_fake_primes_and_incomplete_observables(self):
        for p in (1,4,6,True,F(2),2.5):
            with self.assertRaises(EquivariantDescentError):
                prime_chain_lift(1,p)
        for n in (0,-1,True,F(6),2.5):
            with self.assertRaises(EquivariantDescentError):
                trace_obstruction(n)
        c=source_multidegree(6)
        with self.assertRaises(EquivariantDescentError):
            matrix_chain_diagonal(6,{():F(1)})
        with self.assertRaises(EquivariantDescentError):
            matrix_chain_diagonal(6,{s:float(1) for s in c.basis()})
        with self.assertRaises(EquivariantDescentError):
            prime_chain_lift(100000,2)
        with self.assertRaises(EquivariantDescentError):
            unit_succ_dimension_control(100000)


if __name__=="__main__":
    unittest.main()
