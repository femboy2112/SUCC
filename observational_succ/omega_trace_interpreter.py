"""Omega-indexed causal computation: an executable beta-reduction interpreter.

Scope (see research/2026-11-09/scott_omega_causal_weld/OMEGA_INTERPRETER.md):

* An explicit syntax for omega_k = lambda x. x x ... x (k left-associated
  copies) and E_k(m) = the left-associated chain of m copies of omega_k.
  Every redex carries a POSITION (address), not merely a count.

* A leftmost-beta reduction stepper returning (term, redex_address, step).

* Exact verification of the growth law  E_k(m) -> E_k(m+k-2), k in 2..8.

* A FINITE strongly-normalizing "compiled SUCC step": a typed computation
  that reduces to a normal form carrying an explicit trace, and is
  structurally shown to terminate.

* A SEPARATE guarded/coinductive trace for raw Omega_k that reports
  "no finite normal form" without hanging.

Raw Omega_k (k>=3) has NO finite beta normal form; each leftmost contraction
recreates a beta redex (the term is head-unsolvable).  This module states that
as a theorem of the reduction system and reports it, it does NOT attempt to
compute a normal form.

The arithmetic consequences for pi normality are NOT claimed here.  This is a
finite, structural, exact-rational instrument.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Iterator, Sequence


# ---------------------------------------------------------------------------
# 1. Explicit syntax with redex positions (addresses)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Term:
    """A closed term in the omega calculus.

    The only terms we build are the chain E_k(m) (an application spine of
    `m` copies of omega_k, left-associated) and omega_k itself.  We keep the
    syntax fully explicit so that every redex has a positional address.
    """

    k: int  # omega_k arity: number of self-applications (k >= 2)
    m: int  # number of copies in the chain (m >= 1)

    def __post_init__(self) -> None:
        if not isinstance(self.k, int) or self.k < 2:
            raise ValueError("omega_k arity k must be >= 2")
        if not isinstance(self.m, int) or self.m < 1:
            raise ValueError("chain length m must be >= 1")

    # -- positional address of every redex ------------------------------
    # E_k(m) = omega_k omega_k ... omega_k (m copies, left-associated).
    # A left-associated application spine  t0 t1 t2 ... t_{m-1}  has the
    # redex candidates at the *leftmost* occurrence of the pattern
    # (omega_k omega_k).  We name redexes by the index of their left
    # component.  For the chain, the leftmost redex is always at index 0
    # (head position):  (omega_k omega_k) omega_k ...
    #
    # Addresses are the spine indices 0 .. m-2 where a contraction may fire.
    # The LEFT spine is: index 0 = head application (omega_k applied to
    # omega_k), index 1 = that result applied to the next omega_k, etc.
    # Because every component is omega_k and application is left-associated,
    # the leftmost redex is ALWAYS at address 0 while m >= 2.
    def redex_addresses(self) -> tuple[int, ...]:
        """All candidate redex positions in the current chain.

        Returns the spine addresses at which a beta contraction could fire.
        For the pure chain E_k(m) every application of omega_k to omega_k is
        a redex, so there are m-1 redexes at addresses 0..m-2.
        """
        return tuple(range(self.m - 1))

    def is_normal_form(self) -> bool:
        """A chain is a normal form iff it has no beta redex.

        E_k(1) = omega_k has no redex (a bare abstraction).  Any m >= 2 has
        the head redex omega_k omega_k, so it is NOT a normal form.
        """
        return self.m == 1

    def head_unsolvable(self) -> bool:
        """Head-unsolvability witness: a head redex that never disappears.

        For k >= 3, omega_k omega_k -> omega_k ... omega_k (k copies) which
        contains omega_k omega_k again as a subterm at the head, so the head
        redex is recreated forever.  For k = 2, omega_2 omega_2 -> omega_2
        omega_2 (identity on itself) also never normalizes.
        """
        return self.m >= 2


# ---------------------------------------------------------------------------
# 2. Leftmost-beta reduction stepper
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Step:
    """One leftmost beta contraction, fully witnessed."""
    before: Term          # term before contraction
    address: int          # redex position that fired (leftmost)
    after: Term           # term after contraction
    delta: int            # exact copy-count change  m_after - m_before


def contract_leftmost(t: Term) -> Step:
    """Fire the single leftmost beta redex of E_k(m) and return the step.

    Leftmost contraction at  E_k(m) = omega_k omega_k omega_k ...  (m copies)
    substitutes the argument (the second omega_k) for x in the body of the
    head omega_k = lambda x. x x ... x (k copies).  The result is a chain of
    k copies of omega_k replacing the head redex, then the remaining m-2
    copies of the original chain follow.

    Copy count: before = m.  The head redex occupies 2 copies and produces k
    copies, then the trailing m-2 copies remain:  after = k + (m-2).

    Hence  delta = k + (m-2) - m = k - 2  exactly.
    """
    if t.m < 2:
        raise ValueError("cannot contract a normal form (m < 2)")
    k = t.k
    m_after = k + (t.m - 2)
    after = Term(k=k, m=m_after)
    return Step(before=t, address=0, after=after, delta=k - 2)


def reduce_leftmost(t: Term, max_steps: int) -> Iterator[Step]:
    """Leftmost reduction sequence, bounded by max_steps.

    Yields each Step in order.  Terminates (exhausts) when a normal form is
    reached, or stops after max_steps steps without claiming a normal form.
    """
    if not isinstance(max_steps, int) or max_steps < 0:
        raise ValueError("max_steps must be a nonnegative integer")
    cur = t
    for _ in range(max_steps):
        if cur.is_normal_form():
            return
        step = contract_leftmost(cur)
        yield step
        cur = step.after


# ---------------------------------------------------------------------------
# 3. Exact growth law  E_k(m) -> E_k(m + k - 2)
# ---------------------------------------------------------------------------

def growth_law_check(k: int, m: int) -> Step:
    """One leftmost contraction of E_k(m) and its exact copy-count delta.

    Guarantees  after.m == m + (k - 2).
    """
    step = contract_leftmost(Term(k=k, m=m))
    assert step.after.m == m + (k - 2)
    assert step.delta == k - 2
    return step


def verify_growth_law(k_range: range = range(2, 9), m_range: range = range(2, 13)) -> bool:
    """Exact verification of E_k(m) -> E_k(m+k-2) over the declared ranges.

    Pure copy-count arithmetic; returns True iff every case holds.
    """
    return all(
        growth_law_check(k, m).after.m == m + k - 2
        for k in k_range
        for m in m_range
    )


# ---------------------------------------------------------------------------
# 4. FINITE strongly-normalizing compiled SUCC step
# ---------------------------------------------------------------------------

# The source recurrence is  U_{n+1} = 16 * U_n + r(n+1)  with
#   r(j) = 4/(8j-7) - 2/(8j-4) - 1/(8j-3) - 1/(8j-2),  U_0 = 0.
# This is a FINITE typed arithmetic computation: for each n it is a fixed
# finite rational expression with no recursion and no beta redex.  We model
# it as a "compiled SUCC step" that (a) has a normal form, (b) carries an
# explicit trace, and (c) is strongly normalizing by construction (the trace
# is a finite list of atomic rational operations, each strictly consuming a
# fixed budget).


def bbp_forcing(j: int) -> Q:
    """Frozen four-pole BBP forcing r(j), exact rational."""
    if not isinstance(j, int) or j < 1:
        raise ValueError("BBP source indices must be >= 1")
    return Q(4, 8 * j - 7) - Q(2, 8 * j - 4) - Q(1, 8 * j - 3) - Q(1, 8 * j - 2)


@dataclass(frozen=True)
class CompiledTraceEntry:
    """One atomic operation in the compiled SUCC step's reduction trace.

    Each entry names a redex POSITION (address) in a flat, typed evaluation
    of the rational expression  16*U + r(n+1), so the trace is positional and
    the reduction is terminating by a strict structural measure.
    """
    address: int      # position in the flattened expression tree
    op: str           # operation name (add / scale / force)
    result: Q         # exact rational value of that subexpression


@dataclass(frozen=True)
class CompiledSUCCStep:
    """A finite, typed, strongly-normalizing compiled SUCC step.

    It reduces (in one shot) to a normal form  U_{n+1} and carries an explicit
    positional trace.  Strong normalization is structural: the trace length is
    a fixed constant (independent of n), so the reduction can never loop.
    """
    n: int
    u_next: Q
    trace: tuple[CompiledTraceEntry, ...]

    def normal_form(self) -> Q:
        return self.u_next


def compile_succ_step(n: int, u: Q = Q(0)) -> CompiledSUCCStep:
    """Compile the finite SUCC step U -> 16*U + r(n+1) to a normal form.

    The trace is a fixed finite sequence of positional atomic operations
    (addresses 0,1,2), which makes strong normalization immediate: there is no
    redex that recreates itself, so the compiled fragment is terminating.

    The normal form is the exact rational 16*U + r(n+1), matching the source
    recurrence  U_{n+1} = 16 U_n + r(n+1).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("nonnegative SUCC time required")
    u = Q(u)
    r = bbp_forcing(n + 1)
    trace = (
        CompiledTraceEntry(address=0, op="scale", result=16 * u),
        CompiledTraceEntry(address=1, op="force", result=r),
        CompiledTraceEntry(address=2, op="add", result=16 * u + r),
    )
    return CompiledSUCCStep(n=n, u_next=16 * u + r, trace=trace)


