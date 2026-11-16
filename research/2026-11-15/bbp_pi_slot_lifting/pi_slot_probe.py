"""BBP original-four-pole π-slot lifting and shared-Poisson phase probes.

All source calculations use the literal zero seed and the original rational
forcing. The Euler character exp(2*pi*i*x) uses the circle's angular unit;
there is no pi TARGET value inside phase-source construction.

Finite checks are NOT a proof of base-16 normality.
"""
from __future__ import annotations

from fractions import Fraction


def q_poly(t):
    return 4 - 2*t**3 - t**4 - t**5


def forcing(n: int) -> Fraction:
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be >= 1')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def source_u(n: int) -> Fraction:
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be >= 0')
    u = Fraction(0)
    for j in range(1,n+1):
        u = 16*u + forcing(j)
    return u


def polynomial_prefix(n: int) -> Fraction:
    """Independent finite polynomial integral: int Q(t) sum_{j<n}16^(n-1-j)t^(8j) dt."""
    if n < 0:
        raise ValueError('n >= 0')
    return sum((16**(n-1-j) *
                (Fraction(4,8*j+1)-Fraction(2,8*j+4)-Fraction(1,8*j+5)-Fraction(1,8*j+6))
                for j in range(n)),Fraction())


def tail_interval(n: int, depth: int=24) -> tuple[Fraction,Fraction]:
    """Original source T_n rigorous enclosure, using monotone r and geometric 16 tail."""
    if not isinstance(n,int) or n<0 or not isinstance(depth,int) or depth<0:
        raise ValueError('n and depth >= 0')
    lo = sum((forcing(n+j)/16**j for j in range(1,depth+1)),Fraction())
    hi = lo + forcing(n+depth+1)/ (15*16**depth)
    return lo,hi


def green_diff_interval(n: int, lag: int, depth:int=32):
    """First temporal tail difference T_n-T_(n+lag), certified as interval."""
    a,b=tail_interval(n,depth);c,d=tail_interval(n+lag,depth)
    return a-d,b-c


def double_diff_interval(n:int, q:int, lag:int, depth:int=38):
    """Delta_q Delta_lag T_n = T_(n+q+lag)-T_(n+q)-T_(n+lag)+T_n."""
    bounds = [(1,n),(1,n+q+lag),(-1,n+q),(-1,n+lag)]
    lo=hi=Fraction()
    for s,index in bounds:
        a,b=tail_interval(index,depth)
        if s>0: lo+=a;hi+=b
        else: lo-=b;hi-=a
    return lo,hi


def moment_g(t):
    return q_poly(t)/(16-t**8)


def tail_mark(n:int,t):
    """Rao-Blackwellized version E[C*tau^(8n)|tau=t], with C a BBP coin."""
    return (t**(8*n))*moment_g(t)


def double_diff_mark(n:int, q:int, lag:int,t):
    return tail_mark(n,t)*(1-t**(8*q))*(1-t**(8*lag))


def upper_one_mark_square(n:int)->Fraction:
    # g(t)<=1-t, integral of (1-t)^2 t^(16n)
    return Fraction(2,(16*n+1)*(16*n+2)*(16*n+3))


def upper_bernoulli_one_mark_square(n:int)->Fraction:
    # E[(C t^(8n))^2] = T_(2n) <= integral (1-t) t^(16n)
    return Fraction(1,(16*n+1)*(16*n+2))


def upper_rb_two_diff_square(n:int, lag:int)->Fraction:
    # |1-t^(8lag)|<=8lag(1-t)
    denom=1
    for j in range(1,6):denom*=16*n+j
    return Fraction(64*lag**2*24,denom)


def upper_rb_four_diff_square(n:int,q:int,lag:int)->tuple[Fraction,Fraction]:
    # Uniform-q and fixed-q bounds, respectively
    a=upper_rb_two_diff_square(n,lag)
    denom=1
    for j in range(1,8):denom*=16*n+j
    b=Fraction((64*q*lag)**2*720,denom)
    return a,b


