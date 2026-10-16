"""Pure exact rational observer/zero-oracle-free Hilbert Weil atlas receipt."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.hilbert_weil_atlas import receipt


def main():
    p=argparse.ArgumentParser(description="Verify Hilbert Weil SUCC source-relative observer")
    p.add_argument("--verify",type=Path)
    p.add_argument("--output",type=Path)
    opts=p.parse_args()
    result=receipt()
    if opts.verify is not None:
        if json.loads(opts.verify.read_text(encoding="utf-8")) != result:
            raise SystemExit("HILBERT_WEIL_ATLAS_SOURCE_RECEIPT_MISMATCH")
        print("HILBERT_WEIL_ATLAS_RECEIPT_VERIFIED")
        return
    output=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if opts.output is not None:opts.output.write_text(output,encoding="utf-8")
    else:print(output,end="")


if __name__=="__main__":main()
