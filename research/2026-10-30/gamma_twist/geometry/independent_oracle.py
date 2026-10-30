"""Separate symbolic and Beta-integral oracle; imports no tested module.

SymPy polynomial integration, rational Beta rising products and positive
quadrature differ from the implementation's finite differences/Horner route.
Numerical special-function values are cross-checks, not interval authority.
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import sympy as s
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=80
u,y,z=s.symbols('u y z',real=True)
Q=4-2*s.exp(-3*y*u/8)-s.exp(-4*y*u/8)-s.exp(-5*y*u/8)
# Expanding directly before integrating avoids importing stored jet formulas.
normalized_density=s.series(s.exp(7*y*u/8)*Q/(15*y*u/8),u,0,3).removeO()
log_factor=s.series(s.log(z+(1-z)*s.exp(-y*u)),u,0,4).removeO()/u+(1-z)*y
likelihood_correction=s.series(s.exp(log_factor),u,0,3).removeO()
poly=s.Poly(s.series(normalized_density*likelihood_correction,u,0,3).removeO(),u)
d=2-z
moment=lambda p:sum(coef*s.factorial(k+1)/d**(k+2) for (k,),coef in s.Poly(s.expand(p),y).terms())
num=sum(moment(poly.coeff_monomial(u**j))*u**j for j in range(3))
den=s.simplify(num.subs(z,1))
series=s.series(num/den,u,0,3).removeO()
G0=s.factor(series.coeff(u,0));G1=s.factor(series.coeff(u,1));G2=s.factor(series.coeff(u,2))
assert s.simplify(G1+(z-1)*(511*z-302)/(120*(z-2)**4))==0
assert s.simplify(G2-(z-1)*(159826*z**3-46581*z*z-131748*z+35212)/(14400*(z-2)**6))==0
q=(3-s.sqrt(5))/2
alpha=s.radsimp(s.simplify(G1.subs(z,q)/(1-s.diff(G0,z).subs(z,q))))
beta=s.radsimp(s.simplify((s.diff(G0,z,2).subs(z,q)*alpha**2/2+s.diff(G1,z).subs(z,q)*alpha+G2.subs(z,q))/(1-s.diff(G0,z).subs(z,q))))
assert s.simplify(alpha-(-s.Rational(1231,240)+s.Rational(2671,1200)*s.sqrt(5)))==0
assert s.simplify(beta-(s.Rational(6031,80)-s.Rational(12139211,360000)*s.sqrt(5)))==0
beta_mutant=s.radsimp(s.simplify((q*q-q)/(160*(1-s.diff(G0,z).subs(z,q)))))
assert s.simplify(beta_mutant+s.sqrt(5)/800)==0

# Finite polynomial coefficients by Euler's beta integral, not finite differences.
auth={0:F(4),3:F(-2),4:F(-1),5:F(-1)}
def coeffs(label):
    c=dict(auth)
    if label!='authentic':
        order=4 if label=='quartic_e1' else 3
        eps=5 if label=='cubic_e5' else 1
        for j in range(order+1):c[j]=c.get(j,F(0))+eps*(-1)**j*math.comb(order,j)
    return c

def weights_beta(n,c):
    a=8*n-7;norm=sum(v/F(a+j) for j,v in c.items())
    out=[]
    for j in range(n+1):
        val=F(0)
        for shift,w in c.items():
            x=F(a+shift,8)+n-j
            rising=math.prod(x+k for k in range(j+1))
            val+=w*F(math.factorial(j),8)/rising
        out.append(F(math.comb(n,j))*val/norm)
    assert sum(out)==1 and all(v>0 for v in out)
    return out

raw=json.loads((ROOT/'receipts/exact-probe.log').read_text())
root_rows=[]
q_mp=(3-mp.sqrt(5))/2
a_mp=-mp.mpf(1231)/240+mp.mpf(2671)/1200*mp.sqrt(5)
b_mp=mp.mpf(6031)/80-mp.mpf(12139211)/360000*mp.sqrt(5)
for row in raw['root_enclosures']:
    n=row['n'];c=coeffs(row['source']);w=weights_beta(n,c)
    lo,hi=F(row['lower']),F(row['upper'])
    # Independent power-sum evaluation rather than Horner.
    direct=lambda x:sum((v*x**j for j,v in enumerate(w)),F(0))-x
    assert direct(lo)>=0 and direct(hi)<=0
    center=(mp.mpf(lo.numerator)/lo.denominator+mp.mpf(hi.numerator)/hi.denominator)/2
    second=n*n*(center-q_mp-a_mp/n)
    predicted=b_mp
    if row['source'].startswith('cubic'):
        predicted-=mp.sqrt(5)*(5 if row['source']=='cubic_e5' else 1)/800
    root_rows.append(dict(n=n,source=row['source'],scaled_second=mp.nstr(second,30),
                         predicted=mp.nstr(predicted,30),residual=mp.nstr(second-predicted,30)))

# Four numerical holdouts use a direct positive latent integral, not either
# rational polynomial construction. The actual source signs remain explicit.
quadratures=[]
for n,label in ((17,'authentic'),(31,'cubic_e1'),(53,'cubic_e5'),(89,'quartic_e1')):
    c=coeffs(label);a=8*n-7
    norm=sum(mp.mpf(v.numerator)/v.denominator/(a+j) for j,v in c.items())
    def density(t):
        x=t/(8*n)
        return mp.exp(-a*x)*sum((mp.mpf(v.numerator)/v.denominator)*mp.exp(-j*x) for j,v in c.items())/(8*n*norm)
    def integral_pgf(t):
        return mp.quad(lambda yy:density(yy)*(t+(1-t)*mp.exp(-yy/n))**n,[0,1,4,16,mp.inf])
    finite=mp.findroot(lambda zz:integral_pgf(zz)-zz,(q_mp-mp.mpf('.02'),q_mp))
    matched=next(rr for rr in raw['root_enclosures'] if rr['n']==n and rr['source']==label)
    low,high=F(matched['lower']),F(matched['upper'])
    assert mp.mpf(low.numerator)/low.denominator <= finite <= mp.mpf(high.numerator)/high.denominator
    quadratures.append(dict(n=n,source=label,root=mp.nstr(finite,45)))

# Gamma and Barnes reconstruction is a classical recovery, with explicit units.
cc=(4,-2,-1,-1);dd=(1,4,5,6)
logG=lambda t:sum(c*mp.loggamma(t+mp.mpf(d)/8) for c,d in zip(cc,dd))
logBarnes=lambda t:sum(c*mp.log(mp.barnesg(t+mp.mpf(d)/8)) for c,d in zip(cc,dd))
gamma_rows=[]
for tt in (mp.mpf(0),mp.mpf('0.25'),mp.mpf('1.5'),mp.mpf('7.25')):
    src=sum(mp.mpf(c)/(8*tt+d) for c,d in zip(cc,dd))
    derivative=mp.diff(lambda t:logG(t+1)-logG(t),tt)/8
    assert abs(src-derivative)<mp.mpf('1e-70')
    barnes_defect=logBarnes(tt+1)-logBarnes(tt)-logG(tt)
    assert abs(barnes_defect)<mp.mpf('1e-65')
    gamma_rows.append(dict(time=mp.nstr(tt),source=mp.nstr(src,40),
                           derivative_error=mp.nstr(derivative-src,6),barnes_error=mp.nstr(barnes_defect,6)))

# Three routes to the PREVIOUSLY KNOWN scalar budget: double series with exact
# finite bounds, positive integral, and digamma source mass.
R=lambda n:sum((F(c,8*n-8+d) for c,d in zip(cc,dd)),F(0))
N,J=128,20
double=sum((R(n+j)/16**j for n in range(1,N+1) for j in range(1,J+1)),F(0))
# Missing j>J at each n is < R(n+J+1)/(15*16**J), since R decreases.
trunc_error=sum((R(n+J+1)/F(15*16**J) for n in range(1,N+1)),F(0))
time_error=F(1,8*(8*N+1))
S=-sum(mp.mpf(c)*mp.digamma(mp.mpf(d)/8)/8 for c,d in zip(cc,dd))
B=(S-mp.pi)/15
smoothQ=lambda t:(t*t+2)*(t*t+2*t+2)/sum(t**k for k in range(8))
Bint=mp.quad(lambda t:t**8*smoothQ(t)/(16*(1-t**8/16)),[0,mp.mpf('.5'),1])
assert abs(B-Bint)<mp.mpf('1e-70')
assert mp.mpf(double.numerator)/double.denominator < B < mp.mpf((double+trunc_error+time_error).numerator)/(double+trunc_error+time_error).denominator

# Algebraic periodic gauge controls: agreement of arbitrarily many finite
# integer jets still does not fix the fractional cocycle representative.
t=s.symbols('t',real=True)
gauge=[]
for m in (1,2,3,5):
    g=s.sin(s.pi*t)**(2*m)
    assert all(s.diff(g,t,j).subs(t,0)==0 for j in range(2*m))
    assert s.simplify(s.expand_trig(g.subs(t,t+1))-g)==0
    assert g.subs(t,s.Rational(1,2))==1
    gauge.append(dict(order=2*m,integer_derivatives_zero_through=2*m-1,half_time_log_gauge='epsilon'))

payload=dict(status='PASS',authority='symbolic/exact checks plus labeled numerical cross-checks',
             symbolic_G1=str(G1),symbolic_G2=str(G2),root_alpha=str(s.expand(alpha)),
             root_beta=str(s.expand(beta)),cubic_root_beta_difference=str(beta_mutant),
             root_rows=root_rows,positive_integral_root_holdouts=quadratures,
             gamma_barnes_recovery=gamma_rows,periodic_gauge_controls=gauge,
             recovered_green_budget=dict(N=N,J=J,double_lower=str(double),
                double_upper=str(double+trunc_error+time_error),digamma=mp.nstr(B,65),
                positive_integral=mp.nstr(Bint,65)),
             versions=dict(sympy=s.__version__,mpmath=mp.__version__))
print(json.dumps(payload,indent=2))
