"""Deterministic claim-labeled local SHA256 provenance receipt, no status promotion."""
import argparse
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FILES=['PREREGISTRATION.md','README.md','THEOREMS.md','CLAIM_LEDGER.md','NEXT.md',
       'VALIDATION.md','bridge.py','test_bridge.py','independent_oracle.py',
       'run_probes.py','symbolic_audit.py','wrong_seam_probe.py',
       'INITIAL_FAILED_TEST_LOG.txt','WRONG_SEAM_NEGATIVE_CONTROL.json',
       'SYMPY_AUDIT_LOG.txt','LOCAL_TEST_STDOUT.txt','LOCAL_TEST_STDERR.txt',
       'INDEPENDENT_ORACLE_RAW.json','FINITE_RESULTS.json']

def receipt():
    return {'experiment':'original-BBP-2adic-odometer-to-real-return-carry-seam',
            'parent_sha':'c550cd4089db0367464ff38884797e06359fbcbc',
            'preregistration_commit':'c0a3bda86236486421a6ffd0502ee366f851e8f5',
            'checksums_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in FILES},
            'claims':{'source_return_clone':'PROVED LOCAL',
                      'source_one_bit_return_flip':'PROVED LOCAL',
                      'two_place_carry_exact_reconstruction':'PROVED LOCAL',
                      'real_phase_return_expansivity':'PROVED LOCAL',
                      'finite_source_witnesses':'OBSERVED-FINITE',
                      'measurable_haartohaar_factor':'REFUTED',
                      'return_fiber_signed_decay':'OPEN',
                      'pi_normality':'OPEN'},
            'root_native_suite':'NOT RUN','kernel':'NOT RUN','hosted_ci':'NOT RUN'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true')
    args=parser.parse_args();d=receipt();p=ROOT/'FINITE_RECEIPT.json'
    if args.verify:
        assert json.loads(p.read_text())==d,'receipt mismatch'
        print('FINITE_RECEIPT SHA256_REPLAY_PASS')
    else:
        print(json.dumps(d,indent=2,sort_keys=True))
