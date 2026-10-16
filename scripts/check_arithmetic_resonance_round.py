#!/usr/bin/env python3
"""Bounded source-stable validation of Arithmetic Resonance and inherited gates."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
MODULES = ('prime_wavefront_geometry', 'spectral_response', 'arithmetic_source_range',
           'arithmetic_resolvent', 'cross_prime_wavefront', 'spectral_tail_contract',
           'source_proof_certificate', 'compact_galerkin')


def snapshot():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for directory in ('observational_succ', 'tests', 'scripts')
            for p in sorted((ROOT/directory).glob('*.py'))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', required=True)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--focused-only', action='store_true')
    parser.add_argument('--probes', action='store_true')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    commands = [('versions', ['-c', 'import sys,numpy,scipy,mpmath,sympy; print(sys.version); print({x.__name__:x.__version__ for x in (numpy,scipy,mpmath,sympy)})'])]
    commands += [('focused-'+m, ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_'+m+'.py', '-v']) for m in MODULES]
    if not args.focused_only:
        commands += [('full-unittest', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py'])]
    commands += [(m, ['scripts/'+m+'.py']) for m in
                 ('verify_provenance', 'observer_foundations_probe', 'ordinal_succ_report_probe')]
    if args.probes:
        commands += [(m+'-probe', ['scripts/'+m+'_probe.py', '--output', str(args.output.resolve()/(m+'.json'))])
                     for m in MODULES[:5]]
    result = {'timestamp_utc': datetime.now(timezone.utc).isoformat(),
              'head_at_start': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
              'source_before': snapshot(), 'commands': [], 'finished': False}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    for label, argv in commands:
        start = time.monotonic(); cmd = [args.python, '-B', *argv]
        try:
            p = subprocess.run(cmd, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, timeout=2400 if label == 'full-unittest' else 900)
            log, code = p.stdout, p.returncode
        except subprocess.TimeoutExpired as exc:
            log, code = exc.stdout or '', 124
            if isinstance(log, bytes):
                log = log.decode(errors='replace')
            log += '\nTIMEOUT: validation incomplete\n'
        path = args.output/(label+'.log'); path.write_text(log)
        result['commands'].append({'argv': cmd, 'label': label, 'exit_code': code,
                                   'elapsed_seconds': round(time.monotonic()-start, 3),
                                   'log': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        (args.output/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
        print(label+': exit '+str(code), flush=True)
    result.update(source_after=snapshot(), finished=True)
    result['source_stable'] = result['source_before'] == result['source_after']
    result['all_commands_passed'] = all(x['exit_code'] == 0 for x in result['commands'])
    (args.output/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    raise SystemExit(0 if result['source_stable'] and result['all_commands_passed'] else 1)


if __name__ == '__main__':
    main()
