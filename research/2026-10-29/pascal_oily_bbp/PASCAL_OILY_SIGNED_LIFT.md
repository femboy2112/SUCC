# Operation Pascal ↔ Oily ↔ BBP — authenticated binomial wavefront and signed inverse

**2026-10-29. Research only.** Exact parent SUCC draft #369 at `95f368719a1e020e8bf5b9312b10260a94a0a519`, stacked on #367 at `b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`; live main at first inspection `ac7303b2e0e2ec16e3b1d88d186324e1fae65ea5`. No edits to main, archived BBP source, `U_0=0`, proof IDs, production modules, or workflows. This is a new **declared binomial observation** of an already authentic positive source, not an observation instrument proven uniquely physical. The inherited signed BBP digit sequence is deterministic; no stochastic digits are asserted. **Pi base-16 normality remains OPEN.**

## 0. What this actually adds over previous Pascal and Oily work

Older SUCC Pascal research, especially `research/2026-10-24/PASCAL_CARRY_INTERFEROMETRY.md`, `PI_PASCAL_MAHLER_SOURCE.md`, `PI_PASCAL_ADVERSARIAL_BOUNDARY.md`, and `PASCAL_THREE_SOURCE_COHERENCE.md`, already proves source-specific Pascal finite differences, valuations, 16-bit Walsh profiles, and independent-source controls. PRs #367–#369 already provide a positive original-four-pole convolution carrier, its Oily packet grammar, Gamma-rank triangle, exact Green mixture, and finite log-correction. No credit is claimed for Lucas, Kummer, beta-gamma algebra, Poisson-gamma mixing, or the original BBP series.

The genuinely new-to-this-round interface is a **Pascal Bernoulli-thinning observation applied directly to the original four-pole positive forcing carrier**, with rational finite probabilities, a proved explicit `O(1/n)` total-variation transfer to the exact original Oily two-channel endpoint, and a *selected-phase* Fourier lift with an explicit stable Oily inverse. The natural scale `number of trials = source time n` is declared. Replacing this clock changes the limit. The new finite golden fixed-point branch and original-source first-order fingerprint make the clock and the four poles observable in exact rational controls.

## 1. Source passport and finite Pascal sheet

For `n>=1`, preserve the authentic four-pole rational function

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Let `a=8n-7`, `Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}` and

\[
R(a)=\int_0^\infty e^{-ax}Q(x)\,dx=r(n),\qquad
\mu_n(dx)=\frac{e^{-ax}Q(x)}{r(n)}\,dx\quad(x>0).
\]

The **new, explicit mathematical observation instrument** is: given `X~mu_n`, run `n` conditionally independent Bernoulli trials, each with probability of a **failure** `p(X)=1-e^{-8X}`. Let `J_n` be the number of failures. The parameter `8` is not a fitted number: each authentic source-time increment changes `a` by `8`. The `n` trials are chosen to match the source index `n` (a *clock convention*, not a theorem about physical observers).

**Theorem PO-1: exact original-source Pascal probabilities.** For every `n>=1` and integer `0<=j<=n`,

\[
\boxed{q_n(j)=\Pr(J_n=j)
=\frac{\binom nj}{r(n)}\sum_{k=0}^{j}(-1)^k\binom jk\,r(2n-j+k)>0.}
\]

They sum to one. Their polynomial generating function is the **different Pascal orientation**

\[
\boxed{G_n(z)=\sum_{j=0}^{n}q_n(j)z^j
=\frac1{r(n)}\sum_{k=0}^{n}\binom nk z^{n-k}(1-z)^k r(n+k).}
\]

Both identities are exact with rational coefficients and were checked independently, including endpoint and normalization mutations. Proof: condition on `X`, expand the binomial factors, and integrate `e^{-8kX}`. The four-pole moment identity `E exp(-8kX)=r(n+k)/r(n)` follows by the original Laplace representation. Strict positivity is from the integral, *not* alternating-sign numerical approximation.

This is a real Pascal sheet over the selected source parameter: as the trial history grows, the latent `X` couples its trial outcomes; **the outcomes are independent given `X`, not unconditionally independent**. Their conditional path ordering must still be recorded if arbitrary physical history claims are made.

## 2. Quantitative Pascal → Oily endpoint theorem

Write `Y_n=(8n-7)X_n`. The authentic source satisfies

\[
Q(0)=0,\quad Q'(0)=15,\quad Q''(0)=-59,
\quad Q''(x)<0,\quad Q''(x)\ge-59\ (x\ge0).
\]

Consequently `0<Q(x)<=15x` and `0<=1-Q(x)/(15x)<=59x/30`. Let `Y~Gamma(2,1)` with density `ye^{-y}` and `c=59/30`. Then `Y_n` has density

