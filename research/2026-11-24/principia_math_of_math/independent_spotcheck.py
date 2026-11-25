from random import Random
import sympy as sp
from fractions import Fraction
from observational_succ.principia_semantic_core import compile_null_height, verify_null_height, multiply
from observational_succ.principia_knowledge_volume import make_source, analyze
rng=Random(20261124)
z=sp.Symbol('z'); nchecks=0
for _ in range(360):
 b=rng.choice([2,3,10,16]);p=rng.choice([2,3,5,7]);m=rng.randrange(4);d=rng.randrange(5)
 # Nonzero integral quotient polynomial; constant/random leading coefficient selected independently
 q=[rng.randint(-4,4) for j in range(rng.randrange(1,4))]
 if q[-1]==0:q[-1]=1
 f=(0,p**m)
 for j in range(1,d+1):f=multiply(f,(-1,b**j))
 f=multiply(f,q)
 cert=compile_null_height(f,radix=b,prime=p,valuation=m,depth=d)
 check=verify_null_height(cert)
 poly=sp.Poly.from_list(list(reversed(f)),z,domain=sp.ZZ)
 for j in range(1,d+1): assert poly.eval(sp.Rational(1,b**j))==0
 assert check['leading_abs']==abs(int(poly.LC()))
 assert check['capacity_lower_bound']==p**m*b**(d*(d+1)//2)
 nchecks+=1

kchecks=0
for _ in range(100):
 dim=rng.randrange(2,5)
 pvec=[rng.randint(-3,3) for _ in range(dim)]
 if not any(pvec):pvec[0]=1
 act=[[rng.randrange(-2,3) for _ in range(dim)] for _ in range(dim)]
 src=make_source([pvec], {'a':act})
 profile=analyze(src,3)
 P=sp.Matrix([pvec]);A=sp.Matrix(act)
 expect=[]
 for i in range(4):
  rows=P
  for j in range(1,i+1): rows=rows.col_join(P*(A**j))
  expect.append(rows.rank())
 assert tuple(expect)==profile.dimensions, (expect,profile.dimensions)
 kchecks+=1
print('INDEPENDENT_SYMPY_SPOTCHECK_PASSED',nchecks,'polynomial cases',kchecks,'knowledge-rank cases')

from observational_succ.principia_formal_group import inverse_formal_log
for p,d in [(2,8),(2,12),(3,10),(5,6)]:
 u=inverse_formal_log(p,d)
 U=sum(sp.Rational(a.numerator,a.denominator)*z**i for i,a in enumerate(u) if a)
 L=U
 j=1
 while p**(2*j)<=d:
  L+=sp.Rational(1,p**j)*U**(p**(2*j));j+=1
 pol=sp.Poly(L,z,domain='QQ')
 for k in range(d+1):
  assert pol.nth(k)==(1 if k==1 else 0),(p,d,k,pol.nth(k))
print('INDEPENDENT_SYMPY_FORMAL_INVERSE_PASSED',4,'truncated inverse models')
