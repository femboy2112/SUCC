"""Independent SymPy/mpmath oracle for the model/carrier distinction.

Uses alternative algebraic derivations; independent code, shared model.
Not a pi-digit computation or physical field simulation.
"""
import sympy as S
import mpmath as mp
from collections import defaultdict

mp.mp.dps = 65
base=16
x=S.Rational(1,257)
states=[]
for _ in range(4):
    states.append(x)
    x=(16*x)%1
assert x==states[0] and len(set(states))==4

def digit(q):
    return S.floor(16*q)

def block(q,k):
    ds=[]
    for _ in range(k):
        ds.append(int(digit(q)))
        q=(16*q)%1
    return tuple(ds)

def cond_entropy(k):
    groups=defaultdict(list)
    for z in states:
        groups[block((16*z)%1,k)].append(int(digit(z)))
    s=mp.mpf(0)
    for ds in groups.values():
        hist={d:ds.count(d) for d in set(ds)}
        for c in hist.values():
            p=mp.mpf(c)/len(ds)
            s-=mp.mpf(len(ds))/len(states)*p*mp.log(p)
    return s
assert mp.almosteq(cond_entropy(1),mp.log(2))
assert cond_entropy(2)==0
print('Finite exact 257-cycle: H(D|one future digit)=',mp.nstr(cond_entropy(1),28),
      '; H(D|two future digits)=',mp.nstr(cond_entropy(2),28))

p0=S.Rational(1,2);p_others=S.Rational(1,30)
kl=S.simplify(p0*S.log(16*p0)+15*p_others*S.log(16*p_others))
assert S.simplify(kl-S.log(S.Rational(64,15))/2)==0
h=S.log(16)-kl
print('Exact biased branch KL=',kl,'; entropy rate=',h)
assert (kl>0)==S.true

# The actual zero carrier stays delta_0, but fair inverse-branch
# iterations produce an ever finer uniform grid.
for k in range(1,5):
    m=16**k
    expected=S.Rational(1,2*m)
    cost=S.summation(S.Rational(1,2*m*m),(S.Symbol('j',integer=True),0,m-1))
    assert cost==expected
    print('model fair iteration',k,'grid support',m,'W1-to-Haar=',cost)

# Independent one-dimensional CDF integration for delta0 vs fair predecessor law.
points=[S.Rational(d,16) for d in range(16)]
# Pdelta0 distributes equal 1/16 weights at points; displacement from zero
w1=sum(points,S.Rational(0))/16
assert w1==S.Rational(15,32)
print('True coherent carrier vs fair model W1=',w1)

# Real signed BBP pole at first two times: the model cannot infer prior branch.
def R(a):return S.Rational(4,a)-S.Rational(2,a+3)-S.Rational(1,a+4)-S.Rational(1,a+5)
assert R(1)==S.Rational(47,15)
assert R(9)==S.Rational(106,819)
source=S.symbols('a',positive=True)
assert S.cancel(4/source-2/(source+3)-1/(source+4)-1/(source+5) -
    (15*source**2+121*source+240)/(source*(source+3)*(source+4)*(source+5)))==0

# Check source-tail truncation cohomological residual exactly.
n=3;D=5
Tn=sum(S.Rational(1,16**j)*R(8*(n+j)-7) for j in range(1,D+1))
Tnext=sum(S.Rational(1,16**j)*R(8*(n+j+1)-7) for j in range(1,D+1))
assert S.factor(16*Tn-Tnext-R(8*(n+1)-7)) == -S.Rational(1,16**D)*R(8*(n+D+1)-7)
print('Truncated source-tail identity: exact residual verified')

# Pinsker conclusion for the biased Bernoulli k-block law.
for k in (1,2,3,4):
    bound=mp.sqrt(k*mp.mpf(str(S.N(kl,60)))/2)
    assert bound>0
    print('k=',k,'conditional model adequacy TV upper bound',mp.nstr(bound,16))
print('Independent SymPy/mpmath oracle PASS')
