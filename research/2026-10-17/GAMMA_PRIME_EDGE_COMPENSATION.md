# OPERATION SOURCE-CIRCUIT — Gamma compensates the first prime chiral edge

**Research checkpoint:** 2026-10-17. Parent SUCC Academic Main III merge `610efacf02556e1c5922bc5d4e87d0087f19b446` (PR #152). Draft research branch `research/prime-hinge-chiral-edge-relative-jump-2026-10-17`. **RH PROVED: NO.** The sign of the true four-low first-window short `S_4=A_4-R_4` is **OPEN**. No nontrivial-zero location was consulted or supplied as a construction input.

**Original-source gate:** genuine completed Suzuki/Weil screw kernel in `observational_succ/source_weil_hierarchy.py`, frozen Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256 `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`, source origin `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. This is the exact source used by SUCC's four-low Suzuki/Weil certificates, *not* an auxiliary positive covariance or a Gaussian-only source. Primary mathematical reference: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, §§2,8, particularly the signed kernel and derivative-coordinate/inverse-Neumann realization. See `AGENTS.md` and Academic Main III's corrected PDQ claim supplement. No archival source is rewritten.

**Results:** source-dependent analytic-paper theorem with a standalone exact rational constants/harmonic certificate; pure synthetic chiral controls; an explicit *conditional* original-source interior/edge gluing lemma; exact Gamma–prime endpoint exponent identity. Academic novelty not researched or asserted. Implementation does **not** certify all of `G_a`, `S_4`, RH, or any physical apparatus.

## 1. Full signed source and exact two-edge algebra

Let `b=log 2`, `w=log 2 / sqrt 2`, and `C=gamma_Euler+pi/2+3log2+log pi`. For the first active-prime radius `a=(b+delta)/2` with `0<delta<=1/32`, the frozen original source has **only n=2 active** on `|r|<=2a=b+delta<log3`. Its continuous signed kernel (for this source interval) is

\[
 g(r)=-4(e^{r/2}+e^{-r/2}-2)+\frac C2 |r|
       +w(|r|-b)_+-\sum_{j=0}^\infty\frac4{d_j^2}(1-e^{-d_j|r|/2}),
 \qquad d_j=4j+1.\tag{SC-1}
\]

The genuine source has **both poles**, one real Gamma tower, contact `C`, and the real prime-power coefficient `w`; no fake independent impulse at composite 6. At these radii no later genuine prime powers are active. Work on `H=L²_0(-a,a;C)`. For `u in H`, put `F=Vu`, `F(x)=int_{-a}^x u(t)dt`, so `F in H¹_0(-a,a)` and `\langle Ku,u\rangle=||F||²`, `K=V*V=(-Delta_N)^-1` in the standard SUCC derivative chart.

The actual support strips are

\[
 E_L=(-a,a-b)=(-a,-a+\delta),\quad
 E_R=(b-a,a)=(a-\delta,a).\tag{SC-2}
\]

The strips are disjoint since `delta<b`. Define `L(t)=F(-a+t)` and `R(t)=F(b-a+t)` on `(0,delta)`. The isolated genuine prime kernel has exact energy

\[
 Q_{\rm prime}(u)=-2w\operatorname{Re}\int_0^\delta L(t)\overline{R(t)}dt,\tag{SC-3}
\]

whether or not `F` also occupies the middle. It follows `Q_prime>=-w(||L||²+||R||²)`. If `F` vanishes outside `E_L union E_R`, this is `>=-w ||F||²`, with sharp equality on the symmetric chiral state `L=R`.

The prior edge packet proves the sharp `K`-relative chirality `±w` for any finite polynomial moment-high subspace, while the isolated hinge tends to zero in ordinary Hilbert–Schmidt norm `w² delta⁴/6`. **This is a single signed channel only.** The theorem below uses the *complete original source*.

## 2. THEOREM SC-01 — first-prime Gamma–edge compensation

**Theorem [source-conditional analytic-paper proof, exact rational constants].** Let `b,w,C,g` be precisely (SC-1), with `0<delta<=1/32`, `a=(b+delta)/2`. For every complex `u in L²_0(-a,a)` whose primitive `F=Vu` is supported a.e. in `E_L union E_R`, the completed signed operator satisfies

\[
\boxed{\langle G_a u,u\rangle > \frac{11}{128}\,||F||_2^2
=\frac{11}{128}\,\langle K u,u\rangle\quad(u\ne0).}\tag{SC-4}
\]

This is uniform in the just-opened prime-window width, requires **no** moment condition beyond mean zero, and consequently also applies to the localized part of *any* fixed Legendre high-moment subspace. It is NOT a theorem of positivity for arbitrary `u in H` or `Q_4H` on that entire interval. At `a=1/2`, `delta=1-log2` is larger than `1/32`, and SC-4 **does not apply**; Academic Main III supplies different high-space coercivity there.

**Proof, authentic Gamma.** On mean-zero inputs, the j-th *original* Gamma rung is the positive OU operator `4/d_j² exp(-d_j|x-y|/2)`. Two weak integrations by parts, justified first on `C_c^infty` and then by `H_0^1` density, give

\[
 Q_{\Gamma,j}(u)
 =\frac4{d_j}\|F\|²-
 \iint_{I²}F(x)\overline{F(y)}e^{-d_j|x-y|/2}\,dx\,dy.\tag{SC-5}
\]

All these original rungs are nonnegative, by the positive Fourier multiplier `d_j/(xi²+d_j²/4)` of the exponential kernel. Let `ell=|supp F|<=2delta`. Since `0<exp(-alpha|x-y|)<=1`, Cauchy–Schwarz implies

\[
 |\langle F,e^{-d_j|\cdot|/2}*F\rangle|
 \le \|F\|_1^2\le \ell\|F\|_2^2\le 2\delta\|F\|_2^2.\tag{SC-6}
\]

Discard the nonnegative remainder of the original Gamma tower after sixteen rungs; then

\[
 Q_\Gamma(u)\ge
 \left(\sum_{j=0}^{15}\frac4{4j+1}-32\delta\right)\|F\|².\tag{SC-7}
\]

The exact Fraction sum is `168623511779891008/24142663793423175`, and exact cross-multiplication certifies it is **strictly larger than `223/32`**. Notice `4/(4*15+1)=4/61>2delta` across the claimed range, so even the first sixteen separate finite lower bounds are positive.

**Proof, authentic poles.** The *two* original polar channels are

\[
 Q_{\rm pole}(u)
 =-8|\langle u,\cosh(x/2)\rangle|²
   +8|\langle u,\sinh(x/2)\rangle|².
\]

Integration by parts with `F(±a)=0` makes this

\[
 Q_{\rm pole}(u)=
 2\bigl|\int_I F(x)\cosh(x/2)dx\bigr|²
 -2\bigl|\int_I F(x)\sinh(x/2)dx\bigr|²
 \ge -2\ell\sinh²(a/2)\|F\|².\tag{SC-8}
\]

Here the actual `b<7/10`, so `(b+delta)/4<1/5`. For `0<=x<=1/5`, use `sinh x <= x/(1-x²) <=5/24<1/4`, from its positive Taylor series. Therefore SC-8 is `>=-ell/8 ||F||²>=-delta/4 ||F||²`.

**Proof, contact and prime.** The authentic `C|r|/2` term contributes exactly `-C||F||²`. By SC-3 the *true* prime-2 hinge contributes at least `-w||F||²`. A fully rational standalone computation, using Machin arctangents for pi, positive atanh log series, the `n=16` Euler–Maclaurin enclosure for Euler's constant and integer square-root bounds, proves **`C+w<47/8`**. The exact original-source runtime gate independently checks the same strict inequality using the frozen `contact_iv`, `log2_iv`, `sqrt_inverse(2)` and certifies that `log2+delta<log3`.

Finally, assemble all four original source channels in the `K` norm:

\[
 \frac{Q_{G_a}(u)}{\|F\|²}
 >\frac{223}{32}-32\delta-\frac{47}{8}-\frac\delta4
 \ge\frac{223}{32}-1-\frac{47}{8}-\frac1{128}
 =\boxed{\frac{11}{128}}.\tag{SC-9}
\]

This proves SC-4 without reading zeta zeros, creating any new source, completing a Gaussian *alone*, replacing a signed form by a positive Gram, or invoking a bounded zero-shift inverse. ∎

**Boundary:** This is not a claim that prime `2` creates a universal positive *global* Weil mode. The localization is an essential premise, just as a finite observer can distinguish a boundary packet without observing all interior source-couplings.

## 3. SC-02 — logarithmic Gamma energy growth with localization

For **any** finite-measure support of `F=Vu` of length `0<ell<=1/8` (not necessarily at a prime threshold), choose `M=floor(1/(8ell)) >=1`. By SC-5–SC-6,

\[
 Q_\Gamma(u)\ge
 \Bigl(\sum_{j=0}^{M-1}\frac4{4j+1}-M\ell\Bigr)\|F\|²
 \ge\left(H_M-\frac18\right)\|F\|²
 \ge\left(\log(M+1)-\frac18\right)\|F\|².\tag{SC-10}
\]

Here `H_M=sum(1/j)` is the ordinary harmonic number; the inequalities are elementary because `4/(4j+1) >1/(j+1)` and `Mell<=1/8`. This proves a genuine **logarithmic source-derived energy penalty** for primitive states localized on increasingly small sets, independently of how many moment constraints are imposed. It is not a whole-space coercivity inequality and does not license Fourier multipliers of the prime impulse to be treated as finite-window eigenvalues.

For the edge-primitive packets, ordinary gradient cost also diverges at least quadratically: each strip has length `delta`, and Dirichlet Poincare implies

\[
 \|u\|²=\|F'\|²\ge\frac{\pi²}{\delta²}\|F\|²
 >\frac{9}{\delta²}\|F\|².\tag{SC-11}
\]

The explicit original edge-packet four-moment chiral test has `||u||²/||F||²=234/delta²`. Unlike the `K`-relative prime-current norm, this ordinary resolution demand diverges as the observer's edge support shrinks.

## 4. SC-03 — Gamma–prime boundary phase locking (algebraic, not positivity)

Let `n=p^k` be a **genuine** prime power, `j>=0` an original Gamma index, `b_n=log n`, `d_j=4j+1` and `alpha_j=d_j/2=2j+1/2`. Then

\[
 \boxed{e^{-\alpha_j b_n}=n^{-2j-1/2}.}\tag{SC-12}
\]

The half-density is exactly the one entering the genuine arithmetic prime coefficient `w_n=Lambda(n)/sqrt(n)`. **Only where an actually derived source calculation multiplies these factors**, their product simplifies to

\[
 \boxed{w_n\,e^{-\alpha_j b_n}=\frac{\Lambda(n)}{n^{2j+1}}.}\tag{SC-13}
\]

This is an exact finite/Archimedean *source-normalization identity*: exponential boundary values at genuine prime-clock hinge endpoints become algebraic rational powers times `sqrt(n)` rather than require floating transcendental evaluations of `exp(-alpha log n)`. It is **not** a claim that separate additive Gamma and Euler source channels should be multiplied in the original Weil kernel. In particular `n=6` is rejected as a fake independent prime-place impulse. The new code tests `n=2,3,4,5,7,8` and other genuine prime powers, with the frozen authentic tape as an optional additional gate. The technical opportunity is in source-correct **cross-term and endpoint** integrators: keep the actual Gamma and prime contributions separate, but simplify their endpoint coefficients algebraically before outward rounding.

## 5. SC-04 — conditional buffered gluing and why full positivity remains harder

Let `Fe` be a primitive supported on the two narrow edge strips `E` (length `ell=2delta`). Let `Fb` be a central primitive with disjoint support `B` (length `beta`) at distance `>=g>0` from `E`, and suppose a *separately proved authentic source* bulk inequality holds:

\[
 Q_G(F_b')\ge c_B\|F_b\|²,\qquad c_B\ge0.\tag{SC-14}
\]

This is a **hypothesis**; the current code cannot manufacture it by combining observer labels or appealing to SC-4. Because edge and bulk supports are disjoint, the contact term has no mixed contribution and the prime-2 cross term vanishes (SC-3 reads edges only). The original Gamma primitive cross-kernel is an absolutely convergent series at the positive gap:

\[
 K_\Gamma(r)=\sum_{j\ge0} e^{-(4j+1)r/2}
 =\frac{e^{-r/2}}{1-e^{-2r}},\qquad r\ge g>0.\tag{SC-15}
\]

For `r>=g`, the elementary bound `e^{2g}>=1+2g` gives

\[
 0<K_\Gamma(r)\le 1+\frac1{2g}.
\]

The two polar cross terms contribute at most `4sqrt(ell beta)cosh(a)||Fe||||Fb||` in absolute value. Since `a<1/2`, `cosh(a)<=1/(1-a²)<=4/3`. Thus the *complete original source* satisfies the rigorous conditional two-chart bracket

\[
 \boxed{Q_G(F_e'+F_b')\ge
 \frac{11}{128}\|F_e\|²+c_B\|F_b\|²-2\eta\|F_e\|\|F_b\|,}\tag{SC-16}
\]

with

\[
 \boxed{\eta²\le 2\delta\beta\left(\frac{11}{3}+\frac1{2g}\right)^2.}\tag{SC-17}
\]

An exact algebraic *sufficient* positivity gate is therefore `((11/128)c_B > eta²)`. The implementation reports this condition without asserting `c_B` is source-authenticated. If `g` tends to zero, the gamma cross estimate diverges, explaining why a simple source-norm continuity argument does not glue touching boundaries. As `delta->0`, choosing an admissible gap `g=delta^alpha` with `0<alpha<1/2` gives `eta²=O(delta^(1-2alpha))`, so conditional gluing becomes possible against **any genuinely certified fixed** positive bulk margin. But this neither certifies all possible decompositions (`Fe+Fb` may omit the buffer) nor provides the required bulk margin. A toy matrix `[[1,2],[2,1]]` with positive diagonals but negative mixed energy `-2` remains a mandatory no-ghost control.

**The first-window obstacle survives:** the current `a=1/2` has `delta=1-log2~0.30685`, much larger than `1/32`, and source values can mix boundary and interior without a positive gap. We must not infer `S4>=0` by extrapolation.

## 6. Direct insight into existing PDQ / CertifiedTrial bottleneck

`CertifiedDerivativeEnergyTrial` in Academic Main III is dominated by the conservative midpoint–Lipschitz radius (~18× finite derivative energy at one source configuration). The pinned original source's finite-Gamma derivative on a polynomial response is **piecewise exponential-polynomial**, with only two prime-2 breakpoints `x=±(a-b)` at `a=1/2`. SC-12 shows exactly why an analytic interval integrator can reduce rounding debt: for each Gamma rung, its boundary endpoint exponential involves `exp(-alpha_j log2)=2^(-2j-1/2)` with authenticated `sqrt2`, not an independently approximated irrational exponent. Integrate the exact derivative Gram over the three source intervals, preserve both poles/contact/prime2, then add the existing source-proven *differentiated* Gamma tail. The next proof target is a U-dependent Loewner upper for `||Pi_{P<=3}^perp (Gv)'||²` with correct boundary terms and source-calibrated error, not the older false claim that differentiating an L² projection contracts derivatives.

**Negative-control requirements for any future full evaluator:** `Q_4h` versus `h'` quotient noncommutation; wrong/outside `log2` wavefront; false atom n=6; wrong contact; dropped polar channel; half-density mutation; excessive Gamma-tail cancellation; negative interval Gram eigenvalue smuggled as true S4 negative sign; a large optimized response whose rapidly growing coefficient norm consumes the entire derivative-error budget; making a positive-looking local chart and assuming positive global mixed coupling.

## 7. Explicit theorem and test authority

| Claim | Status | What would invalidate promotion |
|---|---|---|
| SC-01 full signed original-source positivity on the first-edge primitive-support subspace | **PAPER DERIVED; exact rational constants/harmonic certificate; original-source SHA gate** | An error in `g(r)` coefficients/real Gamma rung sign, pole/contact sign, incorrect prime support, invalid OU positivity or an unrecognized active prime |
| SC-02 Gamma grows logarithmically under support narrowing; edge Poincare cost | **CLASSICAL analytic + exact rational finite sum** | A sampled or modified Gamma source substituted for the genuine OU tower, or invalid primitive domain |
| SC-03 source clock half-density algebra at `log n` | **CLASSICAL algebra / exact integer tests** | Composite 6 introduced as independent prime impulse; illicit source product inferred |
| SC-04 buffered two-chart positivity sufficient criterion | **CONDITIONAL PAPER PROOF** | Missing separation gap/central support, negative or unproved bulk margin, wrong joint source, hidden relative phase, or omitting gamma/polar cross coupling |
| Source gate at irrational a | **Exact interval inequality under frozen source formula** | Treating a rounded rational approximation to `a` as the actual wavefront |
| Original `S4` sign/all-radii Weil positivity/RH | **OPEN** | Must supply actual *unmodified complete-source* sign and all-radius argument |

Source independent exact arithmetic is in `gamma_edge_compensation.rational_source_constant_control`, without importing any SUCC source. That proves the necessary rational constants assuming the classical Taylor/Euler–Maclaurin remainder bounds and exact defining constants. A separate **original-source** gate checks those inequalities against the byte-pinned SUCC source (`source_authenticated_compensation`), without fitting a model or importing zeros. It does not constitute an independent formal proof of every imported analytic theorem.

### Reproduction

```bash
python -m unittest discover -s tests -p 'test_prime_hinge_chiral_edge.py' -v
python -m unittest discover -s tests -p 'test_gamma_edge_compensation.py' -v
python -m unittest discover -s tests -p 'test_gamma_prime_phase_lock.py' -v
python scripts/prime_hinge_chiral_edge_probe.py --source --verify
python scripts/gamma_prime_compensation_probe.py --source --verify
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The full repository CI must be checked independently after the exact pushed head. Synthetic standalone tests skip authentic import integrations only when required modules are absent; **a full installed SUCC checkout MUST execute and pass them**. Source snapshots, exact rational packets and negative mutation controls should be retained. Avoid merging or publishing without explicit maintainer review.

**Research verdict:** We have now established one rigorous original-source **local compensation mechanism** and one explicitly conditional **gluing theorem**, together with the exact gamma/prime endpoint phase-lock algebra. The genuine sign of `S4` and the all-support positivity criterion remain open. An operator-valued global Gamma-versus-boundary estimate without artificial gaps would be a much more decisive next lemma.
