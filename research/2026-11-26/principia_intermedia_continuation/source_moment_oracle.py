#!/usr/bin/env python3
"""Independent SymPy determinant/Sturm check of the finite BBP seam specimens.

Run from repository root. Native code uses rational Gaussian elimination;
this oracle uses a determinant polynomial and exact real-root isolation.
No floating approximation is accepted as a sign or root certificate.
"""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

import sympy as sp
from observational_succ import principia_bbp_seams as native


def m(k):
    # Integrate u**k dmu by u=t**8, retaining all original signed poles.
    return (sp.Rational(4,8*k+1)-sp.Rational(2,8*k+4)
            -sp.Rational(1,8*k+5)-sp.Rational(1,8*k+6))


def sr(q):
    return sp.Rational(q.numerator,q.denominator)


def run():
    u=sp.Symbol('u')
    results=[]
    previous=None
    for n in range(1,9):
        h=sp.Matrix(n,n,lambda i,j:m(i+j))
        det=h.det()
        assert det>0
        augmented=sp.Matrix([[m(i+j) for j in range(n+1)] for i in range(n)]
                            +[[u**j for j in range(n+1)]])
        polynomial=sp.Poly(sp.expand(augmented.det()/det),u)
        coeff=tuple(sr(q) for q in native.orthogonal_polynomial(n))
        assert polynomial.as_expr()==sum(c*u**j for j,c in enumerate(coeff))
        assert polynomial.count_roots(0,1)==n
        assert sp.gcd(polynomial,polynomial.diff()).degree()==0
        intervals=polynomial.intervals(eps=sp.Rational(1,2**18))
        assert len(intervals)==n
        for ((a,b),multiplicity) in intervals:
            assert multiplicity==1 and 0<a<=b<1
            if a!=b:
                assert polynomial.eval(a)*polynomial.eval(b)<0
            else:
                assert polynomial.eval(a)==0
        if previous is not None:
            # Interlacing proved classically; these exact finite specimens
            # independently check the generated source-polynomial family.
            for j in range(n-1):
                assert intervals[j][0][1]<previous[j][0][0]
                assert previous[j][0][1]<intervals[j+1][0][0]
        hp=sp.Matrix(n+1,n+1,lambda i,j:m(i+j)).det()/det
        assert hp==sr(native.inner(native.orthogonal_polynomial(n),native.orthogonal_polynomial(n)))
        # Adding a constant breaks the first moment-null constraint.
        bad=polynomial.as_expr()+1
        bad_integral=sum(sp.Poly(bad,u).nth(j)*m(j) for j in range(n+1))
        assert bad_integral==m(0)!=0
        results.append({
            'degree':n,'coefficients_ascending':[str(c) for c in coeff],
            'gram_determinant':str(det),'squared_norm':str(hp),
            'null_jet_orders':list(range(n)), 'first_nonzero_hasse_jet':str(hp/16**(n+1)),
            'roots_in_open_unit_interval':n,
            'root_intervals':[[str(a),str(b)] for ((a,b),_) in intervals],
            'roots_simple':True,'interlacing_with_previous': n>1,
        })
        previous=intervals
    capacities=[]
    for d in range(7):
        h=sp.Matrix(d+1,d+1,lambda i,j:m(i+j))
        inv=h.inv()
        gap=1/max(sum(abs(inv[i,j]) for j in range(d+1)) for i in range(d+1))
        assert gap==sr(native.residual_capacity(d))
        # Exact fresh integer coefficient vectors, no polynomial fit data.
        for j in range(1,18):
            c=sp.Matrix([((-1)**(i+j))*(i*i+3*j+1) for i in range(d+1)])
            assert max(abs(x) for x in h*c)>=gap
        capacities.append({'degree':d,'integer_moment_gap':str(gap),'holdouts':17})
    return {'status':'PASS','authority':'finite exact SymPy algebra and Sturm checks; universal proofs are in the paper',
            'sympy_version':sp.__version__,'source':'original four signed BBP poles, U0=0 unchanged',
            'orthogonal_specimens':results,'capacity_cases':capacities,
            'negative_controls':['added constant breaks moment null','zero/unknown-denominator guards in focused tests']}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path)
    args=parser.parse_args()
    result=run()
    rendered=json.dumps(result,indent=2)+'\n'
    if args.write:
        args.write.write_text(rendered)
    print(json.dumps({'status':result['status'],'orthogonal_degrees':8,'capacity_holdouts':119,
                      'sympy_version':result['sympy_version']}))
