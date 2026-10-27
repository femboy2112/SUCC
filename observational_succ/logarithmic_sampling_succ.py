"""Exact rational source and polynomial oracle for logarithmic SUCC sampling.

The logarithmic deformed Dirac comb and sawtooth identity are proved in
research/2026-10-27/BBP_LOG_DIRAC_SAWTOOTH_THREAD.md. Finite Fraction
checks are controls, NOT proofs of infinite asymptotics or pi normality.

Original four-pole source and U0=0 are invariant. The exact log shifts
are defined mathematically; rational prefix epsilon is its reproducible
finite approximation and is not a logarithm oracle.
"""
from __future__ import annotations

from fractions import Fraction as Q
from typing import Sequence

SOURCE_TAG = 'original signed four-pole BBP, U0=0'
BASE = 16


def _natural(value: int, *, least=0, most=1000) -> int:
    if type(value) is not int or not least <= value <= most:
        raise ValueError(f'expected integer in [{least},{most}]')
    return value


def source_r(n: int) -> Q:
    _natural(n, least=1, most=100000)
    return (Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2))


def canceled_source_r(n: int) -> Q:
    _natural(n, least=1, most=100000)
    return Q(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def states_through(k: int) -> tuple[Q, ...]:
    """Exact original source states U0..Uk."""
    _natural(k,most=1000)
    states=[Q(0)]
    for j in range(1,k+1):
        states.append(BASE*states[-1]+source_r(j))
    return tuple(states)


def pi_prefix(k: int) -> Q:
    """Exact partial BBP identity for pi, no float evaluation."""
    _natural(k,least=1,most=1000)
    return sum((Q(1,BASE**(j-1))*source_r(j)
                for j in range(1,k+1)),Q())


def finite_green_tail(n: int, cutoff: int) -> Q:
    """Finite Green tail sum_{j=n+1..cutoff}16^(n-j) r(j)."""
    _natural(n,least=1,most=1000)
    _natural(cutoff,least=n,most=1000)
    return sum((Q(1,BASE**(j-n))*source_r(j)
                for j in range(n+1,cutoff+1)),Q())


def source_log_shift_ratio(time_index: int, cutoff: int) -> Q:
    """Exact epsilon for finite pi_cutoff in t_n=n log16 + log(1-epsilon).

    In the actual infinite identity, epsilon=T_(n+1)/(pi*16**n).
    Positive finite rational surrogate uses pi_cutoff and T^(cutoff)_(n+1).
    """
    _natural(time_index,most=998)
    _natural(cutoff,least=time_index+1,most=1000)
    T=finite_green_tail(time_index+1,cutoff)
    piL=pi_prefix(cutoff)
    eps=T/(piL*BASE**time_index)
    if not 0 <= eps < 1:
        raise ArithmeticError('invalid positive logarithmic source chart')
    return eps


def log_shift_bounds_from_rational_epsilon(epsilon: Q) -> tuple[Q,Q]:
    """For 0<=e<1: e <= -log(1-e) <= e/(1-e)."""
    if type(epsilon) not in (Q,int) or not 0 <= epsilon < 1:
        raise ValueError('requires exact epsilon in [0,1)')
    e=Q(epsilon)
    return e, e/(1-e)


def _poly(coefficients: Sequence[Q|int]) -> tuple[Q,...]:
    c=tuple(Q(x) if type(x) in (Q,int) else None for x in coefficients)
    if not c or any(x is None for x in c):
        raise ValueError('nonempty exact polynomial coefficient list required')
    return c


def polynomial_at(coefficients: Sequence[Q|int], x: Q|int) -> Q:
    c=_poly(coefficients)
    if type(x) not in (Q,int):
        raise ValueError('exact rational argument required')
    ans=Q()
    for coefficient in reversed(c):
        ans=Q(x)*ans+coefficient
    return ans


def polynomial_integral(coefficients: Sequence[Q|int], lo: Q|int, hi: Q|int) -> Q:
    c=_poly(coefficients)
    if type(lo) not in (Q,int) or type(hi) not in (Q,int):
        raise ValueError('exact rational endpoints required')
    lo,hi=Q(lo),Q(hi)
    return sum((q*(hi**(j+1)-lo**(j+1))/(j+1)
                for j,q in enumerate(c)),Q())


def polynomial_derivative(coefficients: Sequence[Q|int]) -> tuple[Q,...]:
    c=_poly(coefficients)
    return tuple((j*c[j] for j in range(1,len(c)))) or (Q(0),)


def sawtooth_integral_exact(coefficients: Sequence[Q|int], step: Q|int, count: int) -> Q:
    """Integral_0^(N*a) ({t/a}-1/2) f'(t) dt, exact for polynomials."""
    c=_poly(coefficients)
    if type(step) not in (Q,int) or Q(step)<=0:
        raise ValueError('positive exact logarithmic clock step required')
    _natural(count,least=1,most=1000)
    d=polynomial_derivative(c)
    step=Q(step)
    td=(Q(0),)+d
    total=Q()
    for j in range(count):
        low,high=j*step,(j+1)*step
        base=(polynomial_integral(td,low,high)-low*polynomial_integral(d,low,high))/step
        total+=base-Q(1,2)*polynomial_integral(d,low,high)
    return total


def exact_weighted_sampling_identity(coefficients: Sequence[Q|int],
                                     step: Q|int,
                                     shifts: Sequence[Q|int]) -> dict[str,Q]:
    """Finite distributional identity against every polynomial test f.

    Sample sites are t_j=j*step-shifts[j]. Output verifies
      sum f(t_j) - (1/step) int_0^(N step) f
      = (f(0)-f(N step))/2 + int P_a f' - int H_N f'
    where H_N(t)=sum_j 1_[t_j,j step)(t) for shifts>=0.
    No statistical law or pi normality is involved.
    """
    c=_poly(coefficients)
    if type(step) not in (Q,int) or Q(step)<=0:
        raise ValueError('positive rational step required')
    a=Q(step)
    ds=tuple(Q(x) if type(x) in (Q,int) else None for x in shifts)
    if not ds or any(x is None or x<0 for x in ds):
        raise ValueError('nonempty nonnegative rational sampling shifts required')
    N=len(ds)
    _natural(N,least=1,most=1000)
    sample=sum((polynomial_at(c,j*a-d) for j,d in enumerate(ds)),Q())
    continuum=polynomial_integral(c,0,N*a)/a
    boundary=(polynomial_at(c,0)-polynomial_at(c,N*a))/2
    sawtooth=sawtooth_integral_exact(c,a,N)
    derivative=polynomial_derivative(c)
    pulses=sum((polynomial_integral(derivative,j*a-d,j*a)
                for j,d in enumerate(ds)),Q())
    rhs=boundary+sawtooth-pulses
    return {'sample':sample,'continuous':continuum,'boundary':boundary,
            'sawtooth':sawtooth,'source_pulse':pulses,
            'defect_left':sample-continuum,'defect_right':rhs}


CHIRAL_PLUS=(Q(4),Q(2),Q(0),Q(-1),Q(-1),Q(-1,2),Q(0),Q(1,4))
CHIRAL_MINUS=(Q(0),Q(-2),Q(0),Q(-1),Q(0),Q(-1,2),Q(0),Q(-1,4))


def chiral_source(n: int, chirality: str) -> Q:
    """Independent source decomposition from sibling PR #333."""
    _natural(n,least=1,most=100000)
    if chirality not in ('+', '-'):
        raise ValueError('chirality must be + or -')
    taps=CHIRAL_PLUS if chirality=='+' else CHIRAL_MINUS
    return sum((c/Q(8*(n-1)+j+1)
                for j,c in enumerate(taps)),Q())



def chiral_harmonic_counterterm(n:int, chirality:str) -> Q:
    """Exact O(n^-2) counterterm r_+ - 15/(32n), r_- + 15/(32n).

    Consequently each chiral sum has an explicit harmonic-divergent part;
    the opposite Euler--Mascheroni terms cancel upon source gluing.
    """
    _natural(n,least=1,most=100000)
    if chirality not in ('+','-'):
        raise ValueError('chirality must be + or -')
    sign=1 if chirality=='+' else -1
    return chiral_source(n,chirality)-sign*Q(15,32*n)


def chiral_harmonic_remainder_constant_bound(chirality:str) -> Q:
    """Rigorous C/N tail coefficient for sum of harmonic counterterms.

    For n>=2, |r_ch(n)-mass/(8n)| <= C/n^2, with
    C=sum_j |c_j|*(7-j)/32. Thus infinite remainder beyond N>=1
    has modulus <= C/N. This is NOT the value of the finite part.
    """
    if chirality not in ('+','-'):
        raise ValueError('chirality must be + or -')
    taps=CHIRAL_PLUS if chirality=='+' else CHIRAL_MINUS
    return sum((abs(c)*(7-j) for j,c in enumerate(taps)),Q())/32


def chiral_harmonic_prefix(n:int,chirality:str) -> dict[str,Q]:
    """Exact finite source/harmonic decomposition; no numerical gamma input."""
    _natural(n,least=1,most=1000)
    if chirality not in ('+','-'):
        raise ValueError('chirality must be + or -')
    sign=1 if chirality=='+' else -1
    H=sum((Q(1,k) for k in range(1,n+1)),Q())
    raw=sum((chiral_source(k,chirality) for k in range(1,n+1)),Q())
    remainder=sum((chiral_harmonic_counterterm(k,chirality)
                   for k in range(1,n+1)),Q())
    assert raw==sign*Q(15,32)*H+remainder
    return {'raw':raw,'harmonic':H,'counterterm_sum':remainder}


def asymptotic_weight_equivalence(weights: Sequence[Q|int], limit: Q|int) -> Q:
    """Exact universal phase-independent normalized upper bound.

    For any |z_n|<=1, |N^-1 sum weights_n*z_n - limit*N^-1 sum z_n|
    <= N^-1 sum |weights_n-limit|.
    """
    if type(limit) not in (Q,int):
        raise ValueError('exact scalar limit required')
    ws=_poly(weights)
    return sum((abs(w-Q(limit)) for w in ws),Q())/len(ws)


def source_phase_tail_bound(start_index:int,h:int) -> Q:
    """Certified rational upper bound for |sum_{n>=N} source phase correction|.

    Uses 2*pi<44/7 and T_(n+1)<1/[15(n+2)^2], hence
    |sum_{n>=N} e(h*pi*16^n)(e(-h*T_(n+1))-1)|
      <=44*|h|/[105*(N+1)]. This bounds complex modulus, not
    the exact signed constant itself.
    """
    _natural(start_index,most=1000000)
    if type(h) is not int:
        raise ValueError('integer Fourier mode required')
    return Q(44*abs(h),105*(start_index+1))


def source_log_shift_universal_upper(time_index:int) -> Q:
    """Rigorous d_n=-log(1-epsilon_n) <= upper rational from pi>3."""
    _natural(time_index,most=1000000)
    e=Q(1,45*BASE**time_index*(time_index+2)**2)
    return e/(1-e)
