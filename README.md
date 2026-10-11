# Observational SUCC

### Finite observation · Causal history · Semantic mathematics · Ordinal completion

**Observational SUCC (ObsSUCC)** is an independent mathematical and physically motivated research program investigating how an observer embedded in the world builds, updates, and justifies mathematical knowledge from finite causal observations.

The founding hypothesis begins with **the physical carrier**, not with the mathematics an observer subsequently constructs. Quantum theory supplies a successful Hilbert-space description of physical observers and their interactions; this is motivation for the program, **not** a proof that Hilbert space entails arithmetic, a model of neural cognition, or evidence for physical transfinite computation.

> **Status:** early-stage formal and computational research. Some claims are classical mathematics, some are exact new-to-project derivations, others are tested finite models or open conjectures. The Riemann hypothesis (RH) remains unsolved, and Gödel incompleteness has not been mechanized within PA here. See [the claim ledger](docs/CLAIM_LEDGER.md).

## What the project studies

The central question is: **what information, structure, and proof authority survive the transformations from physical interaction to a causal record, a semantic model, a mathematical assertion, and an infinitary global report?**

\[
\mathsf{PhysicalCarrier} \longrightarrow \mathsf{CausalHistory}
\longrightarrow \mathsf{SemanticRepresentation}
\longrightarrow \mathsf{FormalKnowledge}
\longrightarrow \mathsf{GlobalReport}.
\]

These arrows are *proposed, typed mathematical interfaces*, not automatically valid equivalences.

A finite successor extends a record. An ordinal limit collects a compatible directed history. A post-limit report processes that limit. **Accumulating observations does not itself justify a universal proof or a positivity theorem.**

The most distinctive analytic idea is *second-order observation*: comparing how relationships between observations change. In a classical RH application, Suzuki's two-time screw kernel obeys the distributional identity

\[
\frac{\partial^2}{\partial t\partial u}
  K_\Psi(t,u)=\Psi''(t-u)=W_{\mathrm{Weil}}(t-u).
\]

This is an established identification of the completed arithmetic Weil distribution; **positive definiteness remains an RH-equivalent open condition**, not something guaranteed by the observer's physical Hilbert space.

## Read the theory

1. **[Foundations](docs/FOUNDATIONS.md)** — the originating physical/semantic proposal, precise mathematical types, causal SUCC, second derivatives, ordinals, Gödel/Turing, and the difference between reporting and proof.
2. **[Development method](docs/METHOD.md)** — the steelman → crucible → verdict loop that turns informal proposals and analogies into ledger-labeled claims.
3. **[Research architecture](docs/ARCHITECTURE.md)** — what belongs in the general theory, what is an optional RH adapter, how modules and data cross trust boundaries.
4. **[Ideal frame completion trichotomy](research/2026-10-10/IDEAL_FRAME_COMPLETION_TRICHOTOMY.md)** — source-faithful finite/omega/dark observation classes; analytic versus smooth jets; flat invisible germs; divergent-limit counterexample.
5. **[Model-dependent observer-trap theorem](research/2026-10-10/MODEL_DEPENDENT_OBSERVER_TRAPS.md)** — exact model-access and scheduling traps, source-faithful histories, active-probe repairs, finite stabilization and limitations.
6. **[Absorbing Hard SUCC and finite transmission](research/2026-10-10/ABSORBING_HARD_SUCC_AND_TRANSMISSIBILITY.md)** — full compatible-model closure, lawful omega limits, constructive excluded middle, epistemic/physical probe barriers and bit-optimal recipient-side-information channels.
7. **[Knowledge-aided SUCC and the inter-observer ladder](research/2026-10-10/KNOWLEDGE_AIDED_SUCC_LADDER.md)** — multi-frame discovery compressed into one recipient update, alternating ladders, causal receipt, snapshot-versus-continuation counterexamples and the omega ceiling.
8. **[Relative path/value knowledge deltas and proof-shaped probes](research/2026-10-11/RELATIVE_DELTA_PROOF_SHAPES_AND_FROZEN_BASE.md)** — equal empirical access and reasoning, state-anchored directions, verified evolving probe language and limits on returning arbitrary knowledge to a frozen base.
9. **[Claim ledger](docs/CLAIM_LEDGER.md)** — source-backed status of every important theorem, model, analogy, observation and missing lemma.
10. **[Research roadmap](docs/ROADMAP.md)** — executable, falsifiable next investigations independent of RH.
11. **[Source provenance](provenance/README.md)** — immutable historical archive and machine-verifiable Git blob manifest.
12. **[RH outbound handoffs](docs/RH_HANDOFF.md)** — a reproducible contract for exporting RH-bearing discoveries to the RH repos.

