"""Independent hostile check of neighboring cylinder/Stoneham dossier."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

HERE=Path(__file__).parent

def norm(x):x=x%1;return min(x,1-x)

def main():
 # Lawful wider class: arbitrary error t_n in [0,16/(8n+1)^3].
 # The proof only needs these bounds; these are not asserted BBP Green tails.
 tests=0
 starts=[F(a,4096) for a in range(4096)]
 starts += [(F(j,15)+sgn*F(k,100000))%1 for j in range(15) for sgn in (-1,1) for k in (0,1,19,31,390)]
 for x in starts:
  for A,L in ((2,7),(19,4)):
   ys=[];z=x
   for j in range(L): ys.append(z);z=16*z%1
   ds=[int(16*y) for y in ys];C=sum(a!=b for a,b in zip(ds,ds[1:]))
   for mode in (0,1):
    K=sum(norm(15*y+(F(16,(8*(A+j)+1)**3) if (j+mode)%2 else F()))>F(1,20) for j,y in enumerate(ys))
    assert C<=2*K and K<=2*C+2;tests+=1
 reverse=0
 for d in range(16):
  for L in (1,2,5,8):
   Q=16**(L+2);base=F(d*(Q-1),15*Q)
   for t in (F(),F(1,2),F(9999,10000)):
    y=base+t/Q
    for j in range(L):
     assert norm(15*y+F(16,(8*(2+j)+1)**3))<F(1,20)
     y=16*y%1;reverse+=1
 # Exact periodic rational orbit and h17 character alignment.
 x=F(1,255);phases=[]
 for n in range(1,101):
  phases.append(x);assert norm(15*x)==F(1,17)
  assert (17*x)%1==F(1,15);x=16*x%1
 assert len(set(phases))==2
 # Separate direct pulse construction / multiplicities, and algebraic grid bound.
 stages=[]
 for c in (3,5):
  x=F();pulses={c**p:p for p in range(1,5)};counts={}
  for n in range(c**4):
   if n: x=(16*x+(F(1,n) if n in pulses else 0))%1
   if n<c:continue
   p=1
   while c**(p+1)<=n:p+=1
   counts.setdefault(p,{})[x]=counts.setdefault(p,{}).get(x,0)+1
  for p,cs in counts.items():
   q=c**(p-1);M=c*(c-1)
   assert set(cs)=={F(1+c*j,c**p) for j in range(q)}
   assert all(v==M for v in cs.values());stages.append({'c':c,'p':p,'q':q,'multiplicity':M})
 gridchecks=0
 for q in (1,2,3,5,9,25,81,125):
  for H in range(2,258):
   k=(H-1)//q
   # Fourier maximum occurs with all cos=1; this is an exact upper bound.
   exactmax=q*(1+sum((2*(1-F(l*q,H)) for l in range(1,k+1)),F()))
   assert exactmax<=q+H;gridchecks+=1
 path=HERE.parent/'cylinders/CYLINDERS_AND_STONEHAM.md'
 print(json.dumps({'status':'PASS','reviewed_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'transition_configurations':tests,'constant_word_positions':reverse,'periodic01_positions':100,
 'exact_grid_inequalities':gridchecks,'stages':stages,
 'scope':'same-model independent finite implementation plus paper audit; no external referee'},indent=2))

if __name__=='__main__':main()
