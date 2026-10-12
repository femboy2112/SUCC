"""Probe-coherence horizon: an exact finite carrier-backaction countermodel.

This is a mathematical model of a *particular source-observation protocol*,
not evidence for Gödel/RH independence or a general theorem about proofs.
An observer has one mutable carrier initialized to hidden bits (a,b).
Measuring a returns the current a but overwrites b with zero; measuring b
returns current b but overwrites a with zero. A subsequent reading of
the overwritten bit still has a meaning about the NEW carrier, but cannot
be repurposed as a reading of the ORIGINAL source.

The target is original a XOR b. No adaptive deterministic single-carrier
probe protocol can decide that target with certainty over all four initial
worlds. Two fresh independently prepared carriers, non-disturbing probes,
or a sound prior restriction restore decidability. These positive controls
prevent turning a protocol obstruction into universal logical unprovability.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product


class CarrierHorizonError(ValueError):
    """Invalid source, unsupported or mismatched proof-support context."""


def _bit(value):
    if type(value) is not int or value not in (0, 1):
        raise CarrierHorizonError("A bit must be exactly integer 0 or 1")
    return value


@dataclass(frozen=True)
class InitialSource:
    a: int
    b: int

    def __post_init__(self):
        _bit(self.a)
        _bit(self.b)

    @property
    def parity(self):
        return self.a ^ self.b


@dataclass(frozen=True)
class Reading:
    probe: str
    outcome: int
    before_version: int
    after_version: int
    refers_to_initial_source: bool

    def __post_init__(self):
        if self.probe not in ("a", "b"):
            raise CarrierHorizonError("Unknown initial-source probe")
        _bit(self.outcome)
        if (type(self.before_version) is not int
                or type(self.after_version) is not int
                or self.after_version != self.before_version+1):
            raise CarrierHorizonError("Invalid causal carrier version")


@dataclass(frozen=True)
class DestructiveCarrier:
    """Finite mutable carrier with typed source-origin tracking."""

    a: int
    b: int
    a_refers_to_initial: bool = True
    b_refers_to_initial: bool = True
    version: int = 0
    trace: tuple[Reading, ...] = ()

    def __post_init__(self):
        _bit(self.a)
        _bit(self.b)
        if (type(self.a_refers_to_initial) is not bool
                or type(self.b_refers_to_initial) is not bool
                or type(self.version) is not int or self.version < 0):
            raise CarrierHorizonError("Invalid carrier proof support")

    @classmethod
    def from_source(cls, source: InitialSource):
        if not isinstance(source, InitialSource):
            raise CarrierHorizonError("The initial source must be verified")
        return cls(source.a, source.b)

    def probe(self, name: str) -> "DestructiveCarrier":
        if name == "a":
            reading = Reading(
                "a", self.a, self.version, self.version+1,
                self.a_refers_to_initial,
            )
            return DestructiveCarrier(
                self.a, 0, self.a_refers_to_initial, False,
                self.version+1, self.trace+(reading,),
            )
        if name == "b":
            reading = Reading(
                "b", self.b, self.version, self.version+1,
                self.b_refers_to_initial,
            )
            return DestructiveCarrier(
                0, self.b, False, self.b_refers_to_initial,
                self.version+1, self.trace+(reading,),
            )
        raise CarrierHorizonError("Unknown source-sensitive measurement")

    def initial_support(self):
        """Only observations that truthfully refer to the initial carrier."""
        out = {}
        for item in self.trace:
            if item.refers_to_initial_source:
                if item.probe in out and out[item.probe] != item.outcome:
                    raise CarrierHorizonError("Inconsistent initial source evidence")
                out[item.probe] = item.outcome
        return out

    def target_certificate(self) -> int | None:
        """Only issue initial parity if BOTH initial components are justified."""
        observations = self.initial_support()
        if set(observations) == {"a", "b"}:
            return observations["a"] ^ observations["b"]
        return None

    def coherent_original_probes_remaining(self):
        """Not the same as whether current modified bits still can be read."""
        already = self.initial_support()
        return tuple(
            name for name, still_valid in (
                ("a", self.a_refers_to_initial),
                ("b", self.b_refers_to_initial),
            )
            if still_valid and name not in already
        )


def fixed_probe_trace(source: InitialSource, order: tuple[str, ...]):
    if type(order) is not tuple or len(order) > 64:
        raise CarrierHorizonError("Bounded finite probe order required")
    state = DestructiveCarrier.from_source(source)
    for name in order:
        state = state.probe(name)
    return state


def _wire_trace(state: DestructiveCarrier):
    """Exactly what the embedded agent can learn from valid carrier events."""
    return tuple(
        (r.probe, r.outcome, r.refers_to_initial_source, r.before_version)
        for r in state.trace
    )


def indistinguishable_source_pairs(order: tuple[str, ...]):
    sources = tuple(InitialSource(a,b) for a,b in product((0,1), repeat=2))
    outputs = {s: _wire_trace(fixed_probe_trace(s,order)) for s in sources}
    return tuple(
        (a,b) for i,a in enumerate(sources) for b in sources[i+1:]
        if outputs[a] == outputs[b] and a.parity != b.parity
    )


def local_carrier_no_go():
    """Finite exact impossibility for ALL adaptive single-carrier strategies.

    If a deterministic strategy probes a first, worlds 00 and 01 are
    indistinguishable under every later probe: after that first action,
    both carriers and all source-correct observation records agree.
    If it probes b first, 00 and 10 are indistinguishable. Neither can
    output the correct parity for both worlds; stopping without a probe
    leaves all four possible worlds.
    """
    aa = InitialSource(0,0)
    a_rival = InitialSource(0,1)
    b_rival = InitialSource(1,0)
    after_a = (
        DestructiveCarrier.from_source(aa).probe("a"),
        DestructiveCarrier.from_source(a_rival).probe("a"),
    )
    after_b = (
        DestructiveCarrier.from_source(aa).probe("b"),
        DestructiveCarrier.from_source(b_rival).probe("b"),
    )
    if after_a[0] != after_a[1] or after_b[0] != after_b[1]:
        raise ArithmeticError("First-probe adversarial equivalence is broken")
    for first in ("a","b"):
        for next_actions in ((),("a",),("b",),("a","b"),("b","a")):
            if not indistinguishable_source_pairs((first,)+next_actions):
                raise ArithmeticError("A declared adaptive-protocol barrier disappeared")
    return {
        "status":"FINITE_SINGLE_CARRIER_SOURCE_COHERENCE_NO_GO",
        "all_initial_sources":4,
        "target":"original a XOR original b",
        "initial_meaningful_source_probes":["a","b"],
        "after_read_a_original_b_still_meaningful":False,
        "after_read_b_original_a_still_meaningful":False,
        "first_a_indistinguishable_pair":["00","01"],
        "first_b_indistinguishable_pair":["00","10"],
        "proof_support_unreachable_with_one_carrier":True,
        "global_logical_unprovability_claimed":False,
        "RH_claimed":False,
    }


def independent_carrier_repair(source: InitialSource) -> int:
    """Two correctly re-prepared copies provide a and b from same source."""
    a = DestructiveCarrier.from_source(source).probe("a")
    b = DestructiveCarrier.from_source(source).probe("b")
    sa = a.initial_support()
    sb = b.initial_support()
    if set(sa) != {"a"} or set(sb) != {"b"}:
        raise ArithmeticError("Copy source certificates failed")
    result = sa["a"] ^ sb["b"]
    if result != source.parity:
        raise ArithmeticError("Independent-preparation parity reconstruction failed")
    return result


def nondestructive_probe_repair(source: InitialSource) -> int:
    """Alternative probe class: read-only observations of initial source."""
    if not isinstance(source, InitialSource):
        raise CarrierHorizonError("Require an initial source")
    a,b = source.a,source.b
    return a ^ b


def prior_law_repair(candidates: tuple[InitialSource,...]) -> int | None:
    """A mathematically justified prior may determine target without probes."""
    if type(candidates) is not tuple or not candidates:
        raise CarrierHorizonError("Declared nonempty prior source class required")
    if any(not isinstance(s, InitialSource) for s in candidates):
        raise CarrierHorizonError("Invalid source in proof-language premise")
    possibles = {s.parity for s in candidates}
    return next(iter(possibles)) if len(possibles)==1 else None


def _source_projection(source: InitialSource, probe: str) -> int:
    if probe == "a":
        return source.a
    if probe == "b":
        return source.b
    raise CarrierHorizonError("Only source-initial bit probes are admissible")


def probe_family_determines_target(
    candidates: tuple[InitialSource, ...],
    probes: tuple[str, ...],
) -> bool:
    """Logical factorization of target through source probe observations.

    Test the mathematical condition: for every x,y in the candidate class,
    equal responses on the selected probe family imply equal target.
    This is independent of whether those measurements can COEXIST under
    the physical single-carrier observation protocol.
    """
    if type(candidates) is not tuple or not candidates:
        raise CarrierHorizonError("Declare nonempty source candidates")
    if any(not isinstance(s, InitialSource) for s in candidates):
        raise CarrierHorizonError("Malformed source candidate")
    if (type(probes) is not tuple or len(set(probes)) != len(probes)
            or any(p not in ("a","b") for p in probes)):
        raise CarrierHorizonError("Probe family has an undeclared initial-source observable")
    outputs={}
    for s in candidates:
        key=tuple(_source_projection(s,p) for p in probes)
        if key in outputs and outputs[key]!=s.parity:
            return False
        outputs[key]=s.parity
    return True


def minimal_logical_probe_supports(
    candidates: tuple[InitialSource, ...],
) -> tuple[tuple[str, ...], ...]:
    """All inclusion-minimal source-probe sets that suffice for parity.

    Minimality is only with respect to SELECTING probes in the declared
    basis, not minimal proof length, computation, physical time or bytes.
    """
    options=((),("a",),("b",),("a","b"))
    solutions = [p for p in options
                 if probe_family_determines_target(candidates,p)]
    return tuple(p for p in solutions if not any(
        set(q)<set(p) for q in solutions
    ))


def proof_induced_question_rewiring_demo():
    """Demonstrate logical-support contraction from independently proven laws.

    A proof of a=0 (if valid) changes target a XOR b into b, so only b
    must be queried. A proof of a=b turns original parity into the known
    constant zero. The proofs are trusted premises here; this demo does
    not purport to derive those source-class laws from the destructive data.
    """
    universe=tuple(InitialSource(a,b)
                   for a,b in product((0,1),repeat=2))
    a_zero=tuple(s for s in universe if s.a==0)
    a_eq_b=tuple(s for s in universe if s.a==s.b)
    baseline=minimal_logical_probe_supports(universe)
    with_lemma_a_zero=minimal_logical_probe_supports(a_zero)
    with_lemma_equal=minimal_logical_probe_supports(a_eq_b)
    if (baseline != (("a","b"),)
            or with_lemma_a_zero != (("b",),)
            or with_lemma_equal != ((),)):
        raise ArithmeticError("Contextual minimal source probe supports violated")
    # The original a+b support cannot be executed coherently on one copy:
    source=InitialSource(0,1)
    admissible=tuple(
        fixed_probe_trace(source,order).initial_support()
        for order in (("a","b"),("b","a"))
    )
    if any(set(s)=={"a","b"} for s in admissible):
        raise ArithmeticError("Invalid original-source support was permitted")
    # Under a valid source restriction a=0, b-first resolves the target.
    witness=fixed_probe_trace(source,("b",))
    if (witness.initial_support() != {"b":1}
            or witness.initial_support()["b"] != source.parity):
        raise ArithmeticError("Rewired single-probe source theorem failed")
    return {
        "status":"PROOF_INDUCED_MINIMAL_DEPENDENCY_REWIRING",
        "unrestricted_minimal_probe_supports":[list(x) for x in baseline],
        "with_verified_a_zero_law":[list(x) for x in with_lemma_a_zero],
        "with_verified_a_equal_b_law":[list(x) for x in with_lemma_equal],
        "same_carrier_can_jointly_realize_unrestricted_support":False,
        "single_b_probe_works_after_valid_a_zero_law":True,
        "globally_minimal_proof_encoding_claimed":False,
        "contextual_source_laws_are_independently_proven_premises":True,
    }


def probe_coherence_demo():
    theorem = local_carrier_no_go()
    all_sources = tuple(InitialSource(a,b) for a,b in product((0,1),repeat=2))
    witness = fixed_probe_trace(InitialSource(0,1),("a","b"))
    if (witness.initial_support() != {"a":0}
            or witness.target_certificate() is not None
            or witness.trace[1].refers_to_initial_source):
        raise ArithmeticError("Second measurement was laundered into initial source proof")
    repairs = [independent_carrier_repair(s) for s in all_sources]
    if repairs != [0,1,1,0]:
        raise ArithmeticError("Positive two-copy control failed")
    if any(nondestructive_probe_repair(s) != s.parity for s in all_sources):
        raise ArithmeticError("Nondestructive positive control failed")
    eq_class = (InitialSource(0,0),InitialSource(1,1))
    if prior_law_repair(eq_class) != 0:
        raise ArithmeticError("Valid prior implication is not respected")
    if prior_law_repair(all_sources) is not None:
        raise ArithmeticError("Unrestricted source was spuriously decided")
    rewiring=proof_induced_question_rewiring_demo()
    return {
        **theorem,
        "proof_graph_rewiring":rewiring,
        "second_probe_current_value_is_still_defined":True,
        "second_probe_original_source_value_is_no_longer_defined":True,
        "two_independent_preparations_repair_target":True,
        "non_destructive_probe_repairs_target":True,
        "lawful_source_prior_can_decide_without_experiment":True,
        "proof_target_not_uniformly_decidable_for_unrestricted_single_carrier":True,
        "scope":"Finite deterministic original-source measurement protocols only",
    }
