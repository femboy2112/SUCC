# Validation and reproducibility: signed-cancellation barrier

**Authority:** paper proofs and certified finite arithmetic are separate.
Base-16 normality of pi remains **OPEN**. No new Lean declaration or externally
peer-reviewed theorem is claimed.

## Source and work boundary

The native child branch is `research/pi-signed-cancellation-obstruction-2026-10-27`,
based on PR #324 at `fca58d3e0289e57596dd8ca74bace325a450df31`.
All eight requested PR heads were checked again before publication; see
[the live-head receipt](PI_SIGNED_CANCELLATION_LIVE_HEADS.json).
Main was independently read as `6dd80730c3575d91f746546a25da5aedbd2e2737`.

This is an additive research change. The authentic four-pole implementation,
zero selector, frozen archives, inherited production modules and existing tests
are unchanged. The [native snapshot](PI_SIGNED_CANCELLATION_NATIVE_SNAPSHOT.json)
records 1,304 inherited production/test SHA-256 hashes; every one was compared
after the new work. PR #315 was inspected as a sibling, not merged. There were
no writes to Claude's integration branch or main.

Six delegated lanes used separate scratch outputs. Root alone copied reviewed
artifacts into this checkout. Paper audits covered the nonzero-cut packing,
sparse two-sided seam count, finite-type estimates, moving-lag union bound,
mixing factor, E1--E7, the E6a exponent range, and E7's exact conditional second moment. The final audit corrected
two summary quantifiers: the schedule **tends to infinity** (mere unboundedness
does not suffice), and E6 gives a **liminf**, not a pointwise lower bound.
The almost-everywhere mixing/Diophantine intersection is not asserted for
every generic point. These audits use one model family; agreement is not
independent external mathematical authority.

## Native validation

The environment is Python 3.12.14, with the documented editable test install.
Exact versions and unchanged-file count are recorded in
[the environment receipt](PI_SIGNED_CANCELLATION_ENVIRONMENT.json).

| Check | Result | Raw record |
|---|---|---|
| Full native unittest discovery | 9,079 tests passed in 929.340 seconds | [Full log](pi_signed_cancellation_logs/full_native.log) |
| New focused instrument | 20 tests passed | [Log](pi_signed_cancellation_logs/new_focused.log) |
| Inherited selected-boundary / Green / bin-window / CRT / coercivity focus | 81 tests passed | [Log](pi_signed_cancellation_logs/inherited_focus.log) |
| Namespace and provenance test modules | 20 tests passed | [Log](pi_signed_cancellation_logs/namespace.log) |
| Required provenance script | Passed: 72 entries, 17 byte-identical archives, 55 namespace migrations | [Log](pi_signed_cancellation_logs/provenance.log) |
| Required observer-foundations script | Passed; its unresolved mathematical flags remain unresolved | [Log](pi_signed_cancellation_logs/observer.log) |
| Required ordinal-SUCC script | Passed; its finite-scope flags retained | [Log](pi_signed_cancellation_logs/ordinal.log) |
| Canonical exact receipt outside repository cwd | Byte-for-byte replay passed | [Log](pi_signed_cancellation_logs/outside_receipt_replay.log) |
| Independent CRT finite oracle | 8,100 refinement cases and 340 cyclic counts passed | [Log](pi_signed_cancellation_logs/independent_crt_oracle.log) |
| Independent E6/E7 finite controls | Six marker/tail bounds, two determinant branches, 134 root-grid pairs, two exact Gram forms and targeted mutations passed | [Log](pi_signed_cancellation_logs/independent_e6.log) |
| Fresh CLI receipt mutations | False normality, zero-width false energy and source-hash mutations rejected | [Log](pi_signed_cancellation_logs/receipt_mutations.log) |
| Local Markdown paths / balanced math / whitespace | Passed: nine Markdown files, local links, display-math/fence balance and staged whitespace | [Log](pi_signed_cancellation_logs/document_checks.log) |

