# Observational SUCC

### Carrier reconstruction · Source-indexed transitions · Observer-relative proof access

**Observational SUCC (ObsSUCC)** is an independent mathematical research framework for
**constructing, relating, completing, and observing mathematical carriers through lawful
source-indexed transitions**, with explicit accounting of which structure, information, proof
authority, and causal history survive each transformation.

Its underlying research question is **how a finite embodied observer builds, relates, and justifies
mathematical knowledge from causal interactions** — and, concretely, how one constructs an
*equivalent interface to a larger carrier* out of smaller source carriers and their admissible
categorical edges. The physical-observer intuition is the historical motivation; it is **not** a
prerequisite for the mathematics, and the general theory is **independent of the Riemann
hypothesis**. RH is a demanding downstream application, not SUCC's definition.

> **Status.** Early-stage formal and computational research. Some results are classical mathematics
> realized as exact finite source charts; some are exact new-to-project derivations or tested finite
> models; others are open conjectures and preserved counterexamples. **The Riemann hypothesis
> remains OPEN. RH PROVED: NO.** No carrier equivalence in this repository produces Weil positivity,
> and no positive Hilbert covariance is identified with the signed completed Weil form. See the
> [claim index](docs/CLAIM_INDEX.md) and [claim ledger](docs/CLAIM_LEDGER.md).

**Proof Teeth research checkpoint:** [round report](research/2026-10-15/SUCC_PROOF_TEETH_MEGA_ROUND.md)
and [claim supplement](docs/CLAIM_SUPPLEMENT_PROOF_TEETH.md) add the proved finite-Haar-to-profinite-Hilbert
completion, exact minimum-observation certificates, paired YEAN Lean kernels,
and authentic four-low Schur trial obstructions. The original Schur sign remains open.

**Observer–Schur Round II:** [theorem and execution report](research/2026-10-16/OBSERVER_SCHUR_ROUND_II.md)
and [claim supplement](docs/CLAIM_SUPPLEMENT_OBSERVER_SCHUR.md) separate exact energy,
sign and fiber envelopes; add compact Galerkin bounds, relative-residual
counterexamples, typed formal instances and an authentic-source trial-family obstruction.
The original signed Schur problem remains open.

**Arithmetic Resonance:** [source theorem and execution report](research/2026-10-16/ARITHMETIC_RESONANCE_MEGA_ROUND.md)
and [claim supplement](docs/CLAIM_SUPPLEMENT_ARITHMETIC_RESONANCE.md) add exact prime-hinge
geometry, a source-specific dense high-response theorem conditional on inherited
coercivity, and improved two-sided first-window Schur bounds. Fractional spectral
rigidity and the original sign remain open; finite spectral moments alone cannot
control inverse response.

## The central mathematical objects

SUCC works with actual carriers — `N, Z, Q, R, C, Ẑ, Q_p, A_f, A_Q` — and groups, rings, fields,
topological spaces, categories and their structure-preserving morphisms. The crucial idea is not
growing bigger sets; it is building a lawful interface to a larger carrier from smaller source
carriers via explicitly justified operations: **group completion, localization, quotients and
gluing, Cauchy and topological completion, inverse and direct limits, Yoneda reconstruction,
Pontryagin duality, and Fourier/Mellin/Poisson transport.**

The discipline is to distinguish rigorously between the original smaller carrier, its completed
carrier, a proper embedding, a quotient, a categorical equivalence, an isomorphism of a particular
structure, and a finite executable representation of one point. **An equivalence between completed
mathematical objects does not mean the original smaller carriers were already equivalent.**

- **[Carrier Atlas](docs/CARRIER_ATLAS.md)** — the backbone: every reconstruction with its
  construction, comparison map, strength (iso / equivalence / embedding / quotient / dense), what is
  preserved, what is lost, status, and evidence.
- **[Carrier Foundations Synthesis](research/2026-10-15/SUCC_CARRIER_FOUNDATIONS_SYNTHESIS.md)** —
  the paper-style account: notation, the *carrier reconstruction certificate* schema, propositions,
  counterexamples, verification, and a bounded originality statement.

## Source-indexed observation and proof access

The SUCC-specific layer is the **source-indexed** structure: which lawful transition was available
to a finite observer, and what it costs. A target's accessibility is a property of a triple
`(Source, Target, Tools)`, classified as **SimpleField / IdealHardField / FuckedField / Unresolved**.

- **[Observer & Proof-Access Foundations](docs/OBSERVER_PROOF_ACCESS.md)** — the four-class taxonomy
  with calibration examples (Kleene-tree IdealHard, noncompact Fucked, phantom source-maps), compact
  gluing, no-ghost Farkas discipline, and the ordinal termination firewall. **RH is left Unresolved,
  not Fucked, pending a theorem.**

## Established vs. open — the research frontier

The reader should see immediately why Poisson summation is settled while Weil positivity is not:

- **[Research Frontier (2026-10-15)](docs/RESEARCH_FRONTIER_2026-10-15.md)** — six tracks from
  carrier algebra through the signed-Weil/Suzuki frontier, each with exact scope and status.
