# Operation Main XIV — integration receipt

**Date:** 2026-10-28. **Status:** research-status integration of five ancestry-minimal
leaves onto a fresh branch from live `main`. No mathematical status promotion. No
publication, tag, release, force-push, or branch deletion performed.

## 1. Before / after

| | SHA |
| --- | --- |
| `main` before integration | `b763ba8ef375fbac221e29e4396989a635a6ef36` |
| Integration branch | `integration/succ-main-xiv-source-faithful-2026-10-28` |
| Integration HEAD | `b26189d6213bf4bcda0d6427de6ce8dd57a67051` |
| `main` after merge | _recorded after the authorized merge; see §9_ |

## 2. Merged leaves (ancestry verified by `git merge-base`, not PR titles)

| Lane | Leaf | Head | Subsumes (confirmed ancestors) |
| --- | --- | --- | --- |
| Lonely Runner | #353 | `6174ad022a0dead14bc6a0a4d30ec41ac0ed6c99` | #351 |
| BBP / Pólya / observer | #356 | `b89fac9aff8bc0ef20dc0f1beda0020d0141701f` | #344, #346, #347, #348, #349, #352, #354, #355 |
| Wavefront-prior sibling | #345 | `e2defca8b7741efe5aada9d9114a1cc89e0b6bf9` | forks at #344; six unique files only |
| Author provenance | #350 | `a1d01657356669ca141bab67b2fe146c6f0f9322` | standalone single document |
| Independent audit + n=31 | #357 | `249f5778c2df6a81adbe7576a86d5f0cee28d7c7` | three additive files, no production change |

All five share merge-base `b763ba8e` with live `main` (no stale-main divergence).
`--no-ff` merges preserve each original history; no parent was merged and then
re-applied as a fresh patch.

Tree delta vs `main`: **606 files added, 7 modified, 0 deleted.** The six unique
#345 files were added exactly once (357 insertions, 0 deletions).

## 3. Excluded / quarantined (verified NOT ancestors of any merged leaf)

- **DeepSeek effective-density branch** `research/deepseek-primitive-abc-effective-2026-10-28`
  (`7c79883cdc5dc75812ce7ecc0f5f871785b57670`). Its three files
  (`observational_succ/effective_density_abc.py`,
  `research/2026-10-28/PRIMITIVE_ABC_EFFECTIVE_NOTE.md`,
  `tests/test_effective_density_abc.py`) are **absent** from this integration
  (verified by `git cat-file -e HEAD:<path>` → absent). The refuted theorem is
  preserved only as the REFUTED record in `INDEPENDENT_AUDIT.md` §3.
- **#334 / #337** stale prime-ladder / Furstenberg entropy bridge: not merged; the
  refuted transcendence→entropy bridge is not restored.
- The `ravel-*` experimental branches: not in scope, not ancestors of any leaf,
  retained untouched.

The pre-existing valid effective-abc baseline (PR #212 power saving for
`0 ≤ t < 2/3`) is **unchanged** (0 file deletions; not in the modified set).

## 4. Collision reconciliation

Shared modifications between the #353 and #356 lanes:

| Path | Resolution |
| --- | --- |
| `.github/workflows/ci.yml` | Union; both rationale comments kept; `timeout-minutes: 45`; all 57 steps preserved (superset verified both directions). No check removed. |
| `docs/math_memory/CLAIM_CATALOG.json` | Regenerated from the final tree with `build_math_memory.py --write` (not `ours`/`theirs`); `--check` exit 0. |
| `docs/math_memory/INDEX.md` | Union; both new campaign sections kept with their firewall labels. |
| `docs/math_memory/TOPIC_ATLAS.md` | Auto-merged union (non-overlapping hunks); both lanes present. |
| `scripts/build_math_memory.py` | Byte-identical across lanes; `.lake` exclusion repair present exactly once. |
| `docs/math_memory/RELATION_GRAPH.json`, `tests/test_math_memory.py` | Auto-merged union (additive both lanes). |

**Catalog churn is the `.lake` scanner repair, not content loss.** `source_documents`
inventory 7317 → 1121 (6282 `.lake`-scanned entries correctly excluded, 0 remain);
`claim_files` 199 → 203 (+4 supplements); `claims` **1944 → 1990 (+46)** with **0 of
main's claim records missing**. Real content grew; only cached-mathlib pollution was
stripped.

## 5. Frozen-source preservation

Byte-identical to `main` (0 diff lines): `provenance/IMPORT_MANIFEST.json`,
`formal/duck_pi/BBPSourceGenesis.lean`, `formal/duck_pi/BBPIntegral.lean`,
`observational_succ/bbp_minimal_path.py`, `observational_succ/integer_bbp_carrier.py`.
The authentic four-pole BBP forcing and the `U0 = 0` zero seed are unchanged. No
historical theorem IDs or published receipts were rewritten; old receipts keep their
original SHAs.

## 6. Validation (local, on integration HEAD `b26189d6`)

