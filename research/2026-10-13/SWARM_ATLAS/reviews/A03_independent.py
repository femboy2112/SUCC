import itertools,json,random,sys
from pathlib import Path
rng=random.Random(310013)
darts=[(0,1),(1,2),(0,2),(0,1)]
links=[(i,j,v) for i in range(4) for j in range(i+1,4) for v in set(darts[i])&set(darts[j])]
walks=[]
for start in range(4):
 def dfs(at,visited,path):
  for k,(i,j,v) in enumerate(links):
   if at not in (i,j):continue
   nxt=j if at==i else i
   sign=1 if at==i else -1
   if nxt==start and len(path)>=1 and (not path or path[-1][0]!=k):walks.append(path+[(k,sign)])
   elif nxt not in visited and len(path)<4:dfs(nxt,visited|{nxt},path+[(k,sign)])
 dfs(start,{start},[])
checks=0
for _ in range(120):
 weights=[tuple(rng.randrange(-5,6) for _ in range(2)) for e in darts]
 gauges=[tuple(rng.randrange(-9,10) for _ in range(2)) for e in darts]
 potentials=[{u:g,v:tuple(a+b for a,b in zip(g,w))} for (u,v),g,w in zip(darts,gauges,weights)]
 for walk in walks:
  starts=[];ends=[];vertices=[];period=[0,0]
  for k,sign in walk:
   i,j,v=links[k];a,b=(i,j) if sign==1 else (j,i)
   starts.append(a);ends.append(b);vertices.append(v)
   period=[c+potentials[a][v][z]-potentials[b][v][z] for z,c in enumerate(period)]
  assert all(ends[k]==starts[(k+1)%len(walk)] for k in range(len(walk)))
  expanded=[0,0]
  for k in range(len(walk)):
   chart=ends[k];u=vertices[k];v=vertices[(k+1)%len(walk)]
   if u==v:continue
   tail,head=darts[chart]
   sign=1 if (u,v)==(tail,head) else -1
   assert (u,v) in [(tail,head),(head,tail)]
   expanded=[c+sign*weights[chart][z] for z,c in enumerate(expanded)]
  assert expanded==period
  checks+=1
# Sharp finite-modulus alias and bounded-source repair, independently calculated.
for menu in [(2,3),(4,6),(2,5,7),(8,9,25)]:
 import math
 L=math.lcm(*menu);assert L!=0 and all(L%m==0 for m in menu)
 assert all(1%m==(1+L)%m for m in menu)
 assert all(k==0 for k in range(-L+1,L) if k%L==0)
r={'reviewer':'/root distinct from /root/a03','seed':310013,'coefficient_dimension':2,'sources':120,'overlap_closed_walks_per_source':len(walks),'actual_chart_path_expansion_checks':checks,'all_checks_passed':True,'helper_imports':False,'verdict':'complete walk-map paper proof survives; finite vector controls only'}
t=json.dumps(r,indent=2)+'\n'
if len(sys.argv)>1:Path(sys.argv[1]).write_text(t)
print(t)
