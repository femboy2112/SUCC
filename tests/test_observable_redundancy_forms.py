"""Exact positive/negative probes for observationally redundant auxiliary states."""
import unittest
from fractions import Fraction as F

from observational_succ.observable_redundancy_forms import (
    ObservableRedundancyError, ExactSourceExtension, redundancy_controls,
)


class ObservableRedundancyFormsTests(unittest.TestCase):
    def test_null_auxiliary_extension_can_be_forgotten_even_if_source_negative(self):
        for signed in (F(-7,3),F(0),F(2,5),F(5)):
            m=ExactSourceExtension(1,((signed,0,0),(0,0,0),(0,0,0)))
            rec=m.form_descends()
            self.assertTrue(rec["full_source_form_factors_through_quotient"])
            self.assertEqual(rec["unique_descended_form"],((signed,),))
            self.assertFalse(rec["hidden_acyclicity_would_imply_this"])
            self.assertFalse(rec["completed_Weil_form_identified"])

    def test_contractible_positive_auxiliary_energy_not_null_in_source_form(self):
        # A positive hidden Hilbert space cannot be deleted as ZERO information
        # from the same nondegenerate source quadratic form.
        x=ExactSourceExtension(1,((2,0,0),(0,1,0),(0,0,1)))
        self.assertFalse(x.form_descends()["full_source_form_factors_through_quotient"])
        self.assertIsNone(x.form_descends()["unique_descended_form"])
        y=ExactSourceExtension(1,((2,0),(0,0)))
        self.assertTrue(y.form_descends()["full_source_form_factors_through_quotient"])

    def test_hidden_visible_coupling_prevents_bilinear_descent(self):
        x=ExactSourceExtension(1,((2,1),(1,0)))
        self.assertFalse(x.form_descends()["full_source_form_factors_through_quotient"])
        # Even with hidden diagonal zero, mixed cross term is visible.
        self.assertEqual(x.signed_form[0][1],F(1))

    def test_dynamics_preserve_quotient_iff_hidden_kernel_invariant(self):
        q=ExactSourceExtension(1,((5,0),(0,0)))
        good=((1,0),(3,1))
        bad=((1,1),(0,1))
        r=q.dynamics_descend(good)
        self.assertTrue(r["full_source_dynamics_descends"])
        self.assertEqual(r["descended_visible_operator"],((F(1),),))
        self.assertFalse(q.dynamics_descend(bad)["full_source_dynamics_descends"])
        self.assertIsNone(q.dynamics_descend(bad)["descended_visible_operator"])
        # First step may store information into hidden, second reveals it.
        start=(F(1),F(0))
        stored=(good[0][0]*start[0]+good[0][1]*start[1],
                good[1][0]*start[0]+good[1][1]*start[1])
        revealed=(bad[0][0]*stored[0]+bad[0][1]*stored[1],
                  bad[1][0]*stored[0]+bad[1][1]*stored[1])
        self.assertEqual(stored,(F(1),F(3)))
        self.assertEqual(revealed,(F(4),F(3)))

    def test_exact_negative_schur_despite_positive_hidden_fiber(self):
        a=ExactSourceExtension(1,((1,2),(2,1)))
        r=a.schur_shorting()
        self.assertEqual(r["hidden_coupling_correction"],((F(4),),))
        self.assertEqual(r["effective_source_form"],((F(-3),),))
        self.assertFalse(r["effective_form_PSD"])
        self.assertFalse(r["full_enlarged_form_PSD"])
        self.assertTrue(r["hidden_C_positive_definite"])
        self.assertFalse(r["source_to_actual_Weil_distribution_proved"])

    def test_positive_schur_proved_when_full_source_positive(self):
        a=ExactSourceExtension(1,((5,2),(2,1)))
        r=a.schur_shorting()
        self.assertEqual(r["effective_source_form"],((F(1),),))
        self.assertTrue(r["effective_form_PSD"])
        self.assertTrue(r["full_enlarged_form_PSD"])
        self.assertEqual(r["hidden_coupling_correction"],((F(4),),))

    def test_independent_two_hidden_channel_rational_schur(self):
        # A=5; B=[2,1]; C=diag(2,1); penalty=2+1=3, W_eff=2.
        x=ExactSourceExtension(1,((5,2,1),(2,2,0),(1,0,1)))
        r=x.schur_shorting()
        self.assertEqual(r["hidden_coupling_correction"],((F(3),),))
        self.assertEqual(r["effective_source_form"],((F(2),),))
        self.assertTrue(r["effective_form_PSD"])
        self.assertTrue(r["full_enlarged_form_PSD"])
        # Independent direct minimizer y=-C^-1 B^T x at x=1: (-1,-1).
        v=(F(1),F(-1),F(-1))
        Q=sum(v[i]*x.signed_form[i][j]*v[j] for i in range(3) for j in range(3))
        self.assertEqual(Q,F(2))

    def test_full_source_block_psd_is_not_inferred_from_block_positive(self):
        r=redundancy_controls()
        self.assertTrue(r["source_signed_null_extension_can_descend_even_if_negative"])
        self.assertTrue(r["negative_source_recovered_after_null_extension"])
        self.assertEqual(r["positive_hidden_C_indefinite_full_example"]["effective_source_form"],((-3,),))
        self.assertTrue(r["positive_full_source_example"]["effective_form_PSD"])
        self.assertEqual(r["hidden_probe_exposure"],(True,False))
        self.assertFalse(r["auxiliary_positivity_implies_completed_Weil"])

    def test_reject_hidden_singular_shortcut_and_wrong_source_types(self):
        x=ExactSourceExtension(1,((2,0),(0,0)))
        with self.assertRaises(ObservableRedundancyError):
            x.schur_shorting()
        y=ExactSourceExtension(1,((2,0),(0,-1)))
        with self.assertRaises(ObservableRedundancyError):
            y.schur_shorting()
        for matrix in (((1,0),(0,1.2)),((1,2),(0,1)),((1,0),),((1,0,0),(0,1,0))):
            with self.assertRaises(ObservableRedundancyError):
                ExactSourceExtension(1,matrix)
        with self.assertRaises(ObservableRedundancyError):
            ExactSourceExtension(True,((1,0),(0,1)))
        with self.assertRaises(ObservableRedundancyError):
            ExactSourceExtension(1,((1,0),(0,1)),source_id="")
        with self.assertRaises(ObservableRedundancyError):
            ExactSourceExtension(1,((1,0),(0,1)),epoch=True)
        with self.assertRaises(ObservableRedundancyError):
            ExactSourceExtension(1,((1,0),(0,1))).dynamics_descend(((1,0,0),(0,1,0),(0,0,1)))


if __name__=="__main__":
    unittest.main()
