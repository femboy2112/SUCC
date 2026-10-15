#!/usr/bin/env python3
"""Exact deterministic finite-source / Zeno science receipt, no zeros or RH claims."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.zeno_ambient_weil import verdict_receipt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    r=verdict_receipt()
    data=json.dumps(r,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if args.verify:
        text=args.verify.read_text(encoding='utf-8')
        if text!=data:
            raise SystemExit('ZENO_AMBIENT_WEIL_RECEIPT_MISMATCH')
        print('ZENO_AMBIENT_WEIL_RECEIPT_VERIFIED')
    elif args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(data,encoding='utf-8')
        print('ZENO_AMBIENT_WEIL_RECEIPT_WRITTEN')
    else:
        print(data,end='')

if __name__=='__main__':main()
