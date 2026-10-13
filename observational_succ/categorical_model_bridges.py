"""Typed, compositional cross-model bridges for source-relative observational SUCC.

MB1: an exact finite rational-identity certificate proves ALL-frequency equality
     of passive boundary transfer matrices when the allowed RC model orders
     are independently declared (not inferred from finite samples).
MB2: boundary black-box equality is a congruence for parallel composition and
     a well-posed boundary-feedback context, but not hidden-node interventions.
MB3: electrical RC diffusion and thermal diffusion have a law-preserving
     mathematical adapter, not identical empirical semantics or source identity.
MB4: a continuous-time absorbing Markov walk computes the same discounted
     harmonic extension as an RC boundary network (Feynman-Kac/first jump).
MB5: the passive dynamic Dirichlet-to-Neumann map has alternating Loewner
     derivatives; finite monotonicity probes can refute false candidate classes.

All results are classical (black-box functors, Feynman-Kac/Dirichlet,
Schur-complement rationality, Stieltjes spectral theory). Exact Fractions check
finite certificates. No physical-origin attestation, novel theorem or RH claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from typing import Sequence

from .dynamic_boundary_inverse import (
    RCNetwork, BoundarySourceError, exact, inv, mm, madd, mat,
    submatrix, quad, tr,
)


class BridgeError(ValueError):
    """Invalid model context, unlicensed adapter, or failed source certificate."""


def _positive_semidefinite(A):
    """All principal minors >=0: exact criterion for a symmetric matrix."""
    n=len(A)
    if not n or any(len(row)!=n for row in A):
        raise BridgeError("Expected a square matrix")
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        return False
    from .categorical_repair_synthesis import determinant
    return all(determinant(submatrix(A,idx,idx))>=0
               for k in range(1,n+1) for idx in combinations(range(n),k))


def _matrix_equal(A,B):
    return len(A)==len(B) and all(tuple(a)==tuple(b) for a,b in zip(A,B))


@dataclass(frozen=True)
class ModelCapsule:
    """Externally usable contract; the network internals are a mathematical witness.

    The electrical and thermal cases transport a *numerical PDE law*, not
    measurements or ontological claims across physical systems. The original
    graph remains available for second-order refinement and source audits.
    """
    network: RCNetwork
    domain: str
    source_id: str
    epoch: int
    basis_id: str

    def __post_init__(self):
        if not isinstance(self.network,RCNetwork):
            raise BridgeError("A declared rational passive mathematical source required")
        if self.domain not in ("electrical_RC", "thermal_diffusion"):
            raise BridgeError("Unsupported physical semantics; no guessed adapter")
        if (not self.source_id or not self.basis_id
                or type(self.epoch) is not int or self.epoch<0):
            raise BridgeError("Original-source ID, epoch, and basis required")

    @property
    def boundary(self):return self.network.boundary

    @property
    def modal_order_bound(self):return len(self.network.interior)

    def response(self,s):
        return self.network.response(exact(s))

    def public_contract(self):
        return {"boundary":self.boundary,
                "law":"positive_linear_diffusion_with_zero_initial_storage",
                "frequency_domain":"rational Laplace s>=0",
                "physical_domain":self.domain,
                "source_id":self.source_id,"epoch":self.epoch,
                "basis_id":self.basis_id,
                "declared_rational_degree_upper_bound":self.modal_order_bound,
                "physical_origin_authenticated":False}


def thermal_correspondence(source:ModelCapsule, *, new_source_id="thermal-analogy"):
    """Explicit E<->T, current<->heat-flow adapter; no claim that experiments coincide."""
    if source.domain!="electrical_RC":raise BridgeError("Electrical source required for thermal adapter")
    if not new_source_id or new_source_id==source.source_id:
        raise BridgeError("Distinct provenance necessary for cross-domain ANALOGY")
    target=ModelCapsule(source.network,"thermal_diffusion",new_source_id,
                        source.epoch,source.basis_id)
    return {"target":target,"adapter":{
        "voltage":"temperature","current":"heat_flux",
        "conductance":"thermal_conductance","capacitance":"heat_capacity",
        "time":"time", "boundary_order":source.boundary},
        "law_isomorphism":True,
        "same_physical_carrier_asserted":False,
        "same_empirical_units_asserted":False}


@dataclass(frozen=True)
class AllFrequencyCertificate:
    """Finite exact test for a universally quantified rational identity.

    Cross-multiplying two transfer entries has polynomial degree at most
    n_left+n_right. Equality at n_left+n_right+1 distinct nonnegative
    rational points forces polynomial identity. This requires SOURCE-DERIVED
    rational-degree bounds for both *declared* model classes.
    """
    equivalent: bool
    test_points: tuple[Q,...]
    degree_bound: int
    witness: tuple[Q,int,int,Q,Q] | None
    shared_port_names: tuple[str,...]
    comparison: str
    declared_source_context_matched: bool
    physical_source_identity_authenticated: bool
    all_frequency_scope: str


def certify_all_frequency(left:ModelCapsule,right:ModelCapsule,
                          *,adapter="same_semantics"):
    if not isinstance(left,ModelCapsule) or not isinstance(right,ModelCapsule):
        raise BridgeError("Only certified model capsules")
    if left.boundary!=right.boundary or left.basis_id!=right.basis_id:
        raise BridgeError("Port order / semantic basis mismatch; supply separate audited wiring")
    if adapter=="same_semantics":
        if left.domain!=right.domain:
            raise BridgeError("Different units require a declared cross-domain adapter")
        if (left.source_id,left.epoch)!=(right.source_id,right.epoch):
            raise BridgeError("Original source/epoch mismatch in SAME-SOURCE equivalence")
    elif adapter=="thermal_electrical_law":
        if {left.domain,right.domain}!={"electrical_RC","thermal_diffusion"}:
            raise BridgeError("Thermal/electrical numerical law bridge only")
        if left.source_id==right.source_id:
            raise BridgeError("Do not conflate different physical domains as one carrier")
    else:raise BridgeError("Unknown categorical/model adapter")
    d=left.modal_order_bound+right.modal_order_bound
    points=tuple(Q(s) for s in range(d+1))
    for s in points:
        A,B=left.response(s),right.response(s)
        if not _matrix_equal(A,B):
            for i in range(len(A)):
                for j in range(len(A)):
                    if A[i][j]!=B[i][j]:
                        return AllFrequencyCertificate(False,points,d,(s,i,j,A[i][j],B[i][j]),
                            left.boundary,adapter,adapter=="same_semantics",False,
                            "One exact mismatch refutes the proposed all-frequency transfer")
    return AllFrequencyCertificate(True,points,d,None,left.boundary,adapter,
        adapter=="same_semantics",False,
        "Rational Schur transfers of declared orders; zero initial state; s>=0")


def parallel_network(A:RCNetwork,B:RCNetwork,*,name="composed-parallel"):
    """Disjoint interior wiring; shared terminals are identified, currents add.

    This is one typed instance of open-network/cospan composition. We do
    not claim that arbitrary wiring is a valid plain DtN matrix composition.
    """
    if not isinstance(A,RCNetwork) or not isinstance(B,RCNetwork) or A.boundary!=B.boundary:
        raise BridgeError("Parallel wiring needs same ordered terminals")
    b=A.boundary
    renames=[]
    edges=[]
    caps=[]
    for prefix,net in (("A",A),("B",B)):
        sub={v:v if v in b else prefix+":"+v for v in net.vertices}
        renames.extend(sub[v] for v in net.interior)
        edges.extend((sub[u],sub[v],w) for u,v,w in net.edges)
        caps.extend((sub[v],c) for v,c in net.capacitors)
    # Adjacent shared boundary-boundary edges are parallel resistors: sum weights.
    aggregated={}
    for u,v,w in edges:
        key=tuple(sorted((u,v)))
        aggregated[key]=aggregated.get(key,Q(0))+w
    result=RCNetwork(name,b+tuple(renames),b,
        tuple((u,v,w) for (u,v),w in sorted(aggregated.items())),tuple(caps))
    return result


def parallel_context_response(A:RCNetwork,B:RCNetwork,s):
    return madd(A.response(s),B.response(s))


def feedback_response(M,s,k):
    """Boundary-only well-posed linear context y=(I+k Lambda)^-1 Lambda u."""
    if not isinstance(M,(ModelCapsule,RCNetwork)):
        raise BridgeError("A certified source model or capsule is required")
    k=exact(k)
    if k<0:raise BridgeError("Positive feedback impedance only")
    L=M.response(s)
    n=len(L)
    Z=tuple(tuple((Q(1) if i==j else Q(0))+k*L[i][j]
                  for j in range(n)) for i in range(n))
    return mm(inv(Z),L)


def context_reuse_receipt(left:ModelCapsule,right:ModelCapsule,context:RCNetwork,
                         *,feedback_strength=1):
    """Context equivalence follows from all-frequency identity, NOT sample matching."""
    if not isinstance(context,RCNetwork):raise BridgeError("A real lawful context model required")
    cert=certify_all_frequency(left,right)
    if not cert.equivalent:raise BridgeError("Cannot substitute non-equivalent interface behaviors")
    if context.boundary!=left.boundary:raise BridgeError("Composition context port mismatch")
    pa=parallel_network(left.network,context)
    pb=parallel_network(right.network,context)
    composed=certify_all_frequency(
        ModelCapsule(pa,left.domain,left.source_id,left.epoch,left.basis_id),
        ModelCapsule(pb,right.domain,right.source_id,right.epoch,right.basis_id))
    if not composed.equivalent:
        raise ArithmeticError("Black-box parallel congruence violated")
    return {"original":cert,"composed":composed,
            "parallel_all_frequency_equivalent":True,
            "feedback_checked_points":tuple(Q(i) for i in (0,1,3,7)),
            "feedback_equal":all(feedback_response(left,s,feedback_strength)==
                                  feedback_response(right,s,feedback_strength)
                                  for s in (0,1,3,7)),
            "hidden_state_interventions_unrestricted":False,
            "physical_ontology_identified":False}


@dataclass(frozen=True)
class AbsorbingMarkovBridge:
    """CTMC interpretation of a finite graph with strictly positive interior storage.

    On interior I, generator Q=-C^-1 L_II; absorbing boundary rates
    R=-C^-1 L_IB. First-jump/discount gives H(s)=(sI-Q)^-1 R.
    This H(s) is the discounted boundary-hitting kernel; its endpoint
    Dirichlet-to-Neumann flux is L_BB+L_BI H(s).
    """
    network: RCNetwork
    generator: tuple[tuple[Q,...],...]
    exit_rates: tuple[tuple[Q,...],...]
    boundary: tuple[str,...]

    def hitting(self,s):
        s=exact(s)
        if s<0:raise BridgeError("Laplace discount must be nonnegative")
        n=len(self.generator)
        A=tuple(tuple((s if i==j else Q(0))-self.generator[i][j]
                       for j in range(n)) for i in range(n))
        return mm(inv(A),self.exit_rates)

    def boundary_response(self,s):
        Lbb,Lbi,_,_=self.network.components()
        return madd(Lbb,mm(Lbi,self.hitting(s)))

    def exit_probabilities(self):return self.hitting(0)

    def expected_absorption_time(self):
        n=len(self.generator)
        A=tuple(tuple(-self.generator[i][j] for j in range(n)) for i in range(n))
        T=mm(inv(A),tuple((Q(1),) for _ in range(n)))
        return tuple(row[0] for row in T)


def build_markov_bridge(net:RCNetwork):
    if not isinstance(net,RCNetwork) or not net.interior:
        raise BridgeError("Need an actual positive-storage interior network")
    Lbb,Lbi,A,D=net.components()
    if any(c<=0 for c in D):raise BridgeError("Markov time requires strictly positive interior storage")
    n=len(D)
    K=tr(Lbi)
    Qgen=tuple(tuple(-A[i][j]/D[i] for j in range(n)) for i in range(n))
    exits=tuple(tuple(-K[i][j]/D[i] for j in range(len(net.boundary))) for i in range(n))
    if any(Qgen[i][j]<0 for i in range(n) for j in range(n) if i!=j) or any(
        v<0 for row in exits for v in row):
        raise BridgeError("Negative Markov transition or absorption rate")
    if any(sum(Qgen[i],Q(0))+sum(exits[i],Q(0))!=0 for i in range(n)):
        raise BridgeError("Generator violates the lawful conservative-with-absorption relation")
    return AbsorbingMarkovBridge(net,Qgen,exits,net.boundary)


def derivative_sign_certificates(net:RCNetwork,s):
    """Exact Λ'(s) PSD and -Λ''(s) PSD factorizations (source model assumed).

    A=L_II+s C, K=L_IB. Derivative Λ'=K^T A^-1 C A^-1 K;
    -Λ''=2 K^T A^-1 C A^-1 C A^-1 K. Both Gram PSD for A,C SPD.
    Spectral resolution gives ALL higher alternating signs analytically.
    """
    s=exact(s)
    if s<0 or not isinstance(net,RCNetwork):raise BridgeError("Passive model and s>=0 needed")
    _,Lbi,A,D=net.components()
    if not D or any(d<=0 for d in D):raise BridgeError("Strictly positive hidden capacities needed")
    n=len(D)
    As=tuple(tuple(A[i][j]+(s*D[i] if i==j else 0) for j in range(n)) for i in range(n))
    Ai=inv(As)
    C=tuple(tuple(D[i] if i==j else Q(0) for j in range(n)) for i in range(n))
    K=tr(Lbi)
    d1=mm(mm(mm(mm(Lbi,Ai),C),Ai),K)
    dd=mm(mm(mm(mm(mm(mm(Lbi,Ai),C),Ai),C),Ai),K)
    d2=tuple(tuple(2*x for x in row) for row in dd)
    if not _positive_semidefinite(d1) or not _positive_semidefinite(d2):
        raise ArithmeticError("Passive derivative Gram positivity failed")
    return {"s":s,"first_derivative":d1,"negative_second_derivative":d2,
            "loewner_first_positive":True,"loewner_second_negative":True,
            "higher_orders_require_classical_spectral_argument":True,
            "RH_positivity_claimed":False}


def finite_passivity_shadow_test(A0,A1,A2):
    """Necessary finite inequalities ONLY; passing does not characterize all RC laws."""
    X=mat(A0);Y=mat(A1);Z=mat(A2)
    if any(len(M)!=len(X) or len(M[0])!=len(X[0]) for M in (Y,Z)):
        raise BridgeError("Same boundary matrix sizes required")
    increment01=madd(Y,X,sign=-1)
    increment12=madd(Z,Y,sign=-1)
    curvature=madd(increment01,increment12,sign=-1)
    return {"monotone_first":_positive_semidefinite(increment01),
            "monotone_second":_positive_semidefinite(increment12),
            "concave_midpoint":_positive_semidefinite(curvature),
            "all_frequency_passivity_certified":False}


def categorical_bridge_demo():
    from .dynamic_boundary_inverse import star,twin_hubs,serial_pendant,triangle
    a=ModelCapsule(star(),"electrical_RC","one-original-network",0,"3port-Laplace")
    b=ModelCapsule(twin_hubs(),"electrical_RC","one-original-network",0,"3port-Laplace")
    equivalence=certify_all_frequency(a,b)
    thermal=thermal_correspondence(a)
    adapter=certify_all_frequency(a,thermal["target"],adapter="thermal_electrical_law")
    witness=build_markov_bridge(serial_pendant())
    connection=triangle()
    composition=context_reuse_receipt(a,b,connection)
    derivatives=derivative_sign_certificates(serial_pendant(),1)
    dynamic_vs_static=certify_all_frequency(a,ModelCapsule(triangle(),"electrical_RC",
        "one-original-network",0,"3port-Laplace"))
    assert equivalence.equivalent and adapter.equivalent and not dynamic_vs_static.equivalent
    return {"status":"CERTIFIED_CATEGORY_BRIDGES_AND_CONTEXTUAL_MODEL_ABSTRACTION",
            "all_frequency_static_star_twin_equal":equivalence.equivalent,
            "all_frequency_certificate_points":equivalence.test_points,
            "cross_domain_mathematical_adapter":adapter.comparison,
            "physical_origin_transported":adapter.physical_source_identity_authenticated,
            "serial_absorption_probability_sums":tuple(sum(row,Q(0)) for row in witness.exit_probabilities()),
            "star_exit_ratio":build_markov_bridge(a.network).exit_probabilities(),
            "parallel_context_equivalent":composition["parallel_all_frequency_equivalent"],
            "feedback_context_equivalent":composition["feedback_equal"],
            "static_vs_dynamic_counterexample":dynamic_vs_static.witness,
            "passive_derivative_psd":(derivatives["loewner_first_positive"],derivatives["loewner_second_negative"]),
            "all_representations_physically_same":False,
            "RH_or_Weil_positivity_proved":False}


@dataclass(frozen=True)
class ConnectionDiscovery:
    """Pairwise certified mathematical connections; physical origins stay separate."""
    names: tuple[str,...]
    links: tuple[tuple[str,str,str,int],...]
    falsified: tuple[tuple[str,str,str],...]
    components: tuple[tuple[str,...],...]
    potential_abstract_transfers: int
    cross_domain_actual_carrier_identity: bool


def discover_model_connections(capsules:Sequence[ModelCapsule]):
    """E searches a model library, not by names or known interiors.

    Candidates pass: port/basis typing, explicit domain adapter, then a
    sufficient all-frequency rational identity test. The connected groups
    are of mathematical behaviors, NOT shared empirical/ontological sources.
    This uses only declared source models and exact boundary semantics.
    """
    models=tuple(capsules)
    names=tuple(f"{v.domain}:{v.network.name}:{v.source_id}" for v in models)
    if not models or len(set(names))!=len(names) or any(not isinstance(v,ModelCapsule) for v in models):
        raise BridgeError("Nonempty, uniquely identified source-model library required")
    parent=list(range(len(models)))
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    links=[];fails=[]
    for i,j in combinations(range(len(models)),2):
        a,b=models[i],models[j]
        adapter="same_semantics" if a.domain==b.domain else "thermal_electrical_law"
        try:result=certify_all_frequency(a,b,adapter=adapter)
        except BridgeError as exc:
            fails.append((names[i],names[j],"INVALID_CONTEXT:"+str(exc)))
            continue
        if result.equivalent:
            links.append((names[i],names[j],adapter,result.degree_bound))
            ri,rj=root(i),root(j)
            if ri!=rj:parent[rj]=ri
        else:
            fails.append((names[i],names[j],
                         "FINITE_SOURCE_WITNESS:"+str(result.witness)))
    cc={}
    for i,name in enumerate(names):cc.setdefault(root(i),[]).append(name)
    return ConnectionDiscovery(names,tuple(links),tuple(fails),
        tuple(sorted((tuple(sorted(x)) for x in cc.values()))),
        len(links),False)


def _derivative_matrices(net:RCNetwork,s=0):
    """Return Λ',Λ'' at s; zero matrices for memoryless boundary networks."""
    if not isinstance(net,RCNetwork):raise BridgeError("Source model required")
    if not net.interior:
        n=len(net.boundary)
        zero=tuple(tuple(Q(0) for j in range(n)) for i in range(n))
        return zero,zero
    _,Lbi,A,D=net.components()
    if any(c<0 for c in D):raise BridgeError("No negative source storage")
    s=exact(s);n=len(D)
    As=tuple(tuple(A[i][j]+(s*D[i] if i==j else Q(0)) for j in range(n)) for i in range(n))
    Ai=inv(As)
    C=tuple(tuple(D[i] if i==j else Q(0) for j in range(n)) for i in range(n))
    K=tr(Lbi)
    d1=mm(mm(mm(mm(Lbi,Ai),C),Ai),K)
    dd=mm(mm(mm(mm(mm(mm(Lbi,Ai),C),Ai),C),Ai),K)
    d2=tuple(tuple(-2*x for x in row) for row in dd)
    return d1,d2


