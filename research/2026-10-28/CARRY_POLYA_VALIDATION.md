# Carry × Pólya × source-locked zeta: executed validation

Parent `fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`, isolated branch
`research/bbp-resolvent-observer-rigidity-2026-10-28`.
This record reports local execution before the delivery commit. The commit
containing it binds the files; the manifest and kernel observation bind the
exact tested bytes independently of a self-referential commit SHA.

## Executed gates

| Gate | Observed result | Scope |
|---|---|---|
| Full inherited native suite | **9,637 tests passed in 1051.710 seconds**, exit 0 | Python 3.12.3; discovery began before the three new test modules were added; inherited runtime files were unchanged |
| Final focused source suite | **100 tests passed**, including all **40 new tests** | 12 analytic, 17 signed-observer, 10 coherent-Pólya, one cache-isolation regression, plus 60 parent/source/catalog controls; all final test bytes checked |
| Consolidated source runner | **25 commands passed**, all exit 0 | Provenance, observer, ordinal, demo, graphs, academic VII/VIII, dependency/hostile registry, source genesis, nine test files, five independent/replay oracles |
| Source/proof manifest | **36 SHA-256 values verified** | 14 inherited source/contract/namespace files separately matched parent Git bytes; integrity is not mathematical truth |
| Imported-source provenance | **72 items verified** | 17 byte-identical research archives, 55 mechanical namespace migrations |
| Lean | **9 exported declarations checked**, **2 paired false-statement controls rejected** | Lean 4.14.0; pinned mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`; every dependency revision checked; one compiler process at a time |
| Mathematical relation graph | **51 nodes, 60 typed edges passed** | Schema/provenance/dependency lint, not a proof checker |
| Catalog | Regenerated and replayed on this checkout | Research-local warnings retained; historical namespace registry unchanged |
| Compilation / whitespace | Passed | New Python modules/scripts compiled; `git diff --check` clean |

The full inherited suite and the final new tests together cover the final
runtime additions; this is not described as one monolithic final-tree run.
The hosted broad workflow runs the complete combined suite from the pushed
head. Local baselines used SymPy 1.12 and mpmath 1.2.1 already installed on
the machine. The final consolidated replay additionally used an isolated
environment with **SymPy 1.14.0, mpmath 1.3.0, NumPy 2.5.0 and SciPy 1.18.0**;
all 25 gates and canonical receipt comparisons passed. No shared environment
was upgraded.

## Kernel authority and hostile proof checks

`formal/DivisorBoundary.lean` proves four statements: ray telescoping, the
all-horizon signed boundary identity, equality of the two flat-phase sums,
and zero flat-phase edge sum. These hold over every commutative ring.

`formal/PolyaCoherence.lean` proves five statements: row energy, weighted
row summation, the all-dimension real Gram decomposition, the first Hahn
mode identity, and the nonzero scalar-overlap witness.

The runner exports actual theorem types, normalized expression hashes,
source hashes and transitive axioms. Only standard
`propext`, `Classical.choice`, and `Quot.sound` appear. No `sorry`, `admit`,
custom axiom, `unsafe`, or `native_decide` is allowed in the proof sources.
The sign-flipped boundary identity and altered Pólya Gram coefficient fail
with actual type mismatches; corresponding true statements pass.

The source-specific Hilbert normalization, essential spectrum, full complex
channel, Hahn spectrum, Dirichlet continuation and completion obstructions
are **paper proofs**, independently rederived and cross-reviewed. They are
not implied to be formalized by those nine declarations.

## Retained hostile controls and audit corrections

- Original zero seed versus `1/15` is checked with exact rational phase
  turns. Coherent seed `-pi/16` uses certified Green-tail bounds, not a
  floating rational replacement. Wrong-forcing controls are explicitly
  outside the authentic source class.
- Matched early residues fail the exact zeta shift equation; fake primitive
  6 fails the divisor-fiber dimension; single-source zeta and double-source
  zeta squared retain distinct marginals.
- Scalar square-root Pólya amplitudes fail orthogonality; the exact radical
  environment lift passes. A same-population phase-flipped input has
  leakage 1/3 and reduced purity 5/9. Split-dependent stopping preserves
  the full terminal law while changing the internal path law.
- The root independently rederived the signed boundary count, spectral
  shell count, minimal polynomial equation, Laurent constants, and coherent
  lift identities. The analytic worker reviewed the signed proof; the
  observer worker reviewed the analytic proof; the signed worker reviewed
  the observer proof. They share the same model family and source lineage;
  this is not external peer review or three independent source families.
- A separate integration audit caught a SymPy-version field in a semantic
  receipt. It was moved to runtime metadata; polynomial receipts now use
  exact coefficient vectors. Replay under both dependency sets passed.
- A claim-table wording initially conflated nonexistence of a uniform gap
  with refuting a conditional implication assuming that gap. The final row
  correctly refutes gap existence. No impossible-antecedent inference remains.
- Initial Lean attempts used post-4.14 import paths and one redundant `simp`
  step. They failed before certification. The corrected pinned imports and
  proof compile with no admitted goals; the final exporter checks all axioms.
- The inherited mathematical catalog was stale at first inspection. Its
  scanner had included 6,282 untracked `.lake` dependency files, making
  regeneration depend on the presence of a downloaded Lean cache. The
  scanner now excludes `.lake`; a regression verifies cache-invariance
  while retaining neighboring repository proofs. The large generated JSON
  deletion removes only those dependency-cache entries, not repository
  proofs or claims. Regeneration includes inherited parent research and
  this child; historical registry entries are not rewritten. Final coverage
  is 1,956 claim rows, 176 registered namespaces and 1,066 source documents,
  with 125 explicit warnings (including research-local unregistered claims).

## Reproduction and durable evidence

```sh
python scripts/check_carry_polya_source.py --output /tmp/carry-polya-source --full
python scripts/check_carry_polya_lean.py --output /tmp/carry-polya-lean
python scripts/build_math_memory.py --check
```

The local Lean run used the existing read-only dependency project
`/home/leah/SUCC/formal/mathlib_bridge`, passed through
`--dependency-project`. All nine dependency Git revisions were checked
against the repository's pinned manifest; nothing was rebuilt in that
shared cache. Hosted execution uses a fresh pinned dependency tree.

Committed raw command logs and machine records are in
[`carry_polya_receipts/`](carry_polya_receipts/). The source runner copies
the original two parent oracle scripts byte-for-byte into a temporary
layout, then compares their output to inherited receipts, so it does not
rewrite archival files. The three new exact receipts are linked by the
[source/proof manifest](CARRY_POLYA_SOURCE_MANIFEST.json).

**Hosted CI is separate.** Before this commit is pushed, its hosted result
does not exist. The dedicated `carry-polya-source.yml` workflow runs both
Python 3.10 and 3.13 plus the pinned Lean proof/negative-control job. The
existing broad and provenance workflows also run on the delivery head.
Actual current results and downloadable logs must be read from the draft
PR/Actions run, not inferred from this local record. This file makes no
unobserved hosted-success claim.

**Open:** signed cancellation for the exact zero-seeded BBP trajectory,
π normality, RH, academic novelty and physical implementation.
