"""Growing-order rational frames for authentic BBP, with integer log intervals.

No supplied pi digits, seed averages, or independent-prime model. Paper proof
in HIGH_ORDER_FRAMES.md. Float formatting is never a certificate.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, lcm

C = (4, -2, -1, -1)
OFFSETS = (0, 3, 4, 5)


def source(n, coeff=C):
    assert n >= 1
    return sum((Q(c, 8*n-7+d) for c, d in zip(coeff, OFFSETS)), Q())


def selected(n, seed=Q(), coeff=C):
    u = Q(seed)
    for k in range(1, n+1):
        u = 16*u + source(k, coeff)
    return u


def weights(m):
    """Weights of f(j/(2m))-f(-j/(2m)), j=1,...,m."""
    assert m >= 1
    return tuple(Q((-1)**(j+1)*2*m*factorial(m)**2,
                   j*factorial(m-j)*factorial(m+j)) for j in range(1, m+1))


def error_bound(n, m):
    assert n >= 1 and m >= 1
    return Q(8*(16**n-1), 15*(2*m+1))*Q(factorial(m), m**m)**2


def ceil_log2_integer(a):
    assert a >= 1
    return (a-1).bit_length()


def moving_order(n):
    assert n >= 1
    return 4*n + ceil_log2_integer((n+1)**2) + 4


def source_denominator(n):
    """Known denominator passport, not the reduced denominator of U_n."""
    d = 1
    for k in range(1, n+1):
        for shift in OFFSETS:
            d = lcm(d, 8*k-7+shift)
    return d


def reconstruction_order(n):
    return 4*n + ceil_log2_integer(source_denominator(n)) + 4


@lru_cache(None)
def factor(a):
    assert a >= 1
    out = []
    p = 2
    while p*p <= a:
        e = 0
        while a % p == 0:
            a //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if a > 1:
        out.append((a, 1))
    return tuple(out)


def prime_vector(n, m, coeff=C):
    """A_(n,m)=sum_p vector[p]*log(p), full signed prime vector.

    Factor only integers <= 2m(8n-2)+m, never the enormous B_n.
    """
    out = {}
    for j, w in enumerate(weights(m), 1):
        for k in range(1, n+1):
            for c, d in zip(coeff, OFFSETS):
                for sign in (-1, 1):
                    a = 2*m*(8*k-7+d) + sign*j
                    for p, e in factor(a):
                        out[p] = out.get(p, Q()) + sign*w*c*16**(n-k)*e
    return {p: e for p, e in sorted(out.items()) if e}


def ceil_div(a, b):
    return -((-a)//b)


def _atanh_log(a, b, bits, terms):
    """Integer enclosure of 2 atanh(a/b), 0<=a/b<=1/3."""
    assert 0 <= 3*a <= b and terms >= 1
    if not a:
        return 0, 0
    scale = 1 << bits
    ap, bp = a, b
    lo = 0
    for j in range(terms):
        lo += 2*((scale*ap)//(bp*(2*j+1)))
        ap *= a*a
        bp *= b*b
    # First omitted power is ap/bp=(a/b)^(2*terms+1).
    remainder = ceil_div(2*scale*ap*b*b,
                         bp*(2*terms+1)*(b*b-a*a))
    return lo, lo+2*terms+remainder


@lru_cache(None)
def log_integer_interval(a, bits=192, terms=96):
    """Outward integer interval for 2^bits log(a); proof uses atanh series."""
    assert a >= 1
    k = a.bit_length()-1
    b = 1 << k
    low, high = _atanh_log(a-b, a+b, bits, terms)
    l2, h2 = _atanh_log(1, 3, bits, terms)
    return low+k*l2, high+k*h2


def linear_log_interval(vector, bits=192, terms=96):
    """All signs retained; rounding is outward at each rational coefficient."""
    lo = hi = 0
    for p, q in vector.items():
        a, b = log_integer_interval(p, bits, terms)
        if q < 0:
            a, b = b, a
        lo += (q.numerator*a)//q.denominator
        hi += ceil_div(q.numerator*b, q.denominator)
    return lo, hi


def frame_interval(n, m, bits=192, terms=96, coeff=C):
    lo, hi = linear_log_interval(prime_vector(n, m, coeff), bits, terms)
    return Q(lo, 1 << bits), Q(hi, 1 << bits)


def reconstruct(n, bits=256, terms=128):
    """Recover U_n from finite frame observations plus denominator passport.

    Does not use selected(n). Raises if the chosen enclosure is insufficient.
    """
    m = reconstruction_order(n)
    lo, hi = frame_interval(n, m, bits, terms)
    e = error_bound(n, m)
    if m % 2:
        lo -= e
    else:
        hi += e
    d = source_denominator(n)
    first = ceil_div((lo*d).numerator, (lo*d).denominator)
    last = (hi*d).numerator//(hi*d).denominator
    if first != last:
        raise ValueError((n, m, first, last))
    return Q(first, d)


def primary_part(x, p):
    """Canonical p-primary part of a rational modulo Z, not random marginal."""
    d = x.denominator
    pa = 1
    while d % p == 0:
        pa *= p
        d //= p
    if pa == 1:
        return Q()
    return Q((x.numerator*pow(d, -1, pa)) % pa, pa)
