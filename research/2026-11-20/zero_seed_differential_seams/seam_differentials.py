"""Exact source-labelled differential probes for the BBP analytic/finite seam.

Research-only: original four poles U_0=0; source deformation τ enters only as
explicit matched-jet counterfactual Q_τ=Q+τ(1-t)^2.  No normality assertion.
"""
from __future__ import annotations
from fractions import Fraction
from math import floor

OFFSETS = (7, 4, 3, 2)
COEFFICIENTS = (4, -2, -1, -1)


def authentic_forcing(m: int) -> Fraction:
    if type(m) is not int or m < 1:
        raise ValueError("m must be a positive integer")
    return sum((Fraction(c, 8*m-a) for c,a in zip(COEFFICIENTS,OFFSETS)), Fraction())


def mutant_increment(m: int) -> Fraction:
    if type(m) is not int or m < 1:
        raise ValueError("m must be a positive integer")
    return Fraction(2, (8*m-7)*(8*m-6)*(8*m-5))


def forcing(m: int, tau: Fraction | int = 0) -> Fraction:
    tau = Fraction(tau)
    if not 0 <= tau <= 1:
        raise ValueError("matched-jet path tau must be in [0,1]")
    return authentic_forcing(m) + tau*mutant_increment(m)


def finite_source_journal(m: int, depth: int, tau: Fraction | int = 0):
    """At causal clock n=m-1 return S0,S1,S2 from k=0..depth-1.

    All outputs are exact rational.  Partial moments are not reported as exact
    infinite moments. Monotonicity bounds for omitted terms come separately.
    """
    if type(depth) is not int or depth < 1:
        raise ValueError("depth must be >=1")
    moments = [Fraction(),Fraction(),Fraction()]
    for k in range(depth):
        v = forcing(m+k,tau)/16**k
        for j in range(3):
            moments[j] += k**j*v
    return tuple(moments)


def lag_mean_interval(m: int, depth: int, tau: Fraction | int = 0):
    """Rigorous rational interval for analytic G_(m-1)'(1)/G_(m-1)(1).

    For omitted k>=depth, r(m+k) <= r(m+depth), and q=1/16.
    """
    z,first,_ = finite_source_journal(m,depth,tau)
    q = Fraction(1,16)
    c = forcing(m+depth,tau) * q**depth
    tail0 = c/(1-q)
    tail1 = c*(Fraction(depth,1)/(1-q)+q/(1-q)**2)
    return first/(z+tail0),(first+tail1)/z


def lag_signed_derivative_truncated(m: int, depth: int, tau: Fraction | int = 0):
    """Finite-depth EXACT derivative of the TRUNCATED lag mean, not an infinite enclosure.

    Uses exact quotients of finite moments and separate tail bounds.  For a
    clean exact sign proof see THEOREMS.md; this enclosure is a finite probe.
    """
    tau=Fraction(tau)
    z,one,_=finite_source_journal(m,depth,tau)
    dz,done,_ = (Fraction(),Fraction(),Fraction())
    dz=Fraction();done=Fraction()
    for k in range(depth):
        v = mutant_increment(m+k)/16**k
        dz+=v;done+=k*v
    # finite approximate derivative; approximation is tagged as such
    return (done*z-one*dz)/(z*z)


def source_parameter_jacobian(times: tuple[int,...], depth: int | None = None):
    """Unwrapped U_t Jacobian wrt (s,c1,c2,c3,c4) for literal four poles.

    n-th row = 16^n (1, sum_{j<=n} 16^-j /(8j-a_i)).
    """
    if any(type(t) is not int or t < 0 for t in times):
        raise ValueError("nonnegative integer clocks only")
    rows=[]
    for n in times:
        row=[Fraction(16**n)]
        for a in OFFSETS:
            row.append(sum((Fraction(16**(n-j),8*j-a) for j in range(1,n+1)),Fraction()))
        rows.append(tuple(row))
    return tuple(rows)


def finite_endpoint_jacobian(times: tuple[int,...], terminal: int):
    """Rank-one completed-phase endpoint Jacobian for finite terminal M.

    Treats the fixed terminal source as a well-typed rational surrogate; this
    is not the infinite exact pi phase except as M grows.
    """
    if terminal<1 or any(t < 0 for t in times):
        raise ValueError("invalid clocks or terminal")
    beta=(Fraction(1),)+tuple(sum((Fraction(1,16**j*(8*j-a))
                                    for j in range(1,terminal+1)),Fraction())
                               for a in OFFSETS)
    return tuple(tuple(16**n*x for x in beta) for n in times)


