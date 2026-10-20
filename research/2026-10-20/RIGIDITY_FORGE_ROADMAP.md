# Rigidity Forge roadmap — capability levels (Deliverable E)

**Date:** 2026-10-20. Successor to `PROOF_FORGE_ROADMAP.md`. The operation's standard:
**Construct → Identify source → Couple → Find invariant → Bound defects → Prove
rigidity → Certify.** These obligations are kept separate (never collapsed into one
formula). Each level has a completion criterion and a benchmark theorem; a level is
"done" only when the benchmark is proved/certified and hostile-tested.

| level | capability | status | benchmark | completion criterion |
|-------|-----------|--------|-----------|----------------------|
| **1** | exact finite positivity certificates | **DONE** | finite Schur `M⪰0 ⇔ A−BD⁻¹B*⪰0` | exact PD/PSD + negative-vector witnesses; hostile wrong-inverse/wrong-block controls |
| **2** | inequality transport + honest obstruction accounting | **DONE** | form-core positivity transport + its `L²`-dense-not-core negative control | one infinite-dim transport theorem + one exact counterexample to a tempting strengthening; the 8 Gemini refutations |
| **3** | formal transport to an external checker | **see Deliverable C** | Mason–Stothers ⟶ mathlib `Polynomial.abc`; polynomial Fermat | SUCC contract discharged by the imported theorem; `#print axioms` audited; failing source-mismatch control |
| **4** | quantitative arithmetic with named machinery boundaries | **DONE as decisive no-go** | ABC-DEC-02 (`t=1/2` obstruction localized to a layer-uniform `θ=1` wall); GC-01 (exact additive Goldbach Fourier identity) | a concrete quantitative theorem OR a decisive no-go with the exact missing machinery named |
| **5** | authentic source-form positivity | **OPEN** | signed `S₄ = A₄ − R₄` sign | a sharper `κ′` on the even-parity block, on the AUTHENTIC source, with rigorous error bounds — never a finite synthetic Gram |

## Level-by-level

**Level 1 — exact finite positivity (DONE).** `quantitative_rigidity`: Sylvester PD,
all-principal-minors PSD, exact rational negative witnesses, Schur + shorted
complement, square completion. The foundation every other level reuses.

**Level 2 — transport + obstruction accounting (DONE).** Form-core positivity
transport (proved) with its negative control; the shorted-operator extension with
range inclusion; defect **non-additivity** (inverse response is quadratic); the
Bochner four-way distinction (finite PSD ⊄ global PSD ⊄ positive spectrum ⊄
source-identified Weil). The Gemini Crucible lives here: eight exact refutations, the
restricted-coercivity transfer REFUTED, the master identity NOT ADOPTED.

**Level 3 — formal transport (Deliverable C, Lean/mathlib).** Bridge the SUCC
Mason–Stothers certificate to mathlib's `Polynomial.abc`; derive polynomial Fermat.
*Next tasks:* (a) finish/confirm the pinned-mathlib bridge build and axiom audit;
(b) extend the same contract shape to Davenport's inequality and the function-field
`abc` for `K[x,y]`; (c) make `TheoremReference` axiom audits a CI gate.

**Level 4 — quantitative arithmetic (DONE as no-go).** ABC-DEC-01 exact layer
anatomy (`ris(n)^t = ∏_{j≥2} m_j^{t(j−1)}`, = BBLT Lemma 2.2 at `ε₀=0`); ABC-DEC-02
localizes the `t=1/2` ceiling to a layer-uniform `θ=1` wall and names the missing
machinery (BBLT Prop 3.1 Fourier moments + Prop 4.1 geometry-of-numbers counts).
Goldbach: `R_Λ` via `F²` (not `|F|²`), Hardy–Littlewood singular series as a certified
rational enclosure. *Next discriminating tasks:* (a) import a large-sieve / dispersion
input and test whether `S_t` bounds survive past `t=1/2` for the second moment (the
circle-method heuristic predicts the true threshold is `t<1`); (b) a bounded-exponent
major-arc estimate for `R_Λ` via Siegel–Walfisz (major arcs are CLASSICAL; the binary
minor-arc bound is the open obstruction). abc and binary Goldbach stay **OPEN**.

**Level 5 — authentic source positivity (OPEN).** The rigidity core sharpens the
`S₄` obstruction (true complement not compression; gapless high block; form-core
transfer; `#181/#182` non-additivity) but moves **no** sign. *Next probe:* a sharper
`κ′` on the even-parity block on the authentic source with rigorous error accounting.
No zeta-zero construction input; no positive-Gram-as-Weil. `S₄` sign and RH **OPEN**.

## What would change a verdict (per deliverable)
- **C:** mathlib cache pulls and the bridge typechecks → Level 3 done; else the exact
  honest blocker is the deliverable.
- **E/Level 4:** a rigorous large-sieve input beating `t=1/2` would be a genuine new
  estimate; absent it, ABC-DEC-02's localized no-go stands.
- **Level 5/RH:** only an authentic-source `κ′` improvement with error bounds; nothing
  synthetic qualifies.
