"""Exact, source-relative precision transport for nonzero proto-SUCC steps.

Every theorem is finite or elementary classical algebra. A source label is
declared, not authenticated. Proof tables are exact finite premises, not
proofs about a physical carrier or an analytic arithmetic source.

See research/2026-10-11/SOURCE_RELATIVE_PRECISION_TRANSPORT.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .residue_one_arch import prime


class TransportError(ValueError):
    """Invalid frame, context, unsupported lift, or stale certificate."""


def _integer(value: int, label: str) -> int:
    if type(value) is not int:
        raise TransportError(f"{label} must be an exact integer")
    return value


def nonzero_valuation(value: int, p: int) -> int:
    """v_p(value) for nonzero integers, never v_p(0)=an invented finite debt."""
    _integer(value, "value")
    if not prime(p) or value == 0:
        raise TransportError("Need a nonzero integer and an authentic prime p")
    residue = abs(value)
    order = 0
    while residue % p == 0:
        residue //= p
        order += 1
    return order


@dataclass(frozen=True)
class PrecisionFrame:
    """F_d^{r,s}: Z/p^r -> Z/p^s, [x] -> [d*x], when well-defined.

    Exact representative independence: s <= r+v_p(d) for d!=0.
    For d=0, all output resolutions are lawful but the map is constant.
    The proof is unrestricted in r,s; implementation guards huge powers.
    """
    p: int
    r: int
    d: int
    s: int

    def __post_init__(self) -> None:
        if not prime(self.p):
            raise TransportError("p must be prime, not a fake Euler place")
        if not (type(self.r) is int and 1 <= self.r <= 12):
            raise TransportError("Input precision must be in 1..12")
        if not (type(self.s) is int and 1 <= self.s <= 32):
            raise TransportError("Output precision must be in 1..32")
        _integer(self.d, "step d")
        if self.d != 0 and self.s > self.r + nonzero_valuation(self.d, self.p):
            raise TransportError("Output exceeds representative-independent precision")

    @property
    def debt(self) -> int | None:
        return None if self.d == 0 else nonzero_valuation(self.d, self.p)

    @property
    def observed_digits(self) -> int:
        return 0 if self.d == 0 else max(0, self.s - self.debt)

    @property
    def lost_digits(self) -> int:
        return self.r - self.observed_digits

    @property
    def full_clock_faithful(self) -> bool:
        return self.d != 0 and self.observed_digits == self.r

    @property
    def image_size(self) -> int:
        return self.p ** self.observed_digits

    @property
    def fiber_size(self) -> int:
        return self.p ** self.lost_digits

    def observe(self, x: int) -> int:
        """Canonical source residue required; no representative smuggling."""
        _integer(x, "source address")
        if not 0 <= x < self.p ** self.r:
            raise TransportError("Source residue outside declared input clock")
        return (self.d * x) % (self.p ** self.s)

    def full_decode(self, y: int) -> int:
        """Inverse on image ideal iff s=r+v; no inverse for truncated clocks."""
        if not self.full_clock_faithful:
            raise TransportError("No whole-clock inverse at this precision")
        _integer(y, "output residue")
        if not 0 <= y < self.p ** self.s:
            raise TransportError("Output residue not canonical")
        scale = self.p ** self.debt
        if y % scale:
            raise TransportError("Output is not in the lifted image ideal")
        unit = self.d // scale
        x = ((y // scale) * pow(unit, -1, self.p ** self.r)) % (self.p ** self.r)
        if self.observe(x) != y:
            raise ArithmeticError("Inversion identity broken")
        return x


def minimum_full_resolution(p: int, r: int, d: int) -> int | None:
    """Minimum lawful output precision preserving every input residue."""
    if not prime(p) or not (type(r) is int and 1 <= r <= 12):
        raise TransportError("Need a prime and positive input precision")
    _integer(d, "step d")
    return None if d == 0 else r + nonzero_valuation(d, p)


@dataclass(frozen=True)
class ClaimContext:
    """An explicitly declared finite source class with a total claim table.

    basis_id/source_id/claim_id are metadata assertions, NOT external
    attestation or cryptographic proof. Equality checks prevent silent
    reuse against a different supplied source context.
    """
    p: int
    r: int
    claims: tuple[tuple[int, str], ...]
    source_id: str
    basis_id: str
    claim_id: str

    def __post_init__(self) -> None:
        if not prime(self.p) or not (type(self.r) is int and 1 <= self.r <= 12):
            raise TransportError("Claim context requires a prime clock")
        if not (type(self.claims) is tuple and 1 <= len(self.claims) <= 4096):
            raise TransportError("Need a nonempty, bounded finite source table")
        if not all(isinstance(x, str) and x for x in
                   (self.source_id, self.basis_id, self.claim_id)):
            raise TransportError("Explicit source, basis and claim IDs required")
        addresses = []
        for pair in self.claims:
            if (not isinstance(pair, tuple) or len(pair) != 2 or
                    type(pair[0]) is not int or
                    not 0 <= pair[0] < self.p ** self.r or
                    type(pair[1]) is not str):
                raise TransportError("Source addresses/claim labels must be canonical")
            addresses.append(pair[0])
        if addresses != sorted(set(addresses)):
            raise TransportError("Source addresses must be sorted and unique")

    @classmethod
    def from_mapping(cls, p: int, r: int, claims: Mapping[int, str],
                     *, source_id: str, basis_id: str, claim_id: str
                     ) -> "ClaimContext":
        return cls(p, r, tuple(sorted(claims.items())), source_id,
                   basis_id, claim_id)

    def separation_depth(self) -> int:
        """Smallest k allowing claim recovery from x mod p^k on this source.

        k=0 for a constant claim. Otherwise max(v_p(x-y)+1) over
        unequal-labeled source pairs; the answer is <=r.
        """
        k = 0
        for i, (x, tx) in enumerate(self.claims):
            for y, ty in self.claims[i + 1:]:
                if tx != ty:
                    k = max(k, nonzero_valuation(x - y, self.p) + 1)
        return k


def minimum_claim_resolution(context: ClaimContext, d: int) -> int | None:
    """Exact output resolution for a decoder of THIS claim on THIS source.

    Constant claims require only an allowed 1-digit output. A nonconstant
    claim is impossible under d=0 at every finite precision.
    """
    _integer(d, "step d")
    k = context.separation_depth()
    if k == 0:
        return 1
    return None if d == 0 else nonzero_valuation(d, context.p) + k


@dataclass(frozen=True)
class TransportVerdict:
    context: ClaimContext
    frame: PrecisionFrame
    decoder: tuple[tuple[int, str], ...]
    collision: tuple[int, int] | None
    minimum_resolution: int | None

    @property
    def valid(self) -> bool:
        return self.collision is None

    def decode(self, y: int, claimed_context: ClaimContext) -> str:
        if claimed_context != self.context:
            raise TransportError("Stale or differently sourced proof context")
        if not self.valid:
            raise TransportError("Observed fibers contain conflicting claims")
        _integer(y, "observed residue")
        if not 0 <= y < self.frame.p ** self.frame.s:
            raise TransportError("Noncanonical observed address")
        decoder = dict(self.decoder)
        if y not in decoder:
            raise TransportError("No certified source with this observation")
        return decoder[y]


def certify_transport(context: ClaimContext,
                      frame: PrecisionFrame) -> TransportVerdict:
    """Construct unique im(F|X) decoder or an explicit conflicting fiber.

    Finite exact evidence for t = g o F on the DECLARED finite source X;
    requires the supplied claim truth table as a premise.
    """
    if (context.p, context.r) != (frame.p, frame.r):
        raise TransportError("Carrier/basis mismatch between claim and frame")
    decoder: dict[int, str] = {}
    first_source: dict[int, int] = {}
    collision = None
    for x, label in context.claims:
        y = frame.observe(x)
        if y in decoder and decoder[y] != label:
            collision = (first_source[y], x)
            break
        decoder[y] = label
        first_source.setdefault(y, x)
    return TransportVerdict(context, frame, tuple(sorted(decoder.items())),
                            collision, minimum_claim_resolution(context, frame.d))


@dataclass(frozen=True)
class FullLiftComposition:
    first: PrecisionFrame
    second: PrecisionFrame
    composite: PrecisionFrame

    def apply(self, x: int) -> int:
        left = self.second.observe(self.first.observe(x))
        right = self.composite.observe(x)
        if left != right:
            raise ArithmeticError("Precision-lift composition failed")
        return right


def compose_full_lifts(p: int, r: int, d: int, e: int) -> FullLiftComposition:
    """Faithful multiplication transport composes with additive debt."""
    if d == 0 or e == 0:
        raise TransportError("Zero step has no full faithful lift")
    first_s = minimum_full_resolution(p, r, d)
    first = PrecisionFrame(p, r, d, first_s)
    second_s = minimum_full_resolution(p, first_s, e)
    second = PrecisionFrame(p, first_s, e, second_s)
    composite = PrecisionFrame(p, r, d * e, second_s)
    if composite.debt != first.debt + second.debt:
        raise ArithmeticError("Valuation-additive precision composition failed")
    return FullLiftComposition(first, second, composite)


@dataclass(frozen=True)
class InterventionVerdict:
    status: str
    semantic_conflict: tuple[int, int] | None
    observation_conflict: tuple[int, int] | None
    transport: TransportVerdict | None

    @property
    def valid(self) -> bool:
        return self.status == "source-and-observation-preserved"


def certify_intervention(before: ClaimContext, after: ClaimContext,
                         transition: Mapping[int, int],
                         frame_after: PrecisionFrame) -> InterventionVerdict:
    """Check TWO gates: source truth commutes; post-source claim is observable.

    t_before = t_after o h is a necessary independent provenance/semantics
    obligation. It is not implied by bijective clocks or more precision.
    h is an explicitly supplied (not physically established) source map.
    """
    if before.p != after.p or (after.p, after.r) != (
            frame_after.p, frame_after.r):
        raise TransportError("Incompatible source/carrier provenance")
    source = dict(before.claims)
    target = dict(after.claims)
    if (not all(type(x) is int and type(y) is int for x, y in transition.items())
            or set(transition) != set(source)):
        raise TransportError("Intervention must map EVERY original source")
    for x in source:
        if transition[x] not in target:
            raise TransportError("Intervention destination not in source-after class")
        if source[x] != target[transition[x]]:
            return InterventionVerdict("source-truth-changed",
                                       (x, transition[x]), None, None)
    reachable = {z: target[z] for z in set(transition.values())}
    context = ClaimContext.from_mapping(
        after.p, after.r, reachable, source_id=after.source_id,
        basis_id=after.basis_id, claim_id=after.claim_id)
    verdict = certify_transport(context, frame_after)
    if not verdict.valid:
        return InterventionVerdict("post-source-observation-collision",
                                   None, verdict.collision, verdict)
    return InterventionVerdict("source-and-observation-preserved",
                               None, None, verdict)


def precision_transport_demo() -> dict:
    p, r = 5, 2
    low = ClaimContext.from_mapping(
        p, r, {x: str(x % 5) for x in range(25)},
        source_id="finite-clock-X", basis_id="base-v1", claim_id="low-digit")
    high = ClaimContext.from_mapping(
        p, r, {x: str(x // 5) for x in range(25)},
        source_id="finite-clock-X", basis_id="base-v1", claim_id="high-digit")
    coarse, repaired = PrecisionFrame(p, r, 5, 2), PrecisionFrame(p, r, 5, 3)
    low_proof = certify_transport(low, coarse)
    high_failure = certify_transport(high, coarse)
    high_proof = certify_transport(high, repaired)
    if (not low_proof.valid or high_failure.valid or not high_proof.valid or
            low_proof.minimum_resolution != 2 or
            high_proof.minimum_resolution != 3):
        raise ArithmeticError("Proof-relative precision theorem failed")
    composition = compose_full_lifts(5, 2, 5, 10)
    for x in range(25):
        composition.apply(x)
        if repaired.full_decode(repaired.observe(x)) != x:
            raise ArithmeticError("Faithful lifted inverse failed")
    after = ClaimContext.from_mapping(
        p, r, {x: str(x % 5) for x in range(25)},
        source_id="translated-X", basis_id="base-v1", claim_id="low-digit")
    compatible = certify_intervention(low, after,
                                     {x: (x + 5) % 25 for x in range(25)}, coarse)
    reset = ClaimContext.from_mapping(
        p, r, {x: str(x // 5) for x in range(5)},
        source_id="reset-X", basis_id="base-v1", claim_id="high-digit")
    destructive = certify_intervention(high, reset,
                                       {x: x % 5 for x in range(25)}, repaired)
    return {
        "status": "SOURCE_RELATIVE_PRECISION_TRANSPORT_EXACT",
        "p": p, "source_precision": r, "step_d": 5,
        "precision_debt_digits": repaired.debt,
        "source_repair_output_precision": repaired.s,
        "coarse_output_precision": coarse.s,
        "coarse_lost_digits": coarse.lost_digits,
        "coarse_image_size": coarse.image_size,
        "whole_clock_recovered_after_lift": repaired.full_clock_faithful,
        "all_25_source_states_inverted": True,
        "low_digit_claim_minimum_precision": low_proof.minimum_resolution,
        "low_digit_claim_at_coarse_precision": low_proof.valid,
        "high_digit_claim_minimum_precision": high_proof.minimum_resolution,
        "high_digit_claim_at_coarse_precision": high_failure.valid,
        "high_digit_collision_witness": list(high_failure.collision),
        "high_digit_claim_after_repair": high_proof.valid,
        "two_nonzero_lifts_compose": all(composition.apply(x) ==
                                           composition.composite.observe(x)
                                           for x in range(25)),
        "composition_debt_additive": composition.composite.debt ==
                                     composition.first.debt + composition.second.debt,
        "source_preserving_intervention": compatible.valid,
        "destructive_intervention_status": destructive.status,
        "extra_precision_repairs_destructive_source_change": destructive.valid,
        "zero_step_has_finite_full_repair": minimum_full_resolution(5, 2, 0) is not None,
        "finite_source_table_authenticates_physical_truth": False,
        "RH_Gamma_or_Weil_theorem_claimed": False,
    }
