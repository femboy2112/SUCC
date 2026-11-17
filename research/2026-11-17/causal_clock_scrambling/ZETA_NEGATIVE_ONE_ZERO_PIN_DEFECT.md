# The −1 Completion Bridge: BBP Null Seed, Hadamard Zeros, and a Critical-Line Pinning Defect

**SUCC / Principia / π normality + RH interface** — 2026-11-17  
**Originating hypothesis (Leah):** the exact Euler-shaped product of the original zero-seeded BBP computation, when corrected by zeta's prime/Gamma completion, should reveal hidden structure near the RH critical zeros. Perhaps the “critical-line irrational” becomes π after paying a zero/observer bookkeeping defect.

**Verdict:** ZPD-01–04 are **CLASSICAL / PROVED PAPER** formulas and an exact **RH-EQUIVALENT REFORMULATION**, respectively. ZPD-05–06 are scope/no-go results. **No proof of RH, R0, base-16 π normality, or a causal equivalence of BBP clock factors and genuine-prime Euler factors is claimed.** The novel SUCC component is the typed *comparison* of several previously established objects, not priority over Hadamard's factorization or the classical completion identities.

## 1. The source-null BBP jet, exactly as previously proved

Retain the original signed forcing and literal null input
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
For an explicit changed-seed probe \(s\), with original forcing fixed, \(U_N(s)=16^N(s+P_N)\), \(P_N=\sum_{j\le N}16^{-j}r(j)\), and \(P_N\to x=\pi/16\).

