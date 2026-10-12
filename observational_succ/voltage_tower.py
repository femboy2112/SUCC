"""Concrete arithmetic proof descent through a diagonal multi-observer SUCC tower.

Each A/B climber independently validates a disjoint shard of ALL outgoing
edge equations for a proposed integer voltage potential of a finite Gaussian
sieve. The same declared source graph/potential is used throughout. E accepts
ONE epistemic macro action iff all shards have lawful causal histories and
cover every source vertex, and E recomputes their complete exact edge checks.

This is an exact finite distributed proof-labeling construction. It is not
an independent all-K Gaussian moat theorem, network speedup, cryptographic
attestation or a physical high-level proof oracle.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
import json

from .diagonal_tower import ice_climber_tower, TowerError
from .gaussian_holonomy import (
    GaussianSieve, HolonomyError, Vec2, plus, minus, _steps,
    construct_confinement_potential, quotient_holonomy,
)


class VoltageTowerError(ValueError):
    """Nonverifiable mathematical shard, coverage gap, or bad relay."""


@dataclass(frozen=True)
class VoltageShard:
    identity: str
    origin: str
    source_signature: str
    basis: str
    assigned: tuple[Vec2,...]
    checked_edges: int
    parents: tuple[str,...]


@dataclass(frozen=True)
class VoltageProof:
    source_signature: str
    period: int
    checked_vertices: int
    checked_directed_edges: int
    verified_shards: int
    max_lifted_component: int
    epistemic_macro_updates: int
    mathematical_full_source_check: bool


class VoltageTower:
    """One candidate confinement proof split into six exact local checks.

    Checkers trust only source arithmetic and verify edge equations, not a
    sender's claimed 'OK' bit. Every packet is an immutable shard reference
    in a declared in-process issuance journal (no cryptographic source sig).
    """
    def __init__(self, sieve: GaussianSieve, squared_step: int = 1, levels: int = 3):
        self.sieve=sieve
        self.squared_step=squared_step
        self.levels=levels
        self.network=ice_climber_tower(levels)[1]
        self.steps=_steps(squared_step)
        self.vertices=sieve.allowed_residues(max_cells=100_000)
        self.vertex_set=set(self.vertices)
        self.potentials=dict(construct_confinement_potential(sieve,squared_step,max_cells=100_000))
        self.signature=self._signature()
        self.basis='gaussian-integer-voltage-potential-v1'
        self.climbers=tuple(f'{lane}{level}' for level in range(levels) for lane in ('A','B'))
        self.assigned={name:tuple(self.vertices[i] for i in range(len(self.vertices))
                                 if i % len(self.climbers)==j)
                       for j,name in enumerate(self.climbers)}
        if any(not points for points in self.assigned.values()):
            raise VoltageTowerError('Too few quotient vertices for this many observers')
        self.known={n.name:set() for n in self.network.nodes}
        self.shards:dict[str,VoltageShard]={}
        self.transport_log:list[tuple[str,str,tuple[str,...]]]=[]
        # Immutable event entries in append-only observational order. The
        # in-process registry is a declared mathematical trust boundary.
        self.event_log:list[tuple[str,str,str,tuple[str,...]]]=[]
        self.macro_updates=0

    def _signature(self) -> str:
        payload=(tuple(self.sieve.factors),self.squared_step)
        return sha256(json.dumps(payload,separators=(',',':')).encode()).hexdigest()

    def _id(self, name: str) -> str:
        return 'voltage-shard:'+name

    def _expected_parents(self, name: str) -> tuple[str,...]:
        level=int(name[1:])
        if level==0:return ()
        return (self._id(f'A{level-1}'),self._id(f'B{level-1}'))

    def _edge_check(self, vertices: tuple[Vec2,...]) -> int:
        count=0
        q=self.sieve.period
        for src in vertices:
            if src not in self.vertex_set or src not in self.potentials:
                raise VoltageTowerError('Local verification references a nonexistent source vertex')
            if (self.potentials[src][0]%q,self.potentials[src][1]%q)!=src:
                raise VoltageTowerError('Potential does not lift the declared residue')
            for step in self.steps:
                dst=((src[0]+step[0])%q,(src[1]+step[1])%q)
                if dst in self.vertex_set:
                    count+=1
                    if dst not in self.potentials or minus(self.potentials[dst],self.potentials[src])!=step:
                        raise VoltageTowerError('Noncommuting source edge: incorrect potential')
        return count

    def check_at(self, climber: str) -> VoltageShard:
        if climber not in self.assigned:
            raise VoltageTowerError('Unknown local certificate checker')
        identity=self._id(climber)
        if identity in self.shards:
            raise VoltageTowerError('Shard already checked; no repeated physical-origin claim')
        parents=self._expected_parents(climber)
        if not set(parents).issubset(self.known[climber]):
            raise VoltageTowerError('Ladder prerequisites not received before local verification')
        if self._signature()!=self.signature:
            raise VoltageTowerError('Declared authentic arithmetic source changed')
        edge_count=self._edge_check(self.assigned[climber])
        shard=VoltageShard(identity,climber,self.signature,self.basis,
                           self.assigned[climber],edge_count,parents)
        self.shards[identity]=shard
        self.known[climber].add(identity)
        self.event_log.append(('issue',climber,climber,(identity,)))
        return shard

    def relay(self, sender: str, receiver: str,
              selected: tuple[str,...] | None = None) -> tuple[str,...]:
        self.network.link(sender,receiver)
        if selected is None:
            names=tuple(sorted(self.known[sender]-self.known[receiver]))
        else:
            names=tuple(sorted(selected))
        if not names or len(set(names))!=len(names) or not set(names).issubset(self.known[sender]):
            raise VoltageTowerError('Bad, empty, forged or unowned proof relay')
        if any(sh not in self.shards for sh in names):
            raise VoltageTowerError('Cannot relay a shard never mathematically verified')
        self.known[receiver].update(names)
        self.transport_log.append((sender,receiver,names))
        self.event_log.append(('relay',sender,receiver,names))
        return names

    def _replay_causal_network(self) -> None:
        """Verify E's mathematical shard aggregation did not skip relays.

        Replay real issuance/transport order. Validates event DAG and licenses
        each actual network edge; source labels alone cannot prove delivery.
        """
        replay={n.name:set() for n in self.network.nodes}
        for kind,a,b,items in self.event_log:
            if len(set(items))!=len(items) or not items:
                raise VoltageTowerError('Invalid causal event payload')
            if kind=='issue':
                if a!=b or len(items)!=1 or items[0]!=self._id(a):
                    raise VoltageTowerError('False local mathematical observation origin')
                if items[0] in replay[a] or not set(self._expected_parents(a)).issubset(replay[a]):
                    raise VoltageTowerError('Mathematical check illegally preceded prerequisites')
                replay[a].add(items[0])
            elif kind=='relay':
                try:self.network.link(a,b)
                except TowerError as exc:raise VoltageTowerError('Forged network edge') from exc
                if not set(items).issubset(replay[a]):
                    raise VoltageTowerError('Claimed relay before sender possessed certificate')
                replay[b].update(items)
            else:
                raise VoltageTowerError('Unknown causal record action')
        if replay!=self.known:
            raise VoltageTowerError('Receiver possession does not match causal network replay')

    def final_macro_succ(self) -> VoltageProof:
        if self.macro_updates:
            raise VoltageTowerError('The one receiver macro-commit is already recorded')
        if self._signature()!=self.signature:
            raise VoltageTowerError('Source signature drift after local verification')
        self._replay_causal_network()
        expected={self._id(n) for n in self.climbers}
        if self.known['E']!=expected:
            raise VoltageTowerError('One or more required proof shards never reached E')
        claimed=[]
        checked=0
        for name in self.climbers:
            sid=self._id(name)
            shard=self.shards.get(sid)
            if (shard is None or shard.identity!=sid or shard.origin!=name
                    or shard.source_signature!=self.signature or shard.basis!=self.basis
                    or shard.parents!=self._expected_parents(name)
                    or not set(shard.parents).issubset(self.known['E'])
                    or shard.assigned!=self.assigned[name]):
                raise VoltageTowerError('Forged, stale, incomplete or source-mismatched shard')
            count=self._edge_check(shard.assigned)
            if count!=shard.checked_edges:
                raise VoltageTowerError('Lied-about source edge count')
            checked+=count
            claimed.extend(shard.assigned)
        if len(claimed)!=len(self.vertices) or set(claimed)!=self.vertex_set:
            raise VoltageTowerError('Incomplete or duplicated directed-edge source coverage')
        if len(self.potentials)!=len(self.vertices):
            raise VoltageTowerError('Candidate potential does not cover entire source graph')
        independent=quotient_holonomy(self.sieve,self.squared_step,max_cells=100_000)
        if not independent.confined:
            raise VoltageTowerError('Independent holonomy oracle found escape')
        self.macro_updates=1
        return VoltageProof(self.signature,self.sieve.period,len(claimed),checked,
                            len(self.shards),independent.largest_finite_quotient_component,
                            self.macro_updates,True)


def completed_voltage_climb(*, levels: int = 3, source: GaussianSieve | None = None,
                             squared_step: int = 1, descent: bool = True) -> VoltageTower:
    if source is None:
        source=GaussianSieve(((1,2),(2,3)))
    tower=VoltageTower(source,squared_step,levels)
    for level in range(levels):
        if level:
            for receiver in (f'A{level}',f'B{level}'):
                for sender in (f'A{level-1}',f'B{level-1}'):
                    tower.relay(sender,receiver)
        tower.check_at(f'A{level}')
        tower.check_at(f'B{level}')
    if descent:
        for level in range(levels-1,0,-1):
            tower.relay(f'A{level}',f'B{level-1}')
            tower.relay(f'B{level}',f'A{level-1}')
        tower.relay('A0','E')
        tower.relay('B0','E')
    return tower
