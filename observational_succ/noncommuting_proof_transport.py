"""Finite deterministic noncommuting proof transport with source-indexed histories.

Mathematical scope: a declared finite state space, deterministic interventions,
observable outcomes, public action menus and immutable epoch-tagged reports.
A report never exposes the hidden pre-state or post-state to the decoder.
The returned endpoint is a *simulator audit value*, not observer evidence.

Results are classical finite fiber factorization, kernel refinement,
compositional state/output (Mealy) semantics, and finite bisimulation.
This is not a physical instrument, quantum theory, or RH result.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


class SourceTransportError(ValueError):
    """Invalid source, action, carrier history or proof context."""


def _index(s: int, count: int) -> int:
    if type(s) is not int or not 0 <= s < count:
        raise SourceTransportError("State address outside declared carrier")
    return s


@dataclass(frozen=True)
class Instrument:
    """Total outcome and transition arrays, with explicit enabled-domain mask."""
    name: str
    outputs: tuple[int, ...]
    transitions: tuple[int, ...]
    enabled: tuple[bool, ...]

    def validate(self, size: int) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise SourceTransportError("Every action needs a unique name")
        if (not all(type(t) is tuple and len(t) == size
                    for t in (self.outputs, self.transitions, self.enabled))
                or not all(type(v) is int for v in self.outputs)
                or not all(type(v) is bool for v in self.enabled)
                or not all(type(v) is int and 0 <= v < size
                           for v in self.transitions)):
            raise SourceTransportError("Instrument arrays must be typed and total")

    def step(self, state: int) -> tuple[int, int]:
        _index(state, len(self.outputs))
        if not self.enabled[state]:
            raise SourceTransportError("Action unavailable at this carrier state")
        return self.outputs[state], self.transitions[state]


@dataclass(frozen=True)
class EventRecord:
    name: str
    outcome: int
    epoch: int
    source_id: str
    basis_id: str


@dataclass(frozen=True)
class AuditTrace:
    """Public event history plus a separate PRIVILEGED endpoint audit."""
    records: tuple[EventRecord, ...]
    terminal_state: int
    source_id: str
    basis_id: str
    initial_source: int

    @property
    def public_signature(self) -> tuple[tuple[str, int, int], ...]:
        """Never includes hidden initial source nor post-state."""
        return tuple((r.name, r.outcome, r.epoch) for r in self.records)

    @property
    def observed_values(self) -> tuple[int, ...]:
        return tuple(r.outcome for r in self.records)


@dataclass(frozen=True)
class FiniteCarrier:
    count: int
    actions: tuple[Instrument, ...]
    source_id: str
    basis_id: str

    def __post_init__(self) -> None:
        if type(self.count) is not int or not 1 <= self.count <= 128:
            raise SourceTransportError("Finite carrier size must be in 1..128")
        if type(self.actions) is not tuple or not self.actions:
            raise SourceTransportError("Require nonempty available instrument class")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise SourceTransportError("Source identifier required")
        if not isinstance(self.basis_id, str) or not self.basis_id:
            raise SourceTransportError("Frame/basis identifier required")
        names = []
        for action in self.actions:
            if not isinstance(action, Instrument):
                raise SourceTransportError("Malformed instrument")
            action.validate(self.count)
            names.append(action.name)
        if len(names) != len(set(names)):
            raise SourceTransportError("Action names must be unique")

    def action(self, name: str) -> Instrument:
        for instrument in self.actions:
            if instrument.name == name:
                return instrument
        raise SourceTransportError("Probe not in declared physical menu")

    def run(self, source: int, path: tuple[str, ...]) -> AuditTrace:
        state = _index(source, self.count)
        if type(path) is not tuple or len(path) > 32:
            raise SourceTransportError("Bounded typed action sequence required")
        records = []
        for i, name in enumerate(path):
            obs, state = self.action(name).step(state)
            records.append(EventRecord(name, obs, i+1,
                                       self.source_id, self.basis_id))
        return AuditTrace(tuple(records), state,
                          self.source_id, self.basis_id, source)


def _sources(field: FiniteCarrier, source_class: tuple[int, ...]) -> None:
    if (type(source_class) is not tuple or not source_class
            or len(source_class) > field.count
            or tuple(sorted(set(source_class))) != source_class):
        raise SourceTransportError("Source class must be nonempty sorted unique tuple")
    for x in source_class:
        _index(x, field.count)


@dataclass(frozen=True)
class ProofFactor:
    """Constructive deterministic decoder or exact same-trace rival."""
    source_id: str
    basis_id: str
    target_id: str
    path: tuple[str, ...]
    source_class: tuple[int, ...]
    decoder: tuple[tuple[tuple[int, ...], str], ...]
    collision: tuple[int, int] | None

    @property
    def valid(self) -> bool:
        return self.collision is None

    def decode(self, outcomes: tuple[int, ...], *, source_id: str,
               basis_id: str, target_id: str, path: tuple[str, ...]) -> str:
        if ((source_id,basis_id,target_id,path) !=
            (self.source_id,self.basis_id,self.target_id,self.path)):
            raise SourceTransportError("Stale, differently sourced proof packet")
        if not self.valid:
            raise SourceTransportError("Proof target does not factor via transcript")
        values = dict(self.decoder)
        if outcomes not in values:
            raise SourceTransportError("Outcome not certified in source class")
        return values[outcomes]


def factor_original_claim(field: FiniteCarrier, source_class: tuple[int,...],
                          target: tuple[str, ...], path: tuple[str,...],
                          *, target_id: str) -> ProofFactor:
    """Proof iff target is constant on the complete observable trace fibers."""
    _sources(field, source_class)
    if (type(target) is not tuple or len(target) != field.count
            or not all(type(t) is str for t in target)
            or not isinstance(target_id,str) or not target_id):
        raise SourceTransportError("Declare one target label per carrier state")
    observed = {}
    representative = {}
    collision = None
    for x in source_class:
        outputs = field.run(x, path).observed_values
        if outputs in observed and observed[outputs] != target[x]:
            collision = (representative[outputs], x)
            break
        observed[outputs] = target[x]
        representative.setdefault(outputs, x)
    return ProofFactor(field.source_id, field.basis_id, target_id, path,
                       source_class, tuple(sorted(observed.items())), collision)


def partition_refinement_witness(field: FiniteCarrier,
                                 source_class: tuple[int, ...],
                                 fine_path: tuple[str, ...],
                                 coarse_path: tuple[str, ...]
                                 ) -> tuple[int, int] | None:
    """Return (x,y) with equal fine observations but unequal coarse ones.

    Absent witness: ker(F_fine) subset ker(F_coarse); EVERY target
    decodable from coarse observations is then fine-decodable, with
    canonical quotient decoder. A single scalar 'knowledge amount'
    cannot describe incomparable partitions.
    """
    _sources(field, source_class)
    coarse_by_fine = {}
    first = {}
    for x in source_class:
        fine = field.run(x, fine_path).observed_values
        coarse = field.run(x, coarse_path).observed_values
        if fine in coarse_by_fine and coarse_by_fine[fine] != coarse:
            return (first[fine],x)
        coarse_by_fine[fine] = coarse
        first.setdefault(fine,x)
    return None


@dataclass(frozen=True)
class SemanticSquareVerdict:
    """Check whether a post-source claim actually means the old claim."""
    source_id: str
    basis_id: str
    path: tuple[str, ...]
    mismatch: tuple[int, int, str, str] | None

    @property
    def source_semantics_preserved(self) -> bool:
        return self.mismatch is None


def check_source_semantics(field: FiniteCarrier,
                           source_class: tuple[int, ...],
                           before_target: tuple[str, ...],
                           after_target: tuple[str, ...],
                           path: tuple[str, ...]
                           ) -> SemanticSquareVerdict:
    """t_old(x) == t_new(H_path(x)) for EVERY declared initial source.

    This is an independent gate from the original target being decodable
    from the path's public outcomes. Neither gate authenticates a
    physically realized source, a claim table or a hardware intervention.
    """
    _sources(field,source_class)
    for t in (before_target,after_target):
        if type(t) is not tuple or len(t)!=field.count or not all(
                type(v) is str for v in t):
            raise SourceTransportError("Require full typed source truth tables")
    for source in source_class:
        end=field.run(source,path).terminal_state
        if before_target[source] != after_target[end]:
            return SemanticSquareVerdict(field.source_id,field.basis_id,path,
                (source,end,before_target[source],after_target[end]))
    return SemanticSquareVerdict(field.source_id,field.basis_id,path,None)


@dataclass(frozen=True)
class IrretrievablePair:
    first: int
    second: int
    transcript: tuple[int, ...]
    terminal_state: int
    path: tuple[str, ...]
    first_target: str
    second_target: str


def lost_future_original_claim(field: FiniteCarrier, first: int, second: int,
                               target: tuple[str, ...], path: tuple[str,...]
                               ) -> IrretrievablePair | None:
    """Source shadow: same public past, same physical next state, unlike target.

    Any future deterministic adaptive protocol using ONLY state-dependent
    menus/outcomes must produce identical future reports on these worlds.
    No claim of logical/physical impossibility beyond this protocol class.
    """
    if type(target) is not tuple or len(target) != field.count:
        raise SourceTransportError("Target signature mismatched")
    one, two = field.run(first,path),field.run(second,path)
    if (one.public_signature == two.public_signature
            and one.terminal_state == two.terminal_state
            and target[first] != target[second]):
        return IrretrievablePair(
            first, second, one.observed_values, one.terminal_state,
            path, target[first],target[second])
    return None


def finite_future_equivalence(field: FiniteCarrier) -> tuple[tuple[int,int],...]:
    """Greatest Moore/Mealy observational bisimulation, no hidden truth labels.

    Menus are declared OBSERVABLE. For every action, equal enabled status,
    equal public outcome when enabled and equivalent successor states.
    Because states are finite and deterministic, pruning stabilizes in
    finitely many iterations.
    """
    pairs = {(i,j) for i in range(field.count) for j in range(i,field.count)}
    def canon(i:int,j:int): return (i,j) if i<=j else (j,i)
    while True:
        survivors = set()
        for i,j in pairs:
            good=True
            for a in field.actions:
                if a.enabled[i] != a.enabled[j]:
                    good=False; break
                if a.enabled[i] and (
                    a.outputs[i] != a.outputs[j]
                    or canon(a.transitions[i],a.transitions[j]) not in pairs):
                    good=False; break
            if good:
                survivors.add((i,j))
        if survivors == pairs:
            break
        pairs = survivors
    return tuple(sorted(pairs))


def finite_separator(field: FiniteCarrier, first: int, second: int
                     ) -> tuple[str, ...] | None:
    """Shortest action-word distinguishing publicly observable behavior.

    Disabled-action status is visible through the current action menu.
    A None result is exact observational future equivalence, not
    equivalent underlying source identities or equal hidden target values.
    """
    a,b = _index(first,field.count),_index(second,field.count)
    todo=deque([(a,b,())])
    visited={(a,b)}
    while todo:
        x,y,path=todo.popleft()
        for action in field.actions:
            candidate=path+(action.name,)
            if action.enabled[x] != action.enabled[y]:
                return candidate
            if not action.enabled[x]:
                continue
            if action.outputs[x] != action.outputs[y]:
                return candidate
            pair=(action.transitions[x],action.transitions[y])
            if pair not in visited:
                visited.add(pair)
                todo.append((*pair,candidate))
    return None


def _bit_field(nondestructive: bool = False, with_joint: bool = False
               ) -> FiniteCarrier:
    """Actual source bits (a,b) at address s=2*a+b."""
    sa=tuple(s//2 for s in range(4))
    sb=tuple(s%2 for s in range(4))
    if nondestructive:
        ax=bx=tuple(range(4))
    else:
        ax=tuple(2*(s//2) for s in range(4))
        bx=tuple(s%2 for s in range(4))
    yes=(True,)*4
    actions=[
        Instrument("A",sa,ax,yes),
        Instrument("B",sb,bx,yes),
    ]
    if with_joint:
        actions.append(Instrument("JOINT",tuple(range(4)),
                                  tuple(range(4)),yes))
    return FiniteCarrier(4,tuple(actions),
                         "initial-physical-two-bit-source","binary-pair-v1")


def noncommuting_proof_demo() -> dict:
    field=_bit_field()
    src=(0,1,2,3)
    parity=("0","1","1","0")
    ab={s:field.run(s,("A","B")) for s in src}
    ba={s:field.run(s,("B","A")) for s in src}
    if ({trace.terminal_state for trace in ab.values()} != {0}
            or {trace.terminal_state for trace in ba.values()} != {0}):
        raise ArithmeticError("Expected path-endpoint collapse failed")
    if ab[2].observed_values == ba[2].observed_values:
        raise ArithmeticError("Observational order unexpectedly commutes")
    for path in (("A","B"),("B","A")):
        if factor_original_claim(field,src,parity,path,
                                 target_id="original-XOR").valid:
            raise ArithmeticError("Destructive parity incorrectly certified")

    parity_semantics=check_source_semantics(
        field,src,parity,parity,("A","B"))
    first_bit=("0","0","1","1")
    first_preserves_a=check_source_semantics(
        field,src,first_bit,first_bit,("A",))
    first_erase_b=check_source_semantics(
        field,src,first_bit,first_bit,("B",))
    if (parity_semantics.source_semantics_preserved
            or not first_preserves_a.source_semantics_preserved
            or first_erase_b.source_semantics_preserved):
        raise ArithmeticError("Source-meaning square incorrectly assumed")

    a_shadow=lost_future_original_claim(field,0,1,parity,("A",))
    b_shadow=lost_future_original_claim(field,0,2,parity,("B",))
    if (a_shadow is None or b_shadow is None
            or finite_separator(field,a_shadow.terminal_state,
                                b_shadow.terminal_state) is not None):
        raise ArithmeticError("Source-shadow decisive pair missing")
    a_refines_b=partition_refinement_witness(field,src,("A","B"),("B","A"))
    b_refines_a=partition_refinement_witness(field,src,("B","A"),("A","B"))
    if a_refines_b is None or b_refines_a is None:
        raise ArithmeticError("Distinct paths must have incomparable evidence")
    repair=_bit_field(nondestructive=True)
    joint=_bit_field(with_joint=True)
    no_damage=factor_original_claim(repair,src,parity,("A","B"),
                                    target_id="original-XOR")
    joint_result=factor_original_claim(joint,src,parity,("JOINT",),
                                       target_id="original-XOR")
    if not no_damage.valid or not joint_result.valid:
        raise ArithmeticError("Nondestructive joint support controls failed")
    future=finite_future_equivalence(field)
    if future!=tuple((i,i) for i in range(4)):
        raise ArithmeticError("All pairs are separable, but no uniform parity policy exists")
    for i in range(4):
        for j in range(i,4):
            if ((i,j) in future) != (finite_separator(field,i,j) is None):
                raise ArithmeticError("Bisimulation and BFS separator disagree")
    return {
        "status":"NONCOMMUTING_SOURCE_PROOF_TRANSPORT_EXACT",
        "all_four_two_action_endpoints":"00",
        "distinct_ordered_public_histories":True,
        "AB_parity_original_decodable":False,
        "BA_parity_original_decodable":False,
        "AB_vs_BA_partition_refinement":False,
        "post_source_parity_is_original_parity":parity_semantics.source_semantics_preserved,
        "A_preserves_original_a_semantics":first_preserves_a.source_semantics_preserved,
        "B_preserves_original_a_semantics":first_erase_b.source_semantics_preserved,
        "BA_vs_AB_partition_refinement":False,
        "shadow_after_A":{"pair":[0,1],
                          "record":list(a_shadow.transcript),
                          "terminal_state":a_shadow.terminal_state},
        "shadow_after_B":{"pair":[0,2],
                          "record":list(b_shadow.transcript),
                          "terminal_state":b_shadow.terminal_state},
        "same_shadow_no_future_adaptive_proof":True,
        "nondestructive_AB_repairs_original_parity":no_damage.valid,
        "source_joint_read_repairs_original_parity":joint_result.valid,
        "all_distinct_initial_sources_pairwise_separable":True,
        "no_uniform_adaptive_original_parity_protocol":True,
        "bisimulation_agrees_with_independent_BFS_for_all_pairs":True,
        "pre_source_truth_labels_not_leaked_into_reports":True,
        "externally_authenticated_source_laws_claimed":False,
        "quantum_physical_or_RH_theorem_claimed":False,
    }
