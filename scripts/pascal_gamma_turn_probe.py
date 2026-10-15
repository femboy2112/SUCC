"""Exact-rational Pascal Gamma quarter-turn receipt; no unknown zeros."""
import argparse
import json
from pathlib import Path
from observational_succ.pascal_gamma_turn import receipt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output')
    args=p.parse_args()
    data=json.dumps(receipt(),sort_keys=True,indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(data,encoding='utf8')
    else:
        print(data,end='')

if __name__=='__main__':main()
