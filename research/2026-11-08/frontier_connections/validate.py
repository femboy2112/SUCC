"""Replay this round's scoped oracles and mandatory lightweight gates."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
START='525d7c87dd1016aeeea4ac9cd1366cbb935a0441'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--native',action='store_true')
    args=ap.parse_args()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONPATH=str(ROOT),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    rows=[]; comparisons=[]

    def run(name,cmd):
        log=out/(name+'.log');start=time.monotonic()
        with log.open('w') as f:
            result=subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
        rows.append({'name':name,'command':cmd,'exit_code':result.returncode,
                     'seconds':time.monotonic()-start,'log_sha256':sha256(log.read_bytes()).hexdigest()})
        print(name,result.returncode,flush=True)
        if result.returncode:raise RuntimeError('failed '+name)

    try:
        for folder,pattern in ((HERE,'test_energy.py'),(HERE/'observer','test_*.py'),
                               (HERE/'arithmetic','test_*.py'),(HERE/'crucible','qco_oracle.py')):
            run(folder.name+'_tests',[sys.executable,'-m','unittest','discover','-s',str(folder),'-p',pattern,'-v'])
        for name,script,receipt in (
            ('energy',HERE/'energy_oracle.py',HERE/'ENERGY_RECEIPT.json'),
            ('observer',HERE/'observer/oracle.py',HERE/'observer/RECEIPT.json'),
            ('quotient',HERE/'crucible/qco_oracle.py',HERE/'crucible/ORACLE.json')):
            fresh=out/(name+'.json')
            run(name+'_oracle',[sys.executable,str(script),'--output',str(fresh)])
            expected=json.loads(receipt.read_text()); actual=json.loads(fresh.read_text())
            same=expected==actual
            comparisons.append({'name':name,'payload_equal':same,
                                'retained_sha256':sha256(receipt.read_bytes()).hexdigest()})
            if not same:raise AssertionError(name+' receipt changed')
        for gate in ('verify_provenance','observer_foundations_probe','ordinal_succ_report_probe'):
            run(gate,[sys.executable,'scripts/'+gate+'.py'])
        native_inputs=['tests','scripts','observational_succ','formal','provenance','docs','AGENTS.md']
        changes=subprocess.check_output(['git','diff','--name-only',START,'--',*native_inputs],cwd=ROOT,text=True)
        if changes:raise AssertionError('native input changed: '+changes)
        if args.native:
            run('native_suite',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py'])
        run('whitespace',['git','diff','--check'])
    finally:
        prior=HERE.parent/'complement_budget/validation/native_suite.log'
        (out/'SUMMARY.json').write_text(json.dumps({
            'starting_head':START,'commands':rows,'comparisons':comparisons,
            'native_executed_this_round':args.native,
            'native_prior_pass':{'tests':12147,'head':START,
                'receipt':str(prior.relative_to(ROOT)),
                'receipt_sha256':sha256(prior.read_bytes()).hexdigest(),
                'scope':'Prior run; native input trees compared to starting head, not a new full-suite run.'},
            'pi_normality':'OPEN','RH':'OPEN'},indent=2,sort_keys=True)+'\n')


if __name__=='__main__':main()
