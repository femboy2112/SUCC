# VALIDATION — causal-response rotation and phase retrieval

**Source / branch:** Based on exact SUCC draft #463 head 43adc90badfc6b8abc1631a4332c09cda007ccb7, stacked on #462/#460/#459 over Main XIX. All modifications are additive research files and one new root test wrapper; original four signed BBP poles, U0=0, historical contracts, core source, Lean and workflows untouched.

## 1. Focused exact rational finite tests

Run:
~~~sh
python research/2026-11-02/causal_response_rotation/causal_rotation_probe.py
python -m unittest discover -s tests -p 'test_causal_response_rotation.py'
~~~

The standalone exact local script was executed after its final edits:
~~~text
Ran 11 tests in 0.063s
OK
~~~

The 11 test methods check finite regression identities **by exact integer/Fraction arithmetic**, with no floating trigonometry or pi digit inputs:

- uniqueness of all nonzero causal b-power differences for b in {2,3,5,16}, multiple horizons;
- complete original four-pole and coherent zero-seeded changed-source exact Fourier-intensity phase coefficients for h in {1,3,7} and N<=8;
- exact gauge translation of every Fourier coefficient under a changed rational seed;
- exact intensity fourth moment and L2 Haar-defect identity;
- base-b first equal-length carry resonance at q=b+1, no collisions for q<=b on 3 selected causal modes (the prior #404 result is credited);
- exact original and changed forcing 34th-moment resonance \(16U_n+U_{n+2}-17U_{n+1}=\Delta r\), including arbitrary seed shifts;
- exact source cocycle / phase-power versus causal dilation alignment;
- exact exponential latest-phase Fourier-band cutoff for b=2,3,16;
- **new** rational Lagrange causal-differential projectors: modes b^n, moments of arbitrary rational coefficients, exact recovery of each coefficient from N+1 causal derivatives for N<=7 across b=2,3,16;
- rational solenoid branch history/q-commutation and exact full retarded causal Green matrix inversion/source response for b=2,3,16.

The remote uploaded final exact source Git blob was fetched and **matches the actually executed local git hash**:
causal_rotation_probe.py = 0f4c25a2e7db18346fbfbf7aa6352f875d5e6c44.

These finite checks calibrate a proof; they do not establish infinite weak-Haar convergence, which is proved by the analytic Fourier/Stone-Weierstrass derivation in PROOFS.md.

**Added exact structural controls after the original nine methods:** test 10 checks compatible solenoid towers, inverse branch loss and Fourier-character q-commutation at bases 2,3,16. Test 11 checks the full original and changed-source lower-triangular causal effect Jacobian, two-sided inverse, unit source impulse and source difference for N through 24. Final local run is **11/11 PASS** (0.063 s) with exact hash 0f4c25a2e7db18346fbfbf7aa6352f875d5e6c44. Historical 9/10-test receipts remain documented as development stages, not latest validation.

## 2. Independent numerical direct-seed quadrature

A separate implementation does **not** use the difference-pair expansion to calculate the intensity Fourier coefficients. It directly samples the seed circle, evaluates the complex superposition and nonnegative intensity, and integrates via a Nyquist-sufficient equally spaced grid. The original orbit is built from literal four signed rational terms; the coherent shadow from its separately declared source truncation.

Run:
~~~sh
python research/2026-11-02/causal_response_rotation/causal_direct_oracle.py
~~~

Executed result:
~~~text
Ran 1 test in 0.226s
OK
~~~

For both sources, N=2,3, h=1,2, every sampled Haar normalization was within 1e-10 of one and every reconstructed anchored coefficient within 3e-10 of its independently constructed complex phase. The numerical grid was larger than twice the largest causal frequency. This is **double-precision diagnostic evidence only**, not a certified interval or mathematically independent blind review.

The remote uploaded numeric source Git blob was fetched and **matches** the executed local hash:
causal_direct_oracle.py = 688a0c9135146da7bf802166f73face8c315ed80.

**Source-matched normal vs coherent control is an analytic paper theorem (CR-04B), not a finite computation.** It imports the classical existence of a known base-16 normal number (Champernowne) or Borel almost-everywhere normality, the inherited summable real BBP Green tail, and the exact seed translation identity. It proves no normality of π itself, and its source-matched counterseed is an irrational real initial state distinct from the literal rational U0=0 register.

## 3. Proof scope and inherited 34th moment

- CR-01 through CR-06B: full finite proof and infinite weak-limit arguments in PROOFS.md.
- CR-07: SUCC #404 ALREADY proves first 17-factor/34th balanced moment, phase-blindness at lower orders and seed-Haar blindness. This dossier only verifies a representative local source resonance and connects it to the causal-frequency support and anchor.
- CR-08: the shrinking seed aperture principle was inherited from #404; the intensity-norm formulation is a gate-equivalent alternate observation and not a cancellation bound.
- Neither weak Haar nor bounded coefficients at fixed causal frequencies shows the selected real Weyl condition. The same-source coherent seed and changed positive shadow provide explicit failures of that implication.

## 4. Whole-repository and independent authority boundary

The exact 9-method research script and separate 1-method direct quadrature oracle have been run locally. The new root-discoverable test wrapper is committed; **the complete native SUCC 11k+ regression suite, all AGENTS.md provenance/foundation/ordinal commands, hosted latest-head CI, new Lean formalization and external blind referee have not been executed here**. Never claim they passed merely because scripts were uploaded. Check exact hosted PR head status separately.

All mathematical results relying on the standard uniqueness of Fourier characters and circle covering are paper derivations, not new scholarly-priority claims. Pi normality and RH remain OPEN.
