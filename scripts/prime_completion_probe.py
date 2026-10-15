#!/usr/bin/env python3
"""Recalculate exact p-adic source phantom/closed-set/Haar receipts."""
from pathlib import Path
import argparse, json, sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from observational_succ.prime_completion_obstructions import idealhard_prime_bridge_probe


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    options=parser.parse_args()
    measured=idealhard_prime_bridge_probe()
    expected=ROOT/'research/2026-10-15/PRIME_COMPLETION_OBSTRUCTIONS_RECEIPT.json'
    if options.verify:
        if measured!=json.loads(expected.read_text(encoding='utf-8')):
            raise SystemExit('PRIME COMPLETION source/Haar receipt mismatch')
        print('PRIME COMPLETION: exact source/fourier/haar receipt verified')
    else:
        print(json.dumps(measured,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
