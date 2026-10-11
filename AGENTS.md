# Instructions for researchers, maintainers and coding agents

**Mission:** Develop Observational SUCC as a freestanding mathematical and physically motivated theory. Its underlying research question is how finite embodied observers construct knowledge from causal interactions. RH is a downstream application, not the definition of the theory.

## Mandatory research discipline

1. Work on non-main branches; use draft PRs. Do not merge, tag, release, publish or change historical defaults without explicit maintainer authorization.
2. Before modifying an imported theorem or code path, inspect provenance/IMPORT_MANIFEST.json, the frozen source dossier and exact originating Git commit. Never rewrite the preserved archival originals.
3. Keep the author's physical-carrier and semantic intuition separate from model interpretation and existing classical theorems. No claim that Hilbert > integers, that actual human brains perform these computations, or that finite observations entail universal proofs.
4. Every meaningful claim must have: domain, definitions, hypotheses, quantifiers, status label, supporting derivation or test, provenance, adversarial countermodels, and a next falsification opportunity.
5. Distinguish observed events from predictions, mathematical truth from provability, finitary proof from \(\omega\)-rule, and colimits from actual infinite elapsed computation.
6. Positive physical/semantic covariances are not automatically source-derived positive Weil forms. Never silently assert the missing identification.
7. For RH work, require original prime-power/source data, completed Gamma/pole, valid test-function domains, correct half-density/conductor/phase, fake composite and matched non-Euler controls, and **no nontrivial zero positions as construction inputs**.
8. Finite numerical precision is not a proof certificate unless backed by independently derived rigorous error bounds or sound interval arithmetic. Do not invent results or claim CI passes before it does.
9. Preserve test history and regression cases. A newly proposed diagram must be checked at the level of actual maps, coherence laws and failure modes; a visually attractive analogy is not a theorem.
10. Public repository does not imply unlimited redistribution rights. Do not add a license absent the maintainer's explicit choice.
11. Develop proposals through the steelman–crucible–verdict method in docs/METHOD.md: reconstruct the strongest faithful reading, test it adversarially with a receipt (a counterexample, a cited theorem, a ledger REFUTED entry, or a typed contradiction), and record a labeled verdict. A refutation without a receipt, or a status promotion without an independent proof, is not permitted.

## Required validation

~~~sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

See docs/FOUNDATIONS.md, docs/METHOD.md, docs/CLAIM_LEDGER.md, docs/ARCHITECTURE.md, docs/ROADMAP.md and docs/RH_HANDOFF.md.
