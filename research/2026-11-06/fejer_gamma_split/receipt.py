"""Generate and verify deterministic, limited-scope research receipts."""
import hashlib
import json
import sys
from pathlib import Path

BASE=Path(__file__).parent
FILES=[
 'README.md','THEOREMS.md','CLAIM_LEDGER.md','NEXT.md','VALIDATION.md',
 'series_split.py','test_series_split.py','independent_oracle.py','finite_probe.py',
 'LOCAL_TEST_STDOUT.txt','LOCAL_TEST_STDERR.txt','INITIAL_TEST_FAILURE.txt',
 'FINITE_DIAGNOSTICS.json','INDEPENDENT_EXACT_LOG.json',
]
OUT=BASE/'FINITE_RECEIPT.json'

def digest(name):
    contents=(BASE/name).read_bytes()
    return {'sha256':hashlib.sha256(contents).hexdigest(),
            'git_blob_sha1':hashlib.sha1(f'blob {len(contents)}\0'.encode()+contents).hexdigest(),
            'bytes':len(contents)}

def build():
    return {
       'date':'2026-11-06',
       'repo':'femboy2112/SUCC',
       'parent_commit':'ff99fa2861b370d1aac0a76f01e2d8505c5a8740',
       'prereg_commit':'45db50a7dae5ef708acbdbda4bb63f0f2a5dc3e7',
       'claims':{'FG-01':'PROVED LOCAL','FG-02':'PROVED LOCAL / REFUTED CUT-OFF SHORTCUT',
                 'FG-03':'PROVED LOCAL','FG-04':'PROVED LOCAL','FG-05':'PROVED LOCAL',
                 'FG-06':'PROVED LOCAL / OBSERVED-FINITE','FG-07':'PROVED LOCAL',
                 'source_selected_real_weyl':'OPEN','pi_base16_normality':'OPEN','RH':'OPEN'},
       'local_commands':[
          'python -m unittest discover -v -s . -p test_*.py',
          'python independent_oracle.py',
          'python finite_probe.py',
          'python -m compileall -q .',
       ],
       'local_focused_tests':'21/21 PASS',
       'independent_gaussian_fraction_checks':'47/47 exact checks PASS',
       'prereg_original_cases':[[4,5,1],[8,6,1],[16,5,2]],
       'files':{name:digest(name) for name in FILES},
    }

def run():
    data=build()
    if '--verify' in sys.argv:
        assert OUT.exists(), 'receipt file missing'
        expected=json.loads(OUT.read_text())
        assert data==expected, 'receipt mismatch'
        print('SOURCE_LOCAL_RECEIPT_VERIFIED')
        return
    OUT.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print('SOURCE_LOCAL_RECEIPT_WRITTEN')

if __name__=='__main__':run()