| Gate | Result |
| --- | --- |
| `verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, 72 items, `establishes_mathematical_truth: false` |
| `observer_foundations_probe.py` | exit 0, `finite_survival_claims_are_universal_proofs: false` |
| `ordinal_succ_report_probe.py` | exit 0, `positive_definiteness_proved: false` |
| `build_math_memory.py --check` | exit 0 (unregistered research-supplement warnings retained by design) |
| `verify_math_memory_graph.py` | PASS: 51 typed nodes, 60 typed edges; proofs not independently checked |
| `python -m unittest discover -s tests` | **9783 tests**, 1 error — environment-only (see note), passes with repo root importable |
| n=31 exact holdout (`main_xiv_lonely_n31_probe.py --dual 5 8 29 30 31`) | reproduces the published census exactly; probe blob `2a65ed621b25c14116c430d01f21dc93d9b2d806` matches the audited blob |
| Lean kernel — Lonely Runner | `KERNEL_CHECKED 23 theorems; 4 paired controls` (mutants fail), allowed axioms only |
| Lean kernel — Lonely Runner growth | `KERNEL_CHECKED 18 growth theorems; 3 paired controls` incl. upper-half cubic (mutant fails) |
| Lean kernel — carry-Pólya | `KERNEL_CHECKED 9 theorems; 2 paired controls` (mutants fail), allowed axioms only |

**n=31 holdout detail (exact):** n5 → 67 w1-rows / 9 dual checks / accept {remove 1,3;
insert 6,8}; n8 → 170 / 73 / accept {remove 2,3; insert 11,13}; n29 → 6471 / 2025 /
none; n30 → 7723 / 2735 / none; n31 → 7925 / 2651 / none. Conditional on the
GAMMA-05/#353 finite-search bounds; not a universal proof.

**Note on the single test error.** `test_eodcs_meta_choice_descent.test_exact_probe_
receipt_and_independent_count` spawns a subprocess (`python scripts/meta_choice_descent_
probe.py`); locally the package is not editable-installed, so the subprocess cannot
import `observational_succ` (`sys.path[0]` is `scripts/`, not the repo root). The file
is pre-existing on `main` and unmodified by this integration; with the repo root
importable (as CI's `pip install -e ".[test]"` provides) the probe exits 0 with its
expected receipt (729 / 393 / 336; odd/even sections 0/2; `RH_proved: false`) and the
module passes 11/11. This is an inherited environment artifact, not a mathematical
regression. The hosted CI matrix on the exact final HEAD is the authoritative full-suite
gate.

## 7. Independent falsification (two blind adversaries, not same-agent review)

- **Number-theory / finite-search / refutation axis — SURVIVED.** No status inflation
  (w₂ < 28n² stays paper-level everywhere; Lean = upper-half cubic only; LRC not
  claimed). n=31 conditionality stated in receipt, audit, and script. The divisibility
  pruning was shown **provably sound** (at t = 1/r, since r < n, a covering present speed
  must be an exact multiple of r; the pruning is a necessary condition and cannot
  manufacture a false "none"). The DeepSeek REFUTED entry was independently confirmed
  **correct** (3/π² = 1/(2ζ(2)) verified to 40 digits; Montgomery 1987
  Ω_±(X√(log log X)) genuinely contradicts the claimed global O(X) bound; totients
  sieved to X = 2·10⁶ consistent with the audit's "no small-X witness" statement).
- **#356 analytic proof-status / firewall axis — APPROVE.** Every firewall-critical
  statement (the o(N) signed gate, π-normality, RH) is labeled OPEN or is a receipted
  REFUTED; no constructed positive operator/covariance is identified with Weil
  positivity; no ζ-zero is transported through a nonvanishing factor as RH evidence; the
  nine Lean exports are honest finite-algebra identities fenced off from the
  analytic/spectral claims; finite numerics and the author provenance ledger are never
  promoted to proof authority.

**Domain reinforcement gate (adversary recommendation).** The known covers n=74
(remove 70,72; insert 140,144) and n=284 (remove 280,282; insert 560,564) both fully
cover and sit strictly inside the probe's computed search domain (n=74: w1=140 ∈ [74,564],
w2=144 ∈ (140,335]; n=284: w1=560 ∈ [284,2456], w2=564 ∈ (560,1385]). The domain does not
exclude real covers.

## 8. Mathematical status (unchanged; no promotion)

| Result | Status |
| --- | --- |
| Unrestricted two-entry quadratic bound `w₂ < 28 n²` | PAPER-PROVED only; not Lean-verified, not peer-reviewed; academic priority UNVERIFIED |
| Upper-half cubic theorem `w₂ < 3 n³` + source geometry | Lean kernel-checked (18 growth exports), with mutant controls |
| Complete n ≤ 30 census; n=31 exact holdout | Exact / computationally certified, CONDITIONAL on GAMMA-05/#353 finite bounds |
| #356 divisor-boundary, Pólya-coherence, Dirichlet-resolvent | paper-proved analytic/spectral; nine finite-algebra Lean exports only |
| ζ-zero transport through a nonvanishing factor (#352) | NOT RH |
| π base-16 / base-3 normality; RH; general Collatz; shifted Lonely Runner n = 18..94 | OPEN |
| Signed gate `∀ h≠0: Σ_{n≤N} e(h·U_n) = o(N)` on the authentic four-pole source | OPEN — an unproven required cancellation, not an existing bound |
| Author analogy provenance ledger (#350) | research context / intuition, NOT theorem authority |

## 9. Follow-up obligations (non-blocking)

1. Formalize and externally review the unrestricted quadratic theorem before any status
   change; academic priority/novelty remains UNVERIFIED.
2. Independently re-derive the hard-coded domain bounds `B_n`, `Brad` in
   `scripts/main_xiv_lonely_n31_probe.py` straight from the GAMMA dossier and assert the
   coded constants equal the derived values (daniel-style calibration). The containment
   sanity gate above is the cheap discriminator; the full re-derivation is the stronger
   one. The census is labeled conditional precisely because these bounds are the single
   load-bearing unverified input.
3. Two `formal/PolyaCoherence.lean` docstrings (`scalar_overlap_obstruction`,
   `first_hahn_mode`) describe their trivial formal content in prose that overstates it;
   the corresponding ledger labels (CPS-08) are already correct, so this is documentation
   tightening for the author, not a status fix.
4. Hosted CI matrix (Python 3.10 and 3.13 + guarded Lean) must complete on the exact
   final merged HEAD; `[skip ci]` commits in the source history do not confer hosted
   authority on the merge.
