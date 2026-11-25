"""Principia: source-faithful causal memory and minimal future-target compression.

A mathematical model of finite deterministic interventions, not a sensor or a
probability model. Its 'worlds' are possible original sources, not information
available to the observer. Exhaustive source replay certifies a claimed memory.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json


class CausalSourceError(ValueError):
    """The carrier, the remembered observations, or a proof receipt is invalid."""


@dataclass(frozen=True)
class Carrier:
    name: str
    worlds: tuple[str, ...]
    states: tuple[str, ...]
    actions: tuple[str, ...]
    origins: tuple[str, ...]  # by world index
    outputs: tuple[str, ...]  # by state index
    targets: tuple[str, ...]  # by original world index
    transitions: tuple[tuple[str, ...], ...]  # action x state -> state
    costs: tuple[int, ...]  # action costs; 0 is ideal mathematical null cost


def carrier(name: str, worlds, states, actions, origins, outputs, targets,
            transitions, costs=None) -> Carrier:
    c = Carrier(str(name), tuple(worlds), tuple(states), tuple(actions),
                tuple(origins), tuple(outputs), tuple(targets),
                tuple(tuple(row) for row in transitions),
                tuple(costs) if costs is not None else tuple(1 for _ in actions))
    validate_carrier(c)
    return c


def validate_carrier(c: Carrier) -> None:
    if not c.name or not c.worlds or not c.states or not c.actions:
        raise CausalSourceError('source, worlds, states and actions must be nonempty')
    for labels in (c.worlds, c.states, c.actions):
        if any(type(x) is not str or not x for x in labels) or len(set(labels)) != len(labels):
            raise CausalSourceError('malformed or duplicated source label')
    if len(c.origins) != len(c.worlds) or len(c.targets) != len(c.worlds):
        raise CausalSourceError('original world/source contract is incomplete')
    if len(c.outputs) != len(c.states) or len(c.transitions) != len(c.actions):
        raise CausalSourceError('observation/transition contract incomplete')
    if len(c.costs) != len(c.actions) or any(type(x) is not int or x < 0 for x in c.costs):
        raise CausalSourceError('unlicensed or negative intervention cost')
    if any(type(x) is not str for x in c.targets + c.outputs):
        raise CausalSourceError('non-symbolic target/output')
    if any(q not in c.states for q in c.origins):
        raise CausalSourceError('source begins outside carrier')
    for row in c.transitions:
        if len(row) != len(c.states) or any(q not in c.states for q in row):
            raise CausalSourceError('non-total or out-of-carrier causal action')


def passport(c: Carrier) -> str:
    validate_carrier(c)
    # An integrity fingerprint of a DECLARED mathematical source, not external authentication.
    data = [c.name, c.worlds, c.states, c.actions, c.origins,
            c.outputs, c.targets, c.transitions, c.costs]
    return sha256(json.dumps(data, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()


def observation(c: Carrier, state: str) -> str:
    return c.outputs[c.states.index(state)]


def apply(c: Carrier, state: str, action: str) -> str:
    if action not in c.actions or state not in c.states:
        raise CausalSourceError('illegal source action/state')
    return c.transitions[c.actions.index(action)][c.states.index(state)]


@dataclass(frozen=True)
class Step:
    action: str
    outcome: str


@dataclass(frozen=True)
class CausalMemory:
    source: str
    first_report: str
    steps: tuple[Step, ...]
    coupling: tuple[tuple[str, str], ...]  # (original world, current source state)


def reconstruct_coupling(c: Carrier, first_report: str,
                         steps: tuple[Step, ...]) -> tuple[tuple[str, str], ...]:
    rows = tuple((w, q) for w, q in zip(c.worlds, c.origins)
                 if observation(c, q) == first_report)
    for step in steps:
        if step.action not in c.actions or type(step.outcome) is not str:
            raise CausalSourceError('invalid remembered action/outcome')
        rows = tuple((w, apply(c, q, step.action)) for w, q in rows
                     if observation(c, apply(c, q, step.action)) == step.outcome)
    if not rows:
        raise CausalSourceError('remembered observation impossible under source')
    return rows


def initial_memory(c: Carrier, initial_report: str) -> CausalMemory:
    rows = reconstruct_coupling(c, initial_report, ())
    return CausalMemory(passport(c), initial_report, (), rows)


def verify_memory(c: Carrier, memory: CausalMemory) -> tuple[tuple[str, str], ...]:
    if memory.source != passport(c):
        raise CausalSourceError('source law changed without transported passport')
    rows = reconstruct_coupling(c, memory.first_report, memory.steps)
    if memory.coupling != rows:
        raise CausalSourceError('causal coupling was forged or lost')
    return rows


def step_memory(c: Carrier, memory: CausalMemory, action: str, outcome: str) -> CausalMemory:
    rows = verify_memory(c, memory)
    if action not in c.actions:
        raise CausalSourceError('unlicensed action')
    successor = tuple((w, apply(c, q, action)) for w, q in rows
                      if observation(c, apply(c, q, action)) == outcome)
    if not successor:
        raise CausalSourceError('impossible actual observation')
    candidate = CausalMemory(passport(c), memory.first_report,
                             memory.steps + (Step(action, outcome),), successor)
    verify_memory(c, candidate)
    return candidate


def response_paths(c: Carrier, memory: CausalMemory, word: tuple[str, ...]):
    """Source-coupled TARGET + counterfactual response, per same original world.

    Counterfactual bank does not assert that incompatible action sequences were
    actually run on a single copy. For that, solve a licensed policy below.
    """
    rows = verify_memory(c, memory)
    if any(a not in c.actions for a in word):
        raise CausalSourceError('counterfactual uses an illegal action')
    response = []
    for w, q in rows:
        current = q
        answers = []
        for action in word:
            current = apply(c, current, action)
            answers.append(observation(c, current))
        response.append((w, c.targets[c.worlds.index(w)], tuple(answers)))
    return tuple(response)


def joint_potential_outcomes(c: Carrier, memory: CausalMemory,
                             words: tuple[tuple[str, ...], ...]):
    """Retain how different *counterfactuals* are coupled by original worlds."""
    verify_memory(c, memory)
    predictions = tuple(response_paths(c, memory, word) for word in words)
    return tuple((w, target, tuple(table[i][2] for table in predictions))
                 for i, (w, target, _) in enumerate(predictions[0])) if words else tuple(
                     (w, c.targets[c.worlds.index(w)], ()) for w, _ in memory.coupling)


def reachable_atoms(c: Carrier) -> tuple[tuple[str, str], ...]:
    """Reachable marked states (original world, current carrier state)."""
    validate_carrier(c)
    reachable = set()
    for w, initial in zip(c.worlds, c.origins):
        todo = [initial]
        seen = {initial}
        while todo:
            q = todo.pop()
            reachable.add((w, q))
            for action in c.actions:
                next_q = apply(c, q, action)
                if next_q not in seen:
                    seen.add(next_q)
                    todo.append(next_q)
    return tuple(sorted(reachable))


def _target_of(c: Carrier, atom: tuple[str, str]) -> str:
    return c.targets[c.worlds.index(atom[0])]


def _colored(keys: tuple) -> tuple[int, ...]:
    mapping = {}
    out = []
    for key in keys:
        if key not in mapping:
            mapping[key] = len(mapping)
        out.append(mapping[key])
    return tuple(out)


@dataclass(frozen=True)
class FutureQuotient:
    source: str
    atoms: tuple[tuple[str, str], ...]
    colors: tuple[int, ...]
    dimensions: tuple[int, ...]  # partition sizes, not probability/mass


def future_quotient(c: Carrier) -> FutureQuotient:
    """Finite Moore refinement of target-and-future-response equivalence."""
    atoms = reachable_atoms(c)
    index = {atom: i for i, atom in enumerate(atoms)}
    colors = _colored(tuple((_target_of(c, atom), observation(c, atom[1])) for atom in atoms))
    dimensions = [len(set(colors))]
    while True:
        keys = tuple((colors[i], tuple(colors[index[(atom[0], apply(c, atom[1], a))]]
                                     for a in c.actions)) for i, atom in enumerate(atoms))
        new = _colored(keys)
        if new == colors:
            break
        colors = new
        dimensions.append(len(set(colors)))
        if len(dimensions) > len(atoms):
            raise CausalSourceError('partition failed to stabilize within finite bound')
    return FutureQuotient(passport(c), atoms, colors, tuple(dimensions))


def verify_future_quotient(c: Carrier, q: FutureQuotient) -> FutureQuotient:
    """Independent pair-distinguishability least-fixed-point check, not Moore."""
    if q.source != passport(c) or q.atoms != reachable_atoms(c):
        raise CausalSourceError('wrong quotient source or reachable carrier')
    if len(q.colors) != len(q.atoms) or len(q.dimensions) < 1:
        raise CausalSourceError('ill-typed quotient')
    atoms = q.atoms
    # Counterpart to Moore: saturate the relation of DISTINCT observable futures.
    different = set()
    for i, a in enumerate(atoms):
        for j in range(i + 1, len(atoms)):
            b = atoms[j]
            if (_target_of(c, a), observation(c, a[1])) != (_target_of(c, b), observation(c, b[1])):
                different.add((i, j))
    lookup = {atom: i for i, atom in enumerate(atoms)}
    while True:
        change = set()
        for i, a in enumerate(atoms):
            for j in range(i + 1, len(atoms)):
                if (i, j) in different:
                    continue
                b = atoms[j]
                for act in c.actions:
                    x = lookup[(a[0], apply(c, a[1], act))]
                    y = lookup[(b[0], apply(c, b[1], act))]
                    if tuple(sorted((x, y))) in different:
                        change.add((i, j))
                        break
        if not change:
            break
        different.update(change)
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            if (q.colors[i] == q.colors[j]) != ((i, j) not in different):
                raise CausalSourceError('incorrect future-target behavioral quotient')
    if q.dimensions != future_quotient(c).dimensions:
        raise CausalSourceError('forged knowledge-volume refinement history')
    return q


def shortest_distinguishing_path(c: Carrier, a: tuple[str, str],
                                 b: tuple[str, str]) -> tuple[str, ...] | None:
    """A legal word witnessing distinct target or future readout, or None."""
    from collections import deque
    reachable = set(reachable_atoms(c))
    if a not in reachable or b not in reachable:
        raise CausalSourceError('unreachable marked source state')
    queue = deque([(a, b, ())])
    seen = {(a, b)}
    while queue:
        x, y, word = queue.popleft()
        if (_target_of(c, x), observation(c, x[1])) != (_target_of(c, y), observation(c, y[1])):
            return word
        for action in c.actions:
            xx = (x[0], apply(c, x[1], action))
            yy = (y[0], apply(c, y[1], action))
            if (xx, yy) not in seen:
                seen.add((xx, yy))
                queue.append((xx, yy, word + (action,)))
    return None


def strong_future_null(c: Carrier, m: CausalMemory, action: str,
                       q: FutureQuotient | None = None) -> bool:
    """Zero-cost, observationally silent and future-target-neutral at current source.

    This ignores the mere addition of the sham *action label* to an immutable
    archival log; it preserves every declared target/future response. It is not
    strong-null for a toolkit that treats the action record itself as target.
    """
    rows = verify_memory(c, m)
    if action not in c.actions or c.costs[c.actions.index(action)] != 0:
        return False
    q = verify_future_quotient(c, q or future_quotient(c))
    index = {atom: color for atom, color in zip(q.atoms, q.colors)}
    return all(observation(c, apply(c, state, action)) == observation(c, state)
               and index[(w, state)] == index[(w, apply(c, state, action))]
               for w, state in rows)


@dataclass(frozen=True)
class Policy:
    action: str | None
    answer: str | None
    branches: tuple[tuple[str, 'Policy'], ...] = ()


def find_target_policy(c: Carrier, m: CausalMemory, depth: int,
                       allowed: tuple[str, ...] | None = None) -> Policy | None:
    """AND/OR synthesis for an actual one-copy finite observation policy.

    Depth counts interventions, not analytic complexity or physical cost.
    """
    rows = verify_memory(c, m)
    if not isinstance(depth, int) or depth < 0:
        raise CausalSourceError('invalid finite intervention depth')
    allowed = c.actions if allowed is None else tuple(allowed)
    if any(a not in c.actions for a in allowed) or len(set(allowed)) != len(allowed):
        raise CausalSourceError('unlicensed or duplicated action budget')

    @lru_cache(maxsize=None)
    def solve(links: tuple[tuple[str, str], ...], remaining: int) -> Policy | None:
        target_set = {_target_of(c, (w, q)) for w, q in links}
        if len(target_set) == 1:
            return Policy(None, next(iter(target_set)))
        if not remaining:
            return None
        for action in allowed:
            outcomes = {}
            for w, q in links:
                nxt = apply(c, q, action)
                outcomes.setdefault(observation(c, nxt), []).append((w, nxt))
            children = []
            for y, successors in sorted(outcomes.items()):
                sub = solve(tuple(successors), remaining - 1)
                if sub is None:
                    break
                children.append((y, sub))
            else:
                return Policy(action, None, tuple(children))
        return None
    return solve(rows, depth)


def verify_target_policy(c: Carrier, m: CausalMemory, policy: Policy,
                         allowed: tuple[str, ...] | None = None,
                         max_depth: int | None = None) -> int:
    """Independently verify every branch and each original-source target.

    A purported decision tree must have exactly the source-possible branches;
    neither an untested favorable outcome nor an invented branch certifies it.
    """
    rows = verify_memory(c, m)
    legal = set(c.actions if allowed is None else allowed)
    if not legal <= set(c.actions) or (max_depth is not None and max_depth < 0):
        raise CausalSourceError('unlicensed policy toolkit/budget')

    def prove(links: tuple[tuple[str, str], ...], node: Policy, depth: int) -> int:
        if node.action is None:
            target_set = {_target_of(c, pair) for pair in links}
            if len(target_set) != 1 or node.answer not in target_set or node.branches:
                raise CausalSourceError('leaf does not identify original source target')
            return 0
        if node.action not in legal or node.answer is not None:
            raise CausalSourceError('illegal action or premature target answer')
        if max_depth is not None and depth >= max_depth:
            raise CausalSourceError('policy exceeds admitted action depth')
        branches = {}
        for w, q in links:
            next_q = apply(c, q, node.action)
            branches.setdefault(observation(c, next_q), []).append((w, next_q))
        supplied = dict(node.branches)
        if len(supplied) != len(node.branches) or set(supplied) != set(branches):
            raise CausalSourceError('forged, missing, or duplicated outcome branch')
        return 1 + max(prove(tuple(worlds), supplied[y], depth + 1)
                       for y, worlds in branches.items())
    return prove(rows, policy, 0)


def gaussian_theta_null_carrier() -> Carrier:
    """Two zero reports, one from CM rotation, one from an empty norm shell.

    All values derive from the existing exact Z[i] theta-shell implementation.
    The 'lift' is a change of *holomorphic derivative probe order* on the
    immutable mathematical source, not a claim to physically alter the lattice.
    """
    from .principia_cm_theta import theta_shell_moment
    norms = (2, 3)
    initial = tuple(str(theta_shell_moment(n, 2)) for n in norms)
    lifted = tuple(str(theta_shell_moment(n, 4)) for n in norms)
    states = ('n2-jet2', 'n3-jet2', 'n2-jet4', 'n3-jet4')
    return carrier('actual-Gaussian-integer-theta-null-jet-coupling',
                   ('norm2-rotation', 'norm3-empty'), states,
                   ('repeat', 'lift'), states[:2], initial + lifted,
                   ('rotation-cancellation', 'absent-shell'),
                   (states, (states[2], states[3], states[2], states[3])),
                   costs=(0, 1))
