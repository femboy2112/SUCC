"""Checkpoint-indexed observer networks, proof-order dovetailing and causal policy trees.

All theorems in this laboratory are classical finite fixed-point, Horn-closure
or automata arguments.  A finite controller plus an UNBOUNDED external memory/
network may enumerate arbitrary finite programs; a bare finite-state controller
cannot.  Candidate proofs and counterfactual instrument paths are NOT physical
measurements. A ``trusted_event_ids`` registry is a DECLARED source premise,
not an authentication device.

Source-changing interventions are checked against ORIGINAL-source claims using
pairs (original source, current carrier). The possible policy tree is sound in
the supplied complete finite model, not independently authenticated reality.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from typing import Hashable, Mapping

from .carrier_observational_frontier import ControlledCarrier, destructive_parity_model


class MetaTowerError(ValueError):
    """Malformed causal source, theory/epoch or declared resource budget."""


@dataclass(frozen=True)
class GroundRule:
    premises: tuple[str, ...]
    conclusion: str

    def __post_init__(self):
        if (type(self.premises) is not tuple or not self.premises
                or any(type(p) is not str or not p for p in self.premises)
                or len(set(self.premises)) != len(self.premises)
                or type(self.conclusion) is not str or not self.conclusion):
            raise MetaTowerError("Use finite ground positive Horn implications")


@dataclass(frozen=True)
class Report:
    event_id: str
    source_id: str
    basis_id: str
    checkpoint: int
    owner: str
    atom: str

    def __post_init__(self):
        if (any(type(s) is not str or not s for s in
                (self.event_id, self.source_id, self.basis_id, self.owner, self.atom))
                or type(self.checkpoint) is not int or self.checkpoint < 1):
            raise MetaTowerError("Typed event origin, basis and causal checkpoint required")


@dataclass(frozen=True)
class HornTheory:
    source_id: str
    basis_id: str
    axioms: tuple[str, ...]
    rules: tuple[GroundRule, ...]

    def __post_init__(self):
        if not self.source_id or not self.basis_id or not isinstance(self.rules, tuple):
            raise MetaTowerError("Fixed source and logical basis required")
        if (type(self.axioms) is not tuple or len(set(self.axioms)) != len(self.axioms)
                or any(type(a) is not str or not a for a in self.axioms)
                or any(not isinstance(rule, GroundRule) for rule in self.rules)):
            raise MetaTowerError("Distinct named axioms and genuine ground Horn rules required")

    def closure(self, evidence: tuple[str, ...], *, order: tuple[int, ...] | None = None) -> dict:
        """Explicit finite witness for monotone least Horn fixed point.

        Rule order can change the *timing* of discovery, not the final closure.
        Every derived atom records the source rule and positive antecedents.
        Soundness depends on the declared source evidence and trusted axioms.
        """
        if type(evidence) is not tuple or any(type(a) is not str or not a for a in evidence):
            raise MetaTowerError("Proof evidence must be named atoms")
        if order is None:
            order = tuple(range(len(self.rules)))
        if (type(order) is not tuple or len(order) != len(self.rules)
                or set(order) != set(range(len(self.rules)))):
            raise MetaTowerError("One genuine permutation of all rules required")
        known = set(self.axioms) | set(evidence)
        evidence_index = tuple(dict.fromkeys(self.axioms + evidence))
        derivations = []
        while True:
            changed = False
            for i in order:
                rule = self.rules[i]
                if rule.conclusion not in known and set(rule.premises) <= known:
                    known.add(rule.conclusion)
                    derivations.append((rule.conclusion, i, rule.premises))
                    changed = True
            if not changed:
                break
        result = {"closure": tuple(sorted(known)),
                  "premises": evidence_index,
                  "steps": tuple(derivations),
                  "fixed_point_verified": True}
        self.check_proof(result)
        return result

    def check_proof(self, receipt: Mapping) -> bool:
        """Replay a positive Horn proof against the named source and rules."""
        if not isinstance(receipt, Mapping):
            raise MetaTowerError("Malformed proof receipt")
        known = set(self.axioms)
        for atom in receipt["premises"]:
            if not isinstance(atom, str) or not atom:
                raise MetaTowerError("Invalid source premise")
            known.add(atom)
        for conclusion, index, premises in receipt["steps"]:
            if (type(index) is not int or not 0 <= index < len(self.rules)
                    or conclusion != self.rules[index].conclusion
                    or premises != self.rules[index].premises
                    or not set(premises) <= known):
                raise MetaTowerError("A claimed inferential arrow is not justified")
            known.add(conclusion)
        if tuple(sorted(known)) != tuple(receipt["closure"]):
            raise MetaTowerError("Proof conclusion not equal to replayed closure")
        return True

    def all_rule_orders(self, evidence: tuple[str, ...], *, max_rules: int = 7) -> dict:
        """Exhaust all finite orderings where feasible; no shortcut to more axioms."""
        if type(max_rules) is not int or len(self.rules) > max_rules:
            raise MetaTowerError("Ordering explosion: honest resource-limit result")
        expected = self.closure(evidence)["closure"]
        count = 0
        for order in permutations(range(len(self.rules))):
            count += 1
            if self.closure(evidence, order=order)["closure"] != expected:
                raise AssertionError("Positive Horn closure must be order invariant")
        return {"checked_permutations": count, "closure": expected,
                "theorem": "finite monotone ground Horn order-confluence"}


def finite_source_soundness(theory: HornTheory,
                            source_worlds: Mapping[Hashable, tuple[str, ...]]) -> dict:
    """EXACT complete finite interpretation audit of positive Horn rules.

    The stated source-world semantics is NOT authenticated by this algorithm.
    All worlds are assessed, not merely the receiver's favorite hypothesis.
    A syntactically valid derivation is NOT automatically semantically sound.
    """
    if not source_worlds:
        raise MetaTowerError("At least one declared source interpretation needed")
    for world, atoms in source_worlds.items():
        if type(atoms) is not tuple or any(type(x) is not str or not x for x in atoms):
            raise MetaTowerError("Finite ground truth interpretation required")
        truth=set(atoms)
        for axiom in theory.axioms:
            if axiom not in truth:
                return {"sound_relative_to_worlds":False,"counterexample_world":world,
                        "failing_axiom":axiom,"failing_rule":None,
                        "source_semantics_authenticated":False}
        for i, rule in enumerate(theory.rules):
            if set(rule.premises) <= truth and rule.conclusion not in truth:
                return {"sound_relative_to_worlds":False,"counterexample_world":world,
                        "failing_axiom":None,"failing_rule":i,
                        "source_semantics_authenticated":False}
    return {"sound_relative_to_worlds":True,
            "checked_worlds":len(source_worlds),
            "source_semantics_authenticated":False}


def checkpoint_closure(theory: HornTheory, deliveries: tuple[tuple[Report, ...], ...],
                       *, trusted_event_ids: frozenset[str], target: str) -> tuple[dict, ...]:
    """E accumulates finite leased evidence; one closure macro-step per checkpoint.

    Arrival and proof order are immaterial to the final monotonically justified
    closure, provided the causal origin/source/basis attestations are SOUND.
    No empirical verification of the trust registry is claimed here.
    """
    if (not isinstance(trusted_event_ids, frozenset) or type(target) is not str
            or not target or type(deliveries) is not tuple):
        raise MetaTowerError("Declared trusted source registry and target required")
    gathered: dict[str, Report] = {}
    records = []
    last_closure: set[str] = set()
    for t, batch in enumerate(deliveries, start=1):
        if type(batch) is not tuple:
            raise MetaTowerError("One immutable delivery batch per checkpoint")
        for item in batch:
            if not isinstance(item, Report):
                raise MetaTowerError("Malformed delivered event")
            if (item.source_id != theory.source_id or item.basis_id != theory.basis_id
                    or item.checkpoint > t or item.event_id not in trusted_event_ids):
                raise MetaTowerError("Unlicensed or future source event")
            if item.event_id in gathered and gathered[item.event_id] != item:
                raise MetaTowerError("Conflicting replay of an immutable event ID")
            gathered[item.event_id] = item
        evidence = tuple(gathered[k].atom for k in sorted(gathered))
        proof = theory.closure(evidence)
        current = set(proof["closure"])
        if not current >= last_closure:
            raise AssertionError("Append-only Horn closure cannot shrink")
        records.append({"checkpoint": t,
                        "accepted_event_ids": tuple(sorted(gathered)),
                        "newly_justified_atoms": tuple(sorted(current-last_closure)),
                        "derived_atoms": proof["closure"],
                        "target_certified": target in current,
                        "macro_steps_at_E": 1,
                        "source_outcomes_authenticated": False,
                        "proof": proof})
        last_closure = current
    return tuple(records)


def enumerate_action_words(actions: tuple[str, ...], depth: int,
                           *, word_budget: int = 100000) -> tuple[tuple[str, ...], ...]:
    """A finite checkpoint enumerates exactly all words up to given depth.

    A FINITE PROGRAM WITH GROWING EXTERNAL MEMORY generates the sequence.
    It is not a finite-state output-only automaton enumerating it unaided.
    """
    if (type(depth) is not int or depth < 0 or type(word_budget) is not int
            or word_budget < 1 or not actions or len(set(actions)) != len(actions)):
        raise MetaTowerError("Finite action alphabet and positive budgets required")
    count = sum(len(actions)**i for i in range(depth+1))
    if count > word_budget:
        raise MetaTowerError("Exceeded declared program-enumeration budget")
    return tuple(word for length in range(depth+1) for word in product(actions, repeat=length))


def _root(carrier: ControlledCarrier) -> tuple[tuple[Hashable, Hashable], ...]:
    return tuple((s, s) for s in carrier.states)


def _child(carrier: ControlledCarrier, belief: tuple, action: str) -> tuple:
    """Public outcome branches over (original, current carrier) hypotheses."""
    groups: dict[Hashable, list] = {}
    for original, current in belief:
        outcome, after = carrier.step(current, action)
        groups.setdefault(outcome, []).append((original, after))
    order = {s:i for i,s in enumerate(carrier.states)}
    return tuple((obs, tuple(sorted(set(pairs), key=lambda z:(order[z[0]],order[z[1]]))))
                 for obs,pairs in sorted(groups.items(), key=lambda x:repr(x[0])))


def _terminal(belief: tuple, claim: Mapping[Hashable, Hashable]):
    labels = {claim[o] for o, _ in belief}
    return next(iter(labels)) if len(labels) == 1 else None


def verify_policy_tree(carrier: ControlledCarrier, claim: Mapping[Hashable, Hashable],
                       tree: tuple, *, max_depth: int) -> dict:
    """Independent source-by-source replay, never looking up a secret in policy."""
    if set(claim) != set(carrier.states):
        raise MetaTowerError("Original claim must label every possible original state")
    maximum = 0
    visited = []
    for original in carrier.states:
        now = original
        position = tree
        trace = []
        while position[0] != "DONE":
            if len(trace) >= max_depth or position[0] != "ASK" or len(position) != 3:
                raise MetaTowerError("Incomplete, overbudget or noncausal policy")
            action, branch_data = position[1], position[2]
            if action not in carrier.actions or len(dict(branch_data)) != len(branch_data):
                raise MetaTowerError("Illegal action or duplicate response branch")
            outcome, now = carrier.step(now, action)
            available = dict(branch_data)
            if outcome not in available:
                raise MetaTowerError("Missing public outcome branch")
            position = available[outcome]
            trace.append((action, outcome))
        if len(position) != 2 or position[1] != claim[original]:
            raise MetaTowerError("Terminal claim not true of ORIGINAL source")
        maximum = max(maximum, len(trace))
        visited.append(tuple(trace))
    return {"valid": True, "maximum_depth": maximum,
            "source_traces": tuple(visited), "original_truth_given_to_policy": False}


def _winning_at_depth(carrier: ControlledCarrier, claim: Mapping[Hashable, Hashable],
                      max_depth: int) -> tuple | None:
    cache: dict[tuple, tuple | None] = {}

    def rec(belief: tuple, depth: int):
        key = (belief, depth)
        if key in cache:
            return cache[key]
        terminal = _terminal(belief, claim)
        if terminal is not None:
            answer = ("DONE", terminal)
        elif depth == 0:
            answer = None
        else:
            answer = None
            for action in carrier.actions:
                candidates=[]
                for outcome, child in _child(carrier, belief, action):
                    subtree=rec(child,depth-1)
                    if subtree is None:
                        break
                    candidates.append((outcome,subtree))
                else:
                    answer = ("ASK",action,tuple(candidates))
                    break
        cache[key] = answer
        return answer

    return rec(_root(carrier),max_depth)


def _fixed_word_wins(carrier: ControlledCarrier, claim: Mapping, word: tuple[str,...]) -> bool:
    """One identical preset action ordering, independent of observations."""
    outcomes={}
    for s in carrier.states:
        obs = carrier.trace(s,word)
        if obs in outcomes and outcomes[obs] != claim[s]:
            return False
        outcomes[obs] = claim[s]
    return True


def proof_policy_checkpoint(carrier: ControlledCarrier, claim: Mapping,
                             depth: int, *, max_words: int = 100000,
                             full_model_no_go: bool = False) -> dict:
    """Dovetail ALL fixed words and every adaptive AND/OR choice up to depth.

    If no candidate works, that is only a DEPTH-N no-go, unless a separate
    complete finite-model fixed point is checked. Counterfactual paths here
    are SYMBOLIC computations from supplied transition tables, not physical
    observations of unexecuted destructive experiments.
    """
    if set(claim) != set(carrier.states):
        raise MetaTowerError("Original-source claim labels missing")
    words=enumerate_action_words(carrier.actions,depth,word_budget=max_words)
    fixed=tuple(w for w in words if _fixed_word_wins(carrier,claim,w))
    policy=_winning_at_depth(carrier,claim,depth)
    if policy is not None:
        check=verify_policy_tree(carrier,claim,policy,max_depth=depth)
        if check["maximum_depth"] > depth:
            raise AssertionError("Bounded policy contains deeper branch")
        status="FOUND_ADAPTIVE_POLICY"
    else:
        check=None
        status="NO_POLICY_WITHIN_DEPTH"
        if full_model_no_go:
            exact=carrier.adaptive_original_claim(claim)
            if exact["status"] == "NO_UNIFORM_FINITE_POLICY":
                status="MODEL_CERTIFIED_NO_FINITE_POLICY"
            elif exact["rank"] <= depth:
                raise AssertionError("Depth scan disagrees with independent exact model")
    if fixed and policy is None:
        raise AssertionError("Fixed-word success requires an adaptive policy")
    return {"checkpoint_depth":depth,
            "fixed_words_checked":len(words),
            "first_winning_fixed_word":fixed[0] if fixed else None,
            "adaptive_policy":policy,
            "verification":check,
            "status":status,
            "formal_model_table_exhaustive": True,
            "physical_branches_executed":0,
            "source_tables_empirically_authenticated":False}


@dataclass(frozen=True)
class BranchLicense:
    source_id: str
    fresh_token: str
    initial_source_class_id: str

    def __post_init__(self):
        if any(type(v) is not str or not v for v in
               (self.source_id,self.fresh_token,self.initial_source_class_id)):
            raise MetaTowerError("A declared independently prepared carrier token required")


def certify_parallel_roots(carrier: ControlledCarrier,
                           planned_roots: tuple[tuple[BranchLicense, str], ...]) -> dict:
    """Different possible first interventions require separate copy/reset leases.

    Source tokens are DECLARED, not physical authentication. Even valid
    declared leases do not establish the possibility of cloning an unknown
    quantum state.
    """
    if not planned_roots:
        raise MetaTowerError("At least one actual candidate root action")
    seen=set()
    for license, action in planned_roots:
        if not isinstance(license, BranchLicense) or license.source_id!=carrier.source_id:
            raise MetaTowerError("False carrier identity in branch lease")
        if action not in carrier.actions:
            raise MetaTowerError("Branch root not in physical action menu")
        if license.fresh_token in seen:
            raise MetaTowerError("One mutable carrier cannot execute two initial first actions")
        seen.add(license.fresh_token)
    return {"licensed_roots":len(planned_roots),
            "distinct_source_preparations":len(seen),
            "true_state_reprepared_identically":False,
            "source_signature_authenticated":False}


@dataclass(frozen=True)
class FiniteController:
    """Autonomous finite-state command source WITHOUT an external counter/tape."""
    labels: tuple[str, ...]
    next_state: tuple[int, ...]
    initial: int=0

    def __post_init__(self):
        n=len(self.labels)
        if (n==0 or n!=len(self.next_state) or type(self.initial) is not int
                or not 0<=self.initial<n or any(type(s) is not str or not s for s in self.labels)
                or any(type(i) is not int or not 0<=i<n for i in self.next_state)):
            raise MetaTowerError("Finite total autonomous output Mealy/Moore controller")

    def eventual_period(self) -> dict:
        order=[]; where={}; current=self.initial
        while current not in where:
            where[current]=len(order)
            order.append(current)
            current=self.next_state[current]
        a=where[current]
        return {"prefix":tuple(self.labels[s] for s in order[:a]),
                "period":tuple(self.labels[s] for s in order[a:]),
                "cycle_length":len(order)-a,
                "observationally_complete_enumerator":False,
                "requires_external_unbounded_storage_for_arbitrary_word_dovetailing":True}


def nonmonotone_default_countermodel(order: tuple[str, ...]) -> tuple[str, ...]:
    """Default rules A if not B, B if not A cannot be merged cross-order.

    The given schedule controls which applicable default fires first. This
    is a NONMONOTONE logic, not part of positive Horn closure.
    """
    if type(order) is not tuple or set(order)!={"A","B"} or len(order)!=2:
        raise MetaTowerError("Two distinct competing defaults required")
    accepted=set()
    for label in order:
        if label=="A" and "B" not in accepted:
            accepted.add("A")
        if label=="B" and "A" not in accepted:
            accepted.add("B")
    return tuple(sorted(accepted))


def meta_tower_demo() -> dict:
    carrier, parity = destructive_parity_model()
    destructive=proof_policy_checkpoint(carrier, parity,3,full_model_no_go=True)
    states=tuple((a,b) for a in range(2) for b in range(2))
    rows={}
    for a,b in states:
        rows[(a,b),"Q"]=(a,(a,a^b))
        rows[(a,b),"R0"]=(b if a==0 else 0,(a,b))
        rows[(a,b),"R1"]=(b if a==1 else 0,(a,b))
    conditional=ControlledCarrier("source:conditional-parity",states,("Q","R0","R1"),rows)
    contrast=proof_policy_checkpoint(conditional,parity,2)
    theory=HornTheory("one-shared-carrier","v1",(),(
        GroundRule(("evidence-a",),"local-a"),
        GroundRule(("evidence-b",),"local-b"),
        GroundRule(("local-a","local-b"),"original-parity-established")))
    inputs=((Report("r1","one-shared-carrier","v1",1,"A","evidence-a"),),
            (Report("r2","one-shared-carrier","v1",2,"B","evidence-b"),))
    clock=checkpoint_closure(theory,inputs,trusted_event_ids=frozenset(("r1","r2")),
                             target="original-parity-established")
    return {"status":"FINITE_META_OBSERVER_CHECKPOINTS_EXACT",
            "meta_tested_model_not_physical_source":True,
            "destructive_full_order_enumeration":destructive["status"],
            "noncommuting_conditional_adaptive_status":contrast["status"],
            "adaptive_succeeds_where_fixed_length_two_fails": (
                contrast["verification"] is not None and
                contrast["first_winning_fixed_word"] is None),
            "conditional_worst_case_depth":contrast["verification"]["maximum_depth"],
            "checkpoint_e_knowledge":[{"index":x["checkpoint"],"proved":x["target_certified"]}
                                       for x in clock],
            "two_default_orderings_disagree": (
                nonmonotone_default_countermodel(("A","B")) !=
                nonmonotone_default_countermodel(("B","A"))),
            "finite_controller_periodic":FiniteController(("A","B"),(1,0)).eventual_period()["period"],
            "physical_infinity_completed":False,
            "source_authentication_claimed":False,
            "RH_claimed":False}
