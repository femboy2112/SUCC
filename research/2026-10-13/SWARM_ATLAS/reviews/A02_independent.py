import itertools,json,sys
from pathlib import Path
checks=0
n=4;pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
for counts in itertools.product(range(3),repeat=len(pairs)):
 arrows={(i,j):[] for i in range(n) for j in range(n)}
 for i in range(n):arrows[i,i]=[()]
 edges={i:[] for i in range(n)}
 for (i,j),k in zip(pairs,counts):edges[i]+=[(j,(i,j,l)) for l in range(k)]
 for span in range(1,n):
  for i in range(n-span):
   j=i+span
   arrows[i,j]=[(label,)+tail for dst,label in edges[i] if dst<=j for tail in arrows[dst,j]]
 for selected in itertools.product(range(2),repeat=n):
  probe=[i for i,k in enumerate(selected) if k]
  criterion=all(any(arrows[j,x] for j in probe) for x in range(n) if any(len(arrows[x,y])>=2 for y in range(n)))
  faithful=True
  for x in range(n):
   for y in range(n):
    contexts=[u for j in probe for u in arrows[j,x]]
    images={tuple(u+f for u in contexts) for f in arrows[x,y]}
    faithful &= len(images)==len(arrows[x,y])
  assert faithful==criterion
  checks+=1
r={'reviewer':'/root distinct from /root/a02','graph_vertices':4,'edge_multiplicities':[0,1,2],'graphs':3**6,'probe_subsets_per_graph':16,'faithfulness_checks':checks,'all_checks_passed':True,'source_independence':'fresh exact four-vertex free histories; no original helper imports','proof_status':'paper derivation review; finite tests do not certify universal theorem'}
t=json.dumps(r,indent=2)+'\n'
if len(sys.argv)>1:Path(sys.argv[1]).write_text(t)
print(t)
