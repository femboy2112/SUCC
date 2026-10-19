"""Source-faithful online safety games and independently checked certificates.

Classical finite safety games; see ONLINE_SOURCE_REALIZATION.md for full
semantics, proofs, public-command boundaries, and novelty accounting.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

from .lawful_history_gluing import PrivateState, SourceGraph

Request = tuple[str, str]  # requested action and target report


class GameError(ValueError):
    pass


class GameBudgetExceeded(GameError):
    """An incomplete computation, never a losing certificate."""


@dataclass(frozen=True)
class Move:
    position: int
    request: Request
    response: str
    successors: frozenset[int]


@dataclass(frozen=True)
class SafetyGame:
    """Environment requests, resolver responds, environment selects an outcome.

    No available request means terminal safety, not a progress guarantee.
    A request with no response is an immediate resolver loss. Empty outcome
    sets are forbidden; unavailable commands cannot win by vacuity.
    """
    requests: tuple[frozenset[Request], ...]
    moves: frozenset[Move]

    def __post_init__(self):
        if type(self.requests) is not tuple or type(self.moves) is not frozenset:
            raise GameError("Immutable finite arena tables required")
        for requests in self.requests:
            if type(requests) is not frozenset or any(not _request(r) for r in requests):
                raise GameError("Requests must be nonempty action/target strings")
        keys = set()
        for move in self.moves:
            if (not isinstance(move, Move) or type(move.position) is not int
                    or not 0 <= move.position < len(self.requests)
                    or move.request not in self.requests[move.position]
                    or type(move.response) is not str or not move.response
                    or type(move.successors) is not frozenset or not move.successors
                    or any(type(z) is not int or not 0 <= z < len(self.requests)
                           for z in move.successors)):
                raise GameError("Malformed response or outcome table")
            key = (move.position, move.request, move.response)
            if key in keys:
                raise GameError("One complete outcome set per command row")
            keys.add(key)


@dataclass(frozen=True)
class SafetyCertificate:
    winning: frozenset[int]
    # (position, request, chosen response), one per winning request.
    strategy: tuple[tuple[int, Request, str], ...]
    # Rank 0 denotes winning; losing ranks are positive exact integers.
    ranks: tuple[int, ...]
    # (losing position, spoiling request), one per losing position.
    spoilers: tuple[tuple[int, Request], ...]
    # (position, spoiling request, response, chosen lower-rank outcome).
    counteroutcomes: tuple[tuple[int, Request, str, int], ...]


def _request(request):
    return (type(request) is tuple and len(request) == 2
            and all(type(x) is str and x for x in request))


def solve_safety(game: SafetyGame) -> SafetyCertificate:
    """Greatest fixed point, with a total positive/negative certificate."""
    live = set(range(len(game.requests)))
    ranks = [0] * len(game.requests)
    spoilers, counteroutcomes = [], []
    stage = 0
    while True:
        removed = {}
        for x in sorted(live):
            for request in sorted(game.requests[x]):
                moves = [m for m in game.moves if m.position == x and m.request == request]
                if not any(m.successors <= live for m in moves):
                    removed[x] = (request, moves)
                    break
        if not removed:
            break
        stage += 1
        for x, (request, moves) in sorted(removed.items()):
            ranks[x] = stage
            spoilers.append((x, request))
            for move in sorted(moves, key=lambda m: m.response):
                counteroutcomes.append((x, request, move.response, min(move.successors - live)))
        live.difference_update(removed)
    strategy = []
    for x in sorted(live):
        for request in sorted(game.requests[x]):
            choice = min(m.response for m in game.moves
                         if m.position == x and m.request == request and m.successors <= live)
            strategy.append((x, request, choice))
    return SafetyCertificate(frozenset(live), tuple(strategy), tuple(ranks),
                             tuple(spoilers), tuple(counteroutcomes))


def verify_safety(game: SafetyGame, certificate: SafetyCertificate) -> bool:
    """Direct finite certificate verification; does not call solve_safety.

    Winning closure proves a positional strategy. Strict losing ranks plus
    adversarial requests/outcomes prove the complement cannot be winning.
    """
    if not isinstance(certificate, SafetyCertificate):
        return False
    c = certificate
    try:
        universe = set(range(len(game.requests)))
        if (type(c.winning) is not frozenset or not c.winning <= universe
                or any(type(x) is not int for x in c.winning)
                or type(c.ranks) is not tuple or len(c.ranks) != len(universe)
                or any(type(r) is not int or not 0 <= r <= len(universe) for r in c.ranks)
                or any((c.ranks[x] == 0) != (x in c.winning) for x in universe)):
            return False
        if (any(type(table) is not tuple for table in (c.strategy, c.spoilers, c.counteroutcomes))
                or any(type(x) is not int or not _request(r) or type(a) is not str or not a
                       for x, r, a in c.strategy)
                or any(type(x) is not int or not _request(r) for x, r in c.spoilers)
                or any(type(x) is not int or not _request(r) or type(a) is not str
                       or not a or type(z) is not int for x, r, a, z in c.counteroutcomes)):
            return False
        strategy = {(x, r): a for x, r, a in c.strategy}
        spoilers = dict(c.spoilers)
        outcomes = {(x, r, a): z for x, r, a, z in c.counteroutcomes}
        if (len(strategy) != len(c.strategy) or len(spoilers) != len(c.spoilers)
                or len(outcomes) != len(c.counteroutcomes)):
            return False
        winning_keys = {(x, r) for x in c.winning for r in game.requests[x]}
        if set(strategy) != winning_keys or set(spoilers) != universe - c.winning:
            return False
        rows = {(m.position, m.request, m.response): m.successors for m in game.moves}
        for (x, request), response in strategy.items():
            successors = rows.get((x, request, response))
            if successors is None or not successors <= c.winning:
                return False
        expected_outcomes = set()
        for x, request in spoilers.items():
            if request not in game.requests[x]:
                return False
            for move in game.moves:
                if move.position == x and move.request == request:
                    key = (x, request, move.response)
                    expected_outcomes.add(key)
                    z = outcomes.get(key)
                    if (type(z) is not int or z not in move.successors
                            or z in c.winning or not c.ranks[z] < c.ranks[x]):
                        return False
        return set(outcomes) == expected_outcomes
    except (TypeError, ValueError, KeyError, IndexError):
        return False


def private_resolver_game(model: SourceGraph, source: str, abstract_edges=None):
    """Perfect information: the resolver may select a legal private successor.

    Original source and private state are known to both players. Abstract
    requests are public; no response means refusal/failure, not a new receipt.
    Returned indices follow the returned tuple of private states.
    """
    states = tuple(x for x in model.states if x.source == source)
    if not states:
        raise GameError("Unknown original source")
    abstract = model.projected_edges(source) if abstract_edges is None else abstract_edges
    _check_abstract(abstract)
    index = {x: i for i, x in enumerate(states)}
    requests = tuple(frozenset((a, after) for before, a, after in abstract if before == x.report)
                     for x in states)
    moves = frozenset(Move(index[x], (a, z.report), str(index[z]), frozenset((index[z],)))
                      for x, a, z in model.edges if x.source == source
                      and (a, z.report) in requests[index[x]])
    return SafetyGame(requests, moves), states


def _check_abstract(abstract):
    if (type(abstract) is not frozenset
            or any(type(e) is not tuple or len(e) != 3
                   or any(type(v) is not str or not v for v in e) for e in abstract)):
        raise GameError("Explicit immutable abstract-edge table required")


@dataclass(frozen=True)
class ControlContract:
    """Named public commands, with COMPLETE adversarial outcome rows.

    An implementation row (x, action, command) gives all possible successors.
    Command availability may be private, but choosing a command cannot inspect
    it. The belief compiler imposes universal legality before any conditioning.
    """
    model: SourceGraph
    abstract_edges: frozenset[tuple[str, str, str]]
    commands: frozenset[str]
    implementations: frozenset[tuple[PrivateState, str, str, PrivateState]]

    def __post_init__(self):
        _check_abstract(self.abstract_edges)
        if (type(self.commands) is not frozenset
                or any(type(c) is not str or not c for c in self.commands)
                or type(self.implementations) is not frozenset):
            raise GameError("Explicit public commands and complete outcome rows required")
        for row in self.implementations:
            if type(row) is not tuple or len(row) != 4:
                raise GameError("Implementation row is (state, action, command, successor)")
            x, action, command, z = row
            if command not in self.commands or (x, action, z) not in self.model.edges:
                raise GameError("Public implementation must preserve a declared source edge")


def belief_game(contract: ControlContract, observation: tuple[str, ...], *, max_beliefs=16384):
    """Exact pure sure-safety game for a public observer with perfect recall.

    The observation must refine the base report. Beliefs may contain multiple
    original labels: no source oracle is supplied. Return (arena, beliefs).
    A cap failure raises GameBudgetExceeded, not a false impossibility verdict.
    """
    states = contract.model.states
    if (type(observation) is not tuple or len(observation) != len(states)
            or any(type(y) is not str or not y for y in observation)
            or type(max_beliefs) is not int or max_beliefs < 1):
        raise GameError("A finite observation table and positive belief budget required")
    blocks = {}
    for x, signal in zip(states, observation):
        blocks.setdefault(signal, []).append(x)
    if any(len({x.report for x in block}) != 1 for block in blocks.values()):
        raise GameError("Public observation must retain the base report")
    count = sum(2 ** len(block) - 1 for block in blocks.values())
    if count > max_beliefs:
        raise GameBudgetExceeded(f"UNRESOLVED: {count} beliefs exceed budget {max_beliefs}")
    beliefs = tuple(frozenset(part) for signal in sorted(blocks)
                    for size in range(1, len(blocks[signal]) + 1)
                    for part in combinations(blocks[signal], size))
    index = {belief: i for i, belief in enumerate(beliefs)}
    obs = dict(zip(states, observation))
    requests = tuple(frozenset((a, after) for before, a, after in contract.abstract_edges
                               if before == next(iter(belief)).report) for belief in beliefs)
    moves = []
    for i, belief in enumerate(beliefs):
        for action, after in requests[i]:
            for command in contract.commands:
                rows = [frozenset(z for x, a, c, z in contract.implementations
                                  if x == current and a == action and c == command)
                        for current in belief]
                # No postselection on target report: inspect EVERY actual outcome.
                if any(not row or any(z.report != after for z in row) for row in rows):
                    continue
                post = frozenset().union(*rows)
                successors = frozenset(index[frozenset(z for z in post if obs[z] == signal)]
                                       for signal in {obs[z] for z in post})
                moves.append(Move(i, (action, after), command, successors))
    return SafetyGame(requests, frozenset(moves)), beliefs


@dataclass(frozen=True)
class OneStepInterface:
    """One request, one current report, terminal success after a legal command.

    enabled[i] is the set of public commands legal at private source state i.
    Sensors below are declared truthful, total, and nondestructive; that is an
    explicit acquisition contract, not something inferred from a partition.
    """
    enabled: tuple[frozenset[str], ...]

    def __post_init__(self):
        if (type(self.enabled) is not tuple or not self.enabled
                or any(type(row) is not frozenset
                       or any(type(c) is not str or not c for c in row) for row in self.enabled)):
            raise GameError("Finite state-indexed command sets required")


def minimal_conflicts(interface: OneStepInterface, *, max_subsets=65536):
    """Minimal private subsets with no universally legal public command."""
    if type(max_subsets) is not int or max_subsets < 1:
        raise GameError("Positive exact state-subset budget required")
    if 2 ** len(interface.enabled) > max_subsets:
        raise GameBudgetExceeded("UNRESOLVED: private-subset enumeration budget exhausted")
    result = []
    for size in range(1, len(interface.enabled) + 1):
        for part in combinations(range(len(interface.enabled)), size):
            subset = frozenset(part)
            if any(h <= subset for h in result):
                continue
            common = set(interface.enabled[part[0]])
            for x in part[1:]:
                common.intersection_update(interface.enabled[x])
            if not common:
                result.append(subset)
    return tuple(result)


@dataclass(frozen=True)
class Probe:
    name: str
    outputs: tuple[str, ...]
    cost: Fraction

    def __post_init__(self):
        if (type(self.name) is not str or not self.name or type(self.outputs) is not tuple
                or any(type(y) is not str or not y for y in self.outputs)
                or type(self.cost) not in (int, Fraction) or self.cost < 0):
            raise GameError("A declared total probe with exact nonnegative acquisition cost required")


def minimum_probe_repair(interface: OneStepInterface, probes: tuple[Probe, ...], *, max_subsets=65536):
    """Exact minimum-cost fixed probe bundle; not adaptive probe acquisition.

    Returns (cost, all minimum-cost index sets), or (None, ()) if impossible.
    General finite acquisition is a hitting-set problem, not a new sensor.
    """
    if (type(probes) is not tuple or any(not isinstance(p, Probe) for p in probes)
            or len({p.name for p in probes}) != len(probes)
            or any(len(p.outputs) != len(interface.enabled) for p in probes)
            or type(max_subsets) is not int or max_subsets < 1):
        raise GameError("A distinct finite menu of complete lawful probes required")
    if 2 ** len(probes) > max_subsets:
        raise GameBudgetExceeded("UNRESOLVED: probe-subset enumeration budget exhausted")
    conflicts = minimal_conflicts(interface, max_subsets=max_subsets)
    hits = tuple(frozenset(i for i, h in enumerate(conflicts)
                          if len({p.outputs[x] for x in h}) > 1) for p in probes)
    best, choices = None, []
    for size in range(len(probes) + 1):
        for indices in combinations(range(len(probes)), size):
            covered = frozenset().union(*(hits[i] for i in indices))
            if len(covered) != len(conflicts):
                continue
            cost = sum((Fraction(probes[i].cost) for i in indices), Fraction())
            if best is None or cost < best:
                best, choices = cost, [frozenset(indices)]
            elif cost == best:
                choices.append(frozenset(indices))
    return best, tuple(choices)
