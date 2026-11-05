# Fresh source-selected Clausen zero-cylinder tests

**Research-only; numerical diagnostics, not proof of an infinite π claim.** Original four-pole BBP source states were iterated as exact Fractions with a separate collapsed rational forcing oracle. Conditional pair integrals were evaluated via the Clausen/dilogarithm primitive at 48-digit precision, and final decimals rounded for display.

The epochs A=7,11,13 and K=A,A+1,A+2,floor(3A/2),2A,2A+3 were selected in PREREGISTRATION.md BEFORE these tests. Earlier source epochs A=4,6 are DEVELOPMENT.

| A | K | conditional energy mean | cross-cut term | resolved past-past |
|---:|---:|---:|---:|---:|
| 7 | 7 | 0 | 0 | 0 |
| 7 | 8 | +0.005351431 | +0.005351431 | 0 |
| 7 | 9 | -0.079671569 | +0.004334011 | -0.084005580 |
| 7 | 10 | -0.412583386 | -0.000345132 | -0.412238254 |
| 7 | 14 | -0.259862731 | 0 | -0.259862731 |
| 7 | 17 | -0.247793769 | 0 | -0.247793769 |
| 11 | 11 | 0 | 0 | 0 |
| 11 | 12 | -0.000797000 | -0.000797000 | 0 |
| 11 | 13 | +0.010694968 | -0.000180797 | +0.010875766 |
| 11 | 16 | +0.052396438 | -0.000666490 | +0.053062928 |
| 11 | 22 | -0.138964163 | 0 | -0.138964163 |
| 11 | 25 | -0.117477227 | 0 | -0.117477227 |
| 13 | 13 | 0 | 0 | 0 |
| 13 | 14 | -0.000558169 | -0.000558169 | 0 |
| 13 | 15 | +0.007769332 | -0.000290495 | +0.008059827 |
| 13 | 19 | +0.014250402 | +0.000277415 | +0.013972986 |
| 13 | 26 | -0.061556219 | 0 | -0.061556219 |
| 13 | 29 | -0.033953579 | 0 | -0.033953579 |

**Falsifier:** Even the AUTHENTIC zero-seeded BBP conditional mean is not monotone in K or sign-definite. The near-perfect cross-cut cancellation does not control the realized earlier history.

## Preregistered unforced r=0 countermodel at the A^(2/3) scale

| A | t=K-A | actual conditional mean | sharp leading term | actual/leading |
|---:|---:|---:|---:|---:|
| 64 | 8 | -0.10242635228 | -0.11371945931 | 0.900693 |
| 125 | 20 | -0.45177971325 | -0.47200550407 | 0.957149 |
| 216 | 36 | -0.90095457424 | -0.92348312636 | 0.975605 |

Leading term is -(log16/3)t(t-1)(t+1)/A^2. It is proved analytically in THEOREMS.md, not inferred from these three values.

An independently implemented 10-method local unittest suite passed (1.328 s, no failures). The locally executed exact root-test Git blob `580e00468ca7792a23233f331818ca8cf5f92255` was confirmed by live GitHub fetch to equal the committed `tests/test_clausen_cut.py`. The initial 48-digit standalone local source probe had Git blob `17d5f7626dda0e7bf89c4d72e62b41ac426b9e47`; its byte layout/API differs from the committed reproducible `clausen_cut_probe.py`, so no exact-blob local replay of that committed probe is claimed.

No π digit oracle, physical Gaussian vacuum or claim of original Fekete lower bound was used.