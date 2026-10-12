"""Exact fundamental-cycle proof support and restricted-observer no-go.

Classical graph H^1: a voltage 1-cochain is exact iff it vanishes on a
fundamental cycle basis (one for each cotree dart, with graph treated as
an undirected multigraph). A claimed independent cycle-budget lower bound
is explicitly relative to an ORACLE returning only one chosen fundamental
cycle's voltage, not a restriction on arbitrary symbolic mathematics.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from .local_global_descent import VoltageSource, add, sub, neg, DescentError, verify_closed_walk


@dataclass(frozen=True)
class FundamentalCycle:
    chord: str
    walk: tuple[tuple[str,int],...]
    voltage: tuple[int,...]


@dataclass(frozen=True)
class CycleBudget:
    vertices: int
    darts: int
    components: int
    independent_cycles: int
    local_source_equations: int
    cycles: tuple[FundamentalCycle,...]
    global_exact: bool


def fundamental_cycle_certificate(g:VoltageSource)->CycleBudget:
    adj={v:[] for v in g.vertices}
    for d in g.darts:
        adj[d.tail].append((d.head,d.key,1,d.displacement))
        adj[d.head].append((d.tail,d.key,-1,neg(d.displacement)))
    visited=set(); potentials={};parent={};tree_edges=set();components=0
    for root in g.vertices:
        if root in visited:continue
        components+=1;visited.add(root);potentials[root]=(0,)*g.dimension;q=deque([root])
        while q:
            u=q.popleft()
            for v,key,sgn,step in adj[u]:
                if v not in visited:
                    visited.add(v);parent[v]=(u,key,sgn)
                    tree_edges.add(key);potentials[v]=add(potentials[u],step);q.append(v)

    def path_to_root(v):
        result=[]
        while v in parent:
            u,key,sgn=parent[v]
            result.append((key,sgn))
            v=u
        return tuple(reversed(result))

    cycles=[]
    for d in g.darts:
        if d.key in tree_edges:continue
        first=path_to_root(d.tail)
        second=tuple((key,-sgn) for key,sgn in reversed(path_to_root(d.head)))
        walk=first+((d.key,1),)+second
        voltage=add(sub(potentials[d.tail],potentials[d.head]),d.displacement)
        # Zero-valued cycles still have legitimate combinatorial witnesses.
        if voltage!=(0,)*g.dimension:
            verify_closed_walk(g,walk,voltage)
        cycles.append(FundamentalCycle(d.key,walk,voltage))
    beta=len(g.darts)-len(g.vertices)+components
    if beta!=len(cycles):raise AssertionError('Fundamental cycle rank incorrect')
    return CycleBudget(len(g.vertices),len(g.darts),components,beta,len(g.darts),
                       tuple(cycles),all(c.voltage==(0,)*g.dimension for c in cycles))


def adversarial_cycle_probe_lower_bound(beta:int)->dict:
    """For one-fundamental-cycle-at-a-time voltage readouts only.

    The zero source and the beta sources mutating precisely one chord
    are pairwise indistinguishable until its corresponding cycle is tested.
    An arbitrary global proof/circuit may use a different stronger oracle.
    """
    if type(beta) is not int or beta<0:raise DescentError('Nonnegative cycle rank required')
    return {'zero_source':tuple(0 for _ in range(beta)),
            'single_fault_sources':tuple(tuple(int(i==j) for i in range(beta))
                                          for j in range(beta)),
            'required_distinct_cycle_probes':beta,
            'scope':'single-fundamental-cycle voltage oracle, arbitrary cochains'}
