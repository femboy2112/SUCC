# Operation Proof Forge III — deliverables, claim ledger, coordinator report

**Date:** 2026-10-20. **Branch:** `research/proof-forge-iii-2026-10-20`, stacked on
PR #201 (`research/rigidity-forge-2026-10-20`, head `cbc4010`), which is stacked on
PR #200, which is stacked on `main` (`0e56e0a`, **unchanged**). **Nothing merged.**
No force-push, no rewritten archival source, no release/tag, no published manuscript.

Mission: make the certification machinery itself trustworthy, and prove a genuine
quantitative-ascent theorem. Theme: *Source → exact structure → compatible local
constraints → uniform quantitative control → verified global theorem*, every arrow
carrying a checked obligation. **Do not declare the wall broken because the tool
returns `True`.**

---

## Firewall status (unchanged by this round)

**RH PROVED: NO.** ABC OPEN. integer-abc OPEN. binary Goldbach OPEN. signed
`S₄ = A₄ − R₄` sign **CERTIFIED AMBIGUOUS** (unchanged — Part III proves the
corrected rigidity core cannot move it). No nontrivial zeta-zero used as a
construction input. A positive auxiliary Gram is not signed Weil positivity. The
`#181/#182` inverse bounds remain alternatives, not additive. No `sorry` / hidden
axiom / bounded-`decide` masquerading as a universal proof.

---

## A — Trusted-kernel repair (Part I, P0 blocking soundness)

`observational_succ/quantitative_rigidity.py`. Three stop-ship defects, each
reproduced against the real code before repair:

1. **False-positive rigidity certificate.** `RigidityDiagnostics.is_genuine_certificate()`
   never checked the high block `D ⪰ 0`. Exact control `M = diag(1,−1)` (A=1, B=0,
   D=−1): a positive shorted complement (A=1) and trivial range inclusion gave
   `is_genuine_certificate()=True` while `e₂ᵀMe₂=−1`. **Fix:** `high_block_psd` is
   now a load-bearing obligation and a ground-truth `m_psd` cross-check is recorded;
   `is_genuine_certificate()` delegates to a four-valued
   `certificate_status() ∈ {VERIFIED, REFUTED, INAPPLICABLE, UNKNOWN}`. The trap is
   now **REFUTED**.
2. **Incomplete negative witness.** The old float-eigenvector + bounded-denominator
   search missed thin negative cones — e.g. `[[1,−5000],[−5000,24999999]]`
   (det −1, witness `(5000,1)` needs denominator 5000). **Fix:** a complete,
   deterministic **Lagrange symmetric-congruence reduction** (`_congruence_reduce`):
   for every symmetric rational matrix it returns either `None` (CERTIFIED PSD) or an
   exact `v` with `vᵀMv<0`. No numerical third outcome. Completeness proved
   (terminates in ≤ n steps; `W = PᵀSP` invariant maintained) and adversarially
   confirmed (40k probes; independent all-principal-minors oracle; auditor-verified).
3. **Float inputs.** `as_exact_matrix` now rejects `Float` entries
   (`RigidityInputError`); sign decisions go through exact `_sign`, raising
   `UndecidableSignError` on symbolic undecidables instead of an accidental boolean.

Regression suite: 33 tests (thin cones, huge coefficients, singular/indefinite,
nonnegative-diagonal, zero-pivot, congruence covariance, independent exact oracle,
single-sign-flip mutation, float rejection, casus-irreducibilis non-crash).

## B — Formal proof authority (Part II + Part VII, P1)

`observational_succ/proof_authority.py` (new) — a callback-free **trusted kernel**
with four disjoint levels:

- **A Claim metadata** — no authority.
- **B Locally-checked finite certificate** — witness-as-DATA validated by a
  **registered in-repo trusted checker** (no callback parameter; reuses the exact
  Schur kernel). `lambda: True` has no entry point.
- **C Formal-kernel theorem** — validated against the recorded Lean axiom-audit
  **receipt** (`formal/mathlib_bridge/axiom_audit.json`), pinned toolchain/manifest,
  `#print axioms` envelope with `sorryAx`/`native_decide` default-denied; a
  fabricated name is absent from the receipt and rejected.
- **D Original-source realization** — a Level-C theorem **plus** a registered
  source-map check on concrete data. **Level C does not imply Level D.**

`Claim.discharge` enforces, before trusting anything: evidence is an `isinstance` of
a registered artifact (a forged duck-typed look-alike is rejected), level ≥ required,
scope compatibility (a *finite* cert cannot discharge a *global* claim),
normalization match, then exact re-verification returning literal `True`; verdict is
one of the four strings, never a bare bool, never a crash.

Failure controls proven (tests): fabricated theorem name, valid theorem + invalid
source map, finite Gram vs global-kernel claim, wrong-quantifier transport,
alternative normalization, raw callback, forged object, `sorryAx`. **Two-theorem
reuse:** Mason–Stothers → polynomial Fermat (Level C/D) **and** the exact
Schur-complement theorem → a finite negative-witness/positivity application
(Level B), both through one discipline. `proof_contracts.SourceRealizationWitness`
hardened to reject raw-callback identification.

