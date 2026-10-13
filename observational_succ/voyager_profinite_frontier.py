"""Voyager: source-realization gap between finite probes and infinite profiles.

Mathematical inputs ONLY: source-declared complete deterministic machines,
finite binary trace prefixes, and exactly generated target sequences.
No original-source access to a completed infinite experiment is asserted.

General facts proved in the dossier, kernel checked where explicitly marked:
* Any finite complete source has a <=|S| finite-probe refutation if an
  imagined all-future profile cannot be realized by any original state.
* A source class with UNBOUNDED finite memory can realize EVERY finite
  binary prefix without realizing the whole global profile in one state.
* Every fixed finite deterministic machine has ultimately periodic traces.
  Powers-of-two pulses are NOT ultimately periodic (constructive witness).
* Finite consistent observational shadows therefore do not certify that
  an ideal/projective-limit profile is a source-realized trajectory.

This is classical automata/Stone inverse-limit mathematics repackaged as a
typed SUCC epistemic boundary, not independent mathematical priority or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from typing import Callable


class VoyagerError(ValueError):
    """A source, experiment, resource, or proof contract was violated."""


def _binary(word: tuple[int, ...]) -> None:
    if type(word) is not tuple or any(type(x) is not int or x not in (0, 1) for x in word):
        raise VoyagerError("Exact finite binary observation word required")


@dataclass(frozen=True)
class TraceSource:
    source_id: str
    epoch: int
    basis: str
    states: tuple[str, ...]
    output: tuple[int, ...]
    successor: tuple[str, ...]
    initial: str
    source_authenticated: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.states) is not tuple or not self.states
                or len(set(self.states)) != len(self.states)
                or any(type(s) is not str or not s for s in self.states)
                or type(self.output) is not tuple
                or type(self.successor) is not tuple
                or len(self.output) != len(self.states)
                or len(self.successor) != len(self.states)
                or any(type(x) is not int or x not in (0, 1) for x in self.output)
                or any(s not in self.states for s in self.successor)
                or self.initial not in self.states or
                type(self.source_authenticated) is not bool
                or self.source_authenticated):
            raise VoyagerError("Finite source requires total exact law and honest metadata")

    def step(self, state: str) -> str:
        if state not in self.states:
            raise VoyagerError("Probe outside source")
        return self.successor[self.states.index(state)]

    def report(self, state: str) -> int:
        if state not in self.states:
            raise VoyagerError("Probe outside source")
        return self.output[self.states.index(state)]

    def trace(self, horizon: int, *, start: str | None = None) -> tuple[int, ...]:
        if type(horizon) is not int or not 0 <= horizon <= 50000:
            raise VoyagerError("Finite bounded source probe horizon required")
        s = self.initial if start is None else start
        if s not in self.states:
            raise VoyagerError("Unknown initial source")
        out=[]
        for _ in range(horizon):
            out.append(self.report(s))
            s = self.step(s)
        return tuple(out)

    def eventual_period(self, *, start: str | None = None) -> tuple[int, int]:
        """Exact least first-repeat state certificate, source-specific."""
        s = self.initial if start is None else start
        if s not in self.states:
            raise VoyagerError("Unknown source state")
        first={}
        t=0
        while s not in first:
            first[s]=t
            s=self.step(s)
            t+=1
            if t>len(self.states):
                raise AssertionError("Pigeonhole bound violated")
        preperiod=first[s]
        period=t-first[s]
        if period<1 or preperiod+period>len(self.states):
            raise AssertionError("Malformed exact finite-cycle witness")
        if any(self.trace(1,start=self.trace_state(n, start=start))[0] !=
               self.trace(1,start=self.trace_state(n+period,start=start))[0]
               for n in range(preperiod,preperiod+len(self.states)+1)):
            raise AssertionError("Alleged cycle fails a future observation")
        return preperiod,period

    def trace_state(self, steps: int, *, start: str | None = None) -> str:
        if type(steps) is not int or not 0 <= steps <= 50000:
            raise VoyagerError("Invalid finite source SUCC count")
        s=self.initial if start is None else start
        if s not in self.states:
            raise VoyagerError("Unknown source address")
        for _ in range(steps):
            s=self.step(s)
        return s


def eventual_zero_lift(prefix: tuple[int, ...], *,
                       source_id: str = "declared-eventual-zero") -> TraceSource:
    """A lawful FINITE machine generating prefix then zero forever.

    The source class is ALL eventual-zero traces (unbounded complexity),
    while this returned machine is ONE finite witness for ONE finite prefix.
    """
    _binary(prefix)
    if not source_id:
        raise VoyagerError("Source provenance required")
    n=len(prefix)
    states=tuple("q"+str(i) for i in range(n+1))
    return TraceSource(
        source_id,0,"head-and-shift",states,
        prefix+(0,),
        tuple(states[min(i+1,n)] for i in range(n+1)),
        states[0])


def all_one(n:int)->int:
    if type(n) is not int or n<0:
        raise VoyagerError("Stream coordinate must be natural")
    return 1


def powers_of_two_pulse(n:int)->int:
    if type(n) is not int or n<0:
        raise VoyagerError("Stream coordinate must be natural")
    return int(n>=1 and n&(n-1)==0)


def power_two_period_refutation(preperiod:int,period:int)->dict:
    """Universal formula, EXACT witness for any proposed eventual period.

    Choose power of two q > max(preperiod, period); then q+period lies
    strictly between q and 2q, so pulse(q)=1 but pulse(q+period)=0.
    This construction disproves every proposed finite deterministic
    stationary state's eventual periodicity claim for this pulse source.
    """
    if type(preperiod) is not int or preperiod<0 or type(period) is not int or period<1:
        raise VoyagerError("Eventual period requires N>=0 and p>=1")
    q=1
    while q <= max(preperiod,period):
        q *= 2
    if not(q>=preperiod and q<q+period<2*q
           and powers_of_two_pulse(q)==1
           and powers_of_two_pulse(q+period)==0):
        raise AssertionError("Universal gap witness does not refute proposed period")
    return {"preperiod":preperiod,"period":period,
            "witness_time":q,"shifted_time":q+period,
            "source_outputs":(1,0),"periodicity_refuted":True}


def incompatible_pulse_with_finite_machine(machine:TraceSource)->dict:
    """Construct a finite contradiction to a fixed machine representing pulses."""
    N,p=machine.eventual_period()
    w=power_two_period_refutation(N,p)
    pulse_a=powers_of_two_pulse(w["witness_time"])
    pulse_b=powers_of_two_pulse(w["shifted_time"])
    a=machine.report(machine.trace_state(w["witness_time"]))
    b=machine.report(machine.trace_state(w["shifted_time"]))
    if a!=b:
        raise AssertionError("Fixed finite source's periodic state law is false")
    bad=w["witness_time"] if a!=pulse_a else w["shifted_time"]
    if machine.report(machine.trace_state(bad))==powers_of_two_pulse(bad):
        raise AssertionError("Expected a concrete source-vs-ideal mismatch")
    return {"machine_state_count":len(machine.states),
            "cycle_start":N,"cycle_period":p,
            "first_constructive_gap":w["witness_time"],
            "finite_mismatch_index":bad,
            "mismatch_is_original_source_witness":True}


def finite_trace_projective_tower(source:TraceSource, horizon:int) -> dict:
    """Projection of finite source-image prefix sets is surjective.

    The finite complete source has exactly len(states) possible initial
    states; not the infinite family of independently rebuildable machines.
    """
    if type(horizon) is not int or not 0 <= horizon <= 32:
        raise VoyagerError("Require finite tested horizon <= 32")
    stages=[tuple(sorted({source.trace(h,start=s) for s in source.states}))
            for h in range(horizon+1)]
    for h in range(horizon):
        projected={word[:-1] for word in stages[h+1]}
        if projected!=set(stages[h]):
            raise AssertionError("Finite-stage source projection is not onto")
    return {"source_id":source.source_id,
            "epochs_are_one_declared_stationary_law":True,
            "stage_sizes":tuple(len(stage) for stage in stages),
            "projection_surjective":True,
            "full_finite_source_state_cap":len(source.states),
            "ideal_limit_source_realization_claimed":False}


def power_two_gap_memory_lower_bound(machine: TraceSource, pulse_power: int)->dict:
    """Finite-horizon source-memory DEBT: at least 2^k distinct states.

    At times p+1,...,2p-1, where p=2^k, an exactly matched power-two
    pulse is zero, followed by one at 2p. If any two ZERO-interval source
    states repeat, determinism forces the later 1 to have appeared
    earlier inside that zero gap. They must all be distinct; the final
    ONE state is distinct by its output. Thus N>=p.

    This is a theorem conditional on the observed finite source trace
    through time 2p. It does NOT assume any infinite trace existed.
    """
    if (type(pulse_power) is not int or not 1 <= pulse_power <= 9):
        raise VoyagerError("Require finite pulse gap power 1..9")
    p=2**pulse_power
    h=2*p+1
    truth=tuple(powers_of_two_pulse(i) for i in range(h))
    if machine.trace(h)!=truth:
        raise VoyagerError("Lower bound requires exact pulse prefix source match")
    indexed=tuple((t,machine.trace_state(t)) for t in range(p+1,2*p+1))
    if len({state for _,state in indexed})!=p:
        # The independent finite-state oracle detects a contradiction
        # with the exact deterministic output trace.
        raise AssertionError("Repeated state in a zero gap preceding a pulse")
    if len(machine.states)<p:
        raise AssertionError("Finite observed prefix exceeds state-count bound")
    return {
        "source_id":machine.source_id,
        "pulse_gap":p,
        "certified_minimum_states":p,
        "actual_machine_states":len(machine.states),
        "source_horizon":h,
        "all_gap_states_pairwise_distinct":True,
        "original_source_contains_every_later_pulse_claimed":False,
    }


def ideal_eventual_zero_stage(h:int)->tuple[tuple[int,...],...]:
    """All binary prefixes of length h appear in SOME eventually-zero state."""
    if type(h) is not int or not 0 <= h <= 13:
        raise VoyagerError("Bounded independent prefix oracle is 0..13")
    words=tuple(product((0,1),repeat=h))
    if any(eventual_zero_lift(w).trace(h)!=w for w in words):
        raise AssertionError("Constructive finite-source witness missing")
    return words


def truncated_ultrametric(a:tuple[int,...],b:tuple[int,...])->F:
    """Baire/Cantor first-difference dyadic ultrametric on finite words.

    Equality at the truncation horizon means *unknown suffix*, not an
    eternal identity certificate. Thus zero here is pseudodistance on the
    underlying infinite profiles but a metric on distinct finite words.
    """
    _binary(a);_binary(b)
    if len(a)!=len(b):
        raise VoyagerError("Cannot compare different observation resolutions")
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y:
            return F(1,2**i)
    return F(0)


def finite_model_critical_probe_witnesses(
        source: TraceSource, target:Callable[[int],int], *,
        verify_oracle_depth:int=64) -> dict:
    """If target=powers-of-two pulse, construct a bounded finite witness
    for EACH possible initial state of this given finite source.
    """
    if target is not powers_of_two_pulse:
        raise VoyagerError("Constructive global oracle specialized to power-two pulse")
    if type(verify_oracle_depth) is not int or not 1<=verify_oracle_depth<=300:
        raise VoyagerError("Budgeted negative-control depth required")
    witnesses=[]
    for s in source.states:
        # Each state defines a separate fixed finite machine successor trace.
        N,p=source.eventual_period(start=s)
        bad=power_two_period_refutation(N,p)
        t=bad["witness_time"]
        mismatch=t if source.report(source.trace_state(t,start=s))!=target(t) else t+p
        if source.report(source.trace_state(mismatch,start=s))==target(mismatch):
            raise AssertionError("Finite source class evaded universal gap")
        witnesses.append((s,mismatch))
    all_depth=max(t for _,t in witnesses)+1
    exact_check=all(
        source.trace(all_depth,start=s)[t] != target(t)
        for s,t in witnesses)
    if not exact_check:
        raise AssertionError("Independent finite output trace oracle disagreed")
    return {"source_states":len(source.states),
            "refuting_probe_count":len(witnesses),
            "one_refuting_probe_per_source_state":True,
            "probe_times":tuple(witnesses),
            "largest_probe_time":max(t for _,t in witnesses),
            "exact_source_trace_oracle":exact_check,
            "no_original_pulse_source_present":True}


def voyager_demo() -> dict:
    h=12
    sampled=tuple(powers_of_two_pulse(i) for i in range(h))
    witness=eventual_zero_lift(sampled,source_id="voyager-power-two-horizon")
    if witness.trace(h)!=sampled or witness.eventual_period()!=(h,1):
        raise AssertionError("Finite behavioral reconstruction failed")
    finites=finite_trace_projective_tower(witness,12)
    alltrue=eventual_zero_lift(tuple([1]*h),source_id="voyager-all-one")
    if alltrue.trace(h)!=tuple([1]*h):
        raise AssertionError("Finite prefix source positive control failed")
    issue=finite_model_critical_probe_witnesses(witness,powers_of_two_pulse)
    critical=power_two_period_refutation(12,3)
    gap_machine=eventual_zero_lift(
        tuple(powers_of_two_pulse(i) for i in range(17)),
        source_id="voyager-gap-p8")
    gap_debt=power_two_gap_memory_lower_bound(gap_machine,3)
    return {
        "power_two_finite_horizon_debt":{
            "pulse_gap":gap_debt["pulse_gap"],
            "state_lower_bound":gap_debt["certified_minimum_states"],
            "source_horizon":gap_debt["source_horizon"],
            "gap_states_distinct":gap_debt["all_gap_states_pairwise_distinct"]},
        "status":"EXACT_VOYAGER_OBSERVATIONAL_COMPLETION_BOUNDARY",
        "finite_prefix_power_two":list(sampled),
        "exact_original_finite_machine_witness_states":len(witness.states),
        "actual_sampled_source_matches_prefix":True,
        "finite_original_source_tower":{
            "stage_sizes":list(finites["stage_sizes"]),
            "surjective_stage_restrictions":finites["projection_surjective"]},
        "eventual_zero_family":{
            "all_one_prefix_12_has_original_witness":True,
            "all_one_global_profile_realized_by_eventually_zero_source":False,
            "every_finite_binary_prefix_has_a_constructed_source":True,
            "infinite_projective_source_realization_claimed":False},
        "finite_state_nonperiodic_gap":{
            "pulse_q":critical["witness_time"],
            "pulse_q_plus_p":critical["shifted_time"],
            "pulse_values":list(critical["source_outputs"]),
            "arbitrary_fixed_machine_finite_refutation":issue["exact_source_trace_oracle"],
            "bounded_enumeration_of_every_possible_machine_claimed":False},
        "scope":{
            "exact_source_relative_mathematics":True,
            "new_scholarly_priority_claimed":False,
            "physical_all_future_executed":False,
            "every_profinite_thread_is_original_state":False,
            "arithmetic_RH_or_Weil_positivity_proved":False,
            "unbounded_unknown_source_empirically_authenticated":False},
    }
