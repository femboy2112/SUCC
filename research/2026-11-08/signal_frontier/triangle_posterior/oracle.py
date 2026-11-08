"""Exact independent Pascal/circle oracle; no trigonometric floats in checks."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse, importlib.util, json, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))
source_path=ROOT/'research/2026-10-29/operational_triangle_frontier/operational_triangle.py'
spec=importlib.util.spec_from_file_location('tp_inherited_source',source_path)
inherited=importlib.util.module_from_spec(spec);spec.loader.exec_module(inherited)
from observational_succ.duck_bbp import forcing


def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cpow(z,h):
    if h<0:return cpow((z[0],-z[1]),-h)
    r=(F(1),F(0))
    for _ in range(h):r=cmul(r,z)
    return r

def node(t):
    t=F(t);return ((1-t*t)/(1+t*t),2*t/(1+t*t))

def matrix(nodes,H):
    rows=[[F(1)]*len(nodes)]
    for h in range(1,H+1):
        powers=[cpow(z,h) for z in nodes]
        rows.extend([[z[0] for z in powers],[z[1] for z in powers]])
    return rows

def rref(rows):
    a=[list(map(F,row)) for row in rows]
    if not a:return a,[]
    if any(len(row)!=len(a[0]) for row in a):raise ValueError('rectangular matrix required')
    pivots=[];target=0
    for col in range(len(a[0])):
        pivot=next((r for r in range(target,len(a)) if a[r][col]),None)
        if pivot is None:continue
        a[target],a[pivot]=a[pivot],a[target]
        scale=a[target][col];a[target]=[v/scale for v in a[target]]
        for r in range(len(a)):
            if r!=target:
                scale=a[r][col]
                a[r]=[v-scale*w for v,w in zip(a[r],a[target])]
        pivots.append(col);target+=1
        if target==len(a):break
    return a,pivots

def rank(rows):return len(rref(rows)[1])
def apply(rows,q):return [sum((x*y for x,y in zip(row,q)),F()) for row in rows]
def kernel(rows):
    a,pivots=rref(rows);n=len(rows[0]);free=next((j for j in range(n) if j not in pivots),None)
    if free is None:raise ValueError('no nonzero kernel')
    v=[F()]*n;v[free]=F(1)
    for r,p in enumerate(pivots):v[p]=-a[r][free]
    return v

def recover(rows,values):
    n=len(rows[0]);a,pivots=rref([row+[value] for row,value in zip(rows,values)])
    if any(all(v==0 for v in row[:n]) and row[n] for row in a):raise ValueError('inconsistent measurements')
    if pivots[:n]!=list(range(n)):raise ValueError('nonunique inverse')
    return [a[j][-1] for j in range(n)]


def pascal_polynomials(m):
    if type(m) is not int or m<0:raise ValueError('nonnegative integer depth required')
    grades=[[F(1)]]
    for _ in range(m):
        next_grades=[[F()]*(len(grades)+1) for _ in range(len(grades)+1)]
        for j,poly in enumerate(grades):
            for k,c in enumerate(poly):
                next_grades[j][k+1]+=c
                next_grades[j+1][k]+=c
                next_grades[j+1][k+1]-=c
        grades=next_grades
    return grades

def R(a):
    a=F(a)
    if a<=0:raise ValueError('positive a required')
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)

def source_mass(a,m):
    return [sum((c*R(F(a)+8*k)/R(a) for k,c in enumerate(poly)),F())
            for poly in pascal_polynomials(m)]

def eval_poly(poly,x):
    out=F()
    for c in reversed(poly):out=out*x+c
    return out

def discrete_grades(values,weights,m):
    if len(values)!=len(weights) or not values or any(not 0<x<1 for x in values) or sum(weights)!=1 or any(w<0 for w in weights):
        raise ValueError('positive latent family and probability weights required')
    return [sum((w*eval_poly(poly,x) for x,w in zip(values,weights)),F())
            for poly in pascal_polynomials(m)]

def run():
    checks={'rank':0,'recovery':0,'positive_alias':0,'source_mass':0,'posterior_update':0,
            'enumerated_paths':0,'source_forcing':0,'posterior_counterexample':0}
    for m in range(13):
        nodes=[node(F(j,3)) for j in range(m+1)]
        H=(m+1)//2;A=matrix(nodes,H)
        assert rank(A)==m+1;checks['rank']+=1
        total=(m+1)*(m+2)//2;q=[F(j+1,total) for j in range(m+1)]
        assert recover(A,apply(A,q))==q;checks['recovery']+=1
        if m:
            low=(m-1)//2;B=matrix(nodes,low);v=kernel(B)
            eps=min(qj/(2*abs(vj)) for qj,vj in zip(q,v) if vj)
            left=[qj+eps*vj for qj,vj in zip(q,v)];right=[qj-eps*vj for qj,vj in zip(q,v)]
            assert all(x>0 for x in left+right) and left!=right and apply(B,left)==apply(B,right)
            checks['positive_alias']+=1
        for a in (F(1),F(9),F(17),F(32),F(8*m+1)):
            ours=source_mass(a,m)
            target=[inherited.endpoint_mass(a,m,j) for j in range(m+1)]
            assert ours==target and sum(ours)==1 and all(x>0 for x in ours)
            checks['source_mass']+=m+1
            nextrow=source_mass(a,m+1); rebuilt=[F()]*(m+2)
            for j,qj in enumerate(ours):
                f,g=inherited.posterior_prediction(a,m,j)
                assert f+g==1 and 0<f<1 and 0<g<1
                rebuilt[j]+=qj*f;rebuilt[j+1]+=qj*g
            assert rebuilt==nextrow;checks['posterior_update']+=m+2
    values=[F(1,7),F(2,5),F(4,5)];weights=[F(1,6),F(1,3),F(1,2)]
    for m in range(9):
        field=[[F() for _ in values] for _ in range(m+1)]
        for word in product((0,1),repeat=m):
            j=sum(word)
            for k,(x,w) in enumerate(zip(values,weights)):
                prob=w
                for bit in word:prob*=1-x if bit else x
                field[j][k]+=prob;checks['enumerated_paths']+=1
        for j,poly in enumerate(pascal_polynomials(m)):
            assert field[j]==[w*eval_poly(poly,x) for x,w in zip(values,weights)]
    pa=discrete_grades([F(1,5),F(3,5)],[F(1,4),F(3,4)],2)
    pb=discrete_grades([F(2,5),F(4,5)],[F(3,4),F(1,4)],2)
    assert pa==pb==[F(7,25),F(11,25),F(7,25)]
    a3=discrete_grades([F(1,5),F(3,5)],[F(1,4),F(3,4)],3)
    b3=discrete_grades([F(2,5),F(4,5)],[F(3,4),F(1,4)],3)
    assert a3[0]==F(41,250) and b3[0]==F(22,125)
    assert a3[0]/pa[0]==F(41,70) and b3[0]/pb[0]==F(22,35)
    checks['posterior_counterexample']=4
    for n in range(1,101):
        assert R(8*n-7)==forcing(n);checks['source_forcing']+=1
    return {'status':'PASS','authority':'Exact rational finite checks; general and limiting theorems are paper proofs',
            'counts':checks,'total_checks':sum(checks.values()),'max_depth':12,
            'posterior_counterexample':{'depth2':[str(x) for x in pa],
                'depth3_A':[str(x) for x in a3],'depth3_B':[str(x) for x in b3]},
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'inherited_source_sha256':sha256(source_path.read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
