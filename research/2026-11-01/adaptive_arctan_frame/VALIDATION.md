# Validation, provenance, controls and explicit unrun work

**Scope:** additive, research-only package on PR #451 pinned `8ccec135f8abf64f0ea44fab555d9ac1e1b787e1`. All original four BBP poles, literal U0=0, frozen sources, prior claim contracts, production, formal/Lean, workflows and main are untouched. No pi-normality or RH theorem is claimed.

## Actually executed on local partial research snapshot

- Original parent PR #451 arctan files were unpacked from the previously produced local exact ZIP. Three load-bearing Git blob SHAs (`arctan_mirror.py`, `PROOFS.md`, `tests/test_arctan_reciprocity.py`) were checked against live GitHub #451 head, all matched. This is **not** a full SUCC checkout.
- Independent exact integer-polynomial source oracle: **`EXACT_INTEGER_POLYNOMIAL_CERTIFIED`**, including all shifted positivity identities and strict `sin(delta)>1/8` rational margin.
- New root-discoverable `test_adaptive_arctan_frame.py`: **21 methods PASS** with Python stdlib, including invalid input, independent source construction, all-h integer gap algebra, exact Gaussian powers, rational signed-phase interval oracle, old fixed-axis h=13 small-denominator, all-slow h=3 mutation, positive strictly decreasing counterfeit, and selected exact finite source samples.
- Combined available partial parent/categorical tests (previous PR #450 ZIP + previous #451 ZIP + new files): **128 discovered; 127 PASS, 1 SKIP** in forward order and the SAME in reverse order. The skip is inherited, requires the actual `observational_succ` upstream category implementation; it is **not a pass**. No conflicting test paths.
- Python `compileall` on new source and test: PASS.
- Prespecified fresh finite selected source holdouts `(N,h)=(40,13),(72,17),(96,29)` generated using outward exact Fraction/Machin/alternating/Taylor interval arithmetic at 13 terms: all PASS the derived frame inequality. Each signed mean lies within an outward decimal interval of width one unit at 10^-12 resolution, as retained in `FINITE_HOLDOUT_RECEIPT.json`. All cases were chosen before evaluating them. Receipt rerun byte-for-byte matches saved JSON.
- Optional binary64 phase diagnostics from *independent* trigonometric evaluation tested selected harmonics; these are explicitly diagnostic, **not** proof of the all-horizon bound.

## Actual defects, corrections, negative controls

1. Polynomial oracle returned tuples while a literal metadata function initially held lists: fixed type inconsistency; the independent exact integer coefficients were already equal. No mathematical certificate promoted from the failed run.
2. An interval test incorrectly required strict inequality `lo<hi` even for an exact zero phase: corrected to admit `lo=hi`. Exact integer phase `h=15,U1=2/15` is a regression case.
3. A first extremely large Gaussian power case consumed excessive resources; it was removed from the exact finite test grid (the all-h theorem is the symbolic polynomial derivation). High frequencies remain in lightweight independent float diagnostics only.
4. The first finite receipt attempted to serialize enormous rational numerators and hit Python's safe decimal-string digit limit; replaced with outward fixed-point integer endpoints and deterministic hashes. An excessive high-order Taylor budget was reduced to preregistered-certifying 13 terms, after confirming interval widths remain strictly below 1e-10. The unchanged fresh `(N,h)` cases were retained. This is an implementation precision-budget repair, not mathematical refitting of holdout signs.
5. Old fixed-axis `r(2)` mirror at `h=13` has `sin²<1/400` by *exact* Gaussian integers. Incorrect all-slow mirror index at `h=3` has `sin²<1/64` by exact Gaussian integers. Both fail the new claimed uniform `>1/8` lower bound; properly parity-alternating source labels pass.
6. For ANY finite N,H a strictly positive, strictly decreasing rational-completed counterfeit matches all finite source states/mirror labels (when L is sufficiently large). This changes the original four-pole law after L and therefore cannot contradict any theorem authenticating the full source; it refutes claiming finite empirical probes alone establish normality.

## Not run/not claimed

- Full >10,000-test SUCC root suite, official source-provenance/foundations/ordinal scripts, math-memory catalog integration, actual upstream category integration on a full repository checkout, new Lean declaration/theorem binding, external blind referee, full hosted exact-head CI.
- A source-specific all-horizon signed estimate `B_N(h)->0`, proof of π normality or RH, physical quantum interpretation, or new academic priority for standard Fourier/Weyl/Erdős–Turán theory.

**Next verdict-changing evidence:** an authenticated signed estimate surviving the altered-seed and finitely matched positive-source countermodels; preserve genuine negative signs and exact source/seed/probe provenance. Keep DRAFT pending an independent integration review.
