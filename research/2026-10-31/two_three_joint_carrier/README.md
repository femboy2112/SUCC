# SUCC: Original BBP 2-adic × 3-adic Joint Carrier (2026-10-31)

**Research status.** This is the next round after Main XVII and draft PR #426. It does **not** prove π normality, RH, or Furstenberg's ×2×3 conjecture. Its aim is to solve the original-source **local joint carrier** exactly and determine, with a rigorous no-go, what prevents its Haar law from automatically reaching the selected real-circle π orbit.

## What landed

- **TWTH-01/02 — authenticated joint local Haar:** The inherited original BBP isometry n↦U_n in Z₂ and the independent LTE clock n↦16^n in 1+3Z₃ combine via CRT. Every block of 2^a3^(b−1) consecutive times visits every pair (U_n mod2^a,16^n mod3^b) exactly once. This is a genuine exact *joint* Haar theorem on the completed local time product, not an independence model.
- **TWTH-03 — rigorous Archimedean obstruction:** Any continuous equivariant map from the product odometer Z₂×Z₃ under time-successor to the real circle under ×16 has a finite periodic image, with period dividing a product of powers of 2 and 3. It therefore cannot select π/16 or any irrational real trajectory. **The real/solenoid seam is mathematically load-bearing.**
- **TWTH-04/05 — source-selected tripling:** The integer 3 acts on hexadecimal real digits with a three-state carry; original BBP source plus the selected zero boundary certifies exact finite digits/carries. Continuous triangular observer tripling defects transport to the completed π orbit with L1 error < q/(4N).
- **TWTH-06 — solenoid duality erratum:** The inherited Atom 3 note incorrectly identifies the dual of R/NZ with Z/NZ; its actual dual is the infinite lattice (1/N)Z. The intended {2,3}-solenoid dual Z[1/6] is correct after repairing this step. Scalar 16 and 3 act nontrivially on both local fields, even where they are units.
- **TWTH-07 — prime-spectrum firewall:** Vinogradov's prime-multiple equidistribution holds for every irrational α without RH, including explicitly nonnormal α. This refutes equidistribution of prime multiples ⇒ normality of exponentially sampled powers.
- **TWTH-08 — corrected rigidity contract:** ×3-invariance of all selected real-circle weak limits plus appropriate positive entropy in **every jointly ergodic component** would imply π base-16 normality by Rudolph–Johnson. Neither source premise is established. Positive entropy of a nonergodic mixture alone is insufficient.

## Source and proof discipline

The exact source is the original signed four-pole BBP rational recurrence at U_0=0. 3-adic **time clock** 16^n is NOT confused with the generally nonintegral 3-adic BBP state U_n. Distinct mathematical layers are the finite CRT grid, profinite time odometer, connected real-adic solenoid, and actual Archimedean π-selected orbit. No equality of their measures is assumed.

Read [PROOF.md](PROOF.md), [SOLENOID_ERRATUM.md](SOLENOID_ERRATUM.md), [CLAIMS.md](CLAIMS.md), [VALIDATION.md](VALIDATION.md) and [NEXT.md](NEXT.md). Exact rational instruments: two_three_carrier.py; discoverable regression: tests/test_two_three_joint_carrier.py. The work adds only these files; no source, archived mathematical result, production module, main, formal kernel, workflow, tag, release, or publication is changed.

**Author's proposal retained as a research hypothesis:** RH may eventually constrain the selected additive π-phase through a source-faithful spectrum/curvature bridge. The present local theorem and no-go independently establish which parts do NOT require RH and where the unknown Archimedean selected correlation begins.