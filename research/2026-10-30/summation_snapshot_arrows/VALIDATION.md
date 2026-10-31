# Validation, failure checks, and exact file replay

**Parent:** SUCC draft #422 at exact head e8a4978207871a47466cdbb6f15cc86fae784164. All changes are additive in this directory, and previous PR #422 and main are not modified.

## Focused exact standard-library regression

Run from repo root:

~~~sh
python research/2026-10-30/summation_snapshot_arrows/summation_snapshot_probe.py
~~~

Locally executed against the **identical** file uploaded to GitHub: 10/10 unittest methods PASS, 0.005 seconds in the recorded run. Git blob identity of local source 9be5c5710e33b86cdc02fb9f3ff05f44ce836b4d matches the remote GitHub blob SHA.

Test families: completed Laurent Bernoulli coefficients, exact finite cutoff-vs-complete mismatch for N=1..100, exact product triangle partitions through N=12, Rota–Baxter weight/sign, finite Dirichlet product convolution through N=11, Borel counterexample, exact observer-kernel obstruction, finite geometric identity versus evaluation x=2, and sampled positive flat-control sanity. Tests do not prove all-order flatness or integral convergence, both given analytical proofs in README.

## Independent high-precision numerical controls (not proof)

mpmath at 50 decimal digits, distinct quadrature subintervals with Bernoulli local expansion for near-zero cancellation:

| Observation | Numeric result | Error against reference |
|---|---|---|
| integral (K − e^-t/t) dt | 0.5772156649015328606065120900824024310422 | -2.8345e-47 vs Euler gamma |
| integral tK dt | 1.644934066848226436472415166646025189219 | -2.6728e-51 vs π²/6 |
| integral h dt | 0.559463527266089709138395228142 | positive; global gamma-observer change |
| integral t h dt | 2.30980980016149175806774466981 | positive; global Basel-observer change |
| lambda − gamma and (1−gamma)−lambda² | 0.040818323848361987598074744283235687 | difference ~2e-51 |

The **two flat-control integrals** independently satisfy the standard modified-Bessel K formula:
integral h = 2(K_3(2)−2K_2(2)+K_1(2)); integral t h = 2(K_4(2)−2K_3(2)+K_2(2)). This is a cross-check of numerical values, not a substitute for the positivity proof.

## Negative/hostile receipts

- Borel transform fails to preserve ordinary multiplication at coefficient n=2 (3/2 versus 2).
- One-point/total-mass observer cannot recover weighted second moment (1 versus 1/4).
- Coefficient extraction does not commute with N->infinity: finite coefficient -N(N+1)/2 versus completed +1/12.
- Flat positive mutant retains the all-order asymptotic expansion and K(1), yet changes both global integrals.
- Same-source coherent seed -π/16 and PR #421 entire-source mutant remain **untested on a new proposed selected triangle**, so selected Weyl saving remains OPEN.

## Verification limits

Not run: SUCC's full native ~10k regression suite, required root AGENTS.md commands, hosted CI, Lean, or blind external review. Numerical quadrature is not interval-certified. The full finite exact code identity was hash-checked; independent algorithms are same-system authored, not blind independent witnesses. See README and CLAIMS.md for proof authority and unverified steps.
