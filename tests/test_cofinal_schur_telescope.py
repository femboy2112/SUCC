"""Exact adversarial tests for the finite-model cofinal Schur telescope."""
from __future__ import annotations

import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product

from observational_succ.cofinal_schur_telescope import (
    TelescopeError, ConditionalSourceEnvelope, DiagonalToy, FiniteCarrier,
    add, diag, exact, matrix, minor_det, mul, psd, search_toy, trans,
    genuine_source_obligations,
)


def model(kappa=Q(1)):
    v=diag((Q(1,2),Q(1,3)))
    r=tuple(tuple(-q for q in row) for row in v)
    y=((-1,-1),(-1,1))
    b=tuple(tuple(-q for q in row) for row in mul(trans(v),matrix(y)))
    return FiniteCarrier(((2,1),(1,2)),b,mul(v,v),v,y,r,kappa)


def packet(**kwargs):
    base=dict(
        source_sha='0cc8510b71d178fc79e8d410a86d8b6014cf9178',
        radius=Q(1,2),
        channels=('prime2_half_density','real_gamma','pole_plus','pole_minus','contact'),
        low_metric=(Q(1,3),Q(1,5),Q(1,7),Q(1,9)),
        center=diag((Q(1,20),Q(1,10),Q(1,15),Q(1,25))),
        energy_operator_error=Q(1,1000),
        residual_trace_upper=Q(1,100),
        kappa=Q(20699,1000000),
        premises=genuine_source_obligations(),
    )
    return ConditionalSourceEnvelope(**dict(base,**kwargs))


class ExactAlgebraTests(unittest.TestCase):
    def test_all_principal_minors_reject_indefinite(self):
        self.assertFalse(psd(((1,2),(2,1))))
        self.assertFalse(psd(((0,1),(1,0))))
        self.assertTrue(psd(((1,1),(1,1))))
        self.assertTrue(psd(((2,1),(1,2))))

    def test_nonsymmetric_no_certificate(self):
        self.assertFalse(psd(((1,0),(1,1))))

    def test_three_dimensional_indefinite(self):
        self.assertFalse(psd(((1,0,0),(0,0,1),(0,1,0))))

    def test_zero_and_singular_det(self):
        self.assertEqual(minor_det(((1,1),(1,1))),0)
        self.assertEqual(minor_det(((2,1),(1,3))),5)

    def test_reject_inexact_boolean_and_float(self):
        for value in (True,False,0.1):
            with self.subTest(value=value),self.assertRaises(TelescopeError):exact(value)

    def test_rectangular_matrix_wrong_dimensions(self):
        with self.assertRaises(TelescopeError):matrix(((1,2),(3,)),height=2)
        with self.assertRaises(TelescopeError):matrix(((1,2),),height=2)

    def test_exact_cross_column_recovery(self):
        x=model()
        self.assertEqual(x.actual_short(),((Q(),Q(1)),(Q(1),Q())))
        self.assertFalse(psd(x.actual_short()))
        self.assertTrue(psd(x.D))

    def test_finite_zero_trial_no_ghost_negativity(self):
        x=model().trial(((0,0),(0,0)))
        self.assertTrue(psd(add(x.upper,x.reference_short,scale=-1)))
        self.assertTrue(psd(add(x.reference_short,x.lower,scale=-1)))
        self.assertEqual(x.residual_gram,((2,0),(0,2)))
        self.assertFalse(x.source_authenticated)

    def test_finite_exact_trial_converges(self):
        x=model().trial(((2,2),(3,-3)))
        self.assertEqual(x.residual_gram,((0,0),(0,0)))
        self.assertEqual(x.lower,x.upper)
        self.assertEqual(x.upper,x.reference_short)

    def test_all_small_rational_trials_satisfy_bracket(self):
        carrier=model(kappa=Q(1,2))
        for a,b,c,d in product((-1,0,1),repeat=4):
            trial=carrier.trial(((a,b),(c,d)))
            self.assertTrue(psd(add(trial.upper,trial.reference_short,scale=-1)))
            self.assertTrue(psd(add(trial.reference_short,trial.lower,scale=-1)))

    def test_source_B_identity_mutant(self):
        base=model()
        bad=add(base.B,((Q(1),Q()),(Q(),Q())))
        with self.assertRaisesRegex(TelescopeError,'wrong source B'):
            FiniteCarrier(base.A,bad,base.D,base.V,base.Y,base.R,base.kappa)

    def test_source_D_identity_mutant(self):
        base=model()
        bad=add(base.D,((Q(1),Q()),(Q(),Q())))
        with self.assertRaisesRegex(TelescopeError,'wrong source D'):
            FiniteCarrier(base.A,base.B,bad,base.V,base.Y,base.R,base.kappa)

    def test_coercivity_mutant(self):
        base=model()
        with self.assertRaisesRegex(TelescopeError,'coercivity'):
            FiniteCarrier(base.A,base.B,base.D,base.V,base.Y,base.R,Q(2))

    def test_zero_coercivity_mutant(self):
        with self.assertRaises(TelescopeError):model(kappa=Q())

    def test_unpaired_report_mutant(self):
        base=model()
        with self.assertRaises(TelescopeError):
            FiniteCarrier(base.A,base.B,base.D,base.V,((-1,-1),(-1,2)),base.R,base.kappa)


