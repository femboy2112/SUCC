#!/usr/bin/env python3
"""Fresh pinned kernel check, exact axiom audit, and false-proof control."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import resource
import subprocess
import tempfile


def strip_comments(text):
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError('Unclosed Lean comment')
    return ''.join(out)


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root/'formal/InstituteCausal.lean'
    manifest = json.loads((root/'research/2026-10-18/institute/axioms.json').read_text())
    pin = (root/'lean-toolchain').read_text().strip()
    if pin != manifest['toolchain'] or pin != 'leanprover/lean4:v4.14.0':
        raise ValueError('Unexpected toolchain')
    version = subprocess.check_output(['lean','--version'],cwd=root,text=True).strip()
    if not version.startswith('Lean (version 4.14.0,'):
        raise ValueError('Compiler does not match pin')
    code = strip_comments(source.read_text())
    for word in ('sorry', 'admit', 'axiom', 'unsafe', 'native_decide'):
        if re.search(r'\b'+word+r'\b', code):
            raise ValueError('Forbidden proof token: '+word)
    if re.search(r'^\s*import\s', code, re.M):
        raise ValueError('Core-only lane does not allow imports')
    with tempfile.TemporaryDirectory(prefix='succ-institute-lean-') as tmp:
        tmp = Path(tmp)
        false = tmp/'Negative.lean'
        false.write_text('theorem falseControl : False := by decide\n')
        bad = subprocess.run(['lean',str(false)],cwd=root,text=True,capture_output=True,
                             timeout=65,preexec_fn=limits)
        if bad.returncode != 1 or "tactic 'decide' proved that the proposition" not in bad.stdout:
            raise ValueError('False-proof control was not rejected for the expected reason')
        command = ['lean','-o',str(tmp/'InstituteCausal.olean'),str(source)]
        checked = subprocess.run(command,cwd=root,text=True,capture_output=True,
                                 timeout=65,preexec_fn=limits)
        if checked.returncode:
            raise RuntimeError(checked.stdout+checked.stderr)
        declarations = {}
        for line in checked.stdout.splitlines():
            empty = re.fullmatch(r"'([^']+)' does not depend on any axioms",line)
            nonempty = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]",line)
            match = empty or nonempty
            if match is None or match.group(1) in declarations:
                raise ValueError('Unexpected compiler output: '+line)
            declarations[match.group(1)] = [] if empty else [x.strip() for x in match.group(2).split(',')]
        if declarations != manifest['declarations'] or checked.stderr:
            raise ValueError('Exact axiom audit mismatch or compiler stderr')
        record = dict(toolchain=pin, compiler_version=version, source=str(source.relative_to(root)),
                      source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                      exit_code=checked.returncode, negative_control_exit_code=bad.returncode,
                      negative_control_output=bad.stdout, declarations=declarations,
                      compiler_output=checked.stdout,
                      checked_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                      resource_limits=dict(address_space_bytes=1024**3,cpu_seconds=60),
                      command=['lean','-o','TEMP/InstituteCausal.olean',str(source.relative_to(root))])
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__ == '__main__':
    main()
