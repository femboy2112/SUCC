"""Replay scoped tests in separate processes; optional required main gates.

Run from any directory. Outputs go to a requested directory, never to frozen
receipts. Independent oracle names cannot collide across subprocesses.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--full",action="store_true",help="also run the four AGENTS.md gates")
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONPATH=str(ROOT),OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1")
    commands=[]
    for name,folder in (("learning",HERE),("arithmetic",HERE/"arithmetic"),
                        ("spectral",HERE/"spectral"),("crucible",HERE/"crucible")):
        commands.append((name,[sys.executable,"-m","unittest","discover","-s",str(folder),
                               "-p","test_learning.py" if name=="learning" else "test_*.py","-v"]))
    commands.extend([
        ("arithmetic_receipts",[sys.executable,str(HERE/"arithmetic/run_receipts.py"),
                                "--output",str(args.output/"arithmetic_receipts")]),
        ("prime_epoch_receipts",[sys.executable,str(HERE/"arithmetic/run_prime_epoch_receipts.py"),
                                 "--output",str(args.output/"arithmetic_receipts")]),
        ("receipt_equality",[sys.executable,"-c",
          "from pathlib import Path\n"
          "original=Path("+repr(str(HERE/"arithmetic"))+")\n"
          "replayed=Path("+repr(str(args.output/"arithmetic_receipts"))+")\n"
          "for name in ('FINITE_RECEIPTS.json','PRIME_EPOCH_RECEIPTS.json'):\n"
          " assert (original/name).read_bytes()==(replayed/name).read_bytes(),name\n"
          " print(name, 'byte-identical')"]),
        ("spectral_oracle",[sys.executable,str(HERE/"spectral/independent_oracle.py")]),
        ("crucible_oracle",[sys.executable,"-c",
          "import sys,json;sys.path.insert(0,"+repr(str(HERE/"crucible"))+")\n"
          "import hostile_oracle;print(json.dumps(hostile_oracle.run(),sort_keys=True))"]),
        ("lean_version",["lean","--version"]),
        ("lean",["lean",str(HERE/"crucible/ConditionalMemory.lean")]),
    ])
    if args.full:
        commands.extend((Path(s).stem,[sys.executable,s]) for s in (
            "scripts/verify_provenance.py","scripts/observer_foundations_probe.py",
            "scripts/ordinal_succ_report_probe.py"))
        commands.append(("native_suite",[sys.executable,"-m","unittest","discover",
                                         "-s","tests","-p","test_*.py"]))
    rows=[]
    for name,command in commands:
        start=time.monotonic()
        with (args.output/(name+".log")).open("w") as log:
            try:
                result=subprocess.run(command,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
                code=result.returncode
            except OSError as error:
                log.write(str(error)+"\n");code=127
        rows.append({"name":name,"command":command,"exit_code":code,
                     "seconds":time.monotonic()-start})
        print(name,code,flush=True)
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in HERE.rglob("*") if p.suffix in (".py",".lean")}
    result={"baseline":"d32342d375f44ddf62221ad6aff2f534abdc0a03",
            "commands":rows,"code_sha256":hashes,
            "all_passed":all(r["exit_code"]==0 for r in rows),
            "pi_base16_normality":"OPEN","RH":"OPEN"}
    (args.output/"replay.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    return 0 if result["all_passed"] else 1


if __name__=="__main__":raise SystemExit(main())
