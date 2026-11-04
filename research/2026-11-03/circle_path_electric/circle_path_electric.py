"""Exact original BBP circle path/current instruments (research only).

Normality, actual quantum Feynman amplitudes and physical lightning NOT claimed.
The original four signed source terms and literal zero seed are immutable.
"""
from __future__ import annotations
from fractions import Fraction as Q
from collections import Counter
from math import lcm

RADIX = 16


def authentic_r(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("original BBP time n must be a positive integer")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def phase_stream(last_n: int):
    """Source-faithful exact Q/Z sequence using original four-pole recurrence."""
    if type(last_n) is not int or last_n < 0:
        raise ValueError("nonnegative integer horizon required")
    x = Q(0)
    yield 0, x
    for n in range(1, last_n+1):
        x = (16*x + authentic_r(n)) % 1
        if x.denominator % 2 != 1:
            raise AssertionError("Original phase denominator is not odd")
        yield n, x


def source_odd_predecessor(y: Q, forcing: Q=Q(0)) -> tuple[int, Q]:
    """Unique x in Q_odd/Z with 16*x+forcing=y mod 1.

    z=(y-forcing) mod1=a/M, M odd. Only j with a+j*M=0 mod16
    allows x=(z+j)/16 to have odd reduced denominator.
    """
    y, forcing = Q(y), Q(forcing)
    z = (y-forcing)%1
    if z.denominator % 2 != 1:
        raise ValueError("y-forcing must have odd reduced denominator")
    a, M = z.numerator, z.denominator
    j=(-a*pow(M,-1,16))%16
    x=(z+j)/16
    assert x.denominator % 2 == 1
    assert (16*x+forcing-y)%1 == 0
    return j, x


def inverse_candidates(y: Q, forcing: Q=Q(0)) -> tuple[Q,...]:
    z=(Q(y)-Q(forcing))%1
    return tuple((z+j)/16 for j in range(16))


def cyclotomic16_character_sum(delta: int) -> tuple[int,...]:
    """Coefficient vector in Z[zeta_16]=Z[X]/(X^8+1).

    Exactly equals (16,0,...,0) iff delta=0 mod16 and zero otherwise.
    No approximate complex arithmetic is used.
    """
    if type(delta) is not int:
        raise TypeError("integer residue required")
    coefficients=[0]*8
    for q in range(16):
        j=(q*delta)%16
        coefficients[j%8] += 1 if j<8 else -1
    return tuple(coefficients)


def selector_weights(selected: int) -> tuple[int,...]:
    """Fourier-projector coefficients for the selected inverse branch.

    Each weight is Z[zeta_16] 1/16 * sum_q zeta^(q*(j-selected));
    all 16 characters remain in the symbolic definition.
    """
    if type(selected) is not int or not 0 <= selected < 16:
        raise ValueError("branch selected in 0..15")
    return tuple(cyclotomic16_character_sum(j-selected)[0]//16 for j in range(16))


def transfer_frequency(h: int) -> tuple[bool,int|None]:
    """L_r(e_h) is 0 unless 16 | h; if yes it is e_{h/16}(y-r)."""
    if type(h) is not int:
        raise TypeError("integer harmonic")
    return (h%16 == 0, h//16 if h%16 == 0 else None)


def transfer_depth_frequency(h:int,depth:int)->tuple[bool,int|None]:
    if type(depth) is not int or depth<0:
        raise ValueError("depth nonnegative")
    if type(h) is not int:
        raise TypeError("h integer")
    m=16**depth
    return (h % m ==0, h//m if h%m==0 else None)


def cylinder_histogram(phases:tuple[Q,...],depth:int)->dict[int,int]:
    """Base16 cylinder counts with half-open bins (exact Fraction)."""
    if type(depth) is not int or depth<0:
        raise ValueError("depth nonnegative")
    if not phases:
        raise ValueError("nonempty phase cloud")
    m=16**depth
    counts=Counter()
    for p in phases:
        x=Q(p)%1
        idx=(m*x).numerator//(m*x).denominator
        if not 0<=idx<m:
            raise AssertionError("bin out of bounds")
        counts[idx]+=1
    return dict(counts)


def collision_energy(phases:tuple[Q,...],depth:int)->Q:
    """Original-source 16^depth/A^2 sum of exact cylinder-count squares."""
    h=cylinder_histogram(phases,depth)
    A=len(phases)
    return Q(16**depth*sum(v*v for v in h.values()),A*A)


def branching_dissipation(phases:tuple[Q,...],level:int)->Q:
    """Exactly 16^(k+1)*sum_{|w|=k,j}(mu(wj)-mu(w)/16)^2.

    Counts at absent children are implicitly included using the parent norm.
    """
    p=cylinder_histogram(phases,level)
    c=cylinder_histogram(phases,level+1)
    A=len(phases)
    val=Q(16**(level+1)*sum(z*z for z in c.values()),A*A) - Q(16**level*sum(z*z for z in p.values()),A*A)
    if val<0:raise AssertionError("negative current deviation")
    return val


def exact_dissipation_sum(phases:tuple[Q,...],depth:int)->Q:
    return sum((branching_dissipation(phases,k) for k in range(depth)),Q(0))


def explicit_branch_dissipation(phases:tuple[Q,...],level:int)->Q:
    """Independent full 16-child local-splitting calculation."""
    parents=cylinder_histogram(phases,level)
    children=cylinder_histogram(phases,level+1)
    N=len(phases)
    return 16**(level+1)*sum(((Q(children.get(16*w+j,0),N)-Q(v,16*N))**2
                              for w,v in parents.items() for j in range(16)),Q(0))


def empirical_source_epoch(A:int)->tuple[Q,...]:
    if type(A) is not int or A<1:
        raise ValueError("positive epoch")
    return tuple(x for n,x in phase_stream(2*A-1) if n>=A)


def homogeneous_tree_unit_resistance(depth:int)->Q:
    """Root-to-depth effective resistance for a homogeneous 16-ary tree."""
    if type(depth) is not int or depth<0:
        raise ValueError("nonnegative depth")
    return sum((Q(1,16**k) for k in range(1,depth+1)),Q(0))


def coherent_fifth(depth:int)->Q:
    """T(1/5)=1/5, but 16^k-cylinder empirical energy is 16^k."""
    return collision_energy((Q(1,5),)*16,depth)


def original_inverse_receipt(n:int)->dict:
    if type(n) is not int or n<1:
        raise ValueError("original positive source time")
    x0=x1=Q(0)
    for j in range(1,n+1):
        x0=x1
        x1=(16*x1+authentic_r(j))%1
    digit,back=source_odd_predecessor(x1,authentic_r(n))
    return {'n':n,'current':x1,'previous':x0,'selected_digit':digit,
            'floor_digit':int(16*x0),'same':back==x0,
            'predecessor':back,'candidate_integral_count':sum(t.denominator%2==1 for t in inverse_candidates(x1,authentic_r(n)))}


def modular_phase_stream(last_n: int):
    """Second exact original-source oracle: one common odd denominator, integer ring.

    Intentionally independent of Fraction phase recurrence; it retains the
    entire original conductor and all four source terms. Not pi digits.
    """
    if type(last_n) is not int or last_n<0:
        raise ValueError("nonnegative integer horizon")
    sources=tuple(authentic_r(n) for n in range(1,last_n+1))
    M=1
    for a in sources:
        M=lcm(M,a.denominator)
    if M%2==0:
        raise AssertionError("original conductor must be odd")
    z=0
    yield 0,Q(0)
    for n,r in enumerate(sources,1):
        z=(16*z+r.numerator*(M//r.denominator))%M
        yield n,Q(z,M)
