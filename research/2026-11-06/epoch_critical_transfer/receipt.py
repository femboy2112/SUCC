"""Deterministic research-local SHA256 receipt for isolated SUCC epoch Fejer tests."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

FILES = (
    'README.md','THEOREMS.md','CLAIM_LEDGER.md','VALIDATION.md','NEXT.md',
    'epoch_fejer.py','all_radius.py','test_epoch_fejer.py','independent_oracle.py',
    'LOCAL_TEST_LOG.txt','INITIAL_RED_TEST_LOG.txt','INDEPENDENT_ORACLE_LOG.txt',
    'FINITE_RESULTS.json','ALL_RADIUS_HOLDOUT.json','NEW_EPOCH_FOURIER_DIAGNOSTICS.json',
)

def make(root=Path('.')):
    return {
        'parent_pr': 536,
        'parent_exact_head': 'e463a191d82355c707662bdbfb4bf2150fdd4eb7',
        'preregistration_commits': {
            'first': 'fd4f118a8a44cce1d15e9c42b14e57876cfc2844',
            'all_radius': 'c0c36518ea83a003c0892b312fb3536202e3f1f6',
        },
        'tests_focused': '14/14 PASS',
        'independent_oracle': '15 exact checks PASS; same source genealogy',
        'holdouts': { 'A191': 'CERTIFIED FINITE K3', 'A319': 'CERTIFIED FINITE K3'},
        'infinite_selected_K3': 'OPEN',
        'pi_base16_normality': 'OPEN',
        'files_sha256': {n: hashlib.sha256((root/n).read_bytes()).hexdigest() for n in FILES},
    }

if __name__=='__main__':
    import sys
    content=json.dumps(make(),indent=2,sort_keys=True)+'\n'
    dest=Path('RECEIPT.json')
    if '--verify' in sys.argv:
        assert dest.read_text()==content, 'receipt mismatch'
        print('RECEIPT VERIFIED: 15 SHA256 file dependencies match')
    else:
        dest.write_text(content)
        print('RECEIPT GENERATED')
