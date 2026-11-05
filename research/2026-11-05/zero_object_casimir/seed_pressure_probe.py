"""Independent exact source-seed Fekete pressure and Gaussian bridge probes.

The variance coefficient is EXACT rational times pi^2. All original BBP
recurrence states and arithmetic resonances use Fraction and integer gcd.
None of these averaged estimates proves the authentic zero-seed determinant bound.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, pi, log

TAPS=(F(4),F(),F(),F(-2),F(-1),F(-1),F(),F())

def forcing(n:int)->F:
    return sum((w/F(8*(n-1)+j) for j,w in enumerate(TAPS,1)),F())

def original_states(nmax:int)->dict[int,F]:
    s=F(); out={}
    for n in range(1,nmax+1):
        rn=forcing(n)
        # Independent collapsed original forcing from #497.
        oracle=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        assert rn==oracle,(n,rn,oracle)
        s=16*s+rn
        out[n]=s
    return out

def bernoulli2(x:F)->F:
    t=x%1
    return t*t-t+F(1,6)

def epoch_pairs(A:int,U:dict[int,F]):
    return [(i,j,16**j-16**i,U[j]-U[i])
            for i in range(A,2*A) for j in range(i+1,2*A)]

def covariance_coeff(p,q)->F:
    i,j,n,a=p;k,l,m,b=q
    g=gcd(n,m)
    assert g==16**min(i,k)*(16**gcd(j-i,l-k)-1)
    return 2*F(g*g,n*m)*bernoulli2((m//g)*a-(n//g)*b)

def exact_variance_over_pi2(A:int)->F:
    U=original_states(2*A-1)
    pairs=epoch_pairs(A,U)
    return sum((covariance_coeff(p,q) for p in pairs for q in pairs),F())/A**4

def variance_constant_bound(A:int)->F:
    # Var / pi^2 <= (1/3) * (16/15)^2 * (17/15)^2 * (A-1)/A^3
    return F(1,3)*F(16,15)**2*F(17,15)**2*F(A-1,A**3)

def conditioned_bridge_variance(rho:F,d:int,k:int)->F:
    assert F()<rho<F(1) and 0<k<d
    a=rho**k; b=rho**(d-k);cross=rho**d
    # Direct 2x2 Schur computation, distinct from factored formula.
    mat=F(1)-cross*cross
    direct=F(1)-(a*a+b*b-2*cross*a*b)/mat
    factored=(1-rho**(2*k))*(1-rho**(2*(d-k)))/(1-rho**(2*d))
    assert direct==factored
    assert factored<1-rho**(2*k)
    return factored

def main():
    for A in (9,11):
        v=exact_variance_over_pi2(A)
        b=variance_constant_bound(A)
        assert v>0
        assert v<=b,(A,v,b)
        print(f"AUTHENTIC BBP Fekete seed variance A={A}: Var/pi^2 exact rational, decimal={float(v):.14g}; Var={float(v)*pi*pi:.14g}; A^2 Var={float(v)*pi*pi*A*A:.12g}; certified upper {float(b)*pi*pi:.12g}")
        print(f"  rational numerator/denominator digits: {len(str(v.numerator))}/{len(str(v.denominator))}; all gcd resonances PASS")
    for rho,d,k in ((F(2,5),4,1),(F(3,7),7,3),(F(1,2),5,2)):
        actual=conditioned_bridge_variance(rho,d,k)
        correlated=rho**d
        coupling=F(1)-correlated**2
        assert coupling>0 and coupling<1
        print(f"GAUSSIAN BRIDGE rho={rho} d={d} k={k}: conditioned variance={actual} ({float(actual):.9g}), alone={1-rho**(2*k)}, interaction F={.5*log(float(coupling)):.9g}")
    print("ORIGINAL_ZERO_OBJECT_CASIMIR_SEED_PRESSURE_FRESH_EXACT_PASS")
if __name__=='__main__':main()
