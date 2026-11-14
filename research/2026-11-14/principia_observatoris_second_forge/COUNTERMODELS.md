# Countermodels: every significant failed conjecture, with its receipt

**Second Forge, 2026-11-14.** A refutation is listed only with an explicit receipt (a concrete
model, a cited theorem, or a typed contradiction), per [docs/METHOD.md](../../../docs/METHOD.md).
Corpses are kept, not deleted. The *Source* column says who proposed the failed statement:
most of these were the principal investigator's own commissioning conjectures, refuted by the
delegated workstreams or by the PI's own crucible. Each receipt is executable unless marked
*paper*.

Identifiers: `QG/RG/HQ` = [CAUSAL_GEOMETRY.md](CAUSAL_GEOMETRY.md); `FO` =
[agents/OPUS_I_FINITE_OBSERVER.md](agents/OPUS_I_FINITE_OBSERVER.md); `FH` =
[agents/OPUS_III_HORIZON_HUNTER.md](agents/OPUS_III_HORIZON_HUNTER.md); "Geometer CG" =
[agents/OPUS_II_CAUSAL_GEOMETER.md](agents/OPUS_II_CAUSAL_GEOMETER.md).

## 1. Geometry and response

| # | Failed conjecture | Source | Receipt | What survives |
|---|---|---|---|---|
| C-1 | A live structural path implies a net response at some lag | founding intuition, tested by PI | signed diamond `x→y (1), x→y' (1), y→z (1), y'→z (−1)`: `(A^τ)_{zx} = 0` for all `τ` | true for balanced carriers (RG-4); four nodes are minimal for an all-lag failure |
| C-2 | Net response generates a directed path geometry (triangle inequality) | PI | same diamond: `R(x,y)·R(y,z) = 1 > 0 = R(x,z)` | true for balanced carriers (RG-3) |
| C-3 | An unbalanced sign pattern forces some cancellation | PI | directed 4-cycle with one negative edge: not balanced up to sign, at most one walk per length, never cancels (the 3-cycle first used is balanced for `ε = −1`) | imbalance is necessary, not sufficient |
| C-4 | Equal directed cycle products imply unit-equivalence | PI | acyclic diamond with parallel-path ratio `2`: no directed cycles, not unit-equivalent | true when every edge lies on a directed cycle; in general use undirected holonomy (RG-5) |
| C-5 | "`x` is closer to `y` than `z` is" is observer-independent | founding note's uncalibrated reading | weights `2, 1` into a common target; rescaling the first source by `4` reverses the order | round-trip products and lag ratios are unit-free |
| C-6 | Coarse-graining can hide a causal ancestor | PI | **mixed verdict.** False for may-quotients (QG-5: `Q∃*` is the least quasar-free geometry). **True for must-quotients**: `q=(0,0,1)`, single edge `1→2`: `d_∀ = ∞`, `d_C(1,2) = 1` (referee R-3). The first version listed this as REFUTED with no receipt, which broke the receipt rule | may-quotients err only by ghosts, must-quotients only by quasars |
| C-7 | A quotient path lifts from the selected start | inherited SUCC corpse (PAP-04) | three-state ghost `b→c`, reports `A,A,B`, start `a` | exactness criterion QG-3 |
| C-8 | `Q∀* = Q∃*` characterises exactness | PI | PAP-04 chain `0→1→2`, `q=(0,0,1)`: exact, yet must-closure < may-closure | it is sufficient; the exact criterion is `Q∃(R) ≤ Q∀(R*)` |
| C-9 | The source value is a function of the quotient closures | PI ("a fixed point between the two?") | edges `{1→2, 1→0}` versus `{0→1, 1→2}` with `q=(0,0,1)`: same `Q∃, Q∀, Q∃*, Q∀*`, different reachable reports from `0` | recovered through the coarsest exact refinement (Geometer CG-10) |
| C-10 | Lax maps of value structures transport exactness in one direction | PI | `𝒫(ℤ/2) → 𝔹`, `A ↦ [0 ∈ A]`: lax with strict unit and joins; edges `1→2 ({1}), 2→0 ({0}), 2→2 ({1})`, `q=(0,1,1)`: exact upstairs, ghost downstairs | strict maps transport; oplax maps transport all-start exactness only |
| C-11 | Oplax maps transport selected-start exactness | Geometer's own crucible | budget tropical `{0..3,∞}`, `h(a)=⌊a/2⌋`; edges `0→1 (1), 0→3 (2), 2→3 (1)`, blocks `{0},{1,2},{3}`: exact at `0` upstairs, ghost shortcut downstairs | hereditary selected-start exactness transports |
| C-12 | Exact partitions might not be closed under joins | PI | — refuted: they are join-closed (Geometer CG-10) | but **meets fail**: edges `{0→0,0→3,1→0,1→2,2→3,3→0}`, `{012|3}` and `{01|23}` exact, meet `{01|2|3}` not (PI re-checked) |
| C-13 | Selected-start exactness has a canonical coarsest refinement | Geometer's own crucible | edges `{2→0, 2→1, 3→0}`, start `0`: `{03|1|2}` and `{0|1|23}` exact at `0`, their join invents report `1` | all-start version is canonical |
| C-14 | Three states are minimal for a ghost in every value structure | PI (generalising PAP-04) | non-integral value structures admit two-state ghosts (Geometer CG-6) | true for integral value structures |
| C-15 | Signed quotients, like idempotent ones, can only invent | PI | edges `x→z (1), x'→z (−1), x'→w (1)` with `x,x'` merged: one report deleted, another invented, at the same start (a three-state receipt exists too: C-52) | idempotent case: deletion impossible (QG-2) |
| C-16 | The universal image `q_*` pairs with the forward must-quotient | PI | edge `0→2`, `q=(0,1,1)` | it pairs with the backward must-quotient |

