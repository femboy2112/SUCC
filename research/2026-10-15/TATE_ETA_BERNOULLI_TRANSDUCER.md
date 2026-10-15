# DYSPON-SPHERE II — THE TRUE 1/24: Tate, Bernoulli heat, Dedekind eta, and two-channel Euler transduction

**Date:** 2026-10-15. **Parent:** DYSPON-SPHERE I draft PR #112 exact head \`82b9f6730833074a778ba88c71bdef2546cc6409\`; transitive APOLLO PR #110, ONE OBJECT PR #106, TATE PR #103, SUCC main @ \`03db44203147a7b28d445bb9f970fa71360e78c4\`. New research branch only; no main merge, release or external RH-repository edit. **RH PROVED: NO. Academic novelty of all classical identities is NOT claimed.**

## The maintainer's hypothesis and the first fatal sign check

The maintainer observed that DYSPON-SPHERE I's positive original Weil form uses the lower bound 1/24 and proposed a connection with half of zeta(-1). The exact sign is

\[
\boxed{\frac1{24}=-\frac12\zeta(-1),\qquad
\zeta(-1)=-\frac{B_2}{2}=-\frac1{12},\quad B_2=\frac16.}
\tag{ETA-00}
\]

The *old inequality threshold* was **not canonical**. Its authentic source computation is the exact rational

\[
M_{\mathrm{DYS}}
= \sum_{j=0}^{15}\frac4{4j+1}-\frac{111}{16}
=\frac{18140507408283703}{386282620694770800}
\approx0.04696174882436.
\tag{ETA-00a}
\]

It strictly dominates BOTH 1/24 and 1/22; the same conservative certificate DOES NOT reach 1/21. Thus **"the Weil positivity constant is 1/24 because of zeta(-1)" is REFUTED as an inference.** This ablation is load-bearing. It does NOT say stronger inequalities are false, only that this existing source bound does not certify them.

Nevertheless 1/24 has an independent, genuinely *canonical* role in the Dedekind eta function. Its survival under Archimedean modular transport is worth exploring as a DIFFERENT arithmetical source map.

## ETA-01. The heat-origin Bernoulli anomaly (CLASSICAL, exact source algebra)

For t>0, take the elementary **additive integer heat spectrum**

\[
H(t)=\sum_{n\ge1}n e^{-nt}
=\frac{e^{-t}}{(1-e^{-t})^2}
=\frac1{4\sinh^2(t/2)}.
\]

Since \(2\sinh(t/2)/t=1+t^2/24+t^4/1920+\cdots\), rational power-series arithmetic proves

\[
\boxed{H(t)=t^{-2}-\frac1{12}+\frac{t^2}{240}+O(t^4).}\tag{ETA-01}
\]

The constant \(-1/12\) agrees with the analytically continued value \(\zeta(-1)\), while \(-\frac12\) times that *renormalized constant* is \(+1/24\). **This does not assert the divergent ordinary sum \(\sum n\) converges to -1/12.** Under Mellin for Re(s)>2, \(H\) has transform \(\Gamma(s)\zeta(s-1)\); the constant is a finite-part/asymptotic datum, not a source-observed infinite arithmetic sum.

**Crucial provenance distinction:** This heat tower is indexed by ALL positive integers and weights n. It is not the original zeta Weil tower of von Mangoldt weights \(\log p/\sqrt{p^k}\). Analogy is not identification.

## ETA-02. Actual modular transport FORCES 1/24 (CLASSICAL modular S theorem + exact uniqueness deduction)

Define for t>0 and rational \(\alpha\) the source family

\[
E_\alpha(t)=e^{-\alpha t}\prod_{n\ge1}(1-e^{-nt}).
\]

The classical Dedekind eta is \(E_{1/24}(t)=\eta(i t/(2\pi))\), with \(q=e^{-t}\). The **imported** modular inversion law is

\[
\boxed{E_{1/24}(t)=\sqrt{2\pi/t}\;E_{1/24}(4\pi^2/t).}\tag{ETA-02a}
\]

Let \(t_\vee=4\pi^2/t\). Then the general \(\alpha\) transport defect is *exactly*

