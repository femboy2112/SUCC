# Inertial SUCC without absolute position: relative BBP normality, exact 15-torsion quotient, and the Gamma–Green memory constant

**Date:** October 29, 2026. **Status:** research-only scoped paper proofs and local reproducible tests; not kernel-checked, not independently peer reviewed. **Target parent:** draft PR #375 `bcc86f1f5edcb9696ae11451fb6dffede1530434` (inherited #371/#370/#369/#367; separate siblings #368, #373, #376 referenced by pin). **Original four-pole source and zero initial condition are immutable.** π-normality, nonnormality, RH, and any new selected signed `o(N)` estimate remain **OPEN**.

The author's guiding claim is: **the carrier is inertial, the unprepared actualized boundary is zero, and an observer may not know an absolute position even when the neutral fiber has rich fluctuations.** This document makes three independent interpretations explicit and separates their consequences:

1. **Unpointed coordinate freedom (gauge):** an observer cannot infer an absolute spatial origin from displacement readings. Mere ignorance cannot favor any numbered coordinate. There is no normalized translation-invariant probability on the noncompact real line.
2. **Marked inertial preparation:** once the actual carrier has a declared neutral identity and cost-free preparation operations, zero is the unprepared reference (see sibling PR #373). Its virtual fiber may carry an arbitrary nontrivial law `nu`; `delta_0 ⊗ nu` is not a physically empty field. Changing coordinates must transport the mark, dynamics, and forcing together.
3. **Arithmetic observation:** the full absolute zero-seeded BBP phase is **not necessary for normality discrimination**. A time-relative displacement *histogram*—even after discarding its order—still separates normal from nonnormal source orbits, because the original source asymptotically follows `x -> 16x mod 1`. This is a proved **criterion**, not an assertion that the source passes the criterion.

The largest new *quantitative* result is an original-four-pole, **uniform-in-lag** `O(1/N)` signed observation transport whose entire error budget is the finite, source-specific Gamma/digamma constant `M_BBP=0.0162969977...`.

## 1. Exact source and typed neutral carrier

The unchanged original BBP forcing, for every integer `n>=1`, is

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
 \qquad U_0(s)=s,\quad U_{n+1}(s)=16U_n(s)+r(n+1).
 \tag{IR-1}
\]

**The authentic selected source is `s=0`.** Other seeds are controls using the *same forcing*, not alternate original selections. The closed numerator-denominator is exactly

\[
 r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
\]

Put `Q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t}`, `t>0`. Then

\[
 r(n)=\int_0^\infty e^{-(8n-7)t}Q(t)\,dt,
 \quad 0<Q(t)\le15t, \quad Q'(0)=15=16-1.
 \tag{IR-2}
\]

Thus `0<r(n)<=15/(8n-7)^2`. The equality of `Q'(0)` and `16-1` is a **source-specific arithmetic alignment**, not a normality estimate: changing the initial seed preserves it and changes selected orbit statistics.

Define the authentic future Green tail and its original positive kernel:

\[
\begin{aligned}
 T_n&=\sum_{j\ge1}16^{-j}r(n+j)
     =\int_0^1x^{8n}R_P(x)\,dx,\\
 R_P(x)&=\frac{1-x}{(2-x^2)((x-1)^2+1)},\qquad n\ge0.
\end{aligned}\tag{IR-3}
\]

The denominator of `R_P` is at least one on `[0,1]`, so `T_n>0` is strictly decreasing and

\[
\boxed{0<T_n\le\frac1{(8n+1)(8n+2)}.}\tag{IR-4}
\]

The original BBP sum is `pi/16=sum_(j>=1)16^(-j)r(j)`. Put `alpha=s+pi/16`. The exact unwrapped source, with no imaginary random digit generator, is

\[
\boxed{U_n(s)=16^n\alpha-T_n,\quad n\ge0,}\tag{IR-5}
\]

where `T_0=pi/16` makes the n=0 formula exact. At n=1, `T_1=pi-47/15`.