\[
f_n(y)=ye^{-y}\frac{g_a(y)}{D_a},\qquad
g_a(y)=\frac{Q(y/a)}{15y/a},\qquad D_a=\mathbb E_{Y}g_a(Y).
\]

For `a>=16`, `1-2c/a<=D_a<=1` and `D_a>=181/240`. Therefore, by the triangle inequality for total variation,

\[
\operatorname{TV}(\mathcal L(Y_n),\Gamma(2,1))
\le\frac{1-D_a}{D_a}\le\frac{944}{181a}<\frac6a.
\]

The exact source interlacing from PR #367 also gives `EX<2/a`, `EX²<6/a²`. Conditionally on `X`, couple the binomial `J_n` to `Poisson(np)`. The elementary Bernoulli/Poisson coupling gives error `<=np²`; the coupling between Poisson parameters `np` and `aX` has error `<=|np-aX|`. Since

\[
p=1-e^{-8X}\le8X,\quad
|np-aX|\le32nX^2+7X,
\]

we obtain the unconditional bound

\[
\operatorname{TV}(\mathcal L(J_n),\mathrm{Poisson}(Y_n)\text{ mixture})
\le96n\mathbb E[X^2]+7\mathbb E X
<\frac{576n}{a^2}+\frac{14}{a}.
\]

The Gamma(2)-mixed Poisson distribution is precisely

\[
w_j=\int_0^\infty e^{-y}\frac{y^j}{j!}ye^{-y}\,dy
=\frac{j+1}{2^{j+2}}.
\]

**Theorem PO-2 (quantitative, all-index).** For every integer `n>=3`,

\[
\boxed{
\operatorname{TV}(q_n,w)
\le\min\left\{1,\frac{576n}{(8n-7)^2}+\frac{20}{8n-7}\right\}
\le\min\left\{1,\frac{22}{n}\right\}.}
\]

The last inequality uses `8n-7 >=17n/3`. This provides the full Oily grade law from the authentic original forcing's *marked binomial observation*, rather than merely postulating the endpoint's geometric waits. The exponent two arises from the authentic source zero `Q(0)=0`, `Q'(0)=15` and the Gamma(2) boundary. The same leading limit holds for other positive sources with the same first-order boundary zero, so the limit alone does not authenticate every pole.

## 3. Golden fixed point is already born at finite Pascal stage two

The endpoint PGF is `G(z)=(2-z)^(-2)`. Besides the trivial fixed point `1`, its smaller fixed point is

\[
q_*=(3-\sqrt5)/2=\varphi^{-2}.
\]

For finite `n`, `G_n(1)=1`, `G_n(0)=r(2n)/r(n)>0`, and `G_n` is strictly convex for `n>=2`. Its derivative at 1 is

\[
G_n'(1)=E[J_n]=n(1-r(n+1)/r(n)).
\]

For `n=1`, this is less than one; there is no nontrivial interior fixed point. For all `n>=2`, `G_n'(1)>1`. To certify this *universally* rather than by samples, `(n-1)r(n)-nr(n+1)` reduces to a strictly positive denominator times the polynomial

\[
P(n)=30720n^6-14848n^5-30432n^4+7376n^3+6177n^2-1258n-120.
\]

Setting `m=n-2>=0` gives

\[
\begin{aligned}
P(m+2)={}&30720m^6+353792m^5+1664288m^4\\
&+4085200m^3+5505025m^2+3848538m+1085112>0.
\end{aligned}
\]

Thus `G_n(z)=z` has **exactly one interior root** `q_{*,n}` for each `n>=2`, and `q_{*,n}->q_*`. At `n=2` the interior root is exactly `576147/1824887`, certified by a finite rational polynomial.

This turns the Oily golden fixed point into the limit of a **sequence of rational, source-determined Pascal branch selections**, conditional on the declared time-matched binomial instrument.

## 4. The finite source fingerprint and the harmonic/Gamma triangle

The original four-pole source yields a first correction not determined by the universal Gamma(2) leading shape. For every fixed `z in [0,1]`, with `t=1-z`, Taylor expansion with integrable Gamma-moment remainders gives

\[
\boxed{G_n(z)=\frac1{(2-z)^2}
+\frac{t(209-511t)}{120n(1+t)^4}+O_z(n^{-2}).}
\]

Its simplest exact check is

\[
\boxed{q_n(0)=\frac{r(2n)}{r(n)}
=\frac14-\frac{151}{960n}+O(n^{-2}).}
\]

A mutant `r_mut(n)=n^{-2}` has the same leading `Gamma(2)`/Oily limit but `q_mut,n(0)=1/4` exactly at every n, so the **first correction** distinguishes this mutated source. More sophisticated mutants sharing `Q'(0),Q''(0)` need higher jets, as prior SUCC counterexamples already demonstrate.

For the finite nontrivial root,

