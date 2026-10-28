#!/usr/bin/env python3
"""Run new exact census and independent Fraction replay sequentially."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_referee_census import complete_referee_census
from scripts.lonely_runner_referee_fraction import fraction_census, known_controls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-n", type=int, default=21)
    parser.add_argument("--max-n", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 5 <= args.min_n <= args.max_n <= 30:
        parser.error("require 5<=min-n<=max-n<=30")
    if hasattr(os, "sched_getaffinity"):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    records = []
    for n in range(args.min_n, args.max_n+1):
        started = time.monotonic()
        primary, certificates = complete_referee_census(n)
        (destination/f"census-n{n}.json").write_text(json.dumps(primary, indent=2, sort_keys=True)+"\n")
        for name, certificate in certificates.items():
            (destination/name).write_text(json.dumps(certificate, indent=2, sort_keys=True)+"\n")
        primary_seconds = time.monotonic()-started
        print(f"n={n} primary rows={primary['first_speeds']} tests={primary['individually_tested']} survivors={primary['survivor_count']} seconds={primary_seconds:.3f}", flush=True)
        started = time.monotonic()
        independent = fraction_census(n)
        (destination/f"fraction-n{n}.json").write_text(json.dumps(independent, indent=2, sort_keys=True)+"\n")
        for field in ("proved_domain_count", "first_occupancy_rejected", "width_rejected", "first_speeds"):
            if primary[field] != independent[field]:
                raise ArithmeticError(f"independent count mismatch n={n}, field={field}")
        if primary["center_rejected"]+primary["individually_tested"] != independent["fraction_cover_checks"]:
            raise ArithmeticError("independent candidate accounting mismatch")
        accepted = [{"removed": x["removed"], "inserted": x["inserted"]} for x in primary["survivors"]]
        if accepted != independent["survivors"]:
            raise ArithmeticError("independent survivor classification mismatch")
        independent_seconds = time.monotonic()-started
        print(f"n={n} Fraction checks={independent['fraction_cover_checks']} survivors={independent['survivor_count']} seconds={independent_seconds:.3f}", flush=True)
        records.append({"n": n, "primary_seconds": primary_seconds,
                        "independent_seconds": independent_seconds,
                        "proved_domain_count": primary["proved_domain_count"],
                        "first_speeds": primary["first_speeds"],
                        "primary_gap_tests": primary["individually_tested"],
                        "independent_fraction_cover_checks": independent["fraction_cover_checks"],
                        "survivors": accepted})
    controls = known_controls()
    (destination/"known-controls.json").write_text(json.dumps(controls, indent=2, sort_keys=True)+"\n")
    paths = ["observational_succ/lonely_runner_referee_census.py", "scripts/lonely_runner_referee_census.py",
             "scripts/lonely_runner_referee_fraction.py", "observational_succ/lonely_runner_census.py",
             "observational_succ/lonely_runner_two_entry.py"]
    summary = {"schema": "SUCC-referee-census-replay-v1", "complete": True,
               "records": records, "known_controls": controls, "workers": 1,
               "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
               "authority": "complete finite classifications under paper Gamma/pruning proofs; independent Fraction replay",
               "no_full_census_kernel_or_novelty_claim": True}
    (destination/"summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n")
    print("COMPLETE primary and Fraction classifications agree; known n5,n8,n74,n284 controls pass", flush=True)


if __name__ == "__main__":
    main()
