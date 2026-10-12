"""Exact finite carrier-relative behavioral equivalence and adaptive proof bounds.

This is CLASSICAL finite Mealy automata / observational equivalence, organized
as explicit SUCC proof certificates. Source identities and ontology labels are
hypotheses: none is authenticated physically. Finite source-changing protocols
track (ORIGINAL SOURCE, CURRENT CARRIER) separately.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Hashable, Mapping


class FrontierError(ValueError):
    """Invalid source, incomplete instrument, or insufficient resource budget."""


def _canonical(keys: tuple[object, ...]) -> tuple[int, ...]:
    classes: dict[object, int] = {}
    result = []
    for key in keys:
        if key not in classes:
            classes[key] = len(classes)
        result.append(classes[key])
    return tuple(result)


@dataclass(frozen=True)
class ControlledCarrier:
    """One declared deterministic total finite Mealy carrier.

    Each (state,action) maps to (public outcome, NEXT carrier state).
    An observer is NEVER handed the original hidden state. Public action
    availability is constant: the model does not smuggle a menu sensor.
    """
    source_id: str
    states: tuple[Hashable, ...]
    actions: tuple[str, ...]
    transitions: Mapping[tuple[Hashable, str], tuple[Hashable, Hashable]]

    def __post_init__(self) -> None:
        if not isinstance(self.source_id, str) or not self.source_id:
            raise FrontierError("Declare one source identity")
        if not self.states or len(set(self.states)) != len(self.states):
            raise FrontierError("Distinct nonempty source states required")
        if not self.actions or len(set(self.actions)) != len(self.actions) or any(
            type(a) is not str or not a for a in self.actions
        ):
            raise FrontierError("Distinct named publicly executable actions required")
        expected = {(s, a) for s in self.states for a in self.actions}
        if set(self.transitions) != expected:
            raise FrontierError("Every action must be defined at every current carrier state")
        for (_, _), transition in self.transitions.items():
            if type(transition) is not tuple or len(transition) != 2:
                raise FrontierError("Each transition needs (public outcome,next carrier)")
            outcome, successor = transition
            try:
                hash(outcome)
            except TypeError as exc:
                raise FrontierError("Observable outcomes must be hashable") from exc
            if successor not in self.states:
                raise FrontierError("Transitions must remain on the declared carrier")

    def step(self, current: Hashable, action: str) -> tuple[Hashable, Hashable]:
        if current not in self.states or action not in self.actions:
            raise FrontierError("Unknown source state or observation")
        return self.transitions[current, action]

    def trace(self, initial: Hashable, actions: tuple[str, ...]) -> tuple[Hashable, ...]:
        if initial not in self.states:
            raise FrontierError("Unknown initial carrier state")
        q = initial
        outputs = []
        for a in actions:
            out, q = self.step(q, a)
            outputs.append(out)
        return tuple(outputs)

    def partitions(self) -> tuple[tuple[int, ...], ...]:
        """Greatest future-trace equivalence via finite color refinement.

        At round k: identical public output words for EVERY action sequence
        of length <=k. Initial color is deliberately constant. Stabilization
        occurs in <= n-1 strict refinements for n states.
        """
        colors = (0,) * len(self.states)
        history = [colors]
        while True:
            by_state = {s: colors[i] for i, s in enumerate(self.states)}
            keys = tuple(tuple((self.step(s, a)[0], by_state[self.step(s, a)[1]])
                               for a in self.actions) for s in self.states)
            nxt = _canonical(keys)
            if nxt == colors:
                return tuple(history)
            # Key includes all successor classes. Equal successor colors must
            # not coalesce pre-existing distinguishable states when this is
            # a true refinement of trace equivalence: the proof is induction.
            if len(set(nxt)) <= len(set(colors)):
                raise AssertionError("Nonstationary partition refinement")
            colors = nxt
            history.append(colors)
            if len(history) > len(self.states):
                raise AssertionError("Finite state refinement failed to converge")

    def classes(self) -> tuple[tuple[Hashable, ...], ...]:
        colors = self.partitions()[-1]
        return tuple(tuple(s for s, c in zip(self.states, colors) if c == k)
                     for k in range(max(colors) + 1))

    def minimal_behavior_quotient(self) -> dict:
        """Construct the minimal observable deterministic Mealy state quotient.

        This quotient preserves all action/outcome traces from every initial
        state. Its number of classes is a LOWER bound for any deterministic
        carrier representing all of those distinct observable behaviors.
        It is NOT a lower bound for arbitrary probabilistic/nonlinear/quantum
        representations or the full physical state count.
        """
        cls=self.classes()
        where={s:i for i,group in enumerate(cls) for s in group}
        transitions={}
        for i,group in enumerate(cls):
            for a in self.actions:
                out, nxt=self.step(group[0],a)
                for s in group[1:]:
                    other, dest=self.step(s,a)
                    if other!=out or where[dest]!=where[nxt]:
                        raise AssertionError("Trace-equivalence quotient fails congruence")
                transitions[i,a]=(out,where[nxt])
        machine=ControlledCarrier(self.source_id+":behavior-quotient",
                                  tuple(range(len(cls))),self.actions,transitions)
        return {"minimum_behavior_state_count":len(cls),
                "source_to_observable_state":tuple((s,where[s]) for s in self.states),
                "quotient":machine,"source_ontology_identified":False}

    def separating_word(self, a: Hashable, b: Hashable) -> tuple[str, ...] | None:
        """Shortest public action word separating two CURRENT states, or None.

        This pair-specific word need NOT be executable as one globally winning
        ORIGINAL-SOURCE policy when observations change the carrier.
        """
        if a not in self.states or b not in self.states:
            raise FrontierError("Unknown current source hypotheses")
        if a == b:
            return None
        pending = deque([(a, b, ())])
        visited = {(a, b)}
        while pending:
            x, y, prefix = pending.popleft()
            for action in self.actions:
                ox, nx = self.step(x, action)
                oy, ny = self.step(y, action)
                word = prefix + (action,)
                if ox != oy:
                    return word
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    pending.append((nx, ny, word))
        return None

    def claim_quotient(self, claims: Mapping[Hashable, Hashable]) -> dict:
        """Observational predicate descent, only a NECESSARY policy condition."""
        if set(claims) != set(self.states):
            raise FrontierError("Every original source must have a declared claim")
        for cls in self.classes():
            for x in cls[1:]:
                if claims[x] != claims[cls[0]]:
                    if self.separating_word(cls[0], x) is not None:
                        raise AssertionError("False behavioral equivalence")
                    return {"status": "PERMANENTLY_DARK_UNDER_ACTIONS",
                            "witness": (cls[0], x), "classes": self.classes(),
                            "claim_values": (claims[cls[0]], claims[x]),
                            "sufficient_for_policy": False}
        return {"status": "BEHAVIORALLY_FACTORABLE_ONLY",
                "classes": self.classes(), "witness": None,
                "sufficient_for_policy": False}

    def adaptive_original_claim(self, claims: Mapping[Hashable, Hashable],
                                *, max_beliefs: int = 10000) -> dict:
        """Exact finite least AND/OR fixed point on (original,current) pairs.

        Computes MINIMUM WORST-CASE number of actual actions for a uniform
        terminating policy, if one exists. Rejects resource exhaustion; does
        not replace it with "no winning policy".
        """
        if type(max_beliefs) is not int or max_beliefs < 1:
            raise FrontierError("Finite positive belief budget required")
        if set(claims) != set(self.states):
            raise FrontierError("Claim missing for an original source")
        order = {s: i for i, s in enumerate(self.states)}
        def norm(items):
            return tuple(sorted(set(items), key=lambda item: (order[item[0]], order[item[1]])))
        root = norm((s, s) for s in self.states)
        available = [root]
        seen = {root}
        branches = {}
        for belief in available:
            options = {}
            for action in self.actions:
                grouped = {}
                for original, current in belief:
                    outcome, after = self.step(current, action)
                    grouped.setdefault(outcome, []).append((original, after))
                options[action] = tuple(norm(v) for v in grouped.values())
                for child in options[action]:
                    if child not in seen:
                        if len(seen) >= max_beliefs:
                            raise FrontierError("Resource budget exhausted: policy verdict unresolved")
                        seen.add(child)
                        available.append(child)
            branches[belief] = options
        rank = {b: 0 for b in available if len({claims[o] for o, _ in b}) == 1}
        choices = {}
        while True:
            new = []
            for b in available:
                if b in rank:
                    continue
                possible = [(1 + max(rank[child] for child in children), action)
                            for action, children in branches[b].items()
                            if all(child in rank for child in children)]
                if possible:
                    new.append((b, *min(possible)))
            if not new:
                break
            for b, val, act in new:
                rank[b] = val
                choices[b] = act
        if root not in rank:
            return {"status": "NO_UNIFORM_FINITE_POLICY", "rank": None,
                    "reachable_beliefs": len(available), "winning_beliefs": len(rank),
                    "necessary_quotient": self.claim_quotient(claims)["status"]}
        return {"status": "FINITE_WINNING_POLICY", "rank": rank[root],
                "reachable_beliefs": len(available), "winning_beliefs": len(rank),
                "root_action": choices.get(root), "necessary_quotient": self.claim_quotient(claims)["status"]}


def destructive_parity_model() -> tuple[ControlledCarrier, dict[tuple[int, int], int]]:
    """Pairwise separable original states, but neither first action is safe.

    READ_A erases the b bit; READ_B erases the a bit. All states have
    both actions. Original parity must be proved about the original bits.
    """
    states = tuple((a, b) for a in range(2) for b in range(2))
    rows = {}
    for a, b in states:
        rows[(a, b), "READ_A"] = (a, (a, 0))
        rows[(a, b), "READ_B"] = (b, (0, b))
    carrier = ControlledCarrier("source:parity-original", states,
                                ("READ_A", "READ_B"), rows)
    return carrier, {(a, b): a ^ b for a, b in states}


def ontology_alias_model(*, allow_separator: bool = False) -> tuple[ControlledCarrier, dict]:
    """An 'internal' and 'external' ontology with identical lawful behavior.

    Additional certified separator changes the observation category and
    breaks the equivalence; source labels alone do not.
    """
    states = ("inside", "outside")
    acts = ("OBS", "PING") + (("SEPARATOR",) if allow_separator else ())
    rows = {}
    for s in states:
        for a in acts:
            rows[s, a] = (int(s == "outside") if a == "SEPARATOR" else "same", s)
    return ControlledCarrier("one observed carrier, two hypotheses", states, acts, rows), {
        "inside": "internal", "outside": "external"}
