# Positive Carrier Realization II: the field of definition of a carrier, ghost freedom, and the audit of Part I

**Status.** Second session on the positive-carrier programme (Part I:
[`POSITIVE_CARRIER_REALIZATION_THEORY.md`](POSITIVE_CARRIER_REALIZATION_THEORY.md)).  Part I was
found uncommitted and uncommitted-by-anyone in this worktree; it was **audited line by line before
anything was built on it** (§8 records the verdict: the cone theorem, the spectral obstruction, PWₙ
and the cyclotomic clocks stand; four statements are corrected, one claimed termination property is
false and fixed).  Everything new is exact (rationals and exact `ℚ(√5)` arithmetic), reproduced
byte-for-byte by `scripts/positive_carrier_ii_probe.py` into
[`POSITIVE_CARRIER_II_RECEIPT.json`](POSITIVE_CARRIER_II_RECEIPT.json), re-executed by
`tests/test_eodcs_positive_carrier_ii.py` (19 exact tests with mutation controls) and
`tests/test_eodcs_positive_carrier_ii_receipt.py`, and kernel-checked where discrete in
`formal/EODCS_PositiveCarrierII.lean` and `formal/EODCS_PositiveCarrierCone.lean` (Lean 4.14.0 root
pin, no mathlib, no `sorry`/`axiom`; compiled in this session with the pinned toolchain;
`#print axioms` shows only `propext`, `Quot.sound`, and `Classical.choice`).  The second file closes
Part I's "Lean-ready plan": the three identities behind the cone theorem (Part I Theorem 4.1) are
verified over an arbitrary commutative semiring.  Labels follow `docs/CLAIM_LEDGER.md`; claims are
ledgered as PCR-25 … PCR-41 in `docs/CLAIM_SUPPLEMENT_POSITIVE_CARRIER.md`.
Snapshot: branch `research/positive-carrier-realization-2026-10-13`, forked from PR #53 head
`9e7589e5`.  Nothing touches `main`, PR #49's worktrees, PR #54, or any `research/swm-*` branch.

**One-paragraph answer (Part II).**  Positive realizability is not a property of a behavior alone;
it is a property of a behavior *and a field*.  A rational behavior has a positive carrier with
entries in a subfield `F ⊆ ℝ` iff its minimal realization carries an **`F`-rational** polyhedral cone
sandwiched between the closed reachable cone `R̄` and the nonnegative-prediction cone `P` and
invariant under every event (Theorem II.1).  If `R̄` and `P` touch along an **irrational extreme ray
of `P`** — an *irrational contact* — then no rational carrier exists of any size (Theorem II.2).  The
**Fibonacci cat system** (Theorem II.3) — `ℚ²`, two actions running the hyperbolic automorphism
`[[2,1],[1,1]]/4` and its inverse, each with a reset — has linear dimension 2, a 2-state carrier over
`ℚ(√5)` with transition probabilities `(3±√5)/8` and `1/4`, and **no positive carrier over `ℚ`**: the
contact rays are the golden-ratio stable and unstable directions of the automorphism.  This is the
smallest conceivable `ℚ/ℝ` separation (`r ≤ 2` forces `d⁺_ℝ = r`) and it is infinite; at `r = 2`,
`d⁺_ℚ ∈ {2, ∞}` (Theorem II.4).  On the causal side, the **ghost-freedom theorem** (II.5) shows that the
lawful positive dimension is the minimum of `d⁺` over all *lawful completions* of the operational
profile (legal values + menus), that Part I's bottom completion is only one of them, and that the
**ghost gap** `d⁺_law = 1` versus `d⁺_⊥ = 4ⁿ + 1` occurs (phantom walks, Theorem II.6): the values of
illegal partial executions, which no legal experiment measures, can cost unboundedly many states.
Operational-profile equality is decided **exactly** through the refusal completion (II.7).  Finally,
the oracle's blind spot is real and repaired (II.9–II.10): a rational behavior with `d⁺ = r = 3` whose
reachable cone has infinitely many extreme rays, found by an LP-verified grid search, and the Part I
refinement loop — which does not terminate on the Fibonacci system, where it generates Fibonacci
denominators `…, 75025, 514229, …` forever — is round-bounded.

---

## 0. Conventions (from Part I, unchanged)

Behavior `p = (p_σ)`, bottom-completed words, `p_σ(w) = τ(T_w v_σ)` on the minimal realization
`(V_min, T_{a,z}, v_σ, τ)` over `ℚ` (Part I D3, D6); `R̄` = closure of `cone{T_u v_σ}`,
`P = {x : τ(T_w x) ≥ 0 ∀w}`, both closed, convex, pointed, `T`-invariant, with `τ > 0` on
`(R̄ ∪ P) ∖ 0` (Part I Lemma 3.2).  `d⁺(p)` = minimal number of states of a positive carrier of `p`
(Part I D7); Part I Theorem 4.3 (Heller, exact form): `d⁺ < ∞` iff some polyhedral `K` with
`R̄ ⊆ K ⊆ P` is `T`-invariant.  Everything below works in `V_ℝ := V_min ⊗_ℚ ℝ`; "`F`-rational" means
"spanned by vectors with coordinates in `F` with respect to a rational basis of `V_min`".

**D-II.1 (carrier over `F`, positive dimension over `F`).**  For a subfield `F ⊆ ℝ`, a *carrier over
`F`* is a positive carrier (Part I D1) whose event matrices and preparations have entries in `F`;
`d⁺_F(p)` is the minimal number of states of a carrier over `F` realizing `p` (`∞` if none).  Clearly
`d⁺_ℝ ≤ d⁺_F ≤ d⁺_ℚ` for `ℚ ⊆ F ⊆ ℝ`.  The *field of definition* `Fld(p)` is the intersection of all `F`
with `d⁺_F(p) < ∞` (when some exists).

## 1. The rational cone theorem

**Theorem II.1 (sandwiched cone, field-sensitive form; CLASSICAL core, PROVED LOCAL).**  Let `p` be a
valid rational behavior and `F ⊆ ℝ` a subfield.  Then
`d⁺_F(p) < ∞` iff there is an `F`-rational polyhedral cone `K ⊆ V_ℝ` with `R̄ ⊆ K ⊆ P` and
`T_{a,z} K ⊆ K` for all events.  Moreover, if `K` has `m` `F`-rational generators then `d⁺_F ≤ m`.

