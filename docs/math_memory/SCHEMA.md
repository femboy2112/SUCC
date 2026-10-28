# Mathematical-memory schema and proof-authority contract

This directory is an **AI/human discovery layer**, NOT a second canonical theorem registry. Historical authority remains docs/CLAIM_LEDGER.md, docs/CLAIM_INDEX.md, docs/CLAIM_NAMESPACE_REGISTRY.json, source/provenance manifests, original dossiers and actual Lean/kernel/CI receipts.

## Machine relation graph: RELATION_GRAPH.json

Each MM- entry identifies a **memory referent**, not a historical theorem ID: intuition, theorem, defined comparison, conjecture, counterexample or open obligation. Required fields: id, title, statement, kind, status, scope, limitation, next_probe, typed provenance with GitHub PR head SHA and repo path where available.

Edges are typed and evidence-bearing:
- depends_on: from dependent to prerequisite, acyclic, actual hypothesis/derivation required
- reduces_to: exact reduction and declared hypotheses
- does_not_imply: negative result with counterexample
- candidate_bridge: unproved transport/map proposal
- shares_value_with: two scalar values agree, not a common source or isomorphism
- shares_source_with: real common source passport but not independent characters
- formalizes, motivates, specializes, generalizes, complements, constrains: descriptive not proof promotions.

Validator scripts/verify_math_memory_graph.py checks source pin structure, allowed statuses/relations, endpoints and logical dependency cycles, **not** the mathematical truth of a paper result or remote branch state.

## Deterministic whole-checkout claim catalog

Run these commands on the actual target branch after integrating the chosen research paths:

    python scripts/build_math_memory.py --write
    python scripts/build_math_memory.py --check

The resulting docs/math_memory/CLAIM_CATALOG.json records ALL current worktree docs/CLAIM_SUPPLEMENT_*.md table ID rows, stable FQID using the existing registry by file and bare prefix, original bare ID, exact source path/line, raw row, SHA-256 per document, and checked-out research/handoffs/formal Markdown/Lean document names and hashes.

Its status field explicitly remains UNCLASSIFIED_RAW: parsing a row does NOT certify its proof. A missing registered source or unregistered/ambiguous bare prefix is a warning that Claude must resolve against historical provenance; the script never invents namespace aliases. Catalog scope is CURRENT_CHECKOUT_ONLY: it does not see unmerged PRs, external documents or archived orphan commits.

## Full integration requirements

For **all actual SUCC mathematics**, Claude must enumerate every reachable branch and PR head, compute true Git ancestry, register branch-only dossiers without duplicate theorem IDs, retain all old counterexamples/receipts and source signatures, expand conceptual graph beyond its initial 23 curated nodes/25 relations, and regenerate catalog from the final reviewed integration source. Human topic pages and AI graph must resolve to the same historical proofs. The original BBP signed forcing and zero selector, RH proof contract and old Lean theorem statements are immutable.

Mandatory test gates before merge: AGENTS.md full regression/provenance/observer/ordinal; graph lint; claim-catalog generate/replay; Farey/Gauss interval tests; all source hash and CI/Lean checks on final SHA. Do not call this first-stage research branch full integration.

**Always distinguish** finite-to-global Yoneda/Čech *conditional gluing* from a universal global arithmetic proof, selected real Weyl o(N) from p-adic Haar or source-passive representations, and the different historical origins of phi^(-1)-gamma.