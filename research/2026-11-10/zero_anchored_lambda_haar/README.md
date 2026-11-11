# Zero-Anchored Lambda–Haar Compiler

**Date:** 2026-11-10. **Base:** Main XXIII integration candidate
`50481e49592af00d87c602f671a28f3503709de0`, PR #584.
**Outcome:** executable finite compiler and certified observation backend;
paper proofs, exact counterexamples, and reproduced finite signed observations.
**The source-selected statistical contraction and pi normality remain OPEN.**

The user's proposal is preserved in its strong form: retain a recoverable zero
through multiple legitimate reductions, expose any altered seed, and ask whether
the authenticated source forces statistical defects to contract. This round
implements the first two requirements and attacks the third. It does not make a
source certificate stand in for the missing statistical theorem.

## What is built

| Layer | Executable result | Exact boundary |
|---|---|---|
| Typed source language | Rational literals, typed lambdas/application, original source, origin, successor, recovered seed, addition and division by 16 | Finite simply typed calculus with explicit arithmetic delta rules; not a full untyped C-monoid |
| Compiler/reducer | Capture-free de Bruijn beta reduction; normal and applicative strategies; independently checked source/target correspondence | Budget exhaustion is UNRESOLVED; no infinite evaluator execution |
| Source authentication | Unwrapped state, clock, source identity and seed; forward, reverse and direct-prefix checks | Exact nonzero seeds fail original-zero acceptance; a hash alone proves nothing |
| Guarded tail | Finite backward unfoldings and rational bounds for the unique bounded tail fixed point | Observer-depth contraction, not sample-length contraction |
| Haar backend | Source-only common-horizon phase cells and rational interval Wasserstein defects | Every observation uses the completed real orbit and fixed interval chart |
| Pascal backend | Exact coefficients in Q(zeta_16), all nontrivial digit characters, Bernstein future probes and rigorous error | A signed character remains a statistic to estimate, not a zero inserted by rewrite |
| Signed cancellation | Exact adjacent-block CDF overlap identity | Its useful all-epoch lower bound remains unproved for BBP |

The implementation is in
[zero_anchored_lambda.py](../../../observational_succ/zero_anchored_lambda.py) and
[zero_anchored_haar.py](../../../observational_succ/zero_anchored_haar.py).
From this research directory, the repository root is three levels up.

## The requested contraction: what survived and what failed

Let `mu_N` be the law of the first N completed phases starting at clock zero,
`T(x)={16x}`, `C` the uniform inverse-branch operator, `Q=C T_*`, and
`D_N=W1(mu_N,Q mu_N)` in the ordinary interval metric. The target is

```math
D_N\le\theta D_{\lfloor N/2\rfloor}+\varepsilon_N,
\qquad 0\le\theta<1,\quad \varepsilon_N\to0.
```

1. **OPEN for the original zero BBP source.** Without an independently proved
   error bound, the existence of some vanishing epsilon is equivalent to
   normality. This corrects the earlier conversational framing that suggested
   the unspecified contraction target was already a weaker route.
2. **PROVED PAPER:** every actual length-N radix-16 orbit obeys
   `D_N >= 11/(64N)`. For theta below 1/2, any universal remainder must have
   `limsup N epsilon_N >= (11/64)(1-2theta)`.
3. **CLASSICAL IMPORT + DERIVED COROLLARY:** for theta below 1/2, an all-N
   `O(1/N)` remainder is impossible for any infinite orbit. The classical
   one-dimensional L1 discrepancy lower bound requires logarithmic spikes.
   An error such as `O(N^-1/2)` is compatible with this restriction but has
   not been proved for the authentic source.
4. **REFUTED:** the tempting extrapolation
   `D_(2M) <= D_M/16 + 1/(15M)` cannot hold for all sufficiently large M for
   any actual orbit. The finite probe independently falsifies it on every
   declared calibration and holdout length.

The genuinely useful exact identity is

```math
D_{2M}=\frac{D_M^-+D_M^+}{2}-\Omega_M,
```

where `Omega_M` integrates the opposite-sign overlap of the early and late
CDF defects. It identifies the missing signed estimate explicitly. A proposed
proof must control the late-block defect and establish enough overlap for the
actual source, while retaining carries, tails, seed, and endpoints.

## Finite original-source observations

