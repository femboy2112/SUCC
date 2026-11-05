# Post-preregistration Gamma/Beta boundary estimate for the first active prime jet

**2026-11-05 — additive source-independent inequality applied to prime-power shifts.** This strengthens THEOREMS.md §3's earlier coarse bound by a factor 16/π. New-to-this-research-round observation, after preregistration; classical calculus and Cauchy–Schwarz, not an academic priority assertion. The constant π enters through an exact Beta integral, not a physical vacuum energy or the zeta zeros.

## Theorem: a negative prime shift needs an inverse-width smoothness budget

Let I=(0,D) with D=a+δ, \(a>0\), \(0<δ<a\). For \(f\in H^1_0(I;\mathbb C)\) and \(g(a)=\int_0^\delta f(x+a)\overline{f(x)}dx\), define the self-adjoint signed jet \(J=-w(S_a+S_a^*)\), \(w>0\). Its (negative or positive) expectation is \(\langle f,Jf\rangle=-2w\operatorname{Re}g(a)\).

The zero boundary condition at 0 implies, for 0<x<δ,
\[
|f(x)|=\left|\int_0^x f'(u)du\right|
\le\sqrt x\,\|f'\|_{L^2(0,\delta)}.
\]
The zero condition at D=a+δ likewise implies
\[
|f(x+a)|=\left|\int_{x+a}^D f'(u)du\right|
\le\sqrt{\delta-x}\,\|f'\|_{L^2(a,D)}.
\]
Multiplying and integrating gives
\[
|g(a)|\le
\int_0^\delta\sqrt{x(\delta-x)}dx\;
\|f'\|_{L^2(0,\delta)}\|f'\|_{L^2(a,D)}.
\]
The integral is EXACTLY
\[
\int_0^\delta\sqrt{x(\delta-x)}dx
=\delta^2 B(3/2,3/2)
=\delta^2\frac{\Gamma(3/2)^2}{\Gamma(3)}
=\boxed{\frac{\pi\delta^2}{8}} .
\]
Because the two derivative intervals are disjoint (\(δ<a\)), \(2ab\le a^2+b^2\) yields the **new stronger bound**
\[
\boxed{
|\langle f,Jf\rangle|
\le\frac{\pi w}{8}\,\delta^2\|f'\|_{L^2(I)}^2.
}\tag{BG1}
\]
The constant is a **valid nonsharp upper bound**; no extremality claim is made. It is strictly stronger than the previous \(2wδ²\|f'\|²\) and has a transparent mathematical Gamma origin.

For a normalized \(f\) with \(|\langle f,Jf\rangle|\ge\eta w\), \(0<\eta\le1\), BG1 forces
\[
\boxed{\|f'\|_2\ge\sqrt{8\eta/\pi}/\delta.}\tag{BG2}
\]
In particular any normalized probe approaching the ±w operator norm immediately after the gate requires an H¹ derivative budget growing at least as \(δ^{-1}\). The ordinary L² operator norm still JUMPS from 0 at δ=0 to w for every δ>0: the two statements concern different test regularities and have no contradiction.

### Concrete p=2 threshold and relation to SUCC Gamma geometry

At the first nonzero zeta prime-power gate, \(a=\log2\), \(D=2L\), \(L_0=\log2/2\), \(δ=2L-\log2\). The prime-2 jet has \(w=\log2/\sqrt2\), giving
\[
\boxed{|\langle f,J_{2,1,L}f\rangle|
\le \frac{\pi\log2}{8\sqrt2}\,(2L-\log2)^2\|f'\|_2^2}
\qquad \left(\frac{\log2}{2}<L<\log2\right).\tag{BG3}
\]
This π is the same classical Γ ratio \(\Gamma(1/2)^2=\pi\) up to the recurrence \(\Gamma(3/2)=\Gamma(1/2)/2\), not an independent discovery of a new π. It is a genuine **source-specific coefficient** once the p=2 Euler jet weight is inserted, but still an observer-regularity inequality rather than full RH positivity.

A real signal f with two matching sin-shaped packets on (0,δ) and (a,a+δ) has normalized negative expectation -w and normalized \(\|f'\|_2^2=\pi^2/\delta^2\). This is a direct countercontrol showing that the L² operator norm jump survives (at a price in derivatives); the Gamma boundary bound is not a proof that prime energy vanishes for all normalized f as the threshold is approached. The opposite relative sign gives +w.

**Verdict:** BG1–BG3 are paper-proved under H¹_0 and 0<δ<a, and need no zeta zeros or SUCC BBP digits as input. Gamma/Beta occurs loadbearingly in the bounded smooth-interface estimate. Stronger archimedean Γ-form coercivity would be needed to conclude any Weil positivity beyond this estimate. RH remains OPEN; the authentic selected BBP π orbit remains separate.
