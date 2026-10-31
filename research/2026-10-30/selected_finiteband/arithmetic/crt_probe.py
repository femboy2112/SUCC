"""Exact fresh joint-phase/alias controls; finite observations only."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib
from quadrature import source,prefix,primary
HERE=Path(__file__).parent

def dist(x):x=x%1;return min(x,1-x)
def order16(p):
 z=16%p;L=1
 while z!=1:z=z*16%p;L+=1
 return L

def main():
 primes=(1201,1213,1229,1237,1249,1277)
 assert all(p%4==1 and all(p%d for d in range(2,isqrt(p)+1)) for p in primes)
 u=prefix(600);rows=[]
 for p in primes:
  b=(p+7)//8 if p%8==1 else (p+3)//8;L=order16(p)
  ap=[primary(u[n],p) for n in range(b,b+L)]
  assert len(set(ap))==L
  for h in (1,3,7):
   full=[];restored=0;prime_slips=0;phase_strings=[]
   for j in range(L-1):
    n=b+j;a=ap[j+1]-ap[j]
    v=(u[n+1]-ap[j+1])-(u[n]-ap[j])
    x=h*(a+v);assert x==h*(u[n+1]-u[n])
    near=dist(x)<F(1,20);far=dist(h*a)>=F(1,20)
    full.append(not near);prime_slips+=far;restored+=far and near
    phase_strings.append(str(x%1))
   assert 2*sum(full)>=L-1
   rows.append({'p':p,'b':b,'L':L,'h':h,'eligible_L_ge_sqrt_p':L*L>=p,
                'full_slips':sum(full),'lag_count':L-1,'primary_slips':prime_slips,
                'primary_far_full_near':restored,
                'full_phase_sha256':hashlib.sha256('\n'.join(phase_strings).encode()).hexdigest()})
 controls=[]
 for label,cs,offsets in (
  ('authentic',(4,-2,-1,-1),(1,4,5,6)),
  ('wrong_ratio',(5,-2,-1,-1),(1,4,5,6)),
  ('same_ratio',(4,0,-1,0),(1,4,5,6)),
  ('rank_matched_ratio',(F(2),F(11,4),F(-1,2),F(-17,4)),(1,4,5,6)),
  ('seven_pole_null',(-8,8,4,8,2,2,-1),tuple(range(1,8)))):
  v=F();xs=[v]
  for n in range(1,258):
   v=16*v+sum((F(c,8*n-8+d) for c,d in zip(cs,offsets)),F());xs.append(v)
  slips=sum(dist(xs[n+1]-xs[n])>=F(1,20) for n in range(129,257))
  controls.append({'family':label,'A':129,'L':128,'slips':slips})
 assert controls[-1]['slips']==0
 A,B,M=80,120,144;s=-F(u[M].numerator//u[M].denominator,16**M)
 aliaschecks=0
 for p in (3,5,7,13,19,73,1201):
  for n in (1,A,B,M,M+1):
   assert primary(u[n]+16**n*s,p)==primary(u[n],p);aliaschecks+=1
 ds=[dist(u[n+1]-u[n]+15*16**n*s) for n in range(A,B)]
 bound=15*F(1,16**(M-B))*(1+F(1,(8*M+1)**2))+F(16,(8*A+1)**3)
 assert max(ds)<bound<F(1,20) and (16**M*s)%1==0
 print(json.dumps({'status':'PASS','scope':'finite rational observations; no uniform SC06 bound',
  'joint_rows':rows,'controls':controls,
  'dyadic_alias':{'A':A,'B':B,'M':M,'seed':str(s),'odd_primary_checks':aliaschecks,
                  'max_lag_distance':str(max(ds)),'source_derived_upper':str(bound)},
  'cancellations':{'p19_zero_times':list(range(10,17)),
                  'p19_return_n17':str(primary(u[17],19)), 'p73_n274':str(primary(u[274],73))}},indent=2))
 assert all(primary(u[n],19)==0 for n in range(10,17)) and primary(u[274],73)==0

if __name__=='__main__':main()
