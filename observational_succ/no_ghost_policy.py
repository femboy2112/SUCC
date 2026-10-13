"""Exact public-policy realization plans over finite NO-GHOST contracts.

Unlike a simplex of positive trajectories, these equations enforce the fixed
source preparation, chance kernels, and inability to condition decisions on
hidden source/current/branch data. Public history has perfect recall. Every
run must terminate at the declared finite decision horizon; no postselection,
reset, private-state-dependent stopping or empirical execution is inferred.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Hashable, Mapping, Sequence

from .no_ghost import (
    CouplingProblem, FiniteContract, NoGhostError, PossibleHistory, PrivateEvent,
    PublicHistory, exact, solve_nonnegative, verify_dual, verify_primal,
)


@dataclass(frozen=True)
class PolicySystem:
    """Complete finite tree plus a rational linear realization-plan encoding."""

    source_id: str
    basis: str
    horizon: int
    nodes: tuple[PublicHistory, ...]
    menus: Mapping[PublicHistory, tuple[str, ...]]
    variables: tuple[tuple, ...]
    node_index: Mapping[PublicHistory, int]
    action_index: Mapping[tuple[PublicHistory, str], int]
    atoms: tuple[PossibleHistory, ...]
    leaf_index: tuple[int, ...]
    A: tuple[tuple[Q, ...], ...]
    b: tuple[Q, ...]

    def equations(self, restrictions: Sequence[Sequence[Hashable]],
                  local_laws: Sequence[Mapping[Hashable, Q]]):
        """Add observed marginals while retaining operational flow equations."""
        support = CouplingProblem(tuple(a.identity for a in self.atoms),
                                  tuple(tuple(r) for r in restrictions),
                                  tuple(local_laws))
        support_A, support_b = support.equations()
        extra = []
        for row in support_A:
            new = [Q(0)] * len(self.variables)
            for j, coefficient in enumerate(row):
                new[self.leaf_index[j]] += coefficient * self.atoms[j].mass
            extra.append(tuple(new))
        return self.A + tuple(extra), self.b + tuple(support_b)

    def weights(self, realization: Sequence[Q]) -> tuple[Q, ...]:
        realization = tuple(exact(x) for x in realization)
        if not verify_primal(self.A, self.b, realization):
            raise NoGhostError("Invalid public realization plan")
        return tuple(a.mass * realization[i]
                     for a, i in zip(self.atoms, self.leaf_index))

    def policy(self, realization: Sequence[Q]):
        realization = tuple(exact(x) for x in realization)
        if not verify_primal(self.A, self.b, realization):
            raise NoGhostError("Invalid public realization plan")
        ans = {}
        for h, actions in self.menus.items():
            r = realization[self.node_index[h]]
            # Empty menus can only occur at unreachable nonterminal nodes.
            # No hidden action is manufactured there.
            ans[h] = ({a: realization[self.action_index[h, a]] / r for a in actions}
                      if r else {a: Q(int(i == 0)) for i, a in enumerate(actions)})
        return ans


@dataclass(frozen=True)
class PolicyCompilation:
    status: str
    system: PolicySystem | None = None
    reason: str = ""


def compile_public_policy(model: FiniteContract, horizon: int, *,
                          max_prefixes: int = 100000) -> PolicyCompilation:
    """Compile ALL safe public action choices, with exact private chance paths.

    The horizon is a fixed number of decisions, bounded by the distinct event
    occurrences. Actions whose parents have not occurred, or whose row is
    absent at any hidden possibility, are unavailable. A premature dead end
    imposes r_h=0; if forced, the LP is infeasible. It does not get discarded
    as if the observer were allowed to postselect successful branches.
    """
    model.validate()
    if type(horizon) is not int or not 0 <= horizon <= len(model.events):
        raise NoGhostError("Decision horizon must be between zero and the event count")
    if type(max_prefixes) is not int or max_prefixes < 0:
        raise NoGhostError("Nonnegative private-prefix budget required")
    roots = tuple(PossibleHistory(s, c, c, (), exact(p), model.source_id, model.basis)
                  for s, c, p in model.preparation if p)
    count = len(roots)
    if count > max_prefixes:
        return PolicyCompilation("UNRESOLVED", reason="private-prefix budget exhausted")
    parents = {e.occurrence: e.parents for e in model.events}
    pending = deque([((), roots)])
    nodes, menus, successors, atoms = [], {}, {}, []
    while pending:
        h, paths = pending.popleft()
        nodes.append(h)
        if len(h) == horizon:
            atoms.extend(paths)
            continue
        done = {a for a, _ in h}
        actions = tuple(a for a, dependencies in parents.items()
                        if a not in done and dependencies <= done
                        and all((h, a, p.source, p.current) in model.kernels for p in paths))
        menus[h] = actions
        for a in actions:
            by_receipt = defaultdict(list)
            for p in paths:
                for step in model.kernels[(h, a, p.source, p.current)]:
                    if not step.probability:
                        continue
                    e = PrivateEvent(a, step.outcome, p.current, step.after, step.branch)
                    child = PossibleHistory(p.source, p.initial, step.after,
                                            p.events + (e,), p.mass * exact(step.probability),
                                            model.source_id, model.basis)
                    by_receipt[step.outcome].append(child)
                    count += 1
                    if count > max_prefixes:
                        return PolicyCompilation("UNRESOLVED", reason="private-prefix budget exhausted")
            successors[h, a] = tuple(h + ((a, z),) for z in by_receipt)
            pending.extend((h + ((a, z),), tuple(ps)) for z, ps in by_receipt.items())
    variables = tuple(("node", h) for h in nodes) + tuple(
        ("action", h, a) for h, acts in menus.items() for a in acts)
    index = {v: i for i, v in enumerate(variables)}
    node_index = {h: index["node", h] for h in nodes}
    action_index = {(h, a): index["action", h, a] for h, acts in menus.items() for a in acts}
    rows, rhs = [], []

    def equation(coefficients, value=0):
        row = [Q(0)] * len(variables)
        for i, v in coefficients:
            row[i] += Q(v)
        rows.append(tuple(row))
        rhs.append(Q(value))

    equation(((node_index[()], 1),), 1)
    for h, actions in menus.items():
        equation(((node_index[h], -1),) + tuple((action_index[h, a], 1) for a in actions))
        for a in actions:
            for child in successors[h, a]:
                equation(((node_index[child], 1), (action_index[h, a], -1)))
    system = PolicySystem(model.source_id, model.basis, horizon, tuple(nodes), menus,
                          variables, node_index, action_index, tuple(atoms),
                          tuple(node_index[p.public] for p in atoms), tuple(rows), tuple(rhs))
    return PolicyCompilation("COMPILED", system,
                             "Complete public policy tree, possible paths only; solve feasibility next")


def operational_coupling(system: PolicySystem, restrictions, local_laws, *, max_bases=100000):
    """Return an exact realization plan or dual; budget exhaustion is unknown."""
    return solve_nonnegative(*system.equations(restrictions, local_laws), max_bases=max_bases)


def verify_policy_solution(model: FiniteContract, system: PolicySystem, realization,
                           restrictions, local_laws, *, max_prefixes=100000) -> bool:
    """Bind a positive certificate to the original model, then replay it.

    A supplied PolicySystem is data, not an authority: comparing a fresh
    compilation rejects altered atoms, weights, source metadata or equations.
    The additional independent transition replay verifies the realized law.
    This checks a declared mathematical model, not its empirical authenticity.
    """
    try:
        rebuilt = compile_public_policy(model, system.horizon, max_prefixes=max_prefixes)
        if rebuilt.status != "COMPILED" or rebuilt.system != system:
            return False
        if not verify_primal(*system.equations(restrictions, local_laws), realization):
            return False
        actual = replay_public_policy(model, system.horizon, system.policy(realization),
                                      max_prefixes=max_prefixes)
        expected = {a.identity: w for a, w in zip(system.atoms, system.weights(realization)) if w}
        return actual == expected
    except (NoGhostError, TypeError, ValueError, KeyError, AttributeError):
        return False


def verify_policy_obstruction(model: FiniteContract, horizon: int, restrictions,
                              local_laws, dual, *, max_prefixes=100000) -> bool:
    """Verify a dual against freshly source-derived operational equations."""
    try:
        rebuilt = compile_public_policy(model, horizon, max_prefixes=max_prefixes)
        return (rebuilt.status == "COMPILED" and
                verify_dual(*rebuilt.system.equations(restrictions, local_laws), dual))
    except (NoGhostError, TypeError, ValueError, KeyError, AttributeError):
        return False


def replay_public_policy(model: FiniteContract, horizon: int, policy, *, max_prefixes=100000):
    """Independent probability propagation to check a reconstructed policy.

    Unlike compilation this multiplies policy factors during each transition;
    it does not use the linear system, its variables or its leaf weights.
    """
    model.validate()
    if type(horizon) is not int or not 0 <= horizon <= len(model.events):
        raise NoGhostError("Invalid horizon")
    if type(max_prefixes) is not int or max_prefixes < 0:
        raise NoGhostError("Invalid prefix budget")
    frontier = [(s, c, c, (), Q(p)) for s, c, p in model.preparation if p]
    count = len(frontier)
    if count > max_prefixes:
        raise NoGhostError("UNRESOLVED: replay prefix budget exhausted")
    parents = {e.occurrence: e.parents for e in model.events}
    for _ in range(horizon):
        grouped = defaultdict(list)
        for row in frontier:
            grouped[tuple((e.occurrence, e.outcome) for e in row[3])].append(row)
        frontier = []
        for h, private in grouped.items():
            choices = {a: exact(p) for a, p in policy.get(h, {}).items()}
            if any(p < 0 for p in choices.values()) or sum(choices.values(), Q(0)) != 1:
                raise NoGhostError("Policy lacks a normalized public decision")
            done = {a for a, _ in h}
            for a, pa in choices.items():
                if not pa:
                    continue
                if a not in parents or a in done or not parents[a] <= done:
                    raise NoGhostError("Policy violates occurrence ancestry")
                if any((h, a, s, c) not in model.kernels for s, _, c, _, _ in private):
                    raise NoGhostError("Policy action needs hidden-state access")
                for s, initial, c, events, mass in private:
                    for step in model.kernels[(h, a, s, c)]:
                        if not step.probability:
                            continue
                        e = PrivateEvent(a, step.outcome, c, step.after, step.branch)
                        frontier.append((s, initial, step.after, events + (e,),
                                         mass * pa * exact(step.probability)))
                        count += 1
                        if count > max_prefixes:
                            raise NoGhostError("UNRESOLVED: replay prefix budget exhausted")
    result = {}
    for s, initial, c, events, mass in frontier:
        atom = PossibleHistory(s, initial, c, events, mass, model.source_id, model.basis)
        result[atom.identity] = mass
    if sum(result.values(), Q(0)) != 1:
        raise NoGhostError("Operational replay did not retain full unit probability")
    return result