The protocol was fixed in [HOLE_CONTRACT.md](HOLE_CONTRACT.md) and locally
committed as `41ad398` before the finite defect table was generated. This is
local preregistration; no earlier remote publication is claimed. The values
are a new replay for this instrument, not a claim that the digits were unseen
by earlier SUCC work. Clock zero includes the initial hexadecimal digit 3.

Each D below has a certified absolute approximation error at most
`2/16^10 = 1/549755813888` (about `1.82e-12`). Displayed decimals are rounded;
the complete receipt contains exact rational endpoints.

| Early block M | D_M | D_late | D_(2M) | Opposite-sign overlap |
|---:|---:|---:|---:|---:|
| 64 | 0.0674827926 | 0.0253339181 | 0.0430466566 | 0.0033616988 |
| 128 | 0.0430466566 | 0.0239428579 | 0.0146791325 | 0.0188156248 |
| 256 | 0.0146791325 | 0.0204424184 | 0.0144819819 | 0.0030787935 |
| 512 | 0.0144819819 | 0.0135207171 | 0.0132602087 | 0.0007411409 |
| 1024 | 0.0132602087 | 0.0139863060 | 0.0031109128 | 0.0105123446 |
| 2048 | 0.0031109128 | 0.0069696734 | 0.0040054666 | 0.0010348264 |
| 4096 | 0.0040054666 | 0.0036782139 | 0.0026653740 | 0.0011764663 |

In particular, the defect rises between N=2048 and N=4096. Normality does
not require monotone finite defects. Large cancellation on one pair of blocks
does not establish a uniform gain on the next pair.

## Source and seed controls

- The coherent mathematical seed `-pi/16` gives the constant-zero completed
  orbit with `D_N=15/32`. It is an irrational mathematical control, not a
  rational input accepted by the implementation.
- Rational nonzero seeds can produce arbitrarily long finite zero-tail
  shadows under the exact forcing. They pass finite reduction correctness
  and fail the exact original-zero gate. No asymptotic nonnormality claim is
  made for a fixed rational perturbation of pi.
- An explicit different four-pole source has the same positive quadratic
  leading coefficient, the same generic tail contraction and literal zero
  seed, yet has completed value `1/96` and limiting defect `35/128`.
- Another altered source agrees with any prescribed finite BBP prefix and
  every inverse-power asymptotic coefficient, yet completes to a rational
  number. It is not the original rational function. Finite black-box checks
  cannot establish global equality of an unspecified source.

## Replay

From the repository root (Python >=3.10, standard library for the new tools):

```sh
python -m unittest tests.test_zero_anchored_lambda tests.test_zero_anchored_haar -v
python scripts/zero_anchored_lambda_haar_probe.py --output /tmp/lambda-haar.json
python research/2026-11-10/zero_anchored_lambda_haar/adversarial_probe.py
```

The sample generator uses an exact integer enclosure of the original BBP
series. The bulk observations are an arithmetic acceleration with a proved
source identity; the receipt does not claim to have beta-reduced a term with
8,192 successors. The separate lambda replay executes 15 declared state/seed
cases and a finite guarded-tail program through both evaluation strategies.

## Proofs, claims and receipts

- [COMPILER.md](COMPILER.md): grammar, compilation, semantic preservation,
  three-path seed theorem and finite completion.
- [CONSTRUCTION.md](CONSTRUCTION.md): signed Poisson and overlap identities,
  authentic-source attempts, Pascal criterion, four-pole countermodel, and
  cited classical discrepancy restriction.
- [ADVERSARIAL.md](ADVERSARIAL.md): exact quantization floor, hidden
  equivalence, source aliases, seed shadows, and repaired compiler attack.
- [BACKEND_PROOFS.md](BACKEND_PROOFS.md): integer interval and finite backend
  soundness, with explicit coupling and error constants.
- [BACKEND_REVIEW.md](BACKEND_REVIEW.md): attacks that initially failed the
  backend and their replayed rejection after repair.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): earned truth states and remaining debt.
- [VALIDATION.md](VALIDATION.md): actual execution scope and retained failures.
- [FINITE_REPORT.json](receipts/FINITE_REPORT.json): full exact source,
  compiler, Pascal, signed-overlap, and contraction-residual receipt.

All new proofs here are paper proofs reviewed by same-model agents with
different assignments. No Lean formalization, external refereeing, or global
priority claim is made. Original-zero parity balance, pi normality and RH
remain OPEN.
