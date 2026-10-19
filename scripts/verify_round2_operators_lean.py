#!/usr/bin/env python3
"""Pinned bounded residue-core audit, exact declaration set, false-proof control."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

from verify_institute_lean import limits, strip_comments


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest_path = root/'research/2026-10-18/round2/operators_axioms.json'
    manifest = json.loads(manifest_path.read_text())
    source = root/manifest['source']
    pin = (root/'lean-toolchain').read_text().strip()
    if pin != manifest['toolchain'] or pin != 'leanprover/lean4:v4.14.0':
        raise ValueError('Unexpected toolchain')
    version = subprocess.check_output(['lean', '--version'], cwd=root, text=True).strip()
    if not version.startswith('Lean (version 4.14.0,'):
        raise ValueError('Compiler does not match pin')
    code = strip_comments(source.read_text())
    for word in ('sorry', 'admit', 'axiom', 'unsafe', 'native_decide'):
        if re.search(r'\b'+word+r'\b', code):
            raise ValueError('Forbidden proof token: '+word)
    if re.search(r'^\s*import\s', code, re.M):
        raise ValueError('Core-only lane does not allow imports')
    with tempfile.TemporaryDirectory(prefix='succ-residue-lean-') as tmp:
        tmp = Path(tmp)
        false = tmp/'Negative.lean'
        false.write_text('theorem falseControl : False := by decide\n')
        bad = subprocess.run(['lean', str(false)], cwd=root, text=True, capture_output=True,
                             timeout=65, preexec_fn=limits)
        if bad.returncode != 1 or "tactic 'decide' proved that the proposition" not in bad.stdout:
            raise ValueError('False-proof control was not rejected as expected')
        checked = subprocess.run(['lean', '-o', str(tmp/'ResidueTransfer.olean'), str(source)],
                                 cwd=root, text=True, capture_output=True, timeout=65, preexec_fn=limits)
        if checked.returncode or checked.stderr:
            raise RuntimeError(checked.stdout+checked.stderr)
        declarations = {}
        for line in checked.stdout.splitlines():
            empty = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
            nonempty = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]", line)
            match = empty or nonempty
            if match is None or match.group(1) in declarations:
                raise ValueError('Unexpected compiler output: '+line)
            declarations[match.group(1)] = [] if empty else [x.strip() for x in match.group(2).split(',')]
        if declarations != manifest['declarations']:
            raise ValueError('Exact axiom audit mismatch')
        record = dict(status='PASS', scope=manifest['scope'], toolchain=pin, compiler_version=version,
                      source=manifest['source'], source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                      manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                      declarations=declarations, compiler_output=checked.stdout,
                      negative_control_exit_code=bad.returncode, negative_control_output=bad.stdout,
                      checked_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                      resource_limits=dict(address_space_bytes=1024**3, cpu_seconds=60))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
