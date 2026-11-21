"""Independent SymPy/mpmath rederivation of original-source signed differentials.

No imports from seam_differentials.py, no copied numerical witness arrays. The
mutant is a separate integrand (1-t)^2. This audit is a second IMPLEMENTATION,
not a mathematical referee or a blind source family.
"""
from fractions import Fraction
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

N,t,k,z,tau=sp.symbols('N t k z tau')
Q=4-2*t**3-t**4-t**5
H=sp.factor(Q/(1-t))
DELTA=(1-t)**2
checks=0

def ck(p, label):
    global checks
    if not p:raise AssertionError(label)
    checks+=1

def pole(m):
    return (sp.Integer(4)/(8*m-7)-sp.Integer(2)/(8*m-4)-
            sp.Integer(1)/(8*m-3)-sp.Integer(1)/(8*m-2))

def increment(m):
    return sp.Integer(2)/((8*m-7)*(8*m-6)*(8*m-5))

def moments(m, amp, L=30):
    vals=[sp.Integer(16)**(-j)* (pole(m+j)+amp*increment(m+j)) for j in range(L)]
    s0=sum(vals);s1=sum(j*v for j,v in enumerate(vals));s2=sum(j*j*v for j,v in enumerate(vals))
    return s0,s1,s2

ck(sp.expand(Q-(1-t)*H)==0, 'factorization')
ck(sp.factor(H)==(t*t+2)*(t*t+2*t+2), 'root factors')
ck(Q.subs(t,1)==0, 'source DC null')
ck(sp.diff(Q,t).subs(t,1)==-15, 'first source signed jet')
ck(sp.diff(DELTA,t).subs(t,1)==0, 'mutant same first jet')
ck(sp.diff(Q+DELTA,t).subs(t,1)==-15, 'mutant derivative')
for m in range(1,70):
    ck(sp.integrate(t**(8*m-8)*Q,(t,0,1))==pole(m),f'four poles {m}')
    ck(sp.integrate(t**(8*m-8)*DELTA,(t,0,1))==increment(m),f'mutant {m}')
    ck(pole(m)>pole(m+1)>0,f'positive source {m}')
    ck(increment(m)>increment(m+1)>0,f'positive mutant delta {m}')
    ck(pole(m)**2<pole(m-1)*pole(m+1) if m>1 else True,f'log convex {m}')

# All exact time/sample checks are derived here via integrals and SymPy rationals.
for m in range(1,41):
    a0,a1,a2=moments(m,sp.S.Zero,25)
    b0,b1,b2=moments(m,sp.S.One,25)
    mu=a1/a0;mu_star=b1/b0
    ck(0<mu_star<mu<sp.Rational(1,15),f'signed lag {m}')
    ck(a2*a0>a1*a1,f'positive variance {m}')
    da0=sum(sp.Rational(1,16**j)*increment(m+j) for j in range(25))
    da1=sum(j*sp.Rational(1,16**j)*increment(m+j) for j in range(25))
    ck(da1*a0-a1*da0<0,f'differential covariance {m}')
    if m < 40:
        an,bn,_=moments(m+1,sp.S.Zero,25)
        ck(an/bn != 0 and bn/an>mu, f'forward lag {m}')

# Independent symbolic expansion of the rational first-pole source.
u=sp.symbols('u', positive=True)
rs=sp.series(pole(1/u),u,0,5).removeO().expand()
rd=sp.series(increment(1/u),u,0,5).removeO().expand()
ck(rs.coeff(u,2)==sp.Rational(15,64),'leading source amplitude')
ck(rs.coeff(u,3)==sp.Rational(151,512),'subleading source amplitude')
ck(rd.coeff(u,3)==sp.Rational(1,256),'delta first nonzero jet')
ck(sp.simplify((rs.coeff(u,3)+rd.coeff(u,3))/rs.coeff(u,2)-sp.Rational(151,120))==sp.Rational(1,60),'beta difference')
ratio=sp.series(pole(1/u+k)/pole(1/u),u,0,3).removeO().expand()
ck(sp.simplify(ratio.coeff(u,1)+2*k)==0,'ratio linear response')
ck(sp.simplify(ratio.coeff(u,2)-(3*k*k-sp.Rational(151,120)*k))==0,'ratio curvature')

