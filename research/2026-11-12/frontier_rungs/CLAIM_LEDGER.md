# Claim ledger — frontier rungs round (2026-11-12)

Statuses: **PROVED LOCAL** (paper proof in the named file; same-model authorship; audited once by a
separate read-only instance, repairs after that audit not audited again; not external review),
**KERNEL-CHECKED** (Lean 4.14.0 against the pinned mathlib, axioms `propext`, `Classical.choice`,
`Quot.sound`), **IMPORT** (literature, grade in SOURCE_MAP), **COMPUTED FROM IMPORT**,
**OBSERVED** (finite exact computation, no asymptotic authority), **CONDITIONAL**, **OPEN**.

Domain of every LMF statement: an arbitrary real `ξ` (so every seed), `y_n = {16^n ξ}`, shell
measures `ν_B`, limit set `M(ξ)`; or an arbitrary probability measure on `[0,1]`.

| ID | Statement (short) | Status | Falsifier / next test |
|---|---|---|---|
| LMF-01 | `M(ξ)` nonempty, compact, connected, `×16`-invariant; gauge-invariant; normal ⟺ `M = {λ}` | PROVED LOCAL (Weyl, Wall: IMPORT) | a real `ξ` with a non-invariant shell limit |
| LMF-02 | invariant `μ` with `|μ̂(h)| = 1` ⟺ `μ ∈ Δ(K_(h,j))`, value `e(j/15)`; real saving ⟺ one excluded face; Basel sandwich `½(1−Re W) ≤ 1−Re B ≤ 2(1−Re W)`; `A·F_h` one-directional | PROVED LOCAL | an invariant measure violating the dichotomy; weights `p_n` outside `[1/(2A), 2/A]` |
| LMF-03 | Ladder `(N) ⟹ (E) ⟹ (AM) ⟹ (CH_k) ⟹ (CH) ⟹ R1 ⟹ R0`, each strict; R0 ⟺ `δ_0 ∉ M` ⟺ positive lower shell density of binary digit changes, with constants `1/53` and cost `‖2^m ξ‖ ≥ 2^(−((1−c)/(1+c))m−4)`; `(CH_k) ⟺ limsup Re W_B(16^k−1) < 1` | PROVED LOCAL (two strictness witnesses use IMPORTs: maximal entropy, binary Champernowne) | one shell violating a two-sided inequality; a witness on the wrong side |
| LMF-04 | `W_1(ν,λ) ≥ (1/h)(1/4 − ∫‖hy−θ‖dν)` for all `h ≥ 1`; same for `G(ν) = W_1(ν, Cν)` when `16 ∤ h` (false at `h = 16`); shell thresholds `1/4` (R1, R0), `1/60` ((CH)), `1/(4(16^k−1))` ((CH_k)); `1/4`, `1/60` sharp for shells; quantitative (CH) form | PROVED LOCAL | a probability measure below the bound; a shell sequence failing a rung with `limsup` below its threshold |
| LMF-05 | mass `a` on the fixed points ⟹ `W_1 ≥ a²/60`; prefix thresholds `W_1(μ_N,λ) < 1/240`, `D_N < 1/256` ⟹ (CH); `< 1/16`, `D_N < 15/256` ⟹ R1 | PROVED LOCAL (jump lemma repaired after audit) | as above for prefixes |
| LMF-06 | hostile controls on the stated side of every threshold; coherent seed `D = 15/32`, `W_1 = 1/2` | PROVED LOCAL / OBSERVED instances | recomputation |
| RDT-01 | restricted transference lemma at denominators `g·b^m`, non-asymptotic | PROVED LOCAL | one form, base, `g`, `m` with `‖g b^m ξ‖` below the bound |
| RDT-02 | gain = `b`-adic imbalance (for `m ≥ m_0`); a single form with integer-normalised error `≥ 1` is silent at every `m`; exponent `(β+δ−γ)/(α−δ+γ)` if `α > δ`; `ξ_6 = Σ 6^(−k!)`: `μ = ∞`, `v_2 ≤ log 3/log 6` | PROVED LOCAL ((c) corrected after audit) | as RDT-01 |
| RDT-03 | runs ⟺ restricted approximations with constants; L2 failing at `B` ⟹ near-convergent decomposition of `15·16^B`; long runs ⟹ large partial quotients | PROVED LOCAL (sharp `2c` form: IMPORT Dujella) | a planted run violating a constant |
| RDT-04 | BBP partial sums are silent (depth `n − k_n`); Dalzell coefficient `(−1)^(bn)4^(bn−1)`, weight optimum `4 log(1+√2) < 4`; effective-base table | PROVED LOCAL; Dalzell silence OBSERVED for `5 ≤ n ≤ 10` | a partial sum certifying a bound |
| RDT-05 | `v_2(log 2) ≤ 2.3814` (limit `2.3767`) from the tilted family `(2,4,3)`; unrestricted from the same forms `3.3801`; literature `μ−1 = 2.5746` | PROVED LOCAL (prime number theorem: IMPORT; rates in `Q(√73)` evaluated numerically, margin `8·10^(−5)` to the stated bound; `m_0` not explicit). **No novelty claimed.** | an `n` violating a step; `‖2^m log 2‖ < 2^(−2.39m)` for arbitrarily large `m` |
| RDT-06(a) | 2-adic shadow: `v_2(B_n) ≥ (2a − c/2)n − log_2(Dn+1) − 1/2` in Gaussian one-pole families | PROVED LOCAL | one `n` below the bound |
| RDT-06(b,c) | for π, restricted = unrestricted quotient in seven families at `n = 12, 18`; forms with the imbalance on π do not converge | OBSERVED | a convergent family with `v_2(A_n) − v_2(B_n) ≥ cn` |
| RDT-06(d) | `v_2(1/π) ≤ 3.11` | CONDITIONAL on the existence of `lim (1/n) log|J_n|` | — |
| RDT-07 | `v_16(log(16/15)) ≤ Λ(1,16,1) − 1 = 0.8813`; extension to `g·16^m`; **L2 for `log(16/15) ∈ V`** | IMPORT (Rivoal 2007, READ-AT-SOURCE) + COMPUTED FROM IMPORT (no interval enclosure) + PROVED LOCAL extension (`m_0(g, ε)` not explicit) | an error in the reading of Rivoal's Lemmas 1–2; a late shell of `log(16/15)` without a digit change |
| RDT-08 | `arg(1−x) ∈ (π/4)Z ∖ 2πZ` ⟹ `|x| ≥ 2^(−1/2)`, equality exactly at `(1±i)/2` | PROVED LOCAL | — |
| ZSC-06 null relation; ZSC-02 locality lemma; ZSC-03 renewal lemma (33 statements) | exact lemmas of the parent dossier | **KERNEL-CHECKED** (`lean/RECEIPT.json`; 9 mutants refuted) | the check script |
| R0 for π | positive lower shell density of binary digit changes of π; `limsup Re W_(B,1) < 1` | **OPEN** — the named obligation | a sequence of shells with `Re W_(B,1) → 1` refutes it |
| R1, (CH), (CH_k), (AM), (E) for π | — | **OPEN** | — |
| L2 for π | a hexadecimal digit change in every large shell | **OPEN** | — |
| `v_16(π) < 6.1033` | any restricted bound below the unrestricted record | **OPEN** | — |
| (CH), R0 for `log(16/15)` | — | **OPEN** — the named test object | — |
| π base-16 normality | `W_B(h) → 0` for all `h ≠ 0` | **OPEN** | — |

**Separation (κ / φ / σ / ρ).** κ (contact): high for the exact identities and inequalities, which
are tested on instances and, for the carry lemmas, kernel-checked; none for any statement about π's
statistics. φ (toolkit-relative indistinguishability): every witness of LMF-03 and every hostile
control is indistinguishable from π by Diophantine exponents alone; the thresholds of LMF-04
distinguish them only shell by shell. σ (source correctness): the forcing is imported unchanged;
Rivoal's theorem is read at source and evaluated numerically, not re-proved. ρ (commitment): the
preregistered thresholds were partly wrong and are reported as wrong; the previous round's "(CH) is
the weakest signed statement" is withdrawn.
