"""Independent finite calibration for the paper conductor-growth review.

Uses no arithmetic/transfer implementation. Positivity is proved for all
packets in INDEPENDENT_REVIEW.md; these finite checks are regression evidence.
Ordinary floating logarithms below are diagnostics only.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import log
from pathlib import Path
import json


def main():
    coefficients=(4,-2,-1,-1)
    offsets=(1,4,5,6)
    value=F()
    diagnostics=[]
    for n in range(1,1026):
        forcing=sum((F(c,8*n-8+d) for c,d in zip(coefficients,offsets)),F())
        previous=value
        value=(16*value+forcing)%1
        if n-1 in (64,128,256,512,1024):
            diagnostics.append({'n':n-1,
                'log_den_U_over_n':log(previous.denominator)/(n-1),
                'log_den_delta_over_n':log((value-previous).denominator)/(n-1)})
    checks=[]
    for residue,off,weights in (
        (1,(1,4,5,6),(4,-2,-1,-1)),
        (5,(1,4,5,6),(4,-2,-1,-1)),
        (3,(2,3,4,7),(8,4,4,-1)),
        (7,(2,3,4,7),(-32,-16,-16,4))):
        V=F()
        witnesses=[]
        for packet in range(1,33):
            H=16*V
            for s,c in zip(off,weights):
                H+=F(c,8*(packet-1)+s)
                assert H>0 if residue!=7 else H<0
                witnesses.append(str(H))
            V=H
        checks.append({'class8':residue,'packets':32,'partial_states_checked':128,
                       'nonzero':True,'exact_shadow_sha256':sha256('\n'.join(witnesses).encode()).hexdigest()})
    dossier=Path(__file__).resolve().parent.parent/'SHARP_CONDUCTOR_GROWTH.md'
    print(json.dumps({'status':'PASS finite calibration; universal proof separately reviewed',
        'reviewed_dossier_sha256':sha256(dossier.read_bytes()).hexdigest(),
        'partial_shadow_checks':checks,'finite_diagnostics_only':diagnostics,
        'boundary':'fixed epsilon first, then n tends to infinity; no error rate or normality claim'},indent=2))


if __name__=='__main__':
    main()