### Exact computable source intervals, not an assumed transcendental oracle

For integer `n>=0,D>=1`, write `T_(n,D)=sum_(j=1)^D16^(-j)r(n+j)`. Since the positive forcing decreases,

\[
\boxed{T_{n,D}<T_n<T_{n,D}+\frac{16^{-D}}{15}r(n+D+1).}\tag{IR-6}
\]

Also the purely rational source interval

\[
\sum_{j=1}^D16^{-j}r(j)
<\frac\pi{16}
<\sum_{j=1}^D16^{-j}r(j)+16^{-D}\frac1{(8D+1)(8D+2)}
\]

follows without a decimal π input. The signed/source-relative tests use exact `Fraction` arithmetic; any sine/exponential evaluations are separately tagged numerical.

## 2. What the observer cannot know, and what still survives

A fixed coordinate translation `V_n=U_n+a` transforms the arithmetic equation into

\[
\boxed{V_{n+1}=16V_n+[r(n+1)-15a].}\tag{IR-7}
\]

Thus **all** constant translations are valid changes of coordinate if the forcing and neutral mark are transported. With the *unmodified* forcing held fixed **on the circle**, precisely the `15` rotations `a=j/15 (mod 1)` commute with the map. On the unwrapped real line, only a=0 preserves the same forcing exactly. This confirms/reuses the existing origin-gauge work, notably #255, #257, and the richer time-indexed kernel of #373; it is not claimed novel.

This is also the precise **inertial fixed-point distinction**: the unforced real law `x->16x` has the unique fixed point `0`, whereas its compact circle projection `x->16x mod 1` has **15 fixed points**, exactly `C15`. Quotienting the real source into a circle creates the degeneracy; a physical/arithmetical statement about a uniquely prepared real zero cannot be inferred from that projected quotient alone. If instead one demands a probability law invariant under **all** circle translations, the unique normalized law is Haar, *not* `delta_0`. That is an observer-ignorance prior, not evidence that the actual selected trajectory is typical of Haar.

Define the **temporal**, not cross-origin, displacement:

\[
\boxed{\Delta_{n,k}(s)=U_{n+k}(s)-U_n(s)\pmod1,\quad k\ge1.}\tag{IR-8}
\]

It is invariant under a common coordinate shift `U_n -> U_n+a`. By the original recurrence,

\[
\boxed{\Delta_{n,1}=15U_n+r(n+1)\pmod1,}\tag{IR-9}
\]

and for every positive k,

\[
 \Delta_{n,k}=(16^k-1)U_n+\sum_{j=1}^k16^{k-j}r(n+j)\pmod1.
 \tag{IR-10}
\]

**Exact finite quotient recovery:** the observer who knows the authentic forcing tape and measures the consecutive displacement computes

\[
 \boxed{B_n:=\Delta_{n,1}-r(n+1)=15U_n\pmod1.}\tag{IR-11}
\]

This is the full 15-fold quotient of the actual circle phase, not a positive probabilistic surrogate. It requires no absolute circle position or knowledge of the number π in decimal form. The independent original carry/unwrapped seed cannot be recovered from this quotient alone.

For seeds `s,t`, the complete relative lag-k integer-frequency histories from time `n0>=0` agree **iff**

\[
\boxed{(16^k-1)16^{n_0}(s-t)\in\mathbb Z.}\tag{IR-12}
\]

For k=1, `s-t=j/(15*16^n0)`. The corresponding circle orbits differ after time `n0` by a fixed rotation `j/15` (the 16-factor becomes 1 modulo 15 at each step). Thus relative observations have a real **finite identity ambiguity**; normality, being invariant under constant rotation, is identical across the ambiguous class. For k>1 there is a periodic rational rotation of period dividing k; the same normality invariance follows from the classical rational translation theorem (Wall). These are distinct claims from identifying the original unwrapped zero preparation.

**Tool-relative diagnosis:** the relative-readout closure is nonidentifying for **absolute seed identity**. It need not be nonidentifying for **normality**, which descends to this quotient. No claim that the authentic source is intrinsically FuckedField, IdealHard or undecidable is made. Insisting that the observer know its absolute origin would be an unnecessary demand for this target.

