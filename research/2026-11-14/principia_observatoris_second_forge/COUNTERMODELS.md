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
| C-3 | An unbalanced sign pattern forces some cancellation | PI | directed 3-cycle with one negative edge: unbalanced, never cancels | imbalance is necessary, not sufficient |
| C-4 | Equal directed cycle products imply unit-equivalence | PI | acyclic diamond with parallel-path ratio `2`: no directed cycles, not unit-equivalent | true under strong connectivity; in general use undirected holonomy (RG-5) |
| C-5 | "`x` is closer to `y` than `z` is" is observer-independent | founding note's uncalibrated reading | weights `2, 1` into a common target; rescaling the first source by `4` reverses the order | round-trip products and lag ratios are unit-free |
| C-6 | Coarse-graining can hide a causal ancestor | PI | — (QG-5 proves the opposite for may-quotients) | hidden ancestors need an *omitted edge*, not a coarse view |
| C-7 | A quotient path lifts from the selected start | inherited SUCC corpse (PAP-04) | three-state ghost `b→c`, reports `A,A,B`, start `a` | exactness criterion QG-3 |
| C-8 | `Q∀* = Q∃*` characterises exactness | PI | PAP-04 chain `0→1→2`, `q=(0,0,1)`: exact, yet must-closure < may-closure | it is sufficient; the exact criterion is `Q∃(R) ≤ Q∀(R*)` |
| C-9 | The source value is a function of the quotient closures | PI ("a fixed point between the two?") | edges `{1→2, 1→0}` versus `{0→1, 1→2}` with `q=(0,0,1)`: same `Q∃, Q∀, Q∃*, Q∀*`, different reachable reports from `0` | recovered through the coarsest exact refinement (Geometer CG-10) |
| C-10 | Lax maps of value structures transport exactness in one direction | PI | `𝒫(ℤ/2) → 𝔹`, `A ↦ [0 ∈ A]`: lax with strict unit and joins; edges `1→2 ({1}), 2→0 ({0}), 2→2 ({1})`, `q=(0,1,1)`: exact upstairs, ghost downstairs | strict maps transport; oplax maps transport all-start exactness only |
| C-11 | Oplax maps transport selected-start exactness | Geometer's own crucible | budget tropical `{0..3,∞}`, `h(a)=⌊a/2⌋`; edges `0→1 (1), 0→3 (2), 2→3 (1)`, blocks `{0},{1,2},{3}`: exact at `0` upstairs, ghost shortcut downstairs | hereditary selected-start exactness transports |
| C-12 | Exact partitions might not be closed under joins | PI | — refuted: they are join-closed (Geometer CG-10) | but **meets fail**: edges `{0→0,0→3,1→0,1→2,2→3,3→0}`, `{012|3}` and `{01|23}` exact, meet `{01|2|3}` not (PI re-checked) |
| C-13 | Selected-start exactness has a canonical coarsest refinement | Geometer's own crucible | edges `{2→0, 2→1, 3→0}`, start `0`: `{03|1|2}` and `{0|1|23}` exact at `0`, their join invents report `1` | all-start version is canonical |
| C-14 | Three states are minimal for a ghost in every value structure | PI (generalising PAP-04) | non-integral value structures admit two-state ghosts (Geometer CG-6) | true for integral value structures |
| C-15 | Signed quotients, like idempotent ones, can only invent | PI | edges `x→z (1), x'→z (−1), x'→w (1)` with `x,x'` merged: one report deleted, another invented, at the same start | idempotent case: deletion impossible (QG-2) |
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

## 5. Adversarial review

The findings of the hostile referee (OPUS IV), the repairs made in response, and the statements
that survived are recorded in
[agents/OPUS_IV_HOSTILE_REFEREE.md](agents/OPUS_IV_HOSTILE_REFEREE.md) and summarised in
[PROVENANCE_AND_INDEPENDENCE.md](PROVENANCE_AND_INDEPENDENCE.md) §5. The referee reviewed the
documents before the identifiers `CG-n` in CAUSAL_GEOMETRY.md were renamed `QG-n`; its `CG-n`
therefore means this package's `QG-n`.
