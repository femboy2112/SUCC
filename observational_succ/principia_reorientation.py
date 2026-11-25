"""Principia reorientation: exact recovery of present or original position.

Finite source: the original-world/current-state coupling of Principia causal
memory. A minimax attractor over possible source beliefs constructs a lawful
policy with a strictly decreasing worst-case rank; no empirical source or
continuous/infinite theorem is inferred from finite tests.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Literal

from .principia_causal_memory import (
    Carrier, CausalMemory, CausalSourceError, apply, initial_memory,
    observation, passport, verify_memory,
)


class ReorientationError(ValueError):
    """Invalid target/source, policy, or impossible observed transition."""


# A pair retains original source identity even when current position changes.
Coupling = tuple[tuple[str, str], ...]
Mode = Literal['current', 'initial']


@dataclass(frozen=True)
class ReorientationTask:
    carrier: Carrier
    position: tuple[str, ...]  # mathematically declared coordinate/pose per state
    mode: Mode = 'current'


def validate_task(task: ReorientationTask) -> None:
    try:
        passport(task.carrier)
    except CausalSourceError as e:
        raise ReorientationError('unlicensed source carrier') from e
    if task.mode not in ('current', 'initial'):
        raise ReorientationError('unknown position target mode')
    if len(task.position) != len(task.carrier.states):
        raise ReorientationError('position chart does not cover the source')
    if any(type(x) is not str or not x for x in task.position):
        raise ReorientationError('position chart labels must be nonempty symbols')


def task_passport(task: ReorientationTask) -> str:
    validate_task(task)
    payload = [passport(task.carrier), task.position, task.mode]
    return sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest()


def target(task: ReorientationTask, marked: tuple[str, str]) -> str:
    c = task.carrier
    w, q = marked
    if task.mode == 'initial':
        q = c.origins[c.worlds.index(w)]
    return task.position[c.states.index(q)]


def ordered_coupling(task: ReorientationTask, items) -> Coupling:
    # The order of source worlds is stable and is NOT an independent source label.
    order = {w: i for i, w in enumerate(task.carrier.worlds)}
    unique = tuple(set(items))
    if any(w not in order or q not in task.carrier.states for w, q in unique):
        raise ReorientationError('invalid original/current source pair')
    return tuple(sorted(unique, key=lambda pair: (order[pair[0]], pair[1])))


def target_set(task: ReorientationTask, belief: Coupling) -> frozenset[str]:
    return frozenset(target(task, pair) for pair in belief)


def successors(task: ReorientationTask, belief: Coupling, action: str) -> tuple[tuple[str, Coupling], ...]:
    if action not in task.carrier.actions:
        raise ReorientationError('action outside reorientation toolkit')
    groups = {}
    for w, q in belief:
        q1 = apply(task.carrier, q, action)
        groups.setdefault(observation(task.carrier, q1), []).append((w, q1))
    return tuple((out, ordered_coupling(task, groups[out])) for out in sorted(groups))


@dataclass(frozen=True)
class OrientationPolicy:
    action: str | None
    answer: str | None
    branches: tuple[tuple[str, 'OrientationPolicy'], ...] = ()
    rank: int = 0


@dataclass(frozen=True)
class ReorientationCertificate:
    source: str
    first_report: str
    history: tuple[tuple[str, str], ...]
    mode: Mode
    starting_belief: Coupling
    reachable_beliefs: int
    winning_beliefs: int
    rank: int | None  # None means NO winning policy for this starting belief.
    policy: OrientationPolicy | None


def reachable_beliefs(task: ReorientationTask, start: Coupling, max_nodes: int = 30000):
    if not start:
        raise ReorientationError('empty source set is incompatible evidence')
    discovered = {start}
    queue = deque((start,))
    graph = {}
    while queue:
        belief = queue.popleft()
        graph[belief] = {action: successors(task, belief, action)
                         for action in task.carrier.actions}
        for splits in graph[belief].values():
            for _, successor in splits:
                if successor not in discovered:
                    discovered.add(successor)
                    queue.append(successor)
                    if len(discovered) > max_nodes:
                        raise ReorientationError('explicit finite belief-resource limit exceeded')
    return graph


def solve(task: ReorientationTask, memory: CausalMemory,
          max_nodes: int = 30000) -> ReorientationCertificate:
    validate_task(task)
    try:
        rows = verify_memory(task.carrier, memory)
    except CausalSourceError as e:
        raise ReorientationError('source memory failed independent original-world replay') from e
    start = ordered_coupling(task, rows)
    graph = reachable_beliefs(task, start, max_nodes=max_nodes)
    # Backward reachability in a perfect-information adversarial-output game.
    # Rank is the exact minimum worst-case number of interventions to recover
    # the TARGET CURRENT/INITIAL coordinate under the declared source.
    rank = {b: 0 for b in graph if len(target_set(task, b)) == 1}
    choices = {}
    while True:
        additions = {}
        for b, by_action in graph.items():
            if b in rank:
                continue
            candidates = []
            for index, action in enumerate(task.carrier.actions):
                splits = by_action[action]
                if splits and all(child in rank for _, child in splits):
                    candidates.append((1 + max(rank[child] for _, child in splits), index, action))
            if candidates:
                depth, _, action = min(candidates)
                additions[b] = (depth, action)
        if not additions:
            break
        for b, (depth, action) in additions.items():
            rank[b] = depth
            choices[b] = action
    if start not in rank:
        return ReorientationCertificate(task_passport(task), memory.first_report,
                tuple((s.action, s.outcome) for s in memory.steps), task.mode, start,
                len(graph), len(rank), None, None)

    def build(b: Coupling) -> OrientationPolicy:
        if rank[b] == 0:
            return OrientationPolicy(None, next(iter(target_set(task,b))), (), 0)
        action = choices[b]
        return OrientationPolicy(action, None,
                                 tuple((y, build(child)) for y, child in graph[b][action]), rank[b])

    return ReorientationCertificate(task_passport(task), memory.first_report,
            tuple((s.action, s.outcome) for s in memory.steps), task.mode, start,
            len(graph), len(rank), rank[start], build(start))


def verify_policy(task: ReorientationTask, memory: CausalMemory,
                  certificate: ReorientationCertificate) -> int | None:
    """Check source/replayed belief and EVERY legal branch. Not a solver call.

    This verifies a particular claimed finite reorientation policy; it does not
    independently prove policy optimality. Independent brute-force oracle tests
    the minimax claim for small source families.
    """
    validate_task(task)
    root = ordered_coupling(task, verify_memory(task.carrier, memory))
    expected_history = tuple((s.action,s.outcome) for s in memory.steps)
    if (certificate.source != task_passport(task) or
        certificate.first_report != memory.first_report or
        certificate.history != expected_history or certificate.mode != task.mode or
        certificate.starting_belief != root):
        raise ReorientationError('bad source passport or false retained memory')
    if certificate.policy is None:
        if certificate.rank is not None:
            raise ReorientationError('missing claimed winning policy')
        return None  # This verifier does not claim a no-go certificate.

    def check(b: Coupling, tree: OrientationPolicy) -> int:
        if tree.action is None:
            if tree.branches or tree.rank != 0 or len(target_set(task,b)) != 1 or tree.answer not in target_set(task,b):
                raise ReorientationError('stopping without locating the genuine position')
            return 0
        if tree.action not in task.carrier.actions or tree.answer is not None or tree.rank <= 0:
            raise ReorientationError('invalid action/answer at internal node')
        expected = dict(successors(task,b,tree.action))
        if len(tree.branches) != len(expected) or {y for y, _ in tree.branches} != set(expected):
            raise ReorientationError('unexamined or duplicated actual observation branch')
        depths = []
        for observed, child in tree.branches:
            if child.rank >= tree.rank:
                raise ReorientationError('navigation rank does not decrease in every future')
            depths.append(check(expected[observed],child))
        actual_depth = 1 + max(depths)
        if actual_depth != tree.rank:
            raise ReorientationError('forged optimality/rank counter')
        return actual_depth
    depth = check(root,certificate.policy)
    if depth != certificate.rank:
        raise ReorientationError('certificate root rank is false')
    return depth


def reorient_from_anywhere(task: ReorientationTask):
    """Local first observation partitions arbitrary original positions.

    Finite uniform guarantee is only for the declared finite source + toolkit.
    """
    validate_task(task)
    c=task.carrier
    results=[]
    for y in sorted(set(observation(c,q) for q in c.origins)):
        m=initial_memory(c,y)
        certificate=solve(task,m)
        if certificate.rank is not None:
            verify_policy(task,m,certificate)
        results.append((y,certificate))
    return tuple(results)


def ring_with_beacon(n: int, *, marked_side: bool = False) -> ReorientationTask:
    """Fixed globally oriented ring, forward = x -> x+1 (authenticated port)."""
    from .principia_causal_memory import carrier
    if type(n) is not int or n < 4:
        raise ReorientationError('ring needs at least four distinguished sites')
    states=tuple(f'x{i}' for i in range(n))
    outputs=tuple('beacon' if i==0 else 'eastmark' if marked_side and i==1 else 'dark'
                  for i in range(n))
    return ReorientationTask(carrier('known-direction-ring'+str(n), states, states,
                  ('forward','stay'),states,outputs,states,
                  (tuple(states[(i+1)%n] for i in range(n)),states),costs=(1,0)), states)


def ring_with_unknown_heading(n: int, *, side_marker: bool = False,
                              coordinate: str = 'pose') -> ReorientationTask:
    """Reflection-symmetric map unless eastmark breaks its gauge ambiguity."""
    from .principia_causal_memory import carrier
    if type(n) is not int or n < 5 or coordinate not in ('pose','position','distance'):
        raise ReorientationError('invalid reflection-map geometry/target')
    points=tuple((x,h) for x in range(n) for h in (-1,1))
    labels=tuple(f'{x}:{h:+d}' for x,h in points)
    by_point={point:label for point,label in zip(points,labels)}
    observations=tuple('beacon' if x==0 else 'eastmark' if side_marker and x==1 else 'dark'
                       for x,h in points)
    forward=tuple(by_point[((x+h)%n,h)] for x,h in points)
    turn=tuple(by_point[(x,-h)] for x,h in points)
    targets = (labels if coordinate == 'pose' else
               tuple(f'x{x}' for x,h in points) if coordinate=='position' else
               tuple(f'd{min(x,n-x)}' for x,h in points))
    c=carrier(f'reflected-ring-{n}-side-{side_marker}',labels,labels,
              ('forward','turn'),labels,observations,labels,
              (forward,turn),costs=(1,1))
    return ReorientationTask(c,targets)


def homogeneous_ring(n: int, *, reset: bool=False, mode: Mode='current') -> ReorientationTask:
    """All reports dark. Reset changes current pose, not original source."""
    from .principia_causal_memory import carrier
    if type(n) is not int or n<3:
        raise ReorientationError('bad homogeneous ring size')
    states=tuple(f'x{i}' for i in range(n))
    actions=('forward','reset') if reset else ('forward',)
    moves=[tuple(states[(i+1)%n] for i in range(n))]
    if reset:moves.append((states[0],)*n)
    c=carrier(f'homogeneous-{n}-reset-{reset}',states,states,actions,states,
              ('dark',)*n,states,tuple(moves),costs=(1,)*len(actions))
    return ReorientationTask(c,states,mode)


def zigzag_moves(radius: int):
    """One directed, relative-coordinate route visiting all offsets [-R,R].

    At sweep k, go from -(k-1) to +k, then to -k. Thus every finite
    unknown initial offset eventually hits a unique beacon at world origin.
    """
    if type(radius) is not int or radius < 0:
        raise ReorientationError('finite completion radius required')
    for k in range(1,radius+1):
        yield from ('right',)*(2*k-1)
        yield from ('left',)*(2*k)


def trace_zigzag(radius: int) -> tuple[int,...]:
    offset=0
    visited=[0]
    for action in zigzag_moves(radius):
        offset += 1 if action=='right' else -1
        visited.append(offset)
    return tuple(visited)


def find_line_beacon(start: int, *, radius: int) -> tuple[int,int,int] | None:
    """If observed: (initial actual position, action count, current position=0).

    No source guess: the landing action history determines offset relative to
    the observer's original frame. Requires exact direction and unique beacon.
    """
    if type(start) is not int:
        raise ReorientationError('mathematical source position must be integer')
    offset=0
    if start==0:return (0,0,0)
    for t, action in enumerate(zigzag_moves(radius),1):
        offset += 1 if action=='right' else -1
        if start+offset==0:
            return (-offset,t,0)
    return None


@dataclass(frozen=True)
class GaugeObstruction:
    """A source automorphism that hides a target-required orientation."""
    source: str
    permutation: tuple[tuple[str, str], ...]
    witness: tuple[str, str]  # two admissible initial state labels


def certify_gauge_obstruction(task: ReorientationTask,
                              mapping: dict[str, str]) -> GaugeObstruction:
    """Only certifies a strong NO-GO, not all possible no-go reasons.

    For current position require P(q)!=P(gamma(q)) for EVERY q, so no
    lawful word can collapse the two relevant target values. For initial
    position a single different original target pair already suffices.
    """
    validate_task(task)
    c=task.carrier
    if set(mapping) != set(c.states) or set(mapping.values()) != set(c.states):
        raise ReorientationError('not a bijection of the declared source states')
    for q in c.states:
        if observation(c,mapping[q]) != observation(c,q):
            raise ReorientationError('proposed gauge does not preserve local observations')
        for action in c.actions:
            if apply(c,mapping[q],action) != mapping[apply(c,q,action)]:
                raise ReorientationError('proposed gauge does not commute with causal actions')
    allowed_origins=set(c.origins)
    witness=next(((q,mapping[q]) for q in c.origins
                  if mapping[q] in allowed_origins and q!=mapping[q]
                  and task.position[c.states.index(q)] != task.position[c.states.index(mapping[q])]),None)
    if witness is None:
        raise ReorientationError('no target-separated admissible source pair')
    if task.mode=='current' and any(
        task.position[c.states.index(q)] == task.position[c.states.index(mapping[q])]
        for q in c.states):
        raise ReorientationError('present target may converge modulo this gauge')
    return GaugeObstruction(task_passport(task),tuple((q,mapping[q]) for q in c.states),witness)


def verify_gauge_obstruction(task: ReorientationTask, cert: GaugeObstruction) -> GaugeObstruction:
    if cert.source != task_passport(task):
        raise ReorientationError('changed source/position reference in no-go proof')
    expected=certify_gauge_obstruction(task,dict(cert.permutation))
    if expected != cert:
        raise ReorientationError('forged indistinguishability witness')
    return cert


def reflected_ring_gauge(n: int) -> dict[str,str]:
    """Mirror transformation (x,h) -> (-x,-h) on the unmarked ring."""
    if type(n) is not int or n<5:
        raise ReorientationError('bad reflection ring size')
    return {f'{x}:{h:+d}':f'{(-x)%n}:{-h:+d}'
            for x in range(n) for h in (-1,1)}


def homogeneous_ring_gauge(n: int) -> dict[str,str]:
    if type(n) is not int or n<3:
        raise ReorientationError('bad uniform ring size')
    return {f'x{i}':f'x{(i+1)%n}' for i in range(n)}