## 3. The normality theorem uses only an UNORDERED displacement histogram

**Theorem IR-13 (classical dynamics; all horizons / no statistical digit assumption).** Let `b>=2` be an integer, and let `x_n∈T=R/Z` satisfy `x_(n+1)=b*x_n+e_(n+1) mod 1`, with *deterministic* `e_n ->0` in circle distance. For every fixed integer k>=1, the empirical distributions of

`d_(n,k)=x_(n+k)-x_n mod 1`

converge weakly to Haar **if and only if** the empirical distributions of `x_n` converge weakly to Haar.

The histogram retains no chronological order. This is stronger than the trivial observation that the **ordered** differences reconstruct a trajectory up to constant translation. For the source (IR-1), `r(n)->0` meets the hypothesis. Since `U_n(0)=16^(n-1)*pi-T_n` at n>=1 and `T_n->0`, Wall's normal-number criterion gives

\[
 \boxed{\{\Delta_{n,k}(0)\}\text{ equidistributed}
\iff\{U_n(0)\}\text{ equidistributed}
\iff\pi\text{ normal in base 16}.}\tag{IR-13}
\]

**Self-contained proof independent of rational-normality citation:** Let `mu_N=N^-1 sum_(n=1)^N delta_(x_n)` and extract any weakly convergent subsequence `mu`. The original vanishing forcing implies

`(T_b)_*mu=mu`, where `T_b(x)=b*x mod 1`: compare time-shifted sums; the first/last endpoints contribute O(1/N), and the continuity defect caused by `e_n` tends to zero in Cesàro mean. For fixed k, (IR-10)'s general analogue yields `d_(n,k)=(b^k-1)x_n+o(1)`, so their empirical pushforward limit is `[m]_*mu` with `m=b^k-1>0`.

If displacement histograms tend to Haar, then `[m]_*mu=Haar`. For any Haar-null Borel set A, `[m](A)` is null because the finite covering `[m]` is Lipschitz. Moreover

`mu(A) <= mu([m]^{-1}([m](A))) = Haar([m](A))=0`.

So `mu` has an L1 density. Invariance gives `mu_hat(h)=mu_hat(b^j*h)` for all j. By the Riemann–Lebesgue lemma, the right side tends to zero as j increases for every nonzero h. Hence `mu_hat(h)=0` for all h!=0, so `mu=Haar`. As **every** weak subsequential limit is Haar, the full empirical measures converge to Haar. The converse follows from `[m]_*Haar=Haar` and the vanishing error. QED.

This theorem also follows from Wall's classical preservation of b-normality under nonzero rational multiplication, but the invariant-measure proof exposes exactly why the finite cover and vanishing forcing are load-bearing. References: D. D. Wall (1949); D. Airey & B. Mance, *Normality preserving operations for Cantor series expansions*, introduction, https://arxiv.org/abs/1407.0777. No originality is claimed for the underlying normal-number invariance.

**Hostile controls:** Without the source's approximate expanding dynamics the implication fails. Let `a_n={n*theta}` for irrational theta, `x_(2n)=0` and `x_(2n+1)=a_n`. Then unordered one-step increments consist of `a_n` and `-a_n`, and are Haar in the limit, while the position law tends to `1/2 delta_0+1/2 Haar`. Also, a nonuniform law on `[0,1/15)` maps to Haar under `[15]` but is not `T16`-invariant. Neither counterexample obeys the required asymptotically unforced source recurrence.

## 4. Uniform-in-lag original-source signed transport: the new finite quantitative object

Fix an arbitrary real seed s and write `alpha=s+pi/16`. Subtracting the exact **same Green tail** at two times gives

\[
\boxed{\Delta_{n,k}(s)
=(16^k-1)16^n\alpha+T_n-T_{n+k}\pmod1.}\tag{IR-14}
\]

