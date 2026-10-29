import sys,json,time
sys.path.insert(0,'/tmp')
from lonely_finite_probe import config,audit,F
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix,csr_matrix

def chain(v,s,d):
 arcs=[]
 for i,w in enumerate(v):
  for k in range(-2,int(w)+3):arcs.append(((k-s[i]-d)/w,(k-s[i]+d)/w,i,k))
 arcs.sort();first=max((x for x in arcs if x[0]<=1e-10 and x[1]>=0),key=lambda x:x[1]);target=(first[0]+1,first[1]+1,first[2],first[3]+v[first[2]])
 out=[first];right=first[1];j=0
 while right<target[0]-1e-10:
  best=None
  while j<len(arcs) and arcs[j][0]<=right+1e-10:
   a=arcs[j]
   if a[1]>right+1e-12 and (best is None or a[1]>best[1]):best=a
   j+=1
  if best is None:return None
  out.append(best);right=best[1]
 out.append(target);return out

def lp(v,s,d,rng,randomize=False):
 ch=chain(v,s,d)
 if ch is None:return None
 m=len(v);rows=lil_matrix((2*(len(ch)-1),m+1));bs=[]
 for h,(x,y) in enumerate(zip(ch,ch[1:])):
  _,_,i,k=x;_,_,j,l=y;a=v[i];b=v[j]
  for z,sgn in enumerate([1,-1]):
   rows[2*h+z,i]+=sgn*b;rows[2*h+z,j]-=sgn*a;rows[2*h+z,-1]=-a-b;bs.append(sgn*(b*k-a*l))
 c=np.zeros(m+1)
 if randomize:c[:-1]=rng.normal(size=m)
 else:c[-1]=1
 radiusbound=(d,d) if randomize else(0,d)
 sol=linprog(c,A_ub=csr_matrix(rows),b_ub=bs,bounds=[(float(x)-.1,float(x)+.1) for x in s]+[radiusbound],method='highs')
 if not sol.success:return None
 return sol.x[:-1]%1,sol.x[-1],len(ch)

N=int(sys.argv[1]);steps=int(sys.argv[2]);seed=int(sys.argv[3]);rng=np.random.default_rng(seed)
vs=config(N);v=np.array([v for v,s in vs]);s=np.array([float(s) for v,s in vs]);d=float(F(1,N+1));start=time.time()
for z in range(steps):
 p=lp(v,s,d,rng,True)
 if p is None:print(json.dumps({'step':z,'failure':'walkchain','N':N}),flush=True);break
 s,d,_=p
 p=lp(v,s,d,rng,False)
 if p is None:print(json.dumps({'step':z,'failure':'optchain','N':N}),flush=True);break
 s,d,cl=p
 if z%10==0 or d<1/(N+1)-1e-9:print(json.dumps({'step':z,'N':N,'delta':d,'chainlen':cl,'seconds':time.time()-start}),flush=True)
 if d<1/(N+1)-1e-9:
  data={'N':N,'v':v.tolist(),'s':s.tolist(),'delta':d,'seed':seed,'step':z}
  open('/tmp/lonely_candidate_'+str(N)+'.json','w').write(json.dumps(data));break
