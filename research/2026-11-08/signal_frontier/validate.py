"""Reproduce focused frontier checks; expensive full source replay is opt-in.

Native validation is separate: four mandated commands and their raw receipts
are in validation/. No skipped command is called a pass.
"""
import argparse
from hashlib import sha256
import json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source',action='store_true')
    parser.add_argument('--native',action='store_true')
    args=parser.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    rows=[];comparisons=[]
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONPATH=str(ROOT))
    py=sys.executable
    def run(name,cmd):
        log=out/(name+'.log');start=time.monotonic()
        with log.open('w') as f:r=subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
        rows.append({'name':name,'command':cmd,'exit_code':r.returncode,'seconds':time.monotonic()-start,
                     'log_sha256':sha256(log.read_bytes()).hexdigest()})
        print(name,r.returncode,flush=True)
        if r.returncode:raise RuntimeError(name+' failed; see '+str(log))
    def compare(name,fresh,retained):
        equal=json.loads(fresh.read_text())==json.loads(retained.read_text())
        comparisons.append({'name':name,'equal':equal,'retained_sha256':sha256(retained.read_bytes()).hexdigest()})
        if not equal:raise AssertionError(name+' replay mismatch')
    try:
        for folder in [HERE]+sorted(p for p in HERE.iterdir() if p.is_dir() and list(p.glob('test_*.py'))):
            run(folder.name+'_tests',[py,'-m','unittest','discover','-s',str(folder),'-p','test_*.py','-v'])
        oracles=[('fixed_depth','oracle.py','RECEIPT.json'),('crucible','oracle.py','RESULTS.json'),
                 ('prime_resonance','oracle.py','RECEIPT.json'),('fibonacci_geometry','oracle.py','EXACT_RECEIPT.json'),
                 ('fibonacci_geometry','numerical.py','NUMERICAL_RECEIPT.json'),
                 ('triangle_posterior','oracle.py','EXACT_RECEIPT.json'),
                 ('triangle_posterior','numerical.py','NUMERICAL_RECEIPT.json')]
        for folder,script,receipt in oracles:
            name=folder+'_'+script.removesuffix('.py');fresh=out/(name+'.json')
            run(name,[py,str(HERE/folder/script),'--output',str(fresh)])
            compare(name,fresh,HERE/folder/receipt)
        for numerical,receipt in ((False,'EXACT_RECEIPT.json'),(True,'NUMERICAL_RECEIPT.json')):
            name='triangle_geometry_'+('numerical' if numerical else 'oracle');fresh=out/(name+'.json')
            run(name,[py,str(HERE/'triangle_geometry/oracle.py'),'--output',str(fresh)]+(['--numerical'] if numerical else []))
            compare(name,fresh,HERE/'triangle_geometry'/receipt)
        clock_out=out/'clock'
        run('fibonacci_clock_oracle',[py,str(HERE/'fibonacci_covariance/observer.py'),'--output',str(clock_out)]+(['--source'] if args.source else []))
        compare('clock_oracle',clock_out/'ORACLE.json',HERE/'fibonacci_covariance/results/ORACLE.json')
        if args.source:
            for name in ('SOURCE_149.json','SOURCE_673.json','SUMMARY.json'):
                compare('clock_'+name,clock_out/name,HERE/'fibonacci_covariance/results'/name)
            source_out=out/'source'
            for stage in ('development','holdout'):
                run('source_'+stage,[py,str(HERE/'source_probe.py'),'--stage',stage,'--output',str(source_out)])
            for retained in sorted((HERE/'results').glob('origin_*.json')):
                compare(retained.stem,source_out/retained.name,retained)
        for folder in ('referee','triangle_referee'):
            fresh=out/(folder+'.json')
            run(folder+'_oracle',[py,str(HERE/folder/'oracle.py'),'--output',str(fresh)])
            actual=json.loads(fresh.read_text());retained=json.loads((HERE/folder/'RECEIPT.json').read_text())
            # Re-evaluated numerical/algebraic data are compared separately from
            # immutable historical proof-review hash pins.
            for key in ('dependencies','proof_sha256'):
                actual.pop(key,None);retained.pop(key,None)
            equal=actual==retained
            comparisons.append({'name':folder+'_mathematical_payload','equal':equal,
                                'historical_review_pins_preserved':True})
            if not equal:raise AssertionError(folder+' replay mismatch')
        run('source_independent_review',[py,str(HERE/'verify_source.py'),'--output',str(out/'source_review.json')])
        compare('source_review',out/'source_review.json',HERE/'SOURCE_REVIEW.json')
        run('lean_clock',['lean',str(HERE/'formal/FibonacciClock.lean')])
        for gate in ('verify_provenance','observer_foundations_probe','ordinal_succ_report_probe'):
            run(gate,[py,'scripts/'+gate+'.py'])
        if args.native:run('native_suite',[py,'-m','unittest','discover','-s','tests','-p','test_*.py'])
        run('whitespace',['git','diff','--check'])
    finally:
        (out/'replay.json').write_text(json.dumps({'parent':'86327467191420d2157eeae5f4cfa1c2c62810da',
            'commands':rows,'comparisons':comparisons,'full_source_replayed':args.source,
            'native_executed_here':args.native,'code_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest()
            for p in sorted(HERE.rglob('*.py'))},'pi_normality':'OPEN','RH':'OPEN'},indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