Both tails are positive and decreasing, so for **all** k,N>=1,

\[
0<\sum_{n=1}^N(T_n-T_{n+k})
\le\sum_{n=1}^{\min(k,N)}T_n
\le \sum_{n=1}^\infty T_n=:\mathcal M_{\rm BBP}<\infty.
\tag{IR-15}
\]

For an integer h!=0, write `e(x)=exp(2 pi i x)`. The 2π-Lipschitz bound on unit phases proves the **seed-uniform, lag-uniform finite certificate**

\[
\boxed{\left|
\frac1N\sum_{n=1}^N e(h\Delta_{n,k}(s))
-\frac1N\sum_{n=1}^N e(h(16^k-1)16^n\alpha)
\right|\le\frac{2\pi|h|}{N}\mathcal M_{\rm BBP}.}\tag{IR-16}
\]

The crucial difference from the naive source-lag bound is that **the growing factor `16^k` is part of the leading oscillator, not the error**. The full original-source error telescopes and costs a finite *single* memory constant. Even `k=k(N)` may vary arbitrarily in this *comparison inequality*; that does **not** establish uniform Weyl decay of the leading phase, and the fixed-k normality theorem has different quantifiers.

There is a purely rational global fallback:

\[
\boxed{\mathcal M_{\rm BBP}<\sum_{n\ge1}(8n+1)^{-2}
<\frac1{81}+\int_1^\infty(8x+1)^{-2}dx
=\frac{17}{648}.}\tag{IR-17}
\]

A numerical preview of the **source-certified bound**, not a measured Fourier saving, is

`2*pi*M_BBP/N = (0.10239705671231809405...)/N` for h=1.

## 5. The complete finite memory constant is a Gamma/digamma + two-quadratic invariant

**Theorem IR-18 (exact closed form for the original source):**

\[
\boxed{\begin{aligned}
\mathcal M_{\rm BBP}
&=\sum_{n=1}^\infty T_n\\
&=\int_0^1\frac{x^8\,dx}
{(1+x+x^2+\cdots+x^7)(2-x^2)((x-1)^2+1)}\\
&=-\frac\pi{20}+\frac{\sqrt2\pi}{48}
+\frac{\log2}{24}
+\frac{\sqrt2}{24}\log(1+\sqrt2)\\
&=0.01629699773382656556491836321059\ldots.
\end{aligned}}\tag{IR-18}
\]

**Source-only derivation.** Set `S=sum_(j>=2)r(j)`. Exchanging strictly positive source tails with the `16^-j` geometric weights gives

\[
15\mathcal M_{\rm BBP}=S-T_1,\qquad T_1=\pi-47/15.
\]

The original four signed poles and the standard convergent digamma-difference identity yield

\[
 S=-\frac18\bigl(4\psi(9/8)-2\psi(3/2)-\psi(13/8)-\psi(7/4)\bigr).
\tag{IR-19}
\]

Equivalently, `S` is minus one-eighth the `u=0` logarithmic derivative of

\[
 \frac{\Gamma(u+9/8)^4}
 {\Gamma(u+3/2)^2\Gamma(u+13/8)\Gamma(u+7/4)}.
\]

Using the classical digamma reflection/duplication formulas at these eighth-fraction arguments gives

\[
S=-\frac{47}{15}+\frac\pi4+\frac{5\sqrt2\pi}{16}
 +\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2),
\]

hence IR-18. The coefficient sum `4-2-1-1=0` **cancels Euler–Mascheroni gamma exactly** in the digamma expansion. The `sqrt(2)`, Gaussian pair `1 ± i`, and `log(1+sqrt(2))` arise from the **authentic original BBP quadratic factors**; no source connection to the separate 45-degree primitive lattice operator `D` has been proved just by this matching analytic geometry.

A genuinely source-derived **golden continuation** also exists: for `0<=z<=1`,

\[
\mathcal M(z)=\sum_{n\ge1}z^nT_n
=\int_0^1\frac{z x^8}{1-zx^8}R_P(x)\,dx.
\tag{IR-20}
\]