The exact Euler-shaped chronological product from [NBC](NULL_BOUNDARY_EULER_COCYCLE.md) is
\[
G_N(s)=\prod_{n=0}^{N-1}\left(1-\frac{r(n+1)}{U_{n+1}(s)}\right)
=\frac{s}{s+P_N},\quad
G_\infty(s)=\frac{s}{s+\pi/16}.
\]
This is source-defined for the stated denominator domains; it is NOT an Euler product over primes. The authentic \(s=0\) gives a **zero value** but nonzero source jet
\[
\boxed{\mathcal J_{\rm BBP}=G_\infty'(0)=16/\pi.}\tag{ZPD1}
\]
All higher derivatives are powers of this one source endpoint, not independent new spectral data.

## 2. Genuine prime completion at s=−1 and the exact Γ bridge

Use the *different* complex zeta variable \(w\) to avoid confusing it with the BBP seed \(s\). Fix a finite inventory \(Q\) of **genuine rational primes**. As in SUCC [Prime Compensation #661](https://github.com/femboy2112/SUCC/pull/661), put
\[
E_Q(w)=\prod_{p\mid Q}(1-p^{-w})^{-1},
\quad
R_Q(w)=\zeta(w)\prod_{p\mid Q}(1-p^{-w}).
\]
The second coordinate is the **analytically continued** finite coprime/Hurwitz complement; the divergent full prime product at \(w=-1\) must never be inserted as if convergent.

At \(w=-1\),
\[
\boxed{E_Q(-1)R_Q(-1)=\zeta(-1)=-1/12.}\tag{ZPD2}
\]
The Euler register can move when a genuine prime is inserted; the complementary register compensates so their product does not.

Define the classical completed Riemann function
\[
\xi(w)=\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w).
\]
The exact Γ specialization at \(w=-1\), using \(\Gamma(-1/2)=-2\sqrt\pi\), is
\[
\boxed{
\xi(-1)=-2\pi\,\zeta(-1)=\pi/6.
}\tag{ZPD3}
\]

**ZPD-01 (EXACT three-source scalar normalization):**
\[
\boxed{
\mathcal J_{\rm BBP}\,\xi(-1)
=\frac{16}{\pi}\frac{\pi}{6}
=\frac83=-32\,E_Q(-1)R_Q(-1).
}\tag{ZPD4}
\]
This equality holds for every genuine finite prime inventory Q with properly continued R_Q. It is an exact **one-point normalization**, *not* a source-authenticated map from BBP time n to prime p, nor an RH-zero location theorem. The common π value is already built into the known BBP completion and the ξ functional equation.

## 3. The complete nontrivial zero product really encodes the BBP seed jet

Let \(\rho\) range over **all nontrivial zeros of \(\zeta\)** with \(\Im\rho>0\), counted with multiplicity, with the standard symmetry pairing \(\rho\leftrightarrow1-\rho\). The completed \(\xi\) is entire and symmetric, and Hadamard's paired factorization is
\[
\boxed{
\xi(w)=\frac12\prod_{\Im\rho>0}
\left(1-\frac{w(1-w)}{\rho(1-\rho)}\right).
}\tag{ZPD5}
\]
The product over upper-half zeros is locally normally convergent: individual factors differ from one by \(O_w(|\rho|^{-2})\), summable using standard zero counting. No **RH assumption** is used; off-critical-line zeros remain in the product.

Set \(w=-1\). From (ZPD3–5),
\[
\boxed{
\prod_{\Im\rho>0}\left(1+\frac2{\rho(1-\rho)}\right)
=\frac{\pi}{3},
}\tag{ZPD6}
\]
hence
\[
\boxed{
\mathcal J_{\rm BBP}=\frac{16}{3}
\prod_{\Im\rho>0}\left(1+\frac2{\rho(1-\rho)}\right)^{-1}.
}\tag{ZPD7}
\]

**ZPD-02 (EXACT zero-set representation):** the entire zero set of ξ determines the completed scalar that also appears in the original BBP null jet. This is an *existing Hadamard encoding combined with two special-value identities*, not evidence that the BBP recurrence determines the real parts of the zeros. A scalar equality at one fixed argument cannot distinguish RH-true from RH-false possible zero configurations with the same completed ξ value.

## 4. Critical-line projection and the genuine nonnegative bookkeeping defect

Write any upper-half nontrivial zero as
\(\rho=\beta+i\gamma\), \(0<\beta<1,\gamma>0\), and define
\[
t=\gamma^2+\tfrac14,\qquad d=(\beta-\tfrac12)^2.
\]
All actual nontrivial zeta-zero positive heights exceed \(14\), a rigorously established first-zero fact; in particular \(\gamma>\frac12\). This is needed for the factorwise inequality.

For each upper-half zero define its **critical-line projected factor** by retaining its *actual height* \(\gamma\) and pinning \(\beta\mapsto1/2\):
\[
L_\rho=1+\frac2{t}>1,\qquad
F_\rho=1+\frac2{\rho(1-\rho)}.
\]
By direct complex algebra,
\[
\boxed{
|F_\rho|^2
=1+\frac{4(t+1-d)}
{t^2+(2\gamma^2-\tfrac12)d+d^2}.
}\tag{ZPD8}
\]
Because \(d\in[0,1/4)\), \(\gamma>1/2\), the numerator is ≤\(t+1\) and the denominator ≥\(t^2\), with both inequalities strict if \(d>0\). Therefore
\[
\boxed{|F_\rho|\le L_\rho,\quad |F_\rho|=L_\rho
\iff\beta=1/2.}\tag{ZPD9}
\]

Define the positive **critical-line pinning scalar**
\[
\boxed{
\Pi_{\rm pin}:=
3\prod_{\Im\rho>0}
\left(1+\frac2{\gamma_\rho^2+1/4}\right).
}\tag{ZPD10}
\]
This number is defined **without assuming RH**, but the construction presupposes the complete upper-half zero-ordinate multiset. Its irrationality is not known merely from the definition. If RH is true, it equals π; if RH is false, it is strictly larger than π.

The *exact* nonnegative squared-gain defect can be written without logarithms:
\[
\boxed{
L_\rho^2-|F_\rho|^2
=\frac{4d\,\left[3t^2+t-1+(t+1)d\right]}
{t^2\left[t^2+(2t-1)d+d^2\right]}\ge0.
}\tag{ZPD9a}
\]
For actual zero heights \(\gamma>14\), \(t>\frac12\) makes each bracket strictly positive whenever \(d>0\). This displays the **squared horizontal displacement** as an explicit factor rather than hiding it inside an inequality. It is a formal zero-geometry statement, not a measured real-zero displacement.

**ZPD-03 (EXACT RH-EQUIVALENT NONNEGATIVE DEFECT):**
\[
\boxed{
\Pi_{\rm pin}\ge\pi,\quad
\Delta_{\rm RH}:=\log(\Pi_{\rm pin}/\pi)
=\sum_{\Im\rho>0}\log\frac{L_\rho}{|F_\rho|}
\ge0,
}\tag{ZPD11}
\]
\[
\boxed{\Delta_{\rm RH}=0\iff
\Re\rho=\tfrac12\text{ for every nontrivial zero }\rho
\iff\mathrm{RH}.}\tag{ZPD12}
\]

**Proof.** By (ZPD6), the absolutely convergent actual product has modulus
\(\prod_{\Im\rho>0}|F_\rho|=\pi/3\). Each ratio \(L_\rho/|F_\rho|\ge1\) by (ZPD9). The nonnegative sum of logarithms vanishes exactly if all summands vanish. Equality holds termwise precisely for zero real part \(\beta=1/2\). Local normal convergence follows from \(\sum_\rho|\rho|^{-2}<\infty\). \(\square\)

This is a **reformulation of RH** in a positive measurable-looking product difference. It is not a proof that the defect vanishes and does not construct an independent source observer of the entire spectrum. A finite list of currently verified critical-line zeros yields zero *for those terms* and says nothing about the unverified remainder.

### ZPD-04 — the first visible off-line defect is quadratic

At *fixed height* \(\gamma\), expand the per-zero logarithmic defect near the line:
\[
\boxed{
\log\frac{L_\rho}{|F_\rho|}
=\frac{2(3t^2+t-1)}{t^2(t+2)^2}
(\beta-\tfrac12)^2
+O_\gamma((\beta-\tfrac12)^4).
}\tag{ZPD13}
\]
The coefficient is **strictly positive for all actual zeta zero heights**. At large \(\gamma\) it is \(6\gamma^{-4}+O(\gamma^{-6})\). Thus an off-line horizontal displacement has a *zero first derivative* but a *positive second-order* effect, increasingly hard to resolve at high heights.

This is the exact shape of the proposed first-order-null/higher-order-visible observer mechanism, but mathematically it is simply an even analytic expansion around the symmetric critical line. Moving a zero horizontally while holding its height fixed is a **formal comparison**, not a legal deformation of ζ without separately constructing a new entire function.

## 5. The critical no-go for π normality and RH

**ZPD-05 (REFUTED INFERENCE):** the equality of the BBP seed jet with a completed ξ special value is a *single scalar equality*. It can be obtained from the classical BBP π endpoint and ζ(-1) value without knowing RH or any digit-frequency theorem. Because both sides of (ZPD4–7) are already true **regardless of RH**, no logical deduction of RH follows from them. Likewise the spectral pinning defect only **rephrases** the unproved assertion that all zeros lie on the line; it does not demonstrate \(\Delta_{\rm RH}=0\).

**ZPD-06 (typed completion gap):** for genuine prime sets the factor \(1-p\) at \(w=-1\) is nonzero. The BBP chronological product has a literal zero at its first original-seed factor. The common language of **complementary source registers, multiplicative cocycles, observer-normalized zeros and Γ completion** is valid, but no direct map preserving both original four-pole source chronology and genuine-prime factor ancestry has been constructed. The BBP terminal shell norm and the zero pinning defect have unrelated indices and quantifiers.

A "critical-line irrational" in this dossier can be *defined* as the positive real \(\Pi_{\rm pin}\). It is equal to π **if and only if RH**; it is **not** justified to call it an unconditional irrational number, a null-information object or the source of π's digits. The completed \(\xi\) has exact analytic zeros whose germs have higher-order structure; that is distinct from the null seed's first-jet response.

## 6. Verdict-changing next probe, with source passports

A genuine proof bridge would require a new **family** of BBP-source-derived analytic responses \(J(w)\), with a declared map from the original zero-seeded 4-pole/carry history to ξ's zero-dependent logarithmic derivative or to the global zero-pinning defect. For example one would need to derive, rather than posit, an inequality of the form
\[
\Delta_{\rm RH}\le \liminf_{B\to\infty}\mathcal E_B^{\rm BBP}
\quad\text{or}\quad
\liminf_{B\to\infty}R_B(0)\ge\mathcal F(\Delta_{\rm RH}),
\]
with rigorous source maps, correct dimensions and controls. A bound of this shape alone would not force either conjecture without an independently established strict sign or equality.

**Mandatory controls:** same four-pole forcing with tuned locked seed; positive decreasing null-seeded matched locked alternative with nonzero weighted shift residue; finite prime-inventory orientation corruption; hypothetical off-critical-line zeros and the formal height-preserving pin; phase-averaged or Gamma-only scalar source observer; sparse badly approximable κ16. A user-visible analogy or one-point π normalizer is not a source-derived cross-window theorem.

**Claim ledger:**
- ZPD-01/02: **PROVED / CLASSICAL** ξ(-1), finite-prime complementary compensation, paired Hadamard factorization and the exact BBP jet–ξ(-1) scalar bridge.
- ZPD-03/04: **PROVED RH-EQUIVALENT REFORMULATION** and an exact positive quadratic formal off-line defect, **not a proof of RH**.
- ZPD-05/06: **REFUTED shortcut**, **OPEN new arithmetic/spectral transport**.
- Original \(\liminf_B R_B(0)>0\), R0, **π base-16 normality**, RH: **OPEN**.

**Primary/classical references:** NIST DLMF [zeta functional equation](https://dlmf.nist.gov/25.4), [zeta zeros](https://dlmf.nist.gov/25.10); [Encyclopedia of Mathematics ξ](https://encyclopediaofmath.org/wiki/Riemann_xi-function); [paired Hadamard product and normalization](https://vdeangel.xula.edu/Notes/PNT.html); [certified first-zero range / zero count](https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html); [Clay Riemann hypothesis status](https://www.claymath.org/millennium/Riemann-Hypothesis/); [PCE #661](https://github.com/femboy2112/SUCC/pull/661); [NBC](NULL_BOUNDARY_EULER_COCYCLE.md), [IMF](BBP_IMPULSE_MELLIN_FILTER.md), [original terminal endpoint norm](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md).

**Focused exact tests:** [tests/test_zeta_minus_one_zero_pin_defect.py](../../../tests/test_zeta_minus_one_zero_pin_defect.py) and [execution receipt](ZETA_NEGATIVE_ONE_ZERO_PIN_VALIDATION.md). Synthetic zeros in finite tests are controls and are not represented as actual off-critical-line ζ zeros.
