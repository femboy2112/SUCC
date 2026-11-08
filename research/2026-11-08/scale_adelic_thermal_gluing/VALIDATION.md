# Validation — source-specific scale / analytic-place seam

## Local execution performed in isolated Python package

The repository was accessed through connected GitHub tools (Git clone was unavailable in this runtime); for local tests only, a **temporary** API-compatible `duck_bbp` source implementation was constructed from the exact canonical main formula. It is **not included in the PR**; uploaded code imports the pre-existing `observational_succ.duck_bbp.forcing` from main. The source formula and sample values are checked independently in the tests via the literal four partial fractions. This does not substitute for a full checked-out root suite.

Commands on the isolated tree (use PYTHONPATH if executing receipt.py directly):

```shell
python -m unittest discover -s tests -p 'test_adelic_scale_gluing.py' -v
PYTHONPATH=. python research/2026-11-08/scale_adelic_thermal_gluing/receipt.py
python -m compileall -q observational_succ/adelic_scale_gluing.py tests/test_adelic_scale_gluing.py research/2026-11-08/scale_adelic_thermal_gluing/receipt.py
```

The focused 14 `unittest` methods PASS in the isolated Python 3.13 environment (each method includes many exact subcases). A separate exact rational source state, p-adic residue, modular-coefficient interpolation and counterseed receipt is generated deterministically.

### Real finite cross-source checks

- Uniform rational bound tested exactly for n=`1,2,3,8,16,31,64,127,255,1024` and k=`1,2,3,4,8,16,24,48`, plus the algebraic weighted-moment identity for k=1..16.
- 41-adic source reconstruction requires `D(1),D(2),D(3)` units and `41²>2*120`; exact recovered coefficients `(120,-89,16)` match untouched later source times. Wrong prime/precision and visible sample mutation fail closed; a 41²-invisible mutation survives, as it must.
- Product formula checked on exact factorized rationals and original defects, with both numerator and denominator valuations; not only a chosen prime.
- Source-computed dyadic no-π-oracle wrong seeds A=4,8,16,32 satisfy the proved averaged real bound. They are epoch-dependent rational seeds, not a single fixed wrong seed.
- The independent three-channel p-primary oracle uses each of the original four pole events, rechecks **every point in the full epoch** against separately computed three-channel Fraction recurrences at `(A,p,h)=(32,73,1),(80,193,1),(100,233,2)`. These are FINITE cases with small orders `m=9,24,29` and are not asymptotic qualified-prime samples. All checked phase products and Abel inequalities pass at float diagnostic precision.
- Measured complement total variation in these finite cases is approximately `35.52,110.13,129.87`. The resulting Abel upper bounds exceed 1, which honestly demonstrates that a generic total-variation bound is **not** the missing selected Weyl decay.

### Not claimed or not executed

- Full native 12k+ SUCC test suite, provenance verifier, observer/ordinal scripts, Lean kernel, full exact-head hosted CI, scholarly review: **not run in this isolated environment**.
- All-k analytic log lemma is paper-proved by uniform rational bounds, **not** certified by floating logarithm fits.
- The source `r(x)` is uniquely pinned only *within* the original bounded rational pole class. An unrestricted real-analytic extension is NOT pinned by integer samples.
- No proof of the signed p/complement covariance gate, critical Fejer energy decay, or π normality.

## Check state and artifacts

See `FINITE_RECEIPT.json`. Its exact values (rational strings, prime valuations, boolean source checks) are scope-specific reproductions. Complex phase magnitudes and subgroup deltas are ordinary double-precision diagnostics and **not interval certificates**. Keep all raw failures and host-status errors when conducting the eventual full-tree review.
