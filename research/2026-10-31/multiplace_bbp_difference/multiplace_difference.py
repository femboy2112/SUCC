"""Exact original BBP two-point resolvent at the real, 2-adic and 3-adic places.

All original signed poles, no source/seed mutation. Finite rational
certificates only; paper proofs and global scope in PROOF.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd

POLES = ((4,7),(-2,4),(-1,3),(-1,2))

def _integer(n):
    if type(n) is not int:
        raise ValueError("exact integer input required")

def valuation(z, p):
    """v_p for nonzero exact rational. p must be a supplied prime."""
    _integer(p)
    if p<2:
        raise ValueError("prime p>=2 required")
    x=F(z)
    if not x:
        raise ValueError("v_p(0) is infinity")
    def v(n):
        k=0
        n=abs(n)
        while n%p==0:
            k+=1;n//=p
        return k
    return v(x.numerator)-v(x.denominator)

def bbp_source(n):
    """Original unmodified four-pole rational source; all integer indices."""
    _integer(n)
    return sum((F(w,8*n-c) for w,c in POLES),F(0))

def original_denominator(n):
    _integer(n)
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)

def positive_moment_polynomial(t):
    """Exact 4-2t^3-t^4-t^5 = (1-t)(t^2+2)(t^2+2t+2)."""
    x=F(t)
    return (1-x)*(x*x+2)*(x*x+2*x+2)

def source_arch_moment(n):
    """Exact integral int_0^1 t^(8n-8) P(t) dt for n>=1."""
    _integer(n)
    if n<1:raise ValueError("positive integer argument for real integral")
    return (F(4,8*n-7)-F(2,8*n-4)
            -F(1,8*n-3)-F(1,8*n-2))

def source_two_point_arch(x,y):
    """Real positive integral int_0^1 t^(8x-8)(1-t^(8(y-x)))P(t)dt."""
    _integer(x);_integer(y)
    if not 1<=x<y:raise ValueError("real positive moment domain 1<=x<y")
    return source_arch_moment(x)-source_arch_moment(y)

def source_moment_coefficient(y,j):
    """C_j(y) = sum_pole weight/(8y-c)^(j+1).

    For y>=1 this is Gamma(j+1)^(-1) int_0^inf
    u^j exp(-(8y-7)u)P(exp(-u)) du >0 in the REAL place.
    Every C_j(y) is exact rational and can separately be evaluated p-adically.
    """
    _integer(y);_integer(j)
    if j<0:raise ValueError("nonnegative geometric moment order")
    return sum((F(w,(8*y-c)**(j+1)) for w,c in POLES),F(0))

def pole_depth_three(y):
    """Maximum genuine 3-adic pole depth at the integer y, always >=1."""
    _integer(y)
    return max(valuation(8*y-c,3) for _,c in POLES)

def pole_depth_profile(k):
    """Exactly how many y mod 3^k meet max_p v3(8y-c) >= k."""
    _integer(k)
    if k<1:raise ValueError("k>=1")
    modulus=3**k
    roots=tuple(sorted({(c*pow(8,-1,modulus))%modulus for _,c in POLES}))
    return dict(level=k,modulus=modulus,roots=roots,tail_fraction=F(len(roots),modulus))

def truncated_mean_pole_depth(K):
    """Mean of min(d(y),K) on any full 3^K residue system."""
    _integer(K)
    if K<1:raise ValueError("K>=1")
    return F(5,3)-F(2,3**K)

def resolvent_certificate(y,h,J):
    """Simultaneous real/2adic/3adic rational series certificate.

    x=y-h>=1, h>0, and v3(h)>d(y). The two separate source series:
      r(x)=sum_(j>=0)(8h)^j C_j(y), r(y)=C_0(y).
    Difference starts at j=1, with exact rational remainder.
    The SAME finite sums and remainder work at ALL THREE places.
    """
    for k in (y,h,J):_integer(k)
    if h<1 or y-h<1 or J<1:
        raise ValueError("real interval and positive truncation required")
    d=pole_depth_three(y)
    m3=valuation(h,3)
    if m3<=d:
        raise ValueError("3-adic resolvent requires v3(h)>pole depth")
    m2=valuation(h,2)
    exact=bbp_source(y-h)-bbp_source(y)
    prefix=sum(((8*h)**j*source_moment_coefficient(y,j)
                for j in range(1,J)),F(0))
    remainder=sum((F(w*(8*h)**J,
                    ((8*y-c)**J)*(8*(y-h)-c)) for w,c in POLES),F(0))
    assert exact==prefix+remainder
    rho=F(8*h,8*y-7)
    assert 0<rho<1
    bound_real=F(8,8*(y-h)-7)*rho**J
    low2=J*(m2+1)-2
    low3=J*(m3-d)-d
    return {"exact":exact,"prefix":prefix,"remainder":remainder,
            "real_error_upper":bound_real,
            "v2_remainder_lower":low2,"v3_remainder_lower":low3,
            "pole_depth":d,"v2_h":m2,"v3_h":m3,
            "v2_exact":valuation(exact,2),"v3_exact":valuation(exact,3)}

def exact_pole_slope(y):
    """Original source derivative r'(y)=-8*C_1(y), exact rational."""
    _integer(y)
    return -8*source_moment_coefficient(y,1)

