# Actual validation, source boundaries, failed probes and replay instructions

Parent GitHub SUCC PR #450 read at head `a62c5385681890d40e7ca05127e0cc5d71e8b9c0`, itself stacked on #449/#447. New package is ADDITIVE under `research/2026-11-01/arctan_reciprocity/` and `tests/test_arctan_reciprocity.py`. No mainline, production, archives, original four signed poles, U0=0, prior theorem contracts, workflows or Lean files are modified.

## Actually executed on new authored bytes

- **Standalone:** `python -m unittest discover -s tests -p 'test_arctan_reciprocity.py' -q` — 31 discovered, **30 PASS, 1 SKIP**. The skip is the real existing `categorical_source_gluing/source_gluing.py` adapter, absent from a standalone thin workspace; no fake replacement was used.
- **With parent implementation mounted:** the **same 31 tests PASS**, including 34 original source/gluing recurrence crosschecks against the actual parent local file bytes from the previous SUCC categorical bundle.
- **Combined previous local categorical bundle and new files (partial-tree proxy):** `python -m unittest discover -s tests -p 'test_*.py' -q` — **100 discovered, 99 PASS, 1 SKIP**, including both earlier categorical sharpness tests and the new mirror controls. This is NOT the full root SUCC suite or external blind review. The inherited skip depends on the full `observational_succ` core.
- Optional independent `symbolic_probe.py`: **14/14 exact SymPy checks PASS**, including four-pole dlog, Cayley branch inversion, full projective involution, gamma commutator, and degree-16 tangent identity. `SYMBOLIC_RECEIPT.json` records exactly what was checked.
- Deterministic `exact_receipt.py`: **6 harmonic exact Gaussian-rational certificates PASS**, with nonzero integer numerators and rational squared conditioning. `FINITE_RECEIPT.json` records exact source states, values and costs.
- Optional `finite_probe.py`: **16/16 high-precision finite diagnostics PASS**, on the original source and literal zero seed with predeclared N=32/64/128/256, h=1/3/5/7; numeric values of the Weyl mean, two sine quadratures and bound are retained in `FINITE_DIAGNOSTICS.json`. These are finite numerical checks of a proved inequality, NOT a proof that the quadratures vanish as N grows.

## Distinct methods, shared provenance

The algebra is derived on paper from Cayley, Fourier and original source; exact Fraction recurrence and rational source are checked against their combined polynomial counterpart and the parent PR #450 implementation. Integer Gaussian powers use binary exponentiation; one unit test uses independent repeated multiplication of rational Gaussian pairs. The SymPy symbolic probe uses independent expansion. The high-precision finite diagnostics evaluate exact rational states via a separate numerical conversion, but share the same source. Same principal model and source are not blind independent witnesses.

## Recorded failure / repair

An initial test attempted strict inequalities `float(pi_lower)<math.pi<float(pi_upper)` for a 22-term Machin interval of width far below binary64 resolution. Both strict comparisons rounded to the same IEEE double. **The test failed because the observer was too coarse**, not because the exact Fraction Machin bracket failed. It was replaced by a purely exact rational width test; the actual π inclusion follows from the classical Machin identity and alternating series. This is a TLICA-style source-map/probe-precision repair, not silent test suppression.

Another integrity failure was found by `git apply --check` on the provisional generated patch: a LaTeX `\frac` sequence had serialized with an unexpected form-feed control character. Its single occurrence was located, restored, and the patch regenerated. This was a text-serialization issue, not a failed mathematical identity. Raw checks of every committed UTF-8 source and document now reject non-newline control characters.

## Falsification controls

- **Bare rational-angle arctan mirror fails:** an IID base-16 Cantor measure with digits {0,7,8,15} is invariant under ×16 and the unrotated J_1/2, yet is non-Haar. Test checks the exact digit permutations, including nonterminating rational sample and correct tail complement.
- **Coherent nonselected seed:** same original forcing, altered completed point q=1/5 requires an *irrational* initial seed; its sine limit under source-r2 irrational mirror is nonzero. This is a lawful real affine countermodel, but not admitted as original finite rational register state.
- **Wrong projective domain/branch:** projective t=0/infty, negative real t and rational Möbius sign are exercised. The exact algebra never treats atan(-x)+atan(-1/x)=+pi/2.
- **Wrong finite Fourier type:** gamma is infinite-order Gaussian rational, not a finite odd-conductor root of unity. All source phase transports and claimed limits maintain this separation.
- **Source mutant:** q=r2 alone cannot prove normality; a fake source matching a short initial segment retains the same mirror. Nothing here infers the signed estimate from source identification alone.

## NOT run / NOT claimed

- Full current SUCC >10,000 root test suite, `scripts/verify_provenance.py`, full-tree observer/ordinal/foundations probes on a genuine current checkout. Direct `git ls-remote` failed due GitHub DNS in the container; live GitHub connector reads supplied parent provenance and will be used for pushed additive commits.
- New Lean declarations or proof kernel receipts; outside referee; physical quantum mechanism; universal Fourier cancellation, RH or π-normality theorem.
- A proof of AR-08's selected signed single-quadrature `o(N)` estimate. Only the exact *conditional criterion*, its algebraic denominator, and finite source error are established.

**PASS:** source-faithful type and algebraic proof checks, exact finite source estimates, irrational mirror/negative controls, local integration proxy. **OPEN:** analytic selected mirror symmetry / signed saving at all horizons. Do not promote status based on CI, numerical signs, geometric covariance or operator normality.
