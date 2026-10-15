"""Replay a frozen, zero-independent rational signed-Weil spectral-tail receipt."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.signed_weil_h1_tail import receipt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    actual=receipt()
    if args.verify is not None:
        expected=json.loads(args.verify.read_text())
        if expected!=actual:
            raise SystemExit('SIGNED_WEIL_H1_TAIL_RECEIPT_MISMATCH')
        print('SIGNED_WEIL_H1_TAIL_RECEIPT_VERIFIED')
    elif args.output is not None:
        args.output.write_text(json.dumps(actual,indent=2,sort_keys=True)+'\n')
        print('SIGNED_WEIL_H1_TAIL_RECEIPT_WRITTEN')
    else:
        print(json.dumps(actual,indent=2,sort_keys=True))

if __name__=='__main__':main()