def small_shift_valuation(y,m):
    """Sharpened EXACT prime-3 source law, not merely previous lower bound."""
    _integer(y);_integer(m)
    d=pole_depth_three(y)
    if m<=d:raise ValueError("m must exceed local 3-adic pole depth")
    h=6**m
    delta=bbp_source(y-h)-bbp_source(y)
    return {"pole_depth":d,"v2_exact":valuation(delta,2),
            "v3_exact":valuation(delta,3),"v3_formula":m-2*d,
            "old_d_product":valuation(original_denominator(y),3)}

def joint_dyadic_pole_classes(a,K):
    """Exact joint time law for authentic U_n mod2^a and truncated pole depth.

    Uses source recurrence U0=0; source DSI-4 ensures permutation
    at any 2^a complete interval. CRT ensures product classes with
    d(n+1) mod3^K. Cost is a deterministic source pole classification.
    """
    _integer(a);_integer(K)
    if not 1<=a<=10 or not 1<=K<=7:
        raise ValueError("bounded exact finite testing layers")
    q=2**a;pk=3**K;period=q*pk
    # source residues from exact original combined odd-denominator form
    state=0;counts={}
    for n in range(period):
        key=(state,min(pole_depth_three(n+1),K))
        counts[key]=counts.get(key,0)+1
        y=n+1
        A=120*y*y-89*y+16
        D=original_denominator(y)
        state=(16*state+A*pow(D,-1,q))%q
    per_depth={}
    for y in range(1,pk+1):
        d=min(pole_depth_three(y),K)
        per_depth[d]=per_depth.get(d,0)+1
    expected={(v,d):c for v in range(q) for d,c in per_depth.items()}
    return {"period":period,"counts":counts,"expected":expected,
            "factorizes":counts==expected,"depth_counts":per_depth}

def prime_exposure(m):
    """Real nonzero limit, local vanishing and forced external denominator."""
    _integer(m)
    if m<2:raise ValueError("m>=2")
    y=1+6**m
    delta=bbp_source(1)-bbp_source(y)
    v2=valuation(delta,2)
    v3=valuation(delta,3)
    assert v2==m and v3==m-2
    assert F(3)<delta<F(47,15)
    assert gcd(delta.denominator,6)==1
    forced_min=F(5,141)*6**m
    assert delta.denominator>forced_min
    return {"m":m,"delta":delta,"v2":v2,"v3":v3,
            "denominator":delta.denominator,
            "denominator_lower_bound":forced_min,
            "source_limit_real":F(47,15)}

def real_positive_tail_limit(m):
    """Pair source r(1)−r(1+6^m), converges real to 47/15."""
    _integer(m)
    if m<1:raise ValueError("m>=1")
    return source_two_point_arch(1,1+6**m)


def source_gamma_moment_upper(y,j):
    """Rigorous positive real upper bound on C_j(y) via P(e^-u)<=15u."""
    _integer(y);_integer(j)
    if y<1 or j<0:raise ValueError("positive real y, j>=0")
    return F(15*(j+1),(8*y-7)**(j+2))

