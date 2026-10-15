# RH research candidate — source-canonical Suzuki 30-moment Schur

**SUCC branch:** `research/suzuki-canonical-moment-schur-2026-10-14` (draft); pinned parent PR #85 at `dc6b7e3...`, sibling AMW theorem PR #86 at `205ffd02...`. No write to `FuckingRH`; **RH OPEN**.

**Authentic original completed source**: Suzuki's signed compact `G_a` on `H=L0²(-a,a)`, with true prime-power/Gamma/pole/contact/half-density; `Q_W(v)=<G_a(i v'),i v'>` from classical theorem.

1. At a=1/2, the source-true AMW-06B inequality `Q>=369/10000||v||²` on 30-moment null gives `P_high G_a P_high >= κ P_high(-Δ_N)^-1 P_high`. **Not >=κ I**.
2. Canonical `H_low=span{P_1(x/a),...,P_30(x/a)}` in the mean-zero derivative Hilbert space and complement `H_high`; exact low inverse Neumann metric has only boundary pairs 29↔31 and 30↔32. The original G cross coupling need not be sparse. Reflection splits the 30 low modes into two 15-mode parity sectors.
3. Compact spectral theorem plus relative high positivity proves the nonpositive Morse index (including kernel) of **the authentic** `G_(a=1/2)` is at most 30. This bound is NOT a positive spectral statement.
4. For λ>0, the bounded high resolvent `(D+λI)^-1` exists and a true Feshbach `S_λ=A+λ−B(D+λ)^-1B*` has 30 finite coordinates. `G+λI>=0 ↔ S_λ>=0`. An unshifted bounded `D^-1` is unjustified.
5. Source-pinned PR #85 cell stages give an exact rational 30×30 S_N(λ) via Woodbury, with fully derived symmetric operator error. **Better:** missing original Gamma modes are positive, so monotonicity of shorting bounds S_true from below by a spatial-only defect `E_one(λ)`, and the positive Gamma tail appears only in λ-invertibility. No arbitrary covariance substitution.
6. The current parent Lipschitz grid error bound at a=1/2 is >=11/N. Existing N<=24 cannot reach λ near 10^-4; 110001 or more cells would be necessary for that particular crude error *method*. This is no impossibility theorem for other certified quadrature.
7. The AMW unprojected `R_full=<Af,Af>` sufficiency may fail even for diag(10,1)>=0. Source-correct projected or regularized cross interactions must be used.

**Reproduction:** see `research/2026-10-14/SUZUKI_CANONICAL_MOMENT_SCHUR.md`, exact tests, deterministic receipt and focused CI on 3.10/3.13. Parent source sha must match. No nontrivial zeros input, Lean proof, sign verdict or academic novelty claimed.

**Next verdict-changing experiment:** analytic certified Legendre matrix elements of actual `g_a` and action on high sectors, with source-specific resolvent preconditioners and direct 15×15 Schur enclosure at λ→0. Preserve source mutations (fake 6, incorrect Gamma/parity/conductor) and seek real interval margins, not numeric matrix eigenvalue guesses. To prove RH still need all `a>0` and full authentic signed sign.

### Direct analytic signed source low-matrix upgrade (SM-10–13, second checkpoint)

For the actual Suzuki low Legendre modes on L0², each genuine Gamma OU term has **exact** rational+single-exponential form `A_ij+B_ij exp(-2alpha*a)`; the genuine first p=2 prime hinge is a rational polynomial in `log 2` multiplied by `log2/sqrt2`. Contact = `-C_G K`, pole=`-8cc*+8ss*`. The new `suzuki_legendre_source.py` computes intervals of **the original signed Gamma-J low block** without a spatial grid, removing the previous *method-specific* ≥11/N cell-Lipschitz barrier for low-block evaluation. Missing Gamma is PSD and not charged against a lower sign. **Unbuilt:** actual high-resolvent/cross response, sufficiently sharp complete 30×30 matrices at useful J, λ→0 all-test Schur PSD and any RH conclusion. Independent 55-digit original-source integration agrees on 18 low entries, diagnostics only. Provenance pinned to exact PR #85 source module; modified or absent source fails closed.
