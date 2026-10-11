# Gamma–actualization interferometer: finite arithmetic against an Archimedean response

**2026-10-10 — RH OPEN.** This research round constructs and tests a *finite causal readout*, not a new positivity proof.

**Starting state:** actualization/Yoneda branch research/2026-10-10/yoneda-resource-actualization-v1 at 8846993ea0ebd9ea3c156c864376f6f554ad19bd. Default branch main, 22b6dadbd1983159e6c5d8cc32fb9aeff6925ec6, was not modified.

**Implementation:** actualization/gamma_interferometer.py. **Controls:** tests/actualization/test_gamma_interferometer.py.

**Primary literature:** Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), https://doi.org/10.1112/jlms.12785 (Eq. 1.1, Theorems 1.2 and 1.7). Related but weaker: Connes–Consani, *Quasi-inner functions and local factors*, https://arxiv.org/abs/2008.10974 (finite-place Hardy quasi-innerness, not Weil positivity).

## 1. Hypothesis versus repair

User's model: the Gamma factor fixes the already-actualized analytic field; finite-place arithmetic events are a discrete radiation signal measured and correlated against it. Here that picture becomes an explicitly defined map from an integrated arithmetic source to the Archimedean-plus-pole Suzuki response. Neither a physical black hole nor an unknown Gamma interior is asserted. Gamma alone does not define the missing positive Hilbert-space polarization.

There are **two separate obligations**: check that actual finite observations retain the arithmetic Euler-source structure, and derive an *independent, non-circular* positive global pairing identified with the full Weil form. This round implements the first bridge, and proves a no-go for one tempting realization of the second.

## 2. Exact source algebra, no zeros and no future events

For rational arithmetic coefficients \(a(n)\) with \(a(1)=1\), the Dirichlet-convolution logarithm exists coefficientwise:

\[
b=\log_*a=\sum_{r\ge1}\frac{(-1)^{r+1}}{r}(a-\delta_1)^{*r}.
\]

