"""Replay scoped proof oracles; full source spectra and native suite opt-in."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source',action='store_true')
    parser.add_argument('--native',action='store_true')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True,exist_ok=True)
    env = dict(os.environ,PYTHONPATH=str(ROOT),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    rows,comparisons = [],[]

    def run(name,cmd):
        log = out/(name+'.log')
        start = time.monotonic()
        with log.open('w') as f:
            result = subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
        rows.append({'name':name,'command':cmd,'exit_code':result.returncode,
                     'seconds':time.monotonic()-start,'log_sha256':sha256(log.read_bytes()).hexdigest()})
        print(name,result.returncode,flush=True)
        if result.returncode:
            raise RuntimeError('failed '+name+'; see '+str(log))

    def compare(name,fresh,retained,remove=()):
        actual = json.loads(fresh.read_text())
        expected = json.loads(retained.read_text())
        for key in remove:
            actual.pop(key,None)
            expected.pop(key,None)
        equal = actual == expected
        comparisons.append({'name':name,'equal':equal,'excluded_metadata':list(remove),
                             'retained_sha256':sha256(retained.read_bytes()).hexdigest()})
        if not equal:
            raise AssertionError('payload mismatch '+name)

    try:
        for folder in (HERE,HERE/'model',HERE/'resonance',HERE/'hostile',HERE.parent/'signal_frontier/prime_resonance'):
            run(folder.name+'_tests',[sys.executable,'-m','unittest','discover','-s',str(folder),'-p','test_*.py','-v'])
        for folder,script,receipt in (
            ('model','oracle.py','RECEIPT.json'),
            ('resonance','oracle.py','RECEIPT.json'),
            ('hostile','oracle.py','RECEIPT.json'),
            ('hostile','review_oracle.py','REVIEW_RECEIPT.json'),
            ('hostile','model5_review_oracle.py','MODEL5_REVIEW_RECEIPT.json')):
            name=folder+'_'+Path(script).stem
            fresh=out/(name+'.json')
            run(name,[sys.executable,str(HERE/folder/script),'--output',str(fresh)])
            # Review proof/source hashes are historical provenance, not numerical
            # data. A subsequent explicitly reviewed equivalent stream change is
            # documented separately; preserve the original receipt itself.
            compare(name,fresh,HERE/folder/receipt,('dependencies','proof_sha256','reviewed_hashes'))
        for gate in ('verify_provenance','observer_foundations_probe','ordinal_succ_report_probe'):
            run(gate,[sys.executable,'scripts/'+gate+'.py'])
        if args.source:
            sourceout=out/'source'
            for A in (1103,2203,5501,22003):
                run('source_'+str(A),[sys.executable,str(HERE/'source_budget.py'),'--A',str(A),'--output',str(sourceout)])
                compare('source_payload_'+str(A),sourceout/f'source_{A}.json',HERE/f'results/source_{A}.json')
                compare('budget_payload_'+str(A),sourceout/f'budget_{A}.json',HERE/f'results/budget_{A}.json',('code_sha256',))
        if args.native:
            run('native_suite',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py'])
        run('whitespace',['git','diff','--check'])
    finally:
        (out/'replay.json').write_text(json.dumps({'parent':'95d9860de3a52ab76c1a0719e170b609759b17b9',
            'commands':rows,'comparisons':comparisons,'full_source_replayed':args.source,
            'native_executed_here':args.native,'pi_normality':'OPEN','RH':'OPEN'},indent=2,sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