*Proof.*  (⇐)  Normalize the generators by `τ` (positive on `K ∖ 0` since `K ⊆ P`, Part I Lemma
3.2(c)); normalization keeps them `F`-rational.  Part I Theorem 4.1 produces the carrier from
coefficients `B_{a,z}[j][i] ≥ 0` with `T_{a,z} g_i = Σ_j B_{a,z}[j][i] g_j` and `λ_σ ≥ 0` with
`v_σ = Σ λ_σ[i] g_i`; these are feasibility LPs with coefficients in `F`, and a feasible LP with
coefficients in an ordered field has a basic feasible solution in that field (it solves a linear
system with coefficients in `F`).  Hypothesis (M) is automatic on `V_min` (Part I Prop. 3.1(ii)).
Hence a carrier over `F` with `m` states.
(⇒)  Let `K'` be a carrier over `F` with `m` states and `Φ: F^{C'} → F^{Words}`, `Φ(e_c)(v) = 1ᵀ M'_v e_c`
(Part I Theorem 4.2).  The prediction functions `p_σ(u·) = Φ(M'_u π'_σ)` are `F`-combinations of the
`Φ(e_c)`, so `V_min ⊗ F ⊆ W := span_F{Φ e_c}`.  Put `K_W := cone_ℝ{Φ e_c}`, generated by `F`-vectors.
By the Weyl–Minkowski theorem over the ordered field `F` (Fourier–Motzkin elimination is
field-agnostic; Schrijver, *Theory of Linear and Integer Programming*, Thm. 7.1 and Cor. 7.1a),
`K_W = {x ∈ W_ℝ : A x ≥ 0}` with `A` an `F`-matrix, and `V_ℝ = {x : B x = 0}` with `B` rational.  So
`K := K_W ∩ V_ℝ = {x : A x ≥ 0, B x = 0}` is an `F`-polyhedral cone, hence (Minkowski over `F`)
generated by finitely many `F`-vectors: each extreme ray is the one-dimensional solution space of a
subsystem of `F`-linear equations.  `R̄ ⊆ K ⊆ P` and invariance are Part I Theorem 4.2(iii). ∎

For `F = ℝ` this is Part I Theorem 4.3; the content of II.1 is that *the same cone statement decides
realizability over every field*, with the field entering only through the rationality of `K`.

## 2. The irrational-contact obstruction

**Theorem II.2 (contact rays are extreme rays of every sandwiched cone; PROVED LOCAL).**  Let `ℓ` be a
ray with `ℓ ⊆ R̄` and `ℓ` an extreme ray of `P` (`ℓ ∈ ext P`).  Then `ℓ` is an extreme ray of every
polyhedral cone `K` with `R̄ ⊆ K ⊆ P`.  Consequently, if `d⁺_F(p) < ∞` then every such *contact ray*
is `F`-rational; contrapositively, **one irrational contact ray forces `d⁺_ℚ(p) = ∞`** (and
`Fld(p) ⊇ ℚ(coordinates of ℓ)`).

*Proof.*  `ℓ ⊆ R̄ ⊆ K`.  If `x ∈ ℓ` and `x = y + z` with `y, z ∈ K ⊆ P`, extremality of `ℓ` in `P` gives
`y, z ∈ ℓ`; so `ℓ` is extreme in `K`.  By Theorem II.1 (⇒), `d⁺_F < ∞` yields an `F`-rational
sandwiched invariant `K`, whose extreme rays are `F`-rational. ∎

This is a fourth obstruction mechanism, independent of Part I's three (support, spectrum,
availability): it is invisible to nonnegative rank (one-shot matrices of rank ≤ 2 have rational
nonnegative factorizations of size 2), to the peripheral spectrum (all spectra below are real and the
ratios are not roots of unity but the obstruction is to *rational* carriers only — a real one
exists), and to menus (all actions are total).

**Finite certificate in dimension 2 (`two_dimensional_contact_certificate`, exact in `ℚ(√D)`).**  Let
`r(p) = 2`, and let `T = T_{w_in}`, `T' = T_{w_out}` be the operators of two event words.  The routine
certifies, with exact arithmetic in the real quadratic field of the discriminant:
(C1) `T` has real irrational eigenvalues `λ > |λ'|` with `τ`-normalized dominant eigenvector `e`, and
some source `v_σ = c e + c' f` has `c > 0`; then the rays of `Tⁿ v_σ` converge to `e`, so `e ∈ R̄`
(`c ≥ 0` is automatic: `τ(Tⁿ v_σ) ≥ 0` and `τ(e) > 0`);
(C2) `e` is an eigenvector of `T'` with eigenvalue `μ`, the other eigenvalue `ν` of `T'` is real with
`ν > |μ|`, and `τ(f') ≠ 0` for the other eigenvector `f'`; then for `x = c e + c'' f'`,
`τ(T'ⁿ x) = c μⁿ τ(e) + c'' νⁿ τ(f')` has the sign of `c'' τ(f')` for large `n`, so `P ⊆ {c'' τ(f') ≥ 0}`,
a closed half-plane whose boundary is `ℝ e`; since `e ∈ P` and `τ > 0` on `P ∖ 0`, `e` is an extreme
ray of `P` (a decomposition `e = y + z` in `P ⊆ H` forces `y, z ∈ ∂H ∩ P = ℝ_{≥0} e`);
(C3) `e` is irrational (`D` is not a square).
Under (C1)–(C3), Theorem II.2 gives `d⁺_ℚ = ∞`, and Part I Theorem 5.1 gives `d⁺_ℝ = 2`.  Mutation
controls: with `w_out = w_in` the ray is dominant, not subdominant (no certificate); with the
inverse action removed from the Fibonacci system, (C2) fails and a rational two-state carrier is
found by the interval search (receipt `irrational_contact_certificate`, tests
`test_contact_certificate_mutation_controls`).

## 3. The Fibonacci cat system: `(r, d⁺_ℝ, d⁺_ℚ) = (2, 2, ∞)`