The first attempted native run lacked optional numeric dependencies and was
stopped. After those were installed, a complete run had 9,059 tests and one
environment error: `scripts/meta_choice_descent_probe.py` could not import
`observational_succ` because the editable package installation was missing.
The original [failure log](pi_signed_cancellation_logs/initial_native_import_failure.log)
and [subprocess traceback](pi_signed_cancellation_logs/initial_subprocess_import_error.log)
are retained. Its script, implementation and test match the pinned parent
exactly; see [the byte comparison](pi_signed_cancellation_logs/inherited_error_provenance.json).
The affected 11-test module passed with the corrected import path.
Root then ran the repository-prescribed
`python -m pip install -e '.[test]'` and reran the full native suite.
No tracked implementation was patched to hide the environment failure.
A subsequent test process was lost after 1,396 progress dots, with no final
verdict; its [partial log](pi_signed_cancellation_logs/interrupted_native.log)
is retained. It is not counted as a passing run. The final run was monitored
through completion.

Hosted CI on the new commit is a separate authority and is not preclaimed by
this local record. No GitHub rendering audit or new Lean proof was performed.

## Exact instrument and error accounting

The new [probe](../../scripts/pi_signed_cancellation_probe.py) uses only the
standard library and `fractions.Fraction`; no phase is converted to float.
The literal four signed poles and their independently canceled numerator
are compared. Native source adapters are exercised without a shim.

For a rational phase, reduce exactly modulo one to [-1/2,1/2) **before**
approximation. Machin's identity uses 32-term alternating arctangent bounds
and an outward 80-bit rational enclosure of pi. A bounded angle is used in
degree-40 sine/cosine Taylor polynomials. The complete error contains the
phase-rounding debt, pi-interval debt, and `4^41/41!` Taylor remainder.
Component intervals are rounded outward and intersected with [-1,1].
Residue sums and their squared moduli use interval operations, including
intervals crossing zero. Final energies are rounded outward to 40 bits.

The authentic future tail uses exact source summation and the entire omitted
remainder bounded by

```
1 / (15 * 16^J * (n+J+1)^2).
```

Sparse future digits have their own outward remainder. Cut classification
requires containment of the whole enclosure in the half-open one-sided
window; ambiguous cases are reported, never forced into a digit.

The source-hashed [canonical receipt](PI_SIGNED_CANCELLATION_RECEIPT.json)
binds the exact probe and test bytes. It includes these finite observations:

- Actual pi carrier, n=1 through 256: zero certified cut crossings, zero
  ambiguous intervals. This supplies no asymptotic evidence or bound.
- Sparse carrier xi, with the paper's `16^(n-1)xi` indexing:
  at N=64, 48 wrap / 7 internal / 9 outside; at N=256,
  231 / 9 / 16; at N=1024, 988 / 11 / 25. No ambiguity.
- #320's nonnormal source retains exact modular balance and near-maximal
  signed energy. Unbalanced cell sizes can make the normalized energy
  slightly exceed one, exactly as E1 permits.
- E6's finite marker controls enclose rational-approximation distances
  for **all** remaining digit continuations. E7 controls retain the exact
  duplicated-endpoint debt and reject the forbidden-frequency mutation. Finite prefixes do not
  certify normality or the all-denominator theorem.
- The mixing control checks its exact rational transition minorization
  and the conservative higher-mode lower bound 49/900.

Tests also cover all sixteen cut endpoints, omitted-wrap failure, omitted
lag-span failure, nonnormal source mutations, wrong refinement direction,
nonuniform finite-lift weights, fresh de Bruijn orders and huge unwrapped
rational phases. Independent finite oracles are explicit about shared
mathematical constructions: separate implementation is corroboration, not
proof of an infinite claim.

## Reproduction

Run from the repository root:

```sh
python -m pip install -e '.[test]'
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p test_pi_signed_cancellation_probe.py -v
python scripts/pi_signed_cancellation_probe.py --verify research/2026-10-27/PI_SIGNED_CANCELLATION_RECEIPT.json
python research/2026-10-27/pi_crt_independent_oracle.py
python research/2026-10-27/pi_e6_independent_oracle.py
python research/2026-10-27/pi_receipt_cli_mutations.py
```

The probe can also be invoked by absolute path from another directory.
The committed [artifact manifest](PI_SIGNED_CANCELLATION_ARTIFACT_HASHES.json) hashes the new proofs, instrument, tests,
receipts and raw logs. Recompute it after edits; a passing receipt with
different source bytes is deliberately rejected.

The strongest new mathematical statements, their domains and next
falsification opportunities are in
[the synthesis](PI_SIGNED_CANCELLATION_SYNTHESIS.md) and
[claim supplement](../../docs/CLAIM_SUPPLEMENT_SIGNED_CANCELLATION_BARRIER.md).
The selected Weyl bound retains its inherited logarithmic order.