\[
\boxed{\frac{E_\alpha(t)}
{\sqrt{2\pi/t}\,E_\alpha(t_\vee)}
=\exp\bigl[-(\alpha-\tfrac1{24})(t-t_\vee)\bigr].}\tag{ETA-02b}
\]

For every t>0, equality with the canonical modular weight implies \(\alpha=1/24\). This uniqueness is an elementary theorem conditional on the classical eta modular S law; no numerical sample can replace the imported law.

**Probe-gap control:** At the S-fixed t=2π, *every* wrong \(\alpha\) passes the one-point modular test (t=t_vee)! On a transported nonfixed probe t=π or 3π, \(\alpha=1/22\) and \(\alpha=25/24\) fail. The T multiplier under \(\tau\mapsto\tau+1\) determines \(\alpha\) only modulo integers: the wrong \(\alpha=25/24\) passes T yet fails S. These exact symbolic tests prevent a fake normalization win from a fixed-point-only observation.

Also \(\Delta(\tau)=\eta(\tau)^{24}=q\prod_{n\ge1}(1-q^n)^{24}\), an established weight-12 modular cusp form with simple cusp zero. Its q-order \(24\alpha=1\) selects \(\alpha=1/24\) in this q-product family. This is a *different* intrinsic selection mechanism from an arbitrarily weakened positive inequality.

**Interpretation:** True 1/24 is an Archimedean/modular gluing normalization; the older 1/24 was a replaceable certified inequality constant. Their equality alone carries no proof weight.

### ETA-02J. A first derivative at the modular fixed point repairs its value-only probe gap (PROVED EXACT)

The preceding selfdual *value* probe at t=2π accepts every exponent alpha. But the same source-defined S defect has a **first derivative** that can distinguish all alternatives:

\[
L_\alpha(t)=\log\frac{E_\alpha(t)}
{\sqrt{2\pi/t}\,E_\alpha(4\pi^2/t)}
=-(\alpha-\tfrac1{24})(t-4\pi^2/t).
\]
Therefore
\[
\boxed{
L_\alpha(2\pi)=0\quad\forall\alpha,
\qquad
L'_\alpha(2\pi)=-2(\alpha-\tfrac1{24}).
}\tag{ETA-02J}
\]

Thus the **weakest improved local instrument** — one source-indexed derivative at the fixed point rather than another value at the same point — proves canonical alpha iff its defect vanishes. Wrong alpha=1/22 produces the **exact rational** derivative error -1/132; wrong alpha=25/24 produces -2, despite passing the T multiplier and fixed-point S value.

This is a sharp finite observer/probe-gap repair: the missing source distinction lives in a jet rather than the observed value. It is not necessary to scan all modular times once the law's derivative is made available and correctly typed. This is an elementary consequence of ETA-02b, not novel modular theory.

The same fact has a **direct Lambert-source interpretation**. With \(F(t)=\sum\sigma_1(n)e^{-nt}\) as below and \(\partial_t\log E_\alpha=-\alpha+F(t)\), the derivative of the transported S comparison at t=2π is

\[
L_\alpha'(2\pi)=
-2\alpha+2F(2\pi)+\frac1{4\pi}.
\]
Requiring zero first-jet obstruction fixes
\[
\boxed{\alpha=F(2\pi)+\frac1{8\pi}=\frac1{24},}
\]
where the last equality is precisely the independently source-defined classical reciprocity ETA-03SD. This is a **justified source-normalization transducer**, not just a numerical association of 24s. The separate RH-hard Weil-positive operator gate remains untouched.

## ETA-03. Eta logarithmic derivative produces a genuine divisor current (CLASSICAL, exact independent q-polynomial proof)

Set \(q=e^{2\pi i\tau}\), \(\sigma_1(m)=\sum_{d\mid m}d\). Term-by-term differentiating the absolutely convergent eta q-product for |q|<1 gives

\[
\boxed{q\frac d{dq}\log\eta(\tau)
=\frac1{24}-\sum_{n\ge1}\frac{nq^n}{1-q^n}
=\frac1{24}-\sum_{m\ge1}\sigma_1(m)q^m
=\frac{E_2(\tau)}{24}.}\tag{ETA-03}
\]

