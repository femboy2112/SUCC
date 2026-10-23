"""Circle self-coverings, exact chord/Kummer moments, and certified π energies.

Source: unit-circle nested chords (not supplied π digits). All certificates use
stdlib Fraction/isqrt and outward rational Taylor bounds. Neither this module
nor its finite probes proves π normality. Paper theorem statements and
quantifiers: research/2026-10-23/CIRCLE_CHORD_KUMMER_COLLISION.md.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd, isqrt


def _trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return _trim([(a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return _trim(out)


def compose(a, b):
    out = (0,)
    for c in reversed(a):
        out = add(mul(out, b), (c,))
    return out


def evaluate(a, x):
    y = Q(0)
    for c in reversed(a):
        y = y*x + c
    return y


def covering(degree):
    """F_n(X)=|1-z^n|² for X=|1-z|². F_m o F_n=F_mn."""
    if type(degree) is not int or degree < 0:
        raise ValueError("nonnegative integer degree")
    a, b = (0,), (0, 1)
    for _ in range(1, degree):
        c = add((0, 2), add(mul((2, -1), b),
                             tuple(-u for u in a)))
        a, b = b, c
    return a if degree == 0 else b


def fejer_chord(band):
    """Exact K_M(X)=M+1-sum_(h=1)^M(1-h/(M+1))*F_h(X)."""
    if type(band) is not int or band < 0:
        raise ValueError("nonnegative band")
    out = (Q(band+1),)
    for h in range(1, band+1):
        out = add(out, tuple(-Q(band+1-h, band+1)*c
                             for c in covering(h)))
    return out


def chord_fourier(power):
    """D(z)^k=sum_(-k<=h<=k)(-1)^h*C(2k,k+h)*z^h."""
    if type(power) is not int or power < 0:
        raise ValueError("nonnegative power")
    return {h: (-1 if h % 2 else 1)*comb(2*power, power+h)
            for h in range(-power, power+1)}


def haar_moment(power):
    if type(power) is not int or power < 0:
        raise ValueError("nonnegative power")
    return comb(2*power, power)


def polygon_moment(power, vertices):
    if type(vertices) is not int or vertices < 2:
        raise ValueError("invalid polygon")
    return sum(c for h, c in chord_fourier(power).items()
               if h % vertices == 0)


def prime_carries(power):
    """Legendre/Kummer prime-power valuation of C(2k,k)."""
    if type(power) is not int or power < 0:
        raise ValueError("nonnegative power")
    out = {}
    for p in range(2, 2*power+1):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        value, pp = 0, p
        while pp <= 2*power:
            carry = (2*power)//pp - 2*(power//pp)
            if carry not in (0, 1):
                raise ArithmeticError("invalid carry source")
            value += carry
            pp *= p
        if value:
            out[p] = value
    return out


def carry_product(power):
    out = 1
    for p, c in prime_carries(power).items():
        out *= p**c
    return out


def vertex_orbits(vertices, base):
    if (type(vertices) is not int or type(base) is not int
            or min(vertices, base) < 2 or gcd(vertices, base) != 1):
        raise ValueError("requires finite permutation of vertices")
    seen, result = set(), []
    for root in range(vertices):
        if root in seen:
            continue
        orbit, x = [], root
        while x not in seen:
            seen.add(x)
            orbit.append(x)
            x = (base*x) % vertices
        if x != root:
            raise AssertionError("incorrect finite orbit")
        result.append(tuple(orbit))
    return tuple(result)


def replica_count(base, frequency, horizon, band):
    """R for |A_h| <= 2R/N + sqrt((E_(M,N)-1)/R)."""
    if any(type(v) is not int for v in (base, frequency, horizon, band)):
        raise ValueError("integer parameters")
    if base < 2 or frequency == 0 or horizon < 1 or band < 2*abs(frequency):
        raise ValueError("invalid expansion/band")
    r, value = 0, abs(frequency)
    while r < isqrt(horizon) and 2*value <= band:
        r += 1
        value *= base
    return r


def sqrt_interval(lo, hi, digits):
    lo, hi = Q(lo), Q(hi)
    if lo < 0 or hi < lo or type(digits) is not int or digits < 15:
        raise ValueError("invalid sqrt interval")
    scale = 10**digits
    lower = isqrt((lo.numerator * scale**2)//lo.denominator)
    upper = isqrt((hi.numerator * scale**2)//hi.denominator) + 1
    return Q(lower, scale), Q(upper, scale)


def chord_interval(level, digits=78):
    """X_(4^level) nested from X_4=2, X_2m=2-sqrt(4-X_m)."""
    if type(level) is not int or level < 1:
        raise ValueError("level>=1")
    lo = hi = Q(2)
    for _ in range(2*(level-1)):
        rlo, rhi = sqrt_interval(4-hi, 4-lo, digits)
        lo, hi = 2-rhi, 2-rlo
        if lo <= 0 or hi > 4:
            raise ArithmeticError("precision insufficient")
    return lo, hi


def perimeter_interval(level, digits=78):
    xlo, xhi = chord_interval(level, digits)
    rlo, rhi = sqrt_interval(xlo, xhi, digits)
    return Q(4**level, 2)*rlo, Q(4**level, 2)*rhi


def pi_interval(level, digits=78):
    """Rational Archimedean inscribed/tangent polygon π brackets."""
    xlo, xhi = chord_interval(level, digits)
    rlo, rhi = sqrt_interval(xlo, xhi, digits)
    clo, _ = sqrt_interval(1-xhi/4, 1-xlo/4, digits)
    if clo <= 0:
        raise ArithmeticError("cosine lower bound missing")
    return Q(4**level, 2)*rlo, Q(4**level, 2)*rhi/clo


def error_constant():
    """C=(3/20)(22/7)^5, |16^j*pi - Y_(j,K)| < C*16^(-j-2K)."""
    return Q(3, 20)*Q(22, 7)**5


def aligned_phase(index, lookahead=1, digits=78):
    if any(type(v) is not int for v in (index, lookahead, digits)):
        raise ValueError("integer geometric source")
    if index < 0 or lookahead < 1:
        raise ValueError("index>=0 and lookahead>=1")
    level = index+lookahead
    plo, phi = perimeter_interval(level, digits)
    factor, m2 = 16**index, 16**level
    return (factor*(plo+plo**3/(6*m2)),
            factor*(phi+phi**3/(6*m2)))


def aligned_error(index, lookahead=1):
    if (type(index) is not int or type(lookahead) is not int
            or index < 0 or lookahead < 1):
        raise ValueError("invalid source scale")
    return error_constant()/16**(index+2*lookahead)


def energy_transport_error(band, horizon, lookahead=1):
    """Outward rational bound on |E_M,N(π)-E_M,N(aligned phases)|."""
    if any(type(v) is not int for v in (band, horizon, lookahead)):
        raise ValueError("integer scale parameters")
    if min(band, horizon, lookahead) < 1:
        raise ValueError("positive scale parameters")
    return Q(64, 45)*Q(22, 7)*error_constant()*band*(band+2) / (
        horizon*16**(2*lookahead))


def _cos_enclosure(reduced, err, pil, piu, order):
    """Exact rational cosine Taylor + 1-Lipschitz phase error."""
    if abs(reduced) > Q(1, 2) or err < 0 or not 0 < pil < piu < 4:
        raise ValueError("invalid phase or π interval")
    midpoint = (pil+piu)/2
    z = 2*midpoint*reduced
    delta = 2*(piu*err + abs(reduced)*(piu-pil)/2)
    term = total = Q(1)
    for j in range(1, order+1):
        term = -term*z*z / ((2*j-1)*(2*j))
        total += term
    remainder = Q(4)**(2*order+2)/factorial(2*order+2)
    return total-remainder-delta, total+remainder+delta


def _energy_from_phase_intervals(phases, band, pil, piu, order):
    N = len(phases)
    low = high = Q(1)
    for h in range(1, band+1):
        coslo = coshi = Q(0)
        for j in range(N):
            for k in range(j):
                l = h*(phases[j][0]-phases[k][1])
                u = h*(phases[j][1]-phases[k][0])
                center, radius = (l+u)/2, (u-l)/2
                rounded = center+Q(1, 2)
                center -= rounded.numerator//rounded.denominator
                cl, cu = _cos_enclosure(center, radius, pil, piu, order)
                coslo += cl
                coshi += cu
        weight = 2*Q(band+1-h, band+1)
        low += weight*(N+2*coslo)/N**2
        high += weight*(N+2*coshi)/N**2
    return low, high


def certified_energy(base, horizon, band, *, geometric=False, lookahead=5,
                     digits=78, pi_level=26, order=28):
    """Exact rational outer bracket for actual π or aligned algebraic orbit.

    Never substitute a numerical π value. Parenthesized sources:
    actual phases b^jπ from Archimedean polygon brackets; aligned source
    Y_(j,K) is valid only at base 16 and uses chord radicals.
    """
    if any(type(v) is not int for v in
           (base, horizon, band, lookahead, digits, pi_level, order)):
        raise ValueError("integer source inputs")
    if base < 2 or not (2 <= horizon <= 16) or not (1 <= band <= 12):
        raise ValueError("outside stated finite certificate budget")
    pil, piu = pi_interval(pi_level, digits)
    if geometric:
        if base != 16:
            raise ValueError("aligned source is hexadecimal")
        phases = [aligned_phase(j, lookahead, digits) for j in range(horizon)]
    else:
        phases = [(base**j*pil, base**j*piu) for j in range(horizon)]
    return _energy_from_phase_intervals(phases, band, pil, piu, order)


def outward_decimal(lo, hi, places=12):
    """Printed integer enclosure [lower,upper]/10^places is outward."""
    if Q(lo) > Q(hi) or type(places) is not int or places < 1:
        raise ValueError("invalid output bracket")
    scale = 10**places
    a, b = Q(lo)*scale, Q(hi)*scale
    return a.numerator//a.denominator, -((-b.numerator)//b.denominator), scale


def polygon_ensemble_fourier_square(base, frequency, horizon, vertices):
    """Exact mean over ALL m-gon vertices of |A_(h,N)(r/m)|².

    Root-of-unity orthogonality makes this a count of pairs satisfying
    m | h*(b^j-b^k). This is an ENSEMBLE identity, not a selected π orbit.
    """
    if any(type(z) is not int for z in (base, frequency, horizon, vertices)):
        raise ValueError("integer source parameters")
    if base < 2 or frequency == 0 or horizon < 1 or vertices < 2:
        raise ValueError("invalid polygon/time/frequency")
    addresses = [pow(base, j, vertices) for j in range(horizon)]
    count = sum(1 for a in addresses for c in addresses
                if (frequency*(a-c)) % vertices == 0)
    return Q(count, horizon*horizon)


def polygon_ensemble_energy(base, horizon, band, vertices):
    """Exact m-gon ENSEMBLE average of K_M pair energy for T_b orbits.

    If m>M*(b^(N-1)-1), every nonzero frequency has only diagonal
    congruences and the answer is exactly 1+M/N. Exceptional points
    (e.g. source vertex 0) are not controlled by that average.
    """
    if any(type(z) is not int for z in (base, horizon, band, vertices)):
        raise ValueError("integer source parameters")
    if base < 2 or horizon < 1 or band < 1 or vertices < 2:
        raise ValueError("invalid ensemble scale")
    return 1+2*sum(
        (Q(band+1-h, band+1) *
         polygon_ensemble_fourier_square(base, h, horizon, vertices)
         for h in range(1, band+1)), Q())


def wallis_from_circle_moments(power):
    """Strict classical Wallis rational π bracket from the SAME chord moments.

    H_k=binom(2k,k)=full-prime Kummer product=exact polygon k-moment for m>k.
    R_k=2^(4k+1)/[(2k+1)*H_k²] < pi <
         R_k*(4k+2)/(4k+1), k>=1.
    The link is classical and reconstructed in PR #231; not a normality proof.
    """
    if type(power) is not int or power < 1:
        raise ValueError("positive Wallis source index")
    h = haar_moment(power)
    r = Q(2**(4*power+1), (2*power+1)*h*h)
    return r, r*Q(4*power+2, 4*power+1)
