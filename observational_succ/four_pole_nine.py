"""Three positive BBP pole-difference channels and exact 3x3 operator probes.

Research-only: none of these algebraic/observational constructions establishes
base-16 normality of pi. The original signed four-pole source and U_0=0 are
preserved exactly. Only Python standard library is required.
"""

from fractions import Fraction
from itertools import combinations
from math import isqrt, sqrt
from typing import Sequence

SHIFTS = (0, 3, 4, 5)
POLE_COEFFICIENTS = (4, -2, -1, -1)
POSITIVE_CHANNELS = ((3, 2), (4, 1), (5, 1))
PROJECTION = tuple(tuple(Fraction(int(i == j)) - Fraction(1, 4)
                         for j in range(4)) for i in range(4))


def _a(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError('clock must be an exact int or Fraction')
    value = Fraction(value)
    if value <= 0:
        raise ValueError('positive continuous source clock required')
    return value


def _n(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError('source time must be integer')
    if value < 0:
        raise ValueError('source time must be nonnegative')
    return value


def difference_channel(a, shift, multiplicity=1):
    a = _a(a)
    if isinstance(shift, bool) or not isinstance(shift, int) or shift <= 0:
        raise ValueError('positive integer pole offset required')
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity <= 0:
        raise ValueError('positive integer channel multiplicity required')
    return Fraction(multiplicity * shift, 1) / (a * (a + shift))


def signed_four_pole(a):
    a = _a(a)
    return sum((Fraction(c, 1) / (a + d) for c, d in zip(POLE_COEFFICIENTS, SHIFTS)), Fraction(0))


def positive_three_channel(a):
    a = _a(a)
    return tuple(difference_channel(a, d, c) for d, c in POSITIVE_CHANNELS)


def forcing(n):
    _n(n)
    if n < 1:
        raise ValueError('r(n) is defined for n >= 1')
    return signed_four_pole(8*n - 7)


def component_orbit(n):
    """Canonical three zero-seeded recurrences, each positive-forced."""
    _n(n)
    states = [Fraction(0) for _ in POSITIVE_CHANNELS]
    for j in range(1, n + 1):
        local = positive_three_channel(8*j - 7)
        states = [16*x + r for x, r in zip(states, local)]
    return tuple(states)


def original_zero_orbit(n):
    """Independent four-signed-pole recurrence for checking the decomposition."""
    _n(n)
    u = Fraction(0)
    for j in range(1, n+1):
        u = 16*u + forcing(j)
    return u


def source_jets(shifts=(3, 4, 5), multiplicities=(2, 1, 1)):
    """Q'(0), -Q''(0), Q'''(0) for sum c_d(1-exp(-d*x))."""
    if len(shifts) != 3 or len(multiplicities) != 3:
        raise ValueError('three pole-difference channels required')
    return tuple(sum(w * d**j for w, d in zip(multiplicities, shifts))
                 for j in (1, 2, 3))


def rigid_integer_shifts(first_jet, second_jet):
    """All 0<x,0<y<=z integral solutions of 2*x+y+z=m1,
    2*x^2+y^2+z^2=m2. No fitted/numerical roots.
    """
    if (isinstance(first_jet, bool) or isinstance(second_jet, bool)
        or not isinstance(first_jet, int) or not isinstance(second_jet, int)
        or first_jet <= 0 or second_jet <= 0):
        raise ValueError('positive integer source jets required')
    possibilities = []
    for x in range(1, isqrt(second_jet // 2) + 1):
        sum_yz = first_jet - 2*x
        sum_squares = second_jet - 2*x*x
        if sum_yz < 2 or sum_squares < 2:
            continue
        disc = 2*sum_squares - sum_yz*sum_yz
        if disc < 0 or isqrt(disc)**2 != disc:
            continue
        root = isqrt(disc)
        if (sum_yz-root) % 2:
            continue
        y, z = (sum_yz-root)//2, (sum_yz+root)//2
        if y > 0:
            possibilities.append((x, y, z))
    return tuple(possibilities)


def three_basis_at(a):
    """Columns of the canonical three-positive-difference source operator."""
    a = _a(a)
    return tuple(difference_channel(a, d) for d, _ in POSITIVE_CHANNELS)


def source_matrix(times: Sequence[int]):
    if len(times) != 3:
        raise ValueError('exactly 3 distinct clock samples required')
    return tuple(three_basis_at(a) for a in times)


def determinant_3(M):
    a, b, c = M
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def cauchy_determinant(times: Sequence[int]):
    """Closed Cauchy determinant for 3-by-3 channel measurements."""
    if len(times) != 3:
        raise ValueError('three clocks required')
    aa = tuple(_a(t) for t in times)
    ds = tuple(d for d, _ in POSITIVE_CHANNELS)
    numerator = Fraction(1)
    for d in ds:
        numerator *= d
    for i in range(3):
        for j in range(i+1, 3):
            numerator *= (aa[j] - aa[i])*(ds[j]-ds[i])
    denominator = Fraction(1)
    for a in aa:
        denominator *= a
        for d in ds:
            denominator *= a+d
    return numerator/denominator


def recover_multiplicities(times: Sequence[int], sample_values):
    """Exact Gaussian elimination on source samples; fails on duplicate clocks."""
    M = source_matrix(times)
    if len(sample_values) != 3:
        raise ValueError('three source values required')
    rows = [[Fraction(M[i][j]) for j in range(3)]+[Fraction(sample_values[i])]
            for i in range(3)]
    for j in range(3):
        pivot = next((i for i in range(j,3) if rows[i][j] != 0), None)
        if pivot is None:
            raise ValueError('singular source measurement: unable to resolve channels')
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [v/scale for v in rows[j]]
        for i in range(3):
            if i != j:
                scale = rows[i][j]
                rows[i] = [u-scale*v for u,v in zip(rows[i],rows[j])]
    return tuple(row[3] for row in rows)


def mul(A,B):
    rows, inner = len(A), len(B)
    if rows == 0 or inner == 0 or any(len(row)!=inner for row in A):
        raise ValueError('matrix dimension mismatch')
    cols = len(B[0])
    if any(len(row)!=cols for row in B):
        raise ValueError('ragged matrix')
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(inner)),Fraction(0))
                       for j in range(cols)) for i in range(rows))


