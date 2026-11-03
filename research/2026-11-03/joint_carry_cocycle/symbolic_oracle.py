"""Separate SymPy polynomial and recurrence sanity oracle, no asymptotic proof."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as S


def run():
    n,z=S.symbols('n z')
    rh = -1/(4*n-3)-1/(4*(2*n-1))-1/(4*(4*n-1))-1/(32*n)
    r = 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
    A=120*n**2-89*n+16
    D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    assert S.cancel(r-A/D)==0
    # Verify canonical H source matches direct Mellin polynomial of its 8 taps.
    htaps=[S.Rational(x) for x in (0,-2,0,-1,0,S.Rational(-1,2),0,S.Rational(-1,4))]
    mr=sum(htaps[j]/(8*(n-1)+j+1) for j in range(8))
    assert S.cancel(mr-rh)==0
    # This is a finite formal-series identity, not a numerical fit.
    q=S.series(-S.log(1-z)/(1-16*z),z,0,9).removeO().expand()
    vals=[S.expand(q).coeff(z,i) for i in range(9)]
    w=S.Rational(0)
    rec=[w]
    for j in range(1,9):
        w=16*w+S.Rational(1,j)
        rec.append(w)
    assert vals==rec
    # Algebraic carry coboundary on exactly the marked zero seed:
    H,G,rh_symbol,rg_symbol,cH,cG,c,kprev,knext=S.symbols('H G rh rg cH cG c kprev knext')
    yh=16*H+rh_symbol-cH
    yg=16*G+rg_symbol-cG
    total_channels=yh+yg-knext
    previous_sum=H+G-kprev
    original=16*previous_sum+rh_symbol+rg_symbol-c
    derived=S.expand(total_channels-original)
    assert S.simplify(derived-(c-cH-cG+16*kprev-knext))==0
    return {'rational_r_numerator':str(A),'rational_r_denominator':str(D),
            'direct_mellin_H_equals_source':True,
            'weighted_harmonic_first9':[str(x) for x in vals],
            'formal_recurrence_coefficients_match':True,
            'carry_coboundary_polynomial':'c-cH-cG+16*kprev-knext',
            'carry_coboundary_symbolic_zero':True,
            'formal_pi_normality':False}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_name('SYMBOLIC_RECEIPT.json')
    import sys
    if '--verify' in sys.argv:
        assert json.loads(path.read_text())==result
        print('Independent SymPy exact symbolic receipt: PASS')
    else:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print('SymPy exact symbolic receipt written')