**Definition.**  `V = ℚ²`, `τ = (1, 0)`, `v_* = (1, 0)`, `A = [[2,1],[1,1]]` (det 1, `A⁻¹ = 3I − A = [[1,−1],[−1,2]]`).
Action **a**: `tick = A/4`, `reset = v_*(τ − τ·tick) = v_* (½, −¼)`.
Action **b**: `tock = A⁻¹/4`, `reset = v_*(τ − τ·tock) = v_* (¾, ¼)`.  One source `s ↦ v_*`.
`tick·tock = I/16` (the two steps commute); `tick` and the `b`-reset do not commute; the resets are
rank one (information-destroying).  Mass is conserved exactly in both actions.

Let `φ = (1+√5)/2`.  The eigenvalues of `A` are `φ² = (3+√5)/2` and `φ⁻² = (3−√5)/2` with
eigenvectors `e = (1, φ⁻¹) = (1, (√5−1)/2)` (unstable direction) and `e' = (1, −φ) = (1, −(1+√5)/2)`
(stable direction); the slopes are the two roots of `s² + s − 1`.  Both are `τ`-normalized.

**Theorem II.3 (PROVED LOCAL; LEAN-KERNEL VERIFIED number-theoretic core; exact receipts).**
(i) The behavior is valid (every word probability ≥ 0, mass conserved) and `r = 2`.
(ii) `R̄ = P = cone(e, e')`.
(iii) `d⁺_ℝ = 2`: the generators `e, e'` give the carrier
  `B_{a,tick} = diag((3+√5)/8, (3−√5)/8)`, `B_{b,tock} = diag((3−√5)/8, (3+√5)/8)`,
  `B_{a,reset} = [[¼, (3+√5)/8],[(3−√5)/8, ¼]]`, `B_{b,reset} = [[(3+√5)/8, ¼],[¼, (3−√5)/8]]`,
  `λ_s = (½ + √5/10, ½ − √5/10)`; all columns sum to 1, all entries positive, verified exactly in
  `ℚ(√5)` (`golden_carrier`).
(iv) `d⁺_ℚ = ∞`, and `Fld(p) = ℚ(√5)` exactly.

*Proof.*  (i) Every event maps `cone(e,e')` into itself: `tick` and `tock` are diagonal in the basis
`(e, e')` with positive eigenvalues `(3±√5)/8`; the reset functionals are positive on both rays —
`(½, −¼)·e = (5−√5)/8`, `(½, −¼)·e' = (5+√5)/8`, `(¾, ¼)·e = (5+√5)/8`, `(¾, ¼)·e' = (5−√5)/8` — and
`v_* = c e + c' e'` with `c = ½ + √5/10 > 0`, `c' = ½ − √5/10 > 0`.  Since `τ = (1,0)` is positive on
`cone(e,e')` and `v_*` lies in it, every `τ(T_w v_*) ≥ 0`.  Mass conservation is by construction of
the resets.  Minimality: `v_*` and `tick·v_* = (½, ¼)` span; `τ` and `τ·tick = (½, ¼)` separate; so
`r = 2`.  (Receipt: 21,844 words of length ≤ 7 exact-nonnegative; orbit slopes `0, ½, 3/5, 8/13, 21/34, 55/89, …`
under `tick`, `0, −1, −3/2, −8/5, −21/13, …` under `tock` — ratios of consecutive Fibonacci numbers.)
(ii) `R̄ ⊆ cone(e,e')` by (i).  `tickⁿ v_* / (φ²/4)ⁿ → c e` with `c > 0`, so `e ∈ R̄`; `tockⁿ v_*` likewise
gives `e' ∈ R̄`; convexity gives `cone(e,e') ⊆ R̄`.  `cone(e,e') ⊆ P` by (i).  For `x = c e + c' e'`:
`τ(tickⁿ x) = 4^{−n}(c φ^{2n} + c' φ^{−2n})` is negative for large `n` if `c < 0`, and
`τ(tockⁿ x) = 4^{−n}(c φ^{−2n} + c' φ^{2n})` is negative for large `n` if `c' < 0`; so `P ⊆ cone(e,e')`.
(iii) Part I Theorem 4.1 with `K = cone(e,e')` (`(N)` holds, `(P)` by (ii), `(I)` by (i), `(M)` automatic);
the explicit matrices are solved exactly in `ℚ(√5)` by Cramer's rule and re-verified.
(iv) By (ii), `e` is an extreme ray of `P` and lies in `R̄`: an irrational contact ray (its slope
satisfies `s² + s − 1 = 0`, which has no rational root — rational-root theorem on `±1`, and
kernel-checked as `golden_slope_irrational`: no integers `p, q` with `q ≠ 0` and `p² + pq − q² = 0`,
proved by descent through `x² = 5y² ⇒ y = 0`).  Theorem II.2 gives `d⁺_ℚ = ∞`.  For any `F` with
`d⁺_F < ∞`, `e` is `F`-rational, so `√5 ∈ F`; and `d⁺_{ℚ(√5)} = 2` by (iii).  Hence `Fld(p) = ℚ(√5)`. ∎

**Interpretation.**  A SUCC observer whose predictions are exact rationals — every `p_σ(w)` here is a
rational number — may be *unable to carry them in any exact-rational device*: every lawful positive
realization of this behavior must have the golden ratio inside its transition probabilities.  The
carrier constrains the representation at the level of its number field, not only its dimension.
Dynamically: the carrier must contain the stable and the unstable manifold of the cat map as extreme
rays, because the observer can run the map forwards (action **a**) and backwards (action **b**).

**Remark (what the inherited Part I claimed here).**  Part I Prop. 4.5(b)/PCR-09 transferred the
Chistikov–Kiefer–Marušič–Shirmohammadi–Worrell one-shot matrix to a behavior with `d⁺_ℝ = 6`,
`d⁺_ℚ = 7`, and Remark 5.2 left the `r = 2` case open ("smallest candidate for a ℚ/ℝ gap").  Theorem
II.3 replaces this: the gap exists at the smallest possible linear dimension and is infinite, and
its mechanism is dynamical (contact of the two canonical cones along an irrational eigen-direction),
not combinatorial.

## 4. The dimension-two dichotomy

**Theorem II.4 (PROVED LOCAL).**  Let `p` be a valid rational behavior with `r(p) = 2`.  Then
`d⁺_ℝ(p) = 2` and `d⁺_ℚ(p) ∈ {2, ∞}`; `d⁺_ℚ = 2` iff some rational sector `[p_1, p_2]` of the
`τ`-slice contains the reachable slice, lies in the prediction slice, and is mapped into itself by
every event (`rational_interval_invariance`).

