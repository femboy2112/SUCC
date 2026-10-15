"""Source-indexed finite mathematical checks for physically grounded SUCC.

This is a mathematical *laboratory*, not a source-authenticated Higgs dataset,
not a reconstruction of the actual Standard Model, not a universal physical
carrier, and not a proof of RH. All inputs are stipulated, exact toy readings.

Four independent interfaces:
  1. Electroweak tree-level *relations* between mass and Higgs vertices;
  2. Sphere-angle moments and a detector-acceptance/dimension alias;
  3. Finite quantum-state Gram kernels and phase/holonomy alias;
  4. Arithmetic local shell coefficients and a fake-composite mutation.

See research/2026-10-13/EMPIRICAL_CARRIER_RECONSTRUCTION.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import gamma, pi
from typing import Sequence


class CarrierEvidenceError(ValueError):
    """Invalid mathematical source claim, channel normalization or witness."""


def rational_positive(x: Q) -> Q:
    """Only exact, positive rationals; floats cannot issue certificates."""
    if type(x) not in (int, Q) or x <= 0:
        raise CarrierEvidenceError("positive integer/Fraction required (no floats)")
    return Q(x)


@dataclass(frozen=True)
class HiggsChannel:
    """Stipulated extracted on-shell TREE-LEVEL effective vertex, not raw data.

    Fermion:  g_hff = mf/v,  input mass is mf, vertex is dimensionless.
    Vector:   g_hVV = 2*mV**2/v, input mass is mV, vertex has mass dimension 1.
    Both use a declared common mass unit, source id and extraction scheme.
    Higher-order corrections, running and mixing are NOT handled here.
    """
    name: str
    sector: str
    mass: Q
    vertex: Q
    source_id: str
    epoch: int
    scheme: str = "tree-SM-normalized"

    def __post_init__(self) -> None:
        if not self.name or self.sector not in ("fermion", "vector"):
            raise CarrierEvidenceError("named fermion/vector channel required")
        rational_positive(self.mass)
        rational_positive(self.vertex)
        if not self.source_id or type(self.epoch) is not int or self.epoch < 0:
            raise CarrierEvidenceError("source and nonnegative epoch required")
        if self.scheme != "tree-SM-normalized":
            raise CarrierEvidenceError("cannot silently compare different vertex conventions")

    @property
    def inferred_vev(self) -> Q:
        if self.sector == "fermion":
            return Q(self.mass) / Q(self.vertex)
        return 2 * Q(self.mass) ** 2 / Q(self.vertex)


@dataclass(frozen=True)
class HiggsScaleAudit:
    compatible: bool
    scales: tuple[Q, ...]
    cross_sector: bool
    first_conflict: tuple[str, str] | None
    source_id: str
    epoch: int
    empirical_measurement_claimed: bool = False


def audit_higgs_scale(channels: Sequence[HiggsChannel]) -> HiggsScaleAudit:
    """Verify conditional equality of independently *declared* effective scales.

    Returns a witness pair for an incompatible set. A successful comparison
    does NOT identify the full quantum field theory or authenticate its inputs.
    """
    channels = tuple(channels)
    if not channels:
        raise CarrierEvidenceError("at least one channel required")
    origin = (channels[0].source_id, channels[0].epoch, channels[0].scheme)
    for channel in channels:
        if not isinstance(channel, HiggsChannel):
            raise CarrierEvidenceError("unexpected channel")
        if (channel.source_id, channel.epoch, channel.scheme) != origin:
            raise CarrierEvidenceError("different source epochs or extraction schemes")
    scales = tuple(c.inferred_vev for c in channels)
    clash = next(((channels[0].name, c.name) for c in channels[1:]
                  if c.inferred_vev != scales[0]), None)
    return HiggsScaleAudit(
        compatible=clash is None,
        scales=scales,
        cross_sector={c.sector for c in channels} == {"fermion", "vector"},
        first_conflict=clash,
        source_id=origin[0],
        epoch=origin[1],
    )


def angular_even_moment(dimension: int, order: int) -> Q:
    """E[cos(theta)^(2*order)] for uniform direction on S^(d-1).

    Exact formula (1/2)_order / (d/2)_order, for integer d>=2.
    Density of u=cos theta is proportional to (1-u^2)^((d-3)/2).
    """
    if type(dimension) is not int or dimension < 2:
        raise CarrierEvidenceError("spatial dimension must be integer >=2")
    if type(order) is not int or order < 0:
        raise CarrierEvidenceError("nonnegative integer moment order required")
    result = Q(1)
    for j in range(order):
        result *= Q(2*j + 1, dimension + 2*j)
    return result


def effective_angular_dimension(dimension: int, acceptance_power: int) -> int:
    """A(u)=(1-u^2)^k makes d-dimensional isotropy look (d+2k)-dimensional.

    Acceptance A is pointwise within [0,1], k>=0 integer. Normalization
    of accepted-event histogram erases the total-efficiency scale.
    """
    angular_even_moment(dimension, 0)
    if type(acceptance_power) is not int or acceptance_power < 0:
        raise CarrierEvidenceError("nonnegative integer angular acceptance exponent")
    return dimension + 2*acceptance_power


def compatible_angular_carriers(observed_second_moment: Q) -> tuple[tuple[int, int], ...]:
    """All isotropic d>=2 and detector powers k>=0 compatible with E[u^2].

    Only meaningful under the finite family A(u)=(1-u^2)^k and full angular
    coverage except zero-measure endpoints; not generic detector inference.
    """
    m2 = rational_positive(observed_second_moment)
    n = Q(1) / m2
    if n.denominator != 1 or n < 2:
        return ()
    eff = int(n)
    return tuple((eff-2*k, k) for k in range((eff-2)//2 + 1))


def calibrated_angular_dimension(observed_second_moment: Q, known_acceptance_power: int) -> int:
    """Recover d ONLY after an independent accepted-response model is supplied."""
    effective_angular_dimension(2, known_acceptance_power)  # validates integer k>=0
    possibilities = compatible_angular_carriers(observed_second_moment)
    candidates = [d for d, k in possibilities if k == known_acceptance_power]
    if len(candidates) != 1:
        raise CarrierEvidenceError("calibrated angular observation contradicts family")
    return candidates[0]


@dataclass(frozen=True)
class RateFactorization:
    """Unnormalised positive toy rates = acceptance * geometry * amplitude_sq."""
    phase_space: tuple[Q, ...]
    amplitude_sq: tuple[Q, ...]
    acceptance: tuple[Q, ...]

    def __post_init__(self) -> None:
        if not self.phase_space or not (len(self.phase_space) == len(self.amplitude_sq) == len(self.acceptance)):
            raise CarrierEvidenceError("equal nonempty channel vectors required")
        for p, a, e in zip(self.phase_space, self.amplitude_sq, self.acceptance):
            rational_positive(p)
            rational_positive(a)
            rational_positive(e)
            if e > 1:
                raise CarrierEvidenceError("acceptance is a probability <=1")

    @property
    def observations(self) -> tuple[Q, ...]:
        return tuple(Q(p)*Q(a)*Q(e) for p, a, e
                     in zip(self.phase_space, self.amplitude_sq, self.acceptance))


def rate_reparameterize(world: RateFactorization, scales: Sequence[Q]) -> RateFactorization:
    """(phase, amplitude^2)->(phase*c, amplitude^2/c) preserves every rate."""
    if len(scales) != len(world.phase_space):
        raise CarrierEvidenceError("one positive gauge scale per outcome")
    c = tuple(rational_positive(a) for a in scales)
    return RateFactorization(
        phase_space=tuple(Q(p)*x for p, x in zip(world.phase_space,c)),
        amplitude_sq=tuple(Q(a)/x for a,x in zip(world.amplitude_sq,c)),
        acceptance=world.acceptance,
    )


def gram_example(sign: int) -> tuple[tuple[Q, ...], ...]:
    """Two distinct real 3x3 pure-state Gram structures with equal pair rates.

    r=1/4, all diagonal entries 1, all off-diagonal magnitudes r;
    triple Bargmann product is sign/64. Matrices positive definite by strict
    diagonal dominance. These are source-specified quantum models, not data.
    """
    if type(sign) is not int or sign not in (-1,1):
        raise CarrierEvidenceError("choose a +/- phase sign")
    r = Q(1,4)
    return ((Q(1),r,sign*r), (r,Q(1),r), (sign*r,r,Q(1)))


def quantum_rate_signature(gram: tuple[tuple[Q,...],...]) -> tuple[Q,Q,Q]:
    """Pairwise transition-probability measurements |<i|j>|^2."""
    if len(gram) != 3 or any(len(row)!=3 for row in gram):
        raise CarrierEvidenceError("real 3x3 gram expected")
    if any(gram[i][j] != gram[j][i] for i in range(3) for j in range(3)):
        raise CarrierEvidenceError("Hermitian (real symmetric) matrix required")
    if any(gram[i][i] != 1 for i in range(3)):
        raise CarrierEvidenceError("normalized states only")
    return tuple(gram[i][j]**2 for i,j in ((0,1),(1,2),(2,0)))


def quantum_triangle_phase(gram: tuple[tuple[Q,...],...]) -> Q:
    """Bargmann triple product, invariant under each state's +/- phase gauge."""
    quantum_rate_signature(gram)
    return gram[0][1]*gram[1][2]*gram[2][0]


