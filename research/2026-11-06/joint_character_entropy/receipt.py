"""Deterministic local-research file-hash receipt (not an external kernel)."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

FILES=(
    'README.md','THEOREMS.md','PREREGISTRATION.md','PREREG_ADDENDUM.md','CLAIM_LEDGER.md','NEXT.md','VALIDATION.md',
    'joint_entropy.py','independent_oracle.py','signed_certificate.py','entropy_to_character.py',
    'holdout_probe.py','fresh_holdout_probe.py','test_joint_entropy.py','test_signed_certificate.py',
    'test_entropy_to_character.py','test_fresh_holdout.py','LOCAL_TEST_STDERR.txt',
    'INDEPENDENT_ORACLE_RAW.json','HOLDOUT_RAW.json','FRESH_HOLDOUT_RAW.json',
)

def render():
    root=Path(__file__).resolve().parent
    files={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in FILES}
    h=json.loads((root/'HOLDOUT_RAW.json').read_text())
    independent=json.loads((root/'INDEPENDENT_ORACLE_RAW.json').read_text())
    assert h['preregistration_sha256']==files['PREREGISTRATION.md']
    assert h['preregistration_sha256']=='efcefe2c71f3d9898b7dd6f6b45f3cc7ed287cbef651bae66793fd43ae10cc32'
    fresh=json.loads((root/'FRESH_HOLDOUT_RAW.json').read_text())
    assert fresh['prereg_sha256']==files['PREREG_ADDENDUM.md']
    assert fresh['prereg_commit']=='6659899812abee3ae6625907212c8d991dfbf6ee'
    assert h['independent_machin_bbp_matching_digits']==independent['machin_vs_bbp_certified_hex_digits']==128
    assert independent['independent_high_n_phase_overlap_checks']==7
    return {'source':'four authentic signed BBP poles, original U0=0',
            'parent':'f45e4459f2efa6a94bfa5adcf8184c57aa028c55',
            'github_prereg_commit':'d7b5b7b330394992eb43fe533f10962b9c0e9544',
            'all_new_claims_formalized_in_lean':False,
            'native_SUCC_full_suite_executed':False,
            'pi_normality':'OPEN','selected_signed_Weyl_limit':'OPEN','RH':'OPEN',
            'local_focused_tests':29,
            'fresh_commit_first_h3_bounds':fresh['fresh_epochs_h_3'],
            'earlier_signed_epochs_are_preseen':True,
            'prereg_addendum_sha256':fresh['prereg_sha256'],
            'original_pole_independent_checks':h['original_pole_checks'],
            'certified_selected_pi_hex_digits':h['certified_1536_digits'],
            'independent_machin_digits':h['independent_machin_bbp_matching_digits'],
            'independent_late_phase_oracle_checks':independent['independent_high_n_phase_overlap_checks'],
            'finite_selected_signed_bounds':h['selected_epoch_rigorous_signed_weyl_bounds'],
            'file_sha256':files,
            'claim_statuses':{'JC02':'PROVED LOCAL','JC03':'CLASSICAL','JC04':'PROVED LOCAL',
                              'JC05':'PROVED LOCAL','JC07':'PROVED LOCAL (conditional)',
                              'JC09':'OBSERVED-FINITE / certified rational bounds',
                              'JC10':'UNVERIFIED / OPEN'},
            'prereg_sha256':h['preregistration_sha256']}

if __name__=='__main__':
    import sys
    payload=render()
    data=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    if len(sys.argv)>1 and sys.argv[1]=='--verify':
        expected=Path(__file__).with_name('FINITE_RECEIPT.json').read_text()
        assert expected==data,'receipt mismatch; input files changed'
        print('FINITE_RECEIPT_REPLAY_PASS')
    else:
        sys.stdout.write(data)
