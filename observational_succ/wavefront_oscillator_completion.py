"""Source-authenticated Oily two-loop wavefront completion and pumped oscillator.

Source: SUCC Main XIII / PR #340 positive Oily packet kernel; PR #333
signed eight-shell taps. This module never modifies the original BBP signed
forcing, its U_0=0 seed, or the source's expanding real-circle dynamics.

The Oily wavefront grade source is a strictly stable, *passive* triangular
matrix whose Neumann fixed point equals the full original positive R(x).
A distinct *pumped* control repeats the signed first shell each eight ticks,
producing a unique attracting eight-cycle. That cycle is not the original
shrinking eight-shell coefficient sequence or BBP's expanding U_n orbit.

Only Fraction and standard Python arithmetic are required.
"""
from __future__ import annotations

from fractions import Fraction as F
from typing import Iterable

from .wavefront_oracle_two_stage import SourceGeometry

BBP_TAPS = (F(4), F(0), F(0), F(-2), F(-1), F(-1), F(0), F(0))
ZERO = F(0)
ONE = F(1)


def _nat(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("requires a nonnegative integer index")
    return n


def _matrix_multiply(a, b):
    return (
        (a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]),
        (a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]),
    )


def _matrix_power(a, n: int):
    _nat(n)
    z = ((ONE, ZERO), (ZERO, ONE))
    while n:
        if n & 1:
            z = _matrix_multiply(z, a)
        a = _matrix_multiply(a, a)
        n //= 2
    return z


def _apply(a, x):
    return (a[0][0]*x[0] + a[0][1]*x[1],
            a[1][0]*x[0] + a[1][1]*x[1])


def _inverse(a):
    det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    if not det:
        raise ZeroDivisionError("singular candidate source completion")
    return ((a[1][1]/det, -a[0][1]/det),
            (-a[1][0]/det, a[0][0]/det))


def oily_packet_matrix(x):
    """M=[[u,1],[0,v]]. M^(j+1)[0,1] is the jth loop packet sum."""
    s = SourceGeometry(F(x))
    return ((s.u, ONE), (ZERO, s.v))


def packet_matrix_coefficient(x, grade: int) -> F:
    """Authentic *raw* Oily p_j(x), and zero at x=1 (not endpoint w_j)."""
    _nat(grade)
    return (ONE-F(x))/4 * _matrix_power(oily_packet_matrix(x), grade+1)[0][1]


def stationary_oily_state(x):
    """(I-M)^(-1) e2: a unique attractor, with first coordinate 4R/(1-x)."""
    m = oily_packet_matrix(x)
    i_minus_m = ((ONE-m[0][0], -m[0][1]),
                 (-m[1][0], ONE-m[1][1]))
    return _apply(_inverse(i_minus_m), (ZERO, ONE))


def stationary_oily_source(x) -> F:
    """R(x) exactly, including boundary x=1 where raw kernel is zero."""
    x = SourceGeometry(F(x)).x
    return (ONE-x)/4 * stationary_oily_state(x)[0]


def partial_oily_source(x, last_grade: int) -> F:
    """The first last_grade+1 *original* raw positive packet contributions."""
    _nat(last_grade)
    x = SourceGeometry(F(x)).x
    m = oily_packet_matrix(x)
    z = (ZERO, ONE)
    total = ZERO
    for _ in range(last_grade+1):
        z = _apply(m, z)
        total += z[0]
    return (ONE-x)/4 * total


def raw_packet_tail(x, last_grade: int) -> F:
    """Exact nonnegative R - partial; do not infer a signed Fourier estimate."""
    return stationary_oily_source(x) - partial_oily_source(x,last_grade)


def certified_uniform_raw_tail_bound(x, last_grade: int) -> F:
    """Bound using u,v <= 1/2. Sharp at x=1 after division by 1-x."""
    _nat(last_grade)
    x = SourceGeometry(F(x)).x
    return (ONE-x) * F(last_grade+3, 2**(last_grade+2))


