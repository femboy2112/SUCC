"""Exact, source-relative categorical repair discovery over finite Mealy and passive linear laws.

CR1: finite Mealy behavior is the coarsest observation-preserving action congruence.
CR2: finite scalar Hankel data construct a minimal consistent linear-memory model,
     CONDITIONAL on a stated rational-series complexity bound; physical ontology
     and true global response are NOT established by finite observations.
CR3: two strictly positive rational Stieltjes laws, of different minimal modal
     degrees, can agree at ANY chosen finite set of nonnegative frequencies.
CR4: finite dynamic boundary reports propose representational repairs without
     assuming an interior graph or serial-pendant circuit template.

These are classical coalgebra, automata minimization, rational interpolation,
and Ho-Kalman/Stieltjes results expressed in a source-typed SUCC architecture.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


class RepairError(ValueError):
    """Invalid source, inconsistent evidence or failure of declared domain gates."""


def F(x):
    if type(x) is int or isinstance(x, Q):
        return Q(x)
    raise RepairError("Exact rational integer/Fraction required; floats not certified")


def qtuple(seq):
    return tuple(F(x) for x in seq)


def invert(M):
    n=len(M)
    if n==0 or any(len(row)!=n for row in M):
        raise RepairError("Square nonempty rational matrix required")
    T=[[F(x) for x in M[i]]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if T[i][j]),None)
        if pivot is None:raise RepairError("Singular rational source matrix")
        T[pivot],T[j]=T[j],T[pivot]
        a=T[j][j];T[j]=[x/a for x in T[j]]
        for k in range(n):
            if k==j:continue
            v=T[k][j]
            if v:T[k]=[a-v*b for a,b in zip(T[k],T[j])]
    return tuple(tuple(row[n:]) for row in T)


def product(A,B):
    if not A or not B or len(A[0])!=len(B):
        raise RepairError("Incompatible matrix multiplication")
    return tuple(tuple(sum((a*B[k][j] for k,a in enumerate(row)),Q(0))
                       for j in range(len(B[0]))) for row in A)


def matvec(A,v):
    return tuple(sum((a*x for a,x in zip(row,v)),Q(0)) for row in A)


def determinant(A):
    n=len(A)
    if n==0 or any(len(row)!=n for row in A):
        raise RepairError("Nonempty square matrix for determinant")
    B=[[F(x) for x in row] for row in A]
    det=Q(1)
    for j in range(n):
        k=next((k for k in range(j,n) if B[k][j]),None)
        if k is None:return Q(0)
        if k!=j:B[k],B[j]=B[j],B[k];det=-det
        v=B[j][j];det*=v
        for i in range(j+1,n):
            ratio=B[i][j]/v
            for q in range(j,n):B[i][q]-=ratio*B[j][q]
    return det


def positive_definite(A):
    return bool(A) and all(determinant(tuple(tuple(A[i][j] for j in range(k))
                for i in range(k)))>0 for k in range(1,len(A)+1))


@dataclass(frozen=True)
class FiniteMealy:
    """Complete causal action representation, NOT an authenticated physical system."""
    actions: tuple[str,...]
    output: tuple[tuple[int,...],...]
    next_state: tuple[tuple[int,...],...]

    def __post_init__(self):
        if not self.actions or len(set(self.actions))!=len(self.actions) or any(
            type(a) is not str or not a for a in self.actions):
            raise RepairError("Distinct nonempty action names required")
        if len(self.output)!=len(self.actions) or len(self.next_state)!=len(self.actions):
            raise RepairError("One complete table per action required")
        n=len(self.output[0])
        if n<1 or n>64 or any(len(row)!=n for row in self.output+self.next_state):
            raise RepairError("Consistent bounded finite carrier required")
        if any(type(x) is not int for row in self.output for x in row) or any(
            type(x) is not int or not 0<=x<n for row in self.next_state for x in row):
            raise RepairError("Source outputs and transitions must be integer-addressed")

    @property
    def count(self):return len(self.output[0])

    def observe(self,state:int,word:Sequence[str]):
        if type(state) is not int or not 0<=state<self.count:
            raise RepairError("Unknown original carrier state")
        out=[];current=state
        for action in word:
            if action not in self.actions:raise RepairError("Action unavailable")
            a=self.actions.index(action)
            out.append(self.output[a][current])
            current=self.next_state[a][current]
        return tuple(out)


@dataclass(frozen=True)
class BehaviorQuotient:
    """The *coarsest* output-respecting transition congruence."""
    blocks: tuple[tuple[int,...],...]
    action_outputs: tuple[tuple[int,...],...]
    action_transitions: tuple[tuple[int,...],...]
    refinement_steps: int
    source_state_count: int

    def block_of(self,state:int):
        if type(state) is not int or not 0<=state<self.source_state_count:
            raise RepairError("Unknown state")
        return next(i for i,block in enumerate(self.blocks) if state in block)

    def quotient_machine(self):
        return FiniteMealy(tuple(f"a{i}" for i in range(len(self.action_outputs))),
                           self.action_outputs,self.action_transitions)

    def factors_claim(self,values:Sequence[object]):
        if len(values)!=self.source_state_count:raise RepairError("Claim domain mismatch")
        for block in self.blocks:
            for state in block[1:]:
                if values[state]!=values[block[0]]:
                    return {"proved":False,"obstruction":(block[0],state),
                            "cannot_decide_original_source_claim":True}
        return {"proved":True,"decoder":tuple(values[b[0]] for b in self.blocks)}


def minimal_behavioral_quotient(machine:FiniteMealy):
    """Partition refinement computes the final congruence (classical Moore/Myhill-Nerode)."""
    if not isinstance(machine,FiniteMealy):raise RepairError("Finite lawful machine required")
    n=machine.count
    partition=(tuple(range(n)),)
    steps=0
    while True:
        cls={s:i for i,b in enumerate(partition) for s in b}
        nxt={}
        for s in range(n):
            signature=(cls[s],)+tuple((machine.output[a][s],cls[machine.next_state[a][s]])
                            for a in range(len(machine.actions)))
            nxt.setdefault(signature,[]).append(s)
        new=tuple(sorted((tuple(v) for v in nxt.values()),key=lambda g:g[0]))
        if new==partition:break
        if len(new)<=len(partition):
            raise ArithmeticError("Refinement did not strictly increase the partition")
        steps+=1
        partition=new
    lookup={s:i for i,b in enumerate(partition) for s in b}
    output=tuple(tuple(machine.output[a][b[0]] for b in partition)
                 for a in range(len(machine.actions)))
    transition=tuple(tuple(lookup[machine.next_state[a][b[0]]] for b in partition)
                     for a in range(len(machine.actions)))
    for a in range(len(machine.actions)):
        for i,b in enumerate(partition):
            for s in b:
                if machine.output[a][s]!=output[a][i] or lookup[machine.next_state[a][s]]!=transition[a][i]:
                    raise ArithmeticError("Quotient not a valid action/observation functor")
    return BehaviorQuotient(partition,output,transition,steps,n)


def universal_observer_factor(machine:FiniteMealy,proposed_classes:Sequence[int]):
    """Universal map from ANY source-correct quotient onto the minimal behavior quotient.

    A proposed lawful quotient may preserve more internal states than necessary.
    The unique map to the final behavioral quotient must commute with each
    generator and preserve action outputs, hence every composable action word.
    """
    defect=proposed_quotient_defect(machine,proposed_classes)
    if not defect["commutes"]:return defect
    minimal=minimal_behavioral_quotient(machine)
    cls=tuple(proposed_classes)
    labels=tuple(sorted(set(cls)))
    h=[]
    for label in labels:
        source=next(i for i,c in enumerate(cls) if c==label)
        dest=minimal.block_of(source)
        if any(minimal.block_of(i)!=dest for i,c in enumerate(cls) if c==label):
            raise ArithmeticError("Claimed behavioral terminal object contradicted")
        h.append(dest)
    return {"commutes":True,"universal_factor":tuple(zip(labels,h)),
            "minimal_blocks":minimal.blocks,
            "all_generated_action_words_preserved":True,
            "scope":"finite deterministic Mealy generator proof, no physical attestation"}


def shortest_distinguishing_word(machine:FiniteMealy,x:int,y:int):
    """Construct the SHORTEST actual future word separating two states, or return None."""
    from collections import deque
    if x==y:return None
    if any(type(s) is not int or not 0<=s<machine.count for s in (x,y)):
        raise RepairError("Unknown states")
    q=deque([(x,y,())]);seen={(x,y)}
    while q:
        i,j,word=q.popleft()
        for a,name in enumerate(machine.actions):
            w=word+(name,)
            if machine.output[a][i]!=machine.output[a][j]:return w
            pair=(machine.next_state[a][i],machine.next_state[a][j])
            if pair not in seen:seen.add(pair);q.append((pair[0],pair[1],w))
    return None


def proposed_quotient_defect(machine:FiniteMealy,classes:Sequence[int]):
    """Given a proposed quotient mapping, return concrete covariance/output failure."""
    classes=tuple(classes)
    if len(classes)!=machine.count or any(type(x) is not int or x<0 for x in classes):
        raise RepairError("One typed block label per original source state required")
    for i in range(machine.count):
        for j in range(i+1,machine.count):
            if classes[i]!=classes[j]:continue
            for a,name in enumerate(machine.actions):
                if machine.output[a][i]!=machine.output[a][j]:
                    return {"commutes":False,"states":(i,j),"action":name,
                            "failure":"OBSERVATION_NOT_FACTORED"}
                if classes[machine.next_state[a][i]]!=classes[machine.next_state[a][j]]:
                    return {"commutes":False,"states":(i,j),"action":name,
                            "failure":"TRANSITION_NOT_FACTORED"}
    return {"commutes":True,"source_relation_is_congruence":True}


@dataclass(frozen=True)
class StieltjesLaw:
    """Exact positive finite spectral measure: h(s)=sum_j w_j/(s+lambda_j)."""
    poles: tuple[Q,...]
    weights: tuple[Q,...]

    def __post_init__(self):
        if not self.poles or len(self.poles)!=len(self.weights):
            raise RepairError("Nonempty matched poles/weights")
        poles=qtuple(self.poles);weights=qtuple(self.weights)
        if any(x<=0 for x in poles+weights) or len(set(poles))!=len(poles):
            raise RepairError("Distinct positive relaxation rates and positive weights")
        object.__setattr__(self,"poles",poles)
        object.__setattr__(self,"weights",weights)

    @property
    def degree(self):return len(self.poles)

    def response(self,s):
        s=F(s)
        if s<0:raise RepairError("Admissible Laplace s >= 0 only")
        return sum((w/(s+p) for p,w in zip(self.poles,self.weights)),Q(0))

    def moment(self,k):
        if type(k) is not int or not 0<=k<=64:raise RepairError("Bounded moment index")
        return sum((w*p**k for p,w in zip(self.poles,self.weights)),Q(0))


@dataclass(frozen=True)
class FinitePassiveAlias:
    probe_points: tuple[Q,...]
    lower: StieltjesLaw
    higher: StieltjesLaw
    first_holdout: Q
    holdout_residual: Q
    residue_identity: tuple[Q,...]
    extra_calibrations: tuple[Q,...]


def positive_passive_alias(samples:Sequence[object],*,pole_start=1,static_target=Q(1,10)):
    """EXACT alternating-residue counterexample for ANY fixed finite sample set.

    For m distinct s_i>=0 and m+1 distinct positive lambda_j, the rational
    R(s)=prod_i(s-s_i)/prod_j(s+lambda_j) has alternating partial-fraction
    residues, split into two strictly positive Stieltjes sums. They agree
    at every s_i but have different modal degrees (for even m>=2).
    """
    ss=qtuple(samples)
    if len(ss)<1 or len(ss)>12 or len(set(ss))!=len(ss) or min(ss)<0:
        raise RepairError("1..12 distinct nonnegative rational probes")
    extra=[];effective=list(ss)
    if Q(0) not in effective:
        extra.append(Q(0));effective.append(Q(0))
    if len(effective)%2:
        unused=next(Q(i) for i in range(1,100) if Q(i) not in effective)
        extra.append(unused);effective.append(unused)
    effective=tuple(effective)
    if type(pole_start) is not int or pole_start<=0:
        raise RepairError("Positive integer starting pole")
    target=F(static_target)
    if target<=0:
        raise RepairError("Positive desired static DC response")
    poles=tuple(Q(pole_start+i) for i in range(len(effective)+1))
    residues=[]
    for j,l in enumerate(poles):
        numerator=Q(1)
        for s in effective:numerator*=(-l-s)
        denominator=Q(1)
        for k,p in enumerate(poles):
            if k!=j:denominator*=p-l
        residues.append(numerator/denominator)
    plus=[(p,c) for p,c in zip(poles,residues) if c>0]
    minus=[(p,-c) for p,c in zip(poles,residues) if c<0]
    if not plus or not minus:raise ArithmeticError("Residue alternation failed")
    unscaled=StieltjesLaw(tuple(p for p,_ in plus),tuple(w for _,w in plus))
    if unscaled.response(0)<=0:raise ArithmeticError("Incorrect passive normalization")
    scale=target/unscaled.response(0)
    pos=StieltjesLaw(tuple(p for p,_ in plus),tuple(w*scale for _,w in plus))
    neg=StieltjesLaw(tuple(p for p,_ in minus),tuple(w*scale for _,w in minus))
    if any(pos.response(s)!=neg.response(s) for s in effective):
        raise ArithmeticError("Source interpolation not exact")
    if pos.response(0)!=target or neg.response(0)!=target:
        raise ArithmeticError("Static response normalization broken")
    if pos.degree<=neg.degree:lower,higher=pos,neg
    else:lower,higher=neg,pos
    hold=next(Q(i) for i in range(1,100) if Q(i) not in effective)
    delta=pos.response(hold)-neg.response(hold)
    if not delta:raise ArithmeticError("False invisible holdout")
    return FinitePassiveAlias(ss,lower,higher,hold,delta,tuple(residues),tuple(extra))


@dataclass(frozen=True)
class MinimalLinearMemory:
    """Moment-compatible realization, not global uniqueness without a rank bound."""
    dimension: int
    H: tuple[tuple[Q,...],...]
    H_shift: tuple[tuple[Q,...],...]
    generator: tuple[tuple[Q,...],...]
    initial: tuple[Q,...]
    output: tuple[Q,...]
    checked_moments: int

    def moment(self,k:int):
        if type(k) is not int or not 0<=k<=200:raise RepairError("Finite query index 0..200")
        v=self.initial
        for _ in range(k):v=matvec(self.generator,v)
        return sum((a*b for a,b in zip(self.output,v)),Q(0))

    def response(self,s):
        s=F(s)
        if s<0:raise RepairError("Positive real Laplace parameter required")
        M=tuple(tuple(self.generator[i][j]+(s if i==j else 0)
                      for j in range(self.dimension)) for i in range(self.dimension))
        v=matvec(invert(M),self.initial)
        return sum((a*b for a,b in zip(self.output,v)),Q(0))

    def basis_change(self,T):
        """Return proof-transported (A',b',c') and source-check all moments.

        Set x'=T x. Then A'=T A T^-1, b'=T b, c'=c T^-1.
        This is a true naturality/representation similarity certificate,
        not an assertion that the original state coordinates are observable.
        """
        T=tuple(tuple(F(x) for x in row) for row in T)
        if len(T)!=self.dimension or any(len(row)!=self.dimension for row in T):
            raise RepairError("Full dimension preserving basis map needed")
        Ti=invert(T)
        A=product(product(T,self.generator),Ti)
        b=matvec(T,self.initial)
        c=tuple(sum((self.output[k]*Ti[k][j] for k in range(self.dimension)),Q(0))
                for j in range(self.dimension))
        curr=b
        for k in range(self.checked_moments):
            v=sum((a*x for a,x in zip(c,curr)),Q(0))
            if v!=self.moment(k):raise ArithmeticError("Noncommuting proof-basis transform")
            curr=matvec(A,curr)
        return {"generator":A,"initial":b,"output":c,
                "representation_preserves_all_words_by_similarity":True,
                "finite_cross_check_count":self.checked_moments}


def hankel_memory_repair(moments:Sequence[object],*,max_modes=6):
    """Discover the minimum r fitting supplied moments, with exact SPD gates.

    The unique minimal realization statement holds for an INFINITE rational
    sequence of Hankel rank r or a separately certified r-mode source law.
    Finite data here only give a candidate and conditional degree lower bound.
    """
    m=qtuple(moments)
    if len(m)<3 or len(m)>40 or type(max_modes) is not int or not 1<=max_modes<=6:
        raise RepairError("3..40 exact moments and finite modal-search bound required")
    for r in range(1,min(max_modes,(len(m)-1)//2)+1):
        H=tuple(tuple(m[i+j] for j in range(r)) for i in range(r))
        H1=tuple(tuple(m[i+j+1] for j in range(r)) for i in range(r))
        if not positive_definite(H) or not positive_definite(H1):continue
        A=product(invert(H),H1)
        b=(Q(1),)+(Q(0),)*(r-1)
        c=H[0]
        proposal=MinimalLinearMemory(r,H,H1,A,b,c,len(m))
        if all(proposal.moment(k)==m[k] for k in range(len(m))):
            return proposal
    raise RepairError("No strictly passive linear candidate fits every supplied moment")


@dataclass(frozen=True)
class DiscoveredBoundaryLaw:
    """A family-relative fitted boundary law, without an assumed interior graph."""
    arms: tuple[Q,Q,Q]
    alpha: Q
    beta: Q
    gamma: Q
    source_id: str
    epoch: int
    basis_id: str
    linear_memory: MinimalLinearMemory
    failed_repairs: tuple[tuple[str,str],...]

    def h(self,s):
        s=F(s)
        numerator=1+self.gamma*s
        denominator=sum(self.arms,Q(0))+(sum(self.arms,Q(0))*self.gamma+self.alpha)*s+self.beta*s*s
        if denominator<=0 or numerator<=0:raise RepairError("Laplace report not positive")
        return numerator/denominator

    def response(self,s):
        h=self.h(s);g=self.arms
        return tuple(tuple((g[i] if i==j else Q(0))-g[i]*g[j]*h
                           for j in range(3)) for i in range(3))


def _first_matrix_mismatch(A,B):
    return next(((i,j,A[i][j],B[i][j]) for i in range(len(A)) for j in range(len(A[i]))
                 if A[i][j]!=B[i][j]),None)


def _moments_from_reciprocal(G,alpha,beta,gamma,count):
    """h(1/z)=z*(gamma+z)/(beta+(G*gamma+alpha)z+G*z²)."""
    if beta==0:raise RepairError("Second-order recurrence has zero leading coefficient")
    a=[]
    for k in range(count):
        numerator=(gamma if k==0 else Q(1) if k==1 else Q(0))
        if k>=1:numerator-=(G*gamma+alpha)*a[k-1]
        if k>=2:numerator-=G*a[k-2]
        a.append(numerator/beta)
    return tuple(((-1)**k)*v for k,v in enumerate(a))


def discover_boundary_memory(reports:Sequence[object],*,holdouts=(),max_modes=2):
    """Automatically find a rational *law category* from 4 exact source reports.

    Search ladder: static -> local terminal memory -> 1-pole rational law ->
    2-pole rational linear-memory representation. No internal circuit template
    is supplied; a declared order cap remains a model-class assumption.
    """
    from .dynamic_boundary_inverse import BoundaryReceipt,reconstruct_y_triangle,scalar_h_from_response
    r=tuple(reports)
    if len(r)!=4 or any(not isinstance(v,BoundaryReceipt) for v in r):
        raise RepairError("E requires four independent exact boundary receipts")
    sig={(v.source_id,v.source_epoch,v.basis_id) for v in r}
    if len(sig)!=1 or any(not v.observer for v in r):
        raise RepairError("Mixed original source, epoch, basis or observer")
    if tuple(v.laplace_s for v in r)!=(Q(0),Q(1),Q(2),Q(3)):
        raise RepairError("E's four exact sample times must be 0,1,2,3")
    g=tuple(reconstruct_y_triangle(r[0].response)["arms"])
    G=sum(g,Q(0))
    hs=[]
    for v in r:
        h=scalar_h_from_response(v.response,g)
        if h<=0:raise RepairError("Nonpositive boundary transfer")
        expected=tuple(tuple((g[i] if i==j else Q(0))-g[i]*g[j]*h
                             for j in range(3)) for i in range(3))
        if v.response!=expected:raise RepairError("Boundary matrix is not the declared rank-one source law")
        hs.append(h)
    failed=[]
    if all(v.response==r[0].response for v in r):
        raise RepairError("No dynamic evidence: missing memory category NOT forced")
    i,j,actual,static=_first_matrix_mismatch(r[1].response,r[0].response)
    failed.append(("STATIC_MEMORYLESS",f"s=1,({i},{j}):{actual}!={static}"))
    # Adding ONLY diagonal capacitors at external ports cannot alter cross-port coupling.
    cross=next(((i,j) for i in range(3) for j in range(i+1,3)
                if any(v.response[i][j]!=r[0].response[i][j] for v in r[1:])),None)
    if cross is None:raise RepairError("No nonlocal memory defect: class upgrade unjustified")
    failed.append(("TERMINAL_LOCAL_STORAGE",f"cross-port {cross} changes dynamically"))
    q=tuple(1/h for h in hs)
    if q[0]!=G:raise RepairError("DC source does not match reconstructed star signature")
    cap=q[1]-G
    if cap<=0:raise RepairError("No passive single-pole source law at first positive probe")
    wrong=q[0]+Q(2)*cap
    if wrong==q[2]:
        raise RepairError("Observed 2nd-step curvature does not yet force higher order")
    failed.append(("ONE_RELAXATION_MODE",f"q(2)={q[2]} != {wrong}"))
    # Blind degree-(2,1) reciprocal rational interpolation; not a serial topology.
    equations=tuple((Q(s),Q(s*s),-Q(s)*(q[s]-G)) for s in (1,2,3))
    inverse=invert(equations)
    alpha,beta,gamma=matvec(inverse,tuple(q[s]-G for s in (1,2,3)))
    if beta<=0 or gamma<=0 or alpha<=0:
        raise RepairError("Rational candidate violates declared positive-degree gates")
    moments=_moments_from_reciprocal(G,alpha,beta,gamma,8)
    minimum=hankel_memory_repair(moments,max_modes=max_modes)
    if minimum.dimension!=2:
        raise RepairError("Evidence did not justify a genuine 2-mode candidate")
    model=DiscoveredBoundaryLaw(g,alpha,beta,gamma,*next(iter(sig)),minimum,tuple(failed))
    for v in r:
        if model.response(v.laplace_s)!=v.response:
            raise ArithmeticError("Repaired model fails its original measurements")
    if any(model.h(s)!=minimum.response(s) for s in (0,1,2,3,4,11)):
        raise ArithmeticError("Independent minimal realization mismatches rational fit")
    for v in tuple(holdouts):
        if not isinstance(v,BoundaryReceipt) or (v.source_id,v.source_epoch,v.basis_id) not in sig:
            raise RepairError("Holdout source epoch/basis incompatible")
        if model.response(v.laplace_s)!=v.response:
            raise RepairError("Model's unseen held-out boundary prediction FALSIFIED")
    return model


def categorical_repair_demo():
    """Use opaque measurements, independently check held-out source laws."""
    from .dynamic_boundary_inverse import serial_pendant,observe
    source=serial_pendant()
    reports=tuple(observe(source,s,observer=f"tower{s}") for s in (0,1,2,3))
    held=tuple(observe(source,s,observer=f"holdout{s}") for s in (4,11,17))
    model=discover_boundary_memory(reports,holdouts=held)
    alias=positive_passive_alias((0,1,2,3))
    machine=FiniteMealy(("look","read"), ((0,0,0,0),(0,0,1,1)),
                         ((1,2,3,3),(0,1,2,3)))
    q=minimal_behavioral_quotient(machine)
    return {
       "status":"SOURCE_RELATIVE_CATEGORY_GENERATED_MEMORY_REPAIR_EXACT",
       "original_source_hidden_from_inverse":True,
       "discovered_model_category":"POSITIVE_LINEAR_MEMORY",
       "mode_dimension":model.linear_memory.dimension,
       "static_conductances":model.arms,
       "rational_reciprocal_coefficients":(model.alpha,model.beta,model.gamma),
       "discovered_memory_generator":model.linear_memory.generator,
       "observed_hankel_determinant":determinant(model.linear_memory.H),
       "failed_categories":model.failed_repairs,
       "independent_holdouts_confirmed":(4,11,17),
       "all_frequency_physical_ontology_unique":False,
       "finite_passive_alias_probe_points":alias.probe_points,
       "finite_passive_alias_modal_degrees":(alias.lower.degree,alias.higher.degree),
       "finite_passive_alias_holdout":alias.first_holdout,
       "finite_passive_alias_holdout_difference":alias.holdout_residual,
       "behavioral_minimal_classes":q.blocks,
       "smallest_delayed_separator":shortest_distinguishing_word(machine,0,1),
       "source_physically_authenticated":False,
       "RH_or_Weil_positivity_proved":False,
    }
