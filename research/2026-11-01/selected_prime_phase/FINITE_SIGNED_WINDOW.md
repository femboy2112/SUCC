# SPP-10 — exact finite cancellation from the original signed cofactor (no asymptotic claim)

**Follow-up to PR #459 on the same draft branch.** This is a sound rational-interval **FINITE** statement about the exact genuine zero-seeded SUCC states, not a Weyl normality theorem.

At the source-authenticated prime `p=257`, the one-source pole `8n-7` first equals p at `n=33`; p persists through n=128, before first reuse at n=129. The entire time window `W={33,...,128}` has 96 states. The isolated primary phase is of period four: its normalized mean is

\[
 P_{257}=\frac12\big(\cos(8\pi/257)+\cos(128\pi/257)\big)>49/100.
\]

**New exact signed interference theorem (SPP-10).** For the *complete original four-pole* zero-seeded states `U_n` and every indicated integer harmonic h,

\[
 \boxed{\left|\frac1{96}\sum_{n=33}^{128}e(hU_n)\right|
  <\begin{cases}1/16,&h=1,\\1/8,&h=3,5.\end{cases}} \tag{S10}
\]

This is the contribution of the joint p-clock *and the actual p-free cofactor* — a source-specific finite observed cancellation, not just a Galois average. For h=1, it differs substantially from the isolated primary-only mean >49/100. It does not establish any uniform-in-N or any fixed-h long-run bound; the higher-harmonic controls preserve the source and initial boundary.

## How the rational interval certificate is constructed

1. Independently obtain each `U_n` from the raw four poles and from the combined rational source-convolution formula. Check exact identity at every n in the window.
2. Enclose π with Machin's classical identity `π=16 atan(1/5)-4 atan(1/239)`, computing positive arctangent alternating-series lower/upper rational bounds (15 terms each). No decimal digits of π, external approximations, or floating points enter the certificate.
3. At each state reduce `hU_n mod1` exactly to `[-1/2,1/2]` and replace it by its **32-bit dyadic floor**. The exact circular-phase change is below `(44/7)*2^-32`, using `2π<44/7`.
4. Form a rational midpoint π from the verified enclosure. Calculate the Taylor cosine through degree 24 and sine through degree 25 using exact `Fraction` arithmetic. Lagrange remainders are bounded by `(22/7)^25/25!` and `(22/7)^26/26!` respectively, since the argument has absolute value less than `22/7`; all sine and cosine derivatives are bounded by 1. Account separately for the Machin π-interval width and dyadic phase-floor error.
5. Sum all 96 real/imaginary rational intervals. Outward-round endpoints and the `L1` upper bound to a denominator of `10^9`. The certificate compares the *exact pre-rounded* `L1` bound with `1/16` or `1/8`, then checks the rounded upper still lies strictly below that threshold. Since `|z|<=|Re z|+|Im z|`, this rigorously bounds the complex signed mean.

The committed `FINITE_SIGNED_INTERVAL_RECEIPT.json` contains rational component intervals and an **upper bound for each normalized signed amplitude**:

| h | Certified normalized `L1` upper | Strict threshold |
|---|---:|---:|
| 1 | `18832309/500000000` (about 0.0376646) | `1/16` |
| 3 | `82783653/1000000000` (about 0.0827837) | `1/8` |
| 5 | `47732713/500000000` (about 0.0954654) | `1/8` |

These are **stronger than the displayed complex moduli** and are outward-certified. The independent numeric diagnostic in `SIGNED_DIAGNOSTICS.json` uses floating trigonometric functions and is NOT authority for this theorem. The new interval implementation imports only the original exact pure-stdlib source and a differently constructed rational source oracle; the two source algorithms are not independent mathematical provenance families.

## How it changes the frontier

This is an **Observed finite signed saving with sound interval error**, sufficient to refute the assertion that the p=257 source cofactor cannot cancel a coherent primary clock in this finite window. It gives a new focused probe for source-derived three-channel/coprime-cofactor interference, and it directly survives the primary period-four failure control.

It does NOT prove the cofactor saving persists, that all large primes mix, that a source-selected signed Weyl sum is `o(N)`, or that π is normal. The general all-horizon joint cancellation of SPP-09 remains OPEN. Required next probe: an original-source inequality uniform in prime windows p_N≈N and N→∞, distinguishing the coherent changed seeds without Galois averaging.
