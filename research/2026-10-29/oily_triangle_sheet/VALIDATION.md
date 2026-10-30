# Validation and provenance — Oily triangular sheet

## Source and execution boundary

- Pinned upstream: `femboy2112/SUCC main@ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc` (read with live GitHub connector before branching); `AGENTS.md` and `docs/METHOD.md` read at that ref.
- Research branch: `research/oily-order-statistic-golden-sheet-2026-10-29` (created from the pinned main commit).
- Available local environment contains the authored **research package and its standalone test**, **not** a complete local SUCC checkout. An outbound `git ls-remote` was attempted and failed because the container cannot resolve `github.com`. Therefore full native SUCC tests, provenance and observer/ordinal probes, Lean and exact-head hosted CI have **not** run here. The tests below exercise the actual locally authored bytes and are explicitly scoped.
- Historical original signed BBP forcing, zero seed, source archives, claim registry and production code remain untouched. This is an additive research draft.

## Executed commands (local authoring workspace)

```sh
python -m unittest discover -s tests -p 'test_oily_triangle_sheet.py' -v
# 15 test methods PASS in 0.376s; includes 10,010 exhaustive median-insertion rows
python research/2026-10-29/oily_triangle_sheet/triangle_sheet_probe.py
# OILY_TRIANGLE_EXACT_BASIC_PASS
python research/2026-10-29/oily_triangle_sheet/numerical_oracle.py
# independent high-precision quadrature holdout PASS
python -m compileall -q research/2026-10-29/oily_triangle_sheet/triangle_sheet_probe.py research/2026-10-29/oily_triangle_sheet/numerical_oracle.py tests/test_oily_triangle_sheet.py
# exit 0
```

Exact full stderr/stdout captured in [`exact_tests.log`](exact_tests.log), numerical stdout in [`numerical_oracle.log`](numerical_oracle.log), environment in [`python_env.txt`](python_env.txt). Do **not** turn numerical consistency into a proof of a uniform error bound. The `O(a^-2)` asymptotic and the matched-mutant limit have a separate paper derivation in the [README](README.md).

## Independent numeric holdouts (not certified enclosures)

- Original unreduced four-pole integral yields `16*T0=3.1415926535897932384626433832795029...`; 98 pointwise original/reduced comparisons passed at 65 decimal places.
- `T_(n+1)=16 T_n-r(n+1)` checked against independent quadrature through `n=6` at tolerance `1e-48`.
- `Omega=0.040818323848361987598074744283235687...` and source first-jet coefficient `6lambda-19/2=-5.7917960675006309107724789938061713...`.
- `a[F_a(lambda)-Omega]` at `a=16,32,64,128,256,512` tends toward `-5.791796...` (`a=512`: `-5.7322406171...`).
- Source mutant `epsilon=1/2` has predicted `a^2(F_(a,e)-F_a) -> -3.208203932499...`; observed at `a=64,128,256,512`: `-2.66947, -2.91477, -3.05437, -3.12933`, respectively. Slow finite convergence is **not** represented as an exact equality.

## Staged local Git blob identity (before remote upload)

Git blob SHA-1 is computed from the exact authored bytes as `sha1(b'blob '+ascii(byte_count)+b'\0'+raw_bytes)`. The map below is for **locally tested** payloads. Remote upload must be followed by `fetch_file`/tree verification before status promotion.

| File | Bytes | Expected Git blob SHA-1 |
|---|---:|---|
| `research/2026-10-29/oily_triangle_sheet/README.md` | 16346 | `bf20af71f1105ccc9cd063c5260d3e1f5531a030` |
| `research/2026-10-29/oily_triangle_sheet/CLAIMS.md` | 4805 | `c84e66992cd3399a60c17b4835a85da143b37677` |
| `research/2026-10-29/oily_triangle_sheet/NEXT.md` | 3763 | `9b95c829553057990d652bd965b934c8c0766b0e` |
| `research/2026-10-29/oily_triangle_sheet/triangle_sheet_probe.py` | 6435 | `6dee80ae4dcca1c7f3bfae97f4086af432a3b5d4` |
| `research/2026-10-29/oily_triangle_sheet/numerical_oracle.py` | 2564 | `254adf8c1e29f7b19ec1b1c3d2a34f901bd13bbf` |
| `tests/test_oily_triangle_sheet.py` | 8369 | `b067c4114a03f3a9df739a2c4c0b8aa0b7c2c46f` |
| `research/2026-10-29/oily_triangle_sheet/exact_tests.log` | 2236 | `b0f64fc3179506c781b20342609be37748d095d4` |
| `research/2026-10-29/oily_triangle_sheet/numerical_oracle.log` | 1181 | `7fecf79461543bc9fccdb740a84f0e432ef508d4` |
| `research/2026-10-29/oily_triangle_sheet/python_env.txt` | 72 | `985766c82cb41217e714c6f77b983f681204abea` |

## Known limitations and corrections to prior conversational assertions

- The preceding conversational answer mentioned `44,784 exact-rational cases, 25 generating-function comparisons, and nine numerical beta-log integrals` without an actual tool execution receipt in that turn. **Treat that historical run-count assertion as UNVERIFIED.** This round replaces it with the exact logged and reproducible counts above; do not inherit the old numbers as evidence.
- The package is **not** a full repository checkout, so no full-suite success, hosted CI, provenance probe, observer/ordinal probes or Lean authority is claimed.
- The Gamma rank family, first source coefficient and second-order mutant discriminator are not evidence of physical vacuum effects, quantum speedup, normality of pi or RH.
- The source posterior triangle alone is insensitive to the exact selected `U0=0` phase; the coherent counterseed `V0=-pi/16` preserves every positive scalar law. Any proposed proof must explicitly defeat this negative control.
- Sibling research #359/#366/#367 and inherited #310/#345 retain their own statuses. No merge into `main` is requested or authorized.
