"""Source-query-guided genetic hypotheses on an obstruction-grown functor grammar.

The original bijection grammar has no inhabitant for a 3-to-2 (or 8-to-4)
source. E first receives a *proof of grammar insufficiency*, then explores
monotone maps with type-preserving genetic operators. It probes only source
inputs actually observed. Wrong genomes leave no-good clauses, not source edits.
The exact finite functor enumerator is a separate fallback, never genetic credit.
"""
from __future__ import annotations

from dataclasses import dataclass
from random import Random

from .finite_poset_synthesis import (
    PairedPosetSource, PosetFunctor, all_functors, all_isomorphisms,
    infer_right_adjoint,
)
from .relational_model_genetics import GeneticsError


@dataclass(frozen=True)
class EvolutionReceipt:
    seed: int
    grammar_expansion: str
    source_probes: tuple[tuple[str, str], ...]
    no_good_clauses: tuple[tuple[str, str, str], ...]
    candidate_count: int
    genetically_discovered: bool
    genetic_model: tuple[str, ...] | None
    exact_oracle_model: tuple[str, ...] | None
    exact_oracle_rescue: bool
    source_class_certified: bool
    inferred_right_adjoint: tuple[str, ...] | None
    physical_source_authenticated: bool = False


def _chain_check(table: PairedPosetSource):
    for poset in (table.domain, table.codomain):
        if any(not poset.le(a, b) for i, a in enumerate(poset.objects)
               for b in poset.objects[i:]):
            raise GeneticsError("This evolutionary mutation family needs finite chains")


def _proposal(table: PairedPosetSource, observed: dict[str, str],
              rng: Random) -> PosetFunctor | None:
    """Sample a random *monotone* extension of the accumulated observations."""
    a = table.domain.objects
    b = table.codomain.objects
    known = {a.index(x): b.index(y) for x, y in observed.items()}
    if any(i < j and q > r for i, q in known.items() for j, r in known.items()):
        return None
    out = []
    for i in range(len(a)):
        low = out[-1] if out else 0
        upper = min((v for j, v in known.items() if j >= i),
                    default=len(b)-1)
        if i in known:
            if not low <= known[i] <= upper:
                return None
            out.append(known[i])
        else:
            if low > upper:
                return None
            out.append(rng.randint(low, upper))
    return PosetFunctor(table.domain, table.codomain,
                        tuple(b[i] for i in out))


def _breed(a: PosetFunctor, b: PosetFunctor, rng: Random) -> PosetFunctor:
    """Pointwise meet/join of chain functors preserves monotonicity."""
    cod = a.codomain.objects
    left = [cod.index(x) for x in a.images]
    right = [cod.index(x) for x in b.images]
    mixed = [min(x, y) if rng.randrange(2) else max(x, y)
             for x, y in zip(left, right)]
    # min/max chosen independently can spoil monotonicity. Repair to the
    # nearest majorizing monotone sequence; ALWAYS recheck exact functor type.
    for i in range(1, len(mixed)):
        mixed[i] = max(mixed[i], mixed[i-1])
    return PosetFunctor(a.domain, a.codomain, tuple(cod[i] for i in mixed))


