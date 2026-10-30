"""Exact complementary FC09 calibration, no imports from constants front."""
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
import json,hashlib,sys
base=Path(__file__).resolve().parent
p=base/'constants/CONSTANTS_AND_COMPOSITION.md'
t=s.Symbol('t')
rows=[]
for k in range(2,21):
 poly=sum(t**j for j in range(k-1,2*k-1))
 assert s.expand((t-t**k)-(t*t-t**(2*k))-t*(1-t)*(1-poly))==0
 assert s.Poly(poly-1,t).count_roots(0,1)==1
 rows.append(k)
lam=(s.sqrt(5)-1)/2
assert s.simplify(lam+lam**2-1)==0
R=lambda a:Q(6)/(a*(a+3))+Q(4)/(a*(a+4))+Q(5)/(a*(a+5))
positives=[]
for k in (4,6,9):
 for tq in (Q(1,2),Q(3,5)):
  for a in (Q(1,1000),Q(7,13),Q(99)):
   L=R(a/tq)/R(a)
   excess=L-L**k-tq**2+tq**(2*k)
   assert tq*tq<L<tq and excess>0
   positives.append(dict(k=k,t=str(tq),a=str(a),excess=str(excess)))
negatives=[]
for k,tq in ((4,Q(4,5)),(6,Q(7,8)),(9,Q(19,20))):
 a=Q(1,4096); L=R(a/tq)/R(a)
 endpoint=tq-tq**k-tq*tq+tq**(2*k)
 excess=L-L**k-tq*tq+tq**(2*k)
 assert endpoint<0 and excess<0
 negatives.append(dict(k=k,t=str(tq),eta=str(1/tq-1),a=str(a),endpoint=str(endpoint),excess=str(excess)))
out=Path(sys.argv[1]);assert not out.exists()
out.write_text(json.dumps(dict(status='PASS',dossier_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
 factorization_and_unique_root_cases=rows,positive_cases=positives,negative_cases=negatives,
 authority='exact finite calibration; all-a proof is reviewed in GENERAL_COMPOSITION_REVIEW.md',
 python=sys.version,sympy=s.__version__),indent=2)+'\n')
print(json.dumps(dict(factorizations=len(rows),unique_root_counts=len(rows),positive=len(positives),negative=len(negatives),status='PASS')))
