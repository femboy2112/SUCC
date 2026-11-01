# Operation Carrier-Relative Path Measure (CRPM)

**Draft research package, 2026-10-31.** Branches from SUCC Main XVII at `e8598cfa5d32fd1de8e94a3e458a366a0850d59e`. Preserves the original four signed BBP poles, authentic `U_0=0`, all prior theorem contracts, imported archives, production paths, workflows and Lean authority. **π normality and RH remain open.**

## Why this round exists

The proposed rule `||a-b|| = superpos(abs(a-b), carrier)` is more accurately a **carrier-relative observation program**: use a boundary constraint to select all admissible realizations, then distinguish an energy-derived metric from a signed path amplitude whose phase must be authorized by the actual source. Pascal/triangle geometry is not merely decorative: it supplies a calculable cycle space, a Gaussian-binomial phase-carry model, and a falsifiable flatness/holonomy test.

## What is delivered

- **A literal all-path recovery of absolute value:** a discounted simple-walk Green kernel on `Z` satisfies `G(a,b)=(5/4)3^(−|a−b|)`, so `|a−b|=log_3(G(a,a)/G(a,b))`; finite path sums have exact rational error bounds. The fair Pascal positive endpoint law is `binom(n,k)/2^n`.
- **A genuine metric:** for finite connected weighted graphs, exact Thomson minimum energy `R_C(s,t)=(δ_s−δ_t)^T L^+ (δ_s−δ_t)`; `sqrt(R_C)` is a metric. A unit triangle decreases terminal resistance from 2 to 2/3 versus a unit two-edge line. An independent *two-forest* counting oracle verifies the calculations.
- **An exact phase architecture and negative theorem:** gradients of vertex potentials are path independent, so adding such potentials cannot generate relative path cancellation. Only independently authorized nontrivial path phases can alter interference.
- **Pascal path interferometry:** count binary paths by zero-before-one area to construct `[n choose k]_q`, and certify every interior entry of the `n=16` row vanishes at primitive 16th roots, using exact integer polynomial reduction. An independent oracle enumerates all 65,536 paths.
- **An authentic arithmetic square:** `T_n(p x)−p T_n(x)=(1−p)r(n+1)` is a source-dependent noncommutation defect, with a proved summable bound. The square is SEED BLIND.
- **A decisive same-forcing altered-seed control:** `s*=−π/16` yields `U_n(s*)=−T_n`; for every fixed nonzero h and N, `|S_N(h;s*)−N|<11|h|/56`. It is provably **not normal**, despite sharing source forcing, square defects, and the positive carrier.
- **A finite source-typed π gate candidate:** 2-adic clock anti-pairing provides an exact rational bound on real-circle Fourier sums, but selected real mismatch has not been proved to vanish. A perfect-cancellation counterexample confirms this condition is sufficient, not necessary.

## How to run

From repository root:

```sh
python -m unittest discover -s tests -p 'test_carrier_path_measure.py' -v
python research/2026-10-31/carrier_path_measure/carrier_path_measure.py
python research/2026-10-31/carrier_path_measure/independent_oracle.py
```

For full integration, also run the root requirements in `AGENTS.md`. Local environment for this research run had no full checkout or Lean execution, so there is **no claimed full-suite or hosted CI pass**. Exact local raw commands and results are in `VALIDATION.md`.

## Pointers

`PROOFS.md` — definitions, hypotheses, quantifiers, derivations, traps; `CLAIMS.md` — scoped status ledger; `NEXT.md` — next falsification/proof routes; `VALIDATION.md` — local receipts; `carrier_path_measure.py` — Fraction and cyclotomic exact probe; `independent_oracle.py` — structurally independent counting and spanning-forest oracle; `tests/test_carrier_path_measure.py` — root-discoverable regressions.

**Existing SUCC contracts and related work:**

- [Selected π frontier](../../../docs/PI_SELECTED_CATEGORICAL_FRONTIER.md) and [categorical observer atlas](../../../docs/CATEGORICAL_OBSERVER_ATLAS.md).
- [Carrier-first selected transport PR #424](https://github.com/femboy2112/SUCC/pull/424), [counterfactual triangle PR #426](https://github.com/femboy2112/SUCC/pull/426), [two/three prime carrier PR #427](https://github.com/femboy2112/SUCC/pull/427), [Pascal cross-prime PR #428](https://github.com/femboy2112/SUCC/pull/428), [three-place BBP Gamma difference PR #430](https://github.com/femboy2112/SUCC/pull/430).
- Classical background: [Aldous–Fill](https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S7.html), [Bailey–Crandall](https://doi.org/10.1080/10586458.2001.10504441), [Lagarias](https://arxiv.org/abs/math/0101055), [q-binomial root-of-unity paper](https://link.springer.com/article/10.1007/s00026-019-00461-8).

**Decision:** integrate only after scope review. Treat this as a research increment to the observer/carrier interface, NOT a completed π normality proof and NOT a new general SUCC category replacing existing `operational_yoneda_descent`.
