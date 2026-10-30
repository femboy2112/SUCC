"""Separate Gram-Schmidt/positive-source/SymPy oracle; never imports filters.py."""
from fractions import Fraction as Rat
from pathlib import Path
from math import comb
import json,sys
import sympy as s


def positive_source(k):
    a=8*k-7
    return Rat(6,a*(a+3))+Rat(4,a*(a+4))+Rat(5,a*(a+5))


def moments(m,upto):
    return [sum((Rat((-1)**j*comb(m,j))*positive_source(i+j+1)
                 for j in range(m+1)),Rat(0)) for i in range(upto+1)]


def inner(a,b,mu):
    return sum((x*y*mu[i+j] for i,x in enumerate(a) for j,y in enumerate(b)),Rat(0))


def gram_schmidt(n,m):
    mu=moments(m,2*n)
    basis=[]
    for degree in range(n+1):
        monomial=[Rat(0)]*degree+[Rat(1)]
        p=monomial[:]
        for prev in basis:
            ratio=inner(monomial,prev,mu)/inner(prev,prev,mu)
            for j,c in enumerate(prev): p[j]-=ratio*c
        basis.append(p)
    return basis[-1]


def rational(x): return Rat(str(x))

def poly(coeff,z): return sum((s.Rational(c.numerator,c.denominator)*z**i for i,c in enumerate(coeff)),s.S(0))

def source(f,k): return sum((c*positive_source(k+j) for j,c in enumerate(f)),Rat(0))

report=json.loads(Path(sys.argv[1]).read_text())
z=s.Symbol('z')
counts=dict(orthogonal_polynomials=0,sturm_root_counts=0,source_prefix_checks=0,
            filter_divisions=0,direct_orbit_checks=0,dyadic_orbit_checks=0,
            first_omitted_norm_checks=0,jet_checks=0)
for row in report['cases']:
    n,m=row['N'],row['M']; p=gram_schmidt(n,m)
    assert list(map(str,p))==row['polynomial']; counts['orthogonal_polynomials']+=1
    sp=s.Poly(poly(p,z),z)
    assert sp.count_roots(0,1)==n; counts['sturm_root_counts']+=1
    f=s.expand(1-(z-1)**m*sp.as_expr()/(15**m*sp.eval(16)))
    assert s.expand(f-poly(list(map(rational,row['filter'])),z))==0
    quotient,remainder=s.div(f,16-z,z)
    assert remainder==0; counts['filter_divisions']+=1
    coeff=[rational(s.Poly(f,z).nth(i)) for i in range(s.degree(f,z)+1)]
    b=[rational(s.Poly(quotient,z).nth(i)) for i in range(s.degree(quotient,z)+1)]
    q0=source(b,1)
    for k in range(1,n+1):
        assert source(coeff,k)==positive_source(k); counts['source_prefix_checks']+=1
    norm=inner(p,p,moments(m,2*n))
    omitted=-(-1)**m*norm/(15**m*rational(sp.eval(16)))
    assert source(coeff,n+1)-positive_source(n+1)==omitted
    counts['first_omitted_norm_checks']+=1
    # Independent direct weighted source expansion, not iterative recurrence.
    for k in (0,1,2,7,19,41,53):
        un=sum((16**(k-j)*source(coeff,j) for j in range(1,k+1)),Rat(0))
        assert un==16**k*q0-source(b,k+1); counts['direct_orbit_checks']+=1
    # Source moments at infinity derive from literal shifted pole list.
    for j in range(m+2):
        jet=sum((c*a*Rat((-8*i-d)**j) for i,c in enumerate(coeff)
                 for d,a in ((0,4),(3,-2),(4,-1),(5,-1))),Rat(0))
        old=sum((Rat(a*(-d)**j) for d,a in ((0,4),(3,-2),(4,-1),(5,-1))),Rat(0))
        assert (jet==old)==(j<=m); counts['jet_checks']+=1
for row in report['dyadic']:
    coeff=list(map(rational,row['filter'])); f=poly(coeff,z)
    q,r=s.div(f,16-z,z); assert r==0
    b=[rational(s.Poly(q,z).nth(i)) for i in range(s.degree(q,z)+1)]
    alpha=16*source(b,1)
    assert alpha==rational(row['dyadic'])
    for k in range(row['onset'],row['onset']+17):
        un=sum((16**(k-j)*source(coeff,j) for j in range(1,k+1)),Rat(0))
        assert (16**(k-1)*alpha).denominator==1
        assert (un+source(b,k+1)).denominator==1
        counts['dyadic_orbit_checks']+=1
out=Path(sys.argv[2])
if out.exists(): raise FileExistsError(out)
out.write_text(json.dumps(dict(status='PASS',implementation='Gram-Schmidt, three-positive-term force, SymPy Sturm/division, direct weighted orbit',
    python=sys.version,sympy=s.__version__,checks=counts),indent=2)+'\n')
print(json.dumps(counts))
