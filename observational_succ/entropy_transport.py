"""Finite, source-relative information transport: a classical laboratory.

Probability tables, functional dependencies, product-law checks and TV are
exact. Shannon entropies are FLOAT DIAGNOSTICS IN BITS, not interval bounds,
formal proofs, or exact certificates for irrational numerical inequalities.
All terms of each identity use ONE declared joint law. A source_id is a
metadata assertion; this module cannot authenticate a physical source.

The mathematical proofs are elementary entropy chain rules. Provenance:
OpenAI, Bounded-Step Walks on Gaussian Primes (2026), coverage-transfer.tex
and information.tex; see the accompanying research dossier. Conditional
entropy continuity independent of the conditioning alphabet is classical;
the elementary bound here is weaker than Alhejji--Smith (arXiv:1909.00787).
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import fsum, log2
from typing import Hashable, Mapping, Sequence


class EntropyTransportError(ValueError):
    """Malformed law, inconsistent source, or unpaid/noninvertible update."""


@dataclass(frozen=True)
class FiniteLaw:
    """A normalized finite joint distribution with named random variables.

    atoms contains (value_tuple, exact_probability) pairs. Zero mass atoms
    are ignored. Duplicate value tuples are combined without resampling.
    """
    variables: tuple[str, ...]
    atoms: tuple[tuple[tuple[Hashable, ...], Fraction], ...]
    source_id: str

    def __post_init__(self):
        if (type(self.variables) is not tuple or not self.variables
                or any(type(x) is not str or not x for x in self.variables)
                or len(set(self.variables)) != len(self.variables)):
            raise EntropyTransportError("Distinct named variables required")
        if type(self.source_id) is not str or not self.source_id:
            raise EntropyTransportError("Explicit source_id required")
        if type(self.atoms) is not tuple or not self.atoms:
            raise EntropyTransportError("Nonempty immutable probability table required")
        clean = defaultdict(Fraction)
        for atom in self.atoms:
            if type(atom) is not tuple or len(atom) != 2:
                raise EntropyTransportError("Each atom is (values, probability)")
            values, weight = atom
            if type(values) is not tuple or len(values) != len(self.variables):
                raise EntropyTransportError("Atom does not match named variables")
            try:
                hash(values)
            except TypeError as exc:
                raise EntropyTransportError("Atom values must be hashable") from exc
            if not (type(weight) is int or isinstance(weight, Fraction)):
                raise EntropyTransportError("Only integer/Fraction weights are exact")
            if weight < 0:
                raise EntropyTransportError("Negative probability")
            if weight:
                clean[values] += Fraction(weight)
        if sum(clean.values(), Fraction()) != 1:
            raise EntropyTransportError("Probabilities must sum exactly to one")
        object.__setattr__(self, "atoms", tuple(clean.items()))

    def names(self, names: Sequence[str]) -> tuple[str, ...]:
        if isinstance(names, str):
            raise EntropyTransportError("Pass a sequence of variable names, not a string")
        result = tuple(names)
        if len(set(result)) != len(result) or any(x not in self.variables for x in result):
            raise EntropyTransportError("Unknown or repeated variable name")
        return result

    def marginal(self, names: Sequence[str]) -> dict[tuple, Fraction]:
        names = self.names(names)
        indices = tuple(self.variables.index(x) for x in names)
        out = defaultdict(Fraction)
        for atom, weight in self.atoms:
            out[tuple(atom[i] for i in indices)] += weight
        return dict(out)


def _union(*groups: Sequence[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(x for group in groups for x in group))


def entropy(law: FiniteLaw, names: Sequence[str]) -> float:
    """Numerical Shannon entropy in bits; not an exact real certificate."""
    return -fsum(float(p) * (log2(p.numerator) - log2(p.denominator))
                 for p in law.marginal(names).values())


def conditional_entropy(law: FiniteLaw, target: Sequence[str],
                        given: Sequence[str] = ()) -> float:
    target, given = law.names(target), law.names(given)
    joint_names = _union(given, target)
    base = law.marginal(given)
    terms = []
    for values, p in law.marginal(joint_names).items():
        ratio = p / base[values[:len(given)]]
        terms.append(-float(p) * (log2(ratio.numerator) - log2(ratio.denominator)))
    return fsum(terms)


def mutual_information(law: FiniteLaw, left: Sequence[str],
                       right: Sequence[str], given: Sequence[str] = ()) -> float:
    left, right, given = law.names(left), law.names(right), law.names(given)
    return (conditional_entropy(law, left, given)
            - conditional_entropy(law, left, _union(given, right)))


def require_determined(law: FiniteLaw, target: Sequence[str],
                       given: Sequence[str]) -> None:
    """Exact functional-dependency check on every positive-mass atom."""
    target, given = law.names(target), law.names(given)
    joint_names = _union(given, target)
    target_indices = tuple(joint_names.index(x) for x in target)
    seen = {}
    for values in law.marginal(joint_names):
        key = values[:len(given)]
        output = tuple(values[i] for i in target_indices)
        if key in seen and seen[key] != output:
            raise EntropyTransportError(
                f"{target} is not determined by {given}: "
                f"input {key!r} has outputs {seen[key]!r} and {output!r}")
        seen[key] = output


def conditionally_independent(law: FiniteLaw, coordinates: Sequence[str],
                              given: Sequence[str] = ()) -> bool:
    """Exact product-law test; correlated/repeated coordinates are allowed
    by the transport theorem but cannot be billed as independent facts.
    """
    coordinates, given = law.names(coordinates), law.names(given)
    if set(coordinates) & set(given):
        raise EntropyTransportError("Product coordinates must be outside the context")
    joint = law.marginal(_union(given, coordinates))
    base = law.marginal(given)
    singles = [law.marginal(_union(given, (x,))) for x in coordinates]
    # Matching every positive joint atom suffices: the product law is
    # normalized, so agreement on mass one leaves zero mass elsewhere.
    # This avoids enumerating an exponentially large Cartesian alphabet.
    for key, mass in joint.items():
        context, values = key[:len(given)], key[len(given):]
        context_mass = base[context]
        rhs = Fraction(1)
        for marginal, value in zip(singles, values):
            rhs *= marginal[context + (value,)] / context_mass
        if mass / context_mass != rhs:
            return False
    return True


def shared_conditioning_identity(law: FiniteLaw, coordinates: Sequence[str],
                                update: Sequence[str], *,
                                alphabet_sizes: Mapping[str, int],
                                receiver: Sequence[str] = ()) -> dict:
    """Exact MATHEMATICAL identity, displayed with numeric diagnostics.

    Sum marginal deficits = joint deficit + I(X;U|R) - TC(X|R,U).
    Thus the entire shared update costs at most H(U|R), paid once.
    The theorem requires no coordinate or source/update independence.
    """
    coordinates, update, receiver = (law.names(x) for x in
                                     (coordinates, update, receiver))
    if not coordinates:
        raise EntropyTransportError("At least one coordinate required")
    capacity = 0.0
    for x in coordinates:
        size = alphabet_sizes.get(x)
        if type(size) is not int or size < len(law.marginal((x,))):
            raise EntropyTransportError("Declared alphabet must contain every source value")
        capacity += log2(size)
    context = _union(receiver, update)
    joint_deficit = capacity - conditional_entropy(law, coordinates, receiver)
    marginal_sum = fsum(conditional_entropy(law, (x,), context) for x in coordinates)
    total_correlation = marginal_sum - conditional_entropy(law, coordinates, context)
    update_information = mutual_information(law, coordinates, update, receiver)
    update_entropy = conditional_entropy(law, update, receiver)
    return {
        "status": "NUMERIC_ENTROPY_DIAGNOSTIC",
        "sum_conditional_deficits_bits": capacity - marginal_sum,
        "joint_deficit_bits": joint_deficit,
        "update_information_bits": update_information,
        "conditional_total_correlation_bits": total_correlation,
        "identity_rhs_bits": joint_deficit + update_information - total_correlation,
        "shared_update_entropy_bits": update_entropy,
        "upper_bound_bits": joint_deficit + update_entropy,
    }


def reversible_information_transport(law: FiniteLaw, *,
                                    old_target: Sequence[str],
                                    new_target: Sequence[str],
                                    word: Sequence[str], update: Sequence[str],
                                    old_context: Sequence[str] = (),
                                    new_context: Sequence[str] = (),
                                    receiver: Sequence[str] = ()) -> dict:
    """Check conditional frame bijections exactly, then diagnose the loss.

    Given U,R, old/new contexts determine one another and the full frames
    determine one another. Equality holds for any such triangular frame
    bijection, including additive residue translation. No exogeneity of U
    is silently assumed. The receiver context R conditions EVERY term.
    """
    x, xp, w, u, o, op, r = (law.names(names) for names in
                             (old_target, new_target, word, update,
                              old_context, new_context, receiver))
    require_determined(law, o, _union(op, u, r))
    require_determined(law, op, _union(o, u, r))
    require_determined(law, x, _union(xp, op, u, r))
    require_determined(law, xp, _union(x, o, u, r))
    sender = mutual_information(law, x, u, _union(o, r))
    unlocked = mutual_information(law, xp, u, _union(op, w, r))
    already = mutual_information(law, xp, u, _union(op, r))
    old = mutual_information(law, x, _union(u, w), _union(o, r))
    new = mutual_information(law, xp, w, _union(op, r))
    return {
        "status": "EXACT_FRAME_CHECKS_NUMERIC_ENTROPY_DIAGNOSTICS",
        "old_package_information_bits": old,
        "new_word_information_bits": new,
        "loss_bits": old - new,
        "sender_revelation_bits": sender,
        "receiver_unlocking_bits": unlocked,
        "receiver_preexisting_bits": already,
        "identity_loss_bits": sender + unlocked - already,
        "two_update_entropy_bound_bits": 2 * conditional_entropy(law, u, r),
        "receiver_aware_bound_bits": sender + conditional_entropy(law, u, _union(op, w, r)),
    }


def conditional_continuity(p: FiniteLaw, q: FiniteLaw,
                           target: Sequence[str], given: Sequence[str], *,
                           alphabet_size: int) -> dict:
    """Exact TV plus diagnostic |H_P(A|B)-H_Q(A|B)| <= d log|A|+h(d).

    No factor involving |B|. The elementary common-part mixture proof
    works for every d in [0,1], with endpoints interpreted continuously.
    Source/basis declarations must agree before comparing different laws.
    """
    if p.source_id != q.source_id or p.variables != q.variables:
        raise EntropyTransportError("Continuity requires matching source and named basis")
    target, given = p.names(target), p.names(given)
    support = set(p.marginal(target)) | set(q.marginal(target))
    if type(alphabet_size) is not int or alphabet_size < len(support):
        raise EntropyTransportError("Target alphabet is too small")
    pm, qm = p.marginal(_union(target, given)), q.marginal(_union(target, given))
    distance = sum((abs(pm.get(k, 0) - qm.get(k, 0)) for k in pm.keys() | qm.keys()),
                   Fraction()) / 2
    d = float(distance)
    binary = -fsum(float(t) * (log2(t.numerator) - log2(t.denominator))
                   for t in (distance, 1-distance) if t)
    return {
        "status": "EXACT_TV_NUMERIC_ENTROPY_DIAGNOSTICS",
        "total_variation": distance,
        "entropy_difference_bits": abs(conditional_entropy(p, target, given)
                                       - conditional_entropy(q, target, given)),
        "continuity_bound_bits": d * log2(alphabet_size) + binary,
        "target_alphabet_size": alphabet_size,
    }


def block_transport(law: FiniteLaw, *, blocks: Sequence[Sequence[str]],
                    states: Sequence[Sequence[str]], initial: Sequence[str],
                    update: Sequence[str] = (), receiver: Sequence[str] = ()) -> dict:
    """Pay one shared U for an entire moving-state block decomposition.

    Require R_a = f_a(R_0,U,B_<a,R) exactly on the declared source law.
    Then H(V|R_0,R) <= I(V;U|R_0,R) + sum H(B_a|R_a,R).
    An update not determined by the charged inputs is rejected, even if
    an accidental numerical entropy inequality happens to hold.
    """
    blocks, states = tuple(map(law.names, blocks)), tuple(map(law.names, states))
    initial, update, receiver = (law.names(x) for x in (initial, update, receiver))
    word = tuple(x for block in blocks for x in block)
    if not blocks or len(blocks) != len(states) or any(not b for b in blocks):
        raise EntropyTransportError("One starting state per nonempty block required")
    if len(set(word)) != len(word):
        raise EntropyTransportError("Blocks must use distinct observation-event columns")
    prefix = ()
    remaining = 0.0
    for block, state in zip(blocks, states):
        require_determined(law, state, _union(initial, update, receiver, prefix))
        remaining += conditional_entropy(law, block, _union(state, receiver))
        prefix += block
    context = _union(initial, receiver)
    cost = mutual_information(law, word, update, context)
    entropy_cost = conditional_entropy(law, update, context)
    return {
        "status": "EXACT_UPDATE_CHECKS_NUMERIC_ENTROPY_DIAGNOSTICS",
        "word_entropy_bits": conditional_entropy(law, word, context),
        "local_block_entropy_sum_bits": remaining,
        "shared_update_information_bits": cost,
        "shared_update_entropy_bits": entropy_cost,
        "information_bound_bits": remaining + cost,
        "entropy_bound_bits": remaining + entropy_cost,
        "block_count": len(blocks),
    }


def sharp_mod5_law() -> FiniteLaw:
    """Two fair bits: X=2R+1+B, S=-B, X'=X+S mod5, W=R xor B.

    Both residues avoid zero. The map is a translation for each S, and S
    is deterministic from X. I(X;S,W)=2, I(X';W)=0, H(S)=1 bit.
    """
    return FiniteLaw(("X", "S", "XP", "W"), tuple(
        ((2*r + 1 + b, -b, 2*r + 1, r ^ b), Fraction(1, 4))
        for r in range(2) for b in range(2)), "sharp-mod5-four-point-source")


def entropy_transport_probe() -> dict:
    law = sharp_mod5_law()
    sharp = reversible_information_transport(law, old_target=("X",),
        new_target=("XP",), word=("W",), update=("S",))
    require_determined(law, ("S",), ("X",))
    if not conditionally_independent(law, ("XP", "W")):
        raise ArithmeticError("Sharp counterexample lost its exact independence")
    repeated = FiniteLaw(("X0", "X1", "U"),
        (((0, 0, 0), Fraction(1, 2)), ((1, 1, 1), Fraction(1, 2))),
        "duplicate-fact-control")
    identity = shared_conditioning_identity(repeated, ("X0", "X1"), ("U",),
                                           alphabet_sizes={"X0": 2, "X1": 2})
    paid = block_transport(repeated, blocks=(("X0",), ("X1",)),
                           states=(("U",), ("U",)), initial=(), update=("U",))
    try:
        block_transport(repeated, blocks=(("X0",), ("X1",)),
                        states=(("U",), ("U",)), initial=())
    except EntropyTransportError:
        unpaid_rejected = True
    else:
        raise ArithmeticError("Unpaid future information passed update validation")
    return {
        "status": "EXACT_FINITE_STRUCTURE_NUMERIC_ENTROPY_DIAGNOSTICS",
        "entropy_units": "bits",
        "formal_proof_or_interval_certificate": False,
        "sharp_mod5_two_H_control": sharp,
        "repeated_coordinate_identity": identity,
        "repeated_facts_are_independent": conditionally_independent(repeated, ("X0", "X1")),
        "shared_block_update": paid,
        "uncharged_update_rejected": unpaid_rejected,
    }
