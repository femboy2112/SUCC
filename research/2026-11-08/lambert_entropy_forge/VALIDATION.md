# Validation and provenance — Lambert-W entropy forge

**Scope:** 2026-11-08 research-only, based on SUCC draft #559 exact head `44a4a96d2180a66524f882e4a1d50309fc8c97a9`. Frozen holdout protocol: GitHub commit `c207e377143818f95ec12957849834e1d3113661`, **before new-digit analysis**. No source, zero seed, imported provenance, Lean file, workflow or main default is edited. π normality and #544 signed covariance remain OPEN.

## Actual local execution

Python **3.13.5**; repository-stacked new files run against inherited #559/#557 source and test modules. A local minimal copy of the unchanged `duck_bbp` source API was used only to enable the inherited archive in the isolated worktree; it is **not part of this PR**. Source-independent bulk digits are generated in `bbp_bulk_certificate.py` using the unchanged four rational poles and a strict integer enclosure.

1. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_lambert_entropy_forge.py' -v`: **30/30 focused tests PASS**, exit 0; executable tests of exact digit/collision identities, finite entropy inequalities, complementary constant/periodic/coupon controls, dense-checkpoint gluing, trimmed subset, source-bulk prefix and new source receipt.
2. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_bbp_word_spectroscopy.py' -v`: **19/19 inherited spectroscopy tests PASS**, exit 0.
3. `PYTHONPATH=. python research/2026-11-08/lambert_entropy_forge/experiment.py`: exit 0; independently reconstructs the original signed four-pole source coefficient at **all n=1..40,984**, builds a complete rational BBP interval for first **40,960** hex digits (guard=24), aborts if either endpoint crosses a requested digit boundary, and requires exact equality to the already independently per-step-certified 16,384-digit prefix (#557). No digit is inserted from a π lookup table. Replays **16 frozen seeded shuffles** and 4 controls, with all signed chronological lag corrections retained and 5 checkpoints.
4. `sha256sum ...` before/after a complete second source+receipt regeneration: **both hashes identical**, no manual receipt edits.
5. The direct per-step rational orbit run from the frozen protocol was first attempted and stopped after **12,288 already previously certified digits** due to increasing integer-denominator cost, **before analyzing any new word statistics**. The faster alternative is an algebraically equivalent **BBP original-source rational interval** derived in THEOREMS.md; the frozen horizon, controls and claimed digits were unchanged. This is documented openly rather than claiming the original slow command completed.

### Exact immutable outputs

- `CERTIFIED_HEX_40960.txt` SHA-256: `c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527`
- `FINITE_RECEIPT_40960.json` SHA-256: `7f3e5ab1f776e69ae6e4ebfa8198d6d9c0b5a991da49bde9198952718873586a`
- The *first* 16,384-digit prefix matches the predecessor's `CERTIFIED_HEX_16384.txt` byte-for-byte for the hexadecimal characters (case-insensitive normalization). This is a reproducibility cross-check, not an independent random sample.

**Frozen source holdout:** N=40,960, W depth 3; all 4096 distinct three-digit words appear; first complete chronological coverage occurs at n=31,816; `D3=40,850`, `E3=817/8192`, `max count=23`, exact signed pair correction `−50`. Signed first64 lags and all lag residuals are saved. The 16 same-count shuffle D/N values lie in the observed range [0.955078125,1.034228515625]. No P value, iid claim or infinite rate is inferred.

## Proof authority boundaries

- LWE-01 coupon collector, Lambert W and gamma sharp cutoff: **classical inputs**; actual digit histories overlap, unlike the coupon reference.
- LWE-02 exact integer collision sum, LWE-03 finite cyclic entropy inequality, LWE-05 checkpoint gluing, LWE-09 trimmed finite inequality: **paper proofs** with independent finite hostile controls; LWE-03/LWE-09 specialize the inherited SUCC HJA/SCE methods.
- LWE-06 normal-but-spiky: **paper theorem** built on classical Champernowne base-b normality.
- LWE-07 fast exact BBP integer certificate: **proved conditional on the classical BBP π series identification**, not a new π formula or full formal Lean result.
- LWE-08 measured finite statistics: **OBSERVED** at exactly declared horizon, no extrapolation.
- LWE-10 true original source growth estimate: **OPEN**. No estimate for all integer epochs or dense checkpoint sequence is provided.

**Not run locally here:** full SUCC native ~12K tests, repo-wide `scripts/verify_provenance.py`, observer-foundations/ordinal probes and Lean kernel suite, because this isolated research worktree is not a complete repository checkout. Hosted GitHub CI must be checked at the exact final PR head before any merger recommendation. Do not count inherited historical suite results as tests on this branch.