def context_depth_witness(left:ModelCapsule,right:ModelCapsule):
    """When may E leave internals encapsulated? Certified graded context check.

    0: instantaneous (DC) information; 1: first derivative / memory;
    2: second derivative; full: complete boundary LTI behavior;
    hidden intervention: STILL NOT implied by all-frequency equality.
    """
    if left.domain!=right.domain or left.source_id!=right.source_id or left.epoch!=right.epoch or left.basis_id!=right.basis_id or left.boundary!=right.boundary:
        raise BridgeError("Same-source, same-domain and ordered-port gate for graded context")
    z=Q(0)
    if left.response(z)!=right.response(z):
        return {"first_distinguishing_level":"STATIC_DC", "all_frequency":False,
                "hidden_intervention_equivalence":False}
    a=_derivative_matrices(left.network,z)
    b=_derivative_matrices(right.network,z)
    if a[0]!=b[0]:
        return {"first_distinguishing_level":"FIRST_DYNAMIC_DERIVATIVE",
                "all_frequency":False,"hidden_intervention_equivalence":False}
    if a[1]!=b[1]:
        return {"first_distinguishing_level":"SECOND_DYNAMIC_DERIVATIVE",
                "all_frequency":False,"hidden_intervention_equivalence":False}
    eq=certify_all_frequency(left,right)
    return {"first_distinguishing_level":
            "NO_BOUNDARY_DISTINCTION_ALL_FREQUENCIES" if eq.equivalent else "HIGHER_DYNAMIC_ORDER",
            "all_frequency":eq.equivalent,
            "hidden_intervention_equivalence":False,
            "theorem":"rational degree-bound identity"}


