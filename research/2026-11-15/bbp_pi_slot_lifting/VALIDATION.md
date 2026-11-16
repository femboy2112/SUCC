# Validation at the additive research payload (2026-11-15)

**Status: finite source tests and independent numerical/symbolic audit passed; full SUCC/Lean/hosted CI have NOT been run.** Original source is Main XXV `observational_succ/duck_bbp.py` blob `34cb7b64f6975e05586ec220a4655961a8e7b636`; source parent is draft #649 head `55236438e6f38dadcb207011ff3bc7086d41fea0`. **π normality and R0 remain OPEN.**

## Executed checks and exact boundaries

- Focused: `python -W error -m unittest discover -s . -p 'test_pi_slot_probe.py' -v` — **53/53 OK** (original signed poles, independent polynomial U_n derivation, strict rational Green intervals, positive time differences, source-gauge finite telescoping, Bernoulli integer-character blindness, operator source identities, finite Poisson sampling, Oily first/second moments, all-mode instrument finiteness). Finite modulus/grid checks are observations and cannot prove any all-n theorem.
- Independent script: `python independent_audit.py` — **100 separately coded symbolic/high-precision assertions PASS**; SymPy checks the original moment source and finite polynomial decomposition, mpmath quadrature checks time-split phases and four-tap positive Green integrals against independent rational source sums, and Oily derivative identities recover 8/3 and 32/3. `FINITE_REPORT.json` records actual values and scopes. Mpmath values are diagnostics, not rigorous enclosures; the focused tests implement *rational* source-tail bounds independently.
- `python -m compileall -q pi_slot_probe.py test_pi_slot_probe.py independent_audit.py` — PASS.
- `python -m json.tool CLAIM_LEDGER.json >/dev/null` and `python -m json.tool FINITE_REPORT.json >/dev/null` — PASS.
- `source original target no π oracle`: `sample_pi_coin()` uses only source rational functions, uniforms, comparisons, maxima, and an independent uniform click; no arithmetic target π constant. Numeric complex `e(t)` uses the universal angular Fourier factor `2π` for circle parametrization—**that is not the π arithmetic input**.

## Mathematical proofs versus tests

PS-01/02 source operator formula follows exactly from the polynomial/geometric identity; no finite test is claimed as a proof of it. PS-03 Green complete monotonicity follows from a strictly positive source density. PS-04's illegal interchange counterexample is algebraic and decisive. PS-05/09 marked Poisson expectation/variance is derived by conditioning on a **finite Poisson count** (complex bounded factors permitted), not by asserting an unproved physical stochastic law. PS-06 phase transport uses the authentic Green tail and strict rational bounds, not a fit. PS-07 integer coboundary correction is a finite exact telescoping algebra plus the explicit `g(n)=o(16^n)` limit.

## Reproducibility and source hash controls

The output files `TEST_OUTPUT.txt`, `ORACLE_OUTPUT.txt`, `FINITE_REPORT.json`, and generated `SOURCE_MANIFEST.json` accompany the exact tested code. The final Git-blob checks are to be performed **after** upload, and the final Git commit tree should be read back and compared with staged SHA-1 hashes; neither that eventual check nor full root CI is preclaimed by this validation file.

## Unrun / unresolved

- Full native `python scripts/verify_provenance.py`, `python -m unittest discover -s tests`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py` on a complete immutable SUCC checkout.
- Lean kernel formalization, source-independent academic referee review, automatic theorem proving of the infinite asymptotic statements, hosted CI at the candidate commit.
- Any source-only signed all-large-shell bound or actual π-normality proof.
- Physical quantum/Higgs/energy-in-joules inference from the mathematical randomized phase program.

**Hostile control that changes the interpretation:** PR #648's integer coboundary `g(n)=2n²` changes the source presentation but leaves **the same** π/16 and completed circle orbit. It must not be treated as a different real normality target; source-specific chirality and its coupling need a genuine original-forcing predicate, rather than being inferred from the target alone.
