"""Exact finite model-dependent probe access and observer traps.

All probes are deterministic and total on a small, declared finite source class.
At each frame an observer instantly incorporates *all selected* true outcomes,
without editing earlier source records. Preferred models are stable while
compatible, but never confused with a singleton compatibility certificate.

All-source counterfactual diagnoses have privileged access to the declared
actual source. They are laboratory proofs, NOT information a trapped observer
could generate from its own history. Physical/noisy probes, actual neural
cognition and RH are outside scope.
"""
from __future__ import annotations

from dataclasses import dataclass


class ObserverTrapError(ValueError):
    """Malformed finite world, probe menu, event, or false causal history."""


def _names(values, *, what):
    if type(values) is not tuple or not 1 <= len(values) <= 16:
        raise ObserverTrapError(f"{what} must be a nonempty bounded immutable tuple")
    if any(type(v) is not str or not v or len(v) > 64 for v in values):
        raise ObserverTrapError(f"{what} labels must be nonempty bounded strings")
    if len(set(values)) != len(values):
        raise ObserverTrapError(f"{what} labels must be distinct")
    return values


@dataclass(frozen=True)
class FiniteProbeWorld:
    """Finite sources × globally conceivable probes → declared exact outcomes."""

    sources: tuple[str, ...]
    probes: tuple[str, ...]
    outcomes: tuple[tuple[str, ...], ...]

    def __post_init__(self):
        _names(self.sources, what="Source")
        _names(self.probes, what="Probe")
        if type(self.outcomes) is not tuple or len(self.outcomes) != len(self.sources):
            raise ObserverTrapError("Require one complete outcome row per source")
        for row in self.outcomes:
            if type(row) is not tuple or len(row) != len(self.probes):
                raise ObserverTrapError("Every source must answer every global probe")
            if any(type(v) is not str or not v or len(v) > 128 for v in row):
                raise ObserverTrapError("Probe outcomes must be exact bounded labels")

    def outcome(self, source: str, probe: str) -> str:
        if source not in self.sources or probe not in self.probes:
            raise ObserverTrapError("A source or probe is absent from the declared world")
        return self.outcomes[self.sources.index(source)][self.probes.index(probe)]

    def distinguishers(self, a: str, b: str) -> tuple[str, ...]:
        if a not in self.sources or b not in self.sources:
            raise ObserverTrapError("Compare only genuine declared source candidates")
        return tuple(p for p in self.probes if self.outcome(a, p) != self.outcome(b, p))


@dataclass(frozen=True)
class ProbePolicy:
    """Access menu by currently preferred model, or by ALL compatible models.

    'all': every accessible probe is evaluated at each SUCC frame.
    'first': unfair sampling of only the first accessible probe.
    'round_robin': cyclically evaluate one probe per frame.

    In 'compatible_union' scope, unioning menus is a *semantic* expansion:
    it presupposes that every unioned probe is actually executable regardless
    of the observer's physically true source. This is a modeling premise.
    """

    menus: tuple[tuple[str, tuple[str, ...]], ...]
    scheduling: str = "all"
    scope: str = "preferred"

    def __post_init__(self):
        if type(self.menus) is not tuple or not self.menus:
            raise ObserverTrapError("Declare a finite complete model-access map")
        keys = []
        for item in self.menus:
            if type(item) is not tuple or len(item) != 2:
                raise ObserverTrapError("Menus must be (model, probe tuple) pairs")
            model, probes = item
            if type(model) is not str or not model:
                raise ObserverTrapError("Every menu needs a named model")
            keys.append(model)
            _names(probes, what="Accessible probe")
        if len(set(keys)) != len(keys):
            raise ObserverTrapError("Duplicate model menu")
        if self.scheduling not in ("all", "first", "round_robin"):
            raise ObserverTrapError("Unknown probe scheduling policy")
        if self.scope not in ("preferred", "compatible_union"):
            raise ObserverTrapError("Unknown model-access scope")

    def validate(self, world: FiniteProbeWorld):
        if not isinstance(world, FiniteProbeWorld):
            raise ObserverTrapError("Require an exact finite world")
        keys = tuple(k for k, _ in self.menus)
        if set(keys) != set(world.sources):
            raise ObserverTrapError("Every possible source-model must have one access menu")
        for _, probes in self.menus:
            if not set(probes).issubset(world.probes):
                raise ObserverTrapError("Model access points outside globally declared probes")
        return True

    def menu(self, model: str) -> tuple[str, ...]:
        for key, probes in self.menus:
            if model == key:
                return probes
        raise ObserverTrapError("Model absent from access policy")

    def accessible(self, frame: "ObserverFrame", world: FiniteProbeWorld) -> tuple[str, ...]:
        self.validate(world)
        if self.scope == "preferred":
            return self.menu(frame.preferred)
        union = {p for model in frame.compatible for p in self.menu(model)}
        return tuple(p for p in world.probes if p in union)

    def selected(self, frame: "ObserverFrame", world: FiniteProbeWorld) -> tuple[str, ...]:
        menu = self.accessible(frame, world)
        if self.scheduling == "all":
            return menu
        if self.scheduling == "first":
            return menu[:1]
        return (menu[frame.stage % len(menu)],)