## Run it

Python **3.10+**. The primary causal, logical, exact arithmetic and finite qubit models are standard-library-only; optional mathematical experiments use mpmath.

~~~sh
git clone https://github.com/femboy2112/SUCC.git
cd SUCC
python -m pip install -e ".[test]"
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py' -v
python -m observational_succ demo
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/prime_source_certificates_probe.py
python scripts/semantic_data_processing_probe.py
python scripts/observer_trap_probe.py
python scripts/absorbing_frontier_probe.py
python scripts/knowledge_ladder_probe.py
python scripts/relative_delta_probe.py
~~~

The package name is **observational_succ**. No runtime dependency on the original RH repository is required.

### Working research components

| Layer | Key modules | Current scope |
| --- | --- | --- |
| Causal field and actualization | core, engine, arithmetic | Finite steps, source-context records, immutable journals, predictions vs. observations |
| Restricted semantics and categories | phenomenology, yoneda, resource_probe, local_global | Probe-relative recognition, path information, finite versus global views |
| Quantum physical-carrier model | quantum_records, operational_semantics | Exact real-qubit Kraus instruments, causal event replay and semantic-readout data-processing proofs |
| Ideal observational frames | ideal_frames | Exact finite derivative-probe SUCC and bounded-degree reconstruction; separate classical analytic/smooth omega theorems |
| Model-dependent probe traps | observer_traps | Exact finite source-faithful model access, wrong-model self-confirmation, fair escape and uncertainty-aware probe unions |
| Absorbing model and hard SUCC | absorbing_frames, constructive_frontier | Full source-compatible model closure, consistent generation of new epistemic probes, physical blocking, Kripke LEM boundaries and omega+1 examples |
| Inter-observer communication | interobserver_channels | Exact finite target messages, causal certification distinctions, and one-shot zero-error bit-minimal coding using receiver side information |
| Knowledge-aided SUCC and ladders | knowledge_ladder | Full causal multi-step A→B synchronization in one epistemic macro-update, alternating A/B ladder, minimal snapshot compression and future non-equivalence controls |
| Relative knowledge transport | relative_delta | Equal operational placement including probes/reasoner; causal paths and nonredundant values relative to last known position, moving concept basis, verified probe-value or target-decisive proof certificates, and frozen-base coding constraints |
| Gödel, Turing and finite proof | observer_logic, godel_succ, observer_reflection | Self-reference syntax, two-counter controls, checked proof authority, finite-support at omega |
| Ordinal and Hilbert limits | ordinal_succ_report, infinite_realization | Formal omega/omega+1 reports, second-order interaction, nonuniform Hilbert limits |
| Optional RH application bridges | gamma_interferometer, balanced_theta_li, hasse_theta_seam, source_prime_certificates, dirichlet_lambert | Gamma/prime source interfaces, Li-index windows, certified prime-only Suzuki bounds |

The imported RH experiments remain available to audit, but the future general theory is **not defined by RH**.

## Historical source and future exchange

This repo was launched after an extensive program in [femboy2112/FuckingRH](https://github.com/femboy2112/FuckingRH). The migration was pinned to [commit ba075348](https://github.com/femboy2112/FuckingRH/commit/ba075348b7bcc66d938b3e0ca96c26e95bba340a), corresponding to [the observational foundations PR #23](https://github.com/femboy2112/FuckingRH/pull/23). The [manifest](provenance/IMPORT_MANIFEST.json) records the exact original and destination Git blob identities for 72 historical artifacts: **55 mechanically namespaced Python files and 17 unchanged documents**.

New work belongs here first. When it yields an independently meaningful RH-related theorem, export a **self-contained, status-labeled, adversarially tested handoff** to femboy2112/FuckingRH or another RH research repo. Do not quietly convert general observational insights into RH proof claims.

**Professional operating policy:** no merge to main, release, package publishing, or unsupported change of license is implied by the initial repository setup. See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
