"""Proof-support transport under state-changing observations and proportional debt.

An observer has a hidden source bit tape and an ACTIVE proof-support prefix.
Reading the next unobserved bit is an actual carrier action: it records a
source-indexed outcome and can activate additional *previously latent* support.
No bits are created; the target ("all currently active bits are zero") changes
when the active support changes. The source class is all binary tapes, unless
an independently proved restriction is separately supplied.

A second, deliberately separate, clock tracks a theorem's p-adic digit
separation depth, a knowledge-indexed increase in nonunit valuation, and an
independently budgeted precision supply. Neither clock models human cognition,
physical supertasks, proof of RH, or actual source authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .probe_coherence import (
    InitialSource, independent_carrier_repair, local_carrier_no_go,
    nondestructive_probe_repair,
)
from .precision_transport import (
    ClaimContext, PrecisionFrame, certify_transport,
)
from .residue_one_arch import prime


class BackactionError(ValueError):
    """Malformed source, exhausted finite test tape, or incorrect support."""


def _nonnegative(x: int, label: str) -> int:
    if type(x) is not int or x < 0:
        raise BackactionError(f"{label} must be an exact nonnegative integer")
    return x


@dataclass(frozen=True)
class SupportEvent:
    """A causal observation record, and the source contract before/after."""
    index: int
    bit: int
    before_active: int
    after_active: int
    after_knowledge: int
    source_id: str
    carrier_epoch: int

    @property
    def births(self) -> int:
        return self.after_active - self.before_active


@dataclass(frozen=True)
class SupportCarrier:
    """Finite-prefix implementation of the infinite-tape mathematical model.

    Actual bits are supplied for simulation and NOT given to the embedded
    observer. All unobserved tape assignments are considered compatible with
    its history; no program may use the simulator's bit tuple as a theorem.
    Support is prefix [0,active), observed bits are prefix [0,observed).
    """
    tape: tuple[int, ...]
    active: int = 1
    observed: tuple[int, ...] = ()
    background_knowledge: int = 0
    birth_mode: str = "proportional"  # proportional | matched | frozen
    alpha: int = 1
    source_id: str = "declared-latent-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        if (type(self.tape) is not tuple or not self.tape or
                any(type(x) is not int or x not in (0, 1) for x in self.tape)):
            raise BackactionError("Finite hidden tape must be a nonempty tuple of bits")
        if (type(self.active) is not int or
                not len(self.observed) <= self.active <= len(self.tape) or
                self.active < 1):
            raise BackactionError("Active support must contain observations")
        if type(self.observed) is not tuple or any(
            type(x) is not int or x not in (0, 1) for x in self.observed
        ):
            raise BackactionError("History must be a tuple of observed bits")
        if self.observed != self.tape[:len(self.observed)]:
            raise BackactionError("History contradicts the simulator's actual source")
        _nonnegative(self.background_knowledge, "background knowledge")
        _nonnegative(self.alpha, "proportional birth coefficient")
        _nonnegative(self.epoch, "carrier version")
        if self.epoch != len(self.observed):
            raise BackactionError("One observation per carrier version required")
        if self.birth_mode not in ("proportional", "matched", "frozen"):
            raise BackactionError("Unknown source-support growth law")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise BackactionError("Source context must be explicitly labeled")

    @property
    def K(self) -> int:
        """Count of fresh observed bits + declared background knowledge."""
        return self.background_knowledge + len(self.observed)

    @property
    def debt(self) -> int:
        """Number of active, unresolved independent Boolean obligations."""
        return self.active - len(self.observed)

    @property
    def target_contract(self) -> tuple[str, int, str]:
        """Target means: all source bits with index < active are zero."""
        return (self.source_id, self.active, "all-active-bits-zero")

    @property
    def verdict(self) -> str:
        if 1 in self.observed:
            return "refuted"
        if self.debt == 0:
            return "certified-true"
        return "unresolved"

    @property
    def compatible_target_values(self) -> tuple[bool, ...]:
        """All possible answers under unconstrained unknown active bits."""
        if 1 in self.observed:
            return (False,)
        return (True,) if self.debt == 0 else (False, True)

    @property
    def compatible_active_assignments(self) -> int:
        return 1 << self.debt

    def possible_false_witness(self) -> int | None:
        """An unobserved bit position making current target false.

        Only called if no already witnessed 1 and some support is unresolved.
        The all-zero rival and a rival with this bit flipped have identical
        observed transcripts and opposite current target values.
        """
        if self.verdict != "unresolved":
            return None
        return len(self.observed)

    def probe(self) -> tuple["SupportCarrier", SupportEvent]:
        """Atomic probe: read one active bit, then update active support.

        The ACTIVE PROOF CONTRACT changes when births>0. No data is
        retrospectively mutated; this differs from the separately tested
        destructive two-bit carrier whose source bits are overwritten.
        """
        if self.debt <= 0:
            raise BackactionError("No active independent obligation to probe")
        index = len(self.observed)
        value = self.tape[index]
        K_next = self.K + 1
        births = (self.alpha * K_next if self.birth_mode == "proportional"
                  else 1 if self.birth_mode == "matched" else 0)
        new_active = self.active + births
        if new_active > len(self.tape):
            raise BackactionError("Finite simulator exhausted; no claim about infinity")
        updated = SupportCarrier(
            tape=self.tape, active=new_active, observed=self.observed+(value,),
            background_knowledge=self.background_knowledge,
            birth_mode=self.birth_mode, alpha=self.alpha,
            source_id=self.source_id, epoch=self.epoch + 1,
        )
        event = SupportEvent(
            index=index, bit=value, before_active=self.active,
            after_active=new_active, after_knowledge=updated.K,
            source_id=self.source_id, carrier_epoch=updated.epoch,
        )
        if updated.debt != self.debt - 1 + births:
            raise ArithmeticError("Support-frontier conservation law violated")
        return updated, event


def support_frontier_formula(initial_active: int, initial_K: int, alpha: int,
                             n: int, birth_mode: str = "proportional") -> dict:
    """Exact state counts after n successfully executed atomic steps.

    The closed form remains a theorem for the ideal infinite tape. Under
    a frozen finite support it is valid only until the probe menu exhausts.
    """
    for label, val in (("initial active", initial_active),
                       ("initial K", initial_K), ("alpha", alpha),
                       ("steps", n)):
        _nonnegative(val, label)
    if initial_active < 1:
        raise BackactionError("Need an initially outstanding obligation")
    if birth_mode not in ("proportional", "matched", "frozen"):
        raise BackactionError("Unrecognized support growth mode")
    births = (alpha * (n * initial_K + n * (n+1) // 2)
              if birth_mode == "proportional" else
              n if birth_mode == "matched" else 0)
    activated = initial_active + births
    pending = activated - n
    if pending < 0:
        raise BackactionError("Attempt to probe after support was exhausted")
    if birth_mode == "proportional" and alpha >= 1:
        if pending < initial_active:
            raise ArithmeticError("Proportional support theorem contradicted")
    return {
        "knowledge": initial_K + n,
        "active": activated,
        "observed": n,
        "debt": pending,
        "new_obligations": births,
        "completed": pending == 0,
        "birth_mode": birth_mode,
    }


def support_transport_law(before_active: int, after_active: int) -> dict:
    """Exact one-way proof preservation for an expanding support contract.

    T_A(z)=all z_i=0 for i<A. If B>=A, T_B implies T_A, and
    NOT T_A implies NOT T_B. If B>A, T_A does NOT imply T_B:
    take a zero prefix through A and set z_A=1.
    """
    _nonnegative(before_active, "old support")
    _nonnegative(after_active, "new support")
    if not 1 <= before_active <= after_active:
        raise BackactionError("Require nonempty, nested proof-support domains")
    return {
        "forward_true_valid_for_all_sources": before_active == after_active,
        "reverse_true_valid_for_all_sources": True,
        "forward_refutation_valid_for_all_sources": True,
        "new_support_counterexample_bit": (
            before_active if after_active > before_active else None
        ),
        "new_activated_support": after_active - before_active,
        "source_payload_mutated": False,
        "proof_target_changed": after_active > before_active,
    }


@dataclass(frozen=True)
class SupportDescentCertificate:
    """Finite SOURCE-RELATIVE positive-proof gluing verdict.

    The class of allowed latent sources is DECLARED and must be separately
    justified. A correct algorithm for checking a supplied class does not
    certify that it contains the true carrier/source.
    """
    source_id: str
    from_active: int
    to_active: int
    eligible_old_true: int
    counterexample: tuple[int, ...] | None

    @property
    def valid_forward_positive(self) -> bool:
        return self.counterexample is None

    @property
    def vacuous(self) -> bool:
        return self.eligible_old_true == 0

    @property
    def useful_positive_transport(self) -> bool:
        return self.valid_forward_positive and not self.vacuous


def certify_support_descent(source_class: tuple[tuple[int,...],...],
                            from_active: int, to_active: int, *,
                            source_id: str) -> SupportDescentCertificate:
    """Exact relative gluing iff X∩T_from is a subset of T_to.

    The answer is a finite check for a supplied X of equally sized bit
    tapes. This must not be upgraded to a physically source-certified law.
    When X∩T_from is empty the implication is merely vacuous.
    """
    if (type(source_class) is not tuple or not source_class or
            len(source_class)>4096 or type(source_id) is not str or
            not source_id):
        raise BackactionError("Require a nonempty finite declared source class")
    law=support_transport_law(from_active,to_active)
    length=None
    eligible=0
    witness=None
    for bits in source_class:
        if (type(bits) is not tuple or len(bits)<to_active or
                any(type(b) is not int or b not in (0,1) for b in bits)):
            raise BackactionError("Every candidate must have enough exact source bits")
        if length is None:
            length=len(bits)
        if len(bits)!=length:
            raise BackactionError("All source candidates must share one typed carrier")
        if all(b==0 for b in bits[:from_active]):
            eligible+=1
            if any(b!=0 for b in bits[:to_active]) and witness is None:
                witness=bits
    if (law["forward_true_valid_for_all_sources"] and witness is not None):
        raise ArithmeticError("Equal support could not change target truth")
    return SupportDescentCertificate(
        source_id=source_id, from_active=from_active,to_active=to_active,
        eligible_old_true=eligible,counterexample=witness)


@dataclass(frozen=True)
class PrecisionDebtChase:
    """A separate, conditional resource/clock transport experiment.

    One actual, independent source-attested insight per step is ASSUMED.
    At step i>=1, K_i=K_0+i and valuation v increases by alpha*K_i.
    Available output digits q increase by either a fixed c, exactly
    alpha*K_i (matching), or alpha*K_i+surplus (overtaking).

    The claim's fixed separation depth k is *not* automatically authenticated.
    Claim factorization is possible iff q>=v+k. The observation map, when
    instantiated, is truncated at s=min(q,r+v) to avoid reading
    undeclared representative digits.
    """
    p: int
    r: int
    k: int
    K0: int
    alpha: int
    v0: int
    q0: int
    schedule: str   # fixed | matched | surplus
    fixed_capacity: int = 0
    surplus: int = 0

    def __post_init__(self) -> None:
        if not prime(self.p):
            raise BackactionError("Only actual prime-local clocks admitted")
        for name in ("r", "k", "K0", "alpha", "v0",
                     "q0", "fixed_capacity", "surplus"):
            _nonnegative(getattr(self, name), name)
        if not 1 <= self.k <= self.r or self.q0 < 1:
            raise BackactionError("Need nonconstant claim and valid precision")
        if self.schedule not in ("fixed", "matched", "surplus"):
            raise BackactionError("Unrecognized capacity schedule")
        if self.schedule == "surplus" and self.surplus < 1:
            raise BackactionError("Overtaking schedule needs positive extra supply")

    def at(self, n: int) -> dict:
        _nonnegative(n, "stage")
        accumulated_K = n * self.K0 + n*(n+1)//2
        valuation = self.v0 + self.alpha * accumulated_K
        if self.schedule == "fixed":
            supplied = n*self.fixed_capacity
        elif self.schedule == "matched":
            supplied = self.alpha*accumulated_K
        else:
            supplied = self.alpha*accumulated_K + n*self.surplus
        q = self.q0 + supplied
        deficit = valuation + self.k - q
        return {
            "stage": n, "K": self.K0+n, "valuation_debt": valuation,
            "available_digits": q,
            "independent_digit_supply": supplied,
            "claim_digits_needed": valuation+self.k,
            "shortfall": deficit,
            "claim_channel_decodable": deficit <= 0,
            "lawful_output_resolution": min(q, self.r+valuation),
            "source_claim_truth_independently_verified": False,
        }

    def exact_first_decodable_stage(self) -> int | None:
        """Closed-form/binary-search complete decision over all finite n.

        For fixed capacity and alpha>0, shortfall is discretely convex.
        Its global minimum occurs after all strictly negative increments.
        Thus a finite search only through that algebraic turning point
        decides whether *any* finite checkpoint makes decoding possible.
        No artificial probe-count horizon is imposed.
        """
        initial = self.at(0)["shortfall"]
        if initial <= 0:
            return 0
        if self.schedule == "matched":
            return None
        if self.schedule == "surplus":
            return (initial+self.surplus-1)//self.surplus
        if self.alpha == 0:
            if self.fixed_capacity == 0:
                return None
            return (initial+self.fixed_capacity-1)//self.fixed_capacity
        # Delta(shortfall)_i = alpha*(K0+i) - fixed_capacity.
        # Strictly negative increments occur at i in [1..turning].
        turning = max(0, (self.fixed_capacity-1)//self.alpha-self.K0)
        if self.at(turning)["shortfall"] > 0:
            return None
        lower, upper = 0, turning
        while lower < upper:
            mid = (lower+upper)//2
            if self.at(mid)["shortfall"] <= 0:
                upper = mid
            else:
                lower = mid+1
        return lower

    def best_history_stage(self, n: int) -> int:
        """Index of best precision observation through stage n inclusive.

        With an immutable FIXED source and honest retained history, all
        observations can be combined. Each one's fibers are congruence
        classes modulo p^e_i; their intersection is the strongest such
        congruence, with e=max_i e_i. A deteriorating current instrument
        cannot retract an earlier certified source observation.
        """
        _nonnegative(n, "stage")
        if self.schedule == "matched":
            return 0  # all stages have the same input digit depth
        if self.schedule == "surplus":
            return n
        if self.alpha == 0:
            return n if self.fixed_capacity > 0 else 0
        turning = max(0, (self.fixed_capacity-1)//self.alpha-self.K0)
        return min(n, turning)

    def history_at(self, n: int) -> dict:
        """Sound JOINT-transcript factorization for a fixed unchanged source.

        For transformed/source-changing observations this law is UNDEFINED
        unless independently supplied intervention maps transport every
        report to one valid original-source basis. It does not follow from
        a collection of stage-wise decoders with inconsistent source IDs.
        """
        best = self.best_history_stage(n)
        minimum_shortfall = self.at(best)["shortfall"]
        effective_depth = min(self.r, max(0, self.k-minimum_shortfall))
        current = self.at(n)
        return {
            "stage": n,
            "best_retained_stage": best,
            "joint_source_digit_depth": effective_depth,
            "minimum_history_shortfall": minimum_shortfall,
            "joint_claim_decodable": minimum_shortfall <= 0,
            "current_claim_decodable": current["claim_channel_decodable"],
            "source_payload_changes_assumed": False,
            "history_physically_authenticated": False,
        }

    def finite_frame(self, n: int) -> PrecisionFrame:
        """Instantiate prior transport theorem only at safely finite levels."""
        data = self.at(n)
        v = data["valuation_debt"]
        if v > 12 or data["lawful_output_resolution"] > 32 or self.r > 12:
            raise BackactionError("Very large symbolic clocks are not materialized")
        return PrecisionFrame(self.p, self.r, self.p**v,
                              data["lawful_output_resolution"])


def zeno_clock(n: int) -> Fraction:
    """Hypothetical accumulating timestamps t_n=1−2^(−n), not a physical clock."""
    _nonnegative(n, "finite event count")
    if n > 2048:
        raise BackactionError("Unbounded time-limit not numerically executed")
    return Fraction(1) - Fraction(1, 2**n)


def proof_backaction_debt_demo() -> dict:
    """All claims are exact finite witnesses plus mathematically scoped laws."""
    carrier = SupportCarrier((0,)*300, active=1, alpha=1)
    counts = []
    witness = None
    for n in range(9):
        row = support_frontier_formula(1, 0, 1, n)
        if (carrier.K, carrier.active, carrier.debt) != (
                row["knowledge"], row["active"], row["debt"]):
            raise ArithmeticError("Independent support conservation failed")
        if carrier.verdict != "unresolved" or carrier.possible_false_witness() is None:
            raise ArithmeticError("Premature all-zero positive certificate")
        counts.append(row["debt"])
        if n == 2:
            witness = support_transport_law(carrier.active, carrier.active+1)
        carrier, _ = carrier.probe()

    matched = SupportCarrier((0,)*20, active=1, birth_mode="matched")
    for _ in range(8):
        if matched.debt != 1 or matched.verdict != "unresolved":
            raise ArithmeticError("Matched debt closed unexpectedly")
        matched, _ = matched.probe()

    frozen = SupportCarrier((0,0,0,0), active=3, birth_mode="frozen")
    for _ in range(3):
        frozen, _ = frozen.probe()
    if frozen.verdict != "certified-true":
        raise ArithmeticError("Frozen finite original target failed to close")

    falsified = SupportCarrier((1,0,0,0), active=1, birth_mode="matched")
    falsified, _ = falsified.probe()
    if falsified.verdict != "refuted":
        raise ArithmeticError("Single source bit 1 must finitely refute target")

    matched_chase = PrecisionDebtChase(5,2,2,0,1,0,1,"matched")
    super_chase = PrecisionDebtChase(5,2,2,0,1,0,1,"surplus",surplus=1)
    fixed_chase = PrecisionDebtChase(5,2,2,0,1,0,1,"fixed",fixed_capacity=1)
    transient = PrecisionDebtChase(5,2,2,0,1,0,1,"fixed",fixed_capacity=3)
    if not (matched_chase.exact_first_decodable_stage() is None and
            super_chase.exact_first_decodable_stage() == 1 and
            fixed_chase.exact_first_decodable_stage() is None and
            transient.exact_first_decodable_stage() == 1):
        raise ArithmeticError("Capacity/outpacing/no-go classifications failed")

    # Independent claim factorization checks against PR #19's oracle.
    source = ClaimContext.from_mapping(
        5,2,{x:str(x//5) for x in range(25)},
        source_id="finite-proof-source", basis_id="clock-v1",
        claim_id="high-digit")
    if source.separation_depth()!=2:
        raise ArithmeticError("Precision claim does not need two digits")
    oracle = []
    for n in range(5):
        frame = matched_chase.finite_frame(n)
        oracle_result = certify_transport(source,frame)
        symbolic = matched_chase.at(n)["claim_channel_decodable"]
        if oracle_result.valid != symbolic:
            raise ArithmeticError("Symbolic debt differs from source-fiber theorem")
        oracle.append(symbolic)

    if (not transient.history_at(8)["joint_claim_decodable"]
            or transient.history_at(8)["current_claim_decodable"]
            or matched_chase.history_at(8)["joint_claim_decodable"]):
        raise ArithmeticError("Independent retained-history theorem contradicted")

    unrestricted=tuple((a,b) for a in (0,1) for b in (0,1))
    restricted=tuple(bits for bits in unrestricted if bits[1]==0)
    vacuous=tuple(bits for bits in unrestricted if bits[0]==1)
    unrestricted_glue=certify_support_descent(
        unrestricted,1,2,source_id="all-two-bit-sources")
    restricted_glue=certify_support_descent(
        restricted,1,2,source_id="verified-second-bit-zero-hypothesis")
    vacuous_glue=certify_support_descent(
        vacuous,1,2,source_id="no-old-positive-sources")
    if (unrestricted_glue.valid_forward_positive or
            not restricted_glue.useful_positive_transport or
            vacuous_glue.useful_positive_transport):
        raise ArithmeticError("Source-relative support descent model failed")

    no_go = local_carrier_no_go()
    if not no_go["proof_support_unreachable_with_one_carrier"]:
        raise ArithmeticError("Original-source destructive probe witness lost")
    parity_repaired = independent_carrier_repair(InitialSource(0,1))
    if parity_repaired != 1 or nondestructive_probe_repair(InitialSource(0,1)) != 1:
        raise ArithmeticError("Destructive carrier positive controls failed")

    return {
        "status": "SOURCE_BACKACTION_PROOF_DEBT_AND_ZENO_EXACT",
        "proportional_debt_first_nine_stages": counts,
        "debt_growth_equation": "D_n=D0-n+alpha*(n*K0+n*(n+1)/2)",
        "probe_births_proportional_to_new_knowledge": True,
        "matching_births_no_finite_zero_certificate": True,
        "all_zero_proportional_source_never_finitely_certified_under_protocol": True,
        "all_zero_frozen_support_certified_after_three_reads": True,
        "single_one_refuted_after_one_read": True,
        "proof_target_mutated_by_support_growth": witness["proof_target_changed"],
        "old_true_forward_transport_universal": witness["forward_true_valid_for_all_sources"],
        "old_refutation_forward_transport_universal": witness["forward_refutation_valid_for_all_sources"],
        "rate_matched_precision_shortfall_stage_0": matched_chase.at(0)["shortfall"],
        "rate_matched_precision_shortfall_stage_4": matched_chase.at(4)["shortfall"],
        "rate_matched_precision_first_decodable_stage": matched_chase.exact_first_decodable_stage(),
        "overtaking_precision_first_decodable_stage": super_chase.exact_first_decodable_stage(),
        "fixed_capacity_eventually_outrun": fixed_chase.at(8)["shortfall"] > fixed_chase.at(2)["shortfall"],
        "early_transient_can_decide_despite_later_debt": transient.exact_first_decodable_stage()==1 and not transient.at(8)["claim_channel_decodable"],
        "transient_earlier_proof_remains_in_joint_history": transient.history_at(8)["joint_claim_decodable"],
        "transient_current_channel_loses_decodability": transient.history_at(8)["current_claim_decodable"],
        "matched_joint_history_cannot_resolve_original_gap": matched_chase.history_at(8)["joint_claim_decodable"],
        "matched_joint_history_digit_depth": matched_chase.history_at(8)["joint_source_digit_depth"],
        "independent_precision_transport_oracle_matched": oracle,
        "zeno_t_four": str(zeno_clock(4)),
        "zeno_t_eight": str(zeno_clock(8)),
        "omega_probe_event_executed": False,
        "unrestricted_positive_support_gluing": unrestricted_glue.valid_forward_positive,
        "source_restricted_positive_support_gluing": restricted_glue.useful_positive_transport,
        "vacuous_source_law_is_not_useful_positive_proof": vacuous_glue.useful_positive_transport,
        "destructive_single_carrier_original_parity_impossible": True,
        "independent_carrier_restores_original_parity": True,
        "physical_information_time_or_RH_theorem_claimed": False,
    }
