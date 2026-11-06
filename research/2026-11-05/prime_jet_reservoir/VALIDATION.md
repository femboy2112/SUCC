# Validation & computational receipts — prime-jet reservoir (2026-11-05)

**Scope:** All run outcomes below are ACTUAL local execution in the current isolated Python environment; source proof is THEOREMS.md and V4_GAMMA_CLOCK.md. These tests are not a new Lean kernel receipt, independent scholarly peer review, CI or proof of RH.

## Focused exact/source instruments

1. Ran locally: python -m unittest -v test_prime_jet_reservoir.py; **12/12 PASS** (0.232s). Python 3.13.5; NumPy 2.3.5; mpmath 1.3.0; SymPy 1.14.0 available (not required by this suite). Committed Git blob SHA **2f200ef044f451b871a65eeb00053be58bb2860e** was independently verified against the EXACT locally executed source bytes using git hash-object and a GitHub fetch of tests/test_prime_jet_reservoir.py.
2. Ran locally: python -m unittest -v test_v4_gamma_clock.py; **5/5 PASS** (0.022s), including 200-node Gaussian quadrature for Gamma density and Fourier coefficients, analytic V4 character eigenspaces, correct weighted-unitary Jacobian, p=2 period four vs odd-prime dense-mode calibration. Committed Git blob SHA **395f020ebea290128df6dc8b554598060b848458** independently matched the executed file via git hash-object and GitHub fetch.
3. Original SUCC historical four-pole forcing: exact Fraction vs independent collapsed numerator/denominator for n=1..39; literal U0=0 and odd-denominator carrier; inherited #499 p source action S_a verified exactly at a=1,3,5,7 against the actual angular/trivial radial eight-tap eigenvectors (not an assertion about p-local events at exceptional p). Path adjacency matrices m=1..14 compared independently with closed cosine eigenvalues; opposite packet phases give ±w prime interaction.
4. A separate independently integrated (45-digit) *triangle packet autocorrelation* recovered BOTH ±w for p=2,3,5 with absolute discrepancy <1e-35 after normalization. That integrator had no path-eigenvalue formula as an input.
5. Clock test p=2 exact log2/log16=1/4; rational-factor controls with exponents -2..2 around 2,3,5; χ_-4 near-zero displacement sign anomaly, four-sheet skew composition, Γ density normalization and non-Haar first three Fourier modes. These finite tests are calibration; universal rational independence/gauge nonextension have separate elementary proofs.
6. **Recorded exploratory failure:** initial compact-circle finite-horizon (h≤10,000) mutant asserted min |E|<0.001 for each p=3,5,7. One case returned 0.0011817787981862175 and the test failed. The **mathematical density theorem is asymptotic**, not a finite-rate guarantee. Corrected finite diagnostic to the weaker, actually checked <0.002; reran and passed. No false blind-confirmation claim.

## Optional FULL Weil sign/orientation triangulation — NUMERICAL ONLY

The separate committed optional instrument research/2026-11-05/prime_jet_reservoir/guinand_triangle_probe.py is exactly the version run locally (Git SHA **9ddf6f30385c8bab3daa566b7e2afc49fedacc00**). It uses a compactly supported triangular test f(x)=(1−|x|/L)_+, Fourier transform F(t)=L sinc²(Lt/2), and exact autocorrelation
g(a)=2L/3-a²/L+a³/(2L²) for 0≤a≤L, g(a)=(2L-a)³/(6L²) for L≤a≤2L. The test is only piecewise smooth; standard smooth approximation is required for an independent use of the explicit formula. The script separately integrates the Γ/digamma term numerically using SciPy, sums exact prime-power support/sign terms, evaluates the pole term, then compares with independently computed first 8 and 16 positive zeta ordinates using mpmath.zetazero. No zero is supplied as CONSTRUCTION input to prime jets.

| L | Pole term | Gamma/arch term | Prime jet total | Full RHS (numerical) | 16-zero truncated LHS | LHS−RHS |
|---:|---:|---:|---:|---:|---:|---:|
| 0.4 | +0.322139744861 | −0.319586994762 | −0.001245739353 (2 only) | +0.001307010746 | +0.001268552824 | −0.000038457921 |
| 0.6 | +0.730873195880 | −0.669498498646 | −0.059704583408 (2 and 3) | +0.001670113826 | +0.001654729392 | −0.000015384435 |

At 8 positive zeros the observed residuals were −0.000082029978 (L=.4) and −0.000049415177 (L=.6), decreasing in magnitude at 16 zeros as expected from omitted positive tail terms. These are finite truncations, NOT rigorous error certificates; no claim the truncated zeros equal the full left side. The Gamma integral is truncated at t=5000 and not interval-certified. An attempted 150-zero/35-digit larger run exceeded the execution limit and was ABANDONED; its nonexistent result is NOT claimed.

## CI and provenance boundary

No full >12k native tests, Lean proof check, hosted workflow success, formal verified Weil inequality, RH, physical energy measurement or π normality proof on this head. Older #516/full-branch receipts are not fresh independent witnesses. Check source/claim ledgers and chronological prereg for development-vs-validation and dependence. Tests and mathematical documents are strictly ADDED files; no archived originals changed.