\[
\boxed{q_{*,n}=\varphi^{-2}+\frac{b_*}{n}+O(n^{-2}),\quad
b_*=-\frac{1231}{240}+\frac{2671\sqrt5}{1200}\approx-0.1520520.}
\]

Define an **entirely finite-source** Oily–Macaroni contrast from the same real carrier,

\[
\Omega_n=\mathbb E_{X\sim\mu_n}\log((8n-7)X)-q_{*,n}.
\]

For this exact source, `E log((8n-7)X)=1-gamma-59/(240n)+O(n^-2)`, hence

\[
\boxed{\Omega_n\to\varphi^{-1}-\gamma,\qquad
\Omega_n=\varphi^{-1}-\gamma+\frac{1}{n}
\left(\frac{293}{60}-\frac{2671\sqrt5}{1200}\right)+O(n^{-2}).}
\]

The coefficient is approximately `-0.09378130658`; the independent high-precision holdouts converge to it. The finite log expectation is an explicit four-pole Mellin derivative:

\[
\mathbb E\log(aX)= -\gamma-
\frac{\sum_{(d,c)=(0,4),(3,-2),(4,-1),(5,-1)}
 c\,\log(1+d/a)/(a+d)}{R(a)}.
\]

**Reference dependence:** The choice of `n` trials at source time `n` is load-bearing. With `m/n -> rho`, the limiting PGF becomes `(1+rho(1-z))^-2`, so the nontrivial fixed point changes. The golden value is *natural for the time-matched instrument*, not an invariant of every possible observation scheme or a mathematical consequence of the BBP zero seed.

## 5. The whole Pascal/Gamma rank sheet and the exact row-four / 16 alignment

PR #367's positive convolution semigroup has `mu_(a,kappa)` with Laplace transform `[R(a+s)/R(a)]^kappa`. Fix a rank `r=2kappa>0` and repeat the same `n`-trial conditional-binomial observation. Then `aX -> Gamma(r,1)`, and the resulting grade law converges to the generalized negative-binomial distribution with PGF

\[
\boxed{G^{(r)}(z)=(2-z)^{-r}.}
\]

For integer `r>=1`, the coefficients are **Pascal simplex counts**:

\[
\boxed{w_j^{(r)}=\frac{\binom{j+r-1}{r-1}}{2^{j+r}},\quad
(G^{(r)}(S))^{-1}=(2-S)^r
=\sum_{k=0}^r(-1)^k\binom{r}{k}2^{r-k}S^k.}
\]

At rank 4, the inverse is exactly

\[
\boxed{(2-S)^4=16-32S+24S^2-8S^3+S^4.}
\]

This is Pascal row four with alternating signs and powers of two. The leading `16` matches the original BBP digit base, but **it is a combinatorial coefficient**, not a proof of 1/16 digit frequencies. The rank-four positive field is a declared convolution *square* of the original carrier; it is not the original deterministic BBP orbit.

For integer positive convolution power `kappa`, the finite rank `r=2kappa` probabilities are again exact rational numbers:

\[
q_{n,kappa}(j)=\binom nj\sum_{k=0}^j(-1)^k\binom jk
\left(\frac{r(2n-j+k)}{r(n)}\right)^{kappa}.
\]

The source-specific first correction is the exact rational-function limit

\[
\boxed{G_{n}^{(r)}(z)=(2-z)^{-r}+
\frac{r(1-z)}{n(2-z)^{r+2}}
\left[-\frac{151}{240}(2-z)+\frac{r+1}{2}z\right]
+O_{r,z}(n^{-2}).}
\]

For rank four and `z=0`, this yields `q_n^(4)(0)=1/16-151/(1920n)+O(n^-2)`, also independently verified by squaring the exact rational all-success probability. The full rank sheet recovers the user's harmonic–golden–Euler family `D(r)=psi(r)-lambda^r` when the *same* Laplace evaluation `lambda=phi^-1` is declared across ranks. Only rank 2 also makes lambda tied to its own golden fixed point. No universal gamma-normality miracle is inferred.

## 6. Signed, seed-sensitive Fourier lift; finite polynomial inverse

Let `S` be the forward shift on sequences. For any bounded sequence `|z_n|<=1`, define

\[
\Theta_n=\sum_{j=0}^nq_n(j)z_{n+j},\quad
\Sigma_n=\sum_{j\ge0}\frac{j+1}{2^{j+2}}z_{n+j}.
\]

Theorem PO-2 gives

\[
\boxed{|\Theta_n-\Sigma_n|\le2\,\mathrm{TV}(q_n,w)
\le\frac{44}{n},\quad n\ge3.}
\]

**Theorem PO-3 (signed-phase recovery, exact plus quantitative).** Since `Sigma=(2-S)^(-2)z`,

\[
\boxed{z_n=4\Sigma_n-4\Sigma_{n+1}+\Sigma_{n+2}.}
\]

