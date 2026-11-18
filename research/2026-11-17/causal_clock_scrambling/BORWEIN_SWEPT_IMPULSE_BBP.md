# Borwein Swept-Impulse Interferometry — One Rational Two-Pulse Kernel for R0 and Full Base-16 Normality

**SUCC / original four-pole BBP / Principia observer-volume / 2026-11-17**

**Originating proposal (Leah):** a point impulse is a broadband observation direction; sweeping a finite pulse and convolving its successive responses can expose structure at previously invisible support boundaries. The Borwein sinc-integral plateau and Dirac impulse are Fourier-related, “inside-out” perspectives. Use that geometry to construct the previously missing nonnegative \(\mathcal J_B\) from the actual zero-selected BBP orbit, with a proof of two comparison inequalities, and ideally one swept filter that sees every digit-frequency mode.

**Verdict:** BSI-01–07 are exact/classical identities and rigorous equivalences with their stated domains. Their arrangement as an original-BBP source-rational observer interface is a **derived research construction**, not a claim of priority over classical Fourier inversion, Borwein integrals, Weyl, or the already established endpoint norm. **There is no proof that the required all-late-shell inequality holds for π; π base-16 normality remains OPEN.**

## 1. Dirac versus Borwein: precise Fourier common-basis relation

With \(\operatorname{sinc}(t)=\sin(t)/t\), a Dirac delta \(\delta_0\) has constant Fourier transform \(1\). The normalized rectangular density
\[
b_a(x)=\frac1{2a}\mathbf1_{[-a,a]}(x)
\]
has Fourier transform \(\widehat b_a(t)=\operatorname{sinc}(at)\). Therefore a product of sinc functions is the Fourier transform of the **convolution** of their corresponding uniform densities. A sinusoidal steady-state is a single-frequency signal, not an impulse filter. A Borwein *integral* is a scalar functional of this convolution, not a time-domain step function; its plateau is support geometry.

For independent formal uniforms \(X_j\sim \mathrm{Unif}[-a_j,a_j]\), the symmetric Fourier inversion gives, for at least one \(a_j>0\),
\[
\boxed{
I_{\bf a}(\theta)
:=\int_0^\infty\cos(\theta t)\,\operatorname{sinc}(t)
\prod_{j=1}^m\operatorname{sinc}(a_jt)\,dt
=\frac\pi2\,\Pr\left(\left|\theta+\sum_jX_j\right|\le1\right).
}\tag{BSI1}
\]
For \(m\ge2\) the integral is absolutely convergent. The independent uniforms are a **chosen mathematical representation of a test kernel**, not new actual randomness injected into π or a replacement for BBP's source-null seed.

**BSI-01 (EXACT Borwein support threshold):** write \(A=\sum_j a_j\). If \(A\le1\), \(I_{\bf a}(0)=\pi/2\). If \(A>1\), a strictly positive support fraction escapes and \(I_{\bf a}(0)<\pi/2\). This explains the classical sequence with \(a_j=1/(2j+1)\): the first failure is at \(j=7\), where
\[
A=\frac{46027}{45045}=1+\frac{982}{45045},\quad
\boxed{\Pr\left(\left|\sum_{j=1}^7X_j\right|>1\right)
=\frac{6879714958723010531}{467807924720320453655260875000}.}\tag{BSI2}
\]
Proof: set \(Y_j=X_j+a_j\sim[0,2a_j]\). By central symmetry \(\Pr(S>1)=\Pr(\sum Y_j<A-1)\). Because \(A-1<\min_j2a_j\), the leaking simplex is untruncated, with volume \((A-1)^7/7!\); divide by \(\prod_j2a_j\) and double. This exact rational value matches classical Borwein integral evaluations (Borwein–Borwein; Bailey et al.; Fourier random-walk derivations).

More generally, when \(A=1-\delta\), at an edge displacement \(d=\delta+\varepsilon\) with \(0\le\varepsilon\le2\min_j a_j\), the same simplex argument gives
\[
\boxed{\Pr(|d+\textstyle\sum_jX_j|>1)
=\frac{\varepsilon^m}{\Gamma(m+1)\prod_j(2a_j)}.}\tag{BSI3}
\]
The order-\(m\) boundary activation and \(\Gamma(m+1)=m!\) are **genuine simplex/convolution geometry**, not an assertion that increasing m guarantees more information or uniform convergence.

