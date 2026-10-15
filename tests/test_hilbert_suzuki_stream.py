"""True signed Weil operator entries exactly traversed by finite Hilbert source."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ import hilbert_suzuki_stream as h
from observational_succ import source_weil_hierarchy as source
from observational_succ.hilbert_carrier import point


class GenuineHilbertWeilTests(unittest.TestCase):
    def test_true_small_source_matrix_is_recovered_entry_for_entry(self):
        for k in (1,2,3):
            st=h.source_stream(Q(1,2),4,k)
            N=2**k
            self.assertEqual(st.side,N)
            self.assertEqual(st.source_id,'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3')
            self.assertEqual(len(st.samples),N*N)
            self.assertFalse(st.all_test_weil_positive_proved)
            original=source.stage(Q(1,2),4,N)
            self.assertEqual(st.original_stage_center,original.center)
            for d,(i,j,z) in enumerate(st.samples):
                self.assertEqual((i,j),point(k,d))
                self.assertEqual(z,original.center[i][j])

    def test_original_signed_quadratic_is_order_invariant(self):
        st=h.source_stream(Q(1,2),3,3)
        for v in ((1,-1,0,0,0,0,0,0),(1,0,0,0,0,0,0,-1),
                  (1,1,-1,-1,0,0,0,0),(2,-1,-1,0,0,0,0,0)):
            cert=h.source_matrix_pair_witness(st,v)
            self.assertEqual(cert["signed_original_quadratic_rayleigh"],
                             cert["hilbert_stream_rayleigh"])
            self.assertTrue(cert["preserves_full_signed_source_matrix"])
            self.assertFalse(cert["positive_weil_certified"])

    def test_hilbert_consecutive_signed_source_bound(self):
        for a,k in ((Q(1,4),2),(Q(1,2),2),(Q(1,2),3),(Q(3,4),2)):
            st=h.source_stream(a,3,k)
            c=h.local_stream_bounds(st)
            self.assertLessEqual(c["hilbert_max_center_jump"],
                                 c["source_analytic_lipschitz_bound"])
            self.assertEqual(c["main_pinned"],h.MAIN_SOURCE_SHA)
            self.assertTrue(c["same_original_signed_matrix_recovered"])
            self.assertFalse(c["full_original_weil_sign_proved"])

    def test_source_gamma_one_sided_and_original_symmetric_error_not_changed(self):
        st=h.source_stream(Q(1,2),3,2)
        parent=source.stage(Q(1,2),3,4)
        self.assertEqual(st.original_operator_error,parent.norm_error)
        self.assertEqual(st.positive_gamma_tail_bound,
                         source.authentic_positive_gamma_tail_norm(3))
        self.assertEqual(st.spatial_error_without_positive_gamma_tail,
                         source.honest_spatial_error(parent))
        self.assertGreater(st.original_operator_error,st.spatial_error_without_positive_gamma_tail)

    def test_original_source_forgery_refused(self):
        st=h.source_stream(Q(1,2),3,2)
        for bad in (
            replace(st,source_id="AUXILIARY_GAUSSIAN_POSITIVE"),
            replace(st,source_origin_head="unverified-reference"),
            replace(st,original_operator_error=Q()),
            replace(st,samples=tuple(reversed(st.samples))),
            replace(st,samples=tuple((i,j,float(v)) for i,j,v in st.samples)),
            replace(st,original_stage_center=tuple(
                  tuple(float(v) for v in row) for row in st.original_stage_center)),
        ):
            with self.assertRaises(h.HilbertWeilError):
                h.local_stream_bounds(bad)

    def test_original_mean_zero_and_float_source_refused(self):
        st=h.source_stream(Q(1,2),3,2)
        with self.assertRaises(h.HilbertWeilError):
            h.source_matrix_pair_witness(st,(1,1,1,1))
        with self.assertRaises(h.HilbertWeilError):
            h.source_matrix_pair_witness(st,(1.0,-1,0,0))
        with self.assertRaises(h.HilbertWeilError):
            h.source_stream(.5,3,2)
        with self.assertRaises(h.HilbertWeilError):
            h.source_stream(Q(1,2),3,5)

    def test_no_hilbert_reordering_sign_claim(self):
        scope=h.source_interface_metadata()
        self.assertFalse(scope["rh_proved"])
        self.assertFalse(scope["negative_spectral_depth_improvement"]!="NONE_FROM_REORDERING_ALONE")
        self.assertEqual(scope["Sobolev_H01_transport"],"NOT_IDENTIFIED_OR_PRESERVED")


if __name__=="__main__":
    unittest.main()
