"""Constructive versus classical excluded middle, and omega/omega+1 controls.

Finite Kripke semantics provides a genuine countermodel to constructively
deriving P∨¬P, without ever refuting classical excluded middle or inferring a
physical law from unavailable measurements.

The omega example is SYMBOLIC: we prove the infinite-set case from its
definition, not by claiming that a finite Python loop reaches infinity.
"""
from __future__ import annotations

from dataclasses import dataclass


class FrontierError(ValueError):
    pass


@dataclass(frozen=True)
class Formula:
    operation: str
    arguments: tuple["Formula", ...] = ()
    symbol: str = ""

    def __post_init__(self):
        arity = {"atom": 0, "bottom": 0, "not": 1,
                 "and": 2, "or": 2, "implies": 2}
        if self.operation not in arity or type(self.arguments) is not tuple:
            raise FrontierError("Unknown propositional connective")
        if len(self.arguments) != arity[self.operation]:
            raise FrontierError("Malformed propositional formula arity")
        if any(not isinstance(f, Formula) for f in self.arguments):
            raise FrontierError("Formula arguments must be typed propositions")
        if self.operation == "atom":
            if type(self.symbol) is not str or not self.symbol:
                raise FrontierError("Atomic proposition needs a nonempty symbol")
        elif self.symbol:
            raise FrontierError("Only atomic propositions have symbols")


def atom(name: str) -> Formula:
    return Formula("atom", (), name)


def neg(a: Formula) -> Formula:
    return Formula("not", (a,))


def disj(a: Formula, b: Formula) -> Formula:
    return Formula("or", (a, b))


def implication(a: Formula, b: Formula) -> Formula:
    return Formula("implies", (a, b))


@dataclass(frozen=True)
class KripkeModel:
    """Finite rooted partially ordered Kripke frame with monotone atom forcing."""

    nodes: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    true_atoms: tuple[tuple[str, tuple[str, ...]], ...]

    def __post_init__(self):
        if type(self.nodes) is not tuple or not 1 <= len(self.nodes) <= 32:
            raise FrontierError("Expected a finite nonempty rooted frame")
        if len(self.nodes) != len(set(self.nodes)) or any(
            type(node) is not str or not node for node in self.nodes
        ):
            raise FrontierError("Nodes must have unique nonempty names")
        if type(self.edges) is not tuple or type(self.true_atoms) is not tuple:
            raise FrontierError("Kripke relations must be immutable")
        for pair in self.edges:
            if type(pair) is not tuple or len(pair) != 2:
                raise FrontierError("Malformed accessibility edge")
            a, b = pair
            if a not in self.nodes or b not in self.nodes or a == b:
                raise FrontierError("Invalid accessibility edge")
        if len(self.true_atoms) != len(self.nodes):
            raise FrontierError("Every node requires one monotone atom valuation")
        rows = {}
        for row in self.true_atoms:
            if type(row) is not tuple or len(row) != 2:
                raise FrontierError("Malformed atom valuation row")
            node, atoms = row
            if node not in self.nodes or node in rows or type(atoms) is not tuple:
                raise FrontierError("Duplicate, missing or malformed atom valuation")
            if any(type(name) is not str or not name for name in atoms):
                raise FrontierError("Invalid propositional atom name")
            rows[node] = set(atoms)
        if len(rows) != len(self.nodes):
            raise FrontierError("Incomplete Kripke valuation")
        for node in self.nodes:
            if node not in self.successors(self.nodes[0]):
                raise FrontierError("A declared rooted frame must reach every node")
            for desc in self.successors(node):
                if desc != node and node in self.successors(desc):
                    raise FrontierError("Accessibility cannot have a cycle")
                if not rows[node].issubset(rows[desc]):
                    raise FrontierError("Forced atomic truths must persist along extensions")

    def successors(self, node: str) -> tuple[str, ...]:
        if node not in self.nodes:
            raise FrontierError("Unknown observation/knowledge node")
        reachable = {node}
        todo = [node]
        while todo:
            cur = todo.pop()
            for a, b in self.edges:
                if a == cur and b not in reachable:
                    reachable.add(b)
                    todo.append(b)
        return tuple(x for x in self.nodes if x in reachable)

    def forces(self, node: str, formula: Formula) -> bool:
        if node not in self.nodes or not isinstance(formula, Formula):
            raise FrontierError("Forcing needs a known node and a typed formula")
        op = formula.operation
        children = formula.arguments
        if op == "atom":
            return formula.symbol in dict(self.true_atoms)[node]
        if op == "bottom":
            return False
        if op == "not":
            return all(not self.forces(ext, children[0]) for ext in self.successors(node))
        if op == "and":
            return self.forces(node, children[0]) and self.forces(node, children[1])
        if op == "or":
            return self.forces(node, children[0]) or self.forces(node, children[1])
        if op == "implies":
            return all(not self.forces(ext, children[0]) or self.forces(ext, children[1])
                       for ext in self.successors(node))
        raise FrontierError("Invalid connective")

    def excluded_middle(self, node: str, formula: Formula) -> bool:
        return self.forces(node, disj(formula, neg(formula)))


