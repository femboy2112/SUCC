from fractions import Fraction as F
from collections import defaultdict
import json,time

def config(N):
 d=F(1,N+1); R={8,32,192}; S={12,24,48,96}
 return [(v,((1+d)/2 if v in S else -d if v in {16,64} else F(0))%1) for v in range(2,2*N+1,2) if v not in R]+[(3,F(1,4)),(9,F(1,4))]
def audit(vs,d):
 events=defaultdict(list)
 for i,(v,s) in enumerate(vs):
  for k in range(-1,v+2):
   a=max(F(0),(k-s-d)/v);b=min(F(1),(k-s+d)/v)
   if a<b:events[a].append((i,1));events[b].append((i,-1))
 active=set();last=F(0);unique=[F(0)]*len(vs);gaps=[]
 for t,es in sorted(events.items()):
  if t>last:
   if not active:gaps.append((last,t))
   if len(active)==1:unique[next(iter(active))]+=t-last
  for i,sgn in es:
   if sgn==1:active.add(i)
   else:active.discard(i)
  last=t
 return gaps,unique
if __name__=='__main__':
 for N in [96,95,94,93,90,80,60,40,20]:
  vs=config(N);d=F(1,N+1);g,u=audit(vs,d)
  print(json.dumps({'N':N,'n':len(vs),'d':str(d),'gaps':len(g),'gaplen':str(sum((b-a for a,b in g),F(0))),'redundant':[vs[i][0] for i,x in enumerate(u) if x==0],'least':[(vs[i][0],str(u[i])) for i in sorted(range(len(vs)),key=lambda i:u[i])[:8]]}),flush=True)
