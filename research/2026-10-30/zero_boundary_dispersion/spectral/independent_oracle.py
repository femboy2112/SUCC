"""Separate direct rational prefix, polynomials, and high precision oracle.

Does not import spectral_probe. Numeric trigonometry is a cross-check only;
the production rational intervals carry the finite certificate authority.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp
import sympy as sp
mp.mp.dps=100


def exact_source(n):
    ds=(8*n-7,8*n-4,8*n-3,8*n-2)
    den=1
    for d in ds:
        den*=d
    num=4*(den//ds[0])-2*(den//ds[1])-den//ds[2]-den//ds[3]
    return F(num,den)


def from_prefix(n):
    return sum((16**(n-j)*exact_source(j) for j in range(1,n+1)),F(0))


def mm(x):
    return mp.mpf(x.numerator)/x.denominator


def reduced_exp(x):
    x=x%1
    return mp.exp(2j*mp.pi*mm(x))


receipt=json.loads(Path('probe_receipt.json').read_text())
cache={}
checks=[]
for row in receipt['rows']:
    A,N,k=row['A'],row['N'],row['k']
    key=(A,N,k)
    if key not in cache:
        # Independent closed prefix for the first point, then source recursion
        # in Q/Z avoids the primary implementation's growing real rational lift.
        x=from_prefix(A)%1
        phases=[]
        deltas=[]
        for n in range(A,A+N):
            phases.append(x)
            nxt=(16*x+exact_source(n+1))%1
            deltas.append((nxt-x)%1)
            x=nxt
        total=sum((reduced_exp(k*x) for x in phases),mp.mpc(0))/N
        energies={int(h):sum((1-mp.re(reduced_exp(int(h)*x)) for x in deltas))/N
                  for h in receipt['rows'][next(i for i,r in enumerate(receipt['rows']) if (r['A'],r['N'],r['k'],r['J'])==(A,N,k,5))]['mean_energy_intervals']}
        cache[key]=(abs(total)**2,energies)
    sq,es=cache[key]
    lo,hi=map(F,row['phase_mean_squared_interval'])
    assert mm(lo)<=sq<=mm(hi)
    for h,bounds in row['mean_energy_intervals'].items():
        lo,hi=map(F,bounds)
        assert mm(lo)<=es[int(h)]<=mm(hi)
    checks.append({"A":A,"N":N,"k":k,"J":row['J'],"mean_squared":mp.nstr(sq,80),"pass":True})

# Derive the source sign and bound with symbolic rational differences.
n,a=sp.symbols('n a',positive=True)
r=lambda z:4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
gap=sp.factor(240/(8*n+1)**3-(r(n+1)-r(n+2)))
num,den=sp.fraction(gap)
assert all(c>0 for c in sp.Poly(num,n).all_coeffs())
weights=[sp.Rational(c*d,1)/(a+d) for d,c in ((3,2),(4,1),(5,1))]
marks=[sp.cancel(w/sum(weights)) for w in weights]
mark_derivative_checks=[]
for i,d in enumerate((3,4,5)):
    formula=marks[i]*(sum(marks[j]/(a+e) for j,e in enumerate((3,4,5)))-1/(a+d))
    assert sp.cancel(sp.diff(marks[i],a)-formula)==0
    mark_derivative_checks.append(str(sp.factor(sp.diff(marks[i],a))))

# Exact polynomial Gram identity for arbitrary complex variables represented
# by separate real/imaginary indeterminates (no BBP dependence).
gram_checks=[]
for J in (2,3,4,5):
    xs=sp.symbols(f'x0:{J}'); ys=sp.symbols(f'y0:{J}')
    lhs=sum(xs)**2+sum(ys)**2
    rhs=sum(x*x+y*y for x,y in zip(xs,ys))
    rhs+=2*sum(xs[i]*xs[j]+ys[i]*ys[j] for i in range(J) for j in range(i+1,J))
    assert sp.expand(lhs-rhs)==0
    gram_checks.append(J)

out={"status":"PASS separate implementation; not independent referee",
     "numeric_interval_rows":checks,"symbolic_source_gap_numerator":str(sp.expand(num)),
     "symbolic_source_gap_denominator":str(sp.factor(den)),
     "symbolic_mark_derivatives":mark_derivative_checks,"exact_gram_sizes":gram_checks}
Path('independent_oracle_receipt.json').write_text(json.dumps(out,indent=2))
print(f"PASS: {len(checks)} finite interval rows, symbolic original-source inequality, 3 mark derivatives, 4 Gram polynomial identities")
