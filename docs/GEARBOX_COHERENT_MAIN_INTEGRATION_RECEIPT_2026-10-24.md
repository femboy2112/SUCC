# Coherent Main X — π Gearbox integration receipt (2026-10-24)

Successor to `docs/COHERENT_MAIN_INTEGRATION_RECEIPT_2026-10-24.md`. Records the
consolidation of the full open π-source frontier onto one authenticated BBP
source. Epistemic discipline per `AGENTS.md` / `docs/METHOD.md`: labels below are
exact, finite certificates are not proofs, and no claim here promotes π normality
or RH.

## 1. Scope and base

- Prior `main`: `e648df3e4fca73ab6b942232b5ca4b310e9cac08` (PR #267, the #250–#265
  frontier).
- Open PRs consolidated: **21** — #266 and #268–#287.
- Integration branch: `integrate/succ-gearbox-coherent-main-2026-10-24`, built in
  an isolated worktree off `e648df3`.
- Frozen combined candidate (pre-merge): `b62202a3cff89993301437c910adbafe678998ba`.

## 2. Inclusion manifest — ancestry-minimal leaf set

Ancestry verified by `git merge-base --is-ancestor` against the integration tip,
**not** by PR metadata. Ten leaves cover all 21 open PR histories; no leaf is an
ancestor of another (all genuinely required); zero uncovered.

| Leaf | Head | Covers |
|---|---|---|
| #284 | `ac778d22` | #268,#270,#272,#273,#274,#277,#281,#283,#284 (deepest chain) |
| #278 | `e50a7b88` | …#274,#278 |
| #276 | `8c94abd9` | …#275,#276 |
| #280 | `e34cdb17` | #275,#280 |
| #271 | `4eafc615` | #268,#269,#271 |
| #279 | `c098f44b` | #279 (twisted-pair, independent on main) |
| #282 | `cf641d06` | #282 (integer carrier, independent on main) |
| #286 | `67582b20` | #286 (Euler–Mascheroni, independent on main) |
| #287 | `cd58a0b4` | #285,#287 (Euler-adelic) |
| #266 | `e821a90d` | #266 (diverged: 1 ahead / 56 behind main; folded last) |

Merges were history-preserving `--no-ff`. Post-merge, **all 21 PR heads are
ancestors of the candidate tip** (re-verified).

## 3. Semantic conflict decisions

- **Registries (`CLAIM_INDEX.md`, `CLAIM_LEDGER.md`, `ROADMAP.md`,
  `CLAIM_NAMESPACE_REGISTRY.json`).** Every sibling leaf re-triggered these. All
  resolved by **structural additive union** — JSON unioned by namespace identity
  with modify-conflict detection (zero modify-conflicts flagged); markdown unioned
  per hunk. Final registry: **56 namespaces**, 6 registered `resolved_collisions`.
- **README.md.** The per-cluster frontier blurbs are an additive union; a new
  umbrella entry (Coherent Main X) links the Atlas and Frontier Contract and names
  the component clusters. No contradicted material left as active guidance.
- **Two integer carriers (#281 `bbp_natural_carrier`, #282 `integer_bbp_carrier`).**
  They merged into **distinct files** (no path collision). Reconciled by proving
  they are two charts of one source: identical unwrapped $U_n$ for $n=0..59$,
  identical 2-adic reductions, matching certified hex digits against an
  independent Machin oracle. Both APIs preserved; see the cross-branch suite.
- **#266 (diverged).** Merged last; its unique commit is 27 additive files plus
  additive registry rows (one new namespace, `PI_LAG_CARRY`). No already-integrated
  content resurrected (merge-base `ea5f92bb`).
- **Claim identities.** `unregistered_prefix_collisions() == []`; all six
  bare-prefix duplicates (PB/PH/SM/TS/WA/MP) are registered collisions; dotted
  FQIDs disambiguate. No new collision introduced.

## 4. New integration deliverables

- `tests/test_gearbox_source_integration.py` — cross-branch test layer (14 tests),
  independent Machin π oracle as ground truth; one-source/two-carrier identity,
  forcing-law agreement, tail enclosures bracketing the true $\alpha=\pi/16$,
  certified-digit agreement, dyadic factorization, and hostile controls (changed
  initial state, 1/3 counterfeit, dropped forcing, non-authenticated state).
- `docs/PI_GEARBOX_ATLAS.md` — the commuting-square map and the exact missing gear.
- `docs/PI_FRONTIER_CONTRACT.md` — routes A–F with quantifiers and logical debt.

## 5. Validation evidence (combined candidate, Python 3.12)

- Import sweep: **569 modules, 0 import failures**.
- Claim scanner: `unregistered_prefix_collisions() == []`.
- New-donor suites in combination: **632 tests OK**.
- Cross-branch integration suite: **14 tests OK**, oracle-grounded.
- Full mandatory gates (`verify_provenance.py`, full `unittest discover`,
  `observer_foundations_probe.py`, `ordinal_succ_report_probe.py`) — recorded with
  exact counts and exit codes in the PR and the campaign report.

## 6. Scientific status (unchanged by this integration)

π normality, its logical independence, RH, absolute/decimal normality, the
selected signed collision/Fourier estimate (Frontier Contract A–D), and the
Euler/Li/Weil obligations (Route F) all remain **OPEN**. This round unifies
interfaces and adds cross-branch tests; it proves no new asymptotic theorem.
