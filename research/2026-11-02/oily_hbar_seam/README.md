# Operation OILY–ħ: from local finite Haar to selected real cofiber energy

**Draft mathematical research, 2026-11-02.** Exact parent [SUCC PR #469](https://github.com/femboy2112/SUCC/pull/469) at ef6f8894741cac8d952e9fd12d49e4aa7d13fa25, stacked over #467/#466/#464/#463/#462/#460/#459 and merged Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Gamma-seam #468 is read as a sibling, NOT silently merged. All additions are new research documents, probes and a discoverable root test. Original signed BBP source r(n), literal U0=0, historical proofs, Lean, production, provenance, CI and main are IMMUTABLE.

**Truth boundary: NO π NORMALITY PROOF.** The original source's conditional Fourier/cofiber energy bound at ALL horizons is still UNVERIFIED. We prove new exact resolution/no-go and source-selected anti-alias statements, and calibrate a more informative *finite* joint source/cofiber instrument.

## Original four-pole object and carrier

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad U_0=0,\ U_n=16U_{n-1}+r(n).
\]
SUCC's authenticated 2-adic isometry F(n)=U_n satisfies \(U_n\equiv U_m\pmod{16^r}\iff n\equiv m\pmod{16^r}\), with proof inherited from the October 24 DSI dossier. At level r, the dimensionless carrier Weyl phase mesh is \(\theta_r=2\pi/16^r\), **not physical ħ**.

## Newly proved scope (read full proofs)

1. **Height-only source decoder needs LINEAR precision.** For every n>=1 and 1<=r<=2n−1, two odd-denominator rationals admissible under the original source's certified denominator/numerator heights, \(x=1\) and \(y=(16^r+1)/(2\cdot16^r+1)\), have identical local mod16^r address but real circle distance ≥16/33. PNT sharpens its worst-case linear lower depth to \((8/\log16-o(1))n\), against a sufficient \((1+16/\log16+o(1))n\). This is about an observer allowed ONLY residue + certified heights; it does not prohibit direct evaluation of the known original r(n).
2. **Original-source selected moving-carrier REAL anti-alias theorem.** Given any fixed h!=0, for all sufficiently large M and **EVERY** carrier r with Q=16^r<=M, some n in [M,15M) obeys \(\|h(U_{n+Q}-U_n)\|\ge1/32\). Uniform M threshold independent of r. Proof uses the authentic zero boundary, Green tail and a CONSERVATIVE published μ(π)<7.5, not finite samples or a statistical model. As a consequence, the original selected multi-r lag energy is \(\Omega_h((\log N)^2)\), but by a universal inequality this only gives the already known \(\Omega_h(\log N)\) modulus deficit. Earlier 2026-10-26 OILY_DIRECT_ARITHMETIC.md already proved a stronger explicit \((\log_8N)/29-O_h(1)\) deficit; no false improvement claimed.
3. **New actual source-conditioned cofiber energy.** For Q=16^r dividing N, group authentic real phases \(z_n=e(hU_n)\) by their genuine source-local carrier/time class: \(A_a=\sum_{n<N,\ n\equiv a\,(Q)}z_n\). Define
\[
\boxed{G_{N,Q}(h)=\frac Q{N^2}\sum_{a=0}^{Q-1}|A_a|^2,\quad
|S_N(h)/N|^2\le G_{N,Q}(h)\le1.}
\]
An exact local Fourier Parseval formula shows that G is a **joint local residue × selected-real phase** observable, not separate source marginals. A rigorous all-horizon bound \(G\ll_h Q(\log N)^{A_h}/N\), across dense horizons and Q<=N^(1−eps), would prove π normality, but is **UNPROVED**.
4. **Gamma boundary transport remains controlled.** The authentic π completed phases \(\widehat z_n=e(h16^n\pi/16)\) satisfy \(|\sqrt G_U-\sqrt G_\pi|\le (2\pi|h|\sqrt Q/N)\sum_nT_n\); exact, not a G-saving.
5. **A sharp nonnormal adversary.** The base16 Thue–Morse–Mahler number has proven irrationality exponent exactly 2 (Bugeaud 2011) but digits only 0 and 1, so is nonnormal. Same **unchanged four-pole forcing** with a DIFFERENT real seed \(s=c_{TM}-\pi/16\) passes the moving-Q anti-alias argument. Thus Diophantine irrationality + moving carrier nonlocking cannot establish real Haar without the precise selected boundary.
6. **Oily–Macaroni is not a free π phase.** The defined \(\Omega=\varphi^{-1}-\gamma\) is a Gamma reference first-jet difference; common Euler–Mascheroni terms cancel in the original four-pole Gamma source (coefficients sum to zero). A constant phase offset preserves |S|, and a correction O(1/n) changes normalized S by O(logN/N). Any Oily-based proof must produce a new source-derived NONNEGLIGIBLE signed interaction, not a center adjustment.

## Frozen finite original-source holdout and its limits

**Predeclaration committed before evaluation:** N=768,1536,3072; h=9,11,17; Q=16,256, and strict \(G<2Q/N\) across all 18 cases. The source, r(1)… states, exact character phases, and rigorous error budget were frozen independently of finite test results.

**18/18 strict certified PASS** by actual exact Fraction original signed source, rigorous Machin interval, dyadic phase grid 2^19, degree18 rational sin/cos Taylor and outward error. Largest rigorous upper ratio G/(Q/N) = **1.258542912** at N3072,h9,Q16. Separate combined rational source and floating trig oracle reproduces all values under the rigorous upper bounds; float is NOT authority.

These finite results do not extrapolate to all N/h/Q, nor prove the conditional sufficient theorem. The 2^19 grid in the trig oracle is an *Archimedean numerical phase precision*, NOT the source 16-adic \(\hbar\) dimension.

## Reproduction

- [PROOFS.md](PROOFS.md) — quantifiers, moving-scale π approximation contradiction, height-only no-go, Thue–Morse hostile control, conditional Parseval and Gamma transfer.
- [CLAIMS.md](CLAIMS.md), [SOURCE_MAP.md](SOURCE_MAP.md), [NEXT.md](NEXT.md), [VALIDATION.md](VALIDATION.md) — claim grades, provenance, next verdict-changing probe, validation boundaries.
- [PREREGISTRATION.md](PREREGISTRATION.md), [CONDITIONAL_HOLDOUTS.json](CONDITIONAL_HOLDOUTS.json) — frozen test selection and strict exact finite certificates.
- [oily_hbar_probe.py](oily_hbar_probe.py) — 10 exact rational stdlib tests; [conditional_interval.py](conditional_interval.py) — full 18 rigorous source-selected interval replay; [independent_float_oracle.py](independent_float_oracle.py) — float-only second-source diagnostic; root [tests/test_oily_hbar_seam.py](../../../tests/test_oily_hbar_seam.py) — discoverable wrapper.

**This research establishes source-faithful anti-aliasing and an improved instrument, not infinite real-circle equidistribution. Keep DRAFT; no automatic merge, publication or proof status promotion.**