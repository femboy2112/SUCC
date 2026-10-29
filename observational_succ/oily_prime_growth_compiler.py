"""Exact source-typed online Oily packet / prime-zeta split compiler.

All finite-path probabilities are Fraction values.  This module gives
conditional causal realizations, NOT a physical sensor, optimal knowledge,
RH, or signed-BBP phase equidistribution theorem.

Sources: SUCC original Oily u(x)=x-x^2/2, v(x)=x^2/2 and the earlier
source-locked n=ab divisor fibers.  No archived source is modified.
"""
from __future__ import annotations
from fractions import Fraction as F


def _f(v):
    if type(v) not in (F, int):
        raise TypeError('integer/Fraction input required')
    return F(v)


def rates(x):
    x=_f(x)
    if not F(0) <= x <= F(1):
        raise ValueError('authentic Oily parameter x must be in [0,1]')
    return x-x*x/2, x*x/2


def split_sum(u,v,j):
    u,v=map(_f,(u,v))
    if type(j) is not int or j<0 or u<0 or v<0:
        raise ValueError('nonnegative rational rates and integer grade required')
    return sum((u**k*v**(j-k) for k in range(j+1)),F(0))


def oily_joint(x,j,k):
    u,v=rates(x)
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('grade j>=0, first-channel occupancy 0<=k<=j')
    return (1-u)*(1-v)*u**k*v**(j-k)


def oily_grade(x,j):
    u,v=rates(x)
    return (1-u)*(1-v)*split_sum(u,v,j)


def grade_survival(x,j):
    """P(J>=j) for exactly two geometric delays, without infinite sums."""
    u,v=rates(x)
    if type(j) is not int or j<0:
        raise ValueError('nonnegative grade required')
    if u==v:
        return u**j*((j+1)-j*u)
    return ((1-v)*u**(j+1)-(1-u)*v**(j+1))/(u-v)


def stop_probability(x,j):
    """Hazard P(J=j|J>=j), depending on grade (not split)."""
    r=grade_survival(x,j)
    return oily_grade(x,j)/r if r else F(1)


def conditional_split(x,j,k):
    """P(K=k|J=j); x=0 has only grade zero."""
    u,v=rates(x)
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('valid grade/split required')
    total=split_sum(u,v,j)
    if not total:
        raise ValueError('conditional grade has zero probability')
    return u**k*v**(j-k)/total


def unique_local_birth_probability(x,j,k):
    """Unique nearest-neighbor split-preserving chance of K->K+1.

    Given conditional grade laws mu_j(k), no mass can leave the interval
    [0,j+1]. CDF conservation yields a=(F_j(k)-F_(j+1)(k))/mu_j(k).
    Its closed formula is sum_{r=0}^k u^{j+1-r}v^r / h_(j+1).
    Nondegenerate x>0; for x=0 the birth state is never reached.
    """
    u,v=rates(x)
    if x==0:
        raise ValueError('x=0 stops at grade zero; birth is unreachable')
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('valid grade/split required')
    return sum((u**(j+1-r)*v**r for r in range(k+1)),F(0))/split_sum(u,v,j+1)


def unique_birth_cdf(x,j,k):
    """Independently derived CDF flux construction for the same birth rule."""
    if x==0:
        raise ValueError('x=0 birth unreachable')
    F_j=sum((conditional_split(x,j,i) for i in range(k+1)),F(0))
    F_next=sum((conditional_split(x,j+1,i) for i in range(k+1)),F(0))
    return (F_j-F_next)/conditional_split(x,j,k)


def critical_oily_stop(j):
    if type(j) is not int or j<0:
        raise ValueError('grade required')
    return F(j+1,2*(j+2))


def polya_birth(j,k):
    """Exactly Pólya urn one-red-one-blue transition."""
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('valid grade/split required')
    return F(k+1,j+2)


def zeta_prime_joint(q,j,k):
    """Original one-mode geometric prior plus origin-locked uniform split."""
    q=_f(q)
    if not 0<q<1 or type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('0<q<1, j>=0, k in [0,j]')
    return (1-q)*q**j/F(j+1)


def oily_balanced_joint(q,j,k):
    """Two independent equal-rate geometries: split uniform given grade."""
    q=_f(q)
    if not 0<q<1 or type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('0<q<1, j>=0, k in [0,j]')
    return (1-q)**2*q**j


