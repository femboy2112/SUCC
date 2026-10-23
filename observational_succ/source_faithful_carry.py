"""Exact one-based carry, character and disclosed-defect source models.

Paper authority: research/2026-10-23/SOURCE_FAITHFUL_CARRY.md.  This module
checks finite source actions; it does not certify infinite Hilbert/continuum
theorems or the signed completed Weil form.  Composite radices are legitimate
coordinate changes, but are not authenticated primitive prime generators.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt, prod
from typing import Iterable, Mapping

from .reality_pin_arithmetic import log_interval


class CarrySourceError(ValueError):
    """An exact arithmetic/source contract was not met."""


def _int(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise CarrySourceError(f"exact integer >= {minimum} required")
    return n


def _q(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise CarrySourceError("exact int/Fraction coefficients required")
    return Q(x)


def radix_address(n: int, radix: int) -> tuple[int, int]:
    """W_a e_n = e_m tensor e_r; n=a(m-1)+r+1."""
    _int(n, 1); _int(radix, 1)
    m, r = divmod(n - 1, radix)
    return m + 1, r


def source_address(m: int, residue: int, radix: int) -> int:
    _int(m, 1); _int(radix, 1); _int(residue)
    if residue >= radix:
        raise CarrySourceError("residue outside the complete radix register")
    return radix * (m - 1) + residue + 1


def carry_power(m: int, residue: int, radix: int, steps: int = 1) -> tuple[int, int]:
    """W_a S^steps W_a*: all carries, not a residue-only cyclic shift."""
    source_address(m, residue, radix); _int(steps)
    carry, new_r = divmod(residue + steps, radix)
    return m + carry, new_r


def carry_adjoint_power(m: int, residue: int, radix: int,
                        steps: int = 1) -> tuple[int, int] | None:
    """W_a (S*)^steps W_a*: None is the zero ket, not source label 0."""
    n = source_address(m, residue, radix); _int(steps)
    return radix_address(n - steps, radix) if n > steps else None


def residue_channel(n: int, radix: int, residue: int) -> int:
    return source_address(n, residue, radix)


def residue_adjoint(n: int, radix: int, residue: int) -> int | None:
    source_address(1, residue, radix)
    m, r = radix_address(n, radix)
    return m if r == residue else None


def multiplier(n: int, radix: int) -> int:
    """Mathematical V_a for every a>=1; no automatic primality authority."""
    return _int(n, 1) * _int(radix, 1)


def multiplier_adjoint(n: int, radix: int) -> int | None:
    _int(n, 1); _int(radix, 1)
    return n // radix if n % radix == 0 else None


def mixed_address(n: int, radices: Iterable[int]) -> tuple[int, tuple[int, ...]]:
    """Little-endian digits, with the read-order word retained separately."""
    _int(n, 1)
    digits = []
    for a in radices:
        n, r = radix_address(n, a)
        digits.append(r)
    return n, tuple(digits)


def mixed_source(m: int, digits: Iterable[int], radices: Iterable[int]) -> int:
    ds, rs = tuple(digits), tuple(radices)
    _int(m, 1)
    if len(ds) != len(rs):
        raise CarrySourceError("one digit for each retained radix letter")
    for a, r in reversed(tuple(zip(rs, ds))):
        m = source_address(m, r, a)
    return m


def rebase_digits(m: int, digits: Iterable[int], radices: Iterable[int],
                  target_radices: Iterable[int]) -> tuple[int, tuple[int, ...]]:
    rs, ts = tuple(radices), tuple(target_radices)
    for a in rs + ts:
        _int(a, 1)
    if prod(rs) != prod(ts):
        raise CarrySourceError("coordinate comparison requires the same total radix")
    return mixed_address(mixed_source(m, digits, rs), ts)


def character_phase(radix: int, frequency: int, residue: int,
                    *, origin: int = 0, sign: int = 1) -> Q:
    """Exact turns of the KET character exp(sign*2pi*i*k*(r-origin)/a).

    Rational phases retain information discarded by absolute-value checks.
    An arbitrary signed origin is permitted.  The bra coefficient has minus
    this phase; no floating complex approximation is a certificate.
    """
    _int(radix, 1); _int(residue)
    if type(frequency) is not int or type(origin) is not int:
        raise CarrySourceError("integer character frequency and origin required")
    if type(sign) is not int or sign not in (-1, 1) or residue >= radix:
        raise CarrySourceError("declared orientation +/-1 and valid residue required")
    return Q(sign * frequency * (residue - origin), radix) % 1


def character_conductor(radix: int, frequency: int) -> int:
    _int(radix, 1)
    if type(frequency) is not int:
        raise CarrySourceError("integer frequency required")
    return radix // gcd(radix, frequency)


def multiplier_character(radix: int, frequency: int, *, origin: int = 0,
                         sign: int = 1) -> tuple[Q, Q]:
    """(squared magnitude, bra phase in turns) of <chi|W_a V_a>."""
    return Q(1, _int(radix, 1)), (-character_phase(
        radix, frequency, radix - 1, origin=origin, sign=sign)) % 1


def refined_character_phase(a: int, b: int, frequency: int, r: int, s: int,
                            *, sign: int = 1) -> tuple[Q, Q, Q]:
    """Global phase and exact two factors for R=r+a*s in radix a*b.

    The r factor has denominator a*b (the Fourier twiddle); substituting a
    local a-character generally changes the source phase.
    """
    source_address(1, r, a); source_address(1, s, b)
    full = character_phase(a*b, frequency, r+a*s, sign=sign)
    low = character_phase(a*b, frequency, r, sign=sign)
    high = character_phase(b, frequency, s, sign=sign)
    return full, low, high


def exact_vector(vector: Mapping[int, int | Q]) -> dict[int, Q]:
    out = {}
    for n, value in vector.items():
        _int(n, 1)
        x = _q(value)
        if x:
            out[n] = x
    return out


def source_push(vector: Mapping[int, int | Q], action) -> dict[int, Q]:
    """Linear action of a declared source-basis map, including zero kets."""
    out: dict[int, Q] = {}
    for n, value in exact_vector(vector).items():
        m = action(n)
        if m is not None:
            _int(m, 1)
            out[m] = out.get(m, Q()) + value
    return {n: value for n, value in out.items() if value}


def norm_squared(vector: Mapping[int, int | Q]) -> Q:
    return sum((v*v for v in exact_vector(vector).values()), Q())


def block_project(vector: Mapping[int, int | Q], radix: int) -> dict[int, Q]:
    """P_a=A_a* A_a: rational orthogonal projection to block-constant states."""
    _int(radix, 1)
    sums: dict[int, Q] = {}
    for n, v in exact_vector(vector).items():
        m, _ = radix_address(n, radix)
        sums[m] = sums.get(m, Q()) + v
    return {source_address(m, r, radix): total/radix
            for m, total in sums.items() if total for r in range(radix)}


def split_visible_defect(vector: Mapping[int, int | Q], radix: int
                         ) -> tuple[dict[int, Q], dict[int, Q]]:
    """Coherent orthogonal source pair (P_a f,(I-P_a)f); summing repairs f.

    This pair is NOT a measured/dephased density matrix.  If used as a two-
    outcome instrument, squared norms are probabilities for unit input and
    output cross-coherences are lost unless the environment is kept coherent.
    """
    v = exact_vector(vector)
    visible = block_project(v, radix)
    defect = {n: v.get(n, Q())-visible.get(n, Q()) for n in v.keys() | visible.keys()}
    return visible, {n: x for n, x in defect.items() if x}


def nested_defect_sectors(vector: Mapping[int, int | Q], a: int, b: int
                          ) -> tuple[dict[int, Q], dict[int, Q], dict[int, Q]]:
    """Orthogonal (P_ab f, (P_a-P_ab)f, (I-P_a)f), in source coordinates."""
    _int(a, 1); _int(b, 1)
    v = exact_vector(vector)
    pa, first = split_visible_defect(v, a)
    pab = block_project(v, a*b)
    middle = {n: pa.get(n, Q())-pab.get(n, Q()) for n in pa.keys() | pab.keys()}
    return pab, {n: x for n, x in middle.items() if x}, first


def compressed_successor(steps: int, radix: int) -> dict[int, Q]:
    """Exact coefficients of A_a S^h A_a* in powers of coarse S."""
    _int(steps); _int(radix, 1)
    q, r = divmod(steps, radix)
    out = {q: 1-Q(r, radix)}
    if r:
        out[q+1] = Q(r, radix)
    return out


def uniform_defect(radix: int) -> dict[str, Q | str]:
    """Exact all-state norm ledger for authentic V_a vs uniform lift A_a*."""
    _int(radix, 1)
    return {"visible_norm_squared": Q(1, radix),
            "defect_norm_squared": 1-Q(1, radix),
            "overlap_squared": Q(1, radix),
            "norm_distance_squared": f"2*(1-1/sqrt({radix}))"}


def energy_cocycle_ratio(m: int, residue: int, radix: int) -> Q:
    """Exact exp(B_a(m,r))=source_address/m for W_a H0 W_a*−H0 tensor I."""
    return Q(source_address(m, residue, radix), m)


def coarse_energy_product(m: int, radix: int) -> Q:
    """exp(a*(A_a H0 A_a*−H0)(m)), without inexact logarithms."""
    _int(m, 1); _int(radix, 1)
    return prod((energy_cocycle_ratio(m, r, radix) for r in range(radix)), start=Q(1))


@dataclass(frozen=True)
class PrimePowerHalfDensity:
    """Authenticated coefficient log(p)/sqrt(p**exponent), not a Weil form."""
    prime: int
    exponent: int

    def __post_init__(self):
        _int(self.prime, 2); _int(self.exponent, 1)
        if any(self.prime % d == 0 for d in range(2, isqrt(self.prime)+1)):
            raise CarrySourceError("primitive generator must be a rational prime")

    @property
    def endpoint(self) -> int:
        return self.prime ** self.exponent

    @property
    def input_state(self) -> int:
        return self.prime ** (self.exponent-1)

    @property
    def dirichlet_log_coefficient(self) -> Q:
        return Q(1, self.exponent)

    def interval(self, *, terms: int = 24, binary_places: int = 64) -> tuple[Q, Q]:
        """Rigorous rational interval, using exact log tail and integer square root."""
        _int(terms, 1); _int(binary_places, 1)
        lo, hi = log_interval(self.prime, terms=terms)
        scale = 1 << binary_places
        root = isqrt(self.endpoint * scale * scale)
        sqrtlo = Q(root, scale)
        sqrthi = sqrtlo if root*root == self.endpoint*scale*scale else Q(root+1, scale)
        return lo/sqrthi, hi/sqrtlo


def prime_power_at(endpoint: int) -> PrimePowerHalfDensity | None:
    """Unique prime-power source witness; mixed-prime endpoint 6 is rejected."""
    _int(endpoint, 1)
    if endpoint == 1:
        return None
    for p in range(2, isqrt(endpoint)+1):
        if endpoint % p == 0:
            n, r = endpoint, 0
            while n % p == 0:
                n //= p
                r += 1
            return PrimePowerHalfDensity(p, r) if n == 1 else None
    return PrimePowerHalfDensity(endpoint, 1)