Part VII: pinned single-job CI `.github/workflows/mathlib_bridge.yml` that builds
the bridge against its recorded toolchain, audits axioms, fails on
`sorry/admit/native_decide`, runs the source-mismatch control
(`controls/WrongSource.lean`, must fail to elaborate), and Python-validates the
receipt. Coordinator re-ran `lake build` (exit 0), re-read the four axiom sets
(`{propext, Classical.choice, Quot.sound}` verbatim), and confirmed the real
receipt validates through Level C while a fabricated name is rejected.

## C — Operator-space reconciliation (Part III, P4 analysis)

`observational_succ/operator_space_dict.py` + `OPERATOR_SPACE_RECONCILIATION.md`.
The documented tension (gapless authentic high block vs `D ⪰ κI`) is resolved: these
are absolute gaps **in different metrics**. `K = V*V` makes the K-relative
derivative gap and the absolute primitive gap the *same inequality in two metrics*;
they coexist because `V` is not bounded below (`K` compact). **Theorem R3**
(re-verified with the repo's own functions): a K-relative gap *misread as absolute*
flips the certified Schur sign — `M=[[2,0,1],[0,1,0],[1,0,1/10]]`, absolute surrogate
`[1]≻0` but true Schur `[−8]≺0`, witness `(1,0,−10)`. **RH-specific deliverable:** the
corrected rigidity core does **not** change the `S₄` bound — the authentic high
block offers only a K-relative gap, so the surrogate sharpening is unsound and the
binding `1/κ=50` amplification is untouched. `S₄` sign **CERTIFIED AMBIGUOUS**.
(Documentation hazard flagged, not renamed per the no-rewrite rule: two distinct
operators are both named `K` in the archival notes.)

## D — Quantitative-ascent theorem (Part IV, P2 — the flagship)

`observational_succ/residue_box_counting.py` + `RESIDUE_BOX_COUNTING.md`.

**Theorem (CLASSICAL, exact, explicit constant).** For integer `W ≥ 1`,
`R ⊆ (ℤ/Wℤ)²`, integer `X ≥ 1`,
```
N_R(X) = (|R|/W²)·(X²/2) + E_R(X),   |E_R(X)| ≤ 5·|R|·(X/W + 1),
```
local density `|R|/W²`, main-term simplex area `X²/2`, absolute constant `5`.
Lattice-point proof + an independent floor-sum derivation; both agree exactly with
an `O(X²)` brute-force oracle (three-route cross-check, 200k+ probes, zero
violations). **Failure regime (explicit):** the main term beats the proved error
bound iff `X² > 10WX + 10W²`, i.e. `X > W(5+√35) ≈ 10.916W` (safe sufficient
`X ≥ 11W`); exact integer threshold `5W + ⌊√35·W⌋ + 1`; the estimate degenerates at
`W ≍ X`. Pushing past needs a different input (Fourier/large-sieve/dispersion).

## E — Arithmetic research (Part V abc + Part VI Goldbach, P3)

**Part V** (`abc_decomposition.py` + `ABC_CORRELATION_FRONTIER.md`):
- **ABC-DEC-02 qualified** (correctness repair of an over-broad claim): `E=1`
  (squarefree) gives local factor exactly `1−1/p²`, θ-independent, class mean `6/π²`
  for all θ → no `θ=1` wall, but **vacuous** for abc (`ris(abc)=1`); `E≥2` keeps the
  exponent-two layer `p^{θ−2}` divergence at `θ=1`.
- **Four-failure-mode ledger + guard:** (a) diagonal/Cauchy–Schwarz and (b) a
  particular Euler-product majorant are ESTABLISHED; (c) an entire proof class and
  (d) the theorem itself are **NOT** established — guards against upgrading a method
  no-go to a mathematics no-go.
- **ABC-COR-01** (heuristic main term, *not* a bound): the residue-box main term
  `(X²/2)G(t)²`, `G(t)=∏_p(1+p^{t−2}/(1−p^{t−1}))`, is finite **iff `t<1`** — strictly
  past the diagonal `t<1/2` ceiling at main-term level.
- **ABC-COR-02** (PROVED LOCAL, every t): a genuine `X²` bound on the
  bounded-powerful-part moment with explicit finite constants; inherits Part IV's
  growth boundary.
- **ABC-COR-03** (the primary deliverable — a quantified obstruction): residue-box
  gives **no** rigorous `X²` bound (error `~X^{t+2}` overwhelms `X²`); coprimality
  kills only same-prime joint occupation; the single missing estimate is a
  power/log-saving AP integer-point count uniform to `q≍X` = BBLT 2410.12234 Prop 3.1
  (Fourier moments) + 4.1 (geometry of numbers), which the diagonal/non-negative
  toolkit lacks. **ABC OPEN; `t≥1/2` moment bound OPEN.**

**Part VI** (`goldbach_circle.py` + `GOLDBACH_MAJOR_ARCS.md`):
- **GC-03 transport lemma** (CLASSICAL): for even `N`, `∏_{p≤P} 𝔖_p(N) = 2·T(P)·K(N)`
  exactly, with certified enclosure (relative width ≤ `1/(P−2)`); no Siegel–Walfisz,
  no zeta zeros. Re-verified `𝔖(2q)/2C₂ = (q−1)/(q−2)` exact for q=3,5,7,11,13.
- **Docstring repair** (the code was right): `𝔖(2q) = 2C₂(q−1)/(q−2)`, with `2C₂`
  only the `q→∞` limit, distinct from the full singular series.
- **Major-arc benchmark** under explicitly imported Siegel–Walfisz: structural,
  **flagged ineffective (no certificate)**, uniformity bounded to `q ≤ (log N)^A`; no
  arbitrary-`Q` asymptotic inferred. Binary Goldbach OPEN; minor arcs OPEN.

## F — Safe integration candidate

A **reviewable draft PR** stacked on #201 (so its diff is exactly the Proof Forge III
delta), for maintainer approval — **not** an unauthorized merge. PR #200, #201, and
this descendant are a clean stack; no duplicate commits, no claim-ID collisions. The
maintainer decides whether #200, #201 and this land on `main`.

