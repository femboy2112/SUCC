# Mathematical Memory — front page

**What this is.** A cross-topic *discovery layer* for all SUCC mathematics: it makes results recoverable and sources checkable without re-excavating megabytes of branches. It does **not** replace the canonical record ([`docs/CLAIM_LEDGER.md`](../CLAIM_LEDGER.md), [`docs/CLAIM_INDEX.md`](../CLAIM_INDEX.md), [`docs/CLAIM_NAMESPACE_REGISTRY.json`](../CLAIM_NAMESPACE_REGISTRY.json), the categorical observer atlas, the RH property graph) and it **certifies no proof** — statuses live in the supplements, proofs in the dossiers/Lean.

**Firewall (always true until an independent proof says otherwise).** π base-16 **and** base-3 normality are **OPEN**; the only signed real estimate is `∀ h≠0: Σ_{n≤N} e(h U_n) = o(N)` — where `e(x) := exp(2πix)` and `U_n = 16^{n−1}π − T_n` is the **real** four-pole orbit whose fractional part carries the base-16 digits (**not** an integer carry-recursion, for which the sum is trivially `N`) — on the authentic four-pole source. It is an **UNPROVEN required cancellation, not an existing bound**. RH is **OPEN**. 2-adic Haar, moving-CRT energy, Oily packet covariance, log-germ coefficients, rank-r bulk, certified digit handles, and solenoid equivalences are **not** that estimate.

## Start here (routing)

| You want… | Go to |
|---|---|
| The corrected original intuition (circle→line→triangle; φ⁻¹ vs γ; Ω) and the three distinct φ-lineages | [FAREY_GAUSS_GOLDEN_GAMMA_GENESIS.md](../../research/2026-10-27/FAREY_GAUSS_GOLDEN_GAMMA_GENESIS.md) + [TOPIC_ATLAS.md](TOPIC_ATLAS.md) §Genesis |
| A machine-readable typed concept graph (48 referents, 56 typed relations) | [RELATION_GRAPH.json](RELATION_GRAPH.json) (lint: `scripts/verify_math_memory_graph.py --path …`) |
| An exhaustive index of every claim row (1876 rows, path/line/SHA; 176 registered namespaces, 1863 registered rows) | [CLAIM_CATALOG.json](CLAIM_CATALOG.json) (build: `scripts/build_math_memory.py --write/--check`) |
| Historical theorem IDs, proof status, counterexamples | [CLAIM_LEDGER.md](../CLAIM_LEDGER.md) + [CLAIM_INDEX.md](../CLAIM_INDEX.md); FQIDs via [CLAIM_NAMESPACE_REGISTRY.json](../CLAIM_NAMESPACE_REGISTRY.json) |
| The true open-PR ancestry (who descends from whom; what is stale) | [SUCC_MAIN_XII_FRONTIER_ANCESTRY_DAG.md](../../research/2026-10-27/SUCC_MAIN_XII_FRONTIER_ANCESTRY_DAG.md) |
| Which supplements are registered vs. flagged, and why | [REGISTRY_RECONCILIATION_2026-10-27.md](REGISTRY_RECONCILIATION_2026-10-27.md) |
| Domain atlases + natural-language query crosswalk | [TOPIC_ATLAS.md](TOPIC_ATLAS.md) |
| The schema and proof-authority contract | [SCHEMA.md](SCHEMA.md), [START_HERE.md](START_HERE.md) |

## How to query

1. **Vague phrasing** ("that lattice that zoomed out into a Yoneda point") → [TOPIC_ATLAS.md](TOPIC_ATLAS.md) §Natural-language aliases → a concept node (`MM-*`) or claim family.
2. **Concept node** `MM-*` in [RELATION_GRAPH.json](RELATION_GRAPH.json) → its `provenance` (PR + head SHA + path) and its typed edges (`reduces_to`, `does_not_imply`, `candidate_bridge`, …).
3. **Exact claim ID** (e.g. `CAR-07`, `SB-3`) → [CLAIM_CATALOG.json](CLAIM_CATALOG.json) for path/line/SHA → the supplement/dossier → the Lean receipt if any.

Relation-label discipline: `reduces_to`/`depends_on` = proved implication with stated hypotheses; `does_not_imply` = refutation with a counterexample; `candidate_bridge` = unproved proposal; `shares_value_with` = equal scalar only (not a common source); `shares_source_with` = common source passport only. An equivalence is **not** a proof of either side.