## 2. Two pulses cancel the first observer's blind Fourier classes

Choose the fixed *rational* widths
\[
\boxed{\delta=1/18,\quad a=17/36,\quad A=2a=17/18=1-\delta,\quad c=1/(2A^2)=162/289.}\tag{BSI4}
\]
Let \(X_1,X_2\sim \mathrm{Unif}[-a,a]\), and let \(d(\theta)=\|\theta\|_{\mathbb T}\in[0,1/2]\).

**BSI-02 (EXACT quadratic Borwein leakage):** define the *periodized source-frame detector*
\[
\mathsf L(\theta)=1-\frac2\pi I_{(a,a)}(\operatorname{wrap}(\theta)).
\]
Since \(d(\theta)-\delta\le4/9<2a=17/18\), the simplex formula BSI3 holds on the **entire circle**:
\[
\boxed{
\mathsf L(\theta)=\frac{162}{289}\left(d(\theta)-\frac1{18}\right)_+^2,
\quad 0\le\mathsf L\le\frac{32}{289},\quad
\operatorname{Lip}(\mathsf L)=\frac{144}{289}.}\tag{BSI5}
\]
The wrap to the source circle is explicit: \(I_{\bf a}(\theta)\) on the real line is **not** periodically invariant until we specify \(\operatorname{wrap}\). We are not pretending that the auxiliary Borwein Fourier variable is the chronological BBP clock.

Its Haar mean is the exact rational
\[
\boxed{\overline{\mathsf L}=\int_{\mathbb T}\mathsf L(\theta)d\theta
=\frac{256}{7803}.}\tag{BSI6}
\]

**BSI-03 (PROVED all-nonzero-frequency response):** for \(h\in\mathbb Z\setminus\{0\}\), the Fourier coefficient is
\[
\boxed{
\widehat{\mathsf L}(h)
=4c\left[
\frac{(4/9)(-1)^h}{(2\pi h)^2}
+\frac{\sin(\pi h/9)}{(2\pi h)^3}
\right]\ne0.}\tag{BSI7}
\]
Proof: integrate \(2c\int_\delta^{1/2}(t-\delta)^2\cos(2\pi ht)dt\) by parts; the endpoint \(\sin(\pi h)=0\). In the resulting expression, \(\frac49|2\pi h|\ge8\pi/9>1\ge|\sin(\pi h/9)|\), so cancellation is impossible. In particular \(|\hat{\mathsf L}(h)|\asymp_h h^{-2}\) with a nonzero coefficient for **every h** and an absolutely convergent Fourier series.

**Hostile first-order comparison:** one single rectangular pulse with total width \(17/18\) has ramp leakage \((d-\delta)_+/(2A)\) and Fourier coefficient
\[
\widehat{\mathsf L}_1(h)
=\frac{(-1)^h-\cos(2\pi h\delta)}{A(2\pi h)^2},
\]
which is **zero whenever \(9\mid h\)**. A second pulse produces a quadratic hinge and removes these entire blind harmonic classes. This is a concrete operational reason to convolve, not merely to increase the volume of a metaphorical observer.

## 3. The original BBP source supplies the phases, not the auxiliary pulse noise

Keep **exactly**
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
With original \(x=\pi/16\), \(U_{2B}+T_{2B}=16^{2B}x\), and
\[
0<T_{2B}<r(2B+1)/15,
\]
define the genuine **anchored** Borwein shell energy
\[
\boxed{\mathcal J_B(x)=\frac1B\sum_{n=B}^{2B-1}\mathsf L(16^nx),}
\tag{BSI8}
\]
and its fully rational, original-source finite endpoint shadow
\[
\boxed{
\widehat{\mathcal J}_B
=\frac1B\sum_{k=1}^B\mathsf L\left(\frac{U_{2B}}{16^k}\right)
\in\mathbb Q.}\tag{BSI9}
\]

