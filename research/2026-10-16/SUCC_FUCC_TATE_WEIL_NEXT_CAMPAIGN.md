# SUCC × FUCC × Tate × Weil — Next Campaign Plan (2026-10-16)

Status: **planning deliverable**. Nothing here is executed or claimed as a result. It orients the next
mathematical campaign after the Academic Main II integration checkpoint (`main` ← integration head
`325309b`). See [`SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md`](../../docs/SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md).

**RH PROVED: NO.** A certified positive first-window Schur complement would establish first-window
positivity only — **not** RH at all support radii. A rigorous negative direction of the unmodified Weil
form would be extraordinary and requires hostile independent verification before any public claim.

---

## 1. The target object

```text
S_4 = A_4 − R_4          (first-window four-mode Schur complement, inverse-Neumann metric K)
```

Available within stated source hypotheses (Academic Main I + II):
- `A_4 > 0` at `a = 1/2` (WB4, PROVED LOCAL); `D_4 ⪰ (1/50) Q_4 K Q_4`.
- High-sector coercivity relative to `K` (not a gap `κ I`).
- Two-sided brackets `A_4 − L_U − 50 T_{r_U} ⪯ S_4 ⪯ A_4 − L_U` for finite rational, parity-respecting
  high Legendre responses `U`.

**Missing lemma (verdict-changing):** an authenticated high-response approximation whose *certified*
error determines `sign(S_4)`.

## 2. Priority A — construct the source oracle `CertifiedTrial(U, J, precision)`

**Precise lemma.** For finite rational parity-respecting high Legendre response `U`, truncation `J`, and
target precision, return certified rational/interval enclosures of the **original source** quantities
`A_4`, `L_U`, `T_{r_U}` and the two-sided bound `A_4 − L_U − 50 T_{r_U} ⪯ S_4 ⪯ A_4 − L_U`.

**Hard constraints (firewall).** Constant `50` and metric `K` inherited from the **four-mode** high
theorem — never transplanted from the thirty-mode or a modified source. Preserve original contact, the
positive Gamma remainder, genuine prime shifts, both completed-ζ poles, half-density. **Never** introduce
an unproved bounded inverse of the compact high operator. Require finite rational/interval evaluation
errors for each quantity, including differentiated residual tails.

**Falsifying probe.** A `U` where the certified lower bracket and upper bracket straddle 0 → AMBIGUOUS,
not a sign. An input violating parity or source-identity → INVALID SOURCE.

**Known-result recovery control (Priority B).** Before any new holdout, the oracle must independently
reproduce: WB4 `A_4 > 0`; #137 spectral-response certificates; #143 source-normalized Schur bounds; #147
exact prime-active signed spline results; #144 finite rational telescope controls. Each attempt is
classified **POSITIVE CERTIFIED / NEGATIVE CERTIFIED / AMBIGUOUS / INVALID SOURCE**.

**Independent validation.** Recompute every load-bearing enclosure by a second independent algebra
(different decomposition, outward rational intervals, alternative source representation). Two agents
repeating the same calc with the same source are **not** independent witnesses.

## 3. Priority C — four-mode vs thirty-mode transport

**Precise lemma to attempt.** State and prove (or refute) the relationship between the four-mode and
thirty-mode low/high decompositions: whether verified high-response information transports to sharpen the
four-dimensional low bracket, and how response forms, projection changes and source-dependent residual
metrics relate. **Seek a counterexample to any proposed transfer theorem before relying on it.** Do not
assume positivity or convergence rate is preserved under a different source-relative decomposition.

## 4. Priority D — finite spectral resonance & observational horizons