*Proof.*  `d⁺_ℝ = 2` is Part I Theorem 5.1.  If an `ℚ`-rational sandwiched invariant polyhedral cone
exists it is a sector with two rational extreme rays (pointed, full-dimensional since it contains `R̄`
which spans `V`), so Theorem II.1 gives a rational carrier with 2 states; otherwise II.1 gives
`d⁺_ℚ = ∞`.  Invariance of a sector is checked on its two generators: `T_{a,z} g_i` is either `0` or a
positive multiple of a point of the slice (τ > 0 on `K ∖ 0`), and the slice point must lie in the
interval. ∎

The positive control: the bottom-completed FINE carrier of Part I's availability square has `r = 2`
and the interval search returns the rational sector `[0, 2]` with an exactly equivalent 2-state
carrier (receipt `dimension_two_dichotomy_positive_control`).  On the Fibonacci system the search
over all rational endpoints with denominators ≤ 6 and `|p| ≤ 3` returns UNRESOLVED — correctly, since
the only admissible sector is `cone(e, e')` — and the three intervals `[−2, 1]`, `[−1.7, 0.7]`,
`[−55/34, 55/89]` fail explicitly (the last is the pair of Fibonacci convergents on each side: it
contains neither `e'` nor `e`, which lie strictly beyond every convergent).  A full *decision*
procedure at `r = 2` would need the endpoints of the reachable slice as real algebraic numbers and
their attracting/repelling multipliers; it is stated as the next lemma in §12, not claimed.

## 5. Ghost freedom: the lawful positive dimension is a minimum over completions

Part I defined, for a lawful carrier `K` with enabled sets `E_a`: the *bottom completion* `p_⊥(K)`
(refusal mass = mass of the current law outside `E_a`; the outcomes `z ≠ ⊥` of an unavailable action
keep the *partial-execution* values `1ᵀ M_{a,z}(x|_{E_a})`), `d⁺_⊥(K) := d⁺(p_⊥(K))`, and the *lawful
positive dimension* `d⁺_law(K)` := min states of a lawful carrier with the same legal values and the
same legality pattern (Part I D7), proving `d⁺_law ≤ d⁺_⊥` and leaving strictness open (PCR-19).

**D-II.2 (operational profile).**  `Π(K)` consists of the set `L(K)` of legal `(σ, u)` with
`p_σ(u) > 0`, the values `p_σ(u)` on `L(K)`, and the menu `Menu(σ,u) = {a : supp(M_u π_σ) ⊆ E_a}`.
The values `p_⊥(u a z)` for `a ∉ Menu(σ,u)` are **ghosts**: no legal experiment measures them (the
word is illegal), and by Part I Theorem 8.2 every public-history policy, closed-loop law and source
posterior is a function of `Π(K)` alone.

**D-II.3 (lawful completion).**  A total bottom-completed behavior `p'` is a *lawful completion* of
`Π(K)` if (i) `p'_σ(u) = p_σ(u)` on `L(K)`; (ii) for `(σ,u) ∈ L(K)` and every action `a`,
`p'_σ(u a ⊥) = 0` iff `a ∈ Menu(σ,u)`; (iii) `p'` is the complete behavior of some finite positive
total carrier.  (By (ii) and induction, legality in `p'` coincides with legality in `K`.)  `p_⊥(K)` is
a lawful completion (Part I Prop. 8.1).

**Theorem II.5 (ghost freedom; PROVED LOCAL).**  `d⁺_law(K) = min { d⁺(p') : p' a lawful completion of Π(K) }`.

*Proof.*  (≥)  A lawful carrier `K'` of `Π(K)` with `m` states has a bottom completion `K'_⊥`, a total
`m`-state carrier whose behavior satisfies (i) (legal words run through enabled states only, where
`K'` and `K'_⊥` agree), (ii) (Part I Prop. 8.1 in `K'`, whose menus are those of `K` by assumption) and
(iii).  (≤)  Let `K̃` be a total carrier with `m̃` states of a lawful completion `p'`.  Define
`E_a := {c : 1ᵀ M̃_{a,⊥} e_c = 0}` (zero refusal mass) and `K''` := `K̃` with, for each `a` and `z ≠ ⊥`,
the columns of `M̃_{a,z}` on `C̃ ∖ E_a` set to zero.  Mass law: on `E_a` the outcome columns sum to
`1 − 0 = 1`; off `E_a` they are zero.  For `(σ,u) ∈ L(K)` the law of `K''` after `u` equals that of `K̃`
(induction: a legal step uses an action with `p'(…a⊥) = 0`, so every supported state is in `E_a` and
its columns are untouched), hence the legal values agree with `p' = p`; and
`a ∈ Menu_K(σ,u) ⟺ p'(ua⊥) = 0 ⟺ supp ⊆ E_a ⟺ a` uniformly available in `K''`.  So `K''` is a lawful
carrier of `Π(K)` with `m̃` states. ∎

Thus the lawful realization problem is a *completion* problem: choose the ghost values to minimize
positive dimension.  The same holds for the linear dimension: `r_law(Π) := min_{p'} r(p')` can be
strictly below `r(p_⊥(K))` (below: 1 versus 4), so even the "linear predictive dimension" of a
partial-availability behavior is ghost-dependent and the honest invariant is the minimum.

## 6. The ghost gap: phantom walks

**Definition (PHₙ, `phantom_walk_carrier`).**  States `{g} ⊔ {1,…,4}ⁿ`; action **a** = the lazy path walk
with reported position tuple (Part I PWₙ), **enabled on the walk states only**; action **b** = the
silent coordinatewise swap, identity on `g`, total.  Source `σ = ½ δ_g + ½·uniform(walk)`.  Since `g`
stays in every legal support, **a** is never available at `σ`: all its outcome values are ghosts.
Variant with a *legal source*: an extra state `h` on which **a** is enabled, reports the fixed tuple
`0ⁿ` and keeps `h`; second source `η = δ_h`, at which **a** is legal.

