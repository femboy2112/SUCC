import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from observational_succ import (ActualizationError, BasisLift, BudgetExceeded,
                           DomainError, Engine, Frame, I, Limits,
                           LossyHistoryError, ONE, Scalar, run_arithmetic, source_at)
from observational_succ.engine import digest


class EngineTests(unittest.TestCase):
    def test_three_stages_and_no_premature_leaf(self):
        e=run_arithmetic(3)
        self.assertEqual(e.shadow(4)['stage'],'shadow')
        e.step(ONE)
        self.assertEqual(e.shadow(4)['stage'],'observed')
        self.assertNotIn(4,e.coefficients)
        self.assertEqual(Scalar.from_data(e.shadow(12)['weight']),ONE)
        e.propagate()
        self.assertEqual(e.shadow(4)['stage'],'integrated')
        self.assertIn(4,e.coefficients)
        self.assertEqual(Scalar.from_data(e.shadow(12)['weight']),Scalar())

    def test_double_step_and_double_propagate_rejected(self):
        e=Engine();e.step()
        before=e.dumps()
        with self.assertRaises(DomainError):e.step()
        self.assertEqual(before,e.dumps())
        e.propagate(); before=e.dumps()
        with self.assertRaises(DomainError):e.propagate()
        self.assertEqual(before,e.dumps())

    def test_local_context_is_not_coordinate_or_tick(self):
        e=Engine(Frame('F2','modular',(1,),2))
        for x in [ONE,ONE,Scalar(2)]:e.advance(x,context='laboratory',probe='reading')
        self.assertEqual(e.state['last_integration']['status'],'revised')
        self.assertEqual(e.state['tick'],3)
        self.assertEqual(e.coordinate,(1,))
        self.assertEqual(len(e.state['facts']),2)
        e.advance(ONE,context='other laboratory',probe='reading')
        self.assertEqual(e.state['last_integration']['status'],'new_context')
        self.assertEqual(len(e.state['facts']),3)
        self.assertEqual(len(e.records),8)

    def test_prediction_is_not_observational_succ(self):
        e=run_arithmetic(3)
        e.predict(6,Scalar('8/7'),'deliberately false forecast')
        self.assertNotIn(6,e.coefficients)
        self.assertFalse(e.shadow(6)['observed'])
        for _ in range(3):e.advance(ONE)
        self.assertEqual(e.state['expectations']['6']['verdict'],'refuted')
        self.assertEqual(e.state['expectations']['6']['value'],Scalar('8/7').data())
        self.assertEqual(e.coefficients[6],ONE)
        self.assertTrue(any(r.kind=='predict' for r in e.records))

    def test_invalid_unit_event_remains_observed_not_integrated(self):
        e=Engine(arithmetic=True)
        e.step(Scalar(2))
        before=e.dumps()
        with self.assertRaises(DomainError):e.propagate()
        self.assertEqual(e.dumps(),before)
        self.assertEqual(e.state['phase'],'observed')
        self.assertEqual(e.coefficients,{})

    def test_bare_inverse_does_not_reverse_model(self):
        e=run_arithmetic(6); before=e.dumps()
        self.assertEqual(e.bare_inverse(),(5,))
        self.assertEqual(e.dumps(),before)
        self.assertIn(6,e.coefficients)

    def test_lossless_full_reversal_and_replay(self):
        e=Engine(arithmetic=True)
        initial=e.state
        e.predict(6,ONE,'declared rule')
        for n in range(1,13):e.advance(source_at(n,'chi5'))
        forward_records=e.records
        forward=e.dumps()
        e.reverse_all()
        self.assertEqual(e.state,initial)
        self.assertEqual(e.records[:len(forward_records)],forward_records)
        self.assertEqual(len(e.records),2*len(forward_records))
        self.assertTrue(e.verify())
        self.assertEqual(Engine.loads(forward).state['coordinate'],['12'])

    def test_reverse_pending_and_branching(self):
        e=Engine(arithmetic=True);e.advance(ONE);e.step(ONE)
        e.reverse_last()
        self.assertEqual(e.coordinate,(1,))
        e.advance(Scalar(2),context='new branch')
        self.assertEqual(e.coefficients[2],Scalar(2))
        self.assertTrue(e.verify())
        self.assertEqual([r.seq for r in e.records],list(range(1,len(e.records)+1)))

    def test_lossy_view_refuses_reconstruction(self):
        e=run_arithmetic(8)
        original=e.dumps()
        for n in [0,1,3]:
            with self.assertRaises(LossyHistoryError):Engine.loads(json.dumps(e.view(n)))
        self.assertEqual(e.dumps(),original)

    def test_hash_tamper_and_semantic_tamper(self):
        e=run_arithmetic(4)
        d=e.document();d['records'][1]['after']['coordinate']=['500']
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))
        # Re-hash the forged chain: semantic replay still detects a wrong transition.
        for j,r in enumerate(d['records']):
            if j:r['previous']=d['records'][j-1]['hash']
            r['hash']=digest({k:v for k,v in r.items() if k!='hash'})
        d['head']=d['records'][-1]['hash']
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))
        with self.assertRaises(DomainError):Engine.loads(e.dumps(),expected_head='0'*64)
        d=e.document();d['records'][0]['seq']=True
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))

    def test_bad_json_and_missing_history(self):
        for x in ['{}','[]','null','{"schema":NaN}', '{', '{"schema":"x","schema":"y"}']:
            with self.assertRaises(ActualizationError):Engine.loads(x)
        e=run_arithmetic(4);d=e.document();d['records'].pop(1)
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))

    def test_unknown_actions_and_order(self):
        d=run_arithmetic(3).document()
        d['records'][0]['kind']='invent_new_prime'
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))
        e=run_arithmetic(3); e.reverse_last();d=e.document();d['records'][-1]['payload']['of']=1
        with self.assertRaises(DomainError):Engine.loads(json.dumps(d))

    def test_snapshot_aliasing(self):
        e=run_arithmetic(2);before=e.dumps()
        state=e.state;state['coordinate'][0]='999';state['arithmetic'].clear()
        doc=e.document();doc['config']['frame']['name']='mutant'
        self.assertEqual(e.dumps(),before)

    def test_resource_failure_atomicity(self):
        e=Engine(limits=Limits(max_records=2))
        e.advance();before=e.dumps()
        with self.assertRaises(BudgetExceeded):e.advance()
        with self.assertRaises(BudgetExceeded):e.reverse_all()
        self.assertEqual(e.dumps(),before)
        with self.assertRaises(DomainError):Engine(arithmetic='yes')

    def test_byte_budget_does_not_discard_or_half_reverse(self):
        e=Engine(limits=Limits(max_trace_bytes=5000))
        while True:
            before=e.dumps()
            try:
                if e.state['phase']=='ready':e.step()
                else:e.propagate()
            except BudgetExceeded:
                self.assertEqual(e.dumps(),before)
                break
        self.assertEqual(e._bytes,len(e.dumps()))
        self.assertLessEqual(e._bytes,5000)
        before=e.dumps()
        with self.assertRaises(BudgetExceeded):e.reverse_all()
        self.assertEqual(e.dumps(),before)

    def test_conjugate_involution_and_fiber_conservation(self):
        lift=BasisLift('phase',((I,Scalar()),(Scalar(),-I)),(ONE,I))
        e=Engine(arithmetic=True,lifts=(lift,))
        for n in range(1,9):e.advance(source_at(n,'chi5'))
        self.assertTrue(e.conjugated().verify())
        self.assertEqual(e.conjugated().conjugated().dumps(),e.dumps())
        for n,v in e.coefficients.items():self.assertEqual(e.conjugated().coefficients[n],v.conjugate())
        initial=Engine(arithmetic=True,lifts=(lift,)).state
        e.reverse_all();self.assertEqual(e.state,initial)

    def test_cli_roundtrip_and_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'trace.json'
            r=subprocess.run([sys.executable,'-m','observational_succ','run','--steps','6','--source','zeta','--output',str(path)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            r=subprocess.run([sys.executable,'-m','observational_succ','replay',str(path)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertTrue(json.loads(r.stdout)['verified'])
            r=subprocess.run([sys.executable,'-m','observational_succ','run','--domain','modular','--modulus','2','--source','zeta'],capture_output=True,text=True)
            self.assertEqual(r.returncode,2)
            r=subprocess.run([sys.executable,'-m','observational_succ','shadow','--horizon','3','--target','6'],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertEqual(json.loads(r.stdout)['weight'],Scalar(-1).data())


if __name__=='__main__':unittest.main()