def boundary_taylor_jet(net:RCNetwork,order:int,*,center=0):
    """Exact Taylor coefficients of Λ(s) around any rational center s>=0.

    No derivative sampling. Matrix inverse Neumann identity holds analytically
    near each center with positive definite interior. The coefficient at k is
    Λ^(k)(center)/k!. A k-jet records one graded observable context.
    """
    if not isinstance(net,RCNetwork) or type(order) is not int or not 0<=order<=10:
        raise BridgeError("Known RC model and finite jet order <=10 required")
    center=exact(center)
    if center<0:raise BridgeError("Center must be inside the passive domain")
    n=len(net.boundary)
    if not net.interior:
        z=tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))
        return (net.response(center),)+(z,)*order
    Lbb,Lbi,A,D=net.components()
    nI=len(D)
    Ac=tuple(tuple(A[i][j]+(center*D[i] if i==j else Q(0))
                   for j in range(nI)) for i in range(nI))
    Ai=inv(Ac)
    C=tuple(tuple(D[i] if i==j else Q(0) for j in range(nI)) for i in range(nI))
    kterm=Ai
    coeff=[]
    for k in range(order+1):
        val=mm(mm(Lbi,kterm),tr(Lbi))
        if k==0:coeff.append(madd(Lbb,val,sign=-1))
        else:coeff.append(tuple(tuple(((-1)**(k+1))*v for v in row) for row in val))
        kterm=mm(mm(Ai,C),kterm)
    return tuple(coeff)


