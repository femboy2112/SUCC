# Inside-Out Lambda / BBP source operator validation

**2026-10-26**, additive staging after pinned PR #310 `a8c7c85b7a1900d422090f1757c174e7aac69f44`. **π normality and RH remain OPEN.** Source originals unchanged; local results not to be confused with full native-hosted validation.

## Local isolated exact test environment (actual observations)

Tests were performed with Python 3.13 from `/mnt/data/succ_lambda_insideout` using a temporary, NON-PUBLISHED shim for the two inspected native SUCC interfaces `beck_chevalley_source.FiniteMap/finite_map` and `succ_internal_matrix_walk.authentic_r/circle`; those shims were checked against their GitHub signatures/formulas but do not replace native CI. The Oily Totient source module was copied **byte-identically** from PR #310's `observational_succ/oily_macaroni_totient.py`, Git blob `ed959983e4ab1ca874703826207f77efe8acd55d`.

```sh
PYTHONPATH="$PWD/scaffold" python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH="$PWD/scaffold:$PWD" python scripts/lambda_source_duality_probe.py --write
PYTHONPATH="$PWD/scaffold:$PWD" python scripts/lambda_source_duality_probe.py --verify
```

**Observed:** 24 focused unittest checks passed (0 failures/errors/skips), interpreter 3.13.5. Checks cover FinSet exponential and curry/uncurry, Church integer endomorphism action, exact 16th cyclotomic algebra and signed root-of-unity cancellation, `P K=I`, `K P` Fourier projection, native source recurrence/zero-anchor, actual source-selected inverse digits and integer carries, source conductor lcm, exact conditional χ², exact 15-mode spectral Parseval, dyadic parity conditional energy, all-frequency source-shift budget, and the Oily packet-grade not-equal-inverse-lift countermodel.

**Deterministic receipt:** `research/2026-10-26/LAMBDA_SOURCE_DUALITY_RECEIPT.json` written then verified byte-for-byte. A separate altered JSON claiming π normality changed false→true was **rejected** by the same `--verify` command (nonzero exit). All numeric Fourier evaluations in tests are labelled diagnostic or comparison with a proved exact/rational upper bound, not proof certificates.

### Selected finite diagnostics (not extrapolations)

| Original source sample | Exact conditional χ² | Exact h=8 parity energy |
|---|---:|---:|
| N=16, M=1 | 5/4 | 1/16 |
| N=64, M=2 | see receipt | 89/1364 |
| N=128, M=4 | 3437/10260 | 1211/40128 |
| N=256, M=4 | see receipt | 71243/4493440 |
| N=512, M=8 | see receipt | 154897/31105152 |

These finite values are not an all-N decay theorem. The synthetic uniform-digit/moving-tail control has χ²=0 at M=1 and χ²=1 at M=2, while its h=8 Weyl coefficient is `(1-i)/2`, showing why conditional information is essential. The packet grade folded mod16 has exact χ² `75912489607/38653526025`; primitive conditioning has exact χ² `65968750207/11930100625` and h=8 coefficient −1.

## Before merge / remaining CI gates

At creation of this dossier, the **full native repository suite, provenance, observer/ordinal and hosted exact-head CI had not yet been run on this new branch**. Do not promote until the actual integration head passes:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Also audit the native actual test import, claim namespace cross-file guards, original source pin and pinned formal/Lean workflows. No Lean theorem was added in this branch. The mathematical source-specific χ² estimate is a **conditional reduction**, and the claim `Δ_{N,M_N}→0` remains unproved. Explicit normality status is FALSE in test-visible code and receipt.
