#!/usr/bin/env python3
"""Replay the child campaign without altering parent evidence or source pins."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/2026-10-28/lonely_runner/referee'


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    manifests=[ROOT/'research/2026-10-28/lonely_runner/SOURCE_MANIFEST.json',
               PACKAGE/'SOURCE_MANIFEST.json']
    pins={}
    for path in manifests:
        for name,expected in json.loads(path.read_text())['source_hashes'].items():
            if name in pins and pins[name]!=expected:raise RuntimeError('conflicting source pins')
            pins[name]=expected
    for name,expected in pins.items():
        if digest(ROOT/name)!=expected:raise RuntimeError('source hash mismatch: '+name)
    env={**os.environ,'PYTHONPATH':str(ROOT),'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'}
    commands=[];failures=[]
    def run(label,argv):
        start=time.monotonic();log=out/(label+'.log')
        with log.open('w') as f:
            try:
                code=subprocess.run([sys.executable,*argv],cwd=ROOT,env=env,
                                    stdout=f,stderr=subprocess.STDOUT,timeout=600).returncode
            except subprocess.TimeoutExpired:
                f.write('\nTIMEOUT: no passing result\n');code=124
        commands.append({'label':label,'command':[sys.executable,*argv],'exit_code':code,
                         'seconds':time.monotonic()-start,'log':log.name,'sha256':digest(log)})
        if code:failures.append(label)
        print(label,code,flush=True)
    run('referee-tests',['-m','unittest','discover','-s','tests','-p','test_lonely_runner_*referee*.py','-v'])
    run('growth-guard-tests',['-m','unittest','tests.test_lonely_runner_growth_authority','-v'])
    run('endpoint-controls',['-m','unittest','tests.test_lonely_runner_endpoint_refine','-v'])
    run('independent-hostile',['scripts/lonely_runner_referee_hostile.py','--verify',
                              str(PACKAGE/'receipts/quadratic-independent-exact.json')])
    run('receipt-packing',['scripts/lonely_runner_referee_receipts.py','--verify',
                          str(PACKAGE/'receipts/census-21-30')])
    run('census-21-30',['scripts/lonely_runner_referee_census.py','--min-n','21','--max-n','30',
                        '--output',str(out/'census')])
    receipts=PACKAGE/'receipts/census-21-30'
    for n in range(21,31):
        for stem in ('census','fraction'):
            name=f'{stem}-n{n}.json'
            actual=out/'census'/name
            compressed=receipts/(name+'.gz')
            expected=gzip.decompress(compressed.read_bytes()) if compressed.exists() else (receipts/name).read_bytes()
            if not actual.exists() or actual.read_bytes()!=expected:failures.append('replay-drift-'+name)
    if (not (out/'census/known-controls.json').exists() or
        (out/'census/known-controls.json').read_bytes()!=(receipts/'known-controls.json').read_bytes()):
        failures.append('positive-control-drift')
    run('catalog',['scripts/build_math_memory.py','--check'])
    changed=[name for name,expected in pins.items() if digest(ROOT/name)!=expected]
    failures.extend('changed-'+name for name in changed)
    report={'schema':'succ.lonely-runner.referee-validation.v1','status':'PASS' if not failures else 'FAILED',
            'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'python':sys.version,'source_hashes':pins,'commands':commands,'failures':failures,
            'authority':'executed exact tests and source pins; kernel and hosted evidence are separate'}
    (out/'receipt.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],len(pins),'source pins',flush=True)
    return bool(failures)


if __name__=='__main__':raise SystemExit(main())
