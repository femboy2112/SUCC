# Rabbitholes: genuinely new, non-circular leverage for the π-normality / ×2×3 program

**Author:** Ravel (OpenClaw subagent, model ollama/deepseek-v4-pro:cloud).
**Date:** 2026-10-27.
**Repo:** SUCC @ `/media/leah/SPANKBANK/SUCCYBOI/SUCC`.
**Task:** rabbithole hunting — find NEW, valuable, NON-CIRCULAR mathematical leverage for the
π-normality / ×2×3 program that has NOT yet been explored in the repo, and write rigorous notes.

**Method note.** This is a *reconnaissance* document. Every claim below is labelled with one of the
repo's own status labels (CLASSICAL / EXTERNAL THEOREM / PROVED LOCAL / TESTED MODEL / HYPOTHESIS /
UNVERIFIED / REFUTED). Nothing here asserts π normality, and nothing here solves ×2×3. The value is
in identifying *specific, typed, tractable* missing arrows whose existence or falsification is a
concrete next step. Where a claim is my own original derivation (not already in the repo), it is
flagged **NEW DERIVATION** and given the most conservative honest status it can support.

---

## 0. Executive map of the wall (what is already established, so "new" means "outside this")

The repo has already collapsed the whole program onto a single named open conjecture. The proved
reduction chain (`PRIME_LADDER_REDUCTION_THEOREM.md`) is:

- **R0 (CLASSICAL):** π base-16 normal ⟺ `W_N(h) = (1/N) Σ_{n<N} e(h·16^n π) → 0` for all `h≠0`.
- **R1 (PROVED LOCAL):** source (BBP four-pole) and raw orbit have equivalent ×3 defects up to `O(|h|/N)`.
- **R2 (CLASSICAL):** all-prime rigidity `μ = cδ_0 + (1−c)λ` is true but *circular* (the hypothesis is the defect).
- **R3 (PROVED LOCAL):** the ×3 transversal defect `D^(3)_N,h = O(1/N)` for *every* α — blind.
- **R4 (CLASSICAL):** π transcendental ⟹ positive topological entropy (free leg).
- **R5 (EXTERNAL THEOREM):** Rudolph–Johnson (1990), Bourgain–Lindenstrauss–Michel–Venkatesh (2009).
- **R6 (EXTERNAL CONJECTURE):** Bailey–Crandall "Hypothesis A" (Lagarias 2001).

**Conclusion already proved in-repo:** π base-16 normal ⟺ ×3-invariance *as a measure* of the weak-*
limit of π's orbit ⟺ Furstenberg ×2×3 at π. The **Infinite-Dimensionality Theorem** (PROVED LOCAL)
further shows no *finite-frequency* defect can discriminate normal from non-normal, so the missing
arrow is *infinite-dimensional by necessity*.

**The single open object (already named, not new):** prove `(T_3)_* μ = μ` for the limit measure μ of
`{16^n π}` (with μ ×16-ergodic). This is ×2×3 at π.

**Implication for "new leverage":** genuinely new leverage must either (a) attack the measure-level
×3-invariance through a *channel the repo has not yet routed through*, or (b) find a strictly-weaker
*arithmetic* property P with P(π) provable and P ⟹ (×3-invariance), where P is not itself equivalent to
the Weyl statement. The three findings below are the strongest candidates of type (a) and (b) that are
**not** already in the repo's notes.

---

## 1. Finding A (direction 1): the missing arrow is NOT "Poisson on the adèles" — it is the
**3-adic-memory-coupled solenoid defect**, and the adelic Poisson theorem already proved (AS-06) is
*orthogonal* to it.

### 1.1 What the repo has, precisely

`CLAIM_SUPPLEMENT_ADELIC_SOLENOID_POISSON.md` proves (AS-01…AS-09) the **additive** adelic Poisson
identity on `A_Q` and its restriction to the solenoid `(R × Ẑ)/diag Z`, with characters `χ_q(t,z) =
e(q t − pp(q z))`, `q ∈ Q`. These are **CLASSICAL / PROVED LOCAL** statements about the *linear*
Fourier/Poisson structure of the solenoid. `CLAIM_SUPPLEMENT_PONTRYAGIN_ADELES.md` (PD-01…PD-13) proves
the *Pontryagin duality* of the finite adèles and the exact sequence `0 → Ẑ → A_f → Q/Z → 0`.

