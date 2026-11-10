# Claim ledger: BBP Euler–Mascheroni × Gamma16

| ID | Status | Precise scope / quantifiers | Receipt / dependencies | What remains |
|---|---|---|---|---|
| BGEM-01 | DISCLOSED / paper | For all integer g,k>=1, exact regrouped source, positive Laplace Q_g and q-Gamma **integer ratio** | Original four fractions, #568 GM10–13, `test_block_grouping_two_levels`, exact source oracle | Not unique to BBP; no normality |
| BGEM-02 | DISCLOSED / paper | For each fixed integer g>=1, source clock harmonic-log finite part exists and equals log rational minus 2γ; declared normalization gives gamma_g^BBP | Full `PROOFS.md` BGEM2–3, rational tests | Constant depends on clock normalization |
| BGEM-03 | DISCLOSED / paper, CLASSICAL π input | C_g decreases to 4π, with strict rational-tail inequalities, and gamma_g^BBP increases to γ−(log4π)/2 | Exact BBP identity + source-tail inequalities + tests | Does not prove π digits normal |
| BGEM-04 | DISCLOSED / paper | For all fixed g and a>0, normalized positive Mellin first jet; O_g(a^-2) as a→∞ with coefficient 5/2−8g/(16^g−1) | Exact pole calculus, classical Γ derivative ψ(2)=1−γ, independent mpmath quadrature | Fixed-g asymptotic is NOT a growing-g estimate |
| BGEM-05 | DISCLOSED / exact finite arithmetic | At n=7, v3(r7)=−3; at n=8, v31(r8)=−1; at g=8, v3(C8)=−4, v31(C8)=−1 | Independent direct rational/valuation tests, prime-factor receipt | Prime support of **rational arguments**, not of γ or π |
| BGEM-06 | CLASSICAL identity / locally derived | Canonical q-Gamma normalization: γ_q formula and Lambert divisor expansion, all odd p in term denominator support | DLMF 5.18, mpmath qgamma derivative oracle, exact bounded rational series | Universal, not source-selected BBP |
| BGEM-07 | REFUTED stronger claim | “q-Gamma blocking alone determines a unique γ deformation / selects π-normality” | Periodic multiplier changes γ_q with same integer blocking ratios; two-pole source has same q blocker, wrong zero-completion seed has same source jets but nonnormal | A new signed original-zero phase estimate would change conclusion |
| BGEM-08 | OBSERVED FINITE | Numerics / exact finite g=1..16, source n=1..300, q series finite, elliptic/Gamma quadrature | 18 focused unit tests, separate quadrature and exact rational certificates | No blind holdout or universal arithmetic decay |
| BGEM-09 | UNVERIFIED | For the original zero seed, prove asymptotic signed #544 prime/complement phase or #565 future-conditioned digit symmetry decay | No completed probe; source jet/prime support not enough | Main π-normality barrier remains OPEN |

Provenance and dependence: #568 Γ16, #565 recursive Haar, main `duck_bbp`, #307 Oily positive source, classical BBP and DLMF Gamma / q-Gamma. Same source used for all derived formulas; distinct calculations are not independent discovery witnesses. No originality priority claim or physical energy conservation claim.
