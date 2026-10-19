"""Exact 3-way Pareto frontier for finite information-repair + online control.

VERIFIED-EXACT-MODEL. A finite observer acquires information about a finite
source by running probes. Three resources are kept *separate* (SUCC physical
carrier vs semantic discipline):

  * retained semantic information  R -- how much the controller learns about
    the source, measured by the exact rational Gini mutual information
    (order-2 / collision / Tsallis-2 information; the classical CART
    "Gini gain"). This is a *rational* surrogate for Shannon mutual
    information chosen precisely so every certificate stays in ``Fraction``:
        R(S) = sum_{x,y} P(x,y)^2 / P(y)  -  sum_x P(x)^2
    which equals  Gini(prior) - E_y[ Gini(posterior | y) ] >= 0 (Jensen, the
    data-processing direction of order-2 information).
  * lawful acquisition cost       C -- a declared nonnegative rational cost
    charged once per scheduled probe (minimize).
  * physical carrier fidelity     F -- how much of the *forwarded datum* (the
    physical carrier pushed downstream) survives, measured by the surviving
    marginal Gini. A DESTRUCTIVE probe consumes its target datum, so that
    datum contributes 0 to F even though it may have contributed to R.

A finite online controller cannot acquire an observation that has not arrived
yet (future causal realizability). Static schedules are scheduled at each
datum's arrival time; adaptive conditioning is audited separately and a
prescient (acausal) "improvement" is REJECTED by ``audit_realizability``.

Classical recoveries, kept distinct from the SUCC extension:
  * The ``classical_corner`` (lossless + free + realizable) is the clairvoyant
    rate-distortion / zero-cost feedback ideal: full information at zero cost
    with the carrier intact. It is CLASSICAL and, when attainable, dominates
    everything. The SUCC content is that in a *costly, destructive, finite*
    catalog it is NOT attainable, and the realizable frontier is a genuine
    3-way trade.
  * The nonnegativity and monotone data-processing of R is classical
    (concavity of Gini impurity).

No RH content. Finite and exact. Every returned objective record carries
``"RH_proved": False``.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


class RepairControlError(ValueError):
    """Malformed model, false schedule, or a causal-realizability violation."""


def _distribution(pairs: tuple, *, what: str) -> dict:
    """Validate an exact finite rational distribution given as (key, prob) pairs."""
    if type(pairs) is not tuple or not pairs:
        raise RepairControlError(f"Nonempty {what} distribution required")
    table: dict = {}
    total = Fraction(0)
    for item in pairs:
        if type(item) is not tuple or len(item) != 2:
            raise RepairControlError(f"{what}: (outcome, probability) pairs required")
        key, prob = item
        if type(prob) is not Fraction or prob < 0:
            raise RepairControlError(f"{what}: nonnegative Fraction probabilities required")
        if key in table:
            raise RepairControlError(f"{what}: duplicate outcome {key!r}")
        table[key] = prob
        total += prob
    if total != 1:
        raise RepairControlError(f"{what}: probabilities must sum to exactly 1, got {total}")
    return table


def gini(pairs: tuple) -> Fraction:
    """Exact rational Gini impurity 1 - sum p_i^2 of a finite distribution."""
    table = _distribution(pairs, what="Gini")
    return Fraction(1) - sum((p * p for p in table.values()), Fraction(0))


@dataclass(frozen=True)
class Source:
    """A finite source over ``arity`` jointly distributed data, exact rationals."""

    arity: int
    distribution: tuple  # ((x_1,...,x_arity), Fraction) pairs

    def __post_init__(self) -> None:
        if type(self.arity) is not int or self.arity < 1:
            raise RepairControlError("Source arity must be a positive int")
        table = _distribution(self.distribution, what="source")
        for key in table:
            if type(key) is not tuple or len(key) != self.arity:
                raise RepairControlError("Each source outcome must be an arity-length tuple")

    def joint(self) -> dict:
        return dict(self.distribution)

    def marginal(self, index: int) -> dict:
        """Exact marginal of datum ``index`` (1-based)."""
        if type(index) is not int or not 1 <= index <= self.arity:
            raise RepairControlError("Datum index out of range")
        out: dict = {}
        for outcome, prob in self.distribution:
            symbol = outcome[index - 1]
            out[symbol] = out.get(symbol, Fraction(0)) + prob
        return out


@dataclass(frozen=True)
class Probe:
    """A single acquisition. ``channel`` is an exact rational observation model.

    ``channel`` maps each symbol of the target datum's alphabet to a
    distribution over observation symbols (deterministic 0/1 rows = perfect or
    coarsening probe; non-0/1 rows = IMPERFECT / noisy probe). ``destructive``
    consumes the target datum (removing it from the forwarded carrier).
    """

    pid: str
    target: int
    channel: tuple  # ((source_symbol, ((obs_symbol, Fraction), ...)), ...)
    cost: Fraction
    destructive: bool

    def __post_init__(self) -> None:
        if type(self.pid) is not str or not self.pid:
            raise RepairControlError("Probe id must be a nonempty string")
        if type(self.target) is not int or self.target < 1:
            raise RepairControlError("Probe target must be a positive datum index")
        if type(self.cost) is not Fraction or self.cost < 0:
            raise RepairControlError("Probe cost must be a nonnegative Fraction")
        if type(self.destructive) is not bool:
            raise RepairControlError("Probe destructive flag must be a bool")
        if type(self.channel) is not tuple or not self.channel:
            raise RepairControlError("Probe channel must be a nonempty tuple of rows")
        seen = set()
        for row in self.channel:
            if type(row) is not tuple or len(row) != 2:
                raise RepairControlError("Channel rows are (source_symbol, obs_pairs)")
            symbol, obs = row
            if symbol in seen:
                raise RepairControlError(f"Duplicate channel row for symbol {symbol!r}")
            seen.add(symbol)
            _distribution(obs, what=f"channel row {symbol!r}")

    def row(self, symbol) -> dict:
        for s, obs in self.channel:
            if s == symbol:
                return dict(obs)
        raise RepairControlError(f"Channel undefined on source symbol {symbol!r}")


@dataclass(frozen=True)
class ScheduledProbe:
    """A probe placed at an integer time, optionally conditioned on earlier obs."""

    pid: str
    schedule_time: int
    conditions_on: tuple = ()

    def __post_init__(self) -> None:
        if type(self.pid) is not str or not self.pid:
            raise RepairControlError("Scheduled probe id must be a nonempty string")
        if type(self.schedule_time) is not int:
            raise RepairControlError("schedule_time must be an int")
        if (type(self.conditions_on) is not tuple
                or any(type(c) is not str for c in self.conditions_on)):
            raise RepairControlError("conditions_on must be a tuple of probe ids")


@dataclass(frozen=True)
class Vertex:
    """An exact objective triple together with the schedule that realizes it."""

    schedule: tuple  # tuple of probe ids
    retained: Fraction
    cost: Fraction
    fidelity: Fraction


class RepairControlModel:
    """A finite channel: source, probe catalog and per-datum arrival times."""

    def __init__(self, source: Source, probes: tuple, arrivals: tuple):
        if type(source) is not Source:
            raise RepairControlError("source must be a Source")
        if (type(probes) is not tuple or not probes
                or any(type(p) is not Probe for p in probes)):
            raise RepairControlError("probes must be a nonempty tuple of Probe")
        pids = [p.pid for p in probes]
        if len(set(pids)) != len(pids):
            raise RepairControlError("Probe ids must be distinct")
        for p in probes:
            if p.target > source.arity:
                raise RepairControlError(f"Probe {p.pid} targets a datum beyond source arity")
            alphabet = set(source.marginal(p.target))
            declared = {s for s, _ in p.channel}
            if not alphabet <= declared:
                raise RepairControlError(
                    f"Probe {p.pid} channel must cover every target symbol")
        if (type(arrivals) is not tuple or len(arrivals) != source.arity
                or any(type(a) is not int for a in arrivals)):
            raise RepairControlError("arrivals must be one int per datum")
        self.source = source
        self.probes = {p.pid: p for p in probes}
        self.arrivals = arrivals

    # -- objectives ---------------------------------------------------------
    def _lookup(self, schedule: tuple) -> list:
        if type(schedule) is not tuple:
            raise RepairControlError("schedule must be a tuple of probe ids")
        chosen = []
        seen = set()
        for pid in schedule:
            if pid not in self.probes:
                raise RepairControlError(f"Unknown probe id {pid!r}")
            if pid in seen:
                raise RepairControlError(f"Probe {pid!r} scheduled twice")
            seen.add(pid)
            chosen.append(self.probes[pid])
        return chosen

    def retained_information(self, schedule: tuple) -> Fraction:
        """Exact Gini mutual information between the source and the observations.

        R = sum_{x,y} P(x,y)^2 / P(y) - sum_x P(x)^2 >= 0.
        """
        chosen = self._lookup(schedule)
        joint = self.source.joint()
        prior_moment = sum((p * p for p in joint.values()), Fraction(0))
        if not chosen:
            return Fraction(0)
        obs_alphabets = [
            tuple(sorted({o for _, obs in p.channel for o, _ in obs}, key=repr))
            for p in chosen]
        py: dict = {}
        s2: dict = {}  # sum_x P(x,y)^2 grouped by y
        for outcome, px in joint.items():
            # weight of each observation-symbol per probe for this outcome
            weights = []
            for p in chosen:
                weights.append(p.row(outcome[p.target - 1]))
            for combo in product(*obs_alphabets):
                w = px
                for p_row, y in zip(weights, combo):
                    w *= p_row.get(y, Fraction(0))
                if w == 0:
                    continue
                py[combo] = py.get(combo, Fraction(0)) + w
                s2[combo] = s2.get(combo, Fraction(0)) + w * w
        joint_moment = sum((s2[y] / py[y] for y in py), Fraction(0))
        return joint_moment - prior_moment

    def acquisition_cost(self, schedule: tuple) -> Fraction:
        """Exact total lawful cost: one declared cost per scheduled probe."""
        return sum((p.cost for p in self._lookup(schedule)), Fraction(0))

    def carrier_fidelity(self, schedule: tuple) -> Fraction:
        """Surviving physical-carrier information: sum of surviving marginal Gini.

        A destructive probe consumes its target, zeroing that datum's survival.
        """
        destroyed = {p.target for p in self._lookup(schedule) if p.destructive}
        total = Fraction(0)
        for index in range(1, self.source.arity + 1):
            if index in destroyed:
                continue
            total += gini(tuple(self.source.marginal(index).items()))
        return total

    def objectives(self, schedule: tuple) -> dict:
        return {
            "schedule": tuple(schedule),
            "retained": self.retained_information(schedule),
            "cost": self.acquisition_cost(schedule),
            "fidelity": self.carrier_fidelity(schedule),
            "status": "VERIFIED-EXACT-MODEL",
            "RH_proved": False,
        }

    def vertex(self, schedule: tuple) -> Vertex:
        return Vertex(tuple(schedule),
                      self.retained_information(schedule),
                      self.acquisition_cost(schedule),
                      self.carrier_fidelity(schedule))

    # -- Pareto frontier ----------------------------------------------------
    @staticmethod
    def dominates(a: Vertex, b: Vertex) -> bool:
        """``a`` dominates ``b``: no worse on every axis and strictly better once.

        Maximize retained and fidelity; minimize cost.
        """
        no_worse = (a.retained >= b.retained and a.cost <= b.cost
                    and a.fidelity >= b.fidelity)
        strictly = (a.retained > b.retained or a.cost < b.cost
                    or a.fidelity > b.fidelity)
        return no_worse and strictly

    def pareto_frontier(self, schedules: tuple) -> tuple:
        """Exact non-dominated vertices over the given candidate schedules.

        Deduplicates schedules with an identical objective triple (keeps the
        first). Returns a tuple of ``Vertex`` sorted for determinism.
        """
        if type(schedules) is not tuple or not schedules:
            raise RepairControlError("schedules must be a nonempty tuple")
        vertices = [self.vertex(s) for s in schedules]
        frontier = []
        for v in vertices:
            if any(self.dominates(u, v) for u in vertices if u is not v):
                continue
            key = (v.retained, v.cost, v.fidelity)
            if any((w.retained, w.cost, w.fidelity) == key for w in frontier):
                continue
            frontier.append(v)
        frontier.sort(key=lambda v: (v.cost, -v.retained, -v.fidelity, v.schedule))
        return tuple(frontier)

    def classical_corner(self) -> dict:
        """CLASSICAL lossless + free + realizable clairvoyant ideal vertex.

        Full observation of every datum (R = Gini(prior)) at zero cost with the
        carrier intact (F = sum of marginal Gini). This is the classical
        rate-distortion / zero-cost feedback corner, recovered as the limiting
        vertex of a hypothetical free, perfect, non-destructive catalog. It is
        NOT an element of a costly/destructive finite catalog.
        """
        prior = tuple(self.source.joint().items())
        full_fidelity = sum(
            (gini(tuple(self.source.marginal(i).items()))
             for i in range(1, self.source.arity + 1)), Fraction(0))
        return {
            "retained": gini(prior),
            "cost": Fraction(0),
            "fidelity": full_fidelity,
            "status": "CLASSICAL",
            "note": "clairvoyant lossless+free+realizable rate-distortion corner",
            "RH_proved": False,
        }

    # -- future causal realizability ---------------------------------------
    def audit_realizability(self, policy: tuple) -> dict:
        """Audit a (possibly adaptive) policy for future causal realizability.

        A scheduled probe is lawful only if (1) it runs no earlier than its
        target datum's arrival, and (2) every observation it conditions on was
        produced by a probe scheduled STRICTLY earlier. Returns a record; the
        first violation is reported. A prescient "improvement" is thereby
        rejected rather than admitted to the frontier.
        """
        if (type(policy) is not tuple or not policy
                or any(type(sp) is not ScheduledProbe for sp in policy)):
            raise RepairControlError("policy must be a nonempty tuple of ScheduledProbe")
        times = {}
        for sp in policy:
            if sp.pid not in self.probes:
                raise RepairControlError(f"Unknown probe id {sp.pid!r}")
            if sp.pid in times:
                raise RepairControlError(f"Probe {sp.pid!r} scheduled twice")
            times[sp.pid] = sp.schedule_time
        for sp in policy:
            arrival = self.arrivals[self.probes[sp.pid].target - 1]
            if sp.schedule_time < arrival:
                return {"realizable": False, "RH_proved": False,
                        "violation": ("premature", sp.pid, sp.schedule_time, arrival)}
            for cond in sp.conditions_on:
                if cond not in times:
                    return {"realizable": False, "RH_proved": False,
                            "violation": ("absent_conditioner", sp.pid, cond)}
                if times[cond] >= sp.schedule_time:
                    return {"realizable": False, "RH_proved": False,
                            "violation": ("acausal", sp.pid, cond,
                                          sp.schedule_time, times[cond])}
        return {"realizable": True, "RH_proved": False, "violation": None}

    def reject_acausal_improvement(self, policy: tuple) -> dict:
        """Falsifier gate: raise if ``policy`` violates future causal realizability.

        Used to reject a claimed Pareto-improving repair that only "wins"
        because it conditions acquisition on an un-arrived observation.
        """
        audit = self.audit_realizability(policy)
        if not audit["realizable"]:
            raise RepairControlError(
                f"Acausal repair rejected: {audit['violation']}")
        return audit

    def static_policy(self, schedule: tuple) -> tuple:
        """Earliest realizable, non-conditioning placement of ``schedule``."""
        chosen = self._lookup(schedule)
        return tuple(ScheduledProbe(p.pid, self.arrivals[p.target - 1], ())
                     for p in chosen)
