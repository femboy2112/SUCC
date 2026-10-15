"""Reproduce the exact authentic theta Taylor-jet certificate, no zero inputs."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.theta_taylor_jets import receipt

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    data=receipt()
    txt=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.verify:
        if json.loads(args.verify.read_text())!=data:
            raise SystemExit('THETA_JET_SOURCE_RECEIPT_MISMATCH')
        print('THETA_JET_SOURCE_RECEIPT_VERIFIED')
    elif args.output:
        args.output.write_text(txt,encoding='utf-8')
    else:
        print(txt,end='')

if __name__=='__main__':main()
