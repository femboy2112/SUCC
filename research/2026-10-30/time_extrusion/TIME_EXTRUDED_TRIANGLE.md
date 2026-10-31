# Operation TIME EXTRUSION — an exact source-locked triangular worldtube for BBP

**2026-10-30 · research-only, additive to SUCC Main XVI.** Baseline `e18ba565ca540adb7edf3292f5593929e76d91c5`, merged integration PRs #388/#389. Inherits but does not reprove the original four-pole source, Pascal/Gamma operational triangle (TG-01..TG-13), Main XVI golden-locus repair, Kepler III shrinking-target results, and source-relative origin. All original signed poles and the authentic `U_0=0` are immutable. **π normality and RH remain OPEN.** This document distinguishes source-derived classical identities, probabilistic couplings, arithmetic consequences of known irrationality estimates, and still-unproved signed dynamics.

## 1. A three-dimensional triangle whose diagonal is conserved

For all real `a>0`, retain the exact original source

\[
 Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0,\qquad
 R(a)=\int_0^\infty e^{-ax}Q(x)\,dx
 =\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}.
\]

The native clock is `a_n=8n-7>0` for `n>=1`, with `r_n=R(a_n)`. Let `f(x)=e^{-8x}` be the failure likelihood, `g(x)=1-e^{-8x}` success likelihood of SUCC's **declared auxiliary Pascal instrument**. For integers `n>=1`, `m>=0`, `0<=j<=m`, define the *unnormalized ONE-WORD measure*

\[
 \widetilde M_{n,m,j}(dx)
 =e^{-a_nx}Q(x)f(x)^{m-j}g(x)^jdx
 =e^{-[8(n+m-j)-7]x}Q(x)(1-e^{-8x})^jdx.\tag{ET-1}
\]

`m` counts sensor outcomes and `j` is the number of successes. It is not an assertion that π digits are drawn from this likelihood. The word-mass is exactly

\[
 C_{n,m,j}=\int\widetilde M_{n,m,j}
 =\sum_{k=0}^{j}(-1)^k\binom jk R(8(n+m-j+k)-7)>0.\tag{ET-2}
\]

The grade probability is `q_(n,m)(j)=binom(m,j) C_(n,m,j)/r_n`; the *conditional posterior* is `ν_(n,m,j)=M~_(n,m,j)/C_(n,m,j)`.

**ET-01: Exact time-extrusion/selection equation.** The two entire measures, not merely their total masses, satisfy

\[
 \boxed{\widetilde M_{n+1,m,j}=\widetilde M_{n,m+1,j},\qquad
 \nu_{n+1,m,j}=\nu_{n,m+1,j}.}\tag{ET-3}
\]

Consequently the extruded field depends on only two effective integer coordinates `v=n+m-j` and `j`; translations `(n,m,j)->(n+1,m-1,j)` at `m>=1` are **exactly flat** in unnormalized source space. This is the mathematically lawful version of “one more neutral failure selection establishes the next triangle's zero-relative posterior.” It holds for the *specified failure*; replacing a success selection by the same native clock shift is false. In normalized endpoint masses there is an explicit factor:

\[
 q_{n+1,m}(j)
 =\frac{m+1-j}{m+1}\frac{r_n}{r_{n+1}}\,q_{n,m+1}(j).\tag{ET-4}
\]

The usual Pascal diamond is `C_(n,m,j)=C_(n,m+1,j)+C_(n,m+1,j+1)`; the two update multipliers commute, so this declared source sheet is **flat even though outcomes are correlated through the shared latent `X`**. Flatness is not statistical independence, physical collapse, or a non-Abelian holonomy.

The probability of *m* consecutive failures at fixed initial source time n is `r_(n+m)/r_n`, tending to zero like `const_n/m²`. Thus an infinite all-failure branch is a **zero-probability event** under this declared observation law; each finite posterior is well defined, while an infinite realized no-success history cannot be assigned positive probability by the original model. This is the finite/infinite conditional event firewall.

## 2. Gamma shape and the harmonic–golden–Euler rank inside every vertical slice

Fix `j>=0` and let `v=n+m-j` tend to infinity. Set `A=8v-7` and scale `Z=A X` under the posterior `ν_(n,m,j)`. Since

