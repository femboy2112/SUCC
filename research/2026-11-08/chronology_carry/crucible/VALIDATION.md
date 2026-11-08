# Hostile front validation and review

This front was assigned independently before reading the model/theory
proposals. It shares the parent model family and repository; it is not
external scholarly review. No holdout source phase was read while designing
or running the following controls.

Executed from the repository root:

```sh
python -m unittest discover -s research/2026-11-08/chronology_carry/crucible -p 'test_*.py'
python research/2026-11-08/chronology_carry/crucible/carry_controls.py --output research/2026-11-08/chronology_carry/crucible/CONTROL_RECEIPT.json
```

Initial controls: **5 tests PASS**. The exact oracle records:

- 36 complete rational carry partitions for bases2,3,5,16 and depths1,2,3;
- 12 original-forcing finite Green couplings, including exact mismatch measure;
- 15 same-prefix future-phase pairs, including odd denominator, finite local
  place preservation and two-adic precision controls;
- 24 exact future-carry cylinder reconstructions exposing forbidden lookahead.

The oracle uses independent Fraction source arithmetic and exact floor-boundary
enumeration. It imports neither the learned-table implementation nor its
Taylor/interval engine. These are small finite controls, not source holdouts.
The inequalities have complete elementary paper proofs in `THEOREMS.md`;
the tests do not promote the selected-source asymptotic gate.

The theory agent independently reviewed HCP2--3: the full-cell count, finite
Green transport, independence of the completed digit word and future Haar
circle, and the mismatch-risk constants were checked. Its requested
clarification about extending g to ideal digit words outside the observed
literal domain was incorporated. HCP3 remains an ensemble/window statement,
not a bound for zero or for a folded error.

The hostile agent then read the full model implementation and CCM1--3. No
substantive defect was found in current/past carry indexing, the frozen
table's dyadic definition, exact source recurrence, modulus enclosure,
period-square identity or charged residual/resonance accounting. The
canonical prediction certificate is correctly disclosed as no stronger than
the direct identity. This is source/proof review, not an independent full
later-clock execution. The recorded code/proof hashes delimit the reviewed
version; subsequent changes require a fresh scoped review.

The hostile agent independently reviewed CCV1--5: the nilpotent Poisson
compiler, endpoint sign, padded-window covariance normalization, all-epoch
conditional gate, source carry/Green identity and fixed-depth normal-trajectory
prediction-risk proof survived. Its strict folded-residual caveat is necessary.
No paid original-zero estimate is implied by either paper.

The downstream all-epoch covariance/Weyl/normality reduction was inspected
at starting head19d98078b60e47092c9b9d050a70b6b7eabb7cd2. No new defect was
found under its stated fixed-h, all-A, exact source and aperture hypotheses.
No new Lean statement, main-branch modification or external validation is
claimed by this front.

## Follow-up proof and instrument reviews

The final follow-up reviewed the root's FR1--3 finite-range theorem and
`signed_probe.py`, CCM4's whole-table-family dual certificate, and
CCV1-L/Q, CCV6--7's literal-alphabet/quotient/retrodiction refinements.
No substantive defect survived. Two proof-support clarifications were
requested and incorporated: FR3 explicitly uses componentwise pair
transport, and the literal-alphabet occupation formula assigns reference
probability zero to incoming16 instead of treating all17 digits uniformly.

The new [EI1--6 appendix](EXPLICIT_INNOVATION.md) gives an explicit bounded
innovation, a uniformly summable memory tail, a continuous observer on
Z_16 times the incoming literal carry, and its source-authenticated
O_h(log A/A) transport to the Weyl mean. The theory agent and root each
independently checked the formulas, constants and wrong-seed control.
Those checks share the same model family and mathematical ancestry.

Its independent oracle uses the exact root field Q[X]/(X^M+1), not the
main Poisson implementation. **5 additional tests PASS**; the receipt
records28 configurations,3448 exact innovation identities,18 separate
70-digit interval common-factor checks, and612 exact original-source
integer-lift compression identities. It also checks288 exact frequency
scaling/conjugation identities, including the root-proposed EI6 mode reduction.
The memory-tail inequality itself
has a complete paper proof; finite successes do not assert an infinite
source cancellation theorem.

## Independent later-source phase checks

Before the held-out source file existed, fixed probe times
55003,55020,55100,55736,82381,82504,110004 and frequencies1,3 were declared.
The independent implementation computed the BBP finite sum using small
pole-denominator modular powers and192-bit dyadic term floors, followed
by70-digit mpmath interval trigonometry. It imports neither the experiment's
common-denominator source recurrence nor its Taylor phase evaluator.
Two additional tests compare24 small exact Fraction source states/precision
cases and verify binary interval endpoint conversion.

The prepared independent receipt was hashed before the raw source file was
opened: `6e2f417003f00ea723434d8ba59f382066a0a07817be04d86b5999e139bdb577`.
Comparison after the source run completed found **all14 independent phase
intervals contained in the experiment's rectangles**,28 real/imaginary
containments. The independent source sums used1,982,992 small modular terms.
The preparation and comparison receipts retain code and file hashes.
Shared BBP finite-sum mathematics remains one provenance family; this is
independent representation, arithmetic and trigonometric implementation,
not an independent proof of the whole held-out covariance computation.

The later [carry-only actual-source audit](CARRY_ONLY_VALIDATION.md) adds
two guarded tests and six source comparisons, with prepared formula output
separated from subsequent phase comparison. It is a postregistration check
on the same holdout, not a new predictive experiment.

The complete hostile-front suite now has **14 tests PASS**. Reproduction:

```sh
python -m unittest discover -s research/2026-11-08/chronology_carry/crucible -p 'test_*.py'
python research/2026-11-08/chronology_carry/crucible/innovation_oracle.py --output /tmp/innovation-replay.json
python research/2026-11-08/chronology_carry/crucible/independent_phase_check.py prepare --output /tmp/independent-phases.json
python research/2026-11-08/chronology_carry/crucible/independent_phase_check.py compare --independent /tmp/independent-phases.json --source research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz --output /tmp/independent-phase-comparison.json
```

Use the existing environment with mpmath for these commands; no new
dependencies were installed. No Lean/kernel claim is made.

**Original-zero signed covariance: OPEN. Pi base16 normality: OPEN. RH: OPEN.**