Choosing `z=lambda^2=phi^-2` from the inherited original two-stage Oily fixed point yields a positive member `M(lambda²)≈0.003650228020993477...`; `M(1)` is the exact universal lag budget IR-18. The Oily selected value is **marked/grammar dependent**, not a physically or arithmetically canonical gamma/Weil selector.

The same direct integral as IR-18 provides a derivation independent of digamma summation: sum `x^(8n)` first under Tonelli, cancel `1-x^8=(1-x)(1+x+...+x^7)`, then integrate the positive rational kernel. A separate 210-digit numerical oracle tests both methods; its numbers are not the proof.

## 6. Reuse the Farey×Gamma/Eisenstein observer with NO absolute position

PR #375 defined the positive primitive Eisenstein horizontal Fourier coefficients at fixed y>0:

\[
 a_h(y)=\frac{\pi(1+2\pi hy)e^{-2\pi hy}}{2\zeta(4)y}\,\sigma_{-3}(h)>0,
 \quad h\ge1.
\]

Define the **time-relative modular energy** from the actual displacements, without absolute phase input:

\[
\mathcal E^{\mathrm{rel},k}_N(y)
=\int_0^1\left|\frac1N\sum_{n=1}^N
 E(a+\Delta_{n,k}+iy,2)
 -\int_0^1 E(a+x+iy,2)\,dx\right|^2 da.
\]

Parseval gives the exact, positive observation formula

\[
\boxed{\mathcal E^{\mathrm{rel},k}_N(y)
=2\sum_{h\ge1}a_h(y)^2\left|
\frac1N\sum_{n=1}^N e(h\Delta_{n,k})\right|^2.}\tag{IR-21}
\]

The `a_h(y)` are exponentially decaying and strictly positive. Therefore, **for each fixed k and fixed y>0**, IR-13 + Weyl prove the source-authentic equivalence

\[
\boxed{\mathcal E^{\mathrm{rel},k}_N(y)\longrightarrow0
\iff\pi\text{ is normal in base }16.}\tag{IR-22}
\]

The source-debiased relative input `B_n=Delta_(n,1)-r(n+1)` gives exactly the analogous Eisenstein energy for the **15-fold quotient** `[15]U_n`, with no approximation. The raw relative energy and the debiased energy differ by at most

\[
\frac{8\pi}{N}\left(\sum_{n=1}^N r(n+1)\right)
\left(\sum_{h\ge1}h a_h(y)^2\right),
\tag{IR-23}
\]

using the same 2π phase Lipschitz bound and `||A|²-|B|²|<=2|A-B|`.

More strongly, let `E_lac,N,k` be the same positive Fourier series evaluated on the pure lacunary points `(16^k-1)16^n alpha`. The uniform-in-k Green theorem gives

\[
\boxed{|\mathcal E^{\mathrm{rel},k}_N(y)-\mathcal E^{\mathrm{lac},k}_N(y)|
\le\frac{8\pi\mathcal M_{\rm BBP}}{N}\sum_{h\ge1}h a_h(y)^2.}\tag{IR-24}
\]

The final sum is finite because of exponential `e^(-4pi h y)` decay; it has an explicit elementary rational-geometric upper bound after using `sigma_-3(h)<5/4`. This quantitative comparison is **representation transport only**. Neither energy is independently proved to vanish for the true `alpha=pi/16`.

### Relation to the inherited signed mixed-lag theorem (no theorem laundering)

The authenticated SUCC research in PR #319 has an unconditional but only **logarithmic** selected absolute Fourier loss for mixed temporal lags. Specializing its stated domain to one difference `(E^k-I)U_n` and residue period p=1, for fixed `h!=0`, `0<delta<1`, and `k+1<=N^delta`, yields the inherited comparison

\[
\left|\sum_{n=1}^N e(h\Delta_{n,k}(0))\right|
\le N-\frac{1-\delta}{14}\log_8N+O_h(1).
\]

