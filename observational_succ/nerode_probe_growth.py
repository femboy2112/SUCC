"""SUCC probe-language growth from finite deterministic observational obstructions.

Given a complete, stationary, finite source S with U:S->S and q:S->O,
the finite words W_h(s)=(q(s),q(U(s)),...,q(U^h(s))) define increasingly
fine observational quotients. Their first stable partition is the *full*
future-behavior quotient for this one available deterministic action.

When a state-changing square fails, the repair compiler generates new
typed probes q∘U^t by composition, rather than modifying a source law.
Independent exact hitting-set search gives a minimum-weight set of
probe expressions discriminating every truly distinguishable state pair.

Finite computation DOES NOT prove finite completion for unknown/infinite
physical carriers or authenticate an observation instrument.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations, product
from random import Random

from .causal_nerode_succ import SourceTransportError


@dataclass(frozen=True)
class ObserverDynamics:
    source_id: str
    epoch: int
    basis: str
    states: tuple[str, ...]
    next_states: tuple[str, ...]
    reports: tuple[str, ...]
    action: str = "SUCC"
    source_authenticated: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis or not self.action
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.states) is not tuple or not self.states
                or len(set(self.states)) != len(self.states)
                or type(self.next_states) is not tuple
                or type(self.reports) is not tuple
                or len(self.next_states) != len(self.states)
                or len(self.reports) != len(self.states)
                or any(type(s) is not str or not s for s in self.states)
                or any(x not in self.states for x in self.next_states)
                or any(type(x) is not str or not x for x in self.reports)
                or self.source_authenticated):
            raise SourceTransportError("Requires a finite exact declared stationary source")

    def step(self, s: str) -> str:
        try:
            return dict(zip(self.states, self.next_states))[s]
        except KeyError as ex:
            raise SourceTransportError("State outside declared carrier") from ex

    def report(self, s: str) -> str:
        try:
            return dict(zip(self.states, self.reports))[s]
        except KeyError as ex:
            raise SourceTransportError("State outside declared carrier") from ex

    def probe(self, s: str, lag: int) -> str:
        if type(lag) is not int or lag < 0 or lag > 10000:
            raise SourceTransportError("Probe requires explicit finite successor horizon")
        for _ in range(lag):
            s = self.step(s)
        return self.report(s)

    def word(self, s: str, horizon: int) -> tuple[str, ...]:
        if type(horizon) is not int or not 0 <= horizon <= 10000:
            raise SourceTransportError("Finite observation horizon required")
        return tuple(self.probe(s, t) for t in range(horizon + 1))

    def classes(self, offsets: tuple[int, ...]) -> tuple[tuple[str, ...], ...]:
        if (type(offsets) is not tuple or any(type(t) is not int or t < 0
                                              or t > 10000 for t in offsets)
                or len(set(offsets)) != len(offsets)):
            raise SourceTransportError("Probe offsets must be distinct finite naturals")
        fibers: dict[tuple[str, ...], list[str]] = {}
        for s in self.states:
            fibers.setdefault(tuple(self.probe(s, t) for t in offsets), []).append(s)
        return tuple(sorted((tuple(v) for v in fibers.values()),
                            key=lambda group: self.states.index(group[0])))

    def future_classes(self, horizon: int) -> tuple[tuple[str, ...], ...]:
        return self.classes(tuple(range(horizon + 1)))


@dataclass(frozen=True)
class NerodeReport:
    states: int
    stationary_source: str
    stabilization_horizon: int
    block_counts: tuple[int, ...]
    stable_classes: tuple[tuple[str, ...], ...]
    source_transition_quotient: tuple[tuple[str, str, str], ...]
    first_distinguishers: tuple[tuple[str, str, int], ...]
    indistinguishable_pairs: tuple[tuple[str, str], ...]
    stabilized_congruence_verified: bool
    logical_all_future_under_source_contract: bool
    actually_infinite_source_examined: bool = False


def nerode_fixpoint(source: ObserverDynamics) -> NerodeReport:
    n = len(source.states)
    partitions = [source.future_classes(0)]
    for h in range(n):
        following = source.future_classes(h + 1)
        if following == partitions[-1]:
            break
        partitions.append(following)
    else:
        raise AssertionError("Finite partition tower exceeded n strict refinements")
    depth = len(partitions)-1
    blocks = partitions[-1]
    lookup = {s: i for i, block in enumerate(blocks) for s in block}
    # Quotient transition exists because a stable partition is a congruence.
    quotient = []
    for i, block in enumerate(blocks):
        target_set = {lookup[source.step(s)] for s in block}
        output_set = {source.report(s) for s in block}
        if len(target_set) != 1 or len(output_set) != 1:
            raise AssertionError("Observed finite partition plateau is not a congruence")
        quotient.append((str(i), str(next(iter(target_set))),
                         next(iter(output_set))))
    pairs, aliases = [], []
    for i, s in enumerate(source.states):
        for t in source.states[i+1:]:
            diff = next((j for j in range(depth+1)
                         if source.probe(s, j) != source.probe(t, j)), None)
            if diff is not None:
                pairs.append((s, t, diff))
            else:
                aliases.append((s, t))
    return NerodeReport(
        n, source.source_id, depth, tuple(len(p) for p in partitions),
        blocks, tuple(quotient), tuple(pairs), tuple(aliases), True, True,
    )


@dataclass(frozen=True)
class ProbeGrammarReceipt:
    source_id: str
    horizon: int
    full_quotient_classes: int
    generated_expression_grammar: tuple[str, ...]
    greedy_offsets: tuple[int, ...]
    exact_minimum_cost_offsets: tuple[int, ...]
    greedy_declared_cost: int
    exact_declared_cost: int
    greedy_steps_reduce_unresolved_pairs: bool
    exact_grammar_oracle_complete: bool
    physical_counterfactual_reset_available: bool = False
    empirical_source_authenticated: bool = False


def _unresolved_pairs(source: ObserverDynamics,
                      selected: tuple[int, ...],
                      reference: NerodeReport
                      ) -> tuple[tuple[str, str], ...]:
    return tuple((s, t) for s, t, _ in reference.first_distinguishers
                 if all(source.probe(s, i) == source.probe(t, i) for i in selected))


def grow_probe_grammar(source: ObserverDynamics, *, budget_horizon: int = 14,
                       cost_per_successor: int = 1) -> ProbeGrammarReceipt:
    """Finite typed composition synthesis plus *independent* optimal oracle.

    Grammar constructors are seeded with q and "compose right with U".
    The exact set cover oracle cannot rescue an unsuccessful greedy search
    and claim it as greedy optimal. All costs are DECLARED, not measured.
    """
    report = nerode_fixpoint(source)
    H = report.stabilization_horizon
    if (H > budget_horizon or cost_per_successor < 1
            or type(cost_per_successor) is not int):
        raise SourceTransportError("Explicit finite exhaustive grammar budget exceeded")
    offsets = tuple(range(H+1))
    names = tuple("q" if t == 0 else "q_after_" + source.action + "^" + str(t)
                  for t in offsets)
    selected: tuple[int, ...] = ()
    unresolved = _unresolved_pairs(source, selected, report)
    monotonic_decrease = True
    while unresolved:
        ranked = []
        for t in offsets:
            if t in selected:
                continue
            after = _unresolved_pairs(source, selected + (t,), report)
            gain = len(unresolved)-len(after)
            cost = 1+cost_per_successor*t
            ranked.append((gain/cost, gain, -cost, -t, t, after))
        # Ratios here only PRIORITIZE syntax, not mathematical certificates.
        _, gain, _, _, best, remaining = max(ranked, key=lambda x: x[:4])
        if gain == 0:
            raise AssertionError("No legal distinguishing probe found in complete grammar")
        selected += (best,)
        monotonic_decrease &= len(remaining) < len(unresolved)
        unresolved = remaining

    def price(xs: tuple[int, ...]) -> int:
        return sum(1+cost_per_successor*t for t in xs)

    # Exhaustive, independent bounded set cover. No greedy success laundering.
    possible = []
    for length in range(H+2):
        for comb in combinations(offsets, length):
            if not _unresolved_pairs(source, comb, report):
                possible.append((price(comb), len(comb), comb))
    if not possible:
        raise AssertionError("Complete finite word grammar unexpectedly insufficient")
    optimal = min(possible)[2]
    if set(source.classes(selected)) != set(report.stable_classes):
        raise AssertionError("Greedy probes do not reconstruct actual Nerode classes")
    return ProbeGrammarReceipt(
        source.source_id, H, len(report.stable_classes), names,
        selected, optimal, price(selected), price(optimal),
        monotonic_decrease, True,
    )


def delayed_signal_chain(n: int) -> ObserverDynamics:
    """Adversarial source: one final output 1, long causal delay to reach it."""
    if type(n) is not int or not 2 <= n <= 16:
        raise SourceTransportError("Require 2..16 finite states")
    states = tuple("s"+str(i) for i in range(n))
    return ObserverDynamics("delayed-signal-"+str(n), 0, "binary",
                            states,
                            tuple(states[min(i+1, n-1)] for i in range(n)),
                            tuple("1" if i == n-1 else "0" for i in range(n)))


def independently_seeded_unknown_dynamics(seed: int, n: int = 7) -> ObserverDynamics:
    """Source generator separate from probe search; mapping is not preloaded."""
    if type(seed) is not int or type(n) is not int or not 2 <= n <= 9:
        raise SourceTransportError("Finite seeded source arguments required")
    rng = Random(seed * 65537 + 991)
    states = tuple("v"+str(i) for i in range(n))
    next_states = tuple(rng.choice(states) for _ in states)
    reports = tuple(str(rng.randrange(3)) for _ in states)
    return ObserverDynamics("external-table-"+str(seed), 0, "tri-symbol",
                            states, next_states, reports)


def nerode_moonshot_demo() -> dict:
    chain = delayed_signal_chain(8)
    report = nerode_fixpoint(chain)
    probes = grow_probe_grammar(chain)
    if report.stabilization_horizon != 6 or report.block_counts != tuple(range(2,9)):
        raise AssertionError("Delayed-signal proof boundary drift")
    if len(probes.exact_minimum_cost_offsets) != 7:
        raise AssertionError("Long successor ladder incorrectly compressed")
    seeded = [independently_seeded_unknown_dynamics(i) for i in range(20)]
    others = [nerode_fixpoint(s) for s in seeded]
    return {
        "source_relative_stabilization_horizon": report.stabilization_horizon,
        "Nerode_class_counts": list(report.block_counts),
        "distinct_states_in_final_quotient": len(report.stable_classes),
        "grammar_expression_count": len(probes.generated_expression_grammar),
        "minimum_source_specific_probe_basis": list(probes.exact_minimum_cost_offsets),
        "declared_minimum_probe_cost": probes.exact_declared_cost,
        "seeded_independent_source_count": len(seeded),
        "all_test_sources_congruence_checked":
            all(r.stabilized_congruence_verified for r in others),
        "full_source_only_not_empirical": True,
        "unbounded_uniform_finite_bound_claimed": False,
    }
