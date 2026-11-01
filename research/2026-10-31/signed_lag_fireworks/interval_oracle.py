"""Independent outward fixed-point phase oracle, no imported lag instrument.

Source: combined rational four-pole expression, reduced circle recurrence.
Pi: positive BBP partial sum with explicit Green-tail remainder (not Machin).
Cosine: interval angle doubling from a tiny-angle enclosure (not the parent's
17-term direct Taylor evaluation). Integer interval products round outward.
"""
from fractions import Fraction as F
from functools import lru_cache


def source(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive source index required')
    return F(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def circle_states(N, seed=F(0)):
    if type(N) is not int or N < 0:
        raise ValueError('nonnegative integer horizon required')
    u = F(seed) % 1
    out = [u]
    for n in range(1, N+1):
        u = (16*u+source(n)) % 1
        out.append(u)
    return tuple(out)


@lru_cache(maxsize=None)
def pi_interval(depth=28):
    if type(depth) is not int or depth < 1:
        raise ValueError('positive depth required')
    low = sum((F(16, 16**j)*source(j) for j in range(1, depth+1)), F(0))
    return low, low+F(16, 16**depth*64*depth*depth)


def _floor(x):
    return x.numerator // x.denominator


def _ceil(x):
    return -((-x.numerator) // x.denominator)


def _mul(a, b, Q):
    products = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products)//Q, -((-max(products))//Q)


def _square(a, Q):
    low = 0 if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    high = max(a[0]*a[0], a[1]*a[1])
    return low//Q, -((-high)//Q)


def cosine(x, bits=120, halvings=44, output_digits=12):
    """Rigorous enclosure of cos(2*pi*x), exact rational input.

    cos y in [1-y²/2,1], |sin y-y|<=|y|³/6, then 44 exact
    angle-doubling identities with outward 120-bit fixed-point rounding.
    """
    if type(bits) is not int or bits < 80 or type(halvings) is not int or not 20 <= halvings <= 60:
        raise ValueError('precision outside certified instrument range')
    if type(output_digits) is not int or not 4 <= output_digits <= 16:
        raise ValueError('invalid output precision')
    x = F(x) % 1
    if x > F(1, 2):
        x -= 1
    # Enclose the exact phase BEFORE nonlinear rational arithmetic. The
    # source denominator can contain thousands of bits. An outward dyadic
    # interval preserves the true phase while keeping the cube inexpensive.
    phase_grid = 2**96
    cell = (x.numerator*phase_grid)//x.denominator
    xl, xu = F(cell, phase_grid), F(cell+1, phase_grid)
    p, P = pi_interval()
    products = (2*xl*p/2**halvings, 2*xl*P/2**halvings,
                2*xu*p/2**halvings, 2*xu*P/2**halvings)
    ylo, yhi = min(products), max(products)
    Y = max(abs(ylo), abs(yhi))
    Q = 2**bits
    c = (_floor((1-Y*Y/2)*Q), Q)
    s = (_floor((ylo-Y**3/6)*Q), _ceil((yhi+Y**3/6)*Q))
    for _ in range(halvings):
        cc, ss, cs = _square(c, Q), _square(s, Q), _mul(c, s, Q)
        c = (max(-Q, cc[0]-ss[1]), min(Q, cc[1]-ss[0]))
        s = (max(-Q, 2*cs[0]), min(Q, 2*cs[1]))
        assert c[0] <= c[1] and s[0] <= s[1]
    unit = 10**output_digits
    return F((c[0]*unit)//Q, unit), F(-((-c[1]*unit)//Q), unit)


def score_from_states(U, K, h=1, actual=False):
    N = len(U)-1
    if type(K) is not int or not 1 <= K <= N or type(h) is not int or h == 0:
        raise ValueError('valid lag depth and nonzero harmonic required')
    lo = hi = F(0)
    rows = []
    for k in range(1, K):
        a = b = F(0)
        for n in range(1, N-k+1):
            phase = h*(U[n+k]-U[n]) if actual else h*(16**k-1)*U[n]
            l, u = cosine(phase)
            a += l
            b += u
        weight = F(2*(K-k), K*K*N)
        lo += weight*a
        hi += weight*b
        rows.append({'k': k, 'unweighted_interval': [str(a), str(b)],
                     'weight': str(weight)})
    return (lo, hi), rows
