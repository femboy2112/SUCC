# OPERATION MESOSCOPIC SPECTRAL ARMY — source-selected pi frontier

**Status: RESEARCH / DRAFT. No proof of pi normality.** Strictly additive child of SUCC PR #474 (`f60ebe5885c1de1f618d52445de77e089e841d3a`). Original FOUR signed BBP poles, `U_0=0`, frozen proofs, formal/Lean, main, CI and production are unchanged.

## Research contribution

- **MSA-01:** two exact integer full-source oracles (future-fixed common denominator and online changing denominator); no pi digit inputs.
- **MSA-02:** exact O(A log A) real-circle near-pair count with an O(A^2) hostile reference oracle; bins and near pairs equivalent within factor 3.
- **MSA-03:** universal *two-sided* Fejer / collision energy equivalence using the band `1<=|h|<m/2`.
- **MSA-04:** new explicit Gamma-tail spectral Hilbert-norm bound `pi/sqrt(12288 A)` between source and completed orbit at self-scale.
- **MSA-05:** **new conditional proof:** for ANY fixed beta>0, an original zero-seeded dyadic-epoch collision estimate at only `m_A~A^beta` bins, `E_(A,beta)=o(log A)`, suffices for pi normality. The source-specific estimate is STILL OPEN.
- **MSA-06/07:** selected prime-frequency passport and a same-four-pole coherent wrong-seed falsifier.

See [PROOFS.md](PROOFS.md) (full quantified arguments), [NEXT.md](NEXT.md) (parallel mathematical fronts and verdict-changing probes), [SOURCE_MAP.md](SOURCE_MAP.md) (provenance), [VALIDATION.md](VALIDATION.md) (exact and unrun checks), and [FINITE_RECEIPT.json](FINITE_RECEIPT.json) (finite source counts, NOT asymptotics).

## Run locally from repository root

```sh
python -m unittest discover -s tests -p 'test_mesoscopic_spectral_army.py' -v
python research/2026-11-02/mesoscopic_spectral_army/generate_receipt.py
python -m compileall -q research/2026-11-02/mesoscopic_spectral_army tests/test_mesoscopic_spectral_army.py
```

Two distinct exact modulus recurrences agree with independent `Fraction` recurrence on tested small n; large epochs A=4096 and A=8192 use exact integer arithmetic. The finite Fourier checks are *not* interval certificates. `FINITE_RECEIPT.json` is deterministic and reviewable. No all-horizon saving and no formal kernel certificate is claimed.

## One arithmetic target

For some fixed beta>0, original source, all sufficiently large dyadic A, m_A=2^floor(beta log2 A), prove

`#{(n,t) in [A,2A)^2: m_A*||U_n-U_t|| <= 1} = o(A^2 log A/m_A)`.

This is enough **by MSA-02 + MSA-05** to prove the requested normality theorem. It must remain a bound in the selected real embedding with full original p-free cofactor and zero seed. Galois averaging, Gamma positivity, fixed finite data and a large new-prime denominator do not prove it.
