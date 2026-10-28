# Oily Macaroni III — the authentic positive field and its Gamma free-energy cocycle

**2026-10-26 · Research draft #307.** Original four-pole BBP forcing and zero initial condition unchanged. Mathematical virtual paths are not physical virtual particles. **Pi base-16 normality and RH: OPEN.** Classical components: Laplace transforms, exponential families, harmonic regularization and Boltzmann–Gibbs normalization; no academic-priority claim.

## 1. One positive carrier, two representations

Let $a_n=8n-7$ and

$$
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0,\qquad
R(a)=\int_0^\infty e^{-ax}Q(x)\,dx.
$$

Exactly $R(a_n)=r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)$, the authentic BBP forcing. With unnormalized $\rho_n(dx)=e^{-a_nx}Q(x)\,dx$, the positive cone evolves by **actual source-time multiplication**:

$$\boxed{\rho_{n+1}(dx)=e^{-8x}\rho_n(dx),\qquad \operatorname{mass}(\rho_n)=r(n).}$$

Projectivizing to probability measures $\mu_n=\rho_n/r(n)$ produces the exact finite source-conditioned Boltzmann–Gibbs update

$$
\boxed{\mu_{n+1}(dx)=\frac{e^{-8x}}{Z_n}\mu_n(dx),\quad
 Z_n=\mathbb E_{\mu_n}[e^{-8X}]=\frac{r(n+1)}{r(n)}\in(0,1).}
$$

The current potential is $V_n(x)=a_nx-\log Q(x)+\log r(n)$. This changes **mathematical** admissibility weights on the same positive carrier. The raw update is linear; only mass normalization is nonlinear. It asserts no physical vacuum probability.

Since $e^{-8x}$ decreases with $x$, covariance shows $\mathbb E_{\mu_{n+1}}f\le\mathbb E_{\mu_n}f$ for every increasing integrable $f$. The source field increasingly concentrates near the positive boundary.

## 2. Multiplicative SUCC becomes a logarithmic path integral

Each $Z_n$ is rational. The positive free-energy step has an exact continuous/discrete identity using that SAME carrier:

$$
-\log Z_n=\log\frac{r(n)}{r(n+1)}
=\int_{a_n}^{a_n+8}\mathbb E_{\mu_a}X\,da,\qquad
-\partial_a\log R(a)=\mathbb E_{\mu_a}X.
$$

It telescopes without any infinite-limit interchange:

$$
\boxed{\sum_{n=1}^{N-1}(-\log Z_n)=\log\frac{r(1)}{r(N)}.}
$$

The original source zero $Q(0)=0$ and derivative $Q'(0)=15$ give $r(N)\sim15/(64N^2)$. Thus the positive path free energy grows like $2\log N$.

## 3. The source's genuine Euler–Mascheroni finite part

Compare with the harmonic SUCC clock $2H_{N-1}=2\sum_{n=1}^{N-1}1/n$:

$$
\boxed{
\mathcal F_N=\sum_{n=1}^{N-1}
\left(\log\frac{r(n)}{r(n+1)}-\frac2n\right)
=\log\frac{r(1)}{r(N)}-2H_{N-1}.
}
$$

The summands are $O(n^{-2})$, so the limit exists absolutely. Using $r(1)=47/15$, $r(N)\sim15/(64N^2)$ and $H_{N-1}-\log N\to\gamma$, we obtain

$$
\boxed{\lim_{N\to\infty}\mathcal F_N
=\log\frac{64r(1)}{15}-2\gamma
=\log\frac{3008}{225}-2\gamma.}
$$

**Gamma appears without insertion into any finite source measurement.** It is the classical additive/harmonic-vs-logarithmic finite-part correction to the original positive multiplicative SUCC, with a source-specific rational normalization $3008/225$. This is an exact realization of the user's positive-field/continuous-boundary comparison.

Along Fibonacci cutoff $N=F_m$, $\log F_m=m\log\varphi-\frac12\log5+o(1)$, so

$$
\log\frac{r(1)}{r(F_m)}-2m\log\varphi+\log5
\longrightarrow\log\frac{3008}{225}.
$$

The golden clock is a different **declared cofinal reference**. It does not automatically force $\varphi^{-1}-\gamma$. That constant arises in the companion complex first jet after selecting the exponential-law Laplace fixed point; the authentic BBP endpoint's Gamma(2) limit has a different Laplace fixed point. Preserve these source and gauge types.

## 4. Separate signed arithmetic work remains

All $Z_n$ are positive. Their product and Gamma finite part imply no cancellation of $e(hU_n)$ without a separate source-selected signed inequality.

The companion [Hilbert-to-original-Weyl theorem](OILY_LOG_CLOCK_HILBERT_TRANSPORT.md) constructs a source-faithful window embedding with **uniform $O(N^{-1/3})$ error**; this removes a representation-transfer gap but does not prove the weighted signed sum is small. The Oily–Macaroni first jet cancels in relative two-time phases; it is not an automatic signed invariant.

A positive changed source $Q+\epsilon e^{-6x}(1-e^{-x})^3$ retains the first two endpoint jets and leading finite-size constants while changing the actual forcing. No normality status is asserted for that counterfeit. This prevents a false claim of unique source selection by a shared first jet.

## 5. Executable authority

Source module: observational_succ/oily_macaroni_transfer.py, with **exact rational** positive_field_step and finite_field_free_energy_data. Tests: tests/test_oily_macaroni_transfer.py. Local isolated tests **26/26 passed**, including exact telescoping, source identity, stochastic mean monotonicity, finite Gamma limit consistency, Frullani positivity and complex path holdouts. This is *not* a preclaim of full repository or hosted exact-head CI. Historical source files remain unchanged. No new Lean authority or scientific proof of pi normality/RH.

**Next falsification:** prove or obstruct a signed source-conditioned cross-window inequality on the real BBP phases using this exact field; do not promote positive reweighting itself to a cancellation theorem.
