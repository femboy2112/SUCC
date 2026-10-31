"""Complementary closed-form N=0/1 period-fiber checks; no producer imports."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib,json

def beta(a,b):return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))
def integral(p,degree=0):return sum((v/F(k+degree+1) for k,v in p.items()),F(0))
def difference_source(r):
    out={}
    for k,v in r.items():
        if k:
            out[k-1]=out.get(k-1,F(0))+16*k*v
            out[k+7]=out.get(k+7,F(0))-k*v
    return out

rows=[]
for m,N in ((11,1),(13,0)):
    mean=beta(17,m+2)/beta(9,m+2)
    r={}
    for j in range(m+2):
        c=F((-1)**j*comb(m+1,j))
        if N:
            r[9+j]=r.get(9+j,F(0))+c
            r[1+j]=r.get(1+j,F(0))-mean*c
        else:r[1+j]=r.get(1+j,F(0))+c
    d=difference_source(r)
    assert sum(r.values())==0
    assert r.get(0,0)==0
    assert sum(k*v/F(k) for k,v in r.items() if k)==0 # integral of R prime
    orbit=F(0)
    for n in range(1,17):
        forcing=integral(d,8*n-8)
        orbit=16*orbit+forcing
        target=8*n*integral(r,8*n-1)
        assert orbit==target
        if n<=N:assert forcing==orbit==0
        if n==N+1:assert orbit>0
        cp=1+mean if N else F(1)
        assert abs(orbit)<=cp*F(factorial(m+1),(8*n)**(m+1))
    rows.append({'m':m,'N':N,'checks':16,'first_unmatched_positive':True})
root=Path(__file__).resolve().parents[1]
dossier=root/'period_preserving/PERIOD_FIBERS.md'
record={'status':'PASS','rows':rows,'reviewed_sha256':hashlib.sha256(dossier.read_bytes()).hexdigest(),
        'scope':'complementary same-model proof review and N=0/1 exact checks'}
p=Path(__file__).with_name('period_review_receipt.json')
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