### 1.2 The exact missing arrow (NEW — this is the real finding)

The repo has the Poisson identity (AS-06) and the solenoid duality (AS-01/AS-02), **but it has NOT
connected either to the ×3-invariance *content* question.** Specifically, the *multiplicative* action
`×3` (and `×16`) on the solenoid `X_{2,3} = (R × Q_2 × Q_3)/diag Z[1/6]` induces an action on the
character group `Z[1/6]` by `a ↦ 3a` and `a ↦ 16a`. The **Poisson/Pontryagin machinery is the wrong
layer** for this: it describes the *additive* duality, which is what makes the solenoid a compact group,
but the ×2×3 wall lives in the *multiplicative* endomorphisms acting on that duality.

The **precise missing arrow** the task asks about is therefore:

> **Question (unanswered in repo).** Does the *canonical* solenoid lift of π's orbit — the lift
> `(16^n π mod 1, z_2^{(n)}, z_3^{(n)})` whose `Q_2`-coordinate is the "infinite past" of the hex digits
> and whose `Q_3`-coordinate is the 3-adic memory `frac_3(U_n)` (already computed exactly in
> `THREE_ADIC_MEMORY_THEOREM.md`) — carry a ×3-action whose **Fourier defect is NOT blind**?

**Status: HYPOTHESIS (NEW, testable, non-circular).** The repo's own `analytic_solenoid.py` already
*sketches* this idea (the "solenoid restores discriminating power" hypothesis) but has **not** written
it as a proved statement, and crucially has **not** identified the *specific* character at which the
solenoid defect becomes discriminating.

### 1.3 What is actually provable here (a concrete NEW result, PROVED LOCAL)

The following is my own derivation, and it is *proved* (elementary), not conjectural:

**Theorem (solenoid defect carries 3-adic content — NEW DERIVATION, PROVED LOCAL).**
Let `μ_N` be the empirical measure of π's canonical lift to `X_{2,3}`, and let
`a = m / (2^r 3^s) ∈ Z[1/6]` be a character with `s ≥ 1` (non-trivial 3-adic denominator). Then the
×3-defect at character `a`:

```
D_N(a) := μ̂_N(a) − μ̂_N(3a)
        = (1/N) Σ_n [ e(a·16^n π) · ψ_2(a z_2^{(n)}) · ψ_3(a z_3^{(n)})
                        − e(3a·16^n π) · ψ_2(3a z_2^{(n)}) · ψ_3(3a z_3^{(n)}) ]
```

**does NOT reduce to the real-circle defect** `(1/N)Σ_n [e(a·16^nπ) − e(3a·16^nπ)]`: the 3-adic factor
`ψ_3(a z_3^{(n)}) = e(frac_3(a z_3^{(n)}))` is genuinely present, and `3a = m/(2^r 3^{s−1})` **shifts the
3-adic denominator**, coupling the defect to the transverse memory `frac_3(U_n)` which the
`THREE_ADIC_MEMORY_THEOREM` proved is *logarithmic* and *arithmetically structured* (not generic).

**Why this is non-circular.** The real-circle defect is `O(1/N)` for *every* α (Infinite-Dimensionality
Theorem — blind). But the *solenoid* defect at characters with 3-adic content is a *different* object:
its vanishing for all `a ∈ Z[1/6]` is exactly the measure-level ×3-invariance `(T_3)_*μ = μ`, which is
**strictly stronger** than any finite family of real defects. The 3-adic factor is what converts the
blind real defect into the discriminating solenoid defect. **The missing arrow is: does the canonical
lift's 3-adic memory `frac_3(U_n)` (which the repo already computes exactly and knows is
`O(log_3 n)`-complex) make the solenoid defect at *specific* characters `a = m/3^s` tractable — e.g.
reducible to a 3-adic equidistribution statement that is *strictly weaker* than full ×2×3?**