\[
 Q(x)=15x-\frac{59}{2}x²+O(x³),\qquad
 (1-e^{-8x})^j=(8x)^j(1-4jx+O_j(x²)),
\]

we get the exact asymptotic law

\[
 Z\;\Longrightarrow\;\operatorname{Gamma}(j+2,1).\tag{ET-5}
\]

Set `lambda=(sqrt5-1)/2`. The marked harmonic–golden contrast is

\[
 D(j+2)=\psi(j+2)-\lambda^{j+2}
 =H_{j+1}-\gamma-\lambda^{j+2}.\tag{ET-6}
\]

This is source-derived as a *posterior readout* on the extruded triangle. At `j=0` it is the original Oily–Macaroni `D(2)=lambda-gamma`. In the special main-native diagonal `m=n`, the effective rate is `A=16n-8j-7`, and the same result holds for each **fixed** grade j.

**ET-02: Original-four-pole first finite correction to the selected face.** Put `r=j+2`, `c_j=59/30+4j`. A normalized Watson/Laplace expansion gives

\[
 \boxed{\mathbb E_{\nu_{n,m,j}}[\log Z-e^{-\lambda Z}]
 = D(j+2)-\frac{c_j}{A}\,[1+r\lambda^{r+2}]
 +O_j(A^{-2}).}\tag{ET-7}
\]

*Proof:* after the change of variable, the unnormalized shape-r Gamma density is multiplied by `1-c_j Z/A+O_j(Z²/A²)`. Dividing by its mass yields `1-c_j(Z-r)/A+O_j((1+Z²)/A²)` in integrated observables with the displayed logarithmic integrability. For `G_r~Gamma(r,1)`,

\[
 \operatorname{Cov}(G_r,\log G_r)=1,\qquad
 \operatorname{Cov}(G_r,e^{-\lambda G_r})=-r\lambda^{r+2},
\]

using `1/(1+lambda)=lambda`. These give (ET-7). The remainder is for fixed j, not uniformly over j growing with n. The `59/30` term is `-Q''(0)/(2Q'(0))` from the **original four signed poles**; the `4j` term is the success-selection derivative. A source-mutant `Q_fake=15x` removes only the former. Independent high-precision direct quadrature and rational source tests are in the companion oracle.

**Golden-locus guard (Main XVI):** the auxiliary Galton–Watson root `q_(r,theta)=lambda^r` only on `theta=lambda/(1-lambda^r)`. The authentic clock `theta=1` intersects this locus only at r=2. Other rank-j readings can use `D_lambda(r)` but do not automatically inherit a self-consistent golden fixed point at the unaltered clock.

## 3. A sharp almost-sure *virtual-grade cone* over the native time extrusion

On the native Pascal diagonal `m=n`, write `J_n` for the auxiliary grade with exact probabilities `q_(n,n)(j)`, `0<=j<=n`. Its generating function at `z>1` is

\[
 G_n(z)=\mathbb E_{\mu_{a_n}}[z+(1-z)e^{-8X}]^n.
\]

For `1<z<2`, use `1-e^{-8X}<=8X` and `1+t<=e^t` to obtain

\[
 G_n(z)\le\frac{R(8n(2-z)-7)}{R(8n-7)}.\tag{ET-8}
\]

The inherited authentic four-pole mean bound `E_mu_a X<2/a` implies `R(b)/R(a)<(a/b)^2` for `0<b<a`. For `n>=ceil(7/[4(2-z)])` this proves the **all-grade Chernoff estimate**

\[
 \boxed{\Pr(J_n\ge M)\le\frac4{(2-z)^2}z^{-M}}\tag{ET-9}
\]

for every integer M>=0, with no independence hypothesis. Choose any `epsilon>0`, then any `z` with `2^{1/(1+epsilon)}<z<2`. The sum over n of probabilities that `J_n>=(1+epsilon)log_2 n` is finite. The first Borel–Cantelli lemma therefore proves, **for every coupling whatsoever of the specified native cross-sectional grade marginals**,

\[
 \boxed{\limsup_{n\to\infty}\frac{J_n}{\log_2 n}\le1\quad\text{almost surely}.}\tag{ET-10}
\]

