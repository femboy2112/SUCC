# ORIGINAL-THETA CONTOUR → FINITE WEIL SPECTRAL SHADOW

**Research checkpoint:** October 14, 2026. **Source parent:** `femboy2112/SUCC`, draft PR #78, `research/xi-theta-certified-jets-cave-2026-10-14@96fbc5eac5705573014c0c8bbd4fc85c63bf1fd9`. This descends from the authentic original-prime/all-place Gaussian theta continuation PRs #71/#73 and the SUCC Gaussian-Fock PR #74. **Context, not imported:** signed Weil/ideal-hard PRs #75/#76, global sandwich #77, Black Sun #79 and Suzuki Carleman #70. **RH PROVED: NO.** No nontrivial zero location was read, copied, queried or assumed for constructing the mathematical source, contour, or sign witness. Nothing was merged into main, published, released or written to `FuckingRH`.

## 0. Intent, source and mathematical status

**User's moonshot:** make E a lawful finite complex-contour observer of the *one authentic completed zeta*, then prove precisely which piece of Suzuki's signed Weil form that observation identifies. The cave intuition becomes: an authentic source and its analytic model can determine specific finite spectral shadows while leaving unobserved signed spectral components logically unresolved.

**References:** Masatoshi Suzuki (2025), *On the Hilbert space derived from the Weil distribution*, Canadian Journal of Mathematics, Eq. (1.1)-(1.2) and the Weil positivity criterion; Masatoshi Suzuki (2026), *Weil's quadratic form via the screw function*, arXiv:2606.09096v3; standard Jacobi/Poisson theta completion and the classical argument principle/Rouché theorem. Claims about Weil zero-side and signed source-side equivalence are CLASSICAL IMPORTS; the original-source rational certificate and phase transport are **PROVED LOCAL new-to-SUCC assemblies**. No originality/Lean/kernel/physical-world priority asserted.

All arithmetic inputs are the integer theta source `psi(t)=sum_{n>=1}exp(-pi n² t)` at the real Gaussian place. The all-place source identity and analytic continuation were established in parent PR #73:

\[
F(z)=\xi(\tfrac12+z)=\frac12+(z^2-\tfrac14)B(z)\quad\text{with }\quad
B(z)=\int_1^\infty\psi(t)t^{-3/4}\cosh(z\log(t)/2)\,dt,
\]

The specialization at `z=i y` gives `F(iy)=1/2−(y²+1/4)B(iy)`. Functions are even and entire and satisfy `F(-conj z)=conj F(z)`.

## TC-01 — constructing a contour center without reading zeros (TESTED MODEL + independent proof gate)

A finite exploratory E uses only the finite Gaussian integer-theta heat sum, Simpson quadrature on `[1,8]` and a deterministic source-only bisection in the declared interval `14<=y<=15`. Rounded to the rational address grid 1/10000, it proposes

\[
\boxed{y_0=141347/10000,\quad z_0=i y_0,\quad r=1/500.}
\]

The search uses ordinary floating point solely to nominate a probe; it has **zero authority** to certify an analytic claim and never calls zeta, xi or a zero table. Every fact in TC-02/03 is proved independently by fixed-point outward rational arithmetic. The contour parameters are frozen in the reproducible receipt; source replay checks their provenance within this mathematical model, not in physical reality.

## TC-02 — outward rational evaluation of the authentic source (PROVED LOCAL)

At `y=y0`, define the real source moments

\[
B_y=\int_1^\infty\psi(t)t^{-3/4}\cos(\tfrac y2\log t)\,dt,
\quad
S_y=\int_1^\infty\psi(t)t^{-3/4}\frac{\log t}{2}\sin(\tfrac y2\log t)\,dt.
\]

Then, without a zeta oracle,
\[
F(iy)=\frac12-(y²+\tfrac14)B_y,\qquad
F'(iy)=i\bigl(2y B_y-(y²+\tfrac14)S_y\bigr). \tag{TC2}
\]

