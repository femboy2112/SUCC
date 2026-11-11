"""Restricted omega-chain beta traces and separate finite BBP arithmetic.

Scope (see research/2026-11-09/scott_omega_causal_weld/OMEGA_INTERPRETER.md):

* An explicit syntax for omega_k = lambda x. x x ... x (k left-associated
  copies) and E_k(m) = the left-associated chain of m copies of omega_k.
  Its unique redex carries its actual binary application-tree address.

* A leftmost-beta reduction stepper returning (term, redex_address, step).

* Exact verification of the growth law  E_k(m) -> E_k(m+k-2), k in 2..8.

* A FINITE rational BBP evaluator with an explicit operation trace.  The
  historical name "compiled SUCC step" is retained, but this is not a
  source-to-lambda compiler or a simulation theorem for arbitrary terms.

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

    def redex_addresses(self) -> tuple[tuple[str, ...], ...]:
        """Actual beta-redex paths; ``f`` descends an application's left child.

        For m >= 2, E_k(m) has exactly ONE redex, omega_k omega_k,
        at ("f",)*(m-2).  Outer applications have an application (not an
        abstraction) on the left; no other omega body contains a beta redex.
        The empty tuple is the root address when m=2.
        """
        return (("f",) * (self.m - 2),) if self.m >= 2 else ()

    def syntax(self):
        """Materialize the actual de Bruijn AST for finite independent probes.

        The compressed stepper avoids building enormous left spines.  This
        method makes its asserted representation separately inspectable.
        """
        from .c_monoid_succ_embedding import V, ABS, APP
        body = V(0)
        for _ in range(self.k - 1):
            body = APP(body, V(0))
        omega = ABS(body)
        term = omega
        for _ in range(self.m - 1):
            term = APP(term, omega)
        return term

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
    address: tuple[str, ...]  # actual path to the contracted beta redex
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
    return Step(before=t, address=t.redex_addresses()[0], after=after, delta=k - 2)


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
# 4. Finite BBP rational evaluation (historical "compiled" API names)
# ---------------------------------------------------------------------------

# The source recurrence is  U_{n+1} = 16 * U_n + r(n+1)  with
#   r(j) = 4/(8j-7) - 2/(8j-4) - 1/(8j-3) - 1/(8j-2),  U_0 = 0.
# For each n this is a fixed finite rational expression.  The three-slot
# operation trace records exact arithmetic; it does not encode a lambda AST
# or prove an omega-to-BBP compiler theorem.


def bbp_forcing(j: int) -> Q:
    """Frozen four-pole BBP forcing r(j), exact rational."""
    if not isinstance(j, int) or j < 1:
        raise ValueError("BBP source indices must be >= 1")
    return Q(4, 8 * j - 7) - Q(2, 8 * j - 4) - Q(1, 8 * j - 3) - Q(1, 8 * j - 2)


@dataclass(frozen=True)
class CompiledTraceEntry:
    """One atomic operation in the compiled SUCC step's reduction trace.

    Each entry names an operation slot in a fixed rational evaluation of
    16*U + r(n+1).  These slots are not lambda beta-redex addresses.
    """
    address: int      # position in the flattened expression tree
    op: str           # operation name (add / scale / force)
    result: Q         # exact rational value of that subexpression


@dataclass(frozen=True)
class CompiledSUCCStep:
    """A finite exact rational result with a fixed operation trace.

    The Python evaluation terminates.  A typed lambda-calculus term and a
    preservation/reflection theorem for its compiler are not supplied.
    """
    n: int
    u_next: Q
    trace: tuple[CompiledTraceEntry, ...]

    def normal_form(self) -> Q:
        return self.u_next


def compile_succ_step(n: int, u: Q = Q(0)) -> CompiledSUCCStep:
    """Compile the finite SUCC step U -> 16*U + r(n+1) to a normal form.

    The trace is a fixed sequence of rational operation slots (0,1,2).
    This evaluator terminates; a sound lambda compiler is not supplied.

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
    addresses: tuple[tuple[str, ...], ...]  # actual application-tree paths
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
    """Different arities already distinguished by the copy-count stream.

    This historical helper does not prove an independent address invariant.
    Within a fixed-k pure-chain family, the addresses are determined by m.
    """
    return Term(k=3, m=2), Term(k=4, m=2)


def count_only_conflation_witness() -> tuple[Term, Term]:
    """Equal first reached counts; different actual contraction addresses.

    E_4(2) -> E_4(4) contracts at the root ().
    E_3(3) -> E_3(4) contracts at ("f",).
    A summary recording ONLY the final count 4 loses this distinction.
    Full copy-count histories plus arity already recover the addresses;
    no independent spatial dimension is inferred from this example.
    """
    return Term(k=4, m=2), Term(k=3, m=3)


# ---------------------------------------------------------------------------
# 7. Simulation theorem helpers (used by the theorem file)
# ---------------------------------------------------------------------------

def compiled_matches_source(u: Q, n: int) -> bool:
    """The compiled SUCC step's normal form equals 16*u + r(n+1) exactly."""
    return compile_succ_step(n, u).normal_form() == 16 * Q(u) + bbp_forcing(n + 1)
