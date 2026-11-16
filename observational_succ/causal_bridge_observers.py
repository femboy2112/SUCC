"""Source-relative twin interferometer: entanglement as shape, not a message.

Exact rational causal paths, gauge-covariant *present* reports, formal
Q(i)[Q/Z] Bell correlations, and a Choi/Bell mirror (tensor-network) identity.
These are mathematical models, not spacetime wormholes or physical claims.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping


@dataclass(frozen=True)
class Event:
    name: str
    time: Q
    space: Q

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("event must have a name")
        object.__setattr__(self, "time", Q(self.time))
        object.__setattr__(self, "space", Q(self.space))


@dataclass(frozen=True)
class LocalLink:
    source: Event
    target: Event
    phase_turns: Q

    def __post_init__(self):
        object.__setattr__(self, "phase_turns", Q(self.phase_turns))
        dt = self.target.time - self.source.time
        dx = self.target.space - self.source.space
        if dt <= 0 or dt < abs(dx) or self.target == self.source:
            raise ValueError("local link must be future timelike/null (c=1)")


@dataclass(frozen=True)
class CausalWalk:
    links: tuple[LocalLink, ...]
    source_contract: str

    def __post_init__(self):
        if not self.links or not self.source_contract:
            raise ValueError("nonempty path and source contract required")
        if any(self.links[i].target != self.links[i + 1].source
               for i in range(len(self.links) - 1)):
            raise ValueError("path links must connect in causal order")

    @property
    def start(self) -> Event:
        return self.links[0].source

    @property
    def meeting(self) -> Event:
        return self.links[-1].target


@dataclass(frozen=True)
class PresentOutput:
    """Only a *current* value: no remote past event is compared directly."""
    meeting: Event
    model_phase_turns: Q
    source_contract: str
    frame: str = "meeting"

    def __post_init__(self):
        object.__setattr__(self, "model_phase_turns", Q(self.model_phase_turns) % 1)
        if not self.source_contract or not self.frame:
            raise ValueError("frame and source contract required")


def current_output(path: CausalWalk, source_calibration: Q | int, *, frame: str = "meeting") -> PresentOutput:
    """Causal path is consumed into one present-time model output."""
    value = Q(source_calibration) + sum((edge.phase_turns for edge in path.links), Q())
    return PresentOutput(path.meeting, value % 1, path.source_contract, frame)


def meeting_phase(a: PresentOutput, b: PresentOutput) -> Q:
    """Compare *only* present outputs after both entered the same chart."""
    if a.meeting != b.meeting or a.frame != b.frame:
        raise ValueError("outputs are not at same meeting event and frame")
    if a.source_contract != b.source_contract:
        raise ValueError("source contracts differ")
    return (a.model_phase_turns - b.model_phase_turns) % 1


def gauge_transform(path: CausalWalk, calibration: Q | int, gauge: Mapping[Event, Q | int]) -> tuple[CausalWalk, Q]:
    """Gauge edge A_ij -> A_ij + g(j)-g(i), source pin c -> c+g(start).

    Each current output changes by +g(meeting), so meeting difference is invariant.
    This requires a *shared* gauge on the ambient carrier, not independent relabeling.
    """
    points = {e for link in path.links for e in (link.source, link.target)}
    if not points.issubset(gauge):
        raise ValueError("gauge must specify every vertex")
    edges = tuple(LocalLink(e.source, e.target,
                            e.phase_turns + Q(gauge[e.target]) - Q(gauge[e.source]))
                  for e in path.links)
    return CausalWalk(edges, path.source_contract), Q(calibration) + Q(gauge[path.start])


@dataclass(frozen=True)
class Gaussian:
    real: Q = Q(0)
    imag: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "real", Q(self.real))
        object.__setattr__(self, "imag", Q(self.imag))

    def __add__(self, other: Gaussian) -> Gaussian:
        return Gaussian(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> Gaussian:
        return Gaussian(-self.real, -self.imag)

    def __mul__(self, other: Gaussian) -> Gaussian:
        return Gaussian(self.real*other.real - self.imag*other.imag,
                        self.real*other.imag + self.imag*other.real)

    def conjugate(self) -> Gaussian:
        return Gaussian(self.real, -self.imag)


ZERO, ONE, II = Gaussian(), Gaussian(1), Gaussian(0, 1)


@dataclass(frozen=True)
class FormalFourier:
    """Exact finite Q(i)[Q/Z] character sum; *not* a numerical estimate."""
    terms: tuple[tuple[Q, Gaussian], ...] = ()

    def __post_init__(self):
        accumulator: dict[Q, Gaussian] = {}
        for frequency, coefficient in self.terms:
            if not isinstance(coefficient, Gaussian):
                raise TypeError("Gaussian coefficients required")
            frequency = Q(frequency) % 1
            accumulator[frequency] = accumulator.get(frequency, ZERO) + coefficient
        object.__setattr__(self, "terms", tuple(sorted((k, v) for k,v in accumulator.items() if v != ZERO)))

    @classmethod
    def char(cls, q: Q | int) -> FormalFourier:
        return cls(((Q(q) % 1, ONE),))

    def __add__(self, rhs: FormalFourier) -> FormalFourier:
        return FormalFourier(self.terms + rhs.terms)

    def scale(self, coefficient: Gaussian) -> FormalFourier:
        return FormalFourier(tuple((frequency, amplitude * coefficient)
                                   for frequency, amplitude in self.terms))

    def eval_quarter(self) -> Gaussian:
        """Exact cyclotomic evaluation only if every frequency is k/4."""
        powers = (ONE, II, Gaussian(-1), Gaussian(0, -1))
        total = ZERO
        for q, coefficient in self.terms:
            if (4*q).denominator != 1:
                raise ValueError("not a quarter-period character: retain symbolic form")
            total = total + coefficient * powers[int(4*q) % 4]
        return total


def bell_joint_observables(relative_turns: Q | int) -> tuple[FormalFourier, FormalFourier]:
    """For |00>+e(q)|11>, return <XX>=cos(2πq), <XY>=sin(2πq).

    This pair requires distinct measurement settings/ensembles; it is *not* a
    deterministic readout of one Bell pair, nor a measurement before reunion.
    """
    q = Q(relative_turns) % 1
    pos, neg = FormalFourier.char(q), FormalFourier.char(-q)
    cos = pos.scale(Gaussian(Q(1, 2))) + neg.scale(Gaussian(Q(1, 2)))
    sin = pos.scale(Gaussian(0, Q(-1, 2))) + neg.scale(Gaussian(0, Q(1, 2)))
    return cos, sin


def local_bell_marginal(relative_turns: Q | int) -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    """Both local density operators are I/2 for *every* Bell relative phase."""
    Q(relative_turns)
    return ((Q(1, 2), Q()), (Q(), Q(1, 2)))


def classical_dephased_observables() -> tuple[FormalFourier, FormalFourier]:
    """Same local marginals as Bell, no off-diagonal correlation signal."""
    return FormalFourier(), FormalFourier()


def choi_left_and_mirrored_right(matrix: tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]) -> tuple[tuple[Gaussian,...], tuple[Gaussian,...]]:
    """(M⊗I)|Φ+>=(I⊗M^T)|Φ+> as four unnormalised amplitudes.

    This *diagrammatic mirror* is not an operational remote gate or a channel.
    """
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("2x2 matrix required")
    if any(not isinstance(v, Gaussian) for row in matrix for v in row):
        raise TypeError("exact Gaussian matrix required")
    bell = ((ONE, ZERO), (ZERO, ONE))
    # Explicitly compute the two actions independently; right uses transpose.
    left = tuple(sum_gaussian(matrix[a][j] * bell[j][b] for j in range(2))
                 for a in range(2) for b in range(2))
    right = tuple(sum_gaussian(bell[a][j] * matrix[j][b] for j in range(2))
                  for a in range(2) for b in range(2))
    return left, right


def sum_gaussian(values) -> Gaussian:
    result = ZERO
    for x in values:
        result = result + x
    return result


def original_bbp_r(n: int) -> Q:
    """Independent four-pole transcription to be cross-checked with source API."""
    if type(n) is not int or n < 1:
        raise ValueError("integer n>=1 required")
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def original_bbp_state(n: int, seed: Q | int = 0) -> Q:
    """Unwrapped U_n(s), exact rational; not a π equidistribution claim."""
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 required")
    u = Q(seed)
    for m in range(1, n+1):
        u = 16*u + original_bbp_r(m)
    return u


def original_bbp_seed_recovery(n: int, state: Q | int) -> Q:
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 required")
    p = sum((original_bbp_r(m) / 16**m for m in range(1,n+1)), Q())
    return Q(state)/16**n - p
