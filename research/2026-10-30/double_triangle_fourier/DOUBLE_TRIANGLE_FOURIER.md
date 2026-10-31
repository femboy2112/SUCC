# SUCC — Two superimposed time-extruded triangles and their genuine two-dimensional Fourier kernel

**Research date:** 2026-10-30. **Baseline:** verified merged Main XVI, `e18ba565ca540adb7edf3292f5593929e76d91c5` (PR #389). **Parent observation:** research PR #390, time-extruded triangle. **Authority:** self-contained paper calculations + exact rational tests + separate symbolic/numerical oracle. No change to original source, U0=0, main, historical claim IDs, or production modules. **Base-16 normality of pi and RH remain OPEN.** No claim of physical gluon dynamics or scholarly priority for classical Gamma–Poisson/negative multinomial theory.

## 0. Geometric interpretation, with the correct source ownership

Rotate the time extrusion to horizontal time `n` and vertical grade. Triangulate each time–grade square in two ways. Two observation triangles are **not independent** when the second inherits the first's posterior on one common latent source variable `X`. Keeping that posterior, rather than resetting to the prior, is the load-bearing mathematical choice. A rectangular face can therefore be subdivided into two triangles, but the two divisions must agree on the **same source posterior** at the shared endpoint.

Use exactly the authentic original four-pole positive carrier:

```
Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x)>0,
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
a_n=8n-7, r_n=R(a_n),
mu_n(dx)=e^(-a_n x)Q(x) dx/R(a_n),
U_0=0, U_n=16 U_(n-1)+r_n.
```

The two-panel Bernoulli observation is a **declared mathematical sensor** on `mu_n`, not a claim that actual hexadecimal digits are random Bernoulli outcomes. Conditional on the same `X=x`, the panels observe respectively `m1` and `m2` independent Bernoulli trials with success likelihood `p(x)=1-e^(-8x)`; they share `X` even after the first panel completes. Let J,K count successes.

## 1. DTF-01: finite exact posterior-preserving triangular tiling

For all integers n>=1, m1,m2>=0 and 0<=j<=m1, 0<=k<=m2,

\[
\boxed{P_n(J=j,K=k)=\binom{m_1}{j}\binom{m_2}{k}c_{a_n,m_1+m_2,j+k},}
\]

where the *same* positive source coefficient is

\[
c_{a,m,s}=\frac1{R(a)}\int_0^\infty e^{-ax}Q(x)e^{-8(m-s)x}(1-e^{-8x})^s\,dx
=\frac{\sum_{t=0}^s(-1)^t\binom{s}{t}R(a+8(m-s+t))}{R(a)}.
\]

All entries are positive and rational at the native clock. Vandermonde's identity gives

\[
\boxed{P(J+K=\ell)=\binom{m_1+m_2}{\ell}c_{a_n,m_1+m_2,\ell}.}
\]

Moreover, conditional on the *total* grade, the division between the triangles is the source-independent hypergeometric law:

\[
\boxed{P(J=j\mid J+K=\ell)=\frac{\binom{m_1}j\binom{m_2}{\ell-j}}{\binom{m_1+m_2}\ell}.}
\]

**Proof.** Conditional on X, the joint word likelihood is `p(X)^(j+k)(1-p(X))^(m1+m2-j-k)`; integrate against the *same* `mu_n`, multiply by the two binomial word counts, then sum by Vandermonde. The conditional posterior at the intermediate split is proportional to `mu_n(dx) p(x)^j (1-p(x))^(m1-j)`; the second panel must use this posterior. Resetting to `mu_n` before K instead produces `P_reset(J,K)=P(J)P(K)` and generally changes correlations.

**Extrusion coordinate.** The underlying unnormalized posterior measure depends on `v=n+m1+m2-(j+k)` and `j+k`. The first-versus-second-panel split still matters to an observer of **intermediate carries**. Main XVI's equality `M~_(n+1,m,j)=M~_(n,m+1,j)` is retained; no nonzero curvature is inferred from commuting Bernoulli likelihoods. Memory is not curvature.

## 2. DTF-02: the 2D Fourier symbol is one squared mixed lattice resolvent

Take native a_n=8n-7 and two full depth-n panels (m1=m2=n). Since Q(x)=15x+O(x²) and R(a)=15/a²+O(a^-3), the scaled source `Y=a_n X` tends to Gamma(2,1); conditional on Y, J and K tend to **independent Poisson(Y)** variables, but they are *dependent unconditionally* because they share the same Y. Their two-variable generating/characteristic function is

\[
\boxed{H(z,w)=E[z^Jw^K]=\frac1{(3-z-w)^2}\qquad(|z|,|w|\le1).}
\]

Thus the full 2D Fourier response is `H(e^(i theta),e^(i phi))`. Its exact lattice path expansion is

\[
\boxed{[z^jw^k]H=\frac{(j+k+1)\binom{j+k}{j}}{3^{j+k+2}}.}
\]

The binomial counts *staircase interleavings across the tiled rectangle*, while `j+k+1` is the authentic Gamma-rank-two multiplier. The factor `3` is the one remaining exponential clock plus two unit Poisson observation clocks, not a new arithmetic prime-three independence theorem.

For formal lattice shifts X,Y, the exact Green-function equation is

\[
\boxed{(3-X-Y)^2H(X,Y)=1,\qquad (3-X-Y)^2=9-6X-6Y+X^2+2XY+Y^2.}
\]

On the unit Fourier torus `1 <= |3-e^(i theta)-e^(i phi)| <=5`, so `1/25<=|H|<=1` and **the symbol has no zeros**. This is an elliptic-style invertible convolution on a periodic lattice, not a mechanism proving circle-orbit mixing.

**Explicit reset control:** independent restarting of the second latent gives `G(z)G(w)=[(2-z)(2-w)]^(-2)`. Both margins agree, but `H(0,0)=1/9` versus `G(0)^2=1/16`. Source memory is *exactly* the failure of the two-variable Fourier response to factorize. In the shared model `Cov(J,K)=Var(Gamma(2))=2`; in the reset model it is zero. Gamma–Poisson negative-multinomial mixtures are classical; SUCC's contribution is this original-source finite-interface and source-discriminating jet, not the general distribution theorem.

## 3. DTF-03: totient at q=6 sees the shared field, exactly rationally

With `chi_6(j)=1_[gcd(j,6)=1]`, the separate primitive marginal is the inherited `p=416/1323`. In the *shared* two-triangle limit, the exact primitive/primitive cell is

\[
\boxed{p_{11}=\frac{6533558611}{64571925600}.}
\]

The off-diagonal cells `p01=p10=4590078863/21523975200`, and `p00=4356841973/9224560800`. Therefore

\[
\boxed{Cov(chi_6(J),chi_6(K))=p_{11}-p^2
=\frac{197519239153}{85428657568800}>0.}
\]

**Proof with a finite exact certificate:** work in the 36-dimensional group algebra `Q[X,Y]/(X^6-1,Y^6-1)`. Invert the rational linear map `3-X-Y` twice at the origin (no singularity since all its complex eigenvalues have modulus >=1). The resulting 36 coefficients are the probabilities of the `(J mod 6,K mod 6)` cells, since their generating function is H. Sum the four cells with residues 1 and 5. The standalone Fraction solver and an independently written SymPy matrix inverse agree exactly. The positive covariance is also `Var(E[chi_6(Poisson(Y)) | Y])`, hence has a direct nonnegative information interpretation. It is **not a selected pi-phase theorem**.

## 4. DTF-04: genuinely original-four-pole *two-variable* first source jet

For the *finite original source*, set

\[
H_n(z,w)=E_{\mu_{8n-7}}[(z+(1-z)e^{-8X})^n(w+(1-w)e^{-8X})^n].
\]

For every fixed 0<=z,w<=1, the source endpoint expansion `Q(x)=15x-(59/2)x²+O(x³)` and Laplace's method give

\[
\boxed{H_n(z,w)=\frac1{(3-z-w)^2}+\frac{J(z,w)}n+O_{z,w}(n^{-2}),}
\]

\[
\boxed{J(z,w)=\frac{-511(z^2+w^2)-302zw+1115(z+w)-906}{120(3-z-w)^4}.}
\]

A self-contained expansion: put `a=8n-7`, `Y=aX`, `A=1-z`, `B=1-w`, `d=1+A+B=3-z-w`. The normalized source density is

`Y e^(-Y)[1+(59/(240n))(2-Y)+O_Y(n^-2)]`,

and the two conditional binomial factors give

`exp(-(A+B)Y)*[1+[-(7/8)(A+B)Y+(A(1-A)+B(1-B))Y²/2]/n+O_Y(n^-2)]`.

Integrate against Gamma(2) using moments `E[Y^k exp(-cY)]=(k+1)!/(1+c)^(k+2)`; the displayed J follows. All error terms are controlled after exponential-tail truncation, uniformly for fixed z,w in [0,1].

At w=1, J reduces **exactly** to Main XVI's inherited one-variable joint-source 59-jet:

`J(z,1)=(-511z²+813z-302)/[120(2-z)^4]`.

For the Gamma-matched fake positive source `Q_fake(x)=15x` (same a_n and observer), the first source-specific difference is

\[
\boxed{H_n^{BBP}-H_n^{fake}=\frac{59(2-z-w)}{120n(3-z-w)^3}+O(n^{-2}).}
\]

Thus the **2D interaction carries a genuine source-specific finite correction** that is absent from the Gamma(2) universal limit. It is not a unique source fingerprint: mutants matching `Q''(0)` can have the same jet, and the selected zero-seed phase is not involved. Independently, the finite source shared-grade covariance is

`Cov(J,K)=n²[R(a+16)/R(a)-(R(a+8)/R(a))²]=2-569/(60n)+O(n^-2)`.

The tests verify the rational identities, a 36-state finite-group algebra, the w=1 legacy slice, original-vs-fake differences, and independent 75-digit endpoint quadrature at n=30,90,270.

## 5. DTF-05: conserving the observation clock keeps the original golden ratio

Two **full** depth-n triangles double the total observer clock: `theta1=theta2=1`, so diagonal grade `S=J+K` has PGF

`H(z,z)=(3-2z)^(-2)` and nontrivial fixed point `q=1-sqrt(3)/2`, NOT `phi^(-2)`.

If instead **one native n-trial budget is split into two halves** (`m1+m2=n`, `m1/n->theta1`, `m2/n->theta2`, `theta1+theta2=1`), then

\[
H_{split}(z,w)=[1+\theta_1(1-z)+\theta_2(1-w)]^{-2},
\qquad H_{split}(z,z)=(2-z)^{-2}.
\]

So the inherited golden fixed point `phi^(-2)` and Oily–Macaroni `phi^(-1)-gamma` survive **precisely when the total native observation clock is conserved** at rank two. This is a useful **declared observer conservation rule**, not a physical law derived from pi. Main XVI's golden-locus theorem excludes the false claim of uniqueness over all clock/rank pairs.

## 6. DTF-06: why the signed endpoint still fails to cancel by itself

Attach the ACTUAL zero-seeded original recurrence as an endpoint observation:

`z_t(h)=exp(2pi i h U_t(0))` and `Theta_n(h)=sum_(j,k) P_n(J=j,K=k) z_(n+j+k)(h)`.

By DTF-01, `Theta_n` is exactly the single **2n-trial** positive Pascal readout. In the two-full-panel Gamma limit, `S=J+K` has NB(2,theta=2) law

\[
t_\ell=\frac{(\ell+1)2^\ell}{3^{\ell+2}},\quad E[S]=4,\qquad T(z)=\frac1{(3-2z)^2}.
\]

For every n>=3, a source-specific binomial/Poisson coupling and the inherited original scaled-density bound give

\[
\boxed{TV(P_n(S\in\cdot),t)\le \min(1,\ 1152n/(8n-7)^2+34/(8n-7))\le\min(1,45/n).}
\]

Proof details: with a=8n-7, `p=1-exp(-8X)`, Le Cam `TV(Bin(2n,p),Pois(2np))<=2n p²`, `|2np-2aX|<=64n X²+14X`. The authentic exact moment bounds `EX<2/a`, `EX²<6/a²` give `1152n/a²+28/a`; the inherited scaled-density bound `TV(aX,Gamma2)<6/a` finishes. Poisson mixing does not increase TV. The bound `45/n` follows from a>=17n/3 for n>=3. Mark and seed never enter the coupling.

Consequently, for every bounded signed or complex sequence `|z_t|<=1`, every L>=3,N>=1,

\[
\boxed{\left|\frac1N\sum_{n=L}^{L+N-1}\Theta_n(z)
-\frac1N\sum_{n=L}^{L+N-1}z_n\right|
\le\frac8N+\frac{90}{N}\sum_{n=L}^{L+N-1}\frac1n.}
\]

The stationary comparison uses `2 E[S]/N=8/N` because shifting an N-window by ell changes at most 2ell boundary terms. Therefore the two-triangle endpoint sheet is a **uniformly invertible/mean-preserving representation**, not any proof of Weyl cancellation. The coherent same-forcing counterseed `-pi/16` has phases tending to 1 and its two-panel mean also tends to 1. The original `U0=0` Weyl gate `sum_(n<=N)e(hU_n)=o(N)` remains **OPEN**.

**Where the 2D Fourier information *is* different:** keep the intermediate literal carry `kappa_(n+J)`, the final literal carry `kappa_(n+J+K)`, and the relative phase `U_(n+J+K)-U_(n+J)` *before* summing the two grades. The exact finite tensor

`A_n(c,d,q)=sum_(j,k): [kappa_(n+j)=c, kappa_(n+j+k)=d, {U_(n+j+k)-U_(n+j)}=q] P_n(j,k)`

has rational coefficients and original rational circle phase labels for U0=0. It breaks **total-grade sufficiency** because `(j,k)=(0,1)` and `(1,0)` share total grade 1 but observe different intermediate carries whenever `kappa_n != kappa_(n+1)`. Both tensor and exact seed-alias controls are executed. This is **an internal history observation**, not yet a signed intertime estimate. A theorem must use these correlated intermediate labels to get cancellation rather than repackage the endpoint alone.

## 7. DTF-07: opposing triangles and a Fourier anti-shortcut

If instead the two triangles are defined as *independent* endpoint Oily probes with opposing time shifts `n+j-k`, their bilateral stationary convolution has a completely explicit Fourier symbol and spatial kernel:

\[
|G(e^{i\omega})|^2=(5-4\cos\omega)^{-2},\qquad
k_m=\frac{5+3|m|}{27\,2^{|m|}}.
\]

Its exact local inverse is `33 - 20(S+S^(-1)) + 4(S²+S^(-2))`. This is a genuinely nontrivial **5-point elliptic stencil** with Fourier multiplier in [1/81,1], but it preserves all constant/coherent phases and cannot independently prove normality. The backwards-oriented panel is a **declared diagnostic of earlier phases**, not the physical inverse BBP map or the same posterior-preserving two-panel observation.

## 8. Claim status, countermodels and next mathematical gate

**Proved paper / exact finite tests:** finite original-source posterior gluing, Vandermonde/hypergeometric conditional split, independent-vs-shared discrepancy, explicit 2D negative-multinomial Fourier symbol and local stencil, exact q6 primitive covariance, first native 59-jet, sharp clock bookkeeping, quantitative total-grade TV/Cesaro transfer, exact intermediate rational carry-phase tensor.

**Classical inputs:** Gamma–Poisson mixtures; Vandermonde; cyclic finite Fourier; polynomial and Laplace expansions. External literature (for priority context): https://pmc.ncbi.nlm.nih.gov/articles/PMC2945396/ ; https://www.ism.ac.jp/editsec/aism/pdf/038_1_0045.pdf . None of those sources is claimed to analyze this authentic BBP source.

**Failed implications:** common posterior and nonzero mixed q6 covariance **do not** imply random selected hexadecimal digits; 2D Fourier nonfactorization is a property of an auxiliary source-selected observation, not an o(N) Weyl bound; Gamma rank/clock/golden readouts do not force source-selected carry frequencies; reset-independent and opposing-backwards panels are different experiments. Finite selected 16-bin correlations and exact phase labels are observations only.

**Next necessary theorem:** bound a NONPRODUCT, source- and U0=0-sensitive two-time Fourier/carry current in the full signed interior tensor (not merely H(z,w), its coefficient correlations, the total-grade marginal or a filtered Weyl sum). Require a new independently proved saving on a specified harmonic/length band that survives original-source checks and is falsified by coherent counterseed, higher-jet-matched source mutant, q6 premature projection, finite periodic de Bruijn controls and the corrected Main XVI seed alias classes.
