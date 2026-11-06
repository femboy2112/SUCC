# Front B validation index

All commands assume `PYTHONPATH=<repo root>`. Use a Python with `mpmath>=1.3`, and never `python -I`.

| Check | Command | Result (this round) |
|---|---|---|
| Shared framework + CB-1 in the main suite | `python -m unittest tests.test_selected_orbit` | 10 tests OK. Definition path = window path on every admissible triple at `A=64,173`, plus seed `1/5` and a one-pole mutant. |
| Admissibility law `A≥2^{2d−3}` | `python research/2026-11-05/main_xx_forge/front_b/admissibility_law.py 200` | `CERTIFIED-FINITE`, 0 exceptions for `2≤d≤200`. `r` decreasing for `m≥2` is checked symbolically. 35 s. |
| Two independent oracles (CB-1, CB-1g, J, CB-3, J2) | `cd numerics && python -m unittest test_carry_transport` and `python carry_transport_probe.py --stage all` | 13 tests OK (1.8 s). Full stage outputs and runtimes are in `numerics/VALIDATION.md`. |
| CB-1 exact | `numerics` stage `cb1` and `edge` | 591,175 admissible cases with 0 mismatches in either oracle and 0 cross-oracle disagreements. The edge stage reaches `1−S_d=1.07e-4` with 0 mismatches. The first inadmissible depth fails, as it should. A negated-forcing control fails on 50,524 cases. |
| CB-1g exact | `numerics` stage `cb1g` | 118,235 admissible cases, 0 mismatches by two z-routes. Minimum endpoint margin `1.07e-5`. The wrap case (`S_d<1≤16^dT_n`) occurred 0 times. |
| Third cross-check | `numerics` stage `third` | `observational_succ.selected_orbit` agrees with oracle B on all 82 (cell, triple) comparisons. |
| CB-3 construction and sweep | `numerics` stages `cb3`, `j2` | Calibration residual `9e-60`; `p_0=1/16` exactly. Exact `max|E J|≤2.7e-7`. Witness `f1−f2=0.0098±0.0007` against iid null `0.0002±0.0005` at `N=262144`. `J2` exact expectation `≈1.44e-5`, flat in `A`. |
| Hostile review | `hostile_review/` | Rigor audit (BLOCK-narrow, all repaired) and refuter (all core claims SURVIVED, 2 tombstones corrected); see `hostile_review/REVIEW.md`. |

**Not covered:**
- exact CB-1/CB-1g above `A=4096`;
- irrational seeds other than `0` and `s_*`;
- `J2` beyond three representative triples and `ℓ≤3`;
- `d>200` for the admissibility law.

numpy RNG streams for the CB-3 sequences depend on the numpy version (2.5.4 here). The exact-expectation numbers do not.
