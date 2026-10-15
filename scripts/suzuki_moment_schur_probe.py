"""Deterministic exact-rational source-typed Suzuki moment/Schur receipt.

No zero lookup or fitted PSD prior. --source-stage genuinely imports the immutable
parent #85 source module (and refuses a SHA mismatch).
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_moment_schur import receipt,source_small_grid_demonstration


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--source-stage',action='store_true')
    ns=ap.parse_args()
    if ns.source_stage:
        if ns.verify is not None:raise SystemExit('choose only one certificate protocol')
        result=source_small_grid_demonstration()
        if result['low_modes']!=30 or result['parity_blocks']!=[15,15] or not result['source_gamma_gain'] or result['RH_proved']:
            raise SystemExit('AUTHENTIC_STAGE_CERTIFICATE_FAILED')
        print(json.dumps(result,indent=2,sort_keys=True));return
    obj=receipt()
    if ns.verify is not None:
        if not ns.verify.exists():raise SystemExit('MISSING_PINNED_SCIENTIFIC_RECEIPT')
        try:stored=json.loads(ns.verify.read_text())
        except Exception as exc:raise SystemExit('MALFORMED_SCIENTIFIC_RECEIPT') from exc
        if stored != obj:raise SystemExit('SUZUKI_SOURCE_SCHUR_RECEIPT_MISMATCH')
        print('SUZUKI_CANONICAL_SCHUR_EXACT_RECEIPT_VERIFIED');return
    print(json.dumps(obj,sort_keys=True,indent=2))

if __name__=='__main__': main()
