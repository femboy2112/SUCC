# Validation, source map, and provenance — BBP dual boundary

Research local. Parent `femboy2112/SUCC` PR #526 SHA `d2960bacf939fbdfa76c81648b031e182e97d1a6`; work on `research/bbp-2adic-boundary-conservation-2026-11-06` only. Original four signed poles and literal `U0=0` are read-only source inputs. No historical contract, formal Lean, production path, provenance manifest, workflow, or `main` edit.

**Preregistration:** `PREREGISTRATION.md` committed on GitHub as `1f580c21003222946001bc1ceb04b7bbb4901106` before the k=2048 and 4096 modular checks, source mutation, coboundary, and new k11/12 period controls. Earlier k≤1024 zero residues and the p-adic logarithmic proof hypothesis were already explored: classify as calibration, never blind holdouts. The mathematical V(0)=0 result is established by the independent analytic proof in `THEOREMS.md`—not by 4096-bit finite arithmetic.

### Executed commands

```sh
python -m compileall -q bbp_dual_boundary.py test_bbp_dual_boundary.py independent_oracle.py
python -m unittest discover -v -s . -p 'test_*.py' > LOCAL_TEST_STDOUT.txt 2> LOCAL_TEST_STDERR.txt
python independent_oracle.py > INDEPENDENT_ORACLE_LOG.txt
```

- Focused Python 3.13: **18/18 methods PASS**, zero errors/failures, `compileall` PASS. The test suite uses exact Fraction arithmetic and modular inverse modulo powers of 2, not floating point.
- Differently constructed SymPy oracle: original four-pole compact numerator, exact rational-function decomposition, derivative of the formal p-adic-log primitive, Gaussian factorization and odd divided-difference certificate all PASS. This is mathematical/symbolic cross-checking, **not external independent academic review**. Earlier first invocation errored due to an uncancelled symbolic `(z-y)` denominator, corrected with `sp.cancel`; this was an oracle plumbing issue, not a falsified theorem; raw failed stack observed locally and is disclosed here.
- Fresh modular tests: V(0) is zero modulo 2^2048 and 2^4096; first-pole 4→5 mutant past boundary is odd; real/p-adic seed `1/5` contrast and rational source coboundary checks PASS.
- Finite permutation: exhaustive induced V residue map for `k=1...10`; direct recurrence independent of V passes at separate n and k; new clocks k=11,12 congruent across n→n+2^k. The theorem itself holds for **all** k and is proved in THEOREMS.
- Real counterexample: rational decaying shadow `H(n)` provides p-adic full permutation/Haar yet Archimedean phases tend to 0. Dual-boundary source mutant and the more restrictive isometric `2H` mutant are exact algebraic countermodels.

**Explicit unperformed:** full original SUCC >12k test suite at exact research head, repository root verify_provenance.py, observer/ordinal foundation probes, native Lean/kernel, exact-head hosted CI, externally blind refutation, any physical measurements, publication. No π-normality, RH, or real Weyl cancellation claim.

Use `FINITE_RECEIPT.json` to audit source/log SHA256 and prereg scope. The original four-pole BBP sum is a classical source premise; its real π value and normalized invariant appear in SUCC #521/#525. The new mathematical content is typed in the 2-adic integer clock and its finite-residue distribution, not a proof of archimedean normality.
