"""Exact Fourier/causal-self-model and reason/feel admissibility controls."""
import unittest
from dataclasses import replace
from fractions import Fraction
from random import Random

from observational_succ.principia_causal_memory import carrier,initial_memory,step_memory
from observational_succ.principia_reorientation import ReorientationTask,ring_with_beacon
from observational_succ.principia_semantic_core import make_cycle
from observational_succ.principia_dual_compass import (
    CompassError,GaussianRational,dft4,idft4,shift4,spectral_pairing,
    fourier_energy,fourier_autocorrelation,make_appraisal,model_self,
    verify_self,ring_projection,select_dual_compass,verify_dual_compass,
    affine_square_self_paths,cm_rotational_self_modes,
)


def bidirectional_ring(n=5):
    states=tuple('x'+str(i) for i in range(n))
    forward=tuple(states[(i+1)%n] for i in range(n))
    backward=tuple(states[(i-1)%n] for i in range(n))
    c=carrier('source-bidirectional-ring-'+str(n),states,states,
              ('east','west','stay'),states,
              tuple('beacon' if i==0 else 'dark' for i in range(n)),
              states,(forward,backward,states),costs=(1,1,0))
    return ReorientationTask(c,states)


class ExactFourierTests(unittest.TestCase):
    def test_invertible_fourier_on_rational_gaussian_vectors(self):
        rng=Random(11242026)
        for _ in range(120):
            x=tuple(GaussianRational(Fraction(rng.randrange(-4,5),3),
                                    Fraction(rng.randrange(-4,5),5)) for _ in range(4))
            self.assertEqual(idft4(dft4(x)),x)
            self.assertEqual(fourier_energy(x),sum(v.squared_abs() for v in x))
    def test_nonlocal_power_discarding_phase_loses_reference(self):
        x=(1,0,0,0);y=shift4(x,1)
        X,Y=dft4(x),dft4(y)
        self.assertNotEqual(X,Y)
        self.assertEqual(tuple(z.squared_abs() for z in X),
                         tuple(z.squared_abs() for z in Y))
        self.assertNotEqual(idft4(X),idft4(Y))
    def test_cyclic_shift_covariance_shared_gauge_invariance(self):
        x=(1,2,-1,3);y=(0,-2,4,5)
        self.assertEqual(spectral_pairing(x,y),spectral_pairing(shift4(x,2),shift4(y,2)))
        self.assertNotEqual(spectral_pairing(x,y),spectral_pairing(shift4(x,1),y))
        X=dft4(x);Y=dft4(shift4(x,1))
        for k in range(4):
            self.assertEqual(Y[k],X[k]*dft4((0,1,0,0))[k])
    def test_parseval_pairing_and_autocorrelation(self):
        x=(2,-1,0,3);y=(1,0,4,-2)
        self.assertEqual(spectral_pairing(x,y),GaussianRational(sum(a*b for a,b in zip(x,y))))
        C=fourier_autocorrelation(x)
        for lag in range(4):
            self.assertEqual(C[lag],GaussianRational(sum(x[j]*x[(j+lag)%4] for j in range(4))))


class EmbodiedSelfTests(unittest.TestCase):
    def test_self_spectrum_from_actual_action_memory(self):
        task=bidirectional_ring()
        c=task.carrier
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':2})
        m=initial_memory(c,'dark')
        m=step_memory(c,m,'east','dark')
        m=step_memory(c,m,'east','beacon')
        m=step_memory(c,m,'west','dark')
        x=model_self(c,m,scale)
        self.assertEqual(x.trace,(1,3,-3))
        self.assertEqual(x.slots,(1,3,-3,0))
        self.assertEqual(tuple(a.re for a in idft4(x.modes)),x.slots)
        self.assertEqual(verify_self(c,m,scale,x),x)
    def test_forged_spectrum_or_source_is_rejected(self):
        task=bidirectional_ring()
        c=task.carrier
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':2})
        m=initial_memory(c,'dark')
        m=step_memory(c,m,'east','dark')
        x=model_self(c,m,scale)
        with self.assertRaises(CompassError):verify_self(c,m,scale,replace(x,modes=dft4((0,0,0,0))))
        with self.assertRaises(CompassError):verify_self(c,m,scale,replace(x,source='fake'))
        with self.assertRaises(CompassError):model_self(c,m,replace(scale,source='fake'))
    def test_spectrum_is_a_projection_not_substitute_for_full_memory(self):
        # Two different chronological causal memories can have the same modulo-4 signal.
        self.assertEqual(ring_projection((1,0,0,0)),ring_projection((1,0,0,0,0)))
        self.assertNotEqual((1,0,0,0),(1,0,0,0,0))
    def test_actual_affine_square_nonzero_computational_paths(self):
        c=make_cycle(1,2)
        left,right=affine_square_self_paths(c)
        self.assertNotEqual(left,right)
        self.assertNotEqual(dft4(left),dft4(right))
        self.assertEqual(left,(1,0,0,0))
        self.assertEqual(right,(0,2,3,0))
        self.assertEqual(sum(left)-sum(right),-4)
    def test_actual_gaussian_theta_zero_hidden_nonzero_angular_mode(self):
        second,fourth=cm_rotational_self_modes()
        self.assertEqual(second[0],GaussianRational())
        self.assertEqual(second[2],GaussianRational(0,8))
        self.assertEqual(tuple(second[k] for k in (1,3)),(GaussianRational(),GaussianRational()))
        self.assertEqual(fourth[0],GaussianRational(-16))
        self.assertEqual(tuple(fourth[k] for k in (1,2,3)),(GaussianRational(),)*3)