---

## G — Final claim ledger (promoted results)

| ID | Statement | Hypotheses / scope | Status | Authority | Controls | Open debt |
|----|-----------|--------------------|--------|-----------|----------|-----------|
| PF3-I | `is_genuine_certificate` ⟺ `D⪰0` ∧ range-incl ∧ true-Schur-PSD ∧ source | finite symmetric rational blocks | PROVED LOCAL | exact sympy + 33 tests + 2 audits | `diag(1,−1)` trap REFUTED; 12k false-positive hunt | — |
| PF3-I-W | complete exact negative witness for every symmetric rational M | ℚ (exact ordered field) | PROVED LOCAL | Lagrange congruence; 40k probes vs all-minors oracle | thin cone `(5000,1)`; congruence covariance | general exact-algebraic beyond ℚ |
| PF3-II | four-level authority; metadata cannot self-elevate (typed artifacts) | the trusted kernel | PROVED LOCAL | isinstance + registry + receipt + source-map; failure-control tests | forged object, `sorryAx`, wrong source map all rejected | receipt-file provenance is an external trust boundary |
| PF3-IV | `N_R(X)=(|R|/W²)(X²/2)+E`, `|E|≤5|R|(X/W+1)` | `W≥1`, `R⊆(ℤ/Wℤ)²`, integer `X≥1` | CLASSICAL | lattice-point + floor-sum + brute, 200k probes | invalid residue/modulus; additivity; mutation | survives only `W<X/(5+√35)` |
| PF3-V-DEC02q | `E=1` ⇒ factor `1−1/p²` θ-free (vacuous for abc); `E≥2` ⇒ `θ=1` wall | squarefree vs exponent-cap classes | PROVED LOCAL | exact factor + threshold tests | over-broad old claim corrected | `E≥2` constant leans on ABC-CLK-02 |
| PF3-V-COR02 | bounded-powerful-part moment `≤ (X²/2)G_Q²+5X A_Q²+5B_Q²`, all t | `Q` fixed, coprime a+b≤X | PROVED LOCAL | census ≤ bound (t=1,2); explicit constants | — | error-dominated (not a smallness certificate) |
| PF3-V-COR03 | residue-box gives no rigorous `X²` abc-moment bound (method no-go) | the residue-box method | PROVED LOCAL (method no-go) | structural + coprimality probes | NOT a mathematics no-go | the missing uniform-AP saving estimate |
| PF3-VI-GC03 | even-N singular series `∏_{p≤P}𝔖_p = 2T(P)K(N)`, width `≤1/(P−2)` | `N` even, `P ≥ P₀(N)` | CLASSICAL | exact Euler-product + two routes | `𝔖(2q)=2C₂(q−1)/(q−2)` | — |
| PF3-III-R3 | a K-relative gap read as absolute flips the Schur sign | finite exact witness | PROVED LOCAL | repo Schur/surrogate/witness | `S₄` unchanged; no positivity manufactured | RH / `S₄` sign OPEN |

All classical theorems or refutations/obstructions — **no novel mathematics
claimed**. Academic prior art: Haynsworth/Schur shorting; Lagrange's method for
quadratic forms; Mason–Stothers (Stothers 1981, Mason 1984), mathlib `Polynomial.abc`
(Baek–Lee 2024); Hardy–Littlewood singular series; Schoenberg; BBLT (arXiv:2410.12234).

---

## Next verdict-changing probes

1. Import a large-sieve / dispersion input and attempt the uniform-AP saving
   estimate isolated by ABC-COR-03 — the single missing piece for `t≥1/2`.
2. A Siegel–Walfisz major-arc *asymptotic* for `R_Λ` (not just the transport lemma),
   with the effective-vs-ineffective constant stated.
3. Extend the mathlib bridge to Davenport / function-field abc; make the axiom
   audit a hard CI gate (the workflow is pinned; wire it into required checks).
4. A sharper even-parity `κ′` on the **authentic** `S₄` source (nothing synthetic
   qualifies) — the only lever Part III leaves for the signed sign.
