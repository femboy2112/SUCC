#!/usr/bin/env python3
"""Recompute archived Main XXIV exact receipts without overwriting them.

Only runtime Python/head metadata is ignored in #591. All mathematical fields,
source hashes and integer/rational certificate data must match. This is finite
certificate replay, not a proof of normality or RH. Outputs stay outside Git.
"""
from __future__ import annotations

from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import argparse


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/2026-11-10'
sys.path.insert(0, str(ROOT))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def equal(actual, expected, label: str):
    if actual != expected:
        raise AssertionError(label + ': regenerated exact certificate differs from archive')


def normalized(value, encoder=None):
    return json.loads(json.dumps(value, default=encoder))


def replay_lambda(out: Path) -> dict:
    archived = RESEARCH / 'zero_anchored_lambda_haar/receipts/FINITE_REPORT.json'
    saved = json.loads(archived.read_text())
    module = load_module('_main_xxiv_lambda_receipt', ROOT / 'scripts/zero_anchored_lambda_haar_probe.py')
    protocol = saved['protocol']
    actual = normalized(module.run_probe(tuple(protocol['lengths']), protocol['phase_depth'],
                                         protocol['guard']), module.exact_json)
    (out / 'lambda_haar_finite_report.json').write_text(json.dumps(actual, indent=2, sort_keys=True) + '\n')
    expected = dict(saved)
    for key in ('python', 'local_head_at_run'):
        actual.pop(key)
        expected.pop(key)
    equal(actual, expected, '#591 full finite protocol including code hashes')
    return {'pr': 591, 'archived': str(archived.relative_to(ROOT)), 'sha256': sha(archived),
            'blocks': protocol['lengths'], 'ignored_metadata_only': ['python', 'local_head_at_run']}


def replay_joinings(out: Path) -> dict:
    folder = RESEARCH / 'basel_crt_omega_phasebridge/ratio_fiber_joinings'
    archived = folder / 'FINITE_CERTIFICATE.json'
    saved = json.loads(archived.read_text())
    module = load_module('_main_xxiv_joining_receipt', folder / 'certified_fiber.py')
    equal(saved['base_pr'], 588, '#593 base PR')
    equal(saved['outward_scale'], 10**12, '#593 outward integer scale')
    equal(saved['source_only'], True, '#593 source-only contract')
    epochs = []
    for expected in saved['epochs']:
        mean = module.certified_mean(expected['A'], expected['h'])
        digits = module.source_digit_correlations(expected['A'])
        merged = dict(mean, **{k: v for k, v in digits.items() if k != 'A'})
        actual = {key: merged[key] for key in expected}
        # Exclude every floating diagnostic returned by certified_mean.
        for key, value in actual.items():
            if type(value) is not int and not (type(value) is list and all(type(x) is int for x in value)):
                raise AssertionError('#593 noninteger certificate field: ' + key)
        equal(actual, expected, '#593 epoch ' + str(expected['A']))
        epochs.append(actual)
    (out / 'joining_integer_replay.json').write_text(json.dumps(epochs, indent=2, sort_keys=True) + '\n')
    return {'pr': 593, 'archived': str(archived.relative_to(ROOT)), 'sha256': sha(archived),
            'epochs': [r['A'] for r in epochs], 'authority': 'integer outward ticks and exact digit counts'}


def replay_shields(out: Path) -> dict:
    folder = RESEARCH / 'circle_line_lr_observer/height_shield'
    archived = folder / 'height_shield_receipt.json'
    saved = json.loads(archived.read_text())
    module = load_module('_main_xxiv_height_receipt', folder / 'farey_height_shield.py')
    actual_rows = []
    equal(len(saved['certificates']), 7, '#596 recorded certificate count')
    for expected in saved['certificates']:
        cert = module.certify_height(expected['height'], expected['source'])
        actual = module.certificate_summary(cert)
        actual.update(final_source_lo=str(cert.final_source_lo), final_source_hi=str(cert.final_source_hi),
                      replay_verified=module.verify_height_certificate(cert),
                      runs=[asdict(run) for run in cert.runs])
        actual = normalized(actual, str)
        equal(actual, expected, '#596 ' + expected['source'] + ' H=' + str(expected['height']))
        actual_rows.append(actual)
    (out / 'height_shield_replay.json').write_text(json.dumps(actual_rows, indent=2, sort_keys=True) + '\n')
    return {'pr': 596, 'archived': str(archived.relative_to(ROOT)), 'sha256': sha(archived),
            'certificates': len(actual_rows), 'authority': 'complete rational source/run/Farey summaries'}


def replay_zero_anchor(out: Path) -> dict:
    folder = RESEARCH / 'circle_line_lr_observer/zero_anchor_identity'
    archived = folder / 'finite_receipt.json'
    with tempfile.TemporaryDirectory(prefix='succ-xxiv-zero-replay-') as scratch:
        temp = Path(scratch)
        for name in ('build_receipt.py', 'zero_anchor.py'):
            shutil.copyfile(folder / name, temp / name)
        proc = subprocess.run([sys.executable, '-W', 'error', str(temp / 'build_receipt.py')],
                              cwd=temp, capture_output=True, text=True)
        (out / 'zero_anchor_builder.log').write_text(proc.stdout + proc.stderr)
        if proc.returncode:
            raise AssertionError('#597 temporary receipt builder failed; see zero_anchor_builder.log')
        regenerated = temp / 'finite_receipt.json'
        equal(regenerated.read_bytes(), archived.read_bytes(), '#597 byte-exact isolated rebuild')
        shutil.copyfile(regenerated, out / 'zero_anchor_finite_receipt.json')
    return {'pr': 597, 'archived': str(archived.relative_to(ROOT)), 'sha256': sha(archived),
            'authority': 'byte-exact rebuild in disposable directory'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    if out == ROOT or ROOT in out.parents:
        parser.error('write replay outputs outside the checkout')
    out.mkdir(parents=True, exist_ok=True)
    receipt = {'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
               'authority': 'finite exact certificate replay; no universal proof promotion', 'results': []}
    try:
        for operation in (replay_lambda, replay_joinings, replay_shields, replay_zero_anchor):
            result = operation(out)
            receipt['results'].append(result)
            print('PASS', result['pr'], flush=True)
    except Exception as exc:
        receipt.update(status='FAIL', error=f'{type(exc).__name__}: {exc}')
        (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        raise
    receipt['status'] = 'PASS'
    (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
