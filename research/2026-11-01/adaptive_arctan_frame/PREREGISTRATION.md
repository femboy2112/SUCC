# Prespecified fresh source holdouts and validation protocol

The prior arctan PR #451 tested finite horizons N=32,64,128,256 with harmonics 1,3,5,7. This independent round will use NEW pairs:

- Calibration: (N,h)=(4,1),(8,2),(12,3),(16,5),(20,1),(24,13).
- Fresh signed source holdouts: (N,h)=(40,13),(72,17),(96,29).
- Static alternate mirror choices: h=1,2,13,16,17,31,32,96,256,4096 (both harmonic indices, including 16-adic parity turns).
- Hostile negative: old fixed r(2) axis at h=13 has exact squared determinant <1/400; new axis h=13 has squared determinant >1/64.
- Finite original-source oracles: direct four-pole recurrence versus combined rational source; exact Fraction circle states; rational Machin bracket for π, alternating arctan bracket for source angles, outward Taylor intervals for signed means.

**Pass**: all source/code identities and rational enclosures hold with original zero seed. **Fail**: source inconsistency, polynomial coefficient mismatch, false positive transfer to original theorem from altered source, interval sign/error violation, or false full-repo CI claim. **Ambiguous**: finite numerical sign patterns; they cannot prove asymptotic cancellation. If high-horizon exact interval probes are impractical, report the unrun holdout rather than silently change the preregistered sample.
