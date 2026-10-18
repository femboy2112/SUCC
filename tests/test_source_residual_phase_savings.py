"""Source-typed signed Suzuki center/edge residual transfer, CONDITIONAL PR161.

SOURCE-EDGE high Bessel-surplus comparison is an explicit sibling-draft
premise, not independently imported or rebuilt here. Never elevate this to
unconditional Suzuki positivity.
"""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ import source_residual_phase_savings as P
from observational_succ import original_continuum_residual as R


class ExactPhaseIntervalLogic(unittest.TestCase):
    def test_center_edge_fixed_probe_orthogonality(self):
        for name in ("odd_derivative","even_derivative"):
            f=P.orthogonal_center_edge_features(name)
            self.assertEqual(len(f["edge"]),2)
            self.assertEqual(f["edge"][0][1],F(1,8))
            self.assertEqual(f["edge"][1][1],F(1,6144))
            self.assertEqual(f["center"][1],F(1,4) if name=="odd_derivative" else F(1,768))
        with self.assertRaises(P.PhaseSavingError):
            P.orthogonal_center_edge_features("fake")

    def test_robust_rational_matrix_holds_at_hostile_interval_corners(self):
        m=(F(3,7),F(-4,5))
        e=(F(1,12),F(1,15))
        N=F(1,8)
        Q=P.robust_feature_lower(m,e,N,theta=F(1,2))
        for c in ((F(1),F(0)),(F(0),F(1)),(F(1),F(1)),
                  (F(1),F(-1)),(F(-2,3),F(4,7))):
            floor=sum(c[i]*Q[i][j]*c[j] for i in range(2) for j in range(2))
            for sigma in product((-1,1),repeat=2):
                actual=sum((m[k]+sigma[k]*e[k])*c[k] for k in range(2))
                self.assertLessEqual(floor,actual*actual/N)

    def test_zero_observation_cannot_gain_positive_lower(self):
        Q=P.robust_feature_lower((F(0),F(0)),(F(1,8),F(1,4)),F(1,2))
        self.assertLessEqual(Q[0][0],0)
        self.assertLessEqual(Q[1][1],0)
        self.assertFalse(P._is_psd(Q))
        with self.assertRaises(P.PhaseSavingError):
            P.robust_feature_lower((1,2),(0,0),1,theta=0)
        with self.assertRaises(P.PhaseSavingError):
            P.robust_feature_lower((1,2),(-1,0),1)

    def test_source_window_mutants_fail_before_rh_bridge(self):
        p={"b":F(693,1000),"db":F(1,10**6)}
        self.assertEqual(P.positive_source_regions(p),
                         ((-F(1,8),F(1,8)),(F(1,4),F(3,8))))
        for bad in (F(3,5),F(1,2),F(4,5)):
            with self.assertRaises(P.PhaseSavingError):
                P.positive_source_regions({"b":bad,"db":F(1,10**6)})

    def test_projection_removes_all_four_original_primitive_moments(self):
        pieces=(( -F(1,2), F(1,2), (F(1),F(-3),F(2),F(4),F(3),F(1))),)
        projected=P.projected_action_pieces(pieces)
        self.assertTrue(all(v==0 for v in R.projected_piece_moments(projected)))

    def test_rational_signed_matrix_floor_not_fake_psd(self):
        A=((F(-2),F(1,8)),(F(1,8),F(-3)))
        self.assertFalse(P._is_psd(A))
        self.assertLess(P._exact_2d_gershgorin_floor(A),0)
        with self.assertRaises(P.PhaseSavingError):
            P._exact_2d_gershgorin_floor(((1,2),(0,1)))


class OriginalSignedSourceConditionalComparison(unittest.TestCase):
    def test_original_centers_and_edges_and_conditional_source_labels(self):
        params=R.source_parameters()
        P.positive_source_regions(params)
        c=P.source_conditional_phase_saving(J=8,M=80,P=18)
        self.assertEqual(c["original_source_SHA"],R.SOURCE_SHA)
        self.assertTrue(c["genuine_prime_half_density_preserved"])
        self.assertTrue(c["has_sibling_PR161_arithmetic_high_surplus_PAPER_PREMISE"])
        self.assertFalse(c["source_original_S4_unconditional_sign_proved"])
        self.assertFalse(c["RH_proved"])
        self.assertEqual(set(c["parity_comparisons"]),
                         {"odd_derivative","even_derivative"})
        for name,z in c["parity_comparisons"].items():
            self.assertEqual(len(z["edge_test_rows"]),2)
            self.assertEqual(len(z["central_feature_nominal"]),2)
            self.assertEqual(z["inherited_prime2_surplus_weight_floor"],"12/25")
            self.assertTrue(z["source_high_surplus_comparator_is_SIBLING_PR161_CONDITIONAL"])
            self.assertFalse(z["chosen_Schur_lower_PSD_certified"]
                             and not c["conditional_first_window_S4_PSD"])
            self.assertGreaterEqual(F(z["chosen_Schur_lower"][0][0]),
                                     min(F(z["old_original_Schur_lower"][0][0]),
                                         F(z["new_conditional_source_Schur_lower"][0][0])))
        self.assertFalse(c["RH_proved"])


if __name__=="__main__":
    unittest.main()
