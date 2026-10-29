# Validation and scope — 2026-10-28

**Pinned parent:** research draft PR #356, commit b89fac9aff8bc0ef20dc0f1beda0020d0141701f, tree 259c0f2a31d4a60f472aa2844e1ebf1b13457e5d. Additive research-only folder; original SUCC source/zero seed, historical proof catalog, production files and CI workflows unchanged.

**Actual isolated local runs:**
- Python 3.13.5, standard-library exact Fraction implementation: 13/13 unittest methods PASSED, including native birth, beta-binomial winner, bounded martingale, complete-history density, selected/rejected reconstruction, finite KL controls, finite-vs-latent maximum, off-real local roots, and coherent-ancilla dephasing.
- Independently coded SymPy factorial/Beta/oracle: 1323 symbolic checks PASSED, including direct Beta-integral/combinatorial formulas, harmonic Doob identities, native/conditioned history normalization, reverse-polynomial root identity, two-branch source reconstruction.
- Six deliberate false-model controls all rejected (6/6); these are diagnostic model mutations, not mutations to production files.
- Python compileall passed. Numerical KL and Fourier residual checks are OBSERVED; the mathematical claims rest on the written derivations, not decimal evaluation.
- First local unittest had a convergence-tolerance failure for the reverse KL at finite j; tolerance calibrated against the rigorously derived limit, no theorem/source changed.
- First symbolic run assumed SymPy automatically simplifies a Beta function with integer arguments; repaired via explicit expand_func. Retained here as a detector/configuration failure, not a mathematical counterexample.

**Byte identity verified:** the four GitHub Python files match the locally executed source by exact Git blob IDs:
- order_stat_bridge.py = f79e6275ff6b704e3b963854a16e96d23f26d76f
- test_order_stat_bridge.py = 31bd342eaf222aaf7025e8fa6b0fad52e92ef006
- independent_oracle.py = 7d083ee873fa54c8dca6c8fbd66bb68ec984b69f
- mutation_probe.py = 02e138f13c7bdc7286934e2cda2c86356428965f

The research dossier in the GitHub PR was authored directly for review; it is not claimed byte-identical to the longer local zipped dossier, which supplies supplemental notes. Every mathematical statement is scoped to the actual Pólya source or labeled as a countermodel. **One reasoner** produced each implementation; distinct code methods are not blind independent mathematical witnesses.

**Not executed and not claimed:** complete SUCC native checkout, all four AGENTS root gates (provenance, native tests, observer probe, ordinal probe), Lean kernel, hosted CI of the published head, interval arithmetic aroundoff certification, external peer review, academic novelty verification.

CI discipline: use one draft PR and one atomic additive commit with [skip ci]; no workflow configuration changed. A zero-hosted-runs result means NOT TESTED on GitHub, not passed.

RH and pi normality OPEN. No source-faithful map of these local phase-character zeros to the completed-zeta zero spectrum has been constructed.
