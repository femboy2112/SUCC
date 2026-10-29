# Exact local validation and limitations

**Evidence actually generated in this container**

1. `python -m unittest -v test_hopf_source.py`: **34 tests PASS**; 34 named unit tests report `ok`. Arithmetic and quaternionic coordinates use exact Python `fractions.Fraction`, not floating-point assertions. Cases cover Hamilton multiplication, right/left gauge, source polynomial/taps, chiral state and `T^8`, original four signed poles, source zero seed, odd one-chart counterexample, two-chart recovery, two-step rotation, signed-source tomography, pole-basis permutation, arbitrary partner synchronization, wrong chirality, signed-to-absolute pole mutation, and coherent changed-seed finite tail.
2. `python oracle_sympy.py`: **PASS**, independent symbolic derivation of the rank-two source matrix from the original complex even/odd sector rule, characteristic polynomial, orientation sign, `T^T T`, quartic and octic relations, Hamilton anti-factor and two-step rotation. This is independent code using the **same source definition and same model family**, not a blinded independent witness.
3. `python make_receipt.py`: **PASS**, serializes authenticated exact rational examples and named source SHA into `SOURCE_RECEIPT.json`.
4. SHA-256 manifest generated from the final raw bytes; archive creation and ZIP integrity checked during packaging.

**What was NOT run**

- Full SUCC repository Python native CI against current or proposed Main XII, because local work is held separate from changing GitHub and no live checkout was imported.
- Lean formalization, independent human peer review or new mathematical publication priority check.
- Infinite-time numerical proof of anything; pointwise infinite claims in the dossier have separate elementary algebraic or asymptotic arguments. No theorem about real base-16 π normality or RH has been established.
- Any source-preserving cross-time intertwiner between the selected `U0=0` BBP carries and the quaternionic four-sphere; that is **UNVERIFIED** and listed as the next discriminating probe.

**Provenance warning:** the authoritative in-repo definitions were read through the GitHub connector from PR #333 `a0e4bfd9...` and main `6dd8073...`; this package reproduces those formulas in a *new* standalone module rather than importing unreviewed files from a moving branch. Recheck fresh ancestry after Claude's integration before adding any work to GitHub.
