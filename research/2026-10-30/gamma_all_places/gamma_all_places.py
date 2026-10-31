"""All-prime affine-Gamma pole regularization and exact BBP tail transport.

Research-only pure rational implementations; not a p-adic Gamma implementation or
an asymptotic normality proof.  The Gamma recurrences are used analytically in
RESEARCH.md; the rational functions below reproduce their 1-step ratios.
"""
from fractions import Fraction as F
from math import gcd

DELTAS = (1, 4, 5, 6)
AUTH = (4, -2, -1, -1)
AGE_KERNEL = (1, -3, 1, 1)
FAKE = (5, -5, 0, 0)
RANK2_2ADIC_FAKE_PLUS = tuple(a + 4 * b for a, b in zip(AUTH, AGE_KERNEL))
RANK2_2ADIC_FAKE_MINUS = tuple(a - 4 * b for a, b in zip(AUTH, AGE_KERNEL))

def source(n, c=AUTH):
    assert n >= 1
    return sum((F(co, 8 * (n - 1) + de) for de, co in zip(DELTAS, c)), F())

def orbit(n, c=AUTH, seed=F(0)):
    assert n >= 0
    u = F(seed)
    for k in range(1, n + 1):
        u = 16 * u + source(k, c)
    return u

def local_ratio(n, p, c=AUTH):
    """Morita Gamma_p(8t+d+1)/Gamma_p(8t+d): -z if p-unit else -1.

    Product c_delta-powers, evaluated at integer t=n-1.  No external
    p-adic package or unverified analytic continuation is needed.
    """
    assert n >= 1 and p >= 2
    ans = F(1)
    t = n - 1
    for d, co in zip(DELTAS, c):
        z = 8 * t + d
        factor = -z if z % p else -1
        ans *= F(factor) ** co
    return ans

def local_regular(n, p, c=AUTH):
    assert n >= 1 and p >= 2
    return sum((F(co, 8*(n-1)+d) for d, co in zip(DELTAS,c) if (8*(n-1)+d)%p), F())

def local_polar(n, p, c=AUTH):
    assert n >= 1 and p >= 2
    return sum((F(co, 8*(n-1)+d) for d, co in zip(DELTAS,c) if (8*(n-1)+d)%p==0),F())

def two_adic_defect(n, c=AUTH):
    """Exact 2-local omitted channel pair: B/[4(2n-1)]+D/[2(4n-1)]."""
    assert n >= 1
    return F(c[1],4*(2*n-1)) + F(c[3],2*(4*n-1))

def two_integrality_condition(c):
    """For integral channel coefficients: source(n) in Z_2 for ALL n>=1."""
    assert all(int(v)==v for v in c)
    return (int(c[1]) + 2*int(c[3])) % 4 == 0

def v_p_fraction(x, p):
    x=F(x)
    if not x: return None
    a,b=abs(x.numerator),x.denominator
    v=0
    while a%p == 0: a//=p;v+=1
    while b%p == 0: b//=p;v-=1
    return v

def ages(c):
    return tuple(sum((F(co*((q*d)%8),8) for d,co in zip(DELTAS,c)),F()) for q in (1,3,5,7))

def coeff_deform(t):
    return tuple(a+t*b for a,b in zip(AUTH,AGE_KERNEL))

def tail(n, length=160, c=AUTH):
    """Finite future Green tail approximation, with omitted positive tail for AUTH."""
    assert n>=1 and length>=1
    return sum((source(n+j,c)*F(1,16**j) for j in range(1,length+1)),F())

def partial_total_tail(N, length=160):
    return sum((tail(n,length) for n in range(1,N+1)),F())

def total_source_partial(N, c=AUTH):
    return sum((source(n,c) for n in range(1,N+1)), F())

def total_pi_partial(N):
    return sum((F(source(n),16**(n-1)) for n in range(1,N+1)),F())

def sum_tail_rhs_partial(N):
    """Exact N-truncated identity, where m goes to N:
       RHS = (1/15) sum_(m=2)^N r_m (1-16^-(m-1)).
       This equals sum_(n=1)^(N-1) sum_(j=1)^(N-n) 16^-j r_(n+j).
    """
    return sum((source(m)*(1-F(1,16**(m-1)))/15 for m in range(2,N+1)),F())

def time_weighted_gamma(n, c=AUTH):
    """Real Gamma one-step ratio H(t), t=n-1, through its rational factors."""
    assert n>=1
    out=F(1)
    for de,co in zip(DELTAS,c):out *= F(8*(n-1)+de)**co
    return out
