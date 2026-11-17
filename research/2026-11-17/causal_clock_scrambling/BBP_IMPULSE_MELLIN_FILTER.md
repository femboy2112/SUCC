# BBP Signed-Impulse Convolution — a Null Moment, Positive Memory, and Exact Analytic Pole Cancellation

**SUCC / original four-pole BBP / knowledge-volume observation basis — 2026-11-17**

**User-originating idea (Leah):** the source coefficients (4,2,1,1) form an additive hierarchy (1+1=2, 1+1+2=4), while the rational pole residues (1/2,-1/4,-1/8,-1/8) are the signed weights divided by 8. Convolving a source-centered signed impulse with a positive memory kernel may reveal exactly what survives the coarse zero and how the analytic completion transports it.

**Claim ledger:** IMF-01–06 are PROVED PAPER/CLASSICAL algebraic and analytic identities; IMF-07 is a precise spectral **limitation**, not a π normality proof. The source-original R0 lower bound and all-mode Weyl cancellation remain **OPEN**. These factorizations are source-attached derivations of the classical BBP identity, not claims of academic novelty, physical information scrambling, a QM/GR mechanism or a positive statistical Fourier estimate.

## 1. The coefficient/residue map is exactly normalization by 8

Retain without modification the literal source:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Every denominator has derivative 8 with respect to complex \(n\). Hence the poles \(7/8,1/2,3/8,1/4\) have residues
\[
\boxed{(4,-2,-1,-1)/8=(1/2,-1/4,-1/8,-1/8).}\tag{IMF1}
\]

The magnitudes have a **three-input additive relation** \(4=2+1+1\), consistent with the initial terms \(1,1,2,4\) of a Tribonacci-type recurrence; this is not the ordinary Fibonacci recurrence and does not impose a universal recurrence on subsequent BBP coefficients. The actual pole positions, not just their magnitudes, remain load-bearing. [Prior shift-orbit residue proof](BBP_POLE_SHIFT_CRUCIBLE.md) keeps the four pole classes distinct.

## 2. The literal convolution and one zero moment

Set \(a=8n-7\). The offsets of the four reciprocal denominators are precisely \(0,3,4,5\). In a *discrete Mellin-exponent/impulse-lag basis*, use formal impulse \(\delta_j\), convolution \((\delta_i*\delta_j)=\delta_{i+j}\), and the signed source mask
\[
\boxed{
\mu=4\delta_0-2\delta_3-\delta_4-\delta_5
=2(\delta_0-\delta_3)+(\delta_0-\delta_4)+(\delta_0-\delta_5).
}\tag{IMF2}
\]

Write its ordinary generating polynomial
\[
Q(t)=4-2t^3-t^4-t^5.
\]

**IMF-01 (EXACT convolution):**
\[
\boxed{
Q(t)=(1-t)H(t),\qquad H(t)=4+4t+4t^2+2t^3+t^4,
}\tag{IMF3}
\]
or in impulse notation
\[
\boxed{
\mu=(\delta_0-\delta_1)*
(4\delta_0+4\delta_1+4\delta_2+2\delta_3+\delta_4).
}\tag{IMF4}
\]

Thus the coarse DC/total-mass readout is null:
\[
Q(1)=\sum_j\mu_j=0.
\]
But the first signed lag moment is nonzero:
\[
\boxed{Q'(1)=\sum_jj\mu_j=-(2\cdot3+4+5)=-15,\quad H(1)=15.}\tag{IMF5}
\]

The equality \(15=16-1\) is exact and matches the multiplier \(Y_{n+1}-Y_n=15Y_n\) of the **completed** BBP real lift. However IMF5 is differentiated with respect to the *Mellin-exponent variable* \(t\), not a derivative in chronological \(n\). **No intertwinement between those operators has been derived from the matching coefficient alone.**

### Three directed positive source differences

**IMF-02 (EXACT positivity identity):**
\[
\begin{aligned}
r(n)&=2\left(\frac1a-\frac1{a+3}\right)
+\left(\frac1a-\frac1{a+4}\right)
+\left(\frac1a-\frac1{a+5}\right)\\
&=\boxed{\frac6{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)}>0.}
\end{aligned}\tag{IMF6}
\]
The three leading coefficients \(6,4,5\) total 15, so
\[
\boxed{r(n)=15/(64n^2)+O(n^{-3}).}\tag{IMF7}
\]
The original forcing is decreasing by the Mellin representation below. This source mask is more specific than an arbitrary positive \(n^{-2}\) forcing, but positivity/this coefficient do **not** force normality (see the locked-source rivals in the linked crucible).

