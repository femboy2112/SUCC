#!/usr/bin/env python3
"""Replay all root unittests in module-preserving shards, verifying exact coverage.

No tests are excluded, changed, marked expected-failure, or given new thresholds.
This is a documented full-suite replay, not the literal serial unittest command.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest

REPO = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def collect(workers):
    os.chdir(REPO)
    sys.path.insert(0, str(REPO))
    loader = unittest.TestLoader()
    cases = list(flatten(loader.discover("tests", pattern="test_*.py")))
    if loader.errors:
        raise RuntimeError("Test discovery failed: " + "\n".join(loader.errors))
    ids = [case.id() for case in cases]
    assert len(set(ids)) == len(ids), "Duplicate collected test IDs"
    modules = sorted({case.__class__.__module__ for case in cases})
    assignment = {name: i % workers for i, name in enumerate(modules)}
    shards = [[case for case in cases
               if assignment[case.__class__.__module__] == i] for i in range(workers)]
    assert sorted(case.id() for shard in shards for case in shard) == sorted(ids)
    return cases, shards


def digest_ids(ids):
    return hashlib.sha256(("\n".join(sorted(ids))+"\n").encode()).hexdigest()


def run_child(index, workers):
    _, shards = collect(workers)
    selected = shards[index]
    expected = [case.id() for case in selected]
    start = time.monotonic()
    result = unittest.TextTestRunner(verbosity=1).run(unittest.TestSuite(selected))
    receipt = {
        "shard": index, "workers": workers, "collected": len(expected),
        "tests_run": result.testsRun, "failures": len(result.failures),
        "errors": len(result.errors), "skipped": len(result.skipped),
        "expected_failures": len(result.expectedFailures),
        "unexpected_successes": len(result.unexpectedSuccesses),
        "test_ids_sha256": digest_ids(expected),
        "duration_seconds": round(time.monotonic()-start, 3),
        "successful": result.wasSuccessful() and result.testsRun == len(expected),
    }
    (OUT/f"full_suite_shard_{index}.json").write_text(json.dumps(receipt, indent=2)+"\n")
    return 0 if receipt["successful"] else 1


def run_parent(workers):
    cases, shards = collect(workers)
    env = dict(os.environ, PYTHONPATH=str(REPO), OPENBLAS_NUM_THREADS="1",
               OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    coverage = {
        "unsharded_collection_count": len(cases),
        "unsharded_test_ids_sha256": digest_ids(case.id() for case in cases),
        "workers": workers, "assignment": "sorted module ordinal modulo workers",
        "all_ids_unique": True, "partition_exactly_equals_unsharded_collection": True,
        "environment": {"PYTHONPATH": ".", "OPENBLAS_NUM_THREADS": "1",
                        "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "shards": [{"shard": i, "count": len(shard),
                    "test_ids_sha256": digest_ids(case.id() for case in shard),
                    "modules": sorted({case.__class__.__module__ for case in shard})}
                   for i, shard in enumerate(shards)]
    }
    (OUT/"full_suite_coverage.json").write_text(json.dumps(coverage, indent=2)+"\n")
    print(f"Collected {len(cases)} tests; exact partition into {workers} workers.", flush=True)

    def execute(index):
        log = OUT/f"full_suite_shard_{index}.txt"
        with log.open("w") as stream:
            try:
                rc = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                                     "--workers", str(workers), "--child", str(index)],
                                    cwd=REPO, env=env, stdout=stream, stderr=subprocess.STDOUT,
                                    timeout=1200).returncode
            except subprocess.TimeoutExpired:
                rc = 124
        log.write_text(log.read_text(errors="replace").replace(str(REPO), "<repo>"))
        path = OUT/f"full_suite_shard_{index}.json"
        data = json.loads(path.read_text()) if path.exists() else {"shard": index, "successful": False}
        data["exit_code"] = rc
        data["published_log_sha256"] = hashlib.sha256(log.read_bytes()).hexdigest()
        data["log_normalization"] = "execution root replaced with <repo>"
        path.write_text(json.dumps(data, indent=2)+"\n")
        return data

    results = []
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for future in as_completed([pool.submit(execute, i) for i in range(workers)]):
            data = future.result()
            expected = coverage["shards"][data["shard"]]
            assert data.get("test_ids_sha256") == expected["test_ids_sha256"]
            results.append(data)
            print(json.dumps(data), flush=True)
    total = sum(r.get("tests_run", 0) for r in results)
    summary = {
        "status": "PASS" if total == len(cases) and all(
            r["successful"] and r["exit_code"] == 0 for r in results) else "FAIL",
        "tests_run": total, "expected_tests": len(cases),
        "failures": sum(r.get("failures", 0) for r in results),
        "errors": sum(r.get("errors", 0) for r in results),
        "skipped": sum(r.get("skipped", 0) for r in results),
        "workers": workers, "duration_seconds": round(time.monotonic()-start, 3),
        "full_collection_sha256": coverage["unsharded_test_ids_sha256"],
        "coverage_receipt": "full_suite_coverage.json",
        "scope": "Every root-discovered test, exact once-only partition; same tests and assertions as serial discovery. This does not run research-local tests or Lean."
    }
    (OUT/"full_suite_receipt.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(summary), flush=True)
    return 0 if summary["status"] == "PASS" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--child", type=int)
    args = parser.parse_args()
    if args.workers < 1 or (args.child is not None and not 0 <= args.child < args.workers):
        parser.error("invalid worker/shard count")
    return run_child(args.child, args.workers) if args.child is not None else run_parent(args.workers)


if __name__ == "__main__":
    raise SystemExit(main())