class ConditionalSourceAuthorityTests(unittest.TestCase):
    def test_source_packet_no_promotion(self):
        e=packet()
        report=e.bracket()
        self.assertEqual(report['width_in_W_operator_norm'],Q(1,500)+Q(10000,20699))
        self.assertEqual(report['authority'],'CONDITIONAL_ON_SUPPLIED_SOURCE_ENCLOSURES')
        self.assertFalse(report['source_identification_authenticated'])
        self.assertFalse(report['completed_Weil_sign_established'])
        self.assertFalse(report['RH_proved'])

    def test_wrong_source_blob_rejected(self):
        with self.assertRaises(TelescopeError):packet(source_sha='a'*40)

    def test_wrong_radius_rejected(self):
        with self.assertRaises(TelescopeError):packet(radius=Q(3,4))

    def test_wrong_metric_rejected(self):
        with self.assertRaises(TelescopeError):packet(low_metric=(1,1,1,1))

    def test_missing_signed_channels_rejected(self):
        with self.assertRaises(TelescopeError):packet(channels=('real_gamma','prime2_half_density'))

    def test_negative_residual_error_rejected(self):
        with self.assertRaises(TelescopeError):packet(residual_trace_upper=Q(-1,3))

    def test_negative_energy_error_rejected(self):
        with self.assertRaises(TelescopeError):packet(energy_operator_error=Q(-1,3))

    def test_missing_premises_rejected(self):
        with self.assertRaises(TelescopeError):packet(premises=())

    def test_forged_certain_positive_not_promoted(self):
        e=packet(energy_operator_error=0,residual_trace_upper=0)
        r=e.bracket()
        self.assertEqual(r['width_in_W_operator_norm'],0)
        self.assertFalse(r['source_identification_authenticated'])
        self.assertFalse(r['completed_Weil_sign_established'])


class InfiniteSyntheticControls(unittest.TestCase):
    def test_delayed_offline_mode_hidden_for_all_shallow_stages(self):
        toy=DiagonalToy('delayed',delay=37)
        for n in range(37):
            r=toy.stage(n)
            self.assertEqual(r['upper'],Q(1,2))
            self.assertLess(r['lower'],0)
            self.assertGreater(r['upper'],0)
            self.assertFalse(r['original_Weil_authenticated'])
        self.assertEqual(toy.stage(37)['upper'],Q(-1,2))

    def test_delayed_sign_budget_false_unknown(self):
        r=search_toy(DiagonalToy('delayed',delay=37),sign=True,max_stage=36)
        self.assertEqual(r['status'],'BUDGET_UNRESOLVED')
        r=search_toy(DiagonalToy('delayed',delay=37),sign=True,max_stage=37)
        self.assertEqual(r['status'],'CERTIFIED_NEGATIVE_SYNTHETIC')
        self.assertEqual(r['stage'],37)

    def test_delayed_variation_retains_sharp_schur(self):
        toy=DiagonalToy('delayed',delay=11)
        self.assertEqual(toy.stage(11)['lower'],Q(-1,2))
        self.assertEqual(toy.stage(11)['response_norm_squared'],Q(2)**22)

    def test_unbounded_positive_sign_reaches_a_finite_stage(self):
        toy=DiagonalToy('unbounded')
        r=search_toy(toy,sign=True,max_stage=12)
        self.assertEqual(r['status'],'CERTIFIED_POSITIVE_SYNTHETIC')

    def test_unbounded_response_and_residual(self):
        toy=DiagonalToy('unbounded')
        self.assertEqual(toy.stage(10)['response_norm_squared'],385)
        self.assertEqual(toy.stage(20)['response_norm_squared'],2870)
        self.assertEqual(toy.stage(10)['residual_upper'],Q(1,10))
        self.assertLess(toy.stage(20)['residual_upper'],toy.stage(10)['residual_upper'])

    def test_unbounded_accuracy_without_apriori_rate(self):
        r=search_toy(DiagonalToy('unbounded'),accuracy=Q(1,10),max_stage=20)
        self.assertEqual(r['status'],'ACCURACY_CERTIFIED_SYNTHETIC')
        self.assertEqual(r['stage'],11)

    def test_singular_zero_never_strict_sign(self):
        toy=DiagonalToy('singular')
        for n in range(12):
            r=toy.stage(n)
            self.assertEqual(r['upper'],-r['lower'])
            self.assertGreater(r['upper'],0)
            self.assertLess(r['lower'],0)
        result=search_toy(toy,sign=True,max_stage=20)
        self.assertEqual(result['status'],'BUDGET_UNRESOLVED')

    def test_singular_accuracy_still_terminates(self):
        toy=DiagonalToy('singular')
        r=search_toy(toy,accuracy=Q(1,1000),max_stage=10)
        self.assertEqual(r['status'],'ACCURACY_CERTIFIED_SYNTHETIC')
        self.assertLess(r['width'],Q(1,1000))

    def test_singular_response_blowup_despite_narrowing(self):
        toy=DiagonalToy('singular')
        self.assertGreater(toy.stage(8)['response_norm_squared'],toy.stage(6)['response_norm_squared'])
        self.assertLess(toy.stage(8)['width'],toy.stage(6)['width'])

    def test_source_type_not_Weil(self):
        for mode in ('delayed','unbounded','singular'):
            self.assertEqual(DiagonalToy(mode).stage(8)['source'],'EXPLICIT_SYNTHETIC_DIAGONAL')

    def test_reject_bad_accuracy_and_budget(self):
        with self.assertRaises(TelescopeError):search_toy(DiagonalToy('singular'),accuracy=0)
        with self.assertRaises(TelescopeError):search_toy(DiagonalToy('singular'),accuracy=Q(1,4),max_stage=-1)
        with self.assertRaises(TelescopeError):search_toy(DiagonalToy('delayed'))
        with self.assertRaises(TelescopeError):DiagonalToy('bad')


if __name__=='__main__':
    unittest.main()
