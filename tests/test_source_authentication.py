"""Bounded exact and executable tests for a source-contact frontier."""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import copy
import importlib.util
import unittest

from observational_succ.source_authentication import (
    ACTIONS, CREDITS, ModelEvidence, source_instruments,
    choose_registered_action, fixed_policy_null_census, brier_binary,
    field_axes, tagged_source_transcript, delayed_mutant,
)
from observational_succ.recursive_observer import initial_pairs,update_pair,run_trace

HERE=Path(__file__).resolve().parent.parent/'research'/'2026-11-14'/'source_auth_field_frontier'
import sys
sys.path.insert(0,str(HERE))
from independent_replay import ReplayError, validate_session
from run_live_holdout import run_session


class SourceAuthenticationTests(unittest.TestCase):
    def test_J_law_has_source_and_obs_coupled(self):
        p=source_instruments(Q(3,4))
        self.assertEqual(tuple(inst.cost for inst in p),(Q(2),Q(1),Q(4)))
        self.assertEqual(p[0].joint[0][0],(Q(3,4),Q(1,4)))
        self.assertEqual(p[0].joint[1][1],(Q(1,4),Q(3,4)))
        self.assertEqual(p[1].joint[1][0],(Q(1),))
        self.assertEqual(p[2].joint[1][0],(Q(1,4),Q(3,4)))
        self.assertEqual(p[2].transition,((Q(1),Q(0)),(Q(1),Q(0))))

    def test_post_state_factorization_reset_fails(self):
        a=source_instruments(Q(3,4))
        self.assertIsNotNone(a[0].post_state_likelihood())
        self.assertIsNone(a[2].post_state_likelihood())

    def test_binary_posterior_and_history(self):
        inst=source_instruments(Q(3,4))[0]
        z,new=update_pair(initial_pairs((Q(1,2),Q(1,2))),inst,0)
        self.assertEqual(z,Q(1,2))
        self.assertEqual(tuple(sum(r,Q(0)) for r in new),(Q(3,4),Q(1,4)))
        reset=source_instruments(Q(3,4))[2]
        z,past=update_pair(initial_pairs((Q(1,2),Q(1,2))),reset,1)
        self.assertEqual(z,Q(1,2))
        self.assertEqual(tuple(sum(r,Q(0)) for r in past),(Q(1,4),Q(3,4)))
        self.assertEqual(tuple(sum(r[x] for r in past) for x in range(2)),(Q(1),Q(0)))

    def test_single_step_predeclared_evalue(self):
        m=ModelEvidence()
        self.assertEqual(m.action(),'sense')
        self.assertEqual(m.predictive('sense'),((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2))))
        self.assertEqual(m.record('sense',1),Q(1))
        self.assertEqual(m.beliefs[0],(Q(1,4),Q(3,4)))
        self.assertEqual(m.beliefs[1],(Q(1,2),Q(1,2)))
        self.assertEqual(m.credit_total,2)

    def test_feedback_policy_depends_on_observer_belief(self):
        self.assertEqual(choose_registered_action(4,(Q(2,3),Q(1,3))),'reset')
        self.assertEqual(choose_registered_action(4,(Q(1,3),Q(2,3))),'flip')
        self.assertEqual(choose_registered_action(5,(Q(1,3),Q(2,3))),'sense')

    def test_policy_disallows_hidden_oracle(self):
        model=ModelEvidence()
        with self.assertRaises(ValueError):model.record('reveal_source',0)
        with self.assertRaises(ValueError):model.record('reset',0)
        with self.assertRaises(ValueError):model.record('sense',17)

    def test_null_martingale_exact_adaptive(self):
        for h in range(8):
            r=fixed_policy_null_census(h,Q(4))
            self.assertEqual(r['null_E_L'],Q(1))
            self.assertLessEqual(r['null_cross_probability'],Q(1,4))
            self.assertGreater(r['endpoints'],0)

    def test_optional_hindsight_alternative_is_invalid(self):
        # Fit a one-step alternative to the same fair-coin outcome.
        # After seeing y, choose P_y(Y=y)=1. The expectation is 2, not 1.
        expectation=sum((Q(1,2)*Q(1)/Q(1,2) for _ in (0,1)),Q(0))
        self.assertEqual(expectation,Q(2))

    def test_proper_brier_and_nonhidden_policy(self):
        self.assertEqual(brier_binary(Q(3,4),1),Q(1,8))
        self.assertEqual(brier_binary(Q(1,2),1),Q(1,2))
        with self.assertRaises(ValueError):brier_binary(Q(3,2),1)

    def test_field_axis_simple_and_nonidentification_differ_by_target(self):
        a=field_axes(source_exists=True,source_attested=False,
                     target_descends=True,finite_query_program=True)
        self.assertEqual(a['modes'],('SimpleField/model-relative',))
        self.assertFalse(a['physical_source_certified'])
        b=field_axes(source_exists=True,source_attested=False,
                     target_descends=False,finite_query_program=False)
        self.assertEqual(b['modes'],('FuckedField/nonidentifiability',))

    def test_idealhard_and_phantom_separate(self):
        a=field_axes(global_witness_proved=True,
                     no_computable_witness_proved=True,source_exists=True)
        self.assertIn('IdealHardField',a['modes'])
        b=field_axes(phantom_original_lift=True,source_exists=True)
        self.assertIn('FuckedField/phantom-source-map',b['modes'])
        self.assertNotIn('IdealHardField',b['modes'])

    def test_unresolved_and_contradictory_ledger(self):
        self.assertEqual(field_axes()['modes'],('UNRESOLVED/toolkit-relative',))
        self.assertEqual(field_axes(source_exists=False,global_witness_proved=True)['verdict'],'INCOHERENT')
        self.assertEqual(field_axes(finite_query_program=True,
                                    no_computable_witness_proved=True)['verdict'],'INCOHERENT')
        with self.assertRaises(ValueError):field_axes(source_exists='probably')
        with self.assertRaises(ValueError):field_axes(source_exists=1)

    def test_hidden_tag_indistinguishable_for_every_allowed_word(self):
        for count in range(5):
            for word in product(('read','flip'),repeat=count):
                for start in (0,1):
                    h0=tagged_source_transcript(start,0,word)
                    h1=tagged_source_transcript(start,1,word)
                    self.assertEqual(h0[0],h1[0])
                    self.assertEqual(h0[1][0],h1[1][0])
                    self.assertNotEqual(h0[1][1],h1[1][1])

    def test_delayed_mutant_escapes_every_bounded_horizon(self):
        for h in (0,1,2,4,8,30):
            a,b=delayed_mutant(h,False),delayed_mutant(h,True)
            self.assertEqual(a[:h],b[:h])
            self.assertNotEqual(a[h],b[h])

    def test_CRT_finite_phantom_rival(self):
        odds=(3,5,7,11,13,17)
        for k in range(1,len(odds)+1):
            x=1
            for p in odds[:k]:x*=p
            self.assertEqual(x%2,1)
            self.assertTrue(all(x%p==0 for p in odds[:k]))

    def test_live_actual_process_P_replay(self):
        session,audit=run_session('P',12)
        self.assertTrue(audit['verified'])
        self.assertEqual(len(session['steps']),12)
        self.assertEqual(session['reveal']['truth'],'P')
        self.assertEqual(sum(CREDITS[e['action']] for e in session['steps']),
                         session['observer_credit_total'])
        self.assertTrue(session['start']['commitment'])
        self.assertNotIn('truth',session['start'])
        self.assertNotIn('tape_hex',session['start'])

    def test_live_actual_process_Q_replay(self):
        session,audit=run_session('Q',9)
        self.assertTrue(audit['verified'])
        self.assertEqual(audit['source_model'],'Q')

    def test_replay_tamper_outcome_rejected(self):
        session,_=run_session('P',6)
        forged=copy.deepcopy(session)
        forged['steps'][1]['result']['outcome'] ^= 1
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_replay_tamper_tape_commitment_rejected(self):
        session,_=run_session('P',6)
        forged=copy.deepcopy(session)
        forged['reveal']['tape_hex']='00'+forged['reveal']['tape_hex'][2:]
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_replay_tamper_cost_rejected(self):
        session,_=run_session('Q',6)
        forged=copy.deepcopy(session)
        forged['steps'][1]['result']['credits']=999
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_replay_tamper_evidence_rejected(self):
        session,_=run_session('P',6)
        forged=copy.deepcopy(session)
        forged['steps'][2]['e_value']='999/1'
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_replay_tamper_retrospective_belief_rejected(self):
        session,_=run_session('P',7)
        forged=copy.deepcopy(session)
        forged['steps'][0]['posterior_initial_P']=['1/2','1/2']
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_replay_tamper_policy_rejected(self):
        session,_=run_session('P',7)
        forged=copy.deepcopy(session)
        forged['steps'][1]['action']='flip'
        forged['steps'][1]['result']['action']='flip'
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_committed_truth_cannot_change_at_reveal(self):
        session,_=run_session('P',7)
        forged=copy.deepcopy(session)
        forged['reveal']['truth']='Q'
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')

    def test_source_rejects_unlicensed_hidden_state_peek(self):
        import subprocess,sys,json
        p=subprocess.Popen([sys.executable,'-u',str(HERE/'source_process.py'),'--truth','P'],
                            stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,text=True)
        try:
            start=json.loads(p.stdout.readline())
            self.assertNotIn('hidden',str(start))
            p.stdin.write('{'+'"kind":"action","step":0,"action":"peek"'+'}\n')
            p.stdin.flush()
            error=json.loads(p.stdout.readline())
            self.assertEqual(error['kind'],'error')
            self.assertNotIn('tape_hex',str(error))
            self.assertEqual(p.wait(timeout=10),0)
        finally:
            if p.poll() is None:p.kill();p.wait(timeout=10)
            for st in (p.stdin,p.stdout,p.stderr):
                if st is not None:st.close()

    def test_same_future_predictions_do_not_identify_hidden_ontology(self):
        from observational_succ.recursive_observer import JointInstrument,predictively_equivalent_priors
        fair=Q(1,2)
        one=(JointInstrument((((fair,fair),),),Q(1)),)
        hidden=(JointInstrument((((Q(0),Q(0)),(fair,fair)),
                                 ((fair,fair),(Q(0),Q(0)))),Q(1)),)
        self.assertTrue(predictively_equivalent_priors(one,hidden,(Q(1),),(fair,fair)))
        # These source models have distinct numbers of hidden states.
        self.assertNotEqual(one[0].n,hidden[0].n)

    def test_replay_wrong_program_digest_rejected(self):
        session,_=run_session('Q',6)
        forged=copy.deepcopy(session)
        forged['start']['source_sha256']='0'*64
        with self.assertRaises(ReplayError):validate_session(forged,HERE/'source_process.py')


if __name__=='__main__':unittest.main(verbosity=2)
