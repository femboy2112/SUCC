"""Separate SymPy Gram--Schmidt/continued-fraction and analytic calibration.

Does not import resolvent.py. Numerical checks are not rounding certificates.
"""
import json
from pathlib import Path
from math import factorial
import sympy as sp
import mpmath as mp

mp.mp.dps=110
data=json.loads((Path(__file__).parent/'receipts/resolvent-probe.log').read_text())
by_d={int(row['d']):row for row in data['rows']}


def moment(k):
    a=sp.Integer(8*k+1)
    return (15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))


def ip(a,b,mu):
    return sum(x*y*mu[i+j] for i,x in enumerate(a) for j,y in enumerate(b))


def gram_cf(d):
    mu=[moment(k) for k in range(2*d+1)]
    polys=[];norms=[];diagonal=[]
    for j in range(d+1):
        p=[sp.Integer(0)]*j+[sp.Integer(1)]
        for old,h in zip(polys,norms):
            coeff=ip(p,old,mu)/h
            for k in range(len(old)):p[k]-=coeff*old[k]
        polys.append(p);norms.append(ip(p,p,mu))
        if j<d:diagonal.append(ip([0]+p,p,mu)/norms[-1])
    denominator=sp.Integer(16)-diagonal[-1]
    for j in reversed(range(d-1)):
        denominator=16-diagonal[j]-(norms[j+1]/norms[j])/denominator
    return sp.factor(mu[0]/denominator),polys[-1],norms[-1]


rows=[]
for d in (1,3,6,11,14,19):
    got,p,h=gram_cf(d);row=by_d[d]
    assert got==sp.Rational(row['center'])
    assert p==[sp.Rational(x) for x in row['polynomial']]
    assert h==sp.Rational(row['norm'])
    low=mp.mpf(str(sp.N(sp.Rational(row['lower']),105)))
    high=mp.mpf(str(sp.N(sp.Rational(row['upper']),105)))
    assert low<mp.pi/16<high
    rows.append({'d':d,'center_matches':'exact',
                 'actual_error':mp.nstr(mp.pi/16-mp.mpf(str(sp.N(got,105))),20),
                 'interval_width':mp.nstr(high-low,20),
                 'center_denominator_bits':int(sp.denom(got)).bit_length()})


def completed(s):
    return mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)


def theta_finite(s,M):
    out=1/(s*(s-1))
    for n in range(1,M+1):
        c=mp.pi*n*n
        out+=c**(-s/2)*mp.gammainc(s/2,c,mp.inf)
        out+=c**(-(1-s)/2)*mp.gammainc((1-s)/2,c,mp.inf)
    return out


def rational_theta_bound(M,K,ell):
    C=3*(M+1)**2;degree=K+ell
    return sp.Rational(4,2**(ell+C))*sum(
        sp.Rational(factorial(degree),factorial(degree-j)*C**(j+1))
        for j in range(degree+1))


theta=[]
points=[(-1,1),(2,1),(mp.mpc(mp.mpf(1)/3,2),1),
        (-3,2),(mp.mpc(mp.mpf(2)/7,mp.mpf(13)/7),2),
        (mp.mpc(mp.mpf(5)/4,-mp.mpf(7)/3),2)]
for s,K in points:
    for M in (1,2,3):
        for ell in (0,1,2):
            residual=abs(mp.diff(completed,s,ell)-mp.diff(lambda z:theta_finite(z,M),s,ell))
            bound=rational_theta_bound(M,K,ell)
            assert residual<mp.mpf(str(sp.N(bound,105)))
            theta.append({'s':str(s),'M':M,'derivative':ell,
                          'residual':mp.nstr(residual,14),'rational_bound':str(bound)})

# Prime-germ route: differentiate normalized negative germ; compare independent
# positive-exponent zeta log derivative and explicit prime-power cutoff.
X=10000
powers=[]
for p in sp.primerange(2,X+1):
    n=int(p)
    while n<=X:powers.append((n,int(p)));n*=int(p)
germ=[]
for k in range(1,6):
    total=mp.diff(lambda z:mp.log(mp.zeta(-1+z)/mp.zeta(-1)),0,k)
    arch=mp.diff(lambda z:z*mp.log(2*mp.pi)+mp.log(mp.cos(mp.pi*z/2))+mp.log(mp.gamma(2-z)),0,k)
    prime=mp.diff(lambda z:mp.log(mp.zeta(2-z)/mp.zeta(2)),0,k)
    assert abs(total-arch-prime)<mp.mpf('1e-95')
    partial=mp.fsum(mp.log(p)*mp.log(n)**(k-1)/n**2 for n,p in powers)
    tail=mp.fsum(mp.factorial(k)/mp.factorial(k-j)*mp.log(X)**(k-j) for j in range(k+1))/X
    assert 0<prime-partial<tail
    germ.append({'k':k,'corrected_derivative':mp.nstr(prime,30),
                 'prime_cutoff':X,'tail_bound':mp.nstr(tail,20),
                 'actual_cutoff_error':mp.nstr(prime-partial,20)})

# Different symbolic route to the jet annihilator: apply (z*d/dz)^k to
# z(1-z)^K, then evaluate at 1; no import/call of the binomial construction.
z=sp.Symbol('z');annihilators=[]
for K in (1,2,4,7,12):
    poly=z*(1-z)**K
    for k in range(K+1):
        value=sp.diff(poly,z,0).subs(z,1)
        assert value==(0 if k<K else (-1)**K*factorial(K))
        poly=sp.expand(z*sp.diff(poly,z))
    annihilators.append(K)

print(json.dumps({'status':'PASS','authority':'independent implementation, shared mathematical/model lineage',
 'sympy':sp.__version__,'mpmath':mp.__version__,'precision_dps':mp.mp.dps,
 'resolvent':rows,'theta_cases':theta,'prime_germ':germ,
 'symbolic_jet_annihilator_orders':annihilators},indent=2))