**Motivating question.** If an extremely deep off-critical zero existed, which finite arithmetic/spectral
observer would be forced to register its consequences, and at what cost? Connect the finite Weil test
grammar, prime logarithmic wavefronts (#137), Li-type amplification, and source-indexed observer
accessibility (#139/#143/#144). **Distinguish guaranteed finite witnesses from useful computational
discovery bounds.** Attempt quantitative complexity / support-horizon theorems; preserve negative controls
and impossibility results.

## 5. Proof-dependency graph for the campaign

```text
[WB4 A_4>0 (PROVED LOCAL)] ─┐
[high coercivity / K (import, CONDITIONAL)] ─┼─▶ (A) CertifiedTrial oracle ──▶ sign(S_4) attempt
[#147 exact prime-active source (VERIFIED EXACT MODEL)] ─┘        │
                                                                 ├─▶ POSITIVE CERTIFIED ⇒ first-window only (NOT RH)
                                                                 ├─▶ NEGATIVE CERTIFIED ⇒ hostile re-verify before any claim
                                                                 └─▶ AMBIGUOUS ⇒ refine U / J / precision
(A) ──▶ (B recovery controls) ──gate──▶ fresh holdouts at higher Legendre degree
(A) ──▶ (C) 4-mode↔30-mode transport theorem (counterexample-first)
(D) finite-witness horizon ── independent of sign, informs observer cost
```

## 6. Agent-ready work assignments (next campaign)

1. **Oracle-builder** (worktree-isolated, write): implement `CertifiedTrial(U,J,precision)` with outward
   rational intervals; emit per-quantity certified error + differentiated residual tails. Deliver the
   recovery controls (Priority B) green **before** any holdout.
2. **Independent-algebra auditor** (read-only): recompute `A_4`, `L_U`, `T_{r_U}` by a second
   decomposition; confirm enclosures agree; flag any transplanted constant/metric.
3. **Transport-theorem prover/refuter** (read-only + scratch): attempt the 4↔30 transfer lemma;
   counterexample-first.
4. **Horizon theorist** (read-only + scratch): Priority D complexity/support-horizon bounds with negative
   controls.
5. **Firewall warden** (read-only): on every artifact, confirm no promotion to "RH proved", no bounded
   inverse assumed, no covariance/Gram identified with the signed Weil form.

---

## 7. Parallel tracks (§8) — bounded, dependency-aware

Each track lists: one precise lemma · a falsifying probe · a known-result recovery control · an
independent validation method · the next verdict-changing result.

### Track I — Formal proof authority (SUCC × YEAN)
- **Lemma:** the exact SUCC/FUCC affine relation `V_p S = S^p V_p` as a source-labelled finite quotient
  identity, extractable to a YEAN finite proof kernel.
- **Probe:** a finite instance where the extracted kernel disagrees with the Python source model.
- **Recovery:** reproduce the affine two-point and rational cyclic-retract Lean instances already recorded.
- **Independent validation:** Lean/Rust kernel check **distinct** from the analytic model.
- **Verdict-changing:** a formally-checked source→kernel extraction of a residual-Schur inequality.
  (Lean/Rust checks are **not** analytical infinite-dimensional proof; the extraction is a separate obligation.)

### Track II — Effective source-indexed observers
- **Lemma:** a proof-availability condition under which cooperating observers reveal a genuinely new
  distinction (not just added terminology).
- **Probe:** a joint-history configuration that introduces a ghost (violates no-ghost gluing).
- **Recovery:** reproduce #143's collective-observer modular-integration and #144's telescope controls.
- **Independent validation:** discriminating test over source-map adequacy, not vocabulary.
- **Verdict-changing:** executable source access that strictly enlarges accessible distinctions.

### Track III — Tate / Connes normalization
- **Lemma:** identity/contact principal-value normalization of the Tate/Weil interface, source-derived.
- **Probe:** off-identity local data alone attempting to manufacture the global signed form → must fail.
- **Recovery:** reproduce #138 completed-ζ pole residues `(−1,+1)` and the exact `Γ_ℝ` normalization.
- **Independent validation:** second normalization route; compare.
- **Verdict-changing:** a source-derived trace identity that is genuinely the signed completed Weil form
  (currently absent — this is the RH-hard morphism).

### Track IV — SUCC × FUCC arithmetic dynamics
- **Lemma:** the exact braid `V_p S = S^p V_p` and the hyperbolic source
  `{n : 1≤n≤H} ≅ {α : ∏ p^{α_p} ≤ H}` as distinct from a rectangular prime-exponent box.
- **Probe:** an additive/multiplicative pair that is similar numerically but **not** conjugate.
- **Recovery:** reproduce #136/#138 unit→prime weighted equivalence.
- **Independent validation:** source map correctness, not matching numerical factors.
- **Verdict-changing:** an algebraic/probabilistic transport that is source-authenticated end to end.

### Track V — General carrier / proof geometry
- **Lemma:** a no-ghost gluing / finite-to-global completion theorem of independent interest beyond RH.
- **Probe:** a categorical obstruction that blocks the proposed functor.
- **Recovery:** reproduce the Academic Main I carrier-reconstruction certificates.
- **Independent validation:** maps + coherence laws checked, not a visual analogy.
- **Verdict-changing:** an independently interesting completion theorem with a proved preservation obligation.

Keep exploratory branches separate from integration-critical files.
