#!/usr/bin/env python3
"""Complete exact two-entry census; stdout by default, read-only --verify replay."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.lonely_runner_census import canonical_bytes, complete_census


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--certificate-dir", type=Path)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--max-domain-candidates", type=int, default=1000000)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    def progress(n, r1, r2, rows, tested):
        print(f"n={n} removed=({r1},{r2}): {rows} first speeds, {tested} exact gap tests", file=sys.stderr, flush=True)
    receipt, certificates = complete_census(args.n, max_domain_candidates=args.max_domain_candidates,
                                             progress=progress if args.progress else None)
    rendered = json.dumps(receipt, sort_keys=True, indent=2) + "\n"
    if args.verify:
        if args.verify.read_text() != rendered:
            raise SystemExit("census receipt differs from complete exact replay")
        if args.certificate_dir:
            for filename, certificate in certificates.items():
                if (args.certificate_dir / filename).read_bytes() != canonical_bytes(certificate):
                    raise SystemExit(f"certificate differs from exact replay: {filename}")
        print(f"n={args.n}: complete census and supplied certificates match exact replay")
    else:
        if args.certificate_dir:
            args.certificate_dir.mkdir(parents=True, exist_ok=True)
            for filename, certificate in certificates.items():
                (args.certificate_dir / filename).write_bytes(canonical_bytes(certificate))
        if args.output:
            args.output.write_text(rendered)
        else:
            print(rendered, end="")


if __name__ == "__main__":
    main()
