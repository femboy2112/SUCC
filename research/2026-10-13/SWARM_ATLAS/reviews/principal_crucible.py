"""Independent incidence/matrix crucible; imports no investigator/repo helper."""
import itertools,json,sys
from pathlib import Path
checks=0
# An incidence multiplicity presents the canonical comparison to a relation.
# Powerset logic detects coverage; constant-singleton witnesses detect multiplicity.
for nx,ny in [(0,0),(1,1),(2,1),(2,2),(3,2)]:
 for m in itertools.product(range(3),repeat=nx*ny):
  for relation in itertools.product(range(2),repeat=nx*ny):
   if any(k and not r for k,r in zip(m,relation)):continue
   all_truth=True
   for support in itertools.product(range(2),repeat=nx):
    lhs=tuple(any(relation[x*ny+y] and support[x] for x in range(nx)) for y in range(ny))
    rhs=tuple(any(m[x*ny+y] and support[x] for x in range(nx)) for y in range(ny))
    all_truth &= lhs==rhs
   coverage=all(bool(k)==bool(r) for k,r in zip(m,relation))
   assert all_truth==coverage
   # Unique source/preimage per eligible pair is necessary and sufficient for
   # the ACTUAL canonical witness map to be bijective, not just an abstract bijection.
   witness_iso=all(k==r for k,r in zip(m,relation))
   assert (coverage and all(k<=1 for k in m))==witness_iso
   checks+=1
ring_checks=0
for n in range(2,9):
 points=list(itertools.product(range(n),repeat=2))
 def act(g,p):
  a,b,c=g;y,z=p;return ((y+b)%n,(z+c+a*y)%n)
 forms=list(itertools.product(range(n),repeat=3))
 # Distinct group parameters distinguished by just two fixed observer probes.
 signatures={(act(g,(0,0)),act(g,(1,0))) for g in forms}
 assert len(signatures)==n**3
 for g in forms:
  # Lossy quotient retains action law, not original x identity.
  for h in [(1,0,0),(0,1,0),(0,0,1)]:
   a,b,c=g;d,e,f=h;product=((a+d)%n,(b+e)%n,(c+f+a*e)%n)
   for p in [(0,0),(1,0),(0,1)]:assert act(product,p)==act(g,act(h,p));ring_checks+=1
 assert act((1,0,0),act((0,1,0),(0,0)))!=act((0,1,0),act((1,0,0),(0,0)))
 assert all(act((0,1,0),p)!=p for p in points)
result={'reviewer':'/root, distinct from A01/F41 investigators','reasoner_independence':'separate native reasoner; same model/provider and repository lineage','implementation_independence':'integer incidence multiplicities and affine normal-form matrices; no original probe/helper imports','A01_incidence_presentations':checks,'F41_ring_composition_checks':ring_checks,'rings':list(range(2,9)),'all_checks_passed':True,'scope':'bounded hostile regression; acceptance relies on explicit universal proof review'}
text=json.dumps(result,indent=2)+'\n'
if len(sys.argv)>1:Path(sys.argv[1]).write_text(text)
print(text)
