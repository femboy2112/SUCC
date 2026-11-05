# Validation — zero-object Casimir analogue and source-seed pressure

**Parent branch:** draft #513 exact SHA \`727a97a006e929243e0fee1ab44cf52dc68e2c8f\`. All new research and test files are additive. Original four BBP signed poles, literal U0=0, archival source, production, workflows, frozen proof contracts and Lean unchanged.

## Exact committed source replay

The standalone exact-rational source probe [seed_pressure_probe.py](seed_pressure_probe.py) was run in the container and its exact executed bytes Git-blob SHA \`73227edaace1304c9373bef3ce3d56ac0d58c5e7\` were independently verified by fetching that same file from the GitHub child branch. Source SHA-256 \`b9155ee4f8b04198d483206ed81f03bd0f8b2a66086fb5de5393057ada522259\`. It checks original four-pole forcing against the independent collapsed rational polynomial at every used index, and computes exact Fraction full pairwise signed Bernoulli covariance at the **fresh preregistered** A=9,11 epochs. Every gcd resonance identity is checked for each pair of labelled pairs. It also checks the exact rational Schur complement for the prospectively declared Gaussian boundary cases. Execution report ends with \`ORIGINAL_ZERO_OBJECT_CASIMIR_SEED_PRESSURE_FRESH_EXACT_PASS\`. Its raw stdout SHA-256 was \`ef494a31952b71a820cde0398ca08f5d927f34a89b591f73db09bee424de7992\`.

The separate root [tests/test_zero_object_casimir.py](../../../tests/test_zero_object_casimir.py) was run in a local replica with the source probe mounted at its EXACT intended repository-relative path; **12/12 unittest methods passed**, zero errors/failures in 0.270s reported. Its executed Git blob SHA \`613f4c356620c7d2d0c2f5694e1d25f8ad57f427\` was compared with the exact remote file blob and matches; SHA-256 \`58a9aabe1bb0b96bad92b712d627fcfd3e522b44b6138881d286540c4305d5a4\`. Raw full focused test log SHA-256 \`f3adb2227fe2e5f50a815286b553431faa9cdb846c174b9793bfb5886476f219\`.

## Actual finite results (numerical display of exact rational variance multiples)

| A | Var/pi² (exact rational, displayed decimal) | Actual variance | Proved upper bound |
|---:|---:|---:|---:|
| 9 | 0.0020651539376644 | 0.020382252392099 | 0.0527610853908 |
| 11 | 0.0014160838577158 | 0.013976187474423 | 0.0361221180033 |

The exact Fraction coefficient has 99/102 numerator/denominator digits for A=9 and 138/141 digits for A=11; the actual code computes it from source and pair resonance, rather than accepting a fitted decimal as evidence. All 12 focused tests checked authentic original source and seed aliasing, both new variance coefficients, the unforced baseline majorization, exact future zero-prefix phase orthogonality, nontrivial original two-time source correlation, inverse-branch count16, low-resolution full-epoch period, and high-resolution selected phase transport. A separate tiny radix b=2 pair-covariance midpoint quadrature yielded value 0.1596717713 versus exact Bernoulli prediction 0.1596443947; its 0.0000274 difference is numeric calibration, not interval certification.

The Gaussian source-free conditional bridge examples are independently calculated with exact rational fractions:

| rho | d | k | Var inside two-plate bridge | Var under single plate |
|---|---:|---:|---|---|
| 2/5 | 4 | 1 | 15561/18589 | 21/25 |
| 3/7 | 7 | 3 | 16831335520/16955457247 | 116920/117649 |
| 1/2 | 5 | 2 | 315/341 | 15/16 |

Each satisfies strict two-plate suppression. The AR(1) symmetry control reproduces the exact covariance under time reversal.

## Proof vs finite observations and CI status

- The all-A mean, Bernoulli pair covariance, universal variance bound, almost-every-seed Borel–Cantelli result, finite-zero Haar/source resonance, conditional Gaussian formulas and limit-swap refutation are **paper derivations in THEOREMS.md**. Finite source checks calibrate source/number-theoretic implementation, not global validity.
- The *post-preregistration* result CZ-05b (whole-epoch law and high-resolution K≈2A+O(log A) comparison) was identified during follow-up derivation; it is NOT retrospectively labelled preregistered. Its focused high-resolution test passed on A=3,9,17.
- **Not executed/claimed:** all 11k+ SUCC root suite at this child head, new Lean kernel theorem, full exact-head hosted workflows, independent outside referee, original selected s=0 determinant lower bound, π normality or physical Casimir effect.

## Reproduction from the repository root

\`\`\`sh
python research/2026-11-05/zero_object_casimir/seed_pressure_probe.py
python -m unittest discover -s tests -p 'test_zero_object_casimir.py' -v
python scripts/verify_provenance.py
\`\`\`

The expensive whole-repository 11k+ suite should be run at an integration gate, not after each exploratory mathematics commit. Preserve exact-head validation and do not promote parent green status to the present branch.