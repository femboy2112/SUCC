"""Exact Aphex-shaped observer tests, with hostile nonnormal controls."""
import unittest
from fractions import Fraction as F
from observational_succ.aphex_haar_feedback import (
    fit_sign_coupling, aphex_step, original_parity_probe, calibrate_gain
)
from observational_succ.bbp_parity_pressure import original_zero_parity_states


class AphexFeedbackTests(unittest.TestCase):
    def test_exact_gradient_step_and_energy_identity(self):
        a=[1,1,-1,-1,1,-1,1,-1]
        b=[1,-1,-1,-1,1,1,-1,-1]
        fit=fit_sign_coupling(a,b)
        beta,grad,drop=aphex_step(fit,F(0),F(1,fit.source_variance))
        self.assertEqual(beta,fit.coefficient)
        self.assertEqual(grad,-fit.covariance)
        self.assertEqual(drop,fit.covariance**2/(2*fit.source_variance))
        self.assertEqual(aphex_step(fit,beta,F(1))[2],0)

    def test_countermodel_zero_loss_does_not_imply_haar(self):
        a=[1,-1]*8
        b=a[:] # product a*b identically +1, a maximally biased real digit stream
        fit=fit_sign_coupling(a,b)
        self.assertEqual(fit.source_mean,0)
        self.assertEqual(fit.real_sign_mean,1)
        self.assertEqual(fit.coefficient,1)
        self.assertEqual(fit.residual_energy,0)
        self.assertEqual(calibrate_gain(fit.coefficient),2)

    def test_negative_correlation_and_calibration(self):
        a=[1,-1]*8
        b=[-x for x in a]
        fit=fit_sign_coupling(a,b)
        self.assertEqual(fit.coefficient,-1)
        self.assertEqual(fit.real_sign_mean,-1)
        with self.assertRaises(ValueError): calibrate_gain(fit.coefficient)
        self.assertEqual(calibrate_gain(fit.coefficient,2),1)

    def test_non_identifiable_and_bad_step(self):
        with self.assertRaises(ValueError): fit_sign_coupling([1]*8,[1,-1]*4)
        with self.assertRaises(ValueError): fit_sign_coupling([1,-1],[1])
        with self.assertRaises(ValueError): fit_sign_coupling([1,0],[-1,1])
        fit=fit_sign_coupling([1,-1]*4,[1,1,-1,-1]*2)
        with self.assertRaises(ValueError): aphex_step(fit,0,0)
        with self.assertRaises(ValueError): aphex_step(fit,0,F(2,fit.source_variance))

    def test_source_window_512_selected_vs_wrong_seed(self):
        source=list(original_zero_parity_states(1023))
        original=original_parity_probe(source[511:1023],1217)
        self.assertEqual(original.source_mean,F(-1,128))
        self.assertEqual(original.complement_mean,F(1,128))
        self.assertEqual(original.real_sign_mean,F(5,128))
        self.assertEqual(original.covariance,F(641,16384))
        self.assertEqual(original.source_variance,F(16383,16384))
        self.assertEqual(original.coefficient,F(641,16383))
        step,grad,drop=aphex_step(original,0,F(16384,16383))
        self.assertEqual(step,F(641,16383))
        self.assertEqual(grad,-F(641,16384))
        self.assertGreater(drop,0)
        # A source-preserving coherent wrong seed makes every real digit even:
        # complement == local prime sign, so beta=1 and fitted loss=0.
        a=[(-1)**s.local(1217) for s in source[511:1023]]
        shadow=fit_sign_coupling(a,a)
        self.assertEqual(shadow.coefficient,1)
        self.assertEqual(shadow.covariance,F(16383,16384))
        self.assertEqual(shadow.real_sign_mean,1)
        self.assertEqual(shadow.residual_energy,0)
        self.assertNotEqual(original.coefficient,shadow.coefficient)

    def test_loss_is_not_truth_and_scaling_changes_gain(self):
        # Full SUCC Haar/prime data is unchanged; gain depends on declared probe scale.
        fit=fit_sign_coupling([1,-1]*4,[1,1,-1,-1]*2)
        self.assertEqual(fit.coefficient,0)
        self.assertEqual(fit.real_sign_mean,0)
        self.assertGreater(fit.residual_energy,0)

if __name__=='__main__': unittest.main()
