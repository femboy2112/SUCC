"""Replay the scoped signed-CRT validation and preserve raw command receipts."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
COMMANDS=[([sys.executable,'-m','unittest','discover','-s','.','-p','test_*.py','-v'],'focused_tests.log'),
          ([sys.executable,'run_probe.py'],'probe_receipt.json'),
          ([sys.executable,'independent_oracle.py'],'independent_oracle_receipt.json')]
receipts=[]
for argv,filename in COMMANDS:
    started=datetime.now(timezone.utc).isoformat()
    tick=time.monotonic()
    result=subprocess.run(argv,cwd=HERE,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    elapsed=time.monotonic()-tick
    output=result.stdout+result.stderr if filename.endswith('.log') else result.stdout
    (HERE/filename).write_text(output)
    receipts.append({'argv':argv,'cwd':str(HERE),'started_utc':started,
        'finished_utc':datetime.now(timezone.utc).isoformat(),'seconds':elapsed,
        'exit_code':result.returncode,'stdout_artifact':filename,
        'artifact_sha256':hashlib.sha256(output.encode()).hexdigest(),
        'stderr':result.stderr if not filename.endswith('.log') else 'preserved in log'})
    if result.returncode:
        print(result.stderr,file=sys.stderr)
        break
(HERE/'command_receipts.json').write_text(json.dumps({'python':platform.python_version(),
    'platform':platform.platform(),'commands':receipts},indent=2)+'\n')
print(json.dumps({'commands':len(receipts),'exit_codes':[r['exit_code'] for r in receipts]}))
sys.exit(max(r['exit_code'] for r in receipts))
