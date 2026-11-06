"""Run the exact candidate gate serially and preserve external immutable logs."""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

p=argparse.ArgumentParser()
p.add_argument('--output', required=True)
args=p.parse_args()
root=Path(__file__).resolve().parents[3]
out=Path(args.output).resolve()
out.mkdir(parents=True, exist_ok=False)
folder=Path(__file__).resolve().parent.relative_to(root)
env=dict(os.environ, PYTHONPATH=str(root), OMP_NUM_THREADS='1',
         OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
receipt={'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
         'tree':subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=root,text=True).strip(),
         'python':sys.version,'versions':{},'checks':[]}
for name in ('mpmath','sympy','numpy','scipy'):
    receipt['versions'][name]=importlib.import_module(name).__version__
commands=[
 ('provenance',['scripts/verify_provenance.py']),
 ('alpha_tests',['-m','unittest','discover','-s',str(folder/'front_alpha'),'-p','test_*.py']),
 ('alpha_receipt',[str(folder/'front_alpha/carry_probe.py')]),
 ('delta_tests',['-m','unittest','discover','-s',str(folder/'front_delta'),'-p','test_*.py']),
 ('delta_receipt',[str(folder/'front_delta/verify_receipt.py')]),
 ('referee_tests',['-m','unittest','discover','-s',str(folder/'front_referee'),'-p','test_*.py']),
 ('charge_receipt',[str(folder/'charge_probe.py'),'--verify']),
 ('observer',['scripts/observer_foundations_probe.py']),
 ('ordinal',['scripts/ordinal_succ_report_probe.py']),
 ('native',['-m','unittest','discover','-s','tests','-p','test_*.py'])]
for name,argv in commands:
    command=[sys.executable,*argv]
    logfile=out/(name+'.log')
    start=time.monotonic()
    with logfile.open('w') as stream:
        try:
            result=subprocess.run(command,cwd=root,env=env,stdout=stream,
                                  stderr=subprocess.STDOUT,timeout=1800)
            status='passed' if result.returncode==0 else 'failed'
            code=result.returncode
        except subprocess.TimeoutExpired:
            status='timed_out';code=None
    receipt['checks'].append({'name':name,'command':command,'status':status,
        'exit_code':code,'seconds':time.monotonic()-start,
        'log_sha256':hashlib.sha256(logfile.read_bytes()).hexdigest()})
    (out/'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(name,status,round(receipt['checks'][-1]['seconds'],3),flush=True)
print('receipt',out/'VALIDATION.json',flush=True)
sys.exit(any(c['status']!='passed' for c in receipt['checks']))