**Sharpness as a coupling theorem, not as a deterministic π-path statement.** The inherited TV estimate from PR #370 is `TV(q_(n,n),w)<=22/n`, with `w_j=(j+1)/2^(j+2)`. For `M_n=floor((1-epsilon)log_2 n)` the exact tail `(M_n+2)/2^(M_n+1)` dominates `22/n` and has divergent sum. Thus for **independently coupled** grade cross-sections, the second Borel–Cantelli lemma gives the reverse limsup bound `>=1`, hence exact equality. Other couplings can have different lower limits. This is a probabilistic virtual-field **cone**, *not a deterministic restriction on which grade could be chosen at every time*. Every finite grade including grade n has positive probability.

This result is relevant to the user's three-dimensional volume: although each time slice has n+1 grade nodes, almost every realized virtual path under any legitimate coupling eventually lies beneath a **logarithmic face**, while the underlying deterministic circle trajectory remains unconstrained by that cone.

## 4. Exact arithmetic phase worldtube, and the integer seam that survives recentering

The actual original recurrence is

\[
 U_0(s)=s,\quad U_n(s)=16 U_{n-1}(s)+r_n,\quad
 T_n=\sum_{k\ge1}16^{-k}r_{n+k},\quad16T_n=r_{n+1}+T_{n+1}.
\]

For n>=1, define the actual fractional phase `x_n(s)={U_n(s)}`, and the **source-zero-relative** phase `y_n(s)={x_n(s)+T_n}`. Then

\[
 \boxed{y_{n+1}=\{16y_n\},\qquad
 y_n(s)=\{16^{n-1}(\pi+16s)\}.}\tag{ET-11}
\]

The original forcing is *exactly conjugate through a time-dependent coordinate translation* to multiplication by 16. The source-distance bound is inherited: `d_circle(x_n,y_n)<=T_n<(8n+1)^(-2)`, and the entire transverse worldtube has finite displacement budget

\[
 \boxed{\sum_{n=1}^\infty T_n
 =-\frac\pi{20}+\frac{\sqrt2\pi}{48}+\frac{\log2}{24}
 +\frac{\sqrt2\log(1+\sqrt2)}{24}
 =0.01629699773382656\ldots.}\tag{ET-12}
\]

The numerical and closed form are **inherited** from PR #378, not discoveries here. For any circle-Lipschitz `f`, every N and seed,

\[
 \left|\sum_{n\le N}(f(x_n)-f(y_n))\right|
 \le\operatorname{Lip}(f)\sum_{n\le N}T_n.
\]

In particular for `e_h(x)=exp(2pi ihx)` the *unnormalized* Weyl sums differ by at most `2pi|h| times ET-12`, independent of N. This is an exact representation bound, not a bound on either sum.

**ET-03: integer seam cocycle — the part the smooth worldtube cannot erase.** For n>=1 let

\[
 \eta_n(s)=\lfloor x_n(s)+T_n\rfloor=\mathbf1_{y_n(s)<T_n},
 \quad d_{n+1}=\lfloor16y_n\rfloor,\quad
 \kappa_{n+1}=\lfloor16x_n+r_{n+1}\rfloor.
\]

All are exact; `eta` is the cut-crossing flag at the inertial origin. Then the complete integer lift satisfies

\[
 \boxed{\kappa_{n+1}=d_{n+1}+16\eta_n-\eta_{n+1}.}\tag{ET-13}
\]

*Proof:* write `y_n=x_n+T_n-eta_n`, multiply by 16, and apply `16T_n=r_(n+1)+T_(n+1)` and the exact two circle carry identities. This also proves `eta_n` is the complementary *zero-cut* shrinking target `0<=y_n<T_n`. Kepler III's forcing correction target instead uses `[T_n,T_n+r_n)`. The two windows share an endpoint but encode different events: the thin worldtube's **branch cut** and the source's **carry correction**.

For the coherent same-forcing counterseed `s_*=-pi/16`, `y_n=0`, `x_n=1-T_n`, `eta_n=1`, `d_n=0`, `kappa_n=15` for all n>=2. Thus **despite exponentially tame/source-summable transverse displacement**, the symbolic carry labels stay maximally different. No smooth worldtube or positive virtual-field cone by itself proves selected digit normality. Exact Fractions certify ET-13 at the authentic seed and rational changed-seed controls for 40+ time steps.

