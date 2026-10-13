"""Source-changing epistemic transport, exact finite declarations only.

This extends existing SourceChart/RelationalIntervention and FiniteCarrier
interfaces; it does not invent physical source authentication or proof authority.
Paper proofs in CAMBRIAN_A_FOUNDATIONS.md are classical set/probability theory.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from typing import Hashable, Sequence

from .causal_nerode_succ import SourceChart, SourceTransportError
from .eodcs_relational_choice import RelationalIntervention, relational_descent
from .field_relative_closure import FiniteField
from .noncommuting_proof_transport import (
    FiniteCarrier, finite_future_equivalence, finite_separator,
)


def powerset(values: Sequence):
    values = tuple(values)
    for size in range(len(values) + 1):
        yield from combinations(values, size)


@dataclass(frozen=True)
class RelationalBaseChange:
    """Two independent quantified relational lifting gates.

    source_lift: R^-1[p^-1 V] = q^-1[Rbar^-1 V], all report V.
    target_lift: R[q^-1 U] = p^-1[Rbar[U]], all old-report U.
    Witness (old report, current state) is missing in the latter.
    """
    source_id: str
    before_epoch: int
    after_epoch: int
    source_lift: bool
    target_lift: bool
    source_defect: tuple[str, str] | None
    target_defect: tuple[str, str] | None
    complete_declared_source: bool

    @property
    def both_exact(self) -> bool:
        return self.source_lift and self.target_lift


def relational_base_change(source: RelationalIntervention) -> RelationalBaseChange:
    """Compute exact gates; same report support is not complete state lifting."""
    if not isinstance(source, RelationalIntervention):
        raise SourceTransportError("Use the existing typed relational source")
    if not source.all_states_exhaustive:
        raise SourceTransportError("All-predicate equality requires complete source tables")
    descent = relational_descent(source)
    source_defect = None
    if descent.source_witness is not None:
        source_defect = descent.source_witness[:2]
    target_defect = None
    for old_report, states in source.before.fibers():
        reached = {t for x in states for t in source.possible_states(x)}
        reached_reports = {source.after.report(t) for t in reached}
        for target in source.after.states:
            if source.after.report(target) in reached_reports and target not in reached:
                target_defect = (old_report, target)
                break
        if target_defect is not None:
            break
    return RelationalBaseChange(
        source.before.source_id, source.before.epoch, source.after.epoch,
        descent.descended_to_set_valued_observer, target_defect is None,
        source_defect, target_defect, source.all_states_exhaustive,
    )


def forward_evidence(source: RelationalIntervention, old_reports: Sequence[str]) -> dict:
    """Actual source pushforward and abstract post-report completion side by side."""
    if not source.all_states_exhaustive:
        raise SourceTransportError("Incomplete declared evidence domain")
    selected = set(old_reports)
    if not selected <= set(source.before.image()):
        raise SourceTransportError("Evidence outside the original report image")
    reached = {t for x in source.before.states
               if source.before.report(x) in selected
               for t in source.possible_states(x)}
    reports = {source.after.report(t) for t in reached}
    completed = {t for t in source.after.states if source.after.report(t) in reports}
    return {"actual_states": tuple(sorted(reached)),
            "abstract_completed_states": tuple(sorted(completed)),
            "equal": reached == completed}


@dataclass(frozen=True)
class BayesianBaseChange:
    source_id: str
    exact_for_all_old_evidence_and_post_predicates: bool
    # a,b,y; both sides of the exact cross-product equality
    defect: tuple[str, str, str, Q, Q] | None
    null_post_reports: tuple[str, ...]


def bayesian_base_change(source: RelationalIntervention,
                         joint: tuple[tuple[Q, ...], ...]) -> BayesianBaseChange:
    """A independent of Y conditional on B=p(Y), for complete rational J(X,Y).

    The law must have exactly the declared relation support. Null conditioning
    reports are recorded and NEVER normalized. This proves no probabilities
    from support sets, and no actual source attestation from matching labels.
    """
    if not source.all_states_exhaustive:
        raise SourceTransportError("Complete source required for conditional law")
    if (type(joint) is not tuple or len(joint) != len(source.before.states)
            or any(type(row) is not tuple or len(row) != len(source.after.states)
                   for row in joint)):
        raise SourceTransportError("Joint law must cover both typed state charts")
    if any(not isinstance(v, Q) or v < 0 for row in joint for v in row):
        raise SourceTransportError("Require nonnegative exact rational weights")
    if sum((v for row in joint for v in row), Q()) != 1:
        raise SourceTransportError("Joint weights must normalize exactly")
    for i, x in enumerate(source.before.states):
        for j, y in enumerate(source.after.states):
            if (joint[i][j] > 0) != (y in source.possible_states(x)):
                raise SourceTransportError("Joint support disagrees with declared source relation")
    ys = source.after.states
    m_y = {y: sum((joint[i][j] for i in range(len(joint))), Q())
           for j, y in enumerate(ys)}
    m_b = {b: sum((m_y[y] for y in ys if source.after.report(y) == b), Q())
           for b in source.after.image()}
    nulls = tuple(b for b, mass in m_b.items() if mass == 0)
    for a, xs in source.before.fibers():
        indices = tuple(source.before.states.index(x) for x in xs)
        m_ay = {y: sum((joint[i][j] for i in indices), Q()) for j, y in enumerate(ys)}
        for b in source.after.image():
            m_ab = sum((m_ay[y] for y in ys if source.after.report(y) == b), Q())
            for y in ys:
                if source.after.report(y) != b:
                    continue
                left, right = m_ay[y] * m_b[b], m_ab * m_y[y]
                if left != right:
                    return BayesianBaseChange(source.before.source_id, False,
                                               (a, b, y, left, right), nulls)
    return BayesianBaseChange(source.before.source_id, True, None, nulls)


def retained_claims(old_report: Sequence[Hashable],
                    retained_report: Sequence[Hashable]) -> bool:
    """All Boolean claims measurable in old report remain so iff kernel inclusion."""
    old, kept = tuple(old_report), tuple(retained_report)
    if not old or len(old) != len(kept):
        raise SourceTransportError("Reports must share one nonempty original-source domain")
    decoder = {}
    for a, b in zip(old, kept):
        hash(a); hash(b)
        if b in decoder and decoder[b] != a:
            return False
        decoder[b] = a
    return True


def public_history_square(field: FiniteCarrier,
                          paths: tuple[tuple[str, ...], ...]) -> dict:
    """Actual commuting truncation square for a bounded execution span.

    Root and endpoint are audit labels only. The bottom report arrow deletes
    the last public event. Neither privileged label enters that arrow.
    """
    if (type(paths) is not tuple or not paths or len(set(paths)) != len(paths)
            or any(type(path) is not tuple or not path or len(path) > 32 for path in paths)
            or len({len(path) for path in paths}) != 1):
        raise SourceTransportError("Distinct nonempty equal-depth bounded paths required")
    rows = []
    for initial in range(field.count):
        for path in paths:
            full, prefix = field.run(initial, path), field.run(initial, path[:-1])
            long_report, short_report = full.public_signature, prefix.public_signature
            if long_report[:-1] != short_report:
                raise AssertionError("Public record truncation failed to commute")
            rows.append({"audit_original_state": initial,
                         "audit_current_state": full.terminal_state,
                         "path": path, "long_report": long_report,
                         "short_report": short_report})
    roots = sorted(set(row["audit_original_state"] for row in rows))
    epistemic = []
    for report in sorted({row["long_report"] for row in rows}):
        possible_roots = tuple(root for root in roots
                               if any(row["audit_original_state"] == root
                                      and row["long_report"] == report for row in rows))
        epistemic.append((report, possible_roots))
    return {"source_id": field.source_id, "basis_id": field.basis_id,
            "execution_rows": tuple(rows), "public_source_fibers": tuple(epistemic),
            "truncation_square_commutes": True,
            "privileged_root_in_public_report": False,
            "ideal_completion_performed": False,
            "physical_source_authenticated": False}


def pointwise_minimal_supports(field: FiniteField, state: Hashable,
                               target: str) -> tuple[tuple[str, ...], ...]:
    """Inclusion-minimal receipt supports proving this source's target value.

    Unlike FiniteField.factor, support is allowed to depend on the observed
    values. Every rival with another target value must disagree on some probe.
    No inference from an empty source fiber and no carrier feasibility promise.
    """
    if state not in field.states or target not in field.targets:
        raise SourceTransportError("Pointwise certificate source/target absent")
    i = field.states.index(state)
    rivals = tuple(j for j in range(len(field.states))
                   if field.targets[target][j] != field.targets[target][i])
    result = []
    for support in powerset(tuple(field.probes)):
        if any(set(old) <= set(support) for old in result):
            continue
        if all(any(field.probes[p][i] != field.probes[p][j] for p in support)
               for j in rivals):
            result.append(support)
    return tuple(result)


def toolkit_pair_verdict(field: FiniteCarrier, first: int, second: int) -> dict:
    """Reuse two existing independent search/pruning routes; no arbitrary new solver."""
    path = finite_separator(field, first, second)
    equivalent_pairs = finite_future_equivalence(field)
    pair = tuple(sorted((first, second)))
    equivalent = pair in equivalent_pairs
    if equivalent != (path is None):
        raise AssertionError("Pair search and greatest-equivalence pruning disagree")
    return {"state_pair": pair, "separator": path,
            "toolkit_relative_dark": equivalent,
            "closed_equivalence_witness": equivalent_pairs if equivalent else (),
            "physical_source_authenticated": False}


def multiobserver_information(reports: Sequence[Sequence[Hashable]]) -> dict:
    """Finite many-observer common factor and fused report on ONE source domain.

    Common relation = equivalence closure of union of observer kernels.
    Fusion relation = intersection of their kernels. Exact deterministic facts
    are intended, not stochastic common information or statistical independence.
    """
    rows = tuple(tuple(row) for row in reports)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise SourceTransportError("Observers need total reports on one nonempty source")
    for row in rows:
        for value in row:
            hash(value)
    n = len(rows[0])
    parent = list(range(n))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for row in rows:
        representatives = {}
        for i, value in enumerate(row):
            if value in representatives:
                a, b = root(i), root(representatives[value])
                parent[max(a, b)] = min(a, b)
            else:
                representatives[value] = i
    common = tuple(root(i) for i in range(n))
    labels = {value: i for i, value in enumerate(sorted(set(common)))}
    common = tuple(labels[value] for value in common)
    fused = tuple(tuple(row[i] for row in rows) for i in range(n))
    return {"common_factor": common, "common_classes": len(set(common)),
            "fused_report": fused, "fused_classes": len(set(fused)),
            "all_source_states_reconstructed": len(set(fused)) == n}


def and_source(width: int) -> FiniteField:
    if type(width) is not int or not 1 <= width <= 12:
        raise SourceTransportError("Exact AND probe example width must be 1..12")
    states = tuple(range(1 << width))
    return FiniteField("cambrian-AND-original-v1", "bits-v1", states,
                       {f"bit{i}": tuple((s >> i) & 1 for s in states)
                        for i in range(width)},
                       {"AND": tuple(int(s == (1 << width) - 1) for s in states)})
