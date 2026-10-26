# Spectral Purity validation and authority receipt

Base: PR #296, `461942c0bf616518e668d236d1c6b1596665a7dd`.
Branch: `research/spectral-purity-2026-10-25`.
Isolated worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-spectral-purity`.
The `source_baseline.json` receipt records the live open PR heads and source
discussion. Main was `1e3a453e869992961bc2d7f3bb6f2f1ddab38854`.

## Observed local checks

| Command / instrument | Observed result |
|---|---|
| `python scripts/verify_provenance.py` | PASS, preserved source Git blobs |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 |
| Parent IMW/SGO mathematical and native integration tests | 55 tests passed, 48.927 s |
| New innovation focused suite | 17 tests passed |
| New arithmetic focused suite | 13 tests passed |
| New multiscale focused suite | 14 tests passed |
| New selected-embedding interval suite | 6 tests passed |
| Exact probe generation followed by independent replay | PASS, rational values and source SHA256 match |
| New combined focused suite | 50 tests passed, 5.784 s |
| Claim namespace regression suite | 18 tests passed, 0.121 s |
| Explicit removal-modulus boundary holdouts | 15 exact dyadic-boundary cases passed |
| Tampered finite receipt claiming normality | Rejected, exit 1 as required |
| Full required unittest discovery | PASS: 8,405 tests, 960.127 s, exit 0 |

The actual Python interpreter is 3.12.3. Finite certificates use exact
integers/Fraction, polynomial division or rational outward intervals.
Exploratory floating-point calculations were used only to locate candidate
selected-trace failures; the committed conclusions use certified intervals.
The full suite uses `.venv/bin/python` after
`python -m venv --system-site-packages .venv` and
`.venv/bin/python -m pip install -e '.[test]'`. The environment is local to
this worktree; the installation did not replace system packages.

## Lean authority

Actual toolchain: Lean 4.14.0, commit `410fab728470`.
Mathlib: `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, with every dependency
revision checked against the repository manifest. The existing cache at
`/home/leah/SUCC-rf/formal/mathlib_bridge` was read without modifying it.

```bash
python scripts/check_spectral_purity_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output /tmp/succ-spectral-purity-lean-20261025
```

The successful receipt and logs are copied under
`spectral_purity_validation/lean/`. Ten actual declaration types and axiom
sets were exported; only `propext`, `Classical.choice`, and `Quot.sound`
occur. Two matching positive controls compiled, and two false-claim mutants
were rejected: nonnegative innovation defects, and an exceptional bound
with its good-step premise dropped. Compilation was serial, with a 2 GiB
internal memory cap. No `sorryAx` or added theorem axiom was admitted.

This authority covers finite real symmetric-kernel identities and
conditional inequalities. It does not cover complex Fourier realization,
analytic Green transport, infinite countermodel existence, prime-count
asymptotics, or pi normality. No historical formal catalogue was modified.

## Failures preserved and review corrections

- The first portable Lean run exhausted its 2 GiB internal memory budget
  while importing all tactics. Imports were narrowed. The second run
  exposed a missing `field_simp` dependency; that exact import was added.
  Both failed receipts/logs remain beside the successful kernel receipt.
- Early focused test development called a nonexistent cyclotomic `is_zero`
  method and exceeded a finite width cap. Tests were corrected to the
  actual exact-scalar API and declared budget; no assertion was weakened.
- Independent mathematical review corrected an overbroad phrase about
  absolute versus signed innovation conditions: the finite absolute bound
  loses cancellation, while existential slow-window versions can still
  be equivalent by a diagonal argument.
- Different rational pole laws do not alone prove different cumulative
  conductor towers. The multiscale dossier now states that the original
  tower is not asserted preserved; its exact four-pole mismatch is proved.
- Initial full discovery encountered `ModuleNotFoundError` in the existing
  meta-choice subprocess probe: the new worktree was not installed. The
  run was interrupted, its output retained, and test extras installed in
  the isolated environment. The exact failing test then passed. Historical
  code and tests were unchanged; the complete suite then passed in that setup.

Worker derivations share a model family and repository sources. The
cross-reviews and independent finite implementations are useful checks,
not external mathematical refereeing or multiple independent source families.

## Reproducible finite receipt

```bash
python scripts/spectral_purity_probe.py --verify \
  research/2026-10-25/spectral_purity_validation/finite_receipt.json
```

It binds the new code, source carriers, Lean file and checker by SHA256;
checks the exact sequential identity, relative trace cases, selected interval
counterexamples, conductor counts, prescribed large-horizon rational budgets,
both prefix/jet witnesses and the exact-conductor counterfeit; and retains
the highest four-bit Walsh interaction. It reports normality as unproved.
The universal results rely on the written proofs, not these finite rows.

## Markdown and delivery

Eight mathematical documents were submitted to GitHub's GFM renderer. The
receipt records source/HTML hashes and recognized math wrappers and tables;
it does not claim browser pixel inspection or a TeX kernel check. Local links
and display-math delimiters were checked. The machine-readable
`local_validation.json` binds the completed checks to their logs.

Research implementation commit: `7719e20a7c02d17bd3ef82f9ef4509d6167e12f3`.
The following receipt commit adds the explicit removal modulus, proof-boundary
clarifications and final validation records; Python/Lean sources are unchanged
from that implementation commit. Local validation is complete. The coherent
branch push and stacked draft target
`research/succ-internal-matrix-source-2026-10-25`; their final head, PR URL and
hosted CI snapshot are reported in the delivery response. Hosted success is
not inferred from these local results. At the pre-delivery audit, PR #296's
head was unchanged, with three successful workflows and the general
validation workflow cancelled. No merge or release is authorized or performed.
The normality gate remains OPEN.
