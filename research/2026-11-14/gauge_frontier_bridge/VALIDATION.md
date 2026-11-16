# Validation — Gauge-Anchored π / RH Frontier

**2026-11-14.** Research only. A scoped, programmatic local finite analysis of a source/observer no-go and known theorem imports, not a new π/RH proof. The actual zeta or π infinite claims remain open.

## Exact execution evidence

- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_gauge_frontier_bridge.py' -v`: **14/14 PASS** in an isolated working directory, using the standard-library `fractions.Fraction`. Raw output: `receipts/focused_tests.log`.
- `python research/2026-11-14/gauge_frontier_bridge/independent_sympy_oracle.py`: **PASS**, independently constructing the two complex-sample even-function polynomial impostor, checking all jets through second derivative, and directly reconstructing **80** authentic BBP four-pole Green residuals without importing the main module. Numerically evaluates exact Lagarias expression for n=1..256 with 85-digit mpmath as a separate *noncertifying* sanity check. Raw output: `receipts/independent_sympy.log`.
- `python -m compileall -q ...`: **PASS** for the three new Python sources.
- Separate exact-rational finite Lagarias certification from `lagarias_rational_interval(n,16,30)` on **all 512 integers** `1≤n≤512`: **511 strict PASS** (`n>1`), **1 equality** at `n=1`, **zero ambiguous**, **zero negative**. `receipts/lagarias_rational_512.json` records exact numerator/denominator for the tightest positive rational lower gap, occurring at `n=2`. **This is a finite certificate, not RH.** Arithmetic uses two rational enclosing series for `exp(H)` and `log(H)` with explicit tail inequalities. One less accurate lower truncation returning a negative bound is tested to produce *no false conclusion* about the true target.
- The original four-pole forcing and exact truncated Green-cocycle residual are validated for clocks 0..8 and depths 0,1,2,3,5,9 in focused tests, with independent SymPy controls for 80 clock/depth pairs.
- The polynomial finite-jet model validates preserved even/real reflection, nonreal zeros at `±iβ`, equality at all selected finite observation points and jets, and explicitly rejects any claim that the mutated entire function is the original Euler product.
- The elementary phase-bound coefficient is exact, not a claim about any infinite real circle orbit or a π normality estimate.

## External theorem authority (NOT derived or numerically certified here)

- Rodgers–Tao, `Λ≥0` for the **canonical** de Bruijn–Newman deformation; the classical `RH⇔Λ≤0`; hence `RH⇔Λ=0`. `https://arxiv.org/abs/1801.05914`.
- Lagarias (2002), authentic `RH⇔∀n` divisor-sum inequality. `https://arxiv.org/abs/math/0008177`.
- Platt–Trudgian (2021), interval-arithmetic finite-height zero verification. `https://arxiv.org/abs/2004.09765`.
- π Weyl/Haar criterion, normality-preserving finite digit edits, explicit BBP evaluation and exact signed Green transport are **classical/SUCC existing results**; see `docs/PI_NORMALITY_FRONTIER.md`.

## Source and gauge firewalls

1. **Do not replace the selected BBP seed** (`U0=0`) with a nearby seed, a Haar ensemble or the coherent counterseed `−π/16` while claiming source-specific normality. The mathematical finite-completion rivals are **changed-source** controls.
2. **Do not replace genuine `ξ(s)`/Euler product with `cos(z)Q(z)`.** The latter is a fully specified **countermodel to symmetry-plus-finite-jets** only.
3. **Do not call de Bruijn–Newman heat time a gauge**: varying heat time changes the function and the zero target. The `z↦−z` center symmetry is a mathematical involution, not an asserted physical gauge redundancy.
4. **Do not infer impossible proof access from finite model saturation**. If RH is false, its universal RH-equivalent statements have finite counterexamples; if RH is true, a global analytic proof may exist. No independence result is provided.
5. **Keep π and RH sign targets distinct.** BBP's real-circle signed Weyl saving has no demonstrated source-preserving map to the complete signed Weil quadratic functional; neither is forced by positive moment matrices or unitary imagery.

## Missing external gates

- No independent blind peer review or new Lean kernel certificate.
- No full clone of SUCC for local root tests; required checks are **not claimed locally**: `scripts/verify_provenance.py`, full repository test discovery, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`.
- No claim of certified 2026 new strongest finite-height zero check beyond the cited Platt–Trudgian primary result.
- No empirical hardware/source instrumentation beyond finite arithmetic and exact controlled computation; no proof of RH, π normality, π R0, or undecidability.

**Repository action:** additive separate branch stacked on PR #630; verify exact-head GitHub CI after push. Manifest `FILE_HASHES.json` records local source identities; remote blob readback is a separate Git verification step. New source is not an authenticated physical gauge or arithmetic-source replacement.
