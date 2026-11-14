# Theorem forge: statements, authority, dependencies, open premises

**Second Forge, 2026-11-14.** One register for every theorem-bearing claim of the package.
Proofs live in the documents named in the *Proof* column; this file fixes the statement, the
authority actually obtained, and what each claim depends on.

**Authority vocabulary** (per the campaign's quality gates):

- **KERNEL** — encoded statement checked by Lean 4.14 core with no axioms
  (`formal/ObservatorisQuantale.lean`, receipt `receipts/lean-kernel.json`).
- **PROVED** — explicit paper proof in this package.
- **CORROBORATED** — two genuinely different routes agree (e.g. a paper proof by one author and a
  kernel proof or separate implementation by another).
- **CLASSICAL** — a named established theorem, restated; attribution in the proof document.
- **OBSERVED** — holds in exhaustive or sampled exact finite models; not a proof.
- **CONJECTURED / UNVERIFIED / REFUTED (receipt)**.

Two separate records are kept for every row: *internal correctness* (the authority column) and
*source-map adequacy*, which is **NOT ESTABLISHED for any row**: no theorem here certifies that a
declared table describes a real source.

## A. Weighted ancestral reachability and quotient geometry

| ID | Statement (scope: any set `X`, observation `q: X→Y`, value structure `V` with the unital-quantale inequalities; no commutativity) | Authority | Proof | Depends on |
|---|---|---|---|---|
| QG-1 | `R*(x,·)` is the least potential with unit at `x` | KERNEL; CLASSICAL in content | CAUSAL_GEOMETRY §1; Lean `star_closed`, `star_le_of_closed` | — |
| QG-2 | `R*(x,z) ≤ Q∃*(q(x),q(z))` | KERNEL | §1; `star_le_quot_star` | QG-1 |
| QG-3 | all-start exactness ⇔ fibre constancy ⇔ `q_!` preserves potentials ⇔ saturation preserves potentials; selected-start form | KERNEL | §1; `exact_iff_*`, `exactAt_iff_saturated_star_closed` | QG-1, QG-2 |
| QG-4 | `Q∀*(q(x),b) ≤ (q_!R*(x,·))(b) ≤ Q∃*(q(x),b)` | KERNEL | §1; `quotAll_star_le_push_star` | QG-1 |
| QG-5 | a may-quotient geometry has no unseen ancestors | PROVED (corollary) | §2 | QG-2 |
| QG-6 | `Cl_Q∘q_! ⊣ q^*`; it maps `R*(x,·)` to `Q∃*(q(x),·)`; exactness at `x` ⇔ ghost defect vanishes | KERNEL | Lean `closure_push_adjunction`, `closure_push_star_le_quot_star`, `quot_star_le_closure_push_star`, `exactAt_iff_closure_push_le` | QG-1…3 |
| QG-7 | all-start exactness ⇔ `Sat_q∘Cl_R` idempotent | KERNEL | Lean `satClosed_iff_sat_closure_idempotent` | QG-3 |
| QG-8 | selected-start exactness transports along homomorphisms of value structures; not conversely | KERNEL (transport); REPLAYED receipt (non-converse) | Lean `exactAt_map`; `test_observatoris_integration` | QG-3 |
| QG-9 | over truth values the weighted closure is reflexive-transitive closure (PAP recovered) | KERNEL | Lean `star_propQ_iff` | — |

| QG-10 | all-start exactness ⇔ every source edge is realised from every representative of its start report (`Q∃(R) ≤ Q∀(R*)`) | KERNEL (`exact_iff_edgeRealised`); CORROBORATED (Geometer paper proof; PI brute force on 6 000 model/partition pairs) | Geometer CG-3(5) | QG-3 |

**Delegated quotient geometry (OPUS II).** The report
[agents/OPUS_II_CAUSAL_GEOMETER.md](agents/OPUS_II_CAUSAL_GEOMETER.md) numbers its own theorems
`CG-1 … CG-13` ("Geometer CG-n"). Geometer CG-1…4 are independent paper proofs of QG-1…3 and the
selected-start form, which makes those rows **CORROBORATED** (kernel proof by the PI, paper proof
and exhaustive models by a different agent). Additional results registered from that report:

| Geometer ID | Statement | Authority |
|---|---|---|
| CG-5 | strict maps transport exactness; oplax maps transport all-start exactness only; lax maps do not; converses fail | PROVED + REFUTED parts with receipts; strict case also KERNEL |
| CG-6 | three states minimal for a ghost only when `V` is integral; over graded `𝒫(M)` exactness ⇔ lumpability (bisimulation for letter-valued relations) | PROVED |
| CG-7 | `Q∀* ≤ M ≤ ρ̂_x ≤ S ≤ Q∃*`, each link strict; lumpable ⇒ `Q∀*=Q∃*` ⇒ exact ⇒ unpointed, each strict | PROVED; outer links also KERNEL |
| CG-8 | `Cl_Q∘q_! ⊣ q^* ⊣ Int_Q∘q_*`; left Beck–Chevalley ⇔ forward exactness; right ⇔ backward exactness | PROVED; left adjunction also KERNEL |
| CG-9 | ghost defect functional, zero iff exact | PROVED; selected-start form also KERNEL |
| CG-10 | exact partitions are join-closed; unique coarsest exact refinement; meets and selected-start variants fail | PROVED; join closure and the meet receipt re-checked by the PI |
| CG-11 | weighted ghost certificate, sound and complete | PROVED |
| CG-12 | whole-distance preservation ⇔ `q` merges only isomorphic states | CLASSICAL |
| CG-13 | signed weights: lax support, balance, invent-and-delete, `(I−A)^{-1}` lumpable ⇔ `A` lumpable, generic faithfulness | PROVED; OBSERVED on 69 280 pairs |

## B. Response geometry

| ID | Statement (scope: finite square matrix `A` over an ordered field; `A_{vu}` = edge `u→v`) | Authority | Proof | Depends on |
|---|---|---|---|---|
| RG-1 | response support ⊆ structural walks; equality if `A ≥ 0`; fails for signed `A`; four nodes minimal for an all-lag failure | PROVED; OBSERVED exhaustively for 3×3 sign tables | CAUSAL_GEOMETRY §3 | — |
| RG-2 | `n` zero lags force zero at every lag; `n−1` do not | PROVED from CLASSICAL Cayley–Hamilton | §3 | — |
| RG-3 | `A ≥ 0`: `R_{S+T}(x,z) ≥ R_S(x,y)R_T(y,z)`; finiteness pattern = structural ancestry | PROVED | §4 | RG-1 |
| RG-4 | balanced (up to a global sign `ε`) ⇒ `(A^τ)_{yx} = ε^τσ_yσ_x(|A|^τ)_{yx}`; hidden dependency requires imbalance of `A` and `−A`; converse false | PROVED; CORROBORATED (PI and Geometer independently); balance criterion CLASSICAL (Harary) | §4 | — |
| RG-5 | unit changes act by potentials; unit-equivalence ⇔ trivial holonomy; `b₁ = |E|−|V|+c` free magnitudes | PROVED; (b) CLASSICAL diagonal similarity | §5 | — |

## C. Causal horizon

| ID | Statement (scope: finite synchronous network, sensors `S`, record-driven policy) | Authority | Proof | Depends on |
|---|---|---|---|---|
| HQ-1 | for `t < d(H,S)` records agree and states agree outside the radius-`t` ball | PROVED; OBSERVED on sampled linear carriers | CAUSAL_GEOMETRY §6 | — |
| HQ-2 | no evidence before `d(H,S)`; lead time bounded by `d(H,y) − d(H,S)`; attained on balanced linear carriers | PROVED | §6 | HQ-1, RG-1, RG-4 |
| HQ-3 | a model-cone violation witnesses a source edge absent from the model | PROVED | §6 | HQ-1 |
| HQ-4 | `d_Q∃ ≤ d_C ≤ T_eff`; `d_C(x, fibre) ≤ d_Q∀` | PROVED | §6 | QG-2, QG-4, HQ-1 |

## D. Finite observer (delegated: OPUS I)

| ID | Statement | Authority | Proof |
|---|---|---|---|
| FO-1 | observation is a function of `(X, A, (o_a,t_a), start)`; measure/act splitting preserves the core, not single-copy access | PROVED | agents/OPUS_I §A1 |
| FO-2 | responses equal on words of length `≤ n+m−1` ⇔ cores isomorphic (uniquely); sharp; reconstruction from length `≤ 2n−1` | CLASSICAL (Moore, Nerode) + PROVED sharpness; OBSERVED on 46 916 carriers | §A1 |
| FO-3 | `core_A(M) ≅ core(core_{A∪B}(M)|_A)`; exposure minimal at 2 states (readout), 3 (intervention) | PROVED; OBSERVED exhaustively | §A1 |
| FO-4 | dependency on `j` detected at order exactly `h_j = min{|S|: j∈S, Δ_S f ≠ 0}` | PROVED; Möbius inversion CLASSICAL; PI spot-check on all 256 functions of 3 inputs | §A2 |
| FO-5 | baseline transport formula; degree is baseline-invariant; `h_j` need not reach `deg_j` | PROVED; strengthening REFUTED | §A2 |
| FO-6 | certifying absence within degree `d` costs exactly `2·Σ_{i<d} C(k−1,i)` evaluations | PROVED; OBSERVED for `k ≤ 4` | §A2 |
| FO-7 | polynomial jets suffice; smooth jets do not | CLASSICAL | §A2 |
| FO-8 | wiring is not a response invariant; cancellation and gating are distinct mechanisms, with minimal sizes | PROVED; OBSERVED exhaustively | §A3 |
| FO-9 | essential graph of an unrestricted class identifiable ⇔ joint clamping of all potential parents over all contexts | PROVED | §A3 |
| FO-10 | single-copy access decided for all horizons by a belief fixed point; two sufficient conditions; target-wise access does not compose | PROVED; (b1) CORROBORATED by the PI's independent CA-1 | §A4 |

## E. Finite horizons (delegated: OPUS III)

Registered with exact constants in [FINITE_HORIZONS.md](FINITE_HORIZONS.md) §2–§7 (FH-1 … FH-14).
Headline authorities: FH-3 PROVED and CORROBORATED (PI's separate implementation for
`n,m ≤ 3`); FH-5 PROVED; FH-6 PROVED and CORROBORATED (PI's separate elimination for `n ≤ 6`);
FH-7 PROVED and CORROBORATED (PI's brute force for `(n,m) ≤ (3,3)`); FH-10 PROVED;
FH-11, FH-12, FH-13 CLASSICAL.

## F. Classical appearance

| ID | Statement | Authority | Proof |
|---|---|---|---|
| CA-1 | if no operation changes the behaviour class, then behaviour = joint one-shot readout, transcripts are static, and one copy suffices | PROVED (below); CORROBORATED by FO-10(b1); OBSERVED | this file |
| CA-2 | the converse of CA-1 fails | REFUTED converse; receipt: the two-state swap | `test_static_behaviour_does_not_imply_free_observation` |
| CA-3 | free observation, predictive closure at a horizon, determinism of the core, and alignment are pairwise independent diagnostics | OBSERVED by exact witnesses (table below) | `tests/test_observatoris_classical_appearance.py`, `test_observatoris_response_geometry.py` |
| CA-4 | a window of `r` bits on a cyclic shift register predicts the window `t` steps ahead with ambiguity exactly `2^{min(r,t)}` | PROVED (count the unseen bits); OBSERVED | same |
| CA-5 | a declared qubit with toolkit `{X, Z-readout}` is transcript-identical to a deterministic bit | PROVED (both operations preserve the computational basis); OBSERVED for all words of length ≤ 7 | same |
| CA-6 | with `H` added, every transcript distribution equals that of a four-state classical stochastic machine, for words of every length | PROVED (below); OBSERVED for all words of length ≤ 6 | this file; same tests |

**Proof of CA-1.** Suppose `t_a(x) ∼ x` for all `a, x`. By induction on the word, every readout
in a transcript from `x` is taken at a state equivalent to `x`, hence equals the one-shot readout
`o_a(x)`. So equal one-shot readouts imply equal transcripts, i.e. `∼` is the joint one-shot
partition, and reading each instrument once identifies the class. ∎

**Proof of CA-6.** Up to a nonzero scalar, the branch state after any outcome history lies in
`{|0⟩, |1⟩, |+⟩, |−⟩}`: this set is preserved by `X` (which swaps `|0⟩,|1⟩` and fixes `|±⟩` up to
sign) and by `H` (which swaps `|0⟩↔|+⟩`, `|1⟩↔|−⟩`); a `Z` readout of `|0⟩` or `|1⟩` returns that
value and leaves the state, and of `|±⟩` returns each value with squared amplitude `1/2` and
leaves `|0⟩` or `|1⟩`. The classical machine has exactly these four states, these transitions
and these outcome probabilities, and Born probabilities ignore the scalar. Induct on the word. ∎
The statement concerns this three-operation toolkit only. It is the one-qubit stabiliser
fragment; it says nothing about larger toolkits, several systems, or locality constraints.

**Witness table for CA-3** (✓ passes, ✗ fails; every ✗ and the decisive ✓ entries are computed
by tests, the remaining ✓ entries are immediate from the definitions).

| Carrier | free observation | predictive at long horizon | deterministic core | aligned (no hidden wire) |
|---|---|---|---|---|
| shift register through a window | ✓ (readout) | ✗ beyond the resolution | ✓ | ✓ |
| classical network with a hidden shortcut (HQ-3) | ✓ | ✓ on the experiments used to build the model, ✗ on the held-out contrast | ✓ | ✗ |
| declared qubit, toolkit `{X, Z}` | ✓ | ✓ | ✓ | ✓ |
| declared qubit, toolkit `{X, H, Z}` | ✗ | ✓ (in distribution) | ✗ | ✓ |
| destructive A,B,C carrier (inherited SUCC) | ✗ | ✓ | ✓ | ✓ |

**Verdict on the founding hypothesis (§8 of the note).** *"A system appears classical when
geometric closeness lines up with computational form and observation is free"* **SURVIVES as a
family of toolkit-relative diagnostics and FAILS as a single predicate**: the rows above realise
different pass/fail patterns, and row three shows that passing every diagnostic is compatible
with a non-classical declared carrier, while row four shows that failing some is compatible with
an exact classical stochastic model. The qualifier *appears* is not removable.

## G. Open premises and conjectures

1. **Nonlinear balance.** Is there a structural condition on nonlinear networks, analogous to
   balance, that excludes both cancellation and gating? CONJECTURED that monotone + "all contexts
   realised" suffices; not proved.
2. **Stochastic sandwich.** A may/must bracket for hitting probabilities (non-idempotent values).
   UNVERIFIED.
3. **Possible-cancellation criterion.** Characterise sign patterns admitting an exact cancellation
   at a given `(x,y,τ)`. UNVERIFIED; imbalance is necessary and not sufficient.
4. **Intercept theorem.** Conditions under which an observer can not only detect a hidden cause
   before the target is affected but also act in time. Not attempted beyond the detection bound.
5. Items listed as open in the delegated reports.
