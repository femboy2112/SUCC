"""Exact finite boundary identifiability and quantum nondisturbing-alphabet tests.

Only classical finite linear models and *declared* finite quantum alphabets are
modelled. Graph/Gram lemmas are elementary no-information-without-disturbance
facts, not an instrument-independent hardness metric or a physical construction
from SUCC's prime/BBP source. Rational arithmetic only, no numerical sampling.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


class InstrumentContractError(ValueError):
    """Input violates the stated source/instrument family."""


def rational(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise InstrumentContractError("only exact integer and Fraction coordinates")
    return Q(x)


def vector(values: Sequence[int | Q], *, normalized: bool = False) -> tuple[Q, ...]:
    if not isinstance(values, (tuple, list)) or not values:
        raise InstrumentContractError("nonempty vector required")
    v = tuple(rational(x) for x in values)
    norm2 = sum((x*x for x in v), Q())
    if norm2 == 0 or (normalized and norm2 != 1):
        raise InstrumentContractError("nonzero vector; normalized rays need squared norm 1")
    return v


def inner(u: Sequence[int | Q], v: Sequence[int | Q]) -> Q:
    a, b = vector(u), vector(v)
    if len(a) != len(b):
        raise InstrumentContractError("inner product requires same coordinate dimension")
    return sum((x*y for x, y in zip(a, b)), Q())


def overlap_components(states: Sequence[Sequence[int | Q]]) -> tuple[tuple[int, ...], ...]:
    """Connected components of graph <psi_i,psi_j> != 0.

    State vectors need not be normalized here; the graph is invariant under
    any nonzero independent rational rescaling of the vector representatives.
    """
    if not states:
        raise InstrumentContractError("nonempty source alphabet")
    states = tuple(vector(s) for s in states)
    n = len(states)
    if any(len(s) != len(states[0]) for s in states):
        raise InstrumentContractError("all source rays must have common dimension")
    unseen = set(range(n))
    groups = []
    while unseen:
        root = min(unseen)
        group = {root}
        frontier = [root]
        unseen.remove(root)
        while frontier:
            i = frontier.pop()
            for j in sorted(unseen):
                if inner(states[i], states[j]) != 0:
                    unseen.remove(j)
                    group.add(j)
                    frontier.append(j)
        groups.append(tuple(sorted(group)))
    return tuple(groups)


def nondemolition_label_possible(states: Sequence[Sequence[int | Q]],
                                 labels: Sequence[str | int]) -> bool:
    """iff a perfect record of labels can preserve *all* alphabet pure states.

    This assumes isometric coupling of a blank pure probe that leaves each
    listed system ray unchanged, not arbitrary postselection or state prep.
    """
    groups = overlap_components(states)
    if len(labels) != sum(len(g) for g in groups):
        raise InstrumentContractError("one declared label per source state")
    return all(len({labels[i] for i in g}) == 1 for g in groups)


def gram_isometry_defects(states: Sequence[Sequence[int | Q]],
                          markers: Sequence[Sequence[int | Q]]) -> tuple[tuple[Q, ...], ...]:
    """Gram difference G_input - G_(preserved_system * marker).

    For normalized pure system and environment states, a *zero* Gram
    difference is necessary and sufficient for a linear isometry on their
    span realizing |psi_i>|blank> -> |psi_i>|marker_i>. The latter can be
    extended to a unitary on the finite combined Hilbert space.
    """
    if not states or len(states) != len(markers):
        raise InstrumentContractError("matched nonempty alphabet and marker records")
    a = tuple(vector(s, normalized=True) for s in states)
    b = tuple(vector(s, normalized=True) for s in markers)
    if any(len(s) != len(a[0]) for s in a) or any(len(s) != len(b[0]) for s in b):
        raise InstrumentContractError("uniform system/marker dimensions")
    return tuple(tuple(inner(a[i], a[j])*(1-inner(b[i], b[j]))
                       for j in range(len(a))) for i in range(len(a)))


def gram_marker_isometry_possible(states: Sequence[Sequence[int | Q]],
                                   markers: Sequence[Sequence[int | Q]]) -> bool:
    return all(not x for row in gram_isometry_defects(states, markers) for x in row)


def quantitative_leakage_requirement(signal_a: Sequence[int | Q],
                                     signal_b: Sequence[int | Q],
                                     marker_a: Sequence[int | Q],
                                     marker_b: Sequence[int | Q]) -> Q:
    """Necessary lower budget L = |s * (1 - t)|, with s,t exact overlaps.

    If actual joint outputs are within norm delta of the respective *product*
    target states psi_i ⊗ marker_i, isometry forces L <= 2delta+delta^2.
    Does not claim that any delta meeting this inequality suffices.
    """
    a, b = vector(signal_a, normalized=True), vector(signal_b, normalized=True)
    e, f = vector(marker_a, normalized=True), vector(marker_b, normalized=True)
    if len(a) != len(b) or len(e) != len(f):
        raise InstrumentContractError("same dimensions within system/marker pairs")
    return abs(inner(a, b)*(1-inner(e, f)))


def budget_passes_necessary_bound(loss: int | Q, delta: int | Q) -> bool:
    loss, delta = rational(loss), rational(delta)
    if not 0 <= loss <= 2 or not 0 <= delta:
        raise InstrumentContractError("overlap loss nonnegative <=2 and delta nonnegative")
    return 2*delta + delta*delta >= loss


@dataclass(frozen=True)
class ReadoutRotation:
    """One *classical linear*, norm-preserving, active transduction probe.

    Coefficients c²+s²=1, s != 0. Read x0 before intervention and rotated x0
    after intervention; the hidden second coordinate can then be recovered.
    Reading amplitudes this way is *not* a quantum state-measurement protocol.
    """
    cosine: Q = Q(3, 5)
    sine: Q = Q(4, 5)

    def __post_init__(self) -> None:
        c, s = rational(self.cosine), rational(self.sine)
        if c*c+s*s != 1 or s == 0:
            raise InstrumentContractError("exact orthogonal rotation with nonzero mixing")
        object.__setattr__(self, "cosine", c)
        object.__setattr__(self, "sine", s)

    def apply(self, visible: int | Q, hidden: int | Q) -> tuple[Q, Q]:
        a, b = rational(visible), rational(hidden)
        return (self.cosine*a+self.sine*b, -self.sine*a+self.cosine*b)

    def inverse(self, after_visible: int | Q, after_hidden: int | Q) -> tuple[Q, Q]:
        a, b = rational(after_visible), rational(after_hidden)
        return (self.cosine*a-self.sine*b, self.sine*a+self.cosine*b)

    def reconstruct_hidden(self, pre_visible: int | Q, post_visible: int | Q) -> Q:
        return (rational(post_visible)-self.cosine*rational(pre_visible))/self.sine


def cnot_meter_on_real_qubit(state: Sequence[int | Q]) -> dict[str, object]:
    """Exact marker register for CNOT system->ancilla starting in |0>.

    Input normalized alpha|0>+beta|1>; output joint alpha|00>+beta|11>.
    System and probe each have diagonal marginals; the *joint* stays pure.
    """
    v = vector(state, normalized=True)
    if len(v) != 2:
        raise InstrumentContractError("real qubit with two amplitudes")
    a, b = v
    diag = (a*a, b*b)
    survival = a**4 + b**4
    return {"system_diagonal": diag,
            "probe_diagonal": diag,
            "system_survival_fidelity": survival,
            "system_fidelity_loss": 1-survival,
            "probe_click_one_probability": b*b,
            "joint_purity": Q(1),
            "system_purity": a**4 + b**4}


def bbp_seed_phase_alias(seed_a: int | Q, seed_b: int | Q, clock: int) -> bool:
    """Necessary and sufficient later-phase alias for same BBP forcing.

    U_n(s)-U_n(t)=16^n(s-t) by induction. This verifies only *phase* alias,
    not equality of unwrapped histories or source-authenticated zero seed.
    """
    if type(clock) is not int or clock < 0:
        raise InstrumentContractError("nonnegative integer clock")
    d = Q(16)**clock*(rational(seed_a)-rational(seed_b))
    return d.denominator == 1
