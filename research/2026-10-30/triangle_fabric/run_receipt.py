"""Run one bounded command and retain its raw output and execution metadata.

This records execution, not mathematical proof authority. Commands are argv
arrays (no shell). By default numerical libraries use one thread.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--cwd", default=".")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("command required after --")
    dest = Path(__file__).resolve().parent / "receipts"
    dest.mkdir(exist_ok=True)
    log = dest / (args.name + ".log")
    record = dest / (args.name + ".json")
    if log.exists() or record.exists():
        parser.error("receipt already exists: choose a new name")
    env = dict(os.environ)
    env.update({k: "1" for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    def limits():
        cap = args.memory_mib * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (cap, cap))
    start = time.monotonic()
    meta = {"command": command, "cwd": str(Path(args.cwd).resolve()),
            "start_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "timeout_seconds": args.timeout, "memory_limit_mib": args.memory_mib,
            "runner_python": sys.version, "threads": 1,
            "git_head_at_launch": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.cwd, text=True).strip()}
    # Expose a clearly unfinished record while the command runs, so tools
    # validating links to this receipt need not assume a nonexistent file.
    record.write_text(json.dumps({**meta, "status": "RUNNING"}, indent=2) + "\n")
    with log.open("w") as out:
        try:
            completed = subprocess.run(command, cwd=args.cwd, env=env,
                stdout=out, stderr=subprocess.STDOUT, timeout=args.timeout,
                preexec_fn=limits, check=False)
            meta.update(exit_code=completed.returncode, timed_out=False)
        except subprocess.TimeoutExpired:
            meta.update(exit_code=124, timed_out=True)
        except OSError as exc:
            out.write(str(exc) + "\n")
            meta.update(exit_code=127, launch_error=str(exc), timed_out=False)
    meta.update(elapsed_seconds=round(time.monotonic()-start, 3),
                end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                log_sha256=hashlib.sha256(log.read_bytes()).hexdigest(),
                log_bytes=log.stat().st_size)
    record.write_text(json.dumps(meta, indent=2) + "\n")
    print(json.dumps(meta, indent=2), flush=True)
    print(log.read_text()[-3000:], flush=True)
    return meta["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
