"""Finite multi-observer SUCC: a source-indexed diagonal climbing tower.

Independent nondestructive probes are the only physical observations here.
Copies of source-tagged records move along typed network edges; base observer E
receives asynchronously and performs *one epistemic macro SUCC* only after
its evidence has a lawful causal down-closure. The model is not a physical
brain, authenticated measurement protocol, or zero-computation speedup.

Main mathematical theorem: for a fixed source class and stable probe semantics,
intersecting original-source fibers commutes with the union of independent
verified evidence. Finite goal recognition is equivalent to source-target
factorization through the joint evidence. A semantic-minimal support may be
strictly smaller than its required causal provenance down-closure.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable


class TowerError(ValueError):
    """An action lacks causal, physical, source or proof justification."""


@dataclass(frozen=True)
class Probe:
    name: str
    owner: str
    requires: tuple[str, ...]
    outputs: tuple[str, ...]


@dataclass(frozen=True)
class SourceModel:
    source_id: str
    basis_id: str
    sources: tuple[str, ...]
    probes: tuple[Probe, ...]
    target: tuple[str, ...]

    def __post_init__(self) -> None:
        if (not self.source_id or not self.basis_id or not self.sources
                or len(set(self.sources)) != len(self.sources)
                or len(set(p.name for p in self.probes)) != len(self.probes)
                or len(self.target) != len(self.sources)):
            raise TowerError("Invalid source/basis/target signature")
        names = {p.name for p in self.probes}
        if not names:
            raise TowerError("At least one physically declared probe is required")
        for p in self.probes:
            if (not p.name or not p.owner or len(p.outputs) != len(self.sources)
                    or len(set(p.requires)) != len(p.requires) or p.name in p.requires
                    or any(req not in names for req in p.requires)):
                raise TowerError("Malformed probe, response table or prerequisites")
        if any(not isinstance(z, str) for z in self.target):
            raise TowerError("Target labels must have stable string semantics")

    def probe(self, name: str) -> Probe:
        for p in self.probes:
            if p.name == name:
                return p
        raise TowerError("Unknown probe " + name)


@dataclass(frozen=True)
class Node:
    name: str
    level: int
    lane: str


@dataclass(frozen=True)
class Link:
    sender: str
    receiver: str
    kind: str  # ascent or descent


@dataclass(frozen=True)
class TowerNetwork:
    nodes: tuple[Node, ...]
    links: tuple[Link, ...]

    def __post_init__(self) -> None:
        byname = {n.name: n for n in self.nodes}
        if (len(byname) != len(self.nodes) or 'E' not in byname
                or byname['E'] != Node('E', -1, 'E')):
            raise TowerError("Distinct nodes and a level-minus-one base E required")
        for n in self.nodes:
            if n != byname['E'] and (n.level < 0 or n.lane not in ('A', 'B')):
                raise TowerError("Climbers require a nonnegative floor and A/B lane")
        if len(set(self.links)) != len(self.links):
            raise TowerError("Duplicate tower links")
        for e in self.links:
            if e.sender not in byname or e.receiver not in byname or e.sender == 'E':
                raise TowerError("Unknown endpoints or source E forbidden")
            a, b = byname[e.sender], byname[e.receiver]
            if e.kind == 'ascent':
                if b.level != a.level + 1 or b.name == 'E':
                    raise TowerError("An ascent must climb exactly one floor")
            elif e.kind == 'descent':
                if b.level != a.level - 1 or (b.name != 'E' and a.lane == b.lane):
                    raise TowerError("A descent must run exactly one floor diagonally")
            else:
                raise TowerError("Unknown link kind")

    def link(self, sender: str, receiver: str) -> Link:
        for e in self.links:
            if e.sender == sender and e.receiver == receiver:
                return e
        raise TowerError("Unlicensed tower transmission: " + sender + " -> " + receiver)


@dataclass(frozen=True)
class Receipt:
    event_id: str
    probe: str
    observed: str
    origin: str
    source_id: str
    basis_id: str
    parent_ids: tuple[str, ...]
    level: int


@dataclass(frozen=True)
class Transmission:
    sender: str
    receiver: str
    event_ids: tuple[str, ...]
    kind: str


@dataclass(frozen=True)
class ProofCertificate:
    target_value: str
    compatible_sources: tuple[str, ...]
    semantic_minimal: tuple[str, ...]
    causal_closure: tuple[str, ...]
    all_received: tuple[str, ...]
    macro_updates: int
    transport_count: int


class DiagonalTower:
    """Causally replayable nondestructive finite tower.

    source_index is visible only to perform_probe (the model's simulated
    experimenter). Base decisions are made from the declared full source
    table and received records; they never inspect source_index directly.
    The issuance journal is a DECLARED trusted attestation assumption.
    """
    def __init__(self, model: SourceModel, network: TowerNetwork):
        self.model = model
        self.network = network
        names = {n.name: n for n in network.nodes}
        for p in model.probes:
            if p.owner not in names or names[p.owner].level < 0:
                raise TowerError("Missing executable probe owner")
        if len(set(p.owner for p in model.probes)) != len(model.probes):
            raise TowerError("Each climber owns one probe in this minimal model")
        self.known: dict[str, set[str]] = {n.name: set() for n in network.nodes}
        self.issued: dict[str, Receipt] = {}
        self.transmissions: list[Transmission] = []
        self._source_index: int | None = None
        self.macro_updates = 0
        self.last_certificate: ProofCertificate | None = None

    def _current_receipts(self, names: Iterable[str]) -> tuple[Receipt, ...]:
        ids = tuple(sorted(names))
        try:
            return tuple(self.issued[r] for r in ids)
        except KeyError as exc:
            raise TowerError("Undeclared/unissued causal receipt") from exc

    def perform_probe(self, climber: str, source_index: int) -> Receipt:
        if type(source_index) is not int or not (0 <= source_index < len(self.model.sources)):
            raise TowerError("Invalid private simulator source")
        if self._source_index is not None and source_index != self._source_index:
            raise TowerError("Inconsistent true source across physical observations")
        owned = [p for p in self.model.probes if p.owner == climber]
        if len(owned) != 1:
            raise TowerError("Observer lacks exactly one declared physical probe")
        p = owned[0]
        event_id = 'evt:' + p.name
        if event_id in self.issued:
            raise TowerError("Physical observation may not be replayed as a fresh event")
        present = {r.probe: r for r in self._current_receipts(self.known[climber])}
        if not set(p.requires).issubset(present):
            raise TowerError("Missing lawful prerequisite for next mountain tier")
        required = tuple(present[name].event_id for name in p.requires)
        n = next(n for n in self.network.nodes if n.name == climber)
        record = Receipt(event_id, p.name, p.outputs[source_index], climber,
                         self.model.source_id, self.model.basis_id, required, n.level)
        self.issued[event_id] = record
        self.known[climber].add(event_id)
        self._source_index = source_index
        return record

    def transmit(self, sender: str, receiver: str,
                 selected: Iterable[str] | None = None) -> Transmission:
        edge = self.network.link(sender, receiver)
        source_ids = self.known[sender]
        if selected is None:
            ids = tuple(sorted(source_ids - self.known[receiver]))
        else:
            ids = tuple(sorted(selected))
        if not ids or len(set(ids)) != len(ids) or not set(ids).issubset(source_ids):
            raise TowerError("Empty, duplicate, or unowned transmitted evidence")
        for record in self._current_receipts(ids):
            if record.source_id != self.model.source_id or record.basis_id != self.model.basis_id:
                raise TowerError("Source/basis version drift in forwarded observation")
        self.known[receiver].update(ids)
        tx = Transmission(sender, receiver, ids, edge.kind)
        self.transmissions.append(tx)
        return tx

    def source_fiber(self, event_ids: Iterable[str]) -> tuple[int, ...]:
        receipts = self._current_receipts(event_ids)
        candidates = []
        for i in range(len(self.model.sources)):
            if all(self.model.probe(r.probe).outputs[i] == r.observed for r in receipts):
                candidates.append(i)
        return tuple(candidates)

    def semantic_target(self, event_ids: Iterable[str]) -> str | None:
        fiber = self.source_fiber(event_ids)
        if not fiber:
            return None
        values = {self.model.target[s] for s in fiber}
        return next(iter(values)) if len(values) == 1 else None

    def _causal_closure(self, ids: Iterable[str]) -> tuple[str, ...]:
        closure = set(ids)
        queue = list(closure)
        while queue:
            item = queue.pop()
            receipt = self.issued.get(item)
            if receipt is None:
                raise TowerError("Causal dependency references an unissued event")
            for parent in receipt.parent_ids:
                if parent not in closure:
                    closure.add(parent)
                    queue.append(parent)
        return tuple(sorted(closure))

    def _validate_received(self, ids: Iterable[str], *, require_closure: bool) -> tuple[str, ...]:
        selected = tuple(sorted(ids))
        if not selected:
            raise TowerError("No received proof evidence")
        for r in self._current_receipts(selected):
            p = self.model.probe(r.probe)
            n = next(n for n in self.network.nodes if n.name == r.origin)
            if any(x not in self.issued for x in r.parent_ids):
                raise TowerError("Unissued causal parent in purported proof receipt")
            if (p.owner != r.origin or n.level != r.level
                    or r.source_id != self.model.source_id or r.basis_id != self.model.basis_id
                    or r.event_id != 'evt:' + r.probe
                    or set(self.issued[x].probe for x in r.parent_ids) != set(p.requires)
                    or len(r.parent_ids) != len(p.requires)):
                raise TowerError("Wrong source, owner, basis, epoch, or causal parents")
        if require_closure and not set(self._causal_closure(selected)).issubset(selected):
            raise TowerError("Snapshot answers without causal proof-support down-closure")
        return selected

    def _minimum_semantic_support(self, ids: tuple[str, ...], target: str) -> tuple[str, ...]:
        for n in range(len(ids) + 1):
            for subset in combinations(ids, n):
                if self.semantic_target(subset) == target:
                    return subset
        raise TowerError("No semantically sufficient subset")

    def readiness_report(self) -> dict:
        """Finite diagnostic, NOT a claim of free or instantaneous computation.

        E receives proof *claims* and may semantically recognize the target
        before the complete causal support has actually arrived. This report
        does not inspect the private actual source index.
        """
        ids = tuple(sorted(self.known['E']))
        if not ids:
            return {'status':'NO_EVIDENCE','semantic_target':None,
                    'missing_causal_ids':(), 'countermodel_pair':None}
        self._validate_received(ids, require_closure=False)
        need = self._causal_closure(ids)
        missing = tuple(x for x in need if x not in self.known['E'])
        fiber = self.source_fiber(ids)
        if not fiber:
            return {'status':'INCONSISTENT_SOURCE','semantic_target':None,
                    'missing_causal_ids':missing, 'countermodel_pair':None}
        values = {self.model.target[i] for i in fiber}
        witness = None
        if len(values) > 1:
            pair = next((a,b) for a in fiber for b in fiber
                        if self.model.target[a]!=self.model.target[b])
            witness = tuple(self.model.sources[i] for i in pair)
        status = ('CAUSAL_RECEIPTS_MISSING' if missing else
                  'UNRESOLVED_CLAIM' if len(values)>1 else 'PROOF_READY')
        return {'status':status, 'semantic_target':next(iter(values)) if len(values)==1 else None,
                'missing_causal_ids':missing,'countermodel_pair':witness}

    def proof_costs(self) -> dict:
        """Record counts only, NOT an optimal Shannon/message bit cost."""
        return {'local_physical_measurements':len(self.issued),
                'network_transmissions':len(self.transmissions),
                'event_references_carried':sum(len(t.event_ids) for t in self.transmissions),
                'receiver_epistemic_macro_updates':self.macro_updates}

    def ready(self) -> bool:
        """Noncommitting readiness check: not a free physical/proof step."""
        try:
            self._validate_received(self.known['E'], require_closure=True)
        except TowerError:
            return False
        return self.semantic_target(self.known['E']) is not None

    def macro_succ(self) -> ProofCertificate:
        """One finite RECEIVER epistemic action, after all real upstream work."""
        if self.macro_updates:
            raise TowerError("This one-step tower demonstration already committed")
        ids = self._validate_received(self.known['E'], require_closure=True)
        fiber = self.source_fiber(ids)
        if not fiber:
            raise TowerError("Inconsistent source observations: empty possible-world class")
        values = {self.model.target[i] for i in fiber}
        if len(values) != 1:
            raise TowerError("Claim remains source-indistinguishable at E")
        value = next(iter(values))
        semantic = self._minimum_semantic_support(ids, value)
        causal = self._causal_closure(semantic)
        if not set(causal).issubset(ids):
            raise TowerError("Minimal semantic proof lacks lawful historical dependencies")
        self.macro_updates += 1
        certificate = ProofCertificate(value, tuple(self.model.sources[i] for i in fiber),
                                       semantic, causal, ids, self.macro_updates,
                                       len(self.transmissions))
        self.last_certificate = certificate
        return certificate


def ice_climber_tower(levels: int = 3) -> tuple[SourceModel, TowerNetwork]:
    """Alternating A/B columns with both-to-both upward support and downward diagonals.

    Upper floors require certified observations from both lower climbers.
    The goal is the XOR of the top two independent source bits; its two
    semantic witnesses depend on a larger lawful causal climb history.
    """
    if type(levels) is not int or levels < 2 or levels > 5:
        raise TowerError("Tower levels must be between 2 and 5")
    nbits = 2 * levels
    states = tuple(''.join(map(str, bits)) for bits in product((0, 1), repeat=nbits))
    probes = []
    nodes = [Node('E', -1, 'E')]
    for level in range(levels):
        for lane_index, lane in enumerate(('A', 'B')):
            owner = f'{lane}{level}'
            nodes.append(Node(owner, level, lane))
            pindex = 2 * level + lane_index
            required = (() if level == 0
                        else (f'p{2 * (level - 1)}', f'p{2 * (level - 1) + 1}'))
            probes.append(Probe(f'p{pindex}', owner, required,
                                tuple(x[pindex] for x in states)))
    model = SourceModel('climber-immutable-source', 'binary-shared-basis-v1',
                        states, tuple(probes),
                        tuple(str(int(x[-2]) ^ int(x[-1])) for x in states))
    links = []
    for level in range(levels - 1):
        for lane in ('A', 'B'):
            for up in ('A', 'B'):
                links.append(Link(f'{lane}{level}', f'{up}{level+1}', 'ascent'))
    for level in range(levels - 1, 0, -1):
        links.append(Link(f'A{level}', f'B{level-1}', 'descent'))
        links.append(Link(f'B{level}', f'A{level-1}', 'descent'))
    links.extend((Link('A0', 'E', 'descent'), Link('B0', 'E', 'descent')))
    return model, TowerNetwork(tuple(nodes), tuple(links))


def completed_climb(levels: int = 3, source_index: int = 45,
                    *, descend: bool = True) -> DiagonalTower:
    model, network = ice_climber_tower(levels)
    if source_index >= len(model.sources):
        raise TowerError("Chosen source index exceeds source table")
    tower = DiagonalTower(model, network)
    for level in range(levels):
        if level:
            for receiver in (f'A{level}', f'B{level}'):
                for source in (f'A{level-1}', f'B{level-1}'):
                    tower.transmit(source, receiver)
        for lane in ('A', 'B'):
            tower.perform_probe(f'{lane}{level}', source_index)
    if descend:
        for level in range(levels - 1, 0, -1):
            for sender, receiver in ((f'A{level}', f'B{level-1}'),
                                     (f'B{level}', f'A{level-1}')):
                tower.transmit(sender, receiver)
        tower.transmit('A0', 'E')
        tower.transmit('B0', 'E')
    return tower


def destructive_diamond_counterexample() -> dict:
    """A genuine noncommuting source-state example where tower union is illegal.

    A reads a then resets b=0, B reads b then resets a=0.
    Results differ with action order on one unprepared original carrier.
    """
    def A(state):
        a,b=state
        return a,(a,0)
    def B(state):
        a,b=state
        return b,(0,b)
    initial=(1,1)
    ao,s=A(initial)
    bo,end_ab=B(s)
    bo2,s2=B(initial)
    ao2,end_ba=A(s2)
    observed_ab={'A':ao,'B':bo}
    observed_ba={'A':ao2,'B':bo2}
    if end_ab!=end_ba or observed_ab==observed_ba:
        raise AssertionError("Control failed to exhibit causal noncommutativity")
    return {'source':initial,'AB_observations':observed_ab,
            'BA_observations':observed_ba,'common_endpoint':end_ab,
            'commuting_evidence_square':False}
