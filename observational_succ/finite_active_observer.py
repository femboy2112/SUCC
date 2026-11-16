"""Exact finite-state active boundary observability, with instrument backaction.

This is deterministic Mealy-machine/bisimulation mathematics. The transition
is part of the instrument: a probe may alter the state it reads. The result
is relative to a *declared complete action alphabet*, not physical quantum
measurement or an oracle for infinite arithmetic truth.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from itertools import product
from types import MappingProxyType
from typing import Mapping, Sequence


class ProbeContractError(ValueError):
    pass


@dataclass(frozen=True)
class FiniteInstrument:
    states: tuple[str, ...]
    actions: tuple[str, ...]
    transitions: Mapping[tuple[str, str], tuple[str, str]]

    def __post_init__(self) -> None:
        states, actions = self.states, self.actions
        if (type(states) is not tuple or not states or
            any(not isinstance(s, str) or not s for s in states) or
            len(set(states)) != len(states)):
            raise ProbeContractError("distinct nonempty state names required")
        if (type(actions) is not tuple or not actions or
            any(not isinstance(a, str) or not a for a in actions) or
            len(set(actions)) != len(actions)):
            raise ProbeContractError("distinct nonempty probe actions required")
        transitions = dict(self.transitions)
        expected = set(product(states, actions))
        if set(transitions) != expected:
            raise ProbeContractError("complete labelled state/probe transition table required")
        for key, value in transitions.items():
            if (type(value) is not tuple or len(value) != 2 or
                not isinstance(value[0], str) or not value[0] or
                value[1] not in states):
                raise ProbeContractError("each entry is (output, legal next_state)")
        # New shallow copy prevents mutation by callers of original argument.
        object.__setattr__(self, "transitions", MappingProxyType(transitions))

    def allowed(self, actions: Sequence[str] | None = None) -> tuple[str, ...]:
        if actions is None:
            return self.actions
        if type(actions) not in (tuple, list):
            raise ProbeContractError("actions must be a sequence of declared strings")
        actions = tuple(actions)
        if len(set(actions)) != len(actions) or any(a not in self.actions for a in actions):
            raise ProbeContractError("undeclared or duplicate action")
        return actions

    def trace(self, state: str, word: Sequence[str]) -> tuple[tuple[str, ...], str]:
        if state not in self.states:
            raise ProbeContractError("unknown source state")
        if type(word) not in (tuple, list) or any(a not in self.actions for a in word):
            raise ProbeContractError("action word must contain only declared probes; repeats allowed")
        out = []
        for action in word:
            emission, state = self.transitions[state, action]
            out.append(emission)
        return tuple(out), state

    def observational_classes(self, actions: Sequence[str] | None = None) -> tuple[tuple[str, ...], ...]:
        """Greatest output/transition bisimulation, exact after finite refinement.

        s≈t iff EVERY finite probe word yields the same output history. The
        same follows for any deterministic adaptive probe policy, by induction.
        """
        actions = self.allowed(actions)
        class_id = tuple(0 for _ in self.states)
        lookup = {name:i for i,name in enumerate(self.states)}
        for _ in range(len(self.states)):
            signatures = []
            for state in self.states:
                signatures.append(tuple((self.transitions[state,a][0],
                    class_id[lookup[self.transitions[state,a][1]]]) for a in actions))
            ids = {}
            next_class_id = tuple(ids.setdefault(sig,len(ids)) for sig in signatures)
            if next_class_id == class_id:
                break
            class_id = next_class_id
        else:
            raise AssertionError("finite partition refinement must terminate")
        groups={}
        for state, i in zip(self.states,class_id):
            groups.setdefault(i,[]).append(state)
        return tuple(tuple(v) for v in groups.values())

    def shortest_separator(self, left: str, right: str,
                           actions: Sequence[str] | None = None) -> tuple[str, ...] | None:
        """Shortest finite fixed action word with different recorded outputs.

        Each step applies the instrument and updates the carrier independently
        in both hypothetical worlds; it never compares remote actual histories.
        """
        actions = self.allowed(actions)
        if left not in self.states or right not in self.states:
            raise ProbeContractError("unknown candidate source state")
        queue = deque([(left,right,())])
        seen = {(left,right)}
        while queue:
            s,t,word=queue.popleft()
            for a in actions:
                so,sn=self.transitions[s,a]
                to,tn=self.transitions[t,a]
                w=word+(a,)
                if so!=to:
                    return w
                pair=(sn,tn)
                if pair not in seen:
                    seen.add(pair)
                    queue.append((sn,tn,w))
        return None

    def separator_receipt(self,left: str,right: str,
                          actions: Sequence[str] | None = None) -> dict[str,object]:
        word=self.shortest_separator(left,right,actions)
        if word is None:
            return {"separable":False,"word":None,"left":left,"right":right}
        l,t=left,right
        left_updates=[];right_updates=[]
        for a in word:
            lo,ln=self.transitions[l,a]
            to,tn=self.transitions[t,a]
            left_updates.append((a,lo,ln,ln!=l))
            right_updates.append((a,to,tn,tn!=t))
            l,t=ln,tn
        return {"separable":True,"word":word,
                "left_trace":tuple(left_updates),
                "right_trace":tuple(right_updates),
                "last_outputs":(left_updates[-1][1],right_updates[-1][1]),
                "left_changed":any(u[-1] for u in left_updates),
                "right_changed":any(u[-1] for u in right_updates)}
