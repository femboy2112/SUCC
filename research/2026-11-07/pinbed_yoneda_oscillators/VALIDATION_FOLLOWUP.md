# Oscillator pin-bed follow-up: scope, evidence and falsification ledger

**2026-11-07, draft research.** Pinned original parent main d32342d375f44ddf62221ad6aff2f534abdc0a03. Existing PR #542 carries this additive continuation; sister PR #541 and golden PR #540 were inspected read-only. No merge, release or source-contract mutations.

## Actually executed locally (isolated Python 3.13.5 bundle)

- New pushed module source: observational_succ/pinbed_oscillator_bridge.py — exact Git object blob **5b8d4841119ac6a870fae7ff3ac75ab371afee13**.
- New pushed tests: tests/test_pinbed_oscillator_bridge.py — exact Git object blob **1b826c0fca820110e011c82649b2be0909ade849**.
- Both exact blobs checked using GitHub readback against independent local git hash-object. Byte identity checked **after** adding the eleven-test source-specific naturality, wrong-forcing mutation, lagged-holonomy, periodic-alias and explicit numerical error-budget controls.
- Isolated command: PYTHONPATH=. python -m unittest discover -s tests -p 'test_pinbed*.py' -q: **49 PASS / zero failures**. Composition: earlier standalone pin-bed suite 26 tests; second isolated continuous-frame supplement 12 tests; **eleven tests in the newly pushed on-repo suite**. The earlier 26+12 test files are local-bundle only and must not be claimed as checks run on exact GitHub PR head.
- python -m compileall -q observational_succ tests: **PASS** in this isolated worktree. There is no installed full SUCC checkout; package code is tested in isolation against the modules in this bundle, not the complete integrated repository.
- Old compact root package tests run separately: 26 PASS; new continuous window complement tests: 12 PASS; all 49 together 3.916s on local Python 3.13.5. No mpmath or non-stdlib runtime dependency in the new tests.

## Independent checks, with honest strength

1. Finite raw-frame inequality derived analytically from two shifted sine squares, independently cross-checked on all m=2..37, all proper L, all q using summed complex roots versus trigonometric geometric quotient. An exact *rational* uniform lower certificate 1/2 applies whenever 1/2≤L/m≤2/3; floating DFT checks are not interval certificates.
2. Two-tone continuum spectral bounds checked for harmonics in at least [-2000,2000], including finite global ×16 weight-ratio bound. Analytic derivations establish the all-h statement; numerics do not.
3. Direct pair-overlap energy numerically agreed with an independently accumulated Fourier series within a **proved absolute series-tail bound**; finite floating computations are not certified decimal intervals.
4. Exact original rational four-pole zero-seed source histories and hostile rational seeds verified: the BBP phase-plaquette defect is zero for all; a one-state mutation breaks it at two times, and using a wrong forcing shift in the reconstructed surface update produces a distinct output.
5. Exact Q(i) three-intensity polarization checked on 100 random rational pairs; missing reference phase has homometric/power-only aliases. The existence of an experimentally accessible coherent quadratic mixer was **not** tested or assumed.
6. Synthetic paired surfaces satisfy the rank-one syzygy, recovery and affine composition; a cross-channel mutant violates the syzygy. A separately constructed formally coherent but non-positive m_1=2, m_-1=2 countermodel violates the 2×2 Toeplitz probability minor. No finite Toeplitz census is a proof of the infinite Herglotz criterion.

## Source-specific finite diagnostics, explicitly NON-BLIND / NOT asymptotic

For the authentic rational source with literal U0=0, the golden two-channel pair energy was computed by ordinary floating-point cos/arc overlap. The source-to-completed-π difference column is an **analytically proved upper error bound**, not an observed difference or an upper bound for the energy.

| A | Observed finite E_a(mu_A^U) (float) | Proved upper bound on |E_a(mu_A^π)−E_a(mu_A^U)| |
|---:|---:|---:|
| 16 | 0.232734698201 | 0.004011061292 |
| 32 | 0.027729212782 | 0.001002765323 |
| 64 | 0.012456114404 | 0.000250691331 |
| 128 | 0.015385964692 | 0.000062672833 |

These values are not monotone and give no selected all-A rate. The wrong coherent completed-β=0 seed has limiting two-tone energy \(E_a(\delta_0)=2/a-1-\mathrm{sinc}^2(\pi a)>0\), despite having the **same forcing, perfect local phase plaquettes and the same source-error transport**. This is the decisive hostile control against a source-uniform proof.

## Provenance and unknowns

- Inherited source main: docs/PI_NORMALITY_FRONTIER.md, observational_succ/selected_orbit.py; source identity U_n+T_n=16^n(π/16) and tail T_n<1/[15(n+1)^2] are prior SUCC statements, not rediscovered here.
- Sibling #541: continuous B2 pin surface, its realization inverse and the single irrational-aperture one-step instability criterion. Our two-tone a∈(0,1) H^-1 metric repairs that instability by adding phase-coherent translated tests, **not** by changing source dynamics.
- Sibling #540: golden spatial Fejér energy/2-adic fiber triangle. Our new two-channel E is **different** and should not inherit its bounds without a derivation.
- Full root SUCC provenance verifier, >12k native tests, observer/ordinal probes, Lean kernel and exact-head CI were **not executed** in this environment; neither external physical measurement nor scholarly independent review exists. Branch is DRAFT only.
- Mathematical theorem and test evidence are not independent epistemic witnesses simply because both were produced by the same model. Every exact formula lists its own proof.

## Live next discriminator

To upgrade **π base-16 normality: OPEN**, one must prove for every fixed h≠0 the selected zero-seed signed \(A^{-1}\sum_{A≤n<2A}e^{2πihU_n}\to0\), or equivalently source-specific \(E_{a,2}(\mu_A^U)\to0\) at *all* sufficiently large A. Source-tail transfer, dynamic naturality, cross-channel syzygies, and full reconstruction do NOT imply this. Any proposed estimate must fail on the coherent wrong seed and source-matched nonnormal periodic completions. Carries, prime passports, arithmetic odd denominators and zero-seed selection must be actual hypotheses, not post hoc labels.
