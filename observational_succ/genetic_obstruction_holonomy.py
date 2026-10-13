"""Automatic obstruction -> nonflat-connection language repair for binary
model-overlap constraints. Cycle holonomy, not deletion of inconvenient data.

Original equations x_v = x_u XOR b_e need a global potential to hold
simultaneously. Inconsistent cycles have no such potential but still define
lawful per-edge invertible transports in a Z/2Z local system. This is
classical signed-graph/voltage-groupoid mathematics, integrated into model
recombination. The new connection is a representation, not proof of a
single-valued global original-source state.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from itertools import product
from .relational_model_genetics import GeneticsError


@dataclass(frozen=True)
class ParityEdge:
    name:str
    u:str
    v:str
    shift:int
    source_id:str='declared-source'

    def __post_init__(self):
        if (not self.name or not self.u or not self.v or not self.source_id or
            type(self.shift) is not int or self.shift not in (0,1)):
            raise GeneticsError('Typed exact binary local transport required')


@dataclass(frozen=True)
class CycleWitness:
    edge_names:tuple[str,...]
    cycle_nodes:tuple[str,...]
    accumulated_shift:int

    @property
    def nontrivial(self):return self.accumulated_shift!=0


@dataclass(frozen=True)
class GaugeCertificate:
    global_potential:tuple[tuple[str,int],...]|None
    obstruction:CycleWitness|None
    all_transports_are_invertible:bool
    repaired_semantics:str
    source_id:str


def _graph(edges:tuple[ParityEdge,...]):
    if not edges or len({e.name for e in edges})!=len(edges):
        raise GeneticsError('Require finite, distinctly named source edges')
    if len({e.source_id for e in edges})!=1:
        raise GeneticsError('Disparate source edges need verified source morphisms')
    graph={}
    for edge in edges:
        graph.setdefault(edge.u,[]).append((edge.v,edge.shift,edge.name))
        graph.setdefault(edge.v,[]).append((edge.u,edge.shift,edge.name))
    return graph


def discover_holonomy(edges:tuple[ParityEdge,...])->GaugeCertificate:
    """Construct a path-independence witness using a spanning forest.

    Discovery is O(vertices+edges). If a spanning-tree potential fails on an
    edge, the tree path + that edge yields a closed nonzero-Z2 path.
    """
    graph=_graph(edges)
    potential={};parent={};parentedge={};depth={}
    for root in sorted(graph):
        if root in potential:continue
        potential[root]=0;parent[root]=None;depth[root]=0
        todo=deque([root])
        while todo:
            u=todo.popleft()
            for v,delta,name in graph[u]:
                if v not in potential:
                    potential[v]=potential[u]^delta
                    parent[v]=u;parentedge[v]=name;depth[v]=depth[u]+1
                    todo.append(v)
                elif potential[v]!=(potential[u]^delta):
                    # Construct a concrete CLOSED walk: u to root, root to v,
                    # and the closing edge v->u. Walk may repeat its root;
                    # that is fine, since it remains lawful and nonzero.
                    path_u=[u];path_u_edges=[]
                    k=u
                    while parent[k] is not None:
                        path_u_edges.append(parentedge[k]);k=parent[k];path_u.append(k)
                    path_v=[v];path_v_edges=[]
                    k=v
                    while parent[k] is not None:
                        path_v_edges.append(parentedge[k]);k=parent[k];path_v.append(k)
                    # root must agree because the edge joins one component.
                    if path_u[-1]!=path_v[-1]:
                        raise ArithmeticError('Graph search has inconsistent components')
                    nodes=tuple(path_u+list(reversed(path_v[:-1]))+[u])
                    edgeword=tuple(path_u_edges+list(reversed(path_v_edges))+[name])
                    lookup={e.name:e.shift for e in edges}
                    hol=0
                    for name2 in edgeword:hol^=lookup[name2]
                    if hol!=1:
                        raise ArithmeticError('Manufactured incorrect holonomy witness')
                    return GaugeCertificate(None,CycleWitness(edgeword,nodes,hol),True,
                           'SOURCE_DERIVED_NONFLAT_Z2_CONNECTION_NOT_GLOBAL_SECTION',edges[0].source_id)
    out=tuple(sorted(potential.items()))
    return GaugeCertificate(out,None,True,
                            'FLAT_CONNECTION_WITH_GLOBAL_POTENTIAL',edges[0].source_id)


def verify_cycle_witness(edges:tuple[ParityEdge,...],w:CycleWitness)->bool:
    d={e.name:e for e in edges}
    if len(w.cycle_nodes)!=len(w.edge_names)+1 or w.cycle_nodes[0]!=w.cycle_nodes[-1]:
        return False
    hol=0
    for i,name in enumerate(w.edge_names):
        if name not in d:return False
        e=d[name]
        if {w.cycle_nodes[i],w.cycle_nodes[i+1]}!={e.u,e.v} and not (
            w.cycle_nodes[i]==w.cycle_nodes[i+1]==e.u==e.v):
            return False
        hol^=e.shift
    return hol==w.accumulated_shift and hol==1


def brute_force_has_global_section(edges:tuple[ParityEdge,...])->bool:
    nodes=tuple(sorted({v for e in edges for v in (e.u,e.v)}))
    if len(nodes)>14:raise GeneticsError('Finite oracle bounded to 14 vertices')
    for vals in product((0,1),repeat=len(nodes)):
        f=dict(zip(nodes,vals))
        if all(f[e.u]^f[e.v]==e.shift for e in edges):return True
    return False


def transport_along_path(edges:tuple[ParityEdge,...],start:str,
                         steps:tuple[str,...],initial:int)->dict:
    """Operationally meaningful on nonflat connections too: different
    paths with the same endpoints can yield different terminal values.
    """
    graph=_graph(edges)
    if start not in graph or type(initial) is not int or initial not in (0,1):
        raise GeneticsError('Legal original port state required')
    byname={e.name:e for e in edges}
    node=start;value=initial
    for name in steps:
        if name not in byname:raise GeneticsError('Undeclared edge path')
        e=byname[name]
        if e.u==node:node=e.v
        elif e.v==node:node=e.u
        else:raise GeneticsError('Noncomposable path word')
        value^=e.shift
    return {'endpoint':node,'terminal_value':value,'composable_steps':len(steps),
            'original_source_preserved_as_path_history':True}


def obstruction_language_demo():
    edges=(ParityEdge('clock:x-y','x','y',1),
           ParityEdge('thermal:y-z','y','z',1),
           ParityEdge('mechanical:x-z','x','z',1))
    result=discover_holonomy(edges)
    if result.obstruction is None or not verify_cycle_witness(edges,result.obstruction):
        raise ArithmeticError('Expected and failed to construct a nonflat path')
    travel=transport_along_path(edges,result.obstruction.cycle_nodes[0],
                                result.obstruction.edge_names,0)
    return {'all_three_local_edges_legitimate_as_transports':True,
            'global_single_valued_potential_exists':False,
            'holonomy':result.obstruction.accumulated_shift,
            'source_walk':result.obstruction.edge_names,
            'lawful_loop_flips_fiber':travel['terminal_value']==1,
            'new_model_type':result.repaired_semantics,
            'original_constraints_not_silently_deleted':True,
            'physical_ontology_claimed':False}
