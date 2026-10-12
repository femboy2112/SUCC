"""Arithmetic source-derived countermodels for operational Yoneda SUCC/FUCC."""
from itertools import product
import unittest

from observational_succ.operational_yoneda_descent import (
    CertifiedSourceMorphism, DescentError, induced_observation_functor,
)
from observational_succ.prime_clock_yoneda import (
    ArithmeticFunctorError, PrimeClockSource, PrimeClockQuotient,
    verify_arithmetic_source_signature, arithmetic_yoneda_demo,
)
from observational_succ.residue_one_arch import prime


class AuthenticPrimeYonedaTests(unittest.TestCase):
    def test_authentic_ring_quotient_respects_succ_and_prime_dilation(self):
        # Algebraic proof: polynomial integer maps commute with reduction.
        # Independent direct check across every input source at each precision.
        for p,r,k,d,q in (
            (2,2,1,1,3),(2,3,1,-3,5),(3,2,1,1,7),
            (5,2,1,1,11),(5,2,1,-1,3)):
            high=PrimeClockSource(p,r,k,d,q)
            low=PrimeClockSource(p,k,k,d,q)
            self.assertTrue(prime(p) and prime(q))
            self.assertTrue(verify_arithmetic_source_signature(
                high,low)["same_authentic_jet_prime"])
            for x in range(high.modulus):
                y=x%low.modulus
                self.assertEqual(high.shift(x)%low.modulus,low.shift(y))
                self.assertEqual(high.dilate(x)%low.modulus,low.dilate(y))
                self.assertEqual(high.public_report(x),low.public_report(y))
                # The full source output is not disclosed to receiver.
                self.assertEqual((high.dilate(high.shift(x))-
                                  high.shift(high.dilate(x)))%high.modulus,
                                 (d*(q-1))%high.modulus)

    def test_nonflat_fine_defect_can_vanish_in_coarse_observer_quotient(self):
        for p,r,k,d,q in ((2,2,1,1,3),(3,2,1,1,7),
                          (5,2,1,1,11)):
            high=PrimeClockSource(p,r,k,d,q)
            low=PrimeClockSource(p,k,k,d,q)
            self.assertNotEqual(high.coordinate_defect(),0)
            self.assertEqual(low.coordinate_defect(),0)
            self.assertEqual(high.coordinate_defect()%low.modulus,0)
            # Two NONCOMMUTING fine action paths collapse to one
            # endpoint action at a strictly coarser residue resolution.
            for x in range(high.modulus):
                hv=high.shift(high.dilate(x))
                vh=high.dilate(high.shift(x))
                self.assertNotEqual(hv,vh)
                self.assertEqual(hv%low.modulus,vh%low.modulus)

    def test_witnessed_true_prime_fucc_yoneda_functor_and_rank_preservation(self):
        for p,r,k,d,q in ((2,2,1,1,3),(3,2,1,1,7)):
            quotient=PrimeClockQuotient(p,r,k,d,q,True)
            certificate=quotient.exact_certificate()
            self.assertEqual(certificate["status"],
                             "SOURCE_DERIVED_SUCC_FUCC_PRIME_QUOTIENT")
            self.assertFalse(certificate["state_map_injective"])
            self.assertEqual(certificate["abstract_rank"],1)
            self.assertEqual(certificate["concrete_rank"],1)
            self.assertTrue(certificate["source_image_surjective"])
            self.assertTrue(certificate["declared_quotient_invariant_original_claim_lifted"])
            self.assertTrue(certificate["coarse_quotient_functor_verified"])
            self.assertTrue(certificate["coarse_context_onto"])
            self.assertFalse(certificate["real_Gamma_or_completed_Weil_identified"])
            morph=quotient.morphism()
            f=induced_observation_functor(morph,horizon=1)
            self.assertGreater(f.proof_receipt()["checked_functor_compositions"],0)
            self.assertEqual(morph.h,
                             tuple(x%(p**k) for x in range(p**r)))

    def test_reader_free_mathematical_source_never_fabricates_original_target(self):
        for case in ((2,2,1,1,3),(3,2,1,1,7)):
            cert=PrimeClockQuotient(*case,False).exact_certificate()
            self.assertIsNone(cert["abstract_rank"])
            self.assertIsNone(cert["concrete_rank"])
            self.assertTrue(cert["optimal_original_source_rank_equal"])
            self.assertEqual(cert["transported_source_replays"],0)

    def test_wrong_original_high_digit_predicate_cannot_descend(self):
        q=PrimeClockQuotient(2,2,1,1,3)
        m=q.morphism()
        mutation=CertifiedSourceMorphism(
            m.concrete,m.abstract,m.source_concrete,m.source_abstract,
            m.h,tuple(str(x) for x in range(4)),
            m.t_abstract,m.target_id)
        with self.assertRaises(DescentError):
            mutation.verify()

    def test_distinct_actual_primes_can_be_behaviorally_indistinguishable(self):
        q=PrimeClockQuotient(2,2,1,1,3)
        fine=q.fine
        wrong=PrimeClockSource(2,1,1,1,5)
        h=tuple(x%2 for x in range(4))
        twin=CertifiedSourceMorphism(
            fine.carrier(),wrong.carrier(),
            tuple(range(4)),(0,1),h,
            ("0","1","0","1"),("0","1"),"original-parity")
        # Observable/coaction squares all pass. They cannot prove the
        # actual source jet is THREE rather than FIVE.
        self.assertEqual(twin.verify()["status"],
                         "EXACT_SOURCE_COALGEBRA_MORPHISM")
        with self.assertRaises(ArithmeticFunctorError):
            verify_arithmetic_source_signature(fine,wrong)

    def test_shift_parameter_alias_at_coarse_precision_is_not_source_identity(self):
        fine=PrimeClockSource(2,2,1,1,3)
        wrong=PrimeClockSource(2,1,1,3,3)
        m=CertifiedSourceMorphism(
            fine.carrier(),wrong.carrier(),tuple(range(4)),(0,1),
            (0,1,0,1),("0","1","0","1"),("0","1"),"parity")
        self.assertTrue(m.verify()["source_claim_pullback"])
        with self.assertRaises(ArithmeticFunctorError):
            verify_arithmetic_source_signature(fine,wrong)

    def test_fake_composite_euler_source_and_wrong_local_prime_rejected(self):
        for args in ((2,2,1,1,6),(4,2,1,1,3),
                     (2,0,0,1,3),(2,2,0,1,3),
                     (2,2,3,1,3),(5,3,1,1,3)):
            with self.subTest(args=args):
                with self.assertRaises(ArithmeticFunctorError):
                    PrimeClockSource(*args)
        for args in ((2,2,2,1,3),(2,2,0,1,3),
                     (2,1,2,1,3),(2,2,1,1,6)):
            with self.assertRaises(ArithmeticFunctorError):
                PrimeClockQuotient(*args)
        with self.assertRaises(ArithmeticFunctorError):
            verify_arithmetic_source_signature(
                PrimeClockSource(2,2,1,1,3),
                PrimeClockSource(3,1,1,1,3))

    def test_source_derived_yoneda_demo_machine_receipt(self):
        x=arithmetic_yoneda_demo()
        self.assertEqual(x["status"],
                         "AUTHENTIC_PRIME_SUCC_FUCC_YONEDA_TRANSPORT_EXACT")
        self.assertEqual(x["fine_source_modulus"],4)
        self.assertEqual(x["coarse_source_modulus"],2)
        self.assertEqual(x["genuine_prime_place"],2)
        self.assertEqual(x["genuine_prime_jet"],3)
        self.assertEqual(x["fine_noncommuting_defect"],2)
        self.assertEqual(x["coarse_defect"],0)
        self.assertTrue(x["fine_nonflat_coarse_flat"])
        self.assertTrue(x["coarse_source_rank_preserved"])
        self.assertEqual(x["both_original_source_ranks_with_read"],[1,1])
        self.assertEqual(x["both_original_source_ranks_without_read"],[None,None])
        self.assertTrue(x["induced_actual_observation_functor_verified"])
        self.assertTrue(x["different_true_prime_jet_behavioral_alias_exists"])
        self.assertTrue(x["declared_jet_source_signature_rejects_alias"])
        self.assertFalse(x["arithmetic_source_parameters_physically_authenticated"])
        self.assertFalse(x["fake_composite_euler_jet_admitted"])
        self.assertFalse(x["RH_claimed"])


if __name__=="__main__":
    unittest.main()
