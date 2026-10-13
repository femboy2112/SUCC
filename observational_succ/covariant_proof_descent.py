"""Covariant proof-support transport for original-source claims (finite exact).

Theorems are classical fiber factorization, group-action orbit invariance,
and finite-set Beck--Chevalley. Lorentz covariance and ontological / physical
measurement authority are SEPARATE obligations, never inferred from strings.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Sequence


class DescentError(ValueError):
    pass


@dataclass(frozen=True)
class OriginalSourceSquare:
    """C before/current after and observations. All source addresses are concrete.

    F is the carrier intervention C -> C, O_before and O_after are reports,
    and R is the explicit representation transport on BEFORE output labels.
    Proof of an ORIGINAL-source claim is tested through O_after o F, never
    through the hidden simulator's initial-source labels as receiver input.
    """
    source_id: str
    carrier_map: tuple[int,...]
    old_report: tuple[Hashable,...]
    new_report: tuple[Hashable,...]
    original_claim: tuple[Hashable,...]
    report_map: tuple[tuple[Hashable,Hashable],...] = ()
    post_claim: tuple[Hashable,...] | None = None

    def __post_init__(self):
        n=len(self.carrier_map)
        if (not self.source_id or n<1 or any(type(x) is not int or not 0<=x<n for x in self.carrier_map)
                or len(self.old_report)!=n or len(self.new_report)!=n
                or len(self.original_claim)!=n or (self.post_claim is not None
                and len(self.post_claim)!=n)):
            raise DescentError("Declare one finite original/current carrier and target")
        if len(set(a for a,b in self.report_map))!=len(self.report_map):
            raise DescentError("Representation transport is not a function")
        for row in (self.old_report,self.new_report,self.original_claim,
                    self.post_claim or (), (a for a,b in self.report_map),
                    (b for a,b in self.report_map)):
            for value in row:hash(value)

    def observation_square(self)->dict:
        R=dict(self.report_map)
        for x,(u,ob) in enumerate(zip(self.carrier_map,self.old_report)):
            if ob not in R or R[ob]!=self.new_report[u]:
                return {"commutes":False,"source_witness":x,
                        "old_report":ob,"actual_updated_report":self.new_report[u],
                        "transported_report":R.get(ob)}
        return {"commutes":True,"source_witness":None}

    def original_claim_square(self)->dict:
        if self.post_claim is None:
            seen={}
            for x,j in enumerate(self.carrier_map):
                if j in seen and seen[j][1]!=self.original_claim[x]:
                    return {"preserved":False,"source_witness":(seen[j][0],x),
                            "reason":"no current-carrier original-claim interpretation"}
                seen[j]=(x,self.original_claim[x])
            return {"preserved":True,"poststate_values":tuple((j,v) for j,(_,v) in sorted(seen.items()))}
        for x,j in enumerate(self.carrier_map):
            if self.original_claim[x]!=self.post_claim[j]:
                return {"preserved":False,"source_witness":x,
                        "reason":"declared original/post target square does not commute"}
        return {"preserved":True,"poststate_values":None}

    def decoder(self)->dict:
        """Target t factors via AFTER physical observation iff fiber containment.

        This may succeed without observation covariance, or fail although
        observation covariance holds. No inferred authenticity of the model.
        """
        seen={}
        for x,j in enumerate(self.carrier_map):
            report=self.new_report[j]
            value=self.original_claim[x]
            if report in seen and seen[report][1]!=value:
                return {"factors":False,"collision":(seen[report][0],x),
                        "report":report,"targets":(seen[report][1],value),
                        "decoder":None}
            seen[report]=(x,value)
        return {"factors":True,"collision":None,"decoder":tuple((r,v) for r,(_,v) in seen.items())}


def permutation_apply(g:tuple[int,...],x:int)->int:
    return g[x]


def permutation_inverse(g:tuple[int,...])->tuple[int,...]:
    if set(g)!=set(range(len(g))):raise DescentError("An observation frame needs a bijection")
    result=[0]*len(g)
    for i,x in enumerate(g):result[x]=i
    return tuple(result)


def permutation_compose(a:tuple[int,...],b:tuple[int,...])->tuple[int,...]:
    """Product a o b, i.e. apply b followed by a."""
    if len(a)!=len(b) or set(a)!=set(range(len(a))) or set(b)!=set(range(len(b))):
        raise DescentError("Finite common-carrier permutation group required")
    return tuple(a[b[i]] for i in range(len(a)))


@dataclass(frozen=True)
class FrameHolonomy:
    """Group of reversible epistemic frame changes, NOT Lorentz by default."""
    source_id: str
    generators: tuple[tuple[str,tuple[int,...]],...]
    claim: tuple[Hashable,...]

    def __post_init__(self):
        n=len(self.claim)
        if not self.source_id or not n or not self.generators:
            raise DescentError("Source, finite target and generators required")
        if len({name for name,_ in self.generators})!=len(self.generators):
            raise DescentError("Unique frame generator names required")
        for name,g in self.generators:
            if not name or len(g)!=n or set(g)!=set(range(n)):
                raise DescentError("All frame arrows must act invertibly on common carrier")

    def transport(self,path:Sequence[str])->tuple[int,...]:
        table={name:g for name,g in self.generators}
        state=tuple(range(len(self.claim)))
        for symbol in path:
            if symbol.startswith("-"):
                key=symbol[1:]
                if key not in table:raise DescentError("Unknown inverse path generator")
                step=permutation_inverse(table[key])
            else:
                if symbol not in table:raise DescentError("Unknown path generator")
                step=table[symbol]
            state=permutation_compose(step,state)
        return state

    def certificate(self)->dict:
        """Claim descends to orbit quotient iff invariant under ALL generators.

        Tests generators, not factorially many words. Their finite inverses
        preserve any invariant automatically. A failure returns a two-source
        witness with different original target, NOT physical frame curvature.
        """
        for name,g in self.generators:
            for i,j in enumerate(g):
                if self.claim[i]!=self.claim[j]:
                    return {"invariant":False,"generator":name,
                            "source_witness":(i,j),"different_claim_values":(self.claim[i],self.claim[j]),
                            "orbit_partition":None}
        n=len(self.claim)
        seen=set();orbits=[]
        steps=[g for _,g in self.generators]
        steps+=[permutation_inverse(g) for g in steps]
        for i in range(n):
            if i in seen:continue
            stack=[i];seen.add(i);orbit=[]
            while stack:
                x=stack.pop();orbit.append(x)
                for g in steps:
                    y=g[x]
                    if y not in seen:seen.add(y);stack.append(y)
            orbits.append(tuple(sorted(orbit)))
        return {"invariant":True,"orbit_partition":tuple(sorted(orbits)),
                "source_witness":None,"generator":None}


def bit_shears()->FrameHolonomy:
    """GL2(F2): two noncommuting changes of semantic/source coordinates.

    Zero-vs-nonzero is frame-invariant, first bit and XOR are not.
    """
    A=tuple(2*(x//2) + ((x//2) ^ (x%2)) for x in range(4))
    B=tuple(2*((x//2) ^ (x%2)) + (x%2) for x in range(4))
    return FrameHolonomy("source-F2-two-vector",(("A",A),("B",B)),
                         ("zero","nonzero","nonzero","nonzero"))


@dataclass(frozen=True)
class FiniteBeckChevalley:
    """Test the finite SET base-change identity for ∃ across a cospan.

      X --f--> Z <--g-- Y, with declared relation W subset X x Y.
    If W is the actual pullback, then g^* f_! S = q_! p^* S for all S.
    A mere commuting relation W -> X,Y can be proper: then BC can FAIL.
    """
    f: tuple[int,...]
    g: tuple[int,...]
    base_size: int
    relation: tuple[tuple[int,int],...]

    def __post_init__(self):
        if (type(self.base_size) is not int or self.base_size<1 or not self.f or not self.g
            or any(type(z) is not int or not 0<=z<self.base_size for z in self.f+self.g)
            or len(set(self.relation))!=len(self.relation)):
            raise DescentError("Valid finite cospan and relation required")
        for x,y in self.relation:
            if (type(x) is not int or not 0<=x<len(self.f) or type(y) is not int
                    or not 0<=y<len(self.g) or self.f[x]!=self.g[y]):
                raise DescentError("Relation must form a commuting square")

    def audit(self)->dict:
        allowed=set(self.relation)
        pullback={(i,j) for i,x in enumerate(self.f) for j,y in enumerate(self.g) if x==y}
        missing=tuple(sorted(pullback-allowed))
        # For singleton S={i}, missing (i,j) is a direct BC counterexample.
        if missing:
            x,y=missing[0]
            return {"pullback":False,"beck_chevalley_for_all_predicates":False,
                    "source_witness":x,"target_witness":y,
                    "predicate":(x,),"missing_witness":(x,y)}
        return {"pullback":True,"beck_chevalley_for_all_predicates":True,
                "source_witness":None,"missing_witness":None}

    def for_predicate(self,S:tuple[int,...])->dict:
        if any(type(i) is not int or not 0<=i<len(self.f) for i in S):
            raise DescentError("Predicate outside source set")
        s=set(S)
        left=frozenset(y for y in range(len(self.g)) if self.g[y] in {self.f[x] for x in s})
        right=frozenset(y for x,y in self.relation if x in s)
        return {"equal":left==right,"g_star_f_image":tuple(sorted(left)),
                "q_image_p_star":tuple(sorted(right))}


def covariant_proof_demo()->dict:
    h=bit_shears()
    cert=h.certificate()
    a=h.transport(("A","B"));b=h.transport(("B","A"))
    if a==b or not cert["invariant"]:raise AssertionError("Broken noncommuting calibration")
    fail=FrameHolonomy(h.source_id,h.generators,("0","1","0","1")).certificate()
    if fail["invariant"]:raise AssertionError("Wrong parity invariance")
    full=FiniteBeckChevalley((0,1),(0,1),2,((0,0),(1,1)))
    missing=FiniteBeckChevalley((0,1),(0,1),2,((0,0),))
    if not full.audit()["pullback"] or missing.audit()["pullback"]:raise AssertionError
    return {"frame_holonomy_noncommutes":True,
            "zero_claim_invariant":cert["invariant"],
            "parity_claim_invariant":fail["invariant"],
            "orbit_partition":cert["orbit_partition"],
            "complete_pullback_base_change":full.audit()["beck_chevalley_for_all_predicates"],
            "commuting_but_incomplete_square_rejected":not missing.audit()["pullback"],
            "carrier_traces_physically_authenticated":False}
