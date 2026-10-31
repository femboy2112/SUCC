"""Separate symbolic/Stieltjes oracle: imports none of quadrature.py."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import sympy as s

HERE=Path(__file__).parent

def combined(n):
 return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def unrolled(n): return sum((16**(n-j)*combined(j) for j in range(1,n+1)),F())

def rat(x): return s.Rational(x)
def fraction(x): return F(int(s.numer(x)),int(s.denom(x)))

def main():
 z=s.symbols('z')
 Q=4-2*s.exp(-3*z/8)-s.exp(-z/2)-s.exp(-5*z/8)
 lap=s.exp(7*z/8)*Q/(8*z*(16*s.exp(z)-1))
 assert s.simplify(z*(16-s.exp(-z))*lap-s.exp(-z/8)*Q/8)==0
 expansion=s.series(lap,z,0,8).removeO().expand()
 mus=[s.expand(expansion).coeff(z,k)*(-1)**k*s.factorial(k) for k in range(7)]
 checks=[]; allrows=[]
 for name in ('quadrature-witnesses.json','fresh-quadrature-witnesses.json'):
  dat=json.loads((HERE/'receipts'/name).read_text());allrows+=dat['rows']
 for data in allrows:
  if data['status']!='EXACT_POSITIVE_CERTIFICATE': raise AssertionError('missing exact holdout')
  M,J=data['M'],data['J'];bs=list(map(rat,data['nodes']));ws=list(map(rat,data['weights']))
  matrix=s.Matrix([[16/(n-1+b)**2-1/(n+b)**2 for b in bs] for n in range(1,M+1)]
                  +[[b**k for b in bs] for k in range(J+1)])
  rhs=s.Matrix([rat(str(combined(n))) for n in range(1,M+1)]+mus[:J+1])
  solution=matrix.inv()*rhs
  assert list(solution)==ws and all(w>0 for w in ws)
  def g(n):return sum(w/(n+b)**2 for b,w in zip(bs,ws))
  for n in range(M+1): assert fraction(16**n*g(0)-g(n))==unrolled(n)
  assert fraction(16*g(0))==F(data['completed_constant'])
  # Exact Taylor-jet equality through order J+1 in the positive source kernel.
  for k in range(J+1): assert sum(w*b**k for w,b in zip(ws,bs))==mus[k]
  # The first excluded source time is a source discriminator in these witnesses.
  defect=fraction(16*g(M)-g(M+1))-combined(M+1)
  assert defect
  # Fixed rational four-pole family is determined by four native samples.
  checks.append({'M':M,'J':J,'nodes':len(bs),'exact_equations':M+J+1,
                 'next_source_defect':str(defect),'completed_denominator_bits':F(data['completed_constant']).denominator.bit_length()})
 crt=json.loads((HERE/'receipts/crt-fresh.json').read_text())
 uu=[F()]
 for n in range(1,601): uu.append(16*uu[-1]+combined(n))
 for row in crt['joint_rows']:
  b,L,h=row['b'],row['L'],row['h']
  phases=[str((h*(uu[n+1]-uu[n]))%1) for n in range(b,b+L-1)]
  assert hashlib.sha256('\n'.join(phases).encode()).hexdigest()==row['full_phase_sha256']
  def dist(x): x=x%1;return min(x,1-x)
  assert sum(dist(F(x))>=F(1,20) for x in phases)==row['full_slips']
 cauchy=s.Matrix([[s.Rational(1,8*n-8+d) for d in (1,4,5,6)] for n in range(1,5)])
 assert cauchy.det()!=0
 # Independent four-pole combined recurrence, p-primary denominator detection.
 u=[unrolled(n) for n in range(18)]
 assert all(u[n].denominator%19 for n in range(10,17)) and u[17].denominator%19==0
 u274=unrolled(274);assert u274.denominator%73
 print(json.dumps({'status':'PASS','method':'symbolic Laplace series, SymPy inverse and direct unrolling',
 'moments':list(map(str,mus)),'checks':checks,'four_pole_cauchy_determinant':str(cauchy.det()),
 'p19_p73_independent':True,'fresh_joint_rows_independent':len(crt['joint_rows']),'input_hashes':{name:hashlib.sha256((HERE/'receipts'/name).read_bytes()).hexdigest()
 for name in ('quadrature-witnesses.json','fresh-quadrature-witnesses.json')}},indent=2))

if __name__=='__main__': main()