- **[Research Dependency DAG](docs/SUCC_RESEARCH_DEPENDENCY_DAG.md)** — one proof-dependency graph
  with per-arrow status (classical / proved / exact model / implementation / unverified / refuted);
  the firewall line marks exactly where RH sits.

Classical reconstructions (group completion, localization, profinite/CRT limits, completion, adèles,
Pontryagin duality, adelic Poisson, idelic Mellin) are **closed** and realized exactly. SUCC's own
contributions are the typed certificate schema, the proof-access taxonomy, the no-ghost gluing, and
the exact finite source charts with preserved counterexamples. The **downstream Tate/Weil/RH**
application has scoped high-subspace and short-window positivity results, but the low Schur sign, the
low/high resolvent coupling, the `λ↓0` behaviour, and the source→Weil typed morphism remain **OPEN**.

## Run it

Python **3.10+**. The causal, logical, exact-arithmetic and finite-qubit cores are standard-library
only; the mathematical experiments use `mpmath`, and the Black Sun numerical campaign uses `numpy`.

~~~sh
git clone https://github.com/femboy2112/SUCC.git
cd SUCC
python -m pip install -e ".[test]"
python scripts/verify_provenance.py                       # SOURCE_PROVENANCE_VERIFIED, truth:false
python -m unittest discover -s tests -p 'test_*.py'       # full suite; current counts in round receipts
python -m observational_succ demo
python scripts/observer_foundations_probe.py              # finite survival ≠ universal proof
python scripts/ordinal_succ_report_probe.py               # positive-definiteness NOT proved
~~~

The package is **observational_succ**; it has no runtime dependency on any RH repository, and the
general carrier/observer mathematics runs without importing RH code. The `scripts/` tree holds many
further probes (carrier, Tate, Pontryagin, field-trichotomy, Suzuki); each dedicated receipt is
re-checked in its own CI workflow.

## Read the theory

1. **[Foundations](docs/FOUNDATIONS.md)** — physical/semantic proposal, precise types, causal SUCC,
   ordinals, Gödel/Turing, and the difference between reporting and proof.
2. **[Development method](docs/METHOD.md)** — the steelman → crucible → verdict loop that turns
   proposals into ledger-labeled claims.
3. **[Research architecture](docs/ARCHITECTURE.md)** — the general theory vs. the optional RH
   adapter, and how modules cross trust boundaries.
4. **[Carrier Atlas](docs/CARRIER_ATLAS.md)**, **[Observer & Proof Access](docs/OBSERVER_PROOF_ACCESS.md)**,
   **[Research Frontier](docs/RESEARCH_FRONTIER_2026-10-15.md)**,
   **[Dependency DAG](docs/SUCC_RESEARCH_DEPENDENCY_DAG.md)**, **[Claim Index](docs/CLAIM_INDEX.md)**.
5. **[Claim ledger](docs/CLAIM_LEDGER.md)** · **[Roadmap](docs/ROADMAP.md)** ·
   **[Source provenance](provenance/README.md)** · **[RH outbound handoffs](docs/RH_HANDOFF.md)**.

## Historical source and future exchange

This repo was launched after an extensive program in
[femboy2112/FuckingRH](https://github.com/femboy2112/FuckingRH), pinned to
[commit ba075348](https://github.com/femboy2112/FuckingRH/commit/ba075348b7bcc66d938b3e0ca96c26e95bba340a).
The [manifest](provenance/IMPORT_MANIFEST.json) records exact original/destination Git blob
identities for 72 historical artifacts (55 mechanically namespaced Python files, 17 unchanged
documents). New work belongs here first; when it yields an independently meaningful RH-related
theorem, export a self-contained, status-labeled, adversarially tested handoff rather than quietly
converting general observational insight into an RH proof claim.

## Research history (consolidation audits)

The project has been consolidated in documented waves, each preserving its results, status labels,
and counterexamples — nothing is discarded:

- [Integration audit 2026-10-11](docs/INTEGRATION_AUDIT_2026-10-11.md) (PRs #6–#22) ·
  [Gaussian-moat swarm](docs/GAUSSIAN_MOAT_SWARM_AUDIT_2026-10-12.md) ·
  [Moonshot swarm](docs/MOONSHOT_SWARM_AUDIT_2026-10-12.md) ·
  [Third moonshot swarm](docs/MOONSHOT_SWARM3_AUDIT_2026-10-12.md)
- [Many-worlds swarm 2026-10-13](docs/MANY_WORLDS_SWARM_AUDIT_2026-10-13.md) ·
  [Cambrian campaign](docs/CAMBRIAN_CAMPAIGN_2026-10-13.md) ·
  [SUCC Mathematical Atlas](research/2026-10-13/SWARM_ATLAS/SUCC_MATHEMATICAL_ATLAS.md)
- [Phoenix II 2026-10-14](docs/PHOENIX_II_INTEGRATION_AUDIT_2026-10-14.md) (PRs #57–#99)
- **[Academic Main 2026-10-15](docs/ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md) (PRs #101–#131)**
  — this consolidation: the carrier-first academic layer above, 4338 tests, firewall intact.

Public repository does not imply unlimited redistribution rights; no license is added absent the
maintainer's explicit choice.
