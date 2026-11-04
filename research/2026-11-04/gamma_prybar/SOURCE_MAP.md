# Sources, ancestry and authority

The research branch forks directly from main `a673ec95dfac4ef6a61c60222be8b615fd08535d` (tree `be61f8a82a1c96c6b741921c0e3ffa496371211f`). Only this dossier was added. The initial fetch contained 312 research/* branch refs. The 11 named PR metadata records and the PR-triggered workflow rows returned for their exact heads are in [GITHUB_SNAPSHOT.json](GITHUB_SNAPSHOT.json). All 11 were still open drafts at retrieval. Four returned successful PR workflow runs at each SHA; this describes the returned filter, not every possible push run. [MAIN_CI.json](MAIN_CI.json) records the separate, successful main push run 41766329949 and the differently named branch runs at the same SHA.

| PR | Exact inspected head | Target / relationship to main | Inspected material |
|---|---|---|---|
| [#485](https://github.com/femboy2112/SUCC/pull/485) | `cdb01d73839f08cb10b46f51d42afecf44469ee2` | `research/joint-carry-odd-cofiber-2026-11-03`, ancestor of main | Split/inert lag clocks and primary unit averaging |
| [#487](https://github.com/femboy2112/SUCC/pull/487) | `5f69d87d8bddde4f7136229289bc9ebde430c5f0` | `research/split-inert-gamma-lag-2026-11-03`, ancestor of main | Selected numerator and CRT ghosts |
| [#488](https://github.com/femboy2112/SUCC/pull/488) | `f47e3768631cd1628c1390d529811c911e0f6443` | `research/archimedean-numerator-oily-shear-2026-11-03`, ancestor of main | Exact branch current |
| [#489](https://github.com/femboy2112/SUCC/pull/489) | `c0f9c3bb89c8cb473aa2c7edbd24b5ed20acf71d` | `research/circle-path-electric-natural-extension-2026-11-03`, ancestor of main | Shift coupling and one-way energy criterion |
| [#491](https://github.com/femboy2112/SUCC/pull/491) | `e21ff757dd55caccf6ecd51a51eba654d81f8d06` | `main`, 2 commits outside main | Repaired signed frequency transport |
| [#492](https://github.com/femboy2112/SUCC/pull/492) | `a61a3968239ee40448fd3ed2eae0b5652c92b5d3` | `main`, 5 commits outside main | 16-pocket identity, source-native counterseed |
| [#495](https://github.com/femboy2112/SUCC/pull/495) | `b96befcb671644e374272a8465ac247ac0d3f527` | `research/operational-axioms-observer-source-2026-11-04`, 3 commits outside main | LCM lattice, zero seed, proof judgement |
| [#496](https://github.com/femboy2112/SUCC/pull/496) | `a0a2619578a88182c73420901c99994699eb2024` | `research/observer-bridge-busy-beaver-coherence-2026-11-04`, 5 commits outside main | Gamma(2) and Abel boundary |
| [#497](https://github.com/femboy2112/SUCC/pull/497) | `4383bd31340af700e312f13d7ef28af090c152d5` | `research/analytic-exile-frequency-ladder-2026-11-04`, 7 commits outside main | Prime pulses, dual state and radial sign |
| [#498](https://github.com/femboy2112/SUCC/pull/498) | `247030219931ef0722e973eb909960ee4ea7eeac` | `main`, 3 commits outside main | Corrected Gamma window and old-cofactor obstruction |
| [#499](https://github.com/femboy2112/SUCC/pull/499) | `4ff640637d18b8161599402f7c6ba23388a63652` | `research/bbp-frobenius-prime-saturation-2026-11-04`, 10 commits outside main | Angular quotient and denominator proof |

The #485 → #487 → #488 → #489 history is in main by ancestry although the individual PRs still show open. #491, #492 and #498 fork directly from main. #495 is based on #494, #496 on #493, and #497 → #499 is a stack above #496. Comparisons used full git objects, including the named PR refs. No merge or cherry-pick from a draft was performed.

## Original contracts

Checked AGENTS.md, docs/METHOD.md, docs/ROADMAP.md, docs/academic_main_vii/proof_authority_boundary.md, the claim-ledger policy and provenance/IMPORT_MANIFEST.json. The manifest lists 72 imported entries from upstream commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`. Each named donor matches the following main blobs.

| Path | Git blob |
|---|---|
| `provenance/IMPORT_MANIFEST.json` | `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae` |
| `observational_succ/integer_bbp_carrier.py` | `1c034fca97c3466393692b72a3f863e1d71230ed` |
| `observational_succ/bbp_natural_carrier.py` | `74174890efe630ddccff430a371fd9bf0874fd31` |

The normality reduction is in research/2026-11-03/selected_current_front/PROOFS.md. Main already contains CG-01/02 in research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md, including the sharp conductor for U_n and its adjacent difference. The sublinear-lag regime is present in the October 30 zero_boundary_dispersion/crt dossier. DPF-01 in the November 2 macrolag_prime_witness dossier proves eventual nonrepetition. These are inherited, as are the Gamma injection pins and first-order oriented shear. The new estimates have their own quantifiers in PROOFS.md. New paper proofs have no Lean receipt.

## PR #499 archive boundary

Relative to #497 its committed tree adds only PREREGISTRATION.md, PRIMAL_DENOMINATOR_PREREGISTRATION.md and PRIMAL_QUOTIENT_THEOREM.md under prime_character_primal. Compared the separate SUCC_Prime_Character_Primal_2026-11-04.zip, SHA-256 `007722d393df2825d90e5b327be8a28b30bf075fe6ecadf1664759b0efd4009a`. Its 26 focused archive tests ran in an isolated extraction. The three committed Markdown paths and additional files in the archive have separate provenance. The archive implementation and its tests did not enter this integration. [Archive test output](front5/archive_tests.txt).

## External mathematical inputs

- Bailey and Crandall, 2001, Theorems 3.1 and 1.1. The periodic-attractor/rationality statement is unconditional; their normality consequence requires Hypothesis A. Section 4 also gives a changed-seed attractor for the log 2 recurrence and a digit-dense nonnormal completion with a non-rational-polynomial perturbation. [Primary text](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf).
- Lagarias, 2001, Theorems 3.1 and 3.3, remark (1) following Theorem 3.3, and Theorem 4.1. Vanishing perturbations and asymptotic orbit matching can realize arbitrary real completions; irrationality and shadowing alone cannot imply uniform distribution. This does not refute the rational-function hypothesis. [Primary text](https://arxiv.org/pdf/math/0101055).
- Bailey and Crandall, 2002, Theorems 4.6 and 4.8 and Corollary 4.9. Controlled complete/incomplete modular cycles of specific constants supply the cancellation. There is no proven transfer of that length/spacing condition to the selected BBP cofactors. [Published paper](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf).
- Fixed-modulus PNT in arithmetic progressions, in both counting and Chebyshev-weight forms. All applications here allow an unspecified large onset. [Vaughan, Chapter 11, §3](https://personal.science.psu.edu/rcv4/568s20/568chapter11.pdf).
- Gauss rational-argument digamma identity for the signed radial finite part. [NIST DLMF §5.4](https://dlmf.nist.gov/5.4.E19).

The forked investigators share a model family. Agreement on a source identity, Markdown claim or a SHA does not confer independent mathematical authority. Reconciled checks use rational arithmetic in different representations, modular orbit and gcd comparisons, analytic proofs and mutation witnesses.

## Live delta during this run: #500

[Europa Weyl #500](https://github.com/femboy2112/SUCC/pull/500), head `bf103c4a25bbd83b6cfbad1dd77895928300ddd9`, appeared above the pinned #499. It has the same merge-base with main and restores all 14 archive members, including the 26 primal tests. We compared every one of the 14 ZIP members byte-for-byte against its Git blob on #500. All matched. The three-file audit remains correct for #499 itself. On a separate detached #500 checkout, invoking the restored primal suite and Europa native entrypoints passed 29 outer tests, with 4 and 7 nested beta and Weyl tests. [Run output](validation/pr500.txt). Of the four hosted PR-triggered workflows returned when checked, three succeeded and the main validation was running; this is a timestamped observation at the above SHA.

For mathematical attribution, #500's energy/PAIR_SIEVE.md and primal/PRIME_LAYERS.md already contain the square-root mean pair-loss estimate and the same five-shift physical count comparison. Its radial/RADIAL_CONTROL.md gives the exponent 8 and a stronger first-order expansion of J on the radial control. These are overlapping derivations using the same BBP pair dynamics; they are not new priority claims of this dossier. Its energy sieve discards a power-sparse exceptional set of pairs. The bounded number of exceptional lag diagonals in front2, the sharp fine-scale short-return estimate, the ternary occupancy theorem and the mixed-denominator/single-prime orientation test have distinct statements. No files from #500 were imported.
