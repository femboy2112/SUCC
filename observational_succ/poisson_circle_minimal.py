"""Source-typed minimum geometry of circle orbit measures.

Mathematical status: classical Poisson Fourier kernel plus explicitly proved
finite greedy, regret, and transport statements. No pi normality claim.

Rational point oracles use Q[i] and exact Fractions. Every pi-specific finite
certificate constructs its own strict Wallis/Kummer interval; no caller may
assert an unverified pi interval through the public certified entrypoint.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, gcd
from typing import Sequence


RPoint = tuple[Q, Q]


def _nat(x: int, minimum: int = 1) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f"requires an actual integer >= {minimum}")
    return x


def exact_point(num: int, den: int = 1) -> RPoint:
    """Pythagorean rational chart: ((1-t^2)/(1+t^2),2t/(1+t^2))."""
    if type(num) is not int or type(den) is not int or den <= 0:
        raise ValueError("exact rational stereographic parameter required")
    t = Q(num, den)
    x = (1 - t*t)/(1 + t*t)
    y = (2*t)/(1 + t*t)
    return x, y


def _point(p: RPoint) -> RPoint:
    if (type(p) is not tuple or len(p) != 2
            or any(type(v) not in (int, Q) for v in p)):
        raise ValueError("unit-circle point requires exact rational coordinates")
    a, b = Q(p[0]), Q(p[1])
    if a*a + b*b != 1:
        raise ValueError("point is not on the unit circle")
    return a, b


def chord_squared(a: RPoint, b: RPoint) -> Q:
    x, y = _point(a), _point(b)
    return (x[0]-y[0])**2 + (x[1]-y[1])**2


def poisson_chord(a: RPoint, b: RPoint) -> Q:
    """K(z,w)=3/(1+2|z-w|^2), r=1/2 disk Poisson kernel."""
    return 3 / (1 + 2*chord_squared(a, b))


def exact_potential(previous: Sequence[RPoint], candidate: RPoint) -> Q:
    _point(candidate)
    return sum((poisson_chord(p, candidate) for p in previous), Q(0))


def exact_energy(points: Sequence[RPoint]) -> Q:
    if not points:
        raise ValueError("nonempty point sample required")
    n = len(points)
    return sum((poisson_chord(a, b) for a in points for b in points), Q(0)) / (n*n)


def first_greedy_candidate(previous: Sequence[RPoint], max_height: int) -> RPoint:
    """Find the first rational-circle point with potential <= sample count.

    Height is explicitly budgeted; failing to find one does not refute the
    paper termination theorem for unbounded rational-height enumeration.
    """
    _nat(max_height)
    if not previous:
        return Q(1), Q(0)
    n = len(previous)
    seen: set[RPoint] = set()
    # The missing stereographic pole is always an eligible candidate.
    pole = (Q(-1), Q(0))
    if exact_potential(previous, pole) <= n:
        return pole
    seen.add(pole)
    for height in range(1, max_height + 1):
        for den in range(1, height + 1):
            for num in range(-height, height + 1):
                if max(abs(num), den) != height or gcd(abs(num), den) != 1:
                    continue
                candidate = exact_point(num, den)
                if candidate in seen:
                    continue
                seen.add(candidate)
                if exact_potential(previous, candidate) <= n:
                    return candidate
    raise ValueError("declared finite rational-circle search budget exhausted")


def rational_greedy_circle(length: int, max_height: int = 12) -> tuple[RPoint, ...]:
    _nat(length)
    _nat(max_height)
    result: list[RPoint] = []
    for _ in range(length):
        result.append(first_greedy_candidate(result, max_height))
    return tuple(result)


def exact_greedy_regret(points: Sequence[RPoint]) -> tuple[Q, ...]:
    """Excess above the Haar-mean potential n, not optimal-minimum regret.

    Individual excess may be negative. Its cumulative signed sum reconstructs
    exactly E_N - 1; positive-part excess provides a sufficient inequality.
    """
    previous: list[RPoint] = []
    result: list[Q] = []
    for p in points:
        result.append(exact_potential(previous, p) - len(previous))
        previous.append(p)
    return tuple(result)


def energy_from_excess(points: Sequence[RPoint]) -> Q:
    _nat(len(points))
    d = exact_greedy_regret(points)
    n = len(points)
    return 1 + Q(2, n) + 2*sum(d, Q(0))/(n*n)


def safe_positive_regret_bound(points: Sequence[RPoint]) -> Q:
    _nat(len(points))
    n = len(points)
    positive = sum((max(Q(0), v) for v in exact_greedy_regret(points)), Q(0))
    return 1 + Q(2, n) + 2*positive/(n*n)


def _unit_product(a: RPoint, b: RPoint) -> RPoint:
    ar, ai = _point(a)
    br, bi = _point(b)
    return ar*br-ai*bi, ar*bi+ai*br


def exact_power_point(point: RPoint, degree: int) -> RPoint:
    """Exact arithmetic realization of circle multiplication z -> z^degree."""
    _nat(degree, 0)
    base = _point(point)
    out = (Q(1), Q(0))
    while degree:
        if degree & 1:
            out = _unit_product(out, base)
        base = _unit_product(base, base)
        degree //= 2
    return out


def exact_rational_covering_orbit(
    point: RPoint, base: int, horizon: int
) -> tuple[RPoint, ...]:
    """Genuine forward T_b dynamics on Q[i]∩S^1, no point choice freedom."""
    _nat(base, 2)
    _nat(horizon)
    source = _point(point)
    path = []
    for _ in range(horizon):
        path.append(source)
        source = exact_power_point(source, base)
    return tuple(path)


def exact_rational_covering_energy(point: RPoint, base: int, horizon: int) -> Q:
    return exact_energy(exact_rational_covering_orbit(point, base, horizon))


def haar_origin_expected_energy(horizon: int) -> Q:
    """Exact Haar-x expectation for *any* base-b orbit E_N(x), b>=2."""
    _nat(horizon)
    return 1 + Q(2, horizon)


def finite_grid_origin_fourier_square(
    base: int, horizon: int, frequency: int, modulus: int
) -> Q:
    """Independent finite Fourier alias oracle averaged over ALL origins j/m.

    This is a polygon ENSEMBLE average, NOT the Fourier sample of pi or any
    selected vertex. It needs no gcd(base,modulus) assumption.
    """
    _nat(base, 2)
    _nat(horizon)
    _nat(frequency)
    _nat(modulus, 2)
    residues = [pow(base, j, modulus) for j in range(horizon)]
    count = sum(1 for a in residues for c in residues
                if frequency*(a-c)%modulus==0)
    return Q(count, horizon*horizon)


def finite_grid_origin_energy_interval(
    base: int, horizon: int, band: int, modulus: int
) -> tuple[Q,Q]:
    """Exact finite Poisson energy band plus sound all-harmonic tail <=2^-band*2."""
    _nat(band)
    partial=1+2*sum((Q(1,2**h)*finite_grid_origin_fourier_square(
        base,horizon,h,modulus) for h in range(1,band+1)),Q())
    return partial,min(Q(3),partial+Q(2,2**band))


def chord_covering_exact(source_chord: Q, degree: int) -> Q:
    """F_degree(X)=2-2*T_degree(1-X/2), exact fast Chebyshev recurrence.

    This is a *circle semigroup* observable, not an independent map chosen to
    fit a digit sample. Its polynomial is the parent Circle Genesis F_degree.
    """
    if type(source_chord) not in (Q, int) or not 0 <= source_chord <= 4:
        raise ValueError("exact chord state in [0,4] required")
    _nat(degree, 0)
    t = 1-Q(source_chord,2)

    def pair(n: int) -> tuple[Q,Q]:
        if n == 0:
            return Q(1), t
        a,b=pair(n//2)
        c=2*a*a-1
        d=2*a*b-t
        return (c,d) if n%2==0 else (d,2*b*b-1)

    out=2-2*pair(degree)[0]
    if not 0 <= out <= 4:
        raise ArithmeticError("source-faithful Chebyshev image outside chord carrier")
    return out


def exact_energy_from_one_chord(source_chord: Q, base: int, horizon: int) -> Q:
    """Entire orbit energy from ONE un-oriented chord and lawful T_b actions.

    q(z^(b^j),z^(b^k))=F_|b^j-b^k|(q(z,1)), so full orientation is
    unnecessary for this *target* even though it is needed for other actions.
    """
    _nat(base, 2)
    _nat(horizon)
    source_chord=Q(source_chord)
    result=Q(3*horizon)
    for j in range(1,horizon):
        for k in range(j):
            d=chord_covering_exact(source_chord,base**j-base**k)
            result+=2*Q(3)/(1+2*d)
    return result/(horizon*horizon)


def polygon_poisson_energy(vertices: int) -> Q:
    """Exact energy of uniform roots of unity, no trigonometric evaluation."""
    _nat(vertices)
    return 1 + Q(2, 2**vertices - 1)


def ternary_periodic_counterfeit_energy(depth: int) -> Q:
    """EXACT limiting energy for the base-2 orbit of x=1/3^depth.

    2 generates the units modulo 3^depth. Ramanujan characters vanish except
    at frequencies divisible by 3^(depth-1), with ratios -1/2 or 1. Summing
    the positive Poisson Fourier series gives the displayed simple fraction.
    Each depth is periodic and NONNORMAL, yet energies approach 1 rapidly.
    """
    _nat(depth)
    s = 3**(depth-1)
    q = 3*s
    return 1 + Q(1, 2*(2**s-1)) + Q(3, 2*(2**q-1))


def orbit_potential_bijection(base: int, horizon: int) -> tuple[tuple[int, int, int], ...]:
    """Exact lag indices for orbit chord pulls: b^j-b^k=b^k(b^(j-k)-1)."""
    _nat(base, 2)
    _nat(horizon)
    return tuple((k, j-k, (base**k)*(base**(j-k)-1))
                 for j in range(1, horizon) for k in range(j))


def pair_magnification_sum(base: int, horizon: int) -> int:
    _nat(base, 2)
    _nat(horizon)
    return 2*sum((j*base**j-sum(base**k for k in range(j))
                  for j in range(1, horizon)), 0)


def dyadic_nearest_center(lo: Q, hi: Q, bits: int) -> tuple[Q, Q]:
    """Source interval -> exact dyadic center and paid two-sided error."""
    _nat(bits)
    if type(lo) is not Q or type(hi) is not Q or not 0 < lo < hi < 4:
        raise ValueError("certified source interval must be genuine rational bounds")
    m = (lo + hi)/2
    scale = 2**bits
    num = (m.numerator*scale)//m.denominator
    center = Q(num, scale)
    eps = max(abs(center-lo), abs(hi-center))
    return center, eps


def _cos_taylor_enclosure(turns: Q, angle_pi: Q, pi_error: Q, order: int) -> tuple[Q, Q]:
    """Enclose cos(2 pi * turns) with rational Taylor and separate pi error."""
    _nat(order)
    if type(turns) is not Q or abs(turns) > Q(1,2):
        raise ValueError("phase must be an exact reduced rational turn")
    if type(angle_pi) is not Q or type(pi_error) is not Q or pi_error < 0:
        raise ValueError("pi conversion must be rational with a paid error")
    t = 2*angle_pi*turns
    if abs(t) >= 4:
        raise ValueError("Taylor phase outside rational radius bound")
    term = total = Q(1)
    for k in range(1, order + 1):
        term = -term*t*t / ((2*k)*(2*k-1))
        total += term
    radius = Q(4**(2*order+2), factorial(2*order+2)) + 2*abs(turns)*pi_error
    return max(Q(-1), total-radius), min(Q(1), total+radius)


def _centered_turn(t: Q) -> Q:
    nearest = ((t+Q(1,2)).numerator // (t+Q(1,2)).denominator)
    return t-nearest


def rational_turn_energy_interval(
    source: Q, base: int, horizon: int, angle_pi: Q, angle_error: Q, order: int
) -> tuple[Q, Q]:
    """Actual rational phase source; only angle conversion uses a pi interval."""
    _nat(base, 2)
    _nat(horizon)
    if type(source) is not Q:
        raise ValueError("source must be an exact Fraction, not an asserted float")
    lo, hi = Q(0), Q(0)
    for j in range(horizon):
        for k in range(horizon):
            turn = _centered_turn((base**j-base**k)*source)
            cos_lo, cos_hi = _cos_taylor_enclosure(turn, angle_pi, angle_error, order)
            qlo, qhi = 2-2*cos_hi, 2-2*cos_lo
            lo += Q(3,1)/(1+2*qhi)
            hi += Q(3,1)/(1+2*qlo)
    return lo/(horizon*horizon), hi/(horizon*horizon)


@dataclass(frozen=True)
class CertifiedSourceEnergy:
    base: int
    horizon: int
    wallis_steps: int
    center: Q
    pi_error: Q
    energy_lower: Q
    energy_upper: Q
    transport_error: Q

    def __post_init__(self) -> None:
        if not Q(1) <= self.energy_lower <= self.energy_upper <= Q(3):
            raise ValueError("source-derived energy enclosure violates universal bounds")


def certified_pi_energy(
    base: int, horizon: int, *, wallis_steps: int = 128,
    dyadic_bits: int = 44, taylor_order: int = 12
) -> CertifiedSourceEnergy:
    """Source-authenticated finite π energy, independent of input π digits.

    Wallis exact prime-power source is imported from merged PR #231/250.
    The source interval is collapsed to a dyadic rational center with its
    actual error. The source and radian roles of π are paid separately.
    """
    _nat(base, 2)
    _nat(horizon)
    _nat(wallis_steps)
    _nat(dyadic_bits)
    _nat(taylor_order)
    from observational_succ.pi_prime_carry_transport import wallis_pi_bracket
    lower, upper = wallis_pi_bracket(wallis_steps)
    center, eps = dyadic_nearest_center(lower, upper, dyadic_bits)
    finite_lo, finite_hi = rational_turn_energy_interval(
        center, base, horizon, center, eps, taylor_order
    )
    # K(q(t)) has turn-Lipschitz constant <=24π <96. Pair lag: b^j-b^k.
    err = Q(96, horizon*horizon)*eps*pair_magnification_sum(base, horizon)
    # The true energy is >=1 and <=3 for every probability measure.
    return CertifiedSourceEnergy(
        base, horizon, wallis_steps, center, eps,
        max(Q(1), finite_lo-err), min(Q(3), finite_hi+err), err,
    )


def energy_to_weyl_upper(energy_upper: Q, frequency: int) -> Q:
    """Rational bound for |A_h|^2, not an uncertified square root."""
    if type(energy_upper) is not Q or energy_upper < 1 or energy_upper > 3:
        raise ValueError("need a bounded rational geometric energy upper value")
    _nat(frequency)
    return min(Q(1), (energy_upper-1)*2**(frequency-1))
