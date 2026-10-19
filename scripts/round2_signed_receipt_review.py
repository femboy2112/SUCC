#!/usr/bin/env python3
"""Independent finite algebra check of a separately supplied signed-stack packet.

Does not import the signed implementation or certify its infinite-domain proof.
The JSON input is read as data; it supplies no executable command.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import sys
from pathlib import Path


def review(path):
    if hasattr(sys,'set_int_max_str_digits'):
        sys.set_int_max_str_digits(50000)  # bounded exact J24 fractions
    raw=Path(path).read_bytes()
    p=json.loads(raw)
    if p['source_blob']!='0cc8510b71d178fc79e8d410a86d8b6014cf9178' or p['base_commit']!='f309d9104ba480c1999c962af1df7c50f19e1bfe':
        raise ValueError('wrong signed-source credential')
    results={}
    for parity,s in p['sectors'].items():
        k,w=Q(s['kappa']),Q(s['w_floor'])
        assert k>0 and w>0
        # Direct inverse of [[k+w,-w],[-w,k+w]], without source modules.
        den=(k+w)**2-w*w
        inverse_diag=(k+w)/den
        inverse_off=w/den
        beta=1/k-inverse_diag
        assert beta==inverse_off==Q(s['edge_coefficient'])
        alpha=1/k-1/(k+w)
        assert alpha==Q(s['center_coefficient'])
        mat=lambda key:[[Q(x) for x in row]for row in s[key]]
        C,E,gain,old,new=map(mat,('center_Gram','edge_Gram_lower','gain','old_lower','new_lower'))
        for i in range(2):
            for j in range(2):
                assert gain[i][j]==(1+Q(p['eta']))*(alpha*C[i][j]+beta*E[i][j])
                assert new[i][j]-old[i][j]==gain[i][j]
        det=gain[0][0]*gain[1][1]-gain[0][1]**2
        assert gain[0][1]==gain[1][0] and gain[0][0]>0 and det>0
        scale=10**30
        lower=Q((det*scale).numerator//(det*scale).denominator,scale)
        results[parity]={'gain_PD':True,'gain_determinant_lower':str(lower),
            'new_first_diagonal_negative':new[0][0]<0,
            'inverse_formula_directly_verified':True}
    return {'method':'Independent direct 2x2 inverse and exact packet reconstruction; no source-action or infinite-domain reexecution.',
        'input_sha256':hashlib.sha256(raw).hexdigest(),'J':p['J'],'M':p['M'],'P':p['P'],
        'results':results,'RH_proved':False}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_packet',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    out=json.dumps(review(args.source_packet),indent=2)+'\n'
    if args.output: args.output.write_text(out)
    print(out,end='')
