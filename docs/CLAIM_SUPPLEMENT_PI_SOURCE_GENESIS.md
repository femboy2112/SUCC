# Pi Source Genesis claim supplement

Research branch `research/pi-source-genesis-2026-10-24`, based on repaired
PR #252 at `364962ac0c0e8fb4d06c37468a5d50336d68a9ee`.
**PI NORMALITY PROVED: NO.** Scholarly priority is unverified.

“Paper” below means a mathematical derivation with domains and quantifiers,
not an inference from Python tests. Kernel authority is separately itemized
in the [Lean report](../research/2026-10-24/PI_SOURCE_GENESIS_LEAN.md).
Prior statements and archived sources retain their original authority.

| ID | Claim and scope | Status | Evidence and countermodel boundary |
|---|---|---|---|
| PSG-01 | Actual BBP sum equals Real.pi; backward recurrence and selected circle orbit | CLASSICAL; previously Lean-certified and freshly rebuilt | Original PR #232 source; [source audit](../research/2026-10-24/PI_SOURCE_GENESIS_GREEN.md), G1. No equidistribution premise discharged. |
| PSG-02 | Hausdorff complete monotonicity, all-size strict Hankel positivity, infinite homogeneous linear rank, all-n beta bounds | Prior PR #252 paper results, independently rederived | Green G2–G3. Positive continuous rational counterfeit satisfies these structural properties and is nonnormal. |
| PSG-03 | Kernel endpoint coefficients are integer Pell products; signed all-order rational beta envelopes | PROVED LOCAL, PAPER; finite algebra independently checked | Green G4–G6. Fixed-order asymptotic theorem; not convergence in approximation order at fixed n. |
| PSG-04 | Every signed remainder is a strict Hausdorff moment sequence; corrected orbit has arbitrary fixed polynomial approximation order | PROVED LOCAL, PAPER | Green G6–G7. Uses actual kernel and authenticated BBP state; no cancellation follows. |
| PSG-05 | Signed two-time correlation error is uniform in horizon and lag, less than pi times abs(h)/30 | PROVED LOCAL, PAPER; rational constant certified | [Signed S2](../research/2026-10-24/PI_SOURCE_GENESIS_SIGNED.md). Source identity, decreasing summable tail, beta bound. All-K correction gives O(M^(-K-1)) offset error, Green G7. |
| PSG-06 | Horizon-matched rational approximant controls every lag to absolute O_h(N^-2), retaining full conductor and CRT signs | PROVED LOCAL, PAPER; exact finite arithmetic/interval receipts | Signed S3. Correct factor is 128 abs(h)/(15*16^K*(8M+1)*(8M+2)), M=N+K. This controls approximation, not either sum. |
| PSG-07 | Odd M BBP truncations have v2(q_M)=4(M-1) and exact base-16 preperiod M-1 | PROVED LOCAL, PAPER; exact checks | Signed S4. Complete-period averages do not estimate the required initial window; incomplete-sum methods remain open. |
| PSG-08 | Actual pi Fourier sums have an unbounded logarithmic deficit from the triangle bound | PROVED LOCAL consequence of EXTERNAL THEOREM | Signed S5 uses published mu(pi)<8. Existential constant, not numerically instantiated; not BBP-specific; normalized bound still tends to 1. |
| PSG-09 | Finite irrationality measure implies Fourier cancellation | REFUTED | Signed S6: alpha=sum 16^(-2^k), mu(alpha)<=3, but A_h,N(alpha)->1; full source and proof supplied. Not a BBP source. |
| PSG-10 | Any fixed finite tail jet plus positive infinite-rank memory and rational forcing implies normality | REFUTED | Green G8–G9 constructs matching positive rational moment sources with rational selected phase. These are rational coboundaries and do not satisfy exact BBP pole or boundary-value requirements. |
| PSG-11 | Lag observations authenticate the initial state | REFUTED | Same BBP forcing with y0 shifted by k/15 has identical lag correlations. Distinct source state; fixed translation preserves any Haar limit. Signed S2. |
| PSG-12 | Green resolvent covariance/spectrum/stability, orthogonal polynomial and Padé geometry | CLASSICAL operator/moment results specialized to BBP; PAPER | Green sections 4–5. Source spectrum and circle dynamics are different typed objects; exact moment-based evaluation of total mass is circular if mass is already an input. |
| PSG-13 | Finite certified signed pi correlations through N=64 | EXACT FINITE VERIFICATION | [Oracle receipt](../research/2026-10-24/PI_SOURCE_GENESIS_FINITE.json): exact BBP and independently reconstructed Machin sources, rational Taylor enclosures, prime-power phase data. No inference about infinite cancellation. |
| PSG-14 | All fixed nonzero pi modes have o(N) sums, hence base-16 normality | UNPROVED | No result here discharges the source-selected incomplete exponential-sum estimate. |
| PSG-15 | Positive infinite-rank rational forcing, arbitrary finite authentic tail jets AND a nonzero rational-coboundary invariant imply normality | REFUTED, PAPER with exact symbolic witnesses | [Explicit non-coboundary family](../research/2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md): V_m=F-(1-t)^(4m)/(4(1+(1-t)^2)), positive with rational mass, purely periodic selected orbit, invariant -1/4 at pole class3/4, and exact signed beta proximity. The extra pole class excludes the exact four-pole BBP contract. |

The next narrow arithmetic target is a sublinear estimate for one fixed
nonzero mode of the authentic rational two-time observable. This would be
new cancellation information; it alone would not prove normality. A complete
proof still needs all required modes, or a sufficient signed lag aggregate
with its growing-window quantifiers proved from the actual source.

The [execution report](../research/2026-10-24/PI_SOURCE_GENESIS_REPORT.md)
separates exact commits, local tests, hosted CI, paper proofs and kernel declarations.
