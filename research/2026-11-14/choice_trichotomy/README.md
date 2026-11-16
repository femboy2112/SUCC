# Equivariant Choice Trichotomy — SUCC Research Slice

**Date:** 2026-11-14. **Source ancestry:** Principia Observatoris draft #625, which is stacked on #624 and #623. **Research-only**: no source authentication, physical observation, general AoC derivation, π-normality, RH, or general relativity result is claimed.

This package classifies when an observer quotient with a lawful `T`-action has an exact equivariant point section, an equivariant probability-valued section, no such stochastic section, or merely an approximate/inexact relation. It distinguishes an observer's mathematical choice from identification of the actual source history.

**Read:** [THEOREMS.md](THEOREMS.md), then [VALIDATION.md](VALIDATION.md). Run the exact Python model and independent symbolic oracle before claiming a stronger status.

### Particularly important earned distinctions

- For group actions, **point choice** is equivalent to stabilizer fixed points; **stochastic choice** is equivalent to invariant stabilizer measures. Finite fibers always admit the latter, not necessarily the former.
- For general monoid actions, **a finite equivariant quotient can lack even an equivariant stochastic section**. A three-source-state, two-report, one-generator model gives a Farkas contradiction and sharp TV defect `1/2`.
- The canonical full-fiber **set-valued lax lift** always exists under a given equivariant action, but it has no chosen history or normalized probabilities.
- An infinite translation action has no invariant countably additive probability, yet finite uniform windows have exact mismatch `1/(2N+1) → 0`. A fixed finite carrier cannot exhibit an unattained zero minimum; this is the finite/infinite boundary.
- Even an exact forward **Markov quotient** can lack a backward Markov-consistent probabilistic lift; exact stochastic examples demonstrate both directions.

### Files

- `observational_succ/equivariant_choice.py` — exact rational deterministic/stochastic action and Markov quotient checker; proof-witness verifier.
- `tests/test_equivariant_choice.py` — 21 regression methods including mutation, exhaustive small census, group controls, Markov controls and limit defect.
- `research/2026-11-14/choice_trichotomy/independent_sympy_oracle.py` — independent symbolic linear systems for positive and hostile cases.
- `THEOREMS.md`, `VALIDATION.md` and `receipts/` — scoped proofs, environmental and exact test evidence.

### Required next mathematical gates

- Independent review of the finite LP vertex enumeration and Farkas dual.
- Proof-assistant versions of the structural and no-go statements (not checked in this round).
- Authentication of a concrete SUCC source whose actual `T`-action and lawful probes instantiate the abstract kernel.
- Real tests of probe access, disturbance, history retention and source-conditioned posterior law.

This is an additive research fork. Do not merge automatically.
