"""Persistent counterexample-guided evolution of finite semantic bridges.

Extends the PR #43 real genetic proposals: discovered violations become hard
constraints for every later child, not merely a worse fitness score. The exact
verifier can be complete for the DECLARED finite source or explicitly partial.
No exhaustive permutation oracle is used by search. No physical source is assumed.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import factorial
from random import Random
from .relational_model_genetics import (
    BridgeCandidate, Capsule, GeneticsError, PairedSourceTable,
    pullback, transport_capsule, emergent_dependencies,
)


@dataclass(frozen=True)
class BridgeObstruction:
    event: str
    left_value: str
    required_right: str
    rejected_right: str


@dataclass(frozen=True)
class EvolutionResult:
    bridge: BridgeCandidate
    child: Capsule | None
    emergent: tuple
    exclusions: tuple[BridgeObstruction, ...]
    proposals: tuple[tuple[str, ...], ...]
    remaining_bijections: int
    complete_declared_source: bool
    learned_from_verifier: int
    full_permutation_enumeration_used: bool = False


def evolve_with_obstructions(left: Capsule, right: Capsule, source: PairedSourceTable,
                             *, seed: int = 0, max_checks: int = 128) -> EvolutionResult:
    """Counterexamples force new inherited equality genes; all descendants obey.

    Under a consistent bijective source, each failed check fixes a previously
    unfixed left value. At most d-1 failures plus one successful check suffice.
    This is NOT a guarantee for unrestricted evolutionary programming.
    """
    scope = (source.source_id, source.epoch, source.basis)
    if any((m.source_id, m.epoch, m.basis) != scope for m in (left, right)):
        raise GeneticsError('Source/basis/epoch changed across crossover')
    dom, cod = source.left_port.domain, source.right_port.domain
    if len(dom) != len(cod) or not 1 <= max_checks <= 1024 or type(seed) is not int:
        raise GeneticsError('Bounded finite bijective bridge contract required')
    # Check *consistency*, not pre-supply the unknown bridge to the proposal engine.
    observed = {}
    for event, a, b in source.observations:
        if a not in dom or b not in cod or (a in observed and observed[a] != b):
            raise GeneticsError('No function can realize the source reports')
        observed[a] = b
    if len(set(observed.values())) != len(observed):
        raise GeneticsError('No bijection can realize the source reports')
    if source.complete_source_class and set(observed) != set(dom):
        raise GeneticsError('Completeness flag lacks full declared interface coverage')
    rng = Random(seed)
    fixed = {}
    learned, proposed = [], []
    for _ in range(max_checks):
        free_keys = [x for x in dom if x not in fixed]
        free_values = [y for y in cod if y not in fixed.values()]
        rng.shuffle(free_values)
        child_map = dict(fixed)
        # Typed permutation crossover of previous proposals. Hard-learned
        # alleles are immutable; duplicate/forbidden outputs are repaired.
        parents = rng.sample(proposed, 2) if len(proposed) >= 2 else []
        for x in free_keys:
            inherited = parents[rng.randrange(2)][dom.index(x)] if parents else None
            if inherited in free_values and rng.randrange(4):
                value = inherited
            else:
                value = rng.choice(free_values)
            child_map[x] = value
            free_values.remove(value)
        genotype = tuple(child_map[x] for x in dom)
        if any(child_map[w.left_value] != w.required_right for w in learned):
            raise AssertionError('Mutation erased a certified counterexample')
        proposed.append(genotype)
        bad = next(((event, a, b) for event, a, b in source.observations if child_map[a] != b), None)
        if bad is None:
            complete = source.complete_source_class and set(observed) == set(dom)
            bridge = BridgeCandidate(source.source_id, source.epoch, source.basis,
                                     source.left_port, source.right_port,
                                     tuple((x, child_map[x]) for x in dom),
                                     len(source.observations), complete)
            translated = transport_capsule(right, bridge)
            joined = pullback(left, translated)
            if joined.merged is None:
                raise GeneticsError('Valid interface does not ensure jointly realizable parent models')
            new = emergent_dependencies(left, translated, joined.merged)
            return EvolutionResult(bridge, joined.merged, new, tuple(learned), tuple(proposed),
                                   factorial(len(dom)-len(observed)), complete, len(learned))
        event, a, b = bad
        if a in fixed:
            raise AssertionError('A validated old exclusion failed again')
        learned.append(BridgeObstruction(event, a, b, child_map[a]))
        fixed[a] = b
    raise GeneticsError('UNRESOLVED_CHECK_BUDGET, not no-bridge or genetic success')