## 3. Positive Mellin memory and exact root cancellation at radius sqrt(2)

A Mellin/Beta representation is
\[
\boxed{r(n)=\int_0^1 t^{8n-8}Q(t)\,dt.}\tag{IMF8}
\]
The positive kernel factorizes further:
\[
\boxed{H(t)=(t^2+2)(t^2+2t+2)>0\quad(0\le t\le1).}\tag{IMF9}
\]
Thus the signed mask has *one* zero at \(t=1\), while the remaining factors constitute a strictly positive real profile. Equivalently,
\[
\boxed{
r(n)=\sum_{j=0}^4\frac{h_j}{(8n-7+j)(8n-6+j)},
\quad(h_0,\ldots,h_4)=(4,4,4,2,1).
}\tag{IMF10}
\]
Every summand is positive. This is a weighted sum of five genuine **Beta(2)-type** rational integrals: \(\int_0^1 t^{a+j-1}(1-t)\,dt=1/[(a+j)(a+j+1)]\). The decomposition is exact, not an independent probabilistic assertion about π.

The completed BBP sum is uniformly absolutely convergent on \(t\in[0,1]\), so interchange with the integral gives
\[
\sum_{n\ge1}16^{-n}r(n)
=\int_0^1\frac{Q(t)}{16-t^8}\,dt.
\tag{IMF11}
\]

**IMF-03 (EXACT analytic source factor cancellation):** surprisingly, every root of \(H\) has modulus \(\sqrt2\), and the four roots are **among the eight poles of the geometric completion \(1/(16-t^8)\)**. Indeed
\[
\boxed{
16-t^8=(2-t^2)(t^2+2)(t^2+2t+2)(t^2-2t+2).
}\tag{IMF12}
\]
Consequently four off-axis completion poles cancel exactly:
\[
\boxed{
\frac{Q(t)}{16-t^8}
=\frac{1-t}{(2-t^2)(t^2-2t+2)}.
}\tag{IMF13}
\]

The four cancelled roots are \(t=\pm i\sqrt2,-1\pm i\). All have modulus \(\sqrt2\), and their eighth powers equal 16. The four remaining geometric poles are \(t=\pm\sqrt2,1\pm i\), also at that radius. The mechanism is ordinary polynomial factor cancellation; it is an exact source-respecting instance of **coarse analytic compression retaining endpoint information**, not a proof of digit statistics.

### Self-contained classical evaluation of the original π source

**IMF-04 (PROVED elementary BBP evaluation):** the rational integrand has an explicit primitive
\[
\boxed{
F(t)=\frac18\log\!\left[\frac{2-t^2}{t^2-2t+2}\right]
+\frac14\arctan(t-1).
}\tag{IMF14}
\]
Differentiation gives the reduced kernel (IMF13). At both \(t=0,1\), the logarithmic ratio is **exactly 1**, so the logarithm contributes zero to the definite integral; the arctangent gives \(F(1)-F(0)=\pi/16\). Therefore
\[
\boxed{
\sum_{n=1}^\infty16^{-n}r(n)=\frac{\pi}{16}.
}\tag{IMF15}
\]
This independently derives the *known* BBP identity from the exact original four poles, positive impulse convolution and elementary integration. The identity was known before this calculation; this derivation is not claimed to be novel.

## 4. The signed filter's exact Fourier null geometry

On \(|z|=1\), \(z=e^{i\theta}\), put \(c=\cos\theta\). Then

\[
\boxed{
|H(z)|^2=(1+8c^2)\left[8(c+3/4)^2+\frac12\right].
}\tag{IMF16}
\]

**IMF-05 (PROVED finite-filter spectral bounds):**
\[
\boxed{
\frac1{\sqrt2}|1-z|\le|Q(z)|\le15|1-z|,
\quad |z|=1.
}\tag{IMF17}
\]
The only unit-circle zero of \(Q\) is \(z=1\); all other roots have radius \(\sqrt2\). In any *separately declared* cyclic finite-difference observer with unitary shift \(S\),
\[
Q(S)=(I-S)H(S),\quad
\frac1{\sqrt2}\|(I-S)f\|_2\le\|Q(S)f\|_2\le15\|(I-S)f\|_2.
\tag{IMF18}
\]