class SafeDualCompassTests(unittest.TestCase):
    def test_feel_tiebreak_selects_only_reason_safe_actions(self):
        task=bidirectional_ring()
        c=task.carrier
        m=initial_memory(c,'dark')
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':1})
        templates={'east':(1,0,0,0),'west':(-1,0,0,0),'stay':(10,10,10,10)}
        d=select_dual_compass(task,m,scale,templates)
        self.assertIsNotNone(d.reason_rank)
        self.assertIn('east',d.safe_actions)
        self.assertIn('west',d.safe_actions)
        self.assertNotIn('stay',d.safe_actions)
        self.assertEqual(d.chosen_action,'east')
        self.assertEqual(verify_dual_compass(task,m,scale,templates,d),d)
    def test_history_changes_feel_tiebreak_while_reason_stays_correct(self):
        task=bidirectional_ring()
        c=task.carrier
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':0})
        templates={'east':(1,0,0,0),'west':(-1,0,0,0),'stay':(10,10,10,10)}
        m=initial_memory(c,'dark')
        m=step_memory(c,m,'west','dark')
        d=select_dual_compass(task,m,scale,templates)
        self.assertIn('west',d.safe_actions)
        self.assertEqual(d.chosen_action,'west')
        # With the reverse history, the subjective tie-break reverses without
        # changing the mathematical acceptability contract.
        m2=initial_memory(c,'dark')
        m2=step_memory(c,m2,'east','dark')
        d2=select_dual_compass(task,m2,scale,templates)
        self.assertEqual(d2.chosen_action,'east')
    def test_unrecoverable_world_cannot_be_saved_by_feeling(self):
        from observational_succ.principia_reorientation import homogeneous_ring
        task=homogeneous_ring(5)
        c=task.carrier
        m=initial_memory(c,'dark')
        scale=make_appraisal(c,{'forward':1},{'dark':0})
        d=select_dual_compass(task,m,scale,{'forward':(100,100,100,100)})
        self.assertIsNone(d.reason_rank)
        self.assertIsNone(d.chosen_action)
    def test_source_misalignment_or_template_wrong_rejected(self):
        task=bidirectional_ring()
        c=task.carrier
        m=initial_memory(c,'dark')
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':1})
        with self.assertRaises(CompassError):select_dual_compass(task,m,scale,{'east':(1,0,0,0)})
        with self.assertRaises(CompassError):make_appraisal(c,{'east':1},{'dark':0,'beacon':1})
        with self.assertRaises(CompassError):make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0})

class SelfDiscrepancyTests(unittest.TestCase):
    def test_raw_internal_report_cannot_be_confused_with_model_prediction(self):
        from observational_succ.principia_dual_compass import declare_self_readout,compare_self_discrepancy
        task=bidirectional_ring()
        c=task.carrier
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':1})
        m=initial_memory(c,'dark')
        m=step_memory(c,m,'east','dark')
        m=step_memory(c,m,'west','dark')
        report=declare_self_readout(c,m,(2,-1),instrument='declared-local-self-readout')
        res=compare_self_discrepancy(c,m,scale,report)
        self.assertEqual(res.prediction,(1,-1))
        self.assertEqual(res.reported,(2,-1))
        self.assertEqual(res.residual,(1,0))
        self.assertEqual(tuple(z.re for z in idft4(res.residual_modes)),(1,0,0,0))
        self.assertEqual(res.evidence_status,'declared-unvalidated-self-report')
    def test_measured_vs_modeled_mismatch_remains_visible(self):
        from observational_succ.principia_dual_compass import declare_self_readout,compare_self_discrepancy
        task=bidirectional_ring()
        c=task.carrier
        scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':1})
        m=initial_memory(c,'dark')
        m=step_memory(c,m,'east','dark')
        report=declare_self_readout(c,m,(-4,),instrument='user-declared')
        residual=compare_self_discrepancy(c,m,scale,report)
        self.assertEqual(residual.residual,(-5,))
        with self.assertRaises(CompassError):
            compare_self_discrepancy(c,m,scale,replace(report,source='different-source'))
        with self.assertRaises(CompassError):
            compare_self_discrepancy(c,m,scale,replace(report,samples=()))
        with self.assertRaises(CompassError):
            declare_self_readout(c,m,(1,2),instrument='user-declared')

class DynamicTransportTests(unittest.TestCase):
    def test_path_update_in_self_centered_fourier_frame(self):
        from observational_succ.principia_dual_compass import transported_relative_spectrum
        rng=Random(20261124)
        for _ in range(100):
            original=tuple(rng.randrange(-3,4) for _ in range(4))
            d=rng.randrange(-7,8); appraisal=rng.randrange(-5,6)
            relocated=list(shift4(original,-d))
            relocated[0]+=appraisal
            self.assertEqual(transported_relative_spectrum(dft4(original),d,appraisal),
                             dft4(relocated))
    def test_closed_route_does_not_erase_internal_self_history(self):
        from observational_succ.principia_dual_compass import transported_relative_spectrum
        original=dft4((0,0,0,0))
        one=transported_relative_spectrum(original,1,1)
        back=transported_relative_spectrum(one,-1,-1)
        self.assertNotEqual(back,original)
        self.assertEqual(tuple(z.re for z in idft4(back)),(-1,1,0,0))
    def test_changed_heading_changes_transport_phase(self):
        from observational_succ.principia_dual_compass import transported_relative_spectrum
        s=dft4((1,0,0,0))
        forward=transported_relative_spectrum(s,1,0)
        backward=transported_relative_spectrum(s,-1,0)
        self.assertNotEqual(forward,backward)
        self.assertEqual(tuple(z.squared_abs() for z in forward),
                         tuple(z.squared_abs() for z in backward))