def upper_four_diff_mean(n:int,q:int,lag:int)->tuple[Fraction,Fraction]:
    # Uniform-q and fixed-q bounds for positive Delta_q Delta_lag T_n.
    denom3=1
    for j in range(1,4):denom3*=8*n+j
    denom4=denom3*(8*n+4)
    return Fraction(16*lag,denom3), Fraction(64*q*lag*6,denom4)


def coin_gram_interval(n:int,m:int,depth:int=24):
    """E[(C*tau^(8n))(C*tau^(8m))] = T_(n+m), C^2=C."""
    return tail_interval(n+m,depth)


def coin_two_diff_square_interval(n:int,lag:int,depth:int=32):
    # T_(2n)-2T_(2n+lag)+T_(2n+2lag)
    lo=hi=Fraction()
    for s,index in ((1,2*n),(-2,2*n+lag),(1,2*n+2*lag)):
        a,b=tail_interval(index,depth)
        if s>0:lo+=s*a;hi+=s*b
        else:lo+=s*b;hi+=s*a
    return lo,hi


def source_gauge(n:int)->tuple[Fraction,Fraction,Fraction]:
    """Coboundary test tilde r=r+g(n)-16g(n-1) with g(n)=2n^2."""
    orig=mut=Fraction();sum_o=sum_m=Fraction()
    for j in range(1,n+1):
        g_j=2*j*j;g_prior=2*(j-1)**2
        orig=16*orig+forcing(j)
        mut=16*mut+forcing(j)+g_j-16*g_prior
        sum_o+=forcing(j)/16**j
        sum_m+=(forcing(j)+g_j-16*g_prior)/16**j
    return mut-orig,sum_m-sum_o,Fraction(2*n*n,16**n)


def poisson_path_theory(source_amplitude_integral:complex, source_square_integral:float, real_prefix:float, harmonic:int, rate:float):
    """Exact phase and variance furnished by marked Poisson product PGFL."""
    from cmath import exp,pi
    if rate<=0:raise ValueError('rate > 0')
    c=2*pi*harmonic
    mean=exp(1j*c*(real_prefix+source_amplitude_integral))
    variance=exp(c*c*source_square_integral/rate).real-1
    return mean,variance


def weighted_sum_interval(indices:list[int],weights:list[int],depth:int=24):
    if len(indices)!=len(weights):raise ValueError('length mismatch')
    low=high=Fraction()
    for idx,s in zip(indices,weights):
        a,b=tail_interval(idx,depth)
        if s>=0:low+=s*a;high+=s*b
        else:low+=s*b;high+=s*a
    return low,high


def phase_transport_source_tail_budget(n:int):
    """Exact rational bound for T_n; multiply by 2*pi*|h| for phase distance."""
    return tail_interval(n,0)[1]


def original_operator_forcing_integral(n:int)->Fraction:
    """E[(16-tau^8) C tau^(8(n-1))] = r(n), C the BBP coin.

    The (16-L) operator on the conditional source mark cancels its resolvent
    denominator pointwise after conditional expectation.
    """
    if n<1:raise ValueError('n>=1')
    j=n-1
    return (Fraction(4,8*j+1)-Fraction(2,8*j+4)
            -Fraction(1,8*j+5)-Fraction(1,8*j+6))


def operator_telescoping_residual(n:int)->Fraction:
    """Finite (16-L) resolvent identity, tested via exact source coefficients."""
    return source_u(n)-sum((16**(n-j)*original_operator_forcing_integral(j)
                            for j in range(1,n+1)),Fraction())


def chiral_green_energy_interval(n:int,k:int,depth:int=35):
    """E[ (sum_(j=0)^k binom(k,j) chi(n+2j) C*tau^(8(n+2j)))^2 ].

    = sum_(a=0)^(2k) (-1)^a binom(2k,a) T_(2n+2a), strictly positive.
    """
    from math import comb
    if n<0 or k<0:raise ValueError('n,k >= 0')
    return weighted_sum_interval([2*n+2*j for j in range(2*k+1)],
                                 [(-1)**j*comb(2*k,j) for j in range(2*k+1)],depth)