Here \(E_2=1-24\sum_{m\ge1}\sigma_1(m)q^m\) is the classical *quasimodular* Eisenstein series (not an ordinary weight-2 modular form).

The source program computes the coefficients two independent ways:
1. \(\sigma_1(m)\) by exact divisors;
2. directly multiply \(P_N(q)=\prod_{n=1}^N(1-q^n)\) as an integer polynomial, construct its formal reciprocal, and calculate \(qP_N'/P_N\) to order N. Higher product factors cannot alter coefficients of degree <=N.

In both routes the positive-index source is \(-\sigma_1(m)\); the exponent \(1/24\) appears **only as the degree-zero contact**. Mutating the exponent changes no nonzero Fourier coefficient and is detected by the modular S test, not by a finite q-coefficient test. This is an exact SUCC source/probe distinction.

### Archimedean modular reciprocity for the divisor current

Let \(F(t)=\sum_{m\ge1}\sigma_1(m)e^{-mt}\), t>0. From ETA-03,

\[
\frac d{dt}\log E_{1/24}(t)=-\frac1{24}+F(t).
\]

Differentiate ETA-02a using \(t_\vee'= -4\pi^2/t^2\). The result is

\[
\boxed{
F(t)=\frac1{24}-\frac1{2t}+\frac{\pi^2}{6t^2}
-\frac{4\pi^2}{t^2}F(4\pi^2/t).
}\tag{ETA-03S}
\]

This is a **genuinely source-complete Archimedean transform** with a contact-like 1/24 and explicit homogeneous/inhomogeneous pieces. At the self-dual t=2π it implies the exact nontrivial Lambert-series special value

\[
\boxed{F(2\pi)=\frac1{24}-\frac1{8\pi}.}\tag{ETA-03SD}
\]

ETA-03S/SD are classical consequences of the modular law, not new independent number-theory results. The source checker independently calibrates modular S by high-precision q-products, with analytical authority retained at the level of the cited modular law.

## ETA-04. The substantive bridge: TWO exact prime-power channels from ONE eta divisor source (CLASSICAL Euler + EXACT FORMAL PROBE)

Mellin transform ETA-03's divisor current, initially only in its actual convergence domain Re(s)>2:

\[
\boxed{\int_0^\infty F(t)t^{s-1}\,dt
=\Gamma(s)\sum_{n\ge1}\frac{\sigma_1(n)}{n^s}
=\Gamma(s)\zeta(s)\zeta(s-1).}\tag{ETA-04a}
\]

Proof: absolute convergence and Tonelli allow exchange for real Re(s)>2, then complex holomorphy extends within that half-plane. The arithmetic coefficient identity follows from Dirichlet convolution \(\sigma_1=1*\mathrm{id}\). This is an actual Mellin/Gamma Euler object — but the Archimedean factor is \(\Gamma(s)\), not Tate's \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\) for the ordinary completed zeta. **Do not silently identify them.**

Put \(D(s)=\zeta(s)\zeta(s-1)\). For Re(s)>2,

\[
D(s)=\prod_p\frac{1}{(1-p^{-s})(1-p^{1-s})}.
\]

Its logarithmic derivative reads ACTUAL Euler multiplicativity and contains exactly two authentic prime-power currents:

\[
\boxed{-\frac{D'}{D}(s)
=\sum_{p,k\ge1}(\log p)(1+p^k)p^{-ks}.}\tag{ETA-04b}
\]

The shifted factor has

\[
-\frac{\zeta'(s-1)}{\zeta(s-1)}
=\sum_{p,k\ge1}p^k(\log p)p^{-ks},
\]

and their source-faithful difference is exactly

\[
\boxed{
-\frac{D'}{D}(s)
-\left(-\frac{\zeta'(s-1)}{\zeta(s-1)}\right)
=\sum_{p,k\ge1}(\log p)p^{-ks}
=-\frac{\zeta'}{\zeta}(s).
}\tag{ETA-04c}
\]

**This is the honest Tate × eta arithmetic transducer.** One modular all-integers divisor source generates an Eisenstein two-channel Euler jet; subtracting its *declared* shifted channel recovers precisely the original von Mangoldt prime jet. In source-coordinate notation at \(n=p^k\):

| Prime jet | Parent Eisenstein | Shifted channel | Surviving zeta |
|---|---:|---:|---:|
| coefficient of log p | \(1+n\) | \(n\) | \(1\) |

There are ZERO source coefficients at *primitive composite n=6*; this is a direct consequence of the exact Euler product, not a choice to ignore an inconvenient term. The implementation constructs all coefficients of \(-D'/D\) using **finite exact Dirichlet convolution inversion with a formal log-prime basis**, independently of special-function evaluations. For every n<=N it checks the 1+n, n, 1 arithmetic cancellation, including powers 2,4,8,9,25,49 and all composites. A mutant coefficient \(\sigma_1(6)\mapsto\sigma_1(6)+1\) produces the exact fake-composite source \(\log2+\log3\) at n=6, and FAILS transport rather than being hidden in an observer quotient.

**Why this matters for SUCC:** It exhibits a precise dual-current construction in which an all-integer Lambert/divisor observation can be transported, under its true Euler law, into the SUCC/FUCC prime-power clock source. Both parent currents are true positive-weight prime jets before the subtraction; positivity of a signed Weil quadratic form is a DIFFERENT issue.

The finite-source probe also has a rigorous conservative tail for any integer sigma>=4, N>=2:

\[
\left|\sum_{n>N}\sigma_1(n)n^{-s}\right|
\le \frac{N^{3-\sigma}}{\sigma-3},\qquad\Re s=\sigma,
\tag{ETA-04d}
\]

since \(\sigma_1(n)\le n^2\). This certificate is honest ONLY in the specified right half-plane; it cannot justify termwise Euler convergence in the critical strip.

## ETA-05. The diagram that DOES commute — and the one that DOES NOT (GATE / NO-GO)

**Commutative, on declared analytic domains:**

\[
\begin{array}{ccc}
\eta=q^{1/24}\prod(1-q^n)
&\xrightarrow{\;-\text{nonconstant }q\partial_q\log\;}
&\sigma_1(n)\\
&&\downarrow\text{Mellin + Dirichlet convolution}\\
&& \Gamma(s)D(s),\quad D(s)=\zeta(s)\zeta(s-1)\\
&&\downarrow\text{Euler log derivative, SUBTRACT shifted jet}\\
&&-\zeta'(s)/\zeta(s)\quad(\Re s>2).
\end{array}
\]

The q-Eisenstein current / modular 1/24, Dirichlet Euler two-channel jet and original zeta prime-power jet are now **precisely related**. But a commutative source map is NOT a positive Hilbert Gram by itself.

**NOT yet commutative/positive:**

\[
\text{eta S/T normalization}
\;\dashrightarrow\;
\underbrace{W_\zeta\text{ on the full Tate Schwartz--Bruhat test domain}}_{
\text{needs one }\Gamma_{\mathbb R},\text{ half density, real contact, poles}}
\;\dashrightarrow\;
\underbrace{Q_\zeta(f)\ge0\ \forall f}_{
\text{RH-strength missing sign}}.
\]

The real completed Weil contact in APOLLO is \(C_\infty=-\psi(1/4)+\log\pi\), **not 1/24**. The extra \(\zeta(s-1)\) factor has shifted poles and zero structure that cannot be ignored. Logarithmic differentiation and difference of two positive currents **do not preserve positive-definite kernel order**, and analytical continuation does not repair that. The original genuine-prime-2 *negative* test from DYS-07 remains a decisive control against conflation.

The missing work is an **arithmetic, operator-domain-preserving polarization/transducer** carrying modular-Eisenstein/Tate normalization into the full *signed* Weil form and proving an independent domination estimate. This work provides neither the completed identification nor the domination.

### ETA-05B. Full modular object versus its logarithmic-source shadow: they are NOT the same L-function

The canonical 24th power of eta is the modular discriminant

\[
\Delta(\tau)=\eta(\tau)^{24}
=q\prod_{n\ge1}(1-q^n)^{24}
=\sum_{n\ge1}\tau(n)q^n,
\]

where the Ramanujan tau coefficients begin

\[
\Delta=q-24q^2+252q^3-1472q^4+4830q^5-6048q^6+\cdots.
\]

But taking the **logarithmic derivative** changes the source representation:

\[
\boxed{q\,d\log\Delta/dq=E_2
=1-24\sum_{n\ge1}\sigma_1(n)q^n.}\tag{ETA-05B}
\]

The cusp-form coefficients \(\tau(n)\) are NOT \(\sigma_1(n)\); the Mellin/Euler identity \(\zeta(s)\zeta(s-1)\) belongs to the **Eisenstein logarithmic current**, not to the \(L\)-series of \(\Delta\). This is an exact and important source-typing boundary for SUCC's "complete modular object" moonshot.

Independent arithmetic proof instrument: compute \(\Delta/q\) as an integer polynomial from \(\prod(1-q^n)^{24}\), invert it formally, then compute its logarithmic derivative to all degrees <=N-1. Compare that completely separate route with \(1-24\sigma_1(n)\) from divisors. The test checks both correct identities and expressly **refuses** to identify their coefficient sources.

### ETA-05C. The completed Eisenstein object has TWO critical tracks even IF RH (STRUCTURAL NO-GO)

Let the classical completed Riemann xi function satisfy \(\xi(s)=\xi(1-s)\). The canonical product of our divisor-source factors is

\[
X(s)=\xi(s)\xi(s-1).
\]

It obeys a functional symmetry centered at s=1:

\[
\boxed{X(2-s)=X(s).}\tag{ETA-05C}
\]

**Proof:** \(\xi(2-s)=\xi(s-1)\) and \(\xi(1-s)=\xi(s)\); multiply. This construction reads NO nontrivial-zero locations.

If \(\rho\) denotes *any* nontrivial zero of xi, the zero divisor of X contains both \(\rho\) and \(1+\rho\) (with respective multiplicities). Therefore **even conditional on RH**, the two divisor families lie on the *two* real-part tracks \(1/2\) and \(3/2\), not on the symmetry center Re(s)=1. A functional equation about a center does not force all zeros onto that center, and a product of two completed sources is not a spectral proxy for just one of them.

This is not a disproof of any proposed RH approach; it is an exact NO-GO for the shortcut "the centered completed Eisenstein object already has the original zeta one-line sign." The shift \(s\mapsto s-1\) must be removed (or justified as an independent carrier) **before** transporting a sign to the authentic zeta Weil object. Passing a large finite set of symmetric numerical checks would not fix this algebraic type error.

## ETA-06. Why the number 24 is worth following, but not worshiping

1. **Heat finite part:** \(1/24=-\zeta(-1)/2\), recovered from rational Laurent coefficients of the additive tower (CLASSICAL).
2. **Modular uniqueness:** \(q^{1/24}\) is forced by eta's S law on **all** Archimedean clocks; T alone only fixes the phase modulo an integer (CLASSICAL theorem + elementary new-to-project source probe).
3. **Cusp order:** \(\Delta=\eta^{24}=q\prod(1-q^n)^{24}\) is the canonical weight-12 modular discriminant with simple cusp zero (CLASSICAL).
4. **Arithmetic bridge:** \(\eta\)'s nonconstant logarithmic derivative is \(\sigma_1\); its Mellin/Euler diagram yields TWO prime-power channels, whose exact subtraction reconstructs the original \(\Lambda\) jet (CLASSICAL, with new SUCC formal exact code).
5. **Hard negative:** Original DYS Weil \(\frac1{24}\) was *not* selected by modular S or canonical extremality; \(\frac1{22}\) works by the same original source proof. This coincidence cannot certify RH (REFUTED INTERPRETATION).

**The valuable conceptual lesson:** If 24 is to matter for RH, it must arise by a *forced source transport* preserving the original Tate–Weil operator and its sign, not by noticing an arbitrary lower-bound coefficient.

## ETA-07. Proof debt, adversarial controls and verdict-changing next rounds

- **P1 / transport passport:** Build a complete adelic Schwartz–Bruhat Fourier/Mellin test object with source identified *exactly* to APOLLO DYS-01's actual signed Weil kernel. Recover \(\Gamma_{\mathbb R}(s)\), conductor/parity, both poles, half-density, and the identity contact independently of \(\eta\)'s generic \(\Gamma(s)\). Compare against Connes principal-value trace as independent route.
- **P2 / positivity transducer:** Derive a source-correct *operator-level* analogue of ETA-04c. The two currents have positive scalar coefficients, but their signed difference does not automatically have a positive Weil Gram. Find a noncircular intertwiner or variational Schur bound; test the actual first-prime \(a=1/2\) 30-low/positive-high residual of PRs #107/#109.
- **P3 / true source and mutation:** Inject fake 6, shifted prime factor \(p^{k+1}\), wrong eta q-exponent 1/22, altered Gamma contact, modified half-density, and chi(-3) parity/conductor controls. Demand that precisely the intended gate fails. **Never apply an untwisted divisor E2 source to a primitive character without rederiving the twisted modular law.**
- **P4 / probe-gap:** Eta modular S at t=2π is observationally blind to wrong \(\alpha\). Test an entire basis of nonfixed clocks t/π rational, both T and S, then transport true Dirichlet/Euler sources across analytic half-plane boundaries only with quantified functional-analytic maps.
- **P5 / attempted global proof:** Define an actual dense admissible test family and independently prove \(\langle f,W_\zeta f\rangle\ge0\) on all of it via original signed data. Source equality, numerical agreement, or forced modular exponent without independent positivity is insufficient.

## Exact status / reproducibility

| Item | Verdict |
|---|---|
| Initial \(\tfrac1{24}=\tfrac12\zeta(-1)\) without minus sign | REFUTED |
| DYS original lower margin canonically equals 1/24 | REFUTED (same bound also proves 1/22) |
| Bernoulli heat coefficient and zeta(-1) | CLASSICAL / PROVED exact rational series |
| Eta q^(1/24) forced by modular S | CLASSICAL imported S, DERIVED unique alpha |
| Finite q-product → \(-\sigma_1\) | PROVED exact arithmetic through any audited cutoff |
| Mellin divisor current ↔ \(\Gamma(s)\zeta(s)\zeta(s-1)\) | CLASSICAL on Re(s)>2 |
| Two genuine prime log-derivative channels recovering \(\Lambda\) | CLASSICAL all-n proof; PROVED finite exact coefficient oracle |
| Fake-six mutation | REFUTED a forged Euler source via exact nonzero composite atom |
| Eta ⇒ full Weil kernel positivity ⇒ RH | **UNVERIFIED, RH OPEN** |
| Scholarly originality | UNVERIFIED / not claimed |

**Code** \`observational_succ/tate_eta_bernoulli.py\`. **Tests** \`tests/test_tate_eta_bernoulli.py\`. **Proof receipt** \`scripts/tate_eta_bernoulli_probe.py --verify\` versus \`research/2026-10-15/TATE_ETA_BERNOULLI_RECEIPT.json\`. **CI** \`.github/workflows/tate-eta-bernoulli.yml\`. All claim statuses preserve original-source certification separately from classical imported theorems.

**Primary references:** NIST DLMF [25.6.3](https://dlmf.nist.gov/25.6.E3) (negative zeta values/Bernoulli), [27.14.12](https://dlmf.nist.gov/27.14.E12) and [23.17.8](https://dlmf.nist.gov/23.17.E8) (eta product), [23.18.5](https://dlmf.nist.gov/23.18.E5) (modular transformation); Masatoshi Suzuki, [arXiv:2606.09096v3](https://arxiv.org/abs/2606.09096), signed Weil/Suzuki source, not assumed RH. E2 logarithmic derivative and eta^24 discriminant are classical, see e.g. A Planar Cubic Derived from the Logarithm of the Dedekind Eta Function (2021) and standard modular forms references.

**BOTTOM LINE: THE ORIGINAL 1/24 WAS ACCIDENTAL. THE MODULAR 1/24 IS CANONICAL. THE EXACT TWO-PRIME-JET SOURCE TRANSDUCER IS REAL. THE POSITIVITY-PRESERVING TATE→WEIL LAMP IS STILL MISSING. RH PROVED: NO.**
