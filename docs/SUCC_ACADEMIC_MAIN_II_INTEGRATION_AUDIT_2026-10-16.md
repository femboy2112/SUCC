# SUCC Academic Main II — Integration Audit (2026-10-16)

Faithful consolidation of the **15 open draft PRs #133–#147** into
`integration/succ-academic-main-ii-2026-10-16`, targeting `main`. Successor to the Academic Main I
consolidation ([`ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md`](ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md),
`main` = `02fc9f4`).

Machine-readable coverage: [`SUCC_ACADEMIC_MAIN_II_MERGE_COVERAGE.json`](SUCC_ACADEMIC_MAIN_II_MERGE_COVERAGE.json).
Dependency graph: [`SUCC_ACADEMIC_MAIN_II_DEPENDENCY_GRAPH.md`](SUCC_ACADEMIC_MAIN_II_DEPENDENCY_GRAPH.md).
Frontier + status crosswalk: [`SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md`](SUCC_ACADEMIC_MAIN_II_RESEARCH_FRONTIER.md).

**RH PROVED: NO. The Riemann hypothesis remains open.** No positive covariance, Gram, or Galerkin block
is identified with the signed completed Weil form; `S_4 = A_4 − R_4` is unresolved.

## A. Integration

- **Pre-merge `main`:** `02fc9f46ad3b914d49df7a658e304d06ed8a6200`.
- **Integration branch head (code-final):** `325309b`.
- **DAG reconstructed from real Git ancestry** (`merge-base --is-ancestor`), not PR labels. 15 PRs form
  three strictly-stacked chains; **4 terminal tips cover all 15** (every head is a verified ancestor of
  `325309b`). `merge-base(#137,#138) = 24d0f18a` (= head of #135): #137 and #138 genuinely diverge and
  **both** tips are required.
- **Merge order (all `--no-ff`, provenance-preserving, no squash, no cherry-pick of cumulative diffs):**

  | Step | Action | Resulting commit |
  |---|---|---|
  | 1 | merge #138 `research/unit-prime-tate-log-clock-2026-10-16` (7705897a) | `c470a02` |
  | 2 | **repair #138 red CI** (exact rational ξ′/ξ shift) | `8e9fd88` |
  | 3 | merge #137 `research/arithmetic-wavefront-spectral-response-2026-10-16` (95dbf405) | `18fa247` |
  | 4 | merge #144 `research/cofinal-schur-telescope-2026-10-16` (dc497bc5) | `effb595` |
  | 5 | merge #147 `research/prime-active-source-weil-spline-schur-2026-10-16` (8bfc4a7c) | `325309b` |

- **Conflict surface:** 641 distinct changed paths, 249 touched by ≥2 tips, **245 byte-identical**. Only
  four docs diverged (README, CLAIM_INDEX, CLAIM_LEDGER, SUCC_RESEARCH_DEPENDENCY_DAG); three auto-merged
  (non-overlapping additive hunks). The single manual conflict —
  `docs/SUCC_RESEARCH_DEPENDENCY_DAG.md` — was resolved as an **additive union**: Family A's sections
  (Proof Teeth, Observer–Schur Round II, Arithmetic Resonance) and Family B's Collective Observer section
  both retained, in order, nothing dropped, no `ours`/`theirs`.
- **Branch exclusions:** none required; all 15 PRs are represented. The archived 2026-10-14 collection was
  **not** re-merged (already incorporated by earlier consolidations). The YEAN repository was **not**
  modified; its draft references and status are preserved (the YEAN release decision is out of scope).
- **Contributor identities:** the new commits `02fc9f4..325309b` carry only the maintainer's own identities
  (femboy2112 / `136249657+femboy2112` noreply / `femboy2112@gmail.com`); no stranger re-authoring (see
  Dimension A).

## B. Validation

Mandatory gates on the integration head (local, Python 3.12):

| Gate | Result |
|---|---|
| `scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, 72 items, `establishes_mathematical_truth: false` |
| `scripts/observer_foundations_probe.py` | `finite_survival_claims_are_universal_proofs: false` |
| `scripts/ordinal_succ_report_probe.py` | `positive_definiteness_proved: false` |
| `compileall observational_succ tests scripts` | exit 0 (2 benign pre-existing docstring `SyntaxWarning`s) |
| focused tests, 33 new modules | **637 tests OK** |
| full suite `unittest discover -s tests` (py3.12) | **4975 tests OK** (536.9s; +637 vs Academic Main I's 4338) |
| hosted CI, Python 3.10 + 3.13, exact head | **<HOSTED_CI_RESULT>** |

### Fixed failures

- **PR #138 (red → green).** The `completed_tate_clock` ξ′/ξ shift applied the exact polar correction
  `1/s + 1/(s−1)` through the interval engine's **outward-rounding** `__add__`. Because
  `completed_log_derivative_interval` carries an off-grid lower endpoint (prime denominator, e.g. 11 at
  P=11), the first `down()` floored it below the exact value by `< 1/10^32`, breaking the exact identity
  `ξ'/ξ(s)=Λ'/Λ(s)+1/s+1/(s−1)` (GitHub run 38859589242, Python 3.10 & 3.13). **Fix:** translating a
  rational interval by an *exact* rational is lossless, so the shifted endpoints are constructed directly
  (the idiom `logder` itself uses) — both endpoints now exact, width preserved. A new hostile regression
  `test_xi_shift_is_exact_rational_translation_not_outward_rounded` pins the exact identity on both
  endpoints and the `< 1/10^32` budget of the old path. **No floating tolerance, skip, or weakened claim.**
  The original stand-in harness asserted only the lower endpoint and did not exercise the real engine grid;
  that limitation is recorded.
- **PR #140 (historical red, repaired upstream by #143).** `KeyError: 'kind'` in
  `observational_succ/consensus_lambda.py` while reading a dual-port receipt. #143 repairs it and carries a
  regression; its exact-head CI is green. #140's historical red receipt is **preserved**, not reinterpreted
  as green.

### Unresolved issues

None blocking as of the local gates above. The hosted 3.10/3.13 CI result is the authoritative gate: it
is executed on the integration PR targeting `main` (Python 3.10 + 3.13) on the exact pushed head; the
pass count is recorded in the PR checks and the consolidation merge-commit message (the in-tree doc does
not bake the number so that the merged head stays bit-identical to the CI-tested head).

## C. Mathematics

- **Strongest established** (within source hypotheses): exact `Γ_ℝ` via two independent finite models
  (#141/#142, #145); true von Mangoldt prime powers + half-density + both poles + contact preserved under
  hostile controls (#147); the exact completed log-derivative identity (#138, repaired). WB4 `A_4 > 0`
  imported (PROVED LOCAL) — #147 adds cross-checks, **not** a first proof.
- **Conditional:** #137 dense high-response (premise: inherited coercivity `D ⪰ κK`); #144 cofinal
  telescope (its arbitrary-precision oracle does **not** exist; **not** an RH decision procedure).
- **Refuted shortcuts preserved:** positive covariance ≠ Weil positivity; positive spline Gram ≠ signed
  Weil form; positive low Galerkin ≠ positive low Schur; norm-compression ↛ zero-inverse control (REFUTED);
  finite moments alone ↛ inverse-response cap.
- **RH-hard missing lemma:** a certified high-response approximation deciding `sign(S_4)`, and the genuine
  source→Weil signed-form morphism (Track III). See the frontier doc §6.

## D & E. Next campaign and decisive probe

See [`research/2026-10-16/SUCC_FUCC_TATE_WEIL_NEXT_CAMPAIGN.md`](../research/2026-10-16/SUCC_FUCC_TATE_WEIL_NEXT_CAMPAIGN.md):
the `CertifiedTrial(U, J, precision)` four-mode Schur oracle (Priority A/B), 4↔30-mode transport
(Priority C, counterexample-first), finite-witness horizons (Priority D), and Tracks I–V. The smallest
verdict-changing probe: a single certified `U` whose two-sided bracket for `S_4` does not straddle 0.

## F. Hostile audit

Six-dimension read-only hostile audit (ancestry/provenance · CI-repair · signed-Weil/Schur ·
SUCC/FUCC/Gamma interface · docs/claim-ledger · formalization/packaging), each self-verifying serious
findings adversarially:

All six dimensions returned **PASS** or **PASS_WITH_NOTES** with **firewall_intact: true**; **0 confirmed
high/critical findings** (no adversarial verification was triggered because no dimension raised a
high/critical finding). The audit ran read-only on head `325309b` (before the deliverable-doc commit).

| Dim | Scope | Verdict |
|---|---|---|
| A | ancestry & provenance | PASS — all 15 heads ancestral; 4 tips + `merge-base(137,138)=24d0f18a`; 4× `--no-ff` merges + the #138 repair; 93 commits all the maintainer's own identity; `provenance/` tree byte-identical to `main`; 0 deletions |
| B | CI/test repair | PASS_WITH_NOTES — #138 repair is a genuine exact-rational tightening (not tolerance/skip/weaker); regression fails against the old path; #140 `KeyError:'kind'` repaired by #143 with a green regression, historical red receipt preserved; 637/637 new-module tests pass; no weakened/xfail/skip introduced |
| C | signed-Weil / Schur (firewall-critical) | PASS_WITH_NOTES — `S_4=A_4−R_4` preserved OPEN; #147 not claimed as first `A_4>0` proof; #144 telescope conditional, oracle not implemented; coercivity relative to `K` not `κI`; no Gram/Galerkin/host/covariance conflated with the signed Weil form; #138 repair firewall-safe |
| D | SUCC/FUCC/Gamma interface | PASS — braid, von Mangoldt prime powers, one real Gamma, source identity/epoch consistent; positive char-function (TMF) and signed Weil (PWS) kept distinct; numerical oracles quarantined as non-certified |
| E | docs / claim ledger | PASS_WITH_NOTES — see the `PH-` collision handled below |
| F | formalization / packaging | PASS_WITH_NOTES — YEAN kernels recorded-separately, no YEAN source touched; dep notes handled below |

**Notes acted on (this doc's branch):**
- **E (medium) — `PH-` prefix collision.** The new Profinite-Hilbert `PH-01–08`
  (`CLAIM_SUPPLEMENT_PROOF_TEETH.md`, PAPER_PROVED) reuse the `PH-` prefix of the pre-existing Prime Form
  Heat `PH-01–15` (`CLAIM_SUPPLEMENT_PRIME_FORM_HEAT.md`, CLASSICAL). Faithful integration preserves each
  PR's content verbatim (renaming the research + its `profinite_hilbert.py`/receipt references is out of
  scope and risky), so the collision is now **explicitly flagged** in `CLAIM_INDEX.md` (⚠ in the family
  table + an integrity note) rather than left silent; the two namespaces are disjoint in meaning and must
  be disambiguated by supplement file. A future cleanup may renumber the newer IDs.
- **E (low) — O-count wording.** An earlier draft asserted "679 distinct `O####` rows" with "no collision";
  corrected to the verified facts: this integration adds **no** `O####` rows (count unchanged from `main`),
  no duplicate `O####` rows, and the one real `PH-` collision is flagged.
- **E (info) — DAG additive-union seam.** Added the missing blank line before the Collective Observer header.
- **F (low) — stale `pyproject` comment.** Updated: `sympy` is now genuinely exercised by #145's tests and
  installed by both extras.
- **F (low) — unguarded `sympy` import in `test_factorial_gamma_fucc.py`.** Left as-is by design: `sympy` is
  a declared `[test]` dependency, so a hard `ImportError` on a deps-less runner is the correct fail-loud
  behaviour (the prompt forbids globally silent skips); CI installs the extras.
- **C (low) — `PAPER_PROVED` on a criterion-failure no-go.** Pre-existing PR research label; the audit
  confirms it labels a *proved no-go* (a sufficient criterion fails), **not** `S_0` positivity — firewall
  intact. Research claim left verbatim per faithful-integration policy.
- **A/B (info) — identity & tolerance notes.** The 54 "Leah" vs 39 "femboy2112" commits are the same
  account (noreply embeds id `136249657+femboy2112`); the `72` provenance items are manifest entries
  (17+55), with the `provenance/` tree byte-identical to `main`; research float/mpmath tolerances are
  numeric readouts, not proof certificates (firewall already states this). No action required.

Audit workflow: `wf_14008625-580`, 6 agents, 0 errors, 706k subagent tokens. Full per-dimension findings
are in the workflow journal.
