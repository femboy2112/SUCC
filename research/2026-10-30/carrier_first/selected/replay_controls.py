"""Replay exact pinned controls without importing or merging a sibling branch."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
COMMIT = "f650aab0c8710b502f3e08ec1cb2b351c26b2b3f"
PREFIX = "research/2026-10-30/arithmetic_barrier/transfer/"


def main():
    sources = []
    with tempfile.TemporaryDirectory(prefix="succ-selected-control-") as tmp:
        for name in ("transfer_probe.py", "test_transfer.py"):
            path = PREFIX + name
            raw = subprocess.check_output(["git", "show", COMMIT + ":" + path], cwd=ROOT)
            sources.append(dict(commit=COMMIT, path=path,
                                sha256=hashlib.sha256(raw).hexdigest()))
            Path(tmp, name).write_bytes(raw)
        print(json.dumps({"sources": sources,
                          "authority": "replay of pinned inherited tests, not new independent proof"}, indent=2), flush=True)
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", tmp,
                                 "-p", "test_transfer.py", "-v"], cwd=ROOT, check=False)
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