@dataclass(frozen=True)
class ProbeStep:
    """One exact frame's recorded outcomes, with an explicit causal origin."""

    origin: str                   # "policy" or "external"
    prior_preferred: str
    probes: tuple[str, ...]
    outcomes: tuple[str, ...]


@dataclass(frozen=True)
class ObserverFrame:
    """Actualized immutable data separate from fallible preferred semantics."""

    initial_preference: str
    stage: int
    history: tuple[ProbeStep, ...]
    compatible: tuple[str, ...]
    preferred: str

    @classmethod
    def initial(cls, world: FiniteProbeWorld, policy: ProbePolicy,
                preferred: str) -> "ObserverFrame":
        policy.validate(world)
        if preferred not in world.sources:
            raise ObserverTrapError("Preferred source-model must be declared")
        return cls(preferred, 0, (), world.sources, preferred)

    def _raw_advance(self, world: FiniteProbeWorld, policy: ProbePolicy,
                     actual: str, *, origin: str,
                     external_probes: tuple[str, ...] = ()) -> "ObserverFrame":
        policy.validate(world)
        if type(self.stage) is not int or self.stage < 0:
            raise ObserverTrapError("Invalid observer frame index")
        if actual not in self.compatible:
            raise ObserverTrapError("Actual source contradicts the already stored history")
        if self.preferred not in self.compatible:
            raise ObserverTrapError("Preferred semantics must remain evidence compatible")
        if origin == "policy":
            if external_probes:
                raise ObserverTrapError("Policy observation cannot smuggle external probes")
            probes = policy.selected(self, world)
        elif origin == "external":
            probes = _names(external_probes, what="External intervention")
            if not set(probes).issubset(world.probes):
                raise ObserverTrapError("Intervention must use a declared global probe")
        else:
            raise ObserverTrapError("Unknown observation origin")
        values = tuple(world.outcome(actual, p) for p in probes)
        still = tuple(candidate for candidate in self.compatible
                      if all(world.outcome(candidate, p) == v
                             for p, v in zip(probes, values)))
        if actual not in still:
            raise ArithmeticError("Source-faithful observation accidentally excluded truth")
        preferred = self.preferred if self.preferred in still else still[0]
        step = ProbeStep(origin, self.preferred, probes, values)
        return ObserverFrame(self.initial_preference, self.stage + 1,
                             self.history + (step,), still, preferred)

    def verify(self, world: FiniteProbeWorld, policy: ProbePolicy,
               actual: str) -> bool:
        """Recompute entire causal trace against source and policy.

        This is deterministic replay under an externally supplied truth label,
        NOT independent cryptographic or experimental authentication.
        """
        if not isinstance(self.history, tuple) or len(self.history) != self.stage:
            raise ObserverTrapError("Causal history and SUCC clock disagree")
        replay = ObserverFrame.initial(world, policy, self.initial_preference)
        for old in self.history:
            if not isinstance(old, ProbeStep):
                raise ObserverTrapError("Malformed causal step")
            replay = replay._raw_advance(
                world, policy, actual, origin=old.origin,
                external_probes=old.probes if old.origin == "external" else (),
            )
            if replay.history[-1] != old:
                raise ObserverTrapError("Causal record or policy provenance was rewritten")
        if replay != self:
            raise ObserverTrapError("Semantic model or version space differs from replay")
        return True

    def succ(self, world: FiniteProbeWorld, policy: ProbePolicy,
             actual: str) -> "ObserverFrame":
        """Endogenous SUCC: immediately assimilate every scheduled source result."""
        self.verify(world, policy, actual)
        return self._raw_advance(world, policy, actual, origin="policy")

    def intervene(self, world: FiniteProbeWorld, policy: ProbePolicy,
                  actual: str, probes: tuple[str, ...]) -> "ObserverFrame":
        """EXOGENOUS change to access: explicit, auditable, never silent."""
        self.verify(world, policy, actual)
        return self._raw_advance(world, policy, actual,
                                 origin="external", external_probes=probes)

    @property
    def identified(self) -> bool:
        """Full-source identification, NOT mere stability of preferred model."""
        return len(self.compatible) == 1


