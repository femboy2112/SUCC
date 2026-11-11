# Main XXIV — source and signed-statistics entrypoint

[Canonical frontier](../PI_NORMALITY_FRONTIER.md) · [next theorem](../MAIN_XXIV_HANDOFF.md) · [exact contribution manifest](../SUCC_MAIN_XXIV_INTEGRATION_MANIFEST_2026-11-11.json) · [governing claims](../CLAIM_SUPPLEMENT_MAIN_XXIV.md) · [research history](../RESEARCH_HISTORY.md). The single generated catalog below is rebuilt from the integrated tree. Catalog rows are discovery metadata, not proof authority. Source-selected cancellation, parity, pi normality and RH remain OPEN. Historical catalog counts and integration announcements below describe their dated snapshots.

# Mathematical Memory — front page

**What this is.** A cross-topic *discovery layer* for all SUCC mathematics: it makes results recoverable and sources checkable without re-excavating megabytes of branches. It does **not** replace the canonical record ([`docs/CLAIM_LEDGER.md`](../CLAIM_LEDGER.md), [`docs/CLAIM_INDEX.md`](../CLAIM_INDEX.md), [`docs/CLAIM_NAMESPACE_REGISTRY.json`](../CLAIM_NAMESPACE_REGISTRY.json), the categorical observer atlas, the RH property graph) and it **certifies no proof** — statuses live in the supplements, proofs in the dossiers/Lean.

**Firewall (always true until an independent proof says otherwise).** π base-16 **and** base-3 normality are **OPEN**; the only signed real estimate is `∀ h≠0: Σ_{n≤N} e(h U_n) = o(N)` — where `e(x) := exp(2πix)` and `U_n = 16^{n−1}π − T_n` is the **real** four-pole orbit whose fractional part carries the base-16 digits (**not** an integer carry-recursion, for which the sum is trivially `N`) — on the authentic four-pole source. It is an **UNPROVEN required cancellation, not an existing bound**. RH is **OPEN**. 2-adic Haar, moving-CRT energy, Oily packet covariance, log-germ coefficients, rank-r bulk, certified digit handles, and solenoid equivalences are **not** that estimate.

## Start here (routing)

| You want… | Go to |
|---|---|
| The corrected original intuition (circle→line→triangle; φ⁻¹ vs γ; Ω) and the three distinct φ-lineages | [FAREY_GAUSS_GOLDEN_GAMMA_GENESIS.md](../../research/2026-10-27/FAREY_GAUSS_GOLDEN_GAMMA_GENESIS.md) + [TOPIC_ATLAS.md](TOPIC_ATLAS.md) §Genesis |
| A machine-readable typed concept graph (51 referents, 60 typed relations) | [RELATION_GRAPH.json](RELATION_GRAPH.json) (lint: `scripts/verify_math_memory_graph.py --path …`) |
| Claim-row discovery catalog (2055 rows; 179 namespaces, 1921 registered rows; inherited unregistered research IDs retain warnings) | [CLAIM_CATALOG.json](CLAIM_CATALOG.json) (build: `scripts/build_math_memory.py --write/--check`) |
| Historical theorem IDs, proof status, counterexamples | [CLAIM_LEDGER.md](../CLAIM_LEDGER.md) + [CLAIM_INDEX.md](../CLAIM_INDEX.md); FQIDs via [CLAIM_NAMESPACE_REGISTRY.json](../CLAIM_NAMESPACE_REGISTRY.json) |
| Current integration ancestry and historical branch dispositions | [Main XXII manifest](../SUCC_MAIN_XXII_INTEGRATION_MANIFEST_2026-11-09.json); the Main XII DAG below is historical |
| Which supplements are registered vs. flagged, and why | [REGISTRY_RECONCILIATION_2026-10-27.md](REGISTRY_RECONCILIATION_2026-10-27.md) |
| Domain atlases + natural-language query crosswalk | [TOPIC_ATLAS.md](TOPIC_ATLAS.md) |
| The schema and proof-authority contract | [SCHEMA.md](SCHEMA.md), [START_HERE.md](START_HERE.md) |

## How to query

1. **Vague phrasing** ("that lattice that zoomed out into a Yoneda point") → [TOPIC_ATLAS.md](TOPIC_ATLAS.md) §Natural-language aliases → a concept node (`MM-*`) or claim family.
2. **Concept node** `MM-*` in [RELATION_GRAPH.json](RELATION_GRAPH.json) → its `provenance` (PR + head SHA + path) and its typed edges (`reduces_to`, `does_not_imply`, `candidate_bridge`, …).
3. **Exact claim ID** (e.g. `CAR-07`, `SB-3`) → [CLAIM_CATALOG.json](CLAIM_CATALOG.json) for path/line/SHA → the supplement/dossier → the Lean receipt if any.

Relation-label discipline: `reduces_to`/`depends_on` = proved implication with stated hypotheses; `does_not_imply` = refutation with a counterexample; `candidate_bridge` = unproved proposal; `shares_value_with` = equal scalar only (not a common source); `shares_source_with` = common source passport only. An equivalence is **not** a proof of either side.