def balanced_stop(q,j):
    q=_f(q)
    if not 0<q<1 or type(j) is not int or j<0:
        raise ValueError('0<q<1 and j>=0')
    return F(j+1)*(1-q)**2/((j+1)-j*q)


def grade_sizebias_ratio(q,j):
    """d P_two-mode / d P_origin-locked at one fixed prime and grade."""
    q=_f(q)
    if not 0<q<1 or type(j) is not int or j<0:
        raise ValueError('0<q<1, j>=0')
    return (j+1)*(1-q)


def sequential_joint_oily(x,max_j):
    """Exact finite online construction, output terminal and surviving masses.

    At each grade stop independently of k; if continuing, use unique
    nearest-neighbor allocation.  Distribution at EVERY finite stage equals
    original Oily grade/split joint conditional on survival.
    """
    if type(max_j) is not int or not 0<=max_j<=100:
        raise ValueError('max_j from 0 to 100')
    active={0:F(1)}; terminal={}
    for j in range(max_j+1):
        h=stop_probability(x,j)
        for k,m in active.items(): terminal[j,k]=m*h
        next_active={k:F(0) for k in range(j+2)}
        if j<max_j and h<1:
            for k,m in active.items():
                a=unique_local_birth_probability(x,j,k)
                next_active[k] += m*(1-h)*(1-a)
                next_active[k+1] += m*(1-h)*a
        if j<max_j:
            active=next_active
    return terminal


def sequential_joint_zeta(q,max_j):
    if type(max_j) is not int or not 0<=max_j<=100:
        raise ValueError('max_j from 0 to 100')
    q=_f(q)
    if not 0<q<1:
        raise ValueError('q in (0,1)')
    active={0:F(1)}; terminal={}
    for j in range(max_j+1):
        for k,m in active.items(): terminal[j,k]=m*(1-q)
        if j<max_j:
            nxt={k:F(0) for k in range(j+2)}
            for k,m in active.items():
                a=polya_birth(j,k)
                nxt[k]+=m*q*(1-a)
                nxt[k+1]+=m*q*a
            active=nxt
    return terminal


def critical_joint(j,k):
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('grade and split')
    return F(1,2**(j+2))


def naive_polya_amplitude_compression_squared(j):
    """K_j acting LINEARLY on a normalized uniform AMPLITUDE vector.

    K_j is a column-stochastic classical transition, NOT a quantum
    isometry.  K_j omega_j=sqrt((j+1)/(j+2)) omega_(j+1),
    so the norm-squared is (j+1)/(j+2).  The *classical probability*
    distribution, by contrast, is preserved exactly.
    """
    if type(j) is not int or j<0:
        raise ValueError('j>=0')
    return F(j+1,j+2)


def amplitude_row_sums(j):
    """Each output row sum of K_j equals (j+1)/(j+2), exactly."""
    if type(j) is not int or j<0:
        raise ValueError('j>=0')
    out=[F(0)]*(j+2)
    for k in range(j+1):
        a=polya_birth(j,k)
        out[k]+=(1-a)
        out[k+1]+=a
    return tuple(out)


def terminal_coherence_product(depth):
    """Product of coherent squared losses through j=0,...,depth-1."""
    if type(depth) is not int or depth<0:
        raise ValueError('nonnegative depth required')
    out=F(1)
    for j in range(depth):
        out *= naive_polya_amplitude_compression_squared(j)
    return out


def zeta_prime_tail_coupling_bound(beta, prime_cutoff):
    """Rational TV upper bound for all-prime zeta prior truncation.

    Prime exponents J_p are independent Geom(q_p), q_p=p^(-beta), for
    beta>1. Fixing all p>prime_cutoff to zero agrees with the full model
    except when some tail prime occurs, whose probability is bounded by
    sum_(p>cutoff) p^-beta <= cutoff^(1-beta)/(beta-1).
    Integer beta>=2 restriction ensures the returned certificate rational.
    """
    if type(beta) is not int or beta<2 or type(prime_cutoff) is not int or prime_cutoff<2:
        raise ValueError('integer beta>=2, cutoff>=2 required')
    return F(1,(beta-1)*prime_cutoff**(beta-1))
