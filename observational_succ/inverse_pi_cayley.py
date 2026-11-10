"""Cayley reciprocal two-sheet observer for source-lifted hexadecimal parity.

Mathematical identities are proved in the adjacent research dossier. Source
forcing is imported from the canonical duck_bbp implementation; no frozen
source code is modified. Numerical Fourier sums below are diagnostics, NOT
certified floating-point enclosures and NOT pi-normality evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import atan, comb, isqrt, pi, sin, tan

Q = Fraction


def _prime(p: int) -> bool:
    if type(p) is not int or p < 2:
        return False
    if p == 2:
        return True
    if not p % 2:
        return False
    return all(p % j for j in range(3, isqrt(p) + 1, 2))


def parity_of_lift(u: Q) -> int:
    """Real integer-part parity, retaining the entire lift modulo 2."""
    u = Q(u)
    return 1 if (u.numerator // u.denominator) % 2 == 0 else -1


def cayley_halfline_sign(u: Q) -> int | None:
    """Sign of tan(pi*u/2) for noninteger u. Integer chart seams are None."""
    u = Q(u)
    phase = u % 2
    if phase == 0 or phase == 1:
        return None
    return 1 if phase < 1 else -1


def reciprocal_involution(x: Q | None) -> Q | None:
    """Source lift u->u+1 gives line involution x->-1/x; None is infinity."""
    if x is None:
        return Q(0)
    x = Q(x)
    return None if x == 0 else -1 / x


def circle_to_line(u: Q) -> float:
    """Visualization only. For seam-adjacent data use exact lift comparisons."""
    phase = Q(u) % 2
    if phase == 1:
        return float('inf')
    if phase == 0:
        return 0.0
    if abs(phase - 1) < Q(1, 10**13) or min(phase, 2-phase) < Q(1, 10**13):
        raise ValueError('chart too close to a seam for ordinary float projection')
    return tan(pi * float(phase) / 2)


def cauchy_arc_mass(left: float, right: float) -> float:
    """Haar mass of a line interval under dmu=dx/[pi(1+x^2)]."""
    if left > right:
        raise ValueError('left must be <= right')
    return (atan(right) - atan(left)) / pi


def parity_16_polynomial(x: Q) -> Q:
    """Exact numerator Im((1+i*x)^16); zero indicates digit boundary."""
    x = Q(x)
    return sum(((-1)**((k-1)//2) * comb(16,k) * x**k
                for k in range(1, 17, 2)), Q(0))


def distance_to_integer(u: Q) -> Q:
    """Exact distance from a rational real lift to the nearest integer."""
    f = Q(u) % 1
    return min(f, 1-f)


def fejer_halfline_pin(u: Q, H: int) -> float:
    """Fejer-smoothed sign(sin(pi*u)) on the double-cover U mod 2.

    Nonrigorous floating evaluation of an analytically exact trigonometric sum.
    Only O(H) odd signed oscillators are read, no completed pi digit is used.
    """
    if type(H) is not int or H < 1:
        raise ValueError('H must be a positive integer')
    theta = pi * float(Q(u) % 2)
    return (4/pi) * sum((1 - m/(H+1))*sin(m*theta)/m
                         for m in range(1, H+1, 2))


def fejer_tail_bound(H: int, delta: Q) -> float:
    """Analytic error away from integer seams: 4 cot(pi*delta)/[pi(H+1)]."""
    if type(H) is not int or H < 1 or not (0 < Q(delta) < Q(1,4)):
        raise ValueError('H>=1 and 0<delta<1/4 required')
    return 4 / (pi*(H+1)*tan(pi*float(Q(delta))))


def fejer_lipschitz_exact(H: int) -> Q:
    """Exact Lipschitz bound: H+1 minus 1/(H+1) for even H."""
    if type(H) is not int or H < 1:
        raise ValueError('H>=1')
    return Q(H+1) - (Q(1,H+1) if H % 2 == 0 else Q(0))


def fejer_lipschitz(H: int) -> float:
    """Display-only floating conversion of the exact derivative bound."""
    return float(fejer_lipschitz_exact(H))


@dataclass(frozen=True)
class CuspContrast:
    size: int
    plus_size: int
    minus_size: int
    smooth_contrast: float
    plus_near_seam: int
    minus_near_seam: int
    near_seam_error: Q
    fejer_error: float
    green_transport_error: float
    total_analytic_error_display: float


def conditional_cusp_contrast(lifts, source_signs, max_positive_tail: Q,
                              H: int, delta: Q) -> CuspContrast:
    """Source-only quantitative window for the two-fiber parity detail.

    Assumptions: original signed labels a=+/-1, true completed real lifts
    V_n=U_n+T_n with 0<=T_n<=max_positive_tail, and no V_n integer seams.
    beta = 1/2(E[parity(V)|a+] + E[parity(V)|a-]).

    |beta - smooth_contrast| <= near_seam_error + fejer_error
                                + green_transport_error.
    The formula is a paper inequality; float evaluation/display of its
    trigonometric term is NOT rounding-certified. No beta decay is claimed.
    """
    us, labels = tuple(Q(x) for x in lifts), tuple(source_signs)
    if not us or len(us) != len(labels) or any(type(a) is not int or a not in (-1,1) for a in labels):
        raise ValueError('equal nonempty rational lifts and +/-1 source labels required')
    tmax, delta = Q(max_positive_tail), Q(delta)
    if tmax < 0 or tmax >= 1 or not (0 < delta < Q(1,4)):
        raise ValueError('0<=tail<1 and 0<delta<1/4 required')
    if type(H) is not int or H < 1:
        raise ValueError('H must be >=1')
    plus = [i for i,a in enumerate(labels) if a == 1]
    minus = [i for i,a in enumerate(labels) if a == -1]
    if not plus or not minus:
        raise ValueError('both source sign fibers must be populated')
    pin = [fejer_halfline_pin(x,H) for x in us]
    score = (sum(pin[i] for i in plus)/len(plus)
             + sum(pin[i] for i in minus)/len(minus))/2
    # dist(U+T,Z) < 2delta follows from dist(U,Z) < 2delta+tmax.
    aperture = 2*delta + tmax
    bp = sum(distance_to_integer(us[i]) <= aperture for i in plus)
    bm = sum(distance_to_integer(us[i]) <= aperture for i in minus)
    boundary = Q(bp,len(plus)) + Q(bm,len(minus))
    fejer = fejer_tail_bound(H,delta)
    source_cost = fejer_lipschitz(H)*float(tmax)
    total = float(boundary)+fejer+source_cost
    return CuspContrast(len(us),len(plus),len(minus),score,bp,bm,
                        boundary,fejer,source_cost,total)


def original_zero_prime_epoch(A: int, p: int):
    """Unreduced canonical BBP source U0=0 and its simple-pole p labels.

    p must be a genuine prime born by the start of the epoch and must have
    no squared-power source denominator through the epoch. This does NOT
    assert #554's stronger balanced-prime selector hypotheses.
    """
    if type(A) is not int or A < 2 or not _prime(p) or p == 2:
        raise ValueError('A>=2, odd prime p required')
    from observational_succ import duck_bbp
    from observational_succ.bbp_parity_pressure import prime_coordinate
    u = Q(0)
    lifts, signs = [], []
    born = False
    for n in range(1, 2*A):
        r = duck_bbp.forcing(n)
        if r.denominator % p == 0:
            born = born or n <= A
        if r.denominator % (p*p) == 0:
            raise ValueError('p is not a simple-pole source shell')
        u = 16*u+r
        if n >= A:
            lifts.append(u)
            signs.append(1 if prime_coordinate(u,p) % 2 == 0 else -1)
    if not born:
        raise ValueError('p does not appear in original source before epoch')
    return tuple(lifts), tuple(signs)


def original_zero_cusp_contrast(A: int, p: int, H: int, delta: Q):
    """Cusp bound using only canonical rational source, p coordinate and tail bound."""
    from observational_succ import duck_bbp
    lifts, signs = original_zero_prime_epoch(A,p)
    return conditional_cusp_contrast(lifts, signs, duck_bbp.tail_budget(A),H,delta)
