"""Fresh reproducible quotient/gamma checks; no unrequested native rerun."""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    source_out = out/'source'
    py = sys.executable
    rel = str(HERE.relative_to(ROOT))
    commands = []
    comparisons = []
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')

    def run(name, argv):
        before = time.monotonic()
        with (out/f'{name}.log').open('w') as log:
            result = subprocess.run(argv, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
        commands.append({'name': name, 'command': argv, 'exit_code': result.returncode,
                         'seconds': time.monotonic()-before,
                         'log_sha256': sha256((out/f'{name}.log').read_bytes()).hexdigest()})
        print(name, result.returncode, flush=True)
        if result.returncode:
            raise RuntimeError(f'{name} failed; inspect {out/name}.log')

    def same(name, fresh, retained):
        equal = json.loads(fresh.read_text()) == json.loads(retained.read_text())
        comparisons.append({'name': name, 'equal': equal,
                            'retained_sha256': sha256(retained.read_bytes()).hexdigest()})
        if not equal:
            raise AssertionError(f'{name} mathematical replay differs')

    try:
        for name, folder, pattern in [('root_tests', '', 'test_source_probe.py'),
                                      ('quotient_tests', 'quotient', 'test_*.py'),
                                      ('gamma_tests', 'gamma', 'test_*.py'),
                                      ('hostile_tests', 'hostile', 'oracle.py')]:
            run(name, [py, '-m', 'unittest', 'discover', '-s', str(HERE/folder), '-p', pattern, '-v'])
        for name, filename in [('quotient', 'EXACT_RECEIPT.json'), ('gamma', 'RESULTS.json'),
                               ('hostile', 'RESULTS.json')]:
            fresh = out/f'{name}.json'
            run(name+'_oracle', [py, str(HERE/name/'oracle.py'), '--output', str(fresh)])
            same(name, fresh, HERE/name/filename)
        for stage in ('development', 'holdout'):
            run(stage, [py, rel+'/source_probe.py', '--stage', stage, '--output', str(source_out)])
        for retained in sorted((HERE/'results').glob('quotient_*.json')):
            same(retained.stem, source_out/retained.name, retained)
        same('summary', source_out/'SUMMARY.json', HERE/'results/SUMMARY.json')
        run('source_review', [py, rel+'/hostile/verify_source.py', '--output', str(out/'source_review.json')])
        same('source_review', out/'source_review.json', HERE/'hostile/SOURCE_REVIEW.json')
        for name in ('verify_provenance', 'observer_foundations_probe', 'ordinal_succ_report_probe'):
            run(name, [py, 'scripts/'+name+'.py'])
        native_paths = ['observational_succ', 'tests', 'scripts', 'formal', 'provenance', 'docs',
                        'AGENTS.md', 'pyproject.toml', 'requirements.txt', 'requirements-dev.txt']
        run('native_inputs_unchanged', ['git', 'diff', '--exit-code',
             'd32342d375f44ddf62221ad6aff2f534abdc0a03', '--', *native_paths])
        if args.full:
            run('native_suite', [py, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py'])
        run('whitespace', ['git', 'diff', '--check'])
    finally:
        receipt = {'parent': 'a974db527c19708006b9f6d7f0ca01d08d1e0524',
                   'commands': commands, 'comparisons': comparisons,
                   'native_suite': 'executed' if args.full else 'prior pass reused after unchanged-input check',
                   'native_receipt': 'research/2026-11-07/learning_yoneda/validation/native_suite.json',
                   'source_metadata_note': 'stage index script hash refreshed by actual fresh producer; source payloads compared unchanged',
                   'code_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                                   for p in sorted(HERE.rglob('*.py'))},
                   'pi_normality': 'OPEN', 'RH': 'OPEN'}
        (out/'replay.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
