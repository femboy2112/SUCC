# Preregistration — the selected Galois character sector (not a normality proof)

Date 2026-11-06. Research child of PR #532. The algebraic identities below were derived BEFORE any new finite Fourier table tests. These are not statistically discovered; finite oracles merely calibrate the proof.

Original four-pole U0=0 has reduced U_n=a_n/d_n with odd d_n and gcd(a_n,d_n)=1. For G_n=(Z/d_nZ)^× define F_(n,h)(u)=exp(2πi h a_n u/d_n). For every multiplicative character χ on G_n, define normalized \hat F(χ)=|G_n|^-1 Σ_(u∈G_n) F(u) conj χ(u).

Predeclared exact identity: F(1)=Σ_χ \hat F(χ). The trivial χ has mean c_(d_n)(h)/φ(d_n), and Σ_(χ≠1)|\hat F(χ)|²=1−|c_(d_n)(h)/φ(d_n)|². The already proved denominator lower bound ensures fixed-h trivial-sector means exponentially small at large n; consequently the actual real Weyl sum differs from the time-average of the complete *nontrivial* character channels by O_h(1/N). THIS IS A REPHRASING AND A PROOF-OBLIGATION LOCALIZER, NOT a bound on the remaining time-average.

Frozen finite controls prior to runs: original U_1=47/15 (gcd=1) and U_n for n=1..8; exact Ramanujan trivial character for h∈{1,2,3,4,5}; full character Fourier table for G_15≅C2×C4, with generators 11 (order 2) and 2 (order 4) and all eight characters. Also test prime fields p∈{7,11,17} using primitive roots and all φ(p) characters. Require individual reconstruction and Parseval error under 5×10^-12 for float calculation, exact integer Ramanujan evaluation via independent divisor/Mobius formula. Mutation controls: a non-coprime numerator is not primitive of order d (calibrate that the premise matters); nontrivial sector is not individually small for d=15; virtual uniform Haar alone does not imply time Haar. No asymptotic empirical inference.

PASS all proved algebraic identities with exact group-theoretic proof plus correct finite controls. OPEN original source-selected Fourier phase time cancellation / Poisson contraction / π normality / RH. No identification of mod-p Legendre characters with real e(hU_n) unless the explicit Dirichlet/Galois character Fourier basis is used.