def source_moving_prefix_upper(m,J):
    """For y=1+6^m, finite REAL resolvent prefix j=1..J-1 is O_J(6^-2m)."""
    _integer(m);_integer(J)
    if m<1 or J<1:raise ValueError("m>=1,J>=1")
    return F(15*(J-1)*(J+2),2*(8*6**m+1)**2)

def source_difference_polynomial(h):
    """Exact factored Δ(h)=r(1)-r(1+h), h≥1.

    Polynomial numerator factors show p=2 and p=3 cancellation and
    the necessity of growing complementary denominator primes.
    """
    _integer(h)
    if h<1:raise ValueError("h>=1")
    B=24064*h**3+48128*h**2+31664*h+6853
    Den=15*(2*h+1)*(4*h+3)*(8*h+1)*(8*h+5)
    result=F(h*B,Den)
    assert result==bbp_source(1)-bbp_source(h+1)
    return result

def source_perpetual_five_exposure(m):
    """The reduced denominator of Δ(6^m) always contains prime5."""
    _integer(m)
    if m<2:raise ValueError("m>=2")
    h=6**m
    B=24064*h**3+48128*h**2+31664*h+6853
    # h ≡1 (mod5), so B≡4 (mod5), while
    # (2h+1)(4h+3)(8h+1)(8h+5) is a 5-adic unit.
    x=source_difference_polynomial(h)
    return {"value":x,"five_denominator_valuation":-valuation(x,5),
            "numerator_mod_five":(h*B)%5}


def deep_pole_count(N,k,start=0):
    """Literal source-pole positions d(n+1)>=k for a finite integer window."""
    for z in (N,k,start):_integer(z)
    if N<1 or k<2 or start<0:
        raise ValueError("N>=1,k>=2,start>=0 required")
    q=3**k
    rootset=set(pole_depth_profile(k)["roots"])
    return sum(1 for n in range(start,start+N) if (n+1)%q in rootset)

def deep_pole_fraction_upper(N,k):
    """At ANY horizon fraction of deep 3-adic source poles <= 4/3^k+4/N."""
    _integer(N);_integer(k)
    if N<1 or k<2:raise ValueError("N>=1,k>=2 required")
    return F(4,3**k)+F(4,N)

def shallow_phase_removal_certificate(N,k,start=0):
    """If |z_n|=1, removing deep poles alters mean by at most this count/N.

    Valid for actual BBP Fourier phases z_n=e(hU_n), any fixed integer h.
    Does NOT assert the retained shallow-phase sum decays.
    """
    bad=deep_pole_count(N,k,start)
    return {"discarded":bad,"exact_fraction":F(bad,N),
            "universal_upper":deep_pole_fraction_upper(N,k)}


def pole_two_mod_three_shell_count(k,K):
    """For m<k<K, there are exactly 2*3^(K-k-1) residues with v3(8y-2)=k."""
    _integer(k);_integer(K)
    if not 1<=k<K:
        raise ValueError("1<=k<K required")
    return 2*3**(K-k-1)

def prime_three_L1_divergence_lower(m,K):
    """Exact certified lower bound for normalized p3 ABSOLUTE magnitude.

    (1/3^K) sum_(0<=y<3^K) |r(y-6^m)-r(y)|_3
       >= (2/3)(K-m-1), K>=m+2.
    This is NOT a bound on bounded real Fourier phases!
    """
    _integer(m);_integer(K)
    if m<1 or K<m+2:
        raise ValueError("m>=1 and K>=m+2 required")
    return F(2*(K-m-1),3)

def good_pole_mean_absolute(m):
    """EXACT density-weighted p3 norm on d(y)<m classes.

    For m>=2, sum_(d<m) Pr(d)*3^(2*d-m) = 4/3-7/3^m.
    This tends to 4/3, hence p3 pointwise convergence is not L1.
    """
    _integer(m)
    if m<2:raise ValueError("m>=2 required")
    return F(4,3)-F(7,3**m)
