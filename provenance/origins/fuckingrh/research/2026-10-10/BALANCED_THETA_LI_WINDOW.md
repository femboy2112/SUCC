# Balanced theta horizons and zero-free Li coefficient transport

**Date:** 2026-10-10. **RH remains OPEN.** This branch is based on the completed SUCC/Hasse/Gamma seam research at commit \`1cefd6fcb224206b9587de1f414fc2f08cd2cd71\` (draft PR #19). Our work lives on \`aletheia/balanced-theta-li-window-2026-10-10\`, never main.

## Original proposal versus derived results

**User-supplied research prompt:** model Gamma as an integral of rotating vectors; track its exact finite SUCC boundary term; combine integer theta samples and the half-density \(e^{u/2}\); map \(s\mapsto1-1/s\) so the critical line becomes the unit circle; form the finite entire completed theta function \(X_{N,T}\); investigate a numerically observed finite-model double-zero collision at \(T\simeq0.324779980943\); seek an arithmetic-source proof of Li-coefficient positivity, with all source windows chosen without looking at nontrivial zeta zeros.

**Our independent validation and mathematical additions:**
1. Reproduced the alleged **finite-model** double-zero collision from the finite *rotating Gaussian integral* directly, including its local square-root splitting coefficient. NOT a theorem about actual zeta zeros.
2. Identified an exact NONCOMMUTATION of limits for truncated theta reflection, and proved a fully explicit **arithmetically coevolving horizon** \(N(u,\epsilon)\).
3. Derived an explicit source-based, **zero-blind, all-DEGREE numerical-error estimate** for the true Li coefficient versus the finite completed theta coefficient. This proves convergence at **each fixed degree** but fails to provide a uniform positivity theorem because of \(r^{-k}\).
4. Probed half-density mutation and fake integer source \(a(6)=2\); both can be detected by an appropriately positioned theta-duality window. The mirror-fixed probe \(u=0\) is permanently blind to these theta coefficient mutations.
5. Tested positive low-degree Li coefficients in a finite model that nevertheless has an off-critical-line zero pair. This shows why checking finitely many positive coefficients or looking at finite zero motion cannot prove RH.

**References / established theorems:**
- NIST DLMF §20.7(viii), theta modular transformations, https://dlmf.nist.gov/20.7.viii and §20.10.2, theta Mellin transform of \(\Gamma_{\mathbb R}\zeta\), https://dlmf.nist.gov/20.10.E2.
- NIST DLMF §5.5, Gamma shifts and reflection, https://dlmf.nist.gov/5.5.
- Bombieri–Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, Journal of Number Theory 77 (1999), 274–287, https://doi.org/10.1006/jnth.1999.2392; primary paper https://websites.umich.edu/~lagarias/doc/bombieri.pdf. Li is already a discretization of Weil's RH-equivalent sign.
- Prior repo \`actualization/hasse_theta_seam.py\`, \`research/2026-10-10/FINITE_SUCC_HASSE_THETA_SEAM.md\`. This branch supplements, not replaces, the calibrated source-seam countermodels.

## 1. Gamma's finite complex SUCC triangle: valid, but not positivity

Set

\[
\mathcal A_{A,B}(s)=2\int_A^B e^{su-\pi e^{2u}}\,du
=\pi^{-s/2}\Gamma\!\left(s/2;\pi e^{2A},\pi e^{2B}\right).
\]

Here the last \(\Gamma(z;a,b)=\int_a^b t^{z-1}e^{-t}dt\) is an incomplete Gamma **interval**, not the untruncated Gamma. For finite \(A<B\) the function is entire in s.

Differentiating \(e^{su-\pi e^{2u}}\) and integrating by parts yields the EXACT relation

\[
\boxed{
\mathcal A_{A,B}(s+2)-\frac{s}{2\pi}\mathcal A_{A,B}(s)
=\frac{e^{sA-\pi e^{2A}}-e^{sB-\pi e^{2B}}}{\pi}.
}
\]

It is literally a complex vector triangle: shifted term, original term, and boundary correction sum to zero. For \(\Re s>0\), the endpoints \(A\to-\infty\), \(B\to+\infty\) disappear, recovering \(\Gamma_{\mathbb R}(s+2)=[s/(2\pi)]\Gamma_{\mathbb R}(s)\). One may NOT simply discard the lower endpoint when \(\Re s\le0\); analytic continuation and meromorphic Gamma poles enter then. The complex rotation \(e^{i\,\Im(s)\,u}\) is genuine, but curvature/positivity does not follow from a triangle closure identity alone.

## 2. The new exact obstruction: theta SUCC and archimedean exhaustion do not commute

Let

\[
\Theta_N(u)=\sum_{n=-N}^N e^{-\pi n^2e^{2u}},
\qquad
D_N(u)=e^{u/2}\Theta_N(u)-e^{-u/2}\Theta_N(-u).
\]

For the full lattice theta, Poisson summation proves \(\Theta(u)=e^{-u}\Theta(-u)\), hence \(D_\infty(u)=0\).

**Order of limits:** for every fixed finite N,

\[
\Theta_N(u)\to1,\quad
\Theta_N(-u)\to 2N+1
\quad(u\to+\infty).
\]

Therefore

\[
\boxed{\lim_{u\to+\infty}e^{-u/2}D_N(u)=1.}
\]

Yet for each fixed finite u, \(\lim_{N\to\infty}D_N(u)=0\). Any claim that "finite theta is almost self-dual" **uniformly** over unbounded u at fixed N is false. The proper question is which coevolving arithmetic horizon \(N(u)\) lets the model retain full theta duality.

**Source-derived, no-zero bound.** Using Poisson exactness and the two missing Gaussian tails, for arbitrary real u,

\[
\boxed{
|D_N(u)|\le
e^{|u|/2}\operatorname{erfc}(\sqrt\pi N e^{-|u|})
+
e^{-|u|/2}\operatorname{erfc}(\sqrt\pi N e^{|u|}).
}
\]

Proof: for \(c>0\), \(\sum_{n>N}e^{-\pi c n^2}\le\int_N^\infty e^{-\pi c x^2}dx\). The integral is \(\frac{1}{2\sqrt c}\operatorname{erfc}(\sqrt{\pi c}N)\). Multiply by 2 for positive and negative lattice points, then apply the respective theta half-density weights. We emphasize: the bound is an **analytic theorem**. The mpmath display of its value is a high-precision approximation, not an interval-arithmetic certificate.

A simple constructive sufficient condition for \(|D_N(u)|\le\varepsilon\), \(0<\varepsilon<1\), follows from \(\operatorname{erfc}(x)\le e^{-x^2}\):

\[
\boxed{
N\ge e^{|u|}\sqrt{\frac{|u|/2+\log(2/\varepsilon)}{\pi}}.
}
\]

Thus \(N(u)=O(e^{|u|}\sqrt{|u|+\log(1/\epsilon)})\) suffices to maintain an **absolute** reflection-error budget as the archimedean window expands. A fixed multiple of \(e^{|u|}\) is generally not enough to drive the unnormalized absolute defect to zero as u grows: the prefactor \(e^{|u|/2}\) amplifies the undamped Gaussian tail. This is a direct rigorous realization of the user's "coherent infinite path of finite observations taken as a coupled limit."

## 3. Exact half-density selection and fake-six source discriminator

For arbitrary \(\alpha\in\mathbb Q\) define \(D_{\alpha}(u)=e^{\alpha u}\Theta(u)-e^{-\alpha u}\Theta(-u)\). Poisson says

\[
D_{\alpha}(u)=\Theta(u)\bigl(e^{\alpha u}-e^{(1-\alpha)u}\bigr).
\]

For all real u, this vanishes **if and only if \(\alpha=\tfrac12\)**. Thus \(1/2\) is a genuinely selected half-density for the Gaussian self-dual transport, not a numerically tuned centering convention. It is still NOT a proof that zeta's zeros lie on Re(s)=1/2.

For a deliberately broken theta lattice coefficient at n=6 (increase both weights ±6 by δ), the exact *additional* reflection defect is

\[
\boxed{
D_{\rm fake}(u)-D_{\rm true}(u)
=2\delta\bigl(
e^{u/2-\pi36e^{2u}}
-e^{-u/2-\pi36e^{-2u}}
\bigr).
}
\]

At the fixed point u=0, even this fake is invisible: the two terms cancel exactly. At a suitable transverse u (e.g. u≈2) the fake defect is large and **cannot be removed by simply increasing N**. Hence sampling the entire coevolving window is essential. This detects **one specified fake source**, not all arbitrary counterfeits; reflection-symmetric non-zeta source families exist.

The source adapter refuses pending/incomplete prefixes and explicitly labels mutated Gaussian weights as **diagnostics, not the completion of an arbitrary Dirichlet L-function**.

## 4. A zero-free Li-jet production formula entirely from finite heat data

Let \(X_{N,T}(s)\) be the finite entire theta completion

\[
\boxed{
X_{N,T}(s)=\frac12+s(s-1)
\sum_{n=1}^N\int_0^T
e^{-\pi n^2 e^{2u}}
\bigl(e^{su}+e^{(1-s)u}\bigr)\,du.
}
\]

For every finite cutoff it is entire, real-symmetric, and invariant under s↦1-s. Importantly \(X_{N,T}(1)=X_{N,T}(0)=1/2\), so the Li-like analytic logarithm is well-defined near s=1.

Put \(s=1+y\), and define directly from the finite Gaussian source

\[
A_j=\frac1{j!}\sum_{n\le N}\int_0^T
e^{-\pi n^2e^{2u}}u^j[e^u+(-1)^j]\,du.
\]

Then

\[
2X_{N,T}(1+y)=1+\sum_{m\ge1}C_m y^m,
\quad C_m=2(A_{m-1}+A_{m-2}),\quad A_{-1}=0.
\]

Use \(w=(s-1)/s\), \(y=w/(1-w)\). Let \(B_0=1\) and

\[
B_k=\sum_{m=1}^k {k-1\choose m-1}C_m.
\]

The finite Li-like coefficients are determined by the exact formal recursion

\[
\boxed{
\lambda^{N,T}_k
=kB_k-\sum_{j=1}^{k-1}\lambda^{N,T}_j B_{k-j}.
}
\]

Equivalently,
\(\log(2X_{N,T}(1/(1-w)))=\sum_{k\ge1}\lambda_k^{N,T}w^k/k\).
Every coefficient is computed from **finite source integrals**, with **zero nontrivial zero inputs**. The same expression for the true completed ξ produces the actual Li coefficients. Bombieri–Lagarias show that \(\lambda_k(\xi)\ge0\) for **every** k is equivalent to RH.

## 5. New rigorous all-fixed-degree finite approximation estimate

For \(0<r\le1/2\), \(|w|\le r\), \(s=1/(1-w)\),

\[
\frac23\le\Re s\le2,\qquad |s(s-1)|\le B_r=\frac{r}{(1-r)^2}.
\]

On u≥0, \(|e^{su}+e^{(1-s)u}|\le2e^{2u}\).
A universal kernel mass bound is

\[
M=\frac{e^{-\pi}}{\pi(1-e^{-3\pi})}
\quad\text{with}\quad
\max(|2\xi(s)-1|,|2X_{N,T}(s)-1|)
\le\delta_r=2B_rM<1.
\]

Thus neither function vanishes anywhere in this declared small disk and
their analytic logarithms exist **without RH**.

By integrating the missing Gaussian integer and u tails,

\[
\begin{aligned}
E_{N,T}(r)&=B_r\pi^{-1}
\left[
\frac{e^{-\pi(N+1)^2}}
     {(N+1)^2(1-e^{-\pi(2N+3)})}
+\frac{e^{-\pi e^{2T}}}
     {1-e^{-3\pi e^{2T}}}
\right],\\
|\xi(s)-X_{N,T}(s)|&\le E_{N,T}(r).
\end{aligned}
\]

By the mean-value integral for analytic log along the segment between the two nonzero values, \(|\log(2\xi)-\log(2X)|\le2E/(1-\delta_r)\). Applying Cauchy's coefficient estimate on |w|=r:

\[
\boxed{
|\lambda_k(\xi)-\lambda_k^{N,T}|
\le \frac{2k\,E_{N,T}(r)}{(1-\delta_r)r^k}
\qquad(k\ge1).
}
\]

This is an exact mathematically justified **zero-blind, source-derived
error theorem** for every fixed k. Our software evaluates E in mpmath
(nondirected), so a *computer-assisted certified inequality* would need
interval arithmetic or exact rational enclosing functions; none is
claimed.

At r=1/2, δ≈0.05502611; the computed envelope for degree k=12:

| N | T | theorem's lambda_12 error bound (approx.) |
|---:|---:|---:|
| 1 | 0.325 | 161.3 |
| 2 | 0.8 | 0.01157 |
| 3 | 1.2 | 6.04e-11 |
| 4 | 1.5 | 2.61e-23 |

**The OPEN wall is evident in \(r^{-k}\).** We get arbitrarily small
errors at every fixed k but *no uniform relative margin* establishing
positive coefficients for unbounded k. Getting complete arithmetic
information in the limit is not the same as proving an all-k sign law.
A future theorem needs a source-derived inequality that survives
these quantifiers, rather than a proof that particular finite
approximants happen to have positive initial coefficients.

## 6. The finite-model zero collision and the Li detection latency

We independently solved the source-defined **finite** equations

\[
X_{4,T}(1/2+it)=0,\qquad
\partial_tX_{4,T}(1/2+it)=0.
\]

Using direct finite rotating-Gaussian quadrature with analytic derivatives
(no special-function numerical-differentiation instability), the result is

\[
T_*=0.32477998094257380420449\dots,\quad
t_*=11.21007648628445327420037\dots.
\]

The local Taylor coefficients are

\[
X\approx
0.6349512988621883(T-T_*)
-0.00667313540703416(s-s_*)^2,
\]

so the off-line displacement locally scales as
\(9.754505080937\sqrt{T-T_*}\). This is a **numerical** finite-approximant
calibration, not an exact root-location theorem or a known zero of ζ.

At T=0.325 the finite model has off-critical roots near
\(s=0.644637710345+11.2092395146i\) and its reflected/conjugate orbit.
For this right-hand root,

\[
|w|=\big|(s-1)/s\big|\approx0.9988519928107503<1,
\quad
1/(-\log|w|)\approx870.6.
\]

It produces a logarithmic singularity inside the Li-coordinate unit
disk and suggests that detecting the deviation through high-degree
coefficients may require far more than a dozen terms. This scale is
an e-folding heuristic, **not** a proved first-negative coefficient index.

Yet direct *finite Gaussian source* calculations give for the
T=0.325, N=4 model approximately

\[
\lambda_1^{4,0.325}=0.02222101128,\quad
\lambda_2^{4,0.325}=0.08875093226,\quad
\lambda_{12}^{4,0.325}=2.97935737107,
\]

and **all first twelve are positive**, notwithstanding the off-line
finite zero pair. Numerical signs of finitely many coefficients are
not RH certificates. The full true xi values are approximately
\(\lambda_1=0.0230957089661\), \(\lambda_{12}\approx3.26325532062\).

## 7. What this does and does not prove

**Classically established:** the Poisson theta relation, half-density
parity, finite Gamma integration-by-parts cocycle, and Li's
positivity criterion.

**Newly derived in this branch as elementary consequences:**
nonuniform theta double limit and a moving \(N(u,\epsilon)\) bound;
a direct finite Gaussian-to-Li recursive jet algorithm; an explicit
zero-free Cauchy coefficient-error theorem for every fixed Li index.

**Numerically observed, not a root certificate:** finite
double-zero bifurcation, off-line roots at T=0.325, low Li coefficients.

**Hostile controls:** fixed-N reflection fails for large u; generic
fake n=6 source and wrong half-density can have lasting reflection
defects; fixed-point u=0 is blind to the same fake; finite
approximants with off-line zeros can have many positive Li
coefficients.

**Not established:** a uniform sign theorem for **all** Li
coefficients, a completed arithmetic adjoint/polarization identical
to the full Weil functional, or a theorem that finite off-line zeros
necessarily move monotonically toward the line. No RH proof.

**Next consequential theorem target:**
A source-derived inequality controlling the ratio
\(\lambda_k^{N,T}/\mathcal E_{k,N,T}\) uniformly along a rigorously
specified jointly increasing sequence \((k,N(k),T(k))\), plus a
non-circular lower bound for the true completed Li coefficient
or an equivalent closed Weil pairing. Any such theorem MUST read
Euler multiplicativity (and survive mutation controls) rather than
merely reflect modular self-duality of the Gaussian.


## 8. An explicit diagonal infinity of FINITE SUCC windows for ALL Li indices

The source-derived estimate in §5 has an exponential \(r^{-k}\) cost,
but its Gaussian tails decay *faster* in the two source cutoffs.
This lets us explicitly build a jointly expanding observation schedule
that makes **every Li index k have arbitrarily small absolute
approximation error on its own, at a finite stage**.

Put \(r=1/2\), so \(B_r=2\), \(\delta_r<1/2\). For every integer
\(k\ge1\) choose

\[
\boxed{
L_k=(2k+12)\log 2+4\log(k+1),\quad
T_k=\frac12\log\frac{L_k}{\pi},\quad
N_k^{\rm Li}=\left\lceil\sqrt{\frac{L_k}{\pi}}\right\rceil+1.
}
\]

Here \(T_k>0\) for all k≥1. These choices guarantee both Gaussian
tails in §5 are \(O(e^{-L_k})\). In particular
each of the two geometric denominators is >1/2, and
\[
E_{N_k,T_k}(1/2)<\frac8\pi e^{-L_k}<3e^{-L_k}.
\]
Since \(1/(1-\delta_r)<2\),

\[
\boxed{
|\lambda_k(\xi)-\lambda_k(X_{N_k^{\rm Li},T_k})|
<
12 k\,2^k e^{-L_k}
=
\frac{12k}{4096(k+1)^4}2^{-k}
<2^{-k}.
}
\]

This is an unconditional, zero-blind and **degree-indexed** analytic
approximation theorem. Its asymptotic arithmetic and archimedean
budgets satisfy

\[
\boxed{
N_k^{\rm Li}=\Theta(\sqrt k),\qquad
e^{T_k}=\Theta(\sqrt k),\qquad
T_k=\tfrac12\log k+O(1).
}
\]

The appearance of a square-root finite-integer window alongside a
logarithmic Gamma window is structurally reminiscent of the
Riemann–Siegel factor-square cutoff, but \(k\) is a **Li index, not
spectral height t**; identifying them would be an unjustified leap.

**A SECOND independent budget may be required:** the Li-indexed
approximation theorem controls the *integrated* theta completion,
but it does not automatically ensure pointwise finite-lattice
Poisson self-duality at the moving endpoint \(u=T_k\). To demand
both errors below \(2^{-k}\), set

\[
\boxed{
N_k=\max\!\left(
N_k^{\rm Li},\
\left\lceil
e^{T_k}\sqrt{\frac{T_k/2+(k+1)\log2}{\pi}}
\right\rceil+1
\right).
}
\]

Then \(N_k=O(k)\), and simultaneously

\[
\boxed{
|\lambda_k(\xi)-\lambda_k(X_{N_k,T_k})|<2^{-k},
\qquad
|D_{N_k}(T_k)|<2^{-k}.
}
\]

The code implements \`li_coevolving_diagonal\` with optional
simultaneous self-duality, rejects horizons that exceed the bounded
execution budget, and independently checks the sharper erfc bound.

**DO NOT MISREAD THIS.** We have constructed a uniform **accuracy
schedule**, *not a uniform positivity certificate*. Showing that
\(\lambda_k(X_{N_k,T_k})\) always exceeds this error bound by a
source-derived strict positive margin would imply the RH-equivalent
sign condition. No such positive margin is known or claimed here.
The fake a(6)=2 theta source still violates duality at the same
carefully matched \(u=T_k\), so increasing budgets cannot launder
that particular counterfeit.

This diagonal theorem is a concrete expression of the user's
"infinite realization of finitely accessible observations":
no finite stage must contain all Li coefficients, while a single
explicit rule prescribes a finite arithmetic/Gamma window for
EVERY coefficient. It establishes representation and controlled
measurement; the missing global arithmetic sign is the real
fourth-gate problem.