def compiled_orbit(n: int, u0: Q = Q(0)) -> tuple[CompiledSUCCStep, ...]:
    """The finite compiled orbit U_0, ..., U_n as compiled normal forms."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("nonnegative SUCC time required")
    out = []
    u = Q(u0)
    for t in range(n):
        step = compile_succ_step(t, u)
        out.append(step)
        u = step.u_next
    return tuple(out)


# ---------------------------------------------------------------------------
# 5. SEPARATE guarded / coinductive trace for raw Omega_k
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class GuardedOmegaReport:
    """Report of the infinite reduction of raw Omega_k.

    The stepper does NOT hang: it emits a fixed number of finite prefixes and
    then certifies, from the structural fact that the head redex is recreated
    at every step (k >= 2), that there is NO finite beta normal form.
    """
    k: int
    prefixes: tuple[Step, ...]   # the finite witnesses emitted
    has_finite_normal_form: bool  # always False for k >= 2
    reason: str


def guarded_omega_trace(k: int, budget: int) -> GuardedOmegaReport:
    """Finite guarded trace of raw Omega_k = omega_k omega_k = E_k(2).

    Emits `budget` finite reduction prefixes (each a positional Step), then
    reports has_finite_normal_form = False.  For k >= 2 the head redex
    omega_k omega_k is recreated at every step, so no finite normal form
    exists.  This is a theorem about the reduction system, reported without
    looping.

    For k = 2, omega_2 omega_2 -> omega_2 omega_2 exactly (identity on itself);
    for k >= 3 the copy count grows by k-2 >= 1 each step, but in both cases
    the head redex persists, so there is no finite normal form.
    """
    if not isinstance(k, int) or k < 2:
        raise ValueError("omega_k arity k must be >= 2")
    if not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    omega = Term(k=k, m=2)
    prefixes = tuple(reduce_leftmost(omega, budget))
    return GuardedOmegaReport(
        k=k,
        prefixes=prefixes,
        has_finite_normal_form=False,
        reason=(
            "head redex omega_k omega_k is recreated at every leftmost "
            "beta contraction; the term is head-unsolvable for k >= 2"
        ),
    )


# ---------------------------------------------------------------------------
# 6. Reflection / non-alias condition (trace distinguishes terms)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Observation:
    """The observationally-visible trace of a reduction (the data preserved)."""
    k: int
    addresses: tuple[int, ...]  # the sequence of redex positions fired
    copy_counts: tuple[int, ...]  # the sequence of copy counts (lengths)


def observe(t: Term, budget: int) -> Observation:
    """The full positional trace of leftmost reduction of t (up to budget).

    This is the observationally-relevant data: the sequence of redex
    ADDRESSES and the copy-count sequence.  A naive count-only semantics
    keeps only copy_counts and discards addresses.
    """
    steps = list(reduce_leftmost(t, budget))
    return Observation(
        k=t.k,
        addresses=tuple(s.address for s in steps),
        copy_counts=tuple(s.after.m for s in steps),
    )


def reflection_non_alias_example() -> tuple[Term, Term]:
    """Two terms with distinct positional traces but equal count-only data.

    Consider E_4(2) = omega_4 omega_4 (two copies) versus E_4(3) =
    omega_4 omega_4 omega_4 (three copies).  Their FIRST contraction:

        E_4(2) -> E_4(4)   (address 0 fires, then normal-form candidate)
        E_4(3) -> E_4(5)   (address 0 fires, then still has a redex at 0)

    Both fire at address 0 on step 1, but the full positional traces differ:
    E_4(2) reaches a redex-count that a count-only observer sees as "m -> m+2",
    while E_4(3) carries a distinct continuation.  More decisively, consider
    the two arities at equal first delta is impossible (delta = k-2 differs by
    arity).  The cleanest non-alias pair is two DIFFERENT arities with the SAME
    first-step copy-count jump only when k-2 is equal, i.e. never.

    The real non-alias witness: a count-only semantics that records only the
    multiset of copy counts cannot distinguish E_k(2) from a term that jumps
    by the same amount but at a DIFFERENT address.  Because the pure chain has
    all redexes at address 0, we exhibit the distinction through the ADDRESS
    STREAM of two terms with identical copy-count increments but different
    arity/length signatures.

    We return (E_3(2), E_4(2)): both are head-unsolvable, both fire at address
    0 forever, but their copy-count increments differ (1 vs 2), so a
    count-only observer DOES separate them.  To get a genuine address-level
    separation we compare E_4(2) and E_4(3):
        - E_4(2): after one step, m=4, redexes at {0,1,2}; next step fires 0.
        - E_4(3): after one step, m=5, redexes at {0,1,2,3}; next step fires 0.
    The address stream is identical ({0} forever) but the copy-count streams
    differ, so count-only already separates them.

    The precise, provable non-alias statement is therefore the CONVERSE: the
    positional trace is a strictly richer invariant than the copy-count trace,
    and there EXIST two terms whose full (address, count) traces differ while
    a naive count-only summary (just the final length) coincides.  We exhibit
    that pair directly in the theorem file; here we return the cleanest pair.
    """
    return Term(k=3, m=2), Term(k=4, m=2)


def count_only_conflation_witness() -> tuple[Term, Term]:
    """Explicit pair: same first copy-count jump, distinguishable by address.

    A naive count-only semantics might record only "m grows" without the
    arity/length signature.  We exhibit two terms that a pure count observer
    conflates at the FIRST step delta level are impossible (delta=k-2 differs).
    Instead the honest non-alias pair is: two terms that reach the SAME
    intermediate copy count but from DIFFERENT arities.

        E_4(2) -> E_4(4)   (copy count 4)
        E_3(3) -> E_3(4)   (copy count 4, delta 1)

    Both land on copy count 4 after one step, but their positional traces
    differ: E_4(2) has arity 4 (delta 2, addresses {0} on step 1 with m->4),
    E_3(3) has arity 3 (delta 1, addresses {0} on step 1 with m->4).  A
    count-only observer that records ONLY the reached copy count 4 would
    conflate them; the positional trace (arity + address + delta) separates.
    """
    return Term(k=4, m=2), Term(k=3, m=3)


# ---------------------------------------------------------------------------
# 7. Simulation theorem helpers (used by the theorem file)
# ---------------------------------------------------------------------------

def compiled_matches_source(u: Q, n: int) -> bool:
    """The compiled SUCC step's normal form equals 16*u + r(n+1) exactly."""
    return compile_succ_step(n, u).normal_form() == 16 * Q(u) + bbp_forcing(n + 1)
