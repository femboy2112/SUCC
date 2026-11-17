# Validation and authority ledger

**Machine:** local Python with SymPy; actual version numbers logged by scripts below. 2026-11-16 research branch material. The full SUCC root-suite, Main XXIV/XXV/XXVI gates, pinned Lean suite and hosted GitHub Actions are **NOT claimed** in this local research audit.

**Focused exact module:** `python -m unittest discover -s . -p 'test_prime_compensation.py' -v` — 16/16 test methods passed. It checks source labels, primality through n=299, signed face sum through n=120, exact Bernoulli reduced-residue sums through Q=2310, finite prime Euler companion, mixed/linear cancellation, prime insertion order, formal first jets, observer counterexamples, actual Fraction BBP orbit and the same-time source joining.

**Independent SymPy oracle:** `python independent_audit.py` — 162 exact symbolic/coprime/jet/source-Gamma/observer-compression checks and 85 floating complex DFT/phase checks. It performs independent symbolic simplification of O(1,1) transport, exact Hurwitz/Bernoulli residuals, and the four-pole BBP source derivative from Gamma recurrence rather than importing `prime_compensation.py`. The newly added audit explicitly checks flat full boosts, gauge trivialization, exact P T_q(I-JP)T_p J, the p=2 null and 3/5=45/32 gap. The floating checks are **diagnostics**, not rigorous interval-certified arithmetic or all-time phase estimates.

**Source-byte integrity:** after GitHub upload, independently fetch each remote blob from the new branch and compare its exact SHA-1 Git blob hash against the locally constructed file. Until this receipt is obtained, do not report remote identity or PR publication.

**Claim ledger:**
- `PCE-01/02/03/04/05/06/07/08` — exact elementary/classical proofs in THEOREMS, scoped to explicitly authenticated source/chart.
- `PCE-09` — exact finite source-aligned identity; positive all-shell premise **OPEN**.
- `PCE-10` — classical completed reflection and BBP source constant; the dynamic prime-to-BBP and Weil-positive steps **OPEN**.
- `PCE-11` — flat presentation-space boost and observer-relative compression term **EXACT** in declared ambient calibration, no intrinsic curvature or source-hyperbola reinjection.

**Hostile controls required later:** fake composite 6, deliberate linearization error, p=2 sign flip, p/q permutation and flatness, finite shadow wrong seeds, coboundary gauge, prime-inventory saturation, wrong circle chart, incorrect Γ or half-density, and the difference between finite tests and universal quantifiers.
