"""Run this scoped package and preserve raw outputs with command metadata."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--only',choices=('tests','probe','oracle','grids','review'))
    parser.add_argument('--suffix',default='')
    args=parser.parse_args()
    base=Path(__file__).resolve().parent
    commands=[('tests','focused_tests.log',[sys.executable,'-m','unittest','discover','-v','-s','.','-p','test_*.py']),
              ('probe','probe_receipt.json',[sys.executable,'run_probe.py']),
              ('grids','approximate_grid_receipt.json',[sys.executable,'approximate_grids.py']),
              ('oracle','independent_oracle_receipt.json',[sys.executable,'independent_oracle.py']),
              ('review','gauss_review_receipt.json',[sys.executable,'review_gauss.py'])]
    records=[]
    for key,name,argv in commands:
        if args.only and args.only!=key:continue
        if args.suffix:
            p=Path(name);name=p.stem+'-'+args.suffix+p.suffix
        dest=base/name
        if dest.exists():raise RuntimeError('refusing to overwrite '+name)
        start=time.monotonic()
        row={'argv':argv,'cwd':str(base),'start_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
             'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=base,text=True).strip()}
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
        with dest.open('w') as out:
            run=subprocess.run(argv,cwd=base,stdout=out,stderr=subprocess.STDOUT,env=env,timeout=600)
        row.update(exit_code=run.returncode,elapsed_seconds=time.monotonic()-start,
            end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),output=name,
            sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
        records.append(row)
        meta_name='command_receipts'+('-'+args.suffix if args.suffix else '')+('.'+args.only if args.only else '')+'.json'
        (base/meta_name).write_text(json.dumps(records,indent=2)+'\n')
        print(json.dumps(row),flush=True)
        if run.returncode:return run.returncode
    return 0


if __name__=='__main__':raise SystemExit(main())
