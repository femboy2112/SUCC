"""Distinct SymPy stencil solve + direct source logs; no prime_frames import.

mpmath is numerical calibration only. Exact integer intervals come from the
separately implemented probe. Same model lineage is explicitly retained.
"""
from fractions import Fraction
from pathlib import Path
from math import factorial
import json
import sympy as sp
import mpmath as mp


def main():
    mp.mp.dps=210
    root=Path(__file__).parent
    data=json.loads((root/'receipts/frame-data.json').read_text())
    rows=[]
    for row in data['rows']:
        n,m=row['n'],row['m']
        nodes=[sp.Rational(j,2*m) for j in range(-m,m+1)]
        stencil=sp.finite_diff_weights(1,nodes,0)[1][-1]
        def logcarrier(x):
            x=mp.mpf(int(x.p))/int(x.q)
            return mp.fsum(mp.power(16,n-k)*(4*mp.log(8*k-7+x)-2*mp.log(8*k-4+x)
                       -mp.log(8*k-3+x)-mp.log(8*k-2+x)) for k in range(1,n+1))
        got=mp.fsum(mp.mpf(int(w.p))/int(w.q)*logcarrier(x)
                   for w,x in zip(stencil,nodes) if w)
        lo,hi=[mp.mpf(x)/mp.power(2,row['bits']) for x in row['frame_interval']]
        assert lo<got<hi,(n,m,got,lo,hi)
        u=sp.factor(sum(sp.Integer(16)**(n-k)*(sp.Rational(4,8*k-7)-sp.Rational(2,8*k-4)
                      -sp.Rational(1,8*k-3)-sp.Rational(1,8*k-2)) for k in range(1,n+1)))
        assert str(u)==row['exact_U']
        ureal=mp.mpf(int(u.p))/int(u.q)
        err=(-1)**m*(ureal-got)
        eb=mp.mpf(8)*(mp.power(16,n)-1)/(15*(2*m+1))*(mp.factorial(m)/mp.power(m,m))**2
        assert 0<err<eb
        rows.append({'n':n,'m':m,'signed_error':mp.nstr(err,30),'bound':mp.nstr(eb,20),
                     'interval_membership':True,'weight_count':sum(bool(w) for w in stencil)})
    # Finite-grid alias reconstructed as a polynomial, including derivative.
    x=sp.Symbol('x')
    alias=[]
    for m in (2,5,9):
        P=x*sp.prod(1-(2*m*x/j)**2 for j in range(1,m+1))
        assert sp.diff(P,x).subs(x,0)==1
        assert all(P.subs(x,sp.Rational(j,2*m))==0 for j in range(-m,m+1))
        alias.append({'m':m,'same_values':2*m+1,'different_initial_jet':True})
    # Real analytic coherent initial germ: derivative stencil is exact on s*x.
    # Its irrational frame values are not assigned rational prime valuations.
    s=-mp.pi/16
    coherent=[]
    for n in (7,17,31):
        m=2*n+3
        xs=[sp.Rational(j,2*m) for j in range(-m,m+1)]
        ws=sp.finite_diff_weights(1,xs,0)[1][-1]
        jet=mp.fsum(mp.mpf(int(w.p))/int(w.q)*mp.mpf(int(x.p))/int(x.q)*s for w,x in zip(ws,xs))
        assert abs(jet-s)<mp.mpf('1e-190')
        coherent.append({'n':n,'linear_seed_stencil_exact':True,'prime_value_domain':False})
    print(json.dumps({'status':'PASS','precision_dps':mp.mp.dps,'rows':rows,
                      'finite_germ_aliases':alias,'coherent_real_extension':coherent,
                      'sympy':sp.__version__,'mpmath':mp.__version__,
                      'authority':'separate implementation; not external mathematical referee'},indent=2))


if __name__=='__main__':main()