def intuitionistic_lem_demo() -> dict:
    model = KripkeModel(
        ("root", "yes", "no"),
        (("root", "yes"), ("root", "no")),
        (("root", ()), ("yes", ("P",)), ("no", ())),
    )
    p = atom("P")
    assert (not model.forces("root", p)
            and not model.forces("root", neg(p))
            and not model.excluded_middle("root", p)
            and model.excluded_middle("yes", p)
            and model.excluded_middle("no", p)
            and not model.forces("root", neg(disj(p, neg(p)))))
    return {
        "status": "FINITE_KRIPKE_CONSTRUCTIVE_LEM_COUNTERMODEL",
        "root_forces_P": False,
        "root_forces_not_P": False,
        "root_forces_P_or_not_P": False,
        "yes_forces_P_or_not_P": True,
        "no_forces_P_or_not_P": True,
        "classical_excluded_middle_invalidated": False,
        "contradictory_physical_observation_required": False,
    }


def finite_successor_stage(n: int) -> tuple[int, ...]:
    """Proved: F^n(empty)={0,...,n-1} for specified finite n."""
    if type(n) is not int or not 0 <= n <= 10000:
        raise FrontierError("This is a bounded finite witness, not an omega iterator")
    return tuple(range(n))


@dataclass(frozen=True)
class SymbolicOmegaStage:
    """A declared mathematical limit, never an executed infinite event."""

    includes_all_naturals: bool
    includes_seal: bool

    def next_declared_limit_rule(self) -> "SymbolicOmegaStage":
        """Only applies when its INFINITARY antecedent is explicitly justified."""
        return SymbolicOmegaStage(
            self.includes_all_naturals,
            self.includes_seal or self.includes_all_naturals,
        )


def omega_plus_one_demo() -> dict:
    """Example: a monotone, non-omega-continuous closure requires omega+1."""
    omega = SymbolicOmegaStage(True, False)
    successor = omega.next_declared_limit_rule()
    assert (not omega.includes_seal and successor.includes_seal
            and successor.next_declared_limit_rule() == successor)
    return {
        "status": "SYMBOLIC_NON_OMEGA_CONTINUOUS_CLOSURE",
        "finite_prefix_has_seal": False,
        "omega_contains_all_naturals": True,
        "omega_contains_seal": False,
        "omega_plus_one_contains_seal": True,
        "physical_infinite_iteration_executed": False,
        "infinitary_rule_licensed_by_finite_data": False,
    }


def fixed_width_message_capacity(bits: int) -> int:
    """Pigeonhole limit for EXACTLY b transmitted bits."""
    if type(bits) is not int or not 0 <= bits <= 256:
        raise FrontierError("Bounded exact nonnegative bit budget required")
    return 1 << bits
