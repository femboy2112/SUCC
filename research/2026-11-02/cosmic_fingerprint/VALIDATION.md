# Exact regression, independent numerical replay and proof-authority firewall

**2026-11-02**, research-only; parent #464 at 0a69fe3d7260170248e2ef3bf1f1eb5de1b0c0f6, ancestor #463/#462/#460/#459/Main XIX. Source poles and original U0=0 unchanged.

## Executed in a local independent Python container

Exact stdlib-only Q(i) group-ring tests:
~~~sh
python research/2026-11-02/cosmic_fingerprint/cosmic_fingerprint_probe.py
~~~
**16/16 methods PASS**, Ran 16 tests in 0.343s on the final locally tested bytes. A separate checkout-shaped layout with a root wrapper identical to the committed tests/test_cosmic_fingerprint.py also ran unittest discover -s tests -p test_cosmic_fingerprint.py: **16/16 PASS**, Ran 16 tests in 0.358s. The latter is a simulated layout, NOT a full clone/checkout of the genuine SUCC repository.

The tests use EXACT Fractions and Gaussian rationals, with no floating trig, pi digits or stochastic assumptions. They check b-power difference uniqueness, universal auto-power, exact cross intensity vs temporal overlap, two positive phase-step field intensities recovering complex sum, calibrated/common seed shift, rank and separability of two channels, rank-one closure phase null and nontrivial rank2 exact example, lowpass observation barrier, exact L2 noise-budget examples, and the p257 strict source/shadow contrast. The inherited #459 true p257 bound is invoked as a certified premise, not independently recalculated by this script.

**Actually tested and uploaded remote Git blobs** (all re-fetched and checked):
- cosmic_fingerprint_probe.py = ae2a79cf2ae4b562be03efd2c74abc4252fd302d
- independent_sky_oracle.py = a7659fce3d2ac8b85538008e6985c706967f707c
- tests/test_cosmic_fingerprint.py = 4dfebee4c356c43a83f5870f2244d456d88225a6

## Separate direct-sky numerical source oracle

Run:
~~~sh
python research/2026-11-02/cosmic_fingerprint/independent_sky_oracle.py
~~~
Executed: INDEPENDENT_DIRECT_CAUSAL_SKY_FLOAT_ORACLE_PASS. It constructs the original source independently from the literal FOUR signed fractions, and the changed-source shadow from its exact finite rational tail. For N=3, b=16, it directly samples 32,768 seed-circle coordinates without evaluating group-ring/Fourier-pair formulas. The two nonnegative intensity normalizations agree with 1 within 1e-10, the centered cross-correlations and two phase-stepped global positive intensities agree with exact formulas within 1e-9.

For certified historical finite window p257, h1, n33..128, this independent FLOAT-ONLY oracle reports original normalized modulus about 0.0276076406382, coherent changed-source normalized modulus about 0.999999999807, and centered cross-reference contrasts -0.00965448484506 versus +0.989583332947. At h3 it reports about 0.0657073916 versus 0.9999999983 normalized moduli. These numbers are diagnostic and are NOT rigorous interval certificates; the strict true h1 upper is inherited from #459 and analytically converted to a contrast bound in CF-07. See NUMERIC_ORACLE.json for unrounded float outputs.

The paper proof of 0.989 source control uses only rational bounds, and the robustness theorem yields CF14: with a clean reference and an additive science-foreground residual ||eta||2<=1/512, true centered contrast <-7/1536 while coherent shadow >987/1000.

## Scope and missing runs

The analytic finite-M matched/phase-reference identities are proved exactly in PROOFS.md via character orthogonality and Sidon uniqueness; no experiment or astrophysical observation is their authority. Planck/SDSS/EHT references are instrumentation analogues only, not evidence of pi normality. The complete SUCC full native >11k suite, root AGENTS.md provenance/foundations/ordinal commands, hosted exact PR-head CI, new Lean proofs and blind independent referees have NOT been run or observed as passing in this local round. No selected asymptotic S_M(h)=o(M) estimate has been derived.
