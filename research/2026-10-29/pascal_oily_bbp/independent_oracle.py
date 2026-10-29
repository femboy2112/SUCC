"""Independent symbolic/numerical oracle for Pascal/Oily rank bridge.
Does not import pascal_oily_probe.py; no π-normality claims.
"""
import json
from pathlib import Path
import sympy as s
import mpmath as mp

n=s.symbols('n', positive=True, integer=True)
A=s.symbols('a',positive=True)
z=s.symbols('z',real=True)
t=1-z

def R(a):
    return 4/a-2/(a+3)-1/(a+4)-1/(a+5)

def rn(N):
    return s.factor(R(8*N-7))

# A genuinely distinct symbolic derivation of source-specific positivity
# for PGF interior-branch onset (n-1)r(n)>n r(n+1) for n>=2.
P=s.factor((n-1)*rn(n)-n*rn(n+1))
num,den=s.fraction(P)
m=s.symbols('m',nonnegative=True,integer=True)
shiftpoly=s.Poly(s.expand((num/s.Integer(2)).subs(n,m+2)),m)
assert all(c>0 for c in shiftpoly.all_coeffs())
assert s.factor(rn(1)-s.Rational(47,15))==0

# Asymptotic test of normalized endpoint and first two moments,
# with Gamma(rank) distribution for the positive field.
q0=s.factor(rn(2*n)/rn(n))
coeff0=s.limit(n*(q0-s.Rational(1,4)),n,s.oo)
assert coeff0 == -s.Rational(151,960)

rank=s.symbols('r',positive=True)
# Independently expand source-renormalization and Pascal binomial log.
# Under Gamma(rank), source density correction at order n^-1 is
# -c/(8n)*(Y-rank) with c=59/30; n-step Bernoulli thinning expansion
# exp(-tY)*(1 + (-7*t*Y/8+t*(1-t)*Y**2/2)/n).
M0=1/(1+t)**rank
M1=rank/(1+t)**(rank+1)
M2=rank*(rank+1)/(1+t)**(rank+2)
C=s.factor(-s.Rational(7,8)*t*M1 + t*(1-t)*M2/2
   -s.Rational(59,240)*(M1-rank*M0))
Ctrg=s.factor(rank*t/(1+t)**(rank+2)
   *(-s.Rational(151,240)*(1+t)+(rank+1)*(1-t)/2))
assert s.simplify(C-Ctrg)==0
assert s.simplify(C.subs(rank,2)-t*(209-511*t)/(120*(1+t)**4))==0
assert s.simplify(C.subs({rank:2,z:0})+s.Rational(151,960))==0
assert s.simplify(C.subs({rank:4,z:0})+s.Rational(151,1920))==0

lam=(s.sqrt(5)-1)/2
qstar=s.simplify(lam**2)
assert s.simplify((2-qstar)**(-2)-qstar)==0
Cq=s.simplify(C.subs({rank:2,z:qstar}))
qshift=s.simplify(Cq/(1-2/(2-qstar)**3))
Oshift=s.simplify(-s.Rational(59,240)-qshift)
assert s.simplify(qshift-(-s.Rational(1231,240)+s.Rational(2671,1200)*s.sqrt(5)))==0
assert s.simplify(Oshift-(s.Rational(293,60)-s.Rational(2671,1200)*s.sqrt(5)))==0

# Finite source log expectation exact via four-pole Frullani combination,
# and finite fixed point computed *without* the tested probability code.
mp.mp.dps=75
lam_mp=(mp.sqrt(5)-1)/2
Omega=lam_mp-mp.euler

def force_int(k):
    a=8*k-7
    return s.Rational(4,a)-s.Rational(2,a+3)-s.Rational(1,a+4)-s.Rational(1,a+5)

def fixed_point(n):
    den=force_int(n)
    coefs=[force_int(n+k)/den for k in range(n+1)]
    def G(v):
        # Independent orientation E[(z+(1-z) exp(-8X))^n]
        return sum(mp.binomial(n,k)*v**(n-k)*(1-v)**k*
                   (mp.mpf(c.p)/c.q) for k,c in enumerate(coefs))
    return mp.findroot(lambda v:G(v)-v,(mp.mpf('.31'),mp.mpf('.40')))

def logmean(n):
    a=8*n-7
    poles=((0,4),(3,-2),(4,-1),(5,-1))
    num=sum(mp.mpf(c)*mp.log1p(mp.mpf(d)/a)/(a+d) for d,c in poles)
    r0=force_int(n)
    return -mp.euler-num/(mp.mpf(r0.p)/r0.q)

rows=[]
for N in (5,10,20,40,80):
    qt=fixed_point(N)
    le=logmean(N)
    Om=le-qt
    rows.append({'n':N,'finite_fixed':mp.nstr(qt,25),
                 'finite_logmean':mp.nstr(le,25),'Omega_n':mp.nstr(Om,25),
                 'scaled_Omega_defect':mp.nstr(N*(Om-Omega),20),
                 'predicted_Omega_defect':mp.nstr(Oshift.evalf(25),25)})

receipt={'source':'four signed BBP poles, U0=0 not changed',
         'positive_symbolic_shift_coeffs':list(map(str,shiftpoly.all_coeffs())),
         'q0_first_correction':str(coeff0),
         'rank2_pgf_correction':str(s.factor(C.subs(rank,2))),
         'rank4_pgf_correction':str(s.factor(C.subs(rank,4))),
         'fixed_q_shift':str(qshift),'Omega_shift':str(Oshift),
         'rank2_Omega_limit':mp.nstr(Omega,35),
         'held_out_numerical_rows':rows,
         'pi_normality_proved':False,'source_selected_saving_proved':False}
Path('/mnt/data/pascal_oily_moonshot/independent_receipt.json').write_text(
    json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
