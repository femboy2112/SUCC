"""Operational Yoneda, finite belief-continuation descent and proof-policy transfer.

Three theorem levels are deliberately SEPARATE:
1. The classical Yoneda embedding of an actually composed finite path category.
   Restricting its context category can collapse distinct observation histories.
2. Source- and target-preserving coalgebra morphisms of finite deterministic
   instruments induce equality of all lawful outcome trees and transport
   optimal finite adaptive original-source proof policies.
3. Target-labeled belief-continuation bisimulation (with public action/outcome
   signatures) preserves the least fixed-point WINNING RANK of finite games.

The original physical source and claim table are DECLARED. Source-id strings
and tests DO NOT authenticate external physical evidence. No quantum, RH or
physical omega computation is inferred.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from .adaptive_proof_policy import (
    _belief, _options, _terminal, conditional_source_field,
    solve_adaptive_claim,
)
from .noncommuting_proof_transport import (
    FiniteCarrier, Instrument, SourceTransportError, _sources, _bit_field,
)
from .yoneda import (
    Arrow, validate_yoneda, representable_natural_transform,
)
from .core import BudgetExceeded, DomainError


class DescentError(ValueError):
    """A source/claim/action transport boundary is not certified."""


Belief = tuple[tuple[int,int], ...]


@dataclass(frozen=True)
class BeliefGame:
    field: FiniteCarrier
    sources: tuple[int, ...]
    target: tuple[str, ...]
    target_id: str
    nodes: tuple[Belief, ...]
    edges: tuple[tuple[tuple[str, tuple[tuple[int, Belief], ...]], ...], ...]
    goals: tuple[str | None, ...]
    root: Belief

    @classmethod
    def build(cls, field: FiniteCarrier, sources: tuple[int, ...],
              target: tuple[str, ...], *, target_id: str,
              max_nodes: int = 4096) -> "BeliefGame":
        _sources(field, sources)
        if (type(target) is not tuple or len(target) != field.count
                or any(type(x) is not str for x in target)
                or not isinstance(target_id, str) or not target_id
                or type(max_nodes) is not int or not 1<=max_nodes<=100000):
            raise DescentError("Declare exact finite original-source claim and budget")
        root = _belief((s,s) for s in sources)
        nodes = [root]
        seen = {root}
        edge_map = {}
        k = 0
        while k < len(nodes):
            b = nodes[k]
            k+=1
            opts = _options(field,b)
            edge_map[b] = tuple(sorted(opts.items()))
            for branches in opts.values():
                for _, next_b in branches:
                    if next_b not in seen:
                        if len(seen)>=max_nodes:
                            raise BudgetExceeded("Finite belief closure exhausted")
                        seen.add(next_b)
                        nodes.append(next_b)
        return cls(field,sources,target,target_id,tuple(nodes),
                   tuple(edge_map[b] for b in nodes),
                   tuple(_terminal(b,target) for b in nodes),root)

    def options(self, b: Belief) -> dict[str,tuple[tuple[int,Belief],...]]:
        try:
            i=self.nodes.index(b)
        except ValueError:
            raise DescentError("Belief absent from lawful source-reachable closure")
        return dict(self.edges[i])

    def goal(self,b:Belief) -> str|None:
        try:return self.goals[self.nodes.index(b)]
        except ValueError:raise DescentError("Unknown goal context")

    def rank(self)->int|None:
        """Independent root check against the existing certified policy solver."""
        return solve_adaptive_claim(
            self.field,self.sources,self.target,target_id=self.target_id).rank


@dataclass(frozen=True)
class BisimulationVerdict:
    left: BeliefGame
    right: BeliefGame
    relation: tuple[tuple[Belief,Belief],...]
    deletions: int

    @property
    def roots_related(self) -> bool:
        return (self.left.root,self.right.root) in self.relation

    @property
    def ranks_equal_if_related(self) -> bool:
        """Finite winning rank follows by induction over the shared tree."""
        return self.roots_related and self.left.rank()==self.right.rank()

    def transfer_source_policy(self, right_source:int)->dict:
        """Use LEFT policy on RIGHT's actual report stream with virtual LEFT belief.

        This demonstrates BEHAVIORAL proof transfer. Without an independently
        verified source map it is not a certificate of physical identity.
        """
        if not self.roots_related:
            raise DescentError("Unrelated root beliefs cannot transfer policy")
        if right_source not in self.right.sources:
            raise DescentError("Source not in declared receiver class")
        policy=solve_adaptive_claim(
            self.left.field,self.left.sources,self.left.target,
            target_id=self.left.target_id)
        if not policy.winning:
            raise DescentError("Losing policy has no winning evidence to transfer")
        choices={b:name for b,name,_ in policy.policy}
        l_b,r_b=self.left.root,self.right.root
        current=right_source
        history=[]
        for _ in range(policy.rank+1):
            left_answer=self.left.goal(l_b)
            right_answer=self.right.goal(r_b)
            if (l_b,r_b) not in self.relation or left_answer!=right_answer:
                raise ArithmeticError("Transport relation/proof goal was lost")
            if left_answer is not None:
                if left_answer != self.right.target[right_source]:
                    raise ArithmeticError("Transport made a false receiver source claim")
                return {"claim":left_answer,"steps":len(history),
                        "history":tuple(history),
                        "abstract_source_identity_authenticated":False}
            if l_b not in choices:
                raise ArithmeticError("Winning abstract strategy lacks an action")
            name=choices[l_b]
            obs,new_current=self.right.field.action(name).step(current)
            left_branches=dict(self.left.options(l_b)[name])
            right_branches=dict(self.right.options(r_b)[name])
            if obs not in left_branches or obs not in right_branches:
                raise ArithmeticError("Matched public outcomes diverged")
            l_b,r_b=left_branches[obs],right_branches[obs]
            current=new_current
            history.append((name,obs))
        raise ArithmeticError("Transferred finite strategy never terminated")


def greatest_goal_bisimulation(left:BeliefGame,right:BeliefGame, *,
                              max_pairs:int=20000)->BisimulationVerdict:
    """Greatest target-labeled action/outcome bisimulation of reachable beliefs.

    A pair survives iff terminal original-source labels agree (including None),
    available action NAMES agree, outcome labels agree per action and children
    are again in the relation. The finite greatest fixed point is exact.
    """
    count=len(left.nodes)*len(right.nodes)
    if type(max_pairs) is not int or max_pairs<1 or count>max_pairs:
        raise BudgetExceeded("Bisimulation search pair budget exceeded")
    pairs={(a,b) for a in left.nodes for b in right.nodes
           if left.goal(a)==right.goal(b)}
    initial=len(pairs)
    while True:
        keep=set()
        for a,b in pairs:
            oa,ob=left.options(a),right.options(b)
            if set(oa)!=set(ob):
                continue
            valid=True
            for name in oa:
                ba,bb=dict(oa[name]),dict(ob[name])
                if set(ba)!=set(bb) or any(
                    (ba[o],bb[o]) not in pairs for o in ba):
                    valid=False;break
            if valid:keep.add((a,b))
        if keep==pairs:break
        pairs=keep
    return BisimulationVerdict(left,right,tuple(sorted(pairs)),
                               initial-len(pairs))


@dataclass(frozen=True)
class CertifiedSourceMorphism:
    """Declared map concrete -> abstract, source + carrier + action semantics.

    The common names of instruments and their public outcomes must be
    preserved, including state-dependent enabledness; h(s) and t pullbacks
    are checked on EVERY declared source and transition state.
    """
    concrete: FiniteCarrier
    abstract: FiniteCarrier
    source_concrete: tuple[int,...]
    source_abstract: tuple[int,...]
    h: tuple[int,...]
    t_concrete: tuple[str,...]
    t_abstract: tuple[str,...]
    target_id: str

    def verify(self)->dict:
        _sources(self.concrete,self.source_concrete)
        _sources(self.abstract,self.source_abstract)
        if (type(self.h) is not tuple or len(self.h)!=self.concrete.count or
                any(type(v) is not int or not 0<=v<self.abstract.count
                    for v in self.h)):
            raise DescentError("Invalid total source/carrier morphism h")
        if (tuple(sorted(set(self.h[s] for s in self.source_concrete)))
                !=self.source_abstract):
            raise DescentError("Abstraction must cover ALL compatible source worlds")
        if (not isinstance(self.target_id,str) or not self.target_id
                or len(self.t_concrete)!=self.concrete.count
                or len(self.t_abstract)!=self.abstract.count
                or any(type(x) is not str
                       for x in self.t_concrete+self.t_abstract)):
            raise DescentError("Declare source-indexed truth/target table")
        for s in self.source_concrete:
            if self.t_concrete[s]!=self.t_abstract[self.h[s]]:
                raise DescentError(
                    f"Source-claim square failed at original source {s}")
        actions_c={a.name:a for a in self.concrete.actions}
        actions_a={a.name:a for a in self.abstract.actions}
        if set(actions_c)!=set(actions_a):
            raise DescentError("Executable action languages do not agree")
        checks=0
        for q in range(self.concrete.count):
            projected=self.h[q]
            for name,a in actions_c.items():
                b=actions_a[name]
                if a.enabled[q]!=b.enabled[projected]:
                    raise DescentError(
                        f"Instrument availability changed at {q} for {name}")
                if a.enabled[q]:
                    if a.outputs[q]!=b.outputs[projected]:
                        raise DescentError(
                            f"Observable response changed at {q} for {name}")
                    if self.h[a.transitions[q]]!=b.transitions[projected]:
                        raise DescentError(
                            f"Source/carrier effect square failed at {q} for {name}")
                checks+=1
        return {
            "status":"EXACT_SOURCE_COALGEBRA_MORPHISM",
            "concrete_states":self.concrete.count,
            "abstract_states":self.abstract.count,
            "concrete_sources":len(self.source_concrete),
            "abstract_sources":len(self.source_abstract),
            "state_map_injective":len(set(self.h))==len(self.h),
            "source_image_surjective":True,
            "source_claim_pullback":True,
            "all_actions_and_outputs_compatible":True,
            "checked_action_state_squares":checks,
            "independent_physical_provenance_authenticated":False,
        }

    def policy_descent(self)->dict:
        declaration=self.verify()
        a=BeliefGame.build(self.abstract,self.source_abstract,
                            self.t_abstract,target_id=self.target_id)
        c=BeliefGame.build(self.concrete,self.source_concrete,
                            self.t_concrete,target_id=self.target_id)
        relation=greatest_goal_bisimulation(a,c)
        if not relation.roots_related:
            raise ArithmeticError("Valid coalgebra morphism failed game bisimulation")
        abstract_rank=a.rank()
        concrete_rank=c.rank()
        if abstract_rank!=concrete_rank:
            raise ArithmeticError("Source-preserving morphism changed proof rank")
        traces=[]
        if abstract_rank is not None:
            for s in self.source_concrete:
                tr=relation.transfer_source_policy(s)
                if tr["steps"]>abstract_rank:
                    raise ArithmeticError("Transported policy exceeded abstract rank")
                traces.append(tr["steps"])
        return {**declaration,
                "behavioral_bisimulation_roots_related":relation.roots_related,
                "optimal_original_source_rank_equal":True,
                "abstract_rank":abstract_rank,
                "concrete_rank":concrete_rank,
                "transported_source_replays":len(traces),
                "all_transferred_answers_correct":True,
                "claim_source_identity_is_declared_not_authenticated":True}


def duplicate_carrier(abstract:FiniteCarrier, target:tuple[str,...],
                      *,copies:int=2)->tuple[FiniteCarrier,tuple[int,...],tuple[str,...]]:
    """A nontrivial observation-invisible source representation refinement.

    Clone each carrier x into (x,t) with t=0..copies-1, preserve t under
    actions and report the same original abstract outputs. h(x,t)=x is
    noninjective, and no admissible instrument detects the private tag.
    """
    if type(copies) is not int or not 2<=copies<=4:
        raise DescentError("Require 2..4 independent representational copies")
    if type(target) is not tuple or len(target)!=abstract.count:
        raise DescentError("Target domain mismatch")
    h=tuple(x for x in range(abstract.count) for _ in range(copies))
    actions=[]
    for a in abstract.actions:
        actions.append(Instrument(
            a.name,
            tuple(a.outputs[x] for x in h),
            tuple(copies*a.transitions[x]+(q%copies)
                  for q,x in enumerate(h)),
            tuple(a.enabled[x] for x in h)))
    concrete=FiniteCarrier(
        len(h),tuple(actions),
        abstract.source_id+"-declared-representation-refinement",
        abstract.basis_id+"-with-hidden-tag")
    return concrete,h,tuple(target[x] for x in h)


class ObservationPathCategory:
    """Genuine finite FREE PATH CATEGORY of lawful bounded belief histories.

    Objects: source/claim indexed epistemic belief and remaining step budget.
    Arrow: one ordered public action/outcome edge, or a concatenated path.
    Hom-sets are actual composable evidence paths, not arbitrary output
    fingerprints. The classical Yoneda lemma applies to this small category.
    """
    def __init__(self,game:BeliefGame,horizon:int, *,
                 max_objects:int=96,max_paths:int=10000):
        if (type(horizon) is not int or not 0<=horizon<=5
                or type(max_objects) is not int or max_objects<1
                or type(max_paths) is not int or max_paths<1):
            raise DescentError("Bounded finite context/category required")
        self.game=game
        self.max_paths=max_paths
        root=(horizon,game.root)
        contexts=[root]
        ids={root:0}
        edges={}
        edge_labels={}
        token=1
        i=0
        while i<len(contexts):
            remaining,belief=contexts[i]
            edges[i]=[]
            if remaining:
                for name,branches in sorted(game.options(belief).items()):
                    for obs,new_b in branches:
                        new=(remaining-1,new_b)
                        if new not in ids:
                            if len(contexts)>=max_objects:
                                raise BudgetExceeded("Finite Yoneda context budget exceeded")
                            ids[new]=len(contexts)
                            contexts.append(new)
                        dest=ids[new]
                        edges[i].append((token,dest))
                        edge_labels[token]=(name,obs)
                        token+=1
            i+=1
        self.contexts=tuple(contexts)
        self.objects=tuple(range(len(contexts)))
        self.edges={k:tuple(v) for k,v in edges.items()}
        self.edge_labels=edge_labels
        self._hom_cache={}

    def _check(self,x):
        if type(x) is not int or x not in self.objects:
            raise DomainError("Context object outside actual belief category")

    def identity(self,x):
        self._check(x)
        return Arrow(x,x,())

    def hom(self,a,b):
        self._check(a);self._check(b)
        key=(a,b)
        if key in self._hom_cache:return self._hom_cache[key]
        arrows=[]
        if a==b:arrows.append(self.identity(a))
        def walk(here,word):
            for token,nxt in self.edges[here]:
                newword=word+(token,)
                if nxt==b:
                    arrows.append(Arrow(a,b,newword))
                    if len(arrows)>self.max_paths:
                        raise BudgetExceeded("Finite Yoneda hom budget exceeded")
                walk(nxt,newword)
        walk(a,())
        result=tuple(arrows)
        self._hom_cache[key]=result
        return result

    def compose(self,left,right):
        if (not isinstance(left,Arrow) or not isinstance(right,Arrow)
                or right.target!=left.source
                or left not in self.hom(left.source,left.target)
                or right not in self.hom(right.source,right.target)):
            raise DomainError("Invalid source/path/category composition")
        answer=Arrow(right.source,left.target,right.word+left.word)
        if answer not in self.hom(answer.source,answer.target):
            raise DomainError("Composite observation path is not executable")
        return answer

    def pretty_path(self,arrow:Arrow)->tuple[tuple[str,int],...]:
        if arrow not in self.hom(arrow.source,arrow.target):
            raise DomainError("Forged source-path proof")
        return tuple(self.edge_labels[t] for t in arrow.word)


def restricted_yoneda_arrow_detection(category:ObservationPathCategory,
                                      a:int,b:int,
                                      probes:tuple[int,...])->dict:
    """EXACT restricted representable FAITHFULNESS criterion at hom(a,b).

    y_J(f)=y_J(g) iff for every context j in J and every h:j->a,
    f∘h=g∘h. Full Yoneda includes j=a and h=id_a, so any distinct
    f,g are separated. A restricted family may lack any such lamp.
    Faithfulness on a hom-set is NOT the same as FULLNESS: restriction
    may also produce spurious natural transformations not induced by
    any actual arrow.
    """
    if (type(probes) is not tuple or len(probes)!=len(set(probes))
            or any(j not in category.objects for j in probes)):
        raise DomainError("Restricted contexts must be actual distinct objects")
    arrow_set=category.hom(a,b)
    pairs=0
    failed=[]
    certified=[]
    for i,f in enumerate(arrow_set):
        for g in arrow_set[i+1:]:
            pairs+=1
            lamp=None
            for j in probes:
                for h in category.hom(j,a):
                    if category.compose(f,h)!=category.compose(g,h):
                        lamp=(j,h.word)
                        break
                if lamp is not None:break
            if lamp is None:
                failed.append((f.word,g.word))
            else:
                certified.append((f.word,g.word,lamp))
    return {
        "source_hom_size":len(arrow_set),
        "distinct_arrow_pairs":pairs,
        "detected_pairs":len(certified),
        "undetected_pairs":tuple(failed),
        "faithful_on_selected_hom":not failed,
        "context_lamps":tuple(certified),
        "no_inference_of_fullness_or_physical_probe_availability":True,
    }


def least_faithful_context_family(category:ObservationPathCategory,
                                 a:int,b:int, *,
                                 max_subsets:int=30000)->dict:
    """Finite optimal hitting-set search for representable arrow detection.

    Not a minimum physical measurement cost. The contexts are objects
    already present in the freely generated observational category.
    Raises instead of declaring 'darkness' when the search budget fails.
    """
    from itertools import combinations
    if type(max_subsets) is not int or max_subsets<1:
        raise BudgetExceeded("Finite context search budget required")
    considered=0
    for n in range(len(category.objects)+1):
        for subset in combinations(category.objects,n):
            considered+=1
            if considered>max_subsets:
                raise BudgetExceeded("Finite context-set coverage not exhaustive")
            report=restricted_yoneda_arrow_detection(category,a,b,subset)
            if report["faithful_on_selected_hom"]:
                return {
                    "minimum_context_objects":subset,
                    "minimum_context_count":len(subset),
                    "subsets_checked":considered,
                    "arrow_pairs_detected":report["detected_pairs"],
                    "physical_probe_cost_minimized":False,
                }
    raise ArithmeticError("Full Yoneda context family unexpectedly nonfaithful")


def shallow_probe_agreement(left:FiniteCarrier,right:FiniteCarrier,
                            sources:tuple[int,...],horizon:int)->dict:
    """PROTOCOL-SCOPED fixed-word calibration, not a Yoneda embedding.

    Compare ordered public outcomes for every universally executable
    action word through depth h. Probes are identical named instruments;
    sources use the same externally DECLARED address chart. With different
    chart maps use CertifiedSourceMorphism instead of guessing identity.
    """
    if (type(horizon) is not int or not 0<=horizon<=5
            or set(a.name for a in left.actions)!=
               set(a.name for a in right.actions)):
        raise DescentError("Comparable named finite test languages required")
    _sources(left,sources);_sources(right,sources)
    alphabet=tuple(sorted(a.name for a in left.actions))
    checked=0
    for n in range(horizon+1):
        for word in product(alphabet,repeat=n):
            for source in sources:
                try:
                    l=left.run(source,word).observed_values
                except SourceTransportError:l=None
                try:
                    r=right.run(source,word).observed_values
                except SourceTransportError:r=None
                checked+=1
                if l!=r:
                    return {"equal":False,"horizon":horizon,
                            "first_distinguishing_word":word,
                            "distinguishing_source":source,
                            "left_output":l,"right_output":r,
                            "comparisons":checked,
                            "all_adaptive_policies_equivalent_claimed":False}
    return {"equal":True,"horizon":horizon,"comparisons":checked,
            "all_adaptive_policies_equivalent_claimed":False}


def delayed_separator_models()->tuple[FiniteCarrier,FiniteCarrier]:
    """Matched empty/one-step reports, different lawful two-step futures.

    Two initial source worlds 0,1, and two reachable hidden states 2,3.
    In GOOD, A silently exposes the relevant source into 2 vs 3; B reads
    zero at original sources but distinguishes at post-A states.
    In BAD, A sends BOTH sources to 2, irreversibly merging them;
    all later enabled action reports remain indistinguishable.
    """
    yes=(True,)*4
    good=FiniteCarrier(4,(
        Instrument("A",(0,0,0,0),(2,3,2,3),yes),
        Instrument("B",(0,0,0,1),(0,1,2,3),yes),
    ),"declared-delayed-good","chart-v1")
    bad=FiniteCarrier(4,(
        Instrument("A",(0,0,0,0),(2,2,2,2),yes),
        Instrument("B",(0,0,0,1),(0,1,2,3),yes),
    ),"declared-delayed-bad","chart-v1")
    return good,bad


def yoneda_policy_descent_demo()->dict:
    positive=conditional_source_field()
    target=("0","1","1","0")
    concrete,h,t_concrete=duplicate_carrier(positive,target)
    morphism=CertifiedSourceMorphism(
        concrete,positive,tuple(range(8)),tuple(range(4)),h,
        t_concrete,target,"initial-parity")
    transfer=morphism.policy_descent()
    if (transfer["abstract_rank"]!=2
            or transfer["concrete_rank"]!=2
            or transfer["state_map_injective"]):
        raise ArithmeticError("Noninjective observational descent certificate failed")
    bad_source=_bit_field()
    bad_t=("0","1","1","0")
    bad_concrete,bad_h,bad_ct=duplicate_carrier(bad_source,bad_t)
    badmap=CertifiedSourceMorphism(
        bad_concrete,bad_source,tuple(range(8)),tuple(range(4)),
        bad_h,bad_ct,bad_t,"initial-parity")
    negative=badmap.policy_descent()
    if negative["abstract_rank"] is not None or negative["concrete_rank"] is not None:
        raise ArithmeticError("Morphism invented missing proof capabilities")
    base=FiniteCarrier(1,(
        Instrument("A",(0,),(0,),(True,)),
        Instrument("B",(0,),(0,),(True,)),
    ),"tiny-two-arrows","one-known-source")
    g=BeliefGame.build(base,(0,),("yes",),target_id="constant")
    category=ObservationPathCategory(g,1)
    root=0
    leaf=next(i for i,(horizon,_) in enumerate(category.contexts)
              if horizon==0)
    arrows=category.hom(root,leaf)
    if len(arrows)!=2:
        raise ArithmeticError("Two genuine distinct observation paths were collapsed")
    full=validate_yoneda(category,root,leaf)
    restricted=validate_yoneda(category,root,leaf,(leaf,))
    if not (full["source_hom_count"]==2
            and full["natural_transform_count"]==2
            and restricted["natural_transform_count"]==1
            and representable_natural_transform(category,arrows[0],(leaf,))
              ==representable_natural_transform(category,arrows[1],(leaf,))):
        raise ArithmeticError("Full/restricted Yoneda discrimination incorrectly claimed")
    sparse=restricted_yoneda_arrow_detection(category,root,leaf,(leaf,))
    dense=restricted_yoneda_arrow_detection(category,root,leaf,category.objects)
    minimum=least_faithful_context_family(category,root,leaf)
    if (sparse["faithful_on_selected_hom"]
            or not dense["faithful_on_selected_hom"]
            or minimum["minimum_context_objects"]!=(root,)):
        raise ArithmeticError("Context-specific Yoneda separation lamps failed")
    good,bad=delayed_separator_models()
    one=shallow_probe_agreement(good,bad,(0,1),1)
    two=shallow_probe_agreement(good,bad,(0,1),2)
    goal=("0","1","0","1")
    left_game=BeliefGame.build(good,(0,1),goal,target_id="source-bit")
    right_game=BeliefGame.build(bad,(0,1),goal,target_id="source-bit")
    bisim=greatest_goal_bisimulation(left_game,right_game)
    if (not one["equal"] or two["equal"] or bisim.roots_related
            or left_game.rank()!=2 or right_game.rank() is not None):
        raise ArithmeticError("One-step probe alias falsely preserved the winning rank")
    return {
        "status":"OPERATIONAL_YONEDA_SOURCE_POLICY_DESCENT_EXACT",
        "full_yoneda_natural_transforms":full["natural_transform_count"],
        "full_yoneda_actual_distinct_arrows":len(arrows),
        "restricted_yoneda_natural_transforms":restricted["natural_transform_count"],
        "restricted_context_collapses_distinct_arrows":True,
        "restricted_arrow_pairs_undetected":len(sparse["undetected_pairs"]),
        "full_arrow_pairs_detected":dense["detected_pairs"],
        "minimum_faithful_context_count":minimum["minimum_context_count"],
        "minimum_faithful_context_is_source":minimum["minimum_context_objects"]==(root,),

        "noninjective_carrier_abstraction_preserves_winning_rank":transfer["optimal_original_source_rank_equal"],
        "abstract_optimal_rank":transfer["abstract_rank"],
        "concrete_optimal_rank":transfer["concrete_rank"],
        "successful_concrete_policy_source_replays":transfer["transported_source_replays"],
        "losing_original_parity_preserved_as_losing":negative["abstract_rank"] is None,
        "one_probe_model_signature_equal":one["equal"],
        "two_probe_model_signature_equal":two["equal"],
        "two_probe_discriminator":list(two["first_distinguishing_word"]),
        "good_model_winning_rank":left_game.rank(),
        "bad_model_has_no_finite_winning_policy":right_game.rank() is None,
        "root_bisimulation_rejects_shallow_alias":not bisim.roots_related,
        "independent_physical_source_attested":False,
        "Yoneda_fullness_does_not_imply_physical_or_RH_positivity":True,
    }
