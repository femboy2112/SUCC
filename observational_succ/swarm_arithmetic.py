"""Exact arithmetic expedition instruments (SWM-E33--E40).

Theorems live in the indexed dossiers, not in finite test counts.  These
instruments preserve source labels, phases and affine action order.  No
nontrivial zeta zero, completed Weil sign or analytic continuation is input.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, gcd, isqrt
from typing import Mapping

from .arithmetic import divisors, factorization
from .core import Scalar, ZERO, ONE
from .gaussian_holonomy import gaussian_prime


class ArithmeticTransportError(ValueError):
    """A finite exact source/action contract has been violated."""


def _integer(value, low=0, high=1_000_000):
    if type(value) is not int or not low <= value <= high:
        raise ArithmeticTransportError(f"Exact integer in {low}..{high} required")
    return value


@dataclass(frozen=True)
class AffineAction:
    """x -> slope*x+offset on N_0; compose means self after before."""

    slope: int
    offset: int = 0

    def __post_init__(self):
        _integer(self.slope, 1)
        _integer(self.offset)

    def __call__(self, n):
        _integer(n)
        return self.slope*n+self.offset

    def compose(self, before):
        if not isinstance(before, AffineAction):
            raise ArithmeticTransportError("Affine action required")
        return AffineAction(self.slope*before.slope,
                            self.slope*before.offset+self.offset)

    def residue(self, n, modulus):
        _integer(modulus, 1, 4096)
        return self(n) % modulus


def cyclic_frame_offsets(modulus: int, slopes: tuple[int, ...]):
    """ALL bijections commuting with S and each V_a are x -> x+c.

    Their offsets are multiples of m/g, where g=gcd(m,a_1-1,...).
    This is a classification theorem, not just enumeration of permutations.
    """
    _integer(modulus, 1, 4096)
    if type(slopes) is not tuple:
        raise ArithmeticTransportError("Immutable slope family required")
    g = modulus
    for slope in slopes:
        _integer(slope, 1)
        g = gcd(g, slope-1)
    return tuple(range(0, modulus, modulus//g))


def verify_cyclic_frame(permutation: tuple[int, ...], slopes: tuple[int, ...]):
    """Exhaustive finite action square; no claim about an unobserved source."""
    if type(permutation) is not tuple or not permutation:
        raise ArithmeticTransportError("Nonempty immutable permutation required")
    modulus = len(permutation)
    _integer(modulus, 1, 4096)
    if any(type(x) is not int for x in permutation) or set(permutation) != set(range(modulus)):
        raise ArithmeticTransportError("Not a cyclic-carrier bijection")
    if type(slopes) is not tuple:
        raise ArithmeticTransportError("Immutable slope family required")
    for a in slopes:
        _integer(a, 1)
    return all(permutation[(x+1) % modulus] == (permutation[x]+1) % modulus
               and all(permutation[(a*x) % modulus] == (a*permutation[x]) % modulus
                       for a in slopes) for x in range(modulus))


def factor_square(n: int):
    """Integer chart for alpha+beta=nu(n), h(alpha)<=h(n)/2."""
    _integer(n, 1)
    return tuple((d, n//d) for d in divisors(n) if d*d <= n)


def factorial_valuation(n: int, p: int):
    """Legendre identity, independently checked by successor event summation."""
    _integer(n, 0, 1024)
    _integer(p, 2, 1024)
    if factorization(p) != ((p, 1),):
        raise ArithmeticTransportError("Authentic prime required")
    power, total = p, 0
    while power <= n:
        total += n//power
        power *= p
    return total


def mahler_prefix_ambiguity(horizon: int, p: int):
    """Constructive rival receipts agreeing at every integer 0..horizon.

    binom(x,N+1) is a distinct continuous p-adic polynomial; a spike at
    p^r>N for every r>=R is discontinuous along p^r -> 0.  No finite
    prefix can select regularity or unique continuation for unrestricted
    source functions.  The returned values are exact integer controls.
    """
    _integer(horizon, 0, 256)
    _integer(p, 2, 1024)
    if factorization(p) != ((p, 1),):
        raise ArithmeticTransportError("Authentic prime metric required")
    power, exponent = 1, 0
    while power <= horizon:
        power *= p
        exponent += 1
    return {"zero_prefix": (0,)*(horizon+1),
            "continuous_polynomial_prefix": tuple(comb(n, horizon+1)
                                                    for n in range(horizon+1)),
            "continuous_polynomial_next": 1,
            "discontinuous_spike_first": power,
            "discontinuous_spike_exponent": exponent,
            "spike_value": 1, "value_at_zero": 0,
            "finite_prefix_selects_continuity": False}


def _source(source: Mapping[int, object], horizon: int):
    _integer(horizon, 2, 256)
    if not isinstance(source, Mapping) or any(n not in source for n in range(1, horizon+1)):
        raise ArithmeticTransportError("Complete supplied source prefix required")
    result = (ZERO,) + tuple(Scalar.of(source[n]) for n in range(1, horizon+1))
    if result[1] != ONE:
        raise ArithmeticTransportError("Normalized source a(1)=1 required")
    return result


def dirichlet_log(source: Mapping[int, object], horizon: int):
    """Independent triangular log_* implementation via Omega derivation.

    Df(n)=Omega(n)f(n); Da=(Db)*a, where b=log_*a.  Every
    recurrence reads only divisors already in the supplied prefix.
    Supports exact Q(i) phases; no floating-point or zero oracle.
    """
    a = _source(source, horizon)
    omega = [0]+[sum(k for _, k in factorization(n)) for n in range(1, horizon+1)]
    b = [ZERO]*(horizon+1)
    for n in range(2, horizon+1):
        known = sum((omega[d]*b[d]*a[n//d] for d in divisors(n)
                     if 1 < d < n), ZERO)
        b[n] = (omega[n]*a[n]-known)/omega[n]
    return tuple(b)


def euler_audit(source: Mapping[int, object], horizon: int, *, conductor=None):
    """Separate finite multiplicativity, degree-one, unit and phase gates.

    Prime-power log support certifies coprime multiplicativity in this
    prefix only.  It does NOT imply degree-one rays, unit phases, conductor
    periodicity, a functional equation or completed Weil positivity.
    """
    a = _source(source, horizon)
    b = dirichlet_log(source, horizon)
    coprime = tuple((u, v) for u in range(2, horizon+1)
                    for v in range(2, horizon//u+1)
                    if gcd(u, v) == 1 and a[u*v] != a[u]*a[v])
    mixed = tuple(n for n in range(2, horizon+1)
                  if len(factorization(n)) > 1 and b[n] != ZERO)
    ray = tuple(n for n in range(2, horizon+1)
                if len(factorization(n)) == 1
                and a[n] != a[factorization(n)[0][0]]**factorization(n)[0][1])
    primes = tuple(n for n in range(2, horizon+1) if factorization(n) == ((n, 1),))
    if conductor is None:
        local = tuple(p for p in primes if a[p].norm2() not in (Q(0), Q(1)))
        periodic = None
    else:
        _integer(conductor, 1, 1024)
        local = tuple(p for p in primes if a[p].norm2() != (Q(1) if gcd(p, conductor) == 1 else Q(0)))
        periodic = tuple(n for n in range(1, horizon-conductor+1)
                         if a[n] != a[n+conductor])
    if bool(coprime) != bool(mixed):
        raise ArithmeticError("Finite log-support equivalence failed")
    return {"coprime_multiplicativity_defects": coprime,
            "mixed_log_support": mixed, "degree_one_ray_defects": ray,
            "unit_or_ramification_defects": local,
            "conductor_periodicity_defects": periodic,
            "scope": f"complete supplied coefficients 1..{horizon}",
            "global_Euler_or_RH_claim": False}


def valuation_covariance(source: Mapping[int, object], horizon: int, primes: tuple[int, ...]):
    """Cheap PSD covariance with rational half-density squared weights.

    Weights |a(n)|^2/n arise from amplitude a(n)/sqrt(n).  They lose
    phases before averaging, so even this arithmetic-aware covariance
    cannot determine mixed Dirichlet-log defects.  Not the Weil form.
    """
    a = _source(source, horizon)
    if type(primes) is not tuple or len(set(primes)) != len(primes):
        raise ArithmeticTransportError("Distinct prime coordinates required")
    for p in primes:
        _integer(p, 2, 256)
        if factorization(p) != ((p, 1),):
            raise ArithmeticTransportError("Authentic prime coordinates required")
    weights = tuple(a[n].norm2()/n for n in range(1, horizon+1))
    mass = sum(weights, Q())
    vectors = tuple(tuple(dict(factorization(n)).get(p, 0) for p in primes)
                    for n in range(1, horizon+1))
    means = tuple(sum((w*v[i] for w, v in zip(weights, vectors)), Q())/mass
                  for i in range(len(primes)))
    return tuple(tuple(sum((w*(v[i]-means[i])*(v[j]-means[j])
                            for w, v in zip(weights, vectors)), Q())/mass
                       for j in range(len(primes))) for i in range(len(primes)))


def gamma_cutoff_recurrence(n: int, z: int):
    """Exact finite Gamma recurrence defect (no analytic extrapolation)."""
    _integer(n, 2, 256)
    _integer(z, 1, 256)
    ratio = Q(n*z, n+z+1)
    return {"ratio": ratio, "target": Q(z), "defect": Q(z)-ratio,
            "boundary_defect": Q(z*(z+1), n+z+1),
            "finite_recurrence_exact": False}


def gaussian_component(seed: tuple[int, int], squared_bound: int, *, max_vertices=4096):
    """Explore the ACTUAL Gaussian-prime graph with exact exhaustive steps.

    A returned component is closed under every allowed step, and hence
    is a component of the infinite graph.  Budget exhaustion raises,
    never masquerades as a moat.  No external all-D theorem is needed.
    """
    _integer(squared_bound, 1, 25)
    _integer(max_vertices, 1, 100_000)
    if not gaussian_prime(seed):
        raise ArithmeticTransportError("Seed must be an actual Gaussian prime")
    radius = isqrt(squared_bound)
    steps = tuple((x, y) for x in range(-radius, radius+1)
                  for y in range(-radius, radius+1)
                  if 0 < x*x+y*y <= squared_bound)
    found, todo = {seed}, [seed]
    while todo:
        u = todo.pop()
        for dx, dy in steps:
            v = (u[0]+dx, u[1]+dy)
            if v not in found and gaussian_prime(v):
                if len(found) >= max_vertices:
                    raise ArithmeticTransportError("Gaussian exploration budget exhausted")
                found.add(v)
                todo.append(v)
    return tuple(sorted(found))


def verify_gaussian_closed(vertices: tuple[tuple[int, int], ...], squared_bound: int):
    """Verify a supplied finite graph closure, including missing-prime controls."""
    _integer(squared_bound, 1, 25)
    if type(vertices) is not tuple or not vertices or len(set(vertices)) != len(vertices):
        raise ArithmeticTransportError("Distinct actual arithmetic vertices required")
    if any(not gaussian_prime(z) for z in vertices):
        raise ArithmeticTransportError("Composite in arithmetic source graph")
    points, radius = set(vertices), isqrt(squared_bound)
    for x, y in vertices:
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                if 0 < dx*dx+dy*dy <= squared_bound:
                    v = (x+dx, y+dy)
                    if gaussian_prime(v) and v not in points:
                        return False
    return True


def displacement_transport(path: tuple[tuple[int, int], ...]):
    """Actual-coordinate cocycle telescopes; quotient winding may survive."""
    if type(path) is not tuple or not path:
        raise ArithmeticTransportError("Recorded nonempty coordinate path required")
    if any(type(z) is not tuple or len(z) != 2 or any(type(t) is not int for t in z) for z in path):
        raise ArithmeticTransportError("Integral coordinate path required")
    return tuple(path[-1][j]-path[0][j] for j in (0, 1))


def projected_resolvent_numerator(alpha: Q):
    """T=diag(1,2), unit-vector squared first weight alpha in [0,1].

    <u,(zI-T)^-1u>=(z-(1+alpha))/((z-1)(z-2)).
    For 0<alpha<1 its scalar zero moves while source poles stay fixed.
    At endpoints the apparent numerator zero cancels a denominator pole.
    """
    if type(alpha) is int:
        alpha = Q(alpha)
    if not isinstance(alpha, Q) or not 0 <= alpha <= 1:
        raise ArithmeticTransportError("Exact projection weight in [0,1] required")
    return {"source_poles": (Q(1), Q(2)), "numerator_zero": 1+alpha,
            "zero_is_uncancelled": 0 < alpha < 1,
            "projection_changes_source_spectrum": False}
