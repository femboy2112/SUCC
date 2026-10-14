"""Reproduce source-typed mathematical receipts; zero-free construction."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.prime_categorical_sphere import receipt


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    txt=json.dumps(receipt(),sort_keys=True,indent=2,default=str)+'\n'
    if args.output:
        Path(args.output).write_text(txt,encoding='utf-8')
    else:
        print(txt,end='')


if __name__=='__main__':main()