**Theorem II.6 (ghost gap; PROVED LOCAL; exact receipts for n = 1, 2).**
`d⁺_law(PHₙ) = 1` and `d⁺_⊥(PHₙ) = 4ⁿ + 1`.  With the legal source, `d⁺_law = 2` and `d⁺_⊥ ≥ 4ⁿ + 1`.
In particular Part I's PCR-19 ("the weakest source-preserving repair is to realize the bottom
completion") is **REFUTED**: the bottom completion is the canonical completion *determined by `K`*,
not the weakest; the ghost values it insists on can cost `4ⁿ` states.

*Proof.*  Profile of PHₙ at `σ`: the legal histories are the **b**-words, each with value 1 and menu
`{b}`.  The one-state carrier (**a** disabled, **b** total) has the same profile — decided exactly by
Prop. II.7 below (receipt `ghost_freedom.PHn.same_operational_profile = true`) — so `d⁺_law = 1`.
Lower bound for the bottom completion: in any total carrier `K̃` of `p_⊥(PHₙ)`, after the ghost word
`(a, z)` the law is `(2·4ⁿ)^{−1} δ_z` on the walk, where **a** is enabled, so `p_⊥(a z a ⊥) = 0` and the
law after `(a,z)` is supported on `a`-live states (refusal mass 0).  The one-step ghost block
`H[(σ,(a,z)), (a,z')] = p_⊥(az\,az') = (2·4ⁿ)^{−1} P^{⊗n}[z][z']` therefore factors nonnegatively through
the live states, so there are at least `rank₊(P^{⊗n}) ≥ 4ⁿ` of them (Part I's product fooling set,
kernel-checked in general form as `fooling_set_bound`); and `p_⊥(a⊥) = ½ > 0` forces a state of
`supp π̃_σ` with positive refusal mass, which is not live.  Hence `|K̃| ≥ 4ⁿ + 1`; PHₙ itself has
`4ⁿ + 1` states.  With the legal source there are two menus (`{b}` at `σ`, `{a,b}` at `η`), so
`d⁺_law ≥ 2` by the menu-count bound (Part I Lemma 8.4, kernel-checked as `menu_count_bound`), and the
two-state carrier `minimal_lawful_phantom(·, legal_source=True)` attains it (exact profile equality
in the receipt). ∎

The ghost block for PH₁ is `(1/16)·P` (rank 3, fooling set `{(1,1),(2,3),(3,2),(4,4)}`, refusal mass
½ → bound 5 = |PH₁|); for PH₂ it has rank 9 and a product fooling set of size 16 (bound 17 = |PH₂|).
Linear dimensions: `r(p_⊥(PH₁)) = 4`, `r(p_⊥(PH₂)) = 10`, while the one-state completion has `r = 1`.

