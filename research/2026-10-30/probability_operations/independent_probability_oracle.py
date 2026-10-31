"""Independent SymPy / mpmath derivations for Gamma-Oily and Haar operation laws."""
import sympy as s
import mpmath as mp
mp.mp.dps=55

b=16
u=s.symbols('u',positive=True)
t=s.Rational(1,3)
# Normal orbit x, y={16*x}; their joint graph is NOT Haar^2.
measure=s.Rational(5,1)*t/b + t/b
assert measure==s.Rational(1,8)
assert measure!=t*t
print('Normal graph-Haar max(x,T16(x)) CDF at 1/3 =',measure,'versus independent',t*t)
# Uniform inverse branches reconstruct exactly the Lebesgue moments.
for moment in range(7):
    lhs=sum((s.integrate(((d+u)/b)**moment,(u,0,1))/b for d in range(b)),s.Rational(0))
    assert s.simplify(lhs-s.Rational(1,moment+1))==0
print('Uniform inverse-branch moments m=0..6: PASS')

phi=(1+mp.sqrt(5))/2
lam=1/phi
for rank in (2,3,4,6):
    gamma_log=mp.quad(lambda y:mp.power(y,rank-1)*mp.exp(-y)*mp.log(y)/mp.factorial(rank-1),[0,1,mp.inf])
    lap=mp.quad(lambda y:mp.power(y,rank-1)*mp.exp(-(1+lam)*y)/mp.factorial(rank-1),[0,1,mp.inf])
    H=sum(mp.mpf(1)/j for j in range(1,rank))
    expected=H-mp.euler-lam**rank
    assert mp.fabs(gamma_log-(H-mp.euler))<mp.mpf('1e-48')
    assert mp.fabs(lap-lam**rank)<mp.mpf('1e-48')
    assert mp.fabs(gamma_log-lap-expected)<mp.mpf('1e-48')
    print('Oily rank',rank,'D=',mp.nstr(gamma_log-lap,28),'analytic=',mp.nstr(expected,28))
assert abs((1-mp.euler-lam**2)-(lam-mp.euler))<mp.mpf('1e-48')
print('Gamma(2) = -log(U1*U2), Oily λ−γ reconstructed: PASS')

# Separate CDF-integral algorithm for exact finite original-source Wasserstein.
from fractions import Fraction as F
from collections import defaultdict
import importlib.util
spec=importlib.util.spec_from_file_location('probability_operations_probe',__file__.replace('independent_probability_oracle.py','probability_operations_probe.py'))
source=importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)

# Machin, independent from BBP source, gives exact first 80 hex digits.
def atan_interval(q,n):
    S=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
    e=F(1,(2*n+1)*q**(2*n+1))
    return (S,S+e) if n%2==0 else (S-e,S)
a,b=atan_interval(5,85)
c,d=atan_interval(239,24)
ml,mh=a-d/4,b-c/4
M=source.alpha_interval(96)
for k in (8,32,64,80):
    assert (ml*16**k).__floor__()==(mh*16**k).__floor__()
    assert (ml*16**k).__floor__()==(M[0]*16**k).__floor__()
print('Independent rational Machin BBP first 80 hex digits: MATCH')


def exact_cdf_w1(grid_states, length, B=16):
    N=len(grid_states)-1
    SCALE=B**length
    events=defaultdict(F)
    for x in grid_states[:-1]:events[x*B]+=F(1,N)
    for y in grid_states[1:]:
        for d in range(B):events[d*SCALE+y]-=F(1,B*N)
    keys=sorted(events)
    acc=F(0);area=F(0)
    for i,x in enumerate(keys[:-1]):
        acc+=events[x]
        area+=abs(acc)*(keys[i+1]-x)/F(B*SCALE)
    assert acc+events[keys[-1]]==0
    return area

for n in (32,128,256):
    length=8
    ds=source.certified_hex_digits(n+length+2)
    states=source.fixed_radix_tails(ds,length,n)
    cdf=exact_cdf_w1(states,length)
    quantile=source.w1_empirical_vs_predecessor(states,length)
    assert cdf==quantile
    print(f'Independent exact CDF vs quantile W1: N={n}, epsilon={float(cdf):.12f}, identities MATCH')
print('Independent probability-operations oracle PASS')