def kernel_hankel_determinant(x) -> F:
    """2x2 Hankel determinant of grade PGF; nonzero for every x>0."""
    s = SourceGeometry(F(x))
    q = [s.grade_probability(j) for j in range(3)]
    return q[0]*q[2]-q[1]*q[1]


def minimum_registers_oily(x) -> int:
    """Full causal LTI state dimension, including two compulsory delays.

    For x>0 the grade Hankel minor is nonzero, requiring two modes.
    At x=0 the transfer is the pure two-unit delay z^2; it also needs two
    state registers even though its *extra-grade* recurrence has order 0.
    The exhibited two-stage cascade attains dimension two for every x.
    """
    SourceGeometry(F(x))
    return 2


def observer_matrix(x):
    """E1,E2 memory, with E1(t+1) driven by W(t)."""
    s = SourceGeometry(F(x))
    return ((s.u, ZERO), (ONE-s.v, s.v))


def step_observer(state, emitted, x):
    s = SourceGeometry(F(x))
    a,b = F(state[0]),F(state[1])
    return (s.u*a + (ONE-s.u)*F(emitted),
            (ONE-s.v)*a + s.v*b)


def critical_memory_power(n: int):
    """A(1)^n = 2^-n [[1,0],[n,1]], the Jordan/resonance bound."""
    _nat(n)
    return ((F(1,2**n), ZERO),
            (F(n,2**n), F(1,2**n)))


def critical_transient_bound(n: int) -> F:
    """Exact infinity matrix norm of A(1)^n, (n+1)/2^n."""
    _nat(n)
    return F(n+1, 2**n)


def source_signed_tap(index: int) -> F:
    """Actual original *contracting* source coefficient c_(8k+j)."""
    k,j = divmod(_nat(index),8)
    return BBP_TAPS[j]/(16**k)


def pumped_source_oscillator(index: int) -> F:
    """EXTERNALLY pumped periodic extension of the original eight-tap shell.

    Equals 16^floor(n/8) c_n; resets/replenishes the 1/16 shell loss.
    NOT the unpumped BBP source, its Mellin forcing, or its U_n orbit.
    """
    return BBP_TAPS[_nat(index)%8]


