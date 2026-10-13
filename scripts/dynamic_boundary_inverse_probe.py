"""Deterministic exact rational E-tower inverse-network research receipt."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from observational_succ.dynamic_boundary_inverse import demonstration


def wire(x):
    if isinstance(x,Fraction):return str(x)
    if isinstance(x,tuple):return [wire(a) for a in x]
    if isinstance(x,list):return [wire(a) for a in x]
    if isinstance(x,dict):return {k:wire(v) for k,v in x.items()}
    return x


def main():
    payload=wire(demonstration())
    saved=Path(__file__).resolve().parents[1]/'research/2026-10-12/DYNAMIC_BOUNDARY_INVERSE_RECEIPT.json'
    if saved.exists():
        expected=json.loads(saved.read_text(encoding='utf-8'))
        if expected!=payload:
            raise RuntimeError('Exact saved source receipt does not reproduce')
    print(json.dumps(payload,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
