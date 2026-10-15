"""Source-indexed exact compression leakage and its missing-boundary controls."""
import unittest
from fractions import Fraction as F
from observational_succ import wild_boundary_compression as w


class ExactCompressionTests(unittest.TestCase):
    def setUp(self):
        self.T=w.source_shift(5)
        self.C=w.add(w.scale(3,w.eye(5)),
                     w.add(self.T,w.transpose(self.T)))
        self.window=(0,1,2)

    def test_global_transport_and_positive_gamma_like_bath(self):
        self.assertEqual(w.multiply(self.T,w.transpose(self.T)),w.eye(5))
        self.assertEqual(w.commutator(self.T,self.C),w.zero(5,5))
        A=w.add(w.eye(5),self.T)
        self.assertEqual(self.C,w.add(w.eye(5),w.multiply(A,w.transpose(A))))
        for v in ((1,0,0,0,0),(1,1,1,1,1),(1,2,3,4,5)):
            # Positive quadratic energy: v^T C v = |v|² + |(I+T)^T v|²
            out=sum((F(v[i])*self.C[i][j]*v[j]
                     for i in range(5) for j in range(5)),F())
            self.assertGreater(out,0)

    def test_noncommuting_source_compression(self):
        cert=w.finite_boundary_certificate()
        self.assertEqual(cert.full_commutator,w.zero(5,5))
        self.assertEqual(cert.compressed_commutator,
                         ((F(-1),F(),F()),(F(),F(),F()),(F(),F(),F(1))))
        self.assertEqual(cert.norm_square_frobenius,F(2))
        self.assertTrue(cert.leakage_difference_matches)
        self.assertTrue(cert.triple_coherence_zero)
        self.assertFalse(cert.gamma_source_identified)
        self.assertFalse(cert.weil_sign_certified)

    def test_nonfunctoriality_is_exact_leakage(self):
        for A,B in ((self.T,self.C),(self.C,self.T),
                    (self.T,w.transpose(self.T))):
            self.assertEqual(w.compression_defect(A,B,self.window),
                             w.leakage(A,B,self.window))

    def test_associativity_coherence(self):
        # Challenging triple, no assumption of joint source commutativity
        for A,B,C in (
            (self.T,self.C,w.transpose(self.T)),
            (self.C,self.T,self.C),
            (self.T,self.T,self.T),
        ):
            self.assertEqual(w.three_model_coherence(A,B,C,self.window),
                             w.zero(3,3))

    def test_full_carrier_has_no_leakage(self):
        I=tuple(range(5))
        cert=w.finite_boundary_certificate(window=I)
        self.assertEqual(cert.norm_square_frobenius,0)
        self.assertEqual(w.leakage(self.C,self.T,I),w.zero(5,5))
        self.assertEqual(w.compression_defect(self.T,self.C,I),w.zero(5,5))

    def test_scalar_observer_misses_compressed_noncommutativity(self):
        c=w.finite_boundary_certificate(window=(0,))
        self.assertEqual(c.norm_square_frobenius,0)
        self.assertEqual(c.compressed_commutator,((F(0),),))

    def test_basis_gauge_covariance_requires_declared_transport(self):
        signs=(1,-1,1,-1,1)
        A=w.gauge_conjugation(self.T,signs)
        B=w.gauge_conjugation(self.C,signs)
        base=w.commutator(w.compress(self.T,self.window),
                          w.compress(self.C,self.window))
        transported=w.gauge_conjugation(base,signs[:3])
        self.assertEqual(w.commutator(w.compress(A,self.window),
                                     w.compress(B,self.window)),transported)
        self.assertEqual(sum((x*x for r in base for x in r),F()),F(2))
        with self.assertRaises(w.BoundarySourceError):
            w.gauge_conjugation(self.T,(1,2,1,1,1))


    def test_boundary_commutator_survives_small_verified_error(self):
        result=w.conditional_commutator_stability(F(1,10))
        self.assertEqual(result["conditional_operator_lower_bound"],F(4,5))
        self.assertFalse(result["genuine_arithmetic_gamma_error_verified"])
        self.assertFalse(result["positive_weil_proved"])
        self.assertEqual(w.conditional_commutator_stability(F(1,2))[
                            "conditional_operator_lower_bound"],0)
        with self.assertRaises(w.BoundarySourceError):
            w.conditional_commutator_stability(0.1)

    def test_independent_actual_perturbation_respects_bound(self):
        eps=F(1,10)
        B=w.add(self.C,tuple(tuple(eps if i==j==0 else F()
                       for j in range(5)) for i in range(5)))
        T=w.compress(self.T,self.window)
        base=w.commutator(T,w.compress(self.C,self.window))
        pert=w.commutator(T,w.compress(B,self.window))
        self.assertNotEqual(base,pert)
        # Exact column-coordinate lower bound on operator norm.
        actual_lower=max(abs(pert[i][0]) for i in range(3))
        self.assertGreaterEqual(actual_lower,F(4,5))


    def test_wild_limit_pathology_cannot_be_a_weil_sign_jump(self):
        for n in (1,2,3,10,100,1000):
            r=w.signed_limit_nonwild_control(n)
            self.assertEqual(r["distance_to_limit"],F(1,n))
            self.assertEqual(r["limit_negative_depth"],F(1))
            self.assertEqual(r["stage_negative_depth"],max(F(),F(1)-F(1,n)))
            self.assertLessEqual(abs(r["stage_negative_depth"]-F(1)),F(1,n))
            self.assertEqual(r["stage_negative_detected"],n>=2)
            self.assertFalse(r["wild_limit_sign_pathology_possible"])
            self.assertFalse(r["genuine_weil_operator"])

    def test_negative_limit_has_finite_detectable_witness(self):
        self.assertFalse(w.signed_limit_nonwild_control(1)["stage_negative_detected"])
        self.assertTrue(w.signed_limit_nonwild_control(2)["stage_negative_detected"])
        with self.assertRaises(w.BoundarySourceError):
            w.signed_limit_nonwild_control(0)
        with self.assertRaises(w.BoundarySourceError):
            w.signed_limit_nonwild_control(2.0)

    def test_source_epoch_basis_and_invalid_windows(self):
        for fn in (
            lambda:w.finite_boundary_certificate(epoch=-1),
            lambda:w.finite_boundary_certificate(source_id=""),
            lambda:w.finite_boundary_certificate(basis=""),
            lambda:w.finite_boundary_certificate(window=(0,0,1)),
            lambda:w.finite_boundary_certificate(window=(0,8)),
            lambda:w.source_shift(0),
        ):
            with self.assertRaises(w.BoundarySourceError):
                fn()

    def test_no_floats_are_proofs(self):
        with self.assertRaises(w.BoundarySourceError):
            w.mat(((1.0,0),(0,1)))
        with self.assertRaises(w.BoundarySourceError):
            w.scale(0.5,self.T)
        with self.assertRaises(w.BoundarySourceError):
            w.finite_boundary_certificate(epoch=0.0)

    def test_boundary_compression_is_not_wild_topology(self):
        result=w.finite_boundary_certificate()
        self.assertEqual(result.source_id,"FINITE_CYCLIC_TOY")
        self.assertFalse(result.weil_sign_certified)
        self.assertFalse(result.gamma_source_identified)


    def test_orthogonal_wild_reembedding_cannot_fix_signed_weil_toy(self):
        receipt=w.unitary_sign_invariance_control()
        self.assertEqual(receipt["original_negative_rayleigh"],F(-1))
        self.assertEqual(receipt["transported_negative_rayleigh"],F(-1))
        self.assertTrue(receipt["unitary_basis_certified"])
        self.assertFalse(receipt["actual_wild_to_weil_intertwiner"])
        self.assertFalse(receipt["rh_proved"])

    def test_leakage_bounds_direct_sum_component(self):
        # Exact leakage may be nonzero despite global [T,C]=0.
        leak_tc=w.leakage(self.T,self.C,self.window)
        leak_ct=w.leakage(self.C,self.T,self.window)
        self.assertNotEqual(leak_tc,leak_ct)
        self.assertEqual(w.sub(leak_ct,leak_tc),
             w.commutator(w.compress(self.T,self.window),
                          w.compress(self.C,self.window)))

if __name__=="__main__":
    unittest.main()
