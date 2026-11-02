# Exact validation, independent source checks and remaining debt

- Parent PR #454 head confirmed: `a3802f2c1574362a4fb38cc85ab149a0ccb847f2`. The research is additive; no source/seed/formal/production files were changed.
- The new package uses `fractions.Fraction` for source, pole coefficients, Eulerian rational moments, all-x Laurent residual and first/second derivative checkers.
- **15 new root-discoverable exact unit methods PASS** (many subcases). Fresh `(n,k)` exact residual/derivative holdouts, all-order source sign checks, initial 5 closed leading constants, d=1 recovery, d=2/d=3 new limiting rational constants, and nonauthentic positive source mutation rejection.
- **25 optional independent SymPy identities PASS**: eight `(d,k)` pairs with three source rational derivative/limit identities each, plus original signed-pole/combined-rational equivalence. This is a separate computation of exact derivatives but shares source mathematics; not an external referee.
- **FINITE_RECEIPT.json is byte-reproducible** using `python research/2026-11-01/laurent_clock_sharpness/finite_probe.py --check`.
- **198 partial combined tests:** 197 PASS, 1 inherited full-upstream integration SKIP. Constructed from the already available PR #454 partial snapshot, not a genuine complete checkout; no claim about >10k full suite, source provenance, foundations, ordinal or hosted new-head CI until checked.
- Python compileall PASS. Test logs and symbolic receipts retained under this research directory.

## Failure and repair history

- First independent Eulerian `M_d` rational-PGF implementation allocated an undersized polynomial coefficient buffer; the initial test invocation caught `IndexError`. The recurrence was repaired to allocate `len(P)+2` and retain the exact `x[(1-x)P'+(d+1)P]` formula. An unnecessary no-op line was removed. The repaired result matches separate PR #454 moments at d=0..4 and independent symbolic checks.
- The finite moment oracle originally used the general order-bound gate for `M_(d+1)`; it was updated to admit moments 0..25 while executable sharpness order remains 1..24. Domain/negative tests remain explicit. This is an implementation bound, not a claim that the theorem stops at order 24.
- A small-source negative control mutates the original forcing by `+0.01/n^2`, and fails the original source-specific remainder envelope at `n=10000`. This mutant is NOT claimed to share the original pole positions.

## Proof authority and limitations

The all-horizon limiting theorem is an explicit **paper proof** using strict source-pole sign, uniform residual derivative bounds, and an elementary discrete first-derivative exponential-sum estimate. Finite tests cannot verify the infinite limit. No new Lean declaration or external peer review was run.

The result proves the clock threshold sharp **uniformly over all real seeds** in the same original forcing. It is *not* an impossibility result for the single original rational/zero-seeded orbit. No actual signed normality saving was obtained.

## Reproduce

```bash
python -m unittest discover -s tests -p 'test_laurent_clock_sharpness.py' -v
python research/2026-11-01/laurent_clock_sharpness/symbolic_probe.py
python research/2026-11-01/laurent_clock_sharpness/finite_probe.py --check
```