**Lawfulness of the collapse.**  A public-history controller never sees the difference: the policy
"execute **a**" is illegal at `σ` in both PHₙ and its one-state carrier (`closed_loop_law` raises in
both), legal policies have identical closed-loop laws, and the **public menu** — the actions available
for *every* source compatible with the public history, `public_menu` — is `{b}` at the empty history
and `{a,b}` after a report at the legal source (receipt).  Offering an action that some compatible
source cannot execute would make the menu a hidden-source sensor (PR #53 CAR-07); the public menu is
the operational object, and it is a function of `Π`.

## 7. Refusal completion: deciding profile equality exactly

**D-II.4 (refusal completion `p̃`).**  `p̃_σ(u) = p_σ(u)` on legal words; for `(σ,u)` legal and
`a ∉ Menu(σ,u)`: `p̃_σ(u a ⊥) = p_σ(u)` and `p̃_σ(u a z) = 0` for `z ≠ ⊥`; after a refusal the state is
unchanged (`p̃(u a ⊥ v) = p̃(u v)`); for `a ∈ Menu`, `p̃(ua⊥) = 0`.  "If any supported state refuses, the
whole experiment refuses."

**Proposition II.7 (PROVED LOCAL; exact implementation).**
(a) `p̃(K)` is a function of `Π(K)` alone, and `Π(K)` is recovered from `p̃(K)` (legal histories = ⊥-free
words of positive value; menus = `{a : p̃(ua⊥) = 0}`).
(b) `p̃(K)` is realized by the **support-uniform completion** `SU(K)`: states `(c, S)` with `S` a
legally reachable support, transitions `(c,S) →_{a,z} (c', S')` with weight `M_{a,z}[c'][c]` when
`S ⊆ E_a` (where `S' = ⋃_{c∈S} supp(M_{a,z} e_c)` depends on `S` only), and `(c,S) →_{a,⊥} (c,S)` with
weight 1 when `S ⊄ E_a`.  `|SU(K)| ≤ |C|·2^{|C|}`; in practice far fewer (PW₁: 8; FINE: 3; PH₂: 17).
(c) `Π(K₁) = Π(K₂)` iff `SU(K₁)` and `SU(K₂)` are behaviorally equivalent, which Part I's exact
difference-realization closure decides (`profile_equivalence_certificate`).  A negative answer comes
with a distinguishing `(σ, w)`, classified as a *legal value difference* (the word is legal in both)
or a *menu difference* (illegal in one); ghost values never appear.
(d) `p̃(K)` is itself a lawful completion, so `d⁺_law(K) ≤ d⁺(p̃(K)) ≤ |C| 2^{|C|}`.

*Proof.*  (a) is the definition read in both directions.  (b) Induction on the legal word: the law of
`SU(K)` after `u` is `Σ_c x_c δ_{(c, supp x)}` with `x = M_u π_σ`; a step with `supp x ⊆ E_a` reproduces
`M_{a,z} x` with the correct new support (nonnegativity makes the support of `M x` the union of the
column supports over `supp x`); a step with `supp x ⊄ E_a` refuses with total mass `τ(x)` and keeps
the state.  (c) ⇐ by (a) (`p̃` is a function of `Π`); ⇒ since `Π` is recovered from `p̃`.  (d) (i)–(iii)
hold by (a),(b). ∎

Negative control: Part I's availability square — FINE and COARSE agree on every legal probability —
is separated by the certificate at `(mixed, b·ok)` with `p̃₁ = 0`, `p̃₂ = 1`, classified `menu_difference`
(`b` is illegal at `mixed` in FINE).  Positive controls: PW₁ and its 4-state cone carrier, PHₙ and its
one-state carrier, PH₁ (legal source) and its two-state carrier.

**Corrected repair statement (replaces Part I Prop. 8.5 / PCR-19).**  Given a carrier `K` and a
quotient `q` failing the availability square, the *weakest* source-preserving repair is the coarsest
lawful carrier of `Π(K)`, i.e. the minimizer in Theorem II.5; Part I's CAR-4 refinement `q*` with the
enabledness component iterated to its fixed point is the weakest *quotient* repair (a partition is a
special lawful completion), and realizing `p_⊥(K)` is the canonical repair that additionally preserves
`K`'s ghost values — a stronger demand that no legal experiment can justify and that can cost `4ⁿ`
states.  Which one is "weakest" is therefore a modelling decision: Part II's answer is that the
observer-relevant invariant is `Π(K)` (equivalently `p̃(K)`), and the realization-theoretic cost is the
minimum over completions.

**Two SUCC modules already embody the two completions.**  F48's `extend_fiber`
(`swarm_lawful_history.py`) silently *drops* configurations on which an action is disabled — the
partial-execution semantics of the bottom completion — while PR #53's `ActualHistory.advance`
*refuses* the action — the refusal semantics of `p̃`.  Part II shows that these are two lawful
completions of the same profile, that they agree on everything a public-history policy can see, and
that their realization costs can differ by `4ⁿ` states.

## 8. Audit of Part I

Every theorem of Part I was re-derived; the receipt and tests were re-executed; the Lean file was
compiled with the pinned toolchain in this session.

| Part I item | Verdict | Action in Part II |
|---|---|---|
| Thm 4.1–4.3 (cone theorem, Heller form), Lemma 3.2, Prop 3.1 | **SOUND** | strengthened to the field-sensitive form II.1 |
| Thm 6.1 (peripheral spectrum, word-indexed), Cor 6.2 | **SOUND** (sub-quotient and mass-growth argument checked) | unchanged |
| Thm 7.1 (PWₙ: 3ⁿ vs 4ⁿ), Thm 7.3 (C_k: 1+φ(k) vs k), Thm 7.2 (rational clock, d⁺ = ∞) | **SOUND** | general fooling theorem kernel-checked (II Lean §1) |
| Thm 5.1 (r ≤ 2 ⇒ d⁺_ℝ = r) | **SOUND** over ℝ | ℚ-side settled: II.3/II.4 (gap exists, infinite) |
| Remark 5.2 / PCR-05 (ℚ risk at r = 2 "UNVERIFIED") | **RESOLVED** | Theorem II.3: `d⁺_ℚ = ∞` at `r = 2` |
| Prop 4.5(b) / PCR-09 (CKMSW transfer, 6 vs 7) | **SOUND but superseded** | II.3 is smaller (r = 2) and infinite |
| Prop 4.6 / PCR-22 "`reachable_cone_refinement` terminates" | **FALSE as implemented** | on the Fibonacci system the generator count stays at 4 while every round replaces the two outer rays by the next Fibonacci convergents (denominators `F_k`: …, 75025, 514229, …); the loop never ends. Fixed: `max_rounds`; Part I receipt unchanged |
| Prop 8.5 / PCR-19 "weakest repair = bottom completion; d⁺_law < d⁺_⊥ UNVERIFIED" | **REFUTED** (first clause) / **RESOLVED** (second) | Theorems II.5–II.6; corrected statement in §7 |
| §14 "next experiment": contractive rotation as the blind-spot candidate | **MISCHOSEN** | the orbit of a contractive rotation spirals *inside* the hull of its first turn, so its reachable cone is polyhedral and the Part I refinement finds the carrier; the genuine blind spot needs a convex-curve orbit (II.9) |
| Integration map label "E40/CT10" for `carrier_hankel_bounds.py` | **MISLABELED** | the module is CT10 (O379/O380); E40 is the atlas entry on projection zeros |
| Prop 8.1, Thm 8.2, Prop 8.3, Lemma 8.4, Lemma 7.4, Prop 8.7, Remark 8.8 | **SOUND** | Lemma 8.4 kernel-checked (`menu_count_bound`) |

## 9. The oracle's blind spot, exhibited and repaired

**Example II.9 (diagonal contraction, `diagonal_contraction_system`).**  `V = ℚ³`,
`tick = diag(½, ¼, ⅛)`, `τ = (1, ⅛, ⅛)`, `v_* ∝ (1,1,1)`, `reset = v_*(τ − τ·tick)`, silent `b = v_* τ`,
sources `s₀ = (1,0,0)` and `s_*`.  Then `r = 3`, and:
* The reachable rays are `tickⁿ v_* ∝ (1, 2^{−n}, 4^{−n})` and `s₀` — slice points `(t, t²)`, `t = 2^{−n}`,
  and `(0,0)`, all on the parabola `y = x²`.  Every point of a strictly convex curve is an extreme
  point of the convex hull of any subset of the curve containing it, so **`R̄` has infinitely many
  extreme rays and is not polyhedral** (receipt: the first eight orbit rays are each outside the cone
  of the others plus the axis, exact LP).  Consequently the reachable-ray refinement of Part I adds
  the next orbit point every round and never returns a carrier (verdict UNRESOLVED, budget).
* The simplicial cone over the triangle with slice vertices `(1,1), (−2,1), (1,−2)` is sandwiched and
  invariant: `tick` acts on the slice as `(x,y) ↦ (x/2, y/4)`, mapping the vertices to
  `(½,¼), (−1,¼), (½,−½)`, all inside `{x ≤ 1, y ≤ 1, x + y ≥ −1}`; the reset coefficient
  `τ(g) − τ(tick·g) ∝ 32 + 6x + 7y > 0` on the triangle; `v_*` is a vertex; `s₀` is the origin.  Exact
  LP verification and an equivalence certificate give a **3-state rational carrier: `d⁺ = r = 3`**.
* `simplicial_grid_search` (vertices on the integer grid `|x|,|y| ≤ 2` of the ambient slice, each
  candidate verified by LP) finds a different integer triangle after 169 candidates in 0.08 s.

So the gap `d⁺ − r` can vanish while no finite set of *reachable* rays generates an invariant cone: the
Part I search is incomplete even for gap-free behaviors.  The grid search is sound (every hit is a
verified carrier) and, like all searches here, never emits an impossibility verdict.

**Theorem II.10 (termination, corrected form of Part I Prop. 4.6; PROVED LOCAL).**  Each round of
`reachable_cone_refinement` is finite (finitely many exact LPs, Bland's rule); the number of rounds
is not bounded by the generator budget (Fibonacci creep, §8), and is now bounded by `max_rounds`.
Soundness is unchanged: LAWFUL_REALIZATION only after an exact invariance proof and an independent
equivalence certificate.

**The Part II oracle** `carrier_realization_oracle_ii` composes, without touching Part I's code
paths: Part I verdicts → simplicial grid search (ambient grid) → for `r = 2` the rational interval
search → for `r = 2` the irrational-contact certificate over all ordered pairs of single-event words,
returning `FINITE_OBSTRUCTION` with `field = "Q"` and the explicit real dimension 2, so that a
`ℚ`-impossibility is never read as an `ℝ`-impossibility.  Smoke tests: Fibonacci →
`FINITE_OBSTRUCTION/Q`; diagonal contraction → `LAWFUL_REALIZATION`, 3 states; PW₁ → 4 states; rational
clock → spectral `FINITE_OBSTRUCTION`; FINE → 2 states.

## 10. Formal status (Part II)

| Statement | Where | Status |
|---|---|---|
| General fooling-set bound: `k` positive pairwise-fooling cells in a nonnegative integer factorization with `m` terms ⇒ `k ≤ m` (any shape, any `k`) | `EODCS_PositiveCarrierII.lean: fooling_set_bound` (pigeonhole `fin_injective_le` proved from scratch) | LEAN-KERNEL VERIFIED (axioms: propext, Quot.sound, Classical.choice) |
| `p² + pq − q² ≠ 0` for integers with `q ≠ 0` (golden slopes irrational), via `x² = 5y² ⇒ y = 0` by descent | `golden_slope_irrational`, `sqrt5_descent`, `five_dvd_of_five_dvd_sq` | LEAN-KERNEL VERIFIED (axioms: propext, Quot.sound) |
| Menus are functions of supports ⇒ at most `2^m` distinct menus (Part I Lemma 8.4) | `menu_count_bound`, `supportCode_injective` | LEAN-KERNEL VERIFIED |
| Theorems II.1, II.2, II.4, II.5, II.7, II.10 | this dossier | PROVED LOCAL (paper proofs over classical ingredients: Weyl–Minkowski over ordered fields, LP basic solutions) |
| Theorem II.3 (i)–(iv), Theorem II.6, Example II.9 | this dossier + receipt + tests | PROVED LOCAL / TESTED (exact ℚ and ℚ(√5) arithmetic; Lean for the number-theoretic core) |
| Theorem 4.1's three identities — word intertwining `T_w G = G B_w`, behavior transport `τ(T_w Gλ) = 1ᵀB_w λ` under `τG = 1ᵀ`, and column-stochasticity of `B` from mass conservation on generators — over any commutative semiring (`CSR` structure instantiated at ℕ and ℤ; ℚ, ℝ are instances by the field axioms, not constructed in core Lean 4.14) | `EODCS_PositiveCarrierCone.lean: word_intertwine`, `behavior_transport`, `column_stochastic` (matrix algebra `mmul_assoc`, `dot_mvec`, `ident_mmul` from scratch) | LEAN-KERNEL VERIFIED (axioms: propext, Quot.sound, Classical.choice via `funext`); nonnegativity of `B`, `λ` is the cone-membership hypothesis, not an identity, and is not restated |

Mutation controls recorded in tests: a contact certificate with `w_out = w_in` fails (ray dominant
both times); the Fibonacci system without its inverse action loses (C2) and acquires a rational
2-state carrier; shrinking the blind-spot triangle so that it misses `v_*` breaks the cone; the
rational-root check on `x² − 3x + 2` finds a root.

## 11. Prior-art crucible and novelty verdict (Part II)

**Classical / external, not claimed.**  Weyl–Minkowski and Farkas over ordered fields (Schrijver
1986, Ch. 7); basic feasible solutions of LPs lie in the coefficient field; Heller 1965 /
Schönhuth 2009 (real cone criterion); Part I's catalogue (Carlyle–Paz, Fliess, Jaeger, Singh–James–
Rudary, Thon–Jaeger, Fox–Rubin, Benvenuti–Farina, Vidyasagar, Huang–Ge–Kakade–Dahleh, Ohta,
Taghavian–Sjölund).  Rationality of nonnegative factorizations: Chistikov, Kiefer, Marušič,
Shirmohammadi, Worrell, *Nonnegative matrix factorization requires irrationality*, SIAM J. Appl.
Algebra Geom. 1 (2017) (ICALP 2016 version: restricted NMF), and Shitov, *A universality theorem for
nonnegative matrix factorizations* (arXiv:1606.09068): one-shot matrices whose minimal NMF needs
irrational entries.  Refusal/acceptance semantics of processes: Brookes–Hoare–Roscoe failures (1984),
Hennessy's acceptance trees (1985), Phillips' refusal testing (1987) — the support-uniform completion
is a probabilistic refusal determinization.  Polyhedral invariant synthesis and its incompleteness:
Cousot–Halbwachs 1978; template polyhedra (Sankaranarayanan–Sipma–Manna 2005).

**Newly proved SUCC specializations (PROVED LOCAL unless marked).**
1. Theorem II.1: the sandwiched-cone criterion is field-sensitive, and the field enters only through
   the rationality of the cone.
2. Theorem II.2: the irrational-contact obstruction, a fourth mechanism independent of support,
   spectrum and availability; its exact `ℚ(√D)` certificate in dimension 2.
3. Theorem II.3: the Fibonacci cat system, `(r, d⁺_ℝ, d⁺_ℚ) = (2, 2, ∞)`, with the explicit
   `ℚ(√5)` carrier and `Fld = ℚ(√5)` (Lean core).
4. Theorem II.4: the `r = 2` dichotomy over `ℚ`.
5. Theorems II.5–II.6: ghost freedom and the unbounded ghost gap; the refutation of "bottom completion
   is the weakest repair".
6. Proposition II.7: exact decision of operational-profile equality via the refusal completion.
7. Example II.9 and Theorem II.10: the blind spot exhibited with a proof of non-polyhedrality; the
   termination correction; the composed oracle.
8. Six kernel-checked cores (general fooling theorem with its own pigeonhole; golden irrationality;
   menu count; the three cone-theorem identities over any commutative semiring).

**Potential scholarly contributions (to be checked against the HMM/positive-systems literature before
any claim).**  (a) The *field of definition* of a positive (HMM / controlled quasi-)realization as an
invariant, and the contact criterion that bounds it from below; the fact that the `ℚ/ℝ` separation
appears already at linear dimension 2 in the sequential setting and is infinite there, whereas
one-shot matrices of rank ≤ 2 never separate.  I am not aware of a published treatment of rational
versus real *HMM* realizability of a rational process (CKMSW is one-shot), but the question is natural
enough that it should be searched for explicitly.  (b) Partial-availability realization as a
completion problem (ghost freedom), with refusal semantics as the canonical ghost-free completion;
PSR/OOM realization theory assumes executable actions.  (c) The dichotomy II.4 and the contact
certificate as a finite `ℚ`-obstruction.  Items (a)–(c) are modest in technique (quadratic fields,
Weyl–Minkowski, LP) and the value is in the sharpness of the examples.

**Unresolved (UNVERIFIED / CONJECTURE).**  A necessary-and-sufficient criterion for `d⁺_ℚ < ∞`
(contact is sufficient for `∞`, not necessary); the `r = 2` decision procedure (endpoints of the
reachable slice as algebraic numbers); whether "real carrier + no contact ⇒ rational carrier" (the
*slack conjecture*: if some real sandwiched invariant polyhedral `K` has `T_{a,z} K ⊆ relint K ∪ {0}` and
all sources in `relint K`, rational perturbation should give a rational `K`); the exact value
`d⁺_{ℚ(√5)}`-type questions for the cyclotomic clocks (their orbit carriers are rational, so none);
Theorem 4.1 over `ℚ` itself in Lean (its identities are verified generically; a `ℚ` instance needs an
algebra library the pinned no-mathlib lane does not have); whether `d⁺(p̃(K))` can exceed `d⁺_law(K)` strictly (the refusal completion is
ghost-free but its all-or-nothing refusals may force splitting; PH₁ gives 5 vs 1 for `SU`, but
`d⁺(p̃)` itself is not computed).

## 12. Integration map (additions to Part I §13)

* `carrier_field_of_definition.py`: `Quad` (exact `ℚ(√D)`), `fibonacci_cat_system`, `golden_carrier`
  (Theorem 4.1 over `ℚ(√5)`), `two_dimensional_contact_certificate`, `rational_interval_invariance`
  / `rational_interval_search` (II.4), `rational_root_free`.  Interfaces: consumes `LinearSystem` /
  `LinearRealization` from Part I unchanged.
* `carrier_lawful_profile.py`: `operational_profile`, `public_menu` (CAR-07's "menu is not a sensor"
  made executable), `support_uniform_completion` and `profile_equivalence_certificate` (exact; reuses
  Part I's `equivalence_certificate`), `phantom_walk_carrier` / `minimal_lawful_phantom` /
  `ghost_block_certificate` (II.6), `simplicial_grid_search` (II.9), `diagonal_contraction_system`,
  `carrier_realization_oracle_ii` (composition, Part I oracle untouched).
* PR #53 `carrier_indexed.py`: `ActualHistory.advance` refuses unavailable actions = refusal
  semantics (`p̃`); `decide_original` + `original_posterior` are functions of `Π` (Theorem 8.2), so they
  transport across *any* lawful completion, including the one-state phantom carrier.  F48
  `extend_fiber` drops disabled configurations = partial-execution semantics (`p_⊥`); `quotient_source`
  requires enabledness to descend, which is the quotient instance of "menus are part of the profile".
* CT10 `carrier_hankel_bounds.py` (correct label): `hankel_dimension_receipt`'s
  `global_upper_bound_proved: False` convention is kept — Part II's upper bounds come only from
  verified cones; its lower bounds now have a kernel-checked general fooling theorem behind them.
* Lean: `EODCS_PositiveCarrierII.lean` and `EODCS_PositiveCarrierCone.lean` are compiled by the existing `eodcs-lean.yml` glob; CI reproduces
  `POSITIVE_CARRIER_II_RECEIPT.json` byte-for-byte (`eodcs-tests.yml`).  The 4.19 EOS lane and the
  mathlib lane are untouched.
* Part I `carrier_realization.py`: one change, `reachable_cone_refinement(..., max_rounds=32)` (II.10);
  Part I's receipt and 38 tests are unchanged.

## 13. The most consequential remaining obstruction, and the next lemma

The deepest thing Part II shows is that *exactness of the carrier is not free*: an observer with
exact rational predictions may be forced into an irrational carrier.  For SUCC's exact-arithmetic
programme the consequential open question is therefore the **rationality decision**: given a rational
behavior with a real positive carrier, decide whether a rational one exists, and if so bound its
size.  The contact test is a sufficient obstruction; the slack conjecture (§11) is the natural
sufficient condition for existence; between them lies the honest UNRESOLVED.

**Next lemma (concrete, exact, bounded).**  *Dimension-2 decision.*  For `r = 2` with rational data:
(1) prove that the endpoints `α ≤ β` of the reachable slice are real algebraic of degree ≤ 2 and
computable: each is a fixed point of a single event's slice map or the image of such a fixed point
under a bounded word (the slice maps are monotone Möbius maps or constants, and the extreme points
of the orbit closure of a finite monotone IFS on an interval are attained by extremal compositions);
(2) prove that a rational invariant sector exists iff, at each irrational endpoint, no event map has
a repelling or neutral fixed point there and the prediction slice has positive slack — then a
rational endpoint slightly beyond it is pulled inward by every event; (3) run it on the Fibonacci
system (expected: no slack, verdict ∞) and on its one-action truncation (expected: slack, rational
sector found, matching the receipt).  A positive answer makes `d⁺_ℚ` decidable at `r = 2` and gives
the template for the `r = 3` nested-polygon case, where the first `(3, k)` example with `k ≥ 5` and
rational data — or a new obstruction beyond support, spectrum, availability and contact — is still the
theorem worth having.