**BSI-04 (PROVED exact source-rational shadow estimate):**
\[
\boxed{
|\mathcal J_B(x)-\widehat{\mathcal J}_B|
<\epsilon_B,\qquad
\epsilon_B=\frac{16\,r(2B+1)}{7225B}=O(B^{-3}).
}\tag{BSI10}
\]
Proof: by \(\operatorname{Lip}\mathsf L=144/289\) and \(x-U_{2B}/16^{2B}=T_{2B}/16^{2B}\), the average difference is at most \(\frac{144}{289}\frac1B\sum_{k=1}^B T_{2B}16^{-k}<\frac{144}{289}\frac{r(2B+1)}{225B}\), which reduces to \(\epsilon_B\). **No altered forcing, injected random seed, source-blind empirical π digits or Gamma completion is used to compute finite certificates.**

## 4. The fixed Borwein detector is EQUIVALENT to the original R0 anti-locking rung

Let \(d_n=\|16^nx\|_{\mathbb T}\) and \(E_B=B^{-1}\sum_{n=B}^{2B-1}d_n^2\). Elementary cosine bounds imply
\[
8E_B\le1-\Re W_B(x)\le2\pi^2E_B,
\]
so R0 is equivalent to \(\liminf_BE_B>0\).

For each phase \(\mathsf L(\theta)\le c\,d(\theta)^2\), hence \(\mathcal J_B\le cE_B\). A uniform positive \(\liminf\mathcal J_B\) therefore implies R0.

**BSI-05 (PROVED reverse comparison using the actual radix-16 map):** choose the *rational* inner threshold
\[
\boxed{\delta'=35/612,\quad
\delta<\delta'<1/17,\quad C_0=\frac{256}{255}(\delta')^2.}
\]
On any consecutive run of phases with \(d_n<\delta'\), the signed representatives satisfy \(v_{n+1}=16v_n\) with **no integer wrap** because \(|16v_n-v_{n+1}|<17\delta'<1\). Therefore that run's squared energy is less than \(C_0\), regardless of its length.

