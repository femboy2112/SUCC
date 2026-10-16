# Prime-active Weil / Suzuki low-Schur hostile audit

**Date:** 2026-10-16. **Research branch:** `research/prime-active-source-weil-spline-schur-2026-10-16`.
**Parent pinned:** `d7545a1c5fe7b16d12af877513283f802f3d151d` (SUCC draft PR #146). No original/imported module changed. Full repository not available in the local trimmed test tree; GitHub hosted full-suite CI remains separate and is NOT pre-claimed.

## Source identity / prior-art ablation

- Genuine completed zeta Weil source is **already** identified classically via `research/2026-10-15/TATE_TO_WEIL_DISTRIBUTION.md`, CTW-08: conductor 1; one even real Gamma; canonical contact `-gamma_E-log(4*pi)`; both poles 0,1; prime powers `Lambda(p^k)=log p`; half-density `n^-1/2`. No nontrivial zeta-zero inputs.
- `research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md` gives existing `W=-g''` for contact-matched finite source, with error estimates. `research/2026-10-15/ONE_OBJECT_RESIDUAL_SCHUR.md` gives the K-relative variational short. Existing `docs/CLAIM_SUPPLEMENT_TATE_WEIGHTED_BESSEL_FOUR.md`/WB4-LOW had **already proved all four original low Legendre A modes strictly positive** using J64 and true source, with high `D4 >= K/50`. Present first two low entries are an **independent exact-polynomial holdout**, NOT a new low-A4 positivity theorem.
- The new calculation evaluates an *actual*, signed, prime-active, two-test Weil Gram and authentic Suzuki K-relative form with pure-rational enclosures. Its only newly verified sign is for a **restricted** two-dimensional spline plane; the four-mode short `S4=A4-R4` remains completely unresolved.
- Same-paper classical tools (Gamma tail, B-spline convolution, Legendre projection, Poisson/Weil identification) are **dependencies**, not independent discovery witnesses. Mpmath numerical holdouts are independent implementations of selected integrals, not proof of universal theorems.

## Hostile controls and corrections

1. A first exploratory source recognizer accepted `n=6` as a prime power and created a **spurious negative Gram**. It was **refuted and replaced** by extraction of a single true prime base p with exact residue check. The rejected run was not interpreted as RH evidence; unit tests reject composites 6,10,12,15,18,30,36,42.
2. Correct support radius 0.9 cannot observe n=6 (log6>0.9); forcing a fake impulse into the small window is inadmissible. A separate larger-support control produces the predicted negative mutant *difference* without claiming a genuine zeta negative form.
3. Wrong contact `W - delta0/8` produces a certified negative vector whereas genuine W has positive 2D Gram. Contact `delta0 -> K` is tested using the genuine inverse-Neumann metric.
4. Arbitrarily small right-half-plane non-Euler positive multiplier `1+6^(3m)(6^(4m))^-s` creates exact offcritical zeros of the **mutated** product: a counterexample to unqualified analytic continuation stability, NOT to RH.
5. Exact Legendre projections disclose nonzero 30-high leakage although small; new **four-low** projections have exact relative residual squares `2809/6250` and `869/3125`, so P30-nearness cannot justify a WB4 P4-short claim.
6. Low positive P1/P2 entries at J64 are enclosed with original source, but the true four-mode zero-shift `R4` is not bounded. A positive low A4 (previously proved) does not imply positive `A4-R4`; adding a nonnegative toy high response reverses the first scalar sign.
7. Partial local code and tests are *new* modules; no imported source SHA is dynamically attested by these tests. The source matches the documented canonical normalization; full repo integration must preserve the SHA gate of the pre-existing SUCC source.

## Local reproducibility (observed, not CI)

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python scripts/prime_active_weil_spline_probe.py --verify
```

**Executed:** 89 tests, 0 failures, 0 errors, 0 skips in the trimmed local tree (includes 19 new PWS tests, and 70 already-existing local FGF/TMF tests), plus exact deterministic receipt verification. Independent mpmath high-precision quadrature and symbolic controls included. See `PRIME_ACTIVE_WEIL_SPLINE_TEST_LOG.txt` for raw output. The rational interval computations are mathematically bounded but the imported Suzuki/Weil identification remains a classical source theorem; Python tests are not a substitute for independent peer audit.

## Scope-specific next verdict-changing probe

At a=1/2 work in the **four**, not thirty, low Legendre modes P1..P4 from WB4-12/13/LOW. Use actual original source finite-J operator G_J, previously certified high `Q4 G Q4 >= (1/50) Q4 K Q4`, and choose a finite parity-respecting high trial `Y`. Construct outward rational `A4`, `L_Y=Y*B+B*Y-Y*DY`, and derivative residual Gram `T_r=<r_i',r_j'>`; prove `A4-L_Y-50 T_r >=0` or find a source-certified negative vector against **original** G. Discriminating outcomes: POSITIVE **only at a=1/2**, NEGATIVE original Weil (would refute RH), AMBIGUOUS, or INVALID source/probe. `Y=0` is a calibrated weak control; use fake6/wrong contact/wrong gamma/pole and parity mutants without contaminating the genuine candidate. No arbitrary positive Gram substitutions or invertible compact D assumptions. For all-radii RH, any first-window proof must be generalized to all support radii with authentic new prime activations.

**Claim ledger:** PWS-01..PWS-11 in `docs/CLAIM_SUPPLEMENT_PRIME_ACTIVE_WEIL_SPLINES.md`. **RH PROVED: NO.**

## Local Git blob SHA-1s (verified before push)

The following are the exact git-blob digests calculated from the local test sources, excluding this audit (to avoid a recursive hash); every remote write must match these digests before claiming integrity.

| Path | Git blob SHA-1 | Bytes |
|---|---|---:|
| `observational_succ/prime_active_weil_splines.py` | `82a67d94cac5fd9d6946bb69b585f62b3ca6b53b` | 22330 |
| `tests/test_prime_active_weil_splines.py` | `623dd6818fac19b82253f554546d312dbbe818f3` | 14365 |
| `scripts/prime_active_weil_spline_probe.py` | `2ccb796db9b724afe94687155165b408fa12e1e1` | 7393 |
| `research/2026-10-16/PRIME_ACTIVE_WEIL_SPLINE_SCHUR.md` | `45498958dc0c037a101a358625b1877a28f44259` | 25054 |
| `docs/CLAIM_SUPPLEMENT_PRIME_ACTIVE_WEIL_SPLINES.md` | `0d9b1b168b95575719f85819da856ae4f2caf9fd` | 3615 |
| `research/2026-10-16/PRIME_ACTIVE_WEIL_SPLINE_RECEIPT.json` | `429ac1b7973611ac23c4b60fbbe5ea3ab28139e6` | 4087 |
| `research/2026-10-16/PRIME_ACTIVE_WEIL_SPLINE_TEST_LOG.txt` | `bfbd4b0c7606da3b8f84319febf7c79b3e1ec33f` | 13668 |
