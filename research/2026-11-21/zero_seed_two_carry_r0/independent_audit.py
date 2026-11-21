"""Standalone independent formulas for the same finite two-carry assertions.

Does NOT import production or new two_carry_seam module. Mathematical
assumptions are shared, so not a blind independent referee.
"""
import json
from fractions import Fraction as F
from math import comb
from hashlib import sha256
import sympy as sp

count=0
notes={}
def check(cond,label):
 global count
 count+=1
 if not cond:raise AssertionError(label)

def r(n):
 return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def source_t_integral(n,k):
 # integral t^(8n-8) Q(t)(1-t^8)^k dt; calculate by monomials
 return sum((F((-1)**j*comb(k,j)*coef,8*(n+j)-7+a)
   for j in range(k+1) for a,coef in [(0,4),(3,-2),(4,-1),(5,-1)]),F())

def independent_phi(n):
 total=F()
 for j in range(1,n+1):
  for coeff,offset in [(4,7),(-2,4),(-1,3),(-1,2)]:
   denom=8*j-offset
   total+=F(coeff*pow(16,n-j,denom),denom)
   total%=1
 return total

def rtail(n):return r(n+1)/15

z=sp.symbols('z')
Q=4-2*z**3-z**4-z**5
check(sp.expand((1-z)*(z**2+2)*(z**2+2*z+2)-Q)==0,'H factor')
for n in range(1,131):
 check(r(n)>0,f'positive {n}')
 if n>1:check(r(n)<r(n-1),f'decreasing {n}')
 check(r(n)<F(47,15*n*n) if n>1 else r(n)==F(47,15),'budget')
 for k in range(5):
  v=source_t_integral(n,k)
  check(v>0,f'moment positivity {n,k}')
  w=sum((F((-1)**j*comb(k,j))*r(n+j) for j in range(k+1)),F())
  check(v==w,f'finite difference {n,k}')

hankel={}
for n in (1,2,5):
 for size in (1,2,3,4):
  M=sp.Matrix([[sp.Rational(r(n+i+j).numerator,r(n+i+j).denominator) for j in range(size)] for i in range(size)])
  determinant=M.det(method='domain-ge')
  check(determinant>0,f'Hankel minor {n,size}')
  hankel[f'{n}:{size}']=str(determinant)

selected=[1,2,3,11,47,127,256,521,1023,2048,4095]
phis={}
for n in selected:
 ph=independent_phi(n)
 check(0<=ph<1,f'phase range {n}')
 check(ph+rtail(n)<1,f'delta0 {n}')
 check(ph.numerator>=0,f'numerator {n}')
 phis[n]=ph

# Independent exact source replay using rational compact single-expression r(n).
phi=F();dig=[];source_events=[];potential_tail=[]
for n in range(1,4097):
 a=r(n)
 new=16*phi+a
 old_floor=(16*phi).__floor__()
 c=new.__floor__()
 if n>=2 and c>old_floor:source_events.append(n)
 phi=new-c
 if phi+rtail(n)>=1:potential_tail.append(n)
 dig.append(format(c,'X'))
 if n in phis:check(phi==phis[n],f'independent modular check {n}')
check(not source_events,'no source-kick until 4096')
check(not potential_tail,'no possible completion carry until 4096')
check(''.join(dig[:12])=='3243F6A8885A','bbp hex prefix')

# Construct independently a rational changed seed realizing the two carry types.
n=21
s0=F()
for j in range(1,n):s0=16*s0+r(j)
target=(1-r(n)/2)/16
s=(target-s0)/16**(n-1)
check(16**(n-1)*s+s0==target,'seed e calibrated')
phi=(16*target+r(n))%1
check(phi==r(n)/2,'forced kick reset')
check(phi+rtail(n)<1,'forced kick excludes delta')

m=22
s0=F()
for j in range(1,m+1):s0=16*s0+r(j)
small=r(m+1)/32
seed=(-small-s0)/16**m
check((s0+16**m*seed)%1==1-small,'delta calibrated')
check(1-small+r(m+1)/16>1,'delta positive lower')

for p in (7,11,19,29,43,79):
 j=(p*p+7)//8
 m=F(2,(p*p+1)*(p*p+2))
 def residue(v):return v.numerator*pow(v.denominator,-1,p)%p
 check(residue(p*p*r(j))==4%p,f'orig prime mark {p}')
 check(residue(p*p*r(j)+m)==5%p,f'mutant prime mark {p}')

notes=dict(checks=count, source_events=source_events,potential_tail=potential_tail,
           source_clock_sample=selected, finite_replay=4096,
           replay_sha256=sha256(''.join(dig).encode('ascii')).hexdigest(),
           precision='exact rational; symbolic determinants',
           math_status='finite independent implementation of declared source, not independent proof of infinity')
open('independent_audit_receipt.json','w').write(json.dumps(notes,indent=2)+'\n')
print(json.dumps(notes,indent=2))
