#!/usr/bin/env python3
"""Run seven isolated test workers concurrently and preserve raw outputs.

These are separate subprocess instruments, NOT independent AI agents.
Construction and tests share an author; arithmetic enumeration is a distinct
implementation from the production dynamic-programming DAG.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import os
import platform
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
LANES=('fields','shadow','engine','category','resource_probe','local_global','circle_transport')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default=str(ROOT/'research/2026-10-09/field_relative_observational_succ/evidence'))
    args=p.parse_args()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    def worker(lane):
        cmd=[sys.executable,'-m','unittest','discover','-s','tests/observational_succ','-p',f'test_{lane}.py','-v']
        run=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=120,
                           env={**os.environ,'PYTHONHASHSEED':'0','PYTHONPATH':str(ROOT)})
        raw=run.stdout+run.stderr
        (out/f'{lane}.txt').write_text(raw,encoding='utf-8')
        found=re.search(r'Ran (\d+) tests?',raw)
        return {'lane':lane,'command':cmd,'exit_code':run.returncode,
                'tests':int(found.group(1)) if found else None,
                'output_sha256':sha256(raw.encode()).hexdigest()}
    with ThreadPoolExecutor(max_workers=7) as pool: results=list(pool.map(worker,LANES))
    files=sorted((ROOT/'observational_succ').glob('*.py'))+sorted((ROOT/'tests/observational_succ').glob('test_*.py'))+[Path(__file__)]
    hashes={str(path.relative_to(ROOT)):{'sha256':sha256(path.read_bytes()).hexdigest(),
            'git_blob':sha256(path.read_bytes()).hexdigest()} for path in files}
    # Git object identity is SHA1(blob-header || bytes), not the file's SHA256.
    from hashlib import sha1
    for path in files:
        data=path.read_bytes()
        hashes[str(path.relative_to(ROOT))]['git_blob']=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    report={'status':'PASS' if all(r['exit_code']==0 for r in results) else 'FAIL',
            'timestamp_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,
            'platform':platform.platform(),'parallel_workers':3,'independent_model_agents':0,
            'total_tests':sum(r['tests'] or 0 for r in results),'lanes':results,'executed_files':hashes,
            'scope':'new finite operational package only; not full historical repo suite or RH sign',
            'zeros_used':False}
    (out/'audit.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2,sort_keys=True))
    return int(report['status']!='PASS')


if __name__=='__main__':raise SystemExit(main())
