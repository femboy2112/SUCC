#!/usr/bin/env python3
"""Exact finite effective-field probe; universal facts proved in source dossier."""
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from observational_succ.effective_field_gates import effective_field_demo


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    opt=p.parse_args()
    actual=effective_field_demo()
    path=ROOT/'research/2026-10-15/EFFECTIVE_FIELD_GATES_RECEIPT.json'
    if opt.verify:
        if actual!=json.loads(path.read_text(encoding='utf-8')):
            raise SystemExit('EFFECTIVE_FIELD_GATES_RECEIPT DRIFT')
        print('Effective field gates: source-calibrated finite receipt verified')
    else:print(json.dumps(actual,indent=2,sort_keys=True))
if __name__=='__main__':main()
