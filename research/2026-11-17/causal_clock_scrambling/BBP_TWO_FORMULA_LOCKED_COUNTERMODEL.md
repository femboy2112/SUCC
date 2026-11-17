# Two BBP π Forms Can Cancel into a Positive Non-Telescoping Locked Null-Seed Source

**SUCC / original zero-seeded π proof crucible, 2026-11-17**

**Originating objective:** determine whether source-nullity, BBP-like positive decreasing rational forcing, precise \(n^{-2}\) asymptotics and even the shift-orbit residue obstruction together force R0. **Result: NO.** An exact matched control fulfills these conditions while its completed circle orbit is locked.

**Status:** TFL-01–04 are proved rational-function/pole identities and a consequence of two imported classical BBP π series. The external equality of those established π series is a cited premise. This is **not** a counterexample to the authentic original four-pole source and not a proof of π normality.

## 1. Two separate authenticated BBP representations of π

Let the original BBP source be
\[
r_1(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]
The second published base-16 BBP formula (MathWorld BBP-Type Formula, equation 3) yields
\[
r_2(n)=\frac4{8n-6}+\frac2{8n-5}+\frac2{8n-4}-\frac1{2(8n-1)}.
\]
The referenced, already known identities state
\[
\boxed{\sum_{n=1}^\infty 16^{-n}r_1(n)=
\sum_{n=1}^\infty 16^{-n}r_2(n)=\pi/16.}\tag{TFL1}
\]
**Source citation:** https://mathworld.wolfram.com/BBP-TypeFormula.html , identities (2) and (3). We are *not* deriving their classical π evaluations anew in this note, and do not count their shared π value as an independent proof of π normality.

Let
\[
b(n)=\frac1{16n}+\frac5{128n^2},
\quad
\boxed{r_\flat(n):=r_1(n)-r_2(n)+16b(n)-b(n+1).}\tag{TFL2}
\]
This is a rational function of n with rational coefficients.

## 2. Exact null seed, rational endpoint, complete orbit lock

**TFL-01 (PROVED by telescoping and inherited identities):**
\[
\begin{aligned}
\sum_{n=1}^\infty16^{-n}r_\flat(n)
&=\underbrace{\pi/16-\pi/16}_{0}
+\sum_{n=1}^\infty16^{-n}[16b(n)-b(n+1)]\\
&=b(1)=\boxed{13/128}.
\end{aligned}
\tag{TFL3}
\]
The finite telescoping partial sum is \(b(1)-16^{-N}b(N+1)\to b(1)\). The exact *zero-seeded* solution \(V_0=0,\ V_n=16V_{n-1}+r_\flat(n)\) therefore has completed radix-16 circle phase \(e(16^n13/128)=1\) for **every \(n\ge2\)**. R0 is false for this fully specified alternative source.

It does not have the same forcing as the true BBP source. It is a source-class / observer-invariant **hostile control**, not a rival possible history of the authenticated original recurrence.

## 3. A full universal positivity and monotonicity certificate

**TFL-02 (PROVED rational polynomial identities):** the alternative source is strictly positive and strictly decreasing for **every real \(n\ge1\)**. It also satisfies
\[
\boxed{r_\flat(n)=\frac{15}{64n^2}+O(n^{-3}),}
\tag{TFL4}
\]
the exact leading behavior of the genuine BBP source.

The positivity and monotonicity have an explicit **integer-polynomial certificate**. Put \(t=n-1\ge0\). Direct common-denominator expansion yields
\[
r_\flat(t+1)=\frac{P(t)}{Q(t)},
\]
where
\[
\begin{aligned}
Q(t)=128&(t+1)^2(t+2)^2(2t+1)(4t+1)(4t+3)\\
 &\cdot(8t+1)(8t+3)(8t+5)(8t+7),
\end{aligned}
\tag{TFL5}
\]
and \(P(t)\) has the following **high-to-low degree** integer coefficient list:
\[
\boxed{
[3932160,\ 27312128,\ 75347968,\ 110058752,\ 98778592,\
62529440,\ 31089706,\ 11626701,\ 2665404,\ 261609].
}\tag{TFL6}
\]

Every coefficient of \(P\) is strictly positive, and \(Q(t)>0\) for all \(t\ge0\). Therefore \(r_\flat(t+1)>0\).

For strict decrease, use
\[
-\frac{d}{dt}\frac{P(t)}{Q(t)}
=\frac{P(t)Q'(t)-P'(t)Q(t)}{Q(t)^2}.
\]
Call the numerator \(M(t)\). Exact integer polynomial multiplication gives the **high-to-low degree** coefficient list:
\[
\boxed{\begin{aligned}
[&131941395333120,\ 2001386040459264,\ 13762724483825664,\\
&57107684758913024,\ 160843008730726400,\ 329019265493499904,\\
&513696538975797248,\ 640232253360701440,\ 665464316120268800,\\
&597697071217901568,\ 469917563475558400,\ 318523328139358208,\\
&180209372835896320,\ 82149333319184384,\ 29196492196348672,\\
&7823426192495104,\ 1515868579493376,\ 199353056366592,\\
&15846675014400,\ 571889382912].
\end{aligned}}\tag{TFL7}
\]

All 20 coefficients are positive, so \(M(t)>0\) and \(-r_\flat'(t+1)>0\) on \(t\ge0\), with no numerical interpolation assumption. The [exact rational/zero-polynomial regression](../../../tests/test_matched_nontele_locked_source.py) rebuilds and checks this certificate. A separate SymPy implementation verified the common-denominator identity, full coefficient lists and \(n^2\) asymptotic limit.

## 4. The rational pole-shift obstruction remains NONZERO

**TFL-03 (PROVED):** at the original pole \(n=7/8\), \(r_1\) has residue \(+1/2\). The second BBP source \(r_2\) and \(b(n),b(n+1)\) are all regular at that point, so
\[
\boxed{\operatorname{Res}_{n=7/8}r_\flat(n)=1/2.}\tag{TFL8}
\]
No other pole of \(r_\flat\) differs from \(7/8\) by an integer; thus this integer-shift orbit has one isolated nonzero weighted residue. By the rational difference-equation obstruction proved in [BBP Pole-Shift Crucible](BBP_POLE_SHIFT_CRUCIBLE.md), **there exists no rational function \(h(n)\) with \(r_\flat(n)=16h(n)-h(n+1)\)**.

**TFL-04 — decisive no-go:** The combination of
\[
\text{null input} + \text{positive decreasing rational forcing}
+\text{BBP leading \(15/(64n^2)\) asymptotic}
+\text{nonzero weighted pole-shift residues}
\]
does **not** imply R0. Even all those conditions can hold for an exactly zero-locked completed circle.

The complete **original forcing formula, its exact pole inventory and coefficients, and selected chronological winding** remain load-bearing. The statement “BBP has an uncancelled residue” is a valuable source discriminator against rational telescopers but not an asymptotic anti-locking mechanism by itself.

## 5. Connection to the zero/observer-volume thesis and next proof path

The two π representations have nontrivially different finite forcing trajectories; their **completed** source-weighted difference vanishes:
\[
\sum_{n\ge1}16^{-n}[r_1(n)-r_2(n)]=0.
\]
This is a concrete example of a globally vanishing source evaluation with a nontrivial function and surviving pole-orbit information before completion. It matches SUCC's source-typed contextual-zero and differential-history interpretation: **zero at one observation level does not imply zero source form**.

The additional \(b\) term produces a rational nonzero completed endpoint without erasing the non-rational source-memory obstruction. Neither effect amounts to a proof of stochastic digits, physical information scrambling, QFT, or GR.

**Next genuinely discriminating arithmetic proposal:** exhibit a **quantitative functional** on the *entire authenticated original BBP forcing and its zero-seeded integer winding* whose late-shell lower bound excludes both:
1. the matched locked source \(r_\flat\), which defeats positivity, asymptotic matching and isolated residue nonvanishing; and
2. the sparse badly approximable Kempner source, which defeats even optimal irrationality exponent plus infinite digit support.

The target remains \(R_B(0)\ge\delta>0\) for every sufficiently late B, not a source-coarse value that all three models share. Full normality further needs every nonzero Fourier mode.

**Claim ledger:** TFL-01, TFL-02, TFL-03 **PROVED PAPER (imported BBP formula + exact rational/polynomial identities)**; TFL-04 **REFUTED GENERAL INFERENCE**; π R0/normality **OPEN**. This test adds no new actual source history to the original BBP model.

**Dependencies:** [Contextual Zero](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md), [source-null invariant](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [BBP pole-shift weighted residue](BBP_POLE_SHIFT_CRUCIBLE.md), [original endpoint-norm frontier](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), and [SUCC Method](../../../docs/METHOD.md).
