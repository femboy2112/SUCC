"""Exact Walsh tensor rank and positive-source coherent counterseed control."""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s

root=Path(__file__).resolve().parent
raw=json.loads((root/'receipts/exact-probe.log').read_text())
rows=[]
for n_str,data in raw['carry_grade_walsh_tensors'].items():
    n=int(n_str)
    M=s.Matrix([[s.Rational(v) for v in row] for row in data])
    # Walsh inversion gives the actual source-weighted carry residue law.
    chi=lambda mask,d: (-1)**((mask&d).bit_count())
    p=[s.factor(sum(M[0,m]*chi(m,d) for m in range(16))/16) for d in range(16)]
    assert all(x>=0 for x in p) and sum(p)==1
    dispersion=s.factor(sum(1-M[0,m]**2 for m in range(16)))
    assert dispersion==16*(1-sum(x*x for x in p))
    rank=M.rank()
    assert rank>1
    # For the exact coherent seed, its future carry is15 at every marked
    # time n+j. The source/grade weights are identical to authentic.
    coherent=s.Matrix([[M[a,0]*chi(b,15) for b in range(16)] for a in range(16)])
    assert coherent.rank()==1
    coherent_carry_disp=sum(1-coherent[0,m]**2 for m in range(16))
    assert coherent_carry_disp==0
    rows.append(dict(n=n,authentic_rank=rank,coherent_rank=1,
                     authentic_carry_support=[d for d,v in enumerate(p) if v],
                     carry_probabilities=list(map(str,p)),
                     authentic_total_Walsh_dispersion=str(dispersion),coherent_dispersion='0'))
print(json.dumps(dict(status='PASS',scope='finite authentic observations, exact all-time coherent control',rows=rows),indent=2))
