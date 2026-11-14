# Validation and proof-authority boundary — Lawful Probe Budget

**Date:** 2026-11-14 · **Python:** 3.13.5 · **Location:** isolated local source scaffold, NOT a full SUCC checkout. No new Lean proof or physical experiment has been performed.

## Actual commands and receipts

| Command | Observed result | Receipt |
|---|---|---|
| `PYTHONPATH=. python -m unittest discover -s tests -p 'test_probe_budget.py' -v` | **19 test methods, 18 PASS, 1 SKIP** (cross-check against inherited source module unavailable in the isolated scaffold) | `receipts/focused_tests.log` |
| `PYTHONPATH=. python research/2026-11-14/probe_budget/independent_oracle.py` | **PASS**: 320 randomized finite carriers fixed-budget comparisons, 250 adaptive valuations independently reproduced via budget-decreasing policy recursion, 70 losing-trap models rejected for budgets 0–6, 3 strict adaptive improvements; exact source upgrade costs 2 and 5 recovered | `receipts/independent_oracle.json` |
| `python -m compileall -q observational_succ/probe_budget.py tests/test_probe_budget.py research/2026-11-14/probe_budget/independent_oracle.py` | PASS | command exit 0 |
| Exhaustive 3-state one-generator source/report quotient test in focused suite | **279** compatible tables, **24** no equivariant stochastic lift; independent exact implementation reproduces #626's earlier census | focused test `test_small_exhaustive_stochastic_quotient_census_replays_626` |

The one initial test failure was a **false assertion in the test specification**, not a source-model contradiction: it incorrectly equated existence of a mathematically valid point section under identity dynamics with actual source identification. The second initial test failure exposed a **real conjecture defect** in a four-state proposed stochastic-only upgrade: a deterministic singleton intermediate could not feed a nontrivial two-cycle with the stationary uniform distribution. We replaced it with the six-state twin-predecessor construction; the corrected paper proof, solver and holdouts agree. Both errors are preserved here, rather than silently treating the first run as green.

## Scope of checks

The Python library contains three exact procedures: finite weighted pair-cover; a single-copy belief-state AND/OR reachability game with certified policy or adversarial losing region; and exact finite point/stochastic T-compatible section feasibility under each jointly accessible passive-report refinement.

Tests include: cheapest fixed vs adaptive, target identification vs source identification, explicit absence of an unauthorized hidden-ID probe, destructive probe refusal as passive, destructive single-copy no-go, source-history loss after merging, noncongruent report action, nonmonotone reverse lifting, two-stage 6-source costs 2/5, identity dynamics with representative but no knowledge, finite G-orbit uniform stochastic only, exact 3-state census, false optimality mutations, and size-limit exceptions.

**Crucial proof boundary:** Exact LP vertex enumeration, minimax AND/OR solver, and source-action congruence are mathematical algorithms over fully specified finite tables. Executing them is *not* certification that a real physical device offers that readout, that such a readout is nondisturbing, or that an assigned probability is a Bayesian posterior. `available=True` means in-menu mathematical availability only.

**Independent route:** the separate oracle does not use the program's Bellman values when assessing individual budgets. It tests a brute `solves(belief, remaining_cost)` predicate with decreasing budget and compares minimal feasible integers; its fixed-probe selection also independently enumerates candidate sets. The source data and test generator are shared, so this is an independent algorithmic comparison **not** an independent source-model witness or academic peer review.

**Unrun or pending upon authoring:** full native `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/verify_provenance.py`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`, and hosted CI on the final GitHub SHA. On a complete PR checkout the 19th test imports `observational_succ.equivariant_choice` from #626 to cross-check feasible/unfeasible lifts; that branch-dependent test was SKIPPED in isolation, and its future hosted result must be read from GitHub.

## Claim ledger

- PB-01: elementary/classical theorem (minimum fixed budget = weighted pair-cover), paper proof; NP-hardness by explicit reduction to known set-cover.
- PB-02: elementary/classical finite resource-game theorem, paper proof and separately validated certificates.
- PB-03: classical quotient congruence condition, exact model witnesses.
- PB-04: finite rational LP/exhaustive optimization proof, independent small-case census only.
- PB-05/PB-06: specific exact algebraic source countermodels, tested every source/readout assignment within the prescribed menus.
- PB-07/PB-08: exact logical distinction (mathematical representative vs actual ID, current state vs source history).
- PB-09: OBSERVED finite code/test evidence; not a proof of any general mathematical extension beyond paper scope.
- PB-10: OPEN—calibrated posterior and stochastic outcomes / empirical source authentication.

**Main is unchanged.** No π-normality, RH, physical general relativity, omniscient observer, source-derived prior, full category theory or algorithmic efficiency proof is claimed.
