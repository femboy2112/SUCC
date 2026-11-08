"""Three-channel p-primary BBP pulse tomography; research-only, pi OPEN.

All rational quantities are exact. Complex evaluations are diagnostics only.
The authentic forcing is unchanged and the three suborbits have seed zero.
"""
from collections import Counter
from fractions import Fraction as F
from math import isqrt, pi
from cmath import exp

SHIFTS = (3, 4, 5)
WEIGHTS = (2, 1, 1)
EVENTS = ((1, (2, 1, 1)), (4, (-2, 0, 0)),
          (5, (0, -1, 0)), (6, (0, 0, -1)))


def is_prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def channel_forcing(n):
    if type(n) is not int or n < 1:
        raise ValueError('source time must be a positive integer')
    a = 8*n - 7
    return tuple(F(w*d, a*(a+d)) for w, d in zip(WEIGHTS, SHIFTS))


def channel_states(n):
    if type(n) is not int or n < 0:
        raise ValueError('state time must be a nonnegative integer')
    v = (F(0), F(0), F(0))
    for j in range(1, n + 1):
        v = tuple(16*x + y for x, y in zip(v, channel_forcing(j)))
    return v


def stage_vectors(r):
    """Four channel vectors after each p-event in shell r, as rationals.

    Their sum is the corresponding universal scalar PF-02 pulse normalizer.
    """
    if type(r) is not int or r < 0:
        raise ValueError('shell index must be nonnegative')
    v = [16*x for x in channel_states(r)]
    result = []
    for q, marks in EVENTS:
        v = [x + F(mark, 8*r + q) for x, mark in zip(v, marks)]
        result.append(tuple(v))
    return tuple(result)


def valid_clock(p, r=0):
    if not is_prime(p) or p % 8 != 1 or p <= 5:
        raise ValueError('requires prime p=1 mod8, p>5')
    k = (p - 1)//8
    if type(r) is not int or not 0 <= r < k:
        raise ValueError('requires a complete simple-pole shell 0 <= r < (p-1)/8')
    return k


def birth_times(p, r=0):
    k = valid_clock(p, r)
    return (k + 1 + r*p, 4*k + 1 + r*p,
            5*k + 1 + r*p, 6*k + 1 + r*p)


def reduce_fraction(q, p):
    q = F(q)
    if q.denominator % p == 0:
        raise ValueError('denominator is not a p-unit')
    return q.numerator * pow(q.denominator, -1, p) % p


def predicted_residues(p, n):
    """Exact p*V_d(n) mod p for 0<=n before the first p² birth.

    The three V_d are zero-seeded channel orbits, not real phase random variables.
    """
    k = valid_clock(p)
    if type(n) is not int or n < 0:
        raise ValueError('n>=0')
    first = k + 1
    if n < first:
        return (0, 0, 0)
    r, t = divmod(n - first, p)
    valid_clock(p, r)
    j = 0 if t < 3*k else (1 if t < 4*k else (2 if t < 5*k else 3))
    scale = pow(16, t, p)
    return tuple(scale * reduce_fraction(x, p) % p for x in stage_vectors(r)[j])


def direct_residues(p, n):
    """Independent original two-pole-channel recurrence mod p (no PF transport)."""
    valid_clock(p)
    if type(n) is not int or n < 0 or n >= ((p-1)//8 + 1) + ((p-1)//8)*p:
        raise ValueError('n outside proven simple-pole domain')
    v = [0, 0, 0]
    for j in range(1, n + 1):
        a = 8*j - 7
        for i, (d, w) in enumerate(zip(SHIFTS, WEIGHTS)):
            injection = 0
            for sign, den in ((w, a), (-w, a+d)):
                if den % (p*p) == 0:
                    raise ValueError('p² pole excluded')
                if den % p == 0:
                    injection += sign * pow(den//p, -1, p)
            v[i] = (16*v[i] + injection) % p
    return tuple(v)


def multiplicative_order_16(p):
    valid_clock(p)
    x, m = 16 % p, 1
    while x != 1:
        x = (x*16) % p
        m += 1
    return m


def mode_coefficients(p, r, h, mode):
    valid_clock(p, r)
    if type(h) is not int or not isinstance(mode, tuple) or len(mode) != 3 or any(type(t) is not int for t in mode):
        raise ValueError('integer harmonic and integer length-3 Fourier mode required')
    return tuple(reduce_fraction(h*sum(t*x for t,x in zip(mode, v)), p)
                 for v in stage_vectors(r))


def mode_resonance_mass(mode, r=0):
    """Exact limiting FOUR-subtorus Fourier coefficient for fixed integer mode."""
    if len(mode) != 3 or any(type(t) is not int for t in mode):
        raise ValueError('integer three-vector required')
    return F(sum(weight for weight, vec in zip((3,1,1,3), stage_vectors(r))
                 if sum(t*x for t,x in zip(mode,vec)) == 0), 8)


def shell_residue_histogram(p, r, h, mode):
    """Exact histogram of <mode, p V_n> over full shell (direct oracle)."""
    k = valid_clock(p, r)
    first = k+1+r*p
    result = Counter()
    for n in range(first, first + p):
        c = direct_residues(p,n)
        result[h*sum(t*x for t,x in zip(mode,c)) % p] += 1
    return result


def predicted_histogram(p, r, h, mode):
    """Exact cyclic subgroup counts for the same Fourier mode, no phase floats."""
    k = valid_clock(p, r)
    m = multiplicative_order_16(p)
    if k % m:
        raise AssertionError('Euler criterion was violated')
    coeff = mode_coefficients(p,r,h,mode)
    counts = Counter()
    for weight, c in zip((3,1,1,3), coeff):
        for u in range(m):
            counts[c * pow(16,u,p) % p] += weight * (k//m)
    counts[coeff[3]] += 1  # one complete-shell endpoint, at t=8k
    return counts


def subgroup_delta(p):
    """Finite diagnostic of subgroup cancellation, not an analytic bound."""
    m = multiplicative_order_16(p)
    orbit = [pow(16,u,p) for u in range(m)]
    return max(abs(sum(exp(2j*pi*c*x/p) for x in orbit))/m
               for c in range(1,p))


def local_phase_gram(p, r=0, h=1):
    """Hermitian 3x3 Gram from true p-source residues at one full shell."""
    k = valid_clock(p,r)
    start = k+1+r*p
    mat = [[0j]*3 for _ in range(3)]
    for n in range(start,start+p):
        v = direct_residues(p,n)
        z = [exp(2j*pi*h*x/p) for x in v]
        for i in range(3):
            for j in range(3):
                mat[i][j] += z[i]*z[j].conjugate()/p
    return tuple(tuple(row) for row in mat)


def prime_frame_target():
    """Limit for FIRST shell, assuming subgroup character delta->0."""
    return ((1.,0.,0.),(0.,1.,0.5),(0.,0.5,1.))


def root_harmonic_forcing(n):
    return sum(channel_forcing(n), F(0))
