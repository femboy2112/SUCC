"""Exact toy twin-observer rendezvous, framed present outputs, Bell/environment gates.

Mathematical models only. An entangled pair is chosen as *additional* structure;
no BBP source generates a physical quantum device. No collapse interpretation is
assumed, and a successful Bell projection alone never authenticates both paths.

Use integer/rational exact quantities. Convention for |Phi+>: real ray
(|00>+|11>)/sqrt(2), represented by the unnormalised amplitudes (1,0,0,1).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

Q = Fraction


@dataclass(frozen=True)
class Event:
    """An event or 1+1 vector (t,x), with rational c=1 coordinates."""
    t: Q
    x: Q

    def __post_init__(self) -> None:
        object.__setattr__(self, 't', Q(self.t))
        object.__setattr__(self, 'x', Q(self.x))

    def square(self) -> Q:
        return self.t*self.t - self.x*self.x


@dataclass(frozen=True)
class Frame:
    """Local -> common frame by t=gamma(t'+v x'), x=gamma(x'+v t').

    Explicit rational boost with gamma^2(1-v^2)=1, |v|<1.
    This is a Lorentz chart transform, not transport through curved spacetime.
    """
    v: Q = Q(0)
    gamma: Q = Q(1)

    def __post_init__(self) -> None:
        v, gamma = Q(self.v), Q(self.gamma)
        if not (-1 < v < 1 and gamma > 0 and gamma*gamma*(1-v*v) == 1):
            raise ValueError('require positive gamma and an exact subluminal rational Lorentz boost')
        object.__setattr__(self, 'v', v)
        object.__setattr__(self, 'gamma', gamma)

    def to_common(self, event: Event) -> Event:
        return Event(self.gamma*(event.t + self.v*event.x),
                     self.gamma*(event.x + self.v*event.t))

    def from_common(self, event: Event) -> Event:
        return Event(self.gamma*(event.t - self.v*event.x),
                     self.gamma*(event.x - self.v*event.t))


@dataclass(frozen=True)
class PresentReport:
    """Only current model output + source witness + chart, compared at meeting.

    Past observations are NOT directly compared across space-time patches.
    Source witness is a *mathematical* value, not a physically authenticated log.
    """
    observer: str
    frame: Frame
    meeting_local: Event
    model_local: Event
    clock: int
    selected_unwrapped: Q

    def __post_init__(self) -> None:
        if not self.observer or type(self.clock) is not int or self.clock < 0:
            raise ValueError('observer id and nonnegative clock required')
        object.__setattr__(self, 'selected_unwrapped', Q(self.selected_unwrapped))


@dataclass(frozen=True)
class MeetingVerdict:
    coincident_event: bool
    same_model: bool
    source_a_correct: bool
    source_b_correct: bool

    @property
    def accepts(self) -> bool:
        return (self.coincident_event and self.same_model and
                self.source_a_correct and self.source_b_correct)


def original_bbp_forcing(n: int) -> Q:
    """Exact original four signed poles, for a separated source-pin check."""
    if type(n) is not int or n < 1:
        raise ValueError('n>=1 required')
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def source_invariant(clock: int, unwrapped: Q | int) -> Q:
    """Z_n=16^-n U_n - P_n: at authentic literal seed it equals zero.

    This only verifies an algebraic source/seed claim in the declared model.
    It does NOT certify a physical trajectory, observation, or normality.
    """
    if type(clock) is not int or clock < 0:
        raise ValueError('nonnegative clock required')
    p = sum((original_bbp_forcing(j) / 16**j for j in range(1, clock+1)), Q())
    return Q(unwrapped) / 16**clock - p


def report_from_source(observer: str, frame: Frame, meeting_common: Event,
                       model_common: Event, clock: int, seed: Q | int = 0) -> PresentReport:
    """Toy honest report; no independent historical or physical authentication."""
    if type(clock) is not int or clock < 0:
        raise ValueError('nonnegative clock required')
    u = Q(seed)
    for j in range(1, clock+1):
        u = 16*u + original_bbp_forcing(j)
    return PresentReport(observer, frame, frame.from_common(meeting_common),
                         frame.from_common(model_common), clock, u)


def causal_reachability(origin_common: Event, end_common: Event) -> bool:
    """Future timelike-or-null displacement in a chosen flat 1+1 chart."""
    dt = end_common.t - origin_common.t
    dx = end_common.x - origin_common.x
    return dt >= 0 and dt*dt >= dx*dx


def compare_present(a: PresentReport, b: PresentReport,
                    expected_meeting: Event | None = None) -> MeetingVerdict:
    """Compare ONLY frame-transported, meeting-time outputs and source pins.

    Equality of model values is *not* proof that either model is correct.
    A malicious report can forge both model and witness in this toy model.
    """
    meeting_a, meeting_b = a.frame.to_common(a.meeting_local), b.frame.to_common(b.meeting_local)
    return MeetingVerdict(
        meeting_a == meeting_b and (expected_meeting is None or meeting_a == expected_meeting),
        a.frame.to_common(a.model_local) == b.frame.to_common(b.model_local),
        source_invariant(a.clock, a.selected_unwrapped) == 0,
        source_invariant(b.clock, b.selected_unwrapped) == 0,
    )


def bell_with_environment(environment_qubits: int = 0) -> tuple[Q, ...]:
    """A, B then E registers; two fixed Bell amplitudes; no measurements."""
    if type(environment_qubits) is not int or environment_qubits < 0 or environment_qubits > 4:
        raise ValueError('environment_qubits must be 0..4')
    n = 2 + environment_qubits
    z = [Q()] * (2**n)
    z[0] = z[3 * (2**environment_qubits)] = Q(1)
    return tuple(z)


def _check_vector(state: Sequence[Q | int]) -> int:
    length = len(state)
    if length < 4 or length & (length - 1):
        raise ValueError('state dimension must be a power of two >=4')
    n = length.bit_length() - 1
    if any(not isinstance(x, (int, Q)) for x in state):
        raise TypeError('exact integer/Fraction amplitudes only')
    if not any(state):
        raise ValueError('nonzero state required')
    return n


def pauli_path(state: Sequence[Q | int], qubit: int, gate: str) -> tuple[Q, ...]:
    """I,X,Z,XZ Pauli actions, real rays; XZ equals Y up to global phase."""
    n = _check_vector(state)
    if type(qubit) is not int or not 0 <= qubit < n or gate not in ('I','X','Z','XZ'):
        raise ValueError('invalid target/gate')
    mask = 1 << (n - 1 - qubit)
    out = [Q()] * len(state)
    for index, amplitude in enumerate(state):
        new_index = index ^ mask if 'X' in gate else index
        sign = -1 if 'Z' in gate and new_index & mask else 1
        out[new_index] = Q(amplitude) * sign
    return tuple(out)


def controlled_not(state: Sequence[Q | int], control: int, target: int) -> tuple[Q, ...]:
    """Unitary coherent carrier interaction; it is NOT a measurement."""
    n = _check_vector(state)
    if (type(control) is not int or type(target) is not int or
            control == target or not 0 <= control < n or not 0 <= target < n):
        raise ValueError('distinct valid control and target needed')
    cmask, tmask = 1 << (n-1-control), 1 << (n-1-target)
    out = [Q()] * len(state)
    for index, amplitude in enumerate(state):
        out[index ^ tmask if index & cmask else index] = Q(amplitude)
    return tuple(out)


def rational_overlap_marker(t: Q | int) -> tuple[Q, ...]:
    """( |00> e0 + |11> e1 )/sqrt(2), e0=|0>,
       e1=c|0>+s|1>, c=(1-t²)/(1+t²), s=2t/(1+t²).
    It represents a partially distinguishable environmental path marker.
    """
    t = Q(t)
    c, s = (1-t*t)/(1+t*t), (2*t)/(1+t*t)
    vector = [Q()] * 8
    vector[0],vector[6],vector[7] = Q(1),c,s
    return tuple(vector)


def reduced_density(state: Sequence[Q | int], keep: Sequence[int] = (0,1)) -> tuple[tuple[Q,...],...]:
    """Exact normalized density after tracing *unobserved* environment.

    The global pure vector is never physically measured by this routine.
    """
    n = _check_vector(state)
    if (not keep or len(set(keep)) != len(keep) or any(type(k) is not int or
            k < 0 or k >= n for k in keep)):
        raise ValueError('distinct qubit positions required')
    traced = tuple(k for k in range(n) if k not in keep)
    def bits(i: int, positions: Sequence[int]) -> int:
        output = 0
        for pos in positions:
            output = (output << 1) + int(bool(i & (1 << (n-1-pos))))
        return output
    vectors: dict[int,list[Q]] = {}
    for index, value in enumerate(state):
        e, x = bits(index,traced),bits(index,keep)
        if e not in vectors:
            vectors[e] = [Q()] * (2 ** len(keep))
        vectors[e][x] += Q(value)
    norm = sum((Q(a)*Q(a) for a in state),Q())
    size = 2 ** len(keep)
    return tuple(tuple(sum((v[i]*v[j] for v in vectors.values()),Q())/norm
                       for j in range(size)) for i in range(size))


def purity(rho: Sequence[Sequence[Q]]) -> Q:
    n = len(rho)
    if not n or any(len(row)!=n for row in rho):
        raise ValueError('square density matrix required')
    return sum((rho[i][j]*rho[j][i] for i in range(n) for j in range(n)), Q())


def bell_probabilities(rho: Sequence[Sequence[Q]]) -> dict[str,Q]:
    """Probabilities of a Bell-basis measurement made at rendezvous.

    A single + result cannot certify premeasurement purity: a mixed state
    can yield the same outcome with nonzero probability.
    """
    if len(rho)!=4 or any(len(row)!=4 for row in rho):
        raise ValueError('Bell comparison requires a 4x4 AB density')
    return {
      'Phi+':(rho[0][0]+rho[3][3]+rho[0][3]+rho[3][0])/2,
      'Phi-':(rho[0][0]+rho[3][3]-rho[0][3]-rho[3][0])/2,
      'Psi+':(rho[1][1]+rho[2][2]+rho[1][2]+rho[2][1])/2,
      'Psi-':(rho[1][1]+rho[2][2]-rho[1][2]-rho[2][1])/2,
    }


def pauli_pair_syndrome(error_a: str, error_b: str) -> str:
    """Bell outcome for a local Pauli pair; all four diagonal pairs alias to Phi+."""
    state = pauli_path(pauli_path(bell_with_environment(),0,error_a),1,error_b)
    p = bell_probabilities(reduced_density(state))
    outcomes=[label for label,v in p.items() if v==1]
    if len(outcomes)!=1:
        raise AssertionError('Pauli actions must map Bell states to Bell states')
    return outcomes[0]


def independent_reference_syndrome(error_a: str, error_b: str) -> tuple[str,str]:
    """Two *additional* Bell witness pairs with references at rendezvous.

    Assumes the same local error acts on each observer's witness and on its
    twin register. This is an idealized trusted uniform-coupling assumption.
    Does NOT duplicate/qubit-clone the twin entanglement.
    """
    return pauli_pair_syndrome(error_a,'I'), pauli_pair_syndrome('I',error_b)


def exact_marker_coherence(t: Q | int) -> tuple[Q,Q,Q,Q]:
    """For a balanced pure path-marker state: (gamma,F_Bell,purity,D²).
    D² is the pure-marker environment distinguishability squared;
    gamma=Re<e0|e1> for this real marker family.
    """
    t=Q(t)
    gamma=(1-t*t)/(1+t*t)
    d2=1-gamma*gamma
    return gamma, (1+gamma)/2, (1+gamma*gamma)/2, d2
