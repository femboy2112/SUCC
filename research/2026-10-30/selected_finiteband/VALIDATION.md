# Validation receipts and authority boundaries

All results are from the isolated child worktree `SUCC-finiteband-dispersion`,
branch `research/selected-finiteband-dispersion-2026-10-30`, parent PR411
`fa598e3a5a1111c3445200f1ddf48dcdea6bdc09`. The untouched detached parent
checkout `SUCC-finiteband-baseline` was used only for baseline comparison.
No production, source, history, main, workflow or imported theorem was edited.

## Executed validation

* **Full native suite: 10,008 tests PASS**, 966.810 seconds reported by
  unittest;975.800 seconds including runner overhead. Actual UTC execution
  2026-10-30T23:51:07 to2026-10-31T00:07:22. The source checkout imports were
  explicitly checked. This suite does not discover the new research tests.
* **43 new focused tests PASS**, counted once: kernel14, cylinders10,
  arithmetic12, root integer-interval7. Earlier repeated focused runs remain
  in receipts but are not additional tests.
* **63 inherited focused tests PASS:** PR411 finite-band12; transfer/adversary19;
  spectral14; Kempner4; Gamma geometry14. The original PR411 separate oracle
  also reproduced its three stored rows.
* Distinct front oracles and fresh cases pass: rational/SymPy cubature,
  Wronskians, exact prime cofibers, source versus Machin digit enclosures,
  Laplace/Gamma transport and independent high-precision signed products.
  Root finite interval results and all12 fresh signed-window rows pass their
  separate85-digit direct-source checks. These are complementary implementations,
  not independent external mathematical referees.
* **Provenance PASS:**72 original imports. **Foundations PASS. Ordinal PASS.**
  **Math graph PASS:**51 typed nodes,60 edges; this checks metadata, not proofs.
* Source audit verifies eight inherited research manifests, every refreshed
  PR ancestry edge, eight original source/provenance files and actual dependencies.
  Root artifact audit checks all scoped hashes, nested manifests, command-log
  hashes, JSON/Python syntax, local links, and additive-only Git scope.

Raw command receipts are under [receipts](receipts/). Front receipts and
manifests remain in their own directories. The root source manifest excludes
only itself, the recursive final audit log/metadata pair, and Python caches.

## Retained failures and corrections

1. `math-catalog` and `baseline-catalog` both fail with
   `STALE/MISSING mathematics catalog: .../docs/math_memory/CLAIM_CATALOG.json`.
   The untouched exact parent fails identically after normalizing worktree
   paths. This is a **baseline failure**, not a passing gate or new regression.
2. First `source-audit` failed because PR407 uses repository-relative manifest
   paths while older manifests use directory-relative paths. The audit was
   corrected to support the actual formats; all historical manifests remain
   unchanged.
3. `source-audit-final` then caught the shared environment's editable package
   when the audit script was launched directly from below research/. The audit
   now explicitly prepends the current checkout before importing. The native
   suite uses root `python -m unittest`, which already selects this checkout;
   a separate root import check confirmed that path. The corrected audit passes.

All four failed command receipts are preserved. No mathematical focused test
failed. Exploratory read-only path guesses for sibling dossiers and a fetch
using `deepseek-v4-pro-...` instead of actual `deepseek-v4-...` failed before
the correct paths/refs were read. One connector call used incorrect parameter
names and was retried with its required names. These access/inspection errors
are not mathematical counterexamples. The substantive provenance correction
was PR408's prior positive-prefix/jet result; see ROOT_REVIEW and the arithmetic
dossier for the narrowed final contribution.

## Environment and CI

System Python3.12.3 runs the stdlib interval code and receipt wrapper. The
existing `../SUCC-zero-dispersion/.venv/bin/python` is Python3.13.13 with
mpmath1.3.0, NumPy2.5.4, SymPy1.14.0, SciPy1.18.1. No dependencies were
installed. Long commands use a1GiB address-space cap and one numerical-library
thread. The complete suite stayed within these limits.

The starting PR411 exact head has four completed successful hosted workflows.
Related exact-head CI snapshots and live PR/head/base metadata are preserved.
The new child head's hosted CI is checked **after push** and reported with
its exact SHA in the draft PR; local results are not substituted for that
hosted status. There is no new Lean certificate, blind external referee,
scholarly-priority claim, pi-normality theorem, or RH theorem.
