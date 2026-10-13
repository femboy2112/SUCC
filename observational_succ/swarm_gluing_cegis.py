"""X03: source-preserving finite gluing and monotone constraint learning.

Tables are complete *declared mathematical* carriers, not empirical evidence.
Constraint satisfaction speaks about original-coordinate assignments.  It does
not license joint execution of destructive experiments.
"""

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class FiniteTable:
    variables: tuple[str, ...]
    domains: tuple[tuple[int, ...], ...]
    rows: tuple[tuple[int, ...], ...]

    def __post_init__(self):
        if len(self.variables) != len(self.domains):
            raise ValueError("One domain is required per variable")
        if len(set(self.variables)) != len(self.variables):
            raise ValueError("Variable names must be unique")
        if any(not d or len(set(d)) != len(d) for d in self.domains):
            raise ValueError("Domains must be finite, nonempty and duplicate-free")
        if len(set(self.rows)) != len(self.rows):
            raise ValueError("Carrier rows must be unique")
        for row in self.rows:
            if len(row) != len(self.variables):
                raise ValueError("A carrier row has the wrong arity")
            if any(value not in domain for value, domain in zip(row, self.domains)):
                raise ValueError("A carrier row is outside its typed domain")

    @classmethod
    def cartesian(cls, variables, domains):
        variables, domains = tuple(variables), tuple(tuple(d) for d in domains)
        return cls(variables, domains, tuple(product(*domains)))


@dataclass(frozen=True)
class LocalRelation:
    name: str
    scope: tuple[str, ...]
    allowed: tuple[tuple[int, ...], ...]

    def indices(self, source):
        if not self.name or len(set(self.scope)) != len(self.scope):
            raise ValueError("Named relations require a duplicate-free scope")
        if any(v not in source.variables for v in self.scope):
            raise ValueError("Unknown relation coordinate")
        indices = tuple(source.variables.index(v) for v in self.scope)
        if len(set(self.allowed)) != len(self.allowed):
            raise ValueError("Relation rows must be unique")
        for row in self.allowed:
            if len(row) != len(indices):
                raise ValueError("Relation row has the wrong arity")
            if any(value not in source.domains[i] for value, i in zip(row, indices)):
                raise ValueError("Relation row is outside its typed domain")
        return indices


def _predicates(source, relations):
    if len({r.name for r in relations}) != len(relations):
        raise ValueError("Constraint provenance names must be unique")
    return tuple((r.indices(source), frozenset(r.allowed)) for r in relations)


def _satisfies(row, predicate):
    indices, allowed = predicate
    return tuple(row[i] for i in indices) in allowed


def global_sections(source, relations):
    predicates = _predicates(source, relations)
    return tuple(row for row in source.rows
                 if all(_satisfies(row, predicate) for predicate in predicates))


@dataclass(frozen=True)
class TypedGrammar:
    """Finite denotations of any bounded typed grammar with retained originals.

    Extra coordinates can denote probes/auxiliary values.  The grammar may be
    incomplete.  Every candidate's original projection must belong to the fixed
    source.  This checks denotations, not the correctness of a syntax compiler.
    """

    source: FiniteTable
    candidates: FiniteTable

    def projection_indices(self):
        if any(v not in self.candidates.variables for v in self.source.variables):
            raise ValueError("The grammar forgot an original coordinate")
        indices = tuple(self.candidates.variables.index(v) for v in self.source.variables)
        if any(self.source.domains[j] != self.candidates.domains[i]
               for j, i in enumerate(indices)):
            raise ValueError("Original variable domains must be preserved exactly")
        return indices

    def projected_rows(self):
        indices = self.projection_indices()
        originals = tuple(tuple(row[i] for i in indices) for row in self.candidates.rows)
        if any(row not in self.source.rows for row in originals):
            raise ValueError("A grammar candidate invents an undeclared original")
        return originals


def minimal_unsat_core(source, relations):
    """Return a deletion-minimal core, not a minimum-cardinality core."""
    relations = tuple(relations)
    _predicates(source, relations)
    if global_sections(source, relations):
        raise ValueError("A satisfiable problem has no unsatisfiable core")
    core = list(relations)
    for relation in relations:
        trial = tuple(r for r in core if r.name != relation.name)
        if not global_sections(source, trial):
            core = list(trial)
    return tuple(r.name for r in core)


def monotone_cegis(grammar, relations):
    """Exact proposal/check loop; retain every failed original constraint.

    At most min(number of constraints, number of candidates) rejections occur.
    UNSAT_GRAMMAR never asserts that the complete source has no global section.
    Its core is relative to the projected grammar; only a source-verified core
    can prune arbitrary future grammar extensions.
    """
    relations = tuple(relations)
    source, candidates = grammar.source, grammar.candidates
    originals = grammar.projected_rows()
    predicates = _predicates(source, relations)
    learned = []
    rejected = []
    complete = set(originals) == set(source.rows)
    while True:
        candidate = next((i for i, row in enumerate(originals)
                          if all(_satisfies(row, predicates[j]) for j in learned)), None)
        if candidate is None:
            projected_carrier = FiniteTable(source.variables, source.domains,
                                            tuple(dict.fromkeys(originals)))
            core = minimal_unsat_core(projected_carrier,
                                      tuple(relations[j] for j in learned))
            return {"status": "UNSAT_SOURCE" if complete else "UNSAT_GRAMMAR",
                    "projection_surjective": complete,
                    "learned": tuple(relations[j].name for j in learned),
                    "rejections": tuple(rejected), "core": core,
                    "core_scope": "SOURCE" if complete else "GRAMMAR_IMAGE",
                    "core_source_verified": complete,
                    "original_witness": None, "extended_witness": None}
        original = originals[candidate]
        failed = next((j for j, predicate in enumerate(predicates)
                       if not _satisfies(original, predicate)), None)
        if failed is None:
            return {"status": "SAT_SOURCE", "projection_surjective": complete,
                    "learned": tuple(relations[j].name for j in learned),
                    "rejections": tuple(rejected), "core": (),
                    "core_scope": None, "core_source_verified": False,
                    "original_witness": original,
                    "extended_witness": candidates.rows[candidate]}
        if failed in learned:
            raise ArithmeticError("A retained counterexample was forgotten")
        rejected.append({"original": original, "extended": candidates.rows[candidate],
                         "constraint": relations[failed].name})
        learned.append(failed)


def lift_relations(grammar, relations):
    """Coordinate projections implement inverse-image pullback of constraints."""
    grammar.projected_rows()
    _predicates(grammar.source, relations)
    _predicates(grammar.candidates, relations)
    return tuple(relations)


def triangle_problem():
    source = FiniteTable.cartesian(("x", "y", "z"), ((0, 1),) * 3)
    equal, unequal = ((0, 0), (1, 1)), ((0, 1), (1, 0))
    relations = (LocalRelation("xy_equal", ("x", "y"), equal),
                 LocalRelation("yz_equal", ("y", "z"), equal),
                 LocalRelation("xz_unequal", ("x", "z"), unequal))
    return source, relations
