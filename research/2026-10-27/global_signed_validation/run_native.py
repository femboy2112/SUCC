"""Run native gates with raw logs, exit codes and before/after source hashes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
COMMANDS = {
    'full_unittest': ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py'],
    'provenance': ['scripts/verify_provenance.py'],
    'observer': ['scripts/observer_foundations_probe.py'],
    'ordinal': ['scripts/ordinal_succ_report_probe.py'],
    'focused': ['-m', 'unittest', 'tests.test_global_branch_coercivity',
                'tests.test_global_source_curvature', 'tests.test_global_prime_resonance',
                'tests.test_wtf_global_calibration', '-v'],
}


def snapshot():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for folder in ('observational_succ', 'tests')
            for p in sorted((ROOT/folder).rglob('*.py'))}


def main():
    name = sys.argv[1]
    command = [sys.executable] + COMMANDS[name]
    before = snapshot()
    start = time.monotonic()
    stamp = datetime.now(timezone.utc).isoformat()
    log = OUT/f'{name}.log'
    with log.open('w') as stream:
        result = subprocess.run(command, cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
    after = snapshot()
    record = {'command': command, 'cwd': str(ROOT), 'started_utc': stamp,
              'seconds': round(time.monotonic()-start, 3), 'exit_code': result.returncode,
              'production_test_sources_unchanged': before == after,
              'source_count': len(before), 'log': log.name,
              'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()}
    (OUT/f'{name}_result.json').write_text(json.dumps(record, indent=2)+'\n')
    if name == 'full_unittest':
        (OUT/'python_source_snapshot.json').write_text(json.dumps(before, indent=2)+'\n')
    print(json.dumps(record), flush=True)
    raise SystemExit(result.returncode or (0 if before == after else 2))


if __name__ == '__main__':
    main()
