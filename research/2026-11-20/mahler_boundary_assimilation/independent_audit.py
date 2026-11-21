"""Second implementation / diagnostics, same-agent provenance (NOT blind referee).

Does not import the implementation under test.  Tests independent closed-form
inverse parity sums, direct rational 3/2 orbits, brute finite survivor guard,
exact polynomial identities, and nonrigorous spectral trapezoids for illustration.
"""
from fractions import Fraction as F
from itertools import product
import cmath
import json
import math


def w(x):
    return (3 * x + x % 2)//2


def c(x):
    return x//2 if x % 2 == 0 else (3*x+1)//2


def inverse_closed(word, label):
    n=len(word)
    modulus=2**n
    s=0
    ones=0
    for j,b in enumerate(word):
        ones += b
        denpower = j+1 if label == 'W' else ones
        s -= b * (2**j) * pow(3, -denpower, modulus)
    return s % modulus


def direct_bits(x,n,label):
    out=[]
    fun=w if label=='W' else c
    for _ in range(n):
        out.append(x%2)
        x=fun(x)
    return tuple(out)


def direct_survives(g,r,n):
    x=F(g)+r
    for _ in range(n):
        g0=x.numerator//x.denominator
        r0=x-g0
        if not F(0)<=r0<F(1,2):
            return False
        xnext=F(3,2)*x
        g1=xnext.numerator//xnext.denominator
        r1=xnext-g1
        if g1!=w(g0) or not F(0)<=r1<F(1,2):
            return False
        x=xnext
    return True


def source_Q(t):
    return (1-t)*(t*t+2)*(t*t+2*t+2)


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):out[i+j]+=ai*bj
    return out


def run():
    checks=0
    for n in range(1,10):
        for word in product((0,1),repeat=n):
            for label in ('W','C'):
                seed=inverse_closed(word,label)
                assert direct_bits(seed,n,label)==word
                checks+=1

    for g in range(20):
        for j in range(1,9):
            for rnumer in range(90):
                r=F(rnumer,180)
                x=F(g)+r
                v=direct_survives(g,r,j)
                # Independent necessary-and-sufficient finite prefix inequalities.
                gi=g
                low,hi=F(0),F(1,2)
                a,delta=F(1),F(0)
                for _ in range(j):
                    b=gi%2
                    lbound=F(1,3) if b else F(0)
                    ubound=F(1,2) if b else F(1,3)
                    low=max(low,(lbound-delta)/a)
                    hi=min(hi,(ubound-delta)/a)
                    a,delta=F(3,2)*a,F(3,2)*delta-F(b,2)
                    gi=w(gi)
                assert v==(low<=r<hi)
                checks+=1

    H=poly_mul([2,0,1],[2,2,1])
    assert H==[4,4,4,2,1]
    Q=poly_mul([1,-1],H)
    assert Q==[4,0,0,-2,-1,-1]
    K=[-4,4,0,-2,1]
    assert poly_mul(H,K)==[-16,0,0,0,0,0,0,0,1]
    checks+=3
    # Jensen's root formula predicts mean log|Q(r e^(i theta))| exactly.
    # Trapezoid comparison below is NUMERIC DIAGNOSTIC, not proof.
    samples=4096
    max_error=0
    for q in (F(1,4),F(9,16),F(5,4),F(3,2),F(9,4),F(4)):
        r=math.sqrt(float(q))
        numeric=sum(math.log(abs(source_Q(r*cmath.exp(2j*math.pi*k/samples))))
                    for k in range(samples))/samples
        predicted=(math.log(4) if q<1 else
                   math.log(4)+0.5*math.log(float(q)) if q<2 else
                   2.5*math.log(float(q)))
        error=abs(numeric-predicted)
        assert error<2e-5,(q,numeric,predicted,error)
        max_error=max(max_error,error)
        checks+=1
    return {"checks":checks,"spectral_samples_per_radius":samples,
            "max_numeric_spectral_error":max_error,
            "authority":"finite same-agent exact checks; numeric quadrature not certificate"}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
