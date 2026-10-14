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
