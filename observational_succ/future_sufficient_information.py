"""Minimum future-sufficient information for the arithmetic quotient observer.

The principal carry-safe research target. An observer that records only the
quotient block

    O_p(n) = ceil(n / p) = m,    where   n = p(m-1) + r + 1,  0 <= r < p,

discards the residue register r. The question: is the residue necessary to
preserve every future quotient observation under the lawful successor S?

FSO-01 (this module, PROVED LOCAL on the infinite carrier N_{>=1}):
    The largest S-stable equivalence relation that refines current quotient
    equality O_p is the identity. Equivalently, the residue register is
    necessary. The distinguishing continuation has length at most p-1, and the
    bound is sharp (attained by the pair n=1, n=2).

Proof (three lines; the code certifies the one non-trivial premise exactly):
    Let ~ refine O_p-equality and be S-stable. If x ~ y then S^k x ~ S^k y for
    all k, hence O_p(S^k x) = O_p(S^k y) for all k. But for x != y the
    separation lemma below exhibits a k <= p-1 with O_p(x+k) != O_p(y+k).
    Contradiction, so x = y.

The generic finite machinery (classical Moore/Nerode partition refinement) lives
in ``future_safe_quotient``; this module does not reimplement it. It supplies
the arithmetic-specific theorem, a machine-checkable retained-state certificate
(FSO-03), and the restricted-toolkit controls (FSO-04), and it cross-checks the
identity collapse against ``future_safe_quotient.minimize``.

Scope: declared observation O_p and declared action S (plus the FSO-04 variants).
No claim is made about every observer, every probe language, or any infinite
Hilbert statement. No Weil/RH content.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import log2

from observational_succ.carry_safe_polyphase import polyphase_coords
from observational_succ.future_safe_quotient import (
    Edge,
    Machine,
    State,
    distinguishing_word,
    minimize,
    verify_certificate,
)


class FutureInfoError(ValueError):
    """Wrong modulus, state, horizon, or a violated retention contract."""


def _integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise FutureInfoError(f"exact integer >= {minimum} required, got {x!r}")
    return x


def _modulus(p):
    if type(p) is not int or p < 2:
        raise FutureInfoError("observer modulus p >= 2 required")
    return p


# ---------------------------------------------------------------------------
# the observation and the separation lemma (FSO-01 core)
# ---------------------------------------------------------------------------

def quotient_observation(n, p):
    """O_p(n) = ceil(n/p) = m, the quotient block of n = p(m-1)+r+1."""
    _integer(n, 1)
    _modulus(p)
    return (n - 1) // p + 1


def min_separation(x, y, p):
    """Smallest k >= 0 with O_p(x+k) != O_p(y+k); None iff x == y.

    Closed form: 0 if the blocks already differ; else, with residues r < s in
    the same block, k = p - s (<= p-1). A second, independent bounded scan
    cross-checks the closed form in :func:`min_separation_scan`.
    """
    _integer(x, 1)
    _integer(y, 1)
    _modulus(p)
    if x == y:
        return None
    mx, rx = polyphase_coords(x, p)
    my, ry = polyphase_coords(y, p)
    if mx != my:
        return 0
    # same block: residues decide; separation when the larger residue carries
    r, s = sorted((rx, ry))        # r < s strictly (x != y, same block)
    return p - s


def min_separation_scan(x, y, p, horizon=None):
    """Independent route: scan k until O_p(x+k) != O_p(y+k). None if none <= horizon.

    With horizon=None the loop is bounded by p (a separation always exists at
    k <= p-1 for x != y in the same block, and at k=0 across blocks).
    """
    _integer(x, 1)
    _integer(y, 1)
    _modulus(p)
    if x == y:
        return None
    cap = p if horizon is None else horizon
    for k in range(cap + 1):
        if quotient_observation(x + k, p) != quotient_observation(y + k, p):
            return k
    return None


@dataclass(frozen=True)
class SeparationCertificate:
    p: int
    prefix: int
    all_distinct_separated: bool
    sharp_bound: int               # p - 1
    max_length_observed: int
    witness_pair: tuple            # (x, y) achieving the sharp bound
    closed_form_matches_scan: bool


def fso01_certificate(p, N):
    """Exhaustive FSO-01 certificate on the prefix {1..N}: identity collapse + sharpness.

    Verifies every distinct pair is separated (so the S-stable refinement of
    O_p is identity on the prefix), that the length never exceeds p-1, that the
    bound p-1 is attained (witness n=1,2), and that the closed form agrees with
    the independent scan on every pair.
    """
    _modulus(p)
    _integer(N, 2)
    all_sep = True
    matches = True
    max_len = 0
    witness = None
    for x in range(1, N + 1):
        for y in range(x + 1, N + 1):
            cf = min_separation(x, y, p)
            sc = min_separation_scan(x, y, p)
            if cf != sc:
                matches = False
            if cf is None:
                all_sep = False
                continue
            if cf > max_len:
                max_len = cf
                witness = (x, y)
            if cf > p - 1:
                all_sep = False      # would violate the sharp bound
    return SeparationCertificate(
        p, N, all_sep and matches, p - 1, max_len, witness, matches)


def sharp_witness(p):
    """The pair (1, 2) needs exactly p-1 successors (residues 0 and 1, block 1)."""
    _modulus(p)
    return (1, 2, min_separation(1, 2, p))


# ---------------------------------------------------------------------------
# FSO-03 : machine-checkable retained-state certificate
# ---------------------------------------------------------------------------

def arithmetic_quotient_machine(p, N, source_of=None):
    """Finite ``future_safe_quotient.Machine`` for O_p under S on {1..N}.

    Observation is the quotient block; the single action S maps n -> n+1 within
    the prefix (partial at the top). ``source_of(n)`` optionally tags a source
    label per state (defaults to the single source "arith").
    """
    _modulus(p)
    _integer(N, 2)
    if source_of is None:
        source_of = lambda n: "arith"
    states = tuple(
        State(name=f"n{n}", source=source_of(n),
              observation=f"q{quotient_observation(n, p)}", tasks=())
        for n in range(1, N + 1))
    edges = tuple(Edge(start=f"n{n}", action="S", target=f"n{n+1}", cost=Q(0))
                  for n in range(1, N))
    return Machine(states, ("S",), edges)


def confirm_identity_via_minimizer(p, N):
    """Independent cross-check: the classical minimizer collapses the prefix to identity.

    Returns (n_blocks, singletons) with singletons True iff every block is a
    singleton. NOTE: the finite machine also separates the top band via the
    S-availability signal (a finite-horizon observable the infinite FSO-01
    theorem does not use); the direct :func:`fso01_certificate` is the
    authoritative result.
    """
    machine = arithmetic_quotient_machine(p, N)
    cert = minimize(machine)
    singletons = all(len(b) == 1 for b in cert.blocks)
    verify_certificate(machine, cert)        # the engine's own certificate holds
    return len(cert.blocks), singletons


def fso03_certificate(p):
    """Structured retained-state certificate for the FSO-03 schema.

    Records: the observation map, the available action, the original
    observational equivalence (quotient blocks, size p), a shortest
    distinguishing future word, the refined future-safe equivalence (identity),
    the exact retained information (the residue register), the retention cost,
    and the source-history assumptions.
    """
    _modulus(p)
    wx, wy, wlen = sharp_witness(p)
    return {
        "observation_map": "O_p(n) = ceil(n/p) = quotient block m",
        "available_actions": ("S",),
        "original_equivalence": f"O_p-equality: block of size {p} (residues 0..{p-1})",
        "shortest_distinguishing_word": {
            "pair": (wx, wy), "word": ("S",) * wlen, "length": wlen},
        "refined_future_safe_equivalence": "identity on N_{>=1}",
        "retained_information": f"residue register r in {{0..{p-1}}}",
        "retention_cost_states": p,                 # p residues collapse to 1 block pre-S
        "retention_cost_bits": log2(p),
        "source_history_assumptions": (
            "one-based origin; unrestricted lawful successor S available"),
        "sharp_distinguishing_bound": p - 1,
    }


# ---------------------------------------------------------------------------
# FSO-04 : restricted-toolkit controls
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ToolkitPartition:
    p: int
    prefix: int
    toolkit: str
    blocks: tuple                  # tuple of tuples of ints (equivalence classes)
    is_identity: bool
    is_quotient_equality: bool


def _blocks_from_relation(items, related):
    """Partition ``items`` by the equivalence ``related`` (reflexive, symmetric)."""
    blocks = []
    for x in items:
        for b in blocks:
            if related(x, b[0]):
                b.append(x)
                break
        else:
            blocks.append([x])
    return tuple(tuple(b) for b in blocks)


def toolkit_partition(p, N, horizon):
    """Coarsest O_p-refining equivalence stable under S with successor horizon.

    horizon = 0        : no future action usable -> O_p-equality survives
                         (residue discarded, and it is sufficient).
    horizon >= p-1     : unrestricted enough -> identity (FSO-01).
    0 < horizon < p-1  : strictly intermediate classes survive.

    Two states are related iff O_p agrees on every word S^k with k <= horizon.
    """
    _modulus(p)
    _integer(N, 2)
    _integer(horizon, 0)
    items = tuple(range(1, N + 1))

    def related(x, y):
        return min_separation_scan(x, y, p, horizon=horizon) is None

    blocks = _blocks_from_relation(items, related)
    is_identity = all(len(b) == 1 for b in blocks)
    # O_p-equality on the (interior) prefix has blocks exactly the quotient blocks
    quotient_blocks = _blocks_from_relation(
        items, lambda x, y: quotient_observation(x, p) == quotient_observation(y, p))
    is_qeq = blocks == quotient_blocks
    label = ("no-future-action" if horizon == 0 else
             "unrestricted-S" if horizon >= p - 1 else
             f"bounded-horizon-{horizon}")
    return ToolkitPartition(p, N, label, blocks, is_identity, is_qeq)


def toolkit_spectrum(p, N):
    """The full FSO-04 spectrum: horizon 0, an intermediate, and p-1.

    Returns a dict horizon -> ToolkitPartition demonstrating that the minimal
    retained state depends on the action language: it grows from "nothing
    beyond O_p" (horizon 0) through intermediate residue distinctions to the
    full residue register (horizon p-1, identity).
    """
    _modulus(p)
    out = {0: toolkit_partition(p, N, 0)}
    if p >= 3:
        out[1] = toolkit_partition(p, N, 1)
    out[p - 1] = toolkit_partition(p, N, p - 1)
    return out
