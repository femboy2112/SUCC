# Zeno–Ambient SUCC exact validation receipt and provenance boundary

**Source parent**: `research/alexander-wild-ambient-observer-2026-10-14@2feb678f9d29c2b5d520b084be62cde328a8941f` (draft PR #92). New independent research branch: `research/zeno-completion-ambient-weil-2026-10-14`. No protected branch modified. Mathematical original source: **ordinary Euler prime 2 and other authenticated primes**, original single real Gamma/Carleman C0 and completed Weil odd-pole function. No nontrivial zeros or physical instrumentation are used.

## What was actually executed locally

- Python 3.13.5 on the isolated authored new-files overlay; not a full source checkout (the container cannot resolve github.com for git clone).
- Exact parent PR #92 `wild_ambient_succ.py`, test module, probe and receipt were copied into the isolated overlay from the mounted latest V2 assets; their `git hash-object` digests were verified through the GitHub connector as:
  - module `0a84ef0d9671137567c000379935cf9a501aeb76`;
  - tests `b5b358509acbeef9702cc493aa8d469192cc8f33`;
  - probe `01262047a6515a3c9dd2b09cf539a842b63f4f2b`;
  - receipt `16946e71256cd1e380a37920cb89680cbb0a5a50`.
- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -q` -> **70/70 PASS** (39 new exact Zeno/C0/Weil tests and 31 inherited exact A5/topology tests). Distinct source/epoch/type mutation, invalid composite-place, false strong limit, broken uniform continuation, wrong parity and positivity upgrades are regression-locked.
- `PYTHONPATH=. python scripts/zeno_ambient_weil_probe.py --verify research/2026-10-14/ZENO_AMBIENT_WEIL_RECEIPT.json` -> **ZENO_AMBIENT_WEIL_RECEIPT_VERIFIED**, compared as canonical UTF-8 bytes (not only parsed JSON).
- `python -m compileall ...` on new source/tests/probe passed.
- Optional **independent** 60-digit `mpmath` comparison (different integration route): quantified continuum moving-boundary indicator norm ≈0.3244103023, certified lower 2log2/5≈0.2772588722; sharp pole Riesz integral and positive Taylor sum agree beyond 40 digits. **These are diagnostics, not interval/proof certificates.** Full numerical output frozen in `ZENO_AMBIENT_NUMERIC_HOLDOUT.json`.

## What was NOT executed or certified locally

- Complete existing ~2000+ SUCC tests or all Lean packages, as the isolated overlay does not contain the entire remote checkout.
- Python 3.10 local run; the dedicated GitHub 3.10/3.13 workflow is the separate acceptance gate and must be checked on the exact pushed commit.
- Any physical source measurement; software source stamps are not laboratory provenance.
- A source-derived independent positive realization of the FULL completed Weil form, Suzuki's conjectural global spectral limit, or RH.

**Proof scope:** ZA-06/06C are continuum all-L² boundary commutator theorems proved analytically; the rational finite matrix trials are independent calibration, not their basis. ZA-09/10 are all-H0¹ inequalities for the original odd-pole **component only**. ZA-12 is an RH-hard conditional transfer and is UNVERIFIED. See the full dossier and claim supplement for hypotheses and falsifiers.
