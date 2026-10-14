"""Replay the exact rational source certificate, or produce its JSON receipt."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_markov_gluing import receipt


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--verify', type=Path)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    data = receipt()
    if args.verify:
        if json.loads(args.verify.read_text()) != data:
            raise SystemExit('RECEIPT_MISMATCH')
        print('SUZUKI_MARKOV_GLUING_RECEIPT_VERIFIED')
    else:
        text = json.dumps(data, indent=2, sort_keys=True) + '\n'
        if args.output:
            args.output.write_text(text)
        else:
            print(text, end='')


if __name__ == '__main__':
    main()
