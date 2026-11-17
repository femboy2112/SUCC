# Validation and provenance — Prime-path nerve research draft

**Scope:** the exact research-only files in this folder. The original SUCC source, provenance manifest, all earlier research files, production packages and main are unchanged. SHA of the candidate branch/PR is recorded externally after publication.

## Local executions

- `PYTHONPATH=... python -m unittest discover -s ... -p 'test_*.py' -v`: **9/9 PASS**, zero failures/errors, final exact script bytes in this research folder. See `TEST_LOG.txt`.
- `python independent_audit.py`: **115 independent exact SymPy/integer assertions** and **103 independently implemented complex Fourier/critical-line/reflection checks** PASS. Numerical Fourier, critical-line phase and `xi` checks use float or 65-digit mpmath and are diagnostics, not interval proofs; infinite claims are justified by displayed algebraic proofs in `THEOREMS.md`. See `AUDIT_LOG.txt`.
- `python -m compileall -q ...` and `python -m json.tool CLAIM_LEDGER.json`: PASS.
- Initial sign calibration failure `c_30(6)` and its repair are preserved in `CALIBRATION_HISTORY.md`. Do not claim all attempts passed.
- Sources are cross-checked against `docs/PI_NORMALITY_FRONTIER.md`, `docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md`, the positive-clock Pascal construction in `research/2026-11-14/causal_suspension_gamma_zeta/THEOREMS.md`, and prime/Weil claims listed in `SOURCE_MAP.md`. All classical dependencies remain credited.

## Tests and controls

The tests check the subset nerve vs the survival CRT selector for Q=1,2,6,30,210; the elementary source-prime witness for n=2..999; exact rational Bernoulli/Hurwitz finite stage at negative orders -1,-3,-5; signed Ramanujan product; finite Fourier reconstruction; prime insertion compensation at -1; all-prime limit obstruction; fake composite 6; incompleteness at 49; critical-line reflection phase derivative; and classical xi(-1)=xi(2), etc.

## Explicitly NOT executed or proved

- The full `AGENTS.md` four-gate repository checkout (provenance, full native test discovery, observer foundations, ordinal report), the Main XXIV/XXV/XXVI integration gates, a new Lean kernel proof, blind academic review or hosted CI at the yet-to-be-published branch head.
- A theorem identifying arbitrary causal path superpositions with prime-state nerves; our identity requires a **declared squarefree-divisibility path category**.
- A nontrivial source-selected signed coupling between prime arithmetic and the zero-seeded BBP carry trajectory; no R0/π-normality estimate or RH/Weil positivity is claimed.
- A regularization of the bare infinite Euler product at negative integers. Only the exact Q-indexed compensator and its Hurwitz continuation are used.

**Next verdict-changing task:** construct a signed source-coupled, observer-time-indexed joint projector/carry observation that distinguishes the original zero BBP seed from coherent same-forcing wrong seeds and survives all SOURCE_MAP/NEXT controls.
