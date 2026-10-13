"""Lawful (partial-availability) realization: ghost freedom and the operational profile.

Part II of the positive carrier dossier, availability layer.  The inherited
Part I (``carrier_realization.py``) defined, for a lawful carrier K with
enabled sets E_a,

    d+_bot(K)  = positive dimension of the BOTTOM-COMPLETED behavior p_bot
                 (refusal mass = mass of the current law outside E_a; the
                 outcomes z != bot of an unavailable action keep the "partial
                 execution" values M_{a,z} (law restricted to E_a)),
    d+_law(K)  = min |C'| over lawful carriers with the same legal values and
                 the same legality pattern (menus),

and proved d+_law <= d+_bot, leaving strictness open and calling the bottom
completion the weakest repair.  This module settles both:

* ``OperationalProfile``: the legal data proper -- legal histories, their
  values p_sigma(u), and the menu after each -- the invariant that
  public-history policies, closed-loop laws and source posteriors depend on
  (Part I Theorem 8.2).  The values p_bot(u a z) for an UNAVAILABLE a are
  GHOSTS: no legal experiment measures them.

* ``support_uniform_completion``: the refusal completion p~ of a profile
  ("if any supported state refuses, the whole experiment refuses") is always
  realized by the finite carrier with states (c, S), S = support of the
  current law.  Two lawful carriers have the same operational profile iff
  their support-uniform completions are behaviorally equivalent, which
  ``profile_equivalence_certificate`` decides EXACTLY (Part I's difference
  realization); a distinguishing word is a legal experiment or a menu
  difference, never a ghost.

* ``ghost freedom`` (Theorem II.5):  d+_law(Pi) = min over lawful completions
  p' of Pi of d+(p'), and p_bot(K) is one completion among many.

* ``ghost gap`` (Theorem II.6):  the phantom path walks PH_n have
  d+_law = 1 (one source) or 2 (two sources, one of which can execute the
  phantom action legally) while every carrier of their bottom completion
  needs >= 4^n + 1 states (fooling set on the ghost block).  So the bottom
  completion is the CANONICAL repair determined by K, not the weakest one;
  the weakest is: realize the operational profile.

* ``public_menu``: the menu a public-history controller is allowed to use is
  the intersection over sources compatible with the history (prior * p > 0);
  offering more would turn the menu into a hidden-source sensor.

* ``simplicial_grid_search``: a sound (LP-verified) search for invariant
  simplicial cones with slice vertices on a rational grid, for the oracle's
  blind spot: Part II Example II.7 (a diagonal contraction) has d+ = r = 3
  although its reachable cone has infinitely many extreme rays, so the
  reachable-ray refinement of Part I can never find the carrier.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Hashable, Sequence

from .carrier_indexed import rat
from .carrier_realization import (
    BOT, ConeCertificate, LinearRealization, LinearSystem, Mat, PositiveCarrier,
    RealizationError, Vec, Word, calibration_matrix, carrier_from_cone,
    cone_coordinates, dot, equivalence_certificate, fooling_set_lower_bound,
    hankel_block, identity, mat, matvec, minimal_realization, observed_chain_events,
    permutation_event, rank, verify_cone,
)


# --------------------------------------------------------------------------
# operational profile
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class OperationalProfile:
    """Legal histories to a depth, with values and menus.  ``entries`` maps
    (source, word) -> (p_sigma(word), menu tuple).  Finite truncation of an
    infinite object; exact equality of full profiles is decided by
    ``profile_equivalence_certificate``."""
    depth: int
    entries: dict[tuple[Hashable, Word], tuple[Q, tuple[str, ...]]]

    def menus(self) -> set[tuple[str, ...]]:
        return {m for _, m in self.entries.values()}


def operational_profile(carrier: PositiveCarrier, depth: int) -> OperationalProfile:
    entries: dict[tuple[Hashable, Word], tuple[Q, tuple[str, ...]]] = {}
    for s in carrier.preparations:
        frontier: list[Word] = [()]
        for _ in range(depth + 1):
            nxt: list[Word] = []
            for u in frontier:
                p = carrier.probability(s, u)
                if p == 0 or not carrier.legal(s, u):
                    continue
                menu = tuple(a for a in carrier.actions if carrier.available(s, u, a))
                entries[(s, u)] = (p, menu)
                for a in menu:
                    for z in carrier.outcomes(a):
                        nxt.append(u + ((a, z),))
            frontier = nxt
    return OperationalProfile(depth, entries)


def public_menu(carrier: PositiveCarrier, prior: dict[Hashable, Q], word: Word
                ) -> tuple[str, ...] | None:
    """Actions available after ``word`` for EVERY source compatible with it
    (prior * p_sigma(word) > 0).  None if no source is compatible.  A
    public-history controller may only use this menu."""
    compatible = [s for s in prior if rat(prior[s]) > 0 and carrier.probability(s, word) > 0
                  and carrier.legal(s, word)]
    if not compatible:
        return None
    return tuple(a for a in carrier.actions
                 if all(carrier.available(s, word, a) for s in compatible))


# --------------------------------------------------------------------------
# support-uniform (refusal) completion: an exact decision for profile equality
# --------------------------------------------------------------------------

def support_uniform_completion(carrier: PositiveCarrier) -> PositiveCarrier:
    """Total carrier on states (c, S) (S = support of the current law)
    realizing the refusal completion p~: a legal word has its usual value, an
    unavailable action refuses with probability ONE (outcome BOT, state kept),
    and after a refusal everything is as before.  Only legally reachable
    (c, S) pairs are kept.  Size <= |C| 2^|C|; in practice much smaller."""
    n = carrier.dimension
    # explore reachable supports
    supports: list[frozenset[int]] = []
    seen: set[frozenset[int]] = set()
    for v in carrier.preparations.values():
        S = frozenset(c for c in range(n) if v[c] > 0)
        if S not in seen:
            seen.add(S)
            supports.append(S)
    idx = 0
    succ: dict[tuple[frozenset[int], str, Hashable], frozenset[int]] = {}
    while idx < len(supports):
        S = supports[idx]
        idx += 1
        for a in carrier.actions:
            if not all(carrier.enabled[a][c] for c in S):
                continue
            for z in carrier.outcomes(a):
                M = carrier.events[a][z]
                Sp = frozenset(cp for cp in range(n) if any(M[cp][c] > 0 for c in S))
                if not Sp:
                    continue
                succ[(S, a, z)] = Sp
                if Sp not in seen:
                    seen.add(Sp)
                    supports.append(Sp)
    states = [(c, S) for S in supports for c in sorted(S)]
    pos = {st: i for i, st in enumerate(states)}
    m = len(states)
    events: dict[str, dict[Hashable, list[list[Q]]]] = {}
    for a in carrier.actions:
        blk = {z: [[Q(0)] * m for _ in range(m)] for z in carrier.outcomes(a)}
        blk[BOT] = [[Q(0)] * m for _ in range(m)]
        for (c, S) in states:
            j = pos[(c, S)]
            if all(carrier.enabled[a][cc] for cc in S):
                for z in carrier.outcomes(a):
                    M = carrier.events[a][z]
                    Sp = succ.get((S, a, z))
                    if Sp is None:
                        continue
                    for cp in range(n):
                        if M[cp][c] > 0:
                            blk[z][pos[(cp, Sp)]][j] += M[cp][c]
            else:
                blk[BOT][j][j] = Q(1)
        events[a] = {z: tuple(tuple(r) for r in rows) for z, rows in blk.items()
                     if z != BOT or any(x != 0 for r in rows for x in r)}
    preps = {}
    for s, v in carrier.preparations.items():
        S = frozenset(c for c in range(n) if v[c] > 0)
        p = [Q(0)] * m
        for c in S:
            p[pos[(c, S)]] = v[c]
        preps[s] = tuple(p)
    return PositiveCarrier(tuple(states), events, preps, {})


def profile_equivalence_certificate(k1: PositiveCarrier, k2: PositiveCarrier) -> dict:
    """Exact decision: do two lawful carriers have the same operational
    profile (legal values and menus after every legal history, all sources)?
    Equivalent to behavioral equivalence of the support-uniform completions.
    A negative answer returns a distinguishing (source, word): either a legal
    word with different values, or a word ending in BOT, i.e. a menu
    difference.  Ghost values never appear."""
    c1 = support_uniform_completion(k1)
    c2 = support_uniform_completion(k2)
    eq = equivalence_certificate(c1, c2)
    out = {"same_operational_profile": eq["equivalent"], "refusal_completion_sizes": (c1.dimension, c2.dimension)}
    if not eq["equivalent"]:
        w = eq["word"]
        s = eq["source"]
        legal1 = k1.legal(s, w) and k1.probability(s, w) > 0
        legal2 = k2.legal(s, w) and k2.probability(s, w) > 0
        out.update({"source": s, "word": w, "p1": eq["p1"], "p2": eq["p2"],
                    "legal_in_first": legal1, "legal_in_second": legal2,
                    "kind": "legal_value_difference" if (legal1 and legal2) else "menu_difference"})
    return out


# --------------------------------------------------------------------------
# ghost gap: the phantom path walks
# --------------------------------------------------------------------------

def phantom_walk_carrier(copies: int = 1, *, legal_source: bool = False) -> PositiveCarrier:
    """PH_n: a ghost copy of the path walk PW_n hidden behind a disabled state.

    States: g (ghost anchor; h if ``legal_source``) + the 4^n walk states.
    Action 'a' (step and report the position tuple) is enabled on the walk
    states only (and on h); action 'b' (silent swap on every coordinate,
    identity on g/h) is total.  Source 'sigma' = 1/2 on g + 1/2 uniform on
    the walk: g is always in the support, so 'a' is NEVER available at
    sigma -- its outcome values are ghosts.  With ``legal_source`` a second
    source 'eta' = delta_h makes 'a' legal somewhere (it then reports a fixed
    tuple and keeps h).

    Facts (Theorem II.6): d+_law = 1 (resp. 2); the bottom completion needs
    >= 4^n + 1 states (fooling set of size 4^n on the ghost one-step block,
    plus a state carrying the refusal mass)."""
    if copies < 1:
        raise RealizationError("copies >= 1")
    P = calibration_matrix()
    walk = observed_chain_events(P)
    swap = permutation_event((1, 0, 3, 2))
    # tensor power of the walk
    def kron(a: Mat, b: Mat) -> Mat:
        return tuple(tuple(x * y for x in ra for y in rb) for ra in a for rb in b)
    w_events: dict[Hashable, Mat] = {(z,): M for z, M in walk.items()}
    sw = swap
    for _ in range(copies - 1):
        w_events = {z1 + (z2,): kron(M1, M2) for z1, M1 in w_events.items() for z2, M2 in walk.items()}
        sw = kron(sw, swap)
    k = 4 ** copies
    extra = 2 if legal_source else 1
    n = extra + k

    def emb(M: Mat, corner: Sequence[tuple[int, int, Q]]) -> Mat:
        out = [[Q(0)] * n for _ in range(n)]
        for (i, j, v) in corner:
            out[i][j] = v
        for i in range(k):
            for j in range(k):
                out[extra + i][extra + j] = M[i][j]
        return tuple(tuple(r) for r in out)

    zero = tuple(tuple(Q(0) for _ in range(k)) for _ in range(k))
    events: dict[str, dict[Hashable, Mat]] = {"a": {}, "b": {}}
    fixed = tuple(0 for _ in range(copies))
    for z, M in w_events.items():
        corner = [(1, 1, Q(1))] if (legal_source and z == fixed) else []
        events["a"][z] = emb(M, corner)
    corner_b = [(0, 0, Q(1))] + ([(1, 1, Q(1))] if legal_source else [])
    events["b"]["o"] = emb(sw, corner_b)
    enabled = {"a": tuple([False] + ([True] if legal_source else []) + [True] * k)}
    preps: dict[Hashable, Vec] = {
        "sigma": tuple([Q(1, 2)] + ([Q(0)] if legal_source else []) + [Q(1, 2 * k)] * k)}
    if legal_source:
        preps["eta"] = tuple([Q(0), Q(1)] + [Q(0)] * k)
    states = tuple(["g"] + (["h"] if legal_source else []) + list(range(k)))
    return PositiveCarrier(states, events, preps, enabled)


def minimal_lawful_phantom(copies: int = 1, *, legal_source: bool = False) -> PositiveCarrier:
    """The lawful carrier of PH_n's operational profile with d+_law states:
    one state (a disabled, b total) or two states (h with a enabled and
    fixed report, g with a disabled)."""
    fixed = tuple(0 for _ in range(copies))
    if not legal_source:
        return PositiveCarrier((0,), {"a": {fixed: ((Q(0),),)}, "b": {"o": ((Q(1),),)}},
                               {"sigma": (1,)}, {"a": (False,)})
    one = Q(1)
    return PositiveCarrier(("g", "h"),
                           {"a": {fixed: mat([[0, 0], [0, one]])}, "b": {"o": identity(2)}},
                           {"sigma": (1, 0), "eta": (0, 1)}, {"a": (False, True)})


def ghost_block_certificate(carrier: PositiveCarrier, source: Hashable, action: str
                            ) -> dict:
    """Lower bound on d+_bot from the ghost one-step block: rows (source,
    (a,z)), columns (a,z').  Any carrier of the bottom completion factors the
    block nonnegatively through its a-live states; if moreover
    p_sigma(a BOT) > 0 then a further state (positive refusal mass) is needed:
    d+_bot >= fooling + 1."""
    zs = list(carrier.outcomes(action))
    rows = [(source, ((action, z),)) for z in zs]
    cols = [((action, z),) for z in zs]
    H = hankel_block(carrier, rows, cols)
    size, cells = fooling_set_lower_bound(H, exhaustive_limit=6)
    refusal = carrier.probability(source, ((action, BOT),))
    return {"ghost_block": H, "block_rank": rank(H), "fooling_set": cells, "fooling_size": size,
            "refusal_mass": refusal,
            "action_available_at_source": carrier.available(source, (), action),
            "bottom_completion_lower_bound": size + (1 if refusal > 0 else 0)}


# --------------------------------------------------------------------------
# simplicial grid search (sound, never "impossible")
# --------------------------------------------------------------------------

def slice_parametrization(realization: LinearRealization) -> tuple[Vec, tuple[Vec, ...]]:
    """x0 with tau(x0) = 1 and a rational basis k_1..k_{r-1} of ker tau."""
    tau = realization.mass
    r = realization.dimension
    i0 = next((i for i, t in enumerate(tau) if t != 0), None)
    if i0 is None:
        raise RealizationError("zero mass functional")
    x0 = tuple(Q(int(i == i0)) / tau[i0] for i in range(r))
    ks = []
    for j in range(r):
        if j == i0:
            continue
        k = [Q(0)] * r
        k[j] = Q(1)
        k[i0] = -tau[j] / tau[i0]
        ks.append(tuple(k))
    return x0, tuple(ks)


def simplicial_grid_search(realization: LinearRealization, *, system: LinearSystem | None = None,
                           denominators: Sequence[int] = (1, 2), bound: int = 2,
                           max_candidates: int = 200000) -> dict:
    """Search simplicial cones (r generators) whose slice vertices lie on the
    grid {x0 + sum t_i k_i : t_i = p/q, |p| <= bound*q, q in denominators}.
    The grid lives in the realization's coordinates, or -- when ``system`` is
    given -- in the ambient coordinates of that system (its own mass
    functional), mapped into the realization through the reachable basis.
    Each candidate is verified EXACTLY by ``verify_cone``; a hit yields a
    carrier with r = linear dimension states (no gap).  Exhausting the grid is
    reported as UNRESOLVED -- it is not an impossibility proof."""
    from .carrier_realization import solve_in_span
    r = realization.dimension
    if system is None:
        x0, ks = slice_parametrization(realization)
        to_coords = lambda x: x  # noqa: E731
        dim = r
    else:
        amb = LinearRealization(system.dimension, {}, {}, system.mass, (), (), (), (), {})
        x0, ks = slice_parametrization(amb)
        to_coords = lambda x: solve_in_span(realization.basis, x)  # noqa: E731
        dim = system.dimension
    tried = 0
    seen: set[tuple[Vec, ...]] = set()
    for q in denominators:  # coarse grids first
        vals = sorted({Q(p, q) for p in range(-bound * q, bound * q + 1)})
        points = []
        for ts in itertools.product(vals, repeat=dim - 1):
            x = list(x0)
            for t, k in zip(ts, ks):
                x = [a + t * b for a, b in zip(x, k)]
            c = to_coords(tuple(x))
            if c is not None and tuple(c) not in points:
                points.append(tuple(c))
        for combo in itertools.combinations(points, r):
            if combo in seen:
                continue
            seen.add(combo)
            tried += 1
            if tried > max_candidates:
                return {"verdict": "UNRESOLVED", "reason": "candidate budget exhausted", "tried": tried - 1}
            gens = list(combo)
            # cheap necessary filter: every source inside the candidate simplex
            if any(cone_coordinates(gens, v) is None for v in realization.vectors.values()):
                continue
            cert = verify_cone(realization, gens)
            if cert.valid:
                return {"verdict": "LAWFUL_REALIZATION", "generators": tuple(gens), "certificate": cert,
                        "tried": tried, "denominator": q}
    return {"verdict": "UNRESOLVED", "reason": "grid exhausted (not an impossibility proof)", "tried": tried}


# --------------------------------------------------------------------------
# Example II.7: the diagonal contraction (non-polyhedral reachable cone, d+ = r)
# --------------------------------------------------------------------------

def diagonal_contraction_system() -> LinearSystem:
    """V = Q^3, T_tick = diag(1/2, 1/4, 1/8), tau = (1, 1/8, 1/8), v_* prop. (1,1,1),
    reset = v_* (tau - tau T_tick), silent b = v_* tau, sources s0 = (1,0,0), s_*.
    The reachable rays from s_* are (1, 2^-n, 4^-n): slice points (x, x^2) on a
    strictly convex curve, so the closed reachable cone has infinitely many
    extreme rays and the reachable-ray refinement never terminates with a
    carrier; yet the triangle with slice vertices (1,1), (-2,1), (1,-2) is an
    invariant sandwiched simplicial cone: d+ = r = 3."""
    Td = mat([[Q(1, 2), 0, 0], [0, Q(1, 4), 0], [0, 0, Q(1, 8)]])
    tau = (Q(1), Q(1, 8), Q(1, 8))
    vs = (Q(1), Q(1), Q(1))
    t = dot(tau, vs)
    vs = tuple(x / t for x in vs)
    resid = tuple(x - y for x, y in zip(tau, tuple(sum((tau[i] * Td[i][j] for i in range(3)), Q(0)) for j in range(3))))
    Tr = tuple(tuple(vs[i] * resid[j] for j in range(3)) for i in range(3))
    Tb = tuple(tuple(vs[i] * tau[j] for j in range(3)) for i in range(3))
    return LinearSystem(3, {"clock": {"tick": Td, "reset": Tr}, "b": {"ok": Tb}},
                        {"s0": (Q(1), Q(0), Q(0)), "sstar": vs}, tau)


def diagonal_triangle_generators(realization: LinearRealization) -> tuple[Vec, ...]:
    """The three ambient slice vertices (1,1), (-2,1), (1,-2), tau-normalized
    and expressed in the realization's coordinates."""
    from .carrier_realization import solve_in_span
    tau_amb = (Q(1), Q(1, 8), Q(1, 8))
    gens = []
    for (x, y) in [(1, 1), (-2, 1), (1, -2)]:
        g = (Q(1), Q(x), Q(y))
        g = tuple(c / dot(tau_amb, g) for c in g)
        c = solve_in_span(realization.basis, g)
        if c is None:
            raise RealizationError("vertex outside the realization span")
        gens.append(tuple(c))
    return tuple(gens)


# --------------------------------------------------------------------------
# the Part II oracle: Part I verdicts + grid search + rationality routes
# --------------------------------------------------------------------------

def carrier_realization_oracle_ii(system: "LinearSystem | PositiveCarrier", *,
                                  proposed_dimension: int | None = None,
                                  grid_denominators: Sequence[int] = (1, 2),
                                  grid_bound: int = 2, grid_budget: int = 20000,
                                  contact_words: Sequence[Word] | None = None,
                                  **part_i_kwargs) -> dict:
    """Composition of the Part I oracle with the Part II routes.

    1. Part I (``carrier_realization_oracle``): minimal realization, support
       and spectral lower bounds, reachable-ray refinement (round-bounded).
    2. If unresolved: the simplicial grid search in ambient coordinates
       (finds d+ = r carriers whose reachable cone is not polyhedral,
       Example II.7) and, for r = 2, the rational-interval search.
    3. If still unresolved and r = 2: the irrational-contact certificate over
       all ordered pairs of ``contact_words`` (default: the single-event
       words).  A hit is FINITE_OBSTRUCTION *over Q* with the explicit note
       that a 2-state carrier exists over the quadratic field (Theorem II.3);
       the verdict carries ``field = 'Q'`` so that it is never read as a
       real impossibility.
    Every verdict is sound; UNRESOLVED carries no claim.
    """
    from .carrier_field_of_definition import (rational_interval_search,
                                              two_dimensional_contact_certificate)
    from .carrier_realization import carrier_realization_oracle
    amb = system if isinstance(system, LinearSystem) else LinearSystem.of_carrier(system)
    report = carrier_realization_oracle(system, proposed_dimension=proposed_dimension, **part_i_kwargs)
    report["part_ii"] = {}
    if report["verdict"] != "UNRESOLVED":
        return report
    R = minimal_realization(amb)
    lower = report.get("positive_dimension_lower_bound", R.dimension)
    if proposed_dimension is None or proposed_dimension >= R.dimension:
        grid = simplicial_grid_search(R, system=amb, denominators=grid_denominators, bound=grid_bound,
                                      max_candidates=grid_budget)
        report["part_ii"]["grid_search"] = {k: v for k, v in grid.items() if k not in ("certificate",)}
        if grid["verdict"] == "LAWFUL_REALIZATION":
            carrier = carrier_from_cone(grid["certificate"])
            eq = equivalence_certificate(amb, carrier)
            if not eq["equivalent"]:
                raise RealizationError("Internal: grid carrier is not equivalent")
            report.update({"verdict": "LAWFUL_REALIZATION", "carrier": carrier,
                           "carrier_dimension": carrier.dimension, "equivalence": eq,
                           "reason": "simplicial grid search (Part II)"})
            if proposed_dimension is not None and carrier.dimension > proposed_dimension:
                report["verdict"] = "UNRESOLVED"
                report["reason"] = (f"a {carrier.dimension}-state carrier exists; the proposed dimension "
                                    f"{proposed_dimension} is between the lower bound {lower} and that")
            return report
    if R.dimension == 2:
        interval = rational_interval_search(R, denominators=tuple(range(1, 7)), bound=3)
        report["part_ii"]["rational_interval_search"] = {k: v for k, v in interval.items() if k != "certificate"}
        if interval["verdict"] == "LAWFUL_REALIZATION":
            carrier = carrier_from_cone(interval["certificate"])
            eq = equivalence_certificate(amb, carrier)
            if not eq["equivalent"]:
                raise RealizationError("Internal: interval carrier is not equivalent")
            report.update({"verdict": "LAWFUL_REALIZATION", "carrier": carrier, "carrier_dimension": 2,
                           "equivalence": eq, "reason": "rational interval search (Part II)"})
            return report
        words = list(contact_words) if contact_words is not None else [
            ((a, z),) for a in amb.actions for z in amb.outcomes(a)]
        for w1 in words:
            for w2 in words:
                if w1 == w2:
                    continue
                cert = two_dimensional_contact_certificate(amb, w1, w2)
                if cert["verdict"] == "FINITE_OBSTRUCTION":
                    report["part_ii"]["irrational_contact"] = cert
                    report.update({"verdict": "FINITE_OBSTRUCTION", "field": "Q",
                                   "positive_dimension_over_R": 2,
                                   "positive_dimension_over_Q": "infinity",
                                   "reason": ("no rational positive carrier of any size (irrational contact); "
                                              "a 2-state carrier exists over " + cert["field"])})
                    return report
    report["reason"] = report.get("reason", "") + "; Part II routes exhausted (no claim)"
    return report
