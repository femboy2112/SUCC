# Validation and provenance boundary — 2026-11-06

**Environment:** Python 3.13, standard library, local research sandbox `/mnt/data/succ_joint_entropy_round2` (no full local clone of SUCC available). GitHub source/README/AGENTS/π-frontier and predecessor #525 were inspected through the connected GitHub connector. The child research branch began at exact parent #525 head `f45e4459f2efa6a94bfa5adcf8184c57aa028c55`.

**Prior-registration scope and correction:** `PREREGISTRATION.md` sha256 `efcefe2c71f3d9898b7dd6f6b45f3cc7ed287cbef651bae66793fd43ae10cc32`, already committed at GitHub SHA `d7b5b7b330394992eb43fe533f10962b9c0e9544`. That external GitHub commit precedes execution of `holdout_probe.py`; **however the four (A,h)=(223/457,1/2) values had already been explored in scratch before that registration**. Their rigorous finite bounds stand, but they are **pre-seen calibrations**, not blind holdouts. A separate untouched addendum `PREREG_ADDENDUM.md` SHA256 `98d45acdaa6c62a87dceef23fdf9e3ee6f50d441632b2ce354654dbe4ecfb0d7` was committed as `6659899812abee3ae6625907212c8d991dfbf6ee` **before** the genuinely new A=239/503, h=3 calculations. Same-model registration is not independent blind work.

## Reproducible executed commands

```sh
python -m compileall -q joint_entropy.py independent_oracle.py signed_certificate.py entropy_to_character.py holdout_probe.py fresh_holdout_probe.py test_joint_entropy.py test_signed_certificate.py test_entropy_to_character.py test_fresh_holdout.py
python -m unittest discover -v -s . -p 'test_*.py' > LOCAL_TEST_STDOUT.txt 2> LOCAL_TEST_STDERR.txt
python independent_oracle.py > INDEPENDENT_ORACLE_RAW.json
python holdout_probe.py > HOLDOUT_RAW.json
python fresh_holdout_probe.py > FRESH_HOLDOUT_RAW.json
python receipt.py > FINITE_RECEIPT.json
```

**Executed:** `compileall` PASS, **29 unittest methods PASS**, 0 errors/failures (raw output `LOCAL_TEST_STDERR.txt`), independent exact rational oracle PASS, source-digit/finite signed calibration and newly registered holdouts PASS. See raw JSON and file SHA256 receipt; tests are not independent academic referees or formal Lean proofs.

### Certifying arithmetic versus numerical diagnostics

- **RIGOROUS rational interval:** The selected Fourier bounds use rational cosine/sine Taylor series with a worst-case Lagrange remainder using `π<22/7`; true π is enclosed with Machin's formula and alternating-series rational remainder; each selected orbit phase is enclosed using the true four-pole BBP source and a tail error `16^-depth/[15(n+depth+1)^2]`. The complex sample mean lies in a proven norm interval computed by integer-square-root rational rounding. The displayed 12-decimal lower/upper boundaries are intentionally **outward rounded**.
- **Independent finite source check:** Machin and BBP agree on 128 rigorously certified hex digits. Seven high-index phases up to `n=913` have overlapping independent exact intervals, and 200 pole values match an independently assembled rational expression. These are two different analytic routes, but do not establish global normality.
- **Floating numerical diagnostic:** entropy deficits use `math.log` for finite sample display. The finite J9/J19 inequalities are proved analytically; the floating diagnostic values are **not certified exact entropy comparisons to 12 digits**. J19's numerical RHS exceeds 1 at all selected tested epochs. These diagnostics are not rigorous source-specific signed savings.
- **Selected finite signed outputs:** Original four-pole zero seed: **pre-seen calibration** `A=223`, `h=1,2`, and `A=457`, `h=1,2`, and **commit-first fresh holdout** `A=239,503`, `h=3`; all upper bounds less than 1. Periodic completion β=1/5 certified lower greater than 0.99; exact 16-root grid upper less than 1e-6. No asymptotic inference is made.
- **Negative test history:** An initial attempted boundary-failure test at original `n=0,d=1` failed because this digit is already certified. The negative test was repaired by centering a *synthetic rational cell* at the short source-tail interval's boundary. Original failed test outcome remains disclosed in THEOREMS.md/CLAIM_LEDGER.md; no source data or epochs were altered.

## Exact GitHub and native boundaries

- Additive child of #525. Commit the code, docs, controls and independent receipts only on `research/joint-character-entropy-source-2026-11-06` and open a **draft stacked PR** against `research/recursive-carrier-realization-gyroscope-2026-11-06`.
- `main`, original four signed terms, literal `U_0=0`, archived import manifest, `formal/`/Lean, production, workflows and license are **untouched**.
- **NOT EXECUTED:** full native >12k test suite on the child exact head, repository-wide `verify_provenance.py`, observer/ordinal root probes, formal Lean kernel, hosted Actions exact-head CI, independent external mathematical refereeing. Hosted workflows may be queried after PR creation, but never called green until observed.
- **NOT CLAIMED:** a new source-selected infinite signed inequality, all-source zero-entropy semantics, physical quantum evidence, π base-16 normality, RH, publication or scholarly priority.

The finite signed certificate routines need the original source analytic identity and the classical Machin identity as **mathematical premises**. The independent cross-checks calibrate those two routes on named finite inputs; they are not external proof of the underlying historical identities.