The executable certificate uses `N=2` **integer-theta modes**, integration time `[1,8]`, `4096` equally spaced Simpson subintervals, and rational π, logarithm, exponential, cosine and sine enclosures. The validation is not a floating-point integration proof:

* π is bracketed through Machin's arctangent formula with an alternating rational remainder.
* Each rational `log(t)` is reconstructed by range reduction to `[1,2)` and a positive arctanh series with a geometric rational tail.
* Exponentials are bounded using dyadic scaling, positive rational Taylor terms, geometrically dominated tail and outward inversion.
* Sine/cosine are polynomials of fixed degree ≤101, with a global rational Taylor remainder valid for the entire declared argument range `[0,16]`.
* Every elementary interval operation is rounded outward on the exact integer grid `10^-38`.
* The composite Simpson remainder is **proved**, not inferred from convergence: for a single complex source mode `e^{-πn²t} t^{-3/4+i y/2}`, the fourth derivative is bounded by a finite binomial sum with factors `πn²` and the falling factorial of `-3/4+iy/2`. Differentiation in the complex exponent supplies the extra `log t/2` for `S_y`, controlled by `log(8)<3` and an explicit derivative-of-falling-factorial bound. Source loops include the actual `n=1,2` and no fake Euler labels.
* Missing integers `n>=3`: `psi_tail(t)<=2e^{-27t}` for `t>=1`, giving `B_tail<=2e^{-27}/27`, `S_tail<=e^{-27}/27²`.
* Missing time `t>8`: `psi(t)<=2e^{-3t}` yields `B_tail<=2e^{-24}/3`, `S_tail<=e^{-24}(7/3+1/9)`.

The exact rational source receipt provides these particularly readable outward enclosures:

\[
\begin{array}{rcl}
|F(z_0)|&<&1.094\times10^{-7},\\
|F'(z_0)|&>&0.00138260,\\
\text{Simpson error on }B_y&<&3.468\times10^{-10},\\
\text{Simpson error on }S_y&<&6.101\times10^{-10}.
\end{array}
\]

These rounded decimals are *not* the primary certificate; the full `Fraction` endpoints and named error budgets are persisted in `THETA_COMPLEX_CONTOUR_RECEIPT.json` and replayed deterministically.

## TC-03 — certified exactly one simple zero **on the critical line** (PROVED LOCAL, Rouché)

On the full complex disk `|z−z0|<=r`, put `|Re z|<=r`. For every integer `k=0,1,2`, since `psi(t)<=2e^{-3t}`, `log t<=t-1` and `t^{-3/4+r/2}<=1`, the derivative of the analytic theta integral obeys

\[
|B^{(k)}(z)|\le \frac{2e^{-3} k!}{2^k(3-r/2)^{k+1}}.
\]

Differentiate `F(z)=1/2+(z²−1/4)B(z)` twice. This yields, for the stated rational `z0,r`, the outward rational bound

\[
\boxed{\sup_{|z-z_0|\le r}|F''(z)|<3/4.}
\]

Taylor's integral remainder along each complex segment bounds the difference between `F(z)` and its affine Taylor model `L(z)=F(z0)+F'(z0)(z-z0)` by `(3/8)r²` on the boundary. The frozen rational receipt proves the strict Rouché inequality

\[
\boxed{
|F'(z_0)|r-|F(z_0)|-\tfrac12r²\sup_D|F''|
>10^{-6}>0.}\tag{TC3}
\]

Thus `F` and `L` have the same number of zeros inside the disk, counting multiplicity. Since `|F(z0)|<r|F'(z0)|`, `L` has exactly one zero there. Rouché implies **one simple zero** of authentic `F` in the open disk and **none on its boundary**.

The anti-holomorphic involution `z↦-conj(z)` fixes this disk and preserves the zero divisor of even real `F`. The unique zero is fixed by the involution, hence lies on the imaginary axis. In s-coordinates:

\[
\boxed{
\rho=\tfrac12+i\gamma,\quad
\frac{141347}{10000}-\frac1{500}<\gamma<
\frac{141347}{10000}+\frac1{500};
\quad \rho\text{ is a simple zero of }\xi. }
\]

Its conjugate is another simple critical-line zero, also source-derived. This is a **tiny instance of the well-known classical low-lying spectral data**, strictly weaker than established analytic zero information, and is not RH. No nontrivial zeros were used as *inputs*.

## TC-04 — local authentic Weil signed-form comparison (CLASSICAL spectral identity + PROVED LOCAL contour)

Suzuki (2025), Eq. (1.1)-(1.2), defines the authentic Weil distribution on real compact smooth tests and represents its Hermitian form via the completed xi zero divisor. For `f` real in `C_c^infty(R)` set

\[
A_f(s)=\int_\mathbb R f(x)e^{(s-1/2)x}\,dx.
\]

For the certified small positively oriented contour `C` around the one simple source-derived completed zero `rho`, define

\[
\mathcal R_C(f)=\frac{1}{2\pi i}\oint_C
\frac{\xi'(s)}{\xi(s)}A_f(s)A_f(1-s)\,ds.
\]

By the residue theorem and `1−rho=conj rho`, on real tests,

\[
\boxed{\mathcal R_C(f)=|A_f(\rho)|²\ge0.}\tag{TC4}
\]

**This is a genuine completed-Weil spectral summand**, with source-identified zero multiplicity 1, not an invented covariance. A conjugate contour supplies its conjugate summand; the sum is positive. The full signed Weil form also includes every other zero, including high ordinates not enclosed by these contours. **Neither the residual spectral form nor the full Weil form is proved nonnegative.** On a finite interval all exact equalities are initially statements on `C_c^infty` and transport only by justified form/closure theorems, never by untyped substitution.

A direct quantitative corollary: if `f>=0`, `int f=1`, and `supp(f)⊂[-1/100,1/100]`, then `|gamma|<15` and `cos u>=1-u²/2` imply

\[
|A_f(\rho)|²\ge (1-(15/100)²/2)²
=(791/800)²>97/100.\tag{TC4b}
\]

This lower bound is for **one proven local positive summand only**.

## TC-05 — finite source observer recovers a true rank-two Weil spectral *operator* (PROVED LOCAL)

The certified source zero `rho` and conjugate `bar rho` contribute the real positive kernel

\[
K_\gamma(x,y)=2\cos(\gamma(x-y)),
\quad x,y\in(-a,a).
\]

For real `f`, the corresponding quadratic form is `2|int f(x)e^{i gamma x}dx|²>=0`. This is rank at most 2 and positive on `L²(-a,a)` with operator norm at most `4a`, by two explicit Fourier feature vectors.

With `y0=141347/10000` and `|gamma-y0|<r=1/500`, the finite observer uses `K_y0=2cos(y0(x-y))`. The mean value inequality gives uniform kernel error `<=2r|x-y|<=4ar`; the elementary Schur bound on an interval of length `2a` supplies the **whole-space operator bound**

\[
\boxed{\|K_\gamma-K_{y_0}\|_{L²(-a,a)\to L²(-a,a)}\le8a²r.}\tag{TC5}
\]

For the concrete `a=1/2`, this is `1/250`. The entire source-facing phase kernel at rational separations `|x-y|<=1` is certified by outward rational cosine plus `2r|x-y|`, not a fitted zero frequency. This is actual operator-level transport of a *finite* Weil spectral shadow. It does NOT source-identify the full Weil quadratic form with a positive Gram; the signed remainder remains the RH-hard barrier.

## TC-06 — **stronger Plato-cave countermodel inside the critical strip** (PROVED LOCAL algebra)

Even real entire functions can share the authentic first two Taylor coefficients, symmetry, and the same Fock budget yet exhibit off-line zeroes **inside** the classical critical strip.

Let `a0,a1` denote the authentic first two coefficients of `F(z)` (not externally measured zeros). The parent theta certificate establishes `|a0|<1/2`, `|a1|<1/80`. Set

\[
z_*=\tfrac14+20i,\quad
M(z)=(1-z²/z_*²)(1-z²/\bar z_*²)=1+c z²+d z⁴,
\]

where `c=204768/40972801`, `d=256/40972801`. Define

\[
\boxed{G(z)=[a_0+(a_1-a_0c)z²]M(z).}
\]

Then `G(0)=a0`, `[z²]G=a1`, and `G` is even and real-coefficient entire. But `G(z_*)=0`, corresponding to `s=3/4+20i`, *off the critical line inside* `0<Re(s)<1`; reflections give its companions. The direct even Fock polynomial norm is

\[
\|G\|_{\mathcal F}²=|a_0|²+2|a_1|²+24|a_2'|²+720|a_3'|²<1/3<260/27.
\]

The inequality holds even using crude rational coefficient bounds `|a0|<=1/2`, `|a1|<=1/80`, `c<1/100`, `d<1/100000`. `G` **is not the authentic Euler/theta source** and need not satisfy a Weil explicit formula as an L-function. It refutes the invalid finite-shadows+Fock-bound→RH inference, not RH.

## TC-07 — cave interpretation and exact next contract

An observer can reconstruct source-justified finite spectral properties without reading any preexisting zero list. The *true* analytic source fixes the entire function by its open Euler germ and Poisson transport; isolated finite shadows, even with excellent regularity and many constraints, do not. Contour Rouché gives one source-authentic positive Weil spectral projection. To prove the original **global** signed Weil form is nonnegative, one needs a source-first all-test bound on the complementary contributions, including genuine prime jets, Gamma/pole/contact and the full domain. All finite certified zeros on the line will not alone give that inequality; an infinitely high off-line zero remains a logically permitted alternative until excluded by source mathematics.

**Next discriminating experiment:** construct rational certified contour winding for more general source-derived rectangles and test-family forms; develop signed Weil spectral-tail estimates whose sign/absolute debt is derived from the authentic Gamma+prime source, rather than from a list of presumed critical zeros. A quantitative domination theorem controlling the complete remainder would be genuine progress toward Suzuki's conjectural global operator limit or Weil positivity.

## Validation, provenance and falsifiers

Artifacts: `observational_succ/theta_complex_contour.py` (pure integer/rational interval arithmetic), `theta_suzuki_shadow.py` (Weil-local typed operator and fake source controls), `tests/test_theta_complex_contour.py` (18 methods), source replay script, independently implemented 65-digit diagnostic, frozen rational receipt and a scoped claim ledger/RH handoff.

The independent mpmath `gamma*zeta` and direct theta integrals were used **only after the zero-independent rational certificate was built**, as numerical calibration; no precomputed zero ordinates are imported. They agree in center value and derivative to better than `3e-34` at 65 decimal digits. **Those readings are not the interval proof.** The proof uses an authentic Gaussian theta local-mode and time tail bound. Negative controls: forged contour width/site, illegal theta mode for the declared finite cutoff, absence of source-replay, wrong phase, omitted boundary sign, fake off-line strip zeros within a Fock budget, source-blind claim that the rest of Weil is positive. An integer theta mode `n=6` is a lawful **composite integer** in the full theta source; it is not independently a primitive Euler prime. The computation's finite `n=1,2` budget rejects any undeclared extra mode for that reason alone.

Full repository CI and formal Lean kernels are **not claimed** unless the corresponding exact-head remote workflows pass. The independently authored local code/tests are not a full `main` checkout. No novel published priority, physical carrier, nontrivial-zero initial data or RH proof asserted.