def transpose(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))


def _difference(A,B):
    return tuple(tuple(a-b for a,b in zip(aa,bb)) for aa,bb in zip(A,B))


def _matvec(A,x):
    return tuple(sum((t*v for t,v in zip(row,x)),Fraction(0)) for row in A)


def pole_clock(a):
    a = _a(a)
    return tuple((a+d)/(a+d+8) for d in SHIFTS)


def relative_clock_vector(a):
    return _matvec(PROJECTION, pole_clock(a))


def relative_operator(a):
    d=pole_clock(a)
    D=tuple(tuple(d[i] if i==j else Fraction(0) for j in range(4)) for i in range(4))
    return mul(mul(PROJECTION,D),PROJECTION)


def projected_clock_step(a):
    """(actual new relative v, predicted relative v, missing scalar injection)."""
    a=_a(a)
    v=tuple(Fraction(1)/(a+d) for d in SHIFTS)
    x=_matvec(PROJECTION,v)
    scalar=sum(v,Fraction(0))/4
    M=relative_operator(a)
    inject=relative_clock_vector(a)
    predicted=tuple(u+scalar*g for u,g in zip(_matvec(M,x),inject))
    actual=_matvec(PROJECTION,tuple(Fraction(1)/(a+8+d) for d in SHIFTS))
    return actual,predicted,scalar,inject


def relative_commutator(a,b):
    A,B=relative_operator(a),relative_operator(b)
    return _difference(mul(A,B),mul(B,A))


def commutator_closed(a,b):
    u,v=relative_clock_vector(a),relative_clock_vector(b)
    return tuple(tuple(-(u[i]*v[j]-v[i]*u[j])/4 for j in range(4)) for i in range(4))


def commutator_op_norm_sq(a,b):
    """For this rank<=2 real skew operator, exactly (||u||²||v||²-<u,v>²)/16."""
    u,v=relative_clock_vector(a),relative_clock_vector(b)
    dot=lambda x,y:sum((a*b for a,b in zip(x,y)),Fraction(0))
    return (dot(u,u)*dot(v,v)-dot(u,v)**2)/16


def commutator_vandermonde_norm_sq(a,b):
    a,b=_a(a),_a(b)
    result=Fraction(0)
    for t in combinations(SHIFTS,3):
        i,j,k=t
        vand=(j-i)*(k-i)*(k-j)
        den=Fraction(1)
        for d in t:
            den *= (a+8+d)**2 * (b+8+d)**2
        result += Fraction(vand**2)/den
    return 64*(a-b)**2*result


