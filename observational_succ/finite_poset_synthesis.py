"""Obstruction-guided enlargement: finite poset functors and adjoints.

All theorem checks are exact and range over *finite declared* posets.
A source table is a mathematical oracle, not evidence of physical authenticity.
The source-dependent synthesis algorithm starts with isomorphisms, records
counterexamples, and introduces noninvertible functors only on obstruction.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from .relational_model_genetics import GeneticsError


@dataclass(frozen=True)
class FinitePoset:
    objects: tuple[str, ...]
    order: frozenset[tuple[str, str]]

    def __post_init__(self):
        if (type(self.objects) is not tuple or not self.objects
                or len(set(self.objects)) != len(self.objects)
                or any(type(x) is not str or not x for x in self.objects)
                or type(self.order) is not frozenset):
            raise GeneticsError("A finite poset requires distinct named objects")
        s = set(self.objects)
        if (any(a not in s or b not in s for a, b in self.order)
                or any((a, a) not in self.order for a in s)
                or any(a != b and (b, a) in self.order for a, b in self.order)
                or any((a, c) not in self.order for a, b in self.order
                       for x, c in self.order if x == b)):
            raise GeneticsError("The relation must be reflexive, antisymmetric, transitive")

    def le(self, a: str, b: str) -> bool:
        if a not in self.objects or b not in self.objects:
            raise GeneticsError("Unknown object")
        return (a, b) in self.order


def chain(*objects: str) -> FinitePoset:
    if not objects:
        raise GeneticsError("Empty chain")
    return FinitePoset(tuple(objects), frozenset(
        (a, b) for i, a in enumerate(objects) for b in objects[i:]))


@dataclass(frozen=True)
class PosetFunctor:
    domain: FinitePoset
    codomain: FinitePoset
    images: tuple[str, ...]

    def __post_init__(self):
        if (type(self.images) is not tuple
                or len(self.images) != len(self.domain.objects)
                or any(y not in self.codomain.objects for y in self.images)):
            raise GeneticsError("A functor needs one typed image per object")
        f = dict(zip(self.domain.objects, self.images))
        if any(not self.codomain.le(f[a], f[b]) for a, b in self.domain.order):
            raise GeneticsError("Nonmonotone map is not a poset functor")

    def __call__(self, x: str) -> str:
        try:
            return dict(zip(self.domain.objects, self.images))[x]
        except KeyError as ex:
            raise GeneticsError("Outside functor domain") from ex

    def then(self, following: PosetFunctor) -> PosetFunctor:
        if self.codomain != following.domain:
            raise GeneticsError("Functor composition has incompatible interface")
        return PosetFunctor(self.domain, following.codomain,
                            tuple(following(self(x)) for x in self.domain.objects))


def all_functors(domain: FinitePoset, codomain: FinitePoset) -> tuple[PosetFunctor, ...]:
    return tuple(PosetFunctor(domain, codomain, images)
                 for images in product(codomain.objects, repeat=len(domain.objects))
                 if all(codomain.le(images[domain.objects.index(a)],
                                    images[domain.objects.index(b)])
                        for a, b in domain.order))


def all_isomorphisms(domain: FinitePoset, codomain: FinitePoset) -> tuple[PosetFunctor, ...]:
    if len(domain.objects) != len(codomain.objects):
        return ()
    return tuple(f for f in all_functors(domain, codomain)
                 if len(set(f.images)) == len(f.images)
                 and all(domain.le(a, b) == codomain.le(f(a), f(b))
                         for a in domain.objects for b in domain.objects))


def natural_transformation(f: PosetFunctor, g: PosetFunctor) -> bool:
    """In thin categories, F => G has a component iff F(x) <= G(x).

    When components exist their naturality squares commute by uniqueness.
    """
    if f.domain != g.domain or f.codomain != g.codomain:
        raise GeneticsError("Natural transformation must have common categories")
    return all(f.codomain.le(f(x), g(x)) for x in f.domain.objects)


def check_adjunction(left: PosetFunctor, right: PosetFunctor) -> bool:
    if left.domain != right.codomain or left.codomain != right.domain:
        raise GeneticsError("Wrong functor directions for an adjunction")
    return all(left.codomain.le(left(x), y) == left.domain.le(x, right(y))
               for x in left.domain.objects for y in left.codomain.objects)


def infer_right_adjoint(left: PosetFunctor) -> PosetFunctor | None:
    """Independent exhaustive hom-set equivalence, not a guessed formula."""
    found = tuple(g for g in all_functors(left.codomain, left.domain)
                  if check_adjunction(left, g))
    if len(found) > 1:
        raise AssertionError("An adjoint of a poset functor must be unique")
    return found[0] if found else None


def is_order_quotient(f: PosetFunctor) -> bool:
    """Sufficient order-lifting criterion for the universal factor property.

    Surjectivity alone is *not* taken to imply an order quotient. Every
    target order pair must have a comparable source pair above it.
    """
    if set(f.images) != set(f.codomain.objects):
        return False
    return all(any(f(a) == y and f(b) == z and f.domain.le(a, b)
                   for a in f.domain.objects for b in f.domain.objects)
               for y, z in f.codomain.order)


@dataclass(frozen=True)
class PairedPosetSource:
    source_id: str
    epoch: int
    basis: str
    domain: FinitePoset
    codomain: FinitePoset
    observations: tuple[tuple[str, str, str], ...]  # source-state, input, output
    complete: bool

    def __post_init__(self):
        if (not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.observations) is not tuple
                or type(self.complete) is not bool
                or len({s for s, _, _ in self.observations}) != len(self.observations)
                or any(not s or x not in self.domain.objects or y not in self.codomain.objects
                       for s, x, y in self.observations)):
            raise GeneticsError("Malformed typed source/epoch observations")
        seen = {}
        for _, x, y in self.observations:
            if x in seen and seen[x] != y:
                raise GeneticsError("Exact deterministic source contradicts itself")
            seen[x] = y
        if self.complete and set(seen) != set(self.domain.objects):
            raise GeneticsError("Declared complete class must cover every input")

    def oracle(self) -> dict[str, str]:
        return {x: y for _, x, y in self.observations}


@dataclass(frozen=True)
class Exclusion:
    grammar: str
    candidate: tuple[str, ...]
    tested_input: str
    predicted: str
    actual: str


@dataclass(frozen=True)
class SynthesisReport:
    source_id: str
    epoch: int
    basis: str
    original_grammar: str
    resulting_grammar: str
    obstruction: str | None
    probes: tuple[str, ...]
    exclusions: tuple[Exclusion, ...]
    candidates: tuple[PosetFunctor, ...]
    source_class_certified: bool
    order_quotient: bool
    right_adjoint: PosetFunctor | None

    @property
    def unique(self) -> PosetFunctor | None:
        return self.candidates[0] if len(self.candidates) == 1 else None


def _filter_by_probes(candidates: tuple[PosetFunctor, ...],
                      oracle: dict[str, str],
                      grammar: str) -> tuple[tuple[PosetFunctor, ...],
                                             tuple[str, ...], tuple[Exclusion, ...]]:
    """Probe highest currently separating input first; preserve witnesses."""
    remaining = set(oracle)
    survivors = candidates
    queried = []
    killed = []
    while remaining and survivors:
        x = min(remaining, key=lambda v: (-len({f(v) for f in survivors}), v))
        remaining.remove(x)
        queried.append(x)
        good = []
        for f in survivors:
            if f(x) == oracle[x]:
                good.append(f)
            else:
                killed.append(Exclusion(grammar, f.images, x, f(x), oracle[x]))
        survivors = tuple(good)
    return survivors, tuple(queried), tuple(killed)


def synthesize_with_obstructions(table: PairedPosetSource) -> SynthesisReport:
    """No invalid candidate is rescued by editing an observation.

    A complete table permits conditional source-wide claims; an incomplete
    one yields a surviving hypothesis class, never a certified uniqueness.
    """
    oracle = table.oracle()
    old = all_isomorphisms(table.domain, table.codomain)
    surviving, first_probes, dead = _filter_by_probes(old, oracle, "isomorphism")
    if surviving:
        grammar = "isomorphism"
        obstruction = None
        probes = first_probes
        exclusions = dead
    else:
        # A proof of *local grammar* failure, not a claim that any source
        # data are wrong or that the new grammar is true a priori.
        obstruction = ("cardinality-precludes-bijection"
                       if len(table.domain.objects) != len(table.codomain.objects)
                       else "source-refutes-every-isomorphism")
        grammar = "finite-poset-functor"
        surviving, probes, new_dead = _filter_by_probes(
            all_functors(table.domain, table.codomain), oracle, grammar)
        exclusions = dead + new_dead
    certified = table.complete and len(surviving) == 1
    f = surviving[0] if certified else None
    adj = infer_right_adjoint(f) if f else None
    return SynthesisReport(table.source_id, table.epoch, table.basis,
                           "isomorphism", grammar, obstruction, probes,
                           exclusions, surviving, certified,
                           is_order_quotient(f) if f else False, adj)


def quotient_demo() -> dict:
    a, b = chain("a", "b", "c"), chain("cold", "warm")
    table = PairedPosetSource("declared-quotient", 0, "ordered", a, b,
                             (("s0", "a", "cold"), ("s1", "b", "cold"),
                              ("s2", "c", "warm")), True)
    r = synthesize_with_obstructions(table)
    if not (r.source_class_certified and r.right_adjoint and r.order_quotient):
        raise AssertionError("The declared source should synthesize an adjunction")
    f, g = r.unique, r.right_adjoint
    return {
        "initial_obstruction": r.obstruction,
        "invented_grammar": r.resulting_grammar,
        "map": list(f.images),
        "fibers": [[x for x in a.objects if f(x) == y] for y in b.objects],
        "right_adjoint": list(g.images),
        "unit_exists": natural_transformation(
            PosetFunctor(a, a, a.objects), f.then(g)),
        "counit_exists": natural_transformation(
            g.then(f), PosetFunctor(b, b, b.objects)),
        "verified_hom_set_pairs": len(a.objects) * len(b.objects),
        "probes": list(r.probes),
        "source_complete_relative": r.source_class_certified,
        "empirical_authentication": False,
    }
