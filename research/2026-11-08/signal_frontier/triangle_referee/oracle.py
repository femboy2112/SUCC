"""Independent exact triangle referee: no research implementation imports.

Gaussian-rational moment ranks and positive aliases; beta-product source
integrals; exact Q(sqrt5) source/geometric total-variation comparisons.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import argparse
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]


def gadd(z,w):return (z[0]+w[0],z[1]+w[1])
def gmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def gpow(z,n):
    out=(F(1),F(0))
    for _ in range(n):out=gmul(out,z)
    return out


def rows_for(nodes,H):
    rows=[[F(1)]*len(nodes)]
    for h in range(1,H+1):
        values=[gpow(z,h) for z in nodes]
        rows.extend([[v[0] for v in values],[v[1] for v in values]])
    return rows


def rref(matrix):
    a=[r[:] for r in matrix]; nr,nc=len(a),len(a[0]); row=0;pivots=[]
    for col in range(nc):
        found=next((j for j in range(row,nr) if a[j][col]),None)
        if found is None:continue
        a[row],a[found]=a[found],a[row]
        d=a[row][col];a[row]=[v/d for v in a[row]]
        for j in range(nr):
            if j!=row and a[j][col]:
                c=a[j][col];a[j]=[v-c*w for v,w in zip(a[j],a[row])]
        pivots.append(col);row+=1
        if row==nr:break
    return a,pivots


def dot(v,w):return sum((x*y for x,y in zip(v,w)),F())

def null_witness(rows):
    reduced,pivots=rref(rows); nc=len(rows[0])
    free=next(j for j in range(nc) if j not in pivots)
    v=[F()]*nc;v[free]=F(1)
    for i,p in enumerate(pivots):v[p]=-reduced[i][free]
    assert all(dot(row,v)==0 for row in rows)
    return v


@dataclass(frozen=True)
class Q5:
    a:F=F(0)
    b:F=F(0)
    def __add__(self,other):
        other=asq(other);return Q5(self.a+other.a,self.b+other.b)
    def __neg__(self):return Q5(-self.a,-self.b)
    def __sub__(self,other):return self+-asq(other)
    def __mul__(self,other):
        other=asq(other);return Q5(self.a*other.a+5*self.b*other.b,self.a*other.b+self.b*other.a)
    def __pow__(self,n):
        assert type(n) is int and n>=0
        out=Q5(F(1));base=self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        delta=a*a-5*b*b
        assert delta
        return ((delta>0)-(delta<0))*(1 if a>0 else -1)
    def absolute(self):return self if self.sign()>=0 else -self
    def encode(self):return {'rational':str(self.a),'sqrt5':str(self.b)}


def asq(x):return x if isinstance(x,Q5) else Q5(F(x))
ALPHA=Q5(F(-1,2),F(1,2))


def R(a):
    a=F(a);assert a>0
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)


def beta_product(x,j):
    # B(x,j+1), derived by j integrations by parts.
    den=F(1)
    for k in range(j+1):den*=x+k
    return F(factorial(j))/den


def grade_beta(a,m,j):
    beta=F(a,8)+m-j
    integral=F(4)*beta_product(beta,j)-F(2)*beta_product(beta+F(3,8),j)-beta_product(beta+F(1,2),j)-beta_product(beta+F(5,8),j)
    return comb(m,j)*integral/(8*R(a))


def grade_shift(a,m,j):
    # A separate finite monomial integration route used only for cross-checks.
    return comb(m,j)*sum(((-1)**k*comb(j,k)*R(a+8*(m-j+k)) for k in range(j+1)),F())/R(a)


def mixed_binomial(prior,m):
    return [sum((w*comb(m,j)*f**(m-j)*(1-f)**j for f,w in prior),F()) for j in range(m+1)]


def run():
    counts={'full_ranks':0,'positive_moment_aliases':0,'exact_barycentric':0,
            'source_mass_checks':0,'source_integral_crosschecks':0,'source_tv_bounds':0,
            'source_mean_checks':0,'posterior_alias_checks':0,'projectivity_rejections':0,
            'integer_return_checks':0,'pascal_posterior_refinements':0,'integer_seed_phase_carry_aliases':0}
    rank_rows=[]
    for m in range(1,19):
        nodes=[]
        for j in range(m+1):
            t=F(j,7)
            nodes.append(((1-t*t)/(1+t*t),2*t/(1+t*t)))
        assert len(set(nodes))==m+1
        H=(m+1)//2
        rows=rows_for(nodes,H);_,pivots=rref(rows)
        assert len(pivots)==m+1;counts['full_ranks']+=1
        low=rows_for(nodes,H-1)
        v=null_witness(low)
        eps=F(1,2*(m+1))/max(abs(x) for x in v)
        qplus=[F(1,m+1)+eps*x for x in v]
        qminus=[F(1,m+1)-eps*x for x in v]
        assert min(qplus)>0 and min(qminus)>0 and qplus!=qminus
        assert all(dot(row,qplus)==dot(row,qminus) for row in low)
        counts['positive_moment_aliases']+=1
        rank_rows.append({'m':m,'H':H,'full_rank':len(pivots),'lower_H':H-1,
                          'lower_rank':len(rref(low)[1]),'positive_alias':True})
    # General three-point barycentric recovery via oriented determinants.
    nodes=[(F(1),F(0)),(F(3,5),F(4,5)),(F(-5,13),F(12,13))]
    det=lambda x,y:x[0]*y[1]-x[1]*y[0]
    sub=lambda x,y:(x[0]-y[0],x[1]-y[1])
    u,v=sub(nodes[1],nodes[0]),sub(nodes[2],nodes[0]);D=det(u,v)
    assert D
    for a in range(13):
        for b in range(13-a):
            weights=[F(12-a-b,12),F(a,12),F(b,12)]
            phi=(sum((q*z[0] for q,z in zip(weights,nodes)),F()),sum((q*z[1] for q,z in zip(weights,nodes)),F()))
            x=sub(phi,nodes[0]); recovered=[det(x,v)/D,det(u,x)/D]
            assert recovered==weights[1:];counts['exact_barycentric']+=1
    priorA=[(F(1,5),F(1,4)),(F(3,5),F(3,4))]
    priorB=[(F(2,5),F(3,4)),(F(4,5),F(1,4))]
    rowA,rowB=mixed_binomial(priorA,2),mixed_binomial(priorB,2)
    assert rowA==rowB==[F(7,25),F(11,25),F(7,25)]
    thirdA,thirdB=mixed_binomial(priorA,3),mixed_binomial(priorB,3)
    assert thirdA[0]==F(41,250) and thirdB[0]==F(22,125)
    assert thirdB[0]-thirdA[0]==F(3,250)
    assert thirdA[0]/rowA[0]==F(41,70) and thirdB[0]/rowB[0]==F(22,35)
    counts['posterior_alias_checks']=4
    assert ALPHA*ALPHA+ALPHA==Q5(F(1))
    source_rows=[]
    for a in (1,9,37):
        for m in (3,11,64,128):
            source=[grade_beta(a,m,j) for j in range(m+1)]
            assert min(source)>0 and sum(source,F())==1;counts['source_mass_checks']+=1
            assert sum((j*q for j,q in enumerate(source)),F())==m*(1-R(a+8)/R(a));counts['source_mean_checks']+=1
            if m<=11:
                for j,q in enumerate(source):
                    assert q==grade_shift(a,m,j);counts['source_integral_crosschecks']+=1
            geometric=[ALPHA**(m+j)*comb(m,j) for j in range(m+1)]
            assert sum(geometric,Q5())==Q5(F(1))
            tv=sum(((asq(q)-b).absolute() for q,b in zip(source,geometric)),Q5())*F(1,2)
            eta=F(1,10)
            assert (ALPHA*F(1,4)-eta).sign()>0
            bound=asq(1)-(asq(1)+ALPHA)*(4*eta/R(a))-F(1,2*m*eta*eta)
            assert (tv-bound).sign()>=0;counts['source_tv_bounds']+=1
            source_rows.append({'a':a,'m':m,'TV':tv.encode(),'GT9_lower':bound.encode(),
                                'lower_nonvacuous':bound.sign()>0})
    native_rows=[]
    for m in (16,64,128):
        a=8*m-7; source=[grade_beta(a,m,j) for j in range(m+1)]
        assert min(source)>0 and sum(source,F())==1;counts['source_mass_checks']+=1
        tv=sum(((asq(q)-ALPHA**(m+j)*comb(m,j)).absolute() for j,q in enumerate(source)),Q5())*F(1,2)
        bound=asq(1)-(asq(1)+ALPHA)*F(4,m)-(asq(2)+ALPHA)*(2*(1-R(a+8)/R(a)))
        assert (tv-bound).sign()>=0;counts['source_tv_bounds']+=1
        target=ALPHA**2*F(m,2);threshold=0
        while (asq(threshold)-target).sign()<0:threshold+=1
        exponential=asq(1)-(asq(1)-ALPHA**2*F(1,2))**m*2**(threshold-1)-F(2,3)**threshold*R(4*m-7)/R(8*m-7)
        assert (tv-exponential).sign()>=0;counts['source_tv_bounds']+=1
        native_rows.append({'a':a,'m':m,'TV':tv.encode(),'GT10b_lower':bound.encode(),
                            'GT10c_lower':exponential.encode(),'threshold':threshold,
                            'lower_nonvacuous':bound.sign()>0,'exponential_lower_nonvacuous':exponential.sign()>0})
    previous,current=0,1
    for k in range(1,65):
        signed=asq(-previous)+ALPHA*current
        assert signed==ALPHA**k*((-1)**(k-1))
        counts['integer_return_checks']+=1
        previous,current=current,previous+current
    for a in (1,7):
        for m in range(13):
            for j in range(m+1):
                parent=grade_beta(a,m,j)/comb(m,j)
                child0=grade_beta(a,m+1,j)/comb(m+1,j)
                child1=grade_beta(a,m+1,j+1)/comb(m+1,j+1)
                assert parent==child0+child1
                counts['pascal_posterior_refinements']+=1
    projectivity=(R(9)/R(1),R(17)/R(9))
    assert projectivity[0]!=projectivity[1];counts['projectivity_rejections']=1
    # Exact leading source rational form, independent common denominator expansion.
    for a in range(1,101):
        assert R(a)==F(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5))
        counts['source_integral_crosschecks']+=1
    unwrapped0,unwrapped1=F(0),F(1)
    for n in range(1,33):
        old0,old1=unwrapped0,unwrapped1
        unwrapped0=16*old0+R(8*n-7);unwrapped1=16*old1+R(8*n-7)
        assert unwrapped1-unwrapped0==16**n
        assert unwrapped0%1==unwrapped1%1
        assert unwrapped0//1-16*(old0//1)==unwrapped1//1-16*(old1//1)
        counts['integer_seed_phase_carry_aliases']+=1
    proof_paths=[HERE.parent/'triangle_posterior/THEOREMS.md',HERE.parent/'triangle_geometry/THEOREMS.md']
    return {'status':'PASS','authority':'Exact finite Fraction and Q(sqrt5) checks; infinite claims paper-reviewed',
            'counts':counts,'ranks':rank_rows,'source_rows':source_rows,'native_rows':native_rows,
            'projectivity_zero_marginals':[str(x) for x in projectivity],
            'independence':'No front oracle or implementation imports; independent beta-product source integration and Gaussian-rational RREF',
            'proof_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in proof_paths},
            'oracle_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
