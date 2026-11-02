# Exact scope, observed finite samples and verification checklist

**Source:** Main XIX 81045770234a114247e43eb08ae5c6d446e9514a; ancestor #461 exact bd5d2544bea8037df6d52fc3b64eb8fe7adf5979; #465 exact 70f4146d9bcb39e45026e88cc141ddad656f337d; #468 exact 7c7f26ea3ebb530744d695cf485b0e35d0997143; parent #470 exact b682b1f8ea21a1ae1efd529b6011e87453a7e0b6. Sibling #469 ef6f8894741cac8d952e9fd12d49e4aa7d13fa25 is READ-ONLY. The preexisting formulae and source are unchanged.

**Local work in the isolated execution container:** a standalone exact Fraction source/Golden test module and numerical Fejér probe were executed. All 10/10 focused unittest cases passed in 3.415 seconds. The tests cover four-pole rational equivalence and positivity; literal zero-seed finite stitching; positive Fejér polynomial identity; exact source rational Gamma-error bound function; shift/Ward inequality; constant-cap numerical inequality; coherent rational completed seed; Fibonacci two-sheet Bézout and Lucas mod8; a gamma-vs-inverse-golden sanity control; exploratory finite energy. This test is not the repository's >11k suite and not an independent theorem prover.

**Exploratory real-circle energy on the original α_B at B=N** (positive Fejér Fourier representation; double-precision complex trigonometry with exact Fraction modulo-one phases, NOT rigorous numerical enclosures):

| N | H=floor(sqrt N) | observed E(α_N) | rigorous bound on |E(π/16)−E(α_N)| |
|--:|--:|--:|--:|
| 32 | 5 | 1.292575117 | < 4.61e−6 |
| 64 | 8 | 1.242204894 | < 1.33e−6 |
| 128 | 11 | 1.071937976 | < 2.97e−7 |
| 256 | 16 | 1.048075484 | < 7.49e−8 |
| 512 | 22 | 1.031939332 | < 1.72e−8 |
| 768 | 27 | 1.031664646 | < 7.55e−9 |
| 1024 | 32 | 1.025627056 | < 4.43e−9 |

The last column is an EXACT, universal analytic upper bound evaluated approximately for display, not a certificate for the rounded energies. The N=768/1024 entries were later exploratory probes, not independent blinded holdouts. No limit, rate, all-horizon inequality, CI success, external referee, Lean, RH or π-normality is claimed.

**Known regression pitfalls:** floating conversion of huge rational numerator/denominator separately overflows after ~100 states; construct exact residue modulo denominator, THEN convert its Fraction to float. Wrong seed 1/5 is not the genuine U_0=0 and deliberately violates GF-GATE. The Gamma source kernel is balanced (γ terms cancel), while the silver regulator is source-native and the golden unit is only an observer. The finite Γ tail bound is source-authenticated; Fejér kernel positivity is universal, not selected cancellation.

**NOT RUN/CLAIMED for this GitHub branch:** native full SUCC suite, provenance verifier, observer-foundations, ordinal probe, Lean, hosted exact-head CI, external independent referee or global statistical bound. Public native GitHub clone failed DNS (unable to resolve github.com); repository changes made only via authorized connected GitHub writes. Run AGENTS.md commands on a full checkout before integration. Draft branch only: NO merge, tag, release, publication or proof-status promotion.
