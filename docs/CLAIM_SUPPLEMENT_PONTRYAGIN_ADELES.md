# Claim supplement — finite SUCC Pontryagin duality, Tate character transport and the finite adèles

**Date:** 2026-10-15. **Branch:** \`research/pontryagin-finite-adelic-duality-2026-10-15\`. **Parent exact commit:** \`research/edge-carrier-reconstruction-2026-10-15@7cc16f9a3a23b0a2f87bd7c9639cd5bd0757209b\` (draft PR #127). **Dossier:** [PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md](../research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md).

**Research distinction:** Mathematical carrier/group duality is established classical mathematics; original finite observation charts here are declared source models. Neither physical source attestation nor all-test Weil positivity is established. **RH PROVED: NO.**

| Claim | Precise statement and quantifier | Status | Evidence/negative controls |
| --- | --- | --- | --- |
| PD-01 | For every integer n≥1, every additive character of Z/nZ is \(\chi_{n,a}(x)=e^{2πiax/n}\), with unique a mod n | CLASSICAL / PROVED PAPER + EXACT FINITE ORACLE | Finite character algebra, independent exact cyclotomic orthogonality; no false prime place p=6 |
| PD-02 | For n|m, Pontryagin pullback maps label a mod n to a(m/n) mod m and commutes with the actual reduction arrow | CLASSICAL / PROVED PAPER + EXACT FINITE | Complete naturality squares; unchanged-label mutant n=3→m=6 is refuted |
| PD-03 | The **full continuous** Pontryagin dual of compact profinite Zhat is the **discrete** group Q/Z; every character factors through some finite Z/nZ | CLASSICAL / PAPER PROOF, FINITE SOURCE-CHART IMPLEMENTED | Compact-open proof via small-subgroup-free circle arc and kerπ_n neighborhoods; finite samples never presented as proof |
| PD-04 | The bidual of discrete Q/Z reconstructs Zhat through \(\eta(1/n)=e^{2πix_n/n}\) and compatible source residue laws | CLASSICAL / PAPER PROOF + EXACT FINITE | phase_separation, full projective compatibility and delayed-alias negative control |
| PD-05 | \(\operatorname{pp}(x)=\sum_p\{x_p\}_p\bmod Z\) yields short exact locally compact group sequence \(0\to Zhat\to A_f(Q)\to Q/Z\to0\) | CLASSICAL / PAPER PROOF + EXACT REPRESENTED FRAGMENTS | True p-primary decomposition, exact CRT kernel/surjectivity, independent rational additive reciprocity, integer/source mutants |
| PD-06 | The preceding exact sequence **does not split as additive groups**, though set-theoretic sections exist | PROVED PAPER (torsion vs torsion-free classical facts) / EXACT MODEL CONTROL | Af is Q-vector space torsion-free, Q/Z torsion; n(1/n)=1 nonzero witness not a universal machine proof |
| PD-07 | Under finite Tate sign \(\psi_p(y)=e^{-2πi\{y\}_p}\), \(\chi_r(z)=\psi_f(-rz)\), and \(Zhat^\perp=Zhat\subset A_f\) | CLASSICAL / PAPER PROOF + 3-WAY EXACT CROSS ORACLE | Original modular residue, finite adelic principal sum, independent Tate S-chart; true prime projector separates nonintegral source; wrong sign refuted |
| PD-08 | Finite coset Poisson formula for H=dZ/n and positive-phase DFT with **negative** inverse phase, all d|n | CLASSICAL / PROVED PAPER + EXACT CYCLOTOMIC TEST | Independent source table sum, SUCC exact cyclotomic DFT/IDFT, integer brute annihilator and wrong-coset-phase control |
| PD-09 | Tate global Poisson summation on full A_Q with Q self-annihilator and Tamagawa volume 1 | EXTERNAL CLASSICAL (Tate/Poonen), **NOT REPROVED BY OUR FINITE CODE** | Source-specific real Gaussian and p-adic test functions exist in parent; full analytic topology/Haar domains still require actual theorem |
| PD-10 | From finitely many source observations alone one can identify arbitrary Zhat global points or establish complete Tate/Weil positivity | REFUTED AS INFERENCE | LCM source alias, countability of finite descriptions, absent full topological/analytic witnesses |
| PD-11 | A source-derived positive Hilbert form matches the completed genuine Weil quadratic form on all admissible tests, thereby proving RH | UNVERIFIED RH-HARD | No identification/sign theorem; no nontrivial zeta zeros as construction inputs |
| PD-12 | The exact finite source implementation plus classical duality provides a complete universal model of real-world SUCC causal observations | UNVERIFIED PHYSICAL GENERALIZATION | Source IDs, epochs and local finite mathematical probes are declared; no instrument attestation or physical ω-completion |

**Proof and source boundaries:** See paper §§2–9 for proofs, external dependence, normalization, test domains, and edge morphism typing. The positive Q/Z character convention is NOT Tate's negative finite local convention; the explicit r→−r transport is mandatory. The finite cyclic group \(\mathbb Z/6\mathbb Z\) is legitimate; a made-up Euler place \(\mathbb Q_6\) is not.

**Reproduction (pending observed CI completion):**
\`\`\`bash
python -m unittest discover -s tests -p 'test_pontryagin_source_duality.py' -v
python -m unittest discover -s tests -p 'test_finite_adelic_character_bridge.py' -v
python -m unittest discover -s tests -p 'test_pontryagin_tate_atlas.py' -v
python -m unittest discover -s tests -p 'test_finite_cyclic_poisson.py' -v
python scripts/pontryagin_finite_adelic_probe.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
\`\`\`
This list does not claim the tests have run. Academic priority and independent peer review are **UNVERIFIED**.

**Primary sources:** Tate (1950; Cassels–Fröhlich 1967); Poonen (MIT Tate notes, 2015); Jordan Bell, *The Pontryagin duals of Q/Z and Q and the adeles*; Mathlib finite-abelian Pontryagin duality and general continuous-character definitions. Full URLs and statements in the paper's bibliography.