Consequently, for `n>=3`,

\[
\boxed{|z_n-(4\Theta_n-4\Theta_{n+1}+\Theta_{n+2})|
\le\frac{396}{n}.}
\]

This is a genuine source-matched **bounded-error reconstruction of a signed selected path** from its Pascal-virtual readout; no source phase was discarded or replaced by Haar averaging. In particular put `z_n=e(hU_n(s))` for the actual original forcing and any declared real initial seed `s`. The exact affine recursion provides a more explicit twisted frequency-lift for every `j`:

\[
e(hU_{n+j}(s))=e\!\left(h16^j U_n(s)+h\sum_{k=1}^j16^{j-k}r(n+k)\right).
\]

This retains the source phase, all forced carries modulo 1, and the absolute anchor. Changing the seed leaves `q_n` unchanged but changes the lifted phase. For `s=1/15`, the lift rotates by `e(h/15)` at every time; this 15-torsion symmetry is a **known control** and is not a proof that every seed can be identified from relative phases.

The same reconstruction preserves normalized empirical means. For any starting time `L>=3` and `N>=1`,

\[
\boxed{\left|\frac1N\sum_{n=L}^{L+N-1}\Theta_n
-\frac1N\sum_{n=L}^{L+N-1}z_n\right|
\le\frac4N+\frac{44}{N}\sum_{n=L}^{L+N-1}\frac1n.}
\]

The `4/N` comes from `2 E_w[J]/N` and `E_w[J]=2`; the other term comes from the quantitative source TV bound. This is `O(log N/N)`, **for every bounded sequence**, including non-normal coherent counterexamples. Therefore a signed `o(N)` estimate for the Pascal lift would be equivalent to the still-unproved π Weyl estimate, not a weaker theorem that magically supplies it.

The coherent same-forcing seed `s=-pi/16` satisfies `U_n(s)=-T_n ->0`, and hence `z_n->1` for every fixed `h`, so its Pascal lift `Theta_n->1` despite every positive source and Pascal/Gamma identity being intact. This is the required hostile control. Constant `z_n=1` supplies an even simpler control.

## 7. What would move the π-normality frontier

**Succeeded:** Exact authentic finite Pascal probabilities; all-index total-variation transfer to Oily; finite rank-two golden branch; source-specific first-order jet; a rank-four Pascal/16 operator; a seed-anchored signed lift with approximate finite polynomial inverse and explicit Cesàro error. These are research-level paper proofs with separately scoped finite calculations. No original source changes.

**Still missing:** A source-specific, seed-sensitive inequality on the coupled signed carry observable that beats `O(1)` for a normalized Weyl mean. The current Pascal lift faithfully *transports* those Fourier means rather than independently controlling them. The original four-pole, zero-seeded arithmetic orbit has not been proved typical under the positive virtual-path law. This paper does not assume its typicality.

**Next high-value probe:** Keep the joint tensor `q_n(j)*e(hU_(n+j)(0))`, not just either marginal. Test signed conditional carry residues using the authentic integer lift; ablate only the source seed while preserving forcing; compare with Stoneham's proven modular sweeps and mutant `r(n)=n^-2`. Seek a noncircular, source-derived bound on *conditional carry bias* that would imply Fourier cancellation. Do not assert an inference from Pascal rank four, entropy, Gamma centering, finite sample spectra, or positive scalar weights alone.

## 8. Validation, provenance and external ingredients

Reproduction (`python >=3.10`, stdlib):

```sh
python research/2026-10-29/pascal_oily_bbp/pascal_oily_probe.py
```

Independent oracle (requires existing repository test dependencies `sympy`, `mpmath`):

```sh
python research/2026-10-29/pascal_oily_bbp/independent_oracle.py
```

The exact finite probabilities, PGF two orientations, source means, even rank-four convolution, finite fixed roots, Oily inverse, coherent controls and TV bounds are tested with exact rational arithmetic. Symbolic asymptotic coefficients, translated positivity polynomial, and first-order Oily-Macaroni defect are separately checked by independent SymPy algebra and high-precision finite source integrals. The validation receipt is not a hosted CI or Lean kernel certificate.

Primary reference for Le Cam binomial/Poisson inequality: L. Le Cam, *Pacific Journal of Mathematics* 10 (1960), 1181–1197; see also the explicit standard TV form discussed in [this probability reference](https://mathworld.wolfram.com/LeCamsInequality.html). Gamma/Beta integrals and Mellin moments: [NIST DLMF 5.12](https://dlmf.nist.gov/5.12). BBP and hypothesis-A proof boundary: Bailey–Crandall (2001) and Lagarias (2001). Prior SUCC Pascal and Oily dossiers named in §0. The full claimed novelty is only **new to this SUCC integration round**; academic priority is UNVERIFIED.
