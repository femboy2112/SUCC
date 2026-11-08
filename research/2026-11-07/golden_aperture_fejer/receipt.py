"""Deterministic finite source receipt for immutable research file snapshots."""
import sys,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FILES=[
 'golden_aperture.py','test_golden.py','finite_probe.py','large_probe.py',
 'fiber_probe.py','independent_oracle.py','independent_check.py',
 'FINITE_RESULTS.json','LARGE_RESULTS.json','FIBER_PROBE.json',
 'INDEPENDENT_CHECK.json','INDEPENDENT_ORACLE_LOG.json',
 'TEST_STDOUT.txt','TEST_STDERR.txt','INITIAL_TEST_LOG.txt',
 'FINISHED_PROBE_LOG.txt','LARGE_PROBE_LOG.txt','LARGE_PROBE_REPLAY_LOG.txt',
 'FIBER_PROBE_LOG.txt','LARGE_TIMEOUT_NOTE.md',
 'THEOREMS.md','CLAIM_LEDGER.md','README.md','VALIDATION.md','NEXT.md'
]

def content():
    return {'claims':{'GA-01':'PROVED LOCAL','GA-02':'PROVED LOCAL','GA-03':'PROVED-CONDITIONAL',
                      'GA-04':'PROVED LOCAL','GA-05':'PROVED LOCAL','GA-06':'PROVED LOCAL',
                      'GA-07':'PROVED-CONDITIONAL','GA-08':'CERTIFIED-FINITE','GA-09':'PROVED LOCAL','GA-NORMALITY':'OPEN'},
            'pi_normality':'OPEN', 'RH':'OPEN',
            'preregs':{'small':'44a099cc5b9903039e1b305ce989bdf4370839bc',
                       'large':'31ab4a1d123ca48c394cf88b6a4ea74cbe6b7489'},
            'files_sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in FILES}}

def main():
    out=ROOT/'FINITE_RECEIPT.json'; obj=content()
    if '--verify' in sys.argv:
        expected=json.loads(out.read_text())
        assert obj==expected, 'receipt source hash or status changed'
        print('FINITE_RECEIPT_VERIFIED',len(FILES))
    else:
        out.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
        print('FINITE_RECEIPT_WRITTEN',len(FILES))
if __name__=='__main__':main()
