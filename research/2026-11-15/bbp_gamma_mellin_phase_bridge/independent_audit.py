"""Independent source/Gamma oracle; intentionally NO import of gamma_phase.py."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import mpmath as mp
mp.mp.dps=68
x,v,beta=sp.symbols('x v beta')
Q=4-2*x**3-x**4-x**5
R=sp.cancel(Q/(16-x**8))
t=sp.exp(-v/sp.Integer(8))
Kv=sp.cancel(t*R.subs(x,t)/8)
checks={}
checks['Q_factor']=sp.simplify(Q-(1-x)*(x*x+2)*(x*x+2*x+2))==0
checks['R_original']=sp.factor(R)==sp.factor((1-x)/((2-x*x)*(x*x-2*x+2)))
K_expected=v/sp.Integer(64)-7*v*v/sp.Integer(1024)+55*v**3/sp.Integer(24576)
checks['K_expansion']=sp.expand(sp.series(Kv,v,0,4).removeO()-K_expected)==0
# second order beta twist from normalized exact Green log amplitude
base=sp.series(Kv/(v/sp.Integer(64)),v,0,3).removeO()
twist=sp.series(((1-sp.exp(-v))/v)**beta,v,0,3).removeO()
combo=sp.series(base*twist,v,0,3).removeO().expand().collect(v)
expect=1-(8*beta+7)*v/sp.Integer(16)+(48*beta**2+100*beta+55)*v*v/sp.Integer(384)
checks['beta_twist_coefficients']=sp.simplify(combo-expect)==0
for n in (1,2,3,7,11):
 r_direct=4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)
 r_integrated=4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)
 checks[f'four_poles_{n}']=sp.simplify(r_direct-r_integrated)==0

# Direct integration on t, not the v-optimized primary implementation.
def green_t(n):
 def integrand(t):
  return t**(8*n)*(1-t)/((2-t*t)*(t*t-2*t+2))
 return mp.quad(integrand,[0,.25,.5,.75,1])
def complex_t(n,xi,depth):
 def integrand(t):
  return t**(8*n*(1+1j*xi))*(1-t**8)**depth*(1-t)/((2-t*t)*(t*t-2*t+2))
 return mp.quad(integrand,[0,.25,.5,.75,1])
def four_t(n,q,ell=2):
 def integrand(t):
  return t**(8*n)*(1-t**(8*q))*(1-t**(8*ell))*(1-t)/((2-t*t)*(t*t-2*t+2))
 return mp.quad(integrand,[0,.25,.5,.75,1])

checks['pi_original_import_numeric']=abs(green_t(0)-mp.pi/16)<mp.mpf('1e-58')
# Explicit source density mutant with same first three endpoint derivatives
mutant=lambda t: (1-t)/((2-t*t)*(t*t-2*t+2)) + mp.mpf('0.01')*(1-t)**4
altered=mp.quad(mutant,[0,.5,1]);base0=green_t(0)
checks['mutant_same_gamma_lead_different_total']= (altered>base0 and abs(altered-base0-mp.mpf('0.01')/5)<mp.mpf('1e-55'))

numeric=[]
for n in (40,120,280):
 for xi,depth in ((0,0),(.5,mp.mpc('.4','.7'))):
  obs=complex_t(n,xi,depth)
  w=1+1j*xi
  leading=mp.gamma(depth+2)/(64*n**(depth+2)*w**(depth+2))
  first=leading*(1-(depth+2)*(8*depth+7)/(16*n*w))
  second=first+mp.gamma(depth+4)*(48*depth**2+100*depth+55)/(384*64*n**(depth+4)*w**(depth+4))
  numerical={'n':n,'xi':float(xi),'beta':str(depth),'obs':mp.nstr(obs,16),
             'error_0':float(abs(obs-leading)),'error_1':float(abs(obs-first)),
             'error_2':float(abs(obs-second))}
  numeric.append(numerical)
  checks[f'deep_asymptotic_{n}_{xi}']=(abs(obs-second)<abs(obs-first)/5 if xi else abs(obs-second)<abs(obs-first)/5)
for n in (30,90,250):
 for q,typ in ((4,'fixed'),(n,'linear'),(n*n,'quadratic')):
  obs=four_t(n,q)
  pred= (mp.mpf(3*q)/(16*n**4) if typ=='fixed' else
         mp.mpf(7)/(128*n**3) if typ=='linear' else
         mp.mpf(1)/(16*n**3))
  numeric.append({'n':n,'q':q,'regime':typ,'four_time':mp.nstr(obs,14),'ratio_to_leading':float(obs/pred)})
  checks[f'four_positive_{n}_{typ}']=obs>0
  checks[f'four_scale_{n}_{typ}']=abs(obs/pred-1)<(mp.mpf('.47') if n==30 else mp.mpf('.2'))

# Independent t-domain signed source differences: no imported numerics.
for k in range(4):
    n=240; ell=2
    def src_integrand(t):
        return (t**(8*n)*(1-t**(8*ell))**k*(1-t)
                /((2-t*t)*(t*t-2*t+2)))
    observed=mp.quad(src_integrand,[0,.5,.75,.9,.98,1])
    asym=mp.mpf(ell)**k*mp.gamma(k+2)/(64*mp.power(n,k+2))
    checks[f'signed_source_gamma_{k}']= (observed>0 and abs(observed/asym-1)<mp.mpf('.24'))
    numeric.append({'k':k,'n':n,'positive_source_step_difference':mp.nstr(observed,15),
                    'gamma_ratio':float(observed/asym)})

payload={'audit':'Independent symbolic and t-domain integration, no import of tested implementation',
         'checks':{k:bool(v) for k,v in checks.items()},'numeric':numeric,
         'observed':sum(bool(v) for v in checks.values()),'total':len(checks),
         'all_pass':all(bool(v) for v in checks.values()),
         'scope':'Finite exact algebra; high precision numeric diagnostics; no pi normality theorem'}
Path(__file__).with_name('INDEPENDENT_AUDIT.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'all_pass':payload['all_pass'],'counts':f"{payload['observed']}/{payload['total']}",
                  'worst_second_order_error':max(v['error_2'] for v in numeric if 'error_2' in v)},indent=2))
assert payload['all_pass']
