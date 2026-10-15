#!/usr/bin/env python3
"""Exact finite model-graph scientific receipt; run from repository root."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from observational_succ.global_model_sandwich import demo_receipt


def generate():
    return (json.dumps(demo_receipt(),indent=2,sort_keys=True,ensure_ascii=True)+"\n").encode("utf-8")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--verify",type=Path)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    if a.verify and a.output:ap.error("choose output OR verification")
    fresh=generate()
    if a.verify:
        if a.verify.read_bytes()!=fresh:
            raise SystemExit("GLOBAL_MODEL_SANDWICH_RECEIPT_MISMATCH")
        print("GLOBAL_MODEL_SANDWICH_RECEIPT_REPLAY_VERIFIED")
    elif a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_bytes(fresh)
        print("GLOBAL_MODEL_SANDWICH_RECEIPT_SAVED")
    else:
        print(fresh.decode(),end="")

if __name__=="__main__":main()