def gram_positive_definite(gram: tuple[tuple[Q,...],...]) -> bool:
    """Sylvester's criterion for a rational, real-symmetric 3x3 Gram matrix."""
    quantum_rate_signature(gram)
    a,b,c=gram[0]
    d,e=gram[1][1],gram[1][2]
    f=gram[2][2]
    det=a*d*f + 2*b*c*e - a*e*e - d*c*c - f*b*b
    return a>0 and a*d-b*b>0 and det>0


def phase_gauge(gram: tuple[tuple[Q,...],...], signs: Sequence[int]) -> tuple[tuple[Q,...],...]:
    """Gauge K_ij -> e_i K_ij e_j for real unit phases e_i in {+1,-1}."""
    if len(signs)!=3 or any(type(s) is not int or s not in (-1,1) for s in signs):
        raise CarrierEvidenceError("three signed phase choices required")
    quantum_rate_signature(gram)
    return tuple(tuple(signs[i]*gram[i][j]*signs[j] for j in range(3)) for i in range(3))


def local_shell_factor(base: int, exponent: int, depth: int | None=None, *, prime_required: bool=True) -> Q:
    """Formal local shell expansion sum_{k>=0} base^(-k*s), Re(s)>0.

    base must be prime for honest Q_p. A nonprime base is allowed ONLY when
    prime_required=False, to construct explicit fake-Euler negative controls.
    This is algebra over fractions, not an experimentally measured p-adic space.
    """
    if type(base) is not int or base < 2 or type(exponent) is not int or exponent < 1:
        raise CarrierEvidenceError("integer base>=2 and s>=1 required")
    if prime_required and any(base%j==0 for j in range(2,int(base**0.5)+1)):
        raise CarrierEvidenceError("a composite integer is not a finite place")
    if depth is None:
        return Q(base**exponent, base**exponent-1)
    if type(depth) is not int or depth < 0:
        raise CarrierEvidenceError("nonnegative finite shell cutoff required")
    return sum((Q(1,base**(k*exponent)) for k in range(depth+1)), Q(0))