Our new IR-16 then transfers this *inherited* logarithmic bound to the pure lacunary carrier frequency `h(16^k-1)` at **a lag-uniform additional cost at most** `2*pi*|h|*M_BBP`. This is a genuine source-specific **existing** signed-loss bound, not a proof of sublinear `o(N)` and not claimed new scholarly progress. Quantifiers for k growing and h fixed must not be silently interchanged.

## 7. Provenance, hostile controls and categorical diagnosis

**Absolute seed FuckedField / toolkit nonidentification:** Readouts of all temporal relative differences cannot distinguish the exact seed `0` from `1/15` on the circle with original forcing, and, for observations beginning at n=1, cannot distinguish `0` from `1/240`. Original unwrapped states and preparation costs *do* distinguish them. This is a calibrated readout-kernel statement, not a claim that no stronger instrument can distinguish any such states.

**Normality descends:** every seed ambiguity in the full relative-history kernel changes `alpha=s+pi/16` by a rational number, and rational translation preserves base-16 normality. The quotient's inability to identify an *absolute* seed therefore does not itself obstruct the *truth value* of normality. One can build a test complete for the latter while remaining unable to identify the former. Thus the genuine FuckedField statement has target **seed identity**, not normality.

**The coherent same-forcing counterseed** `s=-pi/16` gives `alpha=0`, `U_n=-T_n`, and

\[
 \Delta_{n,k}=T_n-T_{n+k}\to0.
\]

Its relative Eisenstein energy tends to the strictly positive Dirac energy `2sum_(h>=1)a_h(y)^2`. This is the necessary hostile control: it shares *every* original positive packet/Gamma/totient scalar but is nonnormal.

**Source-only positive field and inertial preparation are insufficient.** The concrete inherited PR #373 mutant

\[
 r_d(n)=\frac{16}{(8n+d-7)^2}-\frac1{(8n+d+1)^2},
 \qquad U_n^{(d)}=\frac{16^n}{(d+1)^2}-\frac1{(8n+d+1)^2}
\]

has `U_0=0`, a positive Laplace carrier with `Q_d(t)=t(16e^(-dt)-e^(-(d+8)t))`, and the **same** neutral first jet `Q_d'(0)=15`. At `d=3`, `16^n/(d+1)^2=16^(n-1)` is integral at all positive times; the circle trajectory and every temporal lag converge to zero, so the selected source is **not normal**. This exact-rational counterexample, explicitly marked *different forcing*, refutes any claim that inertial zero plus `15=Q'(0)=16-1` already forces signed cancellation. The original four-pole forcing remains a separate arithmetic obligation; our theorem derives no new signed Weyl cancellation merely from the neutral marked state. This new quotient criterion is a **pathway/probe**, not a `phi`-resolved proof. The source-to-observation map is explicit; the source-to-asymptotic-cancellation map remains **UNVERIFIED**.

**Different observer**: Previous origin twirls in PRs #255/#257 compare *different initial origins* and may cancel the π phase. Here we compare **different times of the very same selected source orbit**; its phase survives as `(16^k-1)16^n alpha`. Conflating these two kinds of "relative" would be a source-map error.

## 8. Executable authority and next gate

Standalone exact implementation: [`relative_observer.py`](relative_observer.py). Regression tests: [`tests/test_inertial_relative_observer.py`](../../../tests/test_inertial_relative_observer.py). Independent 210-digit polynomial/Gamma/Eisenstein oracle: [`independent_oracle.py`](independent_oracle.py). Raw logs and environment description: [`VALIDATION.md`](VALIDATION.md). Local scoped test counts refer only to the staged additive parent archive, not the native full repository.

**Next mathematical target:** prove an original-four-pole, zero-seed-sensitive signed inequality for *relative* Fourier coefficients or its Eisenstein energy that rejects coherent `s=-pi/16` and source-mutant controls. The present complete criterion is still equivalent to normality; it does not weaken the analytic difficulty by itself. If a proposed inequality holds for *every* bounded sequence or is only an origin/Haar average, it is not a normality advance.
