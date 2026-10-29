#!/usr/bin/env python3
"""Verify a source-labelled shifted-runner circle-cover certificate independently."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_verify import (  # noqa: E402
    CandidateBudgetExceeded, CertificateError, exact_maxmin, verify_cover,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", help="JSON certificate path, or - for standard input")
    parser.add_argument("--coverage-only", action="store_true",
                        help="allow delta >= 1/(n+1); label the result non-strict")
    parser.add_argument("--exact-gamma", action="store_true",
                        help="also enumerate the complete finite max-min breakpoint set")
    parser.add_argument("--max-candidates", type=int, default=250000)
    args = parser.parse_args()
    try:
        source = sys.stdin.read() if args.certificate == "-" else Path(args.certificate).read_text()
        certificate = json.loads(source)
        result = verify_cover(certificate, require_counterexample=not args.coverage_only)
        if args.exact_gamma:
            result["exact_maxmin"] = exact_maxmin(certificate["velocities"], certificate["shifts"],
                                                 max_candidates=args.max_candidates)
        print(json.dumps(result, sort_keys=True, indent=2))
    except (CertificateError, CandidateBudgetExceeded, json.JSONDecodeError, OSError) as error:
        print(json.dumps({"accepted": False, "error": str(error)}, sort_keys=True), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
