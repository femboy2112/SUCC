"""Proof-carrying finite SUCC miniature realization over a declared parent carrier.

Distinguishes (1) literal invariant subcarriers, (2) factor/quotient observers,
(3) independently executable dual observers, and (4) ungrounded models.
All state/action/report tables are supplied and do NOT authenticate physics.
Only finite exact deterministic source contracts are certified.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from fractions import Fraction as Q
from typing import Mapping


class MiniatureContractError(ValueError):
    pass


@dataclass(frozen=True)
class Carrier:
    states: tuple[str, ...]
    actions: Mapping[str, Mapping[str, str | None]]
    reports: Mapping[str, str]
    preparations: tuple[str, ...]
    source_id: str

    def __post_init__(self):
        _unique(self.states, "carrier state")
        _unique(tuple(self.actions), "carrier action")
        _unique(self.preparations, "preparation")
        if not self.preparations or not set(self.preparations) <= set(self.states):
            raise MiniatureContractError("missing/undeclared physical preparation")
        if not self.source_id or not isinstance(self.source_id, str):
            raise MiniatureContractError("source ID required")
        if set(self.reports) != set(self.states) or not all(
                isinstance(y, str) for y in self.reports.values()):
            raise MiniatureContractError("complete carrier reports required")
        for action, table in self.actions.items():
            if set(table) != set(self.states):
                raise MiniatureContractError(f"incomplete source action {action}")
            if any(x is not None and x not in self.states for x in table.values()):
                raise MiniatureContractError(f"action {action} targets unknown carrier")


@dataclass(frozen=True)
class Mini:
    states: tuple[str, ...]
    actions: Mapping[str, Mapping[str, str]]
    reports: Mapping[str, str]
    initial: str
    source_id: str

    def __post_init__(self):
        _unique(self.states, "mini state")
        _unique(tuple(self.actions), "mini action")
        if self.initial not in self.states:
            raise MiniatureContractError("unrecognized mini initial state")
        if not self.source_id or not isinstance(self.source_id, str):
            raise MiniatureContractError("source ID required")
        if set(self.reports) != set(self.states) or not all(
                isinstance(y, str) for y in self.reports.values()):
            raise MiniatureContractError("complete mini reports required")
        for action, table in self.actions.items():
            if set(table) != set(self.states) or not set(table.values()) <= set(self.states):
                raise MiniatureContractError(f"incomplete mini action {action}")


def _unique(items: tuple[str, ...], kind: str):
    if not items or any(not isinstance(s, str) or not s for s in items):
        raise MiniatureContractError(f"nonempty string {kind}s required")
    if len(items) != len(set(items)):
        raise MiniatureContractError(f"duplicate {kind}")


def _check_program(parent: Carrier, mini: Mini,
                   macros: Mapping[str, tuple[str, ...]], budget: int):
    if mini.source_id != parent.source_id:
        raise MiniatureContractError("source namespace mismatch")
    if type(budget) is not int or budget < 0 or budget > 100:
        raise MiniatureContractError("finite execution budget required")
    if set(macros) != set(mini.actions):
        raise MiniatureContractError("each miniature action needs a compiled parent program")
    for name, word in macros.items():
        if not isinstance(word, tuple) or len(word) > budget or any(
                token not in parent.actions for token in word):
            raise MiniatureContractError(f"unavailable or overbudget program for {name}")


def _run(parent: Carrier, start: str, word: tuple[str, ...]):
    c = start
    trace = [c]
    for pos, a in enumerate(word):
        nxt = parent.actions[a][c]
        if nxt is None:
            return None, (pos, a, c), trace
        c = nxt
        trace.append(c)
    return c, None, trace


def _reachable(parent: Carrier, seeds: tuple[str, ...],
               words: tuple[tuple[str, ...], ...] | None = None) -> set[str]:
    """Explore actual carrier states, never imagined/decoded source states."""
    queue = list(seeds)
    reached = set(queue)
    words = words if words is not None else tuple((a,) for a in parent.actions)
    for c in queue:
        for word in words:
            nxt, error, _ = _run(parent, c, word)
            if error or nxt in reached:
                continue
            reached.add(nxt)
            queue.append(nxt)
    return reached


def _reject(reason: str, witness: dict) -> dict:
    return {"certified": False, "reason": reason, "witness": witness,
            "source_authenticated_externally": False, "RH_proved": False}


def _accept(kind: str, **kwargs) -> dict:
    return {"certified": True, "realization": kind,
            "source_authenticated_externally": False, "RH_proved": False,
            **kwargs}


def compile_subcarrier(parent: Carrier, mini: Mini, encoding: Mapping[str, str],
                       macros: Mapping[str, tuple[str, ...]], budget: int = 20) -> dict:
    """A genuine invariant encoded finite subcarrier, not merely a model."""
    _check_program(parent, mini, macros, budget)
    if set(encoding) != set(mini.states) or not set(encoding.values()) <= set(parent.states):
        return _reject("unresolved_encoding", {})
    if len(set(encoding.values())) != len(mini.states):
        return _reject("noninjective_encoding", {})
    if encoding[mini.initial] not in parent.preparations:
        return _reject("unavailable_initial_preparation", {"initial": mini.initial})
    accessible = _reachable(parent, parent.preparations)
    ghosts = sorted(set(encoding.values()) - accessible)
    if ghosts:
        return _reject("unreachable_encoded_mini_state", {"ghosts": ghosts})
    validated_traces = []
    for q in mini.states:
        c = encoding[q]
        if parent.reports[c] != mini.reports[q]:
            return _reject("wrong_source_report", {"mini_state": q, "carrier_state": c,
                                                   "actual_report": parent.reports[c]})
        for a in mini.actions:
            target, error, trace = _run(parent, c, macros[a])
            if error:
                return _reject("unsafe_or_unperformed_primitive", {"mini_state": q,
                                 "mini_action": a, "source_trace": trace, "failure": error})
            validated_traces.append({"mini_state": q, "mini_action": a,
                                     "expanded_parent_actions": list(macros[a]),
                                     "source_state_trace": trace,
                                     "intermediate_reports": [parent.reports[x] for x in trace]})
            if target != encoding[mini.actions[a][q]]:
                return _reject("noncommuting_carrier_square", {"mini_state": q,
                       "mini_action": a, "source_trace": trace, "expected":
                       encoding[mini.actions[a][q]], "actual": target})
    return _accept("invariant_subcarrier", states=len(mini.states),
                   strict_inside=len(mini.states) < len(parent.states),
                   initial_prepared=True, maximum_macro_cost=max(map(len, macros.values())),
                   literal_inclusion=all(encoding[q] == q for q in mini.states),
                   source_action_squares_checked=len(mini.states)*len(mini.actions),
                   full_macro_histories=validated_traces)


def compile_factor(parent: Carrier, mini: Mini, decoder: Mapping[str, str],
                   macros: Mapping[str, tuple[str, ...]], budget: int = 20,
                   public_map: Mapping[str, str] | None = None) -> dict:
    """Certified factor: model-mediated miniature without invariant section.

    Every parent state, not just one friendly representative, must satisfy
    each source action and report square. The decoder may describe a hidden
    internal machine state; ONLY its declared public report is a measurement.
    """
    _check_program(parent, mini, macros, budget)
    if set(decoder) != set(parent.states) or set(decoder.values()) != set(mini.states):
        return _reject("incomplete_or_nononto_factor", {})
    if not any(decoder[c] == mini.initial for c in parent.preparations):
        return _reject("unavailable_initial_preparation", {})
    accessible = _reachable(parent, parent.preparations)
    unactualized = sorted(set(mini.states) - {decoder[c] for c in accessible})
    if unactualized:
        return _reject("unreachable_mini_state", {"unactualized": unactualized})
    validated_traces = []
    if public_map is not None and set(public_map) != set(parent.reports.values()):
        return _reject("incomplete_public_report_translation", {})
    for c in parent.states:
        q = decoder[c]
        public = (parent.reports[c] if public_map is None else public_map[parent.reports[c]])
        if public != mini.reports[q]:
            return _reject("public_report_does_not_descend", {"carrier_state": c,
                           "mini_state": q, "actual_report": parent.reports[c]})
        for a in mini.actions:
            target, error, trace = _run(parent, c, macros[a])
            if error:
                return _reject("unsafe_or_unperformed_primitive", {"carrier_state": c,
                       "mini_action": a, "source_trace": trace, "failure": error})
            validated_traces.append({"carrier_state": c, "mini_action": a,
                                     "expanded_parent_actions": list(macros[a]),
                                     "source_state_trace": trace,
                                     "intermediate_reports": [parent.reports[x] for x in trace]})
            if decoder[target] != mini.actions[a][q]:
                return _reject("factor_action_not_well_defined", {"carrier_state": c,
                     "mini_action": a, "source_trace": trace,
                     "expected": mini.actions[a][q], "actual": decoder[target]})
    return _accept("lawful_behavioral_factor", states=len(mini.states),
                   parent_states=len(parent.states), maximum_macro_cost=max(map(len, macros.values())),
                   common_source_squares_checked=len(parent.states)*len(mini.actions),
                   new_physical_instrument_created=False,
                   decoding_is_not_new_sensing=True,
                   full_macro_histories=validated_traces)


def compile_dual_product(parent: Carrier, left: Mini, right: Mini,
                         left_decode: Mapping[str, str], right_decode: Mapping[str, str],
                         left_word: tuple[str, ...], right_word: tuple[str, ...],
                         public_pair: Mapping[str, tuple[str, str]],
                         budget: int = 20) -> dict:
    """Joint source realization plus noninterfering action squares.

    A right- and a left-factor separately existing does not guarantee the
    full product is supported by actual parent states. The designated actions
    preserve the other mini's decoded state, and any hidden carrier holonomy
    remains a separate question.
    """
    if (left.source_id != parent.source_id or right.source_id != parent.source_id or
            len(left.actions) != 1 or len(right.actions) != 1):
        raise MiniatureContractError("common source and one selected action per mini required")
    if type(budget) is not int or not 0 <= budget <= 100:
        raise MiniatureContractError("invalid resource budget")
    if any(not isinstance(w, tuple) or len(w) > budget or any(
           a not in parent.actions for a in w) for w in (left_word, right_word)):
        raise MiniatureContractError("missing or unbudgeted physical macro")
    if set(left_decode) != set(parent.states) or set(right_decode) != set(parent.states):
        return _reject("incomplete_joint_factor", {})
    if set(left_decode.values()) != set(left.states) or set(right_decode.values()) != set(right.states):
        return _reject("nononto_single_factor", {})
    paired = {(left_decode[c], right_decode[c]) for c in parent.states}
    all_pairs = set(product(left.states, right.states))
    if paired != all_pairs:
        return _reject("ghost_joint_states", {"missing_pairs": sorted(all_pairs-paired)})
    starts = tuple(c for c in parent.preparations if (left_decode[c], right_decode[c])
                   == (left.initial, right.initial))
    if not starts:
        return _reject("joint_initial_not_preparable", {})
    reachable = _reachable(parent, starts, (left_word, right_word))
    attainable_pairs = {(left_decode[c], right_decode[c]) for c in reachable}
    if attainable_pairs != all_pairs:
        return _reject("joint_states_not_constructible_from_preparation",
                       {"unreachable_pairs": sorted(all_pairs-attainable_pairs)})
    if set(public_pair) != set(parent.reports.values()):
        return _reject("missing_public_observation_map", {})
    l_action = next(iter(left.actions))
    r_action = next(iter(right.actions))
    for c in parent.states:
        l, r = left_decode[c], right_decode[c]
        if public_pair[parent.reports[c]] != (left.reports[l], right.reports[r]):
            return _reject("unjustified_joint_observation", {"source_state": c})
        for side, word in (("left", left_word), ("right", right_word)):
            nxt, error, trace = _run(parent, c, word)
            if error:
                return _reject("unsafe_joint_action", {"side": side, "trace": trace})
            observed = (left_decode[nxt], right_decode[nxt])
            expected = ((left.actions[l_action][l], r) if side == "left"
                        else (l, right.actions[r_action][r]))
            if observed != expected:
                return _reject("cross_observer_interference", {"side": side,
                          "start_state": c, "trace": trace,
                          "expected": expected, "actual": observed})
    return _accept("independent_joint_factor", product_states=len(all_pairs),
                   parent_states=len(parent.states), initial_prepared=True,
                   source_action_squares_checked=2*len(parent.states),
                   observable_actions_commute=True,
                   physical_actions_proved_commuting=False,
                   true_independent_devices_not_proved=True)


def future_partition(parent: Carrier) -> dict:
    """Construct the smallest full-action deterministic observable quotient.

    The finite states are *model states*. Action closure must be complete;
    physical implementation and calibration are externally unverified.
    """
    if any(v is None for step in parent.actions.values() for v in step.values()):
        raise MiniatureContractError("total actions needed for this minimizer")
    states = tuple(sorted(parent.states))
    symbols = tuple(sorted(parent.actions))

    def rank(signatures):
        values = {key: j for j, key in enumerate(sorted(set(signatures.values())))}
        return {c: values[signatures[c]] for c in states}

    cls = rank({c: parent.reports[c] for c in states})
    stages = [len(set(cls.values()))]
    while True:
        refined = rank({c: (parent.reports[c], tuple(cls[parent.actions[a][c]]
                                    for a in symbols)) for c in states})
        stages.append(len(set(refined.values())))
        if all((refined[c] == refined[d]) == (cls[c] == cls[d])
               for c in states for d in states):
            cls = refined
            break
        if len(stages) > len(states) + 1:
            raise ArithmeticError("finite partition refinement failed to stabilize")
        cls = refined
    blocks = tuple(tuple(c for c in states if cls[c] == i)
                   for i in sorted(set(cls.values())))
    qname = {c: f"q{cls[c]}" for c in states}
    qstates = tuple(f"q{i}" for i in range(len(blocks)))
    quotient = Mini(qstates, {a: {qname[block[0]]:
         qname[parent.actions[a][block[0]]] for block in blocks} for a in symbols},
         {qname[block[0]]: parent.reports[block[0]] for block in blocks},
         qname[parent.preparations[0]], parent.source_id)
    check = compile_factor(parent, quotient, qname, {a: (a,) for a in symbols})
    if not check["certified"] and check["reason"] not in (
        "unavailable_initial_preparation", "unreachable_mini_state"
    ):
        raise ArithmeticError(f"constructed quotient failed semantic checks: {check}")
    return {"mini": quotient, "decoder": qname, "blocks": blocks,
            "stages": stages, "verified": True,
            "carrier_realization_certified": check["certified"],
            "carrier_realization_obstruction": (None if check["certified"]
                                              else check["reason"]),
            "final_model_states": len(blocks),
            "parent_states": len(parent.states), "RH_proved": False}


def dark_target_witness(parent: Carrier, target: Mapping[str, str]) -> dict:
    """Proof that old-action programs cannot reveal a target-disagreeing pair."""
    if set(target) != set(parent.states):
        raise MiniatureContractError("original target must be defined on complete source")
    partition = future_partition(parent)
    for block in partition["blocks"]:
        for i, c in enumerate(block):
            for d in block[i+1:]:
                if target[c] != target[d]:
                    return _reject("target_not_in_parent_observation_closure",
                             {"source_pair": (c, d), "target_values": (target[c], target[d]),
                              "all_finite_action_word_reports_equal": True})
    return _accept("target_constancy_on_behavioral_fibers",
                   existing_actions_sufficient_in_ideal_closure=True,
                   separate_new_physical_access_needed=False)


def compile_nested_factor(parent: Carrier, intermediate: Mini, child: Mini,
                          first_decoder: Mapping[str, str],
                          second_decoder: Mapping[str, str],
                          first_macros: Mapping[str, tuple[str, ...]],
                          second_macros: Mapping[str, tuple[str, ...]],
                          budget: int = 100) -> dict:
    """Composition of two certified finite mini factories is itself certified.

    All child actions are macro substitutions into authentic parent actions.
    A nested interpreter gains expressive convenience, not new sensor access.
    """
    first = compile_factor(parent, intermediate, first_decoder,
                           first_macros, budget=budget)
    if not first['certified']:
        return _reject('uncertified_parent_to_intermediate', {'first': first})
    mid_carrier = Carrier(intermediate.states, intermediate.actions,
                          intermediate.reports, (intermediate.initial,),
                          intermediate.source_id)
    second = compile_factor(mid_carrier, child, second_decoder,
                            second_macros, budget=budget)
    if not second['certified']:
        return _reject('uncertified_intermediate_to_child', {'second': second})
    composite_decoder = {c: second_decoder[first_decoder[c]] for c in parent.states}
    composite_macros = {}
    for a, word in second_macros.items():
        expanded = tuple(token for mid_action in word for token in first_macros[mid_action])
        if len(expanded) > budget:
            return _reject('composite_exceeds_parent_resource_budget',
                           {'mini_action': a, 'expanded_cost': len(expanded),
                            'budget': budget})
        composite_macros[a] = expanded
    final = compile_factor(parent, child, composite_decoder,
                           composite_macros, budget=budget)
    if not final['certified']:
        # The proof obligations should force this to succeed. Refuse the entire
        # construction rather than trusting an invalid composite diagram.
        raise ArithmeticError(f'valid individual factors failed composition: {final}')
    return _accept('nested_miniature_carrier_descent',
                   intermediate_states=len(intermediate.states),
                   child_states=len(child.states),
                   all_three_carrier_squares_verified=True,
                   effective_parent_action_words={a:list(w) for a,w in composite_macros.items()},
                   effective_parent_step_cost=max(map(len, composite_macros.values())),
                   no_new_primitive_action_constructed=True,
                   no_physical_speedup_implied=True,
                   expanded_parent_history=final['full_macro_histories'])


def cyclic_successor_factor(m: int, n: int) -> dict:
    """Closed-form iff for a successor-equivariant Z/m -> Z/n factor.

    A surjective factor exists iff n divides m. An equivariant section
    exists iff m=n. The latter is about action-equivariant sections, not
    arbitrary set-theoretic injections.
    """
    if type(m) is not int or type(n) is not int or not 2 <= n <= m <= 100_000:
        raise MiniatureContractError("finite clock sizes require 2<=n<=m<=100000")
    valid = m % n == 0
    return {"parent_clock": m, "mini_clock": n,
            "surjective_successor_factor_exists": valid,
            "equivariant_subcarrier_section_exists": m == n,
            "proper_factor_is_nonsplit": valid and m > n,
            "counterexample_if_not_factor": None if valid else
                 f"parent identity after {m} successors contradicts mini period {n}",
            "RH_proved": False}


def all_depth_successor_shell_defect(q: int, level: int) -> dict:
    """Exact finite certificate of [S*, P_level] delta_(q**level).

    For every positive integer depth, the formal proof gives the signed
    coefficient 2/(q**level+1) at cell q**level-1. This is a Wold-shell
    non-intertwining obstruction, not a completed arithmetic Weil pairing.
    """
    if type(q) is not int or type(level) is not int or \
            not 2 <= q <= 20 or not 1 <= level <= 8:
        raise MiniatureContractError('finite dilation and positive depth required')
    m = q ** level
    if 2*m > 100_000:
        raise MiniatureContractError('shell witness exceeds exact source budget')
    from observational_succ.dual_shell_observer import project_level, shift_pullback
    f = {m: Q(1)}
    before = shift_pullback(project_level(f, q, level))
    after = project_level(shift_pullback(f), q, level)
    got = before.get(m-1, Q()) - after.get(m-1, Q())
    expected = Q(2, m + 1)
    if got != expected:
        raise ArithmeticError('additive/dilation boundary witness mismatch')
    return {'q': q, 'level': level, 'source_cell': m,
            'detected_at_cell': m-1, 'signed_commutator': str(got),
            'nonzero_at_every_finite_depth_proved_by_formula': True,
            'physical_sensor_installed': False, 'RH_proved': False}
