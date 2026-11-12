"""Exact toy model: shared-environment recoherence vs prime-labelled signed forms.

This is an operational quantum-information *analogy*. Prime powers are validated
arithmetically, but no physical prime channel, negative energy or Weil-form
identification is asserted. No claim of pi normality or RH is implemented.

All amplitudes are rational, stored as unnormalized real pure-state rays; density
matrices are normalized before comparisons. Controlled gates are rational
orthogonal, so all purity and Bell-fidelity receipts are exact Fractions.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt
from typing import Mapping, Sequence


Ray = dict[tuple[int, ...], Q]
Matrix2 = tuple[tuple[Q, Q], tuple[Q, Q]]
R90: Matrix2 = ((Q(0), Q(-1)), (Q(1), Q(0)))
RNEG90: Matrix2 = ((Q(0), Q(1)), (Q(-1), Q(0)))
IDENTITY: Matrix2 = ((Q(1), Q(0)), (Q(0), Q(1)))


def _r(x: int | Q) -> Q:
    if type(x) is not int and type(x) is not Q:
        raise TypeError("exact int or Fraction required")
    return Q(x)


def _check_ray(ray: Mapping[tuple[int, ...], Q], n: int) -> None:
    if not ray:
        raise ValueError("nonzero pure-state ray required")
    if any(type(bits) is not tuple or len(bits) != n or
           any(type(b) is not int or b not in (0, 1) for b in bits)
           for bits in ray):
        raise ValueError("all basis words must be n-bit tuples")
    if not any(_r(x) for x in ray.values()):
        raise ValueError("nonzero ray required")


def _norm2(ray: Mapping[tuple[int, ...], Q]) -> Q:
    return sum((_r(v) ** 2 for v in ray.values()), Q())


def initial_bell_environment() -> Ray:
    """(|00>+|11>)|0>, unnormalized. No measurement or collapse."""
    return {(0, 0, 0): Q(1), (1, 1, 0): Q(1)}


def rotate_shared_environment(ray: Mapping[tuple[int, int, int], Q],
                              control: int, rotation: Matrix2) -> Ray:
    """Apply controlled 2x2 real orthogonal rotation to environment qubit E.

    control is A (0) or B (1). Gates must be orthogonal, rejecting arbitrary
    nonunitary 'negative entropy rates' masquerading as coherent dynamics.
    """
    _check_ray(ray, 3)
    if type(control) is not int or control not in (0, 1):
        raise ValueError("control must name observer A=0 or B=1")
    if (len(rotation) != 2 or any(len(row) != 2 for row in rotation)):
        raise ValueError("2x2 rotation required")
    m = tuple(tuple(_r(v) for v in row) for row in rotation)
    if any(sum((m[k][i] * m[k][j] for k in range(2)), Q()) != int(i == j)
           for i in range(2) for j in range(2)):
        raise ValueError("nonorthogonal environment map would change the norm")
    result: Ray = {}
    for bits, amplitude in ray.items():
        for e_after in range(2):
            coefficient = m[e_after][bits[2]] if bits[control] else int(e_after == bits[2])
            label = (bits[0], bits[1], e_after)
            result[label] = result.get(label, Q()) + _r(amplitude) * coefficient
    result = {key: value for key, value in result.items() if value}
    if _norm2(result) != _norm2(ray):
        raise AssertionError("declared orthogonal update was not norm preserving")
    return result


def density_ab(ray: Mapping[tuple[int, int, int], Q]) -> dict[tuple[tuple[int, int], tuple[int, int]], Q]:
    """Exact reduced AB density, computed independently by partial trace E."""
    _check_ray(ray, 3)
    norm2 = _norm2(ray)
    result: dict[tuple[tuple[int, int], tuple[int, int]], Q] = {}
    for (a, b, e), amp in ray.items():
        for (aa, bb, ee), other in ray.items():
            if e == ee:
                k = ((a, b), (aa, bb))
                result[k] = result.get(k, Q()) + _r(amp)*_r(other)/norm2
    return {key: value for key, value in result.items() if value}


def density_e(ray: Mapping[tuple[int, int, int], Q]) -> dict[tuple[int, int], Q]:
    """Exact reduced E density, partial trace AB."""
    _check_ray(ray, 3)
    norm2 = _norm2(ray)
    result: dict[tuple[int, int], Q] = {}
    for (a, b, e), amp in ray.items():
        for (aa, bb, ee), other in ray.items():
            if (a, b) == (aa, bb):
                key = (e, ee)
                result[key] = result.get(key, Q()) + _r(amp)*_r(other)/norm2
    return {key: value for key, value in result.items() if value}


def density_purity(rho: Mapping[tuple[object, object], Q]) -> Q:
    return sum((_r(amp) * _r(rho.get((j, i), Q())) for (i, j), amp in rho.items()), Q())


def bell_plus_fidelity(rho_ab: Mapping[tuple[tuple[int, int], tuple[int, int]], Q]) -> Q:
    return sum((_r(rho_ab.get(((a, a), (b, b)), Q())) for a in (0, 1) for b in (0, 1)), Q()) / 2


def marker_overlap(ray: Mapping[tuple[int, int, int], Q]) -> Q:
    """For rays with AB support 00/11, equal positive branch weight only.

    Returns real normalized <e0|e1>, *not* a general state purity proxy.
    """
    _check_ray(ray, 3)
    if any(a != b for a, b, e in ray):
        raise ValueError("requires the 00/11 code subspace")
    e0 = (Q(ray.get((0, 0, 0), 0)), Q(ray.get((0, 0, 1), 0)))
    e1 = (Q(ray.get((1, 1, 0), 0)), Q(ray.get((1, 1, 1), 0)))
    norm0 = sum((x*x for x in e0), Q())
    norm1 = sum((x*x for x in e1), Q())
    if norm0 != norm1 or norm0 == 0:
        raise ValueError("balanced, nonzero marker branches required")
    return sum((x*y for x,y in zip(e0,e1)), Q())/norm0


def purity_from_overlap(gamma: int | Q) -> Q:
    g = _r(gamma)
    if abs(g) > 1:
        raise ValueError("normalized state overlap must have |gamma|<=1")
    return (1 + g*g)/2


def fidelity_from_overlap(gamma: int | Q) -> Q:
    g = _r(gamma)
    if abs(g) > 1:
        raise ValueError("normalized state overlap must have |gamma|<=1")
    return (1+g)/2


def independent_reservoir_overlap(gammas: Sequence[int | Q]) -> Q:
    """If branch states factor across independent reservoirs, overlap multiplies."""
    total = Q(1)
    for gamma in gammas:
        g = _r(gamma)
        if abs(g) > 1:
            raise ValueError("normalized reservoir overlaps have modulus<=1")
        total *= g
    return total


def phase_dephasing_step(gamma: int | Q, q: int | Q) -> Q:
    """CPTP Pauli-Z dephasing: rho -> (1-q)rho+q ZrhoZ.

    Restricted 0<=q<=1/2 to form a monotonic *positive-rate* family.
    This model cannot raise |gamma| or recohere a zero overlap.
    """
    g = _r(gamma)
    prob = _r(q)
    if abs(g) > 1 or not 0 <= prob <= Q(1, 2):
        raise ValueError("requires valid overlap and monotone dephasing q in [0,1/2]")
    return g*(1-2*prob)


def minimum_normalized_purity(dimension: int) -> Q:
    """Tr(rho^2)>=1/d for d-dimensional density operators, exact bound."""
    if type(dimension) is not int or dimension < 1:
        raise ValueError("positive finite Hilbert dimension required")
    return Q(1, dimension)


@dataclass(frozen=True)
class PrimePowerLabel:
    """Exact integer support only; symbolic Weil coefficient, no fake floats.

    Prime-power local term is log(p)/sqrt(p**k), NOT 'negative energy'.
    The overall sign must be assigned separately by the declared Weil form.
    """
    prime: int
    exponent: int
    @property
    def integer(self) -> int:
        return self.prime ** self.exponent
    @property
    def formula(self) -> str:
        return f"log({self.prime})/({self.prime}**({self.exponent}/2))"


def prime_power_label(n: int) -> PrimePowerLabel | None:
    """Return actual (p,k) iff n=p^k, p prime and k>=1.

    Distinct from fake composite 'prime place' at n=6. n=1 -> None.
    """
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return None
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            k, m = 0, n
            while m % p == 0:
                m //= p
                k += 1
            return PrimePowerLabel(p,k) if m == 1 else None
    return PrimePowerLabel(n,1)


def prime_power_controlled_kick(ray: Mapping[tuple[int, int, int], Q],
                                source_index: int, control: int = 0) -> Ray:
    """Freely chosen R90 kick gated by honest prime-power support.

    Mathematically SOURCE-LABELLED, not physically/analytically DERIVED from
    log(p)/p^(k/2). This does not realize any Weil distribution.
    """
    label = prime_power_label(source_index)
    if label is None:
        raise ValueError("genuine prime-power index required")
    return rotate_shared_environment(ray, control, R90)


def ordered_event_recoherence(indices: Sequence[int]) -> tuple[Q, Q, Q]:
    """Return (overlap,purity,fidelity) after prime-power-labelled shared kicks."""
    ray = initial_bell_environment()
    for n in indices:
        ray = prime_power_controlled_kick(ray, n)
    g = marker_overlap(ray)
    rho_ab = density_ab(ray)
    return g, density_purity(rho_ab), bell_plus_fidelity(rho_ab)
