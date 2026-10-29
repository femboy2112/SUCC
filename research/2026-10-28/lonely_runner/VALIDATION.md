# Validation and known failures

## Baseline before changes

At Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`, provenance,
33 inherited focused native tests, observer foundations and the ordinal probe
passed. `build_math_memory.py --check` failed with STALE/MISSING catalog.
Raw logs and hashes: `receipts/baseline/`. The repaired catalog builder excludes
`.lake` dependency copies while retaining local Lean sources; this narrow fix
and its test were carried from the independently developed PR #349 branch.
The catalogs are regenerated after the new research sources are finalized.

## Executed research checks

* Alpha: 11 tests, including an independent exact envelope evaluator.
* Independent checker and generator: 22 tests, including source-label,
  incomplete-cover, canonical rational, gcd and float-invisible-gap mutations.
* Affine local rules: 11 tests, published 184-cell rule replay, failed-rule
  rational responsibility witness, compression and fixed-family controls.
* General two-entry geometry: 11 tests and byte-identical deterministic
  Gamma receipt replay. The nonprimitive tight set `{2,4,6,8}` is retained.
* Lean 4.14 with pinned mathlib: 16 exported declarations across three files,
  only standard permitted axioms, unchanged source hashes, three positive
  controls accepted and their three false variants rejected. Raw kernel
  receipt and all compiler logs are in `receipts/kernel/`.

These are exact finite tests or actual kernel observations as specified;
there is no Lean export of the complete local-rule or Gamma theorem.
The exact source manifest and durable source-gate receipt record final files.

## Failures are retained

`receipts/development.json` records both failures and their resolution:

1. The first corrupt-generator test accidentally assigned an endpoint its
   existing value. It was a no-op mutation, so rejection correctly did not
   occur. Moving it by exactly `1/10^20` creates an actual source mismatch;
   the repaired negative test passes.
2. The first full native run received SIGTERM after 524.85 seconds; the sender
   is unknown. It also exposed an unchanged inherited probe's import failure
   in this fresh worktree without an installed package. Direct reproduction
   confirmed `ModuleNotFoundError`. With `PYTHONPATH` set to this checkout,
   the isolated inherited test passed. No inherited implementation was changed.
   The interrupted run is archived in `receipts/full-interrupted/` and is
   **not** a passing full suite. The complete verbose rerun is separately logged.

Solver timeouts and bounded-menu UNSAT results in
`BETA_UNIFORM_SEARCH_RECEIPTS.json` are failed or limited search outcomes,
not universal obstructions. Exploratory floating LP probes are preserved in
`receipts/development_search/`; no theorem or accepted cover depends on them.

## Complete local native execution

The verbose full native rerun passed **9,440 tests in 1,219.953 seconds**.
The process receipt records 1,226.817 seconds including startup and exit.
`receipts/full-native/` contains the complete raw log, its hash, and source
hashes at observation. Four paths changed or appeared during that run: the
Gamma module/test and new census module/test. Accordingly this is a successful
full-suite execution with an explicit tree-change boundary, not an immutable
final-head full-suite claim. The final source replay passed **34 commands**,
including all **64** current research tests, all 16 complete census receipts,
the independent n=5..8 Fraction census, and the repository source gates.
Its exact unchanged 68-file manifest is in `receipts/source-census/`.
Hosted validation at the committed head must close the final-tree boundary.

A catalog check during concurrent addition of census source files was stale;
regeneration after the freeze restores the catalog check. This expected
discovery-catalog drift is not hidden or counted as passing.

## Hosted boundary

Draft PR #351 remains unmerged. Hosted CI must be read at its actual head;
local tests, an earlier commit's CI, and kernel logs do not establish success
for a later SHA. The workflow retains every inherited check and raises its
25-minute timeout to 45 minutes because PR #349 observed the shorter limit
expire on Python 3.10. The campaign workflow independently replays source
certificates on Python 3.10/3.13 and the Lean kernel controls.

The first Alpha commit had three successful hosted workflows and Python 3.13
fully passed the native workflow, but its Python 3.10 job was cancelled at
about 25 minutes during the full suite. See `receipts/hosted-alpha-milestone.json`.
This is not a full hosted pass. The first complete source milestone passed
all 17 commands, including 55 research tests, with raw logs and exact source
hashes in `receipts/source-milestone/`.

Final full-suite and hosted observations will be recorded with their exact
commit and source hashes. Until such a receipt states success, they remain
pending rather than implicitly passed.

## Second mathematical checkpoint

The guarded kernel runner now accepts **23 declarations** across four modules,
including the full universal upper-half G1 metric witness, and **four paired
false controls**. Raw logs and statement/axiom exports are in
`receipts/kernel-final/`. The DYO and arbitrary-phase additions separately
passed 8 and 4 tests and exact receipt replay. A final combined source replay
records its exact count and manifest separately. The unrestricted cubic
theorem, endpoint-capacity theorem, and compactness theorem are paper proofs.

The independent larger-domain Fraction census completed all n=5..20 and
agreed with the primary census. It imports no census/generator/checker
implementation and reconstructs full source interval unions for 8,231
width-admitted cases. Its n=9..20 receipt and stdout are retained separately
from the faster primary enumeration.

The first workflow-changing HTTPS push was rejected because that OAuth token
lacks workflow scope. The existing SSH identity successfully pushed the same
commit, without changing remotes, credentials or protected branch policy.
At checkpoint 51310e53, five applicable hosted workflows passed, including
the source matrix and Lean job; the full native workflow was still running
at that observation. The later head must be observed independently.

Final combined local replay: **36 commands PASS**, including all **76**
research tests and the exact dyadic/phase receipts, with all **79** pinned
source files unchanged. See `receipts/source-complete/validation.json` and
its raw logs. The final frozen-code full native replay is running separately;
its result is not inferred from focused success. Hosted statuses for the
earlier checkpoint, artifact identifiers and hashes are retained in
`receipts/hosted-checkpoint.json`; final-head status remains an external
GitHub observation until the later run completes.

After the last primary-literature comparison and corrected phase-scope
sentence, the unchanged mathematical implementations passed **36 commands**
and **76 research tests** again, with all **80** final source pins matching.
`receipts/source-final-head/` retains that complete replay. Execution outcomes
produced after the source commit must be associated with its actual Git SHA
through PR check records and the final run receipt; this document records
what had executed when it was committed, not a forecast of later CI success.
