# π exponent two: transported determinant proof spine and SUCC observer interpretation

**23 November 2026 — exposition/transport, not an independent π irrationality-exponent proof.** Primary source: OpenAI, *The irrationality exponent of π is 2* (September 24, 2026), [main.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex), [interpolation](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex), [determinant](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/determinant.tex), [conclusion](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/conclusion.tex), and [published Lean formalization](https://github.com/openai/math/blob/main/lean/docs/017.md). Compare the very different p-adic theta-period mechanism in the Alpöge–Claude verified RH proof and SUCC #687; the following is a source-grounded structural comparison, not an identification of the two mathematical proof objects.

## The external theorem and its quantifiers

For every real ν>2, there is a threshold Q(ν) such that **every** rational p/q with q≥Q(ν) satisfies

\[
|\pi-p/q|\ge q^{-\nu}.
\]

The same external manuscript proves irrationality, and Dirichlet's theorem supplies the universal lower bound μ(π)≥2; consequently μ(π)=2. **The threshold is not asserted effective**, and μ=2 does not imply |π-p/q|≥c/q² uniformly.

## Proof spine (each input explicitly attributed)

**P1 — Construct hypothetical arbitrarily good approximations.** Fix ν>2 and suppose arbitrarily large q admit |π−p/q|≤q^(−ν). Select a finite family p_i/q_i of exceptionally good approximants at **successively separated scales**. Let w_i=ceil(log q_i), r_i=2i p_i/q_i, and c_ji=j r_i for j=0,...,K−1. Because π is approximated, c_ji is close to the exact logarithmic period j ω with ω=2πi. These are deterministic rational hypothetical inputs, **not independent samples of primes**.

**P2 — Obtain a nonzero common observation determinant.** The deep *Separated-weight interpolation theorem* (external, interpolation.tex) says: choose the weights w₁,...,w_m successively large with thresholds independent of the centers; under K θ^m<1 and K (w₀/v₀)θ^m<1, the polynomial map

\[
P(Y,X_1,\ldots,X_m)\mapsto
\bigl[P(1+t,c_{ji}+u_i+\log(1+t))\bigr]_{j<K}
\]

surjects onto all jet coefficient packets of weight v₀s+Σ_i (w_i/θ)β_i<H for sufficiently divisible, large H. Truncated logarithm jets G_i(t) are a filtration-preserving coordinate change. Form the matrix of these finite jet evaluations on all monomials in a **full weighted simplex**; surjectivity forces an M×M full-row minor Δ_H≠0. This theorem depends on its own local multiplicity and algebraic-curve/positivity argument on blow-ups; SUCC **has not reproved that algebraic geometry**.

**P3 — The arithmetic readout cannot be arbitrarily small.** The selected entries lie in Q(i) after the appropriate scaling of rows and columns. Clearing the exact q_i and truncated-logarithm LCM denominators gives a **nonzero Gaussian integer determinant**, whose modulus is at least 1. The external Arithmetic Lower Bound lemma yields

\[
\frac{\log|\Delta_H|}{M H}\ge-(1-\bar b)-E_{\rm ar}.
\]

The crucial fact is that nonzero rank, integer-lattice provenance, and the denominator budget refer to the **same determinant**, not separately fitted matrices.

**P4 — The analytic readout has two incompatible saving mechanisms.** Translate the rational centers to exact periods j ω; the approximation errors are O(q_i^(−ν)). The translation tests entire functions f_(a,P)(z)=[u^a]P(e^z,z+u). Rows within one transverse-index group a probe *the same* entire Taylor-coefficient sequence. Repeated Taylor degrees annihilate determinant terms. The external Collision Estimate proves, with c=(log2)/4,

\[
|\det T|\le
\exp\{-c\sum_a n_a^2+MH(E_{\rm hol}+o(1))\}.
\]

If at least ηM rows lie in few low transverse groups, Cauchy–Schwarz forces Σ n_a² large, hence a collision saving. Otherwise most rows have high transverse degree and the approximation errors give a ν-dependent saving. The Determinant Comparison proposition combines them:

\[
\frac{\log|\Delta_H|}{MH}
\le E_{\rm an}+o(1)
+\max\{-c L_H,\ -\nu(A(1-\eta)-\bar b)\},\quad L_H\to L.
\]

This is the *technical mechanism*; phrases such as "hidden information exceeds capacity" are not substitutes for these explicit inequalities.

**P5 — Parameter choice makes the two bounds contradictory.** Fix ν>2. Choose a rational b with 1/2<b<1−1/ν; for sufficiently small positive rational δ let θ=1−δ and A=1−bδ. Then ν(A−θ)>1−θ and A²<θ. Choose rational A/θ<C<1/A and rational A<B<min(1/C,C θ); finally sufficiently small η>0. Take m large, K=floor(C^m), w₀=B^(−m), v₀=2K θ^m w₀. The dimension-dependent errors vanish and L=η²(B/A)^m/(2(m+1)) grows without bound. Then choose **actual** hypothetical exceptional denominators q_i successively far apart to make the remaining error terms small; only after all m, weights, centers have been fixed let H→∞. This gives the explicit contradictory conditions

\[
g:=\nu(A(1-\eta)-\theta)-(1-\theta)>0,\quad
E_{\rm ar}+E_{\rm an}<g,\quad
cL>1+E_{\rm ar}+E_{\rm an}.
\]

Thus the assumed arbitrarily good rational approximations cannot exist. The conclusion proves μ(π)≤2, and classical Dirichlet approximation gives equality.

**Exact finite calibration of one parameter instance (not a proof of P2–P5).** For ν=21/10, choose b=51/100, δ=1/1000, θ=999/1000, A=99949/100000, C=2001/2000, B=3997979/4000000, η=1/1000000. Every elementary ordering/positive-gap premise above holds by exact fractions, including g=26901071/10^12>0. See the focused test.

## Iroh map into Principia / SUCC

- **External carrier / predicted observation:** the source laws are e^ω=1, the rational approximation hypotheses and the logarithmic curves; SUCC's internal model is a finite polynomial jet representation with exact weights and expected periods.
- **Observer discrepancy:** displacements u_i measure *transverse deviation of rational centers from actual periods*. The same matrix is read arithmetically (nonzero Gaussian integer after clearing denominators) and analytically (collision and small approximation errors).
- **Two-observer agreement constraint:** those two readouts have to be compatible **for that same matrix**. Under ν>2, sufficiently separated scales make them incompatible; so the hypothetical rational source law fails. This is a genuine mathematical instance of SUCC's "observer detects a failed external model" architecture.
- **Why new measurements matter:** the interpolation theorem buys full rank through genuinely independent jet directions. In contrast, Iroh theorem I7 proves that perturbing prime weights after compressing them into the scalar x_X gives a rank-one endpoint-phase Jacobian. **More observations of the same lossy representation do not recreate missing source rank.**
- **RH analogue and nonidentification:** Alpöge–Claude uses a normalized arithmetic theta-lattice, p-adic multiplicity and Archimedean capacity; the π exponent paper uses Q(i) interpolation determinants, transverse-degree collisions and approximate logarithmic periods. Their high-level "integer nonzero lower bound vs analytic upper bound" architecture is shared, but their lattices, local inputs, error budgets, and determinants are **not interchangeable**.

## Open bridges and hostile controls

**π normality remains OPEN.** The interpolation proof is a contradiction from approximations |π−p/q|≲q^(−ν) with ν>2; it says nothing about the signed radix-16 Weyl mean on a positive proportion of every late shell. SUCC #686 supplies the decisive generalized Kempner μ=2, nonnormal control. To transfer the determinant strategy to normality, a new source-authenticated nonzero arithmetic matrix must be constructed from the *actual original four-pole BBP prime/cofactor/carry journal* such that a hypothetical R0 failure forces analytic smallness on that **same matrix**. This demands more than phase interpolation and more than GRH prime marginals. Counterseed −π/16, rational phase aliases, the nonnormal μ=2 control, fake Λ(6), missing 1/k, and rank-one endpoint Jacobian must be tested before any claim promotion.

**Claim scope:** P1–P5 are a human-readable **proof map importing the actual published interpolation, determinant and conclusion lemmas**. The only separately locally executed result here is the stated exact finite parameter witness; no new proof of those deep imported lemmas or Lean rebuild is claimed. The SUCC observer interpretation is an explanatory model, not a new theorem equating RH and π's mechanisms.
