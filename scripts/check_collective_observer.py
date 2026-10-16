#!/usr/bin/env python3
"""Run reproducible gates without converting runtime receipts into theorems."""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def snapshot():
    paths = sorted(set(ROOT.glob('observational_succ/*.py')) |
                   set(ROOT.glob('tests/test_*.py')) |
                   set(ROOT.glob('scripts/*collective*.py')))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    before = snapshot()
    commands = [
        ('provenance', ['scripts/verify_provenance.py']),
        ('lambda-tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_source_lambda.py', '-v']),
        ('consensus-tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_consensus_lambda.py', '-v']),
        ('collective-tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_collective_*.py', '-v']),
        ('observer-foundations', ['scripts/observer_foundations_probe.py']),
        ('ordinal', ['scripts/ordinal_succ_report_probe.py']),
        ('lambda', ['scripts/source_lambda_probe.py']),
        ('consensus', ['scripts/consensus_lambda_probe.py']),
    ]
    for name in ('effects', 'modular', 'policy', 'gamma', 'spectral'):
        commands.append((name, [f'scripts/collective_{name}_probe.py']))
    if args.source_root:
        commands.append(('spectral-source', ['scripts/collective_spectral_probe.py',
                        '--source', '--source-root', str(args.source_root.resolve())]))
    if args.full:
        commands.append(('full-tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v']))
    receipt = {'python': platform.python_version(), 'executable': sys.executable,
               'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'head_at_start': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
               'source_sha256_before': before, 'runs': [],
               'runtime_validation_is_not_semantic_or_kernel_proof': True}
    failure = False
    for name, command in commands:
        started = time.monotonic()
        argv = [sys.executable, *command]
        print('RUN '+name, flush=True)
        stdout, stderr = out/(name+'.stdout'), out/(name+'.stderr')
        with stdout.open('wb') as so, stderr.open('wb') as se:
            try:
                code = subprocess.run(argv, cwd=ROOT, stdout=so, stderr=se, timeout=1800).returncode
            except subprocess.TimeoutExpired:
                code = 124
        text = stderr.read_text(errors='replace')
        count = re.search(r'Ran (\d+) tests? in ([\d.]+)s', text)
        record = {'name': name, 'command': argv, 'returncode': code,
                  'wall_seconds': round(time.monotonic()-started, 3),
                  'stdout_sha256': hashlib.sha256(stdout.read_bytes()).hexdigest(),
                  'stderr_sha256': hashlib.sha256(stderr.read_bytes()).hexdigest()}
        if count:
            record['tests'] = int(count.group(1))
            record['test_seconds'] = float(count.group(2))
            record['unittest_OK'] = bool(re.search(r'^OK$', text, re.M))
            record['skipped'] = len(re.findall(r'\.\.\. skipped ', text))
            if not record['unittest_OK'] or record['skipped']:
                failure = True
        receipt['runs'].append(record)
        failure |= code != 0
        (out/'manifest.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
        print(f'DONE {name}: exit {code}', flush=True)
    after = snapshot()
    receipt.update(source_sha256_after=after, sources_stable=before == after,
                   all_gates_passed=not failure and before == after)
    (out/'manifest.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    return 0 if receipt['all_gates_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
