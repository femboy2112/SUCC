"""Independent all-rank Frullani route, no partial fractions or producer import."""
import json
from pathlib import Path
from fractions import Fraction
import mpmath as mp
mp.mp.dps=90

def f(s):
    q=Fraction(s)
    return mp.mpf(q.numerator)/q.denominator

def r(a):
    return 6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5))

root=Path(__file__).resolve().parent
rows=[]
for row in json.loads((root/'rank_receipt.json').read_text())['rows']:
    a=f(row['a']);k=row['k'];norm=r(a)
    def integrand(v):
        l=r(a*(1+v))/norm
        return (l-l**k)/v
    increment=mp.quad(integrand,[0,1,mp.inf])
    baseline=mp.fsum(1/mp.mpf(j) for j in range(2,2*k))
    gap=increment-baseline
    lo,hi=map(f,row['harmonic_gap'])
    assert lo<=gap<=hi
    assert gap>f(row['harmonic_bound'])
    rows.append({'a':row['a'],'k':k,'harmonic_gap':mp.nstr(gap,65),'status':'PASS'})
record={'status':'PASS','method':'positive Frullani integrals at90dps',
        'authority':'numerical oracle, not interval or independent external proof',
        'mpmath':mp.__version__,'rows':rows}
p=root/'rank_oracle_receipt.json'
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
