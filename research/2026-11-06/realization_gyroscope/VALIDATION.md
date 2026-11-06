# Local validation and provenance scope — 2026-11-06

**Environment:** Python 3.x, standard library only, executed in an isolated local `/mnt/data/succ_realization_20261106` directory. The GitHub connected repository was read through the GitHub connector; no local clone of the entire SUCC tree was available. No run is falsely attributed to the live GitHub commit/hosted Actions until it is verified separately.

## Executed commands and preserved raw output

```
python -m compileall -q gyroscope.py test_gyroscope.py independent_oracle.py
python -m unittest discover -v -s . -p 'test_*.py'
python independent_oracle.py
```

- `compileall` **PASS**.
- Focused unit tests **17 run, 17 pass**, no errors/failures. Raw output: `LOCAL_TEST_LOG.txt`.
- Different-formula exact-rational oracle **PASS**: 12 source, 33 closed-state, 7 future-tail enclosures, plus exact phase/recoding and radix digit probes. Raw output: `INDEPENDENT_ORACLE_LOG.txt`.
- Every test and oracle source is SHA256-indexed in `FINITE_RECEIPT.json` (including exact log files). The oracle shares the same source mathematics; **it is not blind external mathematical verification**.
- A separate ephemeral SymPy calculation (not committed as a dependency) expanded `D(n)-n² A(n)` in `t=n-2`, yielding the explicitly positive polynomial in THEOREMS.md; exact integer identities are also tested at held-out integers.

## Finite holdouts and mutants

Original source epochs / indices include `n=1,2,3,7,16,17,31,32,41,61,64,89,97,113,173,251,307,401,509`. Original rational selected states tested at n up to 99 and under four seeds. The other direct rational source oracle tests n up to 97. Original tail enclosures at depth 8, 12, 18 against a separate depth-40 direct series. Binary↔hex identities use exact Fraction for symbolic points and original source states; 4-phase identities use several rational beta seeds across multiple block lengths. Finite staircase bound tested with `K=2000`, but **the all-K theorem is analytical** and does not rely on the finite run.

The hostile controls include changed physical source (+1/37), changed internal model source, mismatched initial model, observer policy variations that leave the authentic arithmetic unaffected, a constant carrier artificially rendered uniform at the first-hex-digit marginal, the same-source `β=1/5` nonnormal completion, and a diagonal versus product joint-correlation control.

## Not executed / missing authorities

- **Full native SUCC test suite (12k+), `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`: not run** because the full checkout was unavailable in the current tool runtime.
- **Lean kernel: not run.** No new Lean theorem or authenticity claim.
- **GitHub hosted CI at the exact pushed commit: not asserted.** Connector branch-commit readback is separate from local test execution.
- **No independent external referee**; same-reasoner mathematical derivation and two implementation routes are separate evidence types.
- **No π normality proof**; `S_A(h)=o(A)` for actual zero-seeded source remains OPEN. The two-connection proof-transport theorem is logically conditional on an authentic signed estimate.

The branch changes only new research files in `research/2026-11-06/realization_gyroscope/`. Neither main nor original/provenance/formal contracts are rewritten. Its integration with Claude's parallel Main XX remains a maintainer review decision, not an automatic merge.