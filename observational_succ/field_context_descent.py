"""Field-relative commuting squares, groupoid holonomy and proof obstructions.

The functor/diagram statements are classical conditional mathematics: declared
carrier maps and source tables are NOT real-world authentication. This is a
new-to-SUCC unified verifier for independent failure surfaces.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Hashable, Sequence

from .field_relative_closure import ClosureError, FiniteField


@dataclass(frozen=True)
class DescentAudit:
    old_source_id: str
    new_source_id: str
    old_probes: tuple[str,...]
    new_probes: tuple[str,...]
    covariance: bool
    truth_square: bool
    updated_report_proves_original_claim: bool
    report_transform: tuple[tuple[tuple[Hashable,...],tuple[Hashable,...]], ...]
    covariance_witness: tuple[Hashable,Hashable] | None
    truth_witness: Hashable | None
    loss_witness: tuple[Hashable,Hashable] | None


def audit_descent(old: FiniteField, new: FiniteField,
                  source_map: Sequence[Hashable], old_probes: Sequence[str],
                  new_probes: Sequence[str], old_target: str, new_target: str) -> DescentAudit:
    """Check three INDEPENDENT gates in one source-changing context square.

    1 O_new o h factors through O_old (covariance, existence of R).
    2 T_old = T_new o h (original-source target meaning).
    3 T_old factors through O_new o h (updated report can prove original).

    Covariance and truth preservation together do NOT imply gate 3; a lossy
    observation may never have been adequate for the original claim.
    """
    oldp,newp=old.names(old_probes),new.names(new_probes)
    if old_target not in old.targets or new_target not in new.targets:
        raise ClosureError("Both source-relative targets must be defined")
    mapping=tuple(source_map)
    if len(mapping)!=len(old.states) or any(s not in new.states for s in mapping):
        raise ClosureError("Source map must be total into actual new carrier")
    new_lookup={x:i for i,x in enumerate(new.states)}
    seen: dict[tuple,tuple[Hashable,tuple]]={}
    new_seen: dict[tuple,tuple[Hashable,Hashable]]={}
    cov_error=None
    loss_error=None
    truth_error=None
    for i,x in enumerate(old.states):
        oi=tuple(old.probes[p][i] for p in oldp)
        j=new_lookup[mapping[i]]
        nj=tuple(new.probes[p][j] for p in newp)
        t=old.targets[old_target][i]
        tn=new.targets[new_target][j]
        if t!=tn and truth_error is None:
            truth_error=x
        if oi in seen and seen[oi][1]!=nj and cov_error is None:
            cov_error=(seen[oi][0],x)
        else:
            seen.setdefault(oi,(x,nj))
        if nj in new_seen and new_seen[nj][1]!=t and loss_error is None:
            loss_error=(new_seen[nj][0],x)
        else:
            new_seen.setdefault(nj,(x,t))
    return DescentAudit(old.source_id,new.source_id,oldp,newp,
                        cov_error is None,truth_error is None,loss_error is None,
                        tuple(sorted(((o,v) for o,(_,v) in seen.items()),key=repr)),
                        cov_error,truth_error,loss_error)


Vector=tuple[int,...]


def _add(x:Vector,y:Vector)->Vector:
    return tuple(a+b for a,b in zip(x,y))


def _neg(x:Vector)->Vector:
    return tuple(-a for a in x)


@dataclass(frozen=True)
class LoopWitness:
    """A true CLOSED walk in the original directed-edge graph, with signs."""
    root: Hashable
    traversals: tuple[tuple[int,int], ...]
    translation: Vector


@dataclass(frozen=True)
class VoltageCertificate:
    status: str
    source_id: str
    source_version: int
    potentials: tuple[tuple[Hashable,Vector],...] = ()
    escape: LoopWitness | None = None


@dataclass(frozen=True)
class SourceVoltageGraph:
    """Finite graph with integer edge voltages, including loops/parallel edges."""
    source_id: str
    source_version: int
    vertices: tuple[Hashable,...]
    edges: tuple[tuple[Hashable,Hashable,Vector],...]
    dimension: int

    def __post_init__(self):
        if not self.source_id or type(self.source_version) is not int or self.source_version<0:
            raise ClosureError("Source identity/version required")
        if type(self.vertices) is not tuple or not self.vertices or len(set(self.vertices))!=len(self.vertices):
            raise ClosureError("Distinct immutable vertices required")
        if type(self.edges) is not tuple:
            raise ClosureError("Require a finite immutable edge list")
        if type(self.dimension) is not int or self.dimension < 1:
            raise ClosureError("Positive integer voltage dimension required")
        V=set(self.vertices)
        for u,v,w in self.edges:
            if u not in V or v not in V or type(w) is not tuple or len(w)!=self.dimension:
                raise ClosureError("Edge must have valid endpoints and vector")
            if any(type(a) is not int for a in w):
                raise ClosureError("Only exact integer voltages supported")

    def walk(self, witness: LoopWitness) -> Vector:
        """Independent witness verifier, checking real traversability/endpoints."""
        if not isinstance(witness,LoopWitness) or witness.root not in self.vertices:
            raise ClosureError("Forged root or invalid loop witness")
        cur=witness.root
        disp=(0,)*self.dimension
        for i,sign in witness.traversals:
            if type(i) is not int or i<0 or i>=len(self.edges) or type(sign) is not int or sign not in (-1,1):
                raise ClosureError("Forged edge token/orientation")
            u,v,w=self.edges[i]
            start,end,d=(u,v,w) if sign==1 else (v,u,_neg(w))
            if cur!=start:
                raise ClosureError("Discontinuous reported source path")
            cur=end
            disp=_add(disp,d)
        if cur!=witness.root or disp!=witness.translation or not any(disp):
            raise ClosureError("Not a closed nonzero-holonomy source witness")
        return disp

    def integrate(self)->VoltageCertificate:
        """Integrate local edge equations or exhibit a NONZERO SOURCE LOOP."""
        adj={v:[] for v in self.vertices}
        for i,(u,v,d) in enumerate(self.edges):
            adj[u].append((v,d,i,1))
            adj[v].append((u,_neg(d),i,-1))
        pot:dict[Hashable,Vector]={}
        parent:dict[Hashable,tuple[Hashable,int,int]|None]={}
        roots:dict[Hashable,Hashable]={}

        def path_to(v:Hashable)->list[tuple[int,int]]:
            out=[]
            while parent[v] is not None:
                prev,idx,sgn=parent[v]
                out.append((idx,sgn))
                v=prev
            return list(reversed(out))

        for base in self.vertices:
            if base in pot:
                continue
            pot[base]=(0,)*self.dimension
            roots[base]=base
            parent[base]=None
            queue=deque([base])
            while queue:
                u=queue.popleft()
                for v,d,i,sgn in adj[u]:
                    candidate=_add(pot[u],d)
                    if v not in pot:
                        pot[v]=candidate
                        parent[v]=(u,i,sgn)
                        roots[v]=base
                        queue.append(v)
                        continue
                    if candidate!=pot[v]:
                        if roots[u]!=roots[v]:
                            raise AssertionError("Graph traversal merged different connected roots")
                        cycle=tuple(path_to(u)+[(i,sgn)]+[(j,-z) for j,z in reversed(path_to(v))])
                        displacement=tuple(a-b for a,b in zip(candidate,pot[v]))
                        witness=LoopWitness(base,cycle,displacement)
                        self.walk(witness)
                        return VoltageCertificate("NONZERO_HOLONOMY",self.source_id,
                                                  self.source_version,escape=witness)
        return VoltageCertificate("GLOBAL_POTENTIAL",self.source_id,
                                  self.source_version,
                                  potentials=tuple((v,pot[v]) for v in self.vertices))

    def verify(self, cert:VoltageCertificate)->bool:
        if not isinstance(cert,VoltageCertificate) or (
             cert.source_id,cert.source_version)!=(self.source_id,self.source_version):
            raise ClosureError("Mismatched source certificate")
        if cert.status=="NONZERO_HOLONOMY":
            if cert.potentials or cert.escape is None:
                raise ClosureError("Malformed nonzero loop certificate")
            self.walk(cert.escape)
            return True
        if cert.status=="GLOBAL_POTENTIAL":
            if cert.escape is not None or tuple(v for v,_ in cert.potentials)!=self.vertices:
                raise ClosureError("Incomplete or forged vertex potential")
            g=dict(cert.potentials)
            if any(len(w)!=self.dimension or any(type(c) is not int for c in w)
                   for w in g.values()):
                raise ClosureError("Nonintegral potential entries")
            for u,v,d in self.edges:
                if _add(g[u],d)!=g[v]:
                    raise ClosureError("False edge-integrating source potential")
            return True
        raise ClosureError("Unknown certificate status")
