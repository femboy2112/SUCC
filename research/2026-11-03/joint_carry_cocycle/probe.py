"""Preregistered exact zero-seeded source/2-adic/real carry checks (NOT Weyl proof)."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from joint_carry import (
    principal_short_cone, anchor_principal,anchor_window_depth,depth2,
    original_r, real_source, gaussian_source, source_principal_binary,
    principal_cocycle_stream,real_carry_cocycle,
    full_zero_seed_modular,coherent_odd_counterfeit, precision_tax_witness,
)

ANCHORS=(23,47,89,193)
INDICES=(521,877,1327)


def hx(n:int) -> str:
    if n<0: raise ValueError('unsigned digest only')
    return hashlib.sha256(n.to_bytes(max(1,(n.bit_length()+7)//8),'big')).hexdigest()


def rational_receipt(x:Q) -> dict:
    x=Q(x)
    scale=1<<40
    lo=(x.numerator*scale)//x.denominator
    hi=-((-x.numerator*scale)//x.denominator)
    return {'sha256_numer':hx(abs(x.numerator)),'numer_sign':(x.numerator>0)-(x.numerator<0),
            'sha256_denom':hx(x.denominator),
            'num_bits':abs(x.numerator).bit_length(),'den_bits':x.denominator.bit_length(),
            'lower_at_2pow40':lo,'upper_at_2pow40':hi}


def run():
    output={'status':'EXACT FINITE OBSERVATIONS ONLY; selected real Weyl and pi normality OPEN',
            'source':'authentic four signed BBP poles; U0=0; canonical zero-seeded H/G projectors',
            'baseline':'8383f69f5eb92eb037dde84f686cf3c77e043c2e',
            'predeclared':'research/2026-11-03/joint_carry_cocycle/PREREGISTRATION.md at commit 2dc96f2116d3a6079a680300f7037a19456ca69c',
            'anchor_holdouts':{},'selected_real_holdouts':{},'cocycle_stream':{},'hostile':{}}
    for k in ANCHORS:
        N=1<<k
        expected=anchor_principal(k)
        row={'n_exponent':k,'h_numer_signed':-1,'g_numer_signed':1,
             'principal_denominator_bits':k+6,'n_window':{}}
        assert principal_short_cone(N)==expected[0]
        assert principal_short_cone(N,'G')==expected[1]
        for d in range(min(8,(k-1)//5)+1):
            h=principal_short_cone(N+d)
            g=principal_short_cone(N+d,'G')
            depth=anchor_window_depth(k,d)
            assert depth2(h)==depth2(g)==depth,(k,d,depth,depth2(h),depth2(g))
            assert (h+g)%1==0
            row['n_window'][str(d)]={'H_depth':depth,'H_numerator_sha256':hx(h.numerator),
                                     'G_numerator_sha256':hx(g.numerator)}
        output['anchor_holdouts'][str(k)]=row
    qH=Q(0)
    h=hashlib.sha256()
    n_checked=0
    for n, a, b in principal_cocycle_stream(4096):
        if n==0:continue
        qH=(16*qH+source_principal_binary(n))%1
        assert qH==a and (a+b)%1==0
        # Stable rolling digest of canonical principal residue, not floats.
        raw=(str(n)+':'+str(a.numerator)+'/'+str(a.denominator)+';').encode()
        h.update(raw)
        n_checked+=1
    output['cocycle_stream']={'length':n_checked,'rolling_sha256':h.hexdigest(),
                              'final_depth':depth2(qH),'final_principal_sha256':hx(qH.numerator)}
    selected={}
    for n,x,y,u in full_zero_seed_modular(max(INDICES)):
        if n not in INDICES:continue
        cert=real_carry_cocycle(x,y)
        assert cert['glued_real_phase']==cert['glued_odd_phase']==u
        assert cert['dyadic_gaussian_part']==principal_short_cone(n,'G')
        selected[str(n)]={
            'local_debt_bits':depth2(cert['dyadic_gaussian_part']),
            'source_real_carry':cert['real_carry'], 'odd_carry':cert['odd_carry'],
            'odd_low_crossing':cert['odd_low_crossing'],
            'odd_high_crossing':cert['odd_high_crossing'],
            'source_carry_defect':cert['carry_difference'],
            'real_H_phase':rational_receipt(x),
            'real_G_phase':rational_receipt(y),
            'original_real_phase':rational_receipt(u),
            'odd_H_phase':rational_receipt(cert['odd_real_part']),
            'odd_G_phase':rational_receipt(cert['odd_gaussian_part']),
        }
    assert len(selected)==len(INDICES)
    output['selected_real_holdouts']=selected
    hostile={}
    for k in ANCHORS:
        d=coherent_odd_counterfeit(k+5)
        assert d['glued_real_phase']==Q(4,5)
        assert d['odd_low_crossing']==d['odd_high_crossing']==0
        hostile[str(k)]={'p2_debt':k+5,'real_phase':[4,5],
                         'odd_boundary_events':[0,0]}
    output['hostile']['coherent_odd_cofactor']=hostile
    output['hostile']['precision_tax']={str(k):precision_tax_witness(k,k+5)
                                            for k in (1,11,37)}
    return output


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    a=p.parse_args()
    result=run()
    out=Path(__file__).with_name('EXACT_RECEIPT.json')
    if a.verify:
        assert json.loads(out.read_text())==result
        print('EXACT original-source new finite receipt replay: PASS')
    else:
        out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print('generated',out,'anchors',list(result['anchor_holdouts']),
              'original finite carry indices',list(result['selected_real_holdouts']))