@dataclass(frozen=True)
class PairTrapCertificate:
    """External theorem checker: a truth-labeled, finite stationary-policy result."""

    status: str
    actual: str
    preferred: str
    admissible_menu: tuple[str, ...]
    future_support: tuple[str, ...]
    globally_separating: tuple[str, ...]
    locally_separating: tuple[str, ...]
    eventually_selected_separators: tuple[str, ...]
    first_refuting_succ: int | None
    stationary_future_fiber: tuple[str, ...]
    self_confirming_false_model: bool
    observer_can_infer_actual_from_this_certificate: bool = False


def certify_stationary_pair(world: FiniteProbeWorld, policy: ProbePolicy,
                            frame: ObserverFrame, actual: str) -> PairTrapCertificate:
    """Exact iff certificate for model-preferred stationary-access policies.

    If the preferred model remains compatible, the probe menu is stationary.
    A false preferred model survives indefinitely IFF no eventually selected
    probe distinguishes it from the source. Exhaustive 'all' and cyclic
    'round_robin' have support=entire menu; 'first' sees only menu[0].

    This externally truth-labeled diagnosis does not supply a trapped agent
    with an impossible endogenous identification oracle.
    """
    if policy.scope != "preferred":
        raise ObserverTrapError("Stationary-pair theorem requires preferred-only menu")
    frame.verify(world, policy, actual)
    preferred = frame.preferred
    menu = policy.accessible(frame, world)
    support = menu if policy.scheduling in ("all", "round_robin") else menu[:1]
    global_diff = world.distinguishers(actual, preferred)
    local_diff = tuple(p for p in menu if p in global_diff)
    support_diff = tuple(p for p in support if p in global_diff)

    if actual == preferred:
        status = "correct-model"
    elif not global_diff:
        status = "global-probe-blind"
    elif support_diff:
        status = "eventual-discrimination"
    elif local_diff:
        status = "scheduling-trap"
    else:
        status = "access-trap"

    period = len(menu) if policy.scheduling == "round_robin" else 1
    delay = next(
        (k + 1 for k in range(period)
         if any(p in global_diff for p in policy.selected(
             ObserverFrame(frame.initial_preference, frame.stage + k,
                           frame.history, frame.compatible, frame.preferred), world))),
        None,
    ) if support_diff else None
    fiber = tuple(candidate for candidate in frame.compatible
                  if all(world.outcome(candidate, p) == world.outcome(actual, p)
                         for p in support))
    return PairTrapCertificate(
        status, actual, preferred, menu, support, global_diff, local_diff,
        support_diff, delay, fiber,
        actual != preferred and delay is None,
        False,
    )


def observer_trap_demo() -> dict:
    """Positive, mutation and repair controls in one small deterministic world."""
    world = FiniteProbeWorld(
        ("A", "B"), ("echo", "separator"),
        (("same", "A"), ("same", "B")),
    )
    closed = ProbePolicy((("A", ("echo",)), ("B", ("echo", "separator"))))
    frame = ObserverFrame.initial(world, closed, "A")
    analysis = certify_stationary_pair(world, closed, frame, "B")
    for _ in range(5):
        frame = frame.succ(world, closed, "B")
    repaired = frame.intervene(world, closed, "B", ("separator",))
    union = ProbePolicy(closed.menus, scope="compatible_union")
    union_frame = ObserverFrame.initial(world, union, "A").succ(world, union, "B")
    unfair = ProbePolicy((("A", ("echo", "separator")),
                          ("B", ("echo", "separator"))), scheduling="first")
    fair = ProbePolicy(unfair.menus, scheduling="round_robin")
    bad_schedule = certify_stationary_pair(
        world, unfair, ObserverFrame.initial(world, unfair, "A"), "B")
    good_schedule = certify_stationary_pair(
        world, fair, ObserverFrame.initial(world, fair, "A"), "B")
    fair_frame = ObserverFrame.initial(world, fair, "A")
    fair_frame = fair_frame.succ(world, fair, "B").succ(world, fair, "B")
    assert (analysis.status == "access-trap" and not frame.identified
            and repaired.identified and union_frame.identified
            and bad_schedule.status == "scheduling-trap"
            and good_schedule.first_refuting_succ == 2
            and fair_frame.identified)
    return {
        "status": "FINITE_OBSERVER_TRAP_CERTIFIED",
        "actual_source_external": "B",
        "preferred_model": "A",
        "model_access_trap": analysis.status,
        "five_succ_updates_preferred": frame.preferred,
        "five_succ_updates_compatible": list(frame.compatible),
        "global_separator": list(analysis.globally_separating),
        "external_intervention_identified": repaired.identified,
        "compatible_union_identified": union_frame.identified,
        "unfair_schedule_trap": bad_schedule.status,
        "round_robin_first_refutation_succ": good_schedule.first_refuting_succ,
        "source_records_rewritten": False,
        "physical_cognition_claimed": False,
        "RH_or_Godel_independence_claimed": False,
    }
