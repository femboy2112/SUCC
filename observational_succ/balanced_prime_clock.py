"""Balanced 12/5 prime clocks for three-channel BBP chronology (research only).

Exact modular residues, counts and rational stage weights.  Complex Fourier
quantities here are finite diagnostics, not a certificate of pi normality.
"""
from collections import Counter
from fractions import Fraction as F
from math import isqrt, pi, log, sqrt
from cmath import exp

from .three_channel_prime_tomography import (
    valid_clock, is_prime, stage_vectors, reduce_fraction, channel_forcing,
    multiplicative_order_16, predicted_residues,
)


def epoch_stage_boundaries(A, p):
    """[A,2A) split by the three later genuine p-pole births.

    Requiring 9A/4 <= p <= 5A/2 excludes any unobserved channel and
    ensures the entire original epoch is inside the FIRST simple-pole shell.
    """
    if type(A) is not int or A < 16:
        raise ValueError('A must be integer >=16')
    k = valid_clock(p)
    if not 9*A <= 4*p or not 2*p <= 5*A:
        raise ValueError('balanced p must satisfy 9A/4 <= p <= 5A/2')
    first = k + 1
    e2, e3, e4 = 4*k+1, 5*k+1, 6*k+1
    if not first <= A < e2 < e3 < e4 < 2*A <= first + p:
        raise ValueError('epoch does not cross precisely the three later births')
    return (A,e2,e3,e4,2*A)


def epoch_stage_lengths(A, p):
    bounds = epoch_stage_boundaries(A, p)
    return tuple(bounds[i+1]-bounds[i] for i in range(4))


def epoch_stage_weights(A, p):
    return tuple(F(length,A) for length in epoch_stage_lengths(A,p))


def epoch_mode_coefficients(p, h, mode):
    if type(h) is not int or type(mode) is not tuple or len(mode) != 3 or any(type(x) is not int for x in mode):
        raise ValueError('integer harmonic and length-three integer mode required')
    valid_clock(p)
    return tuple(reduce_fraction(h*sum(t*x for t,x in zip(mode,v)),p)
                 for v in stage_vectors(0))


def epoch_mode_resonance_mass(A,p,h,mode):
    c = epoch_mode_coefficients(p,h,mode)
    weights = epoch_stage_weights(A,p)
    return sum((w for w,x in zip(weights,c) if x == 0), F(0))


def epoch_histogram_from_stage(A,p,h,mode):
    """Exact p-Fourier scalar phase histogram, no floating-point assumptions."""
    bounds = epoch_stage_boundaries(A,p)
    coeffs = epoch_mode_coefficients(p,h,mode)
    b0 = (p-1)//8 + 1
    out = Counter()
    for i in range(4):
        c = coeffs[i]
        for n in range(bounds[i], bounds[i+1]):
            out[c*pow(16,n-b0,p)%p] += 1
    return out


def epoch_histogram_from_residues(A,p,h,mode):
    """Separate source-channel modular-state route for finite comparison."""
    epoch_stage_boundaries(A,p)
    out = Counter()
    for n in range(A,2*A):
        v = predicted_residues(p,n)
        out[h*sum(t*x for t,x in zip(mode,v)) % p] += 1
    return out


def epoch_complete_cycles_and_remainders(A,p):
    """Exact periods and incomplete lengths for all four chronological stages."""
    m = multiplicative_order_16(p)
    return tuple(divmod(length,m) for length in epoch_stage_lengths(A,p))


def unbalanced_pr4A_channels_locked(A,p):
    """Certify equality C4=C5 at ALL original epoch times near p=4A.

    Condition applies to first complete simple-pole shell and requires
    the initial common birth by A and the channel-4 birth after 2A.
    """
    if type(A) is not int or A < 16:raise ValueError('integer A>=16')
    k = valid_clock(p)
    b = k+1
    return b <= A and 2*A <= 5*k+1 and 2*A <= b+p


