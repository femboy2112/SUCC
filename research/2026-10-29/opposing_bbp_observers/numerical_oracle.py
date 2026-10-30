"""Independent high-precision numerical holdouts, NOT proof certificates."""
import json
import mpmath as mp
from pathlib import Path

mp.mp.dps=105
C=[4,-2,-1,-1]; SHIFTS=[0,3,4,5]
lam=(mp.sqrt(5)-1)/2
R=lambda a:sum(mp.mpf(c)/(a+j) for c,j in zip(C,SHIFTS))
Q=lambda x:4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)

def g_base(a,d):
 return sum(mp.mpf(c)*R(2*a+j)*mp.exp(-(a+j)*abs(d)) for c,j in zip(C,SHIFTS))

def pair_pdf(a,t,d):return mp.exp(-t*d)*g_base(a,abs(d))/(R(a+t)*R(a-t))

def single_O(a):
 logs=sum(mp.mpf(c)*mp.log1p(mp.mpf(j)/a)/(a+j) for c,j in zip(C,SHIFTS))
 return -mp.euler - logs/R(a) - R(a*(1+lam))/R(a)

def discord_O(a):
 terms=sum(mp.mpf(c)*R(2*a+j)*(mp.log1p(mp.mpf(j)/a)/(a+j)+1/(a+j+lam*a)) for c,j in zip(C,SHIFTS))
 return -mp.euler -2*terms/R(a)**2

report={"status":"PASS numerical holdouts; not interval proofs","mpmath_dps":mp.mp.dps,"source_checks":[],"oily_checks":[]}
for a,t in ((mp.mpf(1),mp.mpf('0.2')),(mp.mpf(7),mp.mpf('1.7'))):
 for d in (mp.mpf('0.13'),mp.mpf('.7'),mp.mpf('2.1')):
  base=mp.quad(lambda y:mp.exp(-2*a*y)*Q(y+d)*Q(y),[0,1,2,5,mp.inf])
  symbolic=g_base(a,d)
  assert mp.almosteq(mp.exp(-a*d)*base,symbolic,rel_eps=mp.mpf('1e-65'))
  pplus=pair_pdf(a,t,d);pminus=pair_pdf(a,t,-d)
  assert mp.almosteq(pplus/pminus,mp.exp(-2*t*d),rel_eps=mp.mpf('1e-65'))
  report['source_checks'].append({'a':str(a),'t':str(t),'d':str(d),'ratio':mp.nstr(pplus/pminus,22),'carrier_density':mp.nstr(pplus,22)})
for a in (mp.mpf(7),mp.mpf(43),mp.mpf(400),mp.mpf(4000)):
 S=single_O(a);W=discord_O(a); gap=S-W
 C_S=-mp.mpf(59)/30*(1+2*lam**4)
 C_W=-mp.mpf(59)/30*(mp.mpf(3)/2-lam**3)
 C_gap=mp.mpf(59)/30*(4*lam-mp.mpf(5)/2)
 report['oily_checks'].append({'a':str(a), 'single':mp.nstr(S,25),'disagreement':mp.nstr(W,25),
    'gap':mp.nstr(gap,25), 'gap_limit_lambda':mp.nstr(lam,25),
    'scaled_single_defect':mp.nstr(a*(S-(lam-mp.euler)),22),'single_coefficient':mp.nstr(C_S,22),
    'scaled_disagreement_defect':mp.nstr(a*(W+mp.euler),22),'disagreement_coefficient':mp.nstr(C_W,22),
    'scaled_gap_defect':mp.nstr(a*(gap-lam),22),'gap_coefficient':mp.nstr(C_gap,22)})
# Independently evaluate the direct integral of |Delta| from the positive
# Laplace kernel at small a; compared with the closed four-pole moments.
a=mp.mpf(3);p=lambda z:2*g_base(a,z)/R(a)**2
S_direct=mp.quad(lambda z:p(z)*(mp.log(a*z)-mp.exp(-lam*a*z)),[0,mp.mpf('.02'),mp.mpf('.2'),1,3,9,mp.inf])
assert abs(S_direct-discord_O(a))<mp.mpf('1e-67')
report['direct_disagreement_integral']={'a':str(a),'value':mp.nstr(S_direct,33),'closed':mp.nstr(discord_O(a),33)}
# Golden calibration, Γ2 rate 1±λ
mean=2/(1+lam)-2/(1-lam)
positive=((1-lam**2)**2/4)*(1/(1+lam)+1/(1+lam)**2)
assert abs(mean+4)<mp.mpf('1e-90')
assert abs(positive-lam**2/4)<mp.mpf('1e-90')
for a in (mp.mpf(1),mp.mpf(13),mp.mpf(1000)):
 h=R(a)/mp.sqrt(R(a*(1+lam))*R(a*(1-lam)))
 assert lam<h<mp.sqrt(lam*(1-(a*lam/(a+5))**2))
report['golden']={'lambda':mp.nstr(lam,45),'mean_a_delta_limit':mp.nstr(mean,45),
 'P_delta_positive_limit':mp.nstr(positive,45),'overlap_limit':mp.nstr(lam,45),
 'oily_single_limit':mp.nstr(lam-mp.euler,45), 'oily_disagreement_limit':mp.nstr(-mp.euler,45)}
Path('/mnt/data/succ_opposing_observers/numerical_receipt.json').write_text(json.dumps(report,indent=2))
print('INDEPENDENT_NUMERICAL_PASS',len(report['source_checks']),'kernel tests',len(report['oily_checks']),'oily holdouts', 'plus direct log integration')