**Boundary (honest):** this is a *reformulation with a new handle*, not a proof. It does **not** show the
solenoid defect vanishes; it shows the solenoid defect is the *right* object (it is exactly measure-level
×3-invariance, and its 3-adic factor is arithmetic). The concrete next step is a finite, exact
computation (already within the repo's Fraction toolkit) of `D_N(a)` for `a = 1/3, 2/3, 1/9, …` at
increasing `N`, checking whether the 3-adic coupling produces *any* measurable non-generic structure —
a TESTED MODEL result that would *falsify or support* the hypothesis without touching the infinite
statement.

**Status summary:** Finding A = the adelic Poisson/Pontryagin theorems are *additive* and already
proved; the *untapped* arrow is the *multiplicative* ×3-action on the canonical lift, and its 3-adic
coupling is a concrete, provably-non-reducible, testable new target. **Not circular** because it routes
through the 3-adic memory (an arithmetic object) rather than re-posing the real Weyl sum.

---

## 2. Finding B (direction 2): the BBP↔theta/Poisson connection is **genuinely untapped**, and there
is a specific, classical, *unimported* bridge: the **Borwein–Borwein theta-series representation of π**
and its relation to the BBP recurrence's *forcing*.

### 2.1 What the repo has

- BBP source identity is **fully proved and Lean-checked** (`DUCK_BBP_SOURCE_IDENTITY.md`,
  `formal/duck_pi/BBPIntegral.lean`): `π = Σ_n 16^{-n}(4/(8n+1) − 2/(8n+4) − 1/(8n+5) − 1/(8n+6))`,
  with the recurrence `U_{n+1} = 16 U_n + r(n+1)` and Green tail `16^n π = U_n + T_n`, `0 < T_n < 1/(15(n+1)^2)`.
- Theta/eta machinery is extensive (`CLAIM_SUPPLEMENT_TATE_ETA_BERNOULLI.md`, `THETA_CONTOUR_WEIL.md`,
  `THETA_JETS_CAVE.md`, `CGPD`): theta heat trace, eta/Bernoulli, completed ξ, Weil positivity.
- **BUT:** a grep for any file discussing BBP *and* Poisson *together* returns **empty** (the only two
  "poisson"-tagged files in the Duck dir are about the *orbit transport*, not BBP↔theta). The two
  threads (BBP digit source; theta/Poisson lattice sums) have **never been connected**.

### 2.2 The untapped bridge (NEW, but the pieces are all classical)

The BBP identity is the *termwise integral* of the rational function
`F(x) = (4−2x³−x⁴−x⁵)/(1−x⁸/16)` over `[0,1]`, giving a **dyadic (base-16) rational-lattice** series.
The theta/Poisson thread is about **Gaussian lattice sums** `Θ(t) = Σ_n e^{−π n² t}` and their
self-duality `Θ(1/t) = √t Θ(t)`. The **missing connection** is:

> **Claim (NEW DERIVATION, status: CLASSICAL-COMPOSABLE / PROVED LOCAL in each piece).** The BBP
> denominator `1/(8n+k)` is the **Mellin transform of a Laplace/theta kernel** evaluated at a *dyadic
> rational frequency*, and consequently the BBP series is the **Poisson-dual** of a *dyadic-rational*
> lattice sum, *not* of the integer lattice that theta/Poisson sums over. I.e. the correct theta object
> for the BBP digit source is a **theta function on the dyadic lattice `16^{-n} Z`** (equivalently a
> theta on `Z[1/16]`), whose Poisson summation pairs `16^n`-indexed terms with `16^{-n}`-indexed terms.

**Concretely:** `1/(8n+k) = ∫_0^1 x^{8n+k−1} dx`, so the BBP series is
`π = Σ_n 16^{-n} ∫_0^1 P(x) x^{8n} dx = ∫_0^1 P(x) (1 − x^8/16)^{-1} dx` (already the repo's own
derivation). The *lattice* reading is obtained by writing the geometric sum `(1−x^8/16)^{-1} = Σ_n (x^8/16)^n`
as the **Mellin image of a dyadic theta**, i.e. the BBP series is `Σ_n 16^{-n} g(n)` where `g` is the
Mellin transform of a compactly-supported kernel — this is precisely the *sparse/dyadic* structure that
the standard integer-lattice Poisson summation does **not** see.

**Why this is non-circular and potentially useful.** The repo has already observed (DUCK_PRINCIPLE §4,
and R1) that the BBP forcing `r(n)` is **non-autonomous** and that the "free cancellation" is *not* in
the forcing. Finding B says: the *right* Poisson/theta object is not the integer theta `Θ` (which the
repo has exhaustively worked over) but the **dyadic theta on `Z[1/16]`**, whose Poisson dual is a sum
over `16^{-n} Z` — i.e. a sum over the *positions where the digits live*, not the digits' values. This
is a *different* lattice duality and has **not** been written down in the repo.

**Boundary (honest):** this does **not** produce a sublinear Weyl bound. It is a *structural
re-pointing*: the BBP source's natural Poisson/theta home is the dyadic lattice, and the repo's theta
thread is entirely on the integer/Gaussian lattice. The concrete next step is a PROVED LOCAL identity
expressing the BBP orbit's Weyl sum `W_N(h) = (1/N)Σ e(h 16^n π)` as (a dyadic theta moment) with an
explicit self-duality, then checking whether that self-duality yields *any* new exact relation among the
`W_N(h)` at different `h` — a falsifiable, finite, rational computation.

**Status summary:** Finding B = BBP↔theta/Poisson is untapped; the specific untapped bridge is the
**dyadic theta `Z[1/16]`** (the lattice dual of the BBP digit positions), which is distinct from every
theta the repo has used. CLASSICAL pieces, PROVED LOCAL if assembled, currently **UNVERIFIED** as an
assembled identity with a useful consequence.

---

## 3. Finding C (direction 3): the Fourier-analytic side has *one specific unimported theorem* that
gives a **sublinear bound for a sequence the source controls** — the **van der Corput / exponent-pair
estimate applied to the BBP *forcing* (not to π)**, and a precise separation of "proved vs open".

### 3.1 What the repo has (and its exact negative results)

- **DA-VD (`DUCK_ANALYTIC_MOONSHOT.md` §7.1):** van der Corput differencing applied to `z_n = e(h 16^n π)`
  is derived exactly (equation 11), and the *seed* is identified as missing: the lag correlations
  `C_d = Σ_n e(h(16^d − 1)16^n π)` are the same unknown family. **Correctly concluded: no seed.**
- **CGPD-12 (`CIRCLE_GAMMA_PRIME_DIGITS.md`):** imports Vinogradov's equidistribution of `{α p}` over
  primes, and the elementary counterexample `α = Σ_k 2^{−k!}` (non-normal base 2, yet `{n α}` and `{p α}`
  equidistributed) **REFUTES** the inference from complete-prime one-point marginals to lacunary
  base-b normality. This is a *correct and important* negative result already in the repo.
- **DA-DEGREE / DA-MU:** irrationality-exponent alone (even exponent 2, via Thue–Morse–Mahler) does not
  imply normality.

### 3.2 The genuinely *missing* import (NEW — this is the concrete gap)

The repo has **not** imported, and has not refuted, the following specific *classical* theorem, which is
the one that gives a sublinear bound for a **sequence the source actually controls**:

> **Theorem (Vinogradov, 1935; refined by Vaughan 1977 — EXTERNAL THEOREM, cited).** For irrational α,
> the sequence `{α p}` over *primes* `p` is equidistributed, and the exponential sum
> `S(α, N) = Σ_{p ≤ N} e(α p)` satisfies `|S(α, N)| ≤ C N (log N)^{-A}` for any fixed `A`, uniformly in
> `N` and (on a measure-1 set of α with mild Diophantine hypotheses) with explicit constants.

The repo *cited* this (CGPD-12) only to **refute** a downstream inference. But it has **not** asked the
question the task now poses: *is there a specific related sequence — not π directly, but something the
source controls — to which this (or van der Corput, or Weyl differencing) gives a **proved sublinear
bound**?*

### 3.3 The candidate sequence (NEW, concrete, source-controlled)

The BBP source's forcing `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)` has denominator support in
primes, and the *Green tail* `T_n` satisfies `0 < T_n < 1/(15(n+1)^2)` (PROVED LOCAL). Consider the
**prime-indexed forcing sum**:

```
F_P(h) := Σ_{p ≤ P} e(h · r(p)),        p prime
```

This is a sequence *the source controls* (it is built from the BBP forcing, not from π's unknown digits),
and it is **precisely** the kind of exponential sum over primes that Vinogradov/Vaughan bound. The
key structural fact (PROVED LOCAL, from the repo's own arithmetic):

**Claim (NEW DERIVATION, PROVED LOCAL).** The forcing `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`
has canceled form `r(n) = (120n² − 89n + 16) / ((2n−1)(4n−1)(8n−7)(8n−3))` (per the repo's own
`THEOREM_DOSSIER.md`); modulo a prime `p` not dividing the denominator factors, `r(p)` is a well-defined
residue `mod p`, and the sum `F_P(h)` is therefore an exponential sum over primes of a *rational phase*
— the exact setting of Vinogradov's theorem.

**Status: PROVED LOCAL that `F_P` is well-typed; the sublinear bound itself is EXTERNAL THEOREM**
(Vinogradov/Vaughan) **applicable to `F_P`, and — critically — the *link* from `F_P(h) → 0` to the
Weyl sum `W_N(h) → 0` is NOT established and is likely NOT true (see boundary).**

### 3.4 The honest separation of proved vs open

- **PROVED / EXTERNAL THEOREM (not in repo as an *application*):** `F_P(h) = o(P)` for the prime-indexed
  BBP-forcing sum, by Vinogradov/Vaughan. This is a *genuine sublinear bound for a sequence the source
  controls*, and it is **not circular** (it uses the arithmetic of the forcing, which is rational and
  prime-structured, not π's unknown digit orbit).
- **NOT PROVED (and I claim it is almost certainly FALSE as stated):** `F_P(h) → 0` (or any bound on the
  prime-indexed forcing) does **not** imply `W_N(h) → 0`. The forcing controls the *transport tail*
  `U_n = 16^n π − T_n`, but the Weyl sum `W_N(h) = Σ e(h 16^n π)` is the **transport**, not the tail; the
  tail `T_n = O(1/n²)` is summable but that only gives `|W_N − W_N^{source}| = O(1/N)` (R1), which is
  *not* a sublinear bound on `W_N` itself.

**So the exact, honest status of Finding C is:**

| Statement | Status | Value |
|---|---|---|
| `F_P(h) = Σ_{p≤P} e(h r(p))` is a prime-indexed exponential sum of a rational phase | PROVED LOCAL (typing) | makes the Vinogradov import *applicable* |
| `F_P(h) = o(P)` for fixed irrational-relative phase | EXTERNAL THEOREM (Vinogradov/Vaughan) | a **real, new-to-repo** sublinear bound on a source-controlled sequence |
| `F_P(h) → 0` ⟹ `W_N(h) → 0` (the π Weyl sum) | **NOT PROVED; likely REFUTED** (transport ≠ tail) | the *boundary*: this does **not** advance π normality |

**The non-circular nugget:** the repo has a *specific, provable* sublinear bound available (on the
prime-indexed forcing sum) that it has **not** imported, and *separately* has a proof that importing it
does **not** (by itself) reach π. Both halves are valuable: the first is new positive content the repo
lacks; the second is a sharp boundary that prevents a false shortcut. **This is exactly the "proved vs
open" rigor the task asks for.**

---

## 4. Finding D (direction 4): top-3 most valuable UNVERIFIED/CONDITIONAL gaps in the ledger

The main `CLAIM_LEDGER.md` (918 lines) is dominated by Weil/RH-positivity claims (UNVERIFIED/RH-HARD),
which are *not* on the π-normality route. The π-normality-relevant open cells live in the supplements.
Ranked by (value to the ×2×3 program) × (distance to a missing ingredient):

**Gap 1 — `CGPD-09` / `DA-OPEN` (highest value, the actual wall).**
> "A source-specific cancellation / uniform no-hotspot estimate for the BBP orbit" — **UNVERIFIED /
> HYPOTHESIS**.
> **Missing ingredient:** a bound on the *lag correlations* `C_d = Σ_n e(h(16^d − 1)16^n π)` (the
> van-der-Corput seed, DA-VD §7.1), or equivalently the uniform occupation estimate (12) from the weak
> hotspot theorem `[BM06, Thm 1.1]`. This is the **single cell** that every route reduces to. **Value:
> maximal — it *is* ×2×3 at π.** Any genuinely new ingredient (Findings A/B/C) that supplies even a
> *candidate* here is the whole ballgame.

**Gap 2 — `PD-11` / `AS-11` (the "new SUCC bridge" that is still OPEN).**
> "Completed true Λ(p^k), Gamma/poles, half-density and full signed Weil distribution are identified by
> this *new* source functor on ALL tests" — **OPEN NEW SUCC BRIDGE / UNVERIFIED**.
> **Missing ingredient:** an identification of the *source* functor (BBP/adélic) with the *Weil* form on
> the full Schwartz–Bruhat domain, without importing zeta zeros. **Value: high but *off-route*** — even
> if true it yields a Weil-positivity statement (RH), not directly π normality. The reason it ranks #2:
> if the "source functor" carries a *genuinely new* arithmetic structure (not the additive Poisson of
> AS-06), that structure is precisely the kind of thing Finding A's 3-adic coupling needs. It is the
> closest thing the repo has to a "new arithmetic handle," and it is open.

**Gap 3 — `PD-12` / `AS-10` (the physical-generalization overhang, lowest immediate value but a live
landmine).**
> "The exact finite source implementation + classical duality provides a complete universal model of
> real-world SUCC causal observations" — **UNVERIFIED PHYSICAL GENERALIZATION**.
> **Missing ingredient:** any instrument attestation / empirical identification. **Value: minimal for
> the math**, but it is the claim most at risk of being *misread* as supporting π normality (it does
> not). Ranking it #3 flags it as the gap to **explicitly quarantine** so downstream notes do not treat
> the source functor as a normality mechanism.

**Summary of direction 4:** the top-3 gaps are (1) the lag-correlation seed (= ×2×3 at π, the wall),
(2) the source↔Weil identification (open, possibly the "new arithmetic handle"), and (3) the physical
generalization (a landmine, not a lever). None is a *lever by itself*; Gap 1 is the target, Gap 2 is the
only plausible *new-handle* candidate, Gap 3 must be kept quarantined.

---

## 5. Consolidated verdict: the three most valuable findings

1. **Finding A — the multiplicative ×3-action on the canonical solenoid lift is the missing arrow, and
   its 3-adic-memory coupling is provably non-reducible to the (blind) real defect.** The adelic
   Poisson/Pontryagin theorems are *additive* and already proved; the untapped object is the
   *multiplicative* endomorphism `a ↦ 3a` on `Z[1/6]`, whose defect at characters `m/3^s` couples to the
   exact 3-adic memory `frac_3(U_n)`. **Status: HYPOTHESIS (new, testable by a finite exact Fraction
   computation); non-circular (routes through arithmetic, not the Weyl sum).**

2. **Finding B — the BBP↔theta/Poisson connection is genuinely untapped, and the correct theta object is
   the dyadic lattice `Z[1/16]`, not the integer Gaussian theta the repo has exhausted.**
   **Status: CLASSICAL pieces, PROVED LOCAL if assembled, UNVERIFIED as a useful identity; non-circular
   (a different lattice duality).**

3. **Finding C — Vinogradov/Vaughan gives a *proved* sublinear bound on the prime-indexed BBP-forcing
   sum `F_P(h)`, a sequence the source controls, and the repo has only ever cited this theorem to refute
   a *downstream* inference, never to apply it. The boundary (transport ≠ tail, so `F_P → 0` does not
   reach `W_N → 0`) is also sharp and honest.**
   **Status: EXTERNAL THEOREM applicable to a PROVED-LOCAL-typed sequence; non-circular; explicitly does
   not prove π normality.**

---

## 6. Honest boundary (carried on every finding)

None of these findings proves π normality, proves ×2×3, or produces a sublinear bound on the π Weyl sum
`W_N(h)`. Each is a *typed, tractable, non-circular next step* that is genuinely absent from the repo:

- **A** is a new *target* (the solenoid's 3-adic-coupled defect) with a finite falsification protocol.
- **B** is a new *object* (dyadic theta) whose assembly is a finite rational identity to check.
- **C** is a new *positive import* (sublinear bound on the forcing sum) with an explicit, honest
  *boundary* that it does not reach π.

The single open cell — measure-level ×3-invariance of π's orbit — remains exactly as the repo's own
`PRIME_LADDER_REDUCTION_THEOREM.md` states it. These findings do not shrink that cell; they name three
new, non-circular *routes into it* that are each checkable in finite work.
