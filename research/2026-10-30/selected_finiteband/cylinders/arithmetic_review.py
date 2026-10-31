"""Fresh two-node witness and moment recurrence; imports no arithmetic code."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json


def moments(maximum):
    # Geometric shifting: 15 S_k = 1+sum_{i<k} binom(k,i) S_i.
    S=[]
    for k in range(maximum+1):
        S.append((1+sum((comb(k,i)*S[i] for i in range(k)),F()))/15)
    out=[]
    for k in range(maximum+1):
        value=F()
        for l in range(k+1):
            integral=sum((F(w*((d-7)**(l+1)-(-7)**(l+1)),(l+1)*8**l)
                          for d,w in ((3,2),(4,1),(5,1))),F())
            value+=F(comb(k,l),64)*S[k-l]*integral
        out.append(value)
    return out


def r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def run():
    here=Path(__file__).resolve().parent
    front=here.parent/'arithmetic'
    witness=front/'receipts/fresh-quadrature-witnesses.json'
    rows=json.loads(witness.read_text())['rows']
    mu=moments(5)
    assert mu[0]==F(1,64)
    checks=[]
    for row in rows:
        bs=list(map(F,row['nodes']))
        ws=list(map(F,row['weights']))
        M,J=row['M'],row['J']
        assert len(bs)<=M+J+1
        assert all(w>0 for w in ws)
        assert all(b>=F(1,8) for b in bs)
        for k in range(J+1):
            assert sum((w*b**k for b,w in zip(bs,ws)),F())==mu[k]
        def g(n):
            return sum((w/(n+b)**2 for b,w in zip(bs,ws)),F())
        for n in range(1,M+1):
            assert 16*g(n-1)-g(n)==r(n)
        assert F(row['completed_constant'])==16*g(0)
        checks.append(dict(M=M,J=J,nodes=len(bs),equations=M+J+1))
    # New endpoint-supported two-node witness, no numerical optimizer.
    a,b=F(1,8),F(3,4)
    fa=16/a**2-1/(1+a)**2
    fb=16/b**2-1/(1+b)**2
    wa=(r(1)-mu[0]*fb)/(fa-fb)
    wb=mu[0]-wa
    assert wa>0 and wb>0
    assert wa+wb==mu[0]
    assert wa*fa+wb*fb==r(1)
    def gnew(n):
        return wa/(n+a)**2+wb/(n+b)**2
    alpha=16*gnew(0)
    assert 16*gnew(0)-gnew(1)==r(1)
    first_defect=16*gnew(1)-gnew(2)-r(2)
    assert first_defect!=0
    return dict(status='PASS',reviewed_paper_sha256=hashlib.sha256((front/'ARITHMETIC_THEOREMS.md').read_bytes()).hexdigest(),
                witness_input_sha256=hashlib.sha256(witness.read_bytes()).hexdigest(),
                moment_method='geometric shift recurrence plus integrated offset powers',
                moments=list(map(str,mu)),existing_holdout_checks=checks,
                fresh_closed_form_witness=dict(M=1,J=0,nodes=[str(a),str(b)],weights=[str(wa),str(wb)],
                    completed_rational=str(alpha),next_source_defect=str(first_defect)),
                scope='same-model hostile paper audit and exact independent finite witness')


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
