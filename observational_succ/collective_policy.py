"""Exact chronological finite AND/OR planning over DECLARED joint carriers.

Beliefs retain (original-source index, current-joint-state index). Actions are
chosen from public histories, uniformly executable throughout a belief, and
every supported outcome must win. State indices, private registers, original
labels and offered menus are not policy observations. No source authentication
or physical implementation follows from a finite transition table.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from itertools import combinations, product
import json
from typing import Mapping


class CollectivePolicyError(ValueError):
    """Invalid finite contract or unsound policy certificate."""


class SearchLimit(CollectivePolicyError):
    """Computational exhaustion, never a certificate of losing."""


def _label(value, what):
    if type(value) is not str or not value:
        raise CollectivePolicyError(f"nonempty {what} required")


@dataclass(frozen=True, order=True)
class Cost:
    """Nonnegative path costs; certificate counts declared verification units.

    Depth counts public decisions, actions count physical primitives, messages
    count sends, communication_bits count fixed-width payload bits (framing
    excluded), observation_bits count public/private readout alphabet bits.
    Certificate work is neither tree size nor a claim about Kolmogorov cost.
    """
    depth: int = 0
    actions: int = 0
    messages: int = 0
    communication_bits: int = 0
    observation_bits: int = 0
    certificate: int = 0

    def __post_init__(self):
        if any(type(v) is not int or v < 0 for v in self.vector):
            raise CollectivePolicyError("cost coordinates must be exact naturals")

    @property
    def vector(self):
        return (self.depth, self.actions, self.messages, self.communication_bits,
                self.observation_bits, self.certificate)

    def fits(self, budget: Cost) -> bool:
        return all(a <= b for a, b in zip(self.vector, budget.vector))

    def __add__(self, other: Cost) -> Cost:
        return Cost(*(a + b for a, b in zip(self.vector, other.vector)))

    def __sub__(self, other: Cost) -> Cost:
        return Cost(*(a - b for a, b in zip(self.vector, other.vector)))


@dataclass(frozen=True)
class Source:
    name: str
    target: str

    def __post_init__(self):
        _label(self.name, "original source label")
        _label(self.target, "original source target")


@dataclass(frozen=True)
class JointState:
    """Actual carrier, E-local registers/control, and physical resource stock.

    These are model audit values, not automatically public observations.
    Different original sources may lead to the very same JointState.
    """
    carrier: str
    local: tuple[str, ...]
    resources: tuple[int, ...] = ()

    def __post_init__(self):
        _label(self.carrier, "current carrier")
        if type(self.local) is not tuple or any(type(s) is not str or not s for s in self.local):
            raise CollectivePolicyError("immutable local register labels required")
        if type(self.resources) is not tuple or any(type(n) is not int or n < 0 for n in self.resources):
            raise CollectivePolicyError("physical resource vector must contain exact naturals")


@dataclass(frozen=True, order=True)
class Outcome:
    public: str
    after: int
    readout: str | None = None

    def __post_init__(self):
        _label(self.public, "public outcome")
        if type(self.after) is not int or self.after < 0:
            raise CollectivePolicyError("next joint state must be an index")
        if self.readout is not None:
            _label(self.readout, "actor-private readout")


@dataclass(frozen=True)
class Action:
    name: str
    actor: str
    kind: str
    cost: Cost
    rows: tuple[tuple[Outcome, ...], ...]
    receiver: str | None = None

    def __post_init__(self):
        _label(self.name, "action")
        _label(self.actor, "actor")
        if self.kind not in ("probe", "move", "message") or not isinstance(self.cost, Cost):
            raise CollectivePolicyError("typed action kind and cost required")
        if self.cost.depth != 1:
            raise CollectivePolicyError("each action consumes exactly one decision depth")
        if self.kind == "message":
            _label(self.receiver, "message receiver")
            if (self.receiver == self.actor or self.cost.messages != 1 or self.cost.actions
                    or self.cost.observation_bits):
                raise CollectivePolicyError("one explicit send, distinct recipient, no physical primitive")
        elif (self.receiver is not None or self.cost.messages or self.cost.communication_bits or self.cost.actions < 1):
            raise CollectivePolicyError("physical actions and communication costs are separate")
        if type(self.rows) is not tuple or any(
            type(row) is not tuple or any(not isinstance(o, Outcome) for o in row)
            or len(set(row)) != len(row) for row in self.rows
        ):
            raise CollectivePolicyError("immutable nondeterministic support rows required")


# Every pair resolves against the complete, explicit source and state tables.
Belief = tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class CollectiveModel:
    source_id: str
    target_id: str
    observers: tuple[str, ...]
    sources: tuple[Source, ...]
    states: tuple[JointState, ...]
    initial: Belief
    actions: tuple[Action, ...]
    leaf_cost: Cost = Cost(certificate=1)

    def __post_init__(self):
        _label(self.source_id, "declared source namespace")
        _label(self.target_id, "target identity")
        if (type(self.observers) is not tuple or not self.observers or
                any(type(x) is not str or not x for x in self.observers) or
                len(set(self.observers)) != len(self.observers)):
            raise CollectivePolicyError("unique finite E identities required")
        for items, cls in ((self.sources, Source), (self.states, JointState), (self.actions, Action)):
            if type(items) is not tuple or any(not isinstance(x, cls) for x in items):
                raise CollectivePolicyError("immutable typed finite model tables required")
        if not self.sources or not self.states or len({s.name for s in self.sources}) != len(self.sources):
            raise CollectivePolicyError("nonempty sources/states and unique source identities required")
        if len(set(self.states)) != len(self.states):
            raise CollectivePolicyError("duplicate joint states must be identified explicitly")
        if any(len(s.local) != len(self.observers) or
               len(s.resources) != len(self.states[0].resources) for s in self.states):
            raise CollectivePolicyError("joint state/register/resource dimensions disagree")
        if (not isinstance(self.leaf_cost, Cost) or
                any(self.leaf_cost.vector[:5])):
            raise CollectivePolicyError("leaf certification has certificate work only")
        if type(self.initial) is not tuple or not self.initial:
            raise CollectivePolicyError("nonempty initial original/current relation required")
        for pair in self.initial:
            if (type(pair) is not tuple or len(pair) != 2 or
                    any(type(v) is not int for v in pair) or
                    not 0 <= pair[0] < len(self.sources) or not 0 <= pair[1] < len(self.states)):
                raise CollectivePolicyError("invalid original/current preparation pair")
        if tuple(sorted(set(self.initial))) != self.initial or {s for s, _ in self.initial} != set(range(len(self.sources))):
            raise CollectivePolicyError("canonical preparation relation must cover every declared source")
        if len({a.name for a in self.actions}) != len(self.actions):
            raise CollectivePolicyError("action names must be unique")
        for action in self.actions:
            if (action.actor not in self.observers or
                    (action.receiver is not None and action.receiver not in self.observers) or
                    len(action.rows) != len(self.states) or
                    any(o.after >= len(self.states) for row in action.rows for o in row)):
                raise CollectivePolicyError("action table outside declared joint carrier")
            if action.kind == "message":
                self._validate_message(action)
            else:
                self._validate_readouts(action)

    def _validate_readouts(self, action):
        alphabet, updates = set(), {}
        actor = self.observers.index(action.actor)
        for state, row in zip(self.states, action.rows):
            for outcome in row:
                alphabet.add((outcome.public, outcome.readout))
                after = self.states[outcome.after]
                # Local memories cannot secretly acquire a source distinction
                # missing from the declared public/private readout alphabet.
                for i, old in enumerate(state.local):
                    key = (i, old, outcome.public, outcome.readout if i == actor else None)
                    if updates.setdefault(key, after.local[i]) != after.local[i]:
                        raise CollectivePolicyError("local update uses an undeclared readout")
        if max(0, len(alphabet) - 1).bit_length() > action.cost.observation_bits:
            raise CollectivePolicyError("fixed-width observation alphabet undercharged")

    def _validate_message(self, action):
        """A send reads only sender memory; reception reads only message + old memory.

        The global scheduler still requires uniform legality. Resource changes
        remain declared table assumptions; their actual values are not public.
        """
        sender, receiver = self.observers.index(action.actor), self.observers.index(action.receiver)
        encoder, decoder = {}, {}
        alphabet = set()
        for state, row in zip(self.states, action.rows):
            if not row:
                continue
            if len(row) != 1:
                raise CollectivePolicyError("message adapter requires a deterministic reliable channel")
            outcome = row[0]
            if outcome.readout is not None:
                raise CollectivePolicyError("message cannot introduce a new private sensor readout")
            after = self.states[outcome.after]
            key = state.local[sender]
            if encoder.setdefault(key, outcome.public) != outcome.public:
                raise CollectivePolicyError("message peeks beyond sender local memory")
            key = (state.local[receiver], outcome.public)
            if decoder.setdefault(key, after.local[receiver]) != after.local[receiver]:
                raise CollectivePolicyError("receiver state uses hidden information beyond the message")
            if after.carrier != state.carrier or any(
                    after.local[i] != state.local[i] for i in range(len(self.observers)) if i != receiver):
                raise CollectivePolicyError("send may update recipient and resources, not source/other memories")
            alphabet.add(outcome.public)
        if (max(0, len(alphabet) - 1)).bit_length() > action.cost.communication_bits:
            raise CollectivePolicyError("fixed-width message payload undercharged")


@dataclass(frozen=True)
class Policy:
    """Public outcome tree. Its node position is the complete public history."""
    action: str | None = None
    claim: str | None = None
    branches: tuple[tuple[str, Policy], ...] = ()

    def at(self, history: tuple[tuple[str, str], ...]) -> Policy:
        if type(history) is not tuple:
            raise CollectivePolicyError("public history must be an immutable event sequence")
        node = self
        for name, public in history:
            if node.action != name or public not in dict(node.branches):
                raise CollectivePolicyError("history is not a policy execution")
            node = dict(node.branches)[public]
        return node


@dataclass(frozen=True)
class PolicyResult:
    budget: Cost
    root_belief: Belief
    explored: int
    policy: Policy | None

    @property
    def winning(self):
        return self.policy is not None


def _claim(model, belief):
    labels = {model.sources[s].target for s, _ in belief}
    return next(iter(labels)) if len(labels) == 1 else None


def _branches(action, belief):
    if any(not action.rows[c] for _, c in belief):
        return None
    by_public = {}
    for original, current in belief:
        for outcome in action.rows[current]:
            by_public.setdefault(outcome.public, set()).add((original, outcome.after))
    return tuple((public, tuple(sorted(pairs))) for public, pairs in sorted(by_public.items()))


def solve_collective_policy(model: CollectiveModel, budget: Cost, *, max_nodes: int = 100000) -> PolicyResult:
    """Complete bounded reachability followed by exact bottom-up AND/OR search.

    OR over uniformly legal, affordable actions; AND over ALL public outcomes
    and all hidden poststates sharing each outcome. No fairness assumption.
    max_nodes bounds computation; hitting it raises, rather than returning LOSS.
    """
    if not isinstance(model, CollectiveModel) or not isinstance(budget, Cost):
        raise CollectivePolicyError("typed model and budget required")
    if type(max_nodes) is not int or max_nodes < 1:
        raise CollectivePolicyError("positive search-state limit required")
    root = (model.initial, budget)
    nodes, seen, edges = [root], {root}, {}
    for key in nodes:
        belief, remaining = key
        options = []
        if _claim(model, belief) is None:
            for action in sorted(model.actions, key=lambda a: a.name):
                if not action.cost.fits(remaining):
                    continue
                branches = _branches(action, belief)
                if branches is None:
                    continue
                rest = remaining - action.cost
                successors = tuple((public, (child, rest)) for public, child in branches)
                options.append((action.name, successors))
                for _, child in successors:
                    if child not in seen:
                        if len(seen) >= max_nodes:
                            raise SearchLimit("finite planner state limit exhausted; result UNKNOWN")
                        seen.add(child)
                        nodes.append(child)
        edges[key] = options
    winners = {}
    for key in sorted(nodes, key=lambda k: k[1].depth):
        belief, remaining = key
        claim = _claim(model, belief)
        if claim is not None and model.leaf_cost.fits(remaining):
            winners[key] = Policy(claim=claim)
        else:
            for name, branches in edges[key]:
                if all(child in winners for _, child in branches):
                    winners[key] = Policy(action=name, branches=tuple(
                        (public, winners[child]) for public, child in branches))
                    break
    return PolicyResult(budget, model.initial, len(nodes), winners.get(root))


@dataclass(frozen=True)
class ReplayLeaf:
    original: str
    current: JointState
    history: tuple[tuple[str, str], ...]
    claim: str
    cost: Cost


@dataclass(frozen=True)
class Replay:
    leaves: tuple[ReplayLeaf, ...]
    policy_nodes: int
    public_leaves: int
    concrete_prefixes: int

    @property
    def worst_cost(self):
        return Cost(*(max(leaf.cost.vector[i] for leaf in self.leaves) for i in range(6)))


def replay_policy(model: CollectiveModel, budget: Cost, policy: Policy, *, max_prefixes: int = 100000) -> Replay:
    """Independent certificate interpreter on raw concrete runs, not solver edges.

    Enumerates every nondeterministic run without merging equal hidden states.
    Recomputes legality, costs, public branch coverage and each original target.
    Privileged audit states never become arguments to policy action selection.
    """
    if not isinstance(model, CollectiveModel) or not isinstance(budget, Cost) or not isinstance(policy, Policy):
        raise CollectivePolicyError("typed model/budget/policy required for replay")
    if type(max_prefixes) is not int or max_prefixes < 1:
        raise CollectivePolicyError("positive replay limit required")
    queue = [(policy, model.initial, (), Cost())]
    leaves, nodes, public_leaves, prefixes = [], 0, 0, 0
    actions = {a.name: a for a in model.actions}
    for node, runs, history, spent in queue:
        nodes += 1
        prefixes += len(runs)
        if prefixes > max_prefixes:
            raise SearchLimit("concrete replay limit exhausted; verification incomplete")
        if not isinstance(node, Policy) or type(node.branches) is not tuple:
            raise CollectivePolicyError("malformed policy node")
        if node.action is None:
            total = spent + model.leaf_cost
            if node.branches or not total.fits(budget):
                raise CollectivePolicyError("invalid or overbudget terminal certificate")
            for source, current in runs:
                if node.claim != model.sources[source].target:
                    raise CollectivePolicyError("false ORIGINAL-source claim")
                leaves.append(ReplayLeaf(model.sources[source].name, model.states[current], history, node.claim, total))
            public_leaves += 1
            continue
        if node.claim is not None or node.action not in actions:
            raise CollectivePolicyError("invalid action/certificate node")
        action = actions[node.action]
        total = spent + action.cost
        if not total.fits(budget):
            raise CollectivePolicyError("action exceeds an independent path budget")
        groups = {}
        for source, current in runs:
            row = action.rows[current]
            if not row:
                raise CollectivePolicyError("action illegal in a compatible current state")
            for outcome in row:
                groups.setdefault(outcome.public, []).append((source, outcome.after))
        if any(type(b) is not tuple or len(b) != 2 or type(b[0]) is not str for b in node.branches):
            raise CollectivePolicyError("malformed public policy branches")
        continuations = dict(node.branches)
        if len(continuations) != len(node.branches) or set(continuations) != set(groups):
            raise CollectivePolicyError("missing, duplicated, or fictional public outcome branch")
        for public, next_runs in sorted(groups.items()):
            queue.append((continuations[public], tuple(next_runs), history + ((action.name, public),), total))
    return Replay(tuple(leaves), nodes, public_leaves, prefixes)


def restrict_observers(model: CollectiveModel, active: tuple[str, ...]) -> CollectiveModel:
    """Ablate action owners AND communication endpoints, preserving the carrier."""
    if type(active) is not tuple or len(set(active)) != len(active) or not set(active) <= set(model.observers):
        raise CollectivePolicyError("invalid active E subset")
    return replace(model, actions=tuple(a for a in model.actions if a.actor in active and
                   (a.receiver is None or a.receiver in active)))


def cross_enabled_model() -> CollectiveModel:
    """p0(A), send, p1(B), send, p2(A), send, p3(B), send.

    Even predictable 'same' results must be performed to put the required token
    into sender memory. The final source bit is private until the fourth send.
    """
    locals_by_phase = lambda s: (
        ("ready:p0", "locked"), ("obs:p0", "locked"),
        ("obs:p0", "ready:p1"), ("obs:p0", "obs:p1"),
        ("ready:p2", "obs:p1"), ("obs:p2", "obs:p1"),
        ("obs:p2", "ready:p3"), ("obs:p2", "obs:p3:" + s),
        ("received:" + s, "obs:p3:" + s))
    states = tuple(JointState(s, local, (8 - phase,)) for s in ("0", "1")
                   for phase, local in enumerate(locals_by_phase(s)))
    actions = []
    for phase in range(8):
        rung = phase // 2
        actor = "A" if rung % 2 == 0 else "B"
        message = phase % 2 == 1
        rows = tuple((Outcome(s if phase == 7 else "recorded", i + 1,
                              s if phase == 6 else None),)
                     if i % 9 == phase else () for i, s in enumerate(st.carrier for st in states))
        actions.append(Action(
            f"send:p{rung}" if message else f"p{rung}", actor,
            "message" if message else "probe",
            Cost(depth=1, actions=0 if message else 1, messages=int(message),
                 communication_bits=int(phase == 7), observation_bits=int(phase == 6), certificate=1), rows,
            ("B" if actor == "A" else "A") if message else None))
    return CollectiveModel("declared-cross-enabled-v1", "original-bit", ("A", "B"),
                           (Source("s0", "0"), Source("s1", "1")), states,
                           ((0, 0), (1, 9)), tuple(actions))


def capacity_parity_model(bits: int, capacity: int) -> CollectiveModel:
    """Each public probe reads one bit once and consumes one shared token.

    Capacity 1 on 2 bits: mutually exclusive histories. Capacity 2 on 3 bits:
    every pair is sequentially available, but no triple is executable.
    """
    if type(bits) is not int or type(capacity) is not int or not 1 <= bits <= 4 or not 0 <= capacity <= bits:
        raise CollectivePolicyError("small exact bit/capacity fixture required")
    words = tuple("".join(w) for w in product("01", repeat=bits))
    subsets = tuple(s for k in range(capacity + 1) for s in combinations(range(bits), k))
    states = tuple(JointState(w, tuple(w[i] if i in seen else "unread" for i in range(bits)),
                              (capacity - len(seen),)) for w in words for seen in subsets)
    indices = {state: i for i, state in enumerate(states)}
    actions = []
    for i in range(bits):
        rows = []
        for state in states:
            if not state.resources[0] or state.local[i] != "unread":
                rows.append(())
                continue
            local = list(state.local)
            local[i] = state.carrier[i]
            after = JointState(state.carrier, tuple(local), (state.resources[0] - 1,))
            rows.append((Outcome(state.carrier[i], indices[after]),))
        actions.append(Action(f"p{i}", f"E{i}", "probe", Cost(1, 1, observation_bits=1, certificate=1), tuple(rows)))
    return CollectiveModel(f"declared-capacity-{bits}-{capacity}", "original-parity",
                           tuple(f"E{i}" for i in range(bits)),
                           tuple(Source(w, str(sum(map(int, w)) % 2)) for w in words), states,
                           tuple((i, i * len(subsets)) for i in range(len(words))), tuple(actions))


def miniport_model(port, passport, targets: Mapping[str, str]) -> tuple[CollectiveModel, dict]:
    """Validate a real MiniPort, then execute its actual parent macros.

    At each primitive endpoint translate the PARENT public report; never expose
    the hidden factor decoder. Empty macros explicitly read the current report.
    This provides a finite source-table realization, not physical calibration.
    """
    from .consensus_lambda import MiniPort
    if not isinstance(port, MiniPort):
        raise CollectivePolicyError("actual consensus_lambda.MiniPort required")
    receipt = port.validate(passport)
    parent = port.parent
    if set(targets) != set(parent.preparations):
        raise CollectivePolicyError("target table must label exactly the actual preparations")
    states = tuple(JointState(c, ("ready",)) for c in parent.states)
    index = {state.carrier: i for i, state in enumerate(states)}
    actions = []
    for name, word in sorted(port.macros.items()):
        rows = []
        for state in states:
            current, public = state.carrier, []
            for primitive in word:
                current = parent.actions[primitive][current]
                if current is None:
                    raise CollectivePolicyError("validated macro became unavailable")
                public.append(port.public_map[parent.reports[current]])
            if not word:
                public.append(port.public_map[parent.reports[current]])
            rows.append((Outcome(json.dumps(public, separators=(",", ":")), index[current]),))
        alphabet = {outcome.public for row in rows for outcome in row}
        actions.append(Action("mini:" + name, "E", "probe",
                              Cost(1, max(1, len(word)), observation_bits=(len(alphabet) - 1).bit_length(),
                                   certificate=1), tuple(rows)))
    model = CollectiveModel(parent.source_id, "prepared-source-target", ("E",),
                            tuple(Source(c, targets[c]) for c in parent.preparations), states,
                            tuple((i, index[c]) for i, c in enumerate(parent.preparations)), tuple(actions))
    return model, {"factor": receipt, "passport": asdict(passport), "public_macro_histories_exposed": True,
                   "physical_authentication": False, "hidden_decoder_exposed": False}


def policy_wire(policy: Policy) -> dict:
    """Deterministic, public-only serialized certificate tree."""
    return asdict(policy)
