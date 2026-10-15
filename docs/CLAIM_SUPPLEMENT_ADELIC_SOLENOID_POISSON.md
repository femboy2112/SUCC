# Claim ledger — Adelic solenoid and complete Schwartz–Bruhat Poisson reconstruction (AS-01–AS-12)

**Project:** Observational SUCC, classical carrier-equivalence benchmark.  
**Research date:** 2026-10-15.  
**Branch:** \`research/pontryagin-finite-adelic-duality-2026-10-15\`, draft PR #129, stacked atop the edge-carrier benchmark (draft PR #127).  
**Paper:** [ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md](../research/2026-10-15/ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md).  
**Status:** known mathematical theorems independently derived from declared classical inputs; implementation exercises finitely described original-source charts. **RH PROVED: NO.**

| ID | Claim with typed domain, hypotheses, quantifiers | Status | Evidence / permitted inference |
| --- | --- | --- | --- |
| AS-01 | A_Q/Q is canonically isomorphic as a compact LCA group to (R×Zhat)/diag Z; covolume 1 if vol(Zhat)=1, real Haar=Lebesgue | CLASSICAL / PAPER PROVED | Use A_f=Q+Zhat, Q∩Zhat=Z, fundamental [0,1)×Zhat; rational source chart code is not a full real topology construction |
| AS-02 | Continuous dual of the compact solenoid is discrete Q; rational q character is exp(2πi(qt−pp(qz))) | CLASSICAL / PAPER PROVED | Pontryagin dual of R×Zhat is R×(Q/Z); diagonal Z annihilator forces λ+r∈Z; exact rational chart, gauge and Tate projection controls |
| AS-03 | Full additive A_Q is Pontryagin self-dual with ψ∞ plus and ψ_p minus; annihilator of diagonal Q equals diagonal Q | CLASSICAL / PAPER PROVED using LCA input | Restriction of Af characters to Zhat and quotient Q/Z; source prime projector and local p-adic nondegeneracy; not established from test counts |
| AS-04 | Every g∈S(A_f) is a FINITE linear combination of rational compact-open indicators 1_(u+D Zhat), u,D∈Q, D>0 | CLASSICAL / PAPER PROVED | Local constancy/compact support imply a uniform D Zhat period and finite coset support; Af=Q+D Zhat; source coset representative algorithm on given finitely named inputs |
| AS-05 | Fourier of 1_(u+D Zhat) equals (1/D) ψ_f(uy) 1_(D^-1 Zhat)(y), with correctly normalized Haar | CLASSICAL / PAPER PROVED + EXACT SOURCE CHECK | vol(D Zhat)=1/D; self-annihilating Zhat; independent finite-adele principal-part phase and dual-integer support tests; wrong Haar/shift/sign controls |
| AS-06 | For ALL f∈S(A_Q), adelic Poisson ∑_{q∈Q} f(q)=∑_{q∈Q} fhat(q) | CLASSICAL / PAPER PROVED conditional only on ordinary real Schwartz Poisson + standard LCA Fourier subgroup orthogonality | Finite tensor and rational coset span; reduces to real lattice u+D Z. Code tests generators, not infinite analytic sum |
| AS-07 | For shifted real Gaussian × rational compact-open coset, both adelic sums reduce to explicit shifted Gaussian/Jacobi identity with phase exp(2πi(a−u)m/D) | CLASSICAL / PAPER PROVED + EXACT FRACTION TERMS | Original source/double-index q=u+Dn, ξ=m/D; independent earlier Tate Gaussian test; wrong phase/normalization mutants |
| AS-08 | Outward rational finite Gaussian enclosures plus explicit positive tail bounds 4/[27 t²D⁴(N−|c|)³] and 4D³t^{3/2}/(27N³) for t a positive rational square | PROVED LOCAL EXACT + INDEPENDENT CLASSICAL ANALYTIC INEQUALITIES | Uses π>3, e^x≥x²/2, integral comparison, existing rigorously bounded pi/exp interval routines; overlap cannot prove infinite identity |
| AS-09 | Removing finite Haar factor 1/D from selected D=2 Gaussian dual is refuted by disjoint outward rational total-source intervals | PROVED LOCAL / EXACT COUNTERMODEL | \`wrong_haar_amplitude_witness\`, irrational π/e enclosed with Fractions, no floating sign inference |
| AS-10 | Arbitrary source-accessible physical SUCC histories functorially identify with all adèle Schwartz tests | UNVERIFIED PHYSICAL / CATEGORICAL GENERALIZATION | Mathematical source IDs and rational/profinite programs do not authenticate physical experiments or all real/profinite points |
| AS-11 | Completed true Λ(p^k), Gamma/poles, half-density and full signed Weil distribution are identified by this *new* source functor on ALL tests | OPEN NEW SUCC BRIDGE | Tate Poisson is necessary analytical input, not a direct source-derived identity with Weil; parent has tent tests, not all Schwartz test proof |
| AS-12 | Source-derived complete Weil quadratic is positive semidefinite on entire legitimate test class, proving RH | UNVERIFIED RH-HARD | Cannot deduce sign from Fourier/Parseval or a positive auxiliary Hilbert space; no nontrivial zeros used as construction inputs |

## Adversarial interpretation guards

1. A set-theoretic bijection of points does NOT prove LCA/topological carrier equivalence.
2. S(A_f) means compactly supported locally constant functions on the **restricted-product** finite adèles; it is NOT all bounded functions on ∏Qp. The finite coset span is exact because of local constancy, compactness and rational coset representatives.
3. The complete analytic Poisson theorem is a **finite mathematical proof using established real Poisson**, not a finite physical experiment producing infinitely many terms.
4. Every continuous rational solenoid character has a finite rational label; uncountably many solenoid points do NOT all have finite computable names.
5. The Fourier sign is **real plus / finite minus**. Wrong single-place sign fails diagonal Q-annihilation.
6. Missing finite Haar 1/D, wrong dual annihilator D^-1 Zhat, missing new prime coordinate, and incorrect shifted phases are failure controls.
7. A source index/epoch is a mathematical declaration, not an authenticated natural measurement.
8. Source-equivalent quotient states can erase actual SUCC event history; full history-faithful paths must retain event receipts separately.
9. True arithmetic Λ(p^k), half-density, Gamma, poles and signed Weil identification remain separate from additive Poisson.
10. Fixed finite Gaussian truncation and outward intervals can FALSIFY mutants but do not prove Poisson or positivity by agreement.

## New files and exact reproductions

- \`observational_succ/adelic_solenoid_duality.py\`
- \`observational_succ/adelic_poisson_reconstruction.py\`
- \`observational_succ/adelic_gaussian_interval.py\`
- \`tests/test_adelic_solenoid_duality.py\`
- \`tests/test_adelic_poisson_reconstruction.py\`
- \`tests/test_adelic_gaussian_interval.py\`

\`\`\`bash
python -m unittest discover -s tests -p 'test_adelic_solenoid_duality.py' -v
python -m unittest discover -s tests -p 'test_adelic_poisson_reconstruction.py' -v
python -m unittest discover -s tests -p 'test_adelic_gaussian_interval.py' -v
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
\`\`\`

Status of actual CI must be taken from the focused GitHub workflow run at the final commit. The older PD-01–PD-13 claims remain separately archived in \`CLAIM_SUPPLEMENT_PONTRYAGIN_ADELES.md\`.

## Literature and priority

Source: Tate (1950 thesis); Poonen (2015), *Tate's Thesis*, §5.5 Theorem 5.7; Jordan Bell, *The Pontryagin duals of Q/Z and Q and the adeles*; ordinary Poisson summation, Bruhat–Schwartz test-space theory, Pontryagin duality. Bibliography and proof details in the accompanying paper. **No original academic priority is asserted. No peer-review acceptance has occurred.**
