import numpy as np, cmath, math
from fractions import Fraction as F
p=[F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0)]
d=[F(0),F(8),F(4),F(4),F(0),F(0),F(-1),F(0)]
a=[(2*x+y)/4 for x,y in zip(p,d)]
r=[(2*x-y)/4 for x,y in zip(p,d)]
def src(n,w): return sum((c/F(8*(n-1)+j) for j,c in enumerate(w,1)),F())
def states(n):
 u=y=z=F()
 for i in range(1,n+1):
  u=16*u+src(i,p);y=16*y+src(i,a);z=16*z+src(i,r)
 assert u==y+z
 return u,y,z
def phase(q):return cmath.exp(2j*math.pi*float(q%1))
def state(N,angles={}):
 out=np.empty(1<<N,dtype=complex)
 for bits in range(1<<N):
  parity=sum(((bits>>j)&1)*((bits>>(j+1))&1) for j in range(N-1))%2
  ang=sum((t*(1-2*((bits>>j)&1)) for j,t in angles.items()),F())
  out[bits]=(-1)**parity * cmath.exp(-1j*math.pi*float(ang%2))/math.sqrt(1<<N)
 return out
def act(vec,N,ops):
 out=np.zeros_like(vec)
 for bits,v in enumerate(vec):
  bnew=bits;f=1+0j
  for i,op in ops.items():
   b=(bits>>i)&1
   if op=='P':
    if b==0: f=0;break
    f*=2;bnew^=1<<i
   elif op=='X':bnew^=1<<i
   elif op=='Z':f*=1 if b==0 else -1
  out[bnew]+=f*v
 return np.vdot(vec,out)
def prefix(vec,N,m):
 # x + 2^m * high bits
 return vec.reshape((1<<(N-m),1<<m)).T @ vec.reshape((1<<(N-m),1<<m)).conj()
def approx(a,b):assert abs(a-b)<2e-11, (a,b)
for N in (7,8,9):
 v=state(N)
 for m in range(1,N):
  rho=prefix(v,N,m);approx(np.trace(rho@rho).real,.5)
 for j in range(N):
  ops={j:'X'}
  if j:ops[j-1]='Z'
  if j+1<N:ops[j+1]='Z'
  approx(act(v,N,ops),1)
 for n in (2,5,11):
  u,y,z=states(n)
  for h in (1,3,-2):
   w=state(N,{0:h*y,2:h*z})
   approx(act(w,N,{0:'P',1:'Z'}),phase(h*y))
   approx(act(w,N,{0:'P',2:'P',3:'Z'}),phase(h*u))
   approx(act(w,N,{0:'P',2:'P',4:'P',5:'Z'}),phase(h*u))
 for m in range(1,5):
  angle={0:F(1,7),2:F(3,11)}
  e=prefix(state(m+1,angle),m+1,m)
  obs=prefix(state(N,angle),N,m)
  assert np.max(abs(e-obs))<1e-11,(N,m)
 print('N',N,'source group correlations, stabilizers, cuts, compatible prefix density: PASS')
for N in (7,8,9):
 theta=F(3,17)
 w=np.zeros(1<<N,dtype=complex);w[0]=2**-.5;w[-1]=-phase(theta)*2**-.5
 W=np.zeros(1<<(N+1),dtype=complex);W[0]=2**-.5;W[-1]=-phase(theta)*2**-.5
 assert abs(prefix(w,N,N)[0,-1])>.49
 assert abs(prefix(W,N+1,N)[0,-1])<1e-11
 print('GHZ_N coherence fails finite partial trace of GHZ_(N+1): PASS',N)