def genetic_functor_search(table: PairedPosetSource, *, seed: int,
                           population: int = 12, generations: int = 16
                           ) -> EvolutionReceipt:
    _chain_check(table)
    if (type(seed) is not int or population < 4 or generations < 1):
        raise GeneticsError("Finite reproducible search budgets required")
    rng = Random(seed)
    oracle = table.oracle()
    old = all_isomorphisms(table.domain, table.codomain)
    obstruction = ("NO_ISOMORPHISM_CARDINALITY" if len(table.domain.objects)
                   != len(table.codomain.objects)
                   else "ISOMORPHISM_SEARCH_NOT_PRECLUDED")
    # No global source lookup for choosing mutations or scoring: only queried
    # input-output pairs may constrain a proposal.
    queried = {}
    excludes = set()
    candidates = set()
    generated = 0

    def propose(known: dict[str, str]) -> PosetFunctor | None:
        nonlocal generated
        f = _proposal(table, known, rng)
        generated += 1
        return f

    population_now = [propose({}) for _ in range(population)]
    population_now = [f for f in population_now if f is not None]
    winner = None
    for generation in range(generations):
        unqueried = set(oracle) - set(queried)
        if not unqueried:
            break
        # This maximizes disagreement within current *genetic proposals*;
        # no access to the hidden correct response until the query is made.
        x = min(unqueried, key=lambda k:
                (-len({f(k) for f in population_now}), k))
        y = oracle[x]
        queried[x] = y
        for f in population_now:
            candidates.add(f.images)
            if f(x) != y:
                excludes.add((x, f(x), y))
        population_now = [f for f in population_now
                          if all(f(k) == v for k, v in queried.items())]
        if len(queried) == len(table.domain.objects):
            # Recognition of a proposal already generated BEFORE the final
            # source receipt. Exact source completion after this is not
            # retroactively credited to genetic invention.
            if table.complete and population_now:
                winner = population_now[0]
            break
        if not population_now:
            population_now = [p for _ in range(population)
                              for p in (propose(queried),) if p is not None]
        else:
            parents = tuple(population_now)
            new_generation = list(parents[:population])
            while len(new_generation) < population:
                if rng.randrange(3) == 0:
                    child = propose(queried)
                else:
                    bred = _breed(rng.choice(parents), rng.choice(parents), rng)
                    # A bred proposal must satisfy ALL accumulated no-good
                    # clauses or be rejected, NEVER erase the observed truth.
                    if all(bred(k) == v for k, v in queried.items()):
                        child = bred
                        generated += 1
                    else:
                        child = propose(queried)
                if child is not None:
                    new_generation.append(child)
            population_now = new_generation

    # Totally independent complete-grammar source oracle: even on a genetic
    # miss, finite proof recovery is possible in the declared small universe.
    exact = tuple(f for f in all_functors(table.domain, table.codomain)
                  if all(f(k) == v for k, v in oracle.items()))
    exact_model = exact[0] if table.complete and len(exact) == 1 else None
    adj = infer_right_adjoint(exact_model) if exact_model else None
    is_winner = winner is not None and exact_model is not None \
        and winner.images == exact_model.images
    return EvolutionReceipt(
        seed, obstruction, tuple(sorted(queried.items())),
        tuple(sorted(excludes)), generated,
        is_winner, winner.images if is_winner else None,
        exact_model.images if exact_model else None,
        exact_model is not None and not is_winner,
        exact_model is not None, adj.images if adj else None,
    )


def blind_source_demo(seed: int = 0) -> dict:
    """An external deterministic table picks an unknown 8-to-4 functor.

    The gene sampler sees outputs only when it requests a source probe.
    The construction class (finite chain functors) IS supplied; the actual
    mapping, target fiber partition, and right-adjoint value are NOT.
    """
    rng = Random(314159)  # separate source oracle, not search RNG
    a = tuple("x" + str(i) for i in range(8))
    b = ("cold", "warm", "hot", "plasma")
    source_values = tuple(sorted((rng.randrange(len(b)) for _ in a)))
    from .finite_poset_synthesis import chain
    table = PairedPosetSource(
        "blind-chain-generator-v1", 0, "ordered",
        chain(*a), chain(*b),
        tuple(("state" + str(i), x, b[source_values[i]]) for i, x in enumerate(a)),
        True)
    r = genetic_functor_search(table, seed=seed)
    exact = r.exact_oracle_model
    return {
        "grammar_growth": r.grammar_expansion,
        "source_probes": len(r.source_probes),
        "genetic_success": r.genetically_discovered,
        "exact_oracle_rescue": r.exact_oracle_rescue,
        "exclusion_clauses": len(r.no_good_clauses),
        "source_partition": [
            [x for x, val in zip(a, exact) if val == y] for y in b
        ],
        "right_adjoint": list(r.inferred_right_adjoint) if r.inferred_right_adjoint else None,
        "full_source_relatively_certified": r.source_class_certified,
        "physical_source_authenticated": False,
        "grammar_was_open_ended": False,
    }
