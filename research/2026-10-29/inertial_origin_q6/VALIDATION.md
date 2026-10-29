# Research-only validation — inertial origin q6 (2026-10-29)

Exact original SUCC source: `4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)` with `U0=0`. Work based on PR #376 head `4a396badd6069a8011352133c02ec09af35b2bf6`; sibling PR #373 read but not ancestry-merged. Main unchanged.

- Local exact `python inertial_gauge_probe.py`: **21/21 PASS** (0.207 s).
- Independent `python independent_oracle.py`: full SymPy rational source identity and positive decomposition; **40** direct 76-digit complex signed-bin integrals (largest discrepancy `3.25e-78`); **2** discrete-Haar FFT checks with errors ≤`5.6e-17`; **4** coherent original BBP counterseed Green-tail checks with errors below `8e-63`; **5** 16→0 transition numerical margins positive.
- Exact tests include source-marked chart shift covariance at multiple rational offsets and physical seeds, full 4×17 q6 carry/phase tensor, 15-torsion relative-phase alias, integer seed phase alias, original-Green tail enclosures, actual selected zero-carry/15-run checks, and Haar 17-bin conditional Fourier coefficients.
- The all-n inequalities and the late-time irrationality consequence are paper proofs, not extrapolations from these finite controls.
- No full native SUCC suite, Lean, hosted CI or external peer review is claimed for this new research branch. No frozen source, archived manifest, original four-pole code, or previous PR files modified.
- Read `CLAIMS.md` and `NEXT.md` for explicit result types and falsifiers. README file `INERTIAL_ORIGIN_Q6_CARRY.md` includes the complete derivations.
