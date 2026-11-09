"""Reproduce source Gamma and 16x16 diagnostics from prior certified π digits.

Run from repo root: python research/2026-11-09/bbp_gamma_matrix_deformation/receipt.py
Never assumes new/fresh digits or normality.
"""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from observational_succ.bbp_gamma_matrix_deformation import (
    bbp_gamma_digamma, bbp_gamma_closed, matched_leading_mutation_shift,
    source_gamma_coefficient, q_euler_constant, transition_counts,
    row_normalized, matrix_source_gamma,
)

SOURCE_SHA='4e349f3af293f07c42135caabffe0ce262c7ff282847d71e158f05551cd89a73'
FILENAME=ROOT/'research/2026-11-09/pi_16x16_gamma_spectrum/CERTIFIED_HEX_131072.txt'


def calculate():
    import numpy as np
    raw=FILENAME.read_bytes()
    if sha256(raw).hexdigest()!=SOURCE_SHA:raise AssertionError('certified source bytes changed')
    digits=raw.decode('ascii').strip()
    if len(digits)!=131072:raise AssertionError('wrong source length')
    vals={}
    for name,s in [('old_65536',digits[:65536]),('holdout_65536_PRESEEN',digits[65536:]),('complete_131072',digits)]:
        counts=transition_counts(s)
        P=row_normalized(counts)
        H=np.ones((16,16))/16
        X=np.asarray(P)-H
        M,bound=matrix_source_gamma(P,terms=24,dps=70)
        vals[name]={
            'actual_pair_count':len(s)-1,
            'centered_norm2':round(float(np.linalg.norm(X,2)),12),
            'gamma_deformed_norm2':round(float(np.linalg.norm(M-float(bbp_gamma_closed())*np.eye(16),2)),12),
            'mathematical_tail_bound':float(bound),
            'status':'REUSED SOURCE-CERTIFIED FINITE DIAGNOSTIC, NOT NEW HOLDOUT'
        }
    import mpmath as mp
    with mp.workdps(70):
        strings={
            'gamma_bbp':mp.nstr(bbp_gamma_digamma(70),65),
            'gamma_bbp_closed':mp.nstr(bbp_gamma_closed(70),65),
            'c1':mp.nstr(source_gamma_coefficient(1,70),65),
            'gamma_q_1_16':mp.nstr(q_euler_constant(Fraction(1,16),70),65),
            'matched_leading_mutation_delta':mp.nstr(matched_leading_mutation_shift(70),65),
        }
    return {
        'source':'AUTHENTIC four signed BBP poles and literal U0=0',
        'source_digits_sha256_with_newline':SOURCE_SHA,
        **strings,
        'blocks':vals,
        'pi_normality':'OPEN',
        'claim_status':'SCALAR SOURCE IDENTITY EXACT; MATRIX NUMERICS NON-CERTIFYING'
    }

if __name__=='__main__':
    doc=calculate()
    path=Path(__file__).with_name('FINITE_RECEIPT.json')
    payload=json.dumps(doc,sort_keys=True,indent=2)+'\n'
    if '--verify' in sys.argv:
        if path.read_text()!=payload:raise AssertionError('receipt drift')
        print('FINITE_RECEIPT.json: verified, no changes')
    elif '--write' in sys.argv:
        path.write_text(payload)
        print('FINITE_RECEIPT.json: written')
    else:
        print(payload)
