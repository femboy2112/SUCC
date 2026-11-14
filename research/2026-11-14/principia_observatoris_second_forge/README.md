# Principia Observatoris — the Second Forge

**Research package, 2026-11-14. Draft; not merged; changes no ledger entry.** An independent,
constructive ("from the carrier upward") investigation of the founding hypothesis in
[PR #618](https://github.com/femboy2112/SUCC/pull/618): *geometric closeness is relative causal
relevance, and a finite observer may be unable to tell a delayed finite counterexample from an
asymptotically vanishing defect.* It was carried out without contact with the parallel axiomatic
campaign and is prepared for cross-examination against it.

All statements concern declared finite mathematical models. Nothing here is a claim about
physical spacetime, quantum foundations, RH or π-normality, and no scholarly novelty is claimed.

## Read in this order

| Document | Content |
|---|---|
| [FOUNDATIONAL_KERNEL.md](FOUNDATIONAL_KERNEL.md) | the smallest constructive definition of a finite observer; what was deleted and why; premises that records cannot supply |
| [THEOREM_FORGE.md](THEOREM_FORGE.md) | register of every claim: statement, authority, proof location, dependencies |
| [CAUSAL_GEOMETRY.md](CAUSAL_GEOMETRY.md) | quotient geometry over a value structure; structure versus response; balance; gauge; the unseen causal horizon |
| [FINITE_HORIZONS.md](FINITE_HORIZONS.md) | finite-horizon completeness with sharp constants; limit-identifiable but never certified |
| [COUNTERMODELS.md](COUNTERMODELS.md) | every failed conjecture with its receipt |
| [SUCC_INTEGRATION.md](SUCC_INTEGRATION.md) | explicit relationships to existing SUCC structures, by evidence level |
| [PROVENANCE_AND_INDEPENDENCE.md](PROVENANCE_AND_INDEPENDENCE.md) | what was imported, who derived what, what was mechanically checked, adversarial review, receipts |
| [TENACIOUS_D_HANDOFF.md](TENACIOUS_D_HANDOFF.md) | briefing and theorem interoperability contract for the cross-examination |
| [agents/](agents/) | the delegated workstreams' full reports, including the hostile referees' |

## Executable and formal artifacts

| Artifact | What it checks |
|---|---|
| `formal/ObservatorisQuantale.lean` + `scripts/check_observatoris_lean.py` | weighted ancestral theorems, sandwich, adjunction, closure commutation, change of base — Lean 4.14 core, no axioms |
| `observational_succ/observatoris_quantale_quotient.py` | finite value structures, quotients, exactness conditions, ghost defect, coarsest exact refinement |
| `observational_succ/observatoris_response_geometry.py` | signed linear carriers: support, balance, gauge, cones |
| `observational_succ/observatoris_finite_observer.py` | cores, intervention-order horizons, wiring identifiability, single-copy access |
| `observational_succ/observatoris_finite_horizons.py` | recurrences, machines, automata, moduli, learners |
| `observational_succ/observatoris_classical_appearance.py` | independent diagnostics of classical appearance |
| `tests/test_observatoris_*.py` | positive, negative, mutation and holdout tests; exhaustive small-model searches |

```sh
python -m unittest discover -s tests -p 'test_observatoris_*.py'
python scripts/check_observatoris_lean.py        # needs the pinned Lean 4.14 on PATH
```

## The five results to look at first

1. **Observation–dynamics commutation** (kernel-checked): an observer's quotient geometry is
   exact iff "evolve, then blur" is already closed; in general the truth is bracketed by the
   must- and may-quotients.
2. **Ghosts versus quasars:** coarse-graining can only invent causal routes, never hide one;
   a hidden cause needs an omitted edge, and is found by a contrast, not an invariant.
3. **Structure is not response:** balance is exactly what makes them coincide; the unit-free
   content of a carrier and the possibility of cancellation both live on its cycles.
4. **Limit-identifiable, never certified:** with a declared complexity bound a finite record
   settles all future records at an exact sharp horizon; without it the observer converges and
   can never know that it has.
5. **Executable knowledge is not closed under conjunction.**
