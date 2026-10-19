"""Source-indexed Beck–Chevalley for finite carriers and Prop-valued support.

Classical content (NOT new).  In any regular category — in particular the
category of finite sets — the existential-image left adjoint ``∃_q`` satisfies
the Beck–Chevalley condition across every PULLBACK (cartesian) square::

        S' --g'--> S
        |          |
       q'          q
        v          v
        O' --g---> O            g ∘ q' = q ∘ g'

        g*(∃_q F)  ≅  ∃_{q'}(g'* F)        for every predicate  F ⊆ S.

Here ``∃_q F`` is the image of ``F`` under ``q``, the pullback ``g*`` is the
preimage, and for a cartesian square the canonical comparison is an *equality*
of subobjects of ``O'``.  References: Mac Lane & Moerdijk, *Sheaves in Geometry
and Logic*, §I.9 (the Beck–Chevalley condition); Jacobs, *Categorical Logic and
Type Theory*, §1.9.  This module *reproves the finite case by exhaustive
predicate comparison*; it introduces NO new categorical theorem.

Candidate novelty (labeled new-to-project SYNTHESIS, not a theorem): a
*source-realization* interface layered over the formal existential.  The formal
``∃`` records only a truth value (a subobject of ``O``); a REALIZATION
CERTIFICATE additionally exhibits an ACTUAL source element of ``S`` (resp. of
``S'``) witnessing it.  We exhibit a (non-cartesian) square on which the FORMAL
Beck–Chevalley equality is preserved while a specific source-realization
certificate is BROKEN — the "source-reality firewall": a legitimate
fiber-product witness that is not backed by any genuine element of the source
carrier ``S'``.

Choice discipline (constructive / witnessed).  Every witness selection here is a
deterministic least-index search over an explicitly ordered finite carrier.
That is the dependent/witnessed form of choice (projection out of a decidable
Σ over a finite index), which is immediate and needs no unrestricted axiom of
choice.  Nothing in this file requires ``Classical.choice`` or excluded middle,
and none is used.  Source/basis labels are *declared contracts*, not
independent source authentication.

FIREWALL: finite sets only; exact dict/tuple maps; no floats, no randomness.
No RH / Weil / Schur content.  This is not a physical experiment and not a
proof about human cognition.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any, Hashable


class BeckChevalleyError(ValueError):
    """A malformed carrier, map, square, predicate, or illegal comparison."""


# --------------------------------------------------------------------------- #
# Carriers, maps, predicates (all exact finite data).
# --------------------------------------------------------------------------- #
Element = Hashable
Carrier = tuple  # an ordered tuple of distinct hashable elements (a finite set)


def check_carrier(carrier: Carrier, label: str = "carrier") -> tuple:
    """Validate a finite carrier: an ordered tuple of DISTINCT elements."""
    if not isinstance(carrier, tuple):
        raise BeckChevalleyError(f"{label} must be a tuple (ordered finite set)")
    if len(set(carrier)) != len(carrier):
        raise BeckChevalleyError(f"{label} elements must be distinct")
    return carrier


@dataclass(frozen=True)
class FiniteMap:
    """A total function between two explicit finite carriers.

    ``pairs`` lists ``(x, f(x))`` for every ``x`` in ``domain`` IN DOMAIN ORDER,
    making the map an exact, replayable dict.  ``codomain`` is stored
    explicitly because the pushforward/pullback depend on it, not merely on the
    image.
    """
    domain: Carrier
    codomain: Carrier
    pairs: tuple

    def __post_init__(self) -> None:
        check_carrier(self.domain, "map domain")
        check_carrier(self.codomain, "map codomain")
        if not isinstance(self.pairs, tuple):
            raise BeckChevalleyError("map pairs must be a tuple")
        if tuple(x for x, _ in self.pairs) != self.domain:
            raise BeckChevalleyError(
                "map must assign exactly the domain, in domain order (total, well-defined)"
            )
        cod = set(self.codomain)
        for _, y in self.pairs:
            if y not in cod:
                raise BeckChevalleyError("map image escapes the declared codomain")

    def apply(self, x: Element) -> Element:
        for a, b in self.pairs:
            if a == x:
                return b
        raise BeckChevalleyError(f"{x!r} is not in the map domain")

    def table(self) -> dict:
        return {a: b for a, b in self.pairs}


def finite_map(domain: Carrier, codomain: Carrier, rule) -> FiniteMap:
    """Build a :class:`FiniteMap` from a dict or a callable ``rule``."""
    domain = check_carrier(domain, "domain")
    codomain = check_carrier(codomain, "codomain")
    if callable(rule):
        pairs = tuple((x, rule(x)) for x in domain)
    elif isinstance(rule, dict):
        if set(rule) != set(domain):
            raise BeckChevalleyError("dict rule must have exactly the domain as keys")
        pairs = tuple((x, rule[x]) for x in domain)
    else:
        raise BeckChevalleyError("rule must be a callable or a dict")
    return FiniteMap(domain, codomain, pairs)


def predicate(carrier: Carrier, members) -> frozenset:
    """A Prop-valued predicate on ``carrier`` as its support (the True-set).

    Membership == the proposition holds.  Returned as a ``frozenset`` subset of
    the carrier; equality of predicates is set equality of supports.
    """
    check_carrier(carrier, "predicate carrier")
    support = frozenset(members)
    if not support <= set(carrier):
        raise BeckChevalleyError("predicate support must lie inside its carrier")
    return support


# --------------------------------------------------------------------------- #
# The two base-change operations (adjoints on Prop-valued support).
# --------------------------------------------------------------------------- #
def exists_pushforward(q: FiniteMap, F: frozenset) -> frozenset:
    """``∃_q F`` — the existential image of ``F ⊆ dom(q)`` under ``q``.

    ``(∃_q F)(o)``  ⇔  ∃ s ∈ dom(q).  q(s) = o  ∧  F(s).
    Returned as a subset of ``cod(q)``.
    """
    if not isinstance(F, frozenset) or not F <= set(q.domain):
        raise BeckChevalleyError("F must be a predicate on the domain of q")
    return frozenset(q.apply(s) for s in q.domain if s in F)


def pullback(g: FiniteMap, G: frozenset) -> frozenset:
    """``g* G`` — substitution/preimage of ``G ⊆ cod(g)`` along ``g``.

    ``(g* G)(o') = G(g(o'))``; returned as a subset of ``dom(g)``.
    """
    if not isinstance(G, frozenset) or not G <= set(g.codomain):
        raise BeckChevalleyError("G must be a predicate on the codomain of g")
    return frozenset(o for o in g.domain if g.apply(o) in G)


# --------------------------------------------------------------------------- #
# Cartesian squares of carriers.
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Square:
    """A square of carriers with the four structure maps of Beck–Chevalley::

        S' --g_prime--> S
        |               |
      q_prime           q
        v               v
        O' --g--------> O

    Carriers carry a declared ``source_id`` contract; it is provenance metadata,
    not a certificate of independent source authentication.
    """
    S: Carrier
    S_prime: Carrier
    O: Carrier
    O_prime: Carrier
    q: FiniteMap           # S  -> O
    g: FiniteMap           # O' -> O
    g_prime: FiniteMap     # S' -> S
    q_prime: FiniteMap     # S' -> O'
    source_id: str = "declared-square-source"

    def __post_init__(self) -> None:
        check_carrier(self.S, "S")
        check_carrier(self.S_prime, "S'")
        check_carrier(self.O, "O")
        check_carrier(self.O_prime, "O'")
        checks = [
            (self.q, self.S, self.O, "q: S -> O"),
            (self.g, self.O_prime, self.O, "g: O' -> O"),
            (self.g_prime, self.S_prime, self.S, "g': S' -> S"),
            (self.q_prime, self.S_prime, self.O_prime, "q': S' -> O'"),
        ]
        for m, dom, cod, label in checks:
            if not isinstance(m, FiniteMap):
                raise BeckChevalleyError(f"{label} must be a FiniteMap")
            if m.domain != dom or m.codomain != cod:
                raise BeckChevalleyError(f"{label} has the wrong domain/codomain")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise BeckChevalleyError("explicit nonempty source_id required")


def is_commutative(square: Square) -> bool:
    """Check ``g ∘ q' = q ∘ g'`` as maps ``S' -> O`` (the square's one law)."""
    return all(
        square.g.apply(square.q_prime.apply(s)) == square.q.apply(square.g_prime.apply(s))
        for s in square.S_prime
    )


def fiber_product(square: Square) -> tuple:
    """The explicit pullback object ``S ×_O O' = {(s, o') : q(s) = g(o')}``.

    Enumerated in ``(S × O')`` lexicographic order for determinism.
    """
    return tuple(
        (s, o)
        for s in square.S
        for o in square.O_prime
        if square.q.apply(s) == square.g.apply(o)
    )


def comparison_map(square: Square) -> dict:
    """The canonical ``φ: S' -> S ×_O O',  s' ↦ (g'(s'), q'(s'))`` as a dict.

    Only meaningful when the square commutes (otherwise some image escapes the
    fiber product); callers gate on :func:`is_commutative`.
    """
    return {
        s: (square.g_prime.apply(s), square.q_prime.apply(s))
        for s in square.S_prime
    }


def is_cartesian(square: Square) -> bool:
    """``True`` iff the square is a pullback: ``S' ≅ {(s,o'): q(s)=g(o')}``.

    Concretely: the square commutes AND the comparison map ``φ`` is a bijection
    from ``S'`` onto the fiber product.  Over finite carriers this is decidable
    by an exact element count plus image comparison.
    """
    if not is_commutative(square):
        return False
    P = fiber_product(square)
    phi = comparison_map(square)
    images = list(phi.values())
    # Every image lands in P because the square commutes.
    return len(images) == len(set(images)) and set(images) == set(P)


# --------------------------------------------------------------------------- #
# Beck–Chevalley comparison on Prop-valued support.
# --------------------------------------------------------------------------- #
def bc_left(square: Square, F: frozenset) -> frozenset:
    """Left-hand side  ``g*(∃_q F)``  as a predicate on ``O'``."""
    return pullback(square.g, exists_pushforward(square.q, F))


def bc_right(square: Square, F: frozenset) -> frozenset:
    """Right-hand side  ``∃_{q'}(g'* F)``  as a predicate on ``O'``."""
    return exists_pushforward(square.q_prime, pullback(square.g_prime, F))


def beck_chevalley_holds(square: Square, F: frozenset) -> bool:
    """Formal Beck–Chevalley equality for a single predicate ``F ⊆ S``."""
    F = predicate(square.S, F)
    return bc_left(square, F) == bc_right(square, F)


def all_predicates(carrier: Carrier) -> tuple:
    """Every Prop-valued predicate on ``carrier`` (its full powerset)."""
    check_carrier(carrier, "carrier")
    if len(carrier) > 16:
        raise BeckChevalleyError("exhaustive predicate sweep restricted to <=16 elements")
    out = []
    for bits in product((False, True), repeat=len(carrier)):
        out.append(frozenset(x for x, b in zip(carrier, bits) if b))
    return tuple(out)


def beck_chevalley_holds_all(square: Square) -> bool:
    """Formal Beck–Chevalley equality for EVERY predicate ``F ⊆ S``.

    This is the exhaustive-predicate-comparison check referenced by the theorem:
    for finite carriers it is a complete decision procedure.
    """
    return all(beck_chevalley_holds(square, F) for F in all_predicates(square.S))


# --------------------------------------------------------------------------- #
# Source-realization certificate layer (new-to-project SYNTHESIS).
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class RealizationCertificate:
    """A witness that ``o' ∈ ∃_{q'}(g'* F)`` is backed by an ACTUAL element of
    the source carrier ``S'`` (not merely a formal existential).

    ``witness`` is a genuine ``s' ∈ S'`` with ``q'(s') = o'`` and ``g'(s') ∈ F``.
    ``over`` records the element ``g'(s') ∈ S`` it lies over.
    """
    o_prime: Element
    witness: Element
    over: Element


def realize_right(square: Square, F: frozenset) -> dict:
    """Deterministic source-realizers for the RHS predicate ``∃_{q'}(g'* F)``.

    For each ``o' ∈ O'`` that holds, return the LEAST-index ``s' ∈ S'`` (in the
    carrier's declared order) with ``q'(s') = o'`` and ``g'(s') ∈ F``.  This is a
    witnessed choice from a decidable finite Σ — no unrestricted AC.
    """
    F = predicate(square.S, F)
    certs: dict = {}
    for s in square.S_prime:                       # declared carrier order
        o = square.q_prime.apply(s)
        if o in certs:
            continue
        if square.g_prime.apply(s) in F:
            certs[o] = RealizationCertificate(o, s, square.g_prime.apply(s))
    return certs


def formal_fiber_witnesses(square: Square, F: frozenset) -> tuple:
    """All fiber-product pairs ``(s, o')`` with ``s ∈ F`` — the FORMAL witnesses
    to ``o' ∈ g*(∃_q F)`` coming from an element of ``S``.

    Each such pair is a legitimate existential witness at the ``O`` level; the
    firewall asks whether it is ALSO realized by a genuine element of ``S'``.
    """
    F = predicate(square.S, F)
    return tuple((s, o) for (s, o) in fiber_product(square) if s in F)


def source_realized_fiber_witnesses(square: Square, F: frozenset) -> frozenset:
    """Fiber-product witnesses that ARE backed by an actual ``s' ∈ S'``.

    A pair ``(s, o') ∈ S ×_O O'`` is source-realized iff some ``s' ∈ S'`` has
    ``φ(s') = (s, o')``, i.e. ``g'(s') = s`` and ``q'(s') = o'``.
    """
    F = predicate(square.S, F)
    phi = comparison_map(square)
    realized_pairs = set(phi.values())
    return frozenset(
        (s, o) for (s, o) in formal_fiber_witnesses(square, F) if (s, o) in realized_pairs
    )


def comparison_is_surjective(square: Square) -> bool:
    """``True`` iff the comparison map ``φ`` is SURJECTIVE onto the fiber product
    (it need not be injective).  This is cartesianness minus the injectivity
    clause.
    """
    return set(comparison_map(square).values()) == set(fiber_product(square))


def is_realization_faithful(square: Square) -> bool:
    """``True`` iff the square is *realization-faithful* for every predicate:
    formal Beck–Chevalley holds for all ``F`` AND no formal fiber witness is a
    ghost (unrealized) for any ``F``.

    ELEMENTARY PROPOSITION (academic novelty NOT asserted; proof in the research
    note §8, exhaustively corroborated over all commutative squares with
    carriers of size <= 3): a finite commutative square is realization-faithful
    iff :func:`comparison_is_surjective`.  Faithfulness forbids ghosts
    (needs φ onto the fiber product) but tolerates redundant over-realizers
    (does not need φ injective), so it sits strictly between cartesian and
    merely-formal-Beck–Chevalley.
    """
    if not beck_chevalley_holds_all(square):
        return False
    return all(
        not realization_firewall_breaks(square, F)
        for F in all_predicates(square.S)
    )


def realization_firewall_breaks(square: Square, F: frozenset) -> bool:
    """``True`` iff some FORMAL fiber witness is NOT source-realized in ``S'``.

    When this is ``True`` the formal existential data over ``O`` names a witness
    pair that no actual element of the source carrier ``S'`` certifies — a ghost
    witness.  This can co-occur with :func:`beck_chevalley_holds` being ``True``
    (formal ∃ preserved, realization certificate broken): the source-reality
    firewall.
    """
    formal = set(formal_fiber_witnesses(square, F))
    realized = set(source_realized_fiber_witnesses(square, F))
    return formal != realized


# --------------------------------------------------------------------------- #
# (2) Exhaustive minimal non-cartesian counterexample.
# --------------------------------------------------------------------------- #
def _named(prefix: str, n: int) -> Carrier:
    return tuple(f"{prefix}{i}" for i in range(n))


def _all_maps(domain: Carrier, codomain: Carrier):
    """Every total map ``domain -> codomain``, enumerated deterministically."""
    if len(codomain) == 0:
        # Only the empty domain admits a map into the empty codomain.
        if len(domain) == 0:
            yield FiniteMap(domain, codomain, ())
        return
    for images in product(codomain, repeat=len(domain)):
        yield FiniteMap(domain, codomain, tuple(zip(domain, images)))


def find_minimal_counterexample(max_elements: int = 4, allow_empty: bool = False):
    """Smallest NON-cartesian square with ``g*(∃_q F) ≠ ∃_{q'}(g'* F)``.

    Exhaustive search over finite carriers whose sizes are each in
    ``[lo .. max_elements]`` (``lo = 0`` if ``allow_empty`` else ``1``).
    Ordering (fully deterministic):

    1. ascending total element count ``|S| + |S'| + |O| + |O'|``;
    2. then ascending ``(|O|, |O'|, |S|, |S'|)`` lexicographically;
    3. then the natural product order over maps ``(q, g, g', q')``;
    4. then ascending predicate order over ``F ⊆ S``.

    The FIRST square+predicate that (a) commutes, (b) is not cartesian and
    (c) breaks the formal equality is returned as
    ``(square, F, bc_left, bc_right)``.  Because every size-tuple strictly below
    the winner is exhausted first, the result is minimal in that order.

    With inhabited carriers (``allow_empty=False``) size-4 squares are all
    singletons (hence cartesian), so the minimum lives at total 5.  Admitting
    the empty carrier exposes a smaller (total 3) degenerate witness in which
    ``S'`` is empty and the RHS is vacuous.
    """
    lo = 0 if allow_empty else 1
    hi = max_elements
    for total in range(4 * lo, 4 * hi + 1):
        for nO in range(lo, hi + 1):
            for nOp in range(lo, hi + 1):
                for nS in range(lo, hi + 1):
                    for nSp in range(lo, hi + 1):
                        if nO + nOp + nS + nSp != total:
                            continue
                        O = _named("o", nO)
                        Op = _named("p", nOp)
                        S = _named("s", nS)
                        Sp = _named("t", nSp)
                        for q in _all_maps(S, O):
                            for g in _all_maps(Op, O):
                                for gp in _all_maps(Sp, S):
                                    for qp in _all_maps(Sp, Op):
                                        sq = Square(S, Sp, O, Op, q, g, gp, qp)
                                        if not is_commutative(sq):
                                            continue
                                        if is_cartesian(sq):
                                            continue
                                        for F in all_predicates(S):
                                            L = bc_left(sq, F)
                                            R = bc_right(sq, F)
                                            if L != R:
                                                return sq, F, L, R
    return None


# --------------------------------------------------------------------------- #
# (3) SUCC clock-quotient cartesian square  Z/mZ -> Z/nZ  (n | m).
# --------------------------------------------------------------------------- #
def cyclic_carrier(m: int) -> Carrier:
    """The finite clock ``Z/mZ`` as the explicit carrier ``(0, 1, ..., m-1)``."""
    if type(m) is not int or m < 1 or m > 256:
        raise BeckChevalleyError("clock modulus must be an int in [1, 256]")
    return tuple(range(m))


def clock_reduction(m: int, n: int) -> FiniteMap:
    """The canonical quotient ``Z/mZ -> Z/nZ, x ↦ x mod n`` (requires ``n | m``)."""
    if m % n != 0:
        raise BeckChevalleyError("clock reduction Z/mZ->Z/nZ requires n | m")
    return finite_map(cyclic_carrier(m), cyclic_carrier(n), lambda x: x % n)


def clock_quotient_square(m: int, n: int, mp: int) -> Square:
    """A CARTESIAN square of clock quotients over the shared base ``Z/nZ``::

        S' = Z/mZ ×_{Z/nZ} Z/mpZ --g'--> S = Z/mZ
        |                                 |
       q'                                 q = (mod n)
        v                                 v
        O' = Z/mpZ -------- g=(mod n) --> O = Z/nZ

    Requires ``n | m`` and ``n | mp``.  ``S'`` is built as the genuine fiber
    product ``{(x, y) ∈ Z/mZ × Z/mpZ : x ≡ y (mod n)}`` with the two projections,
    so the square is cartesian by construction; :func:`is_cartesian` re-certifies
    it.  Elements of ``S'`` are the pairs ``(x, y)`` themselves.
    """
    if m % n != 0 or mp % n != 0:
        raise BeckChevalleyError("clock square requires n | m and n | mp")
    S = cyclic_carrier(m)
    O = cyclic_carrier(n)
    Op = cyclic_carrier(mp)
    q = clock_reduction(m, n)
    g = clock_reduction(mp, n)
    Sp = tuple((x, y) for x in S for y in Op if x % n == y % n)
    g_prime = finite_map(Sp, S, lambda xy: xy[0])
    q_prime = finite_map(Sp, Op, lambda xy: xy[1])
    return Square(S, Sp, O, Op, q, g, g_prime, q_prime,
                  source_id=f"declared-clock(Z{m}->Z{n}<-Z{mp})")


def witness_transport(square: Square, F: frozenset, o_prime: Element):
    """Explicit Beck–Chevalley witness transport at a point ``o' ∈ O'``.

    Returns ``(left_witness, right_witness)`` where

    * ``left_witness`` is the least ``s ∈ F`` with ``q(s) = g(o')`` certifying
      ``o' ∈ g*(∃_q F)`` (or ``None`` if ``o'`` is not in the LHS);
    * ``right_witness`` is the least ``s' ∈ S'`` with ``g'(s') = s`` and
      ``q'(s') = o'`` certifying ``o' ∈ ∃_{q'}(g'* F)``.

    For a cartesian square the transport never fails: the pair ``(s, o')`` lies
    in the fiber product and so has a (unique, here) preimage ``s'`` under ``φ``.
    """
    F = predicate(square.S, F)
    if o_prime not in square.O_prime:
        raise BeckChevalleyError("o' must be an element of O'")
    target = square.g.apply(o_prime)
    left = next((s for s in square.S if s in F and square.q.apply(s) == target), None)
    if left is None:
        return None, None
    right = next(
        (s for s in square.S_prime
         if square.g_prime.apply(s) == left and square.q_prime.apply(s) == o_prime),
        None,
    )
    return left, right


# --------------------------------------------------------------------------- #
# Canonical firewall exhibit (new-to-project SYNTHESIS).
# --------------------------------------------------------------------------- #
def firewall_square() -> tuple:
    """A small square where FORMAL Beck–Chevalley holds but a source-realization
    certificate is BROKEN.

    Construction (total 4 elements, all carriers inhabited)::

        O  = (o0,)                 g : p0 ↦ o0
        O' = (p0,)                 q : s0, s1 ↦ o0
        S  = (s0, s1)              g': t0 ↦ s0
        S' = (t0,)                 q': t0 ↦ p0
        F  = {s0, s1}

    * The square commutes but is NOT cartesian: the fiber product is
      ``{(s0,p0), (s1,p0)}`` (2 elements) yet ``S'`` has 1 element.
    * FORMAL Beck–Chevalley HOLDS: both sides equal ``{p0}``.
    * The fiber witness ``(s1, p0)`` (with ``s1 ∈ F``, ``q(s1)=o0=g(p0)``) is a
      legitimate formal existential witness that NO element of the source
      carrier ``S'`` realizes — the ghost witness.  ``realize_right`` certifies
      ``p0`` only through ``t0`` (over ``s0``); ``s1`` has no preimage.

    Returns ``(square, F)``.
    """
    O = ("o0",)
    Op = ("p0",)
    S = ("s0", "s1")
    Sp = ("t0",)
    q = finite_map(S, O, {"s0": "o0", "s1": "o0"})
    g = finite_map(Op, O, {"p0": "o0"})
    g_prime = finite_map(Sp, S, {"t0": "s0"})
    q_prime = finite_map(Sp, Op, {"t0": "p0"})
    square = Square(S, Sp, O, Op, q, g, g_prime, q_prime,
                    source_id="declared-firewall-source")
    F = predicate(S, {"s0", "s1"})
    return square, F


def realization_faithful_noncartesian_square() -> Square:
    """A NON-cartesian square on which the FORMAL Beck–Chevalley equality holds
    for every predicate AND every formal fiber witness is source-realized.

    Construction (the "redundant realizer" square)::

        O  = (o0,)                 q : s0 ↦ o0
        O' = (p0,)                 g : p0 ↦ o0
        S  = (s0,)                 g': t0, t1 ↦ s0
        S' = (t0, t1)              q': t0, t1 ↦ p0

    The fiber product is the single pair ``{(s0, p0)}`` but ``S'`` has TWO
    elements both mapping onto it, so the comparison map ``φ`` is surjective yet
    NOT injective — the square is not a pullback.  Nonetheless:

    * ``beck_chevalley_holds_all`` is True (the extra realizer does not change
      any image), and
    * ``realization_firewall_breaks`` is False for every ``F`` (every formal
      witness ``(s0, p0)`` is backed by an actual ``S'``-element — in fact by
      two of them).

    This is the exact receipt that the *realization-faithful Beck–Chevalley*
    class is STRICTLY LARGER than the cartesian class: faithfulness forbids
    GHOST (unrealized) witnesses but tolerates REDUNDANT (over-realized) ones,
    whereas cartesianness forbids both.  See
    ``research/2026-10-19/BECK_CHEVALLEY_SOURCE.md`` §8.
    """
    O = ("o0",)
    Op = ("p0",)
    S = ("s0",)
    Sp = ("t0", "t1")
    q = finite_map(S, O, {"s0": "o0"})
    g = finite_map(Op, O, {"p0": "o0"})
    g_prime = finite_map(Sp, S, {"t0": "s0", "t1": "s0"})
    q_prime = finite_map(Sp, Op, {"t0": "p0", "t1": "p0"})
    return Square(S, Sp, O, Op, q, g, g_prime, q_prime,
                  source_id="declared-redundant-realizer-source")
