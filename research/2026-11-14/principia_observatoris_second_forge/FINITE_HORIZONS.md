# Finite horizons: delayed finite failure versus asymptotic defect

**Second Forge, 2026-11-14.** This is the principal investigator's synthesis of the finite-horizon
front. Full proofs, sharpness constructions and hostile models are in the delegated report
[agents/OPUS_III_HORIZON_HUNTER.md](agents/OPUS_III_HORIZON_HUNTER.md) (theorems FH-1 … FH-14);
this document states what was established, how it was checked, and what it means for the
founding distinction. Labels: **C** = classical (named source in the report), **P** = proved in
this package, **O** = observed in exact finite models. Executable evidence:
`tests/test_observatoris_finite_horizons.py` (45 tests).

Nothing here bears on physics, RH or π-normality. Every positive result is *inside a declared
model class*; agreement with a class on a finite horizon never shows that a source belongs to it.

## 1. The question

The founding note ([PR #618](https://github.com/femboy2112/SUCC/pull/618) §9, shared input)
separates two regimes that a finite observer may be unable to tell apart:

- **Finite surprise:** some finite index carries a decisive counterexample, possibly very late.
- **Limit-only defect:** every finite residual is nonzero, and equality holds only in the limit.

Its certificate is the pair `a(n) = 1/(n+1)` and `b_H` (equal to `a` through index `H`, then `1`).
We reproduced that certificate independently, then asked the sharper question: **for which model
classes does agreement on a finite horizon force agreement forever, with what exact horizon, and
what precisely is lost when the class restriction is dropped?**

## 2. What a readout-only observer can decide at all (FH-1, FH-2, FH-11, FH-12)

**FH-1 (C/P).** A terminating deterministic adaptive finite-readout protocol decides a target `T`
on a class `X` **iff `T` is continuous at every point of `X`** in the finite-information topology.
At a discontinuity point every such protocol errs on that point or on a neighbour agreeing with
it on everything queried. The regime label on `{a} ∪ {b_H}` is discontinuous at `a`; this
re-proves the founding certificate, adaptive case included.

**Correction recorded.** My brief conjectured the weaker hypothesis "for each finite query set
two members agree on it and differ in target". That is enough against *non-adaptive* protocols
only. *Receipt (REFUTED):* the pointer class `x(0) = k, x(k+1) = β`, target `β`, satisfies the
hypothesis, yet two adaptive queries decide the target. The right condition is discontinuity at
a single point.

**FH-2 (P).** For randomised protocols, at a discontinuity point `x*` and for every `δ > 0` there
is a neighbour `y` with `err(x*) + err(y) ≥ 1 − δ`: worst-case error cannot be pushed below `1/2`.

**FH-11 (C/P): the asymmetry.** "A finite counterexample exists" is an open (Σ⁰₁) property: when
true it is verified by one observation. "No counterexample and defect → 0" is Π⁰₃-complete in
the unrestricted space; relative to the two-regime promise it is closed with **empty interior**.
So the limit-only regime is *never* verified by a finite record — it can only fail to be refuted
— while the finite-surprise regime is verified exactly when its witness is reached. This is the
exact mathematical form of the author's asymmetry, and it is classical learning-theoretic
topology (Gold; Kelly; Vickers; Smyth), not a discovery of this package.

**FH-12 (C).** Three properties of a class are strictly ordered:
*uniform horizon* ⇒ *finite certification* (every member isolated) ⇒ *identification in the limit*
(countable class). Each implication is strict.

## 3. Finite-horizon completeness, with exact constants

All bounds below are **sharp**; each has an explicit extremal pair and an exhaustive small-case
search that could have falsified it.

| Class (declared bounds `n`, `m`) | Agreement that forces equality forever | Status |
|---|---|---|
| Monic linear recurrences of orders ≤ n, ≤ m, any field | first **n + m** terms | FH-3, P (upper bound C) |
| Restricted recurrence families `𝒫`, `𝒬` | **max deg lcm(p, q)** terms | FH-3d, P |
| LTI Markov parameters `C A^k B`, state dims ≤ n, ≤ m, SISO or MIMO | **n + m** parameters (`n+m+1` with feedthrough) | FH-4, C/P |
| Same class, dimension ≤ n | **2n** | FH-3c, C |
| Autonomous deterministic machines, ≤ n and ≤ m states | **n + m − 1** outputs | FH-7, P/O |
| Moore machines with inputs | input words of length **n + m − 2** | FH-8, C/O |
| Mealy machines with inputs | input words of length **n + m − 1** | FH-8, C/O |
| Weighted automata over a field; generative HMMs | words of length **n + m − 1** | FH-9, C/P |
| Rabin probabilistic automata | words of length **n + m − 2** | FH-9, P |
| First-order polynomial recurrences of degree ≤ d | **d + 2** terms | FH-14, P |

**Why the linear bound holds (FH-3).** The difference of the two sequences is annihilated by
`lcm(p,q)`, of degree `D ≤ n+m`, and a sequence satisfying a monic recurrence of order `D` that
vanishes on its first `D` terms is zero. *Sharpness:* `a` annihilated by `tⁿ` and
`b(k) = C(k−n, m−1)` annihilated by `(t−1)^m` agree on exactly `n+m−1` terms, over every field.

**Corrections to the PI's brief (kept as receipts).**
- Machines are *one better* than linear systems: `n+m−1`, not `n+m` (machine state vectors lie in
  a hyperplane).
- `n+m` is **not** sharp for every restricted family: over GF(2) with invertible recurrences of
  order ≤ 1 the horizon is `1`. The correct general constant is `max deg lcm`.
- For Rabin probabilistic automata the sharp word length is `n+m−2`, not the `n+m−1` I quoted
  (receipt: an exact pair first differing at the word `xx`, `15/64` versus `9/64`). Whether the
  primary sources state `n+m−1` or `n+m−2` was **not** checked.

**Independent verification by the PI** (separate code, no import of the delegated module):
the linear sharpness pairs for all `1 ≤ n,m ≤ 3`; the autonomous-machine horizon `n+m−1` by
brute force for `(n,m) ≤ (3,3)`; and the closed form in FH-6 for `n ≤ 6`. All agreed.

## 4. The central statement: limit-identifiable, never certified (FH-5)

For the union `LR = ⋃_n LR_n` of all linear-recurrent sequences (unknown order):

1. **No horizon.** Every member has, for every `N`, another member agreeing with it on `N` terms.
2. **Identification in the limit, with an explicit time.** The conservative minimal-order learner
   is exactly right from prefix length `2·ord(x)` on, with at most `2·ord(x)` mind changes; and
   `2·ord(x)` is optimal for every learner.
3. **No certificate, ever.** A sound stopping rule halts on **no** member of `LR`.
4. **No uniform mind-change bound.**
5. **A declared bound restores everything.** On `LR_n`, "wait `2n` terms, then commit" is a sound
   certifier that halts on every member, and `2n` is optimal.

*Status: P for the constants and the LR-specific argument; the learning-theoretic form is C
(Gold 1967; Osherson–Stob–Weinstein).*

This is the observer's predicament stated without metaphor: **the observer does converge to the
truth, and from some finite time on is exactly right, but no record can ever tell it that this
time has passed — unless a complexity bound on the source is itself part of what is known.**
The bound is not observable; it is a premise about the source.

## 5. The founding pair inside the theory (FH-6, FH-10)

- **`a(k) = 1/(k+1)` has infinite Hankel rank** (every Hilbert matrix is nonsingular; Cauchy
  determinant, C). The limit-only law lies outside *every* finite-dimensional linear class.
- **`b_H` has order exactly `H+2`** for `H ≥ 1` (minimal polynomial `t^{H+1}(t−1)`): the delayed
  surprise is finite-dimensional, with complexity growing with its delay.
- **A declared dimension bound `n` therefore excludes the limit-only law, not the finite
  surprise:** every member of `LR_n` departs from `1/(k+1)` at some index `≤ 2n`. The unique
  order-`n` mimic agrees through index `2n−1` and first misses at index `2n` by exactly
  `(n!)⁴ / ((2n)!·(2n+1)!) ~ (π/2)·16⁻ⁿ`.
- **Precision corollary.** Excluding dimension `n` from that horizon needs about `4n` bits of
  precision at index `2n`; with exact readouts `2n+1` terms suffice.
- **Hostile reading (kept).** A dimension bound does not exclude the limit-only *regime* in
  general: `2^{-k}` has order one, never vanishes and tends to zero.

**Effective moduli (FH-10, P).** With a declared modulus `μ` (`|e_i − e_j| ≤ μ(min(i,j))`), the
set of limits compatible with a prefix of length `N` is exactly `⋂_{j<N}[p_j − μ(j), p_j + μ(j)]`;
its worst-case width is exactly `2μ(N−1)`, so the optimal error radius is `μ(N−1)` (SUCC's
target-oscillation radius, inherited from `docs/CARRIER_RELATIVE_TARGETS.md` §4). Without a
modulus the limit set of every prefix is all of ℝ. **A finite prefix plus a proved modulus
identifies the limit to explicit accuracy; a finite prefix alone constrains nothing.**

## 6. Identification is not verification (FH-13, C)

Even exact identification of a rational linear recurrence does not decide the universal
statement "`e_n ≠ 0` for all `n`": that is the Skolem problem. The zero set has the
Skolem–Mahler–Lech structure, low orders are decidable, and the general problem is open as far
as we know; **the current frontier was not verified against the literature.** For a deterministic
`n`-state machine the same universal statement is decided by its first `n` outputs.

So there are three distinct epistemic levels, and the founding note's two regimes sit across
them: *what the future observations are* (identification), *whether a universal statement about
them holds* (verification), and *whether the record can certify either* (certification).

## 7. Physical size is not complexity (FH-7c)

A carrier with `k` bits of state can hide its first deviation until index `2^k − 1` (a counter
that gates one output when it saturates): a bound on *physical size* is an exponentially weaker
premise than a bound on *state count*, and with a bound only on description length no computable
horizon exists at all (busy-beaver delay; C). A linear carrier of dimension `k`, by contrast, has
a horizon linear in `k`. Which complexity measure the observer is entitled to assume is therefore
the whole question.

## 8. Which assumptions are indispensable

| Drop this | What breaks | Receipt |
|---|---|---|
| the order / state bound | no horizon; only limit identification | FH-5 |
| monic recurrence | every sequence qualifies | `0·x = 0` |
| exact readouts | dimension `n` cannot be excluded below precision `δ_n` | FH-6e |
| the declared modulus | the limit is unconstrained | FH-10c |
| source membership in the class | nothing follows from agreement | boundary of every theorem |
| tail-closure hypothesis in the impossibility theorem | adaptive protocols can win | pointer class |

## 9. Open

- Whether `2d` mind changes is the true worst case for every `d` (observed for small `d` only).
- An index-refined MIMO horizon; a precision-versus-horizon curve beyond index `2n`.
- Polynomial recurrences of order `≥ 2`.
- The exact attribution of the probabilistic-automaton constants in the primary literature.
- The status of the adversarial review of these results is recorded in
  [COUNTERMODELS.md](COUNTERMODELS.md) and
  [PROVENANCE_AND_INDEPENDENCE.md](PROVENANCE_AND_INDEPENDENCE.md).
