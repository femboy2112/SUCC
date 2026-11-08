# Preregistration — cross-place source-selected obstruction and return-fiber probe

Date 2026-11-06. Strict additive child of `femboy2112/SUCC` PR #527, head `c550cd4089db0367464ff38884797e06359fbcbc`. This file is frozen on GitHub **before** performing the new fixed probes named below.

## Known/calibration observations, NOT blind holdouts

Earlier exploration before this preregistration inspected the original rational BBP phase denominators at n=1,2,4,8,16,32,64,128,256,512,1024; 2-adic same-residue real-return separation for shifts 2^k at k=0,...,8 using n near 50; and normalized-residue surrogate error at K=3,...,8. These observations motivate the analytical questions but do NOT validate a fitted law. The original #527 modular k=2048/4096 probes were also already done and are not fresh here.

## Theoretical predictions registered before new probes

* For original completed beta=pi/16 and EVERY k>=0, some arbitrarily large n have p-adic return V(n+2^k) congruent V(n) modulo 2^k, but real-circle completed phases at distance >=1/17 (by a separately supplied rigorous proof, not a finite fit). Raw rational orbit phases differ by >=1/17-2/[15(n+1)^2]. A full-period periodic-completion control need not satisfy this lower bound.
* Any uniformly continuous Z2-clock -> real-circle equivariant decoder must have finite periodic image, so it cannot interpolate an irrational real beta. Measurable equivariant Haar-preserving decoder is also impossible by the zero-entropy odometer factor argument. Neither assertion implies pi normality.
* Finite rational reconstruction from known odd denominator d and Z2 residue modulo 2^K is uniquely certified whenever 2^K >= d. This may require far greater K than a 2-adic clock census provides.
* A uniform residue phase surrogate e(v/2^K) is exactly mean-zero on a complete 2^K clock block, but is NOT expected to approximate the true real phase with small RMS error; the new finite probe tests rather than assumes this.

## Fresh held-out finite probes — NO tuning after observation

* For k=9,10,11, lag Q=2^k, examine exact original rational states x_n={U_n} for integers n in [128,191] inclusive, using the original four-pole r(n) and U0=0. Record the **first** n with circle distance d_T(x_(n+Q),x_n) >=1/4. If no witness exists in that finite window, mark the finite prediction FAILED (it does not refute the all-horizon theorem). Record the exact rational distance and modular congruence U_(n+Q) == U_n (mod 2^k); do NOT alter this window.
* For K=9 and 10, N=2^K, evaluate the **diagnostic floating-point** original-selected h=1 real Weyl magnitude, 2-adic normalized-residue surrogate zero Fourier mean (exact algebraic), real-to-surrogate RMS error and complex correlation. Record all results, favorable or not; do NOT treat floats as rigorous mathematical certificates.
* Newly inspect denominator bit lengths of exact original fractional U_n at n=73,149,293,587. They are finite diagnostics; no general exponential growth claim is preregistered.
* Negative controls: rational shadow H(n)=n/(2n-1)^4 (2-adic isometry, real phase tends to 0), coherent periodic completion beta=1/5 (outside original literal zero seed), and an irrational sparse-digit beta=sum_(j>=2)16^(-j!) (irrational, nonnormal). Distinguish each source/seed type, never pass a real irrational seed to a 2-adic rational source routine.

## Pass/fail scope

The all-horizon theorems require independent symbolic proofs; finite tests establish only the named original-source cases. A failed finite witness search is a reported observation, not a refutation of a theorem with unrestricted n. Explicit countermodels get `REFUTED` labels only for the universal inference they actually contradict. No expected equality between p-adic and real Haar is assumed. No real Weyl saving or pi normality may be claimed from these probes.

Repository conduct: preserve the exact four signed poles, U0=0, historical source/provenance/formal contracts, main and PR #527. Draft research PR only, no merge, tag or release.
