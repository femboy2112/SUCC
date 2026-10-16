# Collective Observer reproduction and validation

Runtime results do not certify paper hypotheses or physical source identity.
Every final local run records the interpreter, exact command, exit status,
stdout/stderr hashes and source snapshots before and after. Full-suite and
hosted statuses must be read from their own receipts, not inherited parent CI.

## Reproduce SUCC

From a checkout of this branch, create a detached sibling checkout at the exact
arithmetic pin (a fresh destination is required):

```sh
git worktree add --detach /tmp/succ-arithmetic-collective 95dbf40553e54c901e9998e14b1b9d67298fa89e
python scripts/check_collective_observer.py --full --source-root /tmp/succ-arithmetic-collective --output /tmp/collective-validation
python scripts/collective_observer_independent_audit.py --output /tmp/collective-audit.json
python scripts/collective_observer_independent_audit.py --sections spectral_source --source-root /tmp/succ-arithmetic-collective --output /tmp/collective-source-audit.json
python scripts/collective_observer_independent_audit.py --sections spectral_receipt --source-root /tmp/succ-arithmetic-collective --output /tmp/collective-receipt-audit.json
```

The runner includes provenance, all lambda/consensus/collective focused tests,
observer/ordinal gates, five new probes, the pinned source calculation and,
with `--full`, the full unittest suite. Output directories must be new; prior
receipts are never overwritten. Run separately under Python 3.10 and 3.13.
The independent signed-source audit is isolated from current-package imports.

New CI adds the same finite/source replay and independent audit under both
interpreters. Existing CI retains its full suite and project research probes.
The pinned sibling is mounted without a merge. No nontrivial zero coordinates
are inputs to the new source Schur calculation. Historical full-suite tests
remain separate calibration evidence; they are not inputs to that bound.

## Formal reproduction

YEAN branch `research/collective-observer-kernel-2026-10-16`, commit
`e62db63cad4da87ce357b62cb4379f873f3daf7c`, draft #138 contains the new
`Yean/SUCC/CollectiveObserver.lean` and its guarded runner. With the pinned
dependencies available, execute:

```sh
python3 tools/check_collective_observer.py --dependencies /path/to/pinned/.lake/packages --rust
python3 research/collective_observer_2026-10-16/refresh_source_map.py --source /path/to/SUCC --check
```

The sealed local proof manifest is
`research/collective_observer_2026-10-16/receipts/run-20261016T174742Z-2015859/manifest.json`,
SHA256 `32b23769136753dade4a9d3caa2b7fce51bc2e676fdb20edfb00eb3629ef284c`.
Lean 4.29.1 (`f72c35b3f637c8c6571d353742168ab66cc22c00`) freshly compiled
one new module; 3060 import records pin cached dependencies. This is not a
fresh full Mathlib or YEAN rebuild. All 20 theorems and 33 audited declarations
passed, ten false controls failed logically, and all 63 Rust tests passed with
Rust 1.85.1. Axiom budget: subsets of `propext`, `Quot.sound`, `Classical.choice`;
both policy theorems use none. Full elaborated types and per-declaration lists
are in the linked repository receipts.

Hosted runs 38943244649 and 38943252538 at this exact YEAN head failed before
any job steps executed because of account billing restrictions. This is
infrastructure failure, not a local kernel pass or theorem failure. The exact
annotations are preserved in `collective_observer_receipts/yean-exact-head-ci.json`.

## Preserved intermediate evidence

- Parent #140 dual-port failure: original local stack trace and hosted log;
  corrected 30-test run and actual miniature contract regression.
- Spectral lane Python 3.12.3: 4508 tests passed in 551.784s. This was a shared
  worktree run, not the principal's final stable-snapshot cross-version gate.
- Focused collective suite: 110 tests, including 26 signed spectral tests.
- First coarse source-projection attempt certified zero energy removal; its
  failed improvement receipt remains alongside the successful exact moments.
- Independent audit uses distinct partition, trajectory-tree, permutation,
  Taylor integration and PSD methods, while retaining common source premises.
- The first new hosted replay workflow at `e736f17` omitted installation of
  the existing test dependencies. Its ordinal probe failed with missing
  `mpmath`, while all other requested replay commands, including the pinned
  arithmetic calculation, passed. The failed logs/artifact are retained; the
  workflow now installs the repository's standard `.[test]` dependencies.

## Final local stable-snapshot validation

| Interpreter | Full suite | Focused interfaces | Source replay and required gates |
|---|---|---|---|
| Python 3.10.20 | 4509 passed, 717.307s, zero skips | 31 lambda + 30 consensus + 110 collective passed | Passed |
| Python 3.13.13 | 4509 passed, 509.575s, zero skips | 31 lambda + 30 consensus + 110 collective passed | Passed |

Both source snapshots remained unchanged during execution. Every one of the
4399 parent tests is retained; 110 new tests account for the final inventory.
The earlier 4508 count is explicitly a development snapshot, not this final
inventory. `principal-test-retention.json` checks that no parent test vanished.
The six exact new probe outputs, including the source calculation, are
byte-identical across interpreters. Nine independent hostile-audit sections
also pass under both versions, with stable before/after hashes. The isolated
signed-source moment and receipt audits are recorded separately and run in CI.

`principal-py310/manifest.json`, `principal-py313/manifest.json` and
`principal-validation-summary.json` bind the commands, logs and code snapshots.
`formal-source-correspondence.json` rechecks the sealed formal manifest/logs,
all 33 exact declaration types/axiom lists and eight current SUCC source files.
This last check is byte integrity and an inspected application contract, not
a new kernel run or a semantic runtime-extraction proof.

The final receipt commit is pushed after these local executions. Hosted CI on
that exact commit is checked separately and reported in the draft PR's current
validation section, avoiding a self-referential receipt commit. Earlier failed
and superseded run receipts remain frozen. An unexecuted, pending, skipped,
cancelled or billing-blocked job is not a pass.
