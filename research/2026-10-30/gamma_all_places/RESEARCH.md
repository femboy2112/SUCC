# Gamma twist, prime snapshots, and the selected complex phase — rigorous all-place research round

**Scope.** Original SUCC four-pole source and seed only, except explicitly marked mutants. All new algebraic statements are paper-level proofs; code checks and high-precision calculations support reproducibility, not universal truth. No new π normality or RH theorem.

## 0. Source passport and the three distinct Gamma objects

Let `delta=(1,4,5,6)`, `c=(4,-2,-1,-1)`, `alpha_delta=delta/8`, and

\[
r(n)=\sum_\delta\frac{c_\delta}{8(n-1)+\delta},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The original BBP identity gives `U_n=16^(n−1)π−T_n` with positive future tail `T_n=Σ_{j>=1}16^{-j}r(n+j)`. The source is the Laplace transform of `Q(x)=4−2e^{-3x}−e^{-4x}−e^{-5x}>0`.

**Different objects, same source support:**

- **Ordinary Gamma time cocycle:** `G_infty(t)=Π_delta Gamma(t+delta/8)^c_delta`, and `H_infty(t)=G_infty(t+1)/G_infty(t)=Π_delta (t+delta/8)^c_delta`.
- **All-prime integer-affine Morita ratio:** `H_p^aff(t)=Π_delta [Gamma_p(8t+delta+1)/Gamma_p(8t+delta)]^c_delta`, defined on `Z_p` for *every* prime including `2`. It is not the value of `G_infty(t)` in a p-adic embedding, nor generally the fractionally shifted `Π Gamma_p(t+delta/8)^c_delta` used in earlier GTP work.
- **Gross–Koblitz finite-field Gamma product:** `Π_i Gamma_p(<p^i delta/8>)`, for a multiplicative character whose order divides eight over a suitable finite field. It is not a known character formula for the selected π real orbit.

Do not silently identify these structures; derivation of a connecting morphism is a separate obligation.

## GPR-01: a single affine argument regularization covers every prime

For `p` prime define `L_delta(t)=8t+delta`. Morita's published recurrence reads

\[
\Gamma_p(z+1)/\Gamma_p(z)=\begin{cases}-z,&z\in\mathbb Z_p^\times,\\-1,&z\in p\mathbb Z_p.\end{cases}
\]

All `L_delta(t)` lie in `Z_p` for `t in Z_p`, **including p=2**. For integer coefficients `c`, define the unit-valued ratio

\[
\mathscr H_p(t)=\prod_\delta\left[\Gamma_p(L_\delta(t)+1)/\Gamma_p(L_\delta(t))\right]^{c_\delta}.
\]

On every p-adic residue disk with fixed set of unit channels, the Morita ratio is rational (`-L_delta` on units, `-1` on nonunits) and therefore locally differentiable. Common signs cancel because `Σ c_delta=0`. Without assuming an analytic global logarithm of `Gamma_p`, its ordinary logarithmic derivative is exact:

\[
\boxed{\frac18\frac{\mathscr H'_p(t)}{\mathscr H_p(t)}
=\sum_{p\nmid(8t+\delta)}\frac{c_\delta}{8t+\delta}.}
\]

The **rational comparison** with the real Gamma one-step derivative gives, at integer `t=n−1`,

\[
\boxed{r(n)-\frac18\mathscr H'_p(n-1)/\mathscr H_p(n-1)
=\Delta_p(n):=\sum_{p\mid(8n-8+\delta)}\frac{c_\delta}{8n-8+\delta}.}
\]

For odd `p` this recovers the earlier Morita unit/polar decomposition; for `p=2` it provides a legitimate affine-argument extension despite the original `delta/8` not belonging to `Z_2`. **Important boundary:** this is a one-*Gamma-argument*-step ratio, not `G_p(t+1)/G_p(t)` with step one in source time. The underlying phase transport is not yet controlled.

The four singular residue classes for `p>5` are distinct because differences of offsets are in `{1,2,3,4,5}`. The only collision primes are `2,3,5`. This recovers the exceptional-prime locus from the singular-channel geometry, not from integer-base equidistribution.

## GPR-02: exact p=2 polar defect and integrality criterion

At p=2, precisely the two even offsets `delta=4,6` are nonunits for **all** integer times. The affine-unit ratio reduces to

\[
\mathscr H_2(t)=\frac{(8t+1)^4}{8t+5},\qquad
\frac18\frac{\mathscr H'_2(t)}{\mathscr H_2(t)}
=\frac4{8t+1}-\frac1{8t+5}.
\]

The missing two-channel defect is

\[
\boxed{\Delta_2(n)=-\frac2{8n-4}-\frac1{8n-2}
=-\frac{3n-1}{(2n-1)(4n-1)}\in\mathbb Z_2.}
\]

This explains the cancellation of nominally 2-singular terms: individually the two fractions need not be integral, while their sum is.

**Theorem (integer-coefficient 2-integrality).** Let `c=(A,B,C,D)` be *integers* at fixed offsets `(1,4,5,6)`. Then, for every integer n>=1,

\[
\boxed{r_c(n)\in\mathbb Z_2\quad\Longleftrightarrow\quad B+2D\equiv0\pmod4.}
\]

**Proof.** Odd-offset fractions are 2-integral. For even offsets, combine exactly:

\[
\frac{B}{4(2n-1)}+\frac{D}{2(4n-1)}
=\frac{B(4n-1)+2D(2n-1)}{4(2n-1)(4n-1)}.
\]

The denominator after the displayed factor 4 is odd. Its numerator modulo 4 is `−B−2D`, independent of `n`. Hence the pair is 2-integral iff the indicated congruence holds. No other term can cancel a nonintegral 2-primary part. Because the criterion is independent of n, holding at one n actually implies holding at every n. The authentic vector has `B+2D=−4`, so it passes. The previously proposed age-matched two-pole mutant `(5,−5,0,0)` fails and has v2(source)=-2. ∎

The authentic combined source denominator is odd for every n and `r(n)≡n mod2`, agreeing with Codex AT-04. This is a source-level 2-adic statement, not a claim about the distribution of π's hex digits.

## GPR-03: all-horizon fixed-precision source non-identifiability

Let `k(n)` denote the difference-source forcing generated by the coefficient vector `e=(1,−3,1,1)`, and define `c_t=c+t e`.

**Exact positivity / Gamma-matching.** In the Laplace representation write `q=e^{-x}`. The difference kernel is

\[
K(q)=1-3q^3+q^4+q^5
=(1-q)^2(q^3+3q^2+2q+1)\ge0\quad(0\le q\le1).
\]

The authentic kernel is strictly positive for `x>0`. Consequently, for every `t>=0`, the deformed kernel `Q_t(x)=Q_auth(x)+tK(e^{-x})` is positive. Because `K(e^{-x})=O(x^2)` near zero, its original rank-two Laplace boundary `Q_t(x)~15x`, and the associated Gamma(2) scaling, are identical to authentic. By the exact four-class matrix calculation in the earlier Gamma-twist dossier, all four Frobenius fractional age summaries are also identical for `c_t` (the kernel has `ages(e)=0`).

**Strong theorem (uniform in all time, arbitrary fixed p2 precision).** For any fixed integer `k>=1`, choose `t=2^{k+2}`. For *every n>=1*,

\[
\boxed{v_2(r_{c_t}(n)-r_c(n))=k,
\qquad v_2(U_n^{(c_t)}-U_n)=k.}
\]

**Proof.** In `k(n)`, the offset-4 contribution is `−3/[4(2n−1)]`, of 2-adic valuation `−2`; the offset-6 contribution is `1/[2(4n−1)]`, of valuation `−1`, and the odd-offset contributions are 2-integral. Thus `v2(k(n))=-2` with no possible cancellation. Multiplication by `t` gives source difference of valuation exactly `k` for all n. The orbit difference `D_n=16 D_(n−1)+t k(n)`, `D_0=0`; inductively, the first term has valuation `k+4` and the second exactly `k`, so `v2(D_n)=k`. ∎

Hence for any chosen precision `2^k`, *every selected rational source and orbit sample* agrees with authentic modulo `2^k`, over the **entire infinite time index**, although the forcing and its real radix constant differ. For k a multiple of 4 this includes any prescribed finite number of 2-adic hexadecimal digits. At the very first p=13 birth, however, `13 U_2^(c_t) ≡ −1+t (mod13)` while authentic has `−1`; `t=2^{k+2}` is never divisible by 13. Thus a genuine odd-prime snapshot separates them.

This is not a counterexample to source authentication by the *complete* four-pole vector or second source jet. Indeed `Q_t''(0)=−59+14t`: the original `−59` uniquely pins `t=0` within this family. It is a sharp counterexample to identifying a source from Gamma rank, Frobenius ages and any finite 2-adic observation resolution alone.

## GPR-04: the exact total Gamma Green-tail budget, and the selected phase

**Previously known:** SUCC has the identity `U_n=16^(n−1)π−T_n`, `T_n>0`, and an `O_h(1)` comparison of selected and pure-radix complex character sums. **New exact constant:** sum the *entire* positive Green tail in time.

From the four poles and `sum c=0`, the absolutely convergent unweighted source mass is

\[
S_R:=\sum_{n=1}^\infty r(n)
=-\frac18\sum_\delta c_\delta\psi(\delta/8).
\]

The proof inserts `1/(k+a)=ψ(k+a+1)−ψ(k+a)` into the partial sums, or uses the identity `sum_(k>=0)[1/(k+a)−1/(k+b)]=ψ(b)−ψ(a)`. Because `sum c=0`, the common harmonic divergence cancels. Independently,

\[
S_R=\int_0^1\frac{Q(u)}{1-u^8}\,du,\qquad
\pi=\int_0^1\frac{Q(u)}{1-u^8/16}\,du,
\quad Q(u)=4-2u^3-u^4-u^5.
\]

By Tonelli (all `r(n)` and `T_n` positive),

\[
\begin{aligned}
\sum_{n\ge1}T_n
&=\sum_{m\ge2} r(m)\sum_{j=1}^{m-1}16^{-j}\\
&=\frac1{15}\sum_{m\ge2}r(m)(1-16^{-(m-1)})\\
&=\boxed{\frac{S_R-\pi}{15}}
=\int_0^1\frac{u^8 Q(u)}{16(1-u^8)(1-u^8/16)}\,du.
\end{aligned}
\]

This positive integral is a separate derivation of the exact total, with no digit samples fitted. Numerically `S_R≈3.3860476195971917219364188314` and `B=(S_R−π)/15≈0.01629699773382656556491836` (80-digit numerical cross-check). The classical bound `T_n<(8n+1)^{-2}` implies the **rigorous tail remainder**

\[
0< B-\sum_{n=1}^{N}T_n <\frac{1}{8(8N+1)}.
\]

For integer h and all N, the elementary chord inequality gives the authentic source-to-pure-radix selected character bridge

\[
\boxed{\left|\sum_{n=1}^{N}e(hU_n)-\sum_{n=1}^{N}e(h16^{n-1}\pi)\right|
\le 2\pi|h|B\approx0.1023970567123181|h|.}
\]

This improves the explicit *constant* and conceptual Gamma source provenance of the already known `O_h(1)` comparison. It proves no cancellation by itself. Dividing by N makes the two normalized character averages differ by `O_h(1/N)`; hence normality of the actual BBP orbit remains equivalent to normality of π in base 16, not proved.

**Infinite phase holonomy:** the infinite product of termwise phase ratios converges absolutely and exactly to the scalar

\[
\prod_{n=1}^{\infty}\frac{e(hU_n)}{e(h16^{n-1}\pi)}
=\exp\big(-2\pi i h (S_R-\pi)/15\big).
\]

It is a source-authenticated Gamma/digamma *accumulated phase budget*, not a mixed signed covariance or a physical quantum holonomy. The same total scalar can coexist with different selected time correlations; no Weyl gain follows from its existence.

## GPR-05: a genuine Gross–Koblitz applicability test, not an inferred BBP Gauss representation

For an **odd** prime p, let `f=ord_8(p)` (1 when p=1 mod8, otherwise 2) and `q=p^f`, so `8 | q−1`. Choose the finite-field Teichmüller character `χ=\bar ω^((q−1)/8)` of order eight. Gross–Koblitz (published 1979) identifies appropriate nontrivial Gauss sums `g(χ^δ)` with p-adic Gamma values at the fractions `<p^i δ/8>` and an explicit prime-root uniformizer power. Normalize `v_p(p)=1`.

For the formally defined *weighted Gauss product* `A_p=Π_delta g(χ^delta)^{c_delta}` (negative powers are allowed because Gauss sums are nonzero), the theorem yields the exact valuation

\[
\boxed{v_p(A_p)=\sum_{i=0}^{f-1}\sum_\delta c_\delta\langle p^i\delta/8\rangle
=\begin{cases}
-15/8,&p\equiv1\pmod8,\\
-5/2,&p\equiv3\pmod8,\\
-5/4,&p\equiv5\pmod8,\\
0,&p\equiv7\pmod8.
\end{cases}}
\]

This is a valid finite-field/Γ_p character construction **for every odd prime**, including the formerly reflected residue classes by using `f=2`. The exact source support enters the character exponents and age sums. **But:** this Gauss product is not established to equal any selected original BBP time-window character sum, rational cofiber, or complementary real phase. It shares age valuations with the entire mutant family `c_t`, so valuations alone cannot distinguish the source. Do not infer Gross–Koblitz automatically supplies an arithmetic proof of π normality.

References: Gross–Koblitz, *Gauss sums and the p-adic Gamma-function*, Ann. Math. 109 (1979), 569–581, https://annals.math.princeton.edu/1979/109-3/p06 ; modern precise Morita recurrence in https://doi.org/10.1007/s40993-024-00593-8 ; original BBP four-pole source via Bailey, Borwein, Plouffe, *Math. Comp.* 66 (1997).

## GPR-06: the still-missing theorem and falsification program

We have **exact source identity**, **exact p-local snapshots**, **all-horizon finite p2 nonidentifiability**, **a full positive Γ-tail error budget**, and **a separate finite-field Gauss product**. We do **not** have a source-authenticated theorem that binds the Gauss-unit products or prime-polar terms to a nontrivial inequality for the **changing complementary real CRT phase** at the actual zero seed.

The earlier Codex SC-06 lag-one energy is a typed target, not a consequence of these Gamma identities; it must fail on coherent counterseed at the appropriate scoped observation and remain compatible with rational translations. An exact formal equality of Gamma and Gauss objects on the *source* side could be derived yet still fail this signed interaction test. Every proposed bridging operator must specify its domain/codomain, whether it is injective, exact time/prime dependence, its source-varying null mutants, and a quantitative non-identity (a signed saving, controlled remainder, or occupancy inequality) before being called an advance toward normality.

The positive `t=2^{k+2}` mutants from GPR-03, age-matched two-pole source, coherent seed `−π/16`, distinct integer-shift aliases, independent Stoneham c3/c5 normal sources and c2 nonnormal source are the mandatory controls. Preserve `Q''(0)=−59` when claiming source uniqueness; the Gamma rank and first jet alone are insufficient. No external academic novelty or physical Lorentz invariance is claimed.