For a length-\(N\) cycle and mean-zero input \(f\), the smallest nonzero shift frequency is \(|1-e^{2\pi i/N}|=2\sin(\pi/N)\), giving
\[
\boxed{\|Q(S)f\|_2\ge\sqrt2\sin(\pi/N)\|f\|_2.}\tag{IMF19}
\]
This **finite-size** gap tends to zero as \(N\to\infty\). A fixed zero reference removes the DC ambiguity, but does **not** generate a uniform infinite-horizon coercivity bound. This is an exact mathematical illustration of why a finite-resolution null-wall or finite positive response is not automatically a π anti-locking theorem.

**Type firewall:** the shift \(S\) here translates *the auxiliary impulse/Mellin-exponent index*. It is **not automatically** the original BBP chronological radix map \(n\mapsto n+1\). Applying IMF18 to the actual BBP circle phases requires a separately constructed source-valid intertwiner. Without it, the spectral bounds are properties of the source's coefficient mask, **not** of the distribution of π's hexadecimal digits.

## 5. Kempner seed ambiguity and the next verdict-changing probe

The base-16 Kempner source \(\kappa_{16}=\sum_{j\ge0}16^{-2^j}\) can indeed be implemented with numerical initial seed zero: \(K_0=0,\ K_n=16K_{n-1}+g(n)\) with \(g(n)=1_{\{n\text{ is a power of }2\}}\). It injects **additional source-law information** through the clock-selective forcing \(g\), not through the numerical seed. This is precisely the user's distinction. It is an adversarial source with a **different causal forcing passport**, not a legitimate alternative to the original BBP zero input.

**IMF-06 (REFUTED overstrong inference):** source-nullity alone cannot imply R0; neither the cancelling zeroth moment \(Q(1)=0\), the positive profile \(H\), the coefficient \(15\), nor the source-specific polynomial pole cancellation IMF13 does so without a nontrivial statement about the original integer winding and the completed radix orbit. The [positive monotone matched locked source](BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md) defeats coarse null/positivity/asymptotic conditions; Kempner defeats irrationality plus tiny source-input intuition.

**The new prospective lamp (OPEN):** derive a *lawful source-history-to-circle-phase transport* from the exact analytic impulse/cancellation structure (IMF2–16) to the authenticated original zero-selected terminal winding \(U_{2B}\), with a **uniform** lower bound on separated backward directions
\[
\boxed{
\exists\epsilon,\vartheta>0,B_0\ \forall B\ge B_0:\quad
\#\left\{1\le k\le B:\left\|U_{2B}/16^k\right\|_{\mathbb T}\ge\epsilon\right\}
\ge\vartheta B.
}\tag{IMF20 — OPEN}
\]
The [proof-direction oracle](PROOF_DIRECTION_ORACLE.md) can verify finite candidates but cannot substitute an unproved global lemma. A winning source-derived transport must distinguish locked source families with similar kernels, shifted seeds, finite rational shadow and near-critical Kempner cold shells. If proven, (IMF20) would imply R0; full π normality still requires every nonzero Fourier mode.

**Execution/provenance:** focused exact rational tests [tests/test_bbp_impulse_filter.py](../../../tests/test_bbp_impulse_filter.py) check convolution, positive differences, Beta decomposition, geometric denominator cancellation, rational antiderivative and spectral factors. Independently executed SymPy tests prove the symbolic identities and integrate the reduced kernel to π/16; a separate 50-digit mpmath quadrature matched the same definite integral. [Validation receipt](BBP_IMPULSE_FILTER_VALIDATION.md) records the executed checks and no-go calibration.

**Source dependencies:** [original PI frontier](../../../docs/PI_NORMALITY_FRONTIER.md), [four integer-shift pole residues](BBP_POLE_SHIFT_CRUCIBLE.md), [source-null invariant](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [Mellin-positive BBP forcing](../../2026-11-16/defect_window_tomography/MOVABLE_BOUNDARY_ORDER_LIFT.md), [terminal rational norm](../../2026-11-16/defect_window_tomography/VIRTUAL_FIELD_FORM_METRIC.md), [source-history oracle](PROOF_DIRECTION_ORACLE.md), and [SUCC METHOD](../../../docs/METHOD.md). All exact identities share the original BBP coefficients and classical algebra; independent computation is implementation cross-checking, not independent arithmetic-source evidence.
