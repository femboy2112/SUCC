# Omega-indexed causal computation: interpreter, simulation, and reflection

Scope of this document: the executable beta-reduction interpreter in
`observational_succ/omega_trace_interpreter.py`, its exact growth law, its
finite strongly-normalizing compiled SUCC fragment, its separate guarded
(coinductive) trace for raw `Ω_k`, the simulation theorem (compilation then
reduction = reduction then compilation), and the reflection/non-alias
condition.

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

Every beta-redex is the pattern `ω_k ω_k`.  A **position (address)** is the
spine index of the redex's left component: address `0` is the head application,
address `1` is the result of the head applied to the next `ω_k`, and so on.
`E_k(m)` has redexes at addresses `0, 1, …, m−2` (there are `m−1` of them).
The **leftmost** redex is always at address `0` whenever `m ≥ 2`.

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

The interpreter verifies this exactly for `k ∈ {2,…,8}` and `m ∈ {1,…,12}`
(`verify_growth_law`), and for `k = 3` the increment is `1`, so `Ω_3` is the
unit syntactic SUCC step (`m → m + 1`).

---

## 3. The finite strongly-normalizing compiled SUCC step

The source recurrence is

    U_0 = 0,    U_{n+1} = 16 U_n + r(n+1),

    r(j) = 4/(8j−7) − 2/(8j−4) − 1/(8j−3) − 1/(8j−2).

This is a **finite typed rational computation**: for each `n` the step is a
single fixed expression `16·U + r(n+1)` with no recursion and no β-redex.  The
interpreter compiles it to a normal form carrying an explicit **positional
trace** of three atomic operations:

    0: scale   16·U
    1: force   r(n+1)
    2: add     16·U + r(n+1)

**Strong normalization is structural:** the trace length is the fixed constant
3, independent of `n`; there is no redex that recreates itself.  Hence the
compiled fragment is terminating (actually, normalizing in one step by
construction).  This is *distinct* from the raw `Ω_k` fragment, which is
head-unsolvable and non-terminating.

---

## 4. Simulation theorem (compilation then reduction = reduction then compilation)

**Theorem (simulation / commuting square).** Let `C` denote the compilation map
(the `compile_succ_step` operation) and let `⟦·⟧` denote reduction to normal
form.  For every rational `U` and every `n ≥ 0`,

    ⟦ C(U, n) ⟧  =  16·U + r(n+1),

i.e. the normal form of the compiled SUCC step is exactly the source map
`U ↦ U_{n+1}`.  Equivalently, the following square commutes:

                  compile
        (U, n)  ───────────►  C(U, n)   (typed compiled term with trace)
          │                       │
          │  reduce               │  reduce (normal form)
          ▼                       ▼
        16U + r(n+1)   =======  ⟦ C(U, n) ⟧   (exact rational)

*Proof.* `compile_succ_step(n, U)` returns `CompiledSUCCStep(u_next = 16·U +
r(n+1), trace = …)`, and `normal_form()` returns exactly `u_next`.  Both sides
are the single rational expression `16·U + r(n+1)` computed with exact
`Fraction` arithmetic.  The equality holds for every rational `U` and every
`n ≥ 0`. ∎

**Corollary (orbit).** Iterating the compiled step reproduces the exact source
orbit: `compiled_orbit(N, 0)` yields normal forms `U_1, U_2, …, U_N` with
`U_n = Σ_{j=1}^n 16^{n−j} r(j)`, matching the source `selected_state`
(`CW-04`).  This is checked exactly by the test suite, with no floating point.

The simulation theorem states that **compilation followed by reduction** and
**reduction of the source map** produce the *same rational data*.  It does not
claim anything about `Ω_k` normal forms (none exist) nor about normality of the
resulting digit sequence.

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

Consequently the positional trace is a **strictly finer** observation than the
copy-count trace, and discarding the address/arity channel loses real
distinctions — exactly the kind of distinction that `CW-14`/`CW-15` warn
against collapsing.

---

## 7. Honest boundaries

* **Proved (finite/structural):** the growth law `E_k(m) → E_k(m+k−2)`
  (`k ∈ 2..8`, exact arithmetic); the strong normalization of the compiled
  SUCC fragment (trace length 3, no redex that recreates itself); the
  simulation equality `⟦C(U,n)⟧ = 16U + r(n+1)`; head-unsolvability (no finite
  β-normal form) of `Ω_k` for `k ≥ 2`; the non-alias witness.

* **Open / not claimed:** any normality or equidistribution statement about the
  hexadecimal digits of π; any signed cancellation (CW-20/CW-21); any claim
  that `Ω_k` has a finite normal form (it does not).  The arithmetic
  consequences of the `Ω_k` growth law for π normality are **not** asserted.

* **Implementation provenance:** the interpreter and tests are one author's
  standard-library implementation; the source algebra is exact and the outputs
  are falsifiable, but an independent second implementation or theorem referee
  is a separate gate (see `VALIDATION.md`).
