# Zero-seed radix microscope · signed BBP Haar packet

Additive research child of **SUCC PR #591** (Main XXIII ancestor); does not
modify any source or compiler module. Implements the *zero-child seed localization*
missing from previous finite lambda/Haar and adjacent-time overlap approaches.

**All-N mathematical result:** For authentic BBP source with `U0=0`,
`alpha=pi/16`, the first zero-child Fourier-energy detail at **real-circle
frequency h=8** satisfies

`J_(N,0)(8) > 16/(225*pi*N^2) > 0` for **every N>=2**.

The theorem has an exact rational sign certificate using Machin's pi interval,
and an independent finite formula/calibration. It is neither **hexadecimal
digit parity** nor **pi base-16 normality**. It detects a small signed
source-selected packet that vanishes for the coherent same-forcing wrong seed,
but because its size is `O(N^-2)` it cannot close the statistical gate.

## Stronger structural result

For Fourier means `W_(N,h)(s)=N^-1 sum_(n<N) e(h*16^n*(alpha+s))`, let
`E_(N,K)(h)` be their squared modulus averaged over the literal zero-seed
cylinder `[0,16^-K]`. Then:

- `E_(N,0)=1/N` **exactly**, independently of pi (annealed orthogonality).
- `sqrt(E_(N,K)) <= (K+sqrt(N-K))/N` for `0<=K<=N`, universally.
- `|E_(N,K)-1/N| <= [K(K-1)+512K/(675|h|)]/N^2`, universally.
- `|E_(N,K)-|W_(N,h)(0)|^2| <= 2[2(N-K)/N+7|h|/(15N)]`, for `K<=N`.
- The sixteen children give an exact source-anchored signed tower
  `E_(N,N)=1/N+sum_(K<N) J_(N,K)`. At depth `K=N-o(N)` energy decay is
  equivalent to the authentic original-zero Weyl cancellation.

This is a **precise observation-resolution gap**: at coarse shrinking
cylinders `K=o(N)`, spatial cancellation holds for *every* source, even
maximally nonnormal ones. At near-point cylinders `K=N-o(N)` it becomes
the unsolved arithmetic assertion about pi. Actual source-selected work
must connect those scales rather than incorrectly beta-reduce away the
missing signed mass.

## Local replay

```sh
python -m unittest discover -s tests -p test_seed_microscope.py -v
python research/2026-11-10/zero_seed_microscope/probe.py
```

The test script uses standard-library `Fraction` and the repo's canonical
`observational_succ.duck_bbp` at runtime. Its direct integral and trig
checks are numerical diagnostics; the exact sign proof rests separately
on rational Machin bounds and geometric majorants.

[Theorems and provenance](MICROSCOPE_THEOREMS.md) ·
[Validation](VALIDATION.md) ·
[Next proof gate](NEXT.md) ·
[Reproducible receipt](receipts/seed_microscope_receipt.json)

**OPEN:** pi base-16 normality, original-zero hexadecimal digit parity,
source-selected cumulative deep-packet decay, the independently bounded
statistical Haar contraction in issue #590, and RH.

## Addendum: fixed-depth signed asymptotic fingerprint tower

For every fixed seed microscope depth K and every integer Fourier frequency
h≠0, the first K early–late rows of the exact signed pair kernel converge
absolutely to a coefficient A_(K,h)(alpha), with a certified geometric
truncation error. The scalar energy satisfies
`E_(N,K,h)=1/N+A_(K,h)(alpha)/N²+O_(K,h)(16^(K-N)/N²)`.
The true h=8 zero-seed sign implies `A_(1,8)(pi/16)>0`; the coherent
completed-zero counterseed has `A_(1,8)(0)=0`. This is a useful
source-selected *fixed-depth* fingerprint, but it cannot control the
deep window K=N-o(N) relevant to π normality. See MS-04b in
`MICROSCOPE_THEOREMS.md`.