Let \(H_B=\#\{n\in[B,2B-1]:d_n\ge\delta'\}\). There are at most \(H_B+1\) maximal cold runs, each with energy \(<C_0\); each hot position contributes at most 1/4. Thus
\[
\boxed{E_B\le\frac{(1/4+C_0)H_B+C_0}{B}.}\tag{BSI11}
\]
Meanwhile every hot position contributes at least \(c(\delta'-\delta)^2=c/612^2\) to the Borwein energy:
\[
\boxed{\mathcal J_B(x)\ge\frac{c}{612^2}\frac{H_B}{B}.}\tag{BSI12}
\]
It follows that \(\liminf_BE_B>0\implies\liminf_B\mathcal J_B>0\). Together with the easy direction and BSI10,
\[
\boxed{
\mathrm{R0}(x)\quad\Longleftrightarrow\quad
\liminf_{B\to\infty}\mathcal J_B(x)>0
\quad\Longleftrightarrow\quad
\liminf_{B\to\infty}\widehat{\mathcal J}_B>0
\ \text{ for the actual BBP }x.}\tag{BSI13}
\]
The first equivalence works for **any real x** under the radix-16 map, while the last rational-shadow comparison requires the **authenticated original BBP source and its tail**.

**OPEN arithmetic debt:** the source-specific all-late-shell positive lower bound for \(\widehat{\mathcal J}_B\). This is a new equivalent proof direction, **not an established asymptotic estimate**.

## 5. One fixed two-pulse kernel, swept around all origins, tests ALL Fourier modes

Write the shell empirical measure \(\mu_B^x=B^{-1}\sum_{n=B}^{2B-1}\delta_{16^nx\bmod1}\). This use of Dirac \(\delta\) is a **point mass on the circle**, distinct from the physical observer's tagged zero \(0*J\) and the Mellin-exponent source impulse mask \(Q=(1-S)H\).

Define a fixed two-sinc filter swept across the *observation-origin axis*
\[
\boxed{
\mathcal J_B^x(\alpha)
=\int_{\mathbb T}\mathsf L(\theta-\alpha)\,d\mu_B^x(\theta)
=\frac1B\sum_{n=B}^{2B-1}\mathsf L(16^nx-\alpha).
}\tag{BSI14}
\]
This is convolution on the circle with one fixed source-passported empirical measure. It does not alter π's seed, forcing or orbit.

**BSI-06 (PROVED single-kernel full-normality criterion):** since every \(\widehat{\mathsf L}(h)\ne0\) for \(h\ne0\),
\[
\boxed{
x\text{ is base-16 normal}
\quad\Longleftrightarrow\quad
\sup_{\alpha\in\mathbb T}
\left|\mathcal J_B^x(\alpha)-\frac{256}{7803}\right|
\longrightarrow0\quad(B\to\infty).
}\tag{BSI15}
\]
Proof (⇒): Weyl normality says \(\mu_B^x\) converges weakly to Haar; the translated family \(\mathsf L(\cdot-\alpha)\) is uniformly bounded and equi-Lipschitz, hence convergence is uniform over \(\alpha\) (also follows from the absolutely convergent Fourier series). Proof (⇐): the h-th \(\alpha\)-Fourier coefficient of \(\mathcal J_B^x\) is \(\widehat{\mathsf L}(h)\overline{W_B^x(h)}\); convergence to the constant Haar mean forces \(W_B^x(h)\to0\) because \(\widehat{\mathsf L}(h)\ne0\). Weyl then gives normality. Dyadic-shell Weyl convergence is equivalent to ordinary Cesàro Weyl convergence (apply the half-interval recurrence for even/odd N and boundedness).

**Operational content:** the infinitely many harmonic tests are repackaged into the **spatial-origin sweep of one fixed two-pulse filter**. There is no asserted algorithmic speedup or independent new arithmetic normality estimate. The entire \(\sup_\alpha\) quantifier remains to be controlled on all late shells.

## 6. One rational terminal endpoint gives a fully rational finite full-normality diagnostic

Using \(q_B=P_{2B}=U_{2B}/16^{2B}\), define the rational translated response
\[
\widehat{\mathcal J}_B(\alpha)=\frac1B\sum_{k=1}^B
\mathsf L\left(\frac{U_{2B}}{16^k}-\alpha\right).
\]
The uniform Lipschitz/tail estimate BSI10 applies for **every** \(\alpha\):
\[
\boxed{
\sup_{\alpha\in\mathbb T}
|\mathcal J_B^x(\alpha)-\widehat{\mathcal J}_B(\alpha)|<\epsilon_B.}\tag{BSI16}
\]
Hence
\[
\boxed{
\pi\text{ base-16 normal}
\iff
\underbrace{\sup_{\alpha\in\mathbb T}
\left|\widehat{\mathcal J}_B(\alpha)-\frac{256}{7803}\right|}_{\mathcal D_B\ \in\mathbb Q}
\to0.
}\tag{BSI17 — EQUIVALENT/OPEN}
\]

**BSI-07 (PROVED exact rational finiteness):** for the original zero-seeded \(U_{2B}\in\mathbb Q\), \(\widehat{\mathcal J}_B(\alpha)\) is a periodic **piecewise quadratic** function of \(\alpha\), with rational breakpoints at the rational phases plus or minus \(\delta\), and at antipodal phase points. On each interval the derivative is linear with rational coefficients. Therefore its global extrema (and \(\mathcal D_B\)) occur at rational endpoints or rational quadratic vertices, and \(\mathcal D_B\) is **computable by finite exact rational arithmetic for every B**. The [focused tests](../../../tests/test_borwein_bbp_sweep.py) include an independent vertex/endpoint implementation, as well as all finite source-tail and spectral controls.

### Finite samples: observed, not predictive

| B | Exact source shadow \(\widehat{\mathcal J}_B(0)\), decimal view | Exact swept \(\mathcal D_B\), decimal view |
|---:|---:|---:|
| 4 | 0.0533852829065 | 0.0242113055283 |
| 8 | 0.0502716494508 | 0.0222601578762 |
| 16 | 0.0292868871480 | 0.0219138312770 |
| 32 | 0.0315644418506 | 0.0057979609367 |
| 64 | 0.0347618039043 | 0.0043242080699 |

Additional source-rational shadow values: B=128 gives 0.0357111154444 and B=256 gives 0.0352099908653. The certified true-shadow errors satisfy \(\epsilon_B=16r(2B+1)/(7225B)\), decreasing as \(O(B^{-3})\). Every stated finite inequality was checked in full Fraction arithmetic; decimals are rounded displays and are NOT a trend extrapolation, prospective holdout, or normality proof.

## 7. A decisive safety/identity firewall and the actual remaining task

- The artificial uniforms in Borwein's convolution are **test-kernel integration variables**, not evidence that π phases are random. A moving observer origin is transported; it does not change the source seed.
- The Dirac point masses \(\mu_B^x\) record **actual deterministic phases**; their convolution with an auxiliary pulse is an **observer report**, not a new source history.
- The source-signed BBP Mellin mask \(Q(t)=4-2t^3-t^4-t^5=(1-t)H(t)\) acts on a **different lag axis** from \(\mathsf L\)'s phase-origin circle. Their conceptual impulse resemblance is not yet an intertwinement between these operators.
- Replacing one pulse by two *does* eliminate the first detector's exact blind harmonic classes, but it does not force the BBP empirical phase measure to become Haar; no Fourier coefficient of that measure has been bounded uniformly for all large B.
- The \(\Gamma(m+1)\) coefficient in the m-fold convolution simplex volume is an authentic mathematical role for Gamma; it does NOT automatically transport the separate BBP reciprocal-Gamma pole completion into the circle detector.
- The locked zero-seed modified forcing, \(x=0\), has \(\widehat{\mathcal J}_B=0\) when completed correctly, and its swept nonuniformity does not vanish. The nonunit fixed orbit \(x=1/15\) passes R0 but still fails the **full-normality** sweep. The rational \(x=1/17\) lies on the cold boundary \(1/17\); choosing our smaller \(\delta=1/18\) correctly detects it. Sparse Kempner-like changed-source cold shells still defeat an unconditional late-shell lower bound.
- The source-typed pairwise phase norm and Borwein detector are distinct valid R0/full-normality *equivalences*. Neither is an already-paid positive lower theorem.

**Verdict-changing offensive:** use the original BBP \(Q=(1-S)H\) signed source impulse, chronological zero section, carry/cofactor history and the new **quadratic support-leak** observable to prove *either* \(\liminf_B\widehat{\mathcal J}_B(0)>0\) (R0), *or*, much stronger, \(\mathcal D_B\to0\) (full normality). A winning source-derived correlation or inequality must predict why the genuine BBP source has different late-shell leakage from the locked and sparse adversaries. The new exact finite calculator and all-mode kernel provide a common-basis place to check such predictions without claiming they exist yet.

**Claim ledger:** BSI-01 exact/classical Borwein support identity; BSI-02 exact two-pulse formula; BSI-03 exact no-blind-mode Fourier theorem; BSI-04 exact zero-seeded BBP rational-tail shadow; BSI-05 classical dynamical equivalence to R0; BSI-06 classical single-kernel Weyl equivalence to full normality; BSI-07 exact finite rational vertex-algorithm certificate; asymptotic original BBP \(\mathcal D_B\to0\), R0 and full normality **OPEN**.

**References:** original Borwein–Borwein \(\operatorname{sinc}\) integrals and Fourier support interpretation: [MathWorld](https://mathworld.wolfram.com/BorweinIntegrals.html), [Bailey–Borwein–Kapoor–Weisstein, Ten Problems in Experimental Mathematics](https://mathexp.eu/bostan/ExpMath19/BaileyBorweinKapoorWeisstein2006_-_Ten_Problems_in_Experimental_Mathematics.pdf), [S. Lototsky's Fourier/random-walk treatment](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/BorweinIntegrals-RandomWalk.pdf). In-repo: [BBP Impulse/Mellin Filter](BBP_IMPULSE_MELLIN_FILTER.md), [Ordinal Mellin/Gamma Observer Tower](ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md), [Source-Null Section](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [terminal source norm and tail](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [source origin transport](CIRCLE_ZERO_FRAME_TRANSPORT.md), [Principia observer method](../../../docs/METHOD.md).

**Reproducibility:** [tests/test_borwein_bbp_sweep.py](../../../tests/test_borwein_bbp_sweep.py), [validation note](BORWEIN_SWEPT_IMPULSE_VALIDATION.md). Standard-library exact rational tests and separately implemented high-precision independent density/Fourier checks. Nothing here modifies original forcing, source seed, frozen provenance or main.