Every factor in a nontrivial convolution is at least 2, so the coefficient at n receives no contribution beyond \(r=\lfloor\log_2 n\rfloor\). Moreover, **b(n) depends only on the coefficients a(d) for d dividing n**. The relation \(-D'(s)/D(s)=\sum_{n\ge2}b(n)\log(n)n^{-s}\) holds as a formal logarithmic derivative and analytically in its convergence region.

Fix the pole and Archimedean response, for \(t\ge0\):

\[
\begin{aligned}
A_\infty(t)={}&4(e^{t/2}+e^{-t/2}-2)
+\frac t2(\psi(1/4)-\log\pi)\\
&+\frac14\left(\pi^2+8G-e^{-t/2}\Phi(e^{-2t},2,1/4)\right).
\end{aligned}
\]

Define the *zeta-normalized finite-source diagnostic*

\[
\boxed{\Psi_a(t)=A_\infty(t)
-\sum_{2\le n\le e^t}\frac{b(n)\log n}{\sqrt n}(t-\log n).}
\]

For the true zeta prefix \(a(n)=1\) through N, unique factorization yields \(b(p^k)=1/k\), and b(n)=0 at non-prime-powers. Therefore

\[
\frac{b(p^k)\log(p^k)}{\sqrt{p^k}}
=\frac{\log p}{p^{k/2}},
\qquad
\boxed{\Psi_a(t)=\Psi_{\mathrm{Suzuki}}(t),\quad0\le t\le\log N.}
\]

That is a **finite exact identity**, not positivity. For a fake or non-zeta source, the response deliberately keeps zeta's archimedean completion fixed as an *experimental control*. It is NOT the completed explicit formula of an arbitrary other L-function; those may have different conductor, root number, Gamma factor, or complex coefficients. Non-real sources are refused.

The implementation reads only coefficients the Engine has *integrated*, never a pending step, a prediction, a shadow event, or any source above N. Missing coefficients cause an explicit error. It retains the Engine journal head, and provides integer-labelled event evaluation to avoid the floor(exp(log n)) rounding trap. mpmath is loaded lazily; the original finite actualization engine keeps its standard-library-only dependencies.

## 3. A genuinely discriminating actualization probe

Each prime-power event is a ramp: the function value is continuous at activation, while the derivative jumps. Distributionally the second derivative records the impulses. An elementary one-sided derivative calculation gives

\[
\boxed{
\Psi'_a(\log m+)-\Psi'_a(\log m-)
=-\frac{b(m)\log m}{\sqrt m}.
}
\]

**Pre-registered control:** change only the direct source coefficient a(6) from 1 to 3/2. The exact connected coefficient becomes b(6)=1/2, where the correct Euler product has b(6)=0.

- At the event time \(t=\log6\), both responses have **identical values**.
- A new derivative jump appears: \(-\log6/(2\sqrt6)\approx-0.365741370117396\).
- By the next event at \(t=\log7\), the difference is exactly \(-\log6\log(7/6)/(2\sqrt6)\approx-0.05637928084454949\).
- Higher connected mutations are generated algebraically at later composites, not silently promoted into new primes.

A mutation of a(2) changes a prime tower and is classified separately. This makes the distinction between a source-correct prime-power event and a fake mixed composite **operational**, with no zero locations or numerical fitting.

## 4. Exact no-go: separate radiation detectors cannot each be PSD

The global Suzuki screw candidate is

\[
G_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
\]

An isolated impulse of weight w at log-location \(a>0\) contributes the kernel

\[
K_{a,w}(t,u)=-w\left[h_a(t)+h_a(u)-h_a(t-u)\right],
\quad h_a(t)=(|t|-a)_+.
\]

Take \(t_1=3a/4\) and \(t_2=5a/4\). Then

\[
[K_{a,w}(t_i,t_j)]_{i,j=1}^2
=\begin{pmatrix}0&-wa/4\\-wa/4&-wa/2\end{pmatrix},
\qquad
\boxed{\det=-w^2a^2/16<0}.
\]

This is a **proved exact counterexample** to positive screw kernels built independently, one impulse at a time. It is negative for *either* sign of nonzero w. It does not rule out complete prime towers, nonlocal interactions, Gamma cancellation, or a source-derived global Hodge-type pairing. The repo already contains analogous no-gos for independent increments; this is a direct, reusable micro-obstruction at the actualization interface, **not independent evidence of an RH breakthrough**.

## 5. Calibrated outputs and claim ledger

The tests recover the existing Suzuki regression values \(\Psi(0.1)=0.05313043381777025410\ldots\) and \(\Psi(1)=0.04400730523685252686\ldots\); verify the Gamma term by a separate convergent exponential sum instead of Lerch Phi; assert b(6)=0 and b(8)=1/3 exactly; test future-access denial; and confirm the fake-six step and the negative determinant. Numerical values use high-precision mpmath, *not certified interval arithmetic*. For prior bounded certified Suzuki checks see scripts/event_dynamics.py.

**DISClOSED in elementary finite scope:** exact Dirichlet-log support, causal-prefix dependence, slope-jump law, negative two-point isolated-impulse determinant. **OBSERVED:** bounded high-precision evaluation and mutation responses. **UNVERIFIED:** an independently positive, exact full Weil pairing. No proof of RH is claimed.

## 6. The real next theorem

Construct compatible nonlocal arithmetic/Archimedean sesquilinear pairings \(B_N\) on a declared Mellin/Schwartz core, together with inclusions that control the **unbounded logarithmic form norm**, so that:

1. Inputs are genuinely integrated Euler data, including exact prime-power clocks and half-density; composite and log-clock mutations falsify inappropriate constructions.
2. The adjoint/polarization is **defined from source geometry** and proved positive without using zeros, RH, or square-root/Cholesky of the target.
3. Archimedean renormalization is carried out before taking limits; a domain-controlled theorem proves \(\lim_N B_N(f,g)=Q_{\rm Weil}(f,g)\).
4. A matched Hecke Euler-product versus non-Euler-product Davenport–Heilbronn test distinguishes arithmetic admissibility from generic completion symmetry.

**Pass:** an independently proved positive completed Weil form, with uniform control of the limit. **Fail:** isolated-event positive squares, generic fake-arithmetic-insensitive covariances, analytic completion alone, or finite PSD scans. **Ambiguous:** finite agreement with no form-domain/exhaustion theorem.

The correction to loose language matters: \(Q=P-K\) is a *linear* sum of forms. Its **global positive sign** is not a sum of independently positive pieces. The hoped-for nonlinear Gram/Schur/Hodge witness must actually be constructed; describing it as a “cross-term” does not construct it.
