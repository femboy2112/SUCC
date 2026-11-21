# Exact validation receipt — BORG–MAHLER

**Date:** 2026-11-20 (America/New_York). **Scope:** new isolated research folder only. Local Python standard library, no CI triggers, no source/provenance/main modifications. A same-agent alternate implementation is **not** an independent mathematical referee. The PDF primary source was reviewed in its page images (Mahler 1968 pp. 314–315).

## Local executed validations

```
python -m unittest discover -s /mnt/data/mahler_boundary_assimilation -p 'test_*.py' -v
# Ran 17 tests — OK

python /mnt/data/mahler_boundary_assimilation/independent_audit.py
# { "checks": 16453,
#   "max_numeric_spectral_error": 4.440892098500626e-16,
#   "spectral_samples_per_radius": 4096,
#   "authority": "finite same-agent exact checks; numeric quadrature not certificate" }

python -m compileall -q /mnt/data/mahler_boundary_assimilation
# Exit 0
```

**Passed exact fixtures:** 720 rational guard checks; initial-state half-open interval and first-failure comparisons for `g0=0..12`, `N=0..6` and 90 grid remainders; 2-adic W/C inversion exhaustive for all binary words through length 8; first-N Mahler 2-adic prefix congruences; real guarded prefix identity; Fibonacci forbidden-word counts; source polynomial multiplication and 79 exact four-pole rational evaluations; matched-jet root-circle mutant; original 12 hex digits imported from #681 and independent replay of their W/C 48-bit residues; radial source-root thresholds and (undefined) index at both root circles; finite mostly-F sparse-zero countermodel.

**Independent-in-code-route checks (NOT independent investigator):** 16,453 alternate checks with separate forward W/C formulas, direct rational multiplier, interval inequalities, source polynomial factor multiplication and 4,096-angle diagnostic log-Mahler quadrature at six radii away from critical roots. The spectral quadrature is *not* a rigorous integral error certificate; the exact analytic result follows from the factor roots and classical Jensen formula.

## Failed expectations repaired before freeze

- Early test used parity word `(1,1,0)` expecting different W/C starting residues at 3 bits. **False:** both maps give residue 3 there. Changed discriminator to `(0,1,1)`, where the two raw-state maps differ; full 2-adic inverse enumeration still passes.
- Rejected noncanonical all-F real encoding `0.FFF...=1` as a proposed counterexample. Replaced by a **canonical irrational** with isolated zero digits `N_k=2^(2^k)`, all other digits F. Proved in `THEOREMS.md` that it has 11-density tending to 1 in *every* late shell but has shell phase energy tending to zero along a subsequence; the finite test uses the exact `N=16,256` shadow on shell `[32,64)`.

## Untested or unclaimed

- Full inherited SUCC suite (>14k tests), root `verify_provenance.py`, foundation/ordinal scripts, hosted Actions, Lean or other external proof kernels: **NOT RUN** for this isolated stack (not even implied green).
- Exact source π first 12 hex digits: **imported from parent #681**, not independently recertified here against a fresh Machin oracle.
- Original Mahler global Z-number existence: **OPEN**. Infinite π normality/R0, source-selected signed all-shell estimate, positive integer Collatz termination, RH: **OPEN**.
- No physically interpreted wave/energy experiment or experimentally calibrated radial boundary.
- No fresh independent blind referee or external claim of academic novelty.

## GitHub publishing authority

This is an additive draft PR above the exact pinned #681 head. Published SHA and remote blob/compare verification are recorded in the PR description and should be independently rechecked by reviewers. No merges, tags, main/provenance/source changes or hosted CI were requested.
