"""Separate positive-integral route; numeric checks are not proof certificates."""
import json
from pathlib import Path
from fractions import Fraction
import mpmath as mp
import sympy as sp
mp.mp.dps=90

def mprational(s):
    q=Fraction(s)
    return mp.mpf(q.numerator)/q.denominator

def R(a):
    return 6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5))

def Rp(a):
    return sum(-c*(2*a+d)/(a*a*(a+d)**2) for c,d in ((6,3),(4,4),(5,5)))

def in_interval(x,pair):
    lo,hi=map(mprational,pair)
    assert lo<=x<=hi,(mp.nstr(x,65),pair)

root=Path(__file__).resolve().parent
record=json.loads((root/'probe_receipt.json').read_text())
rows=[]
for row in record['rows']:
    a=mprational(row['a']); norm=R(a)
    eb=mp.quad(lambda v:a*a*v*(Rp(a*(1+v))/norm)**2,[0,1,mp.inf])
    esb=mp.quad(lambda v:a*a*(Rp(a*(1+v))/norm)**2,[0,1,mp.inf])
    es=-2*a*Rp(a)/norm
    cov=esb-es*eb
    inc=mp.quad(lambda v:(R(a*(1+v))/norm)*(1-R(a*(1+v))/norm)/v,[0,1,mp.inf])
    in_interval(eb,row['EB'])
    in_interval(a*a*cov,row['scaled_covariance'])
    in_interval(a*a*(mp.mpf(1)/5-eb),row['scaled_proportion_gap'])
    in_interval(a*a*(inc-mp.mpf(5)/6),row['scaled_harmonic_gap'])
    lam=(mp.sqrt(5)-1)/2
    lap=R(a*(1+lam))/norm
    golden=(lap-lam**2)*(lam-lap)
    in_interval(golden,row['golden_positive_term'])
    rows.append({'a':row['a'],'EB':mp.nstr(eb,60),'covariance':mp.nstr(cov,60),
                 'log_increment':mp.nstr(inc,60),'status':'PASS'})

# Independent exact symbolic derivation of the interaction coefficients.
u=sp.symbols('u',positive=True)
b=u*(1-u); density=6*b
beta_mean=sp.integrate(b*density,(u,0,1))
beta_var=sp.integrate(b*b*density,(u,0,1))-beta_mean**2
log_mean=sp.integrate(sp.log(u)*density,(u,0,1))
log_cov=sp.integrate(b*sp.log(u)*density,(u,0,1))-beta_mean*log_mean
assert beta_mean==sp.Rational(1,5)
assert beta_var==sp.Rational(1,350)
assert log_mean==-sp.Rational(5,6)
assert log_cov==sp.Rational(1,100)
# Raw finite conditional law, using positive expm1 rather than pole differences.
def h(x):
    if not x:return mp.mpf(1)
    return (-2*mp.expm1(-3*x)-mp.expm1(-4*x)-mp.expm1(-5*x))/(15*x)
conditional=[]
for s in (mp.mpf(1)/7,mp.mpf(1),mp.mpf(3),mp.mpf(11),mp.mpf(37)):
    density=lambda u:6*u*(1-u)*h(s*u)*h(s*(1-u))
    norm=mp.quad(density,[0,mp.mpf('.5'),1])
    eb=mp.quad(lambda u:u*(1-u)*density(u),[0,mp.mpf('.5'),1])/norm
    inc=-mp.quad(lambda u:mp.log(u)*density(u),[0,mp.mpf('.5'),1])/norm
    K=mp.mpf(1379)/900*s*s*mp.exp(-10*s)
    assert mp.mpf(1)/5-eb>K/350
    assert inc-mp.mpf(5)/6>K/100
    conditional.append({'s':mp.nstr(s,30),'EB':mp.nstr(eb,60),
                        'log_increment':mp.nstr(inc,60),'status':'PASS'})
output={'status':'PASS','authority':'separate symbolic and high precision quadrature, shared model lineage',
        'mpmath':mp.__version__,'sympy':sp.__version__,'dps':mp.mp.dps,
        'rows':rows,'conditional_rows':conditional,
        'symbolic_beta_values':list(map(str,(beta_mean,beta_var,log_mean,log_cov)))}
path=root/'independent_receipt.json'
if path.exists():raise SystemExit('refusing to overwrite receipt')
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
