"""Run a command and retain exact head/tree, environment, output and exit."""
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import time

name, root, out = sys.argv[1:4]
command = sys.argv[4:]
root, out = Path(root), Path(out)
out.mkdir(parents=True, exist_ok=True)
git = lambda *a: subprocess.check_output(['git',*a],cwd=root,text=True).strip()
head,tree=git('rev-parse','HEAD'),git('rev-parse','HEAD^{tree}')
assert not git('status','--porcelain','--untracked-files=no'), 'dirty tracked candidate'
env=dict(os.environ,PYTHONPATH=str(root),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
record={'head':head,'tree':tree,'command':command,'cwd':str(root),'python':sys.version,
        'dependencies':{k:importlib.metadata.version(k) for k in ['mpmath','numpy','sympy','scipy']},
        'start_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING'}
receipt=out/(name+'.json'); log=out/(name+'.log')
receipt.write_text(json.dumps(record,indent=2)+'\n')
start=time.monotonic()
with log.open('w') as stream:
    result=subprocess.run(command,cwd=root,env=env,stdout=stream,stderr=subprocess.STDOUT)
unchanged=(head==git('rev-parse','HEAD') and not git('status','--porcelain','--untracked-files=no'))
record.update(exit_code=result.returncode,seconds=time.monotonic()-start,tracked_candidate_unchanged=unchanged,
              log_sha256=hashlib.sha256(log.read_bytes()).hexdigest(),
              finish_utc=datetime.now(timezone.utc).isoformat(),status='PASS' if result.returncode==0 and unchanged else 'FAIL')
receipt.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
raise SystemExit(0 if record['status']=='PASS' else 1)
