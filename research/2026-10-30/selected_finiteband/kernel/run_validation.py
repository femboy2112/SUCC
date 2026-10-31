"""Run this front's focused checks and preserve raw stdout/stderr + receipts."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent


def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    runs=[]
    jobs=[('tests.log',[sys.executable,'-m','unittest','-v','test_kernel_transport.py']),
          ('probe_receipt.json',[sys.executable,'kernel_transport.py']),
          ('oracle_receipt.json',[sys.executable,'independent_oracle.py'])]
    for output,cmd in jobs:
        start=now(); tick=time.monotonic()
        result=subprocess.run(cmd,cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                              env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),
                              timeout=240)
        (HERE/output).write_bytes(result.stdout if output.endswith('.json') else result.stdout+result.stderr)
        stderr_name=output+'.stderr'
        (HERE/stderr_name).write_bytes(result.stderr if output.endswith('.json') else b'')
        runs.append({'command':cmd,'cwd':str(HERE),'start_utc':start,'end_utc':now(),
                     'elapsed_seconds':time.monotonic()-tick,'exit_code':result.returncode,
                     'stdout_file':output,'stderr_file':stderr_name,
                     'stdout_sha256':hashlib.sha256((HERE/output).read_bytes()).hexdigest(),
                     'stderr_sha256':hashlib.sha256((HERE/stderr_name).read_bytes()).hexdigest()})
        print(output,result.returncode,flush=True)
    (HERE/'validation_receipt.json').write_text(json.dumps({'python':sys.version,'runs':runs},indent=2)+'\n')
    if any(x['exit_code'] for x in runs): raise SystemExit(1)


if __name__=='__main__': main()
