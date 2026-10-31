# Executed validation and proof authority

Research worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-triangle-fabric`.
Branch: `research/triangle-categorical-fabric-2026-10-30`.
Exact parent405: `6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`.
All changes are additive under this research directory. No original source,
zero boundary, archival contract, workflow or main file was edited.

## Required repository checks

- Full native suite: **10,008 PASS**,988.767s unittest time,998.180s wrapper
  time, completed2026-10-30T22:44:38UTC. `receipts/full-suite.{json,log}` retains
  full `tests/test_*.py` discovery in this worktree, with a2400-second cap
  and1024MiB address-space cap.
- Provenance: PASS,72 manifest items,17 byte-identical archives.
- Foundations and ordinal probes: PASS.
- Mathematics graph: PASS,51 typed nodes and60 edges. This validates graph
  metadata, not the truth of the linked theorems.
- Mathematics catalog: FAIL on this branch and identically on untouched
  exact parent405. Both receipts retained. The diagnostic differs only in
  the absolute worktree path; the stale catalog was not rewritten.
- Inherited artifact audit: PASS,129 parent405 artifacts and nested/source
  hashes checked. Source audit verifies391 inherited manifest files unchanged
  across six research packages,17 pinned ancestry edges and12 explicit source
  inputs including read-only siblings404/406.
- Final new-package artifact audit: PASS,136 hashed artifacts,30 Python
  syntax trees,49 JSON documents,20 local links,82 nested artifact hashes,
  29 pinned source inputs and31 recorded command-output hashes.

The full suite uses the existing Python3.13.13 environment with mpmath1.3.0,
NumPy2.5.4,SymPy1.14.0,SciPy1.18.1. `receipts/environment.*` verifies that
the imported package comes from THIS worktree, not the environment owner's
parent checkout. Numerical libraries run with one thread. Focused front
tests use Python3.12.3; their separate symbolic oracles use SymPy1.12 and,
where stated, mpmath1.2.1. No dependency installation was required.

## New mathematics and exact experiments

**43 focused unit tests passed:** root period-fiber7, constants11,
categorical14, signed11. A repeated categorical run after entrypoint placement
is retained separately and is not counted twice.

- Period fibers:12 declared and3 fresh exact families;45 separately unrolled
  symbolic-oracle cases. Source positivity follows from the global polynomial
  bound, not sampling. Complementary review adds32 fresh closed-form checks.
- Constants:24 rigorous rational-interval rows (12 two-copy,12 general-rank),
  36 exact partial-fraction identities,12 exact mark-positive cases and4
  exact above-threshold counterexamples. Separate90-digit quadratures provide
  calibration, not interval proof. See `constants/VALIDATION.md`.
- Category:1376 word-pair checks, four support-cycle ranks, three exact
  tomographies, three triangle-matched positive arrows;100 distinct-route
  Beta/interpolation/field checks. See `category/VALIDATION.md`.
- Signed:11 exact filter families and4 dyadic families. Separate Gram-Schmidt,
  exact Sturm, direct-prefix and symbolic-division oracle passes. See
  `signed/VALIDATION.md` for individual counts.
- Complementary reviews: four fresh filters/two dyadic mixtures calibrated
  with rational Machin intervals; categorical cycle/marginal checks; general
  composition Hessian, rate-variance and mark-threshold checks. High-precision
  Frullani quadratures are explicitly numerical calibration.

Universal claims rest on the displayed paper proofs, not finite experiment
counts. Distinct algorithms do not create external or independent-model
proof authority. Root and cross-front reviews retain exact reviewed hashes;
later minor text clarifications are distinguished. No new Lean formalization
or scholarly-priority claim is made.

## Repository access and hosted evidence

Initial remote receipt refreshes PR390–406. Exact parent405 had four successful
hosted workflows. The wrapper returned no PR-triggered runs for392–394;
empty lists are not PASS. The initial406 snapshot had two successful and two
running workflows. Latest statuses are separately recorded where refreshed.
The child PR body records its exact-head CI; parent CI never certifies it.

Two read-only access issues were corrected: the first full-PR-body provenance
write exceeded OS argument size, so a compact metadata record was written;
the just-updated406 commit required one targeted fetch. Neither was a test
failure or mathematical counterexample. An exploratory file lookup in the
category front is documented there. The only failing completed validation
commands are the two matched catalog checks.

## Reproduction

From the research worktree, run each focused suite without overwriting saved
receipts:

```sh
python3 -m unittest discover -s research/2026-10-30/triangle_fabric/period_preserving -p 'test_*.py'
python3 -m unittest discover -s research/2026-10-30/triangle_fabric/constants -p 'test_*.py'
python3 -m unittest discover -s research/2026-10-30/triangle_fabric/category -p 'test_*.py'
python3 -m unittest discover -s research/2026-10-30/triangle_fabric/signed -p 'test_*.py'
python3 research/2026-10-30/triangle_fabric/source_audit.py
python3 research/2026-10-30/triangle_fabric/validate_artifacts.py
```

Some probes exclusively create output files: use a disposable copy or a fresh
output name to rerun them. The source manifest excludes itself, its own audit
receipt pair and generated bytecode to avoid hash cycles. Its validator checks
all remaining artifacts, nested manifests, pinned source bytes, JSON/Python
structure, local Markdown links and recorded command-output hashes. That
audit is provenance checking, not mathematical proof checking.
