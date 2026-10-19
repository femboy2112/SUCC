# SUCC Academic Main IV — Integration Audit (2026-10-18)

**Base `main`:** `610efacf02556e1c5922bc5d4e87d0087f19b446` (Academic Main III).
**Integration branch:** `integration/succ-academic-main-iv-2026-10-18`.
**Scope:** history-preserving consolidation of the 30 stacked draft PRs **#153–#182**.
**Firewall:** **RH PROVED: NO.** The Riemann hypothesis remains OPEN; the four-mode signed
Schur sign `S₄ = A₄ − R₄` remains **OPEN (AMBIGUOUS)**. No positive covariance, Gram, Galerkin
block, or finite-window certificate in this consolidation is the signed completed Weil form, and
no nontrivial zeta-zero ordinate is used as a construction input (independently confirmed across
all 8 tips).

Machine-readable companions: [dependency graph](SUCC_ACADEMIC_MAIN_IV_DEPENDENCY_GRAPH.json) ·
[merge coverage](SUCC_ACADEMIC_MAIN_IV_MERGE_COVERAGE.json).

## 1. True dependency DAG (git ancestry, not PR labels)

30 open draft PRs, all descending cleanly from `610efac`. Computed by commit-set membership of
`rev-list <head> ^610efac` — **8 terminal tips** (every other PR is an ancestor of one of them),
rooted in 4 children of `main` {#153, #154, #157, #178}:

```
main 610efac
├─ 153 ─┬─ 155 ·························· TIP   piecewise-Suzuki certified resolvent / K-Riesz
│       └─ 169 ─ 172 ─ 175 ─ 176 ······· TIP   Connes trace → equivariant-redundancy Weil / Möbius sieve
├─ 154 ─ 156 ─ 158 ─ 159 ─┬─ 160 … 177 ─┬─ 179 ─ 182 ··· TIP   Theorem Forge II
│                         │             └─ 181 ········· TIP   full prime-two inverse (round2-signed)
│                         └─ 161 ─ 163 ·················· TIP   SOURCE-FOUR signed S₄ enclosure
├─ 157 ─ 162 ─ 165 ─┬─ 166 ─ 167 ········ TIP   TESSAIGA×IROH factorial–LCM
│                   └─ 173 ··············· TIP   BDC bidirectional Hilbert cut / Basel–Jordan
└─ 178 ─ 180 ···························· TIP   Institute nucleus (Lean) → Round II forward-disjointness
```

The 8 tips coincide exactly with the candidate SHAs supplied to the operation, confirmed by
independent ancestry computation. Two mathematically load-bearing forks: **#181 vs #182** both
descend from #177 (the "two inverses"); **#163** forks off the #159 telescope line.

## 2. Merge method and conflict resolution

Eight `--no-ff` merges in ancestry order (182, 181, 163, 176, 155, 167, 173, 180) so shared
trunks are merged once and only genuine divergence conflicts. Result: **+84,667 insertions, 540
files, zero deletions** — purely additive; no archival original rewritten. **All 30 PR heads are
ancestors of the integration commit.**

Five conflict hunks, all additive-union registries where two independent roots append entries:

| File | Resolution |
|---|---|
| `docs/CLAIM_NAMESPACE_REGISTRY.json` | structural union — ATX and INS kept as **separate** array objects; JSON re-parses; all 16 `fq_prefix` unique |
| `docs/SUCC_RESEARCH_DEPENDENCY_DAG.md` | additive union (Academic-Transmutation + R2S + Round-II INS sections) |
| `docs/CLAIM_LEDGER.md` | additive union (ATX note + Institute INS note) |
| `docs/CLAIM_INDEX.md` | additive union (R2S bullet + Round II INS note) |

No conflict side was chosen for being newer; every divergent mathematical section is preserved.

## 3. Validation (merged tree, as one repository)

| Gate | Result |
|---|---|
| All 30 PR heads ancestors of integration | **yes, 30/30** |
| Full test suite (Python 3.12) | **`Ran 5915 tests — OK`**, exit 0 |
| `scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, **72/72 items**, 17 byte-identical archives |
| `compileall` observational_succ/tests/scripts | exit 0 |
| `observer_foundations_probe` / `ordinal_succ_report_probe` | exit 0 / exit 0 |
| Lean 4 kernel (pinned `leanprover/lean4:v4.14.0`) | all changed `.lean` typecheck; **no `sorry`/`admit`/`native_decide`, no custom axioms**; `#print axioms` = standard only (`propext`, `Classical.choice`); Forge II `ForgeGameCertificates` **axiom-free** |
| PR178 formal authority | `formal/InstituteCausal.lean` single-author (#178); integrated blob **byte-identical** to the pinned `…/formal_inputs/InstituteCausal.PR178.lean`; Forge II reconstructs-not-redefines |
| Signed-source certificates (#163/#177/#181/#182) | `first_window_sign_certified: False`, `RH_proved: False`; #181 full prime-two inverse yields strict Loewner saving both parity sectors but `new_lower_PSD: False`; Forge II directional `genuine_source_negative: false` → **S₄ OPEN** |
| External-working-directory replay | import + run from `/tmp` OK |
| `git diff --check` | only pre-existing foreign-content trailing whitespace / EOF blanks (non-gating, CI-passed in source PRs); **no conflict markers** |

CI on the exact integration SHA (Python 3.10 + 3.13 matrix + per-feature receipt lanes + Lean
gate) runs on push and is the authoritative cross-interpreter gate.

## 4. Independent hostile math audit — verdict **GO-WITH-CORRECTIONS**

Six independent read-only auditors (foundations, arithmetic, operator-theory,
analytic-source-inverse, namespace-provenance-formal, rh-firewall-status), each verdict backed by
a receipt reproduced against the live branches. All six report **no firewall breach, no zeta-zero
construction input**. No illegitimate claim is committed on any tip; the corrections below are
latent-hazard guards and label-honesty fixes.

**Corrections (ranked):**

1. **[binding at consolidation] #181 ⊕ #182 positive inverse corrections may NOT be summed.**
   Both #181 (prime-two/prime-hinge saving `C ⪰ w₀(I−A_b)`) and #182 (directional correction
   `C ⪰ Z G⁻¹ Z*`) are lower bounds on the **same** operator excess `C = D − κI`, i.e. competing
   **upper** bounds on the identical Schur residual `⟨r,D⁻¹r⟩`. `C⪰X` and `C⪰Y` do **not** give
   `C⪰X+Y`; no common operator inequality licensing the sum exists in the stack. **Rule:** keep
   #181 and #182 as *alternative* enclosures and take the better single bound, never the sum. No
   live breach today (neither branch sums them; #182's paid correction is non-PSD and adds 0;
   git ancestry `merge-base(177,181)=merge-base(177,182)=merge-base(181,182)=f309d91` is clean).
   **Hazard is latent** at deeper truncation `J`, where #182's correction could turn PSD and a
   naive sum would double-count.

2. **[applied] #163 output-field label.** `source_four_prime_schur.py` field
   `true_complete_signed_S4_sign_proved` renamed to **`source_positive_S4_first_window`** (matches
   sibling `source_four_phase_schur.py`). Its value is the first-window corrected-lower PSD test,
   not the all-radii sign; the old name was a latent overclaim. Value unchanged (emits `False` =
   AMBIGUOUS). Single referencing test updated.

3. **[handled by ancestry] #153 ⊆ #176.** The direct-quotient / affine-Pontryagin instrument
   (`direct_quotient_schur.py`, `affine_pontryagin_transfer.py`, `source_direct_quotient_gate.py`)
   is byte-identical in both branches and #153 is a git ancestor of #176; the history-preserving
   merge counts it once. No double-count.

4. **[auto-resolved] #178 INS ledger prose.** The merged `CLAIM_LEDGER.md` carries the Round II
   superset "INS-01–INS-22" (from #180), superseding #178's standalone "INS-01–INS-13/14". No
   stale count survives in the integrated tree.

**Namespace canonicalization.** 16 registry namespaces; all `fq_prefix` unique; 5 documented
*bare*-prefix collisions (PB, PH, SM, TS, WA) each disambiguated at `fq_prefix` and guarded by
`tests/test_claim_namespace_collisions.py`. The **SM** pair — `SOURCE_MINIMALITY` (`SM.MIN`) vs
`SUZUKI_MOMENT_SCHUR` (`SM.SUZ`) — is the one a careless extractor could conflate; the registry's
`resolved_collisions` integrity note ("different provenance… never merge their identities or
assert shared evidence") and the test enforce separation. ~18 feature-supplement prefixes are
unregistered by convention (the base registers only collision-prone families); none collide.

## 5. Strongest integrated results and their honest status

- **#181 full prime-two inverse:** strict positive Loewner saving in both parity sectors, with an
  exact rational, SHA-pinned source-attested error budget per quantity (contact, Γ, κ, margin).
  Still `new_lower_PSD: False` → **first-window S₄ sign not certified.** VERIFIED-EXACT-MODEL.
- **#182 Theorem Forge II:** forward-transport collapse, arithmetic rigidity, source repair;
  directional inverse obstruction `genuine_source_negative: false` on fixed retained data. Lean
  game certificates fully constructive (axiom-free). PROVED-PAPER / VERIFIED-EXACT-MODEL.
- **#163 SOURCE-FOUR:** source-conditional first-window Loewner-lower PSD test; emits AMBIGUOUS on
  committed data. Honest after the Rank-2 rename.
- **#167/#173/#176 arithmetic:** factorial–LCM duality, Basel–Jordan clock, Möbius-positive FUCC
  sieve — classical arithmetic realized as exact finite source charts; "RH-hard sensitivity" is a
  stated conditional, not an RH claim; multi-route checks flagged non-independent by the authors.
- **#178/#180 Institute + Round II:** partial causal descent, atomic/Haar thresholds, forward-only
  intertwiner obstruction, WOT/strong-vs-norm separation — Lean-kernel + paper, 22 INS declarations.

**Governing verdict.** One coherent, reproducible tree; every strong result wears a status label
its evidence earns; RH and the signed S₄ sign stay OPEN; the one load-bearing consolidation rule
(#181/#182 are alternatives, never a sum) is recorded here and must be honored by any downstream
combination.
