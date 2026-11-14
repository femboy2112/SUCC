# Operation Principia Observatoris — first kernel

The self-contained [manuscript](../../../docs/principia_observatoris/README.md)
contains six compact books, a notation/claim register and theorem dependencies.
The work is stacked on founding draft #618; main and historical sources are
unchanged. This is a completed first vertical slice, not a completed universal
theory of observation.

## Hole contract and result

**Question.** When do an observer's current distinctions suffice for lawful
future prediction, and can missing distinctions be exposed within a bounded
horizon without assuming the desired conclusion?

**Weakest useful proved slice.** On an authenticated finite-dimensional linear
carrier, exact prediction through a surjective observation P exists iff its
kernel is invariant. On a Hilbert unit-ball prior, the inaccessible target
component gives the exact best possible prediction error even over nonlinear
decoders. The smallest predictive row-space refinement is constructible, and
an authenticated dimension bound supplies a finite response-discrimination
horizon. Actual acquisition of that information is a separate policy question.
For total linear actions, exact readouts, the full Hilbert ball, a fixed initial
target and state-independent positive costs, CG11 answers its deterministic
minimax version: adaptivity cannot improve on the best fixed schedule. Removing
the full-ball prior admits an exact seven-state counterexample.

**Novelty tax.** The proof ingredients are classical. They close a concrete
SUCC interface between target descent, dynamics, optimal prediction and finite
access; they are not an equivalent restatement of π normality. The authentic
BBP forcing then provides a rigorous stress test: its infinite Hankel rank
blocks a finite-dimensional closure shortcut, and gives a sharp 2d+1-value
discrimination theorem with positive rational margins against dimension-d
stationary linear rivals. No signed normality saving follows.

The [sharp rival radius](sharp_rival_radius.md) also gives the **exact** minimum
uniform error when the rival may redistribute its error across the whole
prefix. Its rational attaining realization is different from the exact-prefix
companion. The two errors have different explicit fixed-order leading constants.

**Cheapest falsifiers retained.** A hidden coordinate escaping into a visible
one; a signed diamond with zero endpoint response; an invented quotient path;
a destructive probe; a late spike; a fitted finite-rank BBP continuation; a
quantum reset channel whose individual outcomes expose hidden coherence.

## Evidence and provenance

| Artifact | Purpose |
|---|---|
| [Provenance audit](provenance_audit.md) | Live source heads, existing theorem map, definition reconciliation, arithmetic frontier |
| [Foundation entrypoint audit](foundation_entrypoints_audit.md) | Complete coverage and hashes for the twelve required foundation files |
| [Geometry review](geometry_review.md) | Exact theorem contract and hostile boundaries |
| [Finite-horizon review](finite_horizon_review.md) | Sharpness, classical references, assumption deletion and scope |
| [Quantum review](quantum_review.md) | Outcome closure, disturbance and finite all-state calibration |
| [Crucible audit](crucible_audit.md) | Independent-implementation checks, discovered errors and repairs |
| [Validation](VALIDATION.md) | Actual commands, exact outcomes, source hashes, limitations |
| [Live-head snapshot](receipts/live_heads.json) | Founding/base and inspected open draft refs |
| [Exact native probe](receipts/exact_probe.json) | Reproducible rational witnesses and native forcing cross-check |
| [Independent audit](receipts/independent_audit.json) | Exhaustive small models, differential tests and hostile mutations |
| [Quantum PSD certificate](receipts/quantum_certificate.json) | All 64 tested signed matrices, positive and negative controls |
| [Arithmetic scale certificate](receipts/arithmetic_scale.json) | Exact beta bounds, independent Rodrigues norms, orthogonality and failed mutants |
| [Adaptive acquisition controls](receipts/adaptive_linear.json) | All 13 fixed schedules on a seven-state prior, nonlinear-action and cost countermodels, and changed randomized-loss objective |
| [Sharp rival radius](sharp_rival_radius.md) | Uniform componentwise discrimination threshold, attaining rival and its relation to the exact-prefix residual |
| [Exact sharp-radius controls](receipts/sharp_rival.json) | Independent cofactors, companion recurrences, PSD minors, Sturm root counts and nonoptimal perturbations |

The independent audit means a separate implementation/decomposition. All agents
were from the same model family. These are not independent physical experiments,
blind external reviewers, truth probabilities or formal-kernel certificates.

## Reproduce

```sh
python -m unittest discover -s tests -p 'test_principia_observatoris.py' -v
python scripts/principia_observatoris_probe.py
python research/2026-11-13/principia_observatoris/independent_audit.py
python research/2026-11-13/principia_observatoris/quantum_certificate_probe.py
python research/2026-11-13/principia_observatoris/arithmetic_scale_probe.py
python research/2026-11-13/principia_observatoris/adaptive_linear_probe.py
python research/2026-11-13/principia_observatoris/sharp_rival_probe.py
python scripts/principia_ancestral_probe.py
python scripts/verify_provenance.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The native library uses exact Python integers and Fractions, rejects floats and
booleans where exact integers are required, and does not add runtime dependencies.
The source tables are finite supplied mathematical models; input labels do not
prove empirical authenticity. Universal results are justified in the manuscript.

## Remaining proof debt

The strongest next obligation is an executable, disturbance-aware predictive
completion theorem: jointly acquire a sufficient predictive statistic on one
carrier with explicit costs, or certify that no admitted policy can do so.
CG10 supplies the fixed-schedule criterion; CG11 solves deterministic noiseless
full-ball acquisition by reducing it to a finite schedule search. Noisy,
finite-bit, more general prior and quantum/disturbance-constrained acquisition
remain open. For arithmetic, the live R0
nonresonance rung and original-source signed cancellation remain open and
require a different source-specific estimate.