## Operation Main XXII — current entrypoint

[Current frontier](../PI_NORMALITY_FRONTIER.md) · [integration audit](../SUCC_MAIN_XXII_INTEGRATION_AUDIT_2026-11-09.md) · [scoped claims](../CLAIM_SUPPLEMENT_MAIN_XXII.md) · [typed Gamma observables](../MAIN_XXII_GAMMA_OBSERVABLES.md). Original-zero parity contrast is OPEN, as are full pi normality and RH. The research-local dossiers remain discoverable through the history index; catalog registration is not proof authority.

**Causal-weld / Cayley follow-up:** [entrypoint](../../research/2026-11-09/cayley_source_observer/README.md),
[local claims](../../research/2026-11-09/cayley_source_observer/CLAIM_LEDGER.md), and
[errata](../../research/2026-11-09/cayley_source_observer/ERRATA.md).
Exact projective observation, coupled source clocks, a common-horizon mean
certificate and conditional parity-future fairness are separated from the
still-open selected signed estimate. The causal-weld semantic repairs do not
certify a full C-monoid or a faithful BBP compiler. Local CAY/CBO/CS labels do
not mint historical theorem namespaces.

## Operation Main XIX — angular / Laurent-clock frontier (2026-11-01)

[Integration index](../../research/2026-11-01/main_xix/MAIN_XIX_CLAIM_REGISTRY.md) · [architecture](../../research/2026-11-01/main_xix/MAIN_XIX_ARCHITECTURE.md) · [provenance DAG](../../research/2026-11-01/main_xix/MAIN_XIX_PROVENANCE_DAG.md) · [validation](../../research/2026-11-01/main_xix/MAIN_XIX_VALIDATION.md) · [handoff](../../research/2026-11-01/main_xix/MAIN_XIX_HANDOFF.md). Integrated three ancestry-minimal leaves (PRs #437, #452, #455) subsuming #437–#455; firewall intact, nothing promoted. The central result is the **all-order Laurent-clock sharpness theorem**: for the same four-pole forcing but the distinct real counterseed `s_*=−π/16` (`U_n(s_*)=−T_n`, completed point 0, nonnormal, not in the original rational-state register), every fixed `d≥1`, `h≠0`, `d+1<c<d+2`, `K_N=⌊c·log_16 N⌋` gives `L^C→1`, `L^[d]→2(d+1)/c−((d+1)/c)²`, defect `(1−(d+1)/c)²>0` — recovering Main XVIII's `d=1` barrier `1/25` and extending it to every order. This is a **seed-uniform transport-precision barrier (a negative result)**, not a source-selected impossibility theorem and **not** progress on `o(N)`. The carrier-relative entropy ⇔ normality statement is a reformulation; the resolution ceiling `D_{N,k}≥log(M/N)` refutes only the naive one-resolution entropy→Fourier certificate. Research-dir prefixes (FP/AC/CH/CSG/CRE/LCS/…) stay local by design and mint no registry namespace. **The selected signed estimate, π base-16/base-3 normality, and RH remain OPEN.**

## Operation Main XVIII — signed-lag frontier (2026-10-31)

[Integration index](../../research/2026-10-31/main_xviii/MAIN_XVIII_CLAIM_REGISTRY.md) · [architecture](../../research/2026-10-31/main_xviii/MAIN_XVIII_ARCHITECTURE.md) · [provenance DAG](../../research/2026-10-31/main_xviii/MAIN_XVIII_PROVENANCE_DAG.md) · [validation](../../research/2026-10-31/main_xviii/MAIN_XVIII_VALIDATION.md) · [handoff](../../research/2026-10-31/main_xviii/MAIN_XVIII_HANDOFF.md). Integrated four leaves (PRs #426, #430, #432, #435) subsuming #426–#435; firewall intact, nothing promoted. The time-correlated signed observable `L_(N,K)(h)=(2/KN)Σ_(k<K)(1−k/K)Re Σ_(n≤N−k) e(h(16^k−1)U_n)` gets a certified source-transport error at `K=⌊log_4 N⌋` and a two-scale **gate equivalence** (original ⇔ doubled-clock criterion within the BBP forcing family) — a criterion, **not** progress on `o(N)`. A sharp hostile barrier `(1−2/c)²` and two nonnormal families (dyadic near-zero seeds; prime-smooth `q=3^a5^b`, spectrum `1_((q/15)|h)`) rule out seed-uniform / forcing-only routes; a route using the exact `U_0=0` boundary is not excluded and is the open frontier. Research-dir prefixes (CT/TWTH/CP/HP/TD) stay local by design and mint no registry namespace. **The selected signed estimate, π base-16/base-3 normality, and RH remain OPEN.**

## Operation Main XVII — carrier & selected-arithmetic frontier (2026-10-31)

[Integration index](../../research/2026-10-31/main_xvii/MAIN_XVII_CLAIM_REGISTRY.md) · [architecture](../../research/2026-10-31/main_xvii/MAIN_XVII_ARCHITECTURE.md) · [provenance DAG](../../research/2026-10-31/main_xvii/MAIN_XVII_PROVENANCE_DAG.md) · [selected-arithmetic attack](../../research/2026-10-31/main_xvii/MAIN_XVII_SELECTED_ARITHMETIC.md). Merged the 35 open research PRs #390–#424 (13 leaves) as a typed carrier stack; firewall intact, nothing promoted. The new sub-result NET-XVII-1 (`Ẽ_p(h) ≥ 1 − (√p+2)/(L−1)`, subgroup/Gauss bound) is a *primary-only* per-window saving — **not** a saving on the full window sum, on dyadic blocks, or on `o(N)`. These supplements are scoped research and mint no registry namespace by design (their internal IDs — PIG/BC/CQ/NWR/RS/FEO/CAT/UZ/DY/SA/FB/MS/CTC/… — stay local, like the prior π-frontier rounds).

## Lonely Runner exact-certificate campaign (2026-10-28)

[Research entry](../../research/2026-10-28/lonely_runner/README.md) and
[LRN local claims](../CLAIM_SUPPLEMENT_LONELY_RUNNER.md): classical deleted-speed
corollary and sharp equality cases; independently checked rational circle
covers; exact finite characterization and bounded search for local uniform
replacement rules; polynomial two-entry growth bounds. Full universal Alpha
metric, upper-half one-insertion hole and real cover-chain soundness have distinct kernel receipts; local-rule
and analytic growth results are paper proofs. Academic novelty remains separate
from those proof statuses. Existing source and theorem namespaces are unchanged.

The same campaign also proves fixed-support affinization of arbitrary phase
schedules and the sharp no-saving obstruction for one affected odd part.
These compactness and endpoint-capacity results are paper proofs, with exact
controls and explicit phase-identity countermodels.

The [referee child campaign](../../research/2026-10-28/lonely_runner/referee/README.md)
adds a complete elementary unrestricted quadratic growth argument, an exact
census through n30, and actual-source upper-half cubic Lean authority. These
are distinct scopes; see [LRF claims](../CLAIM_SUPPLEMENT_LONELY_REFEREE.md).
Academic priority and external peer acceptance remain unverified.

## Carry, Pólya and original-source resolvent child (2026-10-28)

[Results and proof boundaries](../../research/2026-10-28/CARRY_POLYA_SOURCE_LOCKED_SUMMARY.md)
and [CPS research-local claims](../CLAIM_SUPPLEMENT_CARRY_POLYA_RESOLVENT.md):
sharp signed divisor-boundary identity and absence of a uniform origin-pinned
spectral gap; minimal fourth-order original-BBP zeta response; minimal coherent
Pólya environment and universal leakage spectrum. Typed nodes `MM-CPS-1` through
`MM-CPS-3` lead to the three dossiers. Nine limited finite-algebra Lean declarations
are separated from paper analytic/spectral proofs. Historical FQIDs are unchanged;
the regenerated catalog intentionally retains warnings for unregistered research
supplements. **Selected signed BBP cancellation, π normality and RH remain OPEN.**

## Operational triangle / Triangle Genesis (2026-10-29, Operation Main XV)

The **operational triangle** is SUCC's formal observer apparatus: finite-path/source update →
superposed endpoint with retained posterior → typed observation/selection. Apparatus interface
`docs/OPERATIONAL_TRIANGLE.md`; frontier dossiers
`research/2026-10-29/operational_triangle_frontier/` (`THEOREMS.md`, `CLAIMS.md` TG-01–TG-10,
`ORIGINAL_TRIANGLE_PROVENANCE.md`). The author's Harmonic / Golden-ratio / Euler–Mascheroni
triangle and Oily–Macaroni (`Omega_OM = phi^{-1}-gamma`) are the preserved rank-two
(`r=2, theta=1`) specialization, with naming provenance in
`research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md` (PR #365). The prime-ladder
transcendence→entropy bridge (PR #334 R4/R5) is **REFUTED as a general bridge** by the Kempner
firewall (PR #337). Research-draft `TG-` labels are intentionally kept out of the historical FQID
namespace. **Selected signed BBP cancellation, π base-16/base-3 normality and RH remain OPEN.**

**Operation Main XVI (2026-10-29) repair & advance** — `research/2026-10-29/triangle_genesis_repair/`:
corrected the Weyl normalization (gate `T_N=o(N) ⇔ Sbar_N=o(1)`; `Sbar_N=o(N)` vacuous); **proved
the golden locus** `q_(r,theta)=lambda^r ⇔ theta=lambda/(1-lambda^r)` with restricted uniqueness
`theta=1 ⇒ r=2` (TG-11, supersedes "agree only at `(2,1)`"); classified the seven seed-alias classes
with a corrected control slate (TG-12); and proved the literal-carry obstruction (TG-13, distinguishes
aliases but no `|T_N|` saving). Regression `tests/test_triangle_genesis_repair.py`. Firewall unchanged.
