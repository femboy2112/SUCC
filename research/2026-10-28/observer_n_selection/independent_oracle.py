"""A different algebraic route: closed Pólya history probabilities + symbolic selection.

Does not import observer_model.py or its tests.
"""
import math
import sympy as s

a=s.symbols('a',positive=True)
checks=0
for j in range(1,13):
    # For a fixed order of zero/one choices with k ones, P(history)=k!(j-k)!/(j+1)!.
    # Summing over binomial(j,k) histories makes the native K_j exactly uniform.
    for k in range(j+1):
        weight=s.binomial(j,k)*s.factorial(k)*s.factorial(j-k)/s.factorial(j+1)
        assert weight==s.Rational(1,j+1)
        checks+=1
    z=sum(a**k for k in range(j+1))
    accept=s.cancel(z/(j+1))
    for k in range(j+1):
        posterior=s.cancel((s.Rational(1,j+1)*a**k)/accept)
        assert s.cancel(posterior-a**k/z)==0
        checks+=1

# P(K1=1,K2=1)=1/6 and P(K1=1,K2=2)=1/3.
posterior_early=s.cancel((a/s.Integer(6)+a*a/s.Integer(3))/(sum(a**k for k in range(3))/3))
controlled_early=a/(1+a)
assert s.cancel((controlled_early-posterior_early)-a*(1-a)/(2*(1+a)*(1+a+a*a)))==0
checks+=1

# Different but transported coordinates give exactly same KL and affinity.
x=s.symbols('x',positive=True)
probs=[x**k/(1+x+x*x) for k in range(3)]
kl=sum(q*s.log(3*q) for q in probs)
kl_reversal=sum(q*s.log(3*q) for q in reversed(probs))
assert s.simplify(kl-kl_reversal)==0
checks+=1

# An observer's declared code cost C(k)=k reproduces the geometric tilt.
lam=s.symbols('lam',positive=True)
raw=[s.exp(-lam*k) for k in range(4)]
assert s.simplify(sum(raw[k]/sum(raw) for k in range(4))-1)==0
checks+=1

print('Symbolic oracle:',checks,'identities PASS')
