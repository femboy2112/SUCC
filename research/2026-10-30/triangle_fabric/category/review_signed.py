"""Complementary same-model review; fresh fixtures, symbolic linear algebra, Machin intervals.
Declared before execution: (N,M)=(2,5),(4,3),(6,2),(9,4); dyadic (3,4),(6,2).
Does not import the signed front's implementation.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,hashlib
import sympy as s

z=s.Symbol('z')

def r(n):return s.Rational(4,8*n-7)-s.Rational(2,8*n-4)-s.Rational(1,8*n-3)-s.Rational(1,8*n-2)

def mu(k,m):return sum((-1)**j*comb(m,j)*r(k+j+1) for j in range(m+1))

def integral(poly):
    p=s.Poly(poly,z)
    return sum(c*r(k[0]+1) for k,c in p.terms())

def filter_nm(n,m):
    gram=s.Matrix([[mu(i+j,m) for j in range(n)] for i in range(n)])
    coeff=gram.inv()*s.Matrix([-mu(i+n,m) for i in range(n)])
    p=z**n+sum(coeff[j]*z**j for j in range(n))
    f=s.Poly(1-(z-1)**m*p/(15**m*p.subs(z,16)),z)
    q,rem=s.div(f,s.Poly(16-z,z))
    assert rem.is_zero
    alpha=16*integral(q.as_expr())
    return p,f,q,alpha,gram.det()

def atan_interval(d,terms):
    v=sum((F((-1)**k,(2*k+1)*d**(2*k+1)) for k in range(terms)),F())
    nextterm=F((-1)**terms,(2*terms+1)*d**(2*terms+1))
    return min(v,v+nextterm),max(v,v+nextterm)

al,au=atan_interval(5,240);bl,bu=atan_interval(239,80)
pl,pu=16*al-4*bu,16*au-4*bl
rows=[]
for n,m in [(2,5),(4,3),(6,2),(9,4)]:
    p,f,q,alpha,det=filter_nm(n,m)
    assert det>0 and f.degree()==n+m and f.eval(16)==0
    for j in range(n):assert integral(z**j*(f.as_expr()-1))==0
    for j in range(m):assert s.diff(f.as_expr()-1,z,j).subs(z,1)==0
    assert s.diff(f.as_expr()-1,z,m).subs(z,1)!=0
    norm=integral((1-z)**m*p*p)
    L=F(norm/(15**m*p.subs(z,16)**2))
    a=F(alpha)
    errlo,errhi=(pl-a,pu-a) if m%2==0 else (a-pu,a-pl)
    assert 0<L<=errlo<errhi<=F(16,15)*L
    u=s.Rational(0)
    for k in range(1,21):
        rf=integral(z**(k-1)*f.as_expr())
        u=16*u+rf
        tail=integral(z**k*q.as_expr())
        assert u==16**(k-1)*alpha-tail
    rows.append({'N':n,'M':m,'minimal_degree':f.degree(),'gram_det_positive':True,'machin_error_interval_inside_norm_bound':True})

dyadics=[]
for n,m in [(3,4),(6,2)]:
    _,fl,_,lo,_=filter_nm(n,m);_,fh,_,hi,_=filter_nm(n,m+1)
    assert lo<hi
    power=0
    while True:
        numerator=s.floor(lo*2**power)+1
        d=s.Rational(numerator,2**power)
        if d<hi:break
        power+=1
    theta=(d-lo)/(hi-lo)
    f=s.Poly((1-theta)*fl.as_expr()+theta*fh.as_expr(),z)
    q,rem=s.div(f,s.Poly(16-z,z));assert rem.is_zero
    assert 16*integral(q.as_expr())==d
    onset=1+(power+3)//4
    for k in [onset,onset+1,onset+4]:
        assert (16**(k-1)*d).q==1
        tail=integral(z**k*q.as_expr());assert tail>0
    dyadics.append({'N':n,'M':m,'dyadic':str(d),'denominator_power':power,'onset':onset})

path=Path(__file__).parent
reviewed=path.parent/'signed'/'SIGNED_FABRIC.md'
result={'status':'PASS','review_authority':'complementary same-model review; no external proof authority','dossier_sha256':hashlib.sha256(reviewed.read_bytes()).hexdigest(),'sympy_version':s.__version__,'four_fresh_filters':rows,'two_fresh_dyadics':dyadics,'machin_terms':[240,80]}
with (path/'receipts'/'signed-review.json').open('x') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
