"""Reproduce 16x16 real π spectral/carry matrix, source-digits and γ controls.

Run from any directory; requires the exact native PR #566 source module and
this branch's additive `bbp_spectral_gamma` module. Default checks published
exact finite data; --recompute executes 131072 original BBP steps twice.
No π normality or independent stochastic/Markov law is inferred.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from observational_succ.bbp_spectral_gamma import (
    transition_counts,margins,energies,opposite_frequency_energy,
    difference_counts,dobrushin_coefficient,nilpotent_nonhaar_matrix,haar_matrix,matmul)

HERE=Path(__file__).resolve().parent
EXPECTED_FULL='4e349f3af293f07c42135caabffe0ce262c7ff282847d71e158f05551cd89a73'
EXPECTED_HALF='e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53'
EXPECTED_NEW='344972a0bd1028032907c0e2c9495ad7943265bde1fdd98d4be1c7de38520d03'


def _sha(text: str):return hashlib.sha256((text+'\n').encode('ascii')).hexdigest()


def run(*,recompute: bool = False) -> dict:
    digits=(HERE/'CERTIFIED_HEX_131072.txt').read_text().strip()
    assert len(digits)==131072 and _sha(digits)==EXPECTED_FULL
    assert _sha(digits[:65536])==EXPECTED_HALF
    assert _sha(digits[65536:])==EXPECTED_NEW
    if recompute:
        from observational_succ.bbp_spatial_haar_lift import bulk_pi_hex_digits
        assert bulk_pi_hex_digits(131072,24)==digits
        assert bulk_pi_hex_digits(131072,32)==digits
    receipt=json.loads((HERE/'FINITE_SPECTRAL_HOLDOUT.json').read_text())
    out={}
    for name,s in [('previous',digits[:65536]),('holdout',digits[65536:]),('total',digits)]:
        C=transition_counts(s)
        target=receipt[name]
        assert C==tuple(map(tuple,target['count']))
        e1r,e1c,e2,em=energies(C)
        anti=opposite_frequency_energy(C)
        delta=dobrushin_coefficient(C)
        assert difference_counts(C)==tuple(target['diff_counts'])
        assert abs(float(anti)-target['anti'])<1e-12
        assert abs(float(em)-target['Em'])<1e-12
        assert abs(float(e2)-target['E2'])<1e-12
        out[name]={'pairs':sum(map(sum,C)),'E2_exact':str(e2),
                   'mixed225_exact':str(em),'opposite15_exact':str(anti),
                   'dobrushin_exact':str(delta),
                   'min_count':min(map(min,C)),'max_count':max(map(max,C))}
    assert out['previous']['dobrushin_exact']=='497311/8555180'
    assert out['holdout']['dobrushin_exact']=='123803/2292261'
    assert out['total']['dobrushin_exact']=='481818/13186475'
    P=nilpotent_nonhaar_matrix();H=haar_matrix()
    assert matmul(P,P)==H and P!=H
    assert receipt['preregistered_replication']['satisfied'] is False
    return {'digits_source':'original zero BBP four signed poles',
            'full_sha256':EXPECTED_FULL,'prev_sha256':EXPECTED_HALF,
            'fresh_sha256':EXPECTED_NEW,'certified_by_recomputation':recompute,
            'preregistered_inverse_mode_replication':'FAILED (not replicated)',
            'blocks':out,'pi_base16_normality':'OPEN'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recompute',action='store_true',help='two full source guard runs (~45s)')
    args=parser.parse_args()
    print(json.dumps(run(recompute=args.recompute),indent=2,sort_keys=True))
