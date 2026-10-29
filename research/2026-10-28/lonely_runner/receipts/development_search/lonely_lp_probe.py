import sys
sys.path.insert(0,'/tmp')
from lonely_finite_probe import config,audit,F
import numpy as np
from scipy.optimize import linprog
import json,time

def chain(vs,d):
 arcs=[]
 for i,(v,s) in enumerate(vs):
  for k in range(-1,v+2):
   l=(k-s-d)/v;r=(k-s+d)/v
   arcs.append((l,r,i,k))
 arcs.sort(); first=max((x for x in arcs if x[0]<=0<=x[1]),key=lambda x:x[1]);target=(first[0]+1,first[1]+1,first[2],first[3]+vs[first[2]][0])
 out=[first];right=first[1];j=0
 while right<target[0]:
  cand=[]
  while j<len(arcs) and arcs[j][0]<=right:
   if arcs[j][1]>right:cand.append(arcs[j])
   j+=1
  if not cand:return None
  a=max(cand,key=lambda x:x[1]);out.append(a);right=a[1]
 out.append(target);return out

def solve(N):
 vs=config(N);d=F(1,N+1);ch=chain(vs,d)
 if not ch:return {'N':N,'nochain':True}
 m=len(vs);rows=[];bs=[]
 for x,y in zip(ch,ch[1:]):
  _,_,i,k=x;_,_,j,l=y;v=vs[i][0];w=vs[j][0]
  row=np.zeros(m+1);row[i]+=w;row[j]-=v;row[-1]=-v-w
  rows.append(row);bs.append(w*k-v*l)
  row=-row;row[-1]=-v-w;rows.append(row);bs.append(v*l-w*k)
 c=np.zeros(m+1);c[-1]=1
 sol=linprog(c,A_ub=rows,b_ub=bs,bounds=[(-2,2)]*m+[(0,float(d))],method='highs')
 if not sol.success:return {'N':N,'success':False,'message':sol.message}
 ds=F(float(sol.x[-1])).limit_denominator(10**9)
 sv=[(v,F(float(s)).limit_denominator(10**9)%1) for (v,_),s in zip(vs,sol.x)]
 gaps,u=audit(sv,ds)
 result={'N':N,'n':m,'chainlen':len(ch),'delta':str(ds),'bound':str(F(1,m+1)),'gaps':len(gaps),'ratio':float(ds/d)}
 if ds<F(1,m+1):
  result['config']=[(v,str(s)) for v,s in sv]
  if gaps:result['maxgap']=str(max(b-a for a,b in gaps))
 return result
for N in [94,93,92,90,80,60,40,20,18]:
 print(json.dumps(solve(N)),flush=True)
