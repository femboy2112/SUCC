#!/usr/bin/env python3
"""Replay the frozen formal audit with a normal official Lean executable.

No host locator shim is needed in GitHub CI.  The archived rejected sources
remain rejection controls, never accepted theorem dependencies.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import tempfile

from cambrian_audit_c_lean import uncomment, axiom_rows

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lean', default='lean')
    args = parser.parse_args()
    frozen = json.loads((ROOT/'research/2026-10-13/CAMBRIAN_AUDIT_C_RAW.json').read_text())
    version = subprocess.check_output([args.lean, '--version'], text=True).strip()
    assert 'version 4.14.0' in version, version
    results = []
    with tempfile.TemporaryDirectory(prefix='cambrian-formal-ci-') as temporary:
        def check(name, source, accepted, required_names=()):
            path = Path(temporary)/name
            path.write_text(source)
            result = subprocess.run([args.lean, str(path)], cwd=ROOT,
                                    capture_output=True, text=True, timeout=60)
            assert (result.returncode == 0) == accepted, (name, result.stdout, result.stderr)
            if not accepted:
                assert result.returncode == 1 and 'error:' in (result.stdout + result.stderr), (
                    name, 'Infrastructure failure is not a calibrated proof rejection',
                    result.returncode, result.stdout, result.stderr)
            rows = axiom_rows(result.stdout)
            if accepted:
                assert set(required_names) <= set(rows), (name, 'missing axiom output')
                assert all(set(a) <= ALLOWED for a in rows.values()), (name, rows)
            results.append({'name':name,'accepted':accepted,'returncode':result.returncode,
                            'checked_theorems':len(required_names),
                            'standard_axioms_only':accepted and all(set(a)<=ALLOWED for a in rows.values())})
        count = 0
        for name, digest in frozen['formal_source_hashes'].items():
            source = (ROOT/name).read_text()
            assert sha256(source.encode()).hexdigest() == digest, name
            code = uncomment(source)
            assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b',code), name
            names = ['ObservationalSUCC.'+n for n in re.findall(r'^\s*theorem\s+([A-Za-z_0-9]+)',code,re.M)]
            count += len(names)
            check(Path(name).name, source+'\n'+'\n'.join('#print axioms '+n for n in names),True,names)
        appendix = (ROOT/'research/2026-10-13/CAMBRIAN_AUDIT_C_CONTROLS.lean').read_text()
        assert sha256(appendix.encode()).hexdigest() == frozen['audit_appendix_sha256']
        names = ['CambrianAudit.'+n for n in re.findall(r'^\s*theorem\s+([A-Za-z_0-9]+)',uncomment(appendix),re.M)]
        check('audit_positive_controls.lean', (ROOT/'formal/EODCS_CambrianRealization.lean').read_text()+'\n'+appendix+'\n'+'\n'.join('#print axioms '+n for n in names),True,names)
        for name, source in frozen['rejection_control_sources'].items():
            check(name,source,False)
    assert count == frozen['theorem_count'] == 65
    print(json.dumps({'status':'FORMAL_KERNEL_AND_REJECTION_CONTROLS_PASS',
                      'compiler':version,'production_theorems':count,'checks':results},indent=2))


if __name__ == '__main__':
    main()
