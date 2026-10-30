"""Fresh exact quadratic-field aggregate/product review of root clock front."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,prod
import json,hashlib
import mpmath as mp
from fib_composition import fib,ga,gm,gp,gi,gs,harmonic,LAMBDA
root=Path(__file__).resolve().parent
clock=root.parent/'clock_constants'
mp.mp.dps=160
lam=(mp.sqrt(5)-1)/2;phi=1/lam;q=-lam*lam
one=(F(1),F(0));p=gp(LAMBDA,2);qfield=gs(p,-1)
def real(a):return mp.mpf(a[0].numerator)/a[0].denominator+mp.mpf(a[1].numerator)/a[1].denominator*lam
rows=[]
for N in [10,11,12]:
    aggregate=(F(0),F(0))
    for j in range(2,N+1):
        m=fib(j)
        direct=(F(0),F(0))
        for k in range(m+1):
            weight=gs(gm(gp(p,k),gp(LAMBDA,m-k)),F(comb(m,k)))
            direct=ga(direct,gs(weight,harmonic(k)))
        inverse=(harmonic(m),F(0))
        for k in range(1,m+1):inverse=ga(inverse,gs(gp(LAMBDA,k),-F(1,k)))
        assert direct==inverse
        aggregate=ga(aggregate,direct)
    b=mp.fsum(mp.digamma(fib(j)+1)-mp.log(fib(j))+mp.quad(lambda t:t**fib(j)/(1-t),[0,lam]) for j in range(2,N+1))
    rhs=F((N-1)*(N-2),2)*mp.log(phi)+(N-1)*(mp.euler-mp.log(5)/2)+mp.log(mp.qp(q,q,N)/(1-q))+b
    residual=abs(real(aggregate)-rhs)
    assert residual<mp.mpf('1e-100')
    rows.append({'N':N,'maximum_rank':fib(N),'aggregate_field':[str(t) for t in aggregate],
                 'numeric_residual':mp.nstr(residual,8),'status':'PASS'})
products=[]
for N in [3,6,11,17,25]:
    pfield=one
    for n in range(1,N+1):pfield=gm(pfield,ga(one,gs(gp(qfield,n),-1)))
    rhs=gm(gm(gp((F(1),F(1)),N*(N+1)//2),gp(gi((F(1),F(2))),N)),pfield)
    assert rhs==(F(prod(fib(n) for n in range(1,N+1))),F(0))
    products.append({'N':N,'identity':'exact Q(lambda) fibonorial','status':'PASS'})
paths=[clock/'CLOCK_CONSTANTS.md',clock/'clock_constants.py',clock/'numerical_oracle.py',
       root.parent/'receipts/clock-exact.log',root.parent/'receipts/clock-oracle.log']
record={'status':'PASS','authority':'same-model complementary proof/code review plus exact field and fresh high-precision checks',
        'reviewed_sha256':{str(p.relative_to(root.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'finite_aggregate_rows':rows,'product_rows':products}
p=root/'root_clock_review_receipt.json'
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
