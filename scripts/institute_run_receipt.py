#!/usr/bin/env python3
"""Run one bounded command and preserve its bytes, status and source snapshot."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a command is required")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    state = subprocess.check_output(["git", "status", "--porcelain"], text=True)
    before = time.monotonic()
    with output.with_suffix(".log").open("wb") as log:
        proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
        timed_out = False
        try:
            status = proc.wait(timeout=args.timeout)
        except subprocess.TimeoutExpired:
            import signal
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
            status, timed_out = 124, True
    record = dict(command=command, cwd=str(Path.cwd()), started_utc=started,
                  finished_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  elapsed_seconds=round(time.monotonic()-before, 6), exit_code=status,
                  timeout=timed_out, git_head=head, git_status_before=state,
                  log=output.with_suffix(".log").as_posix(),
                  log_sha256=hashlib.sha256(output.with_suffix(".log").read_bytes()).hexdigest())
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record), flush=True)
    raise SystemExit(status)


if __name__ == "__main__":
    main()
