"""Separate route: Euler Beta products + rational Lagrange interpolation.

Does not import arrow_probe; shared mathematical source/model authority remains.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,prod
from itertools import product
import json

HERE=Path(__file__).parent
receipt=json.loads((HERE/'receipts'/'probe.json').read_text())

def source(a):return F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)

def beta(x,k):
    return F(factorial(k),1)/prod((x+j for j in range(k+1)),start=F(1))

def moment(a,ones,zeros):
    return sum((F(c,8)*beta(F(a+d,8)+zeros,ones) for d,c in [(0,4),(3,-2),(4,-1),(5,-1)]),F())/source(a)

def invert_resolvent(parameters,marks,values):
    # Interpolate numerator N(t) of sum v_j/(t+x_j), then take residues.
    answer=[]
    for x in marks:
        t=-F(x)
        numerator=F()
        for i,a in enumerate(parameters):
            denominator_at_a=prod((F(a)+y for y in marks),start=F(1))
            lagrange=prod(((t-b)/(F(a)-b) for k,b in enumerate(parameters) if k!=i),start=F(1))
            numerator+=values[i]*denominator_at_a*lagrange
        derivative=prod((F(y)-x for y in marks if y!=x),start=F(1))
        answer.append(numerator/derivative)
    return answer

cases=0
for row in receipt['snapshot_aliases']:
    a,m=row['a'],row['m']
    expected=[comb(m,j)*moment(a,j,m-j) for j in range(m+1)]
    assert expected==list(map(F,row['endpoint']))
    # Independent direct path perturbation integration, maintaining every prefix grade.
    weights={}
    for bits in product([0,1],repeat=m):
        base=moment(a,sum(bits),m-sum(bits))
        prefix=bits[:3]
        sign=1 if prefix in [(0,1,0),(1,0,1)] else -1 if prefix in [(0,1,1),(1,0,0)] else 0
        delta=F(sign,2)*moment(a,2+sum(bits[3:]),2+(m-3)-sum(bits[3:]))
        weights[bits]=base+delta
    for prefix_length in range(1,m+1):
        observed=[sum((v for bits,v in weights.items() if sum(bits[:prefix_length])==j),F()) for j in range(prefix_length+1)]
        assert observed==[comb(prefix_length,j)*moment(a,j,prefix_length-j) for j in range(prefix_length+1)]
        cases+=1

for row in receipt['cycles']:
    a,m,d=row['a'],row['m'],row['d']
    expected=[[F() for _ in range(m+d+1)] for _ in range(m+1)]
    for bits in product([0,1],repeat=m+d):
        expected[sum(bits[:m])][sum(bits)]+=moment(a,sum(bits),m+d-sum(bits))
    assert expected==[[F(v) for v in ar] for ar in row['joint']]
    cases+=1

for row in receipt['tomography']:
    values=[[F(v) for v in ar] for ar in row['observed']]
    first=[invert_resolvent(row['left'],range(row['m']+1),col) for col in zip(*values)]
    recovered=[invert_resolvent(row['right'],range(row['m']+row['d']+1),ar) for ar in zip(*first)]
    assert recovered==[[F(v) for v in ar] for ar in row['joint']]
    cases+=1

# Verify triangle-blind direction without importing primary quadratic field code.
z=[[F(v) for v in ar] for ar in receipt['triangle_matched_direction']]
H=[sum((F(1,k) for k in range(1,j+1)),F()) for j in range(9)]
# Lambda^n=a_n+b_n*lambda; lambda^2=1-lambda.
lam=[(F(1),F()),(F(),F(1))]
for n in range(2,9):lam.append((lam[-1][1],lam[-1][0]-lam[-1][1]))
assert all(sum(row,F())==0 for row in z)
assert all(sum(col,F())==0 for col in zip(*z))
for i in range(3):
    for j in range(3):
        acc=[F(),F()]
        for r,row in enumerate(z):
            a=(F(1),F()) if i==0 else (H[r],F()) if i==1 else lam[r]
            for s,v in enumerate(row):
                b=(F(1),F()) if j==0 else (H[s],F()) if j==1 else lam[s]
                acc[0]+=v*(a[0]*b[0]+a[1]*b[1])
                acc[1]+=v*(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
        assert acc==[0,0]
        cases+=1

out={'status':'PASS','independence':'separate formulas and implementation; same model, not external referee','prefix_and_joint_and_interpolation_checks':cases,'beta_rows':16,'path_joint_rows':4,'lagrange_tomographies':3,'triangle_basis_pairs':9}
with (HERE/'receipts'/'oracle.json').open('x') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
