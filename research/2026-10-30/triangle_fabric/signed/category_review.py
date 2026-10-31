"""Complementary same-model review, independent exact algebra for CA01-04."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,sys,hashlib
import sympy as s

root=Path(__file__).resolve().parents[4]
dossier=root/'research/2026-10-30/triangle_fabric/category/CATEGORICAL_ARROWS.md'
counts={}
# CA01: no import of category implementation.
rows=[]
for p in (Q(1,7),Q(3,8),Q(7,11)):
 t=1-p
 for length in range(1,10):
  a=[Q(0)]*(length+1); b=a[:]
  for bits in product((0,1),repeat=length):
   n=sum(bits); prob=p**n*t**(length-n); correction=Q(0)
   if length>=3:
    pattern={(0,1,0):1,(0,1,1):-1,(1,0,0):-1,(1,0,1):1}
    sign=pattern.get(bits[:3],0); extra=sum(bits[3:])
    correction=Q(sign,2)*p**(2+extra)*t**(2+length-3-extra)
   assert prob+correction>=0
   a[n]+=prob; b[n]+=prob+correction
  assert a==b and sum(a)==1
  rows.append([str(p),length])
counts['fresh_full_grade_marginals']=len(rows)
# Fresh support graph dimensions, directly constructed in SymPy.
dims=[]
for m,d in ((1,1),(2,1),(3,2),(2,5),(5,2),(6,3),(3,7),(7,4),(8,2),(4,6)):
 edges=[(i,k) for i in range(m+1) for k in range(i,i+d+1)]
 inc=s.Matrix([[int(i==j) for i,k in edges] for j in range(m+1)]+[[int(k==j) for i,k in edges] for j in range(m+d+1)])
 dim=len(edges)-inc.rank(); assert dim==m*(d-1)
 cyc=[]
 for i in range(m):
  for k in range(i+1,i+d):
   z={(i,k):1,(i+1,k+1):1,(i,k+1):-1,(i+1,k):-1}
   cyc.append(s.Matrix([z.get(e,0) for e in edges]))
 if cyc:
  mat=s.Matrix.hstack(*cyc); assert mat.rank()==dim and inc*mat==s.zeros(inc.rows,dim)
 dims.append([m,d,dim])
counts['fresh_cycle_dimensions']=len(dims)
# CA03 independent symbolic Q(sqrt5) design / rational kernel.
m=d=4; edges=[(i,k) for i in range(m+1) for k in range(i,i+d+1)]
lam=(s.sqrt(5)-1)/2
H=lambda n:sum((s.Rational(1,j) for j in range(1,n+1)),s.S(0))
cycles=[]
for i in range(m):
 for k in range(i+1,i+d):
  z={(i,k):1,(i+1,k+1):1,(i,k+1):-1,(i+1,k):-1};cycles.append(z)
columns=[]
for c in cycles:
 vals=[sum(v*H(i)*H(k) for (i,k),v in c.items()),
       sum(v*H(i)*lam**k for (i,k),v in c.items()),
       sum(v*lam**i*H(k) for (i,k),v in c.items()),
       sum(v*lam**(i+k) for (i,k),v in c.items())]
 col=[s.expand(vals[0])]
 for v in vals[1:]:
  v=s.expand(v); col.extend([v.coeff(s.sqrt(5),0),v.coeff(s.sqrt(5),1)])
 columns.append(s.Matrix(col))
design=s.Matrix.hstack(*columns); null=design.nullspace()
assert null and design.rank()<=7
counts['triangle_design_rank']=design.rank();counts['triangle_null_dimension']=len(null)
v=null[0]; Z={e:sum(v[j]*cycles[j].get(e,0) for j in range(len(cycles))) for e in edges}
for f in (lambda i:1,H,lambda i:lam**i):
 for g in (lambda i:1,H,lambda i:lam**i):
  assert s.simplify(sum(value*f(i)*g(k) for (i,k),value in Z.items()))==0
counts['full_triangle_products']=9
# Independent exact Cauchy fixtures with nonconsecutive rational marks.
for r in (2,3,5):
 xs=[s.Rational(j*j,3) for j in range(r)]; pars=[s.Rational(2*j+1,7) for j in range(r)]
 ys=[s.Rational(j*j+j,5) for j in range(r+1)]; bs=[s.Rational(3*j+2,11) for j in range(r+1)]
 C=s.Matrix([[1/(a+x) for x in xs] for a in pars]);D=s.Matrix([[1/(b+y) for y in ys] for b in bs])
 J=s.Matrix([[s.Rational((i+1)*(k+2)+1,97) for k in range(r+1)] for i in range(r)])
 assert C.inv()*(C*J*D.T)*D.inv().T==J
counts['fresh_cauchy_reconstructions']=3
out=Path(sys.argv[1]);assert not out.exists()
out.write_text(json.dumps(dict(status='PASS',reviewed_dossier=str(dossier.relative_to(root)),
 reviewed_sha256=hashlib.sha256(dossier.read_bytes()).hexdigest(),checks=counts,
 cycle_rows=dims,authority='complementary same-model, not external referee',
 python=sys.version,sympy=s.__version__),indent=2)+'\n')
print(json.dumps(counts))