## 2. Finite observer

| # | Failed conjecture | Source | Receipt | What survives |
|---|---|---|---|---|
| C-17 | A new instrument can only refine the core | PI | a new pure intervention makes new states reachable (FO-3) | `core_A ≅ core(core_{A∪B}|_A)` |
| C-18 | The intervention-order horizon reaches the degree at some baseline | PI | `f = x₃·NAND(x₁,x₂)`: degree 3 in `x₃`, horizon ≤ 2 at every baseline (PI re-checked: horizons `1,1,1,1,1,1,2,2`) | `1 = min h_j ≤ max h_j ≤ deg_j` |
| C-19 | The horizon formula is exact under any prior class | PI | class `{0, x₁ + x₁x₂}` needs only order 1 | exact without a prior |
| C-20 | Reading every node without clamping identifies the wiring | PI ("all nodes settable and readable") | FO-9 corollary: full readout without joint clamps fails | joint clamping of all potential parents over all contexts, iff |
| C-21 | Commuting idempotent instruments give free observation | PI | SUCC's destructive A,B,C carrier: commuting, idempotent, and `1[C]` inaccessible at every horizon; 384 such carriers on ≤ 3 states | class non-disturbance suffices (FO-10, CA-1) |
| C-22 | Free observation implies non-disturbing or class-injective instruments | PI | "read then flip" carrier; 36 036 exhaustive counterexamples | neither is necessary |
| C-23 | If every target is separately accessible, the class is accessible | PI | states `A,B,C,D`, three instruments each flagging one state and sending all to `D`: all 8 Boolean targets accessible, the class is not | **executable knowledge is not closed under conjunction** |
| C-24 | Static behaviour (behaviour = one-shot readouts) implies free observation | PI | two-state swap with distinct readouts | converse of CA-1 fails |
| C-25 | Monotone (cancellation-free) networks compose dependencies | PI | `z₁ = x, z₂ ≡ 0, y = z₁ ∧ z₂`: every table monotone, path essential, response constant (gating) | binary single-hidden-node chains do compose (FO-8) |

## 3. Finite horizons

| # | Failed conjecture | Source | Receipt | What survives |
|---|---|---|---|---|
| C-26 | "For each finite query set two members agree on it and differ in target" defeats every protocol | PI | pointer class `x(0)=k, x(k+1)=β`: hypothesis holds, two adaptive queries decide | discontinuity at a point is the right condition (FH-1) |
| C-27 | `n+m` is sharp for every family of linear recurrences | PI | invertible recurrences over GF(2), orders ≤ 1: horizon `1` | `max deg lcm(p,q)` (FH-3d) |
| C-28 | Finite-state machines have the same horizon as linear systems | PI | exhaustive search: `n+m−1` (PI re-checked for `(n,m) ≤ (3,3)`) | one better than linear |
| C-29 | Rabin probabilistic automata need words of length `n+m−1` | PI (quoting from memory) | exact pair first differing at word `xx` (`15/64` vs `9/64`), sharp bound `n+m−2` | `n+m−1` holds for weighted automata and HMMs; primary-source wording unverified |
| C-30 | A dimension bound excludes the limit-only regime | natural reading of FH-6 | `2^{-k}`: order 1, never zero, tends to zero | it excludes the particular law `1/(k+1)` |
| C-31 | A learner that converges can announce convergence | folk expectation | FH-5(d): any halting certifier on linear-recurrent sequences is unsound on `x + δ_t` | a declared order bound restores a certificate at `2n` |

