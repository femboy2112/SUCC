"""Replay the round in fresh output; preserve receipts and pinned inputs."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = '1990b05117d84b33094c8e0f53f7d19b60f48060'


def normal(value):
    if isinstance(value, dict):
        return {k: normal(v) for k, v in value.items() if k != 'seconds'}
    if isinstance(value, list):
        return [normal(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--full', action='store_true', help='also repeat unchanged native suite')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    measurements = out/'measurements'
    measurements.mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONPATH=str(ROOT), OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    commands = []
    for name, folder in [('root', HERE), ('cube', HERE/'cube'), ('chronology', HERE/'chronology'), ('hostile', HERE/'hostile')]:
        commands.append((name+'_tests', [sys.executable, '-m', 'unittest', 'discover', '-s', str(folder), '-p', 'test_*.py', '-v']))
    pairs = []
    for name, script, retained in [
        ('cube_oracle', 'cube/cube_oracle.py', 'cube/receipt.json'),
        ('cube_peer', 'cube/peer_review.py', 'cube/peer_checks.json'),
        ('chronology_oracle', 'chronology/oracle.py', 'chronology/RECEIPTS.json'),
        ('chronology_leakage', 'chronology/leakage_oracle.py', 'chronology/LEAKAGE_RECEIPTS.json'),
        ('hostile_oracle', 'hostile/exact_oracle.py', 'hostile/EXACT_RECEIPT.json'),
        ('independent_instrument', 'hostile/review_instrument.py', 'hostile/INDEPENDENT_REVIEW.json')]:
        target = out/(name+'.json')
        commands.append((name, [sys.executable, str(HERE/script), '--output', str(target)]))
        pairs.append((HERE/retained, target))
    for stage in ('development', 'holdout', 'stress'):
        commands.append(('lag_'+stage, [sys.executable, str(HERE/'run_lag_probe.py'), '--stage', stage, '--output', str(measurements)]))
    commands.append(('selector_oracle', [sys.executable, str(HERE/'selector_oracle.py'), str(out/'selector.json')]))
    pairs.append((HERE/'receipts/selector.json', out/'selector.json'))
    commands.append(('lean_version', ['lean', '--version']))
    commands.append(('lean_transport', ['lean', str(HERE/'hostile/ExactTransport.lean')]))
    for script in ('verify_provenance', 'observer_foundations_probe', 'ordinal_succ_report_probe'):
        commands.append((script, [sys.executable, str(ROOT/'scripts'/(script+'.py'))]))
    if args.full:
        commands.append(('native_suite', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py']))
    results = []
    for name, command in commands:
        started = time.monotonic()
        with (out/(name+'.log')).open('w') as log:
            try:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
                code = result.returncode
            except OSError as error:
                log.write(str(error)+'\n')
                code = 127
        results.append({'name': name, 'command': command, 'exit_code': code, 'seconds': time.monotonic()-started})
        print(name, code, flush=True)
    pairs.extend((p, measurements/p.name) for p in sorted((HERE/'receipts').glob('lag_*.json')))
    comparisons = []
    for left, right in pairs:
        try:
            same = normal(json.loads(left.read_text())) == normal(json.loads(right.read_text()))
        except (OSError, ValueError):
            same = False
        comparisons.append({'retained': str(left.relative_to(HERE)), 'replay': str(right.relative_to(out)), 'identical_mathematical_payload': same})
    native_paths = ['observational_succ', 'tests', 'scripts', 'formal', 'provenance', 'docs', 'AGENTS.md', 'pyproject.toml', 'requirements.txt', 'requirements-dev.txt']
    scope = subprocess.run(['git', 'diff', '--exit-code', PARENT, '--', *native_paths], cwd=ROOT, capture_output=True, text=True)
    (out/'native_scope.log').write_text(scope.stdout+scope.stderr)
    result = {'parent': PARENT, 'commands': results, 'comparisons': comparisons,
              'native_inputs_unchanged': scope.returncode == 0, 'native_suite_rerun': args.full,
              'inherited_native_receipt': 'research/2026-11-07/learning_yoneda/validation/native_suite.json',
              'code_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in HERE.rglob('*') if p.suffix in ('.py', '.lean')},
              'all_passed': all(r['exit_code'] == 0 for r in results) and all(r['identical_mathematical_payload'] for r in comparisons) and scope.returncode == 0,
              'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (out/'replay.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    return 0 if result['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