## 5. A genuine arithmetic bound on long near-closed routes through the extruded volume

There is a simple but useful bound on where the **zero-seeded recentered trajectory** can remain for many stages. Let `b=16`, and suppose the base-b digit word of π starting at place `n` agrees for L consecutive digits with some infinite periodic word of period p>=1. Let its first p digits encode an integer `0<=c<=b^p-1`. The periodic rational point is `rho=c/(b^p-1)` (allow rho=1 for the all-15 expansion). With `M=floor(b^(n-1)pi)` we construct the exact rational

\[
 P/Q=\frac{M+\rho}{b^{n-1}},\qquad Q=b^{n-1}(b^p-1).
\]

Matching L digits gives `|pi-P/Q|<=b^{-(n-1+L)}`. The **published** Zeilberger–Zudilin irrationality-measure bound `mu(pi)<=7.103205334137...` implies for every `nu>7.103205334137...` and every sufficiently large n (uniformly over p and the periodic word),

\[
 \boxed{L\le(\nu-1)(n-1)+\nu\log_{16}(16^p-1)
 <(\nu-1)(n-1)+\nu p.}\tag{ET-14}
\]

Proof: eventual `|pi-P/Q|>=Q^(-nu)` and take base-16 logarithms. This is a *general periodic-shadowing exclusion*, not an equidistribution or digit-frequency estimate. It applies to the inertially recentered selected trajectory `y_n`, and to the original `x_n` only after retaining its source translation. It is not valid for arbitrary changed seeds (e.g. the coherent seed is exactly periodic). At finite horizons source-outward BBP intervals give rational digit certificates, but no finite sample implies the all-horizon bound. Source: Doron Zeilberger and Wadim Zudilin, *Moscow J. Comb. Number Theory* 9 (2020), 407–419, https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html.

**Research-status note (2026):** more recent preprints, including a September 2026 OpenAI mathematical release claiming `mu(pi)=2` with associated Lean formalization, would give a stronger conditional slope `nu-1` for every `nu>2` if independently accepted. Their external proof status is not needed or assumed here. The 2020 published bound suffices for the unconditional theorem above.

## 6. Exact failure mode and actual next proof gate

The operational **microstate extrusion** (ET-1..ET-10) and the **arithmetic worldtube** (ET-11..ET-14) are coupled by their common original source and native time clock, **but not by a source-derived stochastic law making the actual π carry select a particular Pascal outcome**. Attaching a deterministic phase/carry mark to an auxiliary `X` that has seed-blind source law makes the phase mark conditionally deterministic at fixed time. It does not force the posterior to update in response to the actual selected carry. That coupling would be an extra model assumption.

This rules out two easy but false proof strategies:
- Probability one virtual-grade confinement does not imply π itself is a typical virtual path. A fixed legal but probability-zero grade thread may violate the logarithmic cone.
- Summably small source recentering does not imply carry/digit statistics are stable. The exact cocycle ET-13 and coherent counterseed show the branch cut can preserve a radically different symbolic history.

**To move π normality:** prove a seed-zero-specific, signed, long-range estimate for the recentered beta-16 trajectory, possibly by bounding its occupancy of a family of periodic/quasiperiodic worldtube corridors beyond ET-14, **while retaining all four original signed poles and the literal integer seam**. A new result must improve on a known irrationality-measure exclusion or the trivial Weyl upper bound `|N^(-1) sum e(hU_n(0))|<=1` without assuming the same vanishing. Retain the Main XVI seed-alias control slate: coherent `-pi/16` and periodic `1/7` fail; circle aliases and constant 15-torsion twists are not distinguishable by an invariant magnitude observer. Do not merge proof-status labels with geometric equivalences.

## Reproduction

- `python time_extrusion_probe.py -v` — exact four-pole/triangle/normalization/cocycle controls and periodic rational hostile path.
- `python asymptotic_oracle.py` — high-precision direct original-source and Gamma-matched-mutant finite-jet checks.
- `python periodic_tube_probe.py` — exact BBP positive rational enclosures of finite π hexadecimal cylinders (finite observations only).
- `tests.log`, `oracle.log`, `finite_pi_cylinders.log` and `oracle.json` are scoped receipts; all proof universality comes from the derivations above, not the finite samples.
