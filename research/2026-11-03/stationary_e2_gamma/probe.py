"""Replay exact preregistered E² receiver/Gamma rational source holdouts.

Use --verify to compare against frozen finite JSON receipt. No external pi
sample, no floating comparison in any PASS. mpmath not required for replay.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import sys
ROOT=Path(__file__).parent

def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/(name+'.py'))
    mod=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod

e=load('stationary_e_observer')
g=load('gamma_tangent_field')


def sha(q):
    q=F(q)
    return hashlib.sha256(f'{q.numerator}/{q.denominator}'.encode('ascii')).hexdigest()


def receipt():
    rows=[]
    for B in (72,160):
        o=e.observer_at(B)
        a0=e.source_alpha_B(B)
        a1=e.e2_complete(B)
        assert o.alpha==a0==a1
        u=F(0)
        for k in range(1,B+1):u=16*u+e.original_r(k)
        assert o.original_U==u
        seams=[]
        for n in (B//3,2*B//3):
            s=e.observer_at(n)
            valid=s.original_U+e.full_finite_seam(n,B)==16**n*a0
            assert valid
            seams.append({'n':n,'exact_seam':True})
        rows.append({'B':B,'q_B':str(o.q),'p_B':str(o.p),
                     'alpha_B_canonical_sha256':sha(a0),'U_B_canonical_sha256':sha(u),
                     'three_independent_exact_completions':True,'seams':seams})
    q=F(1,2);depth=12
    delta=e.finite_intertwiner_residual(q,depth)
    expected=e.finite_intertwiner_expected(q,depth)
    assert delta==expected
    tangent=[]
    for N in (24,48):
        w=F(1,2)
        obj=g.product_corrected(N,w)
        same=obj.z*g.product_gamma2(N,w)==g.product_raw(N,w)
        assert same
        tangent.append({'N':N,'omega':'1/2','q_N':str(obj.q),
                        'rational_Gaussian_product_factorization':True,
                        'corrected_modulus_float_diagnostic':round(float(obj.z.norm2())**.5,12)})
    return {'date':'2026-11-03','status':'FINITE EXACT OBSERVATIONS ONLY; no source-selected Weyl cancellation',
            'source':'original 4 signed BBP poles; U0=0; old SUCC E2 rank-two chiral 8-tap shell',
            'parent':'16e4d36369822e669f214b455481c25a93ba294c',
            'e_receivers':rows,'gamma_finite_anomaly':{'q':'1/2','B':12,'equals_exact_positive_residual':True,'canonical_sha256':sha(delta)},
            'auxiliary_gamma_tangent':tangent,
            'warning':'Gamma tangent is an auxiliary probability model; coherent same-original-forcing non-Haar seeds persist; exact finite checks do not prove universal bounds.'}


if __name__=='__main__':
    out=receipt()
    file=ROOT/'RECEIPT.json'
    if '--verify' in sys.argv:
        assert file.exists() and json.loads(file.read_text())==out
        print('2/2 E-receiver horizons plus 2/2 tangent holdouts REPLAY PASS')
    else:
        file.write_text(json.dumps(out,indent=2)+'\n')
        print('wrote',file)
    print(json.dumps(out,indent=2))
