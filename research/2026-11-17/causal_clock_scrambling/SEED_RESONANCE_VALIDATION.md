# Seed Resonance — exact test, symbolic, numeric and hostile validation receipt

**Date:** 2026-11-17. Companion to [the theorem note](SEED_RESONANCE_AND_NULL_SUPPORT.md). No randomized simulation is offered as evidence that π has any statistical property. R0 and π base-16 normality remain OPEN.

## Executed exact finite tests

The assistant executed the local stdlib-only file /mnt/data/test_seed_resonance.py using Python unittest discovery. **17 tests were run, 17 passed, zero failures/errors.** The tested exact file was committed as [tests/test_seed_resonance.py](../../../tests/test_seed_resonance.py), and the independently computed Git blob SHA-1 matches GitHub's retrieved blob:

~~~text
5f8542991d53b71a2369e7982672f43d46e8216a
~~~

All rational source and finite-Fourier coefficients were checked as exact Python Fractions/integers. The tests cover: the literal four-pole affine recurrence; exactly invisible nonzero dyadic seeds on later shells; precise finite-shell alias kernel and a mutation just outside it; changing the completed target to rational locked/nonunit forms; null individual first moments and off-diagonal covariances under finite cyclic character averaging; the first nontrivial adjacent-clock relation of 17 raw phase factors; equivalence of all source clocks under changed seeds; seed-independent forcing cocycles; density of dyadic aliases and failure of endpoint continuity for the R0 predicate; locked/Haar-noise distinction; exact mean-square shell coefficient 1/B; and indistinguishable full future real states from either an initial seed or a delayed forcing impulse. The dual-number first-jet test checks the base/tangent *coefficient algebra*, not a physical nilpotent perturbation.

The finite mask group Z/(16^M) is not the continuous Haar circle. The corresponding Fourier orthogonality for continuous Haar is proved directly by integration in the note; the finite experiments calibrate only frequencies resolved before the finite mask wraps.

## Independent symbolic Gamma sensitivity check

A separate SymPy calculation used \(q(y)=(1-2\pi iy)^{-1}\) and \(c(y)=q(y)-q(y/16)^{16}\). It symbolically simplified both exact identities to zero:

\[
\partial_s q(x+s)|_{s=0}-2\pi i\,q(x)^2=0,
\]

\[
\partial_s c(x+s)|_{s=0}
-2\pi i\big(q(x)^2-q(x/16)^{17}\big)=0.
\]

That verifies the source-independent analytic susceptibility formula in the note, **not** a source-specific π Weyl estimate.

A separate 80-decimal-digit mpmath computation with genuine \(x=\pi/16\), seed shift \(s=16^{-3}\), and clocks n=3,4,6 found unchanged integer-time circle phases to working precision, but a fixed nonzero gain shift:
\[
|q(x+s)-q(x)|\approx0.0006077795151511013,
\quad
|c(x+s)-c(x)|\approx0.000957436037380119.
\]
The integer-time equality for these dyadic seeds is an exact theorem, not inferred from the numerical near-zero. The numeric gain differences diagnose the **additional Gamma real-lift instrument**, not digits of π.

## Crucibles and claim boundary

- **Source-canceling changed seed** \(s=-x\) makes the completed orbit identically phase 1, despite the same forcing. Its zero Gamma defect is not evidence for original zero-seed locking.
- **Nonzero dyadic initial seed** \(a/16^m\) becomes *exactly invisible to every later integer-time circle sample* while its real-lift Gamma coefficient changes.
- **Full Haar seed mask** hides source x even from the entire infinite observed orbit distribution. The surviving 17-factor moment identifies the base16 transition, not the original zero seed.
- **Causal-origin alias:** a one-time changed-forcing impulse at clock k has identical full future states to a specifically chosen original-forcing seeded path. Historical/source access, rather than higher-order future probes, is required to discriminate them.
- **Dense null aliases:** every individual finite shadow probe can be fooled; a nonconstant G-invariant R0 indicator is nowhere continuous. This is a topology no-go, not a proof that π is algorithmically undecidable.
- **Random seed average ≠ literal zero seed:** \(\mathbb E_S|W_B(x+S)|^2=1/B\) for Haar S and any x; no valid limit/exchange converts this into a bound at S=0.

**Not executed or claimed in this update:** the full root AGENTS.md unittest suite, provenance/observer/ordinal gates, a Lean kernel formalization, independent physical oscillator or thermal probe, full hosted CI success on the final head, the original-source all-late-shell norm floor, R0 or π normality. Prior commit 8627230a contained a complete locally audited full-suite replay, but adding new files starts a new head and does not inherit a hosted-CI pass automatically.

**Next decisive arithmetic experiment:** freeze a signed source-corrected, zero-seed-passported carry/cofactor comparison with an independently established all-late-shell inequality bounding terminal norm away from zero. Pre-register its wrong-seed, dyadic-erasure, post-k history-alias and sparse-irrational predictions. Any seed-blind correlation that survives the locked \(s=-x\) mutant is calibration, not a π proof.