def spin_135_parts(M):
    """Scalar (1), skew (3), symmetric-traceless (5) for real 3x3.

    This is an O(3)-metric-dependent decomposition; no source-derived
    physical rotational symmetry or nine independent BBP phase modes claimed.
    """
    if len(M)!=3 or any(len(row)!=3 for row in M):
        raise ValueError('3x3 matrix required')
    M=tuple(tuple(Fraction(v) for v in row) for row in M)
    tr=sum((M[i][i] for i in range(3)),Fraction(0))
    scalar=tuple(tuple(tr/3 if i==j else Fraction(0) for j in range(3)) for i in range(3))
    skew=tuple(tuple((M[i][j]-M[j][i])/2 for j in range(3)) for i in range(3))
    quad=tuple(tuple((M[i][j]+M[j][i])/2-scalar[i][j] for j in range(3)) for i in range(3))
    return scalar,skew,quad


def source_channel_weights(a):
    a=_a(a)
    r=signed_four_pole(a)
    return tuple(v/r for v in positive_three_channel(a))


def source_channel_limit_weights():
    return (Fraction(6,15),Fraction(4,15),Fraction(5,15))


def channel_amplitude(a):
    return tuple(sqrt(float(w)) for w in source_channel_weights(a))


def channel_limit_amplitude():
    return tuple(sqrt(float(w)) for w in source_channel_limit_weights())


def normalized_channel_amplitude_budget(a):
    """Rigorous Euclidean bound ||sqrt(w(a))-sqrt(w(infty))||<=5/(2a)."""
    return Fraction(5,2)/_a(a)


def _floor_fraction(x):
    x = Fraction(x)
    return x.numerator // x.denominator


def three_circle_carry_seam(n):
    """Exact three-torus -> one-circle carry seam.

    Returns (relative phases, seam, selected circle phase, integer lift).
    The seam is in {0,1,2}; no integer lift information is silently lost.
    """
    v = component_orbit(n)
    phases = tuple(x - _floor_fraction(x) for x in v)
    seam = _floor_fraction(sum(phases, Fraction(0)))
    selected = sum(phases, Fraction(0)) - seam
    lifted = sum(_floor_fraction(x) for x in v) + seam
    assert selected == original_zero_orbit(n) - _floor_fraction(original_zero_orbit(n))
    assert lifted == _floor_fraction(original_zero_orbit(n))
    return phases, seam, selected, lifted


def three_channel_carry_transport(n):
    """Exact original integer carry = sum of 3 component carries + seam change."""
    _n(n)
    if n < 1:
        raise ValueError('a positive recurrence step is required')
    prev_v = component_orbit(n-1)
    prev_x = tuple(x-_floor_fraction(x) for x in prev_v)
    source = positive_three_channel(8*n-7)
    channel_carries = tuple(_floor_fraction(16*x+r) for x,r in zip(prev_x,source))
    seam_prev = three_circle_carry_seam(n-1)[1]
    seam_next = three_circle_carry_seam(n)[1]
    prev_u = original_zero_orbit(n-1)
    scalar_carry = _floor_fraction(16*(prev_u-_floor_fraction(prev_u))+forcing(n))
    predicted = sum(channel_carries)+seam_next-16*seam_prev
    assert scalar_carry == predicted
    return scalar_carry, channel_carries, seam_prev, seam_next


def cubic_phase_cumulant(data):
    """Complex algebraic third connected moment, NO conjugation.

    Returns third cumulant, reconstructed triple mean, and all lower moments.
    This is not an arithmetic decay theorem: input supplies the time history.
    """
    seq = tuple(data)
    if not seq or any(len(row)!=3 for row in seq):
        raise ValueError('nonempty three-channel phase history required')
    n=len(seq)
    mu=[sum(row[i] for row in seq)/n for i in range(3)]
    pair={(i,j):sum(row[i]*row[j] for row in seq)/n for i,j in ((0,1),(0,2),(1,2))}
    triple=sum(row[0]*row[1]*row[2] for row in seq)/n
    kappa=(triple-mu[0]*pair[1,2]-mu[1]*pair[0,2]-mu[2]*pair[0,1]
            +2*mu[0]*mu[1]*mu[2])
    return kappa,triple,tuple(mu),pair


