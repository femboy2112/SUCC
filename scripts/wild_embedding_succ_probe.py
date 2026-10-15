"""Exact, deterministic SUCC wild-embedding research receipt (not topology proof)."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.wild_embedding_succ import receipt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    value=receipt()
    raw=json.dumps(value,sort_keys=True,indent=2)+'\n'
    if args.verify:
        if args.verify.read_bytes()!=raw.encode('utf-8'):
            raise SystemExit('WILD_EMBEDDING_SOURCE_RECEIPT_MISMATCH')
        print('WILD_EMBEDDING_SOURCE_RECEIPT_VERIFIED')
    elif args.output:
        args.output.write_text(raw,encoding='utf-8')
        print('WILD_EMBEDDING_RECEIPT_WRITTEN')
    else:
        print(raw,end='')


if __name__=='__main__':
    main()
