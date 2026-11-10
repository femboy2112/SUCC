# Omega-indexed causal computation: interpreter, simulation, and reflection

**Audit correction:** the original draft invented extra beta-redex addresses
and described a finite rational evaluator as a source-to-lambda compiler.
The corrected scope is restricted omega-chain beta reduction, its exact growth
law, and a separate terminating BBP arithmetic trace. A faithful compiler remains
UNVERIFIED. See [semantic audit](../cayley_source_observer/SEMANTIC_AUDIT.md);
parent commit `afabc458323ef2e3a20ce2bae77239c4190819c5` preserves the old text.

Everything here is **finite and structural**.  The raw `Ω_k` having no finite
beta normal form is a theorem of the reduction system.  The arithmetic
consequences for π normality are **NOT** claimed.

---

## 1. Syntax and semantics

Define, for integer `k ≥ 2`,

    ω_k := λx. x x … x        (k left-associated self-applications)

and

    Ω_k := ω_k ω_k,           E_k(m) := ω_k ω_k … ω_k   (m copies, left-associated).

`E_k(m)` is an application spine of `m` components, each component being `ω_k`.
Application is left-associated, so the spine is

    ((…((ω_k ω_k) ω_k) …) ω_k).

For `m>=2` there is exactly one beta-redex, `ω_k ω_k`. An address is a tuple
of binary application-child labels, with `f` descending to the left child.
The unique redex is at `('f',)*(m-2)`; `()` is the root for m=2. Every outer
application has an application, not an abstraction, on its left. The omega
bodies contain only variable applications, so introduce no other redexes.

`E_k(1) = ω_k` is a bare abstraction and has no redex, hence is a β-normal form.

**Head-unsolvability.** For `k ≥ 2`, `Ω_k` is head-unsolvable: the head redex
`ω_k ω_k` reduces to a term containing `ω_k ω_k` again at the head (for `k = 2`
it is exactly `ω_2 ω_2`, an identity-on-itself loop; for `k ≥ 3` the copy count
grows but the head redex persists).  Consequently `Ω_k` has **no finite
β-normal form**.  This is asserted as a theorem about the reduction system and
is *reported* by the guarded trace — it is not a claim that the interpreter
computes a normal form by looping.

---

## 2. Growth law (CW-02, CW-03)

**Theorem (growth law).** For every integer `k ≥ 2` and `m ≥ 2`, one leftmost
β-contraction of `E_k(m)` yields `E_k(m + k − 2)`.  The copy count changes by
exactly `k − 2`.

*Proof.* The leftmost redex is the head `ω_k ω_k`, occupying 2 copies.  Its
contraction substitutes the argument for `x` in `λx. x x … x` (k copies),
producing `k` copies of `ω_k`, followed by the remaining `m − 2` copies of the
original spine.  The result is a chain of `k + (m − 2) = m + (k − 2)` copies.
∎

The interpreter verifies this exactly for `k ∈ {2,…,8}` and `m ∈ {2,…,12}`
(`verify_growth_law`), and for `k = 3` the increment is `1`, so `Ω_3` is the
unit syntactic SUCC step (`m → m + 1`).

---

## 3. The separate finite BBP arithmetic trace

The source recurrence is

    U_0 = 0,    U_{n+1} = 16 U_n + r(n+1),

    r(j) = 4/(8j−7) − 2/(8j−4) − 1/(8j−3) − 1/(8j−2).

This is a **finite typed rational computation**: for each `n` the step is a
single fixed expression `16·U + r(n+1)` with no recursion and no β-redex.  The
historically named `compile_succ_step` evaluates it and records three arithmetic
operation slots, which are distinct from beta-redex addresses:

    0: scale   16·U
    1: force   r(n+1)
    2: add     16·U + r(n+1)

The rational expression terminates for each finite input. Its fixed three-slot
trace is not a typed lambda term or a proof of compiler preservation/reflection.
Integer arithmetic cost can grow with input size. The raw omega fragment is a
separate nonnormalizing syntax.

---

## 4. Exact arithmetic evaluation identity

