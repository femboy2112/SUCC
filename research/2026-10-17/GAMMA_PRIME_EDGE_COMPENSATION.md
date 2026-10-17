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

## 8. SC-06 — the genuine Gamma term is a nonlocal Markov/Dirichlet jump energy

**Theorem [CLASSICAL distribution algebra; applied to the authenticated original Gamma rungs].** For zero-extended `F=Vu in H_0^1(I)`, the **exact** Gamma quadratic energy in SC-5 admits a positive double-integral representation

\[
\boxed{Q_\Gamma(F')=\frac12\iint_{\mathbb R^2}
 J(|x-y|)\,|F(x)-F(y)|^2\,dx\,dy,\quad
 J(r)=\sum_{j\ge0}e^{-(4j+1)r/2}=\frac{e^{-r/2}}{1-e^{-2r}}.}\tag{SC-18}
\]

This equality is **not** the full signed Weil form: SC-1 additionally carries original negative contact, polar channels and genuine prime currents. Proof: for each genuine OU rung, `∫_R e^{-(4j+1)|x-y|/2}dy=4/(4j+1)`. Expand the square `|F(x)-F(y)|²`, divide by two, and recover precisely the positive-mode SC-5. Every summand is nonnegative, so monotone convergence allows summing the full tower. For `F in H¹_0` the original operator is finite, and no fictitious independent gamma bath was introduced. The jump kernel obeys `J(r)~1/(2r)` near zero; this is the **logarithmic spectral resistance** behind SC-10 and the Carleman source-range obstruction already appearing in SUCC's earlier papers.

**Important observer-relative conclusion:** if `F_e,F_b` have disjoint supports, the Gamma quadratic on `F_e+F_b` has a *negative* mixed term

\[
Q_\Gamma(F_e'+F_b')-Q_\Gamma(F_e')-Q_\Gamma(F_b')
=-2\operatorname{Re}\iint_{E\times B}F_e(x)\overline{F_b(y)}J(|x-y|)dxdy.\tag{SC-19}
\]

Thus positive Dirichlet self-energy does **not** mean positive cross energy between two independently lawful E measurements. This is a genuine analytic instance of SUCC's collective-observer distinction between marginal positivity and signed relational coupling.

## 9. SC-07 — touching interfaces have a non-vanishing Carleman coupling

Let the left edge and central bulk support intervals touch at an endpoint `x0`; each has width `delta>0`. For **any fixed** polynomial-moment cut `m`, take the nonzero exact edge profile `phi_m(z)=d^m/dz^m[z^(m+1)(1-z)^(m+1)]` and define normalized primitive packets

\[
F_e(x_0-\delta s)=\delta^{-1/2}\varphi_m(s)/\|\varphi_m\|_2,
\quad F_b(x_0+\delta t)=\delta^{-1/2}\varphi_m(t)/\|\varphi_m\|_2
\qquad (0\le s,t\le1).\tag{SC-20}
\]

They vanish at strip endpoints and extend by zero to `H¹_0`, so their derivatives are lawful mean-zero input functions. Integration by parts makes **each** derivative orthogonal to polynomial modes through degree `m`: the individual translated primitive profiles annihilate all moments through degree `m−1`. In particular they lie in `Q4` when `m=4`; this is not a counterexample living only outside SUCC's actual high sector.

The normalized unsigned Gamma *bilinear* edge/bulk interaction satisfies

\[
 \lim_{\delta\downarrow0}\iint_{E\times B}F_e(x)F_b(y)J(|x-y|)dxdy
=\frac1{2\|\varphi_m\|_2^2}\int_0^1\!\int_0^1
 \frac{\varphi_m(s)\varphi_m(t)}{s+t}\,ds\,dt=:\mathcal C_m>0.\tag{SC-21}
\]

**Proof.** With `r=delta(s+t)`, `delta J(delta(s+t)) →1/[2(s+t)]`. The rational upper `J(r)<=1+1/(2r)` dominates the rescaled integrand because `phi_m` vanishes at each boundary and is polynomial. The Carleman denominator has the **positive Laplace factorization** `1/(s+t)=∫_0^∞e^{-λs}e^{-λt}dλ`. Hence the double integral is `∫_0^∞|∫_0^1 e^{-λt}phi_m(t)dt|²dλ`, strictly positive for nonzero phi. More constructively, m integrations by parts give `∫e^{-λt}phi_m(t)dt=λ^m∫e^{-λt}t^(m+1)(1-t)^(m+1)dt`; on λ∈[1,2] this is at least `e^-2 B(m+2,m+2)`. Since `e<3`, the exact rational lower is

\[
\boxed{\mathcal C_m>
\frac{B(m+2,m+2)^2}{162\|\varphi_m\|_2^2}>0,\quad
\mathcal C_4>\frac{13}{90531302400}.}\tag{SC-22}
\]

**This refutes a crucial shortcut:** the gamma cross between touching observer windows is **not** `o(1)` in the `K`-relative metric merely because the windows' lengths shrink. Even imposing *any fixed number of vanishing polynomial moments* does not make it so. SC-04's positive-gap hypothesis genuinely does useful work. But the full Gamma **diagonal** edge energy grows logarithmically (SC-10), so an order-one mixed Carleman coupling does *not* prevent conditional positivity at sufficiently fine resolution.

### SC-08 — conditional no-gap source gluing, with an explicit enormous finite certificate

For the *same source* (SC-1), let `F_e` have the two authentic edge supports and `F_b` have a central support `B` of length `beta` whose closure **may meet** the edge boundaries. Both belong to `H_0^1(I)` and their supports are disjoint. Assume, as a **separate original-source theorem rather than a program label**, that `Q_G(F_b') >= c_B ||F_b||²` for some `c_B>0` throughout the relevant bulk test class. The Gamma cross kernel is `J(s+t)<=1+1/[2(s+t)]`. The classical Carleman integral operator `C f(s)=∫_0^∞ f(t)/(s+t)dt` has `L²` norm at most π by the exact Schur weight `s^(-1/2)`:

\[
 \int_0^\infty\frac{t^{-1/2}}{s+t}dt
 =\frac\pi{\sqrt s}.\tag{SC-23}
\]

There are two edge/bulk interfaces. Each contributes at most `(π/2+sqrt(delta beta)) ||F_{e,i}|| ||F_b||`; Cauchy over edges yields total Gamma coefficient at most `sqrt2(π/2+sqrt(delta beta))`. The two genuine pole channels add at most `2sqrt(2 delta beta)cosh(a)` to that cross coefficient. Contact is diagonal on disjoint primitive supports, and the genuine n=2 hinge depends exclusively on the edge pair (so has zero bulk cross). Using source `a<1/2`, `π/2<11/7`, `cosh(a)<4/3`, and the exact outward rational upper on `sqrt(delta beta)`, define

\[
\eta_0^2\le 2\left(\frac{11}7+\frac{11}3\sqrt{\delta\beta}\right)^2.\tag{SC-24}
\]

Then

\[
Q_G(F_e'+F_b')\ge
c_E(\delta)\|F_e\|²+c_B\|F_b\|²
-2\eta_0\|F_e\|\|F_b\|,\tag{SC-25}
\]

where **every source channel is preserved** and the edge margin can be amplified using SC-10:

\[
M=\left\lfloor\frac1{16\delta}\right\rfloor,
\qquad c_E(\delta)\ge H_M-\frac18-\frac{47}8-\frac\delta4.
\]

This diverges logarithmically as `delta→0`. The exact source-conditional **no-gap** sufficient positivity condition is

\[
\boxed{c_E(\delta)c_B>\eta_0^2.}\tag{SC-26}
\]

It does not follow that the required `c_B` is known or that an arbitrary source test can be split into two `H¹_0` packets which vanish at their shared endpoint. Any general partition of unity with overlapping supports needs its own rigorously controlled **nonlocal IMS** error. The no-gap theorem is conditional for a restricted direct-sum support grammar, not a claim of all-radius Weil positivity.

**An explicit inverse-Ramsey-style proof compression.** If `M>=2^k`, harmonic grouping proves `H_M>=1+k/2`: each dyadic group contributes ≥1/2. Hence `c_E(delta)>=k/2−5−delta/4` with **no need to enumerate** the M individual OU modes. At `delta=2^-36`, `M=2^32=4,294,967,296`; the exact rational certificate gives `c_E>10.9999999999` using only `k=32`. For a *hypothetical separately certified authentic bulk* `c_B=1/2` on `beta=1/4`, the Carleman/polar cross satisfies the exact rational upper `eta_0²<4.94`. Thus the conditional test `(edge margin)*c_B>eta_0²` succeeds **without simulating over four billion Gamma rungs**. The large budget is a theorem-derived witness to the observer's resource-depth bottleneck, not a physical clock, a source-proof of the bulk margin, or an RH result.

**This changes the next proof target:** seek a source-attested bulk margin at the same irrational radius and a nonlocal IMS gluing estimate for general primitives with nonzero interface traces. Do not attempt to infer a global theorem from two positive charts without controlling their actual mixed Carleman kernel.
