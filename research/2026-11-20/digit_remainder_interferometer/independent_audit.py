"""Independent SymPy oracle: no imports from tested source model."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp


def check():
    counts={"hex_inverse":0,"four_stage":0,"walsh_orthogonality":0,
            "branch_norm":0,"original_four_poles":0,"bbp_prefix":0,
            "source_tail_order":0,"root_thresholds":0}
    for den in (5,17,64,97):
        for num in range(den):
            x=sp.Rational(num,den)
            v=16*x
            d=int(sp.floor(v));r=v-d
            assert 0<=d<16 and 0<=r<1 and sp.simplify((d+r)/16-x)==0
            counts["hex_inverse"]+=1
            b=[];y=x
            for _ in range(4):
                bit=int(sp.floor(2*y));y=sp.expand(2*y-bit);b.append(bit)
            assert d==8*b[0]+4*b[1]+2*b[2]+b[3] and r==y
            counts["four_stage"]+=1
    W=sp.Matrix(16,16,lambda k,d: -1 if ((int(k)&int(d)).bit_count()%2) else 1)
    assert W.T*W==16*sp.eye(16)
    counts["walsh_orthogonality"]=16*16
    for offset in (0,1,5,7):
        a=sp.Matrix([sp.Rational((d+offset)**2-7,d+2) for d in range(16)])
        base=(a.dot(a))/16
        bran=(a/4).dot(a/4)
        mixed=(W*a/16).dot(W*a/16)
        assert sp.simplify(base-bran)==0 and sp.simplify(base-mixed)==0
        counts["branch_norm"]+=1
    for n in range(1,97):
        poles=4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)
        reduced=sp.Rational(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        assert sp.factor(poles-reduced)==0
        counts["original_four_poles"]+=1
    # Source-tail certification using exact rational sums; do not import the
    # π digits as a numeric oracle or assume all prefix intervals are narrow.
    M=12
    r=lambda n: 4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)
    lo=sum((r(n)/16**n for n in range(1,M+1)),sp.Rational(0))
    hi=lo+r(M+1)/(15*16**M)
    assert lo<hi and hi<sp.Rational(1)
    assert sp.floor(lo*16**12)==sp.floor(hi*16**12)
    d12=int(sp.floor(lo*16**12))
    assert format(d12,'012X')=='3243F6A8885A'
    counts["bbp_prefix"]+=12
    for n in range(1,96):
        assert r(n)>r(n+1)>0
        counts["source_tail_order"]+=1
    # A separate exact SymPy check of authentic source-root positions on the
    # chosen left-semicircle chart (not a map from the actual pi phase).
    z=sp.symbols('z')
    H=(z*z+2)*(z*z+2*z+2)
    source_roots=(sp.I*sp.sqrt(2),-1+sp.I,-1-sp.I,-sp.I*sp.sqrt(2))
    angular=(sp.Rational(0),sp.Rational(1,4),sp.Rational(3,4),sp.Rational(1))
    for root,u in zip(source_roots,angular):
        assert sp.simplify(H.subs(z,root))==0
        assert 16*u in sp.Integers
        counts["root_thresholds"]+=1
    result={"independent":"SymPy 1.14 symbolic", "status":"PASS", "assertion_classes":counts,
            "total_assertions":sum(counts.values()),"certified_x_prefix":"3243F6A8885A",
            "scope":"exact finite radix observer algebra and BBP source interval; not physical energy, π normality or root-to-digit map"}
    return result

if __name__=='__main__':
    out=check()
    print(json.dumps(out,sort_keys=True,indent=2))
    Path(__file__).with_name('independent_audit_receipt.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