**Evaluation identity.** Let C be the historical `compile_succ_step` operation
and let brackets denote retrieval of its stored rational result. For every
rational U and natural n,

    ⟦ C(U, n) ⟧  =  16·U + r(n+1),

This states equality of rational arithmetic values, not simulation between
two independently defined reduction systems.

*Proof.* `compile_succ_step(n, U)` returns `CompiledSUCCStep(u_next = 16·U +
r(n+1), trace = …)`, and `normal_form()` returns exactly `u_next`.  Both sides
are the single rational expression `16·U + r(n+1)` computed with exact
`Fraction` arithmetic.  The equality holds for every rational `U` and every
`n ≥ 0`. ∎

**Corollary (orbit).** Iterating the compiled step reproduces the exact source
orbit: `compiled_orbit(N, 0)` yields normal forms `U_1, U_2, …, U_N` with
`U_n = Σ_{j=1}^n 16^{n−j} r(j)`, matching the source `selected_state`
(`CW-04`).  This is checked exactly by the test suite, with no floating point.

The identity verifies the evaluator's result. A source-to-lambda encoding and
a preservation/reflection theorem remain separate unproved obligations.

---

## 5. Separate guarded / coinductive trace for raw Ω_k

Raw `Ω_k` has no finite β-normal form.  The interpreter therefore does not try
to reduce it to normal form (which would hang); instead `guarded_omega_trace`
emits a **finite** number of positional prefixes and then certifies, from the
head-unsolvability argument, that `has_finite_normal_form = False`.

This is a **guarded/coinductive** presentation: the infinite reduction is
represented as a productive stream of finite steps together with a proof of
non-termination, rather than as a (nonexistent) finite result.

---

## 6. Reflection / non-alias condition

The observationally-relevant data is the **positional trace**: the sequence of
redex addresses fired, plus the copy-count sequence.  A naive count-only
semantics keeps only the copy counts (or only the final length) and discards
addresses and arity.

**Theorem (non-alias).** There exist two terms that a count-only observer
conflates but whose positional traces differ.  Explicit witness:

    E_4(2) = ω_4 ω_4      ⟶  E_4(4)     (delta = 2, arity 4)
    E_3(3) = ω_3 ω_3 ω_3  ⟶  E_3(4)     (delta = 1, arity 3)

Both land on copy count `4` after one leftmost step.  An observer recording
only "reached copy count 4" conflates them; the positional trace `(arity,
address stream, delta)` separates them (`k = 4, Δ = 2` vs `k = 3, Δ = 1`).

*Proof.* By the growth law, `E_4(2) → E_4(4)` and `E_3(3) → E_3(4)`; both
after-terms have `m = 4`, but the arities and deltas differ (`4 ≠ 3`,
`2 ≠ 1`).  Since the arity `k` and the per-step delta `k − 2` are part of the
positional trace but not part of a count-only summary that records only the
copy count, the two terms are observationally distinct under the positional
semantics and conflated under the naive count-only semantics. ∎

Consequently this trace is finer than the deliberately weaker summary retaining
only the first reached count. In the restricted family, however, the arity and
complete copy-count history determine every address. No independent spatial
dimension or separation from that complete history follows.

---

## 7. Honest boundaries

* **Proved (finite/structural):** the growth law `E_k(m) → E_k(m+k−2)`
  (proved for all k>=2, calibrated at k=2..8); termination of the separate
  rational evaluator; the arithmetic identity `⟦C(U,n)⟧ = 16U + r(n+1)`;
  head-unsolvability (no finite
  β-normal form) of `Ω_k` for `k ≥ 2`; the non-alias witness.

* **Open / not claimed:** any normality or equidistribution statement about the
  hexadecimal digits of π; any signed cancellation (CW-20/CW-21); any claim
  that `Ω_k` has a finite normal form (it does not).  The arithmetic
  consequences of the `Ω_k` growth law for π normality are **not** asserted.

* **Implementation provenance:** the new generic AST enumeration and addressed
  contraction provide a second failure mechanism against the compressed formula.
  This is finite validation, not an external theorem referee; see the follow-up
  validation record for its exact scope.
