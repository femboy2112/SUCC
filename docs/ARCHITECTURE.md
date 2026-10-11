# Architecture of Observational SUCC

## Goal

**Keep the general observer/knowledge theory independent of RH.** Maintain a small, auditable core for causal actualization, computational syntax, proof authority and physically motivated finite quantum instruments. Preserve imported number-theoretic laboratories as optional applications rather than treating RH as axiomatic.

## Conceptual layers

| Layer | Mathematical responsibility | Modules |
| --- | --- | --- |
| Physical carrier and outcome semantics | Finite quantum states, instruments, causal records; exact stochastic readouts and distinguishability loss | quantum_records, operational_semantics |
| Field-relative causal events | Immutable journal, actualized versus pending observations, finite SUCC and contexts | core, engine, arithmetic |
| Semantic representation and observability | Probe families, Yoneda-style restriction, witnessed factorization paths and loss of distinguishability | phenomenology, yoneda, resource_probe, local_global, circle_transport |
| Ideal source-identification and model-relative access | Finite source-compatible version spaces, actualized probe histories, adversarial stationary access traps, conditional reconstruction and finite/omega/dark classification | ideal_frames, observer_traps |
| Absorbing frames and closure | Complete source-compatible fibers, shared exact probe predictions, finite Horn fixed points, constructive forcing and epi/physical access split | absorbing_frames, constructive_frontier |
| Finite communication | Target-specific sufficiency, causal access certificates and bit-minimal zero-error receiver-side-information coding | interobserver_channels |
| Knowledge-aided observer synchronization | Shared basis checks, source-attested local probe batches, strict epistemic catch-up and snapshot-only optimizations | knowledge_ladder |
| Logical proof authority | First-order syntax, Gödel codes, checking finite proofs, finite two-counter program observations | observer_logic, godel_succ, observer_reflection |
| Ordinal/limit phenomena | Directed finite histories, formal omega reports, nonuniform limits, finite proof support | infinite_realization, ordinal_succ_report |
| Mathematical stress tests (optional) | Gamma/FUCC, Euler source, Hasse, Li, Suzuki/Weil, Lambert, certification | gamma_interferometer, gamma_succ_path, balanced_theta_li, hasse_theta_seam, dirichlet_lambert, lambert_succ, source_prime_certificates |

The mathematical subsystems have distinct domains and kinds of evidence. They are **not** a single already-proved functor from physical reality to theorems.

## Typed boundaries

**Observation → history:** the observed event must have a realizable outcome and a known instrument/source context. Prediction is a separate type of object. The finite quantum model stores both a reduced density matrix and immutable classical outcome records; the observer cannot retroactively rewrite them by reinterpreting the state.

**History → semantic model:** an update may reconstruct, compress or forget. A zero connected residual in an invertible arithmetic logarithm does not invalidate the original observation. An unrecoverable compression must disclose information loss.

**Semantic model → new probe access:** the preferred model and the set of *all* history-compatible candidates have different types. A stable favorite is not a completion certificate. A model-generated probe menu may leave a globally distinguishable source undiscovered forever, even with ideal exhaustive local observations. Separate globally absent probes, inaccessible-but-global probes, and accessible-but-never-scheduled probes; an externally forced probe must retain external provenance. The observer_traps module gives a finite exact iff theorem, not a cognitive/physical universality theorem.

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

## The absorbing-model correction and Hard SUCC

The maximally faithful ideal working model is the **complete compatible source class**, not a favored source selected by a tie-breaking prior. It also includes all predictions shared by every compatible candidate and closure under justified inference. An older preferred-model trap remains useful as a calibrated bad-policy countermodel but is not an identity claim about the absorbing observer.

Mathematically separate four types: **actualized source event**, **model-invariant predicted outcome**, **epistemically generated probe** and **physically executable probe**. Contradictory evidence means check the source table, model class and rules; it does **not** refute classical excluded middle. A new probe can be generated by noncontradictory evidence and may be prevented from running by physical feasibility.

Finite Hard SUCC exhausts an exact finite rule/probe universe. For an infinite theoretical closure, Kleene's omega-limit fixed-point theorem requires monotonicity and omega continuity, or another separately proved limit mechanism. A monotone but non-omega-continuous observer closure may need omega+1. No physical infinity was executed.

A source- and report-preserving inter-observer completion requires a finite message, common decoding semantics, and trustworthy causal evidence. The exact full-frame message includes source-compatible lawful probe-acquisition replay, while a shorter target-only witness explicitly lacks that provenance. Finite-alphabet exact universal communication of arbitrary real constants is impossible by countability. For finite one-shot zero-error communication with receiver side information, the optimal fixed-length bit budget is derived from the confusability graph chromatic number, not from mere probe count.

See [the formal research memo](../research/2026-10-10/ABSORBING_HARD_SUCC_AND_TRANSMISSIBILITY.md) and claim ledger O55–O66. The finite implementations do not automatically transport to general neural, quantum, or RH settings.

## Two-observer knowledge transport versus physical observation

A sender's several legitimate local SUCC frames can be imported in one recipient K-SUCC **epistemic macro-step** if both share exact causal prefix, source/probe interpretation and closure rules. Transfer preserves the original observer attribution; it does not become a new physical observation by the receiver. Exact replay certifies only source-compatible, lawfully enabled paths against the *declared* world, not real physical authentication.

The **snapshot placement** (compatible source fiber, shared predictions, derived semantic facts and epistemic probe frontier) is weaker than **continuation placement** (all future behaviors can be matched). A minimal snapshot can omit a seemingly redundant causal event and thereby change the receiver's next local exploration. The strict recorder carries the full provenance-labeled batches and can preserve continuation under equal physical instrument feasibility, deterministic update rules and source outcomes.

Shared language hashes reject stale or changed basis and source versions. Genuine concurrent observers with overlapping, non-prefix evidence will require a new rebase and merge theorem; symbolic labels alone do not validate an epistemic translation across changed mathematical bases. An infinite ladder of finite successful squares is not a finite transmission of an arbitrary infinite result: the limit additionally requires verified topology/continuity, finite description/proof obligations and accounting for all transmission costs.

See [KNOWLEDGE_AIDED_SUCC_LADDER.md](../research/2026-10-10/KNOWLEDGE_AIDED_SUCC_LADDER.md). No general cognitive, quantum, category-level functor or arithmetic RH-sign theorem is being claimed.

## Model-dependent observation and source-relative certification

For a deterministic finite source model, the exact observer-trap machinery tracks the immutable outcome history, a compatible version space, a preferred semantic model, the model-conditioned menu of admissible probes, and an explicitly chosen scheduling rule. The toy observer can be internally stable but globally wrong. Observed causal records remain authoritative even if the preference changes.

The declared global probe universe and an externally supplied actual-source label allow a *laboratory* to certify access/scheduling/source blindness. An actual embedded observer does **not** acquire that external label by running the certification function. Any extension to physical instruments needs a separate physically feasible probe predicate and a source-independent selection mechanism.

A source-identification theorem from compatible-menu union is conditional on all unioned probes being executable. Absence of an effective convergence modulus is separate from structural infinity-stage uniqueness, and finite model classes cannot be genuinely omega-only identifiable under monotone exact observations.

See [model-dependent observer traps](../research/2026-10-10/MODEL_DEPENDENT_OBSERVER_TRAPS.md), [ideal frame completion](../research/2026-10-10/IDEAL_FRAME_COMPLETION_TRICHOTOMY.md), and claim ledger O39–O54. No source-to-Weil positivity or proof-theoretic completeness identification follows.
