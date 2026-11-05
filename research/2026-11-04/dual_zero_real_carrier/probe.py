"""Deterministic finite exact source receipts for projective R support.

Generated numbers are exact finite probes, not proof of all-horizon source
asymptotics, physical Feynman process or pi digit normality.
"""
from __future__ import annotations
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as Q
try:
    from zero_real_carrier import (authentic_r,primal_r,source_phase_stream,
        source_tangent_descriptor,cayley_rational,tangent_minpoly_for_odd_conductor,
        zero_overlap,zero_commutator_hs_square,projective_chart_quarters,
        source_phase_stream,integer_oracle_stream)
except ImportError:
    from .zero_real_carrier import (authentic_r,primal_r,source_phase_stream,
        source_tangent_descriptor,cayley_rational,tangent_minpoly_for_odd_conductor,
        zero_overlap,zero_commutator_hs_square,projective_chart_quarters,
        integer_oracle_stream)

HERE=Path(__file__).resolve().parent
RECEIPT=HERE/'FINITE_RECEIPT.json'

def q(x):
    return f'{x.numerator}/{x.denominator}'

def canonical_bytes(obj):
    return (json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n').encode('utf8')

def compute():
    P={'metadata':{'project':'SUCC','source':'Original BBP + prime-character Gaussian primal',
        'scope':'finite exact observations, no pi-normality proof',
        'inherited_asymptotic':'#497 (6N), #499 (8N); not re-proved by finite probe',
        'parent':'#500 exact head bf103c4a25bbd83b6cfbad1dd77895928300ddd9'},
       'two_zero_projectors':{},'source_states':{},'cayley':{},'tangent_minpolys':{}}
    for M in (3,5,7,15,35):
        P['two_zero_projectors'][str(M)]={'overlap':q(zero_overlap(M)),
            'commutator_HS_norm_squared':q(zero_commutator_hs_square(M))}
    for name,primal in (('original',False),('angular_primal',True)):
        rows=dict(source_phase_stream(61,primal))
        ref=dict(integer_oracle_stream(61,primal))
        assert rows==ref
        states=[]
        for n in (1,2,3,5,8,13,21,37,61):
            x=rows[n]
            desc=source_tangent_descriptor(x)
            states.append({'n':n,'source_phase':q(x) if n<=3 else None,
                           'source_phase_sha256':hashlib.sha256(q(x).encode()).hexdigest(),
                           'source_denominator_bits':x.denominator.bit_length(),
                           'tangent_field_degree_bits':desc['exact_algebraic_degree'].bit_length(),
                           'tangent_field_degree':desc['exact_algebraic_degree'] if n<=2 else None,
                           'all_source_denominator_odd':bool(x.denominator%2)})
        P['source_states'][name]=states
    for t in (Q(0),Q(1),Q(1,2),Q(2,3),Q(4,35),Q(-2,3),Q(5,8)):
        z=cayley_rational(t)
        P['cayley'][q(t)]={'real':q(z[0]),'imag':q(z[1])}
    P['cayley']['infinity']={'real':'-1/1','imag':'0/1'}
    for M in (3,5,7,9,11,15,21,35):
        pol=tangent_minpoly_for_odd_conductor(M)
        assert pol.is_irreducible
        P['tangent_minpolys'][str(M)]={'degree':pol.degree(),
            'leading':str(pol.LC()),'constant':str(pol.eval(0)),
            'coefficients_sha256':hashlib.sha256(','.join(map(str,pol.all_coeffs())).encode()).hexdigest()}
    P['original_first_source']=q(authentic_r(1))
    P['primal_first_source']=q(primal_r(1))
    P['reciprocity_at_first_primal_phase']={'from':'4/35','to':'27/70',
        'Fourier_h_phase_identity':'e(h(1/2-x))=(-1)^h conj(e(hx))'}
    P['quarter_chart_at_half']=[{'real':q(z[0]),'imag':q(z[1])}
                                for z in projective_chart_quarters(Q(1,2))]
    raw=canonical_bytes(P)
    return {'receipt':P,'content_sha256':hashlib.sha256(raw).hexdigest()}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--write',action='store_true')
    ap.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    obj=compute()
    if args.write:
        RECEIPT.write_bytes(canonical_bytes(obj))
        print('WROTE',RECEIPT.name,obj['content_sha256'])
    if args.verify:
        actual=json.loads(RECEIPT.read_text())
        if actual !=obj:raise AssertionError('finite exact source receipt changed')
        print('DUAL_ZERO_REAL_SOURCE_EXACT_RECEIPT_VERIFIED',obj['content_sha256'])
    if not args.write and not args.verify:print(json.dumps(obj,indent=2,sort_keys=True))

if __name__=='__main__':main()
