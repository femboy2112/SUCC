"""Replay exact-rational χ4 source/conductor/parity proof receipts."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.source_character_interaction import character_receipt


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    data=character_receipt()
    if a.verify:
        if json.loads(a.verify.read_text())!=data:
            raise SystemExit('SOURCE_CHARACTER_RECEIPT_MISMATCH')
        print('SOURCE_CHARACTER_RECEIPT_VERIFIED')
    else:
        txt=json.dumps(data,sort_keys=True,indent=2)+'\n'
        if a.output:a.output.write_text(txt)
        else:print(txt,end='')

if __name__=='__main__':main()
