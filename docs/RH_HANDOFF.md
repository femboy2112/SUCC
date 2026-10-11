# Exporting genuine ObsSUCC results to RH repositories

Observational SUCC is a **source of independent mathematics**, not a satellite repo whose purpose is to solve RH. This protocol preserves that independence while allowing mathematically useful discoveries to travel to [femboy2112/FuckingRH](https://github.com/femboy2112/FuckingRH) and any other RH research repositories.

## When an RH handoff is justified

Prepare an outbound handoff only when a concrete lemma, construction, certificate, negative control or quantified obstruction makes a real difference to a specified RH proof obligation. An analogy, generic Hilbert positivity, a source-blind numerical fit, and a proof-equivalent reformulation are not automatically proof progress.

The handoff must state:

1. **A precise theorem or experimental statement**: objects, domains, parameters, hypotheses, quantifiers and sign/continuity conditions.
2. **Research status**: CLASSICAL / PROVED LOCAL / TESTED MODEL / HYPOTHESIS / UNVERIFIED / REFUTED, and a separate explicit line “RH PROVED: no” unless it truly is proved.
3. **Origin and authorship**: exact originating SUCC commit SHA, source paths and mathematical primary references.
4. **Construction method**: distinguish real Euler, fake source, proper conductor/Gamma, half-density, prime phase and all analytic boundary terms. **Do not read nontrivial zero locations during construction**.
5. **What changes**: whether the result is a new lemma, a necessary condition, a no-go, a certified finite evaluator or just a useful coordinate.
6. **Controls**: fake composite at 6, changed prime weight and log phase, wrong half-density, matched Euler/Hecke and non-Euler Davenport–Heilbronn when relevant, and a sufficient uncertainty/error specification.
7. **Reproduction**: zero-independent code, exact or rigorous interval certificates, independent numerical calibration and a reproducible CI link.
8. **Missing theorem**: what remains before a valid global Weil-positive conclusion would follow; no circular sign assumptions.

## Approval and versioning

Write the self-contained handoff in handoffs/rh/NNNN-title.md on a research branch. Link it from handoffs/rh/README.md and the claim ledger. A native SUCC PR should validate it. After review, open a **separate** issue or PR in the RH repo (or explicitly send the handoff) instead of silently pushing into an unrelated RH branch. The RH maintainer decides integration. If an RH branch uses the result, add a cross-link and exact source version here.

Do not merge RH’s unfinished experimental branches into the core ObsSUCC public API. Do not claim the new repository inherits RH’s theorem authority merely by having imported its laboratory code.

## Current first handoff

The first candidate is the rigorous **finite prime-side Suzuki interval** from source_prime_certificates.py: authentic Dirichlet-log prime wavefront, exact rational log/sqrt error enclosures and a strictly negative fake-six source delta. This is a **valid finite arithmetic source instrument**. It is **not** a completed Gamma/pole/Weil kernel and not an RH proof.

Read [the initial handoff](../handoffs/rh/2026-10-10-prime-source-certification.md) or use [the handoff template](../handoffs/rh/TEMPLATE.md).
