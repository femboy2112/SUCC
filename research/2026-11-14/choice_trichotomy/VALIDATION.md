# Validation — Equivariant Choice Trichotomy

**Date:** 2026-11-14. **Authority:** exact finite computational checks + separately authored paper derivations. These are NOT an independent physical experiment, a general category-theoretic proof assistant run, or a full SUCC repository test-suite pass.

## Environment and commands actually executed

- Python **3.13.5**, standard-library `Fraction`, `itertools`, and `unittest` for the main source/tests.
- Independent symbolic oracle: SymPy **1.14.0**; defines equations from the example table without importing the implementation under test.
- `python -m unittest discover -s tests -p 'test_equivariant_choice.py' -v`: **23/23 passed**. Raw stderr/stdout retained in `receipts/focused_tests.log`.
- `python research/2026-11-14/choice_trichotomy/independent_sympy_oracle.py`: **PASS** for rational symbolic systems (swap, transient cycle, 3-state no-go, 4-state no-go and exact TV gap); raw log `receipts/independent_sympy.log`.
- `python -m compileall -q observational_succ/equivariant_choice.py tests/test_equivariant_choice.py`: **PASS**.
- Exact independent census generator (recorded in `receipts/exact_census.json`): enumerates every *total source map*, every *surjective q*, and every compatible *total report map* for one generator with source size 2 or 3; all feasible output kernels are rechecked against exact equations.

## Exact findings and hostile controls

- **2 source states, one generator:** 12 equivariant source/report tables, zero lacking a stochastic section.
- **3 source states, one generator:** 279 tables; **24** lack a stochastic section (all with 2 report states); the representative `a→b→c→c` example is one of them. This is not a universal proof of minimality, which is proved in the manuscript using finite-cycle invariants.
- A rational Farkas witness for the 3-state example is the row combination `-normal(u) + dyn(u,b) - dyn(w,b)`, with coefficients satisfying `λ A=0`, `λ b=-1`. The exact verifier checks the dual certificate against the generated linear system.
- The sharp covariance-defect radius for that model is `1/2` in total variation, independently checked over 21 rational candidate distributions and proved by triangle inequality.
- A single edge mutation `b→b` instead of `b→c` restores an equivariant point section; a separately declared additional identity probe distinguishing b,c also repairs *current-state* reconstruction.
- The finite two-state swap has no equivariant deterministic section but does have uniform `(1/2,1/2)` stochastic section; a three-state transient-cycle model has a nonuniform stationary kernel `(1/2,1/2,0)`.
- Finite group tests: 360 seeded permutation-action models (all finite fibers) checked for uniform equivariant kernel and stabilizer fixed-point equivalence. An additional explicit 4-cycle with nontrivial quotient action has no point section, but has a stochastic one.
- Integer translation: exact `TV(shift uniform[-N,N], uniform[-N,N]) = 1/(2N+1)` checked for seven horizons including `N=50`; analytic proof is in THEOREMS.
- Markov source controls: two different stochastic source laws descend to the same deterministic observed `u→w→w` process, but only the source with absorbing b,c admits a consistent backward stochastic lift. Probability data are declared, not inferred.
- A too-large rational feasibility problem is **rejected explicitly** rather than reported as nonexistent. Invalid source/report equivariance is rejected.

## Algorithmic scope and proof gaps

The exact finite stochastic solver enumerates basic feasible vertices with exact rational elimination. Its correctness for any instance within the variable cap follows from compactness of the fiber-simplex product, rationality of LP data, and the existence of a vertex with independent positive-support columns. Running this implementation successfully verifies a witness but is not itself a formal verification of the source code. Null returned after complete enumeration means infeasibility under those exact finite constraints; variable counts above the default cap **12** throw an error. This is exponential and not advertised as a scalable LP engine.

**Unrun in the available GitHub-only SUCC environment:** `python scripts/verify_provenance.py`, complete `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`, and Lean checks on the new assertions. Existing SUCC core cannot be loaded as a complete local checkout here; the new module has no dependency on missing source code and its focused suite was executed in a clean standalone scaffold.

**No scholarly priority claim:** the stabilizer criterion, invariant-measure orbit simplex, Markov lumpability and LP/Farkas facts are classical in content; the selected examples and integration in SUCC are new-to-project. No external peer review or blind multi-reasoner proof audit has occurred.

**Repository discipline:** additive changes only; no frozen arithmetic source, historical imports, original `U_0=0` contract, production behavior, main merge, tag or release affected. Remote Git blob identities should be compared against `FILE_HASHES.json` after upload; a correct document hash is not a theorem certificate.