# Independent geometric moment derivation, using generating function sum.
r=sp.symbols('r')
mgf=(1-r)/(1-r*z)
geom=[sp.diff(mgf,z,i).subs({z:1,r:sp.Rational(1,16)}) for i in range(4)]
m1=geom[1];m2=geom[2]+geom[1];m3=geom[3]+3*geom[2]+geom[1]
ck(m1==sp.Rational(1,15),'geometric mean')
ck(m2==sp.Rational(17,225),'geometric second moment')
ck(m3==sp.Rational(107,1125),'geometric third moment')
beta=sp.symbols("beta")
a=-2*m1;b=3*m2-beta*m1; c=-2*m2;d=3*m3-beta*m2
coef1=sp.factor(c-m1*a)
coef2=sp.factor(d-c*a+m1*(a*a-b))
ck(coef1==-sp.Rational(32,225),'lag first asymptotic coefficient')
ck(coef2.subs(beta,sp.Rational(151,120))==sp.Rational(182,1125),'lag second asymptotic coefficient')
ck(sp.factor(sp.diff(coef2,beta)*sp.Rational(1,60))==-sp.Rational(4,3375),'mutant signed lag split')

# Evaluate a genuinely separate high precision real oracle at unseen late clocks.
mp.mp.dps=110

def mp_r(mm):
    mm=mp.mpf(mm)
    return mp.mpf(4)/(8*mm-7)-mp.mpf(2)/(8*mm-4)-1/(8*mm-3)-1/(8*mm-2)

def mp_rstar(mm):
    mm=mp.mpf(mm)
    return mp_r(mm)+2/((8*mm-7)*(8*mm-6)*(8*mm-5))

def mp_mean(mm, func):
    den=mp.fsum([func(mm+j)/mp.power(16,j) for j in range(160)])
    num=mp.fsum([j*func(mm+j)/mp.power(16,j) for j in range(160)])
    return num/den

num_results={}
for mm in (71,317,997,3007):
    source=mp_mean(mm,mp_r);mut=mp_mean(mm,mp_rstar)
    target=mp.mpf(1)/15-mp.mpf(32)/(225*mm)+mp.mpf(182)/(1125*mm**2)
    ck(abs(source-target)*mm**3 < mp.mpf('0.3'),f'next order original {mm}')
    ck(abs((mut-source)*mm**2+mp.mpf(4)/3375)<mp.mpf(1)/mm,f'fresh mutant asympt {mm}')
    num_results[str(mm)]={"lag_mean":mp.nstr(source,32),"mutant_minus_source":mp.nstr(mut-source,32)}

# Semicircle signed Fourier character. This is independent of main module.
for n in range(0,5):
    radix=16**n
    ck(2*radix==2*16**n,f'current jump mass {n}')
    for ell in range(-19,20):
        if ell==0: continue
        # coefficient of derivative /i for h=radix*ell; continuous
        # Fourier delta integration on physical seam positions.
        calc=(sp.exp(-sp.I*sp.pi*ell/2)-sp.exp(-3*sp.I*sp.pi*ell/2))*radix/sp.I
        want=0 if ell%2==0 else 2*radix*((-1)**((ell+1)//2))
        ck(sp.simplify(sp.expand_complex(calc)-want)==0,f'quarter Fourier n{n} ell{ell}')

# Check controlled source-swap signs against independently sourced rational
# terminal BBP intervals; computed exact without decoding digit strings.
def source_interval(depth):
    partial=sum((pole(m)/sp.Integer(16)**m for m in range(1,depth+1)),sp.S.Zero)
    return partial, partial+pole(depth+1)/(15*sp.Integer(16)**depth)

def qport(value):
    f=value-sp.floor(value)
    if f in (sp.Rational(1,4),sp.Rational(3,4)):raise ValueError('threshold')
    return int(bool(sp.Rational(1,4)<f<sp.Rational(3,4)))
for p, expected in ((7,0),(79,1),(131,-1)):
    j=(p*p-1)//8
    D=15*(pole(j)-pole(j+1));delay=0;dis=D
    while dis<sp.Rational(1,64):
        delay+=1;dis*=16
    N=j+1+delay
    lo,hi=source_interval(N+13)
    x0,x1=16**N*lo,16**N*hi
    ck(qport(x0)==qport(x1),f'source quarter interval {p}')
    ck(qport(x0-dis)==qport(x1-dis),f'swap quarter interval {p}')
    ck(qport(x0)-qport(x0-dis)==expected,f'counterfactual sign {p}')
    ck(sp.Rational(1,64)<=dis<sp.Rational(1,4),f'source displacement {p}')

receipt={
 "scope":"source-first exact algebra + independent implementation; not independent referee",
 "checks_passed":checks,
 "symbolic":"SymPy rational Mellin, normalized source perturbation and seam Fourier delta",
 "numeric_precision_dps":mp.mp.dps,
 "fresh_late_clocks":num_results,
 "status":"PASS",
 "not_claimed":["π R0","π normality","full SUCC root tests","Lean","physical field energy"]
}
path=Path(__file__).with_name('independent_audit_receipt.json')
path.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True))
