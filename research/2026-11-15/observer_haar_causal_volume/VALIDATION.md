# Validation and reproducibility

Theorems AH-01--AH-10 have written derivations and explicit domains. The finite
runs below audit implementations, signs, source retention and discriminators.
They are not physical quantum experiments, a Lean proof or hosted-CI results.

## Actual executed checks

| Check | Observed result and scope |
|---|---|
| Full inherited discovery suite | **13,332 tests executed; one subprocess import error**, 1,066.104 test-run seconds, exit 1. Started at pinned parent `2c73e6388b24c7a66683d089733105d14acda08a`, before new production/test files existed. The isolated diagnosis and corrected replay are recorded below. |
| Inherited error diagnosis and replay | The unchanged `meta_choice_descent_probe.py` fails with `ModuleNotFoundError: observational_succ` when launched without the repository import path. With `PYTHONPATH=.`, the same probe passes and **all 11 tests** in its inherited module pass (0.146 test-run seconds). No production or test source was changed. |
| Final focused suite | **245 tests PASS**, 6.122 seconds, exit 0; **72 new tests** (24 adaptive observer, 18 Haar/Gamma/source certificates, 30 quantum instruments) plus related inherited tests. |
| Initial focused suite | **244 tests PASS**, 5.970 seconds, exit 0, before the final fixed-plan/beta-reference regression clarifications. Raw history retained separately. |
| Required provenance | **PASS**, exit 0, 0.037 seconds; original registry and archival checks retained in the raw log. |
| Required observer foundations | **PASS**, exit 0, 0.095 seconds. |
| Required ordinal report | **PASS**, exit 0, 1.926 seconds. |
| Root replay of independent translation audit | **111 exact checks PASS** across **18 reversible rational cases**, exit 0, total script 1.131 seconds. Includes nonuniform stationary measures and wrong-adjoint/nonreversible/unequal-depth controls. |
| Native source quadrature diagnostic | The same standalone script evaluates the literal original source at 50 decimal digits, separately labelled non-rigorous. It is an independent expression-level comparison, not an interval proof. |
| Reproducible report probe | **PASS**, exit 0, 0.189 seconds. Computes exact/enclosed plan utilities, source Haar energies, classical Gamma defect and quantum model tables. |
| Proof review | All three bounded reviews closed at theorem SHA-256 `eb7c26b99eac112364db19a746e45e979cfc0abf98f34a29e34487586f0b9125`. Shared model/source provenance is disclosed. |

Counts overlap across inherited, focused and agent runs. They must not be
summed as distinct tests. The inherited full discovery and final focused suite
are separate runs; this record does not call them one final-tree full suite.
The complete inherited discovery was not rerun after the environment correction.
Its raw failure remains a failure in the receipt; the corrected replay resolves
the observed import-path error without claiming a clean full-suite rerun.

## What the controls distinguish

### Adaptive observer

The exact core retains all four probabilities of `(S,theta)`, while a separate
adapter agrees with inherited `JointInstrument` filtering. Rational series
enclosures certify the two-stage cost example. Numerical information scores,
Gibbs probabilities and menu recommendations are labelled approximate.

The 24 tests include a 256-path randomized adaptive likelihood-ratio census,
a 32-path temporal martingale-energy census, independent Decimal logarithms,
zero support, adverse evidence, repeated-record and state-reset mutations.
An already-known target has zero future information; resetting its belief
incorrectly manufactures another bit. A nonuniform reference demonstrates why
increasing inverse temperature need not monotonically concentrate the policy.

### Haar/Gamma and original source

The finite generator model is explicitly symmetric/uniform; the broader
weighted reversible theorem is independently audited. A four-state classical
path has trace defect exactly `1/49`. A directed-cycle control has negative
eigenvalue `-1/25`, rejecting an unqualified positive-defect claim. Independent
source blocks, full resolution and depth zero are null controls; a depth-eight
example rejects monotone defect growth.

For the original Oily law, positive geometric tails give outward rational mass
enclosures. Polynomial cancellation gives exact first/second power moments.
The tests check the canonical BBP prefix, deletion of an original channel,
dyadic mass additivity, every tested positive detail, decreasing residuals,
analytic residual bounds, and a fresh 21-term enclosure against an 8-term one.

The translator additionally checked 48 exact symbolic moments, 45 numerical
mass/energy/residual comparisons and two highest-level/lowest-precision cases
while reviewing the module. Those bounded review runs are recorded in its
notes; they are not additional unittest counts or independent physical data.

### Quantum instruments and classical replicas

All state/instrument entries in the new finite core are real rational numbers.
Exact PSD validation, branch normalization and weighted outcome disposal are
required. The 30 tests include 168 no-signalling cases (12 states, seven
instruments, two wings), 128 joint-probability tables / 512 probabilities,
64 product-state and 28 separable-mixture controls, and all 16 deterministic
CHSH assignment tables.

The dephased and coherent states share all same-basis probabilities and local
marginals. Shared classical signs also reproduce the entire restricted X/Z
table if the qubit model is not trusted. The rotated rational CHSH settings
give `8/5`, `5/2`, `14/5` at coherence `0`, `3/4`, `1`. These are model
predictions. No setting-independence, separation or detector behavior of an
external physical apparatus was measured.

## Boundaries of the receipts

`report_probe.json` rounds source and information enclosures OUTWARD using
integer division to 12 decimal places. Those decimal endpoints remain rigorous
rational bounds. Its Gibbs probabilities and plan recommendation fields are
ordinary numerical approximations, explicitly named as such. The positive
plan inequalities have separate rational certificates.

`translation_audit.json` separates exact rational algebra from 50-digit
quadrature. Neither the quadrature nor agreement among agents proves a
physical source model. The source kernel's exact rational tail proof, not a
rounded plot or fitted model, justifies the certified enclosures.

All concrete proof-review findings were repaired: deterministic initial
posterior, constant versus informative deterministic report, complex Haar
modulus, independent policy randomness, supported reference probabilities,
the precise inverse-temperature limit, positive Gamma depths, normalized
quantum instruments, positive selected-outcome probabilities, and the fact
that forgetting a record retains the intervention that was actually performed.

## Reproduction

From the repository root:

```bash
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
PYTHONPATH=. python -m unittest tests.test_adaptive_haar_observer tests.test_haar_gamma_bridge tests.test_haar_quantum_instruments -v
PYTHONPATH=. python research/2026-11-15/observer_haar_causal_volume/translation_audit.py
PYTHONPATH=. python research/2026-11-15/observer_haar_causal_volume/report_probe.py
```

Production additions and ordinary tests use the standard library. The
independent translation audit requires SymPy and mpmath. Versions and pinned
source hashes are retained in `receipts/environment.json`,
`receipts/inherited_blobs.json`, `receipts/focused.json`, and the final payload
manifest `FILE_HASHES.json` (which excludes itself).