def bbp_pi_over_16_interval(depth: int):
    if depth<1: raise ValueError("depth>=1")
    P=sum((authentic_forcing(j)/16**j for j in range(1,depth+1)),Fraction())
    # authentic forcing monotone, so remaining terms bounded by first omitted
    return P,P+authentic_forcing(depth+1)/(15*16**depth)


def quarter_head(x: Fraction | int) -> int:
    """Half-circle quarter port for exact rational input, convention open edges."""
    t=Fraction(x)%1
    if t==Fraction(1,4) or t==Fraction(3,4):
        raise ValueError("threshold has no assigned continuous sign")
    return int(Fraction(1,4)<t<Fraction(3,4))


def quarter_at_clock(x: Fraction | int,n: int) -> int:
    if n < 0:raise ValueError("clock>=0")
    return quarter_head(Fraction(x)*16**n)


def signed_seam_crossings(x: Fraction, y: Fraction, n: int) -> int:
    """Distributional derivative ∑(δ_{(m+1/4)/16^n}-δ_{(m+3/4)/16^n}).

    Accumulate only for strict crossing endpoints; use rational x,y away from
    seams. x > y reverses orientation. No π digits used.
    """
    x=Fraction(x);y=Fraction(y)
    if n<0: raise ValueError("clock>=0")
    if x == y:return 0
    if x>y:return -signed_seam_crossings(y,x,n)
    a,b=x*16**n,y*16**n
    low = floor(a)-2
    high = floor(b)+2
    total=0
    for j in range(low,high+1):
        if a < j+Fraction(1,4) < b:total+=1
        if a < j+Fraction(3,4) < b:total-=1
    return total


def interval_quarter_certificate(n: int, depth: int) -> int:
    """Certify actual BBP quarter-head from source interval, never predecoded bits."""
    lo,hi=bbp_pi_over_16_interval(depth)
    return _quarter_interval_certificate(16**n*lo,16**n*hi)


def _quarter_interval_certificate(lo: Fraction,hi: Fraction) -> int:
    # A finite source interval cannot straddle an integer/quarter boundary.
    cands=[Fraction(k,4) for k in range(4*floor(lo)-4,4*floor(hi)+9)]
    if any(lo<=z<=hi for z in cands):
        raise ValueError("source precision insufficient at a quarter seam")
    assert quarter_head(lo)==quarter_head(hi)
    return quarter_head(lo)


def clock_source_order_displacement(j: int) -> Fraction:
    if j<1:raise ValueError("clock positive")
    return 15*(authentic_forcing(j)-authentic_forcing(j+1))


def first_radix_delayed_displacement(j: int) -> tuple[int,Fraction]:
    """Minimum d>=0 with 16^d D>=1/64; result always <1/4 if D<1/4."""
    D=clock_source_order_displacement(j)
    if not 0<D<Fraction(1,4):raise ValueError("D outside controlled domain")
    d=0
    while D<Fraction(1,64):
        D*=16;d+=1
    assert Fraction(1,64)<=D<Fraction(1,4)
    return d,D


def quarter_current_total_variation(n: int) -> int:
    """Exact variation of D_s[quarter_at_clock(x+s,n)] over one seed period."""
    if type(n) is not int or n < 0:raise ValueError("clock>=0")
    return 2*16**n


def quarter_current_fourier_over_i(n: int, h: int) -> int:
    """Exact Fourier coefficient of signed quarter-current, divided by i.

    Thus Fourier(Dq_n)(h) = i * this integer, with e(-h x)
    Fourier convention. No Gaussian multiplier is applied here.
    """
    if type(n) is not int or n < 0 or type(h) is not int:
        raise ValueError("nonnegative n and integer frequency required")
    base=16**n
    if h%base:return 0
    j=h//base
    if j%2==0:return 0
    return 2*base*(-1 if (j+1)//2%2 else 1)


def source_order_quarter_response(p: int, extra_terms: int = 12):
    """Exact source-interval quarter-port difference original minus swapped.

    Returns (clock, source-derived displacement, signed ±1/0 response).
    The swapped source modifies two FORCING inputs, not the homogeneous seed.
    """
    if type(p) is not int or p < 7 or p%2==0:
        raise ValueError("odd p>=7 needed")
    for d in range(3, int(p**0.5)+1,2):
        if p%d==0:raise ValueError("p must be prime")
    if extra_terms<1:raise ValueError("extra terms must be positive")
    j=(p*p-1)//8
    Noffset,delta=first_radix_delayed_displacement(j)
    N=j+1+Noffset
    lo,hi=bbp_pi_over_16_interval(N+extra_terms)
    a=_quarter_interval_certificate(lo*16**N,hi*16**N)
    b=_quarter_interval_certificate(lo*16**N-delta,hi*16**N-delta)
    return N,delta,a-b
