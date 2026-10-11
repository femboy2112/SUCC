# Architecture of Observational SUCC

## Goal

**Keep the general observer/knowledge theory independent of RH.** Maintain a small, auditable core for causal actualization, computational syntax, proof authority and physically motivated finite quantum instruments. Preserve imported number-theoretic laboratories as optional applications rather than treating RH as axiomatic.

## Conceptual layers

| Layer | Mathematical responsibility | Modules |
| --- | --- | --- |
| Physical carrier and outcome semantics | Finite quantum states, instruments, causal records; exact stochastic readouts and distinguishability loss | quantum_records, operational_semantics |
| Field-relative causal events | Immutable journal, actualized versus pending observations, finite SUCC and contexts | core, engine, arithmetic |
| Semantic representation and observability | Probe families, Yoneda-style restriction, witnessed factorization paths and loss of distinguishability | phenomenology, yoneda, resource_probe, local_global, circle_transport |
| Logical proof authority | First-order syntax, Gödel codes, checking finite proofs, finite two-counter program observations | observer_logic, godel_succ, observer_reflection |
| Ordinal/limit phenomena | Directed finite histories, formal omega reports, nonuniform limits, finite proof support | infinite_realization, ordinal_succ_report |
| Mathematical stress tests (optional) | Gamma/FUCC, Euler source, Hasse, Li, Suzuki/Weil, Lambert, certification | gamma_interferometer, gamma_succ_path, balanced_theta_li, hasse_theta_seam, dirichlet_lambert, lambert_succ, source_prime_certificates |

The mathematical subsystems have distinct domains and kinds of evidence. They are **not** a single already-proved functor from physical reality to theorems.

## Typed boundaries

**Observation → history:** the observed event must have a realizable outcome and a known instrument/source context. Prediction is a separate type of object. The finite quantum model stores both a reduced density matrix and immutable classical outcome records; the observer cannot retroactively rewrite them by reinterpreting the state.

**History → semantic model:** an update may reconstruct, compress or forget. A zero connected residual in an invertible arithmetic logarithm does not invalidate the original observation. An unrecoverable compression must disclose information loss.

**Semantic model → proof:** syntactic proof authority requires an explicit theory and checked derivation. External reflection axioms and infinitary omega rules are not inferred from the number of observations.

**Finite proof → ordinal completion:** a finitary proof from the union of an increasing chain of theories already uses only axioms from a finite stage. This is a classical theorem about finitary derivations, not a claim that all infinite truths are unprovable.

**Physical Hilbert metric → Weil geometry:** covariance positivity is available in quantum/statistical models, including fake arithmetic. Identification with the completed arithmetic Weil distribution is a separate RH-hard equation.

## Repository layout

- **observational_succ/** — installable Python package; imported code retains the pre-migration internal module boundaries, with a new real-qubit instrument example.
- **tests/** — original regression suite with mechanically translated package paths, plus native SUCC tests and historical source integrity checks.
- **scripts/** — reproducible probes and audit tools. Scripts may need optional mpmath.
- **docs/** — current conceptual architecture, claim status, roadmap and outbound research contracts.
- **handoffs/rh/** — reviewed, standalone RH exports; *not* automatically synchronized with the source RH repository.
- **provenance/origins/fuckingrh/** — 17 byte-identical founding documents. Treat as immutable historical context; some older prose legitimately references the original source path.
- **provenance/IMPORT_MANIFEST.json** — content-addressed map of source Git blobs to destination Git blobs, with declared mechanical transformations.
- **.github/workflows/ci.yml** — tested Python 3.10/3.13 matrix with full code and source verification.

## Research provenance and gates

Claims should be labeled CLASSICAL, PROVED LOCAL, TESTED MODEL, HYPOTHESIS, UNVERIFIED or REFUTED and connected to a precise statement, author/source, proof or test, mutation controls and assumptions.

The mathematical **source of truth** is not merely a numerical plot. Finite negative claims require exact algebra or independently justified error enclosures. Even an impeccably rigorous prime-only interval is not a completed Gamma/Weil interval.

The quantum model is explicitly real two-dimensional and is not a neuroscience result, a general complex QFT model or an experimental verification of SUCC semantics.

## Direction of future change

We should gradually factor out a truly generic typed observer/record core from imported RH-specific arithmetic code. Do this by new adapters with equivalence tests—not a wholesale rewriting of the original import. Keep RH-specific tests as a deliberately difficult falsification environment for the theory.

For proposed diagrams, specify the precise functors/morphisms, domain of objects, continuity or topology, observational equivalence relation, and theorems about information preservation. Do not claim a commutative diagram because two paths look analogous.


## Certified observational-semantic contraction (native SUCC theorem)

The new operational_semantics module defines finite rational evidence laws and stochastic readouts mapping physical measurement outcomes to semantic labels. For every such readout C and any two evidence laws p and q, the exact total-variation contraction theorem holds:

\[
\operatorname{TV}(Cp,Cq)\le\operatorname{TV}(p,q).
\]

This follows by triangle inequality and nonnegative stochastic row normalization; its executable certificate reports a rational before/after distance and slack. It does **not** say that all semantic inference is a stochastic map, nor that quantum measurement itself is classical after arbitrary interactions. The real-qubit Kraus instrument supplies explicit physical outcome distributions. A postprocessing channel can erase the observer's ability to distinguish two earlier hypotheses **without erasing the original source or the separate causal record**.

See [the dedicated research derivation](../research/2026-10-10/FINITE_SEMANTIC_DATA_PROCESSING.md) and native test_operational_semantics.py.
