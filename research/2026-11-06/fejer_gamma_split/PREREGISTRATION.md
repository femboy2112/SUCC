# PREREGISTRATION — split-harmonic/Gamma amplitudes and dyadic return-fiber energy

Date: 2026-11-06. Parent: PR #534 at exact head `ff99fa2861b370d1aac0a76f01e2d8505c5a8740`. Research only; π normality remains OPEN.

## Fixed mathematical rivals, prior to running experiments

- **A (exact normalization only):** write `1/Q=(sum_{j>=0} a_j(Q))*(sum_{ell>=0} a_ell(Q))` with `a_j(Q)=(Q+j)^(-1/2)-(Q+j+1)^(-1/2)`. Each positive absolutely convergent Gamma half-density series sums to `Q^(-1/2)`. Write `1/M=sum_{r>=0} b_r(M)` with `b_r(M)=1/(M+r)-1/(M+r+1)`. Moving these three series inside the two time amplitudes changes no values; must NOT assert a signed saving.
- **B (actual coherent decomposition):** inserting a shared residue delta before independently summing the two amplitudes gives an exact finite Fourier-gluing kernel, with Parseval `R=sum_{u mod Q}|N^(-1)sum_{n<N} z_n exp(-2πiun/Q)|²`. The u=0 term is exactly `|W_N|²`, nonzero modes are nonnegative excess.
- **C (dyadic martingale):** for `Q=2^k`, the source return-energy equals global squared mean plus positive Haar-bit martingale increments. Also `1=|W|²+between-fiber variance+within-fiber dispersion` for |z|=1.
- **D (time-lag Fejer triangle):** expanding independent `M` sums and summing over residue classes yields `R=1/M+(2/M²)sum_{d=1}^{M-1}(M-d)Re C_d`; for completed z_n=e(h 16^n π/16), `C_d` is a selected Weyl sum of high frequency `h(16^(dQ)-1)`. This does not prove its own cancellation.
- **E (Abel infinite time):** for each fixed residue fiber define `F_a(s)=sum_{t>=0}s^t z_{a+tQ}`, |s|<1; exact coefficient `[s^(M-1)] F_a(s)/(1-s)/M` recovers finite time mean. A geometrically weighted Abel mean is a different observable unless a limit argument is separately proved.

## Hostile controls and preregistered finite cases

Exact combinatorial Gaussian-rational phases (not numeric π phases) test algebra identities for Q=2,4,8, M=1,2,3,5, including coherent z_n=1, period-Q phase z_n=exp(2πi n/Q), and an alternating phase z_n=(-1)^n. The last two have W=0 but can have R=1, falsifying unglued product and demonstrating R is stronger than W.

Original authentic four-pole BBP U0=0 selected cases, before measuring: `(Q,M,h)=(4,5,1),(8,6,1),(16,5,2)`. Compute from exact Fraction states and compare independent finite formulas at 1e-10 absolute tolerance. Changed-source control `H(n)=n/(2n-1)^4`, zero seed with real fractions→0. Coherent completed-periodic `β=1/5` control has unit full real character for h not divisible by5.

No fitting of parameters to observed values, no inference of asymptotic decay from finite results. Preserve any failed tests and exact-source mismatches. Claims initially unverified until local execution, then label finite checks observed only. The completed-phase `β=π/16` must be approximated using source tail bound rather than importing floating-point pi digits. Do not modify main or any inherited source/formal file.
