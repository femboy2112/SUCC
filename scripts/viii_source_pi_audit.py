#!/usr/bin/env python3
"""Reproduce the finite Main VIII source / polygon integration checks."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    from pi_polygon_normality_probe import run_probe
    historical = ROOT/'research/2026-10-20'
    operator_source = historical/'CLOUD_EXACT_MOMENT_SOURCE_J10.json'
    operator_receipt = json.loads(operator_source.read_text())
    implementation_hashes = {
        name: sha(ROOT/name) == digest
        for name, digest in operator_receipt['sha256'].items()
    }
    tests = subprocess.run([
        sys.executable, '-m', 'unittest',
        'tests.test_viii_source_pi_holdouts', 'tests.test_pi_polygon_normality',
        'tests.test_cloud_exact_moment_inverse', 'tests.test_cloud_operator_transport', '-v'
    ], cwd=ROOT, capture_output=True, text=True)
    with tempfile.TemporaryDirectory(prefix='succ-viii-source-') as directory:
        output = Path(directory)/'operator.json'
        operator = subprocess.run([
            sys.executable, 'scripts/main_vii_operator_holdout.py',
            '--target-repo', str(ROOT), '--source-receipt', str(operator_source),
            '--output', str(output)
        ], cwd=ROOT, capture_output=True, text=True)
        symbolic = json.loads(output.read_text()) if output.exists() else None
    regenerated_pi = json.dumps(run_probe(), sort_keys=True, indent=2)+'\n'
    pi_path = historical/'PI_POLYGON_NORMALITY_FINITE_RECEIPT.json'
    source_bytes = (ROOT/'observational_succ/source_weil_hierarchy.py').read_bytes()
    git_blob = hashlib.sha1(b'blob '+str(len(source_bytes)).encode()+b'\0'+source_bytes).hexdigest()
    paths = ['observational_succ/pi_polygon_normality.py',
             'tests/test_viii_source_pi_holdouts.py',
             'research/2026-10-20/PI_POLYGON_NORMALITY_PATH_DEFECT.md',
             'scripts/viii_source_pi_audit.py']
    passed = (tests.returncode == 0 and operator.returncode == 0
              and all(implementation_hashes.values())
              and regenerated_pi == pi_path.read_text()
              and git_blob == '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
    return {
        'status': 'PASSED' if passed else 'FAILED',
        'date': '2026-10-21', 'python': platform.python_version(),
        'pre_receipt_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'scope': '34 focused tests, 60 symbolic shifted-Gram cases, exact source/receipt hashes; no full suite or Lean',
        'source_blob': git_blob, 'source_blob_matches_213': git_blob == '0cc8510b71d178fc79e8d410a86d8b6014cf9178',
        'historical_receipt_sha256': {p.name: sha(p) for p in
             (operator_source, historical/'CLOUD_EXACT_MOMENT_SOURCE_HOLDOUT_J6.json', pi_path)},
        'operator_recorded_implementation_hashes_match': implementation_hashes,
        'new_implementation_sha256': {p: sha(ROOT/p) for p in paths},
        'pi_probe_byte_identical_to_historical_receipt': regenerated_pi == pi_path.read_text(),
        'focused_tests': {'exit_code': tests.returncode, 'stdout': tests.stdout, 'stderr': tests.stderr},
        'operator_holdout_exit_code': operator.returncode,
        'operator_holdout': symbolic,
        'operator_source_probe_regenerated': False,
        'formal_kernel_verified': False,
        'pi_normality_proved': False,
        'source_sign_certified': False,
        'repairs': ['strict exact numeric domains reject floating underflow',
                    'computed polygon width kept distinct from ideal geometric gap'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('status','scope','source_blob','pi_probe_byte_identical_to_historical_receipt')}))
    if result['status'] != 'PASSED':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
