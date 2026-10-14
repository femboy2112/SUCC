# SI — Source-indexed model interaction, all-place zeta and analytic gluing

**Parent:** SUCC `research/real-place-weil-identification-2026-10-14` at `55307fec354be0c671562233ca744907cf716ca5` (draft PR #71; transitively includes PR #69 prime-form heat). **RH PROVED: NO.** The full arguments, hypotheses and countermodels are in [`SOURCE_MODEL_ANALYTIC_GLUING.md`](../research/2026-10-14/SOURCE_MODEL_ANALYTIC_GLUING.md). The global adelic Poisson/Fourier and Gamma results are CLASSICAL IMPORTS, not produced by finite Python tests or newly discovered physical source laws.

| Claim ID | Statement and scope | Verdict |
|---|---|---|
| SI-01 | Diagonal `Q∩∏Z_p=Z`; rational product formula; local multiplicative Haar shell gives genuine `(1-p^-s)^-1`, Re(s)>0; one real Gaussian Gamma factor. | CLASSICAL; PROVED LOCAL finite source arithmetic |
| SI-02 | Standard adelic Schwartz–Bruhat tensor `(Gaussian,1_Zp)` and normalized self-dual Fourier/Haar give the full theta Poisson interaction. | CLASSICAL IMPORT; no direct proof assistant formalization |
| SI-03 | One source-compatible theta/Mellin overlap on Re(s)>1 yields unique entire `ξ(s)`, meromorphic ζ, and ξ reflection symmetry on C; never sums Euler primes in Re(s)≤1. | CLASSICAL ANALYTIC; exact derivation in dossier |
| SI-04 | Exact positive rational bound for theta integral and first two s-derivative *tails*, uniform for all imaginary ordinates in a declared real strip; ξ bounds require `|s|≤R`. | PROVED LOCAL analytic, exact Fraction implementation |
| SI-04b | Fully rational two-sided enclosure of the remaining finite integral for `ξ(1/2),ξ(-2),ξ(3)` by monotone Riemann sums, exact π/exp/root intervals and SI-04; explicit source-error bug rejected. | PROVED LOCAL; exact tests + independent numerical check |
| SI-05 | Every fixed finite prime set has normalized theta modular defect tending to `-1` along `t=4^-h`; all-prime limit has defect 0. Two directed limits fail to commute; finite rational depth threshold certificates. | PROVED LOCAL; sharp negative control |
| SI-06 | Globally certified elementary `ξ(s)>59/120` for all REAL `0≤s≤1`, hence real ζ(s)<0 on `(0,1)`; not a vertical strip theorem. | PROVED LOCAL via classical Poisson/positivity |
| SI-07 | `ζ(0)=-1/2`, residue at 1 is 1, all negative even zeros simple; `ζ'(-2m)=(-1)^m (2m)!/[2(2π)^(2m)]ζ(2m+1)`. | CLASSICAL / PROVED LOCAL source model derivation |
| SI-08 | Meromorphic prime current continues as `-ξ'/ξ+1/s+1/(s-1)+(digamma(s/2)-logπ)/2`; not convergent prime series outside Re(s)>1. | CLASSICAL ANALYTIC; denominator pole exclusions necessary |
| SI-09 | At symmetry point `2ζ'(1/2)/ζ(1/2)=γ+π/2+3log2+logπ`, exactly Suzuki's source contact constant, no zero coordinates. | CLASSICAL FUNCTIONAL EQUATION; new SUCC cross-branch link |
| SI-10 | Finite prime observers alias noninteger rational denominators outside their places; conductor mutation requires changed Fourier dual. | PROVED LOCAL countermodels, not physical observation |
| SI-11 | `ξ_fake=(1+10s(s-1))ξ` preserves reflection and endpoint constants but invents off-line real zeros and fails original Euler overlap at s=2. | REFUTES "functional equation suffices" |
| SI-12 | Entire ξ and analytic source continuation prove global Suzuki Weil positivity/RH. | **UNVERIFIED / no implication** |

**Validation:** 42 exact unittest methods passed on an isolated authored research overlay. Frozen exact receipt and independent 65-digit mpmath crosscheck also passed. The latter is **not** a rigorous quadrature certificate for arbitrary complex values; SI-04b is a rigorous finite-integral enclosure only for its supported real arguments. The complete parent checkout, full repository CI and Lean checker are separate gates. All files must be hashed against uploaded Git blobs before commit.

**Known limitations / upcoming trials:** fully certified complex finite-interval quadrature, explicit source-specific zero-count proof on a designated compact contour, and an independent completed-Weil signed-form comparison with valid domains, genuine Gamma/pole/conductor, fake composite and non-Euler controls. Neither contour observations nor analytic continuation alone prove RH. Academic priority of any new-to-SUCC packaging is unverified.