def prime_candidates(A, nearest=F(12,5), require_strong_order=True):
    """Enumerate *finite* balanced prime clocks, sorted by target distance.

    Asymptotic existence is the separate paper theorem; this routine does
    not promise a numerical onset or infer an analytic PNT bound from tests.
    """
    if type(A) is not int or A < 16:raise ValueError('A>=16')
    lo=(9*A+3)//4
    hi=(5*A)//2
    out=[]
    for p in range(lo,hi+1):
        if p%8 != 1 or not is_prime(p):continue
        m=multiplicative_order_16(p)
        bits=p.bit_length()
        if require_strong_order and not (m**3 > p and m**2 * bits**4 > p):
            continue
        try:epoch_stage_boundaries(A,p)
        except ValueError:continue
        out.append((p,m))
    return tuple(sorted(out,key=lambda pair:(abs(F(pair[0])-nearest*A),pair[0])))


def epoch_phase_gram(A,p,h=1):
    """Finite Hermitian phase Gram; complex double values are diagnostics."""
    epoch_stage_boundaries(A,p)
    sums=[[0j]*3 for _ in range(3)]
    for n in range(A,2*A):
        v=predicted_residues(p,n)
        z=[exp(2j*pi*h*x/p) for x in v]
        for i in range(3):
            for j in range(3):
                sums[i][j]+=z[i]*z[j].conjugate()/A
    return tuple(tuple(row) for row in sums)


def target_gram(A,p):
    """Source stage resonance skeleton; finite errors not assumed small."""
    w=epoch_stage_weights(A,p)
    sigma=w[0]+w[1]
    return ((F(1),F(0),F(0)),(F(0),F(1),sigma),(F(0),sigma,F(1)))


def completion_error_budget(A,p,delta):
    """Finite consequence of character-completion theorem, NOT a δ certificate.

    Conditional input delta >= max_{c!=0} |complete S_p(c)|/m.
    Each of four stage chunks has remainder <= sqrt(p)(2+log m).
    """
    epoch_stage_boundaries(A,p)
    if not 0 <= delta <= 1:raise ValueError('delta in [0,1] required')
    m=multiplicative_order_16(p)
    return float(delta)+4*sqrt(p)*(2+log(m))/A


def direct_source_epoch_residues(A,p):
    """Independent full 4-pole modular recurrence, one pass (no stage oracle)."""
    epoch_stage_boundaries(A,p)
    v=[0,0,0]
    out=[]
    for n in range(1,2*A):
        a=8*n-7
        for i,(d,w) in enumerate(zip((3,4,5),(2,1,1))):
            injection=0
            for sign,denom in ((w,a),(-w,a+d)):
                if denom % (p*p) == 0:
                    raise AssertionError('entered p^2 regime')
                if denom % p == 0:
                    injection += sign * pow(denom//p,-1,p)
            v[i]=(16*v[i]+injection)%p
        if n>=A:out.append(tuple(v))
    return out


def dyadic_terminal_shadow(A, extra_terms=10, extra_bits=80):
    """Construct an EXACT p-unit rational anti-Haar epoch seed, no pi oracle.

    Approximates negative BBP constant alpha=pi/16 from exact first
    N=2A+extra_terms FOUR-POLE source terms, rounded downward on a dyadic
    grid of M=8A+extra_bits bits. The resulting denominator is a power of 2,
    so any odd-p component's p-primary residue is unchanged.

    This is a hostile *epoch-dependent* seed, never the original U0=0.
    """
    if type(A) is not int or A < 1 or type(extra_terms) is not int or extra_terms < 1 or type(extra_bits) is not int or extra_bits < 1:
        raise ValueError('A>=1, positive integer margins required')
    N = 2*A+extra_terms
    M = 8*A+extra_bits
    alpha_partial=F(0)
    for n in range(1,N+1):
        alpha_partial += sum(channel_forcing(n), F(0))/16**n
    v = alpha_partial * (1 << M)
    q = v.numerator // v.denominator
    s = -F(q,1<<M)
    assert F(0) <= s+alpha_partial <= F(1,1<<M)
    return s, alpha_partial, N, M


def dyadic_shadow_phase_bound(A, extra_terms=10, extra_bits=80):
    """Analytic rational *upper bound* on |U_n(s)| for A<=n<2A.

    Uses r(j)<1/j² and the exact future Green identity. No pi digits.
    """
    if type(A) is not int or A < 1:raise ValueError('A>=1')
    N=2*A+extra_terms
    M=8*A+extra_bits
    return F(1,1<<(M-4*(2*A))) + F(1,15*(N+1)**2*16**(N-2*A)) + F(1,15*(A+1)**2)
