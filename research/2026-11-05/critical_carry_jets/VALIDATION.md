# Validation — critical source truncation, field-relative zero, second/third observer jets

**Pinned parent:** PR #520 head dad940dc69ae02f71119e8fbb908cca98e6e0846. Only new research and tests added on this child. No original source/Lean/production/workflow/main modifications.

## Executed focused tests: 31/31 PASS

A local standalone test replica with the same exact source files and relative source paths was executed:

\`python -m unittest discover -s . -p 'test_*.py' -v\`

**31 test methods passed, 0 errors/failures, 1.269 s.** Raw final log SHA-256: \`7e53abfbe80e41887c2b1c5991144d4b33106816af9fe5c9d717dbd26c8e6f3d\`. The locally executed test source Git blob SHA-1 hashes were checked independently by GitHub fetch and MATCH the exact committed files:

| Executed file (repo-relative) | Tests | Verified Git blob SHA-1 |
|---|---:|---|
| \`tests/test_critical_carry_jets.py\` | 10 | \`e7a32dfa7b85e754d7250e1988883178b1b6a8ab\` |
| \`tests/test_relative_zero_scale.py\` | 8 | \`9800d58680a4c7fd03517cc2f627d35f56837ad9\` |
| \`research/2026-11-05/critical_carry_jets/test_pair_carry_correlations.py\` | 5 | \`63a53fd5f8ab8572faed3598c787eeb2e76ca40c\` |
| \`tests/test_radial_clausen_jet.py\` | 3 | \`8685b9a3ff7d899cc268c4604056671cce6be543\` |
| \`tests/test_source_multipole_jets.py\` | 5 | \`c5fe7ca404c0a94b506717a36e62b83bdad6ae4f\` |

The separately executed exact rational source two-/three-time interval engine \`research/2026-11-05/critical_carry_jets/paired_carry_correlations.py\` also matches its committed Git blob SHA-1 \`98c8e004fa0171d53d9805b018e820b29ad376bb\`. Its independent truncated spectral covariance was compared numerically with the exact Fraction integral and convergence checked at spectral truncations 25,200,1000. The all-N covariance and variance bounds come from paper Fourier arguments, not numerical truncation.

The root test suite requires stdlib, mpmath and SymPy; these were available locally. The first draft of one MMD root-grid numerical test used an insufficient finite logarithmic tail tolerance and failed. It was repaired by using \`log1p\` and extending the independently convergent series; no mathematical formula was adjusted. The final 31 test methods all passed with exact committed source bytes. Nothing was rewritten in archived tests.

## Fresh exact original source critical correction holdouts

These A were preregistered BEFORE computing actual counts; all source U and R were **unwrapped Fraction** until final display:

| A | m | B/A² | selected corrections / A | mean R |
|---:|---:|---:|---:|---:|
| 139 | 3 | 0.211997 | 0 /139 | 0.001656956 |
| 139 | 4 | 3.391957 | 4 /139 | 0.026517185 |
| 139 | 5 | 54.271311 | 48 /139 | 0.424280778 |
| 277 | 4 | 0.854123 | 2 /277 | 0.006674997 |
| 277 | 5 | 13.665967 | 31 /277 | 0.106801442 |
| 557 | 4 | 0.211237 | 1 /557 | 0.001650540 |
| 557 | 5 | 3.379788 | 15 /557 | 0.026409019 |
| 557 | 6 | 54.076616 | 244 /557 | 0.422544681 |

All listed epoch orders satisfy 0<R_m(n)<1 across the epoch. For coherent same-original-forcing seed β=0, the source Green-tail theorem gives BT_n<1 and **exactly zero corrections** at the specified critical order combinations. The one-pole mutant switches the leading source decay exponent from2 to1; double-null primitive has order3. The original signed source moments M0=0,M1=15,M2=151,M3=1209 passed independently.

## Fresh exact-rational SECOND/THIRD moments of the seed ensemble

Source times n=13,29,61 and original m=2,3,3, respectively, were preregistered. A rational-endpoint partition of the single uniform seed circle computed all pair/triple centered moments EXACTLY. Third centered signs were −,+,+; the full exact fractions are recorded in the 5-method test file. No sampling of digits, no random Monte Carlo, and no hidden π oracle were involved. These are *ensemble* moments, not empirical chronological moments at s=0.

## Finite high-frequency / relative-zero and Clausen controls

- Uniform q-root controls with q=17,257 are indistinguishable from Haar to Fourier probes h<q, but full fixed-radius Q_r>0.
- A high-frequency cosine density has exponentially tiny Q_(1/2) yet exact carry-window bias 1/(2π).
- Fixed-radius kernel/radial-null first/second/third jet identities passed exact symbolic or high-precision numerical controls; finite original-source energy shift A=139,277, λ=−2,1,3 was inside the proven O(|λ|/A) bound. Kernel Hessian has both signs. These energy finite checks use double-precision output and are **not** sound interval certificates; the independent all-A analytic inequalities do not rely on them.
- A fresh first-pole weight mutant and a double-null primitive source verified changed critical exponent1 and3. The moment hierarchy is source authenticity, not source-selected mixing.

## Authority and integration

- All-N claims rely on explicit paper derivations in CRITICAL_CARRY.md, SOURCE_MULTIPOLE_JETS.md and RELATIVE_ZERO_JETS.md, with finite tests used as falsification/calibration.
- The source radix Fourier covariance result is original to this research context but not independently academically refereed, and no global novelty is asserted.
- **NOT RUN OR CLAIMED:** full native SUCC 11k–12k+ test suite at this research head, hosted exact-head complete green, any new Lean kernel theorem, original selected fixed-h Weyl decay, original source-selected Clifford/Pauli qubit physical dynamics, selected Clausen Q_(1/2)(µ_A)→0, or π normality.

Reproduction, after checking out this exact draft branch:

\`\`\`sh
python -m unittest discover -s tests -p 'test_critical_carry_jets.py' -v
python -m unittest discover -s tests -p 'test_relative_zero_scale.py' -v
python -m unittest discover -s tests -p 'test_radial_clausen_jet.py' -v
python -m unittest discover -s tests -p 'test_source_multipole_jets.py' -v
python research/2026-11-05/critical_carry_jets/test_pair_carry_correlations.py
python research/2026-11-05/critical_carry_jets/paired_carry_correlations.py
\`\`\`

Full repo integration/provenance should be run once at the stable merge gate, not per research exploration step.
