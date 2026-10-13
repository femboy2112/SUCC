#!/usr/bin/env python3
"""Replay frozen campaign mathematics; keep runtime metadata visibly separate.

All mathematical fields and source hashes compare exactly.  Only declared
runtime Python versions and the arithmetic invocation's current HEAD are
excluded from mathematical equality; original receipts remain untouched.
"""
import json
from hashlib import sha256
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/2026-10-13'


def replay(script, frozen, runtime_fields=()):
    command = [sys.executable, str(ROOT / 'scripts' / script)]
    result = subprocess.run(command, cwd=ROOT, check=True,
                            text=True, capture_output=True)
    actual = json.loads(result.stdout)
    expected = json.loads((RESEARCH / frozen).read_text())
    runtime = {}
    for field in runtime_fields:
        runtime[field] = {'recorded': expected.pop(field),
                          'current': actual.pop(field)}
    if actual != expected:
        raise AssertionError('Mathematical receipt drift: ' + frozen)
    return {'script': script, 'receipt': frozen, 'runtime_fields': runtime,
            'mathematics_and_hashes_match': True}


def main():
    stored_hash_checks = []
    for filename, field in (('CAMBRIAN_A_VALIDATION.json','sha256'),
                            ('CAMBRIAN_C_ASSIGNMENTS.json','artifact_hashes_sha256')):
        contract = json.loads((RESEARCH/filename).read_text())[field]
        for path, expected in contract.items():
            assert sha256((ROOT/path).read_bytes()).hexdigest() == expected, path
        stored_hash_checks.append({'receipt':filename,'matched_artifacts':len(contract)})
    checked = [
        replay('cambrian_stochastic_probe.py', 'CAMBRIAN_STOCHASTIC_RECEIPT.json'),
        replay('cambrian_a_foundations_probe.py', 'CAMBRIAN_A_RECEIPT.json', ('python',)),
        replay('cambrian_c_geometry_probe.py', 'CAMBRIAN_C_RECEIPT.json'),
        replay('cambrian_d_probe.py', 'CAMBRIAN_D_RESULTS.json', ('python',)),
        replay('cambrian_e_arithmetic_probe.py', 'CAMBRIAN_E_ARITHMETIC_RECEIPT.json',
               ('python','execution_head_sha')),
    ]
    for script in ('cambrian_b_chaos_probe.py', 'cambrian_f_probe.py'):
        result = subprocess.run([sys.executable,str(ROOT/'scripts'/script),'--check'],
                                cwd=ROOT, check=True, text=True, capture_output=True)
        checked.append({'script':script,'internal_frozen_replay':'pass',
                        'stdout':result.stdout.strip()})
    # Re-execute independent audit implementations without rewriting archives.
    for letter in ('A', 'B', 'F'):
        script = {'A':'cambrian_audit_a_probe.py',
                  'B':'cambrian_audit_b_probe.py',
                  'F':'cambrian_audit_f.py'}[letter]
        if letter == 'F':
            # This older script's CLI saves its output. Invoke its pure report
            # entry instead, preserving the originally frozen receipt.
            command = [sys.executable, '-c',
                       "import json,runpy; m=runpy.run_path('scripts/cambrian_audit_f.py'); print(json.dumps(m['report']()))"]
        else:
            command = [sys.executable, str(ROOT/'scripts'/script)]
        result = subprocess.run(command, cwd=ROOT, check=True,
                                text=True, capture_output=True)
        actual = json.loads(result.stdout)
        suffix = 'RESULT' if letter == 'F' else 'RECEIPT'
        expected = json.loads((RESEARCH/f'CAMBRIAN_AUDIT_{letter}_{suffix}.json').read_text())
        runtime = {'python': {'recorded': expected.pop('python'),
                              'current': actual.pop('python')}}
        if letter == 'A':
            # Same source bytes, relocated from isolated to integrated checkout.
            for payload in (actual, expected):
                names = [Path(k).name for k in payload['source_sha256']]
                assert len(names) == len(set(names)), 'Ambiguous source-hash path normalization'
                payload['source_sha256'] = {Path(k).name:v for k,v in
                                            payload['source_sha256'].items()}
            runtime['source_path_normalization'] = 'file basename; every content hash compared'
        if letter == 'B':
            for key in ('F_checkout_observed','root_observed'):
                runtime[key] = {'recorded': expected['source_heads'].pop(key),
                                'current': actual['source_heads'].pop(key)}
        if letter == 'F':
            # Preserve the original audit, while binding the separately reviewed
            # paper correction to BOTH its original and corrected exact bytes.
            corrections = json.loads((RESEARCH/'CAMBRIAN_REVIEWED_CORRECTIONS.json').read_text())['corrections']
            for correction in corrections:
                path = correction['path']
                assert correction['auditor'] == 'F'
                assert expected['source_hashes'][path] == correction['original_sha256']
                assert actual['source_hashes'][path] == correction['corrected_sha256']
                expected['source_hashes'][path] = correction['corrected_sha256']
            runtime['reviewed_paper_corrections'] = corrections
        assert actual == expected, f'Independent audit {letter} receipt drift'
        checked.append({'audit':letter,'mathematics_and_hashes_match':True,
                        'runtime_fields':runtime})
    result = subprocess.run([sys.executable,str(ROOT/'scripts/cambrian_audit_g_holdouts.py'),'--check'],
                            cwd=ROOT,check=True,text=True,capture_output=True)
    checked.append({'audit':'G','internal_frozen_replay':'pass',
                    'stdout':result.stdout.strip()})
    # Every assignment is an actual investigation; none is an invented agent.
    manifest = json.loads((RESEARCH/'CAMBRIAN_SWARM_MANIFEST.json').read_text())
    ids = [a['id'] for a in manifest['explorations']]
    assert sorted(ids) == list(range(1,37)) and len(set(ids)) == 36
    assert all(a['execution_status']=='executed' for a in manifest['explorations'])
    assert sorted(a['id'] for a in manifest['audits']) == list('ABCDEFGH')
    assert all(a['execution_status']=='executed' for a in manifest['audits'])
    for a in manifest['explorations'] + manifest['audits']:
        assert (ROOT/a['dossier']).is_file(), a['dossier']
    print(json.dumps({'status':'EXACT_CAMBRIAN_MATHEMATICS_REPLAY',
                      'research_assignments':len(ids),'audit_assignments':8,
                      'additional_stored_hash_checks':stored_hash_checks,
                      'checks':checked},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
