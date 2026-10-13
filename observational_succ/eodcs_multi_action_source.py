"""Orthogonal SUCC: many causal actions, probe-word genesis and dark fibers.

A finite Moore observer has complete, source-declared action maps U_a and
a report q. E grows an experiment-language by typed composition of actions,
then computes the greatest q-respecting action congruence. Newly created
probe words can distinguish states that EVERY one-step observation aliases.

Two crucial distinctions:
* A source U_a U_b != U_b U_a may have a flat *reported* commutator.
* If a pair survives greatest action congruence, NO finite lawful word in
  this instrument menu can distinguish it. A new source probe is required.

Classical automata theory (Myhill--Nerode / bisimulation), not novel
mathematics or a physics claim. Exact finite path witnesses and source
versions are first-class outputs.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from .causal_nerode_succ import SourceTransportError


@dataclass(frozen=True)
class ActionSource:
    source_id: str
    epoch: int
    basis: str
    states: tuple[str, ...]
    outputs: tuple[str, ...]
    actions: tuple[str, ...]
    transitions: tuple[tuple[str, ...], ...]
    source_authenticated: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis or type(self.epoch) is not int
                or self.epoch < 0 or not self.states or not self.actions
                or len(set(self.states)) != len(self.states)
                or len(set(self.actions)) != len(self.actions)
                or type(self.states) is not tuple
                or type(self.outputs) is not tuple
                or type(self.actions) is not tuple
                or type(self.transitions) is not tuple
                or len(self.outputs) != len(self.states)
                or len(self.transitions) != len(self.actions)
                or any(len(transition) != len(self.states)
                       or any(x not in self.states for x in transition)
                       for transition in self.transitions)
                or any(type(x) is not str or not x for x in
                       self.states+self.outputs+self.actions)
                or self.source_authenticated):
            raise SourceTransportError("Malformed declared finite action/source law")

    def report(self, state: str) -> str:
        try:
            return dict(zip(self.states, self.outputs))[state]
        except KeyError as ex:
            raise SourceTransportError("Unknown observer state") from ex

    def step(self, state: str, action: str) -> str:
        if action not in self.actions:
            raise SourceTransportError("Requested action unavailable in observer menu")
        try:
            return dict(zip(self.states,
                            self.transitions[self.actions.index(action)]))[state]
        except KeyError as ex:
            raise SourceTransportError("Unknown source state") from ex

    def run(self, state: str, word: tuple[str, ...]) -> str:
        if type(word) is not tuple or any(a not in self.actions for a in word):
            raise SourceTransportError("Probe requires lawful finite action word")
        for a in word:
            state = self.step(state, a)
        return state

    def observe(self, state: str, word: tuple[str, ...]) -> str:
        return self.report(self.run(state, word))


@dataclass(frozen=True)
class ActionCongruenceCertificate:
    source_id: str
    block_counts: tuple[int, ...]
    equivalence_classes: tuple[tuple[str, ...], ...]
    shortest_distinguishing_words: tuple[
        tuple[str, str, tuple[str, ...]], ...]
    eternally_indistinguishable_pairs: tuple[tuple[str, str], ...]
    finite_fixpoint_verified: bool
    source_observation_authenticated: bool = False


def action_congruence(source: ActionSource) -> ActionCongruenceCertificate:
    states = source.states
    groups = {}
    for s in states:
        groups.setdefault(source.report(s), []).append(s)
    blocks = tuple(sorted((tuple(v) for v in groups.values()),
                          key=lambda b: states.index(b[0])))
    counts = [len(blocks)]
    while True:
        index = {s: i for i, block in enumerate(blocks) for s in block}
        signatures = {}
        for s in states:
            sig = (source.report(s),) + tuple(
                index[source.step(s, a)] for a in source.actions)
            signatures.setdefault(sig, []).append(s)
        refined = tuple(sorted((tuple(v) for v in signatures.values()),
                               key=lambda b: states.index(b[0])))
        if len(refined) < len(blocks):
            raise AssertionError("Observation refinement cannot merge existing classes")
        if refined == blocks:
            break
        if len(refined) == len(blocks):
            raise AssertionError("Partition renamed but no semantic refinement")
        blocks = refined
        counts.append(len(blocks))
        if len(blocks) > len(states):
            raise AssertionError("Finite automaton quotient never exceeds source size")
    index = {s: i for i, block in enumerate(blocks) for s in block}
    if any(index[source.step(s,a)] != index[source.step(t,a)]
           for block in blocks for s,t in product(block,repeat=2)
           for a in source.actions):
        raise AssertionError("Refined fixed point fails action congruence")
    if any(source.report(s)!=source.report(t)
           for block in blocks for s,t in product(block,repeat=2)):
        raise AssertionError("Refined fixed point changed the original output")

    witnesses, darkness = [], []
    for i,s in enumerate(states):
        for t in states[i+1:]:
            if index[s] == index[t]:
                darkness.append((s,t))
            else:
                w = shortest_distinguishing_word(source,s,t)
                if w is None or source.observe(s,w)==source.observe(t,w):
                    raise AssertionError("Distinct quotient classes need finite witness")
                witnesses.append((s,t,w))
    return ActionCongruenceCertificate(
        source.source_id,tuple(counts),blocks,tuple(witnesses),
        tuple(darkness),True,
    )


def shortest_distinguishing_word(source: ActionSource, s: str, t: str
                                 ) -> tuple[str, ...] | None:
    """Independent pair-graph BFS: minimal length, deterministic action ties."""
    if s not in source.states or t not in source.states:
        raise SourceTransportError("Unlicensed source pair")
    root=(s,t,())
    queue=deque([root])
    seen={(s,t)}
    while queue:
        a,b,word=queue.popleft()
        if source.report(a)!=source.report(b):
            return word
        for action in source.actions:
            next_pair=(source.step(a,action),source.step(b,action))
            if next_pair not in seen:
                seen.add(next_pair)
                queue.append((next_pair[0],next_pair[1],word+(action,)))
    return None


def action_curvature(source: ActionSource, a: str, b: str) -> dict:
    """Two-path transported commutator without assuming group invertibility."""
    if a not in source.actions or b not in source.actions:
        raise SourceTransportError("Both experiment paths require available actions")
    original=[]
    observable=[]
    for s in source.states:
        left=source.run(s,(a,b))
        right=source.run(s,(b,a))
        if left!=right:
            original.append(s)
        if source.report(left)!=source.report(right):
            observable.append(s)
    if not set(observable)<=set(original):
        raise AssertionError("Observable noncommutation implies underlying mismatch")
    return {
        "source_noncommuting_states":tuple(original),
        "observable_noncommuting_states":tuple(observable),
        "source_nonflat_but_observer_flat":
            bool(original) and not observable,
        "unseen_source_noncommutation":tuple(
            s for s in original if s not in observable),
        "physical_curvature_claimed":False,
    }


def newly_generated_probe_demo() -> dict:
    states=("x","y","u","v","c","d")
    src=ActionSource("two-action-obstruction",0,"named-states",
                     states,("0","0","0","0","0","1"),("A","B"),
                     (("u","v","u","v","c","d"),
                      ("x","y","c","d","c","d")))
    first_a = (src.observe("x",("A",)),src.observe("y",("A",)))
    first_b = (src.observe("x",("B",)),src.observe("y",("B",)))
    discovered=shortest_distinguishing_word(src,"x","y")
    if first_a[0]!=first_a[1] or first_b[0]!=first_b[1]:
        raise AssertionError("One-step experiments must remain aliased")
    if discovered!=("A","B"):
        raise AssertionError("The new composite probe must be shortest")
    report=action_congruence(src)
    curvature=action_curvature(src,"A","B")
    return {
        "initial_alias":True,
        "both_one_action_probes_alias":True,
        "synthesized_minimum_word":list(discovered),
        "synthesized_probe_results":
            [src.observe("x",discovered),src.observe("y",discovered)],
        "finite_full_behavior_classes":len(report.equivalence_classes),
        "observable_two_path_commutator":list(curvature["observable_noncommuting_states"]),
        "physical_implementation_created":False,
    }


def dark_toolkit_demo() -> dict:
    states=("a","b","c","d")
    src=ActionSource("dark-source",0,"reported-bits",states,
                     ("0","0","1","1"),("A","B"),
                     (("b","a","d","c"),("a","b","d","c")))
    r=action_congruence(src)
    if shortest_distinguishing_word(src,"a","b") is not None:
        raise AssertionError("Closed action-congruence must never distinguish")
    # A deliberately *unavailable* source instrument would be required.
    lamp={"a":"0","b":"1","c":"0","d":"1"}
    if lamp["a"]==lamp["b"]:
        raise AssertionError("Proposed extension must be a genuine separator")
    return {
        "source_states":len(states),
        "toolkit":list(src.actions),
        "closed_observational_quotient":[list(c) for c in r.equivalence_classes],
        "dark_pair":["a","b"],
        "all_finite_words_unable_to_separate":True,
        "external_lamp_would_separate":True,
        "lamp_present_in_available_menu":False,
        "physical_source_authenticated":False,
    }