def two_adic_valuation(value):
    """Exact v_2 for a nonzero rational; +inf at zero."""
    q=Fraction(value)
    if q == 0:
        return float('inf')
    def count2(i):
        i=abs(i)
        count=0
        while i%2==0:
            i//=2
            count+=1
        return count
    return count2(q.numerator)-count2(q.denominator)


def positive_channel_two_adic_seam(n):
    """Proof-bearing exact values of paired half-integral channels at step n.

    For n>=1 the shifted denominators are a=8n-7, a+3=4(2n-1),
    a+4=8n-3 and a+5=2(4n-1). The pair of v2=-1 channels cancels in Q2/Z2.
    """
    _n(n)
    if n < 1:
        raise ValueError('positive source time required')
    a=8*n-7
    d3,d4,d5=positive_three_channel(a)
    assert d3 == Fraction(3,2*a*(2*n-1))
    assert d4 == Fraction(4,a*(a+4))
    assert d5 == Fraction(5,2*a*(4*n-1))
    pair=d3+d5
    assert pair == Fraction(11*n-4,a*(2*n-1)*(4*n-1))
    assert two_adic_valuation(d3)==-1
    assert two_adic_valuation(d4)==2
    assert two_adic_valuation(d5)==-1
    assert two_adic_valuation(pair)>=0
    assert two_adic_valuation(forcing(n))>=0
    return (d3,d4,d5),pair,forcing(n)


def source_channel_two_adic_history(n):
    """For n>=1, (v2(V3,n),v2(V4,n),v2(V5,n),v2(U_n))."""
    _n(n)
    if n < 1:
        raise ValueError('positive source time required')
    states=component_orbit(n)
    v=tuple(two_adic_valuation(x) for x in states)
    assert v[0] == -1 and v[1] == 2 and v[2] == -1
    assert two_adic_valuation(states[0]+states[2])>=0
    assert two_adic_valuation(sum(states))>=0
    return v+(two_adic_valuation(sum(states)),)


def gamma_two_source_normalizer(a):
    """Monotone source scale factor a^2 R(a)/15, in (0,1)."""
    a=_a(a)
    return a*a*signed_four_pole(a)/15


def authentic_mixed_poisson_pgf(a, z):
    """G_a(z) = E_{mu_a} exp(-a(1-z)X), z exact in [0,1].

    At a->infty this tends (2-z)^(-2). Declared Poisson-mixture
    observation, NOT a distribution of hexadecimal digits of pi.
    """
    a=_a(a)
    if isinstance(z,bool) or not isinstance(z,(int,Fraction)):
        raise TypeError('exact rational PGF argument required')
    z=Fraction(z)
    if not (0<=z<=1):
        raise ValueError('PGF probe z must belong to [0,1]')
    return signed_four_pole(a*(2-z))/signed_four_pole(a)


def authentic_mixed_poisson_mean(a):
    a=_a(a)
    # -a R'(a)/R(a), evaluated with the four signed source poles.
    deriv=sum((Fraction(-c,1)/(a+d)**2 for c,d in zip(POLE_COEFFICIENTS,SHIFTS)),Fraction(0))
    return -a*deriv/signed_four_pole(a)


def golden_fixed_point_bracket(a, bits=80):
    """Certified exact-rational enclosure of the strict interior PGF fixed point.

    The source channel decomposition proves 1 < G_a'(1) < 2, so an
    interior fixed point exists and is unique. The interval is a
    reproducible finite certificate, not a π-normality estimate.
    """
    a=_a(a)
    if isinstance(bits,bool) or not isinstance(bits,int) or not (1<=bits<=300):
        raise ValueError('bits must be integer 1..300')
    if not (1<authentic_mixed_poisson_mean(a)<2):
        raise AssertionError('source-defined supercriticality failed')
    f=lambda q:authentic_mixed_poisson_pgf(a,q)-q
    lo=Fraction(0)
    hi=None
    for k in range(1,80):
        candidate=Fraction(2**k-1,2**k)
        if f(candidate)<0:
            hi=candidate
            break
    if hi is None:
        raise AssertionError('interior fixed-point bracket unavailable')
    for _ in range(bits):
        m=(lo+hi)/2
        if f(m)>0:
            lo=m
        else:
            hi=m
    return lo,hi
