"""Independent SymPy/numpy oracle: not importing observer_pinbed.py.

Source formulas independently reconstructed from four original signed poles.
This calibrates finite theorems, not all-horizon BBP statistical claims.
"""
from __future__ import annotations
import json
import itertools
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as S


def row_bb(t):
    poles=((4,7),(-2,4),(-1,3),(-1,2))
    return [S.Integer(16)**t] + [sum(S.Integer(16)**(t-j)/S.Integer(8*j-beta) for j in range(1,t+1)) for _,beta in poles]


def det_pos5(rows):
    # direct symbolic exact determinant independent of stdlib Gauss-Jordan solver
    return S.Matrix([row_bb(n) for n in rows]).det()


def circle_unit(t):
    t=S.Rational(t)
    return [(1-t*t)/(1+t*t),2*t/(1+t*t)]


def run():
    results={}
    original=S.Matrix([0,4,-2,-1,-1])
    tests=[1,2,3,4,5,6,7]
    matrix=S.Matrix([row_bb(t) for t in tests])
    assert matrix*original==S.Matrix([sum(S.Rational(c,8*j-b)*16**(t-j) for j in range(1,t+1) for c,b in ((4,7),(-2,4),(-1,3),(-1,2))) for t in tests])
    determinants=[det_pos5(inds) for inds in itertools.combinations(tests,5)]
    assert len(determinants)==21 and all(d>0 for d in determinants)
    results['bbp_7_5_minors_checked']=len(determinants)
    results['bbp_five_first_det']=str(determinants[0])
    assert sum(S.Rational(c,8*1-b) for c,b in ((4,7),(-2,4),(-1,3),(-1,2)))==S.Rational(47,15)

    # Source-valid state family and one corruption: distinct 5-row fits.
    base=matrix*original
    err=base.copy()
    err[4]+=S.Rational(1,103)
    matched=set()
    for inds in itertools.combinations(range(7),5):
        sub=matrix[list(inds),:]
        prediction=sub.inv()*err[list(inds),:]
        if sum(int(x!=y) for x,y in zip(matrix*prediction,err))<=1:
            matched.add(tuple(prediction))
    assert matched=={tuple(original)}
    results['bbp_full_exact_one_bad_head']=True

    gpspts=[(1,0),(0,1),(-1,0),(0,-1),(S.Rational(3,5),S.Rational(4,5))]
    H=S.Matrix([[S.Rational(a),S.Rational(b),S.Integer(1)] for a,b in gpspts])
    gpsminors=[H[list(idx),:].det() for idx in itertools.combinations(range(5),3)]
    assert len(gpsminors)==10 and all(v!=0 for v in gpsminors)
    results['gps2_minors_checked']=len(gpsminors)
    target=S.Matrix([S.Rational(17,9),S.Rational(-5,6),S.Rational(7,4)])
    measured=H*target
    corrupt=measured.copy()
    corrupt[2]+=S.Rational(1,97)
    hits=set()
    for idx in itertools.combinations(range(5),3):
        h=H[list(idx),:]
        x=h.inv()*corrupt[list(idx),:]
        if sum(int(u!=v) for u,v in zip(H*x,corrupt))<=1:
            hits.add(tuple(x))
    assert hits=={tuple(target)}
    results['gps2_full_exact_one_bad_head']=True

    # Local GPS geometry: grossly deteriorating precision with clustered directions.
    good=np.array(H.tolist(),dtype=float)
    clustered=np.array([[float(a),float(b),1] for a,b in (circle_unit(t) for t in [0,S.Rational(1,100),S.Rational(2,100),S.Rational(3,100),S.Rational(4,100)])])
    good_sigma=float(np.linalg.svd(good,compute_uv=False)[-1])
    clustered_sigma=float(np.linalg.svd(clustered,compute_uv=False)[-1])
    assert good_sigma>1e-1 and clustered_sigma<1e-3
    assert all(S.Matrix([[*circle_unit(S.Rational(t,100)),1] for t in i]).det()!=0 for i in itertools.combinations(range(5),3))
    results['gps_sigma_min_well_spread']=good_sigma
    results['gps_sigma_min_clustered']=clustered_sigma
    results['sigma_ratio_well_over_clustered']=good_sigma/clustered_sigma

    # Same-source phase alias at all late clocks and exact finite locked counterseed.
    for t in range(1,20):
        assert S.Integer(16)**t/S.Integer(16) in S.Integers
    M=12
    P=sum(S.Rational(1,16**j)*sum(S.Rational(c,8*j-b) for c,b in ((4,7),(-2,4),(-1,3),(-1,2))) for j in range(1,M+1))
    for n in range(M+1):
        U=(S.Matrix([row_bb(n)])*original)[0]
        T=sum(S.Integer(16)**(n-j)*sum(S.Rational(c,8*j-b) for c,b in ((4,7),(-2,4),(-1,3),(-1,2))) for j in range(n+1,M+1))
        assert S.simplify(U+T-S.Integer(16)**n*P)==0
        assert S.simplify(U-S.Integer(16)**n*P+T)==0
    results['bbp_terminal_locked_checks']=M+1

    # Hamming distance 3 for length 7 dimension 5, by positive all-5 minors.
    results['bbp_code_parameters']={'heads':7,'parameters':5,'distance':3,'erasures':2,'arbitrary_errors':1}
    results['gps2_code_parameters']={'heads':5,'parameters':3,'distance':3,'erasures':2,'arbitrary_errors':1}
    out=Path(__file__).with_name('independent_audit_receipt.json')
    out.write_text(json.dumps(results,sort_keys=True,indent=2)+'\n')
    print(json.dumps(results,sort_keys=True,indent=2))
    return results

if __name__=='__main__':
    run()
