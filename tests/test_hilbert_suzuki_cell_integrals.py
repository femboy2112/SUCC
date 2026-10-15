"""Full finite-J genuine Suzuki g_J: cell-average Gamma, prime, pole and contact."""
import unittest
from fractions import Fraction as Q

from observational_succ import hilbert_suzuki_cell_integrals as h
from observational_succ import source_weil_hierarchy as src


def overlap(a,b,c,d):
    return max(a,c)<=min(b,d)


class GenuineSuzukiIntegralTests(unittest.TestCase):
    def test_real_gamma_ou_crosses_absolute_value_diagonal_exactly(self):
        rect=(Q(0),Q(1),Q(0),Q(1))
        k=h.genuine_ou_rect(rect,Q(1))
        # Independent classical double integral: 2e^-1 on unit square.
        ref=2*src.exp_neg(Q(1))
        self.assertTrue(overlap(k.lo,k.hi,ref.lo,ref.hi))
        self.assertGreater(k.lo,0)
        self.assertLess(k.hi,1)
        self.assertLess(k.hi-k.lo,Q(1,10**20))

    def test_original_finite_Gamma_rung_integral_negative_pointwise(self):
        rect=(Q(0),Q(1),Q(0),Q(1))
        for J in (1,2,3,5):
            g=h.genuine_gamma_rect(rect,J)
            self.assertLess(g.hi,0)
            self.assertLess(g.lo,g.hi)

    def test_exact_full_source_block_symmetric_and_typed(self):
        for a,k,J in ((Q(1,4),2,2),(Q(1,2),2,3),(Q(1,2),3,2),(Q(1),2,2)):
            block=h.hilbert_source_complete_block(a,k,J)
            self.assertTrue(block["all_original_source_components"])
            self.assertTrue(block["full_cell_integrals_without_midpoint_sampling"])
            self.assertEqual(block["compressed_block_spatial_quadrature_error"],0)
            self.assertFalse(block["continuum_finite_projection_norm_error_proved_zero"])
            self.assertFalse(block["original_infinite_Gamma_tail_included"])
            self.assertFalse(block["completed_Weil_PSD_proved"])
            self.assertFalse(block["rh_proved"])
            low=block["lower_matrix"]
            hi=block["upper_matrix"]
            n=1<<k
            self.assertEqual(len(low),n)
            self.assertEqual(len(hi),n)
            for i in range(n):
                for j in range(n):
                    self.assertLessEqual(low[i][j],hi[i][j])
                    self.assertEqual(low[i][j],low[j][i])
                    self.assertEqual(hi[i][j],hi[j][i])

    def test_parent_midpoint_analytic_error_encloses_integrated_exact_block(self):
        for a,k,J in ((Q(1,4),2,2),(Q(1,2),2,3),(Q(1,2),3,2)):
            whole=h.hilbert_source_complete_block(a,k,J)
            orig=src.stage(a,J,1<<k)
            n=1<<k
            width=2*a/n
            bound=width*width*src.lipschitz_safe(a,J)+width*orig.kernel_entry_radius
            for i in range(n):
                for j in range(n):
                    lo=whole["lower_matrix"][i][j]
                    hi=whole["upper_matrix"][i][j]
                    center=orig.center[i][j]
                    self.assertLessEqual(lo,center+bound)
                    self.assertGreaterEqual(hi,center-bound)

    def test_hilbert_full_finite_source_readout_retains_original_prime_power(self):
        a=Q(1,2)
        st=h.hilbert_source_complete_block(a,2,3)
        self.assertEqual(st["original_prime_power_tape"],((2,2),))
        sample=h.full_source_cell(a,2,0,3,3)
        self.assertEqual(sample.source, "AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3")
        self.assertEqual(sample.prime_power_source,((2,2),))
        self.assertFalse(sample.positive_full_weil_proved)
        self.assertEqual(sample.spatial_quadrature_error,0)

    def test_wrong_prime_fake6_and_bad_sources_rejected(self):
        for fn in (
            lambda:h.full_source_cell(0.5,2,0,3,3),
            lambda:h.full_source_cell(Q(1,2),5,0,3,3),
            lambda:h.full_source_cell(Q(1,2),2,0,3,0),
            lambda:h.full_source_cell(Q(1,2),2,0,4,2),
            lambda:h.hilbert_source_complete_block(Q(1,2),4,2),
            lambda:h.genuine_ou_rect((Q(1),Q(0),Q(0),Q(1)),Q(1)),
        ):
            with self.assertRaises((h.SuzukiCellIntegralError,
                                    h.HilbertHingeError)):fn()
        with self.assertRaises(src.WeilHierarchyError):
            src.assert_original_source_tape(src.AUTHENTIC_TAPE+((6,6),))

    def test_optional_independent_original_signed_g_j_diagonal_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional original numerical research diagnostic")
        from observational_succ.gaussian_weil_certificates import signed_suzuki_g
        mp.mp.dps=55
        a=Q(1,2);k=1;J=2
        cell=h.full_source_cell(a,k,0,0,J)
        width=mp.mpf("0.5")
        original=mp.quad(lambda r:
            2*(width-r)*signed_suzuki_g(r,J,dps=55),[0,width])/width
        lo=mp.mpf(cell.value_lower.numerator)/cell.value_lower.denominator
        hi=mp.mpf(cell.value_upper.numerator)/cell.value_upper.denominator
        self.assertLessEqual(lo,original)
        self.assertGreaterEqual(hi,original)


if __name__=="__main__":
    unittest.main()
