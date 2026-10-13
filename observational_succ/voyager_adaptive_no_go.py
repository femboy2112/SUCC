"""VOYAGER: source-relative adaptive finite-probe undecidability.

A nonanticipatory policy asks coordinate n based ONLY on earlier outcomes,
stopping after a declared finite bound. For any actual finite transcript,
construct two original mathematical source streams with exactly the same
observed answers: one eventually zero, the other eventually one.

They induce the identical policy branch and final decision, so no binary
terminal judgment can be correct on BOTH source classes. This is the
finite-policy corollary of the Lean arbitrary-finite-probe patch theorem.
The runtime never pretends to have performed an infinity of observations.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable

class VoyagerPolicyError(ValueError):
    pass


@dataclass(frozen=True)
class FinitePatchStream:
    source_id: str
    epoch: int
    basis: str
    observed: tuple[tuple[int,int],...]
    tail: int
    authenticated: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis or
                type(self.epoch) is not int or self.epoch<0 or
                type(self.observed) is not tuple or
                len({n for n,_ in self.observed})!=len(self.observed) or
                type(self.tail) is not int or self.tail not in (0,1) or
                any(type(n) is not int or n<0 or
                    type(v) is not int or v not in (0,1)
                    for n,v in self.observed) or self.authenticated):
            raise VoyagerPolicyError("Mathematical patched stream must be typed and finite")

    def report(self, index:int)->int:
        if type(index) is not int or index<0:
            raise VoyagerPolicyError("Lawful bit coordinate required")
        return dict(self.observed).get(index,self.tail)

    @property
    def eventually_zero(self)->bool:
        return self.tail==0

    def witness_zero_tail_after(self)->int:
        """Exact finite bound beyond every locally patched coordinate."""
        return max((n for n,_ in self.observed),default=-1)+1


@dataclass(frozen=True)
class AdaptiveFinitePolicy:
    source_id: str
    epoch: int
    basis: str
    horizon: int
    next_query_table: tuple[tuple[tuple[int,...],int],...]
    physical_reset_available: bool = False
    empirically_authenticated: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis or
                type(self.epoch) is not int or self.epoch<0 or
                type(self.horizon) is not int or
                not 1<=self.horizon<=8 or
                type(self.next_query_table) is not tuple or
                self.empirically_authenticated or self.physical_reset_available):
            raise VoyagerPolicyError("Use a declared finite mathematical policy tree")
        nodes={bits:idx for bits,idx in self.next_query_table}
        expected={bits for n in range(self.horizon)
                  for bits in product((0,1),repeat=n)}
        if (set(nodes)!=expected or len(nodes)!=len(self.next_query_table)
                or any(type(idx) is not int or idx<0 for idx in nodes.values())
                or any(type(bits) is not tuple or
                       any(type(v) is not int or v not in (0,1) for v in bits)
                       for bits in nodes)):
            raise VoyagerPolicyError("A complete binary nonanticipatory table is required")

    def choose(self, answers:tuple[int,...])->int:
        if type(answers) is not tuple or any(v not in (0,1) for v in answers):
            raise VoyagerPolicyError("Previous answers must be literal binary values")
        if len(answers)>=self.horizon:
            raise VoyagerPolicyError("Cannot query after terminal horizon")
        return dict(self.next_query_table)[answers]


def replay_policy(policy:AdaptiveFinitePolicy,
                  source:Callable[[int],int]) -> tuple[tuple[int,int],...]:
    records=[]
    for k in range(policy.horizon):
        answers=tuple(value for _,value in records)
        coord=policy.choose(answers)
        value=source(coord)
        if type(value) is not int or value not in (0,1):
            raise VoyagerPolicyError("Only original binary source reports may enter history")
        records.append((coord,value))
    return tuple(records)


@dataclass(frozen=True)
class AdaptiveNoGoReceipt:
    source_id: str
    horizon: int
    original_transcript: tuple[tuple[int,int],...]
    eventually_zero_witness: FinitePatchStream
    non_eventually_zero_witness: FinitePatchStream
    source_transcripts_identical: bool
    at_least_one_terminal_label_wrong: bool
    physical_policy_executed: bool = False


def adaptive_finite_probe_no_go(
        policy:AdaptiveFinitePolicy,
        target:Callable[[int],int],
        terminal_declares_eventually_zero:bool) -> AdaptiveNoGoReceipt:
    if type(terminal_declares_eventually_zero) is not bool:
        raise VoyagerPolicyError("A terminal logical claim must be Boolean")
    transcript=replay_policy(policy,target)
    rows={}
    for n,v in transcript:
        if n in rows and rows[n]!=v:
            raise AssertionError("A deterministic source cannot change the same coordinate")
        rows[n]=v
    reports=tuple(sorted(rows.items()))
    z=FinitePatchStream(policy.source_id,policy.epoch,policy.basis,reports,0)
    nz=FinitePatchStream(policy.source_id,policy.epoch,policy.basis,reports,1)
    replay_z=replay_policy(policy,z.report)
    replay_nz=replay_policy(policy,nz.report)
    if replay_z!=transcript or replay_nz!=transcript:
        raise AssertionError("Constructed source patch failed the EXACT adaptive transcript")
    if z.eventually_zero == nz.eventually_zero:
        raise AssertionError("Positive and negative source witnesses conflated")
    incorrect_on_one=(terminal_declares_eventually_zero!=z.eventually_zero or
                      terminal_declares_eventually_zero!=nz.eventually_zero)
    return AdaptiveNoGoReceipt(
        policy.source_id,policy.horizon,transcript,z,nz,True,incorrect_on_one,False)


def generated_policy(horizon:int=5)->AdaptiveFinitePolicy:
    if type(horizon) is not int or not 1<=horizon<=8:
        raise VoyagerPolicyError("Bounded policy constructor requires 1..8 steps")
    def query(bits):
        # The next coordinate depends on the entire ACTUALLY observed
        # bit history, not on any counterfactual future. Repeatable legal
        # queries are permitted, and repeated responses are forced equal.
        return 2*len(bits)+sum((i+1)*(b+1) for i,b in enumerate(bits))%7
    return AdaptiveFinitePolicy(
        "declared-adaptive-voyager",0,"binary-head",
        horizon,tuple((bits,query(bits)) for n in range(horizon)
                      for bits in product((0,1),repeat=n)))


def adaptive_no_go_demo()->dict:
    target=lambda n: int(n>0 and n&(n-1)==0)
    policy=generated_policy(5)
    result=adaptive_finite_probe_no_go(policy,target,True)
    if not result.at_least_one_terminal_label_wrong:
        raise AssertionError("A single finite transcript cannot decide both source classes")
    return {
        "source_id":result.source_id,
        "finite_adaptive_queries":result.horizon,
        "actual_reported_coordinates":[[n,b] for n,b in result.original_transcript],
        "both_witnesses_replay_same_exact_transcript":
            result.source_transcripts_identical,
        "one_stream_eventually_zero":result.eventually_zero_witness.eventually_zero,
        "other_stream_eventually_zero":result.non_eventually_zero_witness.eventually_zero,
        "terminal_decision_for_both_source_classes_not_possible":
            result.at_least_one_terminal_label_wrong,
        "physical_adaptive_measurement_executed":False,
        "source_authentication_claimed":False,
    }
