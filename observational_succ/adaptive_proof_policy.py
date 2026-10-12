"""Exact finite adaptive original-source proof planning under carrier backaction.

A belief tracks pairs (ORIGINAL source, CURRENT carrier). Each admissible
probe has a public outcome and may change the current carrier. The least
AND/OR reachability fixed point decides whether a deterministic adaptive
strategy can certify the ORIGINAL target for every compatible source in
finitely many steps. No physical/quantum/omega/RH conclusion follows.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from itertools import product
from .noncommuting_proof_transport import (
    FiniteCarrier, Instrument, _sources, _bit_field,
)


class PolicyError(ValueError):
    pass


def _belief(pairs):
    x=tuple(sorted(set(pairs)))
    if not x or any(type(pair) is not tuple or len(pair)!=2 or
                    any(type(v) is not int for v in pair) for pair in x):
        raise PolicyError("Malformed source/actual-carrier belief")
    return x


def _terminal(belief, target):
    labels={target[source] for source,_ in belief}
    return next(iter(labels)) if len(labels)==1 else None


def _options(field,belief):
    """Actions must be executable in EVERY compatible current state.

    Unlike the separate future-bisimulation model, this planner does
    NOT treat state-specific offered menus as a free extra observation.
    """
    result={}
    for a in field.actions:
        if not all(a.enabled[actual] for _,actual in belief):
            continue
        groups={}
        for source,actual in belief:
            outcome,after=a.step(actual)
            groups.setdefault(outcome,[]).append((source,after))
        result[a.name]=tuple(
            (outcome,_belief(group)) for outcome,group in sorted(groups.items()))
    return result


@dataclass(frozen=True)
class PolicyVerdict:
    field: FiniteCarrier
    sources: tuple[int,...]
    target: tuple[str,...]
    target_id: str
    root: tuple[tuple[int,int],...]
    reachable: int
    winning_beliefs: int
    rank: int | None
    policy: tuple[tuple[tuple[tuple[int,int],...],str,int], ...]

    @property
    def winning(self):
        return self.rank is not None

    def simulate(self,source:int):
        """Simulator validates every branch, never leaking source to policy."""
        if not self.winning or source not in self.sources:
            raise PolicyError("No sound policy for this source")
        instructions={belief:(name,rank) for belief,name,rank in self.policy}
        belief=self.root
        actual=source
        trace=[]
        for _ in range(self.rank+1):
            done=_terminal(belief,self.target)
            if done is not None:
                if done!=self.target[source]:
                    raise ArithmeticError("Falsely certified original source")
                return {"outcome":done,"steps":len(trace),"trace":tuple(trace)}
            if belief not in instructions:
                raise ArithmeticError("Missing winning continuation")
            name,_=instructions[belief]
            obs,after=self.field.action(name).step(actual)
            nxt=dict(_options(self.field,belief)[name])
            if obs not in nxt or (source,after) not in nxt[obs]:
                raise ArithmeticError("Impossible simulated causal event")
            trace.append((name,obs))
            belief,actual=nxt[obs],after
        raise ArithmeticError("Finite rank never reached a terminal source target")


def solve_adaptive_claim(field:FiniteCarrier,sources:tuple[int,...],
                         target:tuple[str,...], *,
                         target_id:str,max_beliefs:int=4096)->PolicyVerdict:
    _sources(field,sources)
    if (type(target) is not tuple or len(target)!=field.count
            or any(type(v) is not str for v in target)
            or type(target_id) is not str or not target_id
            or type(max_beliefs) is not int or not 1<=max_beliefs<=100000):
        raise PolicyError("Missing source/claim/belief-budget contract")
    root=_belief((s,s) for s in sources)
    queue=[root]
    seen={root}
    edges={}
    i=0
    while i<len(queue):
        b=queue[i]
        i+=1
        edges[b]=_options(field,b)
        for branches in edges[b].values():
            for _,child in branches:
                if child not in seen:
                    if len(seen)>=max_beliefs:
                        raise PolicyError("Finite belief closure exceeded resource budget")
                    seen.add(child)
                    queue.append(child)
    ranks={b:0 for b in queue if _terminal(b,target) is not None}
    choices={}
    while True:
        promoted=[]
        for b in queue:
            if b in ranks:continue
            valid=[]
            for name,branches in edges[b].items():
                if all(child in ranks for _,child in branches):
                    valid.append((1+max(ranks[child] for _,child in branches),name))
            if valid:
                promoted.append((b,min(valid)))
        if not promoted:
            break
        for b,(rank,name) in promoted:
            ranks[b]=rank
            choices[b]=(name,rank)
    verdict=PolicyVerdict(
        field,sources,target,target_id,root,len(queue),len(ranks),
        ranks.get(root),tuple(sorted((b,name,rank)
                                     for b,(name,rank) in choices.items())))
    if verdict.winning:
        for s in sources:
            if verdict.simulate(s)["steps"]>verdict.rank:
                raise ArithmeticError("Bad worst-case policy rank")
    return verdict


def conditional_source_field():
    """A real reversible Q updates the carrier; later choice is outcome-aided.

    Source (a,b). Q reports a then changes (a,b)->(a,a XOR b).
    R0 reads CURRENT b when a=0, otherwise returns 0; R1 reads
    CURRENT b when a=1, otherwise 0. R0/R1 are nondestructive.
    After Q the relevant current b is ORIGINAL parity; using Q's
    observed a, choose R0 or R1. No fixed TWO-action word works.
    """
    states=tuple(range(4))
    yes=(True,)*4
    qa=tuple(s//2 for s in states)
    qnext=tuple(2*(s//2)+((s//2)^(s%2)) for s in states)
    r0=tuple(s%2 if s//2==0 else 0 for s in states)
    r1=tuple(s%2 if s//2==1 else 0 for s in states)
    return FiniteCarrier(4,(
        Instrument("Q",qa,qnext,yes),
        Instrument("R0",r0,states,yes),
        Instrument("R1",r1,states,yes),
    ),"conditional-source-pair","adaptive-parity-v1")


def adaptive_policy_demo():
    sources=(0,1,2,3)
    parity=("0","1","1","0")
    destructive=solve_adaptive_claim(
        _bit_field(),sources,parity,target_id="original-XOR")
    nondestructive=solve_adaptive_claim(
        _bit_field(nondestructive=True),sources,parity,target_id="original-XOR")
    joint=solve_adaptive_claim(
        _bit_field(with_joint=True),sources,parity,target_id="original-XOR")
    conditional=conditional_source_field()
    adaptive=solve_adaptive_claim(
        conditional,sources,parity,target_id="original-XOR")
    if (destructive.winning or not nondestructive.winning
            or nondestructive.rank!=2 or not joint.winning or joint.rank!=1
            or not adaptive.winning or adaptive.rank!=2):
        raise ArithmeticError("Unexpected adaptive game positive/negative controls")
    fixed=[]
    for word in product(("Q","R0","R1"),repeat=2):
        observed={}
        valid=True
        for x in sources:
            report=conditional.run(x,word).observed_values
            if report in observed and observed[report]!=parity[x]:
                valid=False
                break
            observed[report]=parity[x]
        if valid:
            fixed.append(word)
    if fixed:
        raise ArithmeticError("Adaptive advantage refuted by fixed two-action word")
    histories=tuple(adaptive.simulate(x) for x in sources)
    if [h["steps"] for h in histories]!=[2]*4:
        raise ArithmeticError("Unexpected outcome-dependent proof rank")
    return {
        "status":"FINITE_ADAPTIVE_SOURCE_PROOF_GAME_EXACT",
        "destructive_original_parity_winning":destructive.winning,
        "destructive_reachable_beliefs":destructive.reachable,
        "nondestructive_original_parity_winning":nondestructive.winning,
        "nondestructive_worst_case":nondestructive.rank,
        "joint_probe_worst_case":joint.rank,
        "reversible_state_changing_conditional_probe":True,
        "adaptive_conditional_original_parity_winning":adaptive.winning,
        "adaptive_conditional_worst_case":adaptive.rank,
        "any_fixed_two_probe_word_succeeds":bool(fixed),
        "adaptive_action_words":[[a for a,_ in h["trace"]] for h in histories],
        "original_source_given_to_policy":False,
        "menus_offered_as_free_readings":False,
        "actual_hardware_or_RH_theorem_claimed":False,
    }
