"""Twin observers: identical source, empirical probes and reasoning; different focus.

Two language presentations are modeled over ONE immutable circle observation
interface. A uses polynomial/Cartesian identities, B trig/angular identities.
Both can run the same instruments. Their research focus may select different
next probes; focus is *not* physical capability or mathematical truth.

The source family here is constant-speed integer-winding uniform rotations.
A finite snapshot of exact point probes can be incomplete for both observers,
while one exact normalized-tangent observation identifies that integer in
this DECLARED family. Arbitrary smooth paths have a different identifiability
theorem and are documented separately.

Neither hashes nor finite source-table agreement authenticate the physical
provenance of received testimony; true-source simulation is only a test rig.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json

from .circle_translation import (
    CirclePolynomial, TrigFourierPolynomial, GaussianRational,
    cardinal_point, periodic_point_signature, rational_stereographic_chart,
)


class TwinCircleError(ValueError):
    """An invalid shared probe, context, language, or source record."""


def _q(n) -> Fraction:
    if type(n) is int or isinstance(n, Fraction):
        return Fraction(n)
    raise TwinCircleError("Exact integer or rational required")


def _canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _digest(obj) -> str:
    return sha256(_canonical(obj)).hexdigest()


@dataclass(frozen=True)
class CircleProbe:
    """A language-neutral actualizable, time-indexed measurement protocol."""

    kind: str
    time: Fraction

    def __post_init__(self):
        if self.kind not in ("point", "tangent"):
            raise TwinCircleError("Only shared point/tangent probe types implemented")
        t = _q(self.time)
        if not 0 <= t <= 1:
            raise TwinCircleError("Measured loop time must be in [0,1]")
        object.__setattr__(self, "time", t)

    def response(self, winding: int) -> Fraction:
        if type(winding) is not int:
            raise TwinCircleError("Uniform rotation winding must be integer")
        return Fraction(winding) if self.kind == "tangent" else (
            Fraction(winding)*self.time) % 1

    def key(self):
        return (self.kind, str(self.time))


@dataclass(frozen=True)
class TwinCircleBasis:
    """Identical empirical opportunities, source assumptions and reasoner."""

    winding_sources: tuple[int, ...]
    probes: tuple[CircleProbe, ...]
    reasoning_signature: str = "exact-rational-circle-ring-plus-angular-derivative-v1"
    orientation: int = 1

    def __post_init__(self):
        if (type(self.winding_sources) is not tuple
                or not 1 <= len(self.winding_sources) <= 128
                or any(type(k) is not int for k in self.winding_sources)
                or len(set(self.winding_sources)) != len(self.winding_sources)):
            raise TwinCircleError("Finite declared distinct integer source class required")
        if (type(self.probes) is not tuple or not 1 <= len(self.probes) <= 128
                or any(not isinstance(p, CircleProbe) for p in self.probes)
                or len(set(self.probes)) != len(self.probes)):
            raise TwinCircleError("Finite shared set of distinct time probes required")
        if self.orientation != 1 or type(self.orientation) is not int:
            raise TwinCircleError("Twin benchmark fixes one jointly calibrated orientation")
        if type(self.reasoning_signature) is not str or not self.reasoning_signature:
            raise TwinCircleError("Shared logical interpretation is required")

    @property
    def fingerprint(self):
        return _digest({
            "winding_sources": self.winding_sources,
            "probes": [p.key() for p in self.probes],
            "reasoner": self.reasoning_signature,
            "orientation": self.orientation,
        })

    def compatible(self, records: tuple["CircleEvent", ...]) -> tuple[int, ...]:
        if type(records) is not tuple:
            raise TwinCircleError("Source evidence must be immutable")
        observed_indices = set()
        for event in records:
            if not isinstance(event, CircleEvent):
                raise TwinCircleError("Malformed source observation")
            if event.probe_index in observed_indices:
                raise TwinCircleError("A finite probe may be recorded only once")
            if event.probe_index not in range(len(self.probes)):
                raise TwinCircleError("Event refers to undeclared physical instrument")
            observed_indices.add(event.probe_index)
        possible = tuple(
            k for k in self.winding_sources
            if all(self.probes[e.probe_index].response(k) == e.value for e in records)
        )
        if not possible:
            raise TwinCircleError("Observed source records contradict declared source class")
        return possible


@dataclass(frozen=True)
class CircleEvent:
    probe_index: int
    value: Fraction
    origin: str

    def __post_init__(self):
        if type(self.probe_index) is not int:
            raise TwinCircleError("Probe index must be genuine integer")
        object.__setattr__(self, "value", _q(self.value))
        if type(self.origin) is not str or not self.origin:
            raise TwinCircleError("Source origin label required; this is not authentication")


@dataclass(frozen=True)
class TwinCircleObserver:
    """Difference is field-specific FOCUS, not instruments or intelligence."""

    language: str
    focus_order: tuple[int, ...]
    records: tuple[CircleEvent, ...] = ()
    local_steps: int = 0
    knowledge_aided_steps: int = 0

    def validate(self, basis: TwinCircleBasis) -> tuple[int, ...]:
        if self.language not in ("polynomial", "trigonometric"):
            raise TwinCircleError("Observer must use one of two mathematical languages")
        if (type(self.focus_order) is not tuple
                or set(self.focus_order) != set(range(len(basis.probes)))
                or len(self.focus_order) != len(basis.probes)
                or any(type(n) is not int for n in self.focus_order)):
            raise TwinCircleError("Focus may re-order but never remove shared probes")
        if (type(self.local_steps) is not int or self.local_steps < 0
                or type(self.knowledge_aided_steps) is not int
                or self.knowledge_aided_steps < 0):
            raise TwinCircleError("Observer clocks must be exact nonnegative counters")
        return basis.compatible(self.records)

    def available(self, basis: TwinCircleBasis) -> tuple[int, ...]:
        self.validate(basis)
        return tuple(range(len(basis.probes)))  # identical opportunity space

    def next_preferred_probe(self, basis: TwinCircleBasis):
        self.validate(basis)
        used = {e.probe_index for e in self.records}
        return next((i for i in self.focus_order if i not in used), None)

    def local_succ(self, basis: TwinCircleBasis, actual_winding: int):
        current = self.validate(basis)
        if actual_winding not in current:
            raise TwinCircleError("Actual source conflicts with existing records")
        i = self.next_preferred_probe(basis)
        if i is None:
            return self
        event = CircleEvent(i, basis.probes[i].response(actual_winding),
                            self.language)
        state = TwinCircleObserver(
            self.language, self.focus_order, self.records + (event,),
            self.local_steps+1, self.knowledge_aided_steps)
        state.validate(basis)
        return state

    def knowledge_position(self, basis: TwinCircleBasis):
        """Truth-facing closure independent of personal event provenance.

        Both twins know the same mathematical propositions and have identical
        empirical/reasoning ability when source fiber and derived predictions
        match. Re-executable experiment history is a stronger operational
        synchronization requirement checked separately.
        """
        possible = self.validate(basis)
        inferred = tuple(
            (i, choices[0])
            for i, probe in enumerate(basis.probes)
            if len(choices := tuple(sorted(
                {probe.response(k) for k in possible}))) == 1
        )
        return (basis.fingerprint, possible, inferred,
                tuple(range(len(basis.probes))), basis.reasoning_signature)

    def normalized_semantic_position(self, basis: TwinCircleBasis):
        """Language- and focus-independent shared mathematical knowledge.

        Focus is intentionally excluded: both have identical ability to
        execute any named probe, but may prioritize experiments differently.
        """
        compatible = self.validate(basis)
        deduced = tuple(
            (i, values[0])
            for i, probe in enumerate(basis.probes)
            if len(values := tuple(sorted({probe.response(k) for k in compatible}))) == 1
        )
        executed = tuple(sorted((e.probe_index, e.value) for e in self.records))
        future = tuple(i for i in range(len(basis.probes))
                       if i not in {e.probe_index for e in self.records})
        return (basis.fingerprint, compatible, deduced,
                self.available(basis), executed, future,
                basis.reasoning_signature)


def _possible_values(basis, state, probe_index):
    return tuple(sorted({
        basis.probes[probe_index].response(k)
        for k in state.validate(basis)
    }))


def _context_digest(state, basis):
    pos = state.normalized_semantic_position(basis)
    # JSON cannot encode Fraction by default.
    return _digest(repr(pos))


def encode_twin_relative_delta(
    sender: TwinCircleObserver, receiver: TwinCircleObserver, basis: TwinCircleBasis,
) -> bytes:
    """Send pending sender-origin facts as relative directions and values.

    Sender and receiver may have independently observed different probes.
    A received delta constructs their source-compatible *union* of events.
    The next step direction is the INDEX among recipient's as-yet-unmeasured
    legal probes (not an absolute probe name). Shared source table and
    decoder are excluded from communication bit-cost claims.
    """
    sender.validate(basis)
    receiver.validate(basis)
    known = {e.probe_index: e.value for e in receiver.records}
    sender_map = {e.probe_index: e for e in sender.records}
    if any(i in sender_map and sender_map[i].value != v
           for i, v in known.items()):
        raise TwinCircleError("Source records disagree about one shared physical probe")
    pending = [e for e in sender.records if e.probe_index not in known]
    trial = receiver
    steps = []
    for event in pending:
        remaining = tuple(i for i in range(len(basis.probes))
                          if i not in {e.probe_index for e in trial.records})
        if event.probe_index not in remaining:
            raise TwinCircleError("Sender tried to send duplicate physical observation")
        relative_path = remaining.index(event.probe_index)
        possibilities = _possible_values(basis, trial, event.probe_index)
        if event.value not in possibilities:
            raise TwinCircleError("Incompatible source outcome in relative delta")
        outcome_code = None if len(possibilities) == 1 else possibilities.index(event.value)
        steps.append([relative_path, outcome_code, event.origin])
        trial = TwinCircleObserver(
            trial.language, trial.focus_order,
            trial.records + (event,), trial.local_steps,
            trial.knowledge_aided_steps,
        )
        trial.validate(basis)
    return _canonical({
        "protocol":"twin-circle-relative-v1",
        "basis":basis.fingerprint,
        "start":_context_digest(receiver,basis),
        "end":_context_digest(trial,basis),
        "steps":steps,
    })


def decode_twin_relative_delta(
    receiver: TwinCircleObserver, payload: bytes, basis: TwinCircleBasis,
) -> TwinCircleObserver:
    """One K-SUCC; combines compatible independent histories by testimony."""
    receiver.validate(basis)
    if type(payload) is not bytes or not 0 < len(payload) <= 65536:
        raise TwinCircleError("Require one bounded finite message")
    try:
        message = json.loads(payload.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise TwinCircleError("Malformed finite delta message") from exc
    if (type(message) is not dict
            or set(message) != {"protocol","basis","start","end","steps"}
            or message["protocol"] != "twin-circle-relative-v1"
            or message["basis"] != basis.fingerprint
            or message["start"] != _context_digest(receiver,basis)
            or type(message["steps"]) is not list
            or len(message["steps"]) > len(basis.probes)):
        raise TwinCircleError("A message cannot cross an unverified or stale base")
    state = receiver
    for step in message["steps"]:
        remaining = tuple(i for i in range(len(basis.probes))
                          if i not in {e.probe_index for e in state.records})
        if (type(step) is not list or len(step) != 3
                or type(step[0]) is not int
                or not 0 <= step[0] < len(remaining)
                or type(step[2]) is not str or not step[2]):
            raise TwinCircleError("Invalid relative physical measurement path")
        relative_index, index, origin = step
        i = remaining[relative_index]
        values = _possible_values(basis,state,i)
        if len(values) == 1:
            if index is not None:
                raise TwinCircleError("Predictable probe outcome cannot invent information")
            value = values[0]
        else:
            if type(index) is not int or not 0 <= index < len(values):
                raise TwinCircleError("Unknown empirical outcome cannot be inferred freely")
            value = values[index]
        state = TwinCircleObserver(
            state.language, state.focus_order,
            state.records + (CircleEvent(i,value,origin),),
            state.local_steps, state.knowledge_aided_steps,
        )
        state.validate(basis)
    if _context_digest(state,basis) != message["end"]:
        raise TwinCircleError("Recipient did not reproduce declared operational position")
    return TwinCircleObserver(
        state.language,state.focus_order,state.records,
        state.local_steps,state.knowledge_aided_steps+1,
    )

def evaluate_fourier_at_cardinal(
    polynomial: TrigFourierPolynomial, phase,
) -> Fraction:
    """Exact angular-side evaluation at 0, 1/4, 1/2 or 3/4 turns."""
    phase = _q(phase) % 1
    q = phase*4
    if q.denominator != 1:
        raise TwinCircleError("Finite rational Fourier value is only exact at cardinal phases")
    powers = ((1,0),(0,1),(-1,0),(0,-1))
    total = GaussianRational()
    for n, coeff in polynomial.coefficients:
        re,im = powers[(n*q.numerator)%4]
        total = total + coeff*GaussianRational(re,im)
    if total.imag != 0:
        raise ArithmeticError("Real Fourier translation failed at cardinal point")
    return total.real


def translated_probe_report(polynomial: CirclePolynomial, phase) -> tuple[Fraction,Fraction]:
    """Independently evaluate equivalent A and B functions on same raw point."""
    phase = _q(phase) % 1
    quarter = 4*phase
    if quarter.denominator != 1:
        raise TwinCircleError("This exact rational test samples cardinal point phases only")
    x,y = cardinal_point(quarter.numerator,1)
    a = polynomial.at_circle(x,y)
    b = evaluate_fourier_at_cardinal(
        TrigFourierPolynomial.from_circle(polynomial),phase)
    return (a,b)


def normalized_tangent_in_polynomial_language(x, y, winding: int) -> Fraction:
    """omega(x,y)(gamma'_k)/(2*pi) = k using rational circle coordinates."""
    x,y = _q(x),_q(y)
    if x*x+y*y != 1 or type(winding) is not int:
        raise TwinCircleError("Normalized tangent requires rational circle point and integer k")
    dx = -Fraction(winding)*y
    dy = Fraction(winding)*x
    return x*dy-y*dx


def normalized_tangent_in_trig_language(winding: int) -> Fraction:
    """(d theta/dt)/(2*pi) for gamma_k(t)=exp(2*pi*i*k*t)."""
    if type(winding) is not int:
        raise TwinCircleError("Declared uniform angular velocity must be integer")
    return Fraction(winding)


@dataclass(frozen=True)
class HiddenSmoothLoopWitness:
    """Structural witness, not an executed infinite-derivative computation."""
    sample_times: tuple[Fraction, ...]
    open_gap: tuple[Fraction,Fraction]
    original_winding: int
    shifted_winding: int
    all_finite_sample_jets_same_by_flat_step_proof: bool
    physical_infinite_jet_measurements_executed: bool = False


def hidden_smooth_loop_between_samples(samples, winding: int) -> HiddenSmoothLoopWitness:
    """Construct a gap allowing a smooth extra loop invisible to finite jets.

    For any finite sample times insert a flat transition h(t) from 0 to 1
    between adjacent sampled times. Multiplying gamma_k by e^(2*pi*i*h(t))
    preserves the position AND every derivative at each sampled time, but
    increases winding by one. The all-orders statement requires its separate
    analytic mathematical proof; finite software checks the existence
    of the sample-free gap, not infinitely many derivatives.
    """
    if type(samples) is not tuple or len(samples) > 128:
        raise TwinCircleError("Finite rational sampling schedule required")
    pts = tuple(sorted({Fraction(0),Fraction(1)} |
                       {_q(t) for t in samples}))
    if any(t < 0 or t > 1 for t in pts) or type(winding) is not int:
        raise TwinCircleError("Closed finite loop and integer winding required")
    gaps = tuple((a,b) for a,b in zip(pts,pts[1:]) if a < b)
    if not gaps:
        raise TwinCircleError("There must be a real unobserved time interval")
    a,b = gaps[0]
    if any(a < t < b for t in pts):
        raise ArithmeticError("Chosen interval contained a sampled point")
    return HiddenSmoothLoopWitness(tuple(pts),(a,b),winding,winding+1,True)


def twin_circle_demo() -> dict:
    """Same evidence, ability and reasoning; differing focus and one-step relay."""
    probes = tuple(CircleProbe("point",t)
                   for t in (Fraction(0), Fraction(1,4), Fraction(1,2),
                             Fraction(3,4), Fraction(1))) + (
        CircleProbe("point",Fraction(1,8)),
        CircleProbe("tangent",Fraction(0)),
    )
    basis = TwinCircleBasis((1,5,9),probes)
    raw = tuple(CircleEvent(i,basis.probes[i].response(1),"shared")
                for i in range(5))
    a = TwinCircleObserver("polynomial",tuple(range(7)),raw)
    b = TwinCircleObserver("trigonometric",(6,5,0,1,2,3,4),raw)
    assert (a.normalized_semantic_position(basis) ==
            b.normalized_semantic_position(basis))
    first_a = a.local_succ(basis,1)  # chooses phase t=1/8
    first_b = b.local_succ(basis,1)  # chooses normalized tangent t=0
    assert first_a.validate(basis) == (1,9)
    assert first_b.validate(basis) == (1,)
    delta = encode_twin_relative_delta(first_b,first_a,basis)
    caught = decode_twin_relative_delta(first_a,delta,basis)
    assert caught.knowledge_position(basis) == first_b.knowledge_position(basis)
    assert caught.normalized_semantic_position(basis) != first_b.normalized_semantic_position(basis)
    # Twin B still lacks A's independent, now-predictable point observation;
    # one return delta aligns their complete future single-use probe frontiers.
    return_delta = encode_twin_relative_delta(caught,first_b,basis)
    reunited_b = decode_twin_relative_delta(first_b,return_delta,basis)
    assert reunited_b.normalized_semantic_position(basis) == \
           caught.normalized_semantic_position(basis)
    assert (caught.local_steps == 1 and caught.knowledge_aided_steps == 1
            and caught.records[-1].origin == "trigonometric"
            and reunited_b.records[-1].origin == "polynomial")
    x,y = rational_stereographic_chart(Fraction(1,2))
    assert normalized_tangent_in_polynomial_language(x,y,1) == \
           normalized_tangent_in_trig_language(1)
    ambiguity = hidden_smooth_loop_between_samples(
        (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)),1)
    assert ambiguity.original_winding != ambiguity.shifted_winding
    return {
        "status":"EXACT_TWIN_OBSERVER_LANGUAGE_INVARIANCE",
        "initial_mathematical_knowledge_equal":True,
        "physical_probe_capabilities_identical":True,
        "reasoning_capability_identical":True,
        "initial_candidate_windings":list(a.validate(basis)),
        "polynomial_focus_first_probe":str(basis.probes[5].time),
        "trig_focus_first_probe":"normalized tangent at t=0",
        "after_polynomial_focus_candidates":list(first_a.validate(basis)),
        "after_trig_focus_candidates":list(first_b.validate(basis)),
        "knowledge_aided_delta_steps":caught.knowledge_aided_steps,
        "recipient_new_empirical_frames":caught.local_steps-first_a.local_steps,
        "post_first_relay_knowledge_equal": caught.knowledge_position(basis) == first_b.knowledge_position(basis),
        "post_first_relay_operational_history_equal":False,
        "post_reciprocal_relay_operational_position_equal":reunited_b.normalized_semantic_position(basis) == caught.normalized_semantic_position(basis),
        "reciprocal_knowledge_aided_steps_total":caught.knowledge_aided_steps+reunited_b.knowledge_aided_steps,
        "algebraic_and_trig_normalized_tangent_agree":True,
        "smooth_path_finite_jets_can_still_hide_an_extra_loop":True,
        "full_physical_continuum_trajectory_measured":False,
        "source_provenance_cryptographically_authenticated":False,
        "RH_claimed":False,
    }
