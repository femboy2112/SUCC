# Focused validation — Pascal/Oily original-BBP bridge

Date: 2026-10-29. Parent: SUCC PR #369 head `95f368719a1e020e8bf5b9312b10260a94a0a519`. Source four signed poles and `U0=0` unchanged.

## Actually executed

- `python pascal_oily_probe.py` on Python 3.13.5: **20/20 PASS**, including strict rational positivity/normalization, two independently arranged rational Pascal PGFs, root birth, rank-four exact tests, 15-torsion anchor and changed seed controls, Oily inverse, and finite TV bounds.
- `python independent_oracle.py` with SymPy and mpmath: exited 0. Independent symbolic checks recovered the positive shifted integer polynomial, the original `-151/960` first correction, both rank-2 and rank-4 rational-function first corrections, the quadratic-field fixed-point correction, and the finite Oily–Macaroni correction. Five high-precision numerical holdouts n=5,10,20,40,80 converged in the predicted direction.
- `python -m py_compile pascal_oily_probe.py independent_oracle.py`: passed.
- Independent exact rational coefficients are retained under `independent_receipt.json`, and local console output under `validation_stdout.txt` and `independent_output.txt` (these two log files are local, not asserted to be in the PR).

## Local exact source file hashes (SHA-256)

| File | SHA-256 |
|---|---|
| `pascal_oily_probe.py` | `1d9a62ca2837e563f2c375fe974c4bb8244102f624dffab744961342b528b464` |
| `independent_oracle.py` | `c822dc4e5db83ce865dc7cdccb474488fe15a15738780ab97876489c6a399b3a` |
| `PASCAL_OILY_SIGNED_LIFT.md` | `fbfc35d0115cf71860f0b87643b57ae9d6fbd1113ba943b1744c92d49d570827` |
| `CLAIMS.md` | `0797466a7debe0bf1184a814d824493d18b4e8056f5027125fd8d2b0146ade78` |

## Not run / not claimed

No complete SUCC native gate, provenance check, repository main integration, hosted CI, byte-identical exact-head Python replay, Lean kernel, or blind peer review is claimed. The paper derivations, code checks, and original source trace are separate authorities. π normality is **OPEN**. A coherent changed seed and constant phase remain negative controls for every proposed signed saving.
