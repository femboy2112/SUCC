"""Exact, source-bound certificates for predictable report horizons.

For a total finite source T and report h, horizon n is admitted precisely when
h(T**n(x)) depends only on h(x), globally over the declared source table.
This is model-relative report descent, not inference of a law from samples.
See research/2026-11-14/knowledge_volume/HORIZON_THEOREMS.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from heapq import heappop, heappush
import json
from math import gcd


def _natural(value: int, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


@dataclass(frozen=True)
class FiniteReportedSource:
    """States are 0..N-1; report labels are contiguous 0..R-1.

    The whole table is the declared invariant domain. Restricting to a sample
    of visited states is not a certificate for this domain.
    """

    transition: tuple[int, ...]
    report: tuple[int, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "transition", tuple(self.transition))
        object.__setattr__(self, "report", tuple(self.report))
        size = len(self.transition)
        if not size or len(self.report) != size:
            raise ValueError("nonempty transition and report tables must have equal length")
        if any(type(x) is not int or not 0 <= x < size for x in self.transition):
            raise ValueError("transition leaves the declared state domain")
        if any(type(x) is not int or x < 0 for x in self.report):
            raise ValueError("report labels must be nonnegative integers")
        if set(self.report) != set(range(max(self.report) + 1)):
            raise ValueError("report labels must be contiguous and used")

    @property
    def fingerprint(self) -> str:
        payload = {"scheme": "succ.reported-source.v1", "transition": self.transition,
                   "report": self.report}
        return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    @property
    def report_count(self) -> int:
        return max(self.report) + 1


def power_map(source: FiniteReportedSource, horizon: int) -> tuple[int, ...]:
    """Compute T**horizon by squaring, using O(N log(horizon+1)) table work."""
    remaining = _natural(horizon, "horizon")
    result = tuple(range(len(source.transition)))
    base = source.transition
    while remaining:
        if remaining & 1:
            result = tuple(base[x] for x in result)
        remaining >>= 1
        if remaining:
            base = tuple(base[x] for x in base)
    return result


@dataclass(frozen=True)
class HorizonCertificate:
    source_sha256: str
    horizon: int
    induced: tuple[int, ...] | None = None
    collision: tuple[int, int] | None = None

    @property
    def predictable(self) -> bool:
        return self.induced is not None


def _decision(source: FiniteReportedSource, horizon: int,
              power: tuple[int, ...]) -> HorizonCertificate:
    representatives: dict[int, int] = {}
    induced = [-1] * source.report_count
    for state, label in enumerate(source.report):
        future = source.report[power[state]]
        if label in representatives and induced[label] != future:
            return HorizonCertificate(source.fingerprint, horizon,
                                      collision=(representatives[label], state))
        representatives[label] = state
        induced[label] = future
    return HorizonCertificate(source.fingerprint, horizon, induced=tuple(induced))


def certify_horizon(source: FiniteReportedSource, horizon: int) -> HorizonCertificate:
    """Return a full decoder or an explicit equal-present/unequal-future pair."""
    return _decision(source, _natural(horizon, "horizon"), power_map(source, horizon))


def verify_horizon(source: FiniteReportedSource, certificate: HorizonCertificate) -> bool:
    """Replay a claimed positive or negative certificate against exact source bytes."""
    if not isinstance(certificate, HorizonCertificate):
        return False
    if certificate.source_sha256 != source.fingerprint:
        return False
    if type(certificate.horizon) is not int or certificate.horizon < 0:
        return False
    if (certificate.induced is None) == (certificate.collision is None):
        return False
    power = power_map(source, certificate.horizon)
    if certificate.induced is not None:
        mapping = certificate.induced
        if (not isinstance(mapping, tuple) or len(mapping) != source.report_count
                or any(type(y) is not int or not 0 <= y < source.report_count for y in mapping)):
            return False
        return all(mapping[source.report[x]] == source.report[power[x]]
                   for x in range(len(power)))
    pair = certificate.collision
    if (not isinstance(pair, tuple) or len(pair) != 2
            or any(type(x) is not int or not 0 <= x < len(power) for x in pair)):
        return False
    x, z = pair
    return (source.report[x] == source.report[z]
            and source.report[power[x]] != source.report[power[z]])


def compose_horizons(source: FiniteReportedSource, first: HorizonCertificate,
                     second: HorizonCertificate) -> HorizonCertificate:
    """Compose two certified full-report decoders on the same source."""
    if not (verify_horizon(source, first) and verify_horizon(source, second)
            and first.induced is not None and second.induced is not None):
        raise ValueError("composition requires two valid positive same-source certificates")
    mapping = tuple(second.induced[first.induced[y]] for y in range(source.report_count))
    return HorizonCertificate(source.fingerprint, first.horizon + second.horizon, induced=mapping)


@dataclass(frozen=True)
class HorizonProfile:
    """Exact transient/periodic profile certified by repetition of a full T-power.

    A profile reconstructed from external data must pass verify_profile before
    its contains method is trusted; the dataclass is not itself proof authority.
    """

    source_sha256: str
    preperiod: int
    period: int
    admitted: tuple[bool, ...]

    def contains(self, horizon: int) -> bool:
        n = _natural(horizon, "horizon")
        if n >= len(self.admitted):
            n = self.preperiod + (n - self.preperiod) % self.period
        return self.admitted[n]


def horizon_profile(source: FiniteReportedSource, max_powers: int = 100_000) -> HorizonProfile:
    """Find an all-horizon certificate; a resource cap raises, never guesses."""
    cap = _natural(max_powers, "max_powers")
    if not cap:
        raise ValueError("max_powers must be positive")
    seen: dict[tuple[int, ...], int] = {}
    flags: list[bool] = []
    power = tuple(range(len(source.transition)))
    while power not in seen:
        if len(flags) >= cap:
            raise RuntimeError("power-table budget exhausted without a closure certificate")
        n = len(flags)
        seen[power] = n
        flags.append(_decision(source, n, power).predictable)
        power = tuple(source.transition[x] for x in power)
    start = seen[power]
    return HorizonProfile(source.fingerprint, start, len(flags) - start, tuple(flags))


def verify_profile(source: FiniteReportedSource, profile: HorizonProfile) -> bool:
    """Check every recorded power and the closing equality T^(mu+p)=T^mu."""
    if not isinstance(profile, HorizonProfile) or profile.source_sha256 != source.fingerprint:
        return False
    if (type(profile.preperiod) is not int or profile.preperiod < 0
            or type(profile.period) is not int or profile.period <= 0
            or not isinstance(profile.admitted, tuple)
            or len(profile.admitted) != profile.preperiod + profile.period
            or any(type(flag) is not bool for flag in profile.admitted)):
        return False
    power = tuple(range(len(source.transition)))
    start_power = None
    for n, flag in enumerate(profile.admitted):
        if n == profile.preperiod:
            start_power = power
        # Pairwise criterion is intentionally distinct from decoder construction.
        actual = all(source.report[x] != source.report[z]
                     or source.report[power[x]] == source.report[power[z]]
                     for x in range(len(power)) for z in range(x))
        if actual != flag:
            return False
        power = tuple(source.transition[x] for x in power)
    return power == start_power


@dataclass(frozen=True)
class AdditiveHorizonMonoid:
    """Apéry membership from a supplied finite list of positive generators.

    An empty generator list denotes {0}. This is NOT discovery from samples.
    Residue shortest paths compute the least represented value in each class.
    """

    generators: tuple[int, ...]

    def __post_init__(self) -> None:
        raw = tuple(self.generators)
        if any(type(g) is not int or g <= 0 for g in raw):
            raise ValueError("generators must be positive integers; use () for {0}")
        object.__setattr__(self, "generators", tuple(sorted(set(raw))))

    def apery(self) -> tuple[int | None, ...]:
        if not self.generators:
            return ()
        modulus = self.generators[0]
        distances: list[int | None] = [None] * modulus
        distances[0] = 0
        queue = [(0, 0)]
        while queue:
            distance, residue = heappop(queue)
            if distances[residue] != distance:
                continue
            for generator in self.generators:
                candidate = distance + generator
                next_residue = candidate % modulus
                old = distances[next_residue]
                if old is None or candidate < old:
                    distances[next_residue] = candidate
                    heappush(queue, (candidate, next_residue))
        return tuple(distances)

    def contains(self, horizon: int) -> bool:
        n = _natural(horizon, "horizon")
        if not self.generators:
            return n == 0
        least = self.apery()[n % self.generators[0]]
        return least is not None and n >= least

    def tail_parameters(self) -> tuple[int, int]:
        """Return safe threshold c>=1 and period d; c need not be minimal."""
        if not self.generators:
            return (1, 1)
        divisor = 0
        for generator in self.generators:
            divisor = gcd(divisor, generator)
        threshold = max(1, max(x for x in self.apery() if x is not None))
        return threshold, divisor


def realize_horizon_monoid(monoid: AdditiveHorizonMonoid) -> FiniteReportedSource:
    """Finite two-track lasso with exactly the supplied predictable-time monoid.

    Candidate-state domain includes both tracks; this is not a single chosen
    pointed orbit and is not a mutant of the canonical BBP source.
    """
    threshold, period = monoid.tail_parameters()
    positions = threshold + period
    transition: list[int] = []
    report: list[int] = []
    label = 0
    for q in range(positions):
        successor = q + 1 if q + 1 < positions else threshold
        transition.extend((2 * successor, 2 * successor + 1))
        if monoid.contains(q):
            report.extend((label, label))
            label += 1
        else:
            report.extend((label, label + 1))
            label += 2
    return FiniteReportedSource(tuple(transition), tuple(report))
