# Operation Phoenix II — Integration Audit (2026-10-14)

**Campaign:** consolidate the 2026-10-13/14 research explosion (43 open draft PRs, #57–#99) into a single reviewable integration branch and, on green gates, into `main`.

**Pre-merge `main`:** `6e0d88f1b235b85188393bbcd64ac0436cb71a70` (the 2026-10-13 many-worlds consolidation).
**Integration branch:** `integration/succ-phoenix-ii-2026-10-14`.
**Integration head:** `8d77c73c789b` (249 commits ahead of `main`; 385 files changed; +60,073 / −2).

This audit follows the precedents in `docs/INTEGRATION_AUDIT_2026-10-11.md` and `docs/MANY_WORLDS_SWARM_AUDIT_2026-10-13.md`. It is a **faithful integration**: each PR's content, claim-status labels, and firewall language are preserved verbatim. The merge does **not** newly certify any mathematics, and **RH remains open** (`RH PROVED: NO`).

## 1. Verified research DAG

All 43 PR branches were checked against real git ancestry, not PR labels:

- **Every claimed chain-parent is a real git ancestor** of its child (no broken chains).
- **All 43 branches fork from the current `main` HEAD** (`6e0d88f`). Therefore ascending PR number is a valid topological order, and merging in that order means each branch contributes **exactly its incremental diff**.
- Full per-PR data (branch, verified parent, incremental commits/files, shortstat vs main): `docs/PHOENIX_II_DEPENDENCY_GRAPH.json`.

The Black Sun line `#79 → #87 → #91 → #93` is a strict chain; incremental additions are +51 (base), then +7/+5/+5 files — confirming the cumulative PR diffs must **not** be cherry-picked in sequence. It was merged by ancestry, each unique change once.

## 2. Conflict surface (measured, not assumed)

Of 93 files touched incrementally by ≥2 PRs, **88 are byte-identical across their owners** (pure cherry-picks; git auto-resolves). Only **5 files genuinely diverge**:

| File | Owners | Resolution |
|---|---|---|
| `tests/test_zero_centered_purity.py` | 59 / 62,63,64 | **Hazard A.** #59 shipped the broken blob (`325c3e5d`, unclosed paren); #62/#63/#64 carry the fix (`b3c500c0`). Ascending merge order lands the fix on top automatically. Integrated tree = fixed; `compileall` clean. |
| `handoffs/rh/README.md` | 68,73,74,78,82,84,89,96 | **Additive union** of candidate bullets (manual at #73/#96, auto elsewhere). All firewall language preserved; footer `RH remains unsolved` intact. |
| `docs/CLAIM_SUPPLEMENT_BLACK_SUN.md` | 79,87,91,93 | Strict linear chain; tip supersedes cleanly. |
| `docs/CLAIM_SUPPLEMENT_WILD_EMBEDDING.md` | 89 vs 90 | **Two distinct lineages** (different modules/receipts) that collided on one filename. Preserved as two labeled sections (W1–W9 and WES-01–WES-11). Neither clobbered. |
| `.github/workflows/wild-embedding-succ.yml` | 89 vs 90 | Split: #89 keeps `wild-embedding-succ.yml`; #90 moved to `wild-embedding-boundary.yml`. **Both CI lanes survive.** |

## 3. Hazards (from the campaign brief)

- **Hazard A — zero-centered syntax failure:** resolved (see table). Integrated purity test is the fixed blob; whole tree `compileall` exit 0.
- **Hazard B — Black Sun numpy dependency:** numpy is imported **only** by the Black Sun chain (#79/#87/#91/#93; 3/5/7/9 files cumulative). Fixed by adding `numpy>=2.1,<3` to the `test`/`research` extras in `pyproject.toml`. CI already runs `pip install -e ".[test]"`, so the fix restores those tests in the existing lane with per-interpreter resolution (2.2.x on 3.10, 2.5.x on 3.13). No test skipped or deleted. Near-zero Black Sun eigenvalues remain **TESTED MODEL**, not positivity certificates.
- **Hazard C — near-identical branch names:** `research/signed-weiI-h1-spectral-tail-2026-10-14` (capital `I`) has head `bb5b6f96` which is **byte-identical to #82's head**, not #84's. It is a misnamed alias of #82 with **zero unique content**. Category: `DUPLICATE_REF`. Not merged; archive only.

## 4. Mathematical firewall (preserved)

- `scripts/verify_provenance.py` → `SOURCE_PROVENANCE_VERIFIED`, `establishes_mathematical_truth: false`.
- `scripts/observer_foundations_probe.py` → `finite_survival_claims_are_universal_proofs: false`; first counterexample preserved at 19.
- `scripts/ordinal_succ_report_probe.py` → `positive_definiteness_proved: false`.
- Tree-wide scan: **no file asserts RH or Weil positivity is proved**; the tree carries pervasive `RH PROVED: NO` declarations. The merge promoted nothing to "proved".

The NO-GO results listed in the campaign brief (positive source coefficients ≠ Weil positivity; compact Suzuki kernel has no fixed positive gap; strong-operator ≠ norm convergence; positive local projector ≠ complete signed Weil form; finite contour count ≠ all-height RH; moment high-subspace estimate alone ≠ low-Schur positivity; one-sided Loewner on Gamma tails) survive as the research branches' own labeled claims, carried through verbatim.

## 5. Validation

See `docs/PHOENIX_II_VALIDATION.md`. Local gates (Python 3.12, numpy 2.5, mpmath) are green. **The 3.10/3.13 CI matrix is a push-time GitHub Actions fact and is NOT asserted green here** — it requires pushing the integration branch and observing Actions, which is gated on explicit maintainer authorization.

## 6. Branch archival

See `docs/PHOENIX_II_BRANCH_ARCHIVE.md` and `docs/BRANCH_ARCHIVE_MANIFEST_2026-10-14.json`. 162 remote branches classified. No branch is deleted by this audit; the 43 #57–#99 branches retain their open PRs until the integration→main merge auto-closes them. `research/suzuki-weil-finite-to-global-2026-10-13` is **KEEP_ACTIVE** (a separate pending frontier, not integrated here).

## 7. Status

Integration branch assembled and locally validated. The merge to `main`, the push of the integration branch (required to observe 3.10/3.13 CI), and remote branch archival/deletion are **outward actions pending explicit maintainer go** — each with a staged rollback. **RH remains open.**