## 4. Classical appearance

| # | Failed conjecture | Source | Receipt | What survives |
|---|---|---|---|---|
| C-32 | "Classical" is one predicate of a system | strongest reading of the founding note §8 | witness table in THEOREM_FORGE §F: five carriers with different pass/fail patterns | a family of toolkit-relative diagnostics |
| C-33 | Passing every diagnostic certifies a classical carrier | — | declared qubit with toolkit `{X, Z}`: transcript-identical to a bit | "appears classical relative to a toolkit" |
| C-34 | Failing determinism and free observation certifies a non-classical carrier | — | toolkit `{X, H, Z}`: a four-state classical stochastic machine matches every transcript | same |
| C-35 | A deterministic, local, freely observed law is predictable | — | shift register through an `r`-bit window: ambiguity `2^{min(r,t)}` | predictive closure is horizon-relative |

## 5. First-version claims refuted or repaired under adversarial review

The hostile referee's full reports are
[agents/OPUS_IV_HOSTILE_REFEREE.md](agents/OPUS_IV_HOSTILE_REFEREE.md) (findings `R-n`, receipts
in `tests/test_observatoris_referee_receipts.py`) and
[agents/OPUS_IV_REFEREE_ROUND2.md](agents/OPUS_IV_REFEREE_ROUND2.md) (findings `S-n`). The first
referee began before `CG-n` in CAUSAL_GEOMETRY.md was renamed `QG-n`. Every row below was a
statement of this package's first version; the corpse is kept and the live documents carry the
repaired form.

| # | First-version statement | Referee | Receipt | Repaired statement |
|---|---|---|---|---|
| C-36 | HQ-3: any effect at a lag below the model distance witnesses a hidden edge | R-7 REFUTED | model = source, edges `x→s`, `a→y`; a policy copying the sensor into the actuator makes `y` respond at lag 3 with `d_M(x,y)=∞` | add `τ ≤ d_M(x,S)` (or a passive/open-loop observer), preparations differing exactly at `x`, a fixed time convention |
| C-37 | HQ-4: `d_C(x,y) ≤ T_eff` for every observer | R-7 REFUTED | same receipt | holds for passive or open-loop observers |
| C-38 | HQ-2(b): on every nonnegative linear carrier effect and detection times equal structural distances | R-6 REFUTED | `h₁→y`, `h₂→y`, perturbation `(+1,−1)`: target never moves; a clamping policy also blocks the effect | passive observer, carrier balanced up to sign, perturbation aligned with the switching signs |
| C-39 | HQ-4: `d_Q∃(q x,q y) = d_C(x,y)` iff cost-exact | R-4 REFUTED | single edge `0→2`, labels `(0,1,1)`: exact everywhere, `d_Q∃(q0,q1)=1<∞=d_C(0,1)` | exactness equates quotient distance with distance to the *fibre* |
| C-40 | RG-3: for unbalanced carriers no transform of the response gives a triangle inequality | R-9 REFUTED | a never-cancelling unbalanced cycle satisfies it | what defeats every transform is an all-lag cancellation |
| C-41 | RG-3: `−log` of the response is derived, unlike the note's `log(1+1/R)` | R-10 OVERCLAIM | `log(1+1/R)` satisfies the same inequality on 1 000 exact triples | `−log` is singled out only by turning products into sums exactly |
| C-42 | RG-3: `D_T` is a Lawvere-type distance | R-11 OVERCLAIM | chain at `T=1`; `A=[[2]]` gives a negative value; the discount reverses an order | graded family; the clamped all-lag version is a quasi-metric and still depends on `γ` |
| C-43 | §2: ghosts are found by invariants, quasars only by contrasts | R-2 OVERCLAIM | two sources with identical quotient data, one with a ghost at the start | a difference of data regimes, not of failure types |
| C-44 | RG-4 (after the `ε` update): Harary's all-closed-walks-positive criterion; "balance = unit-equivalence to a nonnegative carrier" | R-13 REQUIRES REPAIR | `A=[[−1]]` | closed walks have sign `ε^{|W|}`; `A` or `−A` is unit-equivalent to a nonnegative carrier |
| C-45 | RG-1(c): four nodes are minimal for an all-lag cancellation | R-12 scope | three nodes suffice for self-return at positive lags | minimal for distinct nodes |
| C-46 | QG-3(5): "may = must for the closure" | R-8 REQUIRES REPAIR | fails whenever `q` is not onto (empty meet) | on the image of `q` |
| C-47 | CA-4: window ambiguity is `2^{min(r,t)}` | R-18 REFUTED | `(n,r,t)=(4,2,3)` gives `2` | `2^{min(s, n−s, r, n−r)}`, `s = t mod n` |
| C-48 | CA-3: the diagnostics are pairwise independent, every cell computed | R-19 OVERCLAIM | no pair realises all four combinations; the module's predicate called the shift register not free | three diagnostics are each shown to fail alone; determinism is not separated from free observation |
| C-49 | FH-6: surviving `b_H` are "equivalently those deviating at or before index `n−1`" | R-22 REFUTED at `n=1,H=0` | `b₀` has order 1 and first deviates at index 1 | add "or `H = 0`" |
| C-50 | the Lean "must-is-not-may" control shows the mutated statement false | R-27 REFUTED | the same harness rejects a true statement | the control now proves the negation inside the instance |
| C-51 | two finite-horizon tests | R-23 VACUOUS | one asserted a tautology, one compared a formula with itself | replaced by tests of the falsifiable premises |

