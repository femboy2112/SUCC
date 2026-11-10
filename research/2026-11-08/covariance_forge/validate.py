"""Replay into fresh output, preserving retained receipts and source scope."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = '47ec1ccf9d3579897abb94c047f3b4dc13b4cb70'


def imported_run(path, output):
    return [sys.executable, '-c',
            "import importlib.util,json,sys\n"
            f"sys.path.insert(0,{str(path.parent)!r})\n"
            f"s=importlib.util.spec_from_file_location('forge_replay_unique',{str(path)!r})\n"
            "m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)\n"
            f"open({str(output)!r},'w').write(json.dumps(m.run(),indent=2,sort_keys=True)+'\\n')\n"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--full', action='store_true', help='also repeat the inherited native suite')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONPATH=str(ROOT), OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    commands = []
    for name, folder, pattern in (('instrument', HERE, 'test_instrument.py'),
                                   ('history_certificate', HERE, 'test_history_certificate.py'),
                                   ('arithmetic', HERE/'arithmetic', 'test_*.py'),
                                   ('spectral', HERE/'spectral', 'test_*.py'),
                                   ('crucible', HERE/'crucible', 'test_*.py')):
        commands.append((name, [sys.executable, '-m', 'unittest', 'discover', '-s', str(folder), '-p', pattern, '-v']))
    commands.append(('terminal_receipts', [sys.executable, str(HERE/'arithmetic/run_receipts.py'),
                                           '--output', str(out/'terminal_receipts.json')]))
    for name, path in (('spectral_oracle', HERE/'spectral/oracle.py'),
                        ('hostile_oracle', HERE/'crucible/hostile_exact.py'),
                        ('independent_interval_audit', HERE/'crucible/instrument_audit.py')):
        commands.append((name, imported_run(path, out/(name+'.json'))))
    for stage in ('pilot', 'holdout', 'stress'):
        commands.append((stage, [sys.executable, str(HERE/'run_experiment.py'), '--stage', stage,
                                 '--output', str(out/'measurements')]))
    commands.append(('spectral_measurements', [sys.executable, str(HERE/'run_spectral_probe.py'),
                                              '--output', str(out/'measurements')]))
    commands.append(('history_measurements', [sys.executable, str(HERE/'run_history_probe.py'),
                                             '--output', str(out/'measurements')]))
    compare = (
        "import json;from pathlib import Path\n"
        f"root=Path({str(HERE)!r});out=Path({str(out)!r})\n"
        "def normal(x):\n"
        " if isinstance(x,dict):return {k:normal(v) for k,v in x.items() if k!='seconds'}\n"
        " if isinstance(x,list):return [normal(v) for v in x]\n"
        " return x\n"
        "for p in sorted((root/'receipts').glob('*.json')):\n"
        " if p.stem.startswith('epoch_') or p.stem.startswith('spectral_') and p.stem!='spectral_probe' or p.stem.startswith('history_') and p.stem!='history_probe':\n"
        "  assert normal(json.loads(p.read_text()))==normal(json.loads((out/'measurements'/p.name).read_text())),p\n"
        "  print(p.name,'mathematically identical')\n"
        "for left,right in [('arithmetic/RECEIPTS.json','terminal_receipts.json'),"
        "('spectral/EXACT_RECEIPT.json','spectral_oracle.json'),"
        "('crucible/EXACT_RECEIPTS.json','hostile_oracle.json'),"
        "('crucible/INSTRUMENT_AUDIT.json','independent_interval_audit.json')]:\n"
        " assert json.loads((root/left).read_text())==json.loads((out/right).read_text()),left\n"
        " print(left,'identical JSON payload')\n")
    commands.append(('receipt_reconciliation', [sys.executable, '-c', compare]))
    for script in ('verify_provenance', 'observer_foundations_probe', 'ordinal_succ_report_probe'):
        commands.append((script, [sys.executable, f'scripts/{script}.py']))
    if args.full:
        commands.append(('native_suite', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py']))
    results = []
    for name, command in commands:
        start = time.monotonic()
        with (out/(name+'.log')).open('w') as log:
            try:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
                code = result.returncode
            except OSError as error:
                log.write(str(error)+'\n')
                code = 127
        results.append({'name': name, 'command': command, 'exit_code': code,
                        'seconds': time.monotonic()-start})
        print(name, code, flush=True)
    # The inherited full-suite receipt is relevant only while all its native
    # input paths are byte-identical; retain that provenance instead of silently
    # treating its 12147 tests as new research-namespace tests.
    native_paths = ['observational_succ', 'tests', 'scripts', 'formal', 'provenance',
                    'docs', 'AGENTS.md', 'pyproject.toml', 'requirements.txt', 'requirements-dev.txt']
    check = subprocess.run(['git', 'diff', '--exit-code', PARENT, '--', *native_paths],
                           cwd=ROOT, capture_output=True, text=True)
    if check.returncode:
        (out/'native_scope_diff.log').write_text(check.stdout+check.stderr)
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in HERE.rglob('*.py') if '__pycache__' not in p.parts}
    receipt = {'parent_research': PARENT, 'commands': results, 'code_sha256': hashes,
               'native_inputs_unchanged_from_prior_full_pass': check.returncode == 0,
               'native_suite_rerun': args.full,
               'inherited_native_receipt': 'research/2026-11-07/learning_yoneda/validation/native_suite.json',
               'all_passed': all(r['exit_code'] == 0 for r in results) and check.returncode == 0,
               'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (out/'replay.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    return 0 if receipt['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