def feedback_jet(jet:Sequence[object],impedance=1):
    """Recursive k-jet of (I+kΛ)^-1Λ; context composition without internals."""
    data=tuple(mat(M) for M in jet)
    if not data:raise BridgeError("A finite known interface jet is required")
    k=exact(impedance)
    if k<0:raise BridgeError("Nonnegative feedback impedance required")
    n=len(data[0])
    if any(len(M)!=n or len(M[0])!=n for M in data):
        raise BridgeError("Incompatible interface jet matrices")
    S0=tuple(tuple((Q(1) if i==j else Q(0))+k*data[0][i][j]
                   for j in range(n)) for i in range(n))
    inv0=inv(S0)
    out=[]
    for t,Lt in enumerate(data):
        correction=tuple(tuple(Q(0) for j in range(n)) for i in range(n))
        for j in range(1,t+1):
            prod=mm(data[j],out[t-j])
            correction=madd(correction,tuple(tuple(k*v for v in row) for row in prod))
        out.append(mm(inv0,madd(Lt,correction,sign=-1)))
    return tuple(out)


def graded_context_substitution(left:ModelCapsule,right:ModelCapsule,order:int,
                                *,impedance=1):
    """A source-relative k-jet congruence, not a hidden-intervention promise."""
    if (left.boundary!=right.boundary or left.domain!=right.domain or
        (left.source_id,left.epoch,left.basis_id)!=(right.source_id,right.epoch,right.basis_id)):
        raise BridgeError("Typed and original-source aligned graded models required")
    J1=boundary_taylor_jet(left.network,order)
    J2=boundary_taylor_jet(right.network,order)
    if J1!=J2:
        return {"matching_k_jet":False,"first_failed_order":next(i for i,(x,y) in enumerate(zip(J1,J2)) if x!=y),
                "feedback_context_matches":False,"all_frequency":False}
    F1,F2=feedback_jet(J1,impedance),feedback_jet(J2,impedance)
    if F1!=F2:raise ArithmeticError("Formal context substitution not natural")
    return {"matching_k_jet":True,"matched_orders":order+1,
            "feedback_context_matches":True,
            "all_frequency":certify_all_frequency(left,right).equivalent,
            "hidden_intervention_equivalence":False}
