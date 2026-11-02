# Validation, provenance and boundaries (2026-11-01)

Source/parent: Main XIX `81045770234a114247e43eb08ae5c6d446e9514a`; stacked research head from #459 `ec9c5a98772c60ab06bd4bb0a3d52a751a8bdc6a`. All files in this change are additive research plus one new root test. No main, production, formal, provenance, historical contracts, CI, artifacts, licenses, tags or releases modified.

## Actually executed offline (local staged tree)

- `python -m unittest discover -s tests -p 'test_prime_window_interferometry.py' -v`: **14 tests OK, 0 skips, 0 failures** (the exact finite intervals take ~9 seconds on the local Python 3.13.5 runtime).
- `PYTHONPATH=research/2026-11-01/prime_window_interferometry python research/2026-11-01/prime_window_interferometry/run_receipt.py`: **15 exploratory + 6 preregistered finite rational-interval cases + 4 strict cofactor comparisons**. Output: `RATIONAL_INTERVAL_CERTIFIED: 15 exploratory, 6 preregistered holdout cases; 2 + 2 strict directions`. The full exact-Fraction receipt, including program SHA256 hashes, is `FINITE_RECEIPT.json`. Rerun to regenerate and compare.
- Independently constructed combined polynomial source agrees EXACTLY with all four original signed fractions for `n=1..174`; exact finite source-convolution replay `N=0..60`. Every original p-primary residue and p-free cofactor on all p=5mod8 primes <=509 and all their birth-window indices is checked by `Fraction`, not float.
- All p=5mod8 primes <=1500 validate exact k:4k+2 window map; all p<=2000 validate full-plus-half clock formula. Exact Gram coefficient equality and two independent finite energy constructions checked. Coherent, alternating, p-free spoof, overlapping source-phase identity, and invalid-domain controls exercised.
- The primary/cofactor/current-source **complex numerical** identity for p=13,29,37,53,109,269,373,397,509 and h=1,3,5 uses exact rational states before float trig; tests for these identities are diagnostics, NOT asymptotic numerical certificates. Two exploratory strict directions at p=373,397 are separately certified by exact rational interval inequalities. See `PREREGISTRATION.md` for the two freshly selected primes (1013,1021) and six finite checks; their direction comparisons were diagnosed only AFTER observing the outputs, and then certified separately by rational squared-norm interval inequalities. The first 15 cases were NOT blinded fresh holdouts.
- `python -m compileall -q research/2026-11-01/prime_window_interferometry tests/test_prime_window_interferometry.py`: PASS.

## External mathematical inputs (not 'validated' by finite tests)

- PNT in fixed progression 5 modulo 8, including prime-density in every fixed relative subinterval and the weighted prime-square asymptotic; classical theorem, not reproduced.
- BGK subgroup exponential-sum theorem (Kowalski exposition, Theorem 1.1; source URL in SOURCE_MAP), applied only on original **unweighted complete** p-primary periods with `d_p>=p^gamma`; no application to the full source cofactor is claimed.
- Weyl criterion, original BBP formula and its summable Green tail, inherited from Main XIX / #459; no new proof or digit oracle claimed.

## NOT run / NOT established

Full 11k+ authentic SUCC checkout regression, original scripts `verify_provenance.py`, `observer_foundations_probe.py`, `ordinal_succ_report_probe.py`, hosted branch CI and independent external peer review are **NOT RUN** in this environment: local git checkout fails DNS, and this standalone study uses a staged copy of exactly the new files, not the full repository. No new Lean theorem, certified all-X prime/cofactor saving, base16 normality or RH proof. Do not promote claims from paper to kernel. See NEXT.md for verdict-changing probes.