def finite_euler_coefficients(factors: Sequence[int], max_n: int, *, enforce_primes=True) -> dict[int,int]:
    """Count source representations n=product_i factor_i^k, n<=max_n.

    Valid prime set gives coefficients 0/1 from unique factorization.
    Appending composite 6 to (2,3) gives n=6 multiplicity 2: fake-source
    negative control. This is a coefficient oracle, not zeta analytic closure.
    """
    if type(max_n) is not int or max_n < 1 or len(set(factors)) != len(factors):
        raise CarrierEvidenceError("positive bound; no duplicate factors")
    for p in factors:
        local_shell_factor(p, 1, 0, prime_required=enforce_primes)
    counts={1:1}
    for p in factors:
        nxt={}
        for n, multiplicity in counts.items():
            m=n
            while m<=max_n:
                nxt[m]=nxt.get(m,0)+multiplicity
                m*=p
        counts=nxt
    return dict(sorted(counts.items()))


def gaussian_radial_mellin(dimension: int, real_s: float) -> float:
    """NUMERICAL diagnostic, not proof: pi^((d-s)/2) Gamma(s/2)/Gamma(d/2).

    Real d>=1; s>0. For complex s need analytic continuation/test-domain
    control elsewhere. The value at s=d is 1, from Gaussian normalization.
    """
    if type(dimension) is not int or dimension < 1 or real_s<=0:
        raise CarrierEvidenceError("d>=1, s>0")
    return pi**((dimension-real_s)/2)*gamma(real_s/2)/gamma(dimension/2)


def normalized_archimedean_mellin(dimension: int, real_s: float) -> float:
    """Numerical shadow 2/Omega_(d-1) * Gaussian d-ball Mellin integral.

    Analytically, for every d>=1 and Re(s)>0 this is exactly
    pi^(-s/2)*Gamma(s/2), INDEPENDENT of d.
    The Gaussian and Mellin weight are DECLARED probe choices, not observed
    Higgs phase-space weights or an inferred physical prime Euler product.
    """
    if type(dimension) is not int or dimension<1:
        raise CarrierEvidenceError("dimension>=1 required")
    norm = gamma(dimension/2)/pi**(dimension/2)
    return norm*gaussian_radial_mellin(dimension,real_s)