def signed_four_pole_moment(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive original BBP moment index required")
    return (F(4,8*n-7)-F(2,8*n-4)
            -F(1,8*n-3)-F(1,8*n-2))


def impulse_shell_moment(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive original BBP moment index required")
    return sum((c/F(8*(n-1)+j+1) for j,c in enumerate(BBP_TAPS)), ZERO)


def periodic_response(x, taps: Iterable[F]=BBP_TAPS):
    """Unique attracting periodic state from the explicitly periodic pump.

    State y_t=(E1(t),E2(t)); given period p, y_(t+1)=Ay_t+B W_t.
    Solving y_p=y_0 yields y_0=(I-A^p)^-1 F^p(0).
    Returns (states at t=0..p-1, initial state) using pure Fraction.
    """
    period = tuple(F(v) for v in taps)
    if not period:
        raise ValueError("requires a nonempty finite pumping period")
    a = observer_matrix(x)
    shift = (ZERO,ZERO)
    for v in period:
        shift = step_observer(shift, v, x)
    ap = _matrix_power(a,len(period))
    imap = ((ONE-ap[0][0],-ap[0][1]),
            (-ap[1][0],ONE-ap[1][1]))
    y0 = _apply(_inverse(imap),shift)
    states = []
    cur = y0
    for v in period:
        states.append(cur)
        cur = step_observer(cur,v,x)
    if cur != y0:
        raise ArithmeticError("failed exact periodic source compatibility")
    return tuple(states), y0


def periodic_trace(x, taps=BBP_TAPS, start=(ZERO,ZERO), cycles=1):
    """Finite generated history from arbitrary seed for strong-limit controls."""
    _nat(cycles)
    signal=tuple(F(v) for v in taps)
    if not signal:
        raise ValueError("requires nonempty period")
    current=tuple(F(t) for t in start)
    result=[]
    for _ in range(cycles):
        for w in signal:
            result.append(current)
            current=step_observer(current,w,x)
    return tuple(result), current


def two_stage_high_frequency_condition(x) -> F:
    """Exact ratio max|H|/min|H| on full unit-circle Fourier spectrum.

    Delay is harmless in modulus; for x=1 the ratio is 9, not 1.
    Perfect inversion is formal and amplifies arbitrary signed noise.
    """
    s=SourceGeometry(F(x))
    return (ONE+s.u)/(ONE-s.u) * (ONE+s.v)/(ONE-s.v)


def critical_stage_condition(depth: int) -> int:
    """For m equal endpoint filters, full-frequency conditioning is 3^m."""
    _nat(depth)
    return 3**depth


def critical_periodic_source_average() -> F:
    return sum(BBP_TAPS,ZERO)/len(BBP_TAPS)


def decode_source_two_steps(e2: Iterable[F], x):
    """Exactly recover W(t-2) from reports E2(t),E2(t-1),E2(t-2).

    Requires correct original filter coefficients, exact rational reports,
    and zero prehistory. This decodes only the *already causally delivered*
    past, NOT future innovations or an unknown physical source law.
    """
    s = SourceGeometry(F(x))
    reports = tuple(F(z) for z in e2)
    past = lambda t: reports[t] if t>=0 else ZERO
    return tuple((reports[t]-(s.u+s.v)*past(t-1)+s.u*s.v*past(t-2))
                 /s.normalization for t in range(2,len(reports)))


def decoder_noise_gain(x) -> F:
    """Sharp infinite-stream sup-norm bound, also Fourier condition number.

    Perturbed observer reports at every time have max abs error epsilon;
    the reconstructed two-step-retarded oracle may err by <=gain*epsilon.
    An alternating error sign attains equality for large enough t.
    """
    return two_stage_high_frequency_condition(x)


def normalized_chiral_period_radical2():
    """Eight derived source taps in Q(sqrt(2)), as rational (a,b) pairs.

    W_n=2^(n/2) c_n from the ORIGINAL c_n=ell(T^n b). Since
    T^8=I/16, Q=sqrt(2) T has Q^8=I. This is a continuously pumped
    oscillator: it is NOT the original passive BBP source.
    """
    return tuple((c*2**(j//2),ZERO) if j%2==0
                 else (ZERO,c*2**((j-1)//2))
                 for j,c in enumerate(BBP_TAPS))


def normalized_chiral_periodic_response(x):
    """Exact Q(sqrt(2))-valued 8-cycle without floating sqrt2 arithmetic.

    Each state component is a pair (a,b) meaning a + b sqrt(2).
    """
    taps = normalized_chiral_period_radical2()
    ordinary,_=periodic_response(x,tuple(a for a,b in taps))
    radicals,_=periodic_response(x,tuple(b for a,b in taps))
    return tuple(((a[0],b[0]),(a[1],b[1]))
                 for a,b in zip(ordinary,radicals))


def maximum_entropy_two_bit_emitter(x):
    """Conditional model: unique max Shannon entropy 2-bit source at mean x.

    P(00),P(01),P(10),P(11) for independent Bernoulli(p=x/2).
    This finite *probability interpretation* is added to the BBP source;
    it is not an authenticated microscopic mechanism of the real BBP digits.
    """
    x=SourceGeometry(F(x)).x
    p=x/2
    return ((ONE-p)**2,p*(ONE-p),p*(ONE-p),p*p)


def sizebiased_emitter_rates(x):
    """Canonical Palm/size-biased occupancy masses reproduce Oily u,v.

    With B=X1+X2, E B=x, u=1*P(B=1), v=2*P(B=2).
    At x>0, the actual size-biased B* has law (u/x,v/x) on (1,2).
    The additional rule 'use those masses as geometric retention rates'
    is still a MODELING CHOICE, not forced by maximum entropy alone.
    """
    x=SourceGeometry(F(x)).x
    p00,p01,p10,p11=maximum_entropy_two_bit_emitter(x)
    return (p01+p10,2*p11)
