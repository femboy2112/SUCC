"""Execute real subprocess contact, predeclared P/Q source, adaptive policy.

Run from a complete SUCC checkout with PYTHONPATH=. for imports. The subprocess
never exposes hidden state or committed random tape until the experiment ends.
The published receipt is a replayable finite trace, not a statistical proof
that the real OS RNG is iid or that a physical-world model has been verified.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

from observational_succ.source_authentication import ModelEvidence, ACTIONS, brier_binary
from independent_replay import validate_session

SRC=Path(__file__).with_name('source_process.py')


def run_session(truth,horizon=22):
    command=[sys.executable,'-u',str(SRC),'--truth',truth]
    host_launch=time.perf_counter_ns()
    proc=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,text=True,bufsize=1)
    try:
        first=json.loads(proc.stdout.readline())
        if first['kind']!='start' or first['source_sha256']!=hashlib.sha256(SRC.read_bytes()).hexdigest():
            raise RuntimeError('Source binary not verified at activation')
        model=ModelEvidence()
        steps=[]
        brier_alt=Fraction(0)
        brier_null=Fraction(0)
        scored=0
        for t in range(horizon):
            a=model.action()
            start=time.perf_counter_ns()
            proc.stdin.write(json.dumps({'kind':'action','step':t,'action':a})+'\n')
            proc.stdin.flush()
            result=json.loads(proc.stdout.readline())
            elapsed=max(1,time.perf_counter_ns()-start)
            if result['kind']!='result':
                raise RuntimeError(f'Source rejected registered instrument: {result}')
            if result['credits'] != {'sense':2,'flip':1,'reset':4}[a]:
                raise RuntimeError('Source cost meter not calibrated to declared credits')
            p_alt,p_null=model.predictive(a)
            model.record(a,result['outcome'])
            if len(p_alt)==2:
                brier_alt+=brier_binary(p_alt[1],result['outcome'])
                brier_null+=brier_binary(p_null[1],result['outcome'])
                scored+=1
            steps.append({'action':a,'result':result,
                         'client_round_trip_ns':elapsed,
                         'predictive_P':[str(x) for x in p_alt],
                         'predictive_Q':[str(x) for x in p_null],
                         'e_value':str(model.e_value),
                         'posterior_initial_P':[str(x) for x in model.original_posterior(0)],
                         'posterior_initial_Q':[str(x) for x in model.original_posterior(1)]})
        proc.stdin.write('{"kind":"end"}\n')
        proc.stdin.flush()
        last=json.loads(proc.stdout.readline())
        code=proc.wait(timeout=10)
        if code!=0 or last['kind']!='reveal':
            raise RuntimeError('Source failed to terminate with truthful tape')
        session={'start':first,'steps':steps,'reveal':last,
                 'observer_credit_total':model.credit_total,
                 'observer_e_value':str(model.e_value),
                 'brier_P_total':str(brier_alt),'brier_Q_total':str(brier_null),
                 'brier_scored_events':scored,
                 'host_launch_ns':host_launch}
        validation=validate_session(session,SRC)
        return session,validation
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait(timeout=10)
        for stream in (proc.stdin,proc.stdout,proc.stderr):
            if stream is not None:
                stream.close()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sessions-per-model',type=int,default=8)
    parser.add_argument('--horizon',type=int,default=22)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if not 1<=args.sessions_per_model<=32 or not 1<=args.horizon<=120:
        raise ValueError('Bounded session/horizon required')
    sessions=[]
    summary=[]
    # Predeclare balanced truth, no selection by outcome. Source labels are
    # withheld from the observer policy until reveal for audit.
    for r in range(args.sessions_per_model):
        for truth in ('P','Q'):
            s,v=run_session(truth,args.horizon)
            sessions.append(s)
            summary.append({'truth':truth,'verified':v['verified'],
                            'credits':v['credit_total'],
                            'steps':v['steps'],
                            'e_value':s['observer_e_value'],
                            'brier_P_total':s['brier_P_total'],
                            'brier_Q_total':s['brier_Q_total']})
    payload={'scope':'executed-local-Python-subprocess-only',
             'protocol':'SUCC-COMMIT-TAPE-v1',
             'law':'P=3/4 or Q=1/2 predeclared, independent OS-random tape per session',
             'sessions':sessions,'summary':summary}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=1,sort_keys=True)+'\n')
    for label in ('P','Q'):
        sub=[r for r in summary if r['truth']==label]
        vals=[Fraction(r['e_value']) for r in sub]
        print(f'{label}: {len(sub)} sessions, replay validated; '
              f'E>=4: {sum(v>=4 for v in vals)}, '
              f'E range {float(min(vals)):.5g}..{float(max(vals)):.5g}')
    print('source_sha256:',hashlib.sha256(SRC.read_bytes()).hexdigest())
    print('saved:',args.out)

if __name__=='__main__':main()
