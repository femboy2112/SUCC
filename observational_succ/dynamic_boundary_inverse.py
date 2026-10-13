"""Exact source-relative boundary inverse problem for passive finite RC networks.

What is proved: nonuniqueness of static / even full dynamic boundary geometry;
source-derived dynamic identification in a RESTRICTED positive network class;
strictly positive spectral Hankel determinant for a two-hidden-node example;
minimal observed dynamical dimension rather than ontological vertex count.

Everything exact uses fractions.Fraction, no floating experiment or hidden graph
identity is supplied to the estimator. Conductance/capacitance laws are declared,
not externally authenticated physical measurements. Classical network/Kalman math.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


class BoundarySourceError(ValueError):
    """Malformed source graph, unsupported probe or incompatible evidence."""


def exact(x):
    if type(x) is int or isinstance(x, Q):
        return Q(x)
    raise BoundarySourceError("Exact rational conductances and capacitors only")


def mat(rows):
    result = tuple(tuple(exact(v) for v in row) for row in rows)
    if not result or not result[0] or any(len(row) != len(result[0]) for row in result):
        raise BoundarySourceError("Nonempty rectangular matrix required")
    return result


def zeros(m, n):
    return tuple(tuple(Q(0) for _ in range(n)) for _ in range(m))


def tr(A):
    return tuple(zip(*A))


def mm(A, B):
    if not A or not B or len(A[0]) != len(B):
        raise BoundarySourceError("Incompatible matrix multiplication")
    Bt = tr(B)
    return tuple(tuple(sum((a*b for a,b in zip(row,col)),Q(0)) for col in Bt) for row in A)


def madd(A, B, *, sign=1):
    if len(A)!=len(B) or any(len(a)!=len(b) for a,b in zip(A,B)):
        raise BoundarySourceError("Matrix addition shapes differ")
    return tuple(tuple(x+sign*y for x,y in zip(a,b)) for a,b in zip(A,B))


def submatrix(A,rows,cols):
    return tuple(tuple(A[i][j] for j in cols) for i in rows)


def inv(A):
    n=len(A)
    if not n or any(len(r)!=n for r in A):
        raise BoundarySourceError("Square invertible matrix required")
    work=[[exact(A[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if work[i][j]),None)
        if pivot is None:
            raise BoundarySourceError("Interior network not anchored / singular response")
        work[j],work[pivot]=work[pivot],work[j]
        x=work[j][j]
        work[j]=[q/x for q in work[j]]
        for i in range(n):
            if i==j:continue
            x=work[i][j]
            if x:work[i]=[a-x*b for a,b in zip(work[i],work[j])]
    return tuple(tuple(row[n:]) for row in work)


def rank(A):
    if not A:return 0
    W=[list(row) for row in A]
    m,n=len(W),len(W[0]);r=0
    for c in range(n):
        j=next((j for j in range(r,m) if W[j][c]),None)
        if j is None:continue
        W[r],W[j]=W[j],W[r]
        d=W[r][c];W[r]=[z/d for z in W[r]]
        for j in range(m):
            if j!=r and W[j][c]:
                t=W[j][c];W[j]=[x-t*y for x,y in zip(W[j],W[r])]
        r+=1
        if r==m:break
    return r


def quad(A,x):
    return sum((x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),Q(0))


@dataclass(frozen=True)
class RCNetwork:
    """Positive resistors and nonnegative *interior* storage, labeled boundary."""
    name: str
    vertices: tuple[str,...]
    boundary: tuple[str,...]
    edges: tuple[tuple[str,str,Q],...]
    capacitors: tuple[tuple[str,Q],...]=()

    def __post_init__(self):
        if (not self.name or not self.vertices or len(self.vertices)!=len(set(self.vertices))
                or not self.boundary or len(self.boundary)!=len(set(self.boundary))
                or not set(self.boundary)<=set(self.vertices)):
            raise BoundarySourceError("Malformed physical/model vertices or boundary")
        interior=set(self.vertices)-set(self.boundary)
        covered=set(); pairs=set()
        for a,b,g in self.edges:
            if a not in self.vertices or b not in self.vertices or a==b or exact(g)<=0:
                raise BoundarySourceError("Edges must be positive non-loop conductances")
            key=frozenset((a,b))
            if key in pairs:raise BoundarySourceError("Use one aggregate conductance per pair")
            pairs.add(key)
        for v,c in self.capacitors:
            if v not in interior or v in covered or exact(c)<0:
                raise BoundarySourceError("Only unique, nonnegative interior storage allowed")
            covered.add(v)
        if interior:
            a=self.laplacian()
            pos=[self.vertices.index(v) for v in self.interior]
            inv(submatrix(a,pos,pos))  # also rejects detached interior components

    @property
    def interior(self):
        return tuple(v for v in self.vertices if v not in self.boundary)

    def laplacian(self):
        n=len(self.vertices)
        A=[[Q(0) for _ in range(n)] for _ in range(n)]
        ix={v:i for i,v in enumerate(self.vertices)}
        for a,b,g in self.edges:
            i,j=ix[a],ix[b];g=exact(g)
            A[i][i]+=g;A[j][j]+=g;A[i][j]-=g;A[j][i]-=g
        return mat(A)

    def components(self):
        L=self.laplacian()
        indices={v:i for i,v in enumerate(self.vertices)}
        B=tuple(indices[v] for v in self.boundary)
        I=tuple(indices[v] for v in self.interior)
        D=tuple(exact(dict(self.capacitors).get(v,0)) for v in self.interior)
        return submatrix(L,B,B), submatrix(L,B,I) if I else (), submatrix(L,I,I) if I else (), D

    def response(self,s=0):
        """Dirichlet-to-Neumann of L+sC with zero boundary capacitance."""
        s=exact(s)
        if s<0:raise BoundarySourceError("This exact passive Laplace experiment uses s>=0")
        Lbb,Lbi,A,D=self.components()
        if not D:return Lbb
        As=tuple(tuple(A[i][j]+(s*D[i] if i==j else 0) for j in range(len(D))) for i in range(len(D)))
        return madd(Lbb,mm(mm(Lbi,inv(As)),tr(Lbi)),sign=-1)

    def moments(self,count):
        """High-frequency Markov coefficients M_k of L_BB-Lambda(s).

        For strictly positive interior C, L_BB-Lambda(s) =
        sum_k (-1)^k M_k / s^(k+1), M_k=K^T C^-1 (A C^-1)^k K.
        Higher moments are SOURCE-derived, not inferred from a finite s table.
        """
        if type(count) is not int or not 0<=count<=25:
            raise BoundarySourceError("Finite moment budget 0..25")
        b=len(self.boundary)
        if not self.interior:return tuple(zeros(b,b) for _ in range(count))
        Lbb,Lbi,A,D=self.components()
        if any(c<=0 for c in D):
            raise BoundarySourceError("High-frequency moments require positive interior storage")
        K=tr(Lbi)
        Dinv=tuple(tuple(1/D[i] if i==j else Q(0) for j in range(len(D))) for i in range(len(D)))
        T=mm(A,Dinv)
        curr=mm(Dinv,K)
        out=[]
        for _ in range(count):
            out.append(mm(tr(K),curr))
            curr=mm(T,curr)
        return tuple(out)


def star(arms=(2,3,5),cap=2,*,name="star"):
    g=tuple(exact(x) for x in arms)
    if len(g)!=3 or any(x<=0 for x in g):raise BoundarySourceError("Three positive arms")
    return RCNetwork(name,("a","b","c","h"),("a","b","c"),
                     tuple((v,"h",g[i]) for i,v in enumerate(("a","b","c"))),
                     (("h",exact(cap)),))


def triangle(arms=(2,3,5),*,name="triangle"):
    g=tuple(exact(x) for x in arms)
    if len(g)!=3 or any(x<=0 for x in g):raise BoundarySourceError("Three positive arms")
    G=sum(g,Q(0));b=("a","b","c")
    return RCNetwork(name,b,b,tuple((b[i],b[j],g[i]*g[j]/G) for i in range(3) for j in range(i+1,3)))


def twin_hubs(arms=(2,3,5),cap=2,*,name="twin"):
    g=tuple(exact(x) for x in arms);c=exact(cap)
    if len(g)!=3 or any(x<=0 for x in g) or c<=0:raise BoundarySourceError("Positive two-hub twin")
    b=("a","b","c")
    return RCNetwork(name,b+("h0","h1"),b,
        tuple((v,h,g[i]/2) for h in ("h0","h1") for i,v in enumerate(b)),
        (("h0",c/2),("h1",c/2)))


def serial_pendant(arms=(2,3,5),cap0=2,link=4,cap1=3,*,name="serial"):
    g=tuple(exact(x) for x in arms)
    c0,c1,h=exact(cap0),exact(cap1),exact(link)
    if len(g)!=3 or any(x<=0 for x in g) or min(c0,c1,h)<=0:
        raise BoundarySourceError("Positive serial network required")
    b=("a","b","c")
    return RCNetwork(name,b+("h0","h1"),b,
        tuple((v,"h0",g[i]) for i,v in enumerate(b)) + (("h0","h1",h),),
        (("h0",c0),("h1",c1)))


def reconstruct_y_triangle(dc):
    """Independently recover both geometries from a 3-terminal static shadow.

    For positive full triangle uij=-Lambda_ij: unique positive star arms
      gi = ui,j + ui,k + (ui,j * ui,k)/uj,k.
    Does NOT infer which physical topology is real.
    """
    L=mat(dc)
    if len(L)!=3 or any(len(row)!=3 for row in L):
        raise BoundarySourceError("Exactly 3 grounded-current boundary ports")
    if any(L[i][j]!=L[j][i] for i in range(3) for j in range(3)) or any(sum(row)!=0 for row in L):
        raise BoundarySourceError("Source data violate symmetric current conservation")
    a,b,c=-L[0][1],-L[0][2],-L[1][2]
    if min(a,b,c)<=0:raise BoundarySourceError("No positive full Y/triangle candidate")
    g=(a+b+a*b/c,a+c+a*c/b,b+c+b*c/a)
    T=triangle(g)
    Y=star(g,cap=0)
    if L!=T.response(0) or L!=Y.response(0):
        raise ArithmeticError("Y-delta proof construction inconsistent")
    return {"arms":g,"triangle":T,"star":Y,"dc":L,
            "source_selection_proved":False,
            "static_topology_unique":False}


@dataclass(frozen=True)
class BoundaryReceipt:
    source_id: str
    source_epoch: int
    basis_id: str
    observer: str
    laplace_s: Q
    response: tuple[tuple[Q,...],...]


def observe(graph:RCNetwork,s,*,source_id="shared-RC-carrier",epoch=0,basis="three-terminal-current-v1",observer="A"):
    if not isinstance(graph,RCNetwork) or not isinstance(source_id,str) or not source_id or not isinstance(basis,str) or not basis or not observer or type(epoch) is not int or epoch<0:
        raise BoundarySourceError("Require honest mathematical source/epoch/basis labels")
    return BoundaryReceipt(source_id,epoch,basis,observer,exact(s),graph.response(s))


def filter_candidates(models:Sequence[RCNetwork],receipts:Sequence[BoundaryReceipt]):
    models=tuple(models);receipts=tuple(receipts)
    if not receipts or not models or len(set(m.name for m in models))!=len(models):
        raise BoundarySourceError("Nonempty competing hypotheses and reports required")
    h={(r.source_id,r.source_epoch,r.basis_id) for r in receipts}
    if len(h)!=1 or any(not isinstance(r,BoundaryReceipt) or not r.observer for r in receipts):
        raise BoundarySourceError("Mixed/forged source epochs or basis across towers")
    if any((r.laplace_s<0 or len(r.response)!=len(models[0].boundary)
            or any(len(row)!=len(models[0].boundary) for row in r.response))
           for r in receipts):
        raise BoundarySourceError("Unsupported Laplace input/response shape")
    survivors=[];reject={}
    for model in models:
        if not isinstance(model,RCNetwork):raise BoundarySourceError("Undeclared candidate")
        bad=next((r for r in receipts if model.response(r.laplace_s)!=r.response),None)
        if bad is None:survivors.append(model.name)
        else:reject[model.name]={"s":bad.laplace_s,"model":model.response(bad.laplace_s),"observed":bad.response}
    return {"survivors":tuple(survivors),"rejected":reject,"source_attested":False,
            "meaning":"exact consistency with declared source law, not real physical attestation"}


def scalar_h_from_response(graph_or_resp,arms,port=0,s=None):
    """If L_BB=diag(g), return (L_BB - Lambda(s))_ii/g_i^2."""
    g=tuple(exact(x) for x in arms)
    R=graph_or_resp.response(s) if isinstance(graph_or_resp,RCNetwork) else mat(graph_or_resp)
    if len(R)!=len(g) or not (0<=port<len(g)) or g[port]<=0:
        raise BoundarySourceError("Incompatible source-inferred static arm signature")
    return (g[port]-R[port][port])/(g[port]**2)


def reciprocal_three_frequency_defect(graph:RCNetwork,arms,*,steps=(0,1,2),port=0):
    """Finite accessible source invariant: inverse scalar transfer curvature."""
    if tuple(exact(x) for x in steps)!=(Q(0),Q(1),Q(2)):
        raise BoundarySourceError("This exact receipt uses s=(0,1,2)")
    h=tuple(scalar_h_from_response(graph,arms,port,s) for s in steps)
    if any(x<=0 for x in h):raise BoundarySourceError("Positive hidden transfer required")
    q=tuple(1/x for x in h)
    return {"h":h,"q":q,"second_difference":q[2]-2*q[1]+q[0],
            "single_pole_invariant":q[2]-2*q[1]+q[0]==0}


def block_hankel(moments,size):
    """Exact finite block-Hankel rank certificate for a latent dynamic order."""
    if type(size) is not int or size<1 or len(moments)<2*size-1:
        raise BoundarySourceError("Supply at least 2*size-1 exact Markov moments")
    b=len(moments[0])
    return tuple(tuple(moments[i+j][a][c] for j in range(size) for c in range(b))
                 for i in range(size) for a in range(b))


def scalar_moment_witness(moments,arms,port=0):
    g=exact(arms[port])
    if len(moments)<3 or g<=0:raise BoundarySourceError("Three moments and a positive arm required")
    m=tuple(moments[k][port][port]/g**2 for k in range(3))
    return {"m0":m[0],"m1":m[1],"m2":m[2],"hankel_determinant":m[0]*m[2]-m[1]**2}


def reconstruct_serial_from_moments(dc,moments,port=0):
    """Exact two-hidden serial star parameters from DC and 3 high-freq coefficients.

    Only valid CONDITIONAL on the named 3-arm, 2-storage series topology.
    The source never supplies the hidden network itself as an input.
    """
    arms=reconstruct_y_triangle(dc)["arms"]
    w=scalar_moment_witness(moments,arms,port)
    m0,m1,d=w["m0"],w["m1"],w["hankel_determinant"]
    if m0<=0 or d<=0:raise BoundarySourceError("Not an admissible 2-mode serial candidate")
    c0=1/m0
    G=sum(arms,Q(0))
    link=c0**2*m1-G
    if link<=0:raise BoundarySourceError("Negative/nonpositive recovered hidden link")
    c1=link**2/(c0**3*d)
    if c1<=0:raise BoundarySourceError("Invalid second hidden capacity")
    graph=serial_pendant(arms,c0,link,c1,name="E-reconstructed-two-mode")
    if graph.response(0)!=dc or graph.moments(3)!=tuple(moments[:3]):
        raise ArithmeticError("Reconstructed source fails independent forward model")
    return {"arms":arms,"c0":c0,"link":link,"c1":c1,"hankel_determinant":d,
            "geometry_reconstructed_within_declared_serial_class":True,
            "global_physical_ontology_identified":False,"replay_graph":graph}


def reconstruct_serial_from_finite_responses(dc,r1,r2,r3,port=0):
    """No infinity and no hidden parameters: four finite matrix shadows s=0,1,2,3.

    Conditional on exactly a 3-boundary star with ONE connected capacitive
    pendant, q(s)=1/h_port(s)=G+s*c0+s*c1/(1+s*c1/link).
    Let u_s=(q(s)-G)/s for s=1,2,3.  These three measurements identify
    c0,c1,link over positive rationals. Distinct source/model epochs forbidden
    by the caller's evidence validator; inputs are numerical matrices only.
    """
    arms=reconstruct_y_triangle(dc)['arms']
    G=sum(arms,Q(0))
    matrix=(mat(dc),mat(r1),mat(r2),mat(r3))
    if any(len(R)!=3 or any(len(row)!=3 for row in R) for R in matrix):
        raise BoundarySourceError('Every observer matrix must have three ports')
    hs=tuple(scalar_h_from_response(matrix[k],arms,port) for k in (1,2,3))
    if any(h<=0 for h in hs):
        raise BoundarySourceError('Positive hidden transfer required')
    slopes=tuple((1/h-G)/Q(s) for h,s in zip(hs,(1,2,3)))
    d1=slopes[0]-slopes[1]
    d2=slopes[1]-slopes[2]
    if d1<=0 or d2<=0:
        raise BoundarySourceError('No strictly decreasing passive hidden-pendant slopes')
    R=d1/d2
    if R<=1 or R>=3:
        raise BoundarySourceError('Incompatible source frequency ratio for positive serial class')
    t=(R-1)/(3-R)    # t=c1/link >0
    c1=d1*(1+t)*(1+2*t)/t
    link=c1/t
    c0=slopes[0]-c1/(1+t)
    if min(c0,c1,link)<=0:
        raise BoundarySourceError('Reconstructed capacities/link violate passive source law')
    g=serial_pendant(arms,c0,link,c1,name='E-repaired-from-finite-probes')
    if tuple(g.response(s) for s in range(4))!=matrix:
        raise BoundarySourceError('Finite response matrices incompatible with proposed repair')
    return {'arms':arms,'c0':c0,'link':link,'c1':c1,
            'reciprocal_transfer_slopes':slopes,
            'observed_cross_ratio':R,
            'strict_two_mode_ratio':True,
            'repaired_graph':g,
            'declared_two_hidden_node_topology_assumed':True,
            'physical_topology_proved':False}


def reconstruct_serial_from_receipts(receipts):
    """Typed E aggregator: no mixing epochs, physical source IDs or bases.

    The source signature checks RECORD COHERENCE, not external authenticity.
    Any valid receipt requires a declared honest instrumentation model.
    """
    reports=tuple(receipts)
    if len(reports)!=4 or any(not isinstance(r,BoundaryReceipt) for r in reports):
        raise BoundarySourceError('Four independent finite-rate source reports required')
    signatures={(r.source_id,r.source_epoch,r.basis_id) for r in reports}
    if len(signatures)!=1 or any(not r.observer for r in reports):
        raise BoundarySourceError('E rejected mixed original source, epoch or proof basis')
    if tuple(r.laplace_s for r in reports)!=(Q(0),Q(1),Q(2),Q(3)):
        raise BoundarySourceError('This repair needs exact s=0,1,2,3 checkpoints')
    return reconstruct_serial_from_finite_responses(*(r.response for r in reports))


def spectral_mode_lower_bound(graph:RCNetwork,size):
    """Hankel rank lower bound on minimal *observable dynamic* dimension."""
    m=graph.moments(2*size-1)
    h=block_hankel(m,size)
    return {"rank":rank(h),"hankel":h,"interior_count":len(graph.interior),
            "ontological_interior_count_proved":False}


def change_interior_capacitance(graph:RCNetwork,updates:dict[str,Q],*,name='after-capacitance-intervention'):
    """A SOURCE-CHANGING intervention; preserves edge topology, not dynamics.

    It preserves ALL static Dirichlet-to-Neumann facts, because s=0 erases C.
    Dynamic reports require new epoch/provenance and independent observations.
    """
    if not isinstance(graph,RCNetwork) or not updates or not set(updates)<=set(graph.interior):
        raise BoundarySourceError('Intervention must name existing interior nodes')
    C=dict(graph.capacitors)
    for v,x in updates.items():
        x=exact(x)
        if x<0:raise BoundarySourceError('Negative capacitor intervention')
        C[v]=x
    new=RCNetwork(name,graph.vertices,graph.boundary,graph.edges,tuple(sorted(C.items())))
    if graph.response(0)!=new.response(0):
        raise ArithmeticError('Source-invariant static proof lost under capacitor edit')
    return new


def certified_reciprocal_defect(intervals):
    """Strict source-independent interval sign for q(2)-2q(1)+q(0).

    Input intervals certify the reciprocal scalar transfer at s=0,1,2.
    They are not fake measured frequencies nor arbitrary floating tolerances.
    """
    if not isinstance(intervals,(tuple,list)) or len(intervals)!=3:
        raise BoundarySourceError('Three ordered rational q-intervals required')
    pair=[]
    for v in intervals:
        if not isinstance(v,(tuple,list)) or len(v)!=2:
            raise BoundarySourceError('Each observation must be an interval')
        lo,hi=map(exact,v)
        if lo<=0 or hi<lo:
            raise BoundarySourceError('Positive ordered reciprocal transfer interval')
        pair.append((lo,hi))
    (a,b),(c,d),(e,f)=pair
    bounds=(a-2*d+e,b-2*c+f)
    return {'defect_interval':bounds,
            'strictly_negative':bounds[1]<0,
            'strictly_positive':bounds[0]>0,
            'inconclusive':bounds[0]<=0<=bounds[1]}


def demonstration():
    """Construct geometries from actual synthetic source readouts, then falsify."""
    source=serial_pendant()
    L0=observe(source,0,observer="E0")
    generated=reconstruct_y_triangle(L0.response)
    g=generated["arms"]
    # One-pole star can imitate the 2-pole source at s=1 by choosing c_eff.
    h1=scalar_h_from_response(source,g,0,1)
    c_eff=1/h1-sum(g,Q(0))
    wrong_star=star(g,c_eff,name="fitted-one-mode")
    static=triangle(g,name="static-triangle")
    # E does NOT receive the hidden serial graph as a proposed candidate.
    model=(static,wrong_star)
    r1=observe(source,1,observer="E1")
    r2=observe(source,2,observer="E2")
    a=filter_candidates(model,(L0,))
    b=filter_candidates(model,(L0,r1))
    c=filter_candidates(model,(L0,r1,r2))
    # A different, explicitly declared high-frequency probe supplies three
    # exact source Markov coefficients (not the hidden model parameters).
    r3=observe(source,3,observer="E3")
    finite_repair=reconstruct_serial_from_receipts((L0,r1,r2,r3))
    trained=finite_repair["repaired_graph"]
    # High-frequency moments are an INDEPENDENT validation channel, not input
    # to the finite-sample source repair.
    mom=source.moments(3)
    recovered=reconstruct_serial_from_moments(L0.response,mom)
    if (trained.response(4)!=recovered["replay_graph"].response(4)
            or trained.moments(3)!=mom):
        raise ArithmeticError("Finite and asymptotic repair channels disagree")
    if filter_candidates((trained,),(L0,r1,r2))["survivors"] != (trained.name,):
        raise ArithmeticError("New repair fails previously received evidence")
    for holdout in (Q(4),Q(11),Q(17)):
        if trained.response(holdout)!=source.response(holdout):
            raise ArithmeticError("Repaired model failed independent holdout")
    static_star=star(g,2)
    twin=twin_hubs(g,2)
    if any(static_star.response(s)!=twin.response(s) for s in (0,1,2,5,11)):
        raise ArithmeticError("Full-dynamic observational equivalence broken")
    defect=reciprocal_three_frequency_defect(source,g)
    return {"status":"SOURCE_DERIVED_PASSIVE_BOUNDARY_REPAIR_EXACT",
      "observed_static":L0.response,"derived_arms":g,
      "initial_candidates":a["survivors"],"after_s1":b["survivors"],
      "after_s2":c["survivors"],
      "after_new_two_mode_repair":trained.name,
      "new_repair_predicts_unseen_s_4_11_17":True,
      "finite_cross_ratio":finite_repair["observed_cross_ratio"],
      "wrong_one_pole_capacity":c_eff,
      "scalar_transfer_at_0_1_2":defect["h"],
      "inverse_transfer_at_0_1_2":defect["q"],
      "inverse_transfer_second_difference":defect["second_difference"],
      "single_port_moment_hankel_determinant":scalar_moment_witness(mom,g)["hankel_determinant"],
      "two_mode_minimal_dimension":spectral_mode_lower_bound(source,2)["rank"],
      "twin_interior_count":len(twin.interior),
      "twin_observable_mode_lower_bound":spectral_mode_lower_bound(twin,2)["rank"],
      "recovered_parameters":(recovered["c0"],recovered["link"],recovered["c1"]),
      "physical_source_authenticated":False,
      "canonical_geometry_unique_outside_source_class":False,
      "RH_or_Weil_positivity_proved":False}