| C-52 | Geometer CG-13(4): no three-state example at `τ = 1` where a signed quotient both invents and deletes | S-9 REFUTED | `x→x (1)`, `x′→x′ (−1)`, `x′→z (1)`, `q=(A,A,B)`: source `(1,0)`, quotient `(0,½)` | three states at `τ = 1` is the minimum |
| C-53 | Geometer CG-7: the cited receipt shows both outer sandwich links strict at one `(x,b)` | S-3 REQUIRES REPAIR | the cited chain is `(∞,∞,2,1,1)` | valid receipt `(∞,3,2,1,0)` over the saturating tropical structure; impossible over truth values |
| C-54 | Geometer CG-6(2): a grading into ℕ on the truncated word monoid | S-7 REQUIRES REPAIR | the overflow element forces degree `0` | grading into `ℕ ∪ {∞}` |
| C-55 | FO-4(ii): "consistent with every `j`-independent function" | S-13 wording | — | "some" |
| C-56 | FO-9 summary row without `|V_p| ≥ 2` | S-15 boundary | single-valued parent | hypothesis restored |
| C-57 | the single-copy depth bound `(s−1)(q−1)` is sharp | S-17 | at `(s,q) = (3,3)` the maximum is `3 < 4` | a valid bound, attained at `(2,3)` |

**Survived the second review:** the seven-way exactness equivalence over a noncommutative,
non-integral value structure with non-surjective observations and empty fibres (S-1); both
Beck–Chevalley conditions (S-4); join-closure and the refinement algorithm (S-5); strictness of
the truncated change-of-base maps (S-6); whole-distance preservation (S-8); the core
identification bound with exactly 11 500 cores (S-11); toolkit monotonicity (S-12); the exact
cost of certifying absence by full brute force (S-14); the wiring minimality claims (S-16); the
identifiability criterion on a different graph shape (S-15); and the all-horizon single-copy
criterion with every census count reproduced by an independent implementation (S-17).

**Survived hostile review, seat 1** (what was tried is in the report): the Lean core QG-1…QG-4 including
the reversed-order cost structure, a noncommutative language structure, empty `X` and off-image
`Y` (R-26); QG-5 in its universal-property form (R-1); HQ-1 with memoryful acting observers,
sharpened (R-5); RG-1(a,b), RG-2; RG-5 with a weaker hypothesis (R-14, R-15); RG-6 (R-16); CA-6
for words of every length, with a twelve-identity certificate (R-17); FH-3, FH-7, FH-8, FH-9 with
every constant re-derived and brute-forced (R-20, R-21, R-24, R-25); FH-1, FH-2, FH-5, FH-6(d),
FH-10, FH-11, FH-12, FH-14 re-derived on paper (R-28).
