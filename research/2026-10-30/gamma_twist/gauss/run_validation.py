"""Bounded, no-shell receipt runner for this scoped Gauss dossier."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extra", action="store_true")
    parser.add_argument("--tests-only", action="store_true")
    parser.add_argument("--tag", default="")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    commands = [
        ([sys.executable,"-m","unittest","-v","test_gauss_exact.py"],"focused_tests.log"),
        ([sys.executable,"run_probe.py"],"probe_receipt.json"),
        ([sys.executable,"independent_oracle.py","probe_receipt.json"],"independent_receipt.json")]
    if args.extra:
        commands = [([sys.executable,"extra_probe.py"],"extra_receipt"+args.tag+".json")]
    if args.tests_only:
        commands = [([sys.executable,"-m","unittest","-v","test_gauss_exact.py"],
                     "focused_tests"+args.tag+".log")]
    prefix = "extra_command_receipts" if args.extra else "tests_command_receipts" if args.tests_only else "command_receipts"
    meta = here/(prefix+args.tag+".json")
    if meta.exists():
        raise SystemExit("Refusing to overwrite existing command receipts")
    receipts=[]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")
    for command, filename in commands:
        output = here/filename
        if output.exists():
            raise SystemExit("Refusing to overwrite "+str(output))
        start=time.monotonic()
        row={"command":command,"cwd":str(here),"output":filename,
             "start_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"memory_mib":768,
             "git_head":subprocess.check_output(["git","rev-parse","HEAD"],cwd=here,text=True).strip()}
        def limits():
            resource.setrlimit(resource.RLIMIT_AS,(768*1024**2,768*1024**2))
        with output.open("w") as log:
            completed=subprocess.run(command,cwd=here,env=env,stdout=log,stderr=subprocess.STDOUT,
                                     timeout=600,check=False,preexec_fn=limits)
        row.update(exit_code=completed.returncode,elapsed_seconds=round(time.monotonic()-start,3),
                   end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                   sha256=hashlib.sha256(output.read_bytes()).hexdigest(),bytes=output.stat().st_size)
        receipts.append(row)
        meta.write_text(json.dumps(receipts,indent=2)+"\n")
        print(json.dumps(row),flush=True)
        if completed.returncode:
            print(output.read_text()[-3000:])
            return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
