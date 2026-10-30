"""Exact rational BBP/Gram transport and certified finite spectral probes.

No pi digits are inputs. Trigonometric bounds use rational Machin/Taylor
arithmetic after exact rational reduction and dyadic quantization.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def orbit(count, seed=F(0)):
    out = [F(seed)]
    for n in range(1, count+1):
        out.append(16*out[-1]+r(n))
    return out


def m(d):
    return (16**d-1)//15


def source_defect(n, d):
    return sum((16**(d-j)*(r(n+j)-r(n+1)) for j in range(1, d+1)), F(0))


def source_defect_bound(n, d):
    return F(16*(m(d)-d), (8*n+1)**3)


def atan_interval(q, terms=60):
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    next_term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, s+next_term), max(s, s+next_term)


@lru_cache(maxsize=1)
def pi_interval():
    a, b = atan_interval(5)
    c, d = atan_interval(239)
    return 16*a-4*d, 16*b-4*c


def cos_interval(phase):
    # Reduce before multiplying by pi. Quantization error is bounded explicitly.
    phase = F(phase)
    phase -= (phase+F(1, 2)).numerator//(phase+F(1, 2)).denominator
    den = 2**80
    y = F((phase*den).numerator//(phase*den).denominator, den)
    pl, pu = pi_interval()
    pd = 2**96
    pmid = (pl+pu)/2
    p = F((pmid*pd).numerator//(pmid*pd).denominator, pd)
    x = 2*p*y
    s = sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(24)), F(0))
    # Taylor with degree47 (odd coefficient0) has next derivative bounded1.
    rem = abs(x)**48/factorial(48)
    angle_error = 2*pu/den+2*abs(y)*max(abs(pl-p), abs(pu-p))
    eps = rem+angle_error
    lower, upper = max(F(-1), s-eps), min(F(1), s+eps)
    # Outward dyadic rounding preserves rigor and bounds receipt size.
    outden=2**96
    lower=F((lower*outden).numerator//(lower*outden).denominator,outden)
    upper=-F((-upper*outden).numerator//(-upper*outden).denominator,outden)
    return lower,upper


def energy_interval(phase):
    lo, hi = cos_interval(phase)
    return 1-hi, 1-lo


def mean_energy_interval(values, A, N, h):
    bounds = [energy_interval(h*(values[n+1]-values[n])) for n in range(A, A+N)]
    return sum((a for a, _ in bounds), F(0))/N, sum((b for _, b in bounds), F(0))/N


def gram_transport_bound(values, A, N, k, J, energies=None):
    if energies is None:
        energies = {d: mean_energy_interval(values, A, N, k*m(d)) for d in range(1, J)}
    energies = {d: energies[d] for d in range(1, J)}
    pl, pu = pi_interval()
    source_error = F(2, J*J)*sum((
        (J-d)*2*pu*abs(k)*source_defect_bound(A, d)
        for d in range(1, J)), F(0))
    boundary_error = F(2*(J-1)*(J-2), 3*N*J)
    radicand = 1-F(2, J*J)*sum(((J-d)*energies[d][0] for d in energies), F(0))
    radicand += source_error+boundary_error
    assert radicand >= 0
    return {
        "energies": energies,
        "radicand_upper": radicand,
        "outside_boundary": F(J-1, N),
        "source_error": source_error,
        "inside_boundary": boundary_error,
    }


def source_marks(a):
    weights = [F(c*d, a*(a+d)) for d, c in [(3, 2), (4, 1), (5, 1)]]
    s = sum(weights)
    return tuple(x/s for x in weights)


def mark_derivatives(a):
    p = source_marks(a)
    mean_inverse = sum((p_i/F(a+d) for p_i, d in zip(p, (3, 4, 5))), F(0))
    return tuple(p_i*(mean_inverse-F(1, a+d)) for p_i, d in zip(p, (3, 4, 5)))


def walsh(mask, digit):
    return -1 if (mask & digit).bit_count() % 2 else 1


def carries(values):
    out = [None]
    for n in range(1, len(values)):
        x = values[n-1] % 1
        v = 16*x+r(n)
        out.append(v.numerator//v.denominator)
    return out


def marked_frame(carry):
    # All16 Walsh sectors retained: a signed permutation X_c Z_(c+1).
    c = carry % 16
    return tuple((i ^ c, walsh((c+1) % 16, i)) for i in range(16))


def compose(P, Q):
    return tuple((P[Q[i][0]][0], Q[i][1]*P[Q[i][0]][1]) for i in range(16))


def inverse(P):
    out = [None]*16
    for i, (j, sign) in enumerate(P):
        out[j] = (i, sign)
    return tuple(out)


IDENTITY = tuple((i, 1) for i in range(16))


def edge_frame(source, target):
    return compose(target, inverse(source))


def de_bruijn(base, order):
    a = [0]*(base*order)
    sequence = []
    def db(t, p):
        if t > order:
            if order % p == 0:
                sequence.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for j in range(a[t-p]+1, base):
                a[t] = j
                db(t+1, t)
    db(1, 1)
    return sequence


def stoneham_stage(c, j):
    q = c**j
    u = F(0)
    for n in range(1, q):
        u = 16*u
        for t in range(1, j):
            if n == c**t:
                u += F(1, c**t)
    out = []
    for n in range(q, c*q):
        u = 16*u
        if n == q:
            u += F(1, q)
        u %= 1
        out.append(u)
    return out


def dump_fraction(q):
    return f"{q.numerator}/{q.denominator}"
