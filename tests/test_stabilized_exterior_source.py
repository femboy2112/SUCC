"""Hostile source-typed probes for a stabilized SUCC/FUCC exterior Fock pool."""
import unittest
from fractions import Fraction as F
from itertools import combinations

from observational_succ.stabilized_exterior_source import (
    StabilizedCarrierError, StabilizedExteriorCarrier,
    exact_stabilized_source_controls,
)
from observational_succ.koszul_prime_cancellation import source_multidegree


class StabilizedExteriorSourceTests(unittest.TestCase):
    def test_common_fock_restores_dimension_for_original_SUCC(self):
        c=StabilizedExteriorCarrier((2,3,5,7))
        self.assertEqual(len(c.common_basis),16)
        self.assertEqual(c.action_succ(6,()),(7,()))
        self.assertEqual(c.action_succ(6,(2,3)),(7,(2,3)))
        self.assertEqual(len(source_multidegree(6).basis()),4)
        self.assertEqual(len(source_multidegree(7).basis()),2)
        self.assertFalse(c.is_source_authentic(7,(2,3)))
        self.assertTrue(c.is_source_authentic(6,(2,3)))

    def test_first_hidden_prime_wedge_exposed_by_unit_and_multiplication(self):
        c=StabilizedExteriorCarrier((2,3,7))
        self.assertEqual(c.source_differential(1,(2,)),())
        self.assertEqual(c.source_differential(2,(2,)),(((),1),))
        self.assertEqual(c.source_succ_defect(1,(2,)),{():1})
        self.assertEqual(c.source_fucc_defect(1,(2,),2),{():1})
        for step in ("S","V"):
            r=c.reveal_ghost(1,(2,),step,p=2 if step=="V" else None)
            self.assertFalse(r["authentic_before"])
            self.assertTrue(r["authentic_after"])
            self.assertTrue(r["newly_observable"])
            self.assertFalse(r["auxiliary_source_redundancy_certified"])

    def test_new_wedge_at_next_SUCC_is_not_source_null(self):
        c=StabilizedExteriorCarrier((2,3,5,7))
        r=c.reveal_ghost(6,(7,),"S")
        self.assertEqual(r["source_after"],(7,(7,)))
        self.assertTrue(r["newly_observable"])
        self.assertEqual(r["source_differential_after"],(((),1),))
        self.assertEqual(c.source_succ_defect(6,(7,)),{():1})
        # Conversely wedge2 is authentic at 6, ghost at 7.
        r2=c.reveal_ghost(6,(2,),"S")
        self.assertTrue(r2["authentic_before"])
        self.assertFalse(r2["authentic_after"])
        self.assertFalse(r2["newly_observable"])

    def test_inherited_authentic_prime_lift_chain_commutes_on_real_source_subspace(self):
        c=StabilizedExteriorCarrier((2,3,5,7))
        for n,p in ((1,2),(2,3),(2,2),(6,7),(9,2),(4,5)):
            source=source_multidegree(n)
            for S in source.basis():
                self.assertEqual(c.source_fucc_defect(n,S,p),{})
        # In contrast the enlarged GHOST subspace violates this property.
        self.assertEqual(c.source_fucc_defect(1,(3,),3),{():1})

    def test_full_pool_hodge_positive_on_all_authentic_and_ghost_states(self):
        c=StabilizedExteriorCarrier((2,3,5))
        for n in (1,2,3,4,5,6,7,8,9,12,18,30,64):
            r=c.hodge_unweighted_receipt(n)
            self.assertTrue(r["anticommutator_is_identity_times_source_support"])
            self.assertEqual(r["Hodge_unweighted_eigenvalue"],len(c.original_support(n)))
            self.assertFalse(r["this_is_original_Weil_PSD"])

    def test_signed_differential_has_square_zero_independent_direct(self):
        c=StabilizedExteriorCarrier((2,3,5))
        for n in (1,2,3,6,10,12,30):
            for S in c.common_basis:
                second={}
                for T,a in c.source_differential(n,S):
                    for U,b in c.source_differential(n,T):
                        second[U]=second.get(U,F(0))+a*b
                self.assertEqual({U:v for U,v in second.items() if v},{})

    def test_no_go_simultaneous_Q_and_Qadjoint_equivariance_with_arithmetic_H(self):
        c=StabilizedExteriorCarrier((2,3))
        for n in (1,2,3,6,9,17):
            r=c.source_shift_no_go(n)
            self.assertTrue(r["SUCC_isometry_on_common_fock"])
            self.assertTrue(r["H_cannot_commute_with_S"])
            self.assertTrue(r["simultaneous_Q_Qadjoint_equivariance_refuted"])
            self.assertFalse(r["original_Weil_form_identified"])
            self.assertEqual(r["formal_H_source"],f"log({n})")

    def test_mixed_source_future_exposure_and_global_receipt(self):
        r=exact_stabilized_source_controls()
        self.assertEqual(r["common_Fock_dim"],8)
        self.assertTrue(r["S_from_6_to_7_now_isometric"])
        self.assertTrue(r["first_ghost_reactivated_by_SUCC"]["newly_observable"])
        self.assertTrue(r["first_ghost_reactivated_by_prime_FUCC"]["newly_observable"])
        self.assertFalse(r["global_Hodge_Weil_form_identified"])
        self.assertFalse(r["RH_proved"])

    def test_reject_fake_ghost_sources_and_malformed_steps(self):
        for primes in ((6,),(2,2),(3,2),(True,),(2,)*9):
            with self.assertRaises(StabilizedCarrierError):
                StabilizedExteriorCarrier(primes)
        for bad in ("",True,None):
            with self.assertRaises(StabilizedCarrierError):
                StabilizedExteriorCarrier((2,),source_id=bad)
        with self.assertRaises(StabilizedCarrierError):
            StabilizedExteriorCarrier((2,),epoch=True)
        c=StabilizedExteriorCarrier((2,3))
        with self.assertRaises(StabilizedCarrierError):
            c.source_differential(1,(5,))
        with self.assertRaises(StabilizedCarrierError):
            c.source_succ_defect(100000,())
        with self.assertRaises(StabilizedCarrierError):
            c.action_fucc(2,(),6)
        with self.assertRaises(StabilizedCarrierError):
            c.action_fucc(2,(),5)
        with self.assertRaises(StabilizedCarrierError):
            c.reveal_ghost(1,(2,),"invented-step")


if __name__=="__main__":
    unittest.main()
