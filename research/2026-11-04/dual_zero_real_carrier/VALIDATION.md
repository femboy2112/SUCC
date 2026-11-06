# Validation and precise authority scope

**Date:** 2026-11-04. Source branch pinned to parent PR #500 at `bf103c4a25bbd83b6cfbad1dd77895928300ddd9`. New research tree is an **isolated staging directory**, not a full SUCC checkout. Source reads were from live GitHub and the exact conversation-attached `SUCC_Prime_Character_Primal_2026-11-04.zip`. Original four signed Mellin terms and U0=0 retained byte-equivalent in the new independent script; no original files changed.

### Actually executed

- `python -m unittest discover -s tests -p 'test_zero_real_carrier.py' -v`: **30/30 PASS**. Includes independent integer-LCM state oracle up to n=61 for original and primal, exact cyclotomic character orthogonality in `Z[X]/Phi_M`, rank-one projector algebra, rational Pythagorean chart and split primes, all nine irreducible tangent polynomials, independent SymPy minimal polynomials for six small angles, genuine selected source arithmetic phi-degree reads, reciprocal doubling, projective forced ×16 map, irrational fixed-point polynomial, and anti-Haar controls.
- `python -m unittest discover -s tests -p 'test_prime_character_primal.py'`: **26/26 PASS** inherited restored research-package tests. Those are the prior shared-provenance implementation, not a blind independent referee or a proof of the 8N theorem.
- `python research/2026-11-04/dual_zero_real_carrier/probe.py --verify`: source exact finite receipt replay PASS.
- `python -m compileall` of new code and tests PASS.
- Independent symbolic `SymPy.minimal_polynomial` values agree with the source cyclotomic-rational polynomial for the declared small cases. This implements classical algebra via different functions, not independent scholarly verification.

### Hostile calibration and ordinary test repairs

Initial test drafts had **four input/assumption mistakes**, corrected before the final run: (1) polynomial at T=0 must be Phi_M(1), not Phi_M(0); (2) the test assumed the attached Python package used an `ANG` identifier whereas its public tap key is different, replaced by a source-independent explicit radial tap calculation; (3) a polynomial in Symbol('T') was inadvertently divided as a polynomial in Symbol('t'), corrected by a typed change of variable; (4) the Fourier test incorrectly classified h=M as a nonzero residue frequency, corrected to h%M==0. All are test expectation or variable mistakes; none was suppressed as a source theorem failure. Retain these as future regression notes.

### Not run or not proved

- **Full native SUCC** >11k suite, native provenance/observer/ordinal probes, exact-head hosted CI at final new commit: NOT YET RUN here. The parent #500 had all four hosted checks green on its own HEAD, NOT this child.
- New Lean kernel declarations, independent blinded reviewer, academic priority/novelty certification: NOT RUN.
- **π normality, RH, Dirichlet beta GRH, fixed-h Weyl and J=o(K): OPEN.** The source-specific integer-conductor rates 6N/8N inherit paper proofs from #497/#499/#500 rather than fresh formalization; exact finite tests do not re-prove those asymptotics.
- No physical quantum Feynman amplitude, speedup or actual lightning is identified by the finite Fourier sum.

### Source proof checks that matter

1. Actual state phase rational a/M is NOT the same as rational tangent t=a/M. In particular Y1=4/35 phase has tangent degree24; rational C(4/35)=(1209+280i)/1241 is a distinct circle point.
2. The reciprocal tangent involution adds a factor 2 to every odd-conductor phase denominator, so any proof suppressing source 2-primary gluing fails.
3. The radial **same-source** null channel has tangent degree growth exp(8N+o(N)) but real phase tends to zero, refuting degree/orthogonality⇒Haar.
4. Cauchy Haar reference is the scalar angular kernel's normalized measure, not its chronological empirical measure. Uniform rational unit interval grids do not give Haar unless weighted by the Jacobian.
5. The exact source Möbius tangent dynamics preserve the reference Cauchy measure but also admit the nonnormal algebraic periodic points tan(π/3), tan(π/5), tan(π/15).