def sample_pi_coin(rng):
    """Exactly the screenshot's pi-free finite sampler, one source row.

    Returns (tau, clicked) with P(clicked=1|tau)=Q(tau)/(16-tau**8).
    NOTE: no pi target value occurs in this random program.
    """
    t=rng.random()
    a=int(rng.random()>t)
    b=2+int(max(rng.random(),rng.random())<=t)
    c=2+2*int(rng.random()<=t)+int(max(rng.random(),rng.random())<=t)
    click=int(rng.random()<=a*b*c/(16-t**8))
    return t,click


def poisson_count(rate,rng):
    """Poisson count by exponential waiting times; rate is expected count."""
    if rate<=0:raise ValueError('rate>0')
    elapsed=0.; count=0
    while True:
        elapsed+=rng.expovariate(1.0)
        if elapsed>rate:return count
        count+=1


def phase_product_sample(n:int,h:int,rate:float,rng):
    """Complex, nonunitary unbiased phase estimator from source-only marks.

    Its expectation, not individual samples, is e( h*[U_n+T_n] ).
    """
    import cmath
    from math import pi
    u=source_u(n)%1
    val=cmath.exp(2j*pi*h*float(u))
    for _ in range(poisson_count(rate,rng)):
        tau,coin=sample_pi_coin(rng)
        val*=1+2j*pi*h*coin*(tau**(8*n))/rate
    return val


def four_tap_phase_sample(n:int,q:int,lag:int,h:int,rate:float,rng):
    """Full original 4-time phase e(h Delta_q Delta_lag (U+T)), no pi target."""
    import cmath
    from math import pi
    rational_lift=(source_u(n+q+lag)-source_u(n+q)
                   -source_u(n+lag)+source_u(n))%1
    val=cmath.exp(2j*pi*h*float(rational_lift))
    for _ in range(poisson_count(rate,rng)):
        tau,coin=sample_pi_coin(rng)
        val*=1+(2j*pi*h/rate)*(coin*tau**(8*n)
                                 *(1-tau**(8*q))*(1-tau**(8*lag)))
    return val


def sample_oily_frequency(rng):
    """Exactly q_h=(h+1)/(3*2**h), h>=1, via conditioned two-geometric law."""
    while True:
        h=0
        for _ in range(2):
            while not rng.getrandbits(1):
                h+=1
        if h>=1:return h


def common_shell_phase_sample(B:int,h:int,base_rate:float,rng):
    """One source-quenched Poisson field reused for every n in one original shell."""
    from math import pi
    import cmath
    if B<1 or h<1 or base_rate<=0:raise ValueError('B,h,base_rate must be >0')
    rate=base_rate*h*h
    marks=[sample_pi_coin(rng) for _ in range(poisson_count(rate,rng))]
    amp=0j
    for n in range(B,2*B):
        frac=source_u(n)%1
        z=cmath.exp(2j*pi*h*float(frac))
        for tau,coin in marks:
            z*=1+(2j*pi*h/rate)*coin*tau**(8*n)
        amp+=z
    return amp/B


def all_mode_oily_pair_sample(B:int,base_rate:float,rng):
    """Unbiased estimator of q-weighted full positive Weyl energy C_B.

    Conditional on H, the *two* coherent Poisson shell estimates are independent.
    The real sample can be negative despite a nonnegative expectation.
    """
    h=sample_oily_frequency(rng)
    a=common_shell_phase_sample(B,h,base_rate,rng)
    b=common_shell_phase_sample(B,h,base_rate,rng)
    return (a*b.conjugate()).real,h


def oily_moments():
    """Exact moments of (h+1)/(3*2**h), positive integer h."""
    return Fraction(8,3),Fraction(32,3)
