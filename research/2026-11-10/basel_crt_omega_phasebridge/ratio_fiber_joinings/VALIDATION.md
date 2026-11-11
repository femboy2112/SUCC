# Validation record / CI boundary

## Scoped execution

- Baseline: `femboy2112/SUCC` PR #588 at pinned commit `896c9ff3ceec5eb062a72cf5fc9230b6f80e2467`, based on #585 and #584. New files are additive only. AGENTS.md instructions read. The branch is not eligible for main merge ahead of ancestors or their required full gates.
- Python: 3.13.5, standard library only in the new tests and source certificate. `python -W error -m unittest -q test_ratio_fullblast.py`: **13 tests PASS**, no warnings. Individual functions use exact integer/Fraction arithmetic, with floating outputs only for presentation; exact public tick intervals are rounded OUTWARD.
- Independent basis check: original `r(n)` 4-pole sum equals the separate one-fraction formula over n=1..29. Machin rational arctan bounds independently enclose the BBP source-derived π interval. These routes share the same researcher and are not blind external reviewers.
- Finite two-to-three controls: `f(2ell)=3ell`, `f(2ell+1)=3ell+1`, root-class distinctness, twisted digit-copy constraints, synthetic uniform block counts, `K` recurrence/gcd, period-9 residues, coherent wrong seed and `1/240` common gauge.
- **Source finite holdout (not blind or random):** exact `h=8` phase means for A=263,521,1031; original source only, guard=12 extra hex digits, `2π` from rational Machin. Denote `N=L_A`; exact outward ticks are divided by 10^12:
  - A263, N44: Re [−31276714603,−31276714602], Im [−127208057554,−127208057553]
  - A521, N87: Re [88010046868,88010046869], Im [44604117458,44604117459]
  - A1031, N172: Re [54382687585,54382687586], Im [−2937036627,−2937036626]
  - First digit equality [4,11,5]; first **two** digit equality [0,0,1]; first digit parity equality [24,50,88] (ordered A263,521,1031)

- Independent high-precision smoke: MPMath 180-digit π checked against *separately derived* BBP and rational Machin enclosures; 30 independently sampled rational phase angles lay inside the exact rational Taylor enclosures. **Retained initial failure:** 75-digit MPMath precision was insufficient to discriminate the 64-hex-digit BBP interval (width ≈ 5.6×10⁻⁷⁶); after diagnosing the inadequate check precision, the check was rerun with 180 digits and passed. MPMath is NOT used to generate any of the certified source phase results.

## Crucible / limits

- Finite certified T values DO NOT prove any asymptotic trend. No cross-source probabilistic p-values or IID reference claims for π.
- Probabilistic existence of normal twisted α uses a mathematical variance and Borel–Cantelli proof, **not** observed empirical finite randomness.
- Period-9 cancellation is source-alias, not original-zero π. The sparse irrational control satisfies the full valuation passport but lacks signed cancellation on sparse epochs.
- Common-gauge shift 1/240 does not alter normality; it is a source-coordinate identification, not a Berry or Wilson holonomy.
- Source-selected ratio cancellation remains OPEN; even if proved, it does not substitute for all-mode Weyl/base-16 normality.
- **Not run:** root native ~13k-test suite, full repo provenance/observer/ordinal scripts on this new tree, Lean compilation, external blind review, hosted CI completion, quantum hardware. Required gates remain before main merge.
