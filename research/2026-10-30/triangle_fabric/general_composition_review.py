"""Complementary FC07 review: exact Hessian checks and numerical Frullani calibration.

No import of constants implementation. Quadrature is explicitly NOT an interval proof.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,sys
import mpmath as mp

base=Path(__file__).resolve().parent
source=base/'constants/CONSTANTS_AND_COMPOSITION.md'
checks=dict(pointwise_hessian=0,dirichlet_hessian=0,tilt_variance=0,log_variance=0)
# Dirichlet(2,...,2) expected Hessian, exact rational algebra.
for k in range(2,18):
 d=[Q(2*i-k+1) for i in range(k)]
 assert sum(d)==0
 diag=Q(3,k*(2*k+1)) # E w_i^2
 cross=Q(2,k*(2*k+1))
 expected=(sum(d[i]*d[i]*(Q(1,k)-diag) for i in range(k))-
 sum(d[i]*d[j]*cross for i in range(k) for j in range(k) if i!=j))
 assert expected==Q(2,2*k+1)*sum(x*x for x in d)
 checks['dirichlet_hessian']+=1
# Pointwise p_i p_j domination, including near-singular rates.
for k in (2,4,7,11):
 for a in (Q(1,100),Q(5,2),Q(61)):
  for case in range(5):
   g=[Q((i+1)*(case+2)+1,(i+case)%3+1) for i in range(k)]
   rates=[a+Q(5*((i*7+case*3)%17),16) for i in range(k)]
   w=[x/sum(g) for x in g]
   p=[g[i]/rates[i] for i in range(k)];p=[x/sum(p) for x in p]
   d=[Q((i+case)**2) for i in range(k)];mean=sum(d)/k;d=[x-mean for x in d]
   lhs=sum(p[i]*p[j]*(d[i]-d[j])**2 for i in range(k) for j in range(i+1,k))
   rhs=(a/(a+5))**2*sum(w[i]*w[j]*(d[i]-d[j])**2 for i in range(k) for j in range(i+1,k))
   assert lhs>=rhs;checks['pointwise_hessian']+=1
# Independent finite-rate variance check of the variational lower-bound step.
for a in (Q(1,11),Q(7,3),Q(101)):
 t=[Q(0),Q(2,3),Q(9,4),Q(5)];prob=[Q(1,7),Q(2,7),Q(3,7),Q(1,7)]
 tilted=[p/(a+x)**2 for p,x in zip(prob,t)];total=sum(tilted);tilted=[x/total for x in tilted]
 var=lambda weights:sum(p*x*x for p,x in zip(weights,t))-sum(p*x for p,x in zip(weights,t))**2
 assert min(p/q for p,q in zip(tilted,prob))>=(a/(a+5))**2
 assert var(tilted)>=(a/(a+5))**2*var(prob);checks['tilt_variance']+=1
# Numerical independent positive-source Frullani integrals. Reported only as calibration.
def force(x): return 6/(x*(x+3))+4/(x*(x+4))+5/(x*(x+5))
def rational(x): return mp.mpf(x.numerator)/x.denominator
rows=[]
for k in (2,4,7):
 for aq in (Q(1,2),Q(29,3),Q(211)):
  values=[]
  for precision in (70,100):
   mp.mp.dps=precision;a=rational(aq);ra=force(a);cut=mp.mpf(180)
   def integrand(v):
    L=force(a*(1+mp.exp(v)))/ra
    return -L*mp.expm1((k-1)*mp.log(L))
   integral=mp.quad(integrand,[-cut,-30,-10,0,10,30,cut])
   baseline=sum(mp.mpf(1)/j for j in range(1,2*k))-1
   values.append(integral-baseline)
  assert abs(values[0]-values[1])<mp.mpf('1e-60')
  bound=Q(k-1,2*k+1)*Q(1379,900)*aq**4/(aq+5)**6
  assert values[-1]>rational(bound)>0
  analytic_tail=2*(k-1)*mp.exp(-180)+15/(2*a*a*ra)*mp.exp(-360)
  rows.append(dict(k=k,a=str(aq),gap_100dps=mp.nstr(values[-1],70),
    lower_bound=str(bound),quadrature_tail_upper=mp.nstr(analytic_tail,10),
    precision_agreement='abs difference<1e-60; NOT a quadrature error certificate'))
report=dict(status='PASS',authority='complementary same-model review; exact finite Hessian/variance algebra; numerical Frullani calibration not universal proof',
 source_dossier=str(source.relative_to(base)),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 python=sys.version,mpmath=mp.__version__,exact_checks=checks,calibration=rows)
out=Path(sys.argv[1]);assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(exact_checks=checks,frullani_rows=len(rows),status='PASS')))
