"""Joint outcome/current-state source-law realization of stochastic miniature SUCC.

Exact stochastic lumpability on a *complete declared* finite carrier.
Keeping separate report and next-state marginals is insufficient.
Physical source authentication and actual execution remain external gates.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping


class MiniStochasticError(ValueError):
    pass


# A row atom is (public_report, next_state, exact_probability).
Row = tuple[tuple[str, str, Q], ...]


def _states(states: tuple[str, ...]) -> set[str]:
    if not states or any(not isinstance(s, str) or not s for s in states) or \
            len(states) != len(set(states)):
        raise MiniStochasticError("nonempty unique carrier states required")
    return set(states)


def _row(row: Row, states: set[str]) -> None:
    if not isinstance(row, tuple) or not row:
        raise MiniStochasticError("complete positive probability row required")
    total = Q()
    for report, nxt, prob in row:
        if (not isinstance(report, str) or not report or nxt not in states or
                type(prob) not in (int, Q) or prob <= 0):
            raise MiniStochasticError("malformed or unsupported joint atom")
        total += Q(prob)
    if total != 1:
        raise MiniStochasticError("joint probability row must sum exactly to one")


@dataclass(frozen=True)
class StochasticCarrier:
    states: tuple[str, ...]
    kernels: Mapping[str, Mapping[str, Row]]
    preparations: tuple[str, ...]
    source_id: str

    def __post_init__(self):
        states = _states(self.states)
        if not self.source_id or not isinstance(self.source_id, str):
            raise MiniStochasticError("source declaration required")
        if not self.kernels or not self.preparations or not set(self.preparations) <= states:
            raise MiniStochasticError("preparations and action laws required")
        for name, table in self.kernels.items():
            if not isinstance(name, str) or not name or set(table) != states:
                raise MiniStochasticError("incomplete source instrument")
            for row in table.values():
                _row(row, states)


@dataclass(frozen=True)
class StochasticMini:
    states: tuple[str, ...]
    kernels: Mapping[str, Mapping[str, Row]]
    initial: str
    source_id: str

    def __post_init__(self):
        states = _states(self.states)
        if self.initial not in states or not self.source_id or not self.kernels:
            raise MiniStochasticError("missing mini state/source/transition")
        for name, table in self.kernels.items():
            if not isinstance(name, str) or not name or set(table) != states:
                raise MiniStochasticError("incomplete mini instrument")
            for row in table.values():
                _row(row, states)


def push_row(row: Row, decoder: Mapping[str, str]) -> dict[tuple[str, str], Q]:
    result = {}
    for z, c, p in row:
        key = (z, decoder[c])
        result[key] = result.get(key, Q()) + Q(p)
    return {k: v for k, v in result.items() if v}


def joint_factor(parent: StochasticCarrier, mini: StochasticMini,
                 decoder: Mapping[str, str], compiled_actions: Mapping[str, str]) -> dict:
    """Exact iff for ALL original current-state Dirac priors + public policies.

    Public policies select actions using previously observed public receipts,
    not hidden original/current source labels. One mini action = one actual
    parent action. More general multi-event macros require labelled full traces.
    """
    if mini.source_id != parent.source_id:
        raise MiniStochasticError("source versions differ")
    if set(decoder) != set(parent.states) or set(decoder.values()) != set(mini.states):
        return {"certified": False, "reason": "incomplete_source_factor", "RH_proved": False}
    if set(compiled_actions) != set(mini.kernels) or any(
            action not in parent.kernels for action in compiled_actions.values()):
        raise MiniStochasticError("not an authorized physical action")
    if not any(decoder[c] == mini.initial for c in parent.preparations):
        return {"certified": False, "reason": "unavailable_initial_preparation", "RH_proved": False}
    # Every claimed mini state must have at least one positive-mass lawful
    # path from an authorized preparation; abstract source labels are not free.
    reached = set(parent.preparations)
    queue = list(parent.preparations)
    for c in queue:
        for a in parent.kernels:
            for _, nxt, prob in parent.kernels[a][c]:
                if prob > 0 and nxt not in reached:
                    reached.add(nxt)
                    queue.append(nxt)
    missing = sorted(set(mini.states) - {decoder[c] for c in reached})
    if missing:
        return {"certified": False, "reason": "unreachable_mini_state",
                "witness": {"unrealized_states": missing}, "RH_proved": False}
    total = 0
    for c in parent.states:
        for mini_a, real_a in compiled_actions.items():
            actual = push_row(parent.kernels[real_a][c], decoder)
            expected = push_row(mini.kernels[mini_a][decoder[c]],
                                {q: q for q in mini.states})
            total += 1
            if actual != expected:
                return {"certified": False, "reason": "joint_receipt_state_law_mismatch",
                        "witness": {"carrier_state": c, "action": mini_a,
                                    "actual_joint": {str(k): str(v) for k, v in actual.items()},
                                    "expected_joint": {str(k): str(v) for k, v in expected.items()}},
                        "report_and_next_marginals_may_agree": True,
                        "RH_proved": False}
    return {"certified": True, "realization": "all_prior_stochastic_mini_factor",
            "source_action_joint_rows_checked": total,
            "source_names_preserved": True,
            "hidden_source_policy_access_granted": False,
            "physical_instrument_authenticated": False,
            "no_new_physical_sensing_inferred": True,
            "RH_proved": False}
